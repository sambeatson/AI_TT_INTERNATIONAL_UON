"""Pool the five markets in ATR units (orig sentiment): returns and excursions as multiples of ATR14,
so a WTI or Bitcoin move and an index move are comparable. Writes pooled_<rule>.csv."""
from pathlib import Path
import numpy as np, pandas as pd

OUT = Path(__file__).resolve().parent
RNG = np.random.default_rng(11)

def ci(x, n=4000):
    x = np.asarray(x, float); x = x[~np.isnan(x)]
    if len(x) < 3: return np.nan, np.nan
    m = RNG.choice(x, (n, len(x))).mean(1); return np.percentile(m, 2.5), np.percentile(m, 97.5)

def deg(t):
    a = abs(t); return 'weak <0.2' if a < 0.2 else ('moderate 0.2-0.4' if a < 0.4 else 'strong >=0.4')

rows = []
for rule in ('levels', 'pivot'):
    t = pd.read_csv(OUT / f'out_{rule}/trades.csv')
    f = t[(t.filled) & (t.version == 'orig')].copy()
    f['ret_atr'] = f.ret_pts / f.atr
    f['level'] = np.where(f.leg.isin(['R1', 'S1']), 'level 1 (R1/S1)', np.where(f.leg.isin(['R2', 'S2']), 'level 2 (R2/S2)', 'pivot'))
    f['day'] = np.where(f.side > 0, 'positive day (buy)', 'negative day (sell)')
    f['degree'] = f.tilt.map(deg)
    for by in (['level'], ['level', 'day'], ['asset', 'level'], ['level', 'degree']):
        for k, g in f.groupby(['entry', 'window'] + by):
            lo, hi = ci(g.ret_atr)
            rows.append(dict(rule=rule, grouping='+'.join(by), entry=k[0], window=k[1],
                             group=' | '.join(map(str, k[2:])), n=len(g),
                             ret_atr_mean=g.ret_atr.mean(), ci_lo=lo, ci_hi=hi, hit_rate=(g.ret_pct > 0).mean(),
                             mfe_atr_med=g.mfe_atr.median(), mae_atr_med=g.mae_atr.median(),
                             R10_ge1=(g['R_stop1.0'] >= 1).mean(), ret_pct_mean=g.ret_pct.mean()))
r = pd.DataFrame(rows); r.to_csv(OUT / 'pooled.csv', index=False)
pd.set_option('display.width', 250); pd.set_option('display.float_format', lambda x: f'{x:.2f}')
q = r[(r.entry == '0900UK')]
for g in ('level', 'level+day', 'level+degree', 'asset+level'):
    print('==', g); print(q[q.grouping == g].drop(columns=['grouping', 'entry']).to_string(index=False))
