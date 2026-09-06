*M3 — Technical Analysis Module  │  Modular Prompt Architecture v2.1  │  DO NOT EDIT*

| **M3   ****MODULE 3 — FIXED TECHNICAL ANALYSIS MODULE** *DO NOT EDIT  ·  This module is fixed. Variable placeholders are consumed from M1 at run time.* *Modular Prompt Architecture v2.1  │  April 2026  │  Steps 1–10 unchanged · Step 11 added (Named Output Surface)* |
| --- |

| **M1  VARIABLES** *Provides inputs* | **M2  RESEARCH STD** *Governs evidence* | **M3  TECHNICAL** *← You are here* | **M4  OUTPUT** *Formats results* |
| --- | --- | --- | --- |

You are acting as a **[ROLE_TITLE]** conducting a technical analysis of **[PRIMARY_ASSET]** as of **[AS_OF_DATE]** (**[AS_OF_TIMEZONE]**). Where applicable, the analysis also covers **[SECONDARY_ASSET_1]** and **[SECONDARY_ASSET_2]** as designated comparators. This module governs all technical work. Follow every step in sequence. Do not skip steps, merge steps, or reorder them.

This module runs after M1 variables are declared and M2 source standards are in force, and before M4 output formatting begins. Outputs from this module feed directly into M4 and M5. There is no siloing — every technical conclusion must be explicitly referenced in the relevant M4 sections, and the named outputs in Step 11 are the contract M5 consumes when [PRODUCE_STRATEGY_RECOMMENDATIONS] = YES.

**VARIABLES CONSUMED FROM M1**

| **M1 Variable** | **How M3 uses it** |
| --- | --- |
| [PRIMARY_ASSET] | Instrument under technical review throughout this module |
| [SECONDARY_ASSET_1] | Primary comparator — receives its own OHLC table and technical read alongside [PRIMARY_ASSET] |
| [SECONDARY_ASSET_2] | Second comparator if populated — same treatment as [SECONDARY_ASSET_1]; skip if blank |
| [COUNTER_1] … [COUNTER_5] | Cross-asset counters for VOLator and directional confirmation (Step 6) |
| [LOOKBACK_SHORT] | Number of valid sessions for the 5-day execution block (default 5) |
| [LOOKBACK_MEDIUM] | Number of valid sessions for the regime block (default 25) |
| [AS_OF_DATE] / [AS_OF_TIMEZONE] | Controls the snapshot date and session cut-off |
| [UNIT_OF_MEASURE] / [CURRENCY] | Maintains consistency in all tables and charts |
| [VOL_METHOD] | Volatility calculation method for the VOLator engine (Step 5) |
| [SCALE_METHOD] | Scaling method for cross-asset VOLator comparison (Step 5) |
| [KAUFMAN_PERIOD] | Lookback window for Kaufman Efficiency Ratio (Step 7) |
| [KAUFMAN_EMA_SMOOTH] | EMA period applied to raw KER before classification (Step 7) |
| [KAUFMAN_TREND_THRESHOLD] | Absolute KER level defining trending vs ranging boundary (Step 7) |
| [KAUFMAN_RANGEUP_THRESHOLD] | Inner band boundary for ranging bias direction (Step 7) |
| [CHART_CANDLESTICK] … [CHART_PIVOT] | YES/NO toggles controlling which charts are produced (Step 9) |
| [PIVOT_DAILY] / [PIVOT_WEEKLY] / [PIVOT_MONTHLY] | YES/NO toggles controlling which pivot timeframes are calculated (Step 8) |
| [PIVOT_ABOVE_BELOW_DAILY/WEEKLY/MONTHLY] | Number of levels above HIGH and below LOW shown in pivot chart (Step 8) |
| [PIVOT_CANDLES_N] | Number of candles drawn on the pivot chart (Step 8c, 9e) — default 2 |
| [PIVOT_CANDLES_TF] | Timeframe of candles on the pivot chart (Step 8c, 9e) — default WEEKLY |

| **ABSOLUTE NO-SYNTHESIS RULE** No price, OHLC field, or pivot input may ever be synthesised, estimated, interpolated, or derived from narrative text. If a source fails, try the next. Exhaust up to 50 approved sources before raising a DataCorroborationError. Do not proceed with unverified data. |
| --- |

