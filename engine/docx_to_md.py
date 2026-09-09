"""docx_to_md.py - convert report .docx to markdown, preserving document order.

pandoc is not available in this environment, so this does the job with python-docx. It walks the
body XML rather than doc.paragraphs + doc.tables, because those two lists lose the interleaving and
a report's cards sit in tables between prose sections - order is the whole point.

Headings map to ATX by level; bold/italic runs are marked up; tables become pipe tables (pandoc's
grid tables are harder to read and nothing downstream needs them).

  python engine/docx_to_md.py reports/docx/Gold_Report_11_May_2026.docx --outdir reports/md
  python engine/docx_to_md.py 'reports/docx/Gold*.docx' --outdir reports/md
"""
import argparse, glob, os, re
from docx import Document
from docx.table import Table
from docx.text.paragraph import Paragraph

def _fmt(r, attr):
    """Some of these .docx files were machine-generated and carry a malformed w:val on w:b / w:i
    (literally 'function bold() { [native code] }'), which python-docx rejects. Treat any run whose
    flag will not parse as unformatted rather than losing the document."""
    try:
        return bool(getattr(r, attr))
    except Exception:
        return False

def runs_md(p):
    out = []
    for r in p.runs:
        t = r.text
        if not t:
            continue
        if t.strip():
            lead = t[:len(t) - len(t.lstrip())]
            trail = t[len(t.rstrip()):]
            core = t.strip()
            if _fmt(r, 'bold'):
                core = f'**{core}**'
            if _fmt(r, 'italic'):
                core = f'*{core}*'
            t = lead + core + trail
        out.append(t)
    s = ''.join(out) or p.text
    return re.sub(r'[ \t]+', ' ', s).strip()

def para_md(p):
    txt = runs_md(p)
    if not txt:
        return ''
    style = ((p.style.name if p.style is not None else '') or '').lower()
    m = re.match(r'heading (\d)', style)
    if m:
        return '#' * min(int(m.group(1)), 6) + ' ' + re.sub(r'\*\*|\*', '', txt)
    if style.startswith('title'):
        return '# ' + re.sub(r'\*\*|\*', '', txt)
    if 'list' in style:
        return '- ' + txt
    return txt

def cell_md(c):
    parts = [runs_md(p) for p in c.paragraphs]
    return ' '.join(x for x in parts if x).replace('|', '\\|').strip()

def table_md(t):
    rows = [[cell_md(c) for c in r.cells] for r in t.rows]
    rows = [r for r in rows if any(x for x in r)]
    if not rows:
        return ''
    w = max(len(r) for r in rows)
    rows = [r + [''] * (w - len(r)) for r in rows]
    head, body = rows[0], rows[1:]
    if not any(head):                      # headerless table: synthesise a blank header row
        head, body = [''] * w, rows
    out = ['| ' + ' | '.join(head) + ' |', '|' + '---|' * w]
    out += ['| ' + ' | '.join(r) + ' |' for r in body]
    return '\n'.join(out)

def convert(path):
    doc = Document(path)
    body = doc.element.body
    parts, prev_blank = [], True
    for child in body.iterchildren():
        tag = child.tag.split('}')[-1]
        if tag == 'p':
            md = para_md(Paragraph(child, doc))
            if md:
                parts.append(md); prev_blank = False
            elif not prev_blank:
                parts.append(''); prev_blank = True
        elif tag == 'tbl':
            md = table_md(Table(child, doc))
            if md:
                if not prev_blank:
                    parts.append('')
                parts.append(md); parts.append(''); prev_blank = True
    return re.sub(r'\n{3,}', '\n\n', '\n'.join(parts)).strip() + '\n'

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('pattern', nargs='+'); ap.add_argument('--outdir', required=True)
    ap.add_argument('--force', action='store_true')
    a = ap.parse_args()
    files = sorted({f for p in a.pattern for f in glob.glob(p)})
    os.makedirs(a.outdir, exist_ok=True)
    n_new = n_skip = 0
    for f in files:
        out = os.path.join(a.outdir, os.path.splitext(os.path.basename(f))[0] + '.md')
        if os.path.exists(out) and not a.force:
            n_skip += 1; continue
        md = convert(f)
        open(out, 'w').write(md)
        n_new += 1
        print(f'{os.path.basename(out):48s} {len(md):7,d} chars  '
              f'{md.count(chr(10)+"#"):3d} headings  {md.count("|---"):2d} tables')
    print(f'\nwrote {n_new}, skipped {n_skip} (already present; --force to overwrite)')

if __name__ == '__main__':
    main()
