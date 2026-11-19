"""Does report sentiment add anything beyond the market's own recent move?

forward return (from T, window D0/D1/D5, no pivot rule) ~ tilt + prior 5-day return,
both regressors and the outcome rank-transformed; Newey-West (HAC) standard errors with
lag = window length to allow for the overlap of multi-day windows.
"""
from pathlib import Path
import numpy as np, pandas as pd, statsmodels.api as sm
from scipy.stats import spearmanr, rankdata

ROOT = Path(__file__).resolve().parents[2]; OUT = ROOT / 'studies/sentiment_pivot'
FILES = {'UK100': 'data/raw/UK100_p_M15.csv', 'US500': 'data/raw/US500_p_M15.csv'}
LAGS = {'D0': 1, 'D1': 2, 'D5': 5}

sent = pd.read_csv(OUT / 'sentiment_by_date.csv')
moves = pd.read_csv(OUT / 'market_moves.csv')
prior = []
for a, f in FILES.items():
    b = pd.read_csv(ROOT / f, usecols=['DateTime_Broker', 'Close']); b['date'] = b.DateTime_Broker.str[:10]
    c = b.groupby('date').Close.last(); days = list(c.index)
    for d in sent[sent.asset == a].date:
        if d not in days:          # market closed (e.g. US Memorial Day): no trade, no move
            continue
        i = days.index(d)
        prior.append(dict(asset=a, date=d, prior1=100 * (c.iloc[i - 1] / c.iloc[i - 2] - 1),
                          prior5=100 * (c.iloc[i - 1] / c.iloc[i - 6] - 1)))
prior = pd.DataFrame(prior)
rows = []
for a in FILES:
    s = sent[sent.asset == a].merge(prior, on=['asset', 'date'])
    for v in ('orig', 'rev'):
        rho1, p1 = spearmanr(s[f'tilt_{v}'], s.prior1); rho5, p5 = spearmanr(s[f'tilt_{v}'], s.prior5)
        for (e, w), g in moves[(moves.asset == a) & (moves.version == v)].groupby(['entry', 'window']):
            m = g.merge(s, on='date').sort_values('date')
            y = rankdata(m.mkt_ret_pct); X = sm.add_constant(np.column_stack([rankdata(m.tilt), rankdata(m.prior5)]))
            fit = sm.OLS(y, X).fit(cov_type='HAC', cov_kwds={'maxlags': LAGS[w]})
            fit_t = sm.OLS(y, sm.add_constant(rankdata(m.tilt))).fit(cov_type='HAC', cov_kwds={'maxlags': LAGS[w]})
            rows.append(dict(asset=a, version=v, entry=e, window=w, n=len(m),
                             tilt_vs_prior1=rho1, tilt_vs_prior5=rho5,
                             tilt_alone_coef=fit_t.params[1], tilt_alone_p_hac=fit_t.pvalues[1],
                             tilt_coef_given_prior5=fit.params[1], tilt_p_hac=fit.pvalues[1],
                             prior5_coef=fit.params[2], prior5_p_hac=fit.pvalues[2]))
r = pd.DataFrame(rows); r.to_csv(OUT / 'echo_test.csv', index=False)
pd.set_option('display.width', 250); pd.set_option('display.float_format', lambda x: f'{x:.2f}')
print(r.to_string(index=False))
