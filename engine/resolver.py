"""resolver.py - score a card registry against M15 broker data under a named entry policy.

All times are BROKER time (UTC+3 during BST). Index by DateTime_Broker only.

ENTRY POLICIES (--policy):
  card       Card as written. Monitoring opens at the card's own anchor_broker on the ENTRY SESSION
             (the session AFTER report_date unless --same-session). Market cards fill at the anchor bar
             open; limit/stop cards fill on first touch before the cut-off; conditional cards trigger on
             a confirming daily close and enter at the next session's anchor.
  midnight   CFD-style. Orders live from 02:00 broker (00:00 UK) of the entry session. Same fill rules.
  usopen     Orders live from 16:30 broker (14:30 UK, US cash open). Same fill rules.
  band0845   Disciplined band entry from 08:45 broker with dud screen:
               in band [0, +0.75R] improvement -> market; worse -> wait for return to entry;
               beyond +0.75R -> wait for recovery to entry-0.5R. Stop never moves.

CUT-OFF (--cutoff HH:MM broker): last time an unfilled order may fill. Default 23:00 (equities/other).
   FX: use --cutoff 18:00 and --open 09:00.

MICRO-R GUARD (--min-risk, default 0.25): a fill whose realised risk to the card stop is below this
   fraction of the card's stated R is NOT taken (status SKIPPED_MICRO_R). Set 0 to disable.
MALFORMED (--malformed skip|stop): stop on the wrong side of the fill -> skip (default) or score -1R.

MANAGEMENT (--be): 'card' (use each card's be_rule) | 'tp1' (force BE-on-TP1) | 'none'.
RUNNER: honours SESSION_CLOSE_TIMESTOP when the card says so; else traces to target/stop.

Outputs <out>/ledger.csv (per unit) and <out>/summary.csv (per card, blended R).

  python engine/resolver.py --cards cards/baseline/cards_baseline.csv --data data/raw/US500_p_M15.csv \
        --policy band0845 --out results/baseline_band0845
"""
import argparse, os, re, pandas as pd, numpy as np

# ---------------------------------------------------------------- data
def load(path):
    d = pd.read_csv(path); d['bt'] = pd.to_datetime(d['DateTime_Broker'])
    d = d.sort_values('bt').reset_index(drop=True); d['bdate'] = d['bt'].dt.date
    return d

class Feed:
    def __init__(self, d): self.d = d; self.sess = sorted(d['bdate'].unique())
    def next_session(self, D):
        D = pd.Timestamp(D).date(); n = [s for s in self.sess if s > D]; return n[0] if n else None
    def bars(self, sd, frm_hhmm, to_hhmm=None):
        m = self.d[(self.d['bdate'] == sd) & (self.d['bt'].dt.time >= pd.Timestamp(frm_hhmm).time())]
        if to_hhmm: m = m[m['bt'].dt.time <= pd.Timestamp(to_hhmm).time()]
        return m
    def touch(self, frm, lvl, side, upto=None):
        m = self.d[self.d['bt'] >= pd.Timestamp(frm)]
        if upto is not None: m = m[m['bt'] <= pd.Timestamp(upto)]
        m = m[m['High'] >= lvl] if side == 'up' else m[m['Low'] <= lvl]
        return None if len(m) == 0 else m.iloc[0]['bt']
    def session_close(self, sd):
        s = self.d[self.d['bdate'] == sd]; return (float(s.iloc[-1]['Close']), s.iloc[-1]['bt']) if len(s) else (None, None)
    def daily_closes_after(self, ts): return self.d[self.d['bt'] > pd.Timestamp(ts)].groupby('bdate')['Close'].last()
    def last(self): return float(self.d.iloc[-1]['Close']), self.d.iloc[-1]['bt']

def num(x):
    try:
        v = float(x); return None if np.isnan(v) else v
    except Exception: return None

