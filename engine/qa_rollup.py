"""qa_rollup.py - build and validate the Trust Score roll-up from the per-date QA outputs.

The 57 review sessions each write `<D>_trust_score.md` and never touch a shared CSV - 57 concurrent
appends to one file race, and a session that crashes mid-append corrupts it. This reads the per-date
files instead, parses the score block each one is required to state, recomputes the total from the
category levels, and refuses to emit a roll-up it cannot reconcile.

  python engine/qa_rollup.py --dir qa/gold_regen_qa1 --out qa/gold_regen_qa1/trust_scores.csv

Framework v3.7 §4/§6/§7: category level 0-5 -> multiplier, times the category max, summed and rounded.
Overrides cap the total: a fabricated source at 59 (and zeroes C3), a breached restriction at 74.
"""
import argparse, glob, os, re, sys, pandas as pd

MULT = {5: 1.00, 4: 0.85, 3: 0.65, 2: 0.40, 1: 0.20, 0: 0.00}
MAXES = {'c1': 20, 'c2': 20, 'c3': 25, 'c4': 20, 'c5': 15}
CAP = {'restriction_breach': 74, 'hallucinated_source': 59}
BANDS = [(90, 'Very High'), (75, 'High'), (60, 'Moderate'), (40, 'Low'), (0, 'Very Low')]

def band_of(total):
    return next(name for lo, name in BANDS if total >= lo)

def norm_band(s):
    """Sessions write 'High', 'High_Trust', 'High Trust' - all the same band."""
    s = re.sub(r'[_\s]*trust[_\s]*', ' ', str(s), flags=re.I).strip()
    return ' '.join(w.capitalize() for w in s.split())

def grab(txt, key, cast=float):
    """Sessions state the score block in whatever markdown they chose, so parse defensively.

    Two traps seen in practice: an arithmetic line ("Total = 20.00 + 20.00 + ... = 70.75 -> 71")
    whose first number is a category max, not the total; and category levels given only inside the
    scorecard table. So prefer a compact one-line block, then take the LAST bare-number match
    (the summary sits at the end), and fall back to the table for c1..c5.
    """
    compact = re.search(r'\bc1\s*=\s*\d.*?\bc5\s*=\s*\d[^\n]*', txt, re.I)
    if compact:
        m = re.search(rf'\b{key}\s*[=:]\s*`?([A-Za-z0-9_.]+)', compact.group(0), re.I)
        if m and (cast is str or re.fullmatch(r'-?\d+(?:\.\d+)?', m.group(1))):
            return m.group(1).strip() if cast is str else cast(float(m.group(1)))

    hits = re.findall(rf'^[^\n|]*?[`*\-\s]*{key}\s*[=:]\s*`?\**([A-Za-z0-9_.%/ ]+?)\**`?\s*$',
                      txt, re.I | re.M)
    for v in reversed(hits):
        v = v.strip().rstrip('.').split('/')[0].strip()
        if cast is str:
            return v
        if re.fullmatch(r'-?\d+(?:\.\d+)?', v):
            return cast(float(v))

    if re.fullmatch(r'c[1-5]', key, re.I):          # scorecard-table fallback: | C3 ... | 2 | 0.40 | 25 | ...
        m = re.search(rf'^\|\s*\**{key}\b[^|]*\|\s*\**\s*([0-5])\s*\**\s*\|', txt, re.I | re.M)
        if m:
            return cast(float(m.group(1)))
    if cast is str:
        m = re.search(rf'{key}\s*[=:]\s*\**([A-Za-z_][A-Za-z0-9_ ]*)', txt, re.I)
        return m.group(1).strip() if m else None
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--dir', required=True); ap.add_argument('--out', required=True)
    ap.add_argument('--expect', type=int, default=None, help='number of dates that must be present')
    a = ap.parse_args()

    rows, problems = [], []
    for f in sorted(glob.glob(f'{a.dir}/*_trust_score.md')):
        D = os.path.basename(f).replace('_trust_score.md', '')
        t = open(f).read()
        r = {'report_date': D}
        for k in MAXES:
            r[k] = grab(t, k, int)
        r['total'] = grab(t, 'total', int)
        r['band'] = norm_band(grab(t, 'band', str) or '')
        ov = str(grab(t, 'override', str) or 'none').lower().strip()
        r['override'] = 'none' if ov in ('none', 'na', 'n/a', '-') else ov
        for k in ('card_integrity', 'n_cards', 'n_duds', 'n_warns'):
            r[k] = grab(t, k, float)

        miss = [k for k in list(MAXES) + ['total', 'band'] if r.get(k) is None]
        if miss:
            problems.append(f'{D}: score block missing {miss}'); rows.append(r); continue
        for k in MAXES:
            if r[k] not in MULT:
                problems.append(f'{D}: {k}={r[k]} is not a level 0-5')

        # recompute, then apply any override cap - the cap is why a stated total can sit below the sum
        calc = round(sum(MULT.get(r[k], 0) * MAXES[k] for k in MAXES))
        capped = min(calc, CAP[r['override']]) if r['override'] in CAP else calc
        r['total_recomputed'] = capped
        if abs(r['total'] - capped) > 1:
            problems.append(f'{D}: stated total {r["total"]} vs recomputed {capped} '
                            f'(uncapped {calc}, override {r["override"]})')
        if r['band'] != band_of(r['total']):
            problems.append(f'{D}: band "{r["band"]}" does not match total {r["total"]} '
                            f'(expected "{band_of(r["total"])}")')
        if r['override'] == 'hallucinated_source' and r['c3'] != 0:
            problems.append(f'{D}: hallucinated_source override requires c3=0, got c3={r["c3"]}')
        if not os.path.exists(f'{a.dir}/{D}_feedback.md'):
            problems.append(f'{D}: no feedback file')
        rows.append(r)

    if not rows:
        print('no per-date trust_score files found'); sys.exit(1)
    df = pd.DataFrame(rows).sort_values('report_date')
    df.to_csv(a.out, index=False)
    print(f'wrote {a.out}: {len(df)} dates')
    if a.expect and len(df) != a.expect:
        problems.append(f'expected {a.expect} dates, found {len(df)}')
    ok = df.dropna(subset=['total'])
    if len(ok):
        print(f'total: mean {ok.total.mean():.1f}  sd {ok.total.std():.1f}  '
              f'min {ok.total.min():.0f}  max {ok.total.max():.0f}')
        print('bands:', ok.band.value_counts().to_dict())
        print('overrides:', ok.override.value_counts().to_dict())
        print('category means:', {k: round(ok[k].mean(), 2) for k in MAXES})
        if ok.card_integrity.notna().any():
            print(f'card integrity: mean {ok.card_integrity.mean():.1f}  min {ok.card_integrity.min():.1f}')
    if problems:
        print(f'\n{len(problems)} PROBLEMS:'); [print(' ', p) for p in problems]
    else:
        print('\nno problems')

if __name__ == '__main__':
    main()
