# Teleprompter

A small window that stays on top of everything (including OBS). Put it close to your camera lens.

**Start:** double-click `Teleprompter.bat`. It needs Python 3 (python.org; tick "Add python.exe to
PATH" when installing). Nothing else needs installing. To read a different script, drag its `.txt`
file onto `Teleprompter.bat`.

| Action | Mouse | Keys |
|---|---|---|
| Next section | click | Space, →, ↓, Page Down |
| Previous section | right-click | ←, ↑, Page Up |
| Move the window | drag anywhere | |
| Resize the window | drag the ◢ corner | |
| Text size | mouse wheel | + / − |
| Transparency | | T |
| Reload the script after editing | | R |
| Show / hide help | | H |
| Back to the start | | Home |
| Quit | | Esc or Q |

Long sections shrink automatically to fit the window. Make the window bigger, or press +, to read
larger. Position, size, text size and transparency are remembered between runs
(`teleprompter_settings.json`).

**Editing the script** (`teleprompter_script.txt`, any text editor):

- Sections are separated by a line containing only `---`.
- An optional first line in square brackets is a time cue, shown small at the top.
- A line starting `Show:` is a reminder of what should be on screen, shown small at the bottom.
- Lines starting with `#` are ignored.
- A blank line starts a new paragraph.

**Tip for OBS:** the teleprompter is a separate window. Use a camera and image sources, not a display
capture of the whole screen, so it never appears in the recording.
