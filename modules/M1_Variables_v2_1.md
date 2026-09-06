*M1 — Variables  │  Modular Prompt Architecture v2.1*

| **M1   MODULE 1 — VARIABLES** *EDIT ONLY THIS SECTION  ·  All other modules are fixed and must not be changed* *Modular Prompt Architecture v2.1  │  April 2026* |
| --- |

| **M1  VARIABLES** *← You are here* | **M2  RESEARCH STD** *Fixed — do not edit* | **M3  TECHNICAL** *Fixed — do not edit* | **M4  OUTPUT** *Fixed — do not edit* |
| --- | --- | --- | --- |

| **A   ***ROLE **&** SCOPE* |
| --- |

| **Variable** | **Default** | **Options / Description** |
| --- | --- | --- |
| **[ROLE_TITLE]** |  | e.g., Senior Equity Analyst / FX Strategist / Commodity Analyst |
| **[PRIMARY_ASSET]** |  | Ticker or instrument name — e.g., SPX / GBP/USD / BTC / CL=F / Palm Oil futures |
| **[COMMODITY]** |  | Commodity analyses only: common name — e.g., palm oil / soybean oil / crude oil. Leave blank for FX, equity, or crypto. |
| **[PRODUCT_SPECIFICATION]** |  | Commodity analyses only: exact grade or contract spec — e.g., crude palm oil / RBD palm olein / WTI light sweet. Leave blank otherwise. |
| **[SECONDARY_ASSET_1]** |  | Primary comparator or secondary instrument for analysis — e.g., USDX / Brent / HO / EURUSD |
| **[SECONDARY_ASSET_2]** |  | Second comparator if required — e.g., VIX / Natural Gas / Soybean Oil / EURGBP. Leave blank if not needed. |
| **[ASSET_CLASS]** |  | e.g., Equity Index / FX / Crypto / Commodity / Fixed Income |
| **[MARKET_SCOPE]** | **Global** | global / regional / country-specific |
| **[PRIMARY_REGION]** |  | Main geographic focus — e.g., Southeast Asia / Black Sea / EU / MENA / North America. Leave blank for global-scope analyses. |
| **[DECISION_USE_CASE]** |  | e.g., trading, risk review, procurement, management update |

| **B   ***PRICE **&** MARKET DEFINITION* |
| --- |

| **Variable** | **Default** | **Options / Description** |
| --- | --- | --- |
| **[PRICE_OBJECTIVE]** |  | Current consensus market price / fair value range |
| **[PRICE_BASIS]** |  | e.g., spot / nearby futures / FOB / CIF / settlement |
| **[DELIVERY_BASIS]** |  | e.g., CME front month / FOB Malaysia / London spot |
| **[UNIT_OF_MEASURE]** |  | e.g., USD/mt / cents/lb / index points / USD |
| **[CURRENCY]** | **USD** | e.g., USD / EUR / GBP / MYR |
| **[TICK_SIZE]** |  | Smallest price increment for the primary asset, in [UNIT_OF_MEASURE]. Examples: EUR/USD = 0.0001 (one pip). WTI futures = 0.01 (one cent). ES futures = 0.25 (one quarter-point). S&P 500 cash = 0.01. Required when [PRODUCE_STRATEGY_RECOMMENDATIONS] = YES; may be left blank otherwise. |
| **[TICK_NAME]** |  | Native execution-unit label for the primary asset. Examples: EUR/USD = pip / WTI = tick / ES = tick / S&P 500 cash = point / Gold = tick. Required when [PRODUCE_STRATEGY_RECOMMENDATIONS] = YES; may be left blank otherwise. |
| **[AS_OF_DATE]** |  | Insert exact date — e.g., 15 April 2026 |
| **[AS_OF_TIMEZONE]** | **UTC** | e.g., America/New_York / Europe/London / Asia/Singapore |
| **[LOOKBACK_WINDOW]** | **5 days** | Consensus research window — e.g., last 5 trading days / last 10 calendar days |

| **C   ***SOURCE **&** RESEARCH CONFIGURATION* |
| --- |

| **Variable** | **Default** | **Options / Description** |
| --- | --- | --- |
| **[MINIMUM_SOURCE_COUNT]** | **6** | Minimum independent sources for consensus price build |
| **[PRIORITY_SOURCE_TYPES]** |  | e.g., exchange data, price reporting agencies, broker notes, trade press |
| **[BENCHMARKS_TO_INCLUDE]** |  | e.g., CME, Yahoo Finance, Investing.com, Twelve Data, ECB, FRED |
| **[GEOGRAPHIC_PRICE_REFERENCES]** |  | Key origins/destinations to compare across regions — e.g., FOB Malaysia vs CIF India vs Rotterdam |
| **[COMPARISON_PRODUCTS]** |  | Competing assets or nearby substitutes |
| **[CONSENSUS_METHOD]** | **weighted median** | weighted median / median / weighted average |
| **[RESTRICTIONS]** |  | e.g., no paywalled-only claims; avoid data older than X days |

| **D   ***CROSS-ASSET COUNTERS* |
| --- |

USDX is the mandatory first counter for all asset classes. Remove COUNTER_3–5 if not applicable.

| **Variable** | **Default** | **Options / Description** |
| --- | --- | --- |
| **[COUNTER_1]** | **DX-Y.NYB** | USDX — mandatory. Dollar liquidity / financial conditions proxy |
| **[COUNTER_2]** | **^VIX** | VIX (equity/crypto) or ^TNX 10Y yield (FX/rates). Delete if not applicable |
| **[COUNTER_3]** | **GC=F** | Gold — safe-haven / real yield proxy. Delete if not applicable |
| **[COUNTER_4]** | **CL=F** | Crude Oil — growth / inflation proxy. Delete if not applicable |
| **[COUNTER_5]** | **^GSPC** | S&P 500 — risk appetite / global equity beta. Delete if not applicable |
| **[COUNTER_EXTRAS]** |  | Optional: BTC-USD / EURUSD=X / bond futures / etc. |

| **E   ***TECHNICAL ANALYSIS CONFIGURATION  (consumed by M3)* |
| --- |

Populate the values below. Do not modify the methodology — that is governed by M3.

**E.1  Lookback Windows**

| **Variable** | **Default** | **Options / Description** |
| --- | --- | --- |
| **[LOOKBACK_SHORT]** | **5** | Valid trading sessions — 5-day execution block (fixed by M3 convention) |
| **[LOOKBACK_MEDIUM]** | **25** | Valid trading sessions — 5-week regime block (fixed by M3 convention) |

**E.2  Volatility Engine (VOLator)**

| **Variable** | **Default** | **Options / Description** |
| --- | --- | --- |
| **[VOL_METHOD]** | **ATR** | ATR / Modified_ATR / StdDev / StdDev_Body / Parkinson / Garman_Klass / Sortino_Dominant |
| **[SCALE_METHOD]** | **historical** | historical / percentile / zscore / minmax |

*ℹ  **RSI2 (period = 2) is fixed across all analyses. It is not a configurable variable — do not change the period.*

**E.3  Chart Output Toggles**

Set YES to produce the chart; NO to suppress it. All five default to YES.

| **Control** | **Default** | **Enables / disables** |
| --- | --- | --- |
| [CHART_CANDLESTICK] | YES | 5-Session OHLC candlestick chart |
| [CHART_OPEN_ZERO] | YES | 5-Session Open=0 distance chart (each day normalised to Open=0) |
| [CHART_5WEEK] | YES | 5-Week day-by-day structure chart (~25 sessions) |
| [CHART_VOLATOR] | YES | VOLator comparative volatility chart (primary asset + all counters) |
| [CHART_PIVOT] | YES | Smart-scale floor pivot chart for the most recent session |

**E.4  Pivot Controls**

Toggle which pivot timeframes to calculate and include in the output table. Then set how many levels to show above and below the candle range in the chart. Levels inside the candle H–L range are always shown regardless of these numbers.

**Pivot timeframe — include in calculation:**

| **Control** | **Default** | **Enables / disables** |
| --- | --- | --- |
| [PIVOT_DAILY] | YES | Calculate and display daily pivot levels using prior day H / L / C |
| [PIVOT_WEEKLY] | YES | Calculate and display weekly pivot levels using prior week H / L / C |
| [PIVOT_MONTHLY] | YES | Calculate and display monthly pivot levels using prior month H / L / C |

**Levels to display above HIGH and below LOW in pivot chart:**

| **Variable** | **Default** | **Options / Description** |
| --- | --- | --- |
| **[PIVOT_ABOVE_BELOW_DAILY]** | **3** | Number of daily levels to show above candle HIGH and below candle LOW in the smart-scale chart (e.g., 3 = D.R1/R2/R3 above; D.S1/S2/S3 below) |
| **[PIVOT_ABOVE_BELOW_WEEKLY]** | **3** | Number of weekly levels above HIGH and below LOW |
| **[PIVOT_ABOVE_BELOW_MONTHLY]** | **3** | Number of monthly levels above HIGH and below LOW |

*ℹ  **All pivot levels that fall inside the candle HIGH–LOW range are always shown regardless of the above counts. These controls only affect levels outside the candle body.*

**Pivot chart candle configuration:**

| **Variable** | **Default** | **Options / Description** |
| --- | --- | --- |
| **[PIVOT_CANDLES_N]** | **2** | Number of candles to draw on the pivot chart. Default 2 = prior period candle + current (in-progress) period candle. Increase to add further historical context. |
| **[PIVOT_CANDLES_TF]** | **WEEKLY** | Timeframe of candles drawn on the pivot chart. Default WEEKLY — draws weekly candles, naturally aligning with weekly pivot levels. Options: DAILY / WEEKLY / MONTHLY. |

*ℹ  **With defaults (2 candles, WEEKLY): the pivot chart shows the previous week**'**s completed candle and the current week**'**s in-progress candle, plotted against all active pivot levels. This gives the cleanest short-term structural context without over-crowding the chart.*

**E.5  Kaufman Efficiency Ratio (KER)**

The KER measures directional efficiency: how much of the total price path covered the distance in a straight line over the lookback. Range: −1.0 (perfectly efficient downtrend) to +1.0 (perfectly efficient uptrend). Values near zero indicate noisy, non-directional price action. A short EMA is applied to the raw KER before classification to reduce single-session noise.

| **Variable** | **Default** | **Options / Description** |
| --- | --- | --- |
| **[KAUFMAN_PERIOD]** | **13** | Lookback in daily sessions for KER calculation |
| **[KAUFMAN_EMA_SMOOTH]** | **3** | EMA period applied to the raw KER series before classification. Smooths noise without adding significant lag. |
| **[KAUFMAN_TREND_THRESHOLD]** | **0.13** | Absolute KER level above which the market is classified as trending. Symmetric: +0.13 = trending up; −0.13 = trending down |
| **[KAUFMAN_RANGEUP_THRESHOLD]** | **0.09** | Inner band boundary. KER within ±0.09 = Ranging Neutral. 0.09 to 0.13 = Ranging with upward bias. −0.13 to −0.09 = Ranging with downward bias. |

**Classification logic (applied to the smoothed KER series):**

| **KER Value** | **Classification** | **Logic** |
| --- | --- | --- |
| > +[KAUFMAN_TREND_THRESHOLD] | Trending Up — Strong | Smoothed KER above threshold AND rising |
| > +[KAUFMAN_TREND_THRESHOLD] | Trending Up — Moderate | Smoothed KER above threshold AND flat / mixed |
| < −[KAUFMAN_TREND_THRESHOLD] | Trending Down — Strong | Smoothed KER below −threshold AND falling |
| < −[KAUFMAN_TREND_THRESHOLD] | Trending Down — Moderate | Smoothed KER below −threshold AND flat / mixed |
| +[KAUFMAN_RANGEUP_THRESHOLD] to +[KAUFMAN_TREND_THRESHOLD] | Ranging — Upward Bias | KER in upper inner band |
| −[KAUFMAN_TREND_THRESHOLD] to −[KAUFMAN_RANGEUP_THRESHOLD] | Ranging — Downward Bias | KER in lower inner band |
| Within ±[KAUFMAN_RANGEUP_THRESHOLD] | Ranging — Neutral | KER inside the inner neutral band |

*ℹ  **Strong vs Moderate distinction: if the smoothed KER is itself rising (for positive trending values) or falling (for negative trending values), classify as Strong; otherwise Moderate.*

| **F   ***SCENARIO **&** OUTPUT* |
| --- |

| **Variable** | **Default** | **Options / Description** |
| --- | --- | --- |
| **[SCENARIO_HORIZON]** |  | e.g., next 5 trading days / next 2 weeks / next 30 days |
| **[CONFIDENCE_SCALE]** | **H/M/L** | Low / Medium / High — or 1–5 if a numeric scale is preferred |
| **[OUTPUT_LENGTH]** | **standard** | concise / standard / detailed — see definition table below |
| **[ADDITIONAL_CONTEXT]** |  | Insert any specific concern: earnings, FOMC, geopolitical event, data release, seasonal factor |

**Output length — precise section-by-section definition:**

| **Section** | **Concise** | **Standard** | **Detailed** |
| --- | --- | --- | --- |
| §1–3  Exec Snapshot / Definition / Price Call | Full | Full | Full |
| §4  Price Evidence Table | Omit — sources listed in §3 only | Full table | Full + extended normalization notes |
| §5  Consensus Build Explanation | Omit | Full | Full |
| §6  OHLC + RSI2 Table | Date / OHLC / RSI2 / Trend only — source columns omitted | Full 11-column table | Full + extended validation notes |
| §7  Charts | Charts 1 + 2 only (Candlestick, Open=0) | All toggled charts | All charts |
| §8  Short-Term Technical Analysis | Sequence label + 2-sentence summary | Full session-by-session commentary | Full + inter-session pattern analysis |
| §9  Medium-Term Regime & VOLator | Classification + trade protocol — no metric values | Full with metric values | Full + rolling regime history |
| §10  Cross-Asset Analysis | Omit | Full | Full + extended mechanism paragraphs |
| §11  Floor Pivot Analysis | Omit | Full — all active timeframes | Full — all timeframes |
| §12  Key Market Considerations | Direction label + 1 sentence per factor | Full — all material factors | Full + structural vs cyclical data tables |
| §13  Sentiment & News | Top 2 articles + aggregate only — calendar omitted | Full table + full two-part calendar | Full + extended calendar (2 extra weeks) |
| §14  Macro Context | 3–4 bullets maximum | Full | Full + global spillovers, positioning detail |
| §15  Bull / Bear Balance | 3 risks each side | Full | Full + scenario price targets |
| §16  Forward View | Direction + range only — condensed | Full scenario analysis | Full + probability-weighted scenario table |
| §17  Forecast (1 sentence) | Always included | Always included | Always included |
| §18  Final Analyst Judgement | Always included | Always included | Always included |
| §19  Source Discipline Note | Omit | Full | Full |
| §20  Agent Log | Omit | Full structured log | Full + all source attempts + protocol audit trail |
| §21  Strategy Recommendations | Trade cards 1–3 only — no backtest, no aggregate | Full §21a/b/c/d (cards + 5-day backtest + ‘what is working’ aggregate) | Full + per-trade rationale paragraphs and extended confluence narrative |
| Historical context vs prior episodes | Omit | Omit | Added section |
| Scenario analysis table (bull/base/bear) | Omit | Omit | Added section |

*ℹ  **§21 Strategy Recommendations is produced only when [PRODUCE_STRATEGY_RECOMMENDATIONS] = YES (Section H). When NO, §21 is treated as ‘omit’ at all three output levels regardless of [OUTPUT_LENGTH].*

| **G   ***SUPPLEMENTARY OUTPUTS* |
| --- |

| **Variable** | **Default** | **Options / Description** |
| --- | --- | --- |
| **[PRODUCE_IMAGES]** | **YES — PNG** | Produce PNG images of all charts in addition to embedding them in the report. Output to a session-named folder for downstream use. |
| **[PRODUCE_CSV]** | **YES — CSV** | Produce data CSVs for OHLC used, indicators computed, and pivot levels — as a working spreadsheet companion to the report. |

| **H   ***STRATEGY CONTROLS  (consumed by M5)* |
| --- |

Section H governs the regime-aware, three-tier strategies module. Defaults below are the forward-test baseline. Strategy logic, level derivation, regime gates, and backtest are fixed and governed by M5 — do not modify methodology here.

**H.1  Master Switches**

| **Variable** | **Default** | **Options / Description** |
| --- | --- | --- |
| **[PRODUCE_STRATEGY_RECOMMENDATIONS]** | **NO** | Master switch. YES enables the strategies module and adds §21 Strategy Recommendations to the report. NO suppresses the entire module — M5 is skipped and the report ends at §20. |
| **[DAILY_OPEN_ANCHOR]** | **00:00 UK** | 00:00 UK / 07:00 UK. Defines the entry timestamp for the Trade 1 daily directional. Use the value matching when the analysis run completes. For 24-hour assets (FX, futures), 00:00 UK is the natural session open. For S&P 500 cash, 07:00 UK reflects the pre-market window before NY open. |
| **[PRODUCE_PIVOT_TRADE]** | **YES** | Trade 2 gate. YES produces the regime-aware pivot trade card. NO suppresses Trade 2 only. |
| **[PRODUCE_COMPLEX_TRADE]** | **YES** | Trade 3 gate. YES produces the regime-driven complex trade card. Single switch — regime determines whether 3A (momentum-pullback), 3B (mean-reversion), or 3C (transition breakout) is built. NO suppresses Trade 3 only. |
| **[MAX_SIMULTANEOUS_LONG_SHORT]** | **YES** | If YES, opposing trade cards are permitted across the three strategies (e.g., long Trade 1 + short Trade 2 limit at R2). If NO, the most-recent strategy in build order is suppressed when its direction conflicts with an earlier strategy. |

**H.2  Sizing, Risk, and Tranche Management**

| **Variable** | **Default** | **Options / Description** |
| --- | --- | --- |
| **[ATR_STOP_CAP]** | **3.5** | Maximum stop-loss distance in multiples of ATR(14). Trade 1 SL is the tighter of (structural anchor + 0.25 ATR buffer) or this cap. If the structural stop exceeds the cap, the cap applies and position size is reduced rather than the stop tightened. Recommended range 2.5 – 4.5; 3.5 is the forward-test baseline. |
| **[BE_TRAIL_R]** | **0.2** | Runner-stop offset in R-multiples on Unit 2 fill. When the second tranche fills at +2R (or the structural TP2 equivalent), Unit 3 (runner) stop moves to entry ± [BE_TRAIL_R] × R. 0.2 means the runner is locked in at +0.2R minimum — break-even plus a small slippage buffer. Range 0.0 – 1.0; values above 0.5 begin to choke runner upside. |
| **[CONVICTION_THRESHOLD]** | **0.25** | Absolute direction-score threshold below which Trade 1 is suppressed (the directional conviction is too low to express as a market trade). Trades 2 and 3 still produce because they are regime-driven, not score-driven. Range 0.10 – 0.50. |

**H.3  Direction-Scoring Weights**

