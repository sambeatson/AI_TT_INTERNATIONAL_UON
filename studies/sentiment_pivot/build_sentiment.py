"""Build the per-date sentiment table: original report tilt vs revised (rebuilt-card) tilt.

original = the numeric tilt printed in the report (M2 step 9c / section 13b)
revised  = the sentiment value used by each of the three rebuilt card draws (carried from the
           report, sometimes arithmetic-corrected by the rebuild session per QA feedback)
"""
import csv, glob, json, os, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SETS = {
    'UK100': dict(baseline='cards/baseline/ftse/cards_baseline_ftse.csv', regen='cards/regenerated/ftse_regen1'),
    'US500': dict(baseline='cards/baseline/sp500/cards_baseline_sp500.csv', regen='cards/regenerated/sp500_regen2'),
}
NUM = r'([+\-−]?\s?\d?\.\d+|[+\-−]?\s?[01](?:\.0+)?)'
# Report tilts the regex cannot read cleanly, resolved by reading the report (see REPORT.md, Data).
ORIG_OVERRIDE = {
    ('UK100', '2026-05-14'): -0.05, ('UK100', '2026-05-21'): -0.17, ('UK100', '2026-06-18'): 0.43,
    ('UK100', '2026-07-17'): 0.22, ('UK100', '2026-07-21'): -0.30,
    ('US500', '2026-05-14'): 0.10, ('US500', '2026-05-18'): 0.00, ('US500', '2026-06-30'): -0.30,
    ('US500', '2026-07-10'): 0.10, ('US500', '2026-07-16'): 0.20,
}
ORIG_OVERRIDE_FILE = {
    ('XAUUSD', '2026-05-13', 'Gold_Daily_Report_13May2026.md'): -0.10,
    ('XAUUSD', '2026-05-18', 'Gold_Daily_Report_18-May-2026.md'): -0.45,
    ('XAUUSD', '2026-07-10', 'Gold_Report_10_July_2026.md'): -0.20,
    ('SpotCrude', '2026-06-25', 'WTI_Report_25Jun2026.md'): -0.62,
    ('BTCUSD', '2026-07-24', 'Bitcoin_BTCUSD_Daily_Report_24Jul2026.md'): 0.45,
    ('BTCUSD', '2026-07-26', 'Bitcoin_Daily_Report_26_July_2026.md'): -0.18,
}
SKIP = re.compile(r'stoxx|euro|shenzhen|dax|nasdaq|gold|crude|usd', re.I)
# Original-only sets (no rebuilt cards yet): report files matched by name, primary-asset tilt only.
EXTRA = {
    'XAUUSD': dict(glob=['Gold*.md'], skip=r'stoxx|ftse|s&p|spx|nasdaq|crude|wti|brent|bitcoin|silver|usdx|dollar index|dxy'),
    'SpotCrude': dict(glob=['WTI*.md'], skip=r'stoxx|ftse|s&p|spx|nasdaq|gold|bitcoin|brent|natural gas|usdx|dxy'),
    'BTCUSD': dict(glob=['BTC*.md', 'Bitcoin*.md', 'M1_Bitcoin*.md'], skip=r'ether|eth\b|stoxx|ftse|s&p|spx|nasdaq|gold|crude|wti|usdx|dxy'),
}
MON = {m: i for i, m in enumerate(['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec'], 1)}

def file_date(name):
    m = re.search(r'(\d{4})-(\d{2})-(\d{2})', name)
    if m:
        return f'{m[1]}-{m[2]}-{m[3]}'
    m = re.search(r'(\d{1,2})[-_]?([A-Za-z]{3})[a-z]*[-_]?(\d{4})', name)
    return f'{m[3]}-{MON[m[2].lower()]:02d}-{int(m[1]):02d}'


def num(s):
    return float(s.replace('−', '-').replace(' ', ''))

def report_tilt(md_text, skip=SKIP):
    """First numeric tilt for the primary asset; returns (value, snippet)."""
    pats = [r'numeric\s+tilt\s*[=:]?\s*\**\s*' + NUM,
            r'tilt\s*[=:]\s*\**\s*' + NUM,
            r'tilt\s*\(?\s*' + NUM + r'\s*\)?']
    for p in pats:
        for m in re.finditer(p, md_text, re.I):
            line = md_text[max(0, m.start() - 120): m.end()]
            if skip.search(line.split('\n')[-1]):
                continue
            v = num(m.group(1))
            # "tilt = -0.71 / 4.2 = -0.17": the printed value after the division is the tilt
            tail = re.match(r'\s*\**\s*/\s*[\d.]+\s*=\s*\**\s*' + NUM, md_text[m.end():m.end() + 40])
            if tail:
                v = num(tail.group(1))
            if -1 <= v <= 1:
                return v, re.sub(r'\s+', ' ', md_text[max(0, m.start() - 40): m.end() + 10])
    return None, ''

def regen_value(s):
    if isinstance(s, (int, float)):
        return float(s)
    if isinstance(s, str):
        m = re.search(NUM, s); return num(m.group(1)) if m else None
    for k in ('value', 'signal', 'score'):
        if k in s:
            return float(s[k])
    return None

def main():
    out = ROOT / 'studies/sentiment_pivot/sentiment_by_date.csv'
    rows = []
    for asset, cfg in SETS.items():
        files = {}
        for r in csv.DictReader(open(ROOT / cfg['baseline'])):
            files.setdefault(r['report_date'], r['report_file'])
        for date, rf in sorted(files.items()):
            stem = os.path.splitext(rf)[0]
            md = next(iter(glob.glob(str(ROOT / 'reports/md' / (stem + '.md')))), None)
            if md is None:  # baseline file names sometimes carry "__2_" style suffixes
                md = next(iter(glob.glob(str(ROOT / 'reports/md' / (re.sub(r'_+\d+_$', '', stem) + '*.md')))), None)
            orig, snip = report_tilt(open(md, encoding='utf8').read()) if md else (None, 'no md')
            if (asset, date) in ORIG_OVERRIDE:
                orig, snip = ORIG_OVERRIDE[(asset, date)], 'read from report by hand'
            draws = []
            for k in (1, 2, 3):
                f = ROOT / cfg['regen'] / f'draw{k}/by_date/{date}.json'
                v = None
                if f.exists():
                    d = json.load(open(f)); cards = d if isinstance(d, list) else d.get('cards', [])
                    for c in cards:
                        s = (c.get('direction_components') or {}).get('sentiment') if isinstance(c, dict) else None
                        if s is not None:
                            v = regen_value(s); break
                draws.append(v)
            dv = sorted(x for x in draws if x is not None)
            # median of the draws: robust to a draw that stored the weighted contribution (value x 0.15)
            rows.append(dict(asset=asset, date=date, report_md=os.path.basename(md) if md else '',
                             tilt_orig=orig, tilt_d1=draws[0], tilt_d2=draws[1], tilt_d3=draws[2],
                             tilt_rev=(dv[len(dv) // 2] if len(dv) % 2 else round((dv[0] + dv[-1]) / 2, 4)) if dv else None, orig_snippet=snip[:160]))
    for asset, cfg in EXTRA.items():
        skip = re.compile(cfg['skip'], re.I)
        by_date = {}
        for g in cfg['glob']:
            for md in sorted(glob.glob(str(ROOT / 'reports/md' / g))):
                by_date.setdefault(file_date(os.path.basename(md)), []).append(md)
        for date, mds in sorted(by_date.items()):
            vals = []
            for md in mds:
                v, snip = report_tilt(open(md, encoding='utf8').read(), skip)
                if (asset, date, os.path.basename(md)) in ORIG_OVERRIDE_FILE:
                    v, snip = ORIG_OVERRIDE_FILE[(asset, date, os.path.basename(md))], 'read from report by hand'
                vals.append((v, snip, os.path.basename(md)))
            got = [v for v, _, _ in vals if v is not None]
            # two reports on one date (WTI 10 Jul): average their tilts
            rows.append(dict(asset=asset, date=date, report_md=' + '.join(n for _, _, n in vals),
                             tilt_orig=round(sum(got) / len(got), 4) if got else None,
                             tilt_d1=None, tilt_d2=None, tilt_d3=None, tilt_rev=None,
                             orig_snippet=' | '.join(sn for _, sn, _ in vals)[:160]))
    with open(out, 'w', newline='') as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
    print('wrote', out, len(rows))

if __name__ == '__main__':
    main()
