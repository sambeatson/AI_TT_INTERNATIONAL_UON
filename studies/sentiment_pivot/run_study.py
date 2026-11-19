"""Sentiment cards: a post-event study of report sentiment as a trading signal.

Rules (fixed before any result was looked at):

Signal     tilt s for report date D, from the ORIGINAL report or, where rebuilt cards exist (S&P 500,
           FTSE 100), the REVISED value. s > 0 positive day, s < 0 negative day, s == 0 no trade.
Levels     daily floor pivots for D computed only from bars before D (engine/reference_levels.py):
           cash-session basis for the indices, full-day basis for gold, WTI and Bitcoin.
Entry      from T on D: 09:00 UK (11:00 broker) or US cash open 14:30 UK (16:30 broker).
           px = open of the first M15 bar at or after T. Orders expire 23:00 broker on D.

  rule "levels" (main):  negative day -> SELL LIMIT at R1 and, separately, at R2.
                         positive day -> BUY LIMIT at S1 and, separately, at S2.
                         Each level is its own leg. If price is already through the level at T the
                         limit fills at once at px (a limit order fills at the better price).
  rule "pivot" (comparison, first study): positive -> buy at market above P, buy stop at P below it;
                         negative -> mirror. Extension filter: skip a market entry already beyond the
                         midpoint of S2/S3 (short) or R2/R3 (long).

Windows    from the fill: D0 = rest of day D, D1 = to end of the next trading day, D5 = to end of the
           5th trading day (D plus 4). A window ends early, just before T, on the first later day whose
           report tilt (same version) has the opposite sign.
Measures   MFE / MAE (points, % of entry, ATR14 multiples), return at window end (%), MFE/MAE ratio,
           achievable R with a k x ATR stop (k = 0.5, 1.0): largest favourable move before the stop is
           touched; within a bar the adverse extreme is assumed first.
Degree     |s| < 0.2 weak, 0.2 to < 0.4 moderate, >= 0.4 strong.

Run:  python studies/sentiment_pivot/run_study.py      (writes out_levels/ and out_pivot/)
"""
from pathlib import Path
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'studies/sentiment_pivot'
ASSETS = {  # asset: (price file, pivot basis)
    'US500': ('data/raw/US500_p_M15.csv', 'cash'),
    'UK100': ('data/raw/UK100_p_M15.csv', 'cash'),
    'XAUUSD': ('data/raw/XAUUSD_p_M15.csv', 'full'),
    'SpotCrude': ('data/raw/SpotCrude_p_M15.csv', 'full'),
    'BTCUSD': ('data/raw/BTCUSD_p_M15.csv', 'full'),
}
NAMES = {'US500': 'S&P 500', 'UK100': 'FTSE 100', 'XAUUSD': 'Gold', 'SpotCrude': 'WTI crude', 'BTCUSD': 'Bitcoin'}
ENTRIES = {'0900UK': '11:00', 'USopen': '16:30'}
CUTOFF = '23:00'
WINDOWS = {'D0': 0, 'D1': 1, 'D5': 4}
STOPS_ATR = (0.5, 1.0)
RNG = np.random.default_rng(7)


def load_bars(path):
    b = pd.read_csv(ROOT / path, usecols=['DateTime_Broker', 'Open', 'High', 'Low', 'Close'])
    b['ts'] = pd.to_datetime(b['DateTime_Broker'])
    b['date'] = b['ts'].dt.strftime('%Y-%m-%d')
    b['hm'] = b['ts'].dt.strftime('%H:%M')
    return b.drop(columns='DateTime_Broker').sort_values('ts').reset_index(drop=True)


def level_table(asset, basis):
    """date -> dict of levels; per-date files where they exist, else the combined table."""
    combined = ROOT / f'data/levels/{asset}_levels.csv'
    by_date = ROOT / f'data/levels/{asset}_by_date'
    if by_date.exists():
        rows = {}
        for f in by_date.glob('*.csv'):
            kv = dict(pd.read_csv(f, header=None).values)
            rows[f.stem] = kv
    else:
        t = pd.read_csv(combined)
        rows = {r['date']: r for r in t.to_dict('records')}
    out = {}
    for d, kv in rows.items():
        g = lambda k: float(kv[f'd_{basis}_{k}'])
        out[d] = dict(P=g('P'), R1=g('R1'), R2=g('R2'), R3=g('R3'), S1=g('S1'), S2=g('S2'), S3=g('S3'),
                      atr=float(kv[f'atr14_{basis}']))
    return out


