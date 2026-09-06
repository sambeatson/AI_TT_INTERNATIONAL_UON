"""linter.py - deterministic card-construction checks.

STATIC checks need no market data and can run at generation time (leak-free):
  DUD_STOP_SIDE      stop on the wrong side of entry
  DUD_TP1_SIDE       TP1 on the wrong side of entry
  DUD_TP2_ORDER      TP2 not beyond TP1
  WARN_TP3_ORDER     TP3 not beyond TP2 (inverted ladder; trade but flag)
  DUD_ZERO_R         entry == stop
  WARN_R_TINY        R < 0.3 x ATR14(D-1)     (needs ATR from the slice - still leak-free)
  WARN_R_HUGE        R > 3.0 x ATR14(D-1)
  WARN_TARGET_FAR    TP1 further than 2.5 x ATR14 from entry (unreachable on a daily horizon)
  WARN_DUPLICATE     identical entry/stop/tp1 to another card in the same report or the previous one

MARKET checks need the anchor bar price on day D (post-hoc diagnostic only):
  STALE_ANCHOR       |anchor_px - entry| > 15 pts on a MARKET card
  MISPLACED_LIMIT    long limit above market / short limit below at the anchor
  MISPLACED_STOP     long stop-entry below market / short above at the anchor
  MALFORMED_FILL     stop on the wrong side of the anchor price (market cards)

Usage:
  python engine/linter.py --cards cards/baseline/cards_baseline.csv --data data/raw/US500_p_M15.csv --out qa/baseline/lint.csv
  (omit --data for static-only)
"""
import argparse, pandas as pd, numpy as np

def num(x):
    try:
        v = float(x); return None if np.isnan(v) else v
    except Exception: return None

def atr14_before(d, D):
    s = d[d['bdate'] < pd.Timestamp(D).date()]
    if len(s) == 0: return None
    day = s.groupby('bdate').agg(H=('High','max'), L=('Low','min'), C=('Close','last'))
    pc = day['C'].shift(1)
    tr = pd.concat([day['H']-day['L'], (day['H']-pc).abs(), (day['L']-pc).abs()], axis=1).max(axis=1)
    return float(tr.tail(14).mean()) if len(tr) >= 5 else None

def anchor_price(d, D, hhmm):
    s = d[(d['bdate'] == pd.Timestamp(D).date()) & (d['bt'].dt.time >= pd.Timestamp(hhmm).time())]
    return (float(s.iloc[0]['Open']), s.iloc[0]['bt']) if len(s) else (None, None)

def lint(cards, d=None):
    out = []
    prev = {}
    for _, c in cards.iterrows():
        flags = []
        if bool(c.get('suppressed', False)):
            out.append(dict(card_id=c.card_id, report_date=c.report_date, strategy=c.strategy, flags='SUPPRESSED', dud=False)); continue
        E, SL = num(c.entry), num(c.stop); T = [num(c.tp1), num(c.tp2), num(c.tp3)]
        L = str(c.direction).upper() == 'LONG'; s = 1 if L else -1
        if E is None or SL is None:
            out.append(dict(card_id=c.card_id, report_date=c.report_date, strategy=c.strategy, flags='UNPRICED', dud=True)); continue
        R = abs(E - SL)
        if s*(E-SL) <= 0: flags.append('DUD_STOP_SIDE')
        if T[0] is not None and s*(T[0]-E) <= 0: flags.append('DUD_TP1_SIDE')
        if T[0] is not None and T[1] is not None and s*(T[1]-T[0]) <= 0: flags.append('DUD_TP2_ORDER')
        if T[1] is not None and T[2] is not None and s*(T[2]-T[1]) <= 0: flags.append('WARN_TP3_ORDER')
        if R == 0: flags.append('DUD_ZERO_R')
        key = (round(E,1), round(SL,1), round(T[0],1) if T[0] else None)
        if key in prev and prev[key] != c.report_date: flags.append('WARN_DUPLICATE')
        prev[key] = c.report_date
        if d is not None:
            atr = atr14_before(d, c.report_date)
            if atr:
                if R < 0.3*atr: flags.append(f'WARN_R_TINY({R/atr:.2f}xATR)')
                if R > 3.0*atr: flags.append(f'WARN_R_HUGE({R/atr:.2f}xATR)')
                if T[0] is not None and abs(T[0]-E) > 2.5*atr: flags.append(f'WARN_TARGET_FAR({abs(T[0]-E)/atr:.2f}xATR)')
            px, _ = anchor_price(d, c.report_date, str(c.anchor_broker) if pd.notna(c.anchor_broker) else '09:00')
            if px is not None:
                m = str(c.entry_mode).upper()
                if m == 'MARKET':
                    if abs(px-E) > 15: flags.append(f'STALE_ANCHOR({px-E:+.1f})')
                    if s*(px-SL) <= 0: flags.append('MALFORMED_FILL')
                elif m == 'LIMIT' and ((L and px < E) or ((not L) and px > E)): flags.append(f'MISPLACED_LIMIT({px-E:+.1f})')
                elif m == 'STOP' and ((L and px > E) or ((not L) and px < E)): flags.append(f'MISPLACED_STOP({px-E:+.1f})')
        out.append(dict(card_id=c.card_id, report_date=c.report_date, strategy=c.strategy,
                        flags='|'.join(flags) if flags else 'CLEAN', dud=any(f.startswith('DUD') for f in flags)))
    return pd.DataFrame(out)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--cards', required=True); ap.add_argument('--data', default=None); ap.add_argument('--out', required=True)
    a = ap.parse_args()
    cards = pd.read_csv(a.cards)
    d = None
    if a.data:
        d = pd.read_csv(a.data); d['bt'] = pd.to_datetime(d['DateTime_Broker']); d = d.sort_values('bt'); d['bdate'] = d['bt'].dt.date
    r = lint(cards, d); r.to_csv(a.out, index=False)
    n = len(r[r['flags'] != 'SUPPRESSED'])
    print(f'{n} cards linted | duds {r.dud.sum()} | clean {(r["flags"]=="CLEAN").sum()}')
    fl = r[r['flags'].isin(['CLEAN','SUPPRESSED'])==False]['flags'].str.split('|').explode().str.replace(r'\(.*\)','',regex=True)
    print(fl.value_counts().to_string())

if __name__ == '__main__':
    main()