| **HARD RULES — apply throughout every step of this module** •  Use only validated OHLC data from approved sources. Never synthesise. •  Reject any date that is a weekend, public holiday, or unjustified duplicate. Log rejections in the Agent Log. •  Distinguish clearly at all times between observed data, derived signal, and final judgement. Do not blend these categories in the same sentence. •  [SECONDARY_ASSET_1] and [SECONDARY_ASSET_2] must receive the same OHLC validation treatment as [PRIMARY_ASSET]. They are not decorative references. •  Cross-asset counters confirm or contradict the technical read. They do not replace it. Flag contradiction explicitly — do not suppress it. •  No unsupported pattern claims. Every technical assertion must be derivable from the validated OHLC table. •  The seven-line Final Judgement Syntax (Step 10) is mandatory output. M4 will not function correctly without it. •  The Step 11 Named Output Surface is the contract M5 consumes when [PRODUCE_STRATEGY_RECOMMENDATIONS] = YES. Every named value must be present and dated. |
| --- |

| **STEP 1** | **INPUT VALIDATION — OHLC ****&**** TRADING DATES** |
| --- | --- |

**1a.  Trading Date Validation**

- Accept only Monday–Friday dates. Any Saturday or Sunday row must be rejected and logged.

- Verify the session count matches the expected trading calendar for the relevant exchange. Note any verified public holidays that reduce the count.

- Reject any row where Open = High = Low = Close identically from the prior row (unjustified duplicate). If a duplicate is justified by a verified zero-move session, document it explicitly.

**1b.  Two-Source Corroboration  (Mandatory for all instruments)**

Work through the approved source stack defined in the Source Discipline No-Synthesis Protocol document, in the priority order specified there. Apply this to [PRIMARY_ASSET], [SECONDARY_ASSET_1], [SECONDARY_ASSET_2], and all [COUNTER_1]–[COUNTER_5] used in Step 5. Do not attempt sources outside that document. If all approved sources are exhausted without achieving corroboration, raise a DataCorroborationError and halt — do not proceed.

A value is accepted only when at least TWO independent sources agree within the following tolerances:

| **Asset Type** | **Tolerance** | **Applies to** |
| --- | --- | --- |
| FX 5dp  (EURUSD, GBPUSD, EURCAD, etc.) | ± 0.00005  (0.5 pip) | All OHLC fields; pivot prior-period H / L / C |
| FX 3dp  (EURJPY, USDJPY, etc.) | ± 0.050  (5 pips) | All OHLC fields; pivot prior-period H / L / C |
| Equity index (SPX, DAX, etc.) | ± 0.10 pts | All OHLC fields; pivot prior-period H / L / C |
| USDX / DXY | ± 0.050 pts | All OHLC fields; pivot prior-period H / L / C |
| Commodity — set per [UNIT_OF_MEASURE] | Asset-specific; document assumption | All OHLC fields; pivot prior-period H / L / C |

- If fewer than two sources agree within tolerance, mark that field “single-source — indicative only” in the OHLC table and in any chart that uses it.

- Record every source attempt in the Agent Log: source name, tier, outcome (corroborated / single-source / failed / not attempted), and the corroborated pair with delta when corroboration is achieved.

| **STEP 2** | **5-DAY TECHNICAL BLOCK — Execution-Level Analysis** |
| --- | --- |

Produce a validated OHLC table covering the last [LOOKBACK_SHORT] valid trading sessions for [PRIMARY_ASSET]. Repeat for [SECONDARY_ASSET_1] and [SECONDARY_ASSET_2] if populated.

**2a.  Required Table Fields**

- Date  |  Open  |  High  |  Low  |  Close  |  RSI2  |  Trend  |  Source A  |  Source B  |  Final Value Used  |  Validation Outcome

- RSI2 is fixed at period 2. Do not change the period. Compute from the validated close sequence. RSI2 = 100 − (100 / (1 + RS)) where RS = mean gain / mean loss over 2 periods.

- Trend classification per session: if Close > Open AND RSI2 > 50 → Bullish.  If Close < Open AND RSI2 < 50 → Bearish.  Otherwise → Neutral / Transition.

**2b.  Candle-by-Candle Classification**

