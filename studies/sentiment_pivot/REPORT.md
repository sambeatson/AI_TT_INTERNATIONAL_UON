# Sentiment as a trading signal: a post-event study on S&P 500 and FTSE 100

**Question.** If the report's news sentiment alone decided the trade, would it have worked? We use
the sentiment from the **original** report and from the **revised** (rebuilt-card) version, trade
it against the prior day's pivot, and measure how far price moved for and against the position.

**Short answer.** No. Over the 1–5 days after a report, **sentiment pointed the wrong way more often
than the right way, on both indices**: more bullish reports were followed by weaker markets.

- **S&P 500.** This is explained by the market's own recent move. Sentiment largely echoes the
  previous five days (ρ ≈ 0.55), and those moves partly reversed.
- **FTSE 100.** Sentiment stays contrarian even after allowing for that echo.

Revising the sentiment made almost no difference. Stronger sentiment did not do better. If anything it
did worse.

Everything is reproducible:

```
python studies/sentiment_pivot/build_sentiment.py   # sentiment_by_date.csv
python studies/sentiment_pivot/run_study.py         # trades.csv, summary.csv, by_degree.csv, tilt_vs_market.csv
python studies/sentiment_pivot/echo_test.py         # echo_test.csv
```

---

## 1. Design

The rules were written into `run_study.py` before any result was looked at.

| Element | Rule |
|---|---|
| Sample | 57 report dates per index, 11 May – 31 Jul 2026 |
| Signal | Report tilt *s* in [−1, +1]: *s* > 0 long, *s* < 0 short, *s* = 0 no trade |
| Original vs revised | **Original** is the tilt printed in the report. **Revised** is the median of the three rebuilt-card draws. The rebuilds carried the report tilt but corrected its arithmetic where QA found errors. |
| Pivot | Daily cash-session pivot *P* for date D, computed only from bars before D (no look-ahead) |
| Entry times | **09:00 UK** and **US cash open (14:30 UK)** on the report's own session |
| Long | Price above *P* → **buy at market**. Price at or below *P* → **buy stop at *P*** (fills on the first touch; expires 23:00 broker, 21:00 UK) |
| Short | Mirror image: price below *P* → **sell at market**. Price above *P* → **sell stop at *P*** |
| Extension filter (extra rule, tested separately) | A market short is taken only if price is still **above the "−2.5" support**, read as the midpoint of S2 and S3. A market long is taken only if price is below the R2–R3 midpoint. Stop entries are unaffected. |
| Windows | Measured from the fill: **D0** = rest of the same day; **D1** = to the end of the next day; **D5** = up to five sessions |
| Sentiment reversal | A D1 or D5 window **ends early** if a later report's tilt has the opposite sign. The exit is just before that report's own entry time. |
| Measures | Max favourable excursion (MFE) and max adverse excursion (MAE) in points, % of the asset and ATR multiples; return at window end (%); MFE/MAE ratio; achievable R |
| Achievable R | A stop is placed at 0.5 × ATR or 1 × ATR. We take the largest favourable move reached before the stop is touched, in R. Within a bar the adverse extreme is assumed to come first (conservative). |
| Degree of sentiment | Three bands: weak (\|s\| < 0.2), moderate (0.2–0.4) and strong (≥ 0.4). Also the Spearman correlation of *s* with the market's move from the entry time. |

**Interpretation to confirm.** You wrote "above the −2.5 support". The level files have S1–S3 only, so
I read "−2.5" as halfway between S2 and S3. If you meant something else, such as 2.5 × ATR below the
pivot, it is a one-line change in `run_study.py`.

---

## 2. The data

`sentiment_by_date.csv` holds one row per report date for each index (114 in total).

| | FTSE 100 | S&P 500 |
|---|---:|---:|
| Report dates | 57 | 57 |
| Bullish / bearish / neutral (original) | 35 / 21 / 1 | 30 / 25 / 2 |
| Median \|tilt\| | 0.30 | 0.30 |
| Dates where the revision changed the tilt by more than 0.02 | **17** | **9** |
| Revisions that flipped the sign | 1 (28 May: +0.24 → −0.24) | 1 (30 Jun: −0.30 → +0.25) |

Ten report tilts could not be read automatically and were read by hand; they are listed in
`build_sentiment.py`. The revised value is the median of the three rebuilds, because one rebuild
occasionally stored the weighted contribution (tilt × 0.15) instead of the tilt itself.

---

## 3. Results

**How to read the tables.** Results are per trade, using the original sentiment. "Return" is the
asset's % move from fill to window end, in the trade's direction. Revised-sentiment results are within
a few hundredths of these (`summary.csv`).

