"""reference_levels.py - leak-free, data-derived levels for every session in an M15 feed.

One row per session date D. Every field on row D is computed **only from bars whose broker date is
strictly less than D**, so a row can be handed to a card-generation or QA session for date D without
leaking D. The tool asserts this per row rather than trusting the construction.

This is the substrate the cards are directly derived from: floor pivots (daily / weekly / monthly),
ATR14, RSI2, swing extremes, and the prior close that M5 requires a MARKET entry to be struck at.
Computing them here, from the execution feed, is what makes the pivot-corroboration question moot -
a level struck from this table is corroborated by construction, because it IS the broker series the
resulting order fills against.

  python engine/reference_levels.py --data data/raw/XAUUSD_p_M15.csv --asset XAUUSD \
      --cash-open 16:30 --cash-close 23:00 --out data/levels/XAUUSD_levels.csv

Cash window defaults to 16:30-23:00 broker (US cash session; correct for US500, NAS100 and XAUUSD,
whose volume peaks at 16:30). Pass the right window for other assets - see docs/HANDOVER_METHOD.md.
"""
import argparse, os, numpy as np, pandas as pd

def floor_pivots(H, L, C, pre=''):
    P = (H + L + C) / 3.0
    return {pre+'P': P, pre+'R1': 2*P - L, pre+'S1': 2*P - H,
            pre+'R2': P + (H - L), pre+'S2': P - (H - L),
            pre+'R3': H + 2*(P - L), pre+'S3': L - 2*(H - P)}

def rsi2(closes):
    """M3 definition: simple 2-period means of gains and losses (not Wilder smoothing)."""
    c = pd.Series(list(closes), dtype=float)
    d = c.diff()
    g = d.clip(lower=0).rolling(2).mean()
    l = (-d.clip(upper=0)).rolling(2).mean()
    r = 100 - 100 / (1 + g / l.replace(0, np.nan))
    r[(l == 0) & (g > 0)] = 100.0
    r[(l == 0) & (g == 0)] = 50.0
    return r

def atr14(day):
    pc = day['C'].shift(1)
    tr = pd.concat([day['H'] - day['L'], (day['H'] - pc).abs(), (day['L'] - pc).abs()], axis=1).max(axis=1)
    return tr.rolling(14).mean()

def sessionise(d, lo=None, hi=None):
    x = d if lo is None else d[(d['tod'] >= lo) & (d['tod'] < hi)]
    g = x.groupby('bd')
    return pd.DataFrame({'O': g['Open'].first(), 'H': g['High'].max(),
                         'L': g['Low'].min(), 'C': g['Close'].last(), 'V': g['TickVolume'].sum()})

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--data', required=True); ap.add_argument('--asset', required=True)
    ap.add_argument('--cash-open', default='16:30'); ap.add_argument('--cash-close', default='23:00')
    ap.add_argument('--out', required=True)
    a = ap.parse_args()

    d = pd.read_csv(a.data)
    d['bt'] = pd.to_datetime(d['DateTime_Broker'])
    d = d.sort_values('bt')
    d['bd'] = d['bt'].dt.date
    d['tod'] = d['bt'].dt.time
    lo, hi = pd.Timestamp(a.cash_open).time(), pd.Timestamp(a.cash_close).time()

    full = sessionise(d)
    cash = sessionise(d, lo, hi)
    if len(cash) < len(full) * 0.9:
        print(f'warning: only {len(cash)} of {len(full)} sessions have bars in {a.cash_open}-{a.cash_close}')

    for f in (full, cash):
        f['atr14'] = atr14(f)
    full['rsi2'] = rsi2(full['C']).values
    cash['rsi2'] = rsi2(cash['C']).values

    # calendar week / month keys, for the "prior completed period" pivot tiers
    ix = pd.to_datetime(pd.Series(full.index, index=full.index))
    keys = pd.DataFrame({'wk': ix.dt.isocalendar().year.astype(str) + '-W' + ix.dt.isocalendar().week.astype(str),
                         'mo': ix.dt.strftime('%Y-%m')}, index=full.index)
    agg = {}
    for tag, f in (('full', full), ('cash', cash)):
        j = f.join(keys, how='inner')
        for per in ('wk', 'mo'):
            agg[(per, tag)] = j.groupby(per).agg(H=('H', 'max'), L=('L', 'min'), C=('C', 'last'),
                                                 end=('H', lambda s: s.index[-1]))

    dates = list(full.index)
    rows = []
    for i, D in enumerate(dates):
        if i < 26:                      # need 25 sessions of history plus one to close
            continue
        prior = dates[:i]               # every session strictly before D - the leak boundary
        p1 = prior[-1]
        r = {'asset': a.asset, 'date': str(D), 'n_prior_sessions': len(prior),
             'last_bar_date': str(p1)}
        assert p1 < D, 'LEAK'

        r['prev_close_full'] = full.at[p1, 'C']          # M5 MARKET-entry anchor
        for tag, f in (('full', full), ('cash', cash)):
            if p1 not in f.index:
                continue
            r[f'prev_open_{tag}'] = f.at[p1, 'O']; r[f'prev_high_{tag}'] = f.at[p1, 'H']
            r[f'prev_low_{tag}'] = f.at[p1, 'L'];  r[f'prev_close_{tag}'] = f.at[p1, 'C']
            r[f'atr14_{tag}'] = f.at[p1, 'atr14']; r[f'rsi2_{tag}'] = f.at[p1, 'rsi2']
            r.update(floor_pivots(f.at[p1, 'H'], f.at[p1, 'L'], f.at[p1, 'C'], pre=f'd_{tag}_'))

        for per, pre in (('wk', 'w'), ('mo', 'm')):
            for tag in ('full', 'cash'):
                done = agg[(per, tag)]
                done = done[done['end'] < D]             # completed periods only
                if len(done):
                    last = done.iloc[-1]
                    r[f'{pre}_{tag}_period'] = done.index[-1]
                    r.update(floor_pivots(last['H'], last['L'], last['C'], pre=f'{pre}_{tag}_'))

        for tag, f in (('full', full), ('cash', cash)):
            hist = [x for x in prior if x in f.index]
            for n in (5, 25):
                w = f.loc[hist[-n:]]
                r[f'swing_high_{n}d_{tag}'] = w['H'].max(); r[f'swing_low_{n}d_{tag}'] = w['L'].min()

        rows.append(r)

    out = pd.DataFrame(rows).round(4)
    os.makedirs(os.path.dirname(a.out) or '.', exist_ok=True)
    out.to_csv(a.out, index=False)
    bad = out[out['last_bar_date'] >= out['date']]
    assert bad.empty, f'LEAK on {len(bad)} rows'
    print(f'{a.out}: {len(out)} sessions {out.date.iloc[0]} -> {out.date.iloc[-1]}  '
          f'| leak check OK (last_bar_date < date on every row)')
    print(f'{len(out.columns)} columns')
    print(out[['date', 'prev_close_full', 'atr14_full', 'atr14_cash', 'rsi2_cash',
               'd_full_P', 'd_full_S1', 'd_full_R1', 'w_cash_P']].tail(3).to_string(index=False))

if __name__ == '__main__':
    main()