For each of the [LOOKBACK_SHORT] sessions, assess and record:

- Body direction (bullish / bearish / doji) and body size relative to the session range

- Upper wick length — rejection from high / supply zone pressure

- Lower wick length — rejection from low / demand zone support

- Close location within range: (Close − Low) / (High − Low) — expressed as a percentage

- RSI2 reading and what it confirms or contradicts about the session direction

**2c.  Sequence Assessment**

After classifying individual sessions, assess the [LOOKBACK_SHORT]-day sequence as a whole:

- Continuation: direction persists, low overlap, closes travel in one direction

- Compression: ranges narrowing, overlap increasing, RSI2 converging toward 50

- Indecision: alternating direction, prominent wicks on both sides, RSI2 oscillating

- Exhaustion: final session(s) show extended range with close reverting toward prior open, or wick dominates body on extended move

**2d.  Support and Resistance**

Identify the nearest support and resistance levels derivable directly from the [LOOKBACK_SHORT]-day validated OHLC structure. Only reference levels observable in the data — do not import levels from outside this window unless explicitly labelled as structural.

| **STEP 3** | **5-WEEK REGIME BLOCK — Medium-Term Structure** |
| --- | --- |

Using the last [LOOKBACK_MEDIUM] valid sessions for [PRIMARY_ASSET], assess the medium-term price structure across the following four dimensions:

**3a.  Overlap Ratio**

- For each session pair, measure how much of session N’s High–Low range overlaps session N−1’s range.

- High overlap (> 0.55) → market is range-bound. Low overlap (< 0.45) → directional progression.

**3b.  Directional Persistence**

- Measure: proportion of sessions where direction matches the prior session, weighted with absolute directional bias.

- Persistence > 0.55 with overlap < 0.45 → trending signal. Persistence < 0.50 with overlap > 0.55 → ranging signal.

**3c.  Range Position Bias**

- Where does the most recent close sit within the [LOOKBACK_MEDIUM]-session High–Low range?

- ≥ 67th percentile → Range Top Bias. ≤ 33rd percentile → Range Bottom Bias. Otherwise → Mid-Range.

**3d.  Regime Classification**

- Trending: directional persistence > 0.55, overlap < 0.45, VOLator slope positive (see Step 5), or absolute directional mean > 0.35.

- Ranging: overlap > 0.55, persistence < 0.50, RSI2 median 30–70, absolute directional mean < 0.25.

- Transitional: mixed signals — assign when neither Trending nor Ranging criteria are clearly met.

| **STEP 4** | **SHORT vs MEDIUM-TERM SYNTHESIS** |
| --- | --- |

Combine the Step 2 ([LOOKBACK_SHORT]-day) and Step 3 ([LOOKBACK_MEDIUM]-day) regime reads for [PRIMARY_ASSET] using the matrix below. This synthesis becomes the primary regime input for M4.

| **5-Day Regime** | **5-Week Regime** | **Trade Protocol** |
| --- | --- | --- |
| Trending Bullish | Trending Bullish | High conviction — trend continuation / pullback entries in trend direction |
| Trending Bearish | Trending Bearish | High conviction — trend continuation / pullback entries in trend direction |
| Trending (either) | Ranging | Tactical breakout attempt — treat as range-edge test; reduced size |
| Ranging | Trending (either) | Pullback / consolidation within trend — favour trend resumption; avoid fade |
| Ranging | Ranging | Range-bound — buy low / sell high at validated range extremes |
| Transitional (any) | Any | Reduced conviction — wait for confirmation before committing |

When [SECONDARY_ASSET_1] or [SECONDARY_ASSET_2] diverge from this synthesis — for example, showing opposite regime — flag it explicitly as a caution. Do not suppress it.

| **STEP 5** | **VOLATOR — COMPARATIVE VOLATILITY ENGINE** |
| --- | --- |

Compute scaled comparative volatility for [PRIMARY_ASSET] and each of [COUNTER_1], [COUNTER_2], [COUNTER_3], [COUNTER_4], [COUNTER_5] across the [LOOKBACK_MEDIUM]-session window. Also include [SECONDARY_ASSET_1] and [SECONDARY_ASSET_2] if populated. Use [VOL_METHOD] and [SCALE_METHOD].

