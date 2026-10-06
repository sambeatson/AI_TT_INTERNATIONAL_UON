"""arm_grid.py - score every arm (baseline + K regeneration draws) on the full timing grid and
build one MASTER table, the per-date panel and the equity overlays for the write-up.

  python engine/arm_grid.py --baseline cards/baseline/sp500/cards_baseline_sp500.csv \
      --draws cards/regenerated/sp500_regen2/cards_regen_draw1.csv ...draw2.csv ...draw3.csv \
      --data /path/US500_p_M15.csv --trust qa/regen_20260906_qa1/trust_scores.csv \
      --out results/sp500_v2

GRID   timing  same = enter on the session the report is dated for (the report's own target session;
                      PRIMARY) | next = the session after (the HANDOVER_METHOD default, kept so the
                      numbers line up with run 1)
       policy  card | midnight (00:00 UK) | uk0700 | usopen | band0845 (reference only)
       be      card (each card's own break-even rule) | tp1 (stop to entry once TP1 fills)

MASTER.csv, one row per (arm, timing, policy, be):
  n_dates, n_cards, n_live (not suppressed), n_filled, fill_rate (= filled / live), total_R,
  mean_R_filled, win_rate_filled; for draws also diff_vs_base (total R), a daily-block bootstrap
  95% CI on that difference (dates resampled with replacement, 5,000 draws) and p_le0 = share of
  bootstrap differences <= 0. Effective N is the number of report dates, not cards.
DRAWS.csv  per grid cell: mean total R across draws, min/max, share of draws beating the baseline
           (the STATS_PLAN rule: a change counts only if >= 60% of draws beat the baseline).
PANEL.csv  per date (primary cell same/card/be=card): trust-score columns, baseline R, each draw's
           R, mean draw R and the difference - the input for 'does the QA score predict the gain'.
Non-filled and suppressed cards earn 0R, so total R mixes 'traded well' with 'traded less':
read total_R next to fill_rate and mean_R_filled, never alone.
"""
import argparse, os, subprocess, sys, numpy as np, pandas as pd

POLICIES = ['card', 'midnight', 'uk0700', 'usopen', 'band0845']
TIMINGS = ['same', 'next']
BES = ['card', 'tp1']
HERE = os.path.dirname(os.path.abspath(__file__))

def score(cards, data, out, timing, policy, be):
    os.makedirs(out, exist_ok=True)
    cmd = [sys.executable, os.path.join(HERE, 'resolver.py'), '--cards', cards, '--data', data,
           '--policy', policy, '--be', be, '--out', out] + (['--same-session'] if timing == 'same' else [])
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL)
    return pd.read_csv(os.path.join(out, 'summary.csv'))

def by_date(s, dates):
    s = s.copy(); s['blended_R'] = pd.to_numeric(s.blended_R, errors='coerce').fillna(0)
    return s.groupby('report_date')['blended_R'].sum().reindex(dates).fillna(0)

def block_ci(diff, n=5000, seed=7):
    rng = np.random.default_rng(seed); k = len(diff)
    boots = np.array([diff[rng.integers(0, k, k)].sum() for _ in range(n)])
    return np.percentile(boots, [2.5, 97.5]), float((boots <= 0).mean())

def row(s, live_ids):
    s = s.copy(); s['blended_R'] = pd.to_numeric(s.blended_R, errors='coerce').fillna(0)
    f = s[s.fill_status == 'FILLED']; live = s[s.card_id.isin(live_ids)]
    return dict(n_dates=s.report_date.nunique(), n_cards=len(s), n_live=len(live), n_filled=len(f),
                fill_rate=round(len(f) / len(live), 3) if len(live) else np.nan,
                total_R=round(s.blended_R.sum(), 3),
                mean_R_filled=round(f.blended_R.mean(), 3) if len(f) else np.nan,
                win_rate_filled=round((f.blended_R > 0).mean(), 3) if len(f) else np.nan)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--baseline', required=True); ap.add_argument('--draws', nargs='+', required=True)
    ap.add_argument('--data', required=True); ap.add_argument('--trust', default=None)
    ap.add_argument('--out', required=True)
    ap.add_argument('--asset', default='US500', help='label used in the equity-chart titles')
    a = ap.parse_args()
    arms = [('baseline', a.baseline)] + [(f'draw{i + 1}', p) for i, p in enumerate(a.draws)]
    reg = {nm: pd.read_csv(p) for nm, p in arms}
    live = {nm: set(r.loc[~r.suppressed.astype(str).str.lower().isin(['true', '1']), 'card_id']) for nm, r in reg.items()}
    dates = sorted(set(reg['baseline'].report_date))
    for nm, r in reg.items():
        miss = sorted(set(dates) - set(r.report_date))
        if miss: raise SystemExit(f'{nm} missing dates: {miss}')

    master, draws_rows, keep = [], [], {}
    for t in TIMINGS:
        for p in POLICIES:
            for be in BES:
                cell = f'{t}_{p}_be{be}'; base = None; dR = []
                for nm, path in arms:
                    s = score(path, a.data, os.path.join(a.out, 'runs', nm, cell), t, p, be)
                    r = dict(arm=nm, timing=t, policy=p, be=be, **row(s, live[nm]))
                    dd = by_date(s, dates)
                    if nm == 'baseline': base = dd
                    else:
                        diff = (dd - base).values; ci, ple = block_ci(diff)
                        r.update(diff_vs_base=round(diff.sum(), 3), ci_lo=round(ci[0], 2), ci_hi=round(ci[1], 2), p_le0=round(ple, 3))
                        dR.append(diff.sum())
                    master.append(r); keep[(nm, cell)] = dd
                    print(f'{cell:24s} {nm:9s} total {r["total_R"]:+8.2f}  filled {r["n_filled"]:3d}/{r["n_live"]:3d}', flush=True)
                tot = [m['total_R'] for m in master[-len(arms) + 1:]]
                draws_rows.append(dict(timing=t, policy=p, be=be, baseline_R=master[-len(arms)]['total_R'],
                                       draws_mean_R=round(np.mean(tot), 3), draws_min_R=min(tot), draws_max_R=max(tot),
                                       mean_diff=round(np.mean(dR), 3), share_draws_beating=round(np.mean([x > 0 for x in dR]), 3)))
    os.makedirs(a.out, exist_ok=True)
    pd.DataFrame(master).to_csv(os.path.join(a.out, 'MASTER.csv'), index=False)
    pd.DataFrame(draws_rows).to_csv(os.path.join(a.out, 'DRAWS.csv'), index=False)

    cell = 'same_card_becard'
    panel = pd.DataFrame({'report_date': dates, 'baseline_R': keep[('baseline', cell)].values})
    for nm, _ in arms[1:]: panel[f'{nm}_R'] = keep[(nm, cell)].values
    dcols = [f'{nm}_R' for nm, _ in arms[1:]]
    panel['draws_mean_R'] = panel[dcols].mean(axis=1).round(3); panel['gain'] = (panel.draws_mean_R - panel.baseline_R).round(3)
    if a.trust:
        tr = pd.read_csv(a.trust)[['report_date', 'c1', 'c2', 'c3', 'c4', 'c5', 'total', 'band', 'override']]
        panel = tr.merge(panel, on='report_date', how='right')
    panel.to_csv(os.path.join(a.out, 'PANEL.csv'), index=False)

    eq = os.path.join(a.out, 'equity'); os.makedirs(eq, exist_ok=True)
    for t in TIMINGS:
        for p in POLICIES:
            c = f'{t}_{p}_becard'
            runs = [os.path.join(a.out, 'runs', nm, c, 'summary.csv') for nm, _ in arms]
            subprocess.run([sys.executable, os.path.join(HERE, 'equity.py'), '--runs', *runs, '--labels', *[nm for nm, _ in arms],
                            '--out', os.path.join(eq, f'{c}.png'), '--title', f'{a.asset} cards - {t}-session entry, {p}'],
                           check=True, stdout=subprocess.DEVNULL)
    print(f'wrote {a.out}/MASTER.csv, DRAWS.csv, PANEL.csv, equity/*.png')

if __name__ == '__main__':
    main()