### 3a. FTSE 100

| Entry | Window | Trades | MFE % | MAE % | Median MFE/MAE | Return % (95% CI) | Hit rate | Reach 1R with a 1-ATR stop |
|---|---|---:|---:|---:|---:|---|---:|---:|
| 09:00 UK | D0 | 43 | 0.42 | 0.60 | 0.29 | **−0.23** (−0.42 to −0.04) | 28% | 16% |
| 09:00 UK | D1 | 43 | 0.58 | 0.88 | 0.42 | **−0.36** (−0.57 to −0.16) | 33% | 21% |
| 09:00 UK | D5 | 43 | 0.74 | 1.27 | 0.35 | **−0.52** (−0.82 to −0.21) | 26% | 28% |
| US open | D0 | 37 | 0.29 | 0.44 | 0.38 | **−0.17** (−0.32 to −0.03) | 38% | 3% |
| US open | D1 | 37 | 0.53 | 0.83 | 0.47 | **−0.34** (−0.59 to −0.10) | 38% | 11% |
| US open | D5 | 37 | 0.78 | 1.31 | 0.48 | **−0.47** (−0.78 to −0.16) | 32% | 22% |

### 3b. S&P 500

| Entry | Window | Trades | MFE % | MAE % | Median MFE/MAE | Return % (95% CI) | Hit rate | Reach 1R with a 1-ATR stop |
|---|---|---:|---:|---:|---:|---|---:|---:|
| 09:00 UK | D0 | 44 | 0.50 | 0.56 | 1.04 | −0.01 (−0.19 to +0.17) | 61% | 9% |
| 09:00 UK | D1 | 44 | 0.68 | 0.85 | 0.83 | −0.16 (−0.42 to +0.11) | 41% | 18% |
| 09:00 UK | D5 | 44 | 0.91 | 1.30 | 0.71 | **−0.58** (−0.94 to −0.21) | 30% | 25% |
| US open | D0 | 41 | 0.49 | 0.49 | 1.05 | +0.04 (−0.13 to +0.20) | 59% | 7% |
| US open | D1 | 41 | 0.70 | 0.84 | 0.92 | −0.15 (−0.44 to +0.13) | 39% | 20% |
| US open | D5 | 41 | 0.94 | 1.33 | 0.66 | **−0.56** (−0.95 to −0.20) | 29% | 27% |

**Fills.** Stop orders at the pivot went unfilled on 10–18 days per set; those days have no trade.
Market entries made up about 70% of FTSE trades and about 50% of S&P trades.

### 3c. Risk–reward: what was achievable

- **The adverse excursion was larger than the favourable one in every FTSE cell.** The median MFE/MAE
  ratio is 0.3–0.5: price typically went about twice as far against the position as for it. For the
  S&P, MFE/MAE is about 1.0 on the same day (a coin toss) and falls to about 0.7 over five days.
- **With a 1-ATR stop,** a 1R gain was reached before the stop on only 3–28% of trades. A 2R gain was
  reached on at most 9%.
- **With a tighter 0.5-ATR stop,** 1R (that is, half an ATR) was reached on 16–45% of trades, but the
  stop was hit first on most of the rest.

There is no stop/target combination here that turns this signal into a positive risk–reward.

### 3d. Percentage gained or lost on the asset

The average trade lost:
- **FTSE:** 0.2–0.5% of the index.
- **S&P:** roughly break-even on the same day, and about 0.6% over five days.

Over the same windows, simply **buying at the entry time every day** made money: on average **+0.46%
(FTSE)** and **+0.20% (S&P)** over D5 (`tilt_vs_market.csv`). Both indices rose over the period.

Do not add the returns up into an account total: D1 and D5 windows overlap, so the same move is counted
more than once.

### 3e. Does the degree of sentiment matter?

**No, not in the direction you would hope.** Strong-sentiment trades were not better. On the multi-day
windows they were among the worst:

| Mean return % (original, 09:00 UK) | Weak (<0.2) | Moderate (0.2–0.4) | Strong (≥0.4) |
|---|---:|---:|---:|
| FTSE, D1 | −0.26 | −0.56 | −0.20 |
| FTSE, D5 | −0.40 | −0.45 | **−0.81** |
| S&P, D1 | +0.14 | −0.18 | **−0.51** |
| S&P, D5 | −0.40 | −0.73 | −0.54 |

Each band holds only 11–19 trades. Across all dates, the rank correlation between tilt and the market's
subsequent move is **negative**:

