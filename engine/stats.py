"""stats.py - compare two (or more) scored card sets.

  python engine/stats.py --a results/baseline_band0845/summary.csv --b results/regen_r1_band0845/summary.csv \
        --labels baseline regenerated --out results/compare/stats_band0845.md

Tests (all on blended R per card, non-filled = 0):
  1. Paired by card_id (same date, same strategy):
       Wilcoxon signed-rank, sign test, mean/median difference with a card-level bootstrap CI.
  2. Daily-block bootstrap on TOTAL R difference (resamples report dates with replacement, keeps all cards
     of a date together) - respects the within-day correlation of the three cards. 5,000 resamples.
  3. Fill-rate and dud/defect-rate differences: two-proportion z test.
  4. Distributional: Mann-Whitney U on the filled-card R distributions (unpaired, for k-draw regenerations).
Reports effective sample size = number of report dates, NOT number of cards.

For k regeneration draws, pass all k summaries via --b (repeatable) and the script reports the
distribution of total R across draws plus the fraction of draws beating the baseline.
"""
import argparse, numpy as np, pandas as pd
from scipy import stats as st

def load(p):
    d = pd.read_csv(p); d['blended_R'] = pd.to_numeric(d.blended_R, errors='coerce').fillna(0); return d

def block_boot(a, b, n=5000, seed=7):
    rng = np.random.default_rng(seed)
    da = a.groupby('report_date')['blended_R'].sum(); db = b.groupby('report_date')['blended_R'].sum()
    dates = sorted(set(da.index) | set(db.index)); da = da.reindex(dates).fillna(0); db = db.reindex(dates).fillna(0)
    diff = (db - da).values; k = len(diff)
    boots = np.array([diff[rng.integers(0, k, k)].sum() for _ in range(n)])
    return diff.sum(), np.percentile(boots, [2.5, 97.5]), (boots <= 0).mean(), k

def two_prop(x1, n1, x2, n2):
    p = (x1 + x2) / (n1 + n2); se = np.sqrt(p * (1 - p) * (1 / n1 + 1 / n2))
    z = ((x2 / n2) - (x1 / n1)) / se if se > 0 else 0
    return z, 2 * (1 - st.norm.cdf(abs(z)))

def compare(a, b, la, lb):
    out = [f'# {la} vs {lb}\n']
    m = a.merge(b, on='card_id', suffixes=('_a', '_b'))
    d = m.blended_R_b - m.blended_R_a
    out.append(f'cards paired: {len(m)}  |  report dates: {a.report_date.nunique()} (effective N)\n')
    out.append(f'total R  {la}: {a.blended_R.sum():+.2f}   {lb}: {b.blended_R.sum():+.2f}   diff: {b.blended_R.sum()-a.blended_R.sum():+.2f}\n')
    out.append(f'mean per-card diff: {d.mean():+.3f}  median: {d.median():+.3f}  cards better/worse/same: {(d>0).sum()}/{(d<0).sum()}/{(d==0).sum()}\n')
    nz = d[d != 0]
    if len(nz) >= 6:
        w = st.wilcoxon(nz); out.append(f'Wilcoxon signed-rank (non-zero diffs, n={len(nz)}): W={w.statistic:.0f}  p={w.pvalue:.4f}\n')
        sg = st.binomtest((nz > 0).sum(), len(nz), 0.5); out.append(f'sign test: {(nz>0).sum()}/{len(nz)} positive  p={sg.pvalue:.4f}\n')
    tot, ci, pneg, k = block_boot(a, b, )
    out.append(f'daily-block bootstrap of total-R difference: {tot:+.2f}  95% CI [{ci[0]:+.2f}, {ci[1]:+.2f}]  P(diff<=0)={pneg:.3f}  (blocks={k})\n')
    fa, fb = (a.fill_status == 'FILLED'), (b.fill_status == 'FILLED')
    z, p = two_prop(fa.sum(), len(a), fb.sum(), len(b))
    out.append(f'fill rate: {fa.mean():.1%} -> {fb.mean():.1%}  z={z:+.2f} p={p:.3f}\n')
    ra, rb = a.loc[fa, 'blended_R'], b.loc[fb, 'blended_R']
    if len(ra) > 5 and len(rb) > 5:
        u = st.mannwhitneyu(ra, rb, alternative='two-sided'); out.append(f'Mann-Whitney on filled-card R: U={u.statistic:.0f} p={u.pvalue:.4f}  | win rate {(ra>0).mean():.1%} -> {(rb>0).mean():.1%}\n')
    out.append('\nby family:\n')
    fam = pd.concat([a.groupby('family')['blended_R'].sum().rename(la), b.groupby('family')['blended_R'].sum().rename(lb)], axis=1).fillna(0)
    fam['diff'] = fam[lb] - fam[la]; out.append(fam.round(2).to_markdown() + '\n')
    out.append('\nby month:\n')
    a['m'] = a.report_date.str[:7]; b['m'] = b.report_date.str[:7]
    mo = pd.concat([a.groupby('m')['blended_R'].sum().rename(la), b.groupby('m')['blended_R'].sum().rename(lb)], axis=1).fillna(0)
    mo['diff'] = mo[lb] - mo[la]; out.append(mo.round(2).to_markdown() + '\n')
    return ''.join(out)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--a', required=True); ap.add_argument('--b', nargs='+', required=True)
    ap.add_argument('--labels', nargs='+', default=None); ap.add_argument('--out', required=True)
    x = ap.parse_args()
    a = load(x.a); la = (x.labels or ['A'])[0]
    txt = ''
    if len(x.b) == 1:
        b = load(x.b[0]); lb = (x.labels or ['A', 'B'])[1]; txt = compare(a, b, la, lb)
    else:
        tots = []
        for i, p in enumerate(x.b):
            b = load(p); tots.append(b.blended_R.sum())
        tots = np.array(tots); base = a.blended_R.sum()
        txt = (f'# {la} vs {len(x.b)} regeneration draws\n\nbaseline total R: {base:+.2f}\n'
               f'draws: mean {tots.mean():+.2f}  sd {tots.std(ddof=1):.2f}  min {tots.min():+.2f}  max {tots.max():+.2f}\n'
               f'fraction of draws beating baseline: {(tots>base).mean():.2f}\n'
               f'one-sample t vs baseline: t={st.ttest_1samp(tots, base).statistic:+.2f} p={st.ttest_1samp(tots, base).pvalue:.4f}\n')
        txt += '\n' + compare(a, load(x.b[0]), la, 'draw1')
    open(x.out, 'w').write(txt); print(txt)

if __name__ == '__main__':
    main()
