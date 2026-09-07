# Stage 1 QA roll-up — US500, run regen_20260906_qa1

54 reports scored, one independent session per report date, each session limited to the report for D,
reports dated before D, the D-1 data slices, that date's static linter rows and the fixed prompt stack.
No session saw `results/`, the market-relative lint, the raw data, any later report or slice, or any other
session's output. Outputs: `<D>_trust_score.md`, `<D>_feedback.md`, and `trust_scores.csv`.

## Headline

| | |
|---|---|
| Reports scored | 54 (159 cards) |
| Trust Score | mean **60.5**, median 58, range 41 (16 Jul) – 77 (25 May) |
| Bands | High 3 · Moderate 22 · **Low 29** · none Very High or Very Low |
| Overrides | restriction breach 31 · fabricated source 12 · none 11 |
| Card Integrity | mean **96.1**, min 80.0, exactly 100 on 26 dates |
| Static defects | **3 DUD**, 40 WARN across 159 cards |

The 3 duds reproduce the count documented in `docs/HANDOVER_METHOD.md` for this sample, which is an
independent check that the static linter and the card registry agree with the original pass.

## Category profile

| Category | Max | Mean level | Distribution (level:count) |
|---|---|---|---|
| C1 Prompt adherence | 20 | 2.61 | 1:4 2:19 3:25 4:6 |
| C2 Structural alignment | 20 | 3.94 | 1:2 2:1 3:4 4:38 5:9 |
| **C3 Accuracy & evidence** | 25 | **1.67** | **0:12** 1:3 2:30 3:9 |
| C4 Reasoning & judgment | 20 | 3.33 | 3:36 4:18 |
| C5 Currency & transparency | 15 | 3.13 | 2:3 3:41 4:10 |

Structure is the strongest category and accuracy by far the weakest. The reports are well-formed
containers holding numbers that do not reconcile. C3 is zero on the 12 dates where a fabricated-source
override fired.

## Recurring failures (dates on which each appears, of 54)

| Failure | Dates |
|---|---|
| A card that the rules require to be SUPPRESSED is issued anyway | 54 |
| No wide-stop flag where R exceeds 1×ATR | 49 |
| RSI2 does not reproduce from the report's own closes | 45 |
| An entry sits on the wrong side of the D-1 close | 43 |
| §6 OHLC values outside the CFD-vs-cash basis tolerance | 40 |
| ATR(14) never stated, or materially wrong | 36 |
| Pivots built on a stale session or the wrong week | 31 |
| Card built on the wrong regime branch | 11 |
| Thesis invalidation set equal to the stop | 11 |
| As-of session is D-2 rather than D-1 | 9 |

## What this means for Stage 2

Four observations bear on how regeneration should be framed.

1. **The arithmetic is usually right; the inputs are wrong.** On most dates the pivot ladders reproduce
   to the cent from the report's own stated H/L/C, and several sessions verified the floor-pivot identity
   R2−P = P−S2 holds. The errors enter through the price table and the choice of session, not the formulas.
   Correcting §6 and the pivot basis would fix most downstream levels mechanically.
2. **RSI2 is a systematic arithmetic failure, not a basis difference.** It fails against the reports' own
   closes, so it cannot be explained by the CFD-versus-cash gap. Two sessions independently found the same
   cross-report contradiction on 13 and 14 July, where identical closes carry different RSI2 columns.
3. **Card defects are mostly invisible to the static linter.** Card Integrity averages 96.1 and the linter
   finds only 3 duds, yet every date carries at least one card that departs from its fixed construction
   rule — the wrong regime branch, the wrong retracement level, a missing suppression, an invalidation
   collapsed onto the stop. The linter tests internal geometry; it cannot test whether the right recipe
   was applied. Stage 2's linter gate is necessary but not sufficient.
4. **The restriction breaches are mechanical and easy to remove.** 31 dates leak module codes, bracketed
   variable names or framework identifiers into the report body. That alone caps a report at Moderate
   regardless of its content, and several reports would otherwise have scored High.

## Two decisions this roll-up puts to the operator

- **Number of regeneration draws.** The statistical plan asks for 3–5 per date. Three draws is 162 sessions.
- **Whether to edit the M-modules between Stage 1 and Stage 2.** The failures above are concentrated and
  addressable in `M3` (indicator and pivot arithmetic, stating ATR) and `M5` (suppression gates, regime
  fork, retracement levels). Editing them tests "QA feedback plus a corrected prompt"; leaving them fixed
  tests "QA feedback alone", which is what `docs/LEAKAGE_PROTOCOL.md` §5 describes as the experiment.
  Either is defensible, but they answer different questions and the choice must be recorded before Stage 2.