**5a.  Volatility Calculation — [VOL_METHOD]**

- [VOL_METHOD] = ATR: rolling true range mean. TR = max(High−Low, |High−PrevClose|, |Low−PrevClose|).

- [VOL_METHOD] = Modified_ATR: body-weighted ATR; reduces wick dominance. TR_mod = body + 0.5 × wick.

- [VOL_METHOD] = StdDev: rolling standard deviation of close-to-close percentage returns.

- [VOL_METHOD] = StdDev_Body: rolling standard deviation of (Close−Open)/Open body returns.

- [VOL_METHOD] = Parkinson: sqrt(rolling mean of (ln(High/Low))² / (4 × ln 2)).

- [VOL_METHOD] = Garman_Klass: sqrt(rolling mean of 0.5(ln H/L)² − (2ln2−1)(ln C/O)²).

- [VOL_METHOD] = Sortino_Dominant: use the larger of upside RMS and downside RMS; sign indicates which dominates.

Normalise raw volatility by price (divide by Close) before scaling unless [VOL_METHOD] already returns a dimensionless ratio (StdDev, Parkinson, Garman_Klass, Sortino variants).

**5b.  Scaling — [SCALE_METHOD]**

- [SCALE_METHOD] = historical (default): z-score each asset’s current volatility against its own rolling mean and standard deviation across the [LOOKBACK_MEDIUM] window, then clip to −1 / +1.

- [SCALE_METHOD] = percentile: rank each asset’s current volatility within the cross-section; output 2p−1 where p is the percentile rank (range −1 to +1).

- [SCALE_METHOD] = zscore: z-score within the current cross-section snapshot; clip at ±2 standard deviations then divide by 2.

- [SCALE_METHOD] = minmax: (val − min) / (max − min) rescaled to −1 / +1 within current cross-section.

**5c.  VOLator Slope**

Fit a linear trend to the last 10 observations of the scaled VOLator series for [PRIMARY_ASSET]. A positive slope confirms volatility expansion (trending signal). A negative slope confirms contraction (ranging / transitional signal). Report this slope to Step 3d and Step 4 synthesis.

| **STEP 6** | **CROSS-ASSET CONFIRMATION** |
| --- | --- |

For each of [COUNTER_1], [COUNTER_2], [COUNTER_3], [COUNTER_4], [COUNTER_5], [SECONDARY_ASSET_1], and [SECONDARY_ASSET_2] (skip blanks), state:

- 5-day price direction: Rising / Falling / Flat (based on net change over the [LOOKBACK_SHORT] validated sessions)

- Mechanism: explain the causal channel to [PRIMARY_ASSET], not just the correlation direction

- Confirmation status: Confirms / Contradicts / Neutral relative to the Step 4 synthesis regime

Standard causal interpretations (adapt as appropriate for the asset class):

- [COUNTER_1] (USDX) Rising → tighter global financial conditions; typically negative for risk assets, commodities, and EM FX. Falling → easier conditions.

- [COUNTER_2] (VIX or 10Y) Rising VIX → risk-off; Rising 10Y → rate-driven demand reduction for yield-sensitive assets.

- [COUNTER_3] (Gold) Rising → defensive / inflation premium / real yield compression. Falling → risk-on or rising real yields.

- [COUNTER_4] (Oil) Rising → inflation / supply pressure / growth proxy. Falling → demand concern or supply surplus.

- [COUNTER_5] (SPX or equivalent) Rising → risk appetite supportive. Falling → risk-off, negative for correlated assets.

State explicitly whether the cross-asset read confirms, contradicts, or is neutral relative to the Step 4 regime synthesis. If it contradicts, flag it in the Agent Log and in M4 Section 10 — do not resolve it away silently.

| **STEP 7** | **KAUFMAN EFFICIENCY RATIO (KER)** |
| --- | --- |

**7a.  Calculation**

Compute the KER for [PRIMARY_ASSET] using a lookback of [KAUFMAN_PERIOD] daily sessions:

- Directional move: |Close_today − Close_(today − [KAUFMAN_PERIOD])|

- Total path: Σ |Close_i − Close_(i−1)| over the same [KAUFMAN_PERIOD] sessions