# ---------------------------------------------------------------- entry
def find_entry(feed, c, policy, open_hhmm, cutoff_hhmm, same_session):
    """returns dict(fill_ts, fill_px, rule, session, status, reason)"""
    E, SL = num(c.entry), num(c.stop); L = str(c.direction).upper() == 'LONG'; s = 1 if L else -1
    mode = str(c.entry_mode).upper(); Rc = abs(E - SL)
    D = pd.Timestamp(c.report_date).date()
    es = D if same_session else feed.next_session(D)
    trig = ''
    if mode == 'CONDITIONAL':
        dc = feed.daily_closes_after(pd.Timestamp(D) - pd.Timedelta(minutes=1))
        hit = dc[dc > E] if L else dc[dc < E]
        if len(hit) == 0: return dict(status='NO TRIGGER', reason=f'confirming close beyond {E} never printed', session=None)
        es = feed.next_session(hit.index[0]); trig = f'confirmed close {hit.iloc[0]:.1f} on {hit.index[0]}; '
    if es is None: return dict(status='NO SESSION', reason='no following session in data', session=None)
    anchor = {'card': str(c.anchor_broker) if pd.notna(c.anchor_broker) else open_hhmm,
              'midnight': '02:00', 'usopen': '16:30', 'band0845': '08:45'}[policy]
    if policy == 'card' and anchor < open_hhmm: anchor = open_hhmm   # never earlier than the asset's session open
    w = feed.bars(es, anchor, cutoff_hhmm)
    if len(w) == 0: return dict(status='NO BARS', reason=f'no bars from {anchor} on {es}', session=es)
    px, t0, t1 = float(w.iloc[0]['Open']), w.iloc[0]['bt'], w.iloc[-1]['bt']
    if policy == 'band0845':
        imp = s * (E - px) / Rc
        if -1e-9 <= imp <= 0.75:
            return dict(status='FILLED', fill_ts=t0, fill_px=px, session=es, rule=f'IN BAND ({imp:+.2f}R) market at 08:45', reason=trig)
        if imp > 0.75:
            RE = E - s * 0.5 * Rc; t = feed.touch(t0, RE, 'up' if L else 'dn', t1)
            if t is None: return dict(status='NO FILL', session=es, reason=f'{trig}08:45 {px:.1f} was {imp:+.2f}R beyond entry; no recovery to {RE:.1f} by cut-off')
            return dict(status='FILLED', fill_ts=t, fill_px=RE, session=es, rule=f'RECOVERY to entry-0.5R ({RE:.2f})', reason=trig)
        t = feed.touch(t0, E, 'dn' if L else 'up', t1)
        if t is None: return dict(status='NO FILL', session=es, reason=f'{trig}08:45 {px:.1f} was {imp:+.2f}R worse than entry; never returned to entry by cut-off')
        return dict(status='FILLED', fill_ts=t, fill_px=E, session=es, rule='WAITED for return to entry', reason=trig)
    # card / midnight / usopen: literal order handling
    if mode in ('MARKET', 'CONDITIONAL'):
        return dict(status='FILLED', fill_ts=t0, fill_px=px, session=es, rule=f'MARKET at {anchor} open', reason=trig)
    trig_side = ('up' if L else 'dn') if mode == 'STOP' else ('dn' if L else 'up')
    marketable = ((px >= E) if L else (px <= E)) if mode == 'STOP' else ((px <= E) if L else (px >= E))
    if marketable:
        return dict(status='FILLED', fill_ts=t0, fill_px=px, session=es, rule=f'{mode} already marketable at {anchor} - filled at open', reason=trig)
    t = feed.touch(t0, E, trig_side, t1)
    if t is None: return dict(status='NO FILL', session=es, reason=f'{trig}{mode} {E} not reached from {anchor} to {cutoff_hhmm} on {es} (range {w.Low.min():.1f}-{w.High.max():.1f})')
    return dict(status='FILLED', fill_ts=t, fill_px=E, session=es, rule=f'{mode} touched', reason=trig)

