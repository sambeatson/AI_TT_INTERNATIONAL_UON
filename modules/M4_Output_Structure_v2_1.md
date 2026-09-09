*M4 — Output Structure  │  Modular Prompt Architecture v2.1  │  DO NOT EDIT*

| **M4   ****MODULE 4 — FIXED OUTPUT STRUCTURE** *DO NOT EDIT  ·  Produce all 21 sections in the exact order shown. Green = technical (M3). Amber = updated specification. Pink = strategies (M5).* *Modular Prompt Architecture v2.1  │  April 2026  │  §21 Strategy Recommendations added (M5 integration)* |
| --- |

| **M1  VARIABLES** *Provides inputs* | **M2  RESEARCH STD** *Governs evidence* | **M3  TECHNICAL** *Governs technicals* | **M4  OUTPUT** *← You are here* |
| --- | --- | --- | --- |

| *Navy = standard section* | *Green = M3 technical section* | *Pink = M5 strategies section* |
| --- | --- | --- |

| **REPORT PRESENTATION RULES — Apply to every section of every report** Violations of these rules expose proprietary methodology. They are not style preferences — they are mandatory. **1. TITLE FORMAT  **[Primary Asset Name] Report — [Horizon descriptor, e.g., Week of DD Month YYYY / Daily: DD Month YYYY]. Subheading: ‘With reference to: [Secondary Asset 1] · [Secondary Asset 2] · [Counter common names, space-separated with dots]’. No ‘Institutional’, no framework names, no model names, no output level label anywhere in the title or header. **2. NO VARIABLE EXPOSURE  **Variable names and values must NEVER appear in report output. Do not write [CHART_CANDLESTICK = YES], [PIVOT_ABOVE_BELOW_WEEKLY] = 2, [VOL_METHOD] = ATR, [PIVOT_DAILY] = NO, [PRODUCE_STRATEGY_RECOMMENDATIONS], [BE_TRAIL_R], or any bracketed variable reference anywhere in the report body, charts, tables, footnotes, or Agent Log. State methodology in plain English only. **3. NO MODULE REFERENCES  **Do not reference M1, M2, M3, M4, M5, or any step/section codes from the analytical framework anywhere in the report. Permitted internal cross-reference format: ‘(see §N)’ where N is the report section number only. **4. NO FRAMEWORK IP REFERENCES  **Do not name the analytical framework, its architecture, or any component module anywhere in the report — including the Agent Log, header, and footer. The Agent Log may note internal process steps but must not name the framework. **5. INSTRUMENT NAMING  **Use common market names, not data provider ticker codes. Use: VIX (not ^VIX), Gold (not GC=F), S&P 500 (not ^GSPC), Natural Gas (not NG=F / NGK26), USDX or Dollar Index (not DX-Y.NYB), Brent Crude (not BZ=F), Heating Oil (not HO=F), WTI or Crude Oil (not ^CL=F). Contract month codes (e.g., CLK26) are acceptable in §2 Market Definition and §3 Consensus Price Call where operationally necessary. **6. OHLC CROSS-REFERENCES  **When referencing session data in §8 commentary, use the format: (see §6). Do not write ‘Table §6 reference’ or any module-internal step code. **7. REPORT FOOTER  **Footer format: [Primary Asset] [Report Type] │ [As-of Date] │ [Role Title]. No framework name, no module codes, no version numbers. **8. STRATEGIES SECTION (§21)  **When §21 is produced, all stops and targets must appear in BOTH price and the asset’s native execution unit (pip / tick / point / dollar). Variable names like [TICK_SIZE] never appear; only the numeric value and the native-unit label do. **9. PRE-EMIT NAMING SCAN  **Rules 1–8 are checked once more, mechanically, on the finished text before the report is issued. Scan the whole deliverable — title, header, every section, every table cell, chart titles and captions, footnotes, the Agent Log and the footer — and confirm that none of the following appears anywhere: the letter-plus-digit module codes M1 to M5 in any form (‘M5 §5.1’, ‘the M3 surface’, ‘Modules A and B of the approved stack’); any step or patch code from the analytical framework (‘Step 4’, ‘§11b’, ‘PATCHES’, ‘OPEN-008’); the framework or architecture name, or any version string for it; any token in square brackets; any internal field, signal, weight, trigger or label identifier, whether bracketed or not (for example daily-open-anchor, conviction-threshold, regime-label, cross-asset-confirm, sentiment-tilt, produce-strategy-recommendations, and the direction-weight names); and any data provider ticker code barred by Rule 5. Each hit is removed and replaced with plain language describing what was done — ‘the conviction threshold’, ‘the regime-mapping rule’, ‘the sentiment weighting’ — never with the identifier. This scan is the last action before issue: a single surviving hit is a restriction breach that caps the report’s trust band regardless of the quality of its analysis, and it is the cheapest defect in the whole report to prevent. |
| --- |

**MASTER OUTPUT STRUCTURE — 21 sections in fixed order**

| **#** | **Section** | **Required Content** | **Module Source** | **Tag** |
| --- | --- | --- | --- | --- |
| 1 | Executive Snapshot | One paragraph: consensus price, market tone, 3 dominant drivers, short- and medium-term technical regime, Kaufman regime classification, single most important watch item. | M2 §7 + M3 §10 |  |
| 2 | Market Definition | Commodity/asset, specification, scope, delivery basis, unit, currency, as-of date, lookback window — restated from M1. | M1 A–B |  |
| 3 | Consensus Price Call | Table: consensus price, range, basis, confidence level, market tone, 1–2 line rationale. | M2 Steps 4–5 |  |
| 4 | Price Evidence Table | Source │ Date/Time │ Raw Quote │ Normalized Quote │ Basis/Location │ Relevance Classification │ Notes. Min [MINIMUM_SOURCE_COUNT] rows. | M2 Steps 2–4 |  |
| 5 | Consensus Build Explanation | How comparables were normalized; observation weighting rationale; exclusions; why the final number is most defensible. | M2 Steps 3–5 |  |
| 6 | Validated OHLC + RSI2 Table | 5-day validated table with dual-source corroboration. See §6 spec below. | M3 §1–2 | **M3** |
| 7 | Charts | Up to 5 charts, subject to chart toggles. See §7 spec — chart sizing rules are mandatory. | M3 §9 | **M3** |
| 8 | Short-Term Technical Analysis | Candle-by-candle analysis and sequence assessment. See §8 spec. | M3 §2, §4 | **M3** |
| 9 | Medium-Term Regime & VOLator | Regime classification and VOLator read. See §9 spec. | M3 §3–5 | **M3** |
| 10 | Cross-Asset Analysis | Counter directional reads and mechanisms. See §10 spec. | M3 §6 | **M3** |
| 11 | Floor Pivot Analysis | Pivot tables and chart. See §11 spec. | M3 §8 | **M3** |
| 12 | Key Market Considerations | Structured fundamentals — supply, demand, policy, macro, catalysts. See §12 spec. | M2 Step 6 | **UPD** |
| 13 | Sentiment, News & Calendar | Per-article table, aggregate (categorical + numeric tilt), and two-part news calendar. See §13 spec. | M2 Steps 8–10 | **UPD** |
| 14 | Macro Context | Rates, inflation, liquidity, FX, positioning. See §14 spec. | M2 Step 6 | **UPD** |
| 15 | Bull / Bear Balance | Main upside risks │ main downside risks. Must cross-reference pivot position, regime, and §13d upcoming events. | M2 Step 7 |  |
| 16 | Forward View | Expected direction, trading range, base case invalidation. Must respect technical regime; flag if contradicting. | M2 §7 + M3 §10 |  |
| 17 | Forecast (ONE sentence) | Exactly one sentence. Derived strictly from technicals + sentiment + cross-asset. No scenario hedging. | M3 §10 integration note |  |
| 18 | Final Analyst Judgement | Consensus price call, confidence, 3 most important reasons, single watch item. | M2 §7 |  |
| 19 | Source Discipline Note | Live vs indicative data. Data gaps. Normalization assumptions. Corroboration status per instrument. | M3 §1, §6 |  |
| 20 | Agent Log | Sources attempted, validation method, corroboration pairs, sentiment derivation, forecast reasoning, anomalies, and (when active) M5 trace including direction-score weights, suppression reasons, and backtest reconstruction notes. Timestamp. | M2 + M3 + M5 | **UPD** |
| 21 | Strategy Recommendations | Directional conviction summary, three regime-aware trade cards (price + native unit), 5-session no-leakage backtest, and ‘what is working’ aggregate. See §21 spec. Produced ONLY when [PRODUCE_STRATEGY_RECOMMENDATIONS] = YES. | M5 | **M5** |

| **§6  VALIDATED OHLC + RSI2 TABLE (5-Day) — Technical Integration** *Full dual-source corroborated OHLC table for [PRIMARY_ASSET] and secondary assets. Governs data quality bar for all downstream technical sections.* |
| --- |

Produce one table for [PRIMARY_ASSET]. Repeat for [SECONDARY_ASSET_1] and [SECONDARY_ASSET_2] if populated. The table must contain the following columns exactly:

| **Column** | **Content** |
| --- | --- |
| Date | Session date — must be a valid trading day (Mon–Fri, no holidays) |
| Open | Validated open price in [UNIT_OF_MEASURE] |
| High | Validated session high |
| Low | Validated session low |
| Close | Validated session close — bold |
| RSI2 | Period-2 RSI computed from validated close sequence |
| Trend | Bullish (Close > Open AND RSI2 > 50) / Bearish (Close < Open AND RSI2 < 50) / Neutral (all other combinations) |
| Source A | Name of first corroborating source |
| Source B | Name of second corroborating source |
| Final Value Used | The accepted value after reconciliation |
| Validation Outcome | CORROBORATED / SINGLE-SOURCE (indicative) / REJECTED — with delta where two sources agree |

- Any row where Validation Outcome is SINGLE-SOURCE must be labelled ‘indicative only’ in the table and cannot be used for pivot calculations.

- RSI2 note: the period is fixed at 2. Do not vary it. Compute from the validated close column only.

- RSI2 must reproduce from the Close column of this table. Beneath the table, show the working for the most recent session in one line: the two close-to-close changes, the mean gain, the mean loss, RS, and the resulting value. Where the earliest row is seeded by closes outside the block, print those closes and their dates too. A published RSI2 that cannot be reproduced from stated closes is a data failure, not a rounding difference, and every downstream sentence that quotes it must move with the corrected value.

- The Open, High and Low columns carry observed values on the basis declared for the table. A field reconstructed from a narrative percentage, interpolated from a prior close, or scaled from a proxy instrument is labelled as such in its own row and may not be shown as CORROBORATED, used for pivots, or cited as an execution reference.

| **§7  CHARTS — Technical Integration** *All charts must fit within the page content area. Chart sizing rules below are mandatory — overflow through page margins is a formatting failure.* |
| --- |

**§7a  Chart Eligibility**

Produce only the charts whose toggle is set to YES in the configuration: [CHART_CANDLESTICK], [CHART_OPEN_ZERO], [CHART_5WEEK], [CHART_VOLATOR], [CHART_PIVOT]. Suppress any chart set to NO entirely — do not produce a placeholder or blank space.

**§7b  Mandatory Chart Sizing Rules**

The document page content area is 6.5 inches wide (9,360 DXA / 5,943,600 EMU) with 1-inch margins on all sides. Every embedded chart must respect this constraint exactly:

- Maximum embedded width: 9,000 DXA (6.25 inches / 5,760,000 EMU) — leaves a small visual breathing margin inside the content area.

- Height: scale proportionally to the generated chart aspect ratio. Never hard-code a height that would cause the image to overflow vertically into the next section.

- Charts must be embedded as inline images — not floating, not behind/in front of text. Floating images can drift outside margins during rendering.

- Do not generate charts wider than 9.5 inches at source (at 150 DPI this is ~1425 pixels). Wider source images produce scaling artefacts when embedded.

Recommended generation dimensions — defaults unless the asset or session count requires adjustment:

| **Chart** | **Width (in)** | **Height (in)** | **DPI** | **Notes** |
| --- | --- | --- | --- | --- |
| Candlestick (5-day) | 9.0 | 4.8 | 150 | Portrait-landscape hybrid; fits full content width |
| Open=0 Distance | 9.0 | 4.8 | 150 | Same dimensions as candlestick for visual consistency |
| 5-Week Structure | 9.0 | 4.8 | 150 | ~25 bars; wider aspect preferred; do not exceed 9 in |
| VOLator Comparison | 9.0 | 5.0 | 150 | Multiple series; legend must not overflow chart frame |
| Pivot Chart | 9.0 | 6.5 | 150 | Taller for pivot line spacing; 6.5 in height maximum |

*ℹ  **If using the agentic technical engine, set figsize width ≤ 9.0 and dpi=150 for all charts. The pivot chart may use dpi=150 with figsize=(9.0, 6.5). Do not exceed these values.*

**§7c  Chart Content Requirements**

- Chart 1 — Candlestick: exactly [LOOKBACK_SHORT] validated sessions for [PRIMARY_ASSET]. Green fill = bullish, red fill = bearish. Black wick lines. X-axis: session dates. Title states asset, date range, and [UNIT_OF_MEASURE].

- Chart 2 — Open=0 Distance: same [LOOKBACK_SHORT] sessions. Set Open'=0 for each session; plot High'=High−Open, Low'=Low−Open, Close'=Close−Open. Y-axis label: ‘Distance from Open ([UNIT_OF_MEASURE])’.

- Chart 3 — 5-Week Structure: all [LOOKBACK_MEDIUM] sessions as direction-coded bars with close-line overlay. Makes overlap and persistence visually clear.

- Chart 4 — VOLator: scaled volatility series (−1 to +1) for [PRIMARY_ASSET] and all active counters. Reference lines at 0, ±0.5. Legend must sit inside the chart frame. Title states volatility method and scaling method.

- Chart 5 — Pivot: draw [PIVOT_CANDLES_N] candles of [PIVOT_CANDLES_TF] timeframe using the smart-scale pivot level algorithm. OHLC annotated on each candle. Active timeframes colour-coded. Do not show variable names or configuration values on the chart.

| **§8  SHORT-TERM TECHNICAL ANALYSIS — Technical Integration** *Candle-by-candle classification and sequence assessment for [PRIMARY_ASSET] and secondary assets. Must not repeat OHLC numbers already in §6 — reference the table by session date instead.* |
| --- |

Present findings in the following structure for [PRIMARY_ASSET]. Where [SECONDARY_ASSET_1] and [SECONDARY_ASSET_2] are populated, provide a condensed equivalent.

- Session-by-session commentary: for each of the [LOOKBACK_SHORT] sessions in §6, reference the date and state — candle direction, body/wick structure, close location within range (as %), RSI2 reading, and what the combination signals. Keep to 2–3 sentences per session. Reference the OHLC table using the format (see §6).

- Sequence assessment: classify the [LOOKBACK_SHORT]-session sequence overall as: Continuation / Compression / Indecision / Exhaustion. State the specific evidence that supports this classification.

- Nearest support and resistance: quote the price levels directly observable from the validated OHLC table. Do not import levels from outside this window unless labelled as structural.

- Judgement label — use exactly one of: Bullish continuation / Bearish continuation / Indecision / Range / Exhaustion — reversal risk. This label feeds §1 Executive Snapshot and §16 Forward View.

- Confirm the judgement label is consistent with the regime classification in §9. If they conflict, state the conflict explicitly.

| **§9  MEDIUM-TERM REGIME ****&**** VOLator — Technical Integration** *Regime classification for [PRIMARY_ASSET] derived from the [LOOKBACK_MEDIUM]-session window. VOLator scaled volatility readings for primary and all counters.* |
| --- |

- Regime classification: state Trending / Ranging / Transitional for [PRIMARY_ASSET]. Cite the supporting metrics: overlap ratio (value), directional persistence (value), VOLator slope (positive/negative), median RSI2, range position bias.

- Bias: state Bullish / Bearish / Neutral as the directional component of the regime.

- ATR(14): state the value as a number, with its 14-session window and the bar basis it was computed on. This is the single figure every stop buffer, stop cap, target cap and wide-stop test in §21 is a multiple of, so it must appear here explicitly and must be the same number that appears on each card. Do not leave it to be inferred from a buffer or a cap, and do not substitute a proxy. State the Kaufman efficiency ratio with its period and smoothing in the same way.

- VOLator current readings: list the scaled volatility value (−1 to +1) for [PRIMARY_ASSET] and each active counter. State whether each is above or below its 0 midpoint and whether it is expanding or contracting.

- Preferred trade protocol: state the protocol that follows from combining the short-term (§8) and medium-term regime assessments. If they conflict, flag it explicitly.

- Kaufman confirmation: state the Kaufman Efficiency Ratio classification and whether it agrees with or contradicts the regime. If it disagrees, state which signal takes precedence and why.

| **§10  CROSS-ASSET ANALYSIS — Technical Integration** *Directional reads, causal mechanisms, and confirmation/contradiction status for all active counters and secondary assets. Do not recalculate — format and contextualise the cross-asset technical reads.* |
| --- |

For each active counter ([COUNTER_1], [COUNTER_2], [COUNTER_3], [COUNTER_4], [COUNTER_5]) and secondary assets ([SECONDARY_ASSET_1], [SECONDARY_ASSET_2]), state the following in a structured format:

| **Element** | **Required content** |
| --- | --- |
| 5-day direction | Rising / Falling / Flat — based on net change over [LOOKBACK_SHORT] validated sessions |
| Mechanism | The causal channel to [PRIMARY_ASSET] — not just correlation direction. One sentence stating the transmission mechanism. |
| Confirmation status | Confirms / Contradicts / Neutral — relative to the regime classification in §9 |
| Implication | What this counter reading means specifically for the price view of [PRIMARY_ASSET] |

- Contradiction flag: where any counter contradicts the regime synthesis, state it in bold and do not resolve it silently. Contradictions feed §15 Bull/Bear Balance and §16 Forward View.

- Do not recalculate the cross-asset analysis. This section formats and contextualises the technical readings — it adds narrative context and implication only.

| **§11  FLOOR PIVOT ANALYSIS — Technical Integration** *Pivot tables and smart-scale chart for active timeframes. Mandatory table order: R5 → P → S5. Chart must fit within page margins per §7 sizing rules.* |
| --- |

Produce pivot output for each active timeframe ([PIVOT_DAILY], [PIVOT_WEEKLY], [PIVOT_MONTHLY]). Skip any disabled timeframe entirely — do not produce a placeholder.

- Pivot table: one table per active timeframe. Mandatory row order (top to bottom): R5, R4, R3, R2, R1, P, S1, S2, S3, S4, S5. Never sort by ascending value. Resistance at top, support at bottom.

- Input row per table: immediately above each set of levels, print the prior-period H, L and C used and the session date or date range they came from — the completed session before the report date for daily, the last fully completed calendar week for weekly, the last fully completed calendar month for monthly. A table built on an earlier session, on a part-week, or on the extremes of a single session standing in for a whole week is wrong at the input and every level in it is wrong with it. Confirm in the same place that R2 − P = P − S2 holds on the printed levels.

- Source status per table: state whether prior-period H/L/C were corroborated by two sources or single-source only. If single-source, mark all levels in that table ‘indicative only’. The same flag is propagated through the M3 Named Output Surface and is consumed by the §21 strategies suppression rules.

- Pivot chart: draw [PIVOT_CANDLES_N] candles of [PIVOT_CANDLES_TF] timeframe. Apply smart-scale level selection. Embed at maximum 9,000 DXA wide (see §7b). Do not show variable names on the chart.

- Position narrative: for each active timeframe, state where the most recent close sits relative to P, nearest resistance, and nearest support. Flag any confluence zone where daily, weekly, and monthly levels are within 0.05% of each other.

| **§12  KEY MARKET CONSIDERATIONS — Updated Specification** *Structured fundamentals assessment. Supply, demand, substitution, policy, macro, near-term catalysts. Each subheading ends with a direction label.* |
| --- |

Include only subheadings that are materially relevant. For each active subheading, state explicitly whether it is price-supportive, price-negative, or neutral.

- Supply — production pace, harvest/crush, weather, inventory levels, OPEC/cartel decisions. Cite official source: EIA, USDA WASDE, MPOB, OPEC MOMR as appropriate.

- Demand — consumption, renewable fuels, import demand, seasonal patterns. Cite official demand data.

- Substitution / Spreads — pricing vs [COMPARISON_PRODUCTS], switching risk, crack spreads, inter-commodity differentials.

- Policy / Regulation — tariffs, export taxes, quotas, blending mandates, sanctions.

- Macro / Logistics / FX — [CURRENCY] moves, freight, interest rates, curve structure, speculative positioning.

- Near-term Catalysts — explicitly flag all upcoming events from §13d that could materially affect [PRIMARY_ASSET] within [SCENARIO_HORIZON].

Label each factor as structural (lasting 6+ months) or cyclical (event-driven, reversible within [SCENARIO_HORIZON]). Cite the official data source for any quantitative assertion.

| **§13  SENTIMENT, NEWS ****&**** CALENDAR — Updated Specification** *Per-article sentiment table, aggregate summary (categorical + numeric tilt), and two-part news calendar. Four sub-sections in sequence.* |
| --- |

**§13a  Per-Article Sentiment Table**

One row per article. Minimum [MINIMUM_SOURCE_COUNT] for [PRIMARY_ASSET]; minimum 2 per secondary asset.

| **Field** | **Example** | **Requirement** |
| --- | --- | --- |
| Source | Reuters | Full publication name |
| URL | https://... | Complete URL — no shortened links |
| Date | 14 Apr 2026 | Publication date; time where available |
| Headline | Exact title | Verbatim — do not paraphrase |
| Classification | Institutional / Media / Official / Trade Press | Tag per evidence hierarchy |
| Derived Sentiment | Bullish / Bearish / Neutral / Mixed | Explicitly derived from article language per the methodology |
| Derivation quote | e.g., “Goldman forecasts...” | Direct quote ≤ 15 words from article that supports the classification |

*ℹ  **Derivation quote must be ≤ 15 words directly from the source. It justifies the sentiment classification. Do not paraphrase. Empty Derivation Quote is a protocol failure.*

**§13b  Aggregate Sentiment Summary**

- Categorical label and counts: e.g., ‘3 Bullish (2 institutional, 1 media), 1 Bearish (media), 1 Neutral (official) = Predominantly Bullish’.

- Numeric tilt: a signed scalar in [−1, +1] computed as the source-class-weighted mean of article-level scores. Reported alongside the categorical label, e.g., ‘Predominantly Bullish (tilt = +0.43)’. Mandatory when [PRODUCE_STRATEGY_RECOMMENDATIONS] = YES — the tilt is consumed by §21 directional conviction.

- Divergence flag: state whether aggregate sentiment agrees with or contradicts current price action and the technical regime (§9). If there is a contradiction, state which signal takes precedence and why.

- Low-confidence flag: tilts computed on fewer than three articles must be labelled low-confidence in this section.

**§13c  News Calendar — Previous Period**

Cover [LOOKBACK_WINDOW] ending [AS_OF_DATE]. Events material to [PRIMARY_ASSET] or its counters only.

| **Date** | **Event** | **Prior / Context** | **Impact** | **Market Implication for [PRIMARY_ASSET]** |
| --- | --- | --- | --- | --- |
| Mon 14 Apr | FOMC Minutes / CPI / OPEC MOMR | Prior value or context | High | Mechanism — what moved, direction, magnitude |

**§13d  News Calendar — Upcoming Period**

Cover upcoming [SCENARIO_HORIZON] from [AS_OF_DATE]. Same columns. For Market Implication: state mechanism for both a beat and a miss where relevant.

- Bold the single highest-impact upcoming event. One sentence explaining how a surprise would change the consensus price view for [PRIMARY_ASSET].

- All events here become primary watch items for §16 Forward View, §17 Forecast, and §21 trade-card holding-period collision flagging.

| **§14  MACRO CONTEXT — Updated Specification** *Rates, inflation, liquidity, FX flows, positioning. Must cross-reference counter readings from §10 and upcoming events from §13d.* |
| --- |

- Rates and monetary policy — central bank stance for [CURRENCY] and key cross pairs. Cross-reference [COUNTER_2] reading from §10.

- Inflation — relevant CPI/PPI/PCE trajectory. State whether price-supportive, price-negative, or neutral for [PRIMARY_ASSET].

- Safe-haven / Real yields — [COUNTER_3] (Gold) trend from §10. Rising Gold = defensive demand or real yield compression. Falling Gold = risk-on or rising real yields. State causal implication for [PRIMARY_ASSET].

- Liquidity and FX — [COUNTER_1] (USDX) trend from §10. Causal mechanism for [PRIMARY_ASSET].

- Energy — [COUNTER_4] direction and mechanism. Relevant for commodity and equity analyses.

- Positioning — COT data, VIX level, DXY positioning, or commodity fund flows where available.

Cross-reference requirement: explicitly cite the counter readings from §10 for each active counter. Do not re-derive them independently. If the macro narrative contradicts the cross-asset reads in §10, flag the contradiction — do not resolve it silently.

Upcoming event cross-reference: identify any §13d event that affects the macro variables in this section. Label it as a watch item and state the directional risk for [PRIMARY_ASSET] if it surprises.

| **§21  STRATEGY RECOMMENDATIONS — M5 Integration  (NEW)** *Regime-aware three-tier trade cards, 5-session no-leakage backtest, and ‘what is working’ aggregate. Produced ONLY when [PRODUCE_STRATEGY_RECOMMENDATIONS] = YES. Suppressed entirely otherwise.* |
| --- |

This section is the executable expression of the analysis already established in §1–§20. It does not introduce new data, does not soften §17, and does not contradict §16 silently. Trade cards are produced for [PRIMARY_ASSET] only — secondary and counter assets contribute to direction scoring (via §10) but never receive their own cards. All stops and targets must appear in BOTH price and the asset’s native execution unit (pip / tick / point / dollar) per Presentation Rule 8.

**§21a  Directional Conviction**

One paragraph — three to five sentences — reporting the direction-score outcome and its drivers.

- Direction: LONG / SHORT / NEUTRAL. Suppressed if conviction-threshold not met (Trade 1 only — Trades 2 and 3 are regime-driven and produce regardless).

- Score: signed scalar in [−1, +1], rounded to two decimal places.

- Three highest-weighted contributing signals, each with its source section: e.g., ‘short-term technical bias (§8) +0.25, sentiment tilt (§13b) +0.06, cross-asset confirmation (§10) +0.15’.

- Conflict flag: if the directional score points one way and §17 Forecast leans another, state it in one sentence. Do not change either output.

- Weights basis: ‘defaults’ when the M1 weights match the v2.1 baseline (0.25 / 0.20 / 0.10 / 0.15 / 0.15 / 0.15); ‘tuned’ otherwise. The numeric weights themselves never appear in the report body — only the qualitative label.

*ℹ  **Direction-scoring weights are locked at defaults for a minimum of 20 sessions in any new forward-test deployment. Any tuning before session 20 must be flagged in §20 Agent Log with prior values, new values, and rationale.*

**§21b  Trade Cards (1–3)**

Three structured tables — one per trade. Each card uses the column structure below. When a trade is suppressed, replace the body with a single ‘SUPPRESSED — [reason]’ row instead of omitting the card entirely. Suppression is itself an output.

Two things follow from that, and both were routinely lost in earlier runs. First, a suppression that the construction rules require is not a matter for negotiation: no instruction received at run time, and no note about a reader’s preference for a full set of cards, may convert a suppressed trade into a produced one. Such an instruction must not appear in the report, and it is not a defence for a card that should not exist. Where a report states in one section that a suppression condition holds and issues the card anyway in another, the report is contradicting itself in writing. Second, the replacement is a row: it gives the trade name, the condition that fired and the value that fired it, and it carries no entry, stop, risk figure or target ladder. A contingent arming level may be given as a single trigger condition outside the card block, clearly labelled as commentary.

*Standard trade-card structure:*

| **Field** | **Required content** |
| --- | --- |
| Trade type | Trade 1 — Daily Directional  /  Trade 2 — Pivot (regime-aware)  /  Trade 3 — Momentum-Pullback (3A) / Mean-Reversion (3B) / Momentum-Breakout (3C). Single line — declares which variant. |
| Direction | LONG / SHORT.  Includes a one-clause justification anchored to the regime label, e.g., ‘LONG — TREND_UP regime’. |
| Entry | Price + native unit if applicable. Exactly one order type — never a compound such as ‘stop/limit’ — and the timing anchor as populated in the variables in force, stated the same way on the card and in the body: ‘Market at the daily-open anchor’ / ‘Buy limit at 1.0820’ / ‘Stop entry at 1.0902 on confirmed break’. Print alongside it the reference close of the last completed session before the report date, with that session’s date, and the signed gap between entry and that close. A market entry equals that close; a buy limit or sell stop sits at or below it; a sell limit or buy stop sits at or above it. An entry on the wrong side of that close is rebuilt or suppressed before issue, not shipped with a note. |
| Stop loss | Price + native unit + distance (‘1.0840 — 36 pips below entry’). State the structural anchor used: 5-day swing low, daily S2, range boundary, etc. |
| Risk (R) | The entry-to-SL distance as a single number in price AND native unit, followed by the same distance expressed as a multiple of the stated ATR(14) to two decimals. This is the unit for tranche TP placement. Where that multiple exceeds 1.00 the card carries the ‘wide stop’ flag in its caveats — the flag follows from the arithmetic and is not a matter of judgement. State the ATR(14) figure used on the card so the multiple can be checked. |
| TP1 (Unit 1) | Price + native unit + ratio. For Trade 1 / Trade 2: ‘+1R’. For Trade 3 variants: structural target (38.2% retrace / range mid / measured-move = 1×width). |
| TP2 (Unit 2) | Same format as TP1 at +2R / structural TP2. |
| TP3 (Unit 3 — runner) | Same format. Includes the runner exit rule: time-stop at session close + 3×ATR cap (Trade 1); pivot P (Trade 2); 100%+ extension or range breakout (Trade 3). |
| Tranche management | Three-tranche universal rule: ‘3 equal units; Unit 1 exits at TP1; Unit 2 exits at TP2; on Unit 2 fill, Unit 3 SL moves to entry ± 0.2R’. Trade 3A only: structural runner override on 100%-extension break — SL moves to halfway between entry and 0% anchor. |
| Confluences at entry / SL / TPs | List structural confluences within 0.15 × ATR of each level: pivot, swing, fib, round number, cross-asset. Two-or-more within 0.15 ATR labelled ‘strong confluence’. |
| Thesis invalidation | A named structural level at a **different price** from the stop, stated as a close-through condition: the first level whose close-through breaks the directional narrative (e.g., ‘daily close back through the pivot’). It may sit beyond the stop or inside it, but ‘coincides with the stop’ is not an invalidation — a level that cannot be reached without the stop already having been hit carries no information, and a card giving one is incomplete. |
| Caveats | Comma-separated flags where applicable: ‘single-source-indicative pivots’ (corroboration flag from §11), ‘ATR-stop cap applied — position size reduced’, ‘holding-period collides with §13d Tier-1 event [name]’, ‘low-confidence sentiment tilt’, ‘conflict with §17 forecast’. |

*ℹ  **All price values rendered in [UNIT_OF_MEASURE]; native-unit values in [TICK_NAME] count units (e.g., ‘36 pips’, ‘50 ticks’, ‘24 points’). Variable names never appear in the rendered card.*

*Suppression-row format (when a trade does not produce):*

| **Trade** | **SUPPRESSED — Reason** |
| --- | --- |
| Trade 1 — Daily Directional | SUPPRESSED — Direction score │0.18│ below conviction threshold. |
| Trade 2 — Pivot (RANGE) | SUPPRESSED — All accessible pivot tiers (S1 / S1.5 / S2 / R1 / R1.5 / R2) are SINGLE-SOURCE INDICATIVE per §19; level-based limit orders cannot be placed against indicative levels. |
| Trade 3B — Mean-Reversion | SUPPRESSED — RANGE regime requires both KER < trend-threshold and VOLator slope ≤ 0; KER condition not met. Trade fork falls through to 3A (Momentum-Pullback). |