- KER = Directional move / Total path. Range: −1.0 to +1.0. Multiply by sign(Close_today − Close_(today−period)) to preserve direction.

Apply a [KAUFMAN_EMA_SMOOTH]-period EMA to the raw KER series to produce the smoothed KER. Use the smoothed KER for all classification below.

**7b.  Classification**

| **Smoothed KER Value** | **Classification** | **Condition** |
| --- | --- | --- |
| > +[KAUFMAN_TREND_THRESHOLD] | Trending Up — Strong | Smoothed KER above threshold AND the smoothed KER series itself is rising |
| > +[KAUFMAN_TREND_THRESHOLD] | Trending Up — Moderate | Smoothed KER above threshold AND the smoothed KER series is flat or mixed |
| < −[KAUFMAN_TREND_THRESHOLD] | Trending Down — Strong | Smoothed KER below −threshold AND the smoothed KER series itself is falling |
| < −[KAUFMAN_TREND_THRESHOLD] | Trending Down — Moderate | Smoothed KER below −threshold AND the smoothed KER series is flat or mixed |
| +[KAUFMAN_RANGEUP_THRESHOLD] to +[KAUFMAN_TREND_THRESHOLD] | Ranging — Upward Bias | KER in the upper inner band |
| −[KAUFMAN_TREND_THRESHOLD] to −[KAUFMAN_RANGEUP_THRESHOLD] | Ranging — Downward Bias | KER in the lower inner band |
| Within ±[KAUFMAN_RANGEUP_THRESHOLD] | Ranging — Neutral | KER inside the innermost neutral band |

Thresholds in the table above use the values declared in [KAUFMAN_TREND_THRESHOLD] and [KAUFMAN_RANGEUP_THRESHOLD]. Do not hard-code the numbers — reference the variables so they remain editable from M1.

**7c.  Integration**

Report the KER classification alongside the Step 4 synthesis. Where KER agrees with the regime synthesis, it increases confidence. Where KER disagrees — for example, KER shows Ranging Neutral while Step 4 shows Trending — flag it as a mixed signal and state it explicitly in Step 10 and in M4.

| **STEP 8** | **FLOOR PIVOT ANALYSIS** |
| --- | --- |

Calculate floor pivots for [PRIMARY_ASSET] for each timeframe where the corresponding toggle is set to YES:

- [PIVOT_DAILY] = YES → calculate using prior day H / L / C

- [PIVOT_WEEKLY] = YES → calculate using prior week H / L / C

- [PIVOT_MONTHLY] = YES → calculate using prior month H / L / C

**8a.  Formula**

- P = (H_prior + L_prior + C_prior) / 3

- R1 = 2P − L_prior  |  R2 = P + (H_prior − L_prior)  |  R3 = H_prior + 2(P − L_prior)  |  R4 = R3 + (H_prior − L_prior)  |  R5 = R4 + (H_prior − L_prior)

- S1 = 2P − H_prior  |  S2 = P − (H_prior − L_prior)  |  S3 = L_prior − 2(H_prior − P)  |  S4 = S3 − (H_prior − L_prior)  |  S5 = S4 − (H_prior − L_prior)

| **SOURCE RULE** Prior-period H / L / C must each be verified by at least two independent sources within the stated corroboration tolerance before any pivot levels are computed. If fewer than two sources are available, mark all pivot levels for that timeframe ‘indicative — single source only’ in the table and in the chart. |
| --- |

**8b.  Table Display Order  (mandatory)**

Always top-to-bottom in both the table and any printed listing:  R5 → R4 → R3 → R2 → R1 → P → S1 → S2 → S3 → S4 → S5.  Never sort by ascending value. Resistance at the top; support at the bottom.

**8c.  Smart Chart Scale  (mandatory when [CHART_PIVOT] = YES)**

- Do NOT plot all 33 levels. Extreme Y-axis span makes the candle invisible.

- Pool all levels from all active timeframes into one flat list. Select: [PIVOT_ABOVE_BELOW_DAILY] nearest levels above candle HIGH (daily timeframe), [PIVOT_ABOVE_BELOW_WEEKLY] above from weekly, [PIVOT_ABOVE_BELOW_MONTHLY] above from monthly — plus the equivalent numbers below candle LOW — plus all levels inside the H–L range from any timeframe.

