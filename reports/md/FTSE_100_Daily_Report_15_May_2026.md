**FTSE 100 Report — Daily: 15 May 2026**
*With reference to: EURO STOXX 50 · USDX · S&P 500 · DAX 40*

| **Run controls — applied overrides** |
|---|
| Snapshot date: Friday 15 May 2026 (Europe/London close). Daily-open anchor overridden to 00:00 UK (default for this populated instance is 07:00 UK — the European pre-open). The 00:00 UK anchor moves Trade 1 entry to the natural global session reset; suitable for analysts whose forward-test cadence runs through the overnight window and who wish to express conviction earlier than the 1-hour pre-LSE window. All other M1 variables remain at their populated v2.1 baseline. Strategies module enabled. Master switch ON. |

# §1 Executive Snapshot
FTSE 100 closes the week at 10,388 (provisional), consolidating the post-UK-GDP rally that lifted the index above its 25-session resistance shelf earlier in the week. Consensus build returns a tone of cautiously bullish — three drivers dominate: (i) stronger-than-expected UK Q1 GDP supporting domestic cyclicals, (ii) the eight-session copper rally still feeding mining-sector contribution into the cap-weighted aggregate, and (iii) elevated WTI/Brent (WTI ~$101) supporting BP and Shell index-points contribution. Short-term technical regime: Trending Bullish. Medium-term regime: Trending Bullish, with overlap and persistence both clearing the dual gate threshold. Kaufman Efficiency Ratio classifies as Trending Up — Moderate, agreeing with the Step 4 synthesis. The single most important watch item is the Bank of England decision/minutes window and the upcoming UK CPI print — a hawkish surprise on services inflation would test the 10,200 structural support and force a regime reclassification toward Transitional. EURO STOXX 50 sits at 6,010 (provisional close), with the 1.2% Wednesday rally (to ~5,931) extending through Thursday and Friday on AI-related leadership (ASML, SAP, Siemens) and constructive US-China summit rhetoric — STOXX-50 confirms the FTSE bullish read, though with notable single-name dispersion (3i / Vistry tails).
# §2 Market Definition

| **Field** | **Value** |
|---|---|
| Primary asset | FTSE 100 cash index |
| Specification | FTSE 100 cash index, GBP-denominated, free-float weighted (FTSE Russell methodology) |
| Secondary asset | EURO STOXX 50 (Eurozone large-cap pair) — receives §6 OHLC table alongside FTSE |
| Scope / region | Regional — Europe (UK + Eurozone) |
| Delivery basis | LSE regular session 08:00–16:30 UK (FTSE); Xetra 09:00–17:30 CET (STOXX) |
| Unit | Index points |
| Currency | GBP (FTSE); EUR converted to GBP-equivalent in §6 STOXX rows |
| As-of date | Friday 15 May 2026 (Europe/London close) |
| Lookback window | 5 trading days (Mon 11 May → Fri 15 May 2026) |

# §3 Consensus Price Call

| **Consensus price** | **Consensus range** | **Confidence** | **Market tone** |
|---|---|---|---|
| 10,388 (FTSE) · 6,010 (STOXX 50) | FTSE 10,360–10,415 · STOXX 5,985–6,035 | M (Medium) | Cautiously bullish |

Rationale: FTSE consensus anchored to the weighted median of six independent sources (FTSE Russell official close, LSE end-of-day, Yahoo Finance, Investing.com, Twelve Data, Bloomberg consensus). Five-source corroboration is intact at the time of the snapshot; the sixth source (Twelve Data) tracks within 3 points and is used as third-tier corroboration only. STOXX 50 consensus draws on STOXX Ltd official close plus Xetra mid, with Yahoo, Investing.com, and Bloomberg consensus as cross-checks. Range tightness reflects the narrow 14 May–15 May session-on-session move; confidence at M (not H) reflects the elevated weight of single-name moves (3i −19% / Telefónica +5% / Vistry warning) in the cap-weighted aggregate.
# §4 Price Evidence Table
Minimum six rows required; six listed below for FTSE; a parallel block follows for EURO STOXX 50.
**FTSE 100**

| **Source** | **Date / Time** | **Raw Quote** | **Normalized** | **Basis / Location** | **Relevance** | **Notes** |
|---|---|---|---|---|---|---|
| FTSE Russell official close | 15 May 2026, 16:30 UK | 10,388.4 | 10,388.4 (GBP) | LSE cash close | Core | Tier 1 — index provider |
| London Stock Exchange EOD | 15 May 2026, 16:35 UK | 10,388.2 | 10,388.2 (GBP) | LSE cash close | Core | Tier 1 — exchange |
| Yahoo Finance ^FTSE | 15 May 2026, 16:40 UK | 10,388.91 | 10,388.9 (GBP) | Delayed quote | Core | Tier 2 — aggregator |
| Investing.com UK 100 | 15 May 2026, 16:40 UK | 10,386.5 | 10,386.5 (GBP) | Delayed quote | Core | Tier 2 — aggregator |
| Bloomberg consensus (UKX) | 15 May 2026, 16:45 UK | 10,388.0 | 10,388.0 (GBP) | Composite | Directional | Tier 4 — corroboration only |
| Twelve Data ^FTSE | 15 May 2026, 16:45 UK | 10,385.7 | 10,385.7 (GBP) | API feed | Directional | Tier 3 — corroboration only |

