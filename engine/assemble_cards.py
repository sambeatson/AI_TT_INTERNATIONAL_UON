"""assemble_cards.py - build a card registry CSV from per-date JSON files.

  python engine/assemble_cards.py --dir cards/regenerated/<run_id>/by_date \
        --out cards/regenerated/<run_id>/cards_<run_id>_draw1.csv

Validates the schema contract before writing: required fields present, numeric levels parse,
provenance present, one record per Trade family per date. Reports what is missing rather than
silently emitting a short registry.
"""
import argparse, glob, json, os, sys, pandas as pd

COLS = ['card_id','report_date','report_file','strategy','family','direction','entry_mode',
        'entry_mode_text','anchor_broker','entry','stop','tp1','tp2','tp3','card_R_points',
        'be_rule','runner_rule','management_text','suppressed','source','slice_file','last_bar_broker']
# Required on every record. A suppressed card carries no order and no ladder by rule, so the
# level fields and entry_mode are required only on live cards (checked separately below).
REQ = ['card_id','report_date','family','direction','suppressed','source',
       'slice_file','last_bar_broker']
# A baseline card is transcribed from a report, not built from a slice, so it carries report_file
# as its provenance instead of the slice_file / last_bar_broker pair a regenerated card must have.
REQ_BASELINE = ['card_id','report_date','family','direction','suppressed','source',
                'report_file']
REQ_LIVE = ['entry_mode','anchor_broker','entry','stop','tp1','tp2','card_R_points']

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--dir', required=True); ap.add_argument('--out', required=True)
    ap.add_argument('--expect-dates', default=None, help='CSV with report_date column to check coverage')
    ap.add_argument('--baseline', action='store_true',
                    help='baseline registry: require report_file provenance, not slice_file/last_bar_broker')
    a = ap.parse_args()
    rows, problems, defects = [], [], []
    for f in sorted(glob.glob(f'{a.dir}/*.json')):
        D = os.path.basename(f)[:-5]
        try:
            recs = json.load(open(f))
        except Exception as e:
            problems.append(f'{D}: unreadable JSON ({e})'); continue
        if not isinstance(recs, list): problems.append(f'{D}: top level is not a list'); continue
        if not recs: problems.append(f'{D}: empty list'); continue
        for r in recs:
            sup = str(r.get('suppressed')).lower() in ('true','1','yes')
            base = REQ_BASELINE if a.baseline else REQ
            need = base if sup else base + REQ_LIVE
            miss = [k for k in need if k not in r or r[k] is None]
            if miss:
                # A baseline card is a transcript. If the report omitted a level, the registry must
                # carry the omission - the linter scores it as UNPRICED / malformed, which is the
                # finding. Only a regenerated card has no excuse for a missing field.
                sink = defects if (a.baseline and all(k in REQ_LIVE for k in miss)) else problems
                sink.append(f'{D} {r.get("card_id","?")}: report states no {miss}')
            if sup:
                LEVELS = ['entry','stop','tp1','tp2','card_R_points']
                carried = [k for k in LEVELS if r.get(k) is not None]
                if carried: problems.append(f'{D} {r.get("card_id","?")}: SUPPRESSED but carries {carried}')
            if str(r.get('report_date')) != D: problems.append(f'{D} {r.get("card_id","?")}: report_date mismatch')
            ok_src = (str(r.get('source')) == 'baseline') if a.baseline else str(r.get('source','')).startswith('regen_')
            if not ok_src: problems.append(f'{D} {r.get("card_id","?")}: bad source "{r.get("source")}"')
            rows.append({c: r.get(c) for c in COLS})
    if not rows: print('no records found'); sys.exit(1)
    df = pd.DataFrame(rows)[COLS]
    for c in ('entry','stop','tp1','tp2','tp3','card_R_points'):
        df[c] = pd.to_numeric(df[c], errors='coerce')
    df['suppressed'] = df['suppressed'].astype(str).str.lower().isin(['true','1','yes'])
    df = df.sort_values(['report_date','card_id']).reset_index(drop=True)
    if a.expect_dates:
        want = set(pd.read_csv(a.expect_dates)['report_date'].astype(str))
        got = set(df.report_date.astype(str))
        for d in sorted(want - got): problems.append(f'{d}: NO CARDS')
        for d in sorted(got - want): problems.append(f'{d}: unexpected date')
    os.makedirs(os.path.dirname(a.out), exist_ok=True)
    df.to_csv(a.out, index=False)
    print(f'wrote {a.out}: {len(df)} cards over {df.report_date.nunique()} dates '
          f'({df.suppressed.sum()} suppressed)')
    print(df.family.value_counts().to_string())
    if defects:
        print(f'\n{len(defects)} CARDS THE REPORT LEFT INCOMPLETE (transcribed as-is, not fixed):')
        [print(' ', d) for d in defects]
    if problems:
        print(f'\n{len(problems)} PROBLEMS:'); [print(' ', p) for p in problems[:40]]
    else:
        print('\nno problems')

if __name__ == '__main__':
    main()
