# US500 — baseline card set scored, five entry policies

Asset: US500 (S&P 500 CFD, M15, broker UTC+3). Data: `data/raw/US500_p_M15.csv`, 1 Apr – 3 Sep 2026,
112 sessions, 10,228 bars, volume peak 16:30 broker (US cash open) — offset verified with `engine/tz_check.py`.
Cards: `cards/baseline/cards_baseline.csv`, 159 cards over 54 report dates (11 May – 31 Jul 2026), 20 suppressed.
Engine: `engine/resolver.py --open 09:00 --cutoff 23:00`, `--min-risk 0.25`, `--malformed skip`, `--be card`
(and `--be tp1` for the variant). Sizing for the equity chart: USD 1,000,000 account, fixed 2,500 risk per card (0.25%).

Regression fixture reproduced: band0845 TOTAL R **−9.49**. All five ledgers and summaries are byte-identical
to the shipped `results/baseline_*` files.

## Headline

| policy | filled | fill rate | W/L | win rate | total R | card-basis R | final equity | max DD |
|---|---|---|---|---|---|---|---|---|
| band0845 | 71 | 44.7% | 22/49 | 31.0% | **−9.49** | −26.29 | 976,280 | −7.4% |
| band0845 `--be tp1` | 71 | 44.7% | 26/45 | 36.6% | −5.03 | −22.41 | 987,415 | −6.6% |
| card | 79 | 49.7% | 24/55 | 30.4% | −13.87 | +9.00 | 965,320 | −6.6% |
| usopen | 78 | 49.1% | 21/57 | 26.9% | −14.48 | +7.83 | 963,800 | −7.2% |
| midnight | 79 | 49.7% | 23/56 | 29.1% | −17.73 | +6.06 | 955,665 | −6.2% |

Fill-status counts, band0845: FILLED 71 · NO FILL 66 · SUPPRESSED 20 · NO TRIGGER 2.
Literal policies additionally skip SKIPPED_MALFORMED 8–9 and SKIPPED_MICRO_R 7–9 (the dud screen and band
policy absorb these).

## By month and family (total R)

| policy | May | Jun | Jul | Trade 1 | Trade 2 | Trade 3 | Trade 3A | Trade 3B | Trade 3C |
|---|---|---|---|---|---|---|---|---|---|
| band0845 | +19.28 | −16.52 | −12.24 | −6.82 | −2.67 | +0.48 | +0.71 | 0 | −1.18 |
| band0845 `--be tp1` | +20.28 | −13.87 | −11.44 | −6.11 | −1.07 | +0.41 | +2.91 | 0 | −1.18 |
| card | +11.07 | −15.77 | −9.18 | −5.70 | −2.88 | +0.35 | −4.72 | 0 | −0.93 |
| usopen | +13.43 | −16.71 | −11.20 | −8.65 | −5.46 | −1.00 | +1.71 | 0 | −1.09 |
| midnight | +5.03 | −12.05 | −10.72 | −6.31 | −8.39 | +0.48 | −3.06 | 0 | −0.46 |

## band0845 detail

Entry branch: IN BAND 28 · WAITED for return to entry 30 · RECOVERY to entry−0.5R 13.
Unit exits (213 units): stopped out 137 · TP1 23 · runner time-stop at session close 22 · TP2 13 ·
OPEN_MTM at end of data 9 · runner target 5 · BE trail 4.
Realised risk below 0.5× card R: 10 cards (min ratio 0.253; none below the 0.25 guard).

Best five (blended R): 2026-05-19_Trade_2 +7.66 · 2026-05-19_Trade_1 +5.86 · 2026-05-19_Trade_3A +3.42 ·
2026-07-24_Trade_2 +2.55 · 2026-05-11_Trade_2 +1.38.
Worst: 20 cards at exactly −1.00 (all three units stopped; first five by date: 2026-05-18_Trade_3C,
2026-06-02_Trade_1, 2026-06-02_Trade_2, 2026-06-03_Trade_2, 2026-06-03_Trade_3A).

## Defects (market linter, post-hoc, `qa/baseline/lint_baseline.csv`)

77 of 139 non-suppressed cards carry at least one flag; 3 duds (2 × DUD_TP1_SIDE, 1 × DUD_TP2_ORDER).
STALE_ANCHOR 25 · WARN_R_TINY 17 · MISPLACED_STOP 15 · MISPLACED_LIMIT 11 · WARN_TP3_ORDER 10 ·
WARN_TARGET_FAR 10 · MALFORMED_FILL 3 · WARN_R_HUGE 3 · WARN_DUPLICATE 2.
Static (leak-free) lint: 3 duds, 124 clean of 139; identical to `qa/baseline/lint_baseline_static.csv`.

## Files

`results/baseline_{band0845,band0845_betp1,card,usopen,midnight}/{ledger,summary}.csv`,
`results/compare/equity_baseline_policies.png` (+ `_stats.csv`).
