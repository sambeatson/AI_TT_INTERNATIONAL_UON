# Sentiment as a trading signal: post-event study across five markets

**Question.** If the report's news sentiment alone set the direction, could it be traded? Two rules
are tested on every report from 11 May to 2 August 2026, across five markets:

- **Main rule:** fade into the day's levels. On a negative day, sell limits at R1 and at R2. On a
  positive day, buy limits at S1 and at S2.
- **Comparison:** the first study's pivot rule.

**Short answer.** No market shows a tradable edge from report sentiment.

1. **Entering at R1/S1 neutralises the loss but does not create a gain.** Pooled across the five
   markets, R1/S1 entries average about **0 ATR** at every horizon (95% intervals span zero, hit rate
   about 50%). The pivot rule loses about **−0.15 ATR** over five days.
2. **R2/S2 entries are worse than R1/S1:** −0.1 to −0.2 ATR. When price reaches the second level, it
   is usually running against the sentiment.
3. **Stronger sentiment did worse, not better,** on both rules.
4. **In every market, sentiment restates the previous five days of price.** The correlation with the
   prior 5-day return is 0.56–0.68. Beyond that echo, sentiment adds no information on the S&P 500, gold
   or WTI. It is **contrarian on the FTSE 100 and Bitcoin**.

Revising the sentiment (S&P and FTSE rebuilds) changes results by a few hundredths of a percent.
Shanghai is not included: there is no Shanghai price feed.

```
python studies/sentiment_pivot/build_sentiment.py   # sentiment_by_date.csv (267 report dates)
python studies/sentiment_pivot/run_study.py         # out_levels/, out_pivot/
python studies/sentiment_pivot/pooled.py            # pooled.csv (ATR units, five markets)
python studies/sentiment_pivot/echo_test.py         # echo_test.csv, market_moves.csv
```

---

## 1. Design

The rules are written into `run_study.py`.

| Element | Rule |
|---|---|
| Markets and reports | S&P 500 (57), FTSE 100 (57), gold (57), WTI crude (57 dates, 58 reports), Bitcoin (39, including 12 weekend dates) |
| Signal | Report tilt *s* in [−1, +1]. Positive day if *s* > 0, negative day if *s* < 0, no trade if *s* = 0. **Original** tilt for all five markets. **Revised** tilt (median of three rebuilt-card draws) for the S&P and FTSE only, since the others have no rebuilds yet. |
| Levels | Daily floor pivots for date D from bars **before D only** (`engine/reference_levels.py`, which asserts this row by row). Cash-session basis for the two indices; full-day basis for gold, WTI and Bitcoin, which trade around the clock. WTI and Bitcoin level tables were built for this study (`data/levels/SpotCrude_levels.csv`, `BTCUSD_levels.csv`). |
| Entry times | **09:00 UK** and **US cash open (14:30 UK)** on the report's own session. Orders expire 21:00 UK. |
| **Main rule (levels)** | Negative day: **sell limit at R1** and, as a separate leg, **at R2**. Positive day: **buy limit at S1** and **at S2**. If price is already through a level at the entry time, the limit fills at once at that price. |
| Comparison rule (pivot) | Positive day: buy at market above the pivot, or with a buy stop at the pivot from below. Negative day: the mirror image. |
| Windows | From the fill: **D0** = same day; **D1** = to the end of the next day; **D5** = up to five sessions. A window ends early if a later report reverses the sentiment sign. |
| Measures | Max favourable and adverse excursion (MFE, MAE) and the return at window end. These are in % of the asset per market, and in **ATR multiples** when pooling, so a 2% Bitcoin move and a 0.5% index move are comparable. Also achievable R with a 1-ATR stop (adverse extreme assumed first within a bar). |
| Degree | Weak \|s\| < 0.2; moderate 0.2–0.4; strong ≥ 0.4 |

---

## 2. The sentiment data

| | S&P 500 | FTSE 100 | Gold | WTI | Bitcoin |
|---|---:|---:|---:|---:|---:|
| Report dates | 57 | 57 | 57 | 57 | 39 |
| Positive / negative / zero days | 30 / 25 / 2 | 35 / 21 / 1 | 10 / 43 / 1 | 24 / 32 / 0 | 9 / 27 / 1 |
| Median tilt | +0.10 | +0.13 | −0.32 | −0.18 | −0.20 |
| Revised by rebuild (changed / sign flips) | 9 / 1 | 17 / 1 | – | – | – |

Gold and Bitcoin reports were **mostly bearish** over the period.

