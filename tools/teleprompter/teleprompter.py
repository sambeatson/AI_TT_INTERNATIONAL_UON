"""Teleprompter: a small borderless window that stays on top of everything.

    Drag anywhere ........ move the window
    Click ................ next section          Right-click ....... previous section
    Space / Right / PgDn . next                  Left / PgUp ....... previous
    + / - or mouse wheel . text size             Home .............. back to the start
    T .................... cycle transparency    R ................. reload the script file
    H .................... show/hide this help   Esc / Q ........... quit
    Drag the corner mark (bottom right) to resize.

The script is a plain text file (teleprompter_script.txt next to this file, or a path given on the
command line). Sections are separated by a line containing only ---. In each section:
    [0:15-0:30]        optional first line in square brackets: a time cue, shown small at the top
    Show: ...          optional line: what should be on screen, shown small at the bottom
    # ...              comment, ignored
    anything else      the words to say (a blank line starts a new paragraph)

Window position, size, text size and transparency are remembered in teleprompter_settings.json.
"""
import json
import os
import re
import sys
import tkinter as tk

HERE = os.path.dirname(os.path.abspath(__file__))
SCRIPT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, 'teleprompter_script.txt')
SETTINGS = os.path.join(HERE, 'teleprompter_settings.json')

NAVY, WHITE, PALE = '#10263B', '#FFFFFF', '#9FC3E0'   # Nottingham Blue background
DRAG_THRESHOLD = 6                                     # pixels: less than this counts as a click
ALPHAS = (0.92, 0.75, 1.0)
HELP = ('Click: next   Right-click: back   Drag: move   Corner: resize   '
        '+/- or wheel: size   T: transparency   R: reload   Esc: quit')


def load_segments(path):
    with open(path, encoding='utf-8-sig') as f:
        raw = f.read()
    segments = []
    for part in re.split(r'^\s*---\s*$', raw, flags=re.M):
        cue, show, body = '', '', []
        for line in part.strip().splitlines():
            s = line.strip()
            if s.startswith('#') or (not s and not body):
                continue
            if not cue and not body and s.startswith('[') and s.endswith(']'):
                cue = s[1:-1]
            elif s.lower().startswith('show:'):
                show = s[5:].strip()
            else:
                body.append(s)
        text = '\n'.join(body).strip()
        text = re.sub(r'(?<!\n)\n(?!\n)', ' ', text)       # rejoin lines wrapped inside a paragraph
        if text or cue or show:
            segments.append(dict(cue=cue, show=show, text=text))
    return segments or [dict(cue='', show='', text='(The script file is empty.)')]


