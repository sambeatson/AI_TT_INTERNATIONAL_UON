"""qa_slice_stats.py - leak-free reference numbers for QA of the report dated D, from its slice.

  python engine/qa_slice_stats.py --slice data/slices/US500/US500_upto_2026-05-10.csv --date 2026-05-11 \
        [--closes 7200.75 7259.22 7365.12 7337.11 7398.93]

Prints, from the slice only (bars with broker date < D):
  - last 5 broker sessions: cash-session OHLC (16:30-23:00 broker = 09:30-16:00 ET) and full-day OHLC
  - RSI2 (M3 definition: RS = mean gain / mean loss over 2 periods, simple means) on cash closes
  - ATR14 (D-1) on cash-session and full-day bars
  - daily floor pivots from the D-1 session (P, R1-R3, S1-S3), cash-session and full-day
  - weekly floor pivots from the prior completed calendar week (cash-session)
  - 5-day and 25-day swing high/low (cash-session)
  - optional: RSI2 recomputed from --closes (the report's own close sequence) to test its arithmetic
The CFD feed is not the cash index: expect a small basis difference (a few points) on every field.
"""
import argparse, pandas as pd, numpy as np

def rsi2(closes):
    c = pd.Series(list(closes), dtype=float); d = c.diff()
    g = d.clip(lower=0).rolling(2).mean(); l = (-d.clip(upper=0)).rolling(2).mean()
    rs = g / l.replace(0, np.nan)
    r = 100 - 100 / (1 + rs)
    r[(l == 0) & (g > 0)] = 100.0
    r[(l == 0) & (g == 0)] = 50.0
    return r

def pivots(H, L, C):
    P = (H + L + C) / 3
    return dict(P=P, R1=2*P-L, S1=2*P-H, R2=P+(H-L), S2=P-(H-L), R3=H+2*(P-L), S3=L-2*(H-P))

def atr14(day):
    pc = day['C'].shift(1)
    tr = pd.concat([day['H']-day['L'], (day['H']-pc).abs(), (day['L']-pc).abs()], axis=1).max(axis=1)
    return float(tr.tail(14).mean())

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--slice', required=True); ap.add_argument('--date', required=True)
    ap.add_argument('--closes', nargs='*', type=float, default=None)
    ap.add_argument('--cash-open', default='16:30'); ap.add_argument('--cash-close', default='23:00')
    a = ap.parse_args()
    d = pd.read_csv(a.slice); d['bt'] = pd.to_datetime(d['DateTime_Broker']); d = d.sort_values('bt')
    d['bdate'] = d['bt'].dt.date
    D = pd.Timestamp(a.date).date()
    assert d['bdate'].max() < D, f'slice contains bars on/after {D} - LEAK, stop'
    t = d['bt'].dt.time
    cash = d[(t >= pd.Timestamp(a.cash_open).time()) & (t < pd.Timestamp(a.cash_close).time())]
    agg = dict(O=('Open','first'), H=('High','max'), L=('Low','min'), C=('Close','last'))
    dc = cash.groupby('bdate').agg(**agg); df = d.groupby('bdate').agg(**agg)
    dc['RSI2'] = rsi2(dc['C']).values
    print(f'slice: {a.slice}\nlast bar in slice: {d.bt.max()}  (report date D = {D})\n')
    print(f'LAST 5 SESSIONS - cash-session OHLC ({a.cash_open}-{a.cash_close} broker) with RSI2 on cash closes:')
    print(dc.tail(5).round(2).to_string())
    print('\nLAST 5 SESSIONS - full broker-day OHLC:')
    print(df.tail(5).round(2).to_string())
    last = dc.index[-1]
    print(f'\nD-1 session used for daily pivots: {last}')
    print(f'ATR14 (cash-session bars): {atr14(dc):.2f}    ATR14 (full-day bars): {atr14(df):.2f}')
    pc = pivots(*dc.loc[last, ['H','L','C']]); pf = pivots(*df.loc[last, ['H','L','C']])
    print('DAILY PIVOTS from D-1 cash session:  ' + '  '.join(f'{k} {v:.2f}' for k, v in pc.items()))
    print('DAILY PIVOTS from D-1 full day:      ' + '  '.join(f'{k} {v:.2f}' for k, v in pf.items()))
    wk = dc.copy(); wk['w'] = pd.to_datetime(wk.index).to_period('W-FRI')
    Dw = pd.Timestamp(D).to_period('W-FRI')
    prev = wk[wk['w'] < Dw]
    if len(prev):
        pw = prev[prev['w'] == prev['w'].max()]
        W = pivots(pw['H'].max(), pw['L'].min(), pw['C'].iloc[-1])
        print(f'WEEKLY PIVOTS from prior week ({pw.index[0]}..{pw.index[-1]}, cash): ' + '  '.join(f'{k} {v:.2f}' for k, v in W.items()))
    print(f'SWING 5d  (cash): high {dc.tail(5).H.max():.2f} ({dc.tail(5).H.idxmax()})  low {dc.tail(5).L.min():.2f} ({dc.tail(5).L.idxmin()})')
    print(f'SWING 25d (cash): high {dc.tail(25).H.max():.2f} ({dc.tail(25).H.idxmax()})  low {dc.tail(25).L.min():.2f} ({dc.tail(25).L.idxmin()})')
    print(f'D-1 cash close {dc.C.iloc[-1]:.2f}   D-1 full-day close (23:45 bar) {df.C.iloc[-1]:.2f}')
    if a.closes:
        r = rsi2(a.closes)
        print('\nRSI2 recomputed from the REPORT\'S OWN closes (' + ', '.join(f'{c:.2f}' for c in a.closes) + '): ' + ', '.join('n/a' if np.isnan(x) else f'{x:.1f}' for x in r))
        print('(needs closes before the 5-day window to value the first two rows; the last three are exact tests of the report arithmetic)')

if __name__ == '__main__':
    main()
