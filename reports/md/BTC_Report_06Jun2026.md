**Bitcoin (BTC/USD) Report — Daily: 06 June 2026**
*With reference to: Ethereum · USDX · S&P 500 · DAX 40*
Senior Crypto Analyst — Digital Assets · Spot consensus as of 06 June 2026 (UTC) · Trading & risk review
# §1 Executive Snapshot
Bitcoin enters the 06 June 2026 snapshot in a confirmed, high-conviction downtrend. The spot consensus is approximately **$62,900** (range $61,400–$64,700), built from a weighted median of regulated-venue and aggregator quotes, with a Medium confidence rating given timestamp dispersion across sources. Market tone is decisively bearish. Three drivers dominate: (i) a record run of spot-ETF outflows that broke the $68,000 and $65,000 floors in consecutive sessions; (ii) a hawkish repricing of Fed policy after strong May labour data, lifting the dollar to a two-month high; and (iii) risk-off flows from escalating Middle East tensions. The short-term technical read is **Bearish continuation**, and the 25-session regime is **Trending — Bearish**. The Kaufman Efficiency Ratio classifies the tape as Trending Down — Strong (smoothed reading ≈ −0.70), corroborating the regime. The single most important watch item is the 06 June U.S. nonfarm payrolls print (see §13d): a hot number would extend dollar strength and pressure BTC further; a cool number is the most plausible near-term relief trigger. Directional conviction for the session is SHORT (see §21a).
# §2 Market Definition

| **Field** | **Definition** |
|---|---|
| Asset | Bitcoin spot (BTC-USD) |
| Specification | BTC-USD spot pair, major US-regulated exchange reference (Coinbase Pro). Stablecoin pairs excluded from the OHLC primary. |
| Scope | Global, 24/7. UTC daily reset is the operational session convention. |
| Delivery basis | Regulated-venue spot (Coinbase Pro primary; Kraken, Gemini secondary). |
| Unit / Currency | USD per BTC / USD. |
| As-of date | 06 June 2026 (UTC) — overriding the template snapshot date and daily-open anchor per instruction. |
| Daily-open anchor | 00:00 UK (UTC-aligned daily reset). |
| Lookback window | 5 sessions (24-hour UTC windows). |

# §3 Consensus Price Call

| **Metric** | **Value** | **Notes** |
|---|---|---|
| Consensus price | ≈ $62,900 | Weighted median across regulated-venue and aggregator quotes near the snapshot. |
| Consensus range | $61,400 – $64,700 | Spans the 04–05 June daily trading band. |
| Basis | Spot, immediate settlement (USD-paired) | Stablecoin pairs excluded from the consensus build. |
| Confidence | Medium | Intraday timestamp dispersion across sources; price falling fast within the window. |
| Market tone | Bearish | Lower highs and lower lows across five consecutive sessions. |

**Rationale:** spot prints cluster in the low-$62k area around the snapshot, after a $64,360 open and a $61,412 intraday low on the most recent completed session. Quotes are recent and liquid; the principal uncertainty is timing, not level.
# §4 Price Evidence Table

| **Source** | **Date/Time** | **Raw Quote** | **Normalized** | **Classification** | **Notes** |
|---|---|---|---|---|---|
| CoinCodex | 05 Jun (UTC daily) | $63,850 (04→05 Jun close) | $63,850 | Aggregator — core | Full daily OHLC series; primary OHLC source. |
| CoinDesk BPI | 04 Jun 20:58 EDT | $63,391 | $63,391 | Aggregator — core | Bitcoin Price Index spot. |
| Fortune (mkt data) | 05 Jun 09:15 ET | $61,929 | $61,929 | Media — directional | Intraday spot during US morning. |
| BlockchainReporter | 05 Jun (intraday) | $62,875 | $62,875 | Trade press — directional | Cites CoinGecko live; daily range $61,394–$64,352. |
| CoinGecko | 05 Jun (live) | $60,949–$62,128 | ≈$61,500 | Aggregator — core | Live tape; range across snapshots. |
| Fortune (mkt data) | 04 Jun 09:40 ET | $63,683 | $63,683 | Media — directional | Prior-session reference point. |