**§21c  5-Session No-Leakage Backtest**

Reconstruct the prior [BACKTEST_LOOKBACK_DAYS] sessions (default 5) under the same trade-card logic, using only data available at each prior t−1 close. Sentiment, regime, ATR, swings, pivots — all are recomputed at t−1 with no forward leakage.

| **Column** | **Required content** |
| --- | --- |
| Date (t−N) | Session at which the trade card would have been issued: e.g., ‘Tue 22 Apr 2026 (t−5)’. |
| Strategy | Trade 1 / Trade 2 / Trade 3A / 3B / 3C — match what the backtest reconstruction would have produced. |
| Direction | LONG / SHORT / SUPPRESSED. |
| Triggered | YES / NO. NO when entry conditions not met within the resolution window. Limit orders only trigger when price reaches the limit price within the t-session range. |
| Entry / Exit | Price values from the actual t-session and forward OHLC. Slippage = 0 in backtest. |
| Outcome (R) | Sum of tranche R-multiples realised. ‘OPEN @ +0.5R’ if unresolved at t+5. SL-first tick-priority rule applies when both SL and TP could fill within the same bar. |
| Days to resolution | Number of sessions between trigger and final exit. ‘5+ (open)’ for unresolved. |

One row per (session × strategy). Up to 15 rows total over a 5-session × 3-strategy window, fewer when suppressions occur. Suppressed reconstructions are still reported as rows for traceability — they do not contribute to the §21d aggregate.

**§21d  ‘What Is Working’ Aggregate**

Single paragraph plus one-line limitations. Aggregate per strategy type over the [BACKTEST_LOOKBACK_DAYS] window.

- Per-strategy line: ‘Trade 1 over the last 5 sessions: triggered N/M times, mean R = +X.XX, hit rates TP1 / TP2 / TP3 = a% / b% / c%.’

- Strongest performer: name the strategy with highest mean R (closed positions only).

- Weakest performer: name the strategy with lowest mean R, or note ‘insufficient triggers to rank’.

- Limitations boilerplate (mandatory, verbatim): ‘Five-session windows are too small to support statistical claims. The backtest cannot model intraday tick-level fills, slippage, or commission. Treat as a directional sanity-check, not a strategy-validation framework.’

| **ANTI-SILO INTEGRATION — all cross-feeds mandatory** *Every section that depends on another must cite, not re-derive. Contradictions are flagged, not silently resolved.* |
| --- |

| **Section** | **Must reference** |
| --- | --- |
| §1  Executive Snapshot | Technical regime summary (§8–§9) + §8 judgement label + §13b aggregate sentiment (categorical + tilt). When §21 active, summarise §21a directional conviction in one sentence. |
| §8  Short-Term TA | Must cite §6 OHLC table using (see §6); must be consistent with §9 regime |
| §9  Regime & VOLator | Regime synthesis + Kaufman classification + VOLator slope |
| §10 Cross-Asset | Cross-asset technical reads — does not recalculate |
| §11 Pivot Analysis | Pivot source status; chart compliant with §7b sizing |
| §12 Key Considerations | Must flag §13d upcoming catalysts; weight factors relative to §9 regime |
| §13 Sentiment & News | Numeric tilt mandatory in §13b when §21 active — feeds §21a |
| §14 Macro Context | Must cite counter reads from §10; must flag §13d as watch items |
| §15 Bull / Bear | Must reference §13d highest-impact event; must cite pivot position from §11 |
| §16 Forward View | Must reference §13d calendar; must respect §9 regime; flag if contradicting |
| §17 Forecast (1 sentence) | Derived from §9 integration note + §13b aggregate sentiment direction. Independent of §21 — never edited to align with trade-card direction. |
| §19 Source Discipline | Must record corroboration status of every pivot timeframe used by §21 (single-source-indicative flag is the contract M5 reads). |
| §20 Agent Log | When §21 active, must include: direction-score weights basis (default / tuned), suppression reasons, backtest reconstruction notes (sessions reconstructed, sentiment freeze rule applied). |
| §21 Strategy Recommendations | §21a consumes §13b numeric tilt + §10 cross-asset confirmation + §9 regime + §7 KER. §21b confluences cite §11 pivots and §8 swing levels. §21 caveats cite §13d (news collisions) and §19 (single-source-indicative pivots). |

*Modular Prompt Architecture v2.1  │  M4 Output Structure  │  April 2026*

M4 │ April 2026 │ page  of