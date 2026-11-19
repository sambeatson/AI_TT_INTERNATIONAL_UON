"""Sentiment-pivot card: a post-event study of report sentiment as a trading signal.

Rules (fixed before any result was looked at):

Signal     tilt s for report date D, from the ORIGINAL report or the REVISED (rebuilt-card) value.
           s > 0 LONG, s < 0 SHORT, s == 0 no trade.
Pivot      daily cash pivot P for D, computed only from bars before D (data/levels/<asset>_by_date/D.csv).
Entry      at T on D: 09:00 UK (11:00 broker) or US cash open 14:30 UK (16:30 broker).
           px = open of the first M15 bar at or after T.
           LONG : px > P -> buy at market (px).  px <= P -> buy stop at P, filled on the first bar from T
                  with high >= P at max(P, bar open); expires 23:00 broker on D.
           SHORT: mirror image (sell at market below P, sell stop at P from above).
Extension  additional rule, tested separately: a MARKET entry is skipped when price has already run
filter     past the "2.5" level, i.e. the midpoint of S2 and S3 for a short (midpoint of R2 and R3 for a
           long). Stop entries at P are unaffected.
Windows    excursion measured from the fill over
             D0 = rest of day D,  D1 = to end of the next trading day,  D5 = to end of the 5th trading
             day (D plus 4).  A window ends early at time T on the first later day whose report tilt
             (same version) has the opposite sign: the sentiment reversed.
Measures   MFE / MAE (points, % of entry, ATR14 multiples), close at window end (%), MFE/MAE ratio,
           and achievable R: with a stop of k x ATR (k = 0.5, 1.0) placed at entry, the largest
           favourable move reached before the stop is touched, in R. Within a bar the adverse extreme
           is assumed to come first (conservative).
Degree     |s| < 0.2 weak, 0.2 to < 0.4 moderate, >= 0.4 strong; plus Spearman of s against the
           market's move from T, regardless of fill.

Run:  python studies/sentiment_pivot/run_study.py
"""
from pathlib import Path
import numpy as np
import pandas as pd
from scipy.stats import spearmanr

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'studies/sentiment_pivot'
ASSETS = {'UK100': 'data/raw/UK100_p_M15.csv', 'US500': 'data/raw/US500_p_M15.csv'}
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
    return b.drop(columns='DateTime_Broker').reset_index(drop=True)


def levels(asset, date):
    f = ROOT / f'data/levels/{asset}_by_date/{date}.csv'
    kv = dict(pd.read_csv(f, header=None).values)
    g = lambda k: float(kv[k])
    return dict(P=g('d_cash_P'), R2=g('d_cash_R2'), R3=g('d_cash_R3'), S2=g('d_cash_S2'),
                S3=g('d_cash_S3'), atr=g('atr14_cash'))


def excursion(path, side, fill, atr):
    """path: bars from the fill bar to the window end (inclusive)."""
    fav = (path['High'] - fill) if side > 0 else (fill - path['Low'])
    adv = (fill - path['Low']) if side > 0 else (path['High'] - fill)
    mfe, mae = float(fav.max()), float(adv.max())
    end = float(path['Close'].iloc[-1])
    res = dict(mfe=mfe, mae=mae, ret=side * (end - fill))
    for k in STOPS_ATR:
        stop = k * atr
        best = 0.0
        for f_, a_ in zip(fav.values, adv.values):
            if a_ >= stop:            # adverse first within the bar
                break
            best = max(best, f_)
        res[f'R_stop{k}'] = best / stop
        res[f'stopped{k}'] = bool((adv >= stop).any())
    return res