Tilts were read from each report's §13b aggregate. Sixteen that the parser could not read cleanly were
read by hand; they are listed in `build_sentiment.py`. A tilt printed as a division ("−0.71 / 4.2 =
−0.17") is taken as the result after the equals sign.

WTI has two reports for 10 July; their tilts are averaged.

---

## 3. Main rule: buy S1/S2 on positive days, sell R1/R2 on negative days

### 3a. How often the orders filled (09:00 UK, original sentiment)

| | S&P 500 | FTSE 100 | Gold | WTI | Bitcoin |
|---|---:|---:|---:|---:|---:|
| Sell R1 (negative days) | 16 of 25 | 16 of 21 | 15 of 46 | 9 of 33 | 8 of 28 |
| Sell R2 | 6 of 25 | 3 of 21 | 5 of 46 | 4 of 33 | 2 of 28 |
| Buy S1 (positive days) | 16 of 30 | 16 of 34 | 6 of 10 | 9 of 24 | 4 of 10 |
| Buy S2 | 10 of 30 | 5 of 34 | 2 of 10 | 3 of 24 | 2 of 10 |

**About half the R1/S1 orders fill on the indices, and a quarter to a third on the commodities and
Bitcoin.** R2/S2 fills are rare: 2–10 per market. Per-market results for R2/S2 are anecdotes, so the
conclusions rest on the pooled tables.

### 3b. Pooled across the five markets (ATR units, 09:00 UK)

| | Window | Trades | Return, ATR (95% CI) | Hit rate | Median MFE / MAE, ATR | 1R reached with a 1-ATR stop |
|---|---|---:|---|---:|---|---:|
| **R1/S1** | D0 | 115 | −0.01 (−0.11 to +0.09) | 50% | 0.33 / 0.29 | 5% |
| **R1/S1** | D1 | 115 | −0.02 (−0.16 to +0.12) | 48% | 0.50 / 0.43 | 17% |
| **R1/S1** | D5 | 115 | +0.02 (−0.16 to +0.21) | 47% | 0.54 / 0.54 | 29% |
| **R2/S2** | D0 | 42 | −0.09 (−0.28 to +0.07) | 48% | 0.28 / 0.21 | 5% |
| **R2/S2** | D1 | 42 | −0.20 (−0.44 to +0.01) | 45% | 0.40 / 0.51 | 10% |
| **R2/S2** | D5 | 42 | −0.18 (−0.43 to +0.06) | 52% | 0.41 / 0.53 | 19% |
| *Pivot rule* | D0 | 210 | −0.02 (−0.09 to +0.05) | 49% | 0.31 / 0.34 | 10% |
| *Pivot rule* | D1 | 210 | −0.07 (−0.17 to +0.03) | 44% | 0.47 / 0.56 | 19% |
| *Pivot rule* | D5 | 210 | −0.14 (−0.31 to +0.02) | 40% | 0.60 / 0.83 | 33% |

The US-open entry gives the same picture: R1/S1 between −0.05 and −0.01 ATR, R2/S2 between −0.13 and
−0.09, and the pivot rule −0.16 at D5 (`pooled.csv`).

- **Risk–reward.** At R1/S1 the favourable and adverse excursions are about equal (MFE/MAE ≈ 1). With a
  1-ATR stop, 1R was reached on 5% of trades the same day and 29% within five days. That is roughly
  what a random entry gives, not an edge.
- **Waiting for R1/S1 improves on the pivot rule.** Taking the trade at a better price removes the
  pivot rule's five-day loss (−0.14 → +0.02 ATR). It does not turn sentiment into a profit.
- **R2/S2 is worse.** By the time price stretches to the second level, the day is usually trending
  against the report.

### 3c. Positive days vs negative days (pooled, 09:00 UK)

| | D1 return, ATR | D5 return, ATR |
|---|---:|---:|
| Buy S1 on positive days (51) | −0.01 | +0.01 |
| Sell R1 on negative days (64) | −0.02 | +0.02 |
| Buy S2 (22) | −0.18 | −0.18 |
| Sell R2 (20) | −0.22 | −0.18 |
| *Pivot: buy on positive days (91)* | −0.14 | **−0.29** (−0.52 to −0.05) |
| *Pivot: sell on negative days (119)* | −0.02 | −0.03 |

The pivot rule's losses come mostly from buying on positive days. The level rule's buy-at-S1 avoids that.

### 3d. Per market, R1/S1 legs (09:00 UK)

| Return at D5 | ATR (95% CI) | % of asset | Trades |
|---|---|---:|---:|
| S&P 500 | **−0.36** (−0.70 to −0.04) | −0.34% | 32 |
| FTSE 100 | +0.14 (−0.12 to +0.40) | +0.18% | 32 |
| Gold | +0.16 (−0.25 to +0.69) | +0.28% | 21 |
| WTI | +0.25 (−0.38 to +0.91) | +1.41% | 18 |
| Bitcoin | +0.08 (−0.24 to +0.37) | +0.15% | 12 |

Only the S&P result is distinguishable from zero, and it is a loss. Per-leg and per-window tables in
% of the asset are in `out_levels/summary.csv`.

### 3e. Degree of sentiment (pooled, 09:00 UK)

| Return, ATR | Weak (<0.2) | Moderate (0.2–0.4) | Strong (≥0.4) |
|---|---:|---:|---:|
| R1/S1, D1 | +0.13 (31) | +0.04 (46) | **−0.19** (38) |
| R1/S1, D5 | 0.00 | +0.13 | −0.10 |
| R2/S2, D1 | −0.17 (7) | −0.04 (22) | **−0.49** (13) |
| Pivot, D1 | +0.07 (55) | −0.14 (71) | −0.10 (84) |

**Strong sentiment is the worst band** on the level rule, as it was on the pivot rule in the first
study. This is what you would expect if strong sentiment mostly reflects a move that has already
happened.

---

## 4. Does sentiment carry information at all? (no trading rule)

These are Spearman correlations of tilt with the market's move from 09:00 UK, regardless of any order.
They are then repeated controlling for the prior 5-day return: ranks, with Newey–West standard errors
for the overlapping windows (`echo_test.csv`).

| | Tilt vs prior 5-day return | Tilt vs next 1 day | Tilt vs next 5 days | Tilt beyond the prior move? |
|---|---:|---:|---:|---|
| S&P 500 | **0.56** | −0.24 | **−0.29** | **No** (p > 0.15) |
| FTSE 100 | **0.64** | **−0.33** | **−0.37** | **Yes, contrarian** (D5: p < 0.01; US open D1: p = 0.03) |
| Gold | **0.68** | **−0.28** | **−0.33** | **No** (p > 0.1) |
| WTI | **0.58** | +0.04 | +0.01 | **No** relationship at all |
| Bitcoin | **0.67** | −0.29 | −0.17 | **Yes, contrarian at D1** (p = 0.01); n = 39 |

- **The echo is universal.** In all five markets the reports' sentiment largely restates the last five
  days of price.
- **Following sentiment only made money where the market fell and the reports were bearish.** On WTI,
  following the sentiment at market made +0.85% over D5 while buy-and-hold lost 1.4%. Sentiment had no
  ranking power there (ρ ≈ 0); the gain came from a bearish majority in a falling market.

---

## 5. Original vs revised sentiment (S&P and FTSE)

| R1/S1, 09:00 UK, % of asset | D1 original | D1 revised | D5 original | D5 revised |
|---|---:|---:|---:|---:|
| FTSE: sell R1 | 0.00 | 0.00 | +0.09 | +0.09 |
| FTSE: buy S1 | +0.19 | +0.23 | +0.27 | +0.31 |
| S&P: sell R1 | +0.02 | +0.06 | −0.39 | −0.34 |
| S&P: buy S1 | −0.19 | −0.19 | −0.29 | −0.29 |

The rebuild corrected the arithmetic of the tilt, not its sources. As a result the trades barely change.

---

## 6. Caveats

1. **Small samples.** R2/S2 has 2–10 fills per market. The per-market R1/S1 cells have 12–32 trades.
   Rely on the pooled tables.
2. **One 12-week period**, with different trends by market: indices rising, gold and WTI falling,
   Bitcoin mixed. Direction and trend are entangled. Gold and Bitcoin reports were mostly bearish, so
   their results are mostly short trades.
3. **Many comparisons:** 5 markets × 2 rules × 2 entry times × 3 windows × legs × degree bands. Treat
   any single p ≈ 0.05 as a lead. The universal echo (every p < 0.001) and the strong-sentiment pattern
   are the robust findings.
4. **Limits through a level at the entry time** fill at that price, which is better than the level.
   This is common: **30% of R1/S1 fills at 09:00 UK and 40% at the US open** (25–44% by market). On those
   days the order is in effect a market order taken after an extended move. The `mode` column in
   `out_levels/trades.csv` separates them (`AT_T` vs `LIMIT`).
5. **MFE and MAE are upper bounds,** not executable exits. Use the 1-ATR-stop column for what could
   realistically be captured.
6. **Bitcoin** includes weekend sessions; its "next day" can be a Saturday.
7. **Sentiment was never verified against its sources.** Both versions carry the report's own reading
   of the news.

---

## 7. Implications

- **For the strategy module.** Sentiment should not set trade direction on its own. Where it is used,
  as one of six inputs in the direction score, first remove what the prior 5-day return already
  explains. Otherwise the score counts recent momentum twice: once as the technical signal and once as
  sentiment.
- **If sentiment is used at all, enter at R1/S1, not at the pivot or market.** The better entry is what
  removes the loss. Do not add at R2/S2.
- **Contrarian FTSE and Bitcoin results** came out of this data. They need testing out of sample
  (later reports) before anyone acts on them.

## Files

| File | Contents |
|---|---|
| `sentiment_by_date.csv` | Tilt per report date for five markets (original; revised and per-draw for S&P and FTSE) |
| `out_levels/trades.csv`, `out_pivot/trades.csv` | One row per leg × window: fill, MFE/MAE, return, achievable R, reversal date; unfilled orders included |
| `out_*/summary.csv` | Per market × version × entry × leg × window (pivot rule also with the extension filter) |
| `out_*/fill_rates.csv`, `out_*/by_degree.csv` | Fill counts; results by sentiment strength |
| `pooled.csv` | Five markets pooled in ATR units, by level, by direction, by degree and by market |
| `echo_test.csv`, `market_moves.csv` | Tilt vs prior and forward market moves; regression controlling for the prior 5-day return |