# ---------------------------------------------------------------- resolve
def resolve(feed, c, ent, be_mode, min_risk=0.25, malformed='skip'):
    E, SL = num(c.entry), num(c.stop); T = [num(c.tp1), num(c.tp2), num(c.tp3)]
    L = str(c.direction).upper() == 'LONG'; s = 1 if L else -1
    fp, ft, es = ent['fill_px'], ent['fill_ts'], ent['session']
    Rr = abs(fp - SL); Rc = abs(E - SL)
    rows = []
    if s * (fp - SL) <= 0:
        if malformed == 'stop':
            for u in ('Unit 1', 'Unit 2', 'Unit 3'):
                rows.append(dict(unit=u, exit_px=SL, exit_ts=ft, exit_reason='MALFORMED - stop on wrong side of fill', R=-1.0, R_card=-1.0))
            return rows, Rr, 'MALFORMED'
        return [dict(unit='All', exit_px='', exit_ts='', exit_reason='MALFORMED - stop on wrong side of fill; not taken', R=0.0, R_card=0.0)], Rr, 'SKIPPED_MALFORMED'
    if Rr < min_risk * Rc:
        return [dict(unit='All', exit_px='', exit_ts='', exit_reason=f'MICRO-R - realised risk {Rr:.1f} < {min_risk:.2f} x card R {Rc:.1f}; not taken', R=0.0, R_card=0.0)], Rr, 'SKIPPED_MICRO_R'
    sside, tside = ('dn', 'up') if L else ('up', 'dn')
    be_rule = str(c.be_rule) if be_mode == 'card' else {'tp1': 'BE_ON_TP1', 'none': 'NONE'}[be_mode]
    timestop = str(c.runner_rule) == 'SESSION_CLOSE_TIMESTOP'
    tp1t = feed.touch(ft, T[0], tside) if T[0] is not None else None
    tp2t = feed.touch(ft, T[1], tside) if T[1] is not None else None
    slt = feed.touch(ft, SL, sside)
    be_lvl = fp + s * 0.2 * Rr
    be_arm = None
    if be_rule == 'BE_ON_TP1' and tp1t is not None and (slt is None or tp1t <= slt): be_arm, be_lvl = tp1t, fp
    elif be_rule == 'BE_0.2R_ON_TP2' and tp2t is not None and (slt is None or tp2t <= slt): be_arm = tp2t
    def exit_unit(i):
        tgt = T[i]; tt = feed.touch(ft, tgt, tside) if tgt is not None else None
        cand = []
        if tt is not None: cand.append((tt, tgt, f'TP{i+1} reached' if i < 2 else 'runner target reached'))
        if i == 2 and timestop:
            cl, clt = feed.session_close(es); cand.append((clt, cl, 'card runner time-stop at entry-session close'))
        if i >= 1 and be_arm is not None:
            bt = feed.touch(be_arm, be_lvl, sside)
            if bt is not None: cand.append((bt, be_lvl, f'BE trail hit ({be_rule})'))
        if slt is not None: cand.append((slt, SL, 'stopped out'))
        cand = [x for x in cand if x[0] is not None]
        if not cand:
            cl, clt = feed.last(); return clt, cl, 'unresolved at end of data - MTM'
        cand.sort(key=lambda x: x[0]); return cand[0]
    for i, u in enumerate(('Unit 1', 'Unit 2', 'Unit 3')):
        et, ep, er = exit_unit(i)
        rows.append(dict(unit=u, exit_px=round(ep, 2), exit_ts=et, exit_reason=er,
                         R=round(s * (ep - fp) / Rr, 3), R_card=round(s * (ep - E) / Rc, 3)))
    return rows, Rr, 'FILLED'

