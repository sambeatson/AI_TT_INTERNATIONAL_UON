# Teleprompter for Windows - no installation needed (uses the PowerShell and .NET that ship with Windows).
# Start it with Teleprompter.bat. Same controls and script format as teleprompter.py:
#   Drag anywhere = move  |  Click = next  |  Right-click = back  |  Drag the corner mark = resize
#   Space / Right / Down / PgDn = next  |  Left / Up / PgUp = back  |  Home = start
#   + / - or mouse wheel = text size  |  T = transparency  |  R = reload script  |  H = help  |  Esc / Q = quit
param([string]$ScriptPath)

$ErrorActionPreference = 'Stop'
Add-Type -AssemblyName System.Windows.Forms
Add-Type -AssemblyName System.Drawing
[System.Windows.Forms.Application]::EnableVisualStyles()
try {   # crisp text on high-DPI (laptop) screens instead of a blurry stretched window
    Add-Type -Namespace TeleprompterNative -Name Dpi -MemberDefinition '[System.Runtime.InteropServices.DllImport("user32.dll")] public static extern bool SetProcessDPIAware();'
    [void][TeleprompterNative.Dpi]::SetProcessDPIAware()
} catch { }

try {
    $Here = Split-Path -Parent $MyInvocation.MyCommand.Path
    if (-not $ScriptPath) { $ScriptPath = Join-Path $Here 'teleprompter_script.txt' }
    $SettingsPath = Join-Path $Here 'teleprompter_settings_ps.json'

    $Navy  = [System.Drawing.Color]::FromArgb(16, 38, 59)     # Nottingham Blue
    $Pale  = [System.Drawing.Color]::FromArgb(159, 195, 224)
    $White = [System.Drawing.Color]::White
    $Alphas = @(0.92, 0.75, 1.0)
    $HelpText = 'Click: next   Right-click: back   Drag: move   Corner: resize   +/- or wheel: size   T: transparency   R: reload   Esc: quit'
    $Keys = [System.Windows.Forms.Keys]
    $Measure = [System.Windows.Forms.TextFormatFlags]::WordBreak

    # all mutable state lives in one hashtable (PowerShell variable names are not case-sensitive)
    $State = @{ i = 0; size = 30; alpha_i = 0; x = 120; y = 120; w = 760; h = 320; help = $true
                moved = $false; start = $null; gstart = $null; segs = $null }

    if (Test-Path -LiteralPath $SettingsPath) {
        try {
            $cfg = Get-Content -LiteralPath $SettingsPath -Raw | ConvertFrom-Json
            foreach ($k in 'size', 'alpha_i', 'x', 'y', 'w', 'h') {
                if ($null -ne $cfg.$k) { $State[$k] = [int]$cfg.$k }
            }
        } catch { }
    }
    $onScreen = $false
    foreach ($scr in [System.Windows.Forms.Screen]::AllScreens) {
        if ($scr.WorkingArea.Contains($State.x + 20, $State.y + 20)) { $onScreen = $true }
    }
    if (-not $onScreen) { $State.x = 120; $State.y = 120 }

    function Load-Segments {
        $list = New-Object System.Collections.ArrayList
        if (-not (Test-Path -LiteralPath $ScriptPath)) {
            [void]$list.Add(@{ cue = ''; show = ''; text = "Could not find the script file:`n$ScriptPath" })
            return ,$list
        }
        $raw = [System.IO.File]::ReadAllText($ScriptPath, [System.Text.Encoding]::UTF8)
        foreach ($part in [regex]::Split($raw, '(?m)^\s*---\s*$')) {
            $cue = ''; $show = ''; $lines = New-Object System.Collections.ArrayList
            foreach ($line in ($part.Trim() -split "`r?`n")) {
                $ln = $line.Trim()
                if ($ln.StartsWith('#') -or ($ln -eq '' -and $lines.Count -eq 0)) { continue }
                if ($cue -eq '' -and $lines.Count -eq 0 -and $ln.StartsWith('[') -and $ln.EndsWith(']')) {
                    $cue = $ln.Substring(1, $ln.Length - 2)
                } elseif ($ln -match '^(?i)show:') {
                    $show = $ln.Substring(5).Trim()
                } else {
                    [void]$lines.Add($ln)
                }
            }
            $text = ($lines -join "`n").Trim()
            $text = [regex]::Replace($text, '(?<!\n)\n(?!\n)', ' ')     # rejoin lines wrapped inside a paragraph
            if ($text -or $cue -or $show) { [void]$list.Add(@{ cue = $cue; show = $show; text = $text }) }
        }
        if ($list.Count -eq 0) { [void]$list.Add(@{ cue = ''; show = ''; text = '(The script file is empty.)' }) }
        return ,$list
    }

    # ---- window ------------------------------------------------------------------------------------
    $form = New-Object System.Windows.Forms.Form
    $form.Text = 'Teleprompter'
    $form.FormBorderStyle = [System.Windows.Forms.FormBorderStyle]::None
    $form.TopMost = $true
    $form.ShowInTaskbar = $true
    $form.BackColor = $Navy
    $form.StartPosition = [System.Windows.Forms.FormStartPosition]::Manual
    $form.Location = New-Object System.Drawing.Point($State.x, $State.y)
    $form.Size = New-Object System.Drawing.Size($State.w, $State.h)
    $form.MinimumSize = New-Object System.Drawing.Size(260, 120)
    $form.KeyPreview = $true
    $form.Padding = New-Object System.Windows.Forms.Padding(14, 8, 14, 8)
    $form.Opacity = $Alphas[$State.alpha_i % $Alphas.Count]

    $body = New-Object System.Windows.Forms.Label
    $body.Dock = [System.Windows.Forms.DockStyle]::Fill
    $body.AutoSize = $false
    $body.UseCompatibleTextRendering = $false
    $body.ForeColor = $White
    $body.BackColor = $Navy
    $body.TextAlign = [System.Drawing.ContentAlignment]::TopLeft
    $body.Font = New-Object System.Drawing.Font('Segoe UI', [single]$State.size)

    $top = New-Object System.Windows.Forms.Label
    $top.Dock = [System.Windows.Forms.DockStyle]::Top
    $top.Height = 26
    $top.UseCompatibleTextRendering = $false
    $top.ForeColor = $Pale
    $top.BackColor = $Navy
    $top.Font = New-Object System.Drawing.Font('Segoe UI', [single]10)

    $bottom = New-Object System.Windows.Forms.Label
    $bottom.Dock = [System.Windows.Forms.DockStyle]::Bottom
    $bottom.AutoSize = $false
    $bottom.UseCompatibleTextRendering = $false
    $bottom.ForeColor = $Pale
    $bottom.BackColor = $Navy
    $bottom.Font = New-Object System.Drawing.Font('Segoe UI', [single]9.5)

    $grip = New-Object System.Windows.Forms.Label
    $grip.Text = [string][char]0x25E2
    $grip.ForeColor = $Pale
    $grip.BackColor = $Navy
    $grip.Font = New-Object System.Drawing.Font('Segoe UI', [single]11)
    $grip.Size = New-Object System.Drawing.Size(20, 20)
    $grip.Cursor = [System.Windows.Forms.Cursors]::SizeNWSE
    $grip.Anchor = [System.Windows.Forms.AnchorStyles]'Bottom, Right'
    $grip.Location = New-Object System.Drawing.Point(($form.ClientSize.Width - 20), ($form.ClientSize.Height - 20))

    $form.Controls.Add($body)
    $form.Controls.Add($top)
    $form.Controls.Add($bottom)
    $form.Controls.Add($grip)
    $grip.BringToFront()

    # ---- behaviour ---------------------------------------------------------------------------------
    function Fit-Text {
        $w = [Math]::Max(200, $body.ClientSize.Width)
        $avail = $body.ClientSize.Height
        $size = $State.size
        while ($true) {
            $f = New-Object System.Drawing.Font('Segoe UI', [single]$size)
            $h = [System.Windows.Forms.TextRenderer]::MeasureText($body.Text, $f, (New-Object System.Drawing.Size($w, [int]::MaxValue)), $Measure).Height
            if ($h -le $avail -or $size -le 12) { break }
            $f.Dispose()
            $size -= 2
        }
        $old = $body.Font
        $body.Font = $f
        if ($old) { $old.Dispose() }
    }

    function Render {
        $seg = $State.segs[$State.i]
        $top.Text = ('{0}    {1} / {2}' -f $seg.cue, ($State.i + 1), $State.segs.Count).Trim()
        $b = ''
        if ($seg.show) { $b = 'SHOW: ' + $seg.show }
        if ($State.help) { if ($b) { $b += "`n" }; $b += $HelpText }
        $bottom.Text = $b
        $w = [Math]::Max(200, $form.ClientSize.Width - 28)
        if ($b) {
            $bottom.Height = [System.Windows.Forms.TextRenderer]::MeasureText($b, $bottom.Font, (New-Object System.Drawing.Size($w, [int]::MaxValue)), $Measure).Height + 6
        } else {
            $bottom.Height = 4
        }
        $body.Text = $seg.text
        $form.PerformLayout()
        Fit-Text
    }

    function Go-To([int]$n) {
        $State.i = [Math]::Max(0, [Math]::Min($State.segs.Count - 1, $n))
        if ($State.i -gt 0) { $State.help = $false }
        Render
    }

    function Save-Settings {
        try {
            @{ size = $State.size; alpha_i = $State.alpha_i; x = $form.Location.X; y = $form.Location.Y
               w = $form.Size.Width; h = $form.Size.Height } | ConvertTo-Json | Set-Content -LiteralPath $SettingsPath -Encoding UTF8
        } catch { }
    }

    function Set-TextSize([int]$d) {
        $State.size = [Math]::Max(10, [Math]::Min(96, $State.size + $d))
        Render
        Save-Settings
    }

    $State.segs = Load-Segments

    # mouse: drag to move, click to advance
    $onDown = {
        param($sender, $e)
        $State.start = @([System.Windows.Forms.Cursor]::Position, $form.Location)
        $State.moved = $false
    }
    $onMove = {
        param($sender, $e)
        if ($e.Button -ne [System.Windows.Forms.MouseButtons]::Left -or $null -eq $State.start) { return }
        $p0 = $State.start[0]; $l0 = $State.start[1]; $p = [System.Windows.Forms.Cursor]::Position
        $dx = $p.X - $p0.X; $dy = $p.Y - $p0.Y
        if ([Math]::Abs($dx) -gt 6 -or [Math]::Abs($dy) -gt 6) { $State.moved = $true }
        if ($State.moved) { $form.Location = New-Object System.Drawing.Point(($l0.X + $dx), ($l0.Y + $dy)) }
    }
    $onUp = {
        param($sender, $e)
        if ($e.Button -eq [System.Windows.Forms.MouseButtons]::Right) { Go-To ($State.i - 1) }
        elseif ($e.Button -eq [System.Windows.Forms.MouseButtons]::Left) {
            if ($State.moved) { Save-Settings } else { Go-To ($State.i + 1) }
        }
        $State.start = $null
    }
    foreach ($c in @($form, $body, $top, $bottom)) {
        $c.Add_MouseDown($onDown)
        $c.Add_MouseMove($onMove)
        $c.Add_MouseUp($onUp)
    }

    # corner grip: resize
    $grip.Add_MouseDown({ param($sender, $e) $State.gstart = @([System.Windows.Forms.Cursor]::Position, $form.Size) })
    $grip.Add_MouseMove({
        param($sender, $e)
        if ($e.Button -ne [System.Windows.Forms.MouseButtons]::Left -or $null -eq $State.gstart) { return }
        $p = [System.Windows.Forms.Cursor]::Position
        $w = [Math]::Max(260, $State.gstart[1].Width + $p.X - $State.gstart[0].X)
        $h = [Math]::Max(120, $State.gstart[1].Height + $p.Y - $State.gstart[0].Y)
        $form.Size = New-Object System.Drawing.Size($w, $h)
    })
    $grip.Add_MouseUp({ param($sender, $e) $State.gstart = $null; Save-Settings })

    $form.Add_MouseWheel({ param($sender, $e) if ($e.Delta -gt 0) { Set-TextSize 2 } else { Set-TextSize -2 } })

    $form.Add_KeyDown({
        param($sender, $e)
        $k = $e.KeyCode
        if ($k -eq $Keys::Space -or $k -eq $Keys::Right -or $k -eq $Keys::Down -or $k -eq $Keys::PageDown) { Go-To ($State.i + 1) }
        elseif ($k -eq $Keys::Left -or $k -eq $Keys::Up -or $k -eq $Keys::PageUp) { Go-To ($State.i - 1) }
        elseif ($k -eq $Keys::Home) { Go-To 0 }
        elseif ($k -eq $Keys::Oemplus -or $k -eq $Keys::Add) { Set-TextSize 2 }
        elseif ($k -eq $Keys::OemMinus -or $k -eq $Keys::Subtract) { Set-TextSize -2 }
        elseif ($k -eq $Keys::T) {
            $State.alpha_i = ($State.alpha_i + 1) % $Alphas.Count
            $form.Opacity = $Alphas[$State.alpha_i]
            Save-Settings
        }
        elseif ($k -eq $Keys::R) { $State.segs = Load-Segments; Go-To $State.i }
        elseif ($k -eq $Keys::H) { $State.help = -not $State.help; Render }
        elseif ($k -eq $Keys::Escape -or $k -eq $Keys::Q) { $form.Close() }
        else { return }
        $e.Handled = $true
        $e.SuppressKeyPress = $true
    })

    $form.Add_Resize({ if ($State.segs) { Render } })
    $form.Add_Shown({ Render; $form.Activate() })
    $form.Add_FormClosing({ Save-Settings })

    [void]$form.ShowDialog()
}
catch {
    [System.Windows.Forms.MessageBox]::Show("Teleprompter error:`n`n$($_.Exception.Message)`n`nLine $($_.InvocationInfo.ScriptLineNumber)", 'Teleprompter') | Out-Null
}