- Scale Y-axis to the selected subset only, with 15% margin top and bottom. The tallest candle plotted must occupy ≥ 15% of the Y-axis span.

- Number of candles: draw [PIVOT_CANDLES_N] candles of [PIVOT_CANDLES_TF] timeframe. With the default settings ([PIVOT_CANDLES_N] = 2, [PIVOT_CANDLES_TF] = WEEKLY): draw the prior completed week’s candle and the current (in-progress) week’s candle. Annotate each candle’s OHLC values on the left margin: O = open, H = high (bold), L = low (bold), C = close (bold, orange). Label each candle by its period (e.g., ‘W/E 11 Apr’, ‘W/E 18 Apr current’).

- Chart title format: ‘[PRIMARY_ASSET] — Pivot Structure | [Period descriptor]  (e.g., Week of DD Mon YYYY)’. Do not include variable names or configuration values in the chart title or subtitle.

**8d.  Position Narrative**

For each active timeframe, state where the most recent close of [PRIMARY_ASSET] sits relative to the pivot structure: above / below / at P; approaching / testing / through R1 or S1; inside a confluence zone where daily, weekly, and monthly levels are within 0.05% of each other.

| **STEP 9** | **CHART GENERATION** |
| --- | --- |

Produce only the charts whose toggle is set to YES in M1. Apply the specifications below exactly.

**9a.  Candlestick Chart  [CHART_CANDLESTICK]**

- Exactly [LOOKBACK_SHORT] validated candles for [PRIMARY_ASSET]. Green fill = Close ≥ Open. Red fill = Close < Open. Black wick lines. X-axis labels: date of each session. Title states asset, date range, and unit.

**9b.  Open=0 Distance Chart  [CHART_OPEN_ZERO]**

- For each of the [LOOKBACK_SHORT] sessions, set Open' = 0 and plot: High' = High − Open, Low' = Low − Open, Close' = Close − Open. Purpose: exposes directional travel and rejection normalised to each session’s open level. Y-axis label: ‘Distance from Open  ([UNIT_OF_MEASURE])’.

**9c.  5-Week Structure Chart  [CHART_5WEEK]**

- Plot all [LOOKBACK_MEDIUM] sessions for [PRIMARY_ASSET] as colour-coded vertical bars (green = bullish, red = bearish, grey = neutral) with a close-line overlay. Purpose: makes overlap, directional persistence, and range rotation visually evident.

**9d.  VOLator Chart  [CHART_VOLATOR]**

- Plot the scaled volatility series (−1 to +1) for [PRIMARY_ASSET] and all active counters across the [LOOKBACK_MEDIUM]-session window. Reference lines at 0, +0.5, −0.5. Legend labels each series by name. Title states method: [VOL_METHOD] / [SCALE_METHOD].

**9e.  Pivot Chart  [CHART_PIVOT]**

- Apply smart-scale algorithm from Step 8c. Draw [PIVOT_CANDLES_N] candles of [PIVOT_CANDLES_TF] timeframe for [PRIMARY_ASSET] (default: prior week candle + current week candle). Colour-code pivot lines by timeframe: daily = blue solid, weekly = purple dashed, monthly = red dash-dot. Do not display variable names or configuration values anywhere on the chart.

| **STEP 10** | **FINAL TECHNICAL JUDGEMENT SYNTAX** |
| --- | --- |

| **This seven-line block is mandatory output. M4 cannot function correctly without it. Output it verbatim as the final element of this module, then feed it into M4 Section 1 (Executive Snapshot) and M4 Section 17 (Forecast).** |
| --- |

Complete exactly these seven lines using the results of Steps 2–9:

**Short-term technical state:   **[Trending / Ranging / Transitional]  —  [Bullish / Bearish / Mixed]   *(from Step 2 + Step 4 synthesis)*

**Medium-term technical state:  **[Trending / Ranging / Transitional]  —  [Bullish / Bearish / Mixed]   *(from Step 3 + Step 4 synthesis)*

**KER regime confirmation:      **[Classification from Step 7]  —  [Agrees with / Contradicts / Neutral vs Step 4]

**Preferred trade protocol:     **[Trend pullback / Range fade / Reduced conviction]   *(from Step 4 matrix)*

**Integration note:             **[M4 forecast / macro / sentiment should lean with / oppose / remain cautious]

**Pivot reference:              **[Close vs nearest D.P / W.P / M.P — above / below / testing / at confluence]   *(from Step 8d)*

**Source status:                **[Corroborated: Source_A × Source_B | Sources tried: N | Un-corroborated fields: none / list]

| **STEP 11** | **NAMED OUTPUT SURFACE  (for M5 / downstream module consumption)** |
| --- | --- |

| **Required when [PRODUCE_STRATEGY_RECOMMENDATIONS] = YES.  Optional otherwise.** This step adds no new analysis. It exposes values already produced in Steps 2–8 under stable, addressable names so that M5 (Strategies) can consume them deterministically. No value here may be synthesised or estimated — every entry must be traceable to its originating step. |
| --- |

**11a.  Surface contract**

Emit the following named values for [PRIMARY_ASSET] only.  Counter and secondary assets do not appear in this surface.  Every value is dated to [AS_OF_DATE].  Values are reported in [UNIT_OF_MEASURE] and (where applicable) [TICK_NAME] units.

| **Named output** | **Source step** | **Definition / format** |
| --- | --- | --- |
| atr_14 | Step 5 (VOLator) | ATR on [PRIMARY_ASSET], 14-session lookback. Native units — same as price. Required scalar. |
| rsi2_latest | Step 2 | Most recent RSI2 value for [PRIMARY_ASSET]. Range 0–100. |
| swing_high_5d / swing_low_5d | Step 2 (5-day block) | Highest high and lowest low across the [LOOKBACK_SHORT] validated sessions. Two scalars in price units. |
| swing_high_25d / swing_low_25d | Step 3 (5-week block) | Highest high and lowest low across the [LOOKBACK_MEDIUM] validated sessions. Two scalars in price units. |
| fractal_swings | Step 2 / 3 | Ordered list of fractal swing points (high/low + index + magnitude) detected over the lookback. Used by M5 §4b for adaptive fib anchor selection. Empty list if no fractal qualifies. |
| pivots_daily, pivots_weekly, pivots_monthly | Step 8 | For each timeframe where the M1 toggle is YES: dict of {P, R1..R5, S1..S5}, plus a corroboration flag (CORROBORATED / SINGLE-SOURCE-INDICATIVE). Skip the timeframe entirely if its toggle is NO. |
| nearest_support, nearest_resistance | Step 2d | Nearest support and resistance levels visible in the 5-day OHLC structure. Two scalars in price units. |
| ker_value, ker_class | Step 7 | Smoothed KER scalar in [−1, +1] and the seven-bucket classification label. |
| volator_slope | Step 5c | Linear slope of the last 10 scaled VOLator observations for [PRIMARY_ASSET]. |
| cross_asset_confirm | Step 6 | One of {CONFIRM, CONTRADICT, MIXED, NEUTRAL}. Aggregate over the active counters using the rule in §11c below. |
| regime_label | Steps 4 + 5 + 7  (composite) | One of {TREND_UP, TREND_DOWN, RANGE, TRANSITION}. Mapping rule in §11b below. |
| sentiment_tilt | From M2 §13b | Pass-through of the numeric tilt for [PRIMARY_ASSET]. M3 does not recompute it; it forwards the M2 value into the surface so that M5 has a single contract to read. |
| seven_line_judgement | Step 10 | The full seven-line block as a structured object with one named field per line. |

**11b.  Consolidated regime_label — mapping rule**

regime_label is a function of the Step 4 synthesis, the KER classification (Step 7), and the VOLator slope (Step 5c). The mapping is deterministic and must produce exactly one of the four labels.

| **regime_label** | **Conditions  (all must hold)** |
| --- | --- |
| TREND_UP | Step 4 synthesis = ‘Trending Bullish — Trending Bullish’  OR  (Step 4 = ‘Trending Bullish (any)’  AND  ker_class ∈ {Trending Up — Strong, Trending Up — Moderate}  AND  volator_slope ≥ 0). |
| TREND_DOWN | Mirror of TREND_UP — bearish across all three signals. |
| RANGE | Step 4 synthesis = ‘Ranging — Ranging’  AND  │ker_value│ < [KAUFMAN_TREND_THRESHOLD]  AND  volator_slope ≤ 0.  Both KER and VOLator gates must pass — this is the dual-gate rule M5 §3a depends on. |
| TRANSITION | Default fall-through — used when Step 4 returns ‘Transitional (any)’, when KER and VOLator disagree, or when any single gate for TREND_UP / TREND_DOWN / RANGE fails to be unambiguously satisfied. |