def excursion(path, side, fill, atr):
    fav = (path['High'] - fill) if side > 0 else (fill - path['Low'])
    adv = (fill - path['Low']) if side > 0 else (path['High'] - fill)
    res = dict(mfe=float(fav.max()), mae=float(adv.max()), ret=side * (float(path['Close'].iloc[-1]) - fill))
    for k in STOPS_ATR:
        stop, best = k * atr, 0.0
        for f_, a_ in zip(fav.values, adv.values):
            if a_ >= stop:
                break
            best = max(best, f_)
        res[f'R_stop{k}'] = best / stop
    return res


def entries_levels(after, live, side, L, px):
    """Limit orders at S1/S2 (buy) or R1/R2 (sell). Returns list of (leg, mode, idx, fill) or (leg, None...)."""
    legs = []
    for leg in (('S1', 'S2') if side > 0 else ('R1', 'R2')):
        lvl = L[leg]
        if side * (lvl - px) >= 0:                       # already through the level at T
            legs.append((leg, 'AT_T', after.index[0], px))
            continue
        hit = live[live['Low'] <= lvl] if side > 0 else live[live['High'] >= lvl]
        if hit.empty:
            legs.append((leg, None, None, None))
            continue
        o = float(hit['Open'].iloc[0])
        fill = min(lvl, o) if side > 0 else max(lvl, o)
        legs.append((leg, 'LIMIT', hit.index[0], fill))
    return legs


def entries_pivot(after, live, side, L, px):
    P = L['P']
    if side * (px - P) > 0:
        ext = (L['R2'] + L['R3']) / 2 if side > 0 else (L['S2'] + L['S3']) / 2
        return [('P', 'MARKET_EXT' if side * (px - ext) > 0 else 'MARKET', after.index[0], px)]
    hit = live[live['High'] >= P] if side > 0 else live[live['Low'] <= P]
    if hit.empty:
        return [('P', None, None, None)]
    o = float(hit['Open'].iloc[0])
    return [('P', 'STOP', hit.index[0], max(P, o) if side > 0 else min(P, o))]


def run(rule):
    sent = pd.read_csv(OUT / 'sentiment_by_date.csv')
    rows = []
    for asset, (path, basis) in ASSETS.items():
        bars = load_bars(path)
        lv = level_table(asset, basis)
        days = sorted(bars['date'].unique())
        di = {d: i for i, d in enumerate(days)}
        last_idx = bars.groupby('date').apply(lambda g: g.index[-1]).to_dict()
        s_a = sent[sent.asset == asset].set_index('date')
        versions = ['orig'] + (['rev'] if s_a['tilt_rev'].notna().any() else [])
        for version in versions:
            tilt = s_a[f'tilt_{version}']
            for date, s in tilt.items():
                if date not in di or pd.isna(s) or s == 0 or date not in lv:
                    continue
                L, side = lv[date], (1 if s > 0 else -1)
                day = bars[bars.date == date]
                for ename, T in ENTRIES.items():
                    after = day[day.hm >= T]
                    if after.empty:
                        continue
                    px = float(after['Open'].iloc[0])
                    live = after[after.hm < CUTOFF]
                    legs = (entries_levels if rule == 'levels' else entries_pivot)(after, live, side, L, px)
                    for leg, mode, fill_idx, fill in legs:
                        base = dict(asset=asset, version=version, entry=ename, date=date, tilt=s, side=side,
                                    leg=leg, mode=mode, filled=mode is not None, px_T=px, atr=L['atr'],
                                    level=L.get(leg, np.nan))
                        if mode is None:
                            rows.append(base)
                            continue
                        base.update(fill=fill, fill_ts=bars.at[fill_idx, 'ts'])
                        for wname, k in WINDOWS.items():
                            end_idx = last_idx[days[min(di[date] + k, len(days) - 1)]]
                            reversed_on = ''
                            for j in range(1, k + 1):
                                if di[date] + j >= len(days):
                                    break
                                dj = days[di[date] + j]
                                sj = tilt.get(dj, np.nan)
                                if not pd.isna(sj) and sj * s < 0:
                                    cut = bars[(bars.date == dj) & (bars.hm >= T)]
                                    if not cut.empty:
                                        end_idx, reversed_on = cut.index[0] - 1, dj
                                    break
                            end_idx = max(end_idx, fill_idx)
                            e = excursion(bars.loc[fill_idx:end_idx], side, fill, L['atr'])
                            r = dict(base, window=wname, reversed_on=reversed_on,
                                     mfe_pts=e['mfe'], mae_pts=e['mae'], ret_pts=e['ret'],
                                     mfe_pct=100 * e['mfe'] / fill, mae_pct=100 * e['mae'] / fill,
                                     ret_pct=100 * e['ret'] / fill, mfe_atr=e['mfe'] / L['atr'],
                                     mae_atr=e['mae'] / L['atr'], rr=e['mfe'] / e['mae'] if e['mae'] > 0 else np.nan)
                            for k2 in STOPS_ATR:
                                r[f'R_stop{k2}'] = e[f'R_stop{k2}']
                            rows.append(r)
    return pd.DataFrame(rows)


