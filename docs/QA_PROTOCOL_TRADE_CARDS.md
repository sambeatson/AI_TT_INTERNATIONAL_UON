# QA protocol — Trust Score v3.7 applied to trade-card research reports

The supplied framework (`docs/AI_Output_Trust_Score_Framework_v3.7.pdf`) scores outputs of the
Variables / Research Standard / Methodology / Output Structure architecture. These reports use the
same architecture under different module names (M1 Variables · M2 Research Standard · M3 Technical ·
M4 Output Structure · M5 Strategies). The five categories, weights, 0–5 rubric and multipliers are used
**unchanged**. Only the anchors are mapped.

## Category anchors for these reports
| # | Category (max) | Anchored to | What the reviewer checks |
|---|---|---|---|
| 1 | Prompt adherence (20) | M1 Variables block | asset, coverage window, anchor time, sources list, currency, restrictions honoured |
| 2 | Structural alignment (20) | M4 output structure §1–§21 | all sections present and ordered; OHLC+RSI2 table is a table; two charts; §21a/b/c/d present |
| 3 | Accuracy & evidence (25) | M2 Research Standard | OHLC triangulated across the named sources and reconciled; every quantitative claim sourced; RSI2 arithmetic shown; numbers reconcile across §2, §4, §21; no fabricated URL/source |
| 4 | Reasoning & judgment (20) | M3 technical + M5 strategy logic | directional score derivation traceable; cross-asset mechanism not just correlation; regime call consistent with levels; **card construction** (see §Card Integrity) |
| 5 | Currency & transparency (15) | M2 data-recency + no-synthesis protocol | every data point dated; anchor-override caveats present; assumptions explicit; forecast is one calibrated sentence; restrictions (no synthesis, no invented sources) honoured |

Override rules apply as written: a fabricated source caps the report at Low Trust and zeros Category 3;
a breached restriction caps at Moderate Trust and drops Category 1 one level.

## Card Integrity — a SEPARATE deterministic score (not folded into the 100)
Because card construction was the dominant failure in the baseline (45 of 159 cards), it gets its own
hard score so that it is neither averaged away nor double-counted. It is produced by `engine/linter.py`
in **static mode** (no market data — leak-free) and is reported alongside the Trust Score:

```
Card Integrity = 100 - 40*(#DUD flags) - 10*(#WARN flags), floored at 0, per card; report-level = mean
```
DUD: stop side, TP1 side, TP2 order, zero R. WARN: TP3 order, R tiny (<0.3 ATR), R huge (>3 ATR),
target far (>2.5 ATR), duplicate. The reviewer copies the linter output into the QA sheet verbatim and
uses it to write the card-specific feedback. The reviewer does not re-derive it by hand.

## Leak-safety of the review
The reviewer scores with the report, the reports before it, the data slice to D-1, and the static
linter. Nothing else. Category 3 accuracy checks compare the report's stated D-1 OHLC to the slice — that
is permitted and is the main accuracy test. The reviewer never opens `results/`.

## Output per report (`qa/<run_id>/<D>_trust_score.md`)
1. The Section 7 checklist table, every row filled (notes, evidence location, 0–5).
2. Category roll-up table: level, multiplier, points, one-line justification.
3. Total, band, override check.
4. Card Integrity table (linter rows).
5. **Feedback** (`<D>_feedback.md`): numbered, specific, actionable, and *only* things the regeneration
   agent can act on without new research. For each card: what is wrong with the level construction and
   what rule it violates. For the report: which data reconciliation failed and which section is missing.
   No commentary on whether the trade "would have worked" — the reviewer does not know and must not guess.

## Roll-up (`qa/<run_id>/trust_scores.csv`)
`report_date, file, c1, c2, c3, c4, c5, total, band, override, card_integrity, n_cards, n_duds, n_warns`