Six signed-weight contributions to the direction score. Defaults sum to 1.00 and represent the forward-test baseline. These defaults are locked for a minimum of 20 sessions in any new forward-test deployment — tuning before that point destroys the comparability of the §21d ‘what is working’ aggregate.

| **Variable** | **Default** | **Options / Description** |
| --- | --- | --- |
| **[W_SHORT_TECH]** | **0.25** | 5-day technical bias weight (M3 §2a trend + RSI2). |
| **[W_MEDIUM_REGIME]** | **0.20** | 5-week structural regime weight (M3 §3). |
| **[W_VOLATOR]** | **0.10** | VOLator regime weight (M3 §5). |
| **[W_KAUFMAN]** | **0.15** | Kaufman KER classification weight (M3 §7). |
| **[W_SENTIMENT]** | **0.15** | Aggregate sentiment tilt weight (M2 §13b). |
| **[W_CROSS_ASSET]** | **0.15** | Cross-asset confirmation weight (M3 §6 — USDX first, then VIX/Oil/Gold/SPX as relevant). |

*ℹ  **Weights must sum to ≤ 1.00. If a sum **<** 1.00 is supplied (e.g., zero-weighting sentiment), the missing mass is left as ‘residual unallocated’ — direction score is computed on the smaller weight base and logged accordingly. Do not auto-renormalise to 1.00.*

**H.4  Fib Swing Anchor and Backtest**

| **Variable** | **Default** | **Options / Description** |
| --- | --- | --- |
| **[FIB_RANGE_DAYS]** | **4** | Default minimum lookback for fib swing anchor. M5 extends adaptively to a maximum 10 sessions if the swing magnitude is < 2 × ATR(14) at the default lookback. Range 3 – 10. |
| **[BACKTEST_LOOKBACK_DAYS]** | **5** | Number of prior sessions replayed in the §7 no-leakage backtest. Range 3 – 10. Larger windows produce more stable ‘what is working’ aggregates but extend execution time and may straddle regime changes. |

*ℹ  **Trade cards are produced for [PRIMARY_ASSET] only. Secondary and counter assets contribute to direction scoring (via M3 §6 cross-asset reads) but never receive their own trade cards. Section H variables must never appear by name in the report body — per M4 Presentation Rule 2 (No Variable Exposure).*

| **QUICK REFERENCE — WHAT M1 CONTROLS** **A  Role ****&**** Scope:  **Role, primary asset, commodity + spec (if applicable), secondary comparators (1–2), asset class, market scope, region, use case **B  Price ****&**** Market:  **Exact asset, basis, unit, currency, tick size and tick name, date, and research window **C  Source Configuration:  **Minimum sources, source types, benchmarks, geographic price references, consensus method **D  Cross-Asset Counters:  **Which instruments feed the VOLator and cross-asset confirmation (USDX mandatory) **E.1  Lookback Windows:  **Short (5d) and medium (25d) session counts **E.2  Volatility Engine:  **VOLator method and scaling method. RSI2 is fixed at period 2. **E.3  Chart Toggles:  **YES / NO for each of the five chart types **E.4  Pivot Controls:  **Timeframes to calculate + levels above/below candle + candle count and timeframe for pivot chart **E.5  Kaufman KER:  **Period, EMA smoother, trend threshold, range-up threshold, classification logic **F  Scenario ****&**** Output:  **Forecast horizon, confidence scale, output length, additional context **G  Supplementary Outputs:  **Standalone images and CSV tables matching the data and graphs used in the report **H  Strategy Controls:  **Master switches (produce strategies, daily-open anchor, pivot trade, complex trade, simultaneous long/short). Sizing & risk (ATR stop cap, BE trail, conviction threshold). Direction-scoring weights (six signals). Fib lookback and backtest window. |
| --- |

*Modular Prompt Architecture v2.1  │  M1 Variables  │  April 2026*

M1 Variables │ April 2026 │ page  of