# FTSE 100: did QA plus real-data card rebuilding change the outcome?

57 report dates (11 May to 31 Jul 2026), one baseline card set and three independent regeneration draws.
Every figure below is reproducible with:

```
python engine/arm_grid.py --baseline cards/baseline/ftse/cards_baseline_ftse.csv \
  --draws cards/regenerated/ftse_regen1/cards_regen_draw{1,2,3}.csv \
  --data data/raw/UK100_p_M15.csv --trust qa/ftse_qa1/trust_scores.csv --out results/ftse_v1 --asset UK100
```

## Short answer

**No, not detectably, and the direction differs from the S&P.**

- At the 07:00 UK anchor the original cards made **+9.4R**. The three rebuilt sets made **−3.0, +2.2 and −0.8R**,
  so none of the three draws beat the baseline. But the baseline's lead rests on three cards: without
  them it is −9.0R, about where the rebuilt sets are without their own best three.
- **At the US cash open the result reverses, as it did for the S&P**: all three draws beat the
  baseline (+2.7, +8.3, +1.8R against −0.7R).
- No interval in the grid excludes zero, apart from the band0845 reference cell (see below).

## What was done

| step | what | where |
|---|---|---|
| 1 | Original report cards scored against real data | `cards/baseline/ftse/cards_baseline_ftse.csv` (171 cards, 152 live; static lint 6 DUD, 15 TP3-order warnings, 5 unpriced) |
| 2 | Original cards re-scored at the altered entry timings | `runs/baseline/*` |
| 3 | Every report quality-assured on Trust Score v3.7 | `qa/ftse_qa1/` (57 score files, 57 feedback files, `trust_scores.csv`, `RUN_LOG.md`) |
| 4 | Cards rebuilt from QA feedback plus real data to 23:59 the night before, three independent draws | `cards/regenerated/ftse_regen1/draw{1,2,3}/`, registries `cards_regen_draw{k}.csv`, `lint/`, `RUN_LOG.md` |
| 5 | Rebuilt cards scored at midnight UK, 07:00 UK and US open (plus card anchor and the band0845 reference) | `runs/draw{k}/*` |
| 6 | Comparison | `MASTER.csv`, `DRAWS.csv`, `PANEL.csv`, `equity/*.png` |

**Leak control.** This was the same as for the S&P. Each regeneration session saw only four things:

- the report;
- its QA feedback;
- a UK100 level file computed from bars strictly before D;
- UK100, USDX, US500, VIX and news slices ending at D−1.

Results, raw feeds and full-data lint were kept out of the repository for the whole run
(`qa/gold_regen_qa1/QUARANTINE.md`). They were restored afterwards, and both regression fixtures
re-verified: US500 band0845 −9.49R, gold −0.59R.

The UK100 cash window is the LSE session, 10:00–18:30 broker (08:00–16:30 London). 25 May was a UK bank
holiday; its level row repeats 22 May.

**Incidents** (all in the two RUN_LOGs):

- A usage limit stopped 20 sessions; none had written output.
- A container recycle wiped the git-ignored slices. Three draw-1 outputs built without them were
  superseded. The slices were rebuilt from history and leak-checked, all affected jobs were re-run, and
  sessions now stop on a missing input.
- About 15 QA and regeneration sessions listed a directory against the rule. They saw filenames only and
  opened nothing.

## Main result: correct session, totals in R (0.25% risk per card)

| entry timing | BE rule | baseline | draw 1 | draw 2 | draw 3 | draws beating baseline |
|---|---|---:|---:|---:|---:|---:|
| card anchor (09:00 broker) | card | +9.4 | −2.1 | +1.6 | −0.5 | 0 of 3 |
| card anchor | stop to entry at TP1 | +8.1 | −0.4 | +2.3 | +3.6 | 0 of 3 |
| midnight UK | card | −9.4 | −10.3 | −0.6 | −7.0 | 2 of 3 |
| midnight UK | TP1 | −8.2 | −6.3 | −0.5 | −2.2 | 3 of 3 |
| 07:00 UK | card | +9.4 | −3.0 | +2.2 | −0.8 | 0 of 3 |
| 07:00 UK | TP1 | +8.1 | −1.2 | +1.2 | +3.3 | 0 of 3 |
| **US open (14:30 UK)** | card | −0.7 | **+2.7** | **+8.3** | **+1.8** | **3 of 3** |
| **US open** | TP1 | +1.6 | +2.6 | +6.9 | +1.5 | 2 of 3 |
| band0845 (reference only) | card | +24.3 | −8.4 | −5.6 | −4.1 | 0 of 3 |

The rebuilt cards anchor at 09:00 broker (07:00 UK) except a few Trade 2 cards armed from the LSE open at
10:00, so "card anchor" and "07:00 UK" are close to the same test.

**Daily-block bootstrap on the gain** (dates resampled, 5,000 draws):

- **07:00 UK, card BE rule:**
  - draw 1: −12.4R [−40.0, +12.7]
  - draw 2: −7.2R [−39.9, +20.7]
  - draw 3: −10.2R [−39.7, +15.5]
- **US open, card BE rule:**
  - draw 1: +3.5R [−18.9, +24.8]
  - draw 2: +9.1R [−13.4, +31.7]
  - draw 3: +2.5R [−20.4, +23.9]
  - probability the gain is ≤ 0: 0.21 to 0.39
- **band0845 is the only cell with an interval near or below zero:**
  - draw 1: [−66.4, −0.3]
  - draws 2 and 3: upper bounds +4.6 and +5.5

  That is a reference policy (08:45 broker with a price band). Its baseline total of +24.3R comes from a
  handful of large runner wins, so it should not be read as a finding.

### The baseline total is three cards

| baseline (07:00 UK) | total | without its 3 best cards |
|---|---:|---:|
| original cards | +9.4 | −9.0 |
| rebuilt, draw 1 / 2 / 3 | −3.0 / +2.2 / −0.8 | −12.1 / −6.9 / −9.9 |

The three are:

| card | R |
|---|---:|
| 29 May 3B | +6.8 |
| 20 May Trade 1 | +6.3 |
| 28 Jul Trade 1 | +5.3 |

These are tight-stop cards whose runner ran several R. Without its three best cards, the original set
loses about as much as the rebuilt sets do. The headline gap at 07:00 UK is a tail event the rebuild
did not reproduce, not a systematic difference. The block bootstrap's width reflects this.

## Why the totals move little even though the cards changed a lot

| | baseline | draw 1 | draw 2 | draw 3 |
|---|---:|---:|---:|---:|
| live cards (not suppressed) | 152 | 75 | 71 | 73 |
| dates with no live card | 0 | 9 | 10 | 9 |
| trend-pullback (3A) cards live | 28 | 2 | 3 | 2 |
| fill rate of live cards (07:00 UK) | 74% | 77% | 76% | 77% |
| mean R per filled card (07:00 UK) | +0.08 | −0.05 | +0.04 | −0.01 |
| mean R per filled card (US open) | −0.01 | +0.06 | +0.19 | +0.04 |
| static-lint DUD cards | 6 | 0 | 0 | 0 |

- **Half the trades.** The rebuilt sets carry 71–75 live cards against 152. On real ATR (often 110–150
  points against the 60–90 the reports implied), many tight stops fail the 0.3×ATR floor. The real
  25-day boundaries also never confirmed a break, so no 3C card went live in any draw.
- **The regime call moved from TREND to TRANSITION** on almost every date. The reports' KER readings
  (often +0.25 to +0.5) did not reproduce: smoothed KER on cash closes was mostly within ±0.15. The
  third card became a suppressed 3C, and Trade 2 became a breakout-side card on daily pivots.
- **Trade 1 never flipped direction.** The rebuilt majority call differs from the report on 20 of 57 dates.
  Every one of those changes is between live and suppressed; none goes from LONG to SHORT.
- **Construction-clean, again with no payoff.** Zero static-lint DUDs against six in the original set.

## Does the QA score predict anything?

Spearman correlations across the 57 dates (07:00 UK entry, card BE rule):

| | original cards' R | rebuilt cards' R (mean of 3 draws) | gain from rebuilding |
|---|---:|---:|---:|
| Trust Score total | 0.04 (p 0.75) | 0.00 (p 0.99) | −0.05 (p 0.70) |
| C3 accuracy and evidence | 0.12 (p 0.36) | 0.13 (p 0.33) | −0.08 (p 0.55) |