def boot_ci(x, n=4000):
    x = np.asarray(x, float); x = x[~np.isnan(x)]
    if len(x) < 3:
        return np.nan, np.nan
    m = RNG.choice(x, (n, len(x))).mean(1)
    return np.percentile(m, 2.5), np.percentile(m, 97.5)


def degree(t):
    a = abs(t)
    return 'weak <0.2' if a < 0.2 else ('moderate 0.2-0.4' if a < 0.4 else 'strong >=0.4')


def summarise(trades, outdir, extra_rule=None):
    f = trades[trades.filled].copy()
    f['degree'] = f['tilt'].map(degree)
    keys = ['asset', 'version', 'entry', 'leg', 'window']
    sets = [('all', f)]
    if extra_rule == 'pivot':
        sets.append(('ext_filter', f[f['mode'] != 'MARKET_EXT']))
    out = []
    for name, g0 in sets:
        for k, g in g0.groupby(keys):
            lo, hi = boot_ci(g.ret_pct)
            out.append(dict(zip(keys, k), rule=name, n=len(g), at_T=int(g['mode'].isin(['AT_T', 'MARKET', 'MARKET_EXT']).sum()),
                            long=int((g.side > 0).sum()), short=int((g.side < 0).sum()),
                            mfe_pct_mean=g.mfe_pct.mean(), mae_pct_mean=g.mae_pct.mean(),
                            mfe_atr_med=g.mfe_atr.median(), mae_atr_med=g.mae_atr.median(),
                            rr_median=g.rr.median(), mfe_gt_mae=(g.mfe_pts > g.mae_pts).mean(),
                            ret_pct_mean=g.ret_pct.mean(), ret_ci_lo=lo, ret_ci_hi=hi, hit_rate=(g.ret_pct > 0).mean(),
                            R05_ge1=(g['R_stop0.5'] >= 1).mean(), R10_mean=g['R_stop1.0'].mean(),
                            R10_ge1=(g['R_stop1.0'] >= 1).mean(), R10_ge2=(g['R_stop1.0'] >= 2).mean(),
                            reversed=int((g.reversed_on.fillna('') != '').sum())))
    summ = pd.DataFrame(out)
    summ.to_csv(outdir / 'summary.csv', index=False)
    fills = (trades[trades.window.isna() | (trades.window == 'D0')]
             .groupby(['asset', 'version', 'entry', 'leg'])
             .agg(signals=('filled', 'size'), filled=('filled', 'sum')).reset_index())
    fills.to_csv(outdir / 'fill_rates.csv', index=False)
    deg = (f.groupby(keys[:-1] + ['window', 'degree'])
             .agg(n=('ret_pct', 'size'), ret_pct_mean=('ret_pct', 'mean'),
                  hit_rate=('ret_pct', lambda x: (x > 0).mean()), R10_ge1=('R_stop1.0', lambda x: (x >= 1).mean()))
             .reset_index())
    deg.to_csv(outdir / 'by_degree.csv', index=False)
    return summ


if __name__ == '__main__':
    for rule in ('levels', 'pivot'):
        od = OUT / f'out_{rule}'
        od.mkdir(exist_ok=True)
        t = run(rule)
        t.to_csv(od / 'trades.csv', index=False)
        summarise(t, od, extra_rule=rule)
        print(rule, t[t.window.isna() | (t.window == 'D0')].groupby(['asset', 'version', 'entry'])
              .filled.agg(['size', 'sum']).to_string())