*ℹ  **regime_label is the contract M5 §3 consumes. Do not relax the dual-gate RANGE rule — a label of RANGE without both KER and VOLator confirmation will cause M5 to construct a Trade 3B mean-reversion card on a market that may already be transitioning out of the range.*

**11c.  cross_asset_confirm — aggregation rule**

Each active counter from Step 6 emits a per-counter label of Confirms / Contradicts / Neutral. Aggregate to a single value as follows:

- CONFIRM if ≥ 60% of active counters confirm and none contradict.

- CONTRADICT if ≥ 60% of active counters contradict.

- MIXED if confirms and contradicts both occur (regardless of proportion).

- NEUTRAL if all active counters are Neutral, or if fewer than two counters are active.

**11d.  Single-source flagging on the surface**

Any pivot level emitted on the surface that came from a single-source prior-period H/L/C carries the SINGLE-SOURCE-INDICATIVE corroboration flag.  M5 reads this flag and suppresses Trade 2 entirely if all accessible pivot tiers for the active direction are SINGLE-SOURCE-INDICATIVE.  Do not strip the flag for compactness — it is part of the contract.

**11e.  Worked example (illustrative)**

To illustrate the format, not to define values. Real values come from the live data.

| **Field** | **Example value** |
| --- | --- |
| atr_14 | 0.0058  (EUR/USD — 58 pips) |
| rsi2_latest | 32.4 |
| swing_high_5d / swing_low_5d | 1.0921 / 1.0834 |
| swing_high_25d / swing_low_25d | 1.1015 / 1.0789 |
| pivots_daily | {P: 1.0876, R1: 1.0902, R2: 1.0930, S1: 1.0850, S2: 1.0824, ..., flag: CORROBORATED} |
| ker_value, ker_class | −0.18, ‘Trending Down — Moderate’ |
| volator_slope | +0.04 |
| cross_asset_confirm | CONFIRM  (USDX rising, VIX rising → both consistent with EUR/USD bearish bias) |
| regime_label | TREND_DOWN |
| sentiment_tilt | −0.31  (passed through from M2 §13b) |

**M4 INTEGRATION FLAGS — WHERE M3 OUTPUTS MUST FLOW**

| **M4 Section** | **Must receive from M3** |
| --- | --- |
| §1  Executive Snapshot | Short-term + medium-term regime, KER read, and Seven-Line Judgement (all of Step 10) |
| §6  OHLC + RSI2 Table | Full validated 5-day table from Step 2 including Source A / B / Validation Outcome columns |
| §7  Charts | All charts produced in Step 9 (subject to [CHART_*] toggles) |
| §8  Short-Term Technical | Candle classification and sequence assessment from Step 2b–2d |
| §9  Medium-Term Regime | Regime classification, overlap, persistence, range bias from Step 3 + VOLator slope from Step 5 |
| §10 Cross-Asset Analysis | Full counter directional reads, mechanisms, and confirmation status from Step 6 |
| §11 Pivot Analysis | Tables, chart, and position narrative from Step 8 |
| §15 Bull / Bear Balance | Must cross-reference pivot position and regime from Steps 4 + 8 |
| §16 Forward View | Must state whether it respects or contradicts M3 regime classification; flag if contradicting |
| §17 Forecast (1 sentence) | Derived from Step 10 integration note — exactly one sentence, no hedging |
| §21 Strategy Recommendations  (via M5) | Step 11 Named Output Surface — ATR(14), swings, pivots with corroboration flag, regime_label, ker / VOLator / cross-asset / sentiment_tilt. Consumed by M5 only when [PRODUCE_STRATEGY_RECOMMENDATIONS] = YES. |

*Modular Prompt Architecture v2.1  │  M3 Fixed Technical Analysis Module  │  April 2026*

M3 │ April 2026 │ page  of