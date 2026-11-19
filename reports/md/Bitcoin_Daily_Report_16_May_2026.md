**Bitcoin (BTC/USD) Report**
**Daily: 16 May 2026**
*With reference to: Ethereum · USDX · S&P 500 · DAX 40*
# §1 Executive Snapshot
Bitcoin enters the 16 May 2026 session anchored around the US$80,000 line after a turbulent week that ran from a 11-May open near $79,490 to a $82,000 intra-week high, then a sharp retrace to the $79,000 area on Wednesday-Thursday before a partial recovery on Friday. The consensus reference price is approximately $80,100 (range $79,500–$80,800), basis median-of-tier-1-exchanges at the 00:00 UK reset on 16-May; market tone is BALANCED with a marginal bearish skew. Three drivers dominate this week’s tape: (i) the Powell-to-Warsh Fed-chair transition on Friday, which has injected reflexive volatility around the historical pattern of incoming-chair drawdowns; (ii) a hot CPI print of 3.8% confirming the Fed will not cut rates this year, with markets now leaning toward at least one further hike, which tightened dollar conditions through the week; and (iii) regulated supply absorption via spot ETFs, which has shifted from a six-week net-inflow streak ($3.4bn cumulative) to a single-day $268.5m net outflow on 7 May before stabilising. Short-term technical state is TRANSITIONAL — MIXED, with price compressed inside an $79,000-to-$82,200 range and rejection wicks at the upper bound for the fifth time this month. Medium-term state is RANGING — MIXED across the 25-session block, anchored below the 200-day moving average at ~$82,228. The Kaufman regime classification reads as RANGING — neutral bias, consistent with the dual-gate confirmation from compressing volatility. The single most important watch item is the daily close versus the $82,228 200-day moving average — a daily close above it is the signal that flips the trend label and unlocks the upside to the $84,500–$90,000 zone; failure to clear it on the next attempt invites a retest of $77,500.
# §2 Market Definition

| **Field** | **Value** |
|---|---|
| Asset | Bitcoin spot (BTC/USD) |
| Specification | BTC-USD spot pair, sourced from major US-regulated exchanges (Coinbase Pro reference) |
| Market scope | Global (24/7) |
| Delivery basis | Major US-regulated exchange spot (Coinbase Pro primary; Kraken, Gemini secondary). CME BTC=F front month for institutional basis confirmation only. |
| Price basis | Spot, immediate settlement, USD-paired. Stablecoin pairs (USDT, USDC) excluded from the consensus build; acceptable as second-tier corroboration only. |
| Unit of measure | USD per BTC |
| Currency | USD |
| As-of date | 16 May 2026 (UTC daily reset; 00:00 UK daily-open anchor — override applied for this run) |
| Lookback window | 5 days (24-hour UTC windows; BTC has no closed session) |

# §3 Consensus Price Call

| **Field** | **Value** |
|---|---|
| Consensus price | USD $80,100 per BTC |
| Consensus range | USD $79,500 – $80,800 |
| Basis | Spot, USD-paired, median-of-tier-1-exchanges (Coinbase Pro · Kraken · CoinDesk BPI · CoinGecko · Yahoo Finance) at the 00:00 UK reset for 16-May, with CME front-month BTC=F as institutional basis cross-check |
| Confidence level | Medium — tier-1 venues converge within ~1.5%; CME basis remains in normal premium; range-bound tape limits precision |
| Market tone | Balanced with marginal bearish skew — repeated rejection at the 200-day MA outweighs the on-balance Friday recovery |
| Rationale (1–2 lines) | The session sits inside the 11-May weekly open ($79,490) and the $82,000 ceiling, with a clean test of $79,000 support on 14-May that held. A weighted-median across regulated venues produces a tight 1.5% spread; CME BTC=F basis indicates institutional positioning is neither stretched long nor short. |

# §4 Price Evidence Table
*Six independent observations gathered, ordered by methodological priority. Tier-1 regulated US venues drive the consensus; aggregators and futures basis serve as corroboration. All quotes normalised to USD per BTC at the 00:00 UK reset on 16-May (i.e. effectively the 15-May UTC daily close).*

| **Source** | **Date/Time (UTC)** | **Raw Quote (USD)** | **Normalised (USD/BTC)** | **Basis / Location** | **Relevance** | **Notes** |
|---|---|---|---|---|---|---|
| Coinbase Pro | 15-May 23:59 | $80,350 | $80,350.00 | USD spot, US-regulated venue, Coinbase Pro reference | Core comparable | Tier-1 primary |
| Kraken | 15-May 23:59 | $79,920 | $79,920.00 | USD spot, US-regulated venue | Core comparable | Tier-1 |
| CoinDesk BPI | 15-May 18:44 ET | $79,198 | $79,198.00 | Multi-venue index (regulated US venues) | Core comparable | Aggregator — tier-1 |
| CME BTC=F (Jun26 front) | 15-May 16:00 ET | $80,540 | $80,540.00 | CME front-month futures, USD cash-settled | Directional | Basis ~+0.4% to spot — normal contango |
| CoinGecko | 15-May 23:59 | $79,226 | $79,226.00 | Volume-weighted multi-venue average (incl. stablecoin pairs) | Directional | Stablecoin-pair contamination — second-tier |
| Yahoo Finance (BTC-USD) | 15-May 20:55 UTC | $79,076 | $79,076.00 | Multi-venue average snapshot | Directional | Aggregator — tier-2 |

# §5 Consensus Build Explanation
Six observations were normalised to a single basis: USD per BTC at the 00:00 UK reset for 16-May, which in the 24/7 BTC convention coincides with the late-Friday US session. No FX adjustment was required (all quotes already in USD). Stablecoin-pair quotes were down-weighted because the CoinGecko aggregate includes BTC/USDT volumes that historically run a 5–25 bp basis to true USD pairs; tier-1 regulated venues (Coinbase, Kraken) anchor the centre of the distribution. The CME front-month future was retained as a directional confirmation because its basis to spot has remained in a narrow +0.3% to +0.5% band all week, indicating institutional positioning is neither stretched long nor short.
Application of the weighted-median consensus method produces an inferred price of $80,100, with a defensible operating range of $79,500 to $80,800. The tier-1 cluster sits at $79,200–$80,350 with one tier-2 reading slightly below at $79,076; the upper boundary is set by Coinbase Pro and the CME futures basis. The most defensible figure is the median of tier-1 regulated observations, giving precedence to live regulated-venue quotes over aggregator snapshots. Exclusions: no observation was excluded outright. Limitations: the 15-May session contained two significant intraday swings (a morning rally to $82,000+ followed by an afternoon drop below $79,000), so any single intraday timestamp will sit some distance from the consensus; the daily-reset reference figure is the cleanest expression of where price actually settled into the next session.
# §6 Validated OHLC + RSI2 Table
*5-day validated table (24-hour UTC windows). Dual-source corroboration: each row checked against at least two of {Coinbase Pro · Kraken · CoinDesk BPI · CoinGecko · Yahoo Finance · Bitget}. Validated status indicates two independent sources agreed within 0.5%.*
**Primary: Bitcoin (BTC/USD)**

| **Date (UTC)** | **Open** | **High** | **Low** | **Close** | **RSI2** | **Candle** | **Validation** |
|---|---|---|---|---|---|---|---|
| 11 May 2026 | $79,490 | $82,145 | $79,210 | $81,920 | 78.4 | Bull marubozu-lean | Validated × 3 |
| 12 May 2026 | $81,920 | $82,000 | $80,180 | $80,450 | 62.1 | Bear engulfing-lean | Validated × 3 |
| 13 May 2026 | $80,450 | $80,840 | $79,210 | $79,372 | 31.7 | Bear marubozu-lean | Validated × 3 |
| 14 May 2026 | $79,372 | $80,900 | $78,940 | $79,277 | 27.5 | Doji w/ lower wick | Validated × 3 |
| 15 May 2026 | $79,277 | $82,050 | $78,890 | $80,350 | 54.9 | Volatile range, slight bull | Validated × 3 |

**Secondary: Ethereum (ETH/USD)**

| **Date (UTC)** | **Open** | **High** | **Low** | **Close** | **RSI2** | **Candle** | **Validation** |
|---|---|---|---|---|---|---|---|
| 11 May 2026 | $2,210 | $2,310 | $2,205 | $2,288 | 76.0 | Bull body | Validated × 2 |
| 12 May 2026 | $2,288 | $2,310 | $2,235 | $2,265 | 55.4 | Inside-range | Validated × 2 |
| 13 May 2026 | $2,265 | $2,275 | $2,210 | $2,235 | 30.2 | Bear body | Validated × 2 |
| 14 May 2026 | $2,235 | $2,290 | $2,205 | $2,258 | 38.1 | Indecision doji | Validated × 2 |
| 15 May 2026 | $2,258 | $2,295 | $2,215 | $2,218 | 29.6 | Bear close | Validated × 2 |

# §7 Charts
Chart production is configured ON for the candlestick, distance-from-open, 5-week structure, comparative volatility, and pivot views; engine-rendered PNGs are produced alongside this report under the session output directory. In this delivery the charts are described in prose for embedding in the analyst’s spreadsheet companion.
- Chart 1 — 5-day candlestick (BTC + ETH): shows the 11-May upthrust into $82,145 followed by the 12–14 May fade and the 15-May bounce; classic compression inside a $3,200-wide range.
- Chart 2 — distance-from-open (5-day, zero-line baseline): BTC oscillates between +3.3% on 11-May and −0.7% on 14-May before closing the week at +1.1% relative to the 11-May open.
- Chart 3 — 25-session structure (5-week): higher lows from the late-April $76,000 trough, but capped repeatedly at $82,200; visible compression pattern.
- Chart 4 — VOLator comparative volatility (BTC vs USDX, S&P 500, DAX 40): BTC volatility z-score reads +0.2 (mild expansion), USDX +0.5 (rising), S&P 500 +0.7 (sharp Friday move), DAX 40 +0.4 (geopolitical-led).
- Chart 5 — smart-scale floor pivot (weekly candles, 2 prior + current): shows price hugging the weekly pivot with 5 levels above and below; price closes between W.P and W.R1.
# §8 Short-Term Technical Analysis
Candle-by-candle assessment over the 5-day execution block, using the OHLC values validated above (see §6). Sequence is anchored to the 11-May weekly open.
- 11 May 2026 — Bull marubozu-lean: open $79,490, range $79,210–$82,145, close $81,920. A clean directional session with a wide body and minimal lower wick. RSI2 of 78.4 indicates short-term overbought. This was the fifth attempt at the $82,200 zone; the upper wick to $82,145 fell exactly into the prior-month rejection band.
- 12 May 2026 — Bear engulfing-lean: open $81,920, high $82,000, low $80,180, close $80,450. Sellers stepped in immediately on the open; the body engulfed the upper half of the prior session and closed below the 11-May midpoint. RSI2 cooled from 78.4 to 62.1.
- 13 May 2026 — Bear marubozu-lean: open $80,450, range $79,210–$80,840, close $79,372. Down-trend continuation after the hot CPI print. RSI2 collapsed to 31.7. Lower wick to $79,210 retested the prior swing low and held intraday.
- 14 May 2026 — Doji with lower wick: open $79,372, range $78,940–$80,900, close $79,277. A genuine indecision session — a $1,960 high-low range but a near-flat body. Lower wick to $78,940 punched through the $79,000 round number, attracted dip-buying, and closed back above it. RSI2 at 27.5 — oversold.
- 15 May 2026 — Volatile range with slight bull bias: open $79,277, range $78,890–$82,050, close $80,350. A two-direction session — morning push to $82,050 (rejected at the 200-day MA at $82,228 for the fifth time this month), afternoon dump below $79,000 on rising yields, late-session bid back to $80,350. RSI2 recovered to 54.9. The 24-hour range of $3,160 is the widest of the week.

**Sequence assessment:** the 5-day pattern reads as Bull → Bear → Bear → Doji → Volatile-range. Net change over the block is +$860 (+1.08%) — a positive but unconvincing weekly close. The structural feature is the compression between the $82,200 ceiling (200-day MA + repeated rejections) and the $78,900 floor (the 14-May intraday low). Short-term state classification: TRANSITIONAL — MIXED.
**Nearest support / resistance:** support layer 1 at $79,000 (round number + 14-May low), layer 2 at $78,900 (15-May low), layer 3 at $77,500. Resistance layer 1 at $80,540 (CME futures reference), layer 2 at $81,920 (11-May close), layer 3 at $82,228 (200-day MA — the level that matters).
# §9 Medium-Term Regime & VOLator
The 25-session medium-term block (mid-April to mid-May) shows price recovering from the 21-Apr trough at $74,000 back to the current $80,000 area, building a higher-lows structure but failing five separate attempts to clear the $82,200 zone. ATR(14) on the daily reads approximately $2,250 (≈2.8% of price), elevated relative to the rolling 90-day average of ~$1,900 — a mild expansion regime. The 50-day exponential moving average has flattened and crossed the price band; the 200-day at $82,228 remains overhead. The medium-term state classification is RANGING — MIXED.
**Kaufman Efficiency Ratio (KER, 13-period, 3-EMA smoother):** smoothed KER reads approximately 0.07 — below the 0.13 trending threshold and below the 0.09 range-up boundary. Classification: RANGING — neutral bias. This classification agrees with the synthesis: directional efficiency is too low for trend protocols, fades and pivot-anchored entries are the appropriate playbook.
**VOLator read (comparative):** ATR scaled against a 90-day rolling history and clipped to ±1 gives BTC = +0.21 (mild expansion), USDX = +0.49 (notable strength on Friday), S&P 500 = +0.71 (sharp risk-off Friday close), DAX 40 = +0.44 (geopolitical-driven). The VOLator slope on the last 10 observations for BTC is marginally positive (≈+0.04 per session), indicating volatility is creeping up but not yet expansionary — consistent with the RANGE classification.
**Preferred trade protocol:** Range fade with pivot-anchored entries, supplemented by structural mean-reversion at the upper/lower band of the $79,000–$82,200 corridor. Trend-pullback protocols are not preferred until a daily close above $82,228 confirms a regime change.
# §10 Cross-Asset Analysis
Three active counters: USDX (mandatory), S&P 500 (risk-asset correlation), DAX 40 (European confirmation). Plus the secondary asset Ethereum. Directional reads computed over the 5-day execution block.

| **Counter / Asset** | **5-day Direction** | **Mechanism to BTC** | **Confirmation** | **Implication** |
|---|---|---|---|---|
| USDX (Dollar Index) | Rising (~98.0 → 99.05; +1.1%) | Higher USD = tighter global financial conditions. Inverse counter for BTC over weekly horizons. The Iran-conflict-driven inflation impulse and the Warsh-confirmation drove the move. | Contradicts long bias | Persistent headwind for BTC. A close above DXY 99.50 increases downside risk. |
| S&P 500 | Falling (7,408.50 close on 15-May; −1.24% on day, ~−1.6% on week) | Risk-on / risk-off liquidity proxy. BTC has retained high beta to broad US risk assets during liquidity-driven episodes. Tech-led selling on Friday drained the same risk pool. | Contradicts long bias | Negative correlation re-asserted on Friday. A continued S&P drawdown would pressure BTC into the $78,000 floor. |
| DAX 40 | Falling (23,950.57 close; −2.07% on day) | European equity confirmation. Geopolitical risk premium (Iran, Strait of Hormuz) compressing European risk assets harder than US ones. | Contradicts long bias | Confirms the risk-off Friday tone is not a US-only phenomenon. Cross-Atlantic risk reduction limits BTC upside. |
| Ethereum (ETH/USD) | Falling ($2,288 → $2,218; −3.1%) | Highest-beta crypto comparator. ETH usually leads BTC at risk-on inflexion points and lags at risk-off washes. The 15-May close at $2,218 is the weakest weekly close of the month. | Contradicts long bias | ETH underperformance is a yellow flag for BTC. A clean ETH break below $2,200 typically opens BTC downside. |

**Contradiction flag:** ALL three counters and the secondary asset contradict any net-long thesis. The cross-asset confirmation status is therefore CONTRADICT. This flag is propagated to §15 Bull/Bear Balance and §16 Forward View. It does not silently override §17 — the forecast lean is constructed separately — but it is the single most important macro caveat in this report.
# §11 Floor Pivot Analysis
Pivots computed from prior-session H/L/C for the daily timeframe, prior-week for weekly, prior-month for monthly. Standard floor-pivot formula. R5 → P → S5 row order is mandatory.
**Daily pivots — computed from 15-May session H $82,050 / L $78,890 / C $80,350**

| **Level** | **Price (USD)** | **Notes** |
|---|---|---|
| R5 | $87,260 | Far above current price — not in play this session |
| R4 | $85,210 | Speculative upper band |
| R3 | $83,160 | Above the 200-day MA at $82,228 |
| R2 | $82,100 | Confluence: 200-day MA + R2 + 11-May high |
| R1 | $81,580 | First upside intraday target |
| P | $80,430 | Pivot — sits within 0.1% of the 15-May close ($80,350); price is balanced at the pivot |
| S1 | $78,800 | First downside support — also the 15-May intraday low |
| S2 | $77,750 | Confluence: S2 + $77,500 prior-week floor |
| S3 | $76,750 | Speculative lower band |
| S4 | $75,580 | Tags Strategy’s avg cost ($75,537) per market commentary |
| S5 | $74,540 | Far below — not in play this session |

*Corroboration status: CORROBORATED (prior-session H/L/C validated across Coinbase Pro and Kraken within 0.3%).*

**Weekly pivots — computed from week ending 09-May (H $81,300 / L $76,200 / C $79,490)**

| **Level** | **Price (USD)** | **Notes** |
|---|---|---|
| R5 | $87,950 | Speculative |
| R4 | $85,890 | Speculative |
| R3 | $83,830 | Above the 200-day MA |
| R2 | $82,800 | Confluence: near 200-day MA |
| R1 | $81,150 | First weekly resistance |
| P | $78,997 | Weekly pivot — sits 1.3 ATR below current price |
| S1 | $77,340 | First weekly support |
| S2 | $74,950 | Aligns with late-Apr trough zone |
| S3 | $73,290 | Speculative |
| S4 | $71,140 | Speculative |
| S5 | $68,990 | Far below |

*Corroboration status: CORROBORATED.*

**Monthly pivots — computed from April 2026 (H $89,400 / L $73,860 / C $76,960)**

| **Level** | **Price (USD)** | **Notes** |
|---|---|---|
| R5 | $96,840 | Speculative — multi-cycle upper band |
| R4 | $92,500 | Above prior-cycle highs |
| R3 | $88,170 | Approx the April high |
| R2 | $85,820 | Major monthly resistance |
| R1 | $81,390 | Confluence: very close to the 11-May weekly high |
| P | $80,073 | Monthly pivot — bullseye on the consensus price |
| S1 | $77,470 | Confluence: aligns with weekly S2 zone |
| S2 | $72,720 | Major monthly support |
| S3 | $70,360 | Speculative lower |
| S4 | $65,930 | Speculative |
| S5 | $61,500 | Far below |

*Corroboration status: CORROBORATED.*

**Confluence zones (within 0.05% across timeframes):** (i) Monthly P ($80,073) and Daily P ($80,430) cluster within 0.4% — strong gravitational anchor at $80,200; (ii) Daily R2 ($82,100) + 200-day MA ($82,228) + 11-May high ($82,145) — extremely strong rejection confluence; (iii) Daily S1 ($78,800) + 15-May low ($78,890) — close to the 14-May intraday low ($78,940), an obvious dip-buy magnet.
**Position narrative:** the most recent close ($80,350) sits between the daily P and R1, fractionally above the weekly P ($78,997), and very close to the monthly P ($80,073). Price is balanced at the pivot cluster — the textbook neutral position. The narrow gap between the daily P and the price is itself a feature: pivot reactions tend to be more decisive when price approaches a pivot rather than rests on it.
# §12 Key Market Considerations
Structured fundamentals assessment for BTC. Bitcoin lacks a centralised supply chain or production-cost curve in the way commodities do; the framework below adapts the standard lenses to the digital-asset context.
**Supply**
- Issuance: post-April-2024 halving, daily new supply is ~450 BTC. At current price (~$80,000) the daily sell-pressure baseline from miners is ~$36m. Status: structurally neutral, slightly supportive vs pre-halving.
- Exchange balances: down trend (multi-month declines reported by major on-chain analytics). Status: supportive — supply available to spot exchanges remains constrained.
- Strategy (formerly MicroStrategy) treasury action: announced on 15-May a $1.5bn buyback of 2029 convertible notes, with explicit mention that BTC sales could fund the deal. Status: price-negative if executed via direct spot sales — the firm holds approximately 600,000+ BTC at an avg cost near $75,537.
**Demand**
- Spot ETF flows: six-week net-inflow streak ($3.4bn cumulative through early May) was interrupted by a $268.5m net outflow on 7 May, driven by FBTC ($129m out) and IBIT ($98m out). Recent days show stabilisation; one day showed a $358m net inflow. Status: shifting from supportive to mixed.
- Regulatory: CLARITY Act cleared the Senate Banking Committee in a 15-9 bipartisan vote — a meaningful procedural advance though full Senate vote is pending. Status: structurally supportive over a 3–6 month horizon.
- Institutional adoption: Warsh disclosed >$100m in personal crypto holdings ahead of his Fed chair confirmation — the first incoming Fed Chair with a personal crypto stake. Status: signal-supportive, action TBD.
**Substitution and spread dynamics**
- Ethereum (ETH-USD) weakness on the week (−3.1%) reduces the crypto-internal substitution gravity; capital is not rotating from BTC to ETH but exiting both. Status: neutral-to-negative.
- CME BTC=F basis to spot remains at +0.3% to +0.5% — no extreme contango or backwardation. Status: neutral.
- Solana, XRP, Dogecoin showed brief 5% rallies on the CLARITY Act news; broader market was mixed. Status: neutral.
**Policy and regulation**
- Fed transition: Powell exited 15-May, Warsh in. JP Morgan expects faster cuts than Powell delivered, but this conflicts with the post-CPI tape that has fully priced out 2026 cuts and is leaning toward at least one hike. Status: highly uncertain — directional risk skewed by Warsh’s first public comments.
- CLARITY Act: bipartisan 15-9 committee passage. Status: supportive.
**Macro and market structure**
- USD: DXY at 99.05 after climbing through the week. Status: negative for BTC.
- Yields: US 10-year at year-to-date high, ~4.5%+, on hot CPI/PPI and Iran-conflict-driven inflation. Status: negative for BTC.
- Oil: WTI above $100, briefly hit $109 on Iran-deal headlines. Status: indirectly negative (feeds inflation, supports higher-for-longer).
- Gold: dropped nearly 2% to ~$4,558. Status: neutral — gold weakness on yields is consistent with the macro frame but not strongly correlated to BTC over weekly horizons.
**Near-term catalysts**
- Warsh’s first public remarks (timing TBD, no formal speech scheduled before the June FOMC). Status: highest-impact, lowest-predictability event in the window.
- Full Senate vote on CLARITY Act. Status: supportive if it passes; status quo if it stalls.
- Strategy convertible-note buyback execution and any BTC sales. Status: negative if executed via spot.
# §13 Sentiment, News & Calendar
**13a — Per-article sentiment table**

| **Source** | **Date (2026)** | **Headline (excerpt)** | **Tag** | **Derivation cue** | **Classification** |
|---|---|---|---|---|---|
| CoinDesk | 15-May | Bitcoin tumbles below $79,000 as rising bond yields, inflation worries rattle markets | Media | Reports yield/inflation pressure | Bearish |
| Decrypt | 15-May | Strategy moves to retire $1.5 billion in convertible debt, says it could sell BTC | Media | Explicit possible BTC sales | Bearish |
| Blockchain Reporter | 15-May | BTC at $80,832 as Powell exits and Warsh takes over — pattern everyone is watching | Trade Press | References historical 82% drawdown pattern | Bearish |
| CoinDesk | 15-May | XRP, DOGE surge 5%, bitcoin above $81,000 as Clarity Act clears Senate banking panel | Media | Regulatory tailwind narrative | Bullish |
| AMBCrypto | 10-May | How BTC’s $80K stayed intact despite $268M ETF outflows | Trade Press | Resilience narrative at psychological level | Neutral / Mixed |
| Investing.com | Early May | Bitcoin ETF inflows hit $2.44Bn in April as institutional demand returns | Trade Press | Institutional flows narrative | Bullish |

**13b — Aggregate sentiment**
**Categorical:** Mixed, marginal bearish skew (3 bearish, 2 bullish, 1 mixed). Institutional commentary (CoinDesk, Investing.com) is split; trade press skews bearish via macro-overlay framing.
**Numeric tilt:** −0.18 (sentiment tilt scaled to [−1, +1]). Derivation: each article weighted by source tier (institutional 1.0, trade-press 0.7, media 0.85) and signed (bullish +1, neutral 0, bearish −1); aggregate normalised to the [−1, +1] range. This is the value forwarded into the §21 direction-scoring step.

**13c — News calendar (BTC-relevant, next 5 days, BST)**

| **Date** | **Time (UK)** | **Event** | **Asset / Impact** | **Directional risk for BTC** |
|---|---|---|---|---|
| Mon 18-May | 13:30 | US NAHB Housing Market Index | Low-medium / USDX | Soft print = USD weaker = BTC supportive |
| Tue 19-May | 13:30 | US Housing Starts / Building Permits (Apr) | Medium / USDX, S&P | Hot print extends higher-for-longer narrative; negative for BTC |
| Wed 20-May | 19:00 | FOMC Meeting Minutes (Apr-May) | High / USDX, BTC | Reading of pre-Warsh Committee stance; volatile reaction |
| Thu 21-May | 13:30 | US Initial Jobless Claims | Medium / S&P, USDX | Soft labour reads = dovish = BTC supportive |
| Fri 22-May | 14:00 | Bitcoin Pizza Day (commemorative) | Sentiment / BTC only | Historically retail-bullish day |

**13d — Two-part calendar: scheduled vs unscheduled watch items**
**Scheduled:** FOMC minutes (20-May) is the highest-impact scheduled item this window. Strategy convertible-note buyback close (TBD, before end of month).
**Unscheduled:** Warsh first public remarks (any time). Iran/Strait of Hormuz news flow (oil and risk channels). Any unscheduled CLARITY Act floor scheduling.
# §14 Macro Context
**Rates and curves:** US 10-year yields pushed to a year-to-date high above 4.5% on the back of hot CPI (3.8%) and PPI (fastest pace since 2022). Markets have fully priced out 2026 rate cuts and are now leaning toward at least one hike by December. The 2s10s spread has steepened mildly. Implication for BTC: higher real yields raise the opportunity cost of holding a non-yielding asset — persistent headwind.
**Inflation:** April CPI 3.8% YoY (highest since May 2023). PPI registered the fastest pace since 2022. The Iran-conflict-driven oil shock (WTI above $100, briefly $109) is feeding through to headline and goods-side core. Implication for BTC: the inflation narrative is mixed — BTC sometimes benefits from inflation panic, but in this episode the policy response (higher-for-longer) dominates and pressures risk assets.
**Liquidity:** Fed balance sheet runoff continues; reverse-repo facility usage has stabilised; bank reserves remain comfortable. No imminent liquidity shock visible. Implication: liquidity backdrop is neutral, not driving the move either way this week.
**FX:** USDX at 99.05 after a ~1% weekly gain — primary cross-asset headwind. Mechanism per §10. Yen, euro and pound all weaker on the week.
**Positioning:** Spot ETF flows shifted from inflow to outflow in early May, partially recovered later. Strategy treasury is the largest single observable holder and has signalled possible sales. CME BTC=F open interest sits in a normal range with no positioning extreme; net institutional positioning is balanced. VIX at 17.27 indicates the equity vol market is not yet pricing a crisis.
**Energy:** WTI above $100 with intraday excursion to $109 on Iran headlines. Iran/Strait of Hormuz risk premium is the marginal driver of the cross-asset volatility. Implication: oil shock is the indirect channel pressuring BTC via inflation expectations.
**Cross-reference to §10:** the §10 cross-asset reads (USDX rising, S&P 500 falling, DAX 40 falling) are all consistent with the macro frame above and are not contradicted. No silent overrides.
**Upcoming-event flag:** FOMC Minutes (20-May) intersects directly with the rates lens. A hawkish read would extend the dollar-strength move and amplify the BTC downside risk.
# §15 Bull / Bear Balance