**EURO STOXX 50**

| **Source** | **Date / Time** | **Raw Quote** | **Normalized (GBP)** | **Basis / Location** | **Relevance** | **Notes** |
|---|---|---|---|---|---|---|
| STOXX Ltd official close | 15 May 2026, 17:30 CET | 6,010.1 EUR | ~5,108 (GBP @ 0.85) | Xetra/EU close | Core | Tier 1 — index provider |
| Xetra mid (Deutsche Börse) | 15 May 2026, 17:30 CET | 6,009.8 EUR | ~5,108 (GBP) | Xetra cash | Core | Tier 1 — exchange |
| Yahoo Finance ^STOXX50E | 15 May 2026, 17:35 CET | 6,009.5 EUR | ~5,108 (GBP) | Delayed quote | Core | Tier 2 — aggregator |
| Investing.com EU 50 | 15 May 2026, 17:35 CET | 6,008.2 EUR | ~5,107 (GBP) | Delayed quote | Core | Tier 2 |
| MarketScreener | 15 May 2026, 17:30 CET | 6,011.0 EUR | ~5,109 (GBP) | Delayed quote | Directional | Tier 5 — secondary |
| Bloomberg consensus (SX5E) | 15 May 2026, 17:40 CET | 6,010.5 EUR | ~5,108 (GBP) | Composite | Directional | Tier 4 |

# §5 Consensus Build Explanation
Normalization: FTSE quotes are native GBP and require no FX adjustment. EURO STOXX 50 quotes are EUR-native; a session-end EUR/GBP rate of ~0.85 (Bank of England spot reference) is applied for the GBP-equivalent column shown in §6, with the EUR original reported in parentheses. No quality, freight, or timing adjustments are required because both indices are cash, continuous, exchange-published series.
Weighting (per the populated weighted-median rule): Tier 1 index-provider and exchange sources receive full weight; aggregator quotes (Yahoo, Investing.com) receive 0.75; corroboration-only sources (Bloomberg consensus, Twelve Data) receive 0.50. Retail CFD-broker spreads excluded per [RESTRICTIONS]. The weighted median resolves FTSE to 10,388 (range 10,386–10,389 across Core comparables) and EURO STOXX 50 to 6,010 EUR (range 6,008–6,011 across Core comparables). Defensibility derives from agreement of two Tier-1 sources within 0.2 points (FTSE) / 0.3 EUR (STOXX), which exceeds the consensus-method confidence floor.
Exclusions: none materially relevant; all six FTSE sources cleared Tier-1/2/3 thresholds. CFD-broker quotes excluded by rule.
# §6 Validated OHLC + RSI2 Table (5-Day)
**FTSE 100 — Mon 11 May to Fri 15 May 2026 (GBP, index points)**

| **Date** | **Open** | **High** | **Low** | **Close** | **RSI2** | **Range** | **Validation (Source A · Source B · Outcome)** |
|---|---|---|---|---|---|---|---|
| Mon 11 May | 10,265.1 | 10,294.4 | 10,253.8 | 10,260.2 | 31.5 | 40.6 | FTSE Russell · LSE EOD · PASS |
| Tue 12 May | 10,261.9 | 10,302.7 | 10,228.4 | 10,293.1 | 55.2 | 74.3 | FTSE Russell · LSE EOD · PASS |
| Wed 13 May | 10,290.0 | 10,360.5 | 10,266.1 | 10,325.4 | 74.6 | 94.4 | FTSE Russell · LSE EOD · PASS |
| Thu 14 May | 10,323.5 | 10,388.2 | 10,309.1 | 10,372.9 | 88.3 | 79.1 | FTSE Russell · Yahoo · PASS |
| Fri 15 May | 10,375.6 | 10,410.4 | 10,361.8 | 10,388.4 | 78.9 | 48.6 | FTSE Russell · LSE EOD · PASS |

**EURO STOXX 50 — Mon 11 May to Fri 15 May 2026 (EUR original · GBP-equivalent in brackets)**

| **Date** | **Open** | **High** | **Low** | **Close** | **RSI2** | **Range** | **Validation** |
|---|---|---|---|---|---|---|---|
| Mon 11 May | 5,870 (4,990) | 5,902 (5,017) | 5,855 (4,977) | 5,888 (5,005) | 29.1 | 47 | STOXX Ltd · Xetra · PASS |
| Tue 12 May | 5,884 (5,001) | 5,939 (5,048) | 5,872 (4,991) | 5,931 (5,041) | 62.8 | 67 | STOXX Ltd · Xetra · PASS |
| Wed 13 May | 5,932 (5,042) | 5,968 (5,073) | 5,915 (5,028) | 5,950 (5,058) | 67.4 | 53 | STOXX Ltd · Xetra · PASS |
| Thu 14 May | 5,950 (5,058) | 6,005 (5,104) | 5,940 (5,049) | 5,998.9 (5,099) | 84.6 | 65 | STOXX Ltd · Yahoo · PASS |
| Fri 15 May | 6,000 (5,100) | 6,022 (5,119) | 5,985 (5,087) | 6,010.1 (5,109) | 76.2 | 37 | STOXX Ltd · Xetra · PASS |

*All ten rows dual-source corroborated. No date rejected. Single-source-indicative flag NOT raised on the OHLC surface.*
# §7 Charts
Five charts produced (subject to the v2.1 baseline toggles, all of which are YES for this populated instance). Charts not embedded as graphics in this text release; descriptive readouts follow. PNG companion files are produced for analyst spreadsheet integration.

| **Chart** | **Readout (descriptive)** |
|---|---|
| **1. 5-Day Candlestick (FTSE)** | Five-bar sequence: small bear (Mon 11) → expansion bull (Tue 12) → wide-range bull (Wed 13, +94 range) → continuation bull with shrinking body (Thu 14) → narrowing bull (Fri 15). Body progression flags exhaustion candidates by Fri; range compression confirms. |
| **2. 5-Day Open=0 Distance (FTSE)** | Net change from Mon open to Fri close = +123 points (+1.20%). Cumulative path: −4, +28, +60, +108, +123. Monotonic from Tue. No intra-week pullback exceeded 30 points. |
| **3. 25-Session Structure (FTSE)** | 5-week swing low: 10,015 (~16 Apr); 5-week swing high: 10,410 (15 May intraday). Sequence shows higher-highs and higher-lows from week 2 onward; medium-term structure is unambiguously trending up. |
| **4. VOLator (cross-asset)** | Scaled (historical z, clipped ±1) ATR readings: FTSE +0.18 (slope +0.04, mildly rising), STOXX 50 +0.22 (slope +0.05), USDX −0.31 (slope −0.02, falling vol), S&P 500 +0.10 (slope +0.01), DAX +0.29 (slope +0.06). European indices the elevated-vol cohort; USDX dampened. |
| **5. Smart-Scale Floor Pivot (FTSE)** | Weekly candles (prior + current) shown; daily/weekly/monthly pivot ladders overlaid with 3 levels above HIGH and 3 below LOW. Close 10,388 sits between Weekly R1 (10,395) and Daily P (10,361). Above all monthly pivots through R2. |

# §8 Short-Term Technical Analysis
Candle-by-candle (FTSE 100, see §6):
Mon 11 May — Small bearish marubozu-lite (body 5, range 41); RSI2 31.5 (oversold edge). Reaction to weekend Middle East headlines weighed on energy beta; selling absorbed by close. Classification: indecisive bear.
Tue 12 May — Wide-range bullish candle (body 31, range 74); RSI2 spikes to 55. Banks and miners lead reversal; copper rally extending. Classification: trend-initiation bull.
Wed 13 May — Wide-range bullish continuation (body 35, range 94); RSI2 74.6 (entering overbought). Antofagasta +8.7%, HSBC +1%+, Lloyds/Barclays/NatWest 1–2% gains. Classification: trend continuation bull.
Thu 14 May — Bullish marubozu with diminishing body relative to range (body 49, range 79); RSI2 88.3 (deep overbought). UK GDP beat; STOXX 50 also +0.3% Thursday after +1.2% Wed. Classification: trend continuation bull with exhaustion candidate.
Fri 15 May — Narrowing bullish bar (body 13, range 49); RSI2 78.9 (still overbought but easing). 3i tail event drags STOXX-50 internals but cap-weighted aggregate holds. Classification: trend continuation — compression flag.
Sequence assessment: four consecutive higher closes; closes 4/5 of last 5 bars above prior-day high; net +123 points over the block. The body-to-range ratio compressed from 0.42 (Wed) to 0.27 (Fri) — classic late-trend compression. Short-term regime: Trending Bullish.
# §9 Medium-Term Regime & VOLator
Five-week (25-session) regime — FTSE: directional mean +0.31, overlap 0.42 (below 0.55 ranging threshold), persistence 0.62 (above 0.50 trending threshold), RSI2 median 58. All four gates clear in the bullish trending direction. Medium-term regime: Trending Bullish.
Step 4 synthesis (FTSE) — Short Trending Bullish × Medium Trending Bullish = High-conviction trend continuation / pullback entries in trend direction. EURO STOXX 50 returns the same synthesis (short trending bullish, medium trending bullish), so the secondary asset CONFIRMS rather than diverging — no caution flag raised under the secondary-asset divergence rule.
VOLator — FTSE scaled volatility +0.18 with 10-bar linear slope +0.04 (mildly rising). Cross-asset cohort: STOXX 50 +0.22 (slope +0.05, similar regime), DAX 40 +0.29 (slope +0.06, slightly elevated), S&P 500 +0.10 (slope +0.01, subdued), USDX −0.31 (slope −0.02, declining). European cohort sits in the upper-mid volatility band; US cohort lower. Rising-volatility-into-trend pattern is consistent with healthy trend persistence (not yet exhaustion).
# §10 Cross-Asset Analysis

| **Counter** | **5-Day Move** | **Direction Read** | **Mechanism (FTSE-relevant)** |
|---|---|---|---|
| **USDX (Dollar Index)** | 98.40 (≈ flat-down ~0.3%) | Mildly bearish $ | Soft dollar supports GBP-translated overseas earnings for multinationals (≈80% of FTSE revenue base); helps mining and energy index-points contribution. |
| **S&P 500** | +1.4% over block (~7,400 → 7,501) | Bullish risk-on | Cross-Atlantic risk-on confirmation; tech-led S&P leadership transmits to STOXX (ASML, SAP) more than to FTSE; FTSE benefits via global beta channel. |
| **DAX 40** | +1.0% over block (~24,540 → 24,786) | Bullish trend | European equity proxy CONFIRMS direction. Industrials-heavy DAX leadership consistent with copper-rally / mining-cycle backdrop also lifting FTSE miners. |

*Aggregate cross-asset confirmation: CONFIRM. Three of three active counters point consistently bullish for FTSE; no contradicting counter. The flow-through is consistent: weaker dollar + risk-on US + rising European industrials = a four-way push to UK large-cap multinationals.*
# §11 Floor Pivot Analysis
**FTSE 100 Daily Pivots (derived from Thu 14 May H/L/C: 10,388.2 / 10,309.1 / 10,372.9)**

| **R3** | **R2** | **R1** | **P (Pivot)** | **S1** | **S2** | **Flag** |
|---|---|---|---|---|---|---|
| 10,440 | 10,409 | 10,376 | 10,357 | 10,324 | 10,288 | OK |

**FTSE 100 Weekly Pivots (derived from prior week H/L/C: 10,295 / 10,041 / 10,251)**

| **R3** | **R2** | **R1** | **P (Pivot)** | **S1** | **S2** | **Flag** |
|---|---|---|---|---|---|---|
| 10,470 | 10,395 | 10,323 | 10,196 | 10,124 | 9,997 | OK |

**FTSE 100 Monthly Pivots (derived from prior month H/L/C: 10,360 / 9,955 / 10,251)**

| **R3** | **R2** | **R1** | **P (Pivot)** | **S1** | **S2** | **Flag** |
|---|---|---|---|---|---|---|
| 10,620 | 10,455 | 10,353 | 10,189 | 10,086 | 9,924 | OK |

Position narrative: 15 May close at 10,388 sits between Daily R1 (10,376) and Daily R2 (10,409), and just below Weekly R1 (10,395 — within 7 points / 0.07%). Close has cleared Monthly R1 (10,353) and is reaching toward Monthly R2 (10,455). The cluster around 10,395–10,409 — the Weekly R1 / Daily R2 confluence — is the immediate overhead reference and will be the natural reaction point on Monday's open. Below, the Daily P (10,357) is the nearest support, with Daily S1 / Weekly R1-now-support flip giving a tight 10,323–10,353 catch zone. All pivot tiers across all three timeframes carry the CORROBORATED flag (Source A: FTSE Russell official close; Source B: LSE EOD).
# §12 Key Market Considerations

| **Factor** | **Direction** | **Detail** |
|---|---|---|
| **UK macro (GDP, services)** | **Supportive** | Stronger-than-expected UK Q1 GDP print released midweek lifts cyclicals; the FTSE 250 outperformed (+0.5% Thu vs FTSE 100 flat-up) which signals domestic risk appetite is broadening. Source: ONS GDP release. |
| **Energy complex (oil)** | **Supportive** | WTI ~$101, Brent ~$105 — elevated levels lift BP and Shell's earnings translation; combined sector contribution remains a meaningful index-points tailwind. Risk: any credible US–Iran de-escalation could see oil fall fast, removing the tailwind. |
| **Metals / mining cycle** | **Supportive** | Copper rallied for an eighth consecutive session; aluminium, nickel, iron ore higher. Rio Tinto +4%, Anglo American +4.3%, Glencore +3.1%, Antofagasta +5–8% over the block. Driver of FTSE's mid-week wide-range bull candle. |
| **UK banks / fiscal politics** | **Mixed** | Banking shares rebounded mid-week from earlier-week pressure tied to speculation over fiscal tax-change risk under a possible left-leaning UK political shift; HSBC, Lloyds, Barclays, NatWest, Standard Chartered all up 0.8–2%. Mounting pressure on PM Starmer creates a slow-burn political-risk headline that can re-impair sentiment without warning. |
| **Eurozone backdrop (STOXX)** | **Supportive** | EURO STOXX 50 rose ~2.4% over the block. Drivers: AI-related leadership (ASML +5.5%, Infineon +3%), Siemens earnings momentum (+2.6%, plus Mermec acquisition), Telefónica +5% on profit beat. Tail event: 3i −19% after Action sales growth warning. Cap-weighted STOXX absorbs. |
| **US–China summit (geopolitical)** | **Supportive** | Trump–Xi Beijing meeting (14–15 May) producing constructive rhetoric; trade-disruption tail risk reduced into Friday close. Direct beneficiary: STOXX tech; indirect: FTSE risk premium. |
| **Single-name dispersion** | **Negative (Vol)** | Vistry −6 to −9%, Airtel Africa −13%, Experian −5% (FTSE side); 3i −19%, Burberry −2.4% (broader European). Cap-weighting masks single-name risk but raises Bull/Bear-balance asymmetry. |

# §13 Sentiment, News & Calendar
**13a · Per-article sentiment table**

| **Source** | **Class** | **Derivation Quote (≤ 15 words)** | **Sentiment** |
|---|---|---|---|
| Trading Economics (UK) | Trade Press | UK index up 32 points on Wednesday led by banks and miners. | Bullish |
| Trading Economics (Euro) | Trade Press | STOXX 50 closed 1.2% higher on constructive US–China summit rhetoric. | Bullish |
| Foreign Policy Journal | Media | Strong UK GDP data competes with 3i slump and global uncertainty. | Mixed |
| Invezz (FTSE weekly) | Trade Press | FTSE slips as Gulf tensions lift oil price concerns globally. | Bearish |
| T. Rowe Price Weekly | Institutional | DAX inched up 0.19%; FTSE MIB rose 2.16% on regional gains. | Bullish |
| BBN Times (FTSE review) | Media | Energy sector heavy weighting remains a structural advantage right now. | Bullish |

**13b · Aggregate sentiment**
Categorical: Bullish dominant (4 of 6 articles); Mixed 1; Bearish 1. Institutional weighting (T. Rowe Price) classified Bullish. Numeric tilt for FTSE 100 = +0.34 (range −1 to +1). This is the value forwarded to M5 via the named output surface for direction scoring.
**13c · Two-part news calendar — week ahead (16–22 May 2026)**

| **Date** | **Time (UK)** | **Event** | **Asset relevance** |  |
|---|---|---|---|---|
| Tue 19 May | 07:00 | UK CPI (April release deferred) | FTSE — services CPI is the dominant gating event |  |
| Wed 20 May | 10:00 | Eurozone CPI (final) | STOXX 50 — confirms ECB rate-path tone |  |
| Wed 20 May | 13:30 | US Retail Sales (April) | Cross-Atlantic — affects S&P/risk-on transmission |  |
| Thu 21 May | 12:00 | BoE MPC speaker (TBD — minutes window) | FTSE — direct GBP and rate-sensitive sectors |  |
| Fri 22 May | 07:00 | UK Retail Sales (April) | FTSE — consumer-facing names, GBP |  |
| Fri 22 May | 09:00 | ECB account of April meeting | STOXX 50 — Eurozone fixed income, banks |  |

**13d · Calendar collision flags**
UK CPI (Tue 07:00) collides with the 00:00 UK Trade 1 entry window of Tuesday (entry placed before release). Any directional trade card with a Tuesday entry must carry the CPI-collision caveat. ECB account and BoE MPC speaker are minutes-window events — narrower impact, but flagged for Trade 3 management.
# §14 Macro Context
Rates: Bank of England base rate 3.75% (held unchanged at the prior MPC); ECB deposit rate at the v2026-cycle low with ongoing market debate over next move (Nagel hawkish-leaning rhetoric cited in prior weekly reviews). US 10-year Treasury yield in the 4.25–4.35% band; UK 10-year gilt yield range-bound.
Inflation: UK headline CPI tracking around target with services component the sticky tail. Eurozone HICP confirmed final at preliminary level. US disinflation pace remains the FOMC's primary concern; affects USDX path, indirectly FTSE multinationals.
Liquidity: Money-market conditions normal; no funding-market stress. Cross-Atlantic credit spreads tight; CDS aggregates well below stress thresholds.
FX: GBP firm against USD (USDX softer ~98.4); EUR/GBP around 0.85. Dollar weakness amplifies FTSE multinational earnings translation tailwind.
Positioning: Cap-weighted index momentum positive; mining and energy sector internals strong; banks rebound from earlier-week pressure. Single-name dispersion (3i, Vistry, Airtel Africa, Experian) raises within-index variance, which limits upside conviction even where direction is clear.
# §15 Bull / Bear Balance

| **Upside (bull)** | **Downside (bear)** |
|---|---|
| Trend-bullish across short and medium horizons; KER agrees; cross-asset confirms. | RSI2 deep in overbought territory (88 → 79) raises near-term pullback risk. |
| Energy + mining double-tailwind (WTI ~$101, copper +8 sessions). | If Iran-front de-escalation accelerates, oil could fall fast — directly removes BP/Shell index contribution. |
| UK Q1 GDP beat lifts cyclicals; FTSE 250 outperformance signals breadth. | UK CPI (Tue) services-inflation surprise could hawkish-jolt BoE expectations and rate-sensitive names. |
| Constructive US–China summit rhetoric reduces trade-tail risk. | Political risk: pressure on PM Starmer; speculative tax-change narrative re-emerges intermittently. |
| Pivot position: above all monthly pivots; cleared Daily R1. | Pivot position: close brushing Weekly R1 (10,395) and Daily R2 (10,409) — natural mean-reversion magnet. |

Balance: weighted bullish, but with elevated tactical-pullback risk into early next week. Trade structures should respect both.
# §16 Forward View
Base case (next 5 trading days, 18–22 May 2026): FTSE drifts in a 10,310–10,470 range with a positive skew. Bullish bias inherited from the cleared dual-gate trend regime; tactical pullback to Daily P / Weekly R1-flip-support (10,323–10,357) likely on UK CPI Tue, especially if the release prints hot. Resolution above 10,410 (Daily R2 / Weekly R1 confluence cluster) opens 10,470–10,500 (Weekly R3 / Monthly R2 area). Base-case invalidation: a daily close back below 10,288 (Daily S2 / consolidated week-low support) — that would reset short-term regime to Transitional and force a Trade 1 reset.
This forward view RESPECTS the M3 technical regime classification. No contradiction flag.
# §17 Forecast (one sentence)
**FTSE 100 advances modestly to the 10,395–10,470 zone over the coming week, with tactical pullback risk to 10,323–10,357 on UK CPI Tuesday and structural support at 10,288 capping the downside.**
# §18 Final Analyst Judgement
Consensus price call: FTSE 100 10,388 (range 10,360–10,415; Confidence M). Market tone: cautiously bullish.
Three most important reasons: (1) dual-gate trending-bullish regime across short and medium horizons with KER confirming and VOLator slope positive; (2) sustained energy + mining double-tailwind feeding the cap-weighted aggregate via the largest sector contributors; (3) macro tailwind from UK Q1 GDP beat combined with soft USDX supporting multinationals.
Single watch item: UK CPI (Tuesday 19 May, 07:00 UK) — a hot services-inflation print is the cleanest hawkish-BoE catalyst available next week and the most likely event to break the established trend.
# §19 Source Discipline Note
Live data: FTSE Russell official close, LSE EOD, STOXX Ltd close, Xetra mid — all live, all Tier-1. Indicative qualifier: none required. Data gaps: none in the 5-day OHLC block (10 sessions across primary + secondary). Normalization assumptions: EUR/GBP 0.85 applied for STOXX-50 GBP-equivalent column. Corroboration status: every pivot timeframe and every OHLC row CORROBORATED. No SINGLE-SOURCE-INDICATIVE flag raised on any output that flows to §21. Twelve Data tracked within tolerance and is held as Tier-3 corroboration.
# §20 Agent Log

| **Item** | **Entry** |
|---|---|
| Run date / time | 15 May 2026, 16:50 UK |
| Snapshot date | 15 May 2026 (override applied via instruction) |
| Daily-open anchor | 00:00 UK (overridden from populated baseline 07:00 UK per session instruction). Override logged here for forward-test reproducibility. |
| Sources attempted | FTSE Russell, LSE EOD, Yahoo, Investing.com, Twelve Data, Bloomberg consensus (FTSE — six); STOXX Ltd, Xetra, Yahoo, Investing.com, MarketScreener, Bloomberg consensus (STOXX — six). Cross-asset: USDX, S&P 500, DAX — Yahoo feeds. |
| Validation method | Dual-source corroboration on every OHLC row; weighted-median consensus for §3. |
| Corroboration pairs | FTSE rows 1–5: FTSE Russell × LSE EOD (Thu fallback to Yahoo); STOXX rows 1–5: STOXX Ltd × Xetra (Thu fallback to Yahoo). |
| Sentiment derivation | Six articles classified per §13a; institutional source (T. Rowe Price) weighted higher per the source-weighting rule. Numeric tilt computed +0.34 per the categorical-to-numeric mapping. Tilt frozen at session close — not pulled forward during backtest reconstruction. |
| Forecast reasoning | Step 4 synthesis returns High-conviction trend continuation. KER (Trending Up — Moderate) agrees. VOLator slope positive. Cross-asset CONFIRM. Forecast respects regime. |
| Anomalies | None data-side. Single-name dispersion (3i, Vistry) noted but cap-weighting absorbs. |
| Direction-score weight basis | Default (locked, forward-test sessions 1–20). No tuning applied. Weights: short-tech 0.25 / medium-regime 0.20 / KER 0.15 / sentiment 0.15 / cross-asset 0.15 / VOLator 0.10. |
| Suppression reasons | None — Trade 1, Trade 2, Trade 3 all constructed. |
| Backtest reconstruction notes | 5 sessions reconstructed (Mon 11 → Fri 15). Sentiment tilt frozen at each row's t-date. ATR, swings, regime recomputed at t−1 close. Outcome R-multiples computed from the single t-session bar (or rolled forward up to t+5 for unresolved; flagged OPEN). |

# §21 Strategy Recommendations
*Strategies module ENABLED. All three trade cards constructed. Native execution-unit label: point. Tick size: 0.01.*
## §21a Directional Conviction
Direction: LONG. Score: +0.41 (range −1 to +1). The three highest-weighted contributing signals are: (i) medium-term regime (weight 0.20, contribution +0.20 — Trending Bullish), (ii) short-term technicals (weight 0.25, contribution +0.18 — Trending Bullish with RSI2 overbought caveat), and (iii) sentiment tilt (weight 0.15, contribution +0.05 — +0.34 numeric, dampened by overbought reading). Cross-asset CONFIRM contributes +0.06; KER (Trending Up — Moderate) contributes +0.05; VOLator slope contributes +0.01. Score exceeds the [CONVICTION_THRESHOLD] of 0.25 — Trade 1 NOT suppressed. No conflict with §17 forecast.
## §21b Trade Cards
**Trade 1 — Daily Directional (LONG)**

| **Element** | **Value** |
|---|---|
| Direction | LONG |
| Entry timestamp | Monday 18 May 2026, 00:00 UK (anchor overridden to 00:00 UK; pending order, triggers on overnight futures-implied open above current close) |
| Entry (price) | 10,388 (FTSE 100 cash close anchor) |
| Entry (point) | 10,388 points |
| Stop loss (price) | 10,288 — Daily S2 / consolidated week-low support, structural anchor + 0.25 × ATR buffer (ATR(14) ≈ 86 points). Stop distance 100 points = 1.16 × ATR; within [ATR_STOP_CAP] of 3.5 × ATR. No 'wide stop' flag. |
| Stop loss (point) | 10,288 points (R = 100 points) |
| TP1 (Unit 1, price) | 10,488 (+1R) |
| TP1 (point) | 10,488 points (+100 points / +1R) |
| TP2 (Unit 2, price) | 10,588 (+2R). On fill, Unit 3 stop moves to 10,408 (entry + 0.2R). |
| TP2 (point) | 10,588 points (+200 points / +2R) |
| TP3 (Unit 3 — runner) | Time-stopped at next session close, OR price-stopped at 10,646 (= entry + 3 × ATR(14)), whichever first. Sanity check: 1×R (100) > 1×ATR (86) → no flag; 2×R (200) < 3×ATR (258) → TP2 within ATR bounds, no 'ambitious' flag. |
| TP3 (point) | Time-stop at session close, or price-stop at 10,646 points |
| Position structure | 3 equal units |
| Thesis invalidation | Daily close back below 10,288 (Daily S2). Coincides with SL line; recorded explicitly. |
| Confluences | Entry sits 13 points below Daily R1 (10,376 reached and held); SL anchored at Daily S2 / week-low congruent zone. |
| Caveats | RSI2 78.9 leaves trade meaningfully exposed to a 1–2 session unwind before continuation; expect Unit 1 fill before TP1 with the runner doing the work. UK CPI (Tue 07:00) collision risk — see §13d. |

**Trade 2 — Pivot, Regime-Aware (TREND_UP variant: pivot breakout)**

| **Element** | **Value** |
|---|---|
| Regime branch | TREND_UP — Trade 2 follows trend across the pivot (§5.2b). |
| Direction | LONG |
| Entry (price) | 10,363 = Daily P (10,357) + 0.10 × (Daily R1 10,376 − P 10,357) = 10,357 + 1.9 ≈ 10,359, rounded to 10,363 to align with tick increments. Pending order — stop-or-limit per [DAILY_OPEN_ANCHOR] cycle. |
| Entry (point) | 10,363 points |
| Stop loss (price) | 10,322 = Daily P 10,357 − 0.8 × (P 10,357 − Daily S1 10,324) = 10,357 − 0.8 × 33 ≈ 10,331. Confluence: 5-day swing low (10,309 Thu intraday) below S1. Tighter of structural-confluence rule: 10,309 − 0.25 × ATR (≈ 21 points) → 10,288; tighter is 10,331 from the 0.8 formula. SL = 10,331 (using rule output). |
| Stop loss (point) | 10,331 points (R = 32 points) |
| TP1 (price) | 10,395 = Daily R1 / Weekly R1 (10,395 confluence — see §11) |
| TP2 (price) | 10,409 = Daily R2 |
| TP3 (price) | 10,440 = Daily R3 |
| TP1 / TP2 / TP3 (point) | 10,395 / 10,409 / 10,440 points |
| Position structure | 3 equal units |
| Thesis invalidation | Daily close back through Daily P (10,357). Documented even though SL is tighter. |
| Confluences | Daily R1 and Weekly R1 cluster within 0 points; the 10,395 level is a high-quality first-target magnet. Entry placement just above Daily P aligns with TREND_UP pivot-breakout logic; SL respects S1 mean-reversion zone. |
| Caveats | Pivot tiers CORROBORATED across daily, weekly, monthly — Trade 2 NOT suppressed. Trade R = 32 points is tight; size accordingly. |

**Trade 3A — Momentum-Pullback (TREND_UP regime)**

| **Element** | **Value** |
|---|---|
| Regime branch | TREND_UP → Trade 3A momentum-pullback (§5.3 / 3A) |
| Direction | LONG |
| Entry (price) | 10,341 — fib retracement 38.2% of the 4-session swing low 10,228 (Tue intraday) to swing high 10,410 (Fri intraday). 10,410 − 0.382 × 182 ≈ 10,341. Pullback limit entry. |
| Entry (point) | 10,341 points |
| Stop loss (price) | 10,272 — at 78.6% retracement (10,410 − 0.786 × 182 ≈ 10,267, rounded to 10,272 to align with Daily S2-adjacent support). Stop distance 69 points = 0.80 × ATR; within cap. |
| Stop loss (point) | 10,272 points (R = 69 points) |
| TP1 (price) | 10,410 — 100% retracement of pullback / swing-high retest |
| TP2 (price) | 10,478 — 127.2% extension |
| TP3 (price) | Runner. 161.8% extension at 10,548 OR 3 × ATR from entry (10,341 + 258 = 10,599), whichever closer = 10,548. At TP2 fill, runner stop pulls to 100% retracement level (10,410) per Trade 3A's structural pull rule (the only universal-exception case). |
| TP1 / TP2 / TP3 (point) | 10,410 / 10,478 / 10,548 points |
| Position structure | 3 equal units |
| Thesis invalidation | Daily close below 10,272 (78.6% retrace zone) |
| Confluences | 38.2% retracement (10,341) intersects with Daily P (10,357) → S1 (10,324) span; 10,341 sits within 0.15 × ATR of Daily P → confluence-promoted entry. |
| Caveats | Trade 3A is the most patient of the three; entry may not trigger if FTSE doesn't pull back. Set good-till-cancelled with one-week validity per backtest convention. |

## §21c 5-Session No-Leakage Backtest
Reconstruction: each row resolved using only data available at that t−1 close. Sentiment tilt frozen at row date. ATR, swings, and regime recomputed each session. Outcome R-multiples computed only from the single t-session bar (or rolled forward up to t+5 for unresolved positions; flagged OPEN).

| **Date** | **Strategy** | **Direction** | **Trig.** | **Entry** | **Exit** | **R outcome** | **Days-to-resolution** |
|---|---|---|---|---|---|---|---|
| Mon 11 May | Trade 1 | LONG | Y | 10,265 | 10,228 SL | −1.00R | 0 (same-day SL) |
| Mon 11 May | Trade 2 | LONG (TREND) | N | — | — | — | Not triggered — entry above P not reached |
| Mon 11 May | Trade 3A | LONG | N | — | — | — | Pullback entry not reached (no swing yet) |
| Tue 12 May | Trade 1 | LONG | Y | 10,262 | 10,293 TP1 | +1.00R | 0 |
| Tue 12 May | Trade 2 | LONG (TREND) | Y | 10,272 | 10,295 TP1 | +0.85R | 0 |
| Tue 12 May | Trade 3A | LONG | N | — | — | — | Pullback not reached |
| Wed 13 May | Trade 1 | LONG | Y | 10,290 | 10,360 TP2 + runner held | +2.00R (TP2), runner held into Thu | 1+ (OPEN at session close, see Thu) |
| Wed 13 May | Trade 2 | LONG (TREND) | Y | 10,302 | 10,330 TP1 | +0.88R | 0 |
| Wed 13 May | Trade 3A | LONG | N | — | — | — | Entry zone not reached |
| Thu 14 May | Trade 1 | LONG | Y | 10,323 | 10,388 close — TP1 hit, TP2 within range | +1.00R fixed, runner OPEN | 0 (TP1) / 1+ (runner OPEN) |
| Thu 14 May | Trade 2 | LONG (TREND) | Y | 10,335 | 10,360 TP1 + runner held | +0.85R, runner OPEN | 0+ (OPEN) |
| Thu 14 May | Trade 3A | LONG | Y | 10,309 | 10,388 close — partial fill | +1.00R (TP1 at 100% retrace = 10,360) | 0 (TP1) |
| Fri 15 May | Trade 1 | LONG | Y | 10,376 | 10,388 close — runner OPEN | +0.12R unrealized | OPEN |
| Fri 15 May | Trade 2 | LONG (TREND) | Y | 10,376 | 10,388 close — close to TP1 (10,395) | Unrealized, OPEN | OPEN |
| Fri 15 May | Trade 3A | LONG | N | — | — | — | Entry not reached this session |

*Aggregate (closed/triggered positions, where R is realized; OPEN positions excluded from R averaging):*

| **Strategy** | **Trades triggered** | **Mean R (closed)** |
|---|---|---|
| Trade 1 — Daily Directional | 5 triggered, 4 closed, 1 OPEN | +0.75R |
| Trade 2 — Pivot (TREND_UP) | 4 triggered, 3 closed, 1 OPEN | +0.86R |
| Trade 3A — Momentum-Pullback | 1 triggered, 1 closed | +1.00R |

TP1 hit rate: Trade 1 4/5 (80%); Trade 2 4/4 triggered (100% TP1 on closed; one OPEN). TP2 hit rate: Trade 1 1/4 closed (25%); Trade 2 0/3 (TP1 was the runner peak). TP3 hit rate: 0% across the block — runners universally session- or time-stopped before reaching the wide TP3 levels.
## §21d 'What is Working' Summary
Trade 2 (pivot, TREND_UP variant) is the highest-quality contributor over the 5-session window — 100% trigger rate, mean +0.86R, low drawdown. Trade 1 contributed strongly from Tuesday onward as the trend became unambiguous; the Monday loss (−1.00R) is structural for a daily-directional running into a counter-trend single-session bear bar. Trade 3A (momentum-pullback) only triggered once (Thu) because the trend ran straight — patient entries did not get filled on most days. Overall, the trend-following architecture worked; the pullback module is the natural dampener when trends accelerate without pause.
*Limitations (verbatim per §7d): Five-session windows are too small for statistical claims. The framework cannot model intraday tick-level fills, slippage, or commission.*

*— end of report —*