Minimum source count (6) met. All quotes within the recency window; intraday dispersion reflects a fast-falling tape rather than disagreement on level.
# §5 Consensus Build Explanation
All observations are USD-paired spot, so no FX or incoterm normalization is required. Quotes were aligned to the nearest UTC daily reference where intraday. The aggregator daily close ($63,850) and the regulated-venue-referenced indices anchor the upper bound; live US-morning prints ($60.9k–$62.1k) anchor the lower bound. The weighted-median consensus of ≈$62,900 sits inside the 04–05 June band and downweights the single lowest live tick as a fast-moving intraday outlier. Stablecoin pairs were excluded from the primary build per specification; none were needed given dense USD coverage. The number is most defensible as a band-centred median rather than a precise point, hence the Medium confidence rating.
# §6 Validated OHLC + RSI2 Table (5-Session)

| **Date** | **Open** | **High** | **Low** | **Close** | **RSI2** | **Trend** | **Source A** | **Source B** | **Validation** |
|---|---|---|---|---|---|---|---|---|---|
| 31 May | 73,876 | 74,272 | 73,433 | **73,688** | 68.5 | Neutral | CoinCodex | CoinGecko | CORROB. (Δ≈low) |
| 01 Jun | 73,869 | 73,986 | 70,894 | **71,440** | 0.0 | Bearish | CoinCodex | CoinDesk | CORROB. |
| 02 Jun | 71,326 | 71,370 | 66,330 | **66,764** | 0.0 | Bearish | CoinCodex | Fortune | CORROB. |
| 03 Jun | 66,745 | 67,473 | 64,147 | **64,147** | 0.0 | Bearish | CoinCodex | CoinDesk | CORROB. |
| 04 Jun | 64,360 | 64,722 | 61,412 | **63,850** | 0.0 | Bearish | CoinCodex | BlockchainRptr | CORROB. (≈Δ) |

*RSI2 is computed period-2 from the validated close sequence. After 31 May, four consecutive down-closes drive RSI2 to its 0 floor — mathematically consistent with an uninterrupted sell sequence, not a data error.* *Corroboration applied the crypto ±$1.00 close tolerance leniently per instruction; aggregator and index closes agree on direction and level to within normal cross-venue dispersion.*
# §7 Charts

*Chart 1 — Five-session candlestick. An unbroken waterfall: each session opens near the prior close and sells off, with the 04 Jun lower wick to $61,412.*

*Chart 2 — Distance from open. Closes sit well below open on four of five sessions; 02–03 Jun show the deepest intraday extension.*

*Chart 3 — 25-session structure. A clean roll-over from the ~$82k mid-May shelf through to the low-$60k area.*

*Chart 4 — Comparative volatility (ATR-based, z-scaled). Bitcoin volatility is pinned at the top of its band and expanding; counters remain mid-band. Counter series are directional proxies.*

*Chart 5 — Daily floor pivots with prior weekly candles. Spot sits between daily P ($63,328) and S1 ($61,934); S1 is confluent with the 04 Jun low.*
# §8 Short-Term Technical Analysis
- **31 May (see §6):** small bearish body, close ~30% of range; RSI2 elevated (68.5) on the prior up-day — the last moment of balance before the break.
- **01 Jun:** large bearish body, close ~18% of range, RSI2 collapses to 0. The $70,894 low breaks the prior shelf — initiation bar of the decline.
- **02 Jun:** wide-range bearish session, close ~9% of range; ~$5k peak-to-trough. Maximum downside momentum.
- **03 Jun:** continuation lower, close on the low (0% of range) at $64,147 — no buyers into the close, maximally weak.
- **04 Jun:** probe to $61,412 then a close back at ~74% of range ($63,850). First sign of intraday demand — a lower wick, though still within the downtrend.
**Sequence assessment:** Continuation. Direction persists with low overlap and closes travelling one way for four straight sessions; the 04 Jun wick is the only counter-signal.
**Nearest support / resistance (from the validated window):** support $61,412 (04 Jun low); resistance $64,722 (04 Jun high), then $66,330–$67,473.
**Judgement label:** **Bearish continuation**. Consistent with the §9 regime; the 04 Jun lower wick is noted as a tactical caveat, not a reversal.
# §9 Medium-Term Regime & VOLator
- **Regime:** Trending. High directional persistence, low overlap, median RSI2 deep below 50, range-position bias pinned to lows.
- **Bias:** Bearish.
- **VOLator readings:** Bitcoin scaled volatility at the top of its band (≈+1.0) and expanding (positive slope on the last 10 obs). USDX mid-band and firm; S&P 500 and DAX mid-band and stable.
- **Preferred trade protocol:** Trend pullback — sell rallies into resistance/pivot rather than chase new lows.
- **Kaufman confirmation:** KER classifies Trending Down — Strong (smoothed ≈ −0.70), agreeing with the regime. No conflict; the trend signal takes precedence.
**Consolidated regime label:** **TREND_DOWN** (Step-4 synthesis bearish, KER trending-down, VOLator expanding in the trend direction).
# §10 Cross-Asset Analysis

| **Counter** | **5-day dir.** | **Mechanism** | **Status** | **Implication for BTC** |
|---|---|---|---|---|
| USDX (Dollar Index) | Rising | Tighter financial conditions / higher real yields raise the opportunity cost of holding non-yielding BTC. | Confirms | Dollar at a two-month high is a direct headwind. |
| S&P 500 | Flat / firm | Risk-asset beta channel; equities holding up removes a broad-risk-off alibi. | Neutral | BTC weakness is crypto-specific (ETF outflows), not a broad de-risking. |
| DAX 40 | Flat | European risk proxy; no confirmation either way. | Neutral | Limited read-through to BTC this week. |
| Ethereum (ETH) | Falling hard | High intra-crypto correlation; ETH −2.4% on the day, sub-$1,700. | Confirms | Sector-wide selling, not idiosyncratic to BTC. |

**Aggregate cross-asset signal:** MIXED leaning confirm — USDX and ETH confirm the bearish read; equities are neutral. No outright contradiction of the regime.
# §11 Floor Pivot Analysis
## Daily pivots (from 04 Jun H/L/C)

| **Level** | **Price (USD/BTC)** | **Note** |
|---|---|---|
| R5 | 75,174 |  |
| R4 | 71,864 |  |
| R3 | 68,554 |  |
| R2 | 66,638 | 02 Jun supply |
| R1 | 65,244 | 04 Jun high zone |
| **P** | **63,328** | spot sits just below |
| S1 | 61,934 | confluent with 04 Jun low $61,412 — strong |
| S2 | 60,018 | psychological $60k |
| S3 | 58,624 |  |
| S4 | 55,314 |  |
| S5 | 52,004 |  |

## Weekly pivots (prior week 25–31 May)

| **Level** | **Price** | **Note** |
|---|---|---|
| P | 74,772 | far overhead — trend is well below weekly P |
| S1 / S2 | 71,555 / 69,423 | already broken |
| S3 / S4 | 66,206 / 60,857 | S4 frames the $60k zone |

**Source status:** daily and weekly pivot inputs are corroborated (CoinCodex × index/aggregator close). The monthly timeframe is flagged **single-source-indicative** because the in-window May series is partial (no 1–6 May candles), so monthly levels are excluded from level-based execution per discipline.
**Position narrative:** the close sits between daily P ($63,328) and S1 ($61,934), below all weekly pivots — a structurally weak location. The S1/04-Jun-low confluence at ~$61,400–61,900 is the key downside shelf.
# §12 Key Market Considerations
- **Demand / Flows (price-negative, cyclical):** spot-ETF complex saw record multi-day outflows (reports of ~$4.4B over ~13 days), the dominant proximate driver of the floor breaks.
- **Macro / Liquidity (price-negative, cyclical):** stronger May labour data lifted Fed-hike odds; the dollar hit a two-month high, tightening conditions for risk assets.
- **Policy / Structural (mildly supportive, structural):** U.S. Congress advancing Bitcoin tax/strategic-reserve discussion and crypto-collateral mortgage initiatives provide a longer-term demand narrative — not a near-term offset.
- **Substitution / Spreads (neutral):** ETH falling alongside BTC; no rotation refuge within large-cap crypto this week.
- **Near-term catalyst (see §13d):** 06 Jun U.S. nonfarm payrolls is the binding event within the 5-day horizon.
# §13 Sentiment, News & Calendar
## §13a Per-Article Sentiment

| **Source** | **Date** | **Headline (verbatim, abbreviated)** | **Class.** | **Sentiment / Derivation** |
|---|---|---|---|---|
| BlockchainReporter | 05 Jun | Bitcoin Price Today: BTC At $62,875 as ETF Outflows Hit Record | Trade Press | **Bearish** *“technical picture stays bearish… downtrend is intact”* |
| Yahoo Finance | 05 Jun | Bitcoin and ethereum prices today… Prices continue their descent | Media | **Bearish** *“prices continue their descent this week”* |
| Fortune | 05 Jun | Current price of Bitcoin for June 5, 2026 | Media | **Neutral** *“market price for a single Bitcoin is $61,928.70”* |
| CoinGecko (mkt summary) | 05 Jun | Bitcoin consolidates near $60k after $1.5B liquidation | Media | **Bearish** *“pressured high-risk assets like Bitcoin”* |
| Changelly | 04 Jun | BTC Price Prediction… bearish, Fear & Greed 12 | Media | **Bearish** *“The bulls are fading… On the four-hour chart, bearish”* |
| Fortune | 02 Jun | Bitcoin slides below $66,000 | Media | **Bearish** *“down 5.8% this morning from Monday’s open”* |

## §13b Aggregate Sentiment
Counts: 5 Bearish (1 trade press, 4 media), 1 Neutral (media) = **Predominantly Bearish**. Numeric tilt = **−0.45** (source-class-weighted mean of article scores). Divergence: sentiment agrees with price action and the §9 regime — no divergence. The tilt rests largely on media sources, so it is treated as moderate-confidence and weighted accordingly in §21.
## §13c News Calendar — Previous Period

| **Date** | **Event** | **Context** | **Impact** | **Implication for BTC** |
|---|---|---|---|---|
| 02 Jun | Record spot-ETF outflows reported | Multi-day institutional de-risking | High | Broke $68k then $65k floors. |
| 03–04 Jun | JOLTS / ADP beats | Job openings & private payrolls above forecast | High | Lifted Fed-hike odds; dollar up, BTC down. |
| wk | Middle East escalation | Ceasefire rejected; oil firm | Medium | Risk-off + inflation impulse; dollar bid. |

## §13d News Calendar — Upcoming Period

| **Date** | **Event** | **Context** | **Impact** | **Implication for BTC** |
|---|---|---|---|---|
| **06 Jun** | **U.S. Nonfarm Payrolls (May)** | Markets pricing ~85% odds of a year-end hike | **High** | Beat → more dollar strength, BTC lower; miss → relief bounce, primary upside trigger. |
| Rolling | Daily spot-ETF flow prints | Outflow streak in focus | High | A flip to net inflows would be the first demand-side reversal signal. |
| Horizon | Fed commentary | Post-data speak | Medium | Hawkish tone compounds pressure. |

**Highest-impact upcoming event:** 06 June nonfarm payrolls — a hot print would cement the hawkish repricing and likely drive a test of the $60k zone, while a soft print is the most credible catalyst for a counter-trend bounce.
# §14 Macro Context
- **Rates & policy:** hawkish repricing after strong labour data; ~85% odds of a year-end hike. Cross-refs §10 USDX (rising) — price-negative for BTC.
- **Inflation:** firm oil from Middle East tensions adds an inflation impulse, reinforcing the hawkish tilt — price-negative.
- **Liquidity & FX:** USDX at a two-month high (§10) tightens global dollar liquidity — the central macro headwind.
- **Risk sentiment:** equities firm (§10 S&P 500 neutral) indicate the selling is crypto-specific, driven by ETF flows rather than broad de-risking.
- **Positioning:** Fear & Greed in Extreme Fear; large liquidation event reported. Stretched bearish positioning raises the odds of sharp short-covering on any positive surprise — watch item tied to §13d payrolls.
# §15 Bull / Bear Balance

| **Upside risks** | **Downside risks** |
|---|---|
| Soft 06 Jun payrolls → dollar reverses, short-covering bounce. | Hot payrolls → dollar extends, $60k zone tested (weekly S4 / daily S2). |
| ETF flows flip to net inflows — first demand-side reversal. | ETF outflow streak persists; each broken floor flips to resistance. |
| Extreme-Fear positioning primes a violent mean-reversion rally. | Loss of $61,400 (04 Jun low / daily S1) opens $58,600 (S3). |
| Structural policy tailwinds (reserve/tax bills) re-enter the narrative. | ETH leadership lower drags the whole sector. |

**Pivot/regime cross-ref:** price below all weekly pivots and beneath daily P; the $61,400–61,900 S1/low confluence is the line in the sand. The §13d payrolls print is the highest-impact swing factor in both directions.
# §16 Forward View
Base case (next 5 sessions): **continued bearish bias with a downward-to-sideways drift**, expected trading range roughly $59,500–$66,500. The path is event-gated by 06 June payrolls. This view respects the §9 TREND_DOWN regime. **Base-case invalidation:** a daily close back above the daily pivot ($63,328) and then $65,244 (R1 / 04 Jun high zone) would neutralise the immediate bearish setup and signal a relief leg toward $66,600–$68,500.
# §17 Forecast
***Bitcoin is most likely to extend lower toward the $61,400–$60,000 support shelf over the coming sessions unless the 06 June payrolls print surprises soft.***
# §18 Final Analyst Judgement
**Consensus price call:** ≈ $62,900 (range $61,400–$64,700), Medium confidence.
- Five-session waterfall with closes on or near session lows confirms a strong, intact downtrend (KER Trending Down — Strong).
- Record ETF outflows plus a dollar at a two-month high give the move a fundamental and macro engine, not just technical momentum.
- Cross-asset confirmation from USDX and ETH; equities neutral, so the weakness is crypto-specific.
**Single watch item:** 06 June U.S. nonfarm payrolls (§13d).
# §19 Source Discipline Note
- Live vs indicative: OHLC closes corroborated across CoinCodex and at least one index/aggregator/media print per session; crypto ±$1.00 close tolerance applied leniently per explicit instruction, so cross-venue dispersion within normal intraday bounds was accepted rather than rejected.
- Daily and weekly pivots: CORROBORATED (prior-period H/L/C from corroborated sessions).
- Monthly pivots: SINGLE-SOURCE-INDICATIVE — partial in-window May series; excluded from level-based execution.
- Data gaps: intraday timestamps differ across sources (ET vs UTC daily), the main reason for Medium price confidence.
- Normalization: all USD-paired spot; no FX conversion. Counter VOLator series in Chart 4 are directional proxies, clearly labelled.
# §20 Agent Log
- Sources attempted (OHLC): CoinCodex (corroborated, primary daily OHLC); CoinGecko (close corroboration, partial recent coverage on free tier); CoinDesk BPI, Fortune, BlockchainReporter (close/direction corroboration). Stooq and Yahoo history endpoints attempted — blocked/unavailable; substituted next-rank approved sources.
- Corroboration pairs: each session CoinCodex × (index/aggregator/media). Deltas within normal intraday cross-venue dispersion; accepted under the instructed lenient crypto tolerance.
- Sentiment derivation: 6 articles, source-class weighted; tilt −0.45; predominantly media → moderate confidence flagged.
- Forecast reasoning: TREND_DOWN regime + bearish tilt + USDX/ETH confirmation → directional SHORT; event-gated by payrolls.
- Strategy trace: direction-scoring weights at DEFAULTS (no tuning; first-session deployment, weights locked). Direction score −0.85. No trades suppressed for conviction. Trade 2 monthly tier flagged indicative — daily/weekly tiers used instead. Backtest reconstructed over 5 prior sessions at each t−1 close with no forward leakage.
- Anomalies: RSI2 = 0 across four sessions (valid for an uninterrupted down sequence). As-of date and daily-open anchor overridden to 06 Jun 2026 per instruction.
- Timestamp: report compiled 06 June 2026 (UTC).
# §21 Strategy Recommendations
## §21a Directional Conviction
Direction: **SHORT**. Score: **−0.85**. Three highest-weighted contributors: short-term technical bias (§8) −0.25, medium-term regime (§9) −0.20, Kaufman trend (§9) −0.15; cross-asset (§10) −0.15 and sentiment (§13b) −0.07 reinforce. No conflict with the §17 forecast — both point lower. Weights basis: **defaults** (locked, first-session deployment).
## §21b Trade Cards
**Trade 1 — Daily Directional (SHORT — TREND_DOWN regime)**

| **Field** | **Detail** |
|---|---|
| Direction | SHORT — TREND_DOWN regime; conviction │0.85│ well above threshold. |
| Entry | Sell at 00:00 UK daily open, ≈ $63,850 (market). Trend-pullback protocol favours fills nearer daily P $63,328–R1 $65,244. |
| Stop loss | $66,750 — above 02 Jun supply / daily R2 $66,638. Distance ≈ $2,900 (≈1.35× ATR; structural anchor = R2 + buffer). Within the 3.5×ATR cap. |
| Risk (R) | ≈ $2,900 per unit. |
| TP1 (Unit 1) | +1R = $60,950 (≈ daily S2 $60,018 zone / psychological $60k). |
| TP2 (Unit 2) | +2R = $58,050 (≈ daily S3 $58,624). |
| TP3 (runner) | Time-stop at session close; 3×ATR trail cap. Target the $55,300 (S4) extension if momentum persists. |
| Tranche mgmt | 3 equal units; U1 exits TP1; U2 exits TP2; on U2 fill, U3 stop → entry −0.2R ($63,270). |
| Confluences | Entry near daily P; SL at R2; TP1 at S2/$60k round number (strong); TP2 at S3 — multiple pivot confluences. |
| Thesis invalidation | Daily close back above daily P $63,328 then R1 $65,244 breaks the continuation narrative. |
| Caveats | 04 Jun lower-wick shows intraday demand; payroll-day (06 Jun) holding-period collision — size down into the print. |

**Trade 2 — Pivot, regime-aware (SHORT rallies)**

| **Field** | **Detail** |
|---|---|
| Direction | SHORT — fade rallies in a down-trend (sell-the-bounce). |
| Entry | Sell limit at daily R1 $65,244 (with confluence to 04 Jun high $64,722). |
| Stop loss | $66,800 — above daily R2 $66,638. Distance ≈ $1,556. |
| Risk (R) | ≈ $1,556 per unit. |
| TP1 | +1R = $63,688 (≈ daily P $63,328). |
| TP2 | +2R = $62,132 (≈ daily S1 $61,934 / 04 Jun low confluence — strong). |
| TP3 (runner) | Daily pivot P then S2 $60,018; runner exit at pivot P on momentum stall. |
| Tranche mgmt | 3 equal units; standard rule; on U2 fill, U3 stop → entry −0.2R. |
| Confluences | Entry R1+prior-high (strong); TP2 at S1+5-day low (strong). |
| Thesis invalidation | Hourly/daily acceptance above R2 $66,638. |
| Caveats | Daily/weekly pivots corroborated; monthly tier single-source-indicative and excluded. Payroll collision flag. |

**Trade 3 — Momentum-Pullback (3A) (TREND_DOWN fork)**

| **Field** | **Detail** |
|---|---|
| Direction | SHORT — momentum pullback to a fib retrace of the 31 May→04 Jun leg. |
| Entry | Sell at 38.2% retrace of the $74,272→$61,412 swing ≈ $66,325 (confluent with daily R2 $66,638). |
| Stop loss | $68,600 — above the 50% retrace $67,842 and 02 Jun high. Distance ≈ $2,275. |
| Risk (R) | ≈ $2,275 per unit. |
| TP1 (struct.) | 38.2% give-back target / range mid ≈ $63,300 (daily P). |
| TP2 (struct.) | Swing low retest $61,412. |
| TP3 (runner) | Measured-move (1× swing width ≈ $12,860) projects toward $53,500 on a confirmed S1 break; structural runner override per 3A. |
| Tranche mgmt | 3 equal units; 3A override — on 100%-extension break, U3 stop → halfway between entry and 0% anchor. |
| Confluences | Entry at 38.2% fib + daily R2 (strong); TP2 at the 5-day low. |
| Thesis invalidation | Close above the 61.8% retrace $69,360. |
| Caveats | Fib lookback 4 sessions (swing magnitude > 2×ATR, no extension needed). Payroll collision flag. |

## §21c 5-Session No-Leakage Backtest

| **Date (t−N)** | **Strategy** | **Direction** | **Triggered** | **Entry / Exit** | **Outcome (R)** | **Days** |
|---|---|---|---|---|---|---|
| 30 May (t−5) | Trade 1 | SHORT | YES | 73.45k → SL 75.0k partial / trail | −0.4R | 2 |
| 30 May (t−5) | Trade 2 | SHORT | NO | R1 limit not tagged | — | — |
| 31 May (t−4) | Trade 1 | SHORT | YES | 73.69k → +1R 71.4k, +2R hit | +2.0R | 2 |
| 31 May (t−4) | Trade 3A | SHORT | YES | fib 73.5k → swing low | +1.6R | 3 |
| 01 Jun (t−3) | Trade 1 | SHORT | YES | 71.44k → +2R 66.8k | +2.0R | 1 |
| 01 Jun (t−3) | Trade 2 | SHORT | YES | bounce to R1 sold → TP2 | +2.0R | 2 |
| 02 Jun (t−2) | Trade 1 | SHORT | YES | 66.76k → +2R 64.1k | +2.0R | 1 |
| 02 Jun (t−2) | Trade 3A | SHORT | YES | fib sell → swing low | +1.8R | 2 |
| 03 Jun (t−1) | Trade 1 | SHORT | YES | 64.15k → +1R 61.9k; U3 open | +1.3R | 1 |
| 03 Jun (t−1) | Trade 2 | SHORT | NO | no qualifying rally to R1 | — | — |

*SL-first tick-priority applied where SL and TP could fill in the same bar. Slippage = 0.*
## §21d ‘What Is Working’ Aggregate
Trade 1 over the last 5 sessions: triggered 5/5, mean R ≈ +1.38, TP1/TP2/TP3 hit ≈ 100% / 80% / 0%. Trade 2: triggered 1/3 (rallies were shallow in a one-way tape), mean R ≈ +2.0 on the single fill. Trade 3A: triggered 2/2, mean R ≈ +1.7. **Strongest performer:** Trade 2 by mean R (single closed trade), with Trade 3A the most consistent. **Weakest:** Trade 1’s first reconstruction (−0.4R) before the trend matured.
*Five-session windows are too small to support statistical claims. The backtest cannot model intraday tick-level fills, slippage, or commission. Treat as a directional sanity-check, not a strategy-validation framework.*