class Teleprompter:
    def __init__(self):
        self.cfg = dict(geometry='760x320+120+120', size=30, alpha_i=0)
        try:
            with open(SETTINGS, encoding='utf-8') as f:
                self.cfg.update(json.load(f))
        except (OSError, ValueError):
            pass
        self.segments = self._load()
        self.i = 0
        self.show_help = True
        self._fit_job = None

        r = self.root = tk.Tk()
        r.title('Teleprompter')
        r.overrideredirect(True)                         # no title bar or border
        r.attributes('-topmost', True)
        r.attributes('-alpha', ALPHAS[self.cfg['alpha_i'] % len(ALPHAS)])
        r.configure(bg=NAVY)
        r.geometry(self.cfg['geometry'])

        self.top = tk.Label(r, bg=NAVY, fg=PALE, anchor='w', font=('Segoe UI', 11))
        self.top.pack(fill='x', padx=14, pady=(8, 0))
        self.body = tk.Label(r, bg=NAVY, fg=WHITE, justify='left', anchor='nw')
        self.body.pack(fill='both', expand=True, padx=14, pady=6)
        self.bottom = tk.Label(r, bg=NAVY, fg=PALE, anchor='w', justify='left', font=('Segoe UI', 10))
        self.bottom.pack(fill='x', padx=14, pady=(0, 8))
        self.grip = tk.Label(r, text='◢', bg=NAVY, fg=PALE, cursor='bottom_right_corner', font=('Segoe UI', 12))
        self.grip.place(relx=1.0, rely=1.0, anchor='se')

        for w in (r, self.top, self.body, self.bottom):
            w.bind('<ButtonPress-1>', self._press)
            w.bind('<B1-Motion>', self._drag)
            w.bind('<ButtonRelease-1>', self._release)
            w.bind('<ButtonRelease-3>', lambda e: self.step(-1))
            w.bind('<MouseWheel>', self._wheel)                       # Windows / macOS
            w.bind('<Button-4>', lambda e: self.resize_text(+2))      # Linux wheel up
            w.bind('<Button-5>', lambda e: self.resize_text(-2))      # Linux wheel down
        self.grip.bind('<ButtonPress-1>', self._grip_press)
        self.grip.bind('<B1-Motion>', self._grip_drag)
        self.grip.bind('<ButtonRelease-1>', lambda e: self._save())

        keys = {'<space>': lambda e: self.step(1), '<Right>': lambda e: self.step(1),
                '<Next>': lambda e: self.step(1), '<Down>': lambda e: self.step(1),
                '<Left>': lambda e: self.step(-1), '<Prior>': lambda e: self.step(-1),
                '<Up>': lambda e: self.step(-1), '<Home>': lambda e: self.goto(0),
                '<plus>': lambda e: self.resize_text(+2), '<equal>': lambda e: self.resize_text(+2),
                '<KP_Add>': lambda e: self.resize_text(+2), '<minus>': lambda e: self.resize_text(-2),
                '<KP_Subtract>': lambda e: self.resize_text(-2),
                '<t>': lambda e: self.cycle_alpha(), '<T>': lambda e: self.cycle_alpha(),
                '<r>': lambda e: self.reload(), '<R>': lambda e: self.reload(),
                '<h>': lambda e: self.toggle_help(), '<H>': lambda e: self.toggle_help(),
                '<Escape>': lambda e: self.quit(), '<q>': lambda e: self.quit(), '<Q>': lambda e: self.quit()}
        for k, fn in keys.items():
            r.bind(k, fn)
        r.bind('<Configure>', self._on_configure)
        self.render()
        r.after(200, r.focus_force)

    # ---- content -------------------------------------------------------------------------------
    def _load(self):
        try:
            return load_segments(SCRIPT)
        except OSError as e:
            return [dict(cue='', show='', text=f'Could not open the script file:\n{SCRIPT}\n\n{e}')]

    def render(self):
        seg = self.segments[self.i]
        self.top.configure(text=f'{seg["cue"]}    {self.i + 1} / {len(self.segments)}'.strip())
        self.body.configure(text=seg['text'], font=('Segoe UI', self.cfg['size']))
        bottom = f'SHOW: {seg["show"]}' if seg['show'] else ''
        if self.show_help:
            bottom = (bottom + '\n' if bottom else '') + HELP
        self.bottom.configure(text=bottom)
        self._rewrap()

    def _rewrap(self):
        width = max(200, self.root.winfo_width() - 40)
        self.body.configure(wraplength=width)
        self.bottom.configure(wraplength=width)
        if self._fit_job:
            self.root.after_cancel(self._fit_job)
        self._fit_job = self.root.after(30, self._fit)

    def _fit(self):
        """Shrink the text (never below 12 pt) until the section fits the window; never grows past
        the chosen size, so +/- still sets the size you normally read at."""
        self._fit_job = None
        r = self.root
        r.update_idletasks()
        avail = r.winfo_height() - self.top.winfo_reqheight() - self.bottom.winfo_reqheight() - 36
        size = self.cfg['size']
        while True:
            self.body.configure(font=('Segoe UI', size))
            r.update_idletasks()
            if self.body.winfo_reqheight() <= avail or size <= 12:
                break
            size -= 2

    def step(self, d):
        self.goto(self.i + d)

    def goto(self, i):
        self.i = max(0, min(len(self.segments) - 1, i))
        if self.i > 0:
            self.show_help = False          # the help line disappears once you start
        self.render()

    def resize_text(self, d):
        self.cfg['size'] = max(10, min(96, self.cfg['size'] + d))
        self.render()
        self._save()

    def cycle_alpha(self):
        self.cfg['alpha_i'] = (self.cfg['alpha_i'] + 1) % len(ALPHAS)
        self.root.attributes('-alpha', ALPHAS[self.cfg['alpha_i']])
        self._save()

    def toggle_help(self):
        self.show_help = not self.show_help
        self.render()

    def reload(self):
        self.segments = self._load()
        self.i = min(self.i, len(self.segments) - 1)
        self.render()

    # ---- mouse: drag to move, click to advance ---------------------------------------------------
    def _press(self, e):
        self.root.focus_force()
        self._start = (e.x_root, e.y_root, self.root.winfo_x(), self.root.winfo_y())
        self._moved = False

    def _drag(self, e):
        x0, y0, wx, wy = self._start
        dx, dy = e.x_root - x0, e.y_root - y0
        if abs(dx) > DRAG_THRESHOLD or abs(dy) > DRAG_THRESHOLD:
            self._moved = True
        if self._moved:
            self.root.geometry(f'+{wx + dx}+{wy + dy}')

    def _release(self, e):
        if self._moved:
            self._save()
        else:
            self.step(1)

    def _wheel(self, e):
        self.resize_text(+2 if e.delta > 0 else -2)

    def _grip_press(self, e):
        self._gstart = (e.x_root, e.y_root, self.root.winfo_width(), self.root.winfo_height())
        return 'break'

    def _grip_drag(self, e):
        x0, y0, w, h = self._gstart
        nw, nh = max(260, w + e.x_root - x0), max(120, h + e.y_root - y0)
        self.root.geometry(f'{nw}x{nh}+{self.root.winfo_x()}+{self.root.winfo_y()}')
        return 'break'

    def _on_configure(self, e):
        if e.widget is self.root:
            self._rewrap()

    # ---- settings ---------------------------------------------------------------------------------
    def _save(self):
        r = self.root
        self.cfg['geometry'] = f'{r.winfo_width()}x{r.winfo_height()}+{r.winfo_x()}+{r.winfo_y()}'
        try:
            with open(SETTINGS, 'w', encoding='utf-8') as f:
                json.dump(self.cfg, f, indent=1)
        except OSError:
            pass

    def quit(self):
        self._save()
        self.root.destroy()

    def run(self):
        self.root.mainloop()


if __name__ == '__main__':
    Teleprompter().run()