**For the FTSE the Trust Score predicts nothing**, neither for the original cards nor for the rebuilt ones.
The weak S&P association between Trust Score and rebuilt-card R (ρ 0.27, p 0.04) does not replicate. That
supports reading the S&P result as a chance finding among multiple tests.

By override, mean R per date:

| override | dates | original | rebuilt | gain |
|---|---:|---:|---:|---:|
| none | 11 | −0.55 | −0.18 | +0.38 |
| restriction breach | 25 | +0.60 | +0.20 | −0.39 |
| hallucinated source | 21 | +0.03 | −0.16 | −0.19 |

The only pattern shared with the S&P is a small one. Rebuilding helps most where the report had no
override and helps least where it had one. The cell means are far inside the noise.

## Stability of the rebuild

- **Trade 1's state** (LONG, SHORT or suppressed) is identical across all three draws on **47 of 57 dates**,
  against 52 for the S&P. The ten that differ sit at the 0.25 gate. Each turns on one of three
  judgement calls:
  - the short-term technical signal;
  - which swing counts as the "last completed" one;
  - a cross-asset leg (DAX, Euro Stoxx and Brent were never in the slices).
- **Regime label.** Across all three draws it is TRANSITION on 156 of 171 date-draws, RANGE on 8 and
  TREND_UP on 7. Eleven dates split across draws:
  - **RANGE vs TRANSITION on 7 dates** (02 Jun, 03 Jun, 09 Jun, 17 Jul, 22 Jul, 24 Jul, 27 Jul). The
    cause is the RANGE gate's RSI2-median clause (30–70), which the FTSE's frequent RSI2 = 100 readings break.
  - **TREND_UP vs TRANSITION on 4 dates** (25 May, 29 Jun, 28 Jul, 30 Jul). The cause is a volatility
    slope near zero.
  - **03 Jul** is TREND_UP in every draw.
- **Spread at the US open.** Across draws it is about 6.5R, against ±20R across dates.

**Audit flags.** These cards are kept as issued:

- **Weekly pivot tier:** five Trade 2 cards were built on the weekly tier (06-18 in all three draws,
  05-28 in draws 1 and 3).
- **Off-formula entries:** four Trade 2 entries were placed at R1 rather than P+0.10×(R1−P), mostly
  following the QA feedback's suggestion (06-15 d3, 07-17 d2 and d3, 07-29 d3).
- **Effect on the totals:** excluding them changes each draw's 07:00 UK total by −1.2 to +0.4R and its
  US open total by −1.2 to +0.8R.

## QA Stage 1 summary (FTSE, 57 reports)

- **Score:** mean Trust Score 52.9, lower than the S&P's 60.1. Bands: Low 44, Moderate 12, Very Low 1, none High.
- **Accuracy:** mean C3 (accuracy and evidence) 1.11 of 5.
- **Overrides:** restriction breach 25, hallucinated source 21, none 11.

The FTSE reports fail in the same ways as the S&P ones, more often:

- prior-session OHLC off the cash feed by 15–130 points;
- daily pivots from D−2, and weekly or monthly pivots from the wrong period;
- ATR stated at 60–90 against a real 100–150;
- opens copied from the prior close and labelled "corroborated";
- module codes left in the body.

## Limitations

1. **57 dates is small.** The intervals are about ±20–30R. A real effect of a few R in total would not
   be detectable, and the 07:00 UK headline depends on three cards.
2. **DAX, Euro Stoxx 50 and Brent were never available.** Sentiment was carried from the report
   unverified. Those components decide Trade 1 on the ten dates where the draws disagree.
3. **The UK100 feed is a CFD, not the cash index.** The level file's `prev_close_full` (the MARKET entry)
   can sit 20–70 points from the LSE cash close when the feed moves after 16:30 London. This pushed some
   rebuilt Trade 1 stops onto deeper pivots and made some Trade 2 orders flip between stop and limit form.
4. **Bank holiday.** 25 May has no UK100 session, so cards dated 25 May fill on 26 May. Its level row repeats 22 May.
5. **The rule-book is ambiguous in places** that the draws resolved differently:
   - the breakout side for TRANSITION Trade 2 ("failed retest" wording);
   - "nearest support" for the Trade 1 stop;
   - the alternative S1−0.25×ATR stop.

   Each card records its reading in `rationale`.
