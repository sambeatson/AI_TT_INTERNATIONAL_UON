"""slices.py - build LEAK-FREE data slices for report regeneration and QA.

For a report dated D, the agent doing QA or card regeneration may see ONLY
bars whose BROKER DATE is strictly before D. That is the last bar of broker
date D-1 (23:45 broker). Nothing from broker date D.

  python engine/slices.py --data data/raw/US500_p_M15.csv --dates cards/baseline/cards_baseline.csv \
        --out data/slices/US500

Produces one CSV per report date:  data/slices/US500/US500_upto_<D-1>.csv
and a manifest listing the last bar included, so the cut is auditable.

Optional extra feeds (VIX, DXY) are sliced with the same rule. News uses --news (D rows kept, actual blanked):
  python engine/slices.py --data data/raw/VIX_D1.csv --dates ... --out data/slices/VIX --tscol DateTime_Broker
  python engine/slices.py --data data/news/news_events.csv --dates ... --out data/slices/NEWS --tscol timestamp_broker --news
"""
import argparse, os, pandas as pd

def cut(df, tscol, D, news=False):
    ts = pd.to_datetime(df[tscol]); Dd = pd.Timestamp(D).date()
    if not news: return df[ts.dt.date < Dd]
    past = df[ts.dt.date < Dd].copy()
    today = df[ts.dt.date == Dd].copy()
    if 'actual' in today: today['actual'] = ''          # scheduled calendar for D is ex-ante; the print is not
    today['note'] = 'SCHEDULED-FOR-D: actual withheld'
    return pd.concat([past, today], ignore_index=True)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--data', required=True)
    ap.add_argument('--dates', required=True, help='CSV with a report_date column')
    ap.add_argument('--out', required=True)
    ap.add_argument('--tscol', default='DateTime_Broker')
    ap.add_argument('--news', action='store_true', help='news mode: keep D rows with actual blanked')
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    df = pd.read_csv(a.data)
    dates = sorted(pd.read_csv(a.dates)['report_date'].unique())
    stem = os.path.splitext(os.path.basename(a.data))[0].split('_')[0]
    man = []
    for D in dates:
        s = cut(df, a.tscol, D, a.news)
        last = pd.to_datetime(s[a.tscol]).max() if len(s) else None
        fn = f'{a.out}/{stem}_upto_{(pd.Timestamp(D)-pd.Timedelta(days=1)).date()}.csv'
        s.to_csv(fn, index=False)
        man.append(dict(report_date=D, slice_file=fn, rows=len(s), last_bar_broker=str(last)))
    pd.DataFrame(man).to_csv(f'{a.out}/MANIFEST.csv', index=False)
    print(pd.DataFrame(man).to_string(index=False))

if __name__ == '__main__':
    main()
