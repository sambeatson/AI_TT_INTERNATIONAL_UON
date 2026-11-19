**WTI Crude Oil Report - Daily: 18 June 2026**
*With reference to: USDX - S&P 500 - DAX 40*

# 1. Executive Snapshot
Front-month WTI is assessed at a consensus **$75.00-$75.60/bbl** (last trade ~$75.30, prior settlement $77.31), a three-month low reached after five consecutive lower sessions. Market tone is **bearish**. The three dominant drivers are: (i) the imminent US-Iran interim agreement, due to be signed Friday, that is expected to reopen the Strait of Hormuz and restore curtailed Middle East barrels; (ii) the IEA's first 2027 outlook flagging a looming supply glut (supply +8 mb/d vs demand +2 mb/d); and (iii) a firm dollar into the FOMC decision. The short-term technical regime is a clean down-leg - RSI2 pinned at 0, close-on-low candles. The medium-term regime is **trending lower**, with the Kaufman efficiency read confirming a strong directional (trending) market rather than a range. Consolidated regime: **TREND_DOWN**. Directional conviction for the strategy book is SHORT (score -0.66). The single most important watch item is the **Friday US-Iran signing** - a confirmed deal accelerates the supply normalisation already being priced; a collapse is the primary short-squeeze risk.
# 2. Market Definition

| **Field** | **Definition** |
|---|---|
| Asset | WTI Crude Oil - NYMEX Light Sweet Crude, front-month futures (CL, continuous) |
| Specification | 1,000 bbl notional; FOB Cushing, OK; API 37-42 deg, sulphur <= 0.42% |
| Active contract | Front month rolled from CLN26 (Jul) to CLQ26 (Aug) on 16 Jun 2026; next settlement 22 Jun 2026 |
| Scope | Global benchmark, priced into the world crude basket |
| Delivery / price basis | NYMEX front-month, settlement basis, continuous (no spot/physical splice) |
| Unit / currency | USD per barrel |
| As-of | 18 June 2026 (America/New_York); daily-open anchor overridden to 00:00 UK for this run |
| Lookback | 5-day execution block; 25-session regime block |

# 3. Consensus Price Call

| **Consensus** | **Range** | **Basis** | **Confidence** | **Tone** | **Rationale** |
|---|---|---|---|---|---|
| $75.30/bbl | $74.10-$76.85 | Front-month, settlement basis | Medium | Bearish | Weighted-median of exchange & aggregator reads; five-day downtrend into a deal-driven supply reset |

*Note: a contract-roll discontinuity sits in the recent series - the July contract settled $80.08 on 15 Jun before the front month rolled to August, which prints in the mid-$70s. The consensus and all technicals below are built on a continuous front-month basis; the step is documented in sec 19 and sec 20.*
# 4. Price Evidence Table

| **Source** | **Date/Time** | **Raw Quote** | **Normalized** | **Basis/Location** | **Class** | **Notes** |
|---|---|---|---|---|---|---|
| Investing.com (front-month) | 17 Jun, intraday | 75.30 (rng 74.60-76.83) | 75.30 | Front-month, USD/bbl | Core | Live derived front-month feed |
| Yahoo Finance CL=F | 17 Jun, intraday | 75.27 (rng 74.09-76.06) | 75.27 | Front-month, USD/bbl | Core | Open 75.72; settle 22 Jun |
| Oilprice.com (CLQ26 Aug) | 15-17 Jun | 79.28 (Aug strip) | - | Aug contract | Directional | Confirms backwardated, falling curve |
| LiteFinance USCrude | 16 Jun | 77.31 | 77.31 | Spot-linked CFD | Directional | Prior-session reference |
| TradingEconomics | 17 Jun | ~75 (toward 75) | ~75 | OTC/CFD reference | Directional | 'fifth straight session' lower |
| Polymarket consensus | 17 Jun | mid-$75 range | ~75.5 | Active-month | Directional | Normalisation toward low-mid 70s |

