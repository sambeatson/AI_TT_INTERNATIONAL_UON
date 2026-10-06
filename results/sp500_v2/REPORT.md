# S&P 500: did QA plus real-data card rebuilding change the outcome?

57 report dates (11 May to 31 Jul 2026), one baseline card set and three independent regeneration draws.
Every figure below is reproducible with:

```
python engine/arm_grid.py --baseline cards/baseline/sp500/cards_baseline_sp500.csv \
  --draws cards/regenerated/sp500_regen2/cards_regen_draw{1,2,3}.csv \
  --data data/raw/US500_p_M15.csv --trust qa/regen_20260906_qa1/trust_scores.csv --out results/sp500_v2
```

## Short answer

**No, not detectably.** Rebuilding the cards from the QA feedback and the real prior-day data changed
*which* cards exist, a lot. It did not move the trading outcome by an amount distinguishable from
noise at 57 dates. The one consistent difference is at the US cash open, where all three draws beat
the baseline. Even there the 95% interval on the gain runs from about −17R to +28R.

## What was done

| step | what | where |
|---|---|---|
| 1 | Original report cards scored against real data | `cards/baseline/sp500/cards_baseline_sp500.csv` (168 cards; reproduces the 159-card fixture exactly) |
| 2 | Original cards re-scored at the altered entry timings | `runs/baseline/*` |
| 3 | Every report quality-assured on Trust Score v3.7 | `qa/regen_20260906_qa1/` (57 score files, 57 feedback files, `trust_scores.csv`) |
| 4 | Cards rebuilt from QA feedback plus real data to 23:59 the night before, three independent draws | `cards/regenerated/sp500_regen2/draw{1,2,3}/`, registries `cards_regen_draw{k}.csv` |
| 5 | Rebuilt cards scored at midnight UK, 07:00 UK and US open (plus card anchor and the band0845 reference) | `runs/draw{k}/*` |
| 6 | Comparison | `MASTER.csv`, `DRAWS.csv`, `PANEL.csv`, `equity/*.png` |

Leak control: each regeneration session saw only the report, its QA feedback, a level file computed from
bars strictly before D, and price, VIX and news slices ending at D−1. Results, raw feeds and full-data lint
were moved out of the repository for the whole run (`qa/gold_regen_qa1/QUARANTINE.md`). Four sessions
that saw something they should not have, and fourteen killed by a usage limit, were set aside and re-run
(`cards/regenerated/sp500_regen2/RUN_LOG.md`).

## A timing correction that affects earlier results

