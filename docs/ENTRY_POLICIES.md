# Entry policies and management variants

All times broker (UTC+3 in BST = UK clock + 2). Entry session = the session AFTER report_date unless the
card states same-session execution (`--same-session`). Every filled position keeps the card's original
stop; realised R = |fill − stop|. Fills whose realised risk is below 25% of card R are not taken
(`--min-risk 0.25`). Fills where the stop lands on the wrong side of the entry are not taken (`--malformed skip`).

| Policy | Monitoring opens | Fill rule | Purpose |
|---|---|---|---|
| `card` | the card's own anchor (translated to broker time; floored at the asset session open) | literal: market at anchor open; limit/stop on first touch; conditional on confirming close then next anchor | "as written" |
| `midnight` | 02:00 broker (00:00 UK) | literal | CFD-style, orders resting from the day boundary |
| `usopen` | 16:30 broker (14:30 UK, US cash open) | literal | US-open entry; the anchor most cards' logic assumes |
| `band0845` | 08:45 broker | band: in [0, +0.75R] improvement → market; worse → wait for return to entry; beyond → wait for recovery to entry −0.5R; dud screen first | disciplined, no-chase |

Cut-off (last time an unfilled order may fill): equities/indices/energy/metals/crypto **23:00 broker**;
FX **18:00 broker** with monitoring open **09:00** (`--open 09:00 --cutoff 18:00`).

## Management variants (`--be`)
| Flag | Behaviour |
|---|---|
| `card` | each card's own rule (`be_rule` column: NONE / BE_0.2R_ON_TP2 / BE_ON_TP1) |
| `tp1` | force breakeven on the TP1 fill for Units 2–3 (the 28 May improvement) |
| `none` | never move the stop |

Runner (Unit 3): honours `SESSION_CLOSE_TIMESTOP` when the card says so; otherwise traces to target/stop.

## Baseline results (S&P 500, 159 cards, shipped US500_p_M15.csv 1 Apr–3 Sep) — regression reference
| policy | filled | W/L | total R |
|---|---|---|---|
| band0845 | 71 | 22/49 | **−9.49** |
| band0845 `--be tp1` | 71 | 26/45 | −5.03 |
| card | 79 | 24/55 | −13.87 |
| usopen | 78 | 21/57 | −14.48 |
| midnight | 79 | 23/56 | −17.73 |

The BE-on-TP1 variant beats card management by +4.46R on 16 affected cards
(daily-block bootstrap 95% CI [+1.19, +7.99], Wilcoxon p = 0.017). It is the one management change
with statistical support and should be carried as a standing variant.

## Deprecated (tested, dominated, kept in results/baseline for the record)
06:45 next-session pure rebase (−29.10R); 06:45 market-if-better / −0.5R (−18.79R).
