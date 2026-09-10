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

def norm_override(s):
    """Map whatever the session wrote onto the three values the framework defines.

    Real variants seen: "restriction_breach**", "none`", "not triggered", "-1 level**" (a session
    describing the override's *effect* rather than naming it). Anything that mentions a restriction
    or a fabricated source is that override; anything else is none.
    """
    v = re.sub(r'[^a-z ]', ' ', str(s or 'none').lower())
    if 'hallucinat' in v or 'fabricat' in v:
        return 'hallucinated_source'
    if 'restriction' in v or 'breach' in v:
        return 'restriction_breach'
    return 'none'


def norm_band(s):
    """Sessions write 'High', 'High_Trust', 'High Trust', 'High**', 'High (75-89)' - one band."""
    s = re.sub(r'\([^)]*\)', ' ', str(s))            # drop a parenthesised range
    s = re.sub(r'[*_`]', ' ', s)                      # drop markdown emphasis
    s = re.sub(r'[_\s]*trust[_\s]*', ' ', s, flags=re.I).strip()
    return ' '.join(w.capitalize() for w in s.split())

SCORE_KEYS = ('c1', 'c2', 'c3', 'c4', 'c5', 'total', 'band', 'override',
              'card_integrity', 'n_cards', 'n_duds', 'n_warns')

def score_line(txt):
    """The canonical one-line score block, if the session wrote one.

    Sessions were asked to state the block on its own lines, and most also emit a single summary
    line. Prefer that line: parsing it avoids every trap in the prose (an arithmetic derivation
    whose first number is a category max, a "Reviewer note on the band:" paragraph, a percentage
    in a table cell). A line qualifies if it carries `total` plus at least two other score keys.
    """
    best = None
    for line in txt.splitlines():
        if not re.search(r'\btotal\s*[=:]', line, re.I):
            continue
        n = sum(1 for k in SCORE_KEYS if re.search(rf'\b{k}\s*[=:]', line, re.I))
        if n >= 3 and (best is None or n >= best[0]):
            best = (n, line)
    return best[1] if best else None


def _num(seg, cast):
    seg = re.sub(r'/\s*100\b', '', seg)          # "83/100" is a score out of 100, not two numbers
    nums = re.findall(r'-?\d+(?:\.\d+)?', seg)
    if not nums:
        return None
    # A rounding arrow ("76.75 -> 77") or an explicit sum ("20.00 + 17.00 + ... = 83") both put the
    # answer last. Anything else - a bare value, or a value followed by prose - puts it first.
    pick = nums[-1] if re.search(r'->|\u2192|\+', seg) else nums[0]
    return cast(float(pick))


def grab(txt, key, cast=float, line=None):
    """Pull one score field. `line` is the canonical block when one was found."""
    for src in ([line] if line else []) + [txt]:
        m = re.search(rf'\b{key}\s*[=:]\s*(.*?)(?=\s+[a-z_]+\s*[=:]|$)', src,
                      re.I | (0 if src is line else re.M))
        if not m:
            continue
        seg = m.group(1).strip().strip('*`').rstrip('.').strip()
        if cast is str:
            v = re.split(r'\s*[(\u2014-]{1,2}\s|\s*\(', seg)[0].strip()
            if v and len(v) < 40:
                return v
            continue
        v = _num(seg, cast)
        if v is not None:
            return v
    if re.fullmatch(r'c[1-5]', key, re.I):        # scorecard-table fallback: | C3 ... | 2 | 0.40 | 25 |
        m = re.search(rf'^\|\s*\**{key}\b[^|]*\|\s*\**\s*([0-5])\s*\**\s*\|', txt, re.I | re.M)
        if m:
            return cast(float(m.group(1)))
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
        sl = score_line(t)
        r = {'report_date': D}
        for k in MAXES:
            r[k] = grab(t, k, int, sl)
        r['total'] = grab(t, 'total', int, sl)
        r['band'] = norm_band(grab(t, 'band', str, sl) or '')
        r['override'] = norm_override(grab(t, 'override', str, sl))
        for k in ('card_integrity', 'n_cards', 'n_duds', 'n_warns'):
            r[k] = grab(t, k, float, sl)

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
        r['total_uncapped'] = calc

        # The framework says an override "caps the band". Sessions read that two ways, and both are
        # defensible: cap the number (total -> 74) or keep the raw number and cap only the label.
        # Accept either, record which was used, and still reject a report that matches neither.
        as_capped = abs(r['total'] - capped) <= 1 and r['band'] == band_of(capped)
        as_labelled = abs(r['total'] - calc) <= 1 and r['band'] == band_of(capped)
        r['cap_convention'] = ('n/a' if capped == calc else
                               'capped_total' if as_capped else
                               'capped_band_only' if as_labelled else 'inconsistent')
        if not (as_capped or as_labelled):
            if abs(r['total'] - capped) > 1 and abs(r['total'] - calc) > 1:
                problems.append(f'{D}: stated total {r["total"]} matches neither the recomputation '
                                f'{calc} nor its capped value {capped} (override {r["override"]})')
            else:
                problems.append(f'{D}: band "{r["band"]}" is not "{band_of(capped)}" as the '
                                f'{r["override"]} override requires')
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