The reports state which session they are for ("Report dated for Monday 11 May 2026 session"; "Forward
date: Tuesday 16 June"). The scoring default inherited from `docs/HANDOVER_METHOD.md` entered every card
on the session *after* the report date, one day late. Run 1 (`regen_20260906_qa1`) and the gold baseline
were scored that way. Here the **primary timing is the report's own session** (`--same-session`); the
one-day-late timing is kept as `next` so the numbers line up with run 1.

The baseline alone moves materially: card-anchor total R is **−7.0** on the correct session against
**−15.9** one day late.

## Main result: correct session, totals in R (0.25% risk per card)

| entry timing | BE rule | baseline | draw 1 | draw 2 | draw 3 | draws beating baseline |
|---|---|---:|---:|---:|---:|---:|
| card anchor (09:00 broker) | card | −7.0 | −7.5 | −4.5 | −8.5 | 1 of 3 |
| card anchor | stop to entry at TP1 | −6.2 | −4.8 | −1.0 | −6.2 | 3 of 3 |
| midnight UK | card | −11.0 | −11.3 | −10.7 | −11.5 | 1 of 3 |
| midnight UK | TP1 | −10.3 | −10.4 | −8.8 | −10.6 | 1 of 3 |
| 07:00 UK | card | −6.2 | −7.5 | −4.5 | −8.5 | 1 of 3 |
| 07:00 UK | TP1 | −6.3 | −4.8 | −1.0 | −6.2 | 3 of 3 |
| **US open (14:30 UK)** | card | −2.5 | **+0.5** | **+5.2** | **+0.4** | **3 of 3** |
| **US open** | TP1 | +2.3 | **+4.2** | **+7.6** | **+3.7** | **3 of 3** |
| band0845 (reference only) | card | −4.5 | −6.6 | −5.0 | −9.0 | 0 of 3 |

The regenerated cards all anchor at 09:00 broker, which is 07:00 UK, so "card anchor" and "07:00 UK" are
the same test for them.

Daily-block bootstrap on the gain (dates resampled, 5,000 draws), US open, card BE rule: draw 1 +3.0R
[−18.4, +24.5], draw 2 +7.6R [−12.0, +27.8], draw 3 +2.9R [−16.8, +22.3]. The probability that the gain is
≤ 0 is 0.22 to 0.39. No cell in the grid has an interval that excludes zero. Full table: `MASTER.csv`.

## Why the totals barely move even though the cards changed a lot

| | baseline | draw 1 | draw 2 | draw 3 |
|---|---:|---:|---:|---:|
| live cards (not suppressed) | 146 | 87 | 93 | 92 |
| dates with no live card | 0 | 5 | 6 | 5 |
| fill rate of live cards (07:00 UK) | 66% | 69% | 67% | 69% |
| mean R per filled card (07:00 UK) | −0.07 | −0.12 | −0.07 | −0.14 |
| mean R per filled card (US open) | −0.03 | +0.01 | +0.09 | +0.01 |
| static-lint DUD cards | 3 | 0 | 0 | 0 |

- **About 40% fewer trades.** On real ATR, many of the reports' tight stops fail the 0.3×ATR risk floor,
  and the real 25-day boundaries rarely confirm a break. Suppressed cards earn 0R, so they pull the total
  toward zero in both directions.
- **The regime call moved from TREND to TRANSITION** on most dates. The baseline had 30 trend-pullback
  (3A) cards; each draw has 11 to 13. The rebuilt cards trade breakouts of the daily pivot instead.
- **Trade 1 never flipped direction.** The rebuilt majority call differs from the report on 19 of 57
  dates, but every one of those is a switch between live and suppressed, never LONG to SHORT.
- **The rebuilt cards are construction-clean.** Zero static-lint DUDs against three in the original set.
  Clean construction did not translate into better outcomes, which echoes the Stage 1 finding that Card
  Integrity is uncorrelated with the Trust Score.

## Does the QA score predict anything?

Spearman correlations across the 57 dates (07:00 UK entry, card BE rule):

| | original cards' R | rebuilt cards' R (mean of 3 draws) | gain from rebuilding |
|---|---:|---:|---:|
| Trust Score total | 0.01 (p 0.95) | 0.27 (p 0.04) | 0.16 (p 0.23) |
| C3 accuracy and evidence | −0.01 (p 0.95) | 0.26 (p 0.05) | 0.21 (p 0.11) |

- **The Trust Score says nothing about how the original cards traded.**
- It is weakly associated with how the *rebuilt* cards traded. That fits a reading where a higher-quality
  report carries a better narrative and regime call into the rebuild once its numbers are replaced by
  real ones. But this is one significant result among six tests and should be treated as a lead, not a
  finding.

By override, mean R per date:

| override | dates | original | rebuilt | gain |
|---|---:|---:|---:|---:|
| none | 12 | +0.09 | +0.43 | +0.34 |
| restriction breach | 32 | −0.18 | −0.13 | +0.04 |
| hallucinated source | 13 | −0.19 | −0.59 | −0.40 |

Reports with a fabricated source are the ones where rebuilding helped least. That is consistent with the
rebuild inheriting the report's narrative inputs, sentiment in particular, which is carried over
unverified.

## Stability of the rebuild

Trade 1's state (LONG, SHORT or suppressed) is identical across all three draws on 52 of 57 dates. The
five that differ sit at the 0.25 score gate, where one judgement call (usually the short-term technical
signal, or a cross-asset leg that could not be verified) decides it. Within an asset the procedure is
reproducible; the spread across draws (about 4R at US open) is smaller than the spread across dates.

## QA Stage 1 summary (S&P, 57 reports)

Mean Trust Score 60.1 (Low 30, Moderate 23, High 3, Very Low 1). Mean C3 (accuracy and evidence)
1.65 of 5. Overrides: restriction breach 32, hallucinated source 13, none 12. The commonest restriction
breach is module codes and bracketed variable names left in the report body. The commonest accuracy
failure is building levels on the wrong prior session (D−2 or an earlier week) and understating ATR.

## Limitations

1. **57 dates is small.** The intervals are about ±20R. A real effect of a few R in total would not be
   detectable.
2. **Sentiment and two cross-asset legs were carried, not verified.** Sessions had VIX but not USDX or
   DAX, and the news itself was not re-read. Those components sit near the 0.25 gate on several dates and
   are the main source of disagreement between draws.
3. **Holiday sessions.** The level files for 26 May and 6 July take their daily pivots from short CFD
   holiday sessions (Memorial Day, 3 July). Sessions handled this by judgement; it is logged, not fixed.
4. **Exposure incidents** (logged in RUN_LOG): four outputs superseded for possible sight of post-D data;
   two minor directory listings with no prices kept; twenty early draw-1 sessions ran on a shared scratch
   folder without reporting a collision.
5. **The rule-book is ambiguous in places** that the draws resolved differently. Examples: which pivot
   counts as "nearest support", the "whichever is tighter" stop clause, and the 3C breakout side under
   TRANSITION. Each card records its reading in `rationale`.
