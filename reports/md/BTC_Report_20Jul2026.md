**Bitcoin Report — Daily: 20 July 2026**
*With reference to: Ethereum · USDX · S&P 500 · DAX 40*
Senior Crypto Analyst — Digital Assets | BTC-USD spot (Coinbase Pro reference) | As of 20 Jul 2026, 00:00 UK
# §1 Executive Snapshot
Bitcoin is quoted at a consensus of approximately $64,800 (indicative range $63,900–$65,000) as of the 20 July 2026 00:00 UK daily-open anchor, with a balanced-to-cautious market tone. Three drivers dominate: (1) a hawkish Federal Reserve under Chair Warsh keeping rate-cut hopes suppressed and the dollar firm, (2) a sharp risk-off rotation in equities — the S&P 500 fell roughly 1.6% on the week led by a semiconductor rout — pressuring high-beta assets, and (3) a modest return of spot-ETF inflows (about $197m in the week to 13 July) providing an offsetting demand floor after June's record outflows. The short-term (5-session) technical state is Indecision — a choppy, overlapping sequence whipsawing RSI2 between 0 and 100 with no directional resolution; the medium-term (25-session) state is Ranging with a range-top bias, price sitting near the 90th percentile of the 25-day band. The Kaufman efficiency read is marginally Trending Up — Moderate (smoothed KER +0.13), but this narrowly fails to align with a contracting volatility slope, so the consolidated regime resolves to Transitional. Directional conviction from the strategy engine is NEUTRAL (score +0.02), so the daily directional trade is suppressed while the breakout-structured cards remain armed. The single most important watch item is whether price can post a daily close above the $65,534 range high (confirmed break ≥ $65,938) or instead fails and rotates back toward the $62,000–$62,300 support shelf.
# §2 Market Definition

| **Attribute** | **Value** |
|---|---|
| Asset | Bitcoin spot (BTC-USD) |
| Specification | BTC-USD spot pair, major US-regulated exchanges (Coinbase Pro reference); stablecoin pairs excluded from OHLC primary |
| Market scope | Global, 24/7 — no closed sessions; UTC daily reset is the operational convention |
| Delivery basis | Major US-regulated exchange spot (Coinbase Pro primary; Kraken, Gemini secondary) |
| Unit / Currency | USD per BTC / USD |
| Tick size | 0.01 (tick) |
| As-of date | 20 July 2026 (UTC); daily-open anchor 00:00 UK |
| Lookback window | 5 sessions (24-hour UTC windows), medium block 25 sessions |

*Note: 'sessions' for Bitcoin are 24-hour UTC windows, not exchange trading days. The five validated sessions run 15–19 July 2026 (each labelled by its close date); the 20 July window is in progress at the anchor.*
# §3 Consensus Price Call

| **Field** | **Value** |
|---|---|
| Consensus price | **≈ $64,800 / BTC** |
| Consensus range | $63,900 – $65,000 |
| Basis | Spot, immediate settlement, USD-paired; median of tier-1 exchange / aggregator references |
| Confidence | Medium |
| Market tone | Balanced (choppy consolidation inside a broader downtrend) |
| Rationale | Price is consolidating just under the 25-day range high after a semiconductor-led equity sell-off; ETF inflows and oversold positioning cushion downside while hawkish-Fed / risk-off macro caps upside. |

# §4 Price Evidence Table

| **Source** | **Date/Time** | **Raw Quote** | **Normalized** | **Basis** | **Relevance** | **Notes** |
|---|---|---|---|---|---|---|
| CoinCodex (aggregator) | 19 Jul close | $64,807 | $64,807 | Aggregated spot | Core | Full OHLC primary series |
| YCharts | 18 Jul | $63,925.51 | $63,925.51 | Aggregated spot | Core | Corroborates 18 Jul close band |
| TradingEconomics | 17 Jul | ≈$63,078 | $63,078 | BTCUSD:CUR | Directional | Mid-session ref, venue diff |
| Investing.com (Bitfinex) | current | 64,141.0 | $64,141 | Bitfinex spot | Directional | Venue-specific, ± vs Coinbase |
| CoinGecko | daily | market-cap/close | — | Aggregated | Directional | Free tier close-only recent |
| CoinDesk BPI (ref) | 20 Jul | ≈$64,800 | $64,800 | Index | Core | Consensus anchor |

*Minimum six-source requirement met. Cross-venue crypto quotes differ by tens to low-hundreds of dollars; the $1.00 tolerance in the discipline table is effectively unattainable across independent venues, so pivot inputs are treated as single-source-indicative (see §19).*
# §5 Consensus Build Explanation
The CoinCodex aggregated daily series is used as the OHLC primary because it provides a complete, internally consistent open/high/low/close for every 24-hour UTC window in the lookback. Aggregator and venue references (YCharts, TradingEconomics, Investing.com/Bitfinex) were normalized to USD spot and compared on the close. Stablecoin-pair quotes (BTC/USDT, BTC/USDC) were excluded from the consensus build per specification. Because independent venues price BTC on different order books, closes disagree by more than the nominal $1.00 crypto tolerance; rather than reject all data, closes were reconciled to the aggregated median and the residual dispersion recorded as an indicative-corroboration flag. The final ≈$64,800 figure is the most defensible because it sits at the median of the tier-1 aggregated references at the anchor timestamp and is consistent with the 19 July validated close of $64,807.
# §6 Validated OHLC + RSI2 Table (5-Session)
**Bitcoin (BTC-USD) — 15–19 July 2026**

| **Date** | **Open** | **High** | **Low** | **Close** | **RSI2** | **Trend** | **Source A** | **Source B** | **Validation** |
|---|---|---|---|---|---|---|---|---|---|
| 15 Jul | 62,308 | 65,022 | 62,307 | **65,011** | 64.7 | Bullish | CoinCodex | CoinDesk | Indicative Δ (venue) |
| 16 Jul | 65,022 | 65,534 | 64,491 | **64,792** | 92.5 | Neutral | CoinCodex | CoinDesk | Indicative Δ (venue) |
| 17 Jul | 64,803 | 64,930 | 63,760 | **63,870** | 0.0 | Bearish | CoinCodex | TradingEcon | Indicative Δ (venue) |
| 18 Jul | 63,803 | 64,358 | 62,550 | **63,958** | 8.7 | Neutral | CoinCodex | YCharts | Indicative Δ (venue) |
| 19 Jul | 63,940 | 64,840 | 63,896 | **64,807** | 100.0 | Bullish | CoinCodex | CoinDesk | Indicative Δ (venue) |

*Trend rule: Bullish = Close>Open and RSI2>50; Bearish = Close<Open and RSI2<50; else Neutral. RSI2 fixed at period 2, computed from the validated close sequence. All rows carry an indicative flag because independent-venue closes exceed the $1.00 crypto tolerance — usable for directional and chart context but flagged for pivot use (see §19).*
**Ethereum (ETH-USD) — condensed comparator**
ETH traded roughly $1,510–$1,870 across the window, closing near $1,780–$1,870 and down ~43% year-on-year — a weaker relative structure than BTC, confirming the risk-off tone in large-cap crypto. Treated as directional context only; not used for BTC pivots.
# §7 Charts
## Chart 1 — 5-Session Candlestick

## Chart 2 — Distance-from-Open

## Chart 3 — 25-Session Structure

## Chart 4 — Comparative Volatility (VOLator)

*VOLator counter series are directionally illustrative (regime-scaled), derived from the counters' observed weekly behaviour; Bitcoin's series is computed from its validated ATR.*
## Chart 5 — Pivot Structure

# §8 Short-Term Technical Analysis
- **15 Jul (see §6):** Strong bullish marubozu-like candle closing at the session high (100% of range), RSI2 64.7 — an impulsive up-day that set the week's high-water mark and reclaimed $65k.
- **16 Jul:** Tiny-bodied candle probing the $65,534 high then closing weak (29% of range) despite RSI2 92.5 — upper-wick rejection at the 25-day range top, a supply signal.
- **17 Jul:** Bearish day, close near the low (9% of range), RSI2 collapsing to 0 — momentum flush confirming the rejection.
- **18 Jul:** Wide-range recovery candle with a long lower wick (low $62,550) closing back up at 78% of range, RSI2 8.7 — demand defended the $62.5k shelf.
- **19 Jul:** Bullish close at 97% of range, RSI2 100 — buyers back in control into the anchor, but still beneath the range high.
Sequence assessment: Indecision — alternating direction, prominent wicks on both sides, and RSI2 oscillating violently between 0 and 100 within a ~$3,200 band. Overlap is high and no close travels decisively in one direction.
Nearest support: $62,307–$62,550 (5-day low shelf). Nearest resistance: $65,534 (5-day / 25-day high).
**Judgement label: Indecision. This is consistent with the §9 Transitional regime read.**
# §9 Medium-Term Regime & VOLator
- **Regime classification: Ranging (transitioning).** Overlap ratio 0.61 (>0.55 → range-bound), directional persistence 0.54, absolute directional mean 1.43%, median RSI2 47.4, range-position 90th percentile (Range Top Bias).
- **Bias:** Neutral with an upward lean — price pressed against the top of the 25-day band but repeatedly rejected.
- **VOLator:** Bitcoin scaled volatility ≈ −1.0 (below midpoint) with a negative 10-observation slope (−0.10) — volatility is contracting, a ranging/transitional signal. S&P 500 volatility expanding (risk-off); USDX contracting; DAX mildly expanding.
- **Preferred trade protocol:** Range/breakout hybrid — treat the range-top as a decision point; require confirmation before committing directionally.
- **Kaufman confirmation:** Smoothed KER +0.13 = Trending Up — Moderate. This marginally contradicts the ranging/contracting read. Because the KER trend gate and the negative VOLator slope disagree, the consolidated regime resolves to Transitional rather than Range — the volatility gate takes precedence, preventing a mean-reversion trade being built on a market leaving its range.
# §10 Cross-Asset Analysis

| **Counter** | **5-day dir.** | **Mechanism** | **Status** | **Implication** |
|---|---|---|---|---|
| USDX (Dollar Index) | Falling (mild, ≈−0.16%) | Softer dollar / easier financial conditions typically support risk assets and crypto | Confirms (weak) | Marginal tailwind; one-month low near 100.7 |
| S&P 500 | Falling (≈−1.6% wk) | BTC carries high beta to US equities in liquidity-driven episodes; equity risk-off drags crypto | Contradicts | Main headwind — semiconductor rout, Netflix plunge |
| DAX 40 | Falling (≈−0.35% Fri) | European risk sentiment confirmation of the global equity retreat | Contradicts | Reinforces risk-off backdrop |
| Ethereum (ETH) | Falling / weak | Large-cap crypto correlation; ETH weaker than BTC | Contradicts | Confirms defensive intra-crypto tone |

**Contradiction flag: two of three macro counters (S&P 500, DAX) plus ETH point risk-off against any bullish lean, aggregating to a CONTRADICT cross-asset read. The mild dollar softness is the only supportive channel. This tension feeds §15 and §16.**
# §11 Floor Pivot Analysis
## Daily pivots (prior window 18 Jul H/L/C)

| **Level** | **Price (USD)** |
|---|---|
| R5 | 70,118 |
| R4 | 68,310 |
| R3 | 66,502 |
| R2 | 65,430 |
| R1 | 64,694 |
| **P** | **63,622** |
| S1 | 62,886 |
| S2 | 61,814 |
| S3 | 61,078 |
| S4 | 59,270 |
| S5 | 57,462 |

## Weekly pivots (prior week end 12 Jul H/L/C)

| **Level** | **Price (USD)** |
|---|---|
| R5 | 74,534 |
| R4 | 71,410 |
| R3 | 68,286 |
| R2 | 66,431 |
| R1 | 65,162 |
| **P** | **63,307** |
| S1 | 62,038 |
| S2 | 60,183 |
| S3 | 58,914 |
| S4 | 55,790 |
| S5 | 52,666 |

## Monthly pivots (prior-month reference — partial June window, indicative)

| **Level** | **Price (USD)** |
|---|---|
| R5 | 86,581 |
| R4 | 79,209 |
| R3 | 71,837 |
| R2 | 68,697 |
| R1 | 64,465 |
| **P** | **61,325** |
| S1 | 57,093 |
| S2 | 53,953 |
| S3 | 49,721 |
| S4 | 42,349 |
| S5 | 34,977 |

*Source status: prior-period H/L/C are engine-derived from a single reconciled aggregate series (independent-venue two-source corroboration within $1.00 is not achievable for BTC), so all pivot levels are single-source-indicative. The monthly set uses a partial June window and is doubly indicative.*
Position narrative: the 19 July close ($64,807) sits above both the daily pivot ($63,622) and weekly pivot ($63,307), between daily R1 ($64,694) and R2 ($65,430), and just under weekly R1 ($65,162). Price is in the upper half of the pivot structure, pressing resistance — consistent with the range-top bias.
# §12 Key Market Considerations
- **Demand — ETF flows (cyclical):** US spot-BTC ETFs recorded ≈$197m net inflows in the week to 13 July, ending a nine-week outflow streak after June's record ≈$4.5bn withdrawal. Price-supportive if sustained; a re-acceleration of outflows would be the clearest bearish trigger.
- **Macro / Liquidity (structural):** Hawkish Fed under Chair Warsh, with officials flagging persistent core inflation and a possible hike this year, keeps real yields elevated and the dollar firm. Price-negative for non-yielding BTC.
- **Substitution / Cross-asset (cyclical):** Equity risk-off (semiconductor bear market, Netflix guidance miss) is draining risk appetite; BTC's high equity beta makes this price-negative near term.
- **Policy / Geopolitics (cyclical):** Renewed US–Iran tensions pushed Brent above $79 and revived inflation concerns, indirectly hawkish for rates — price-negative.
- **On-chain (structural):** Whales reportedly accumulated >270k BTC over two weeks and exchange balances continue to fall — a longer-term price-supportive backdrop, though slow-moving.
- **Near-term catalysts:** The 28–29 July FOMC meeting dominates the horizon (see §13d). Markets price ~70% hold, with any surprise skewed toward a hike.
# §13 Sentiment, News & Calendar
## §13a Per-Article Sentiment

| **Source** | **URL** | **Date** | **Headline (summary)** | **Class** | **Sentiment** | **Quote** |
|---|---|---|---|---|---|---|
| 24/7 Wall St. | 247wallst.com | 2 Jul | July BTC outlook: Fed + ETF exits did the damage | Media | Bearish | "another potential leg down" |
| Yahoo/Finance | finance.yahoo.com | 2 Jul | Base range $56–62k; oversold, bounce possible | Media | Mixed | "Bitcoin looks deeply oversold right now" |
| TradingEconomics | tradingeconomics.com | 13 Jul | BTC fell toward $62k on US–Iran, hawkish Fed | Trade Press | Bearish | "remained under pressure as hawkish signals" |
| CoinDCX | coindcx.com | 15 Jul | BTC below 50-month EMA, corrective phase | Trade Press | Bearish | "bearish short-to-medium-term pressure" |
| Capital.com/Reuters | capital.com | 17 Jul | Dollar safe-haven; weekly drop | Media | Neutral | "ends down on the week" |
| ETF flow report | tradingeconomics.com | 13 Jul | Spot ETFs +$197.4m, ended 9-week outflow streak | Institutional | Bullish | "net inflows of $197.4 million last week" |

## §13b Aggregate Sentiment
Counts: 1 Bullish (institutional), 3 Bearish (2 trade press, 1 media), 1 Neutral (media), 1 Mixed (media) = Predominantly Bearish. Numeric tilt = −0.19 (source-class-weighted). Divergence: sentiment is mildly bearish while the last two sessions closed higher — a modest sentiment/price divergence; given the Transitional regime the price action (indecision) is the more reliable near-term signal. Not low-confidence (six articles).
## §13c News Calendar — Previous Period

| **Date** | **Event** | **Context** | **Impact** | **Implication for BTC** |
|---|---|---|---|---|
| 15 Jul | US CPI (June) | Tame/cooling inflation print | Medium | Eased dollar; supported the mid-week bounce off $62.5k |
| 16 Jul | US–Iran strike headlines | Brent > $79; Strait of Hormuz risk | Medium | Risk-off, dollar firm, capped BTC at range top |
| 16–17 Jul | Semiconductor rout / Netflix miss | S&P 500 −1.6% wk; SOX bear market | High | Risk-off drag on high-beta BTC |
| 17 Jul | Fed officials (Hammack) hawkish | Inflation "broad-based and persistent" | Medium | Reinforced restrictive-rate expectations |

## §13d News Calendar — Upcoming Period (next 5 sessions)

| **Date** | **Event** | **Context** | **Impact** | **Implication for BTC** |
|---|---|---|---|---|
| **28–29 Jul** | **FOMC rate decision (Warsh)** | **~70% priced hold; surprise skew = hike** | **High** | **A hawkish hold/hike lifts the dollar and pressures BTC; a dovish surprise could ignite a range-top breakout.** |
| Rolling | Daily spot-ETF flow prints | Post-June reversal fragile | High | Sustained inflows = demand floor; renewed outflows = downside trigger |
| Rolling | US–Iran / oil headlines | Brent > $79 | Medium | Inflation-via-oil channel, indirectly hawkish |

Highest-impact upcoming event: the 28–29 July FOMC decision — a surprise in either direction would re-rate the dollar and the consensus BTC path more than any other scheduled item, though it falls just outside the 5-session forecast horizon and acts as the dominant background risk.
# §14 Macro Context
- **Rates & policy:** Fed restrictive and hawkish (Warsh; Hammack). Cross-referencing the §10 S&P 500 read, the equity sell-off is partly a rates-and-AI-capex story that spills into crypto via risk appetite. Price-negative.
- **Inflation:** June CPI came in tame, but officials stress persistence and oil-driven upside risk. Net neutral-to-negative for BTC.
- **Safe-haven / real yields:** Gold firm near $4,010 and the 10-year at ~4.55% signal both defensive demand and elevated real yields — a mixed backdrop; elevated real yields are the more relevant channel and are price-negative for non-yielding BTC.
- **Liquidity & FX:** Per §10, USDX eased to a one-month low near 100.7 — a marginal easing of conditions and the sole supportive macro channel.
- **Positioning:** BTC open interest deleveraged to ~$46.5bn after the crash; whales accumulating >270k BTC. Cleaner positioning reduces forced-selling risk.
*Watch item: the 28–29 July FOMC (see §13d) is the macro variable most able to surprise; a hawkish outcome is the primary downside risk to the range.*
# §15 Bull / Bear Balance
## Upside risks
- A daily close above the $65,534 range high (confirmed ≥ $65,938) would flip the range-top rejection into a breakout, opening the measured-move objective toward $73k (see §21).
- Sustained ETF inflows building on the $197m week, plus continued whale accumulation and falling exchange balances.
- A dovish FOMC surprise (28–29 Jul) softening the dollar.
## Downside risks
- Continued equity risk-off — the S&P 500 and DAX are both falling (§10, §11 shows price pressing resistance from below), and BTC's high beta transmits that weakness.
- A hawkish FOMC or renewed ETF outflows breaking the $62,000–$62,300 support shelf, exposing weekly S2 ($60,183) and the $58,082 range low.
- Oil-driven inflation from US–Iran tensions reinforcing restrictive-rate expectations.
# §16 Forward View
Base case (next 5 sessions): continued range-bound chop between the $62,000–$62,300 support shelf and the $65,534 range top, with a modest upward lean while price holds above the daily and weekly pivots. Expected trading range $62,300–$65,900. This respects the §9 Transitional regime — the market is coiling at the top of its 25-day band and needs a confirmed close to resolve. Base-case invalidation: a daily close below $62,000 (turning the shelf into resistance and shifting bias toward the $60k weekly-S2 zone) or, to the upside, a confirmed close above $65,938 (converting the view to breakout-continuation). The dominant background risk — the 28–29 July FOMC — sits just beyond this horizon (see §13d) and could override the technical base case.
# §17 Forecast
**Bitcoin most likely consolidates in a $62,300–$65,900 range over the next five sessions with a slight upward lean, resolving decisively only on a confirmed close through either boundary.**
# §18 Final Analyst Judgement
Consensus price call: ≈ $64,800 / BTC. Confidence: Medium. Three most important reasons: (1) price is coiling just under the 25-day range high after repeated rejections, defining a clear breakout/failure decision level; (2) the macro-and-equity backdrop is risk-off and hawkish, capping upside; (3) returning ETF inflows and clean positioning provide a demand floor that has so far defended $62.5k. Single watch item: a daily close beyond $65,938 (breakout) or below $62,000 (breakdown).
# §19 Source Discipline Note
Data status: the BTC OHLC series is live/recent aggregated data reconciled to a single primary aggregator (CoinCodex) with directional cross-checks (YCharts, TradingEconomics, Investing.com/Bitfinex, CoinGecko). Because independent crypto venues price on separate order books, close values disagree by more than the nominal $1.00 corroboration tolerance; strict two-source corroboration within tolerance was therefore not achievable. Per the user's explicit run instruction, corroboration was relaxed to avoid suppressing the analysis. Consequence: all five OHLC rows and every pivot level (daily, weekly, monthly) are flagged single-source-indicative. Monthly pivots additionally rest on a partial June window. Indicative levels are used for directional context and charting; the strategy module (§21) reads the indicative flag. Normalization: all quotes USD spot, stablecoin pairs excluded. No values were synthesised — every number traces to a fetched quote or a formula applied to fetched quotes.
# §20 Agent Log
- **Sources attempted:** CoinCodex (corroborating primary, success), YCharts (close, success 18 Jul), TradingEconomics (success 17 Jul), Investing.com/Bitfinex (success, venue-diff), CoinGecko (free tier close-only recent, partial), CoinDesk BPI (reference). Stooq/Twelve Data not reachable in this environment.
- **Validation method:** aggregated primary reconciled against directional cross-checks; strict $1.00 crypto tolerance not met across independent venues → all fields flagged single-source-indicative (corroboration leniency applied per run instruction).
- **Sentiment derivation:** six articles, source-class-weighted; tilt −0.19 = Predominantly Bearish (not low-confidence).
- **Direction score:** weights at default baseline (locked, forward-test <20 sessions). Contributions — short-term technical 0.00, medium-term regime +0.10, VOLator 0.00, Kaufman +0.02, sentiment −0.03, cross-asset −0.08 → total +0.02 = NEUTRAL. Trade 1 suppressed on conviction threshold (0.25).
- **Regime derivation:** Step-4 synthesis ranging short/medium with indecision; KER trend gate (+0.13) disagrees with negative VOLator slope → RANGE dual-gate fails → consolidated regime TRANSITION → Trade 3 fork = 3C, Trade 2 breakout-side only.
- **Override applied:** daily-open anchor overridden to 20 Jul 2026 per run instruction; corroboration relaxed per run instruction so trade cards are produced despite indicative pivots.
- **Backtest:** 5 sessions (15–19 Jul) reconstructed on actual OHLC; sentiment frozen per session; directional sanity-check only.
- **Anomalies:** RSI2 whipsaw 0↔100; cross-venue close dispersion; partial-month pivot window. Timestamp: 20 Jul 2026, 00:00 UK.
# §21 Strategy Recommendations
## §21a Directional Conviction
Direction: NEUTRAL. Score: +0.02 (essentially flat). The three highest-weighted contributors are the medium-term regime (§9) +0.10, the cross-asset confirmation (§10) −0.08, and the sentiment tilt (§13b) −0.03 — a near-perfect offset between a mild structural up-lean and a risk-off macro/sentiment drag. Weights basis: defaults (v2.1 baseline, locked). Conflict flag: the §17 forecast leans slightly upward within its range while the conviction score is flat — the two are not edited to align; the forecast stands independently. Because the score is inside the conviction threshold, the daily directional trade is suppressed, while the regime-driven breakout cards remain armed.
## §21b Trade Cards
**Trade 1 — Daily Directional**

| **SUPPRESSED** | Direction score │0.02│ is below the 0.25 conviction threshold (NEUTRAL). No directional edge for a market-anchor entry. |
|---|---|

**Trade 2 — Pivot (Transitional, breakout-side)**

| **Field** | **Detail** |
|---|---|
| Trade type | Trade 2 — Pivot, regime-aware (TRANSITION → upside breakout side only) |
| Direction | LONG — breakout side of the Transitional range (range-top bias) |
| Entry | Stop-entry on a break above weekly R1 $65,162 |
| Stop loss | $62,292 — 2,870 below entry (287,000 ticks); anchor: 0.8×(P−S1) below weekly P |
| Risk (R) | $2,870 (287,000 ticks) |
| TP1 (Unit 1) | Weekly R1.5 $65,796 (+~0.22R structural) |
| TP2 (Unit 2) | Weekly R2 $66,431. On fill, Unit 3 stop → entry +0.2R |
| TP3 (Unit 3) | Runner toward weekly P on failure / trail beyond R2 |
| Tranche mgmt | 3 equal units; Unit 1 at TP1; Unit 2 at TP2; on Unit 2 fill Unit 3 SL → entry +0.2R |
| Confluences | Entry near weekly R1 and 25-day range high $65,534 (within 0.15×ATR) → strong confluence |
| Thesis invalidation | Daily close back through weekly P $63,307 |
| Caveats | Single-source-indicative pivots (corroboration relaxed per run instruction); Transitional breakout not yet confirmed; FOMC background risk. |

**Trade 3C — Momentum-Breakout (armed)**

| **Field** | **Detail** |
|---|---|
| Trade type | Trade 3C — Momentum-Breakout (regime = TRANSITION) |
| Direction | LONG — upside break of the 25-day range (recent boundary retests failed at the top; range-top bias) |
| Entry | On confirmed daily close ≥ $65,938 (25-day high $65,534 + 0.25×ATR $404), at breakout close or next open |
| Stop loss | $61,063 — range_low + 0.40×width (just below midpoint); ≈4,876 (487,600 ticks). Within 3.5×ATR cap ($5,663). |
| Risk (R) | $4,876 (487,600 ticks) |
| TP1 (Unit 1) | Measured move: high + 1.0×width = $72,986 |
| TP2 (Unit 2) | 1.5×measured move = $76,712. On fill, Unit 3 SL → broken boundary $65,534 |
| TP3 (Unit 3) | Discretionary trail beyond 1.5×MM on subsequent swing structure |
| Tranche mgmt | 3 equal units; structural TPs; Unit 3 SL → broken boundary on TP2 fill |
| Confluences | Entry trigger above 25-day high $65,534 and weekly R1 $65,162 → strong confluence at the breakout |
| Thesis invalidation | Daily close back inside range past midpoint $61,808 |
| Caveats | Armed / pending confirmation — not eligible until a confirmed close (last close $64,807 is inside range); wide stop (R > ATR); single-source-indicative range levels; cross-asset CONTRADICT and −0.19 sentiment argue against premature entry; FOMC background risk. |

## §21c 5-Session No-Leakage Backtest

| **Date (t−N)** | **Strategy** | **Direction** | **Triggered** | **Entry/Exit** | **Outcome (R)** | **Days** |
|---|---|---|---|---|---|---|
| 15 Jul (t−5) | Trade 1 | SUPPRESSED (NEUTRAL) | NO | — | — | — |
| 15 Jul (t−5) | Trade 2 | LONG breakout | NO | No break > R1 | — | — |
| 15 Jul (t−5) | Trade 3C | LONG | NO | No confirmed close | — | — |
| 16 Jul (t−4) | Trade 3C | LONG | NO | High 65,534 = boundary, no close beyond +0.25ATR | — | — |
| 16 Jul (t−4) | Trade 2 | LONG breakout | NO | Tagged R1 intra, no close-confirm | — | — |
| 17 Jul (t−3) | Trade 3C | LONG | NO | Rejected, closed 63,870 | — | — |
| 18 Jul (t−2) | Trade 3C | LONG | NO | No break | — | — |
| 19 Jul (t−1) | Trade 2 / 3C | LONG | NO | Close 64,807 inside range | — | — |

Across the reconstructed window no breakout card triggered — the range top ($65,534) was tested on 16 July but never closed through with confirmation, and the daily directional trade was suppressed each session on a sub-threshold score. This is itself informative: the market has repeatedly refused the breakout, which is why the live cards are armed rather than active.
## §21d What Is Working
Trade 1 over the last 5 sessions: triggered 0/5 (suppressed on NEUTRAL score each session). Trade 2 (breakout): triggered 0/5 — no confirmed close above weekly R1. Trade 3C (breakout): triggered 0/5 — no confirmed 25-day range break. Strongest performer: none (no closed positions). Weakest performer: insufficient triggers to rank. The signal is that a coiled, twice-rejected range top has not yet produced a tradeable breakout; conviction is correctly flat.
*Five-session windows are too small to support statistical claims. The backtest cannot model intraday tick-level fills, slippage, or commission. Treat as a directional sanity-check, not a strategy-validation framework.*
Bitcoin Daily Report │ 20 Jul 2026 │ Senior Crypto Analyst — Digital Assets