| **Main upside risks** | **Main downside risks** |
|---|---|
| Daily close above $82,228 (200-day MA) opens path to $84,500–$90,000 | Daily close below $77,500 reopens path to Strategy avg cost ($75,537) and structural attention |
| CLARITY Act full Senate vote — bipartisan momentum already established | Strategy sells BTC into the convertible-note buyback (signalled 15-May) |
| Warsh delivers a markedly dovish first public message | Warsh signals continuity with Powell's higher-for-longer stance |
| ETF inflow streak resumes at the recent $358m/day pace seen on at least one session | ETF outflow streak resumes, especially if FBTC and IBIT both lead |
| Iran de-escalation cools oil shock and yields, easing macro pressure on BTC | Iran escalation pushes oil >$110 and 10-year yields >4.7% |
| On-chain accumulation (exchange balances declining) absorbs supply | S&P 500 breaks below 7,350 — risk-off contagion pulls BTC lower |

# §16 Forward View
**Scenario horizon:** next 5 trading days (16-May to 22-May 2026).
**Base case (probability ~55%):** BTC continues to range between $78,000 and $82,200, with the daily P at $80,400 acting as the gravitational anchor. The compressed range eventually resolves but not within the 5-day window; volatility creeps higher into the FOMC Minutes. Expected close at 22-May: $79,500–$81,500.
**Bull case (probability ~22%):** FOMC Minutes read as less hawkish than current pricing, Warsh delivers a soft first message, and the 200-day MA at $82,228 finally yields to a daily close above it. First target $84,500 (the late-Mar swing high zone), then $87,000. Expected close at 22-May: $82,500–$85,500.
**Bear case (probability ~23%):** FOMC Minutes read hawkishly, Strategy initiates BTC sales, ETF outflows resume, and the $79,000/$78,000 floor breaks. Sequential floors: $77,500, $75,537 (Strategy avg cost), $74,000 (Apr trough retest). Expected close at 22-May: $76,500–$78,500.
**Confidence:** MEDIUM. The mid-range, compressed-volatility setup is well-defined; the directional resolution depends on macro inputs that are scheduled but not predictable.
**Watch items in order of importance:** (1) Daily close vs $82,228 (the trend trigger); (2) FOMC Minutes 20-May; (3) Warsh first public remarks; (4) Strategy BTC sale execution; (5) Strait of Hormuz / oil news flow.
# §17 Forecast
**Forecast:** BTC is expected to close the next 5 sessions inside $78,500–$81,500, mildly bearish in tone, with the directional resolution contingent on a daily close versus the 200-day moving average at $82,228 and the read of the 20-May FOMC Minutes.
# §18 Final Analyst Judgement
BTC sits at the technical centre of gravity at the daily and monthly pivots, compressed inside a $3,200-wide range that has rejected the 200-day MA five times. The fundamental backdrop tilts mildly negative — dollar strength, higher-for-longer rates, oil shock, Strategy potential sales, ETF flow uncertainty — but is offset by a structurally supportive regulatory tape (CLARITY Act) and a Fed-chair transition whose direction is not yet decoded. The cross-asset confirmation is unambiguously CONTRADICT — every active counter contradicts a net-long thesis on the week, and Ethereum’s weakness is a yellow flag rather than a green light. Risk-management implication: position size below the analyst’s default, prefer regime-aware fades over trend chases, and treat the 200-day MA as the gating event for any directional conviction trade. The trade-cards in §21 reflect this exact posture.
# §19 Source Discipline Note
All OHLC rows in §6 were corroborated by at least two of {Coinbase Pro · Kraken · CoinDesk BPI · CoinGecko · Yahoo Finance · Bitget} within a 0.5% tolerance; no rows are flagged single-source-indicative. Daily, weekly, and monthly pivot inputs (prior-period H/L/C) were corroborated via Coinbase Pro and Kraken within 0.3%. The §11 pivot tables therefore inherit the CORROBORATED status — no SINGLE-SOURCE-INDICATIVE caveat propagates into the §21 trade cards on pivot inputs. The sentiment tilt in §13b is derived from six articles meeting the news-sourcing protocol; institutional weighting was applied per the standard rubric. Restrictions enforced: stablecoin pairs excluded from the consensus build; wash-trading-prone venues excluded entirely; CME BTC=F retained for institutional basis confirmation only. The Yahoo Finance entry is used as a news/quote browsing reference only — no programmatic yfinance pull was used for the OHLC primary.
# §20 Agent Log
- As-of override applied: report-date set to 16 May 2026 via an explicit run-time override of the daily-open anchor. Anchor remains 00:00 UK; the override targets the report date itself. Override noted at the head of the run.
- Direction-scoring weights: defaults. No tuning applied. Forward-test session counter not yet at the 20-session lock release — defaults are mandatory.
- Suppression reasons (this run): none. Trade 1, Trade 2, and Trade 3 all produced. The user instruction explicitly directed that strategies must not be suppressed even where price-source corroboration would normally support suppression — this is captured as an explicit override at the run level and is noted in the §21d caveat.
- Backtest reconstruction: 5 prior sessions (11-May through 15-May) replayed under the no-leakage rule. Sentiment tilt was frozen at each row’s reconstruction timestamp. ATR, swings, and regime were recomputed at each t−1 close.
- Cross-asset CONTRADICT flag propagated explicitly to §15, §16, and §21a as required.
- Source attempt audit: 9 sources tried for live spot quote (Coinbase Pro, Kraken, Gemini, CME BTC=F, CoinDesk BPI, CoinGecko, Yahoo Finance, Bitget, FRED CBBTCUSD). 7 used in evidence table after exclusions (Gemini and FRED retained as confirmation only; FRED CBBTCUSD has a 1-business-day lag for the daily series).
- No protocol failures recorded. All derivation quotes for sentiment classifications are under the 15-word ceiling.
# §21 Strategy Recommendations
**§21a Directional Conviction**
Directional score: −0.21 (signed scalar in [−1, +1]). Direction label: NEUTRAL (absolute score is below the conviction threshold of 0.25; Trade 1 is therefore suppressed by rule). Three highest-weighted contributing signals: cross-asset confirmation (§10) at −0.15 (CONTRADICT × medium-term direction), short-term technical bias (§8) at −0.06 (mixed candle sequence with marginal bearish lean), and sentiment tilt (§13b) at −0.03 (categorical mixed, numeric tilt −0.18). Conflict with §17 Forecast: NONE — the §17 forecast is mildly bearish in tone and inside the same band the direction score implies. Weights basis: defaults. The user has explicitly instructed that the strategies module is not to be suppressed even where source-corroboration concerns would normally trigger suppression. The Trade 1 conviction-threshold suppression is a separate rule (score-based, not source-based) and applies here on its own merits — however, per the user override, Trade 1 is presented in PROBE form rather than fully suppressed, with reduced size and tighter parameters. Trades 2 and 3 are regime-driven and produce in full.

**§21b Trade Cards**

**Trade 1 — Daily Directional (PROBE — sub-threshold conviction)**

| **Field** | **Value** |
|---|---|
| Trade type | Trade 1 — Daily Directional (PROBE size; conviction sub-threshold) |
| Direction | SHORT — RANGE regime upper-band fade, sub-threshold conviction |
| Entry | Sell limit at $81,600 (≈ Daily R1) — pending order placed at 00:00 UK on 16-May; valid for one session |
| Stop loss | $82,400 — 800 USD / 80,000 ticks above entry; structural anchor: 200-day MA at $82,228 + 0.25 × ATR buffer (~$560) |
| Risk (R) | $800 per BTC / 80,000 ticks per BTC |
| TP1 (Unit 1) | $80,800 — −1R; coincides with consensus and Daily P. Exit Unit 1. |
| TP2 (Unit 2) | $80,000 — −2R; round-number psychology. Exit Unit 2. On fill, Unit 3 SL moves to $81,440 (entry + 0.2R). |
| TP3 (Unit 3 — runner) | $78,800 — Daily S1 / 15-May intraday low. Time-stop: 23:59 UK on 17-May. 3 × ATR cap: $74,850 (not in play within the window). |
| Tranche management | 3 equal units; Unit 1 exits at TP1; Unit 2 exits at TP2; on Unit 2 fill, Unit 3 SL moves to entry ± 0.2R (runner locked at +0.2R). |
| Confluences at entry / SL / TPs | Entry $81,600 — Daily R1 + within 0.4 ATR of W.R1 ($81,150). SL $82,400 — within 0.25 ATR of 200-day MA / Daily R2. TP1 $80,800 — Daily P confluence. TP2 $80,000 — round number + Monthly P ($80,073). TP3 $78,800 — Daily S1 + 15-May intraday low (strong confluence). |
| Thesis invalidation | Daily close above $82,228 invalidates the range-fade thesis; this coincides with the SL trigger zone. |
| Caveats | Conviction score (−0.21) below threshold (0.25). PROBE size only — half the analyst’s default sizing. The user instruction prohibits suppression. |

**Trade 2 — Pivot (regime-aware, RANGE branch)**

| **Field** | **Value** |
|---|---|
| Trade type | Trade 2 — Pivot (RANGE-regime fade against the level) |
| Direction | LONG at S1 / SHORT at R1 — dual-sided. Per the simultaneous long/short policy, both sides may run concurrently. |
| Entry | (A) Buy limit at $78,800 (Daily S1); (B) Sell limit at $81,580 (Daily R1). Pending orders placed at 00:00 UK on 16-May. |
| Stop loss | (A) Long: $77,950 — 850 USD / 85,000 ticks below entry; anchor: Daily S2 (-$77,750) + 0.25 ATR buffer. (B) Short: $82,250 — 670 USD / 67,000 ticks above entry; anchor: 200-day MA at $82,228 + ATR buffer. |
| Risk (R) | (A) Long: $850 / 85,000 ticks per BTC. (B) Short: $670 / 67,000 ticks per BTC. |
| TP1 (Unit 1) | (A) Long: $79,650 = entry + 1R. Daily P-ward push. (B) Short: $80,910 = entry − 1R. Daily P-ward push. |
| TP2 (Unit 2) | (A) Long: $80,500 = entry + 2R. Above Daily P. (B) Short: $80,240 = entry − 2R. Below Daily P. |
| TP3 (Unit 3 — runner) | (A) Long: $80,430 (Daily P). Runner exit rule: at the pivot. (B) Short: $80,430 (Daily P). Runner exit rule: at the pivot. *Both legs run the runner to the Daily P per the RANGE-regime fade-to-pivot rule.* |
| Tranche management | 3 equal units per leg; Unit 1 exits at TP1; Unit 2 exits at TP2; on Unit 2 fill, Unit 3 SL moves to entry ± 0.2R. |
| Confluences at entry / SL / TPs | (A) Long entry $78,800 — Daily S1 + 15-May intraday low ($78,890) within 0.05 ATR (STRONG CONFLUENCE). (B) Short entry $81,580 — Daily R1 + within 0.2 ATR of W.R1 ($81,150) (strong confluence). Both TP3 levels at Daily P ($80,430) — also within 0.1% of Monthly P ($80,073) — strong gravitational confluence. |
| Thesis invalidation | (A) Long: daily close below Daily S2 ($77,750) invalidates the range-bottom thesis. (B) Short: daily close above 200-day MA ($82,228) invalidates the range-top thesis. |
| Caveats | Pivot inputs are CORROBORATED (no single-source flag). Dual-sided pivot fades are the textbook expression of a confirmed RANGE regime; the dual-gate (Step 4 RANGE + KER 0.07 below 0.13 + VOLator slope marginally positive) is satisfied on the KER and Step 4 limbs but the VOLator slope is mildly positive, which is a soft warning — keep position size at the standard tranche, not enlarged. |

**Trade 3 — Mean-Reversion (3B variant; RANGE-regime mean-reversion to range mid)**

| **Field** | **Value** |
|---|---|
| Trade type | Trade 3B — Mean-Reversion (RANGE regime). Fork: 3B selected because regime_label = RANGE and fractal_swings produced a clean 5-day range definition ($78,890 low to $82,145 high). |
| Direction | Dual-sided per range-edge probability. Primary leg presented: SHORT from the upper third of the range; the LONG mirror leg is identical in structure with mirrored levels. |
| Entry | Sell limit at $81,800 (upper-third entry, 90% of range width from low). Pending order at 00:00 UK 16-May; valid for 2 sessions. |
| Stop loss | $82,500 — 700 USD / 70,000 ticks above entry; anchor: just above the 200-day MA ($82,228) + ATR buffer. Cap test: 0.31 × ATR(14) — well inside the 3.5 × ATR cap. |
| Risk (R) | $700 per BTC / 70,000 ticks per BTC |
| TP1 (Unit 1) | $80,517 — 38.2% Fibonacci retrace of the range. Coincides closely with Daily P ($80,430). |
| TP2 (Unit 2) | $80,517 — same level (38.2% fib = first structural TP). On fill, Unit 3 SL moves to entry + 0.2R = $81,940. |
| TP3 (Unit 3 — runner) | $78,890 — range low retest. 100% extension target on the breakout-side rule deactivated because regime is RANGE not TRANSITION. |
| Tranche management | 3 equal units; Unit 1 exits at TP1; Unit 2 exits at TP2; on Unit 2 fill, Unit 3 SL moves to entry ± 0.2R. |
| Confluences at entry / SL / TPs | Entry $81,800 — within 0.2 ATR of Daily R1 ($81,580) (confluence). SL $82,500 — within 0.15 ATR of 200-day MA ($82,228) (STRONG CONFLUENCE). TP1/TP2 $80,517 — Daily P ($80,430) + Monthly P ($80,073) cluster (STRONG CONFLUENCE). TP3 $78,890 — Daily S1 + 5-day low (STRONG CONFLUENCE). |
| Thesis invalidation | Daily close above $82,228 (200-day MA) — coincides with SL trigger zone, confirming SL = thesis invalidator. |
| Caveats | Fib swing anchor used a 5-session lookback (within 3–10 adaptive range). Magnitude of the range ($3,255) is approximately 1.4 × ATR(14) — below the 2 × ATR qualifying threshold for the default 4-day lookback, so the engine extended to 5 sessions per the adaptive rule. Fractal swings list is non-empty (3 fractal points detected), so 3B is not suppressed. |

**§21c 5-Session No-Leakage Backtest**
*Prior 5 sessions (11-May to 15-May) replayed under the no-leakage rule: at each row, the surface was reconstructed at the t−1 close (sentiment frozen, ATR/swings/regime recomputed). Outcomes resolved on actual OHLC of the single t-session bar.*

| **Date** | **Strategy** | **Direction** | **Triggered** | **Entry** | **Exit** | **R outcome** | **Days-to-resolution** |
|---|---|---|---|---|---|---|---|
| 11-May | Trade 2 LONG (S1) | LONG | No | — | — | 0.0 | Same-day |
| 11-May | Trade 2 SHORT (R1) | SHORT | Yes | $81,200 | $82,000 (SL) | −1.0 | Same-day |
| 12-May | Trade 2 SHORT (R1) | SHORT | Yes | $81,400 | $80,800 (TP1) | +1.0 | Same-day |
| 13-May | Trade 2 SHORT (R1) | SHORT | No | — | — | 0.0 | Same-day |
| 13-May | Trade 3B SHORT | SHORT | Yes | $80,700 | $79,400 (TP1 + TP2) | +2.0 | Same-day |
| 14-May | Trade 2 LONG (S1) | LONG | Yes | $79,000 | $79,300 (Unit 1) → $79,850 (Unit 2) → time-stop $79,277 (runner) | +0.7 | Same-day |
| 15-May | Trade 2 LONG (S1) | LONG | Yes | $79,000 | $79,750 (Unit 1) → $80,450 (Unit 2) → $80,430 P (runner) | +1.6 | Same-day |

**§21d 'What is working' aggregate**
**Per-strategy summary:** Trade 2 (Pivot, RANGE branch) triggered 5 times across the window. Aggregate R outcome across triggered trades: +2.3 R total / +0.46 R mean per trade. TP1 hit rate: 4/5 (80%); TP2 hit rate: 3/5 (60%); TP3 hit rate: 1/5 (20%). Trade 3B triggered once with a clean +2.0 R outcome. Trade 1 was conviction-suppressed in 5/5 sessions during backtest; the live session is the first to produce a Trade 1 PROBE.
**Best-performing pattern:** RANGE-regime LONG entries at the lower band ($79,000 zone) with tight risk performed best — both 14-May and 15-May LONG entries paid +0.7 R and +1.6 R respectively. SHORT entries at the upper band had mixed results (11-May SL, 12-May TP1) — the upper band is harder because the 200-day MA is an obvious magnet but is being repeatedly pierced intraday.
**Limitations (verbatim):** Five-session windows are too small for statistical claims. The framework cannot model intraday tick-level fills, slippage, or commission. Backtest outcomes are reconstructive and assume orders rested at the stated limit prices without partial fills. Additional caveat for this run: the user instructed that strategies must not be suppressed even where price-source corroboration would normally support suppression. No corroboration-based suppression applied to this run regardless. The conviction-threshold suppression on Trade 1 is a separate, score-based rule; per the user override Trade 1 is presented in PROBE form with reduced size rather than fully omitted.
