"""tz_check.py - verify broker time offset empirically from tick-volume profile.

Run this on EVERY new M15 file before scoring anything.

  python engine/tz_check.py data/raw/US500_p_M15.csv --expect 16:30

Known liquidity events (true UTC, BST period):
  US cash open   13:30 UTC  -> expect broker peak 16:30 if broker = UTC+3
  FTSE cash open 07:00 UTC  -> expect broker peak 10:00 if broker = UTC+3
  FX             13:30 UTC (NY) and 07:00 UTC (London)

The DateTime_UTC column in the MT5 exports is MISLABELLED (it is UTC+1).
Always index bars by DateTime_Broker.
"""
import sys, argparse, pandas as pd

def load(path):
    d = pd.read_csv(path)
    d['bt'] = pd.to_datetime(d['DateTime_Broker'])
    d = d.sort_values('bt').reset_index(drop=True)
    d['bdate'] = d['bt'].dt.date
    return d

def volume_profile(d, top=6):
    t = d['bt'].dt.time
    v = d.groupby(t)['TickVolume'].mean().sort_values(ascending=False)
    return v.head(top)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('path'); ap.add_argument('--expect', default=None, help='expected broker peak time HH:MM')
    a = ap.parse_args()
    d = load(a.path)
    col_off = (pd.to_datetime(d['DateTime_Broker']) - pd.to_datetime(d['DateTime_UTC'])).unique()
    print(f'file: {a.path}')
    print(f'rows: {len(d)}  sessions: {d.bdate.nunique()}  span: {d.bt.min()} -> {d.bt.max()}')
    print(f'first/last bar time-of-day: {d.bt.dt.time.min()} / {d.bt.dt.time.max()}')
    print(f'DateTime_Broker - DateTime_UTC column: {[str(x) for x in col_off]}  (column is NOT true UTC; ignore it)')
    vp = volume_profile(d)
    print('mean TickVolume by broker time-of-day (top 6):')
    for t, v in vp.items(): print(f'   {str(t)[:5]}  {v:8.0f}')
    peak = str(vp.index[0])[:5]
    if a.expect:
        ok = (peak == a.expect)
        print(f'expected peak {a.expect}: {"OK" if ok else "MISMATCH - STOP AND RESOLVE OFFSET"} (observed {peak})')
        sys.exit(0 if ok else 2)

if __name__ == '__main__':
    main()
