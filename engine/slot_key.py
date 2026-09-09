"""slot_key.py - re-key a scored summary.csv on (report_date, trade slot) so the two arms pair.

Why this exists
---------------
engine/stats.py pairs the two card sets with an inner merge on `card_id`. That is correct only when
both arms emit the same card_id for the same slot. They do not: the M5 regime fork renames the third
card by regime (Trade 3A / 3B / 3C), so a date where the baseline read TREND and the regeneration
read TRANSITION produces `..._Trade_3A` against `..._Trade_3C`. An inner merge on card_id silently
drops exactly those rows - the cards where the two arms disagree most, which is the effect under test.

This rewrites `card_id` to `<report_date>_slot<N>`, N taken from the family ("Trade 1" -> 1,
"Trade 3C" -> 3), and reindexes both arms onto the union of slots. A slot present in one arm only
(the baseline omits three Trade 2 cards) is filled with blended_R = 0 and fill_status = 'NO CARD',
which is what a card that was never written earns. Total R is therefore unchanged in both arms; only
the pairing changes.

  python engine/slot_key.py --a results/baseline_card/summary.csv \
      --b results/regen_.._card/summary.csv --outdir results/paired/card
"""
import argparse, os, pandas as pd

def slot(fam):
    s = str(fam).strip()
    for ch in s:
        if ch.isdigit():
            return int(ch)
    raise ValueError(f'no slot digit in family {fam!r}')

def key(d):
    d = d.copy()
    d['slot'] = d['family'].map(slot)
    if d.duplicated(['report_date', 'slot']).any():
        bad = d[d.duplicated(['report_date', 'slot'], keep=False)][['report_date', 'family', 'card_id']]
        raise SystemExit(f'two cards in one slot:\n{bad}')
    d['card_id'] = d['report_date'].astype(str) + '_slot' + d['slot'].astype(str)
    return d

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--a', required=True); ap.add_argument('--b', required=True)
    ap.add_argument('--outdir', required=True)
    x = ap.parse_args()
    a, b = key(pd.read_csv(x.a)), key(pd.read_csv(x.b))
    union = sorted(set(a.card_id) | set(b.card_id))
    out = []
    for d, src in ((a, x.a), (b, x.b)):
        miss = [k for k in union if k not in set(d.card_id)]
        pad = pd.DataFrame({'card_id': miss})
        pad['report_date'] = [k.rsplit('_slot', 1)[0] for k in miss]
        pad['family'] = ['Trade ' + k.rsplit('_slot', 1)[1] for k in miss]
        pad['strategy'] = pad['family']; pad['direction'] = 'NONE'
        pad['policy'] = d['policy'].iloc[0] if len(d) else ''
        pad['fill_status'] = 'NO CARD'; pad['blended_R'] = 0.0; pad['blended_R_card'] = 0.0
        m = pd.concat([d, pad], ignore_index=True).sort_values('card_id')
        assert len(m) == len(union), (len(m), len(union))
        assert abs(m.blended_R.sum() - d.blended_R.sum()) < 1e-9
        out.append((m, os.path.basename(os.path.dirname(src))))
    os.makedirs(x.outdir, exist_ok=True)
    for m, nm in out:
        m.to_csv(os.path.join(x.outdir, nm + '.csv'), index=False)
    print(f'{x.outdir}: {len(union)} slots  |  ' + '  '.join(
        f'{nm} totR={m.blended_R.sum():+.2f} padded={int((m.fill_status=="NO CARD").sum())}' for m, nm in out))

if __name__ == '__main__':
    main()