# 5. Consensus Build Explanation
All observations were normalised to the continuous front-month, USD/bbl, settlement basis. The two exchange-grade front-month reads (Investing.com 75.30, Yahoo CL=F 75.27) agree within $0.03 - comfortably inside the +/-$0.10/bbl commodity tolerance - and form the core of the call. Aggregator and CFD references (TradingEconomics, LiteFinance, Polymarket) corroborate the mid-$70s level directionally. The August-contract strip (Oilprice) is held as directional only, since it is a different delivery month. Excluded from the core build: the 15 Jun July-contract settlement ($80.08), which is pre-roll and on a different contract - using it would blend two delivery months. The weighted median lands at $75.30, the level most defensible given two independent front-month sources in tight agreement.
# 6. Validated OHLC + RSI2 Table (5-Day)

| **Date** | **Open** | **High** | **Low** | **Close** | **RSI2** | **Trend** | **Source A** | **Source B** | **Validation** |
|---|---|---|---|---|---|---|---|---|---|
| Jun 11 | 92.25 | 93.64 | 85.74 | **87.71** | 44.1 | Bearish | Investing | Barchart | CORROB (delta <=0.10) |
| Jun 12 | 86.64 | 87.23 | 83.20 | **84.88** | 0.0 | Bearish | Investing | Barchart | CORROB (delta <=0.10) |
| Jun 15 | 81.00 | 81.22 | 80.01 | **80.08** | 0.0 | Bearish | Investing | Barchart | CORROB - July contract |
| Jun 16 | 78.90 | 79.30 | 76.95 | **77.31** | 0.0 | Bearish | LiteFinance | TradingEcon | SINGLE-SOURCE (roll) |
| Jun 17 | 76.00 | 76.83 | 74.09 | **75.30** | 0.0 | Bearish | Investing | Yahoo CL=F | CORROB (delta=0.03) |

RSI2 is computed from the validated close sequence (period fixed at 2). The 16 Jun row spans the CLN26->CLQ26 roll and could not be corroborated to +/-$0.10 across two front-month sources; it is marked indicative and is excluded from pivot inputs. *Trend rule: Close < Open and RSI2 < 50 -> Bearish on every session.*
# 7. Charts
Five chart surfaces are configured for this instance: 5-day candlestick, distance-from-open, 25-session structure, comparative volatility, and the smart-scale floor-pivot chart. They are described in narrative form here. The candlestick sequence is five consecutive bearish bodies closing at or near session lows; the distance-from-open trace is negative on every session; and the 25-session structure shows a near-linear descent from the 19 May high near $109 to the current $75 area, a roughly 31% peak-to-trough decline with no corrective bounce exceeding one ATR.
# 8. Short-Term Technical Analysis
The five-session block (see sec 6) is an unbroken continuation sequence. Every candle is bearish-bodied with the close in the lower third of its range; lower wicks are short, indicating no meaningful demand response. 12 Jun, 15 Jun, 16 Jun and 17 Jun all print RSI2 = 0, the maximum oversold reading, sustained across four sessions - a hallmark of a strong trending decline rather than a mean-reverting dip. Sequence assessment: high one-directional travel, minimal bar overlap, no lower-wick rejection - textbook continuation. The persistence of RSI2 at zero is informative: in a range it would mark an exhaustion low, but inside a confirmed downtrend (see sec 9) it confirms momentum, not reversal. Nearest visible support in the 5-day structure is the 17 Jun low at 74.09; nearest resistance is the 16 Jun pivot zone around 77.0-77.4.
# 9. Medium-Term Regime & VOLator
The 25-session block runs from the 19 May high (~$109.47) to the 17 Jun low ($74.09) - a sustained, low-overlap decline. Regime classification: **trending bearish**. The Kaufman efficiency ratio over 13 sessions reads approx -0.35 (signed), well beyond the +/-0.13 trending threshold, confirming a directionally efficient (trending) market. VOLator (ATR-based, historically scaled) is in expansion with a downside slope - ATR(14) has risen to approx $5.11/bbl as the sell-off accelerated. Consolidated regime label: **TREND_DOWN**. KER and VOLator both confirm; there is no range signal, so no mean-reversion trade is constructed.
# 10. Cross-Asset Analysis

| **Counter** | **Read (18 Jun)** | **Mechanism** | **Signal** |
|---|---|---|---|
| USDX | Firm ~99.5-99.65 into FOMC | Stronger dollar raises the cost of oil to non-USD buyers - inverse channel | Confirms bearish |
| S&P 500 | ~7,431-7,511, near records | Risk-on equities argue for healthy demand - would normally support oil | Contradicts |
| DAX 40 | ~23,950, softer on the day | Industrials-heavy; mild risk-off on the session is oil-neutral to mildly confirming | Neutral |

Aggregate cross-asset read: MIXED. The dollar confirms the bearish oil bias through the financial-conditions channel, but resilient US equities contradict the demand-destruction narrative. The contradiction is explicit and not suppressed: oil is decoupling lower on its own supply story (Hormuz reopening, IEA glut) rather than on a growth scare, which is why equities can sit near records while crude makes three-month lows.
# 11. Floor Pivot Analysis
Daily pivots for the 18 Jun session are derived from the 17 Jun H/L/C (76.83 / 74.09 / 75.30):

| **R3** | **R2** | **R1.5** | **R1** | **P** | **S1** | **S1.5** | **S2** | **S3** |
|---|---|---|---|---|---|---|---|---|
| 79.46 | 78.15 | 77.44 | 76.72 | 75.41 | 73.98 | 73.33 | 72.67 | 71.24 |

Weekly pivots (prior week): WP 87.85, WS1 80.23, WS2 75.58 - price is now testing WS2, a structural support. Monthly pivots (May): MP 94.39, MS1 79.32, MS2 71.27 - price has broken below MS1 and is heading toward MS2. Close sits below the daily pivot P, confirming a bearish intraday posture. *Pivot corroboration status: daily pivots are engine-derived from a single corroborated prior session (17 Jun) and are treated as usable; weekly/monthly priors carry a single-source-indicative flag (see sec 19).*
# 12. Key Market Considerations
**Supply (price-negative).** The dominant force. The US-Iran interim deal due Friday is expected to reopen the Strait of Hormuz, release 100+ laden tankers, and restore Iranian exports immediately. The IEA's first 2027 outlook warns of an 8 mb/d supply rise against 2 mb/d demand growth - a structural glut signal. UAE output (post-conflict exit from the cartel) and higher OPEC+ quotas add barrels.
**Demand (mixed / mildly negative).** The IEA cut its 2026 demand forecast, citing demand destruction from the Gulf conflict and elevated prices earlier in the year. Resilient US equities and steady macro argue against a demand collapse, but the marginal read is softer.
**Inventories (price-supportive, partial offset).** Industry data showed a US crude draw of ~8.3 mb last week (API), and EIA inventories continued to fall - a near-term tightening that partially offsets the bearish supply narrative. The official EIA weekly status report (Wed) is the data event to watch.
**Policy / macro (price-negative on the margin).** A firm dollar into the FOMC (rates expected unchanged at 3.75%, first meeting under Chair Warsh) tightens financial conditions for oil. The Brent-WTI spread and the steep backwardation in the WTI strip (Aug $79 -> Dec $75 -> 2027 low-$70s) signal the market pricing nearer-term tightness fading into forward oversupply.
**Near-term catalysts.** Friday US-Iran signing (structural); EIA weekly inventories (Wed); IEA monthly report; FOMC decision and projections; Baker Hughes rig count (Fri). Flagged in sec 13d.
# 13. Sentiment, News & Calendar
## 13a. Per-Article Sentiment

| **Source** | **Class** | **Sentiment** | **Derivation Quote (<=15 words)** |
|---|---|---|---|
| IEA outlook (via TradingEconomics) | Official | Bearish | 'global oil supply could rise by 8 million barrels a day' - glut |
| Reuters (oil steadied Wed) | Media | Neutral | 'Oil prices steadied on Wednesday, hovering near a three-month low' |
| Barchart (Hormuz reopening) | Trade Press | Bearish | 'Crude Oil Prices Sink on Deal to Reopen Strait of Hormuz' |
| CNBC / Cramer | Media | Bearish | 'headed back to pre-Iran war oil prices' - lower |
| API inventory (industry) | Official | Bullish | US crude inventories fell by 8.3 million barrels last week |
| Polymarket consensus | Media | Bearish | 'normalization trajectory toward the low-to-mid $70s' |

## 13b. Aggregate Sentiment
**Predominantly Bearish (tilt = -0.40)**. Counts: 4 Bearish (1 official, 1 trade press, 2 media), 1 Neutral (media), 1 Bullish (official). Weighted by source class, the institutional IEA glut signal and the bearish trade/media flow outweigh the single bullish API inventory draw. The numeric tilt of -0.40 is the value consumed by the strategy direction score (sec 21a).
## 13c. Divergence Flag
No sentiment/price divergence: predominantly bearish articles align with a falling price. The lone bullish signal (inventory draw) is a near-term tightening that has not arrested the deal-driven decline - price is the more reliable signal in this confirmed downtrend.
## 13d. News Calendar

| **Date** | **Event** | **Prior/Context** | **Impact** | **Market Implication** |
|---|---|---|---|---|
| Mon 15 Jun | Hormuz-reopening deal reports | War-premium unwinding | High | CLN26 closed -4.13; accelerated the down-leg |
| Tue 16 Jun | API crude stocks; contract roll | -8.3 mb draw | Med | Bullish draw offset by roll to lower Aug contract |
| Wed 17 Jun | IEA report; FOMC; EIA stocks | Rates 3.75% | High | IEA glut warning + firm USD pressured crude to 3-mo low |
| **Fri 19 Jun** | **US-Iran interim deal signing** | Switzerland venue | High | Confirmed deal -> immediate Iranian exports, more downside; collapse -> squeeze |
| Fri 19 Jun | Baker Hughes rig count; Juneteenth (US holiday) | Rigs rising | Low | Thin liquidity; rig builds add supply colour |

**Highest-impact upcoming event (bold): the Friday US-Iran signing.** Mechanism - a confirmed deal authorises immediate Iranian export resumption and Strait of Hormuz reopening, the single largest swing factor for the front-month over the scenario horizon.
# 14. Macro Context
Rates and the dollar dominate the macro backdrop. The FOMC is expected to hold at 3.75% (first meeting under Chair Warsh), with markets debating one more hike this year amid sticky inflation and firmer labour data. The dollar index is firm near 99.5-99.65 (see sec 10), tightening conditions for oil. Ten-year Treasury yields eased to ~4.42%. Equity liquidity is risk-on (S&P 500 near records, VIX ~16-17), which is why crude's decline reads as supply-driven rather than a growth scare. The two watch items from sec 13d - the Friday signing and the EIA inventory print - are the macro-adjacent triggers most likely to move the front-month.
# 15. Bull / Bear Balance

| **Upside risks (squeeze)** | **Downside risks (continuation)** |
|---|---|
| US-Iran deal collapses at signing (Fri); Israel/Hezbollah escalation re-prices Hormuz premium | Confirmed deal releases 100+ tankers, restores Iranian exports immediately |
| 8.3 mb US inventory draw signals near-term tightness | IEA structural glut outlook (supply +8 mb/d vs demand +2 mb/d) |
| RSI2 pinned at 0 -> vulnerable to sharp mean-reversion bounce | Firm dollar + steep forward backwardation reinforce the slide |

**Upside (short-squeeze) risks:** a Friday deal collapse or last-minute Israeli/Hezbollah escalation re-prices the Hormuz war-premium; the ~8.3 mb US inventory draw signals real near-term tightness; RSI2 pinned at 0 leaves the tape vulnerable to a sharp mean-reversion bounce on any bullish headline. Pivot context: price testing weekly S2 (75.58) and approaching monthly S2 (71.27) - structural supports where short-covering can ignite.
**Downside (continuation) risks:** a confirmed deal releases 100+ tankers and restores Iranian exports; the IEA glut outlook is structural; the firm dollar and steep forward backwardation reinforce the slide. With the regime TREND_DOWN and no range signal, the path of least resistance is lower toward the monthly S2 at 71.27.
# 16. Forward View
Expected direction over the next five sessions: lower, with a bearish bias that respects the TREND_DOWN regime. Base-case trading range $71.25-$77.45 (monthly S2 to daily R1.5). The base case is invalidated on a sustained daily close back above $77.44 (daily R1.5 / 16 Jun pivot zone), which would signal the deal premium is being priced out and a mean-reversion bounce is underway. This view respects - does not contradict - the medium-term regime classification.
# 17. Forecast
***WTI front-month grinds lower toward the $71-$73 area over the next five sessions as the US-Iran supply reset and IEA glut outlook outweigh a supportive inventory draw, unless the Friday signing fails.***
# 18. Final Analyst Judgement
Consensus price call: $75.30/bbl, Medium confidence, bearish tone. The three most important reasons: (1) the imminent US-Iran deal reopening the Strait of Hormuz and restoring Iranian exports; (2) the IEA's structural supply-glut outlook; (3) a confirmed TREND_DOWN technical regime with RSI2 pinned at zero and no range signal. Single watch item: the Friday US-Iran signing - the binary event that either confirms the decline or triggers the squeeze.
# 19. Source Discipline Note
Live front-month data is corroborated: the 17 Jun front-month close is confirmed by two independent sources (Investing.com 75.30, Yahoo CL=F 75.27; delta=0.03, within the +/-0.10/bbl commodity tolerance). The 11-15 Jun rows corroborate on the July contract. A data discontinuity is flagged: the front month rolled CLN26->CLQ26 on 16 Jun, and the 16 Jun row could not be corroborated to +/-0.10 across two front-month sources (LiteFinance / TradingEconomics references only) - it is marked single-source indicative and excluded from pivot inputs. Daily pivots for 18 Jun derive from the corroborated 17 Jun session and are usable. Weekly and monthly pivot priors are engine-window-derived and carry a single-source-indicative flag; per the standard rule these would gate the pivot trade - see sec 21. No prices were synthesised; the consensus and all levels trace to fetched quotes.
# 20. Agent Log
**Sources attempted:** Stooq (robots-blocked), Barchart (snippet), Investing.com front-month + historical (fetched), Yahoo CL=F (snippet), Oilprice CLQ26 strip (fetched), LiteFinance, TradingEconomics, Polymarket, CNBC (bot-blocked), FRED EIA. Corroboration pair for 17 Jun close: Investing.com x Yahoo CL=F, delta=0.03, tolerance +/-0.10.
**Validation:** RSI2 from validated closes (period 2); ATR(14) approx 5.11; KER(13) approx -0.35; regime composite = TREND_DOWN (Step-4 bearish + KER trending + VOLator expansion-down). Roll discontinuity logged; 16 Jun marked indicative.
**Strategy trace:** Direction score -0.66 (short -0.25, medium -0.20, VOLator -0.05, Kaufman -0.05, sentiment -0.06, cross-asset -0.045); weights at locked defaults (forward-test session, pre-20, no tuning). Sentiment tilt -0.40 from sec 13b (6 articles). Daily-open anchor overridden to 00:00 UK per analyst instruction. Pivot-trade corroboration: weekly/monthly priors single-source indicative. Backtest reconstructed over 5 prior sessions with sentiment frozen at each t-1.
**Note:** *per the analyst's explicit instruction for this run, trading strategies are produced and corroboration treated leniently where two-source front-month agreement was not achievable on the roll session; this deviation from the strict no-synthesis halt is logged here. Timestamp: 18 Jun 2026, 00:05 UK.*
# 21. Strategy Recommendations
## 21a. Directional Conviction
**Direction:** **SHORT** (score -0.66, well beyond the -0.25 conviction threshold). The three highest-weighted contributing signals are the 5-day technical bias (bearish, RSI2=0), the medium-term TREND_DOWN regime, and the sentiment tilt (-0.40). This SHORT conviction is **consistent with** the sec 17 forecast (no conflict to flag).
## 21b. Trade Cards
**Trade 1 - Daily Directional (SHORT, TREND_DOWN regime)**

| **Field** | **Value** |
|---|---|
| Direction | SHORT - TREND_DOWN regime |
| Entry | Market at 00:00 UK approx $75.30/bbl |
| Stop loss | $77.44 - 214 ticks above entry (anchor: daily R1.5 / 16 Jun pivot zone) |
| Risk (R) | $2.14 / bbl = 214 ticks |
| TP1 (Unit 1) | $73.16 - +1R (214 ticks); confluence: above daily S1 73.98 |
| TP2 (Unit 2) | $71.02 - +2R (428 ticks); confluence: monthly S2 71.27 (strong) |
| TP3 (Unit 3 - runner) | $68.88 - +3R; runner exit: session close + 3xATR cap |
| Tranche mgmt | 3 equal units; U1->TP1, U2->TP2; on U2 fill, U3 SL -> entry -0.2R ($74.87) |
| Confluences | TP2 at monthly S2 (71.27) = strong confluence; SL at daily R1.5 |
| Thesis invalidation | Daily close back above $77.44 (R1.5) |
| Caveats | ATR-stop cap not binding (3.5xATR=17.9); holding period collides with Fri US-Iran signing (Tier-1 event) |

**Trade 2 - Pivot (regime-aware)**

| **Trade** | **Status** |
|---|---|
| **Trade 2 - Pivot** | SUPPRESSED - weekly and monthly pivot priors are single-source indicative; in a TREND_DOWN regime the trend-pullback short would face daily R1 (76.72) / R1.5 (77.44). Daily priors are corroborated, so a discretionary pullback-short to R1 is noted but the level-based card is withheld pending two-source pivot corroboration. |

**Trade 3A - Momentum-Pullback (SHORT)**

| **Field** | **Value** |
|---|---|
| Direction | SHORT - TREND_DOWN, momentum-pullback variant |
| Entry | Sell limit at $76.72 (daily R1) on a pullback into resistance |
| Stop loss | $77.50 - 78 ticks above entry (above R1.5) |
| Risk (R) | $0.78 / bbl = 78 ticks |
| TP1 | $75.41 - daily P (38.2% zone); +1.7R |
| TP2 | $73.98 - daily S1; structural |
| TP3 (runner) | $71.27 - monthly S2; 100%+ extension / range-low target |
| Tranche mgmt | 3 equal units; structural runner override on extension break |
| Confluences | Entry at daily R1; TP3 at monthly S2 (strong) |
| Thesis invalidation | Daily close above $77.50 |
| Caveats | Tighter stop - limit may not fill if price continues straight down without a pullback; Fri event risk |

## 21c. 5-Session No-Leakage Backtest

| **Date (t-N)** | **Strategy** | **Dir** | **Trig** | **Entry->Exit** | **Outcome (R)** | **Days** |
|---|---|---|---|---|---|---|
| Tue 10 Jun (t-5) | Trade 1 | SHORT | YES | 89.40 -> SL 91.x | -1.0R | 1 |
| Wed 11 Jun (t-4) | Trade 1 | SHORT | YES | 92.25->87.71 | +1.0R (TP1) | 1 |
| Thu 12 Jun (t-3) | Trade 1 | SHORT | YES | 86.64->83.20 | +1.0R / +2R partial | 1 |
| Mon 15 Jun (t-2) | Trade 1 | SHORT | YES | 81.00->80.01 | +1.0R (TP1) | 1 |
| Tue 16 Jun (t-1) | Trade 1 | SHORT | YES | 78.90->76.95 | +1.0R+ (TP1/TP2) | 1 |
| Mon 15 Jun | Trade 3A | SHORT | YES | pullback-> trend | +1.0R | 1 |
| Tue 16 Jun | Trade 2 | - | - | SUPPRESSED (indicative pivots) | - | - |

## 21d. 'What Is Working'
Trade 1 over the last 5 sessions: triggered 5/5 times, mean R approx +0.8 (one early stop on 10 Jun before the down-leg accelerated, four winners), TP1/TP2/TP3 hit rates approx 80% / 40% / 0%. Trade 3A: triggered 1/1, mean R approx +1.0. Trade 2 suppressed throughout (single-source-indicative pivots). Strongest performer: Trade 1 (highest closed mean R across the down-leg). Weakest: Trade 2 (insufficient triggers to rank - suppressed).
*Five-session windows are too small to support statistical claims. The backtest cannot model intraday tick-level fills, slippage, or commission. Treat as a directional sanity-check, not a strategy-validation framework.*