| Spearman ρ (p) | D0 | D1 | D5 |
|---|---:|---:|---:|
| FTSE, 09:00 UK | −0.18 (0.19) | **−0.33 (0.01)** | **−0.37 (0.01)** |
| FTSE, US open | −0.23 (0.09) | **−0.31 (0.02)** | **−0.42 (<0.01)** |
| S&P, 09:00 UK | −0.04 (0.77) | −0.24 (0.08) | **−0.29 (0.03)** |
| S&P, US open | 0.00 (0.98) | −0.21 (0.12) | **−0.28 (0.04)** |

### 3f. Why: sentiment echoes the recent market move

The reports' sentiment is strongly correlated with what the market had **already** done:

| ρ (tilt vs return before the report) | Prior day | Prior 5 days |
|---|---:|---:|
| FTSE | 0.23 | **0.64** |
| S&P | **0.49** | **0.56** |

We regressed the market's forward move on tilt and the prior 5-day return together (ranks; Newey–West
standard errors to allow for overlapping windows; `echo_test.csv`):

- **S&P:** once the prior 5-day return is included, **tilt adds nothing** (coefficient ≈ 0, p > 0.15
  everywhere). The prior move itself predicts the reversal at D5 (p ≈ 0.02–0.04). The S&P sentiment is a
  restatement of recent price, and recent price partly mean-reverted.
- **FTSE:** **tilt stays negative beyond the prior return** at the US open, D1 and D5 (coefficient −0.32
  and −0.50, HAC p = 0.03 and < 0.01). It is weaker at 09:00 UK (D1 p = 0.10, D5 p < 0.01). On the FTSE,
  the news tone itself looked contrarian over this period.

### 3g. Original vs revised sentiment; the extension filter

- **Revision barely mattered.** The same-sign revisions changed tilt sizes but rarely the trade
  direction. The two sign flips are 2 trades out of more than 40. Every cell moves by a few hundredths of
  a percent, e.g. FTSE 09:00 D5: −0.52% original vs −0.47% revised.
- **The extension filter rarely applied.** Only 1–5 market entries per set had already run past the
  2.5 level. On the FTSE, skipping them helped a little (US open D5 summed return −17.3% → −13.1%). On the
  S&P it made no difference.

---

## 4. Caveats

1. **Small sample, one period.** There are 57 dates per index over 12 weeks, both in rising markets
   (FTSE about 10,100 → 10,900). A contrarian result in a rising market partly reflects bearish reports
   being wrong in an uptrend. Results by direction are in `trades.csv` (`side`).
2. **Many tests.** The grid covers 2 indices × 2 versions × 2 entries × 3 windows, plus the degree bands.
   Treat single p-values near 0.05 as leads. The FTSE contrarian result is consistent across entries and
   windows, which is more convincing than any one cell.
3. **Overlap.** D1 and D5 windows overlap across consecutive dates. The plain p-values in §3e overstate
   significance. The HAC p-values in §3f allow for this.
4. **MFE and MAE are not executable.** They are upper bounds on what was available. The achievable-R
   measure is the realistic one.
5. **Stop fills.** Excursion is measured over the whole fill bar, so a stop-entry trade's MAE can include
   price before the trigger. This overstates MAE slightly.
6. **Sentiment was never verified.** Both versions carry the report's own reading of the news. The
   revision corrected arithmetic, not sources.
7. **Price data and pivots.** Broker CFD data is used; pivots are on the cash-session basis.

---

## 5. What this suggests next

- **Test the contrarian reading out of sample.** "Fade the report's sentiment" is a post-hoc idea from
  this study, so it must not be judged on these same 57 dates. The natural test is the gold, WTI and
  Bitcoin reports (same framework, untouched by this analysis), or a later period for the FTSE.
- **Control for the echo before using sentiment at all.** For any market, check whether sentiment
  carries information beyond the prior 5-day return. On the S&P it did not.
- **For the strategy module,** the sentiment weight (0.15 in the six-signal direction score) is pushing
  the score the wrong way on the FTSE. It is at best neutral on the S&P.

## Files

| File | Contents |
|---|---|
| `sentiment_by_date.csv` | Original and revised tilt per date (with each draw), plus the report text it was read from |
| `trades.csv` | One row per trade × window: fill mode and price, MFE/MAE, return, achievable R, reversal date |
| `summary.csv` | Aggregates per asset × version × entry × window, with and without the extension filter |
| `by_degree.csv` | The same, split by weak / moderate / strong sentiment |
| `tilt_vs_market.csv` | Spearman correlation of tilt with the market's move, plus the always-long and follow-sentiment benchmarks |
| `market_moves.csv` | The market's move from each entry time, regardless of fill |
| `echo_test.csv` | Tilt vs prior returns, and tilt's effect controlling for the prior 5-day return (HAC) |