def run():
    sent = pd.read_csv(OUT / 'sentiment_by_date.csv')
    rows, moves = [], []
    for asset, path in ASSETS.items():
        bars = load_bars(path)
        days = sorted(bars['date'].unique())
        di = {d: i for i, d in enumerate(days)}
        s_a = sent[sent.asset == asset].set_index('date')
        for version in ('orig', 'rev'):
            tilt = s_a[f'tilt_{version}']
            for date, s in tilt.items():
                if date not in di or pd.isna(s):
                    continue
                L = levels(asset, date)
                for ename, T in ENTRIES.items():
                    day = bars[bars.date == date]
                    after = day[day.hm >= T]
                    if after.empty:
                        continue
                    px = float(after['Open'].iloc[0])
                    # market move from T regardless of fill: for the degree-of-sentiment test
                    for wname, k in WINDOWS.items():
                        last = days[min(di[date] + k, len(days) - 1)]
                        endc = float(bars[bars.date == last]['Close'].iloc[-1])
                        moves.append(dict(asset=asset, version=version, entry=ename, window=wname,
                                          date=date, tilt=s, mkt_ret_pct=100 * (endc - px) / px))
                    if s == 0:
                        continue
                    side = 1 if s > 0 else -1
                    P = L['P']
                    ext_lvl = (L['R2'] + L['R3']) / 2 if side > 0 else (L['S2'] + L['S3']) / 2
                    if side * (px - P) > 0:
                        mode, fill, fill_ts = 'MARKET', px, after['ts'].iloc[0]
                        fill_idx = after.index[0]
                        extended = side * (px - ext_lvl) > 0
                    else:
                        live = after[after.hm < CUTOFF]
                        hit = live[(live['High'] >= P)] if side > 0 else live[(live['Low'] <= P)]
                        extended = False
                        if hit.empty:
                            rows.append(dict(asset=asset, version=version, entry=ename, date=date,
                                             tilt=s, side=side, mode='STOP', filled=False, pivot=P, px_T=px))
                            continue
                        mode, fill_idx = 'STOP', hit.index[0]
                        o = float(bars.at[fill_idx, 'Open'])
                        fill = max(P, o) if side > 0 else min(P, o)
                        fill_ts = bars.at[fill_idx, 'ts']
                    base = dict(asset=asset, version=version, entry=ename, date=date, tilt=s, side=side,
                                mode=mode, filled=True, extended=extended, pivot=P, px_T=px, fill=fill,
                                fill_ts=fill_ts, atr=L['atr'])
                    for wname, k in WINDOWS.items():
                        end_day = days[min(di[date] + k, len(days) - 1)]
                        end_idx = bars[bars.date == end_day].index[-1]
                        reversed_on = ''
                        for j in range(1, k + 1):
                            if di[date] + j >= len(days):
                                break
                            dj = days[di[date] + j]
                            sj = tilt.get(dj, np.nan)
                            if not pd.isna(sj) and sj * s < 0:
                                cut = bars[(bars.date == dj) & (bars.hm >= T)]
                                if not cut.empty:
                                    end_idx = cut.index[0] - 1   # exit just before the new card would trade
                                    reversed_on = dj
                                break
                        if end_idx < fill_idx:
                            end_idx = fill_idx
                        e = excursion(bars.loc[fill_idx:end_idx], side, fill, L['atr'])
                        r = dict(base, window=wname, reversed_on=reversed_on,
                                 mfe_pts=e['mfe'], mae_pts=e['mae'], ret_pts=e['ret'],
                                 mfe_pct=100 * e['mfe'] / fill, mae_pct=100 * e['mae'] / fill,
                                 ret_pct=100 * e['ret'] / fill,
                                 mfe_atr=e['mfe'] / L['atr'], mae_atr=e['mae'] / L['atr'],
                                 rr=e['mfe'] / e['mae'] if e['mae'] > 0 else np.nan)
                        for k2 in STOPS_ATR:
                            r[f'R_stop{k2}'] = e[f'R_stop{k2}']
                            r[f'stopped{k2}'] = e[f'stopped{k2}']
                        rows.append(r)
    trades = pd.DataFrame(rows)
    trades.to_csv(OUT / 'trades.csv', index=False)
    pd.DataFrame(moves).to_csv(OUT / 'market_moves.csv', index=False)
    return trades, pd.DataFrame(moves)


def boot_ci(x, n=4000):
    x = np.asarray(x, float)
    x = x[~np.isnan(x)]
    if len(x) < 3:
        return np.nan, np.nan
    m = RNG.choice(x, (n, len(x))).mean(1)
    return np.percentile(m, 2.5), np.percentile(m, 97.5)


def degree(t):
    a = abs(t)
    return 'weak <0.2' if a < 0.2 else ('moderate 0.2-0.4' if a < 0.4 else 'strong >=0.4')


def summarise(trades, moves):
    f = trades[trades.filled & trades.window.notna()].copy()
    f['degree'] = f['tilt'].map(degree)
    out = []
    for filt in ('all', 'ext_filter'):
        g0 = f if filt == 'all' else f[~f.extended.fillna(False).astype(bool)]
        for keys, g in g0.groupby(['asset', 'version', 'entry', 'window']):
            lo, hi = boot_ci(g.ret_pct)
            out.append(dict(zip(['asset', 'version', 'entry', 'window'], keys), rule=filt, n=len(g),
                            market=int((g['mode'] == 'MARKET').sum()), stop=int((g['mode'] == 'STOP').sum()),
                            mfe_pct_mean=g.mfe_pct.mean(), mae_pct_mean=g.mae_pct.mean(),
                            mfe_atr_med=g.mfe_atr.median(), mae_atr_med=g.mae_atr.median(),
                            rr_median=g.rr.median(), mfe_gt_mae=(g.mfe_pts > g.mae_pts).mean(),
                            ret_pct_mean=g.ret_pct.mean(), ret_pct_sum=g.ret_pct.sum(), ret_ci_lo=lo, ret_ci_hi=hi,
                            hit_rate=(g.ret_pct > 0).mean(),
                            R05_mean=g['R_stop0.5'].mean(), R05_ge1=(g['R_stop0.5'] >= 1).mean(),
                            R05_ge2=(g['R_stop0.5'] >= 2).mean(),
                            R10_mean=g['R_stop1.0'].mean(), R10_ge1=(g['R_stop1.0'] >= 1).mean(),
                            R10_ge2=(g['R_stop1.0'] >= 2).mean(),
                            reversed=int((g.reversed_on.fillna('') != '').sum())))
    summ = pd.DataFrame(out)
    summ.to_csv(OUT / 'summary.csv', index=False)

    deg = (f.groupby(['asset', 'version', 'entry', 'window', 'degree'])
             .agg(n=('ret_pct', 'size'), ret_pct_mean=('ret_pct', 'mean'), hit_rate=('ret_pct', lambda x: (x > 0).mean()),
                  mfe_pct_mean=('mfe_pct', 'mean'), mae_pct_mean=('mae_pct', 'mean'),
                  R10_ge1=('R_stop1.0', lambda x: (x >= 1).mean()))
             .reset_index())
    deg.to_csv(OUT / 'by_degree.csv', index=False)

    sp = []
    for keys, g in moves.groupby(['asset', 'version', 'entry', 'window']):
        rho, p = spearmanr(g.tilt, g.mkt_ret_pct)
        agree = ((np.sign(g.tilt) * np.sign(g.mkt_ret_pct)) > 0)[g.tilt != 0].mean()
        nz = g[g.tilt != 0]
        sp.append(dict(zip(['asset', 'version', 'entry', 'window'], keys), n=len(g), spearman=rho, p=p,
                       sign_agreement=agree,
                       # benchmarks at market from T, no pivot rule, no reversal cut
                       follow_sentiment_ret_mean=(np.sign(nz.tilt) * nz.mkt_ret_pct).mean(),
                       always_long_ret_mean=g.mkt_ret_pct.mean()))
    sp = pd.DataFrame(sp)
    sp.to_csv(OUT / 'tilt_vs_market.csv', index=False)
    return summ, deg, sp


if __name__ == '__main__':
    trades, moves = run()
    summ, deg, sp = summarise(trades, moves)
    pd.set_option('display.width', 250); pd.set_option('display.max_columns', 40)
    print(trades.groupby(['asset', 'version', 'entry']).apply(lambda g: pd.Series(dict(
        rows=len(g), unfilled=int((~g.filled).sum())))).to_string())