# ---------------------------------------------------------------- run
def run(cards, feed, policy, open_hhmm, cutoff_hhmm, be_mode, same_session, min_risk=0.25, malformed='skip'):
    out = []
    for _, c in cards.iterrows():
        base = dict(card_id=c.card_id, report_date=c.report_date, strategy=c.strategy, family=c.get('family', ''),
                    direction=c.direction, entry_mode=c.entry_mode, entry=c.entry, stop=c.stop, tp1=c.tp1, tp2=c.tp2, tp3=c.tp3,
                    card_R_points=c.card_R_points, policy=policy, source=c.get('source', ''))
        if bool(c.get('suppressed', False)):
            out.append(dict(**base, fill_status='SUPPRESSED', unit='All', R=0.0, R_card=0.0)); continue
        if num(c.entry) is None or num(c.stop) is None:
            out.append(dict(**base, fill_status='UNPRICED', unit='All', R=0.0, R_card=0.0)); continue
        ent = find_entry(feed, c, policy, open_hhmm, cutoff_hhmm, same_session)
        if ent['status'] != 'FILLED':
            out.append(dict(**base, fill_status=ent['status'], entry_session=ent.get('session'), fill_reason=ent.get('reason'),
                            unit='All', R=0.0, R_card=0.0)); continue
        rows, Rr, st = resolve(feed, c, ent, be_mode, min_risk, malformed)
        for r in rows:
            out.append(dict(**base, fill_status=st, entry_session=ent['session'], entry_rule=ent['rule'], fill_reason=ent.get('reason',''),
                            fill_ts=ent['fill_ts'], fill_px=round(ent['fill_px'], 2), R_points=round(Rr, 2),
                            risk_vs_card=round(Rr / abs(num(c.entry) - num(c.stop)), 3), **r))
    led = pd.DataFrame(out); led['family'] = led['family'].fillna(''); led['direction'] = led['direction'].fillna('n/a')
    summ = led.groupby(['card_id', 'report_date', 'strategy', 'family', 'direction', 'policy'], as_index=False).agg(
        fill_status=('fill_status', 'first'), entry_rule=('entry_rule', 'first') if 'entry_rule' in led else ('fill_status', 'first'),
        fill_ts=('fill_ts', 'first') if 'fill_ts' in led else ('fill_status', 'first'),
        fill_px=('fill_px', 'first') if 'fill_px' in led else ('fill_status', 'first'),
        R_points=('R_points', 'first') if 'R_points' in led else ('R', 'first'),
        risk_vs_card=('risk_vs_card', 'first') if 'risk_vs_card' in led else ('R', 'first'),
        units=('unit', 'count'), blended_R=('R', 'mean'), blended_R_card=('R_card', 'mean'))
    summ['blended_R'] = summ.blended_R.round(3); summ['blended_R_card'] = summ.blended_R_card.round(3)
    return led, summ

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--cards', required=True); ap.add_argument('--data', required=True); ap.add_argument('--out', required=True)
    ap.add_argument('--policy', default='band0845', choices=['card', 'midnight', 'usopen', 'band0845'])
    ap.add_argument('--open', default='09:00', help='asset session open, broker HH:MM (card policy floor)')
    ap.add_argument('--cutoff', default='23:00', help='last time an unfilled order may fill, broker HH:MM')
    ap.add_argument('--be', default='card', choices=['card', 'tp1', 'none'])
    ap.add_argument('--min-risk', type=float, default=0.25, help='skip fills whose realised risk < this fraction of card R')
    ap.add_argument('--malformed', default='skip', choices=['skip','stop'], help='stop-on-wrong-side fills: skip (0R) or stop (-1R)')
    ap.add_argument('--same-session', action='store_true', help='enter on report_date itself rather than the next session')
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    cards = pd.read_csv(a.cards); feed = Feed(load(a.data))
    led, summ = run(cards, feed, a.policy, a.open, a.cutoff, a.be, a.same_session, a.min_risk, a.malformed)
    led.to_csv(f'{a.out}/ledger.csv', index=False); summ.to_csv(f'{a.out}/summary.csv', index=False)
    f = summ[summ.fill_status == 'FILLED']
    print(f'policy={a.policy} be={a.be} open={a.open} cutoff={a.cutoff} | cards {len(summ)} | filled {len(f)} '
          f'| W/L {(f.blended_R>0).sum()}/{(f.blended_R<0).sum()} | TOTAL R {summ.blended_R.sum():+.2f} '
          f'| card-basis {summ.blended_R_card.sum():+.2f}')
    print(summ.fill_status.value_counts().to_string())

if __name__ == '__main__':
    main()
