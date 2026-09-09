**GOLD (SPOT) — DAILY TECHNICAL & STRATEGY REPORT**
XAU/USD spot · GC=F front-month corroboration
*Senior Commodities Analyst — Precious Metals*
**Report date: 16 July 2026 (Europe/London) · Data snapshot: 15 July 2026 close**
Modular Prompt Architecture v2.1 · M1 Gold instance · M5 Strategies ENABLED
## Run Configuration & Overrides

| **Parameter** | **Value** | **Status** |
|---|---|---|
| [PRIMARY_ASSET] | Gold (XAU/USD spot) | M1 default |
| [AS_OF_DATE] | 16 July 2026 | USER OVERRIDE (M1 = 29 Apr 2026) |
| [DAILY_OPEN_ANCHOR] | 00:00 UK | USER OVERRIDE INSTRUCTED — value re-affirmed at 00:00 UK |
| [UNIT_OF_MEASURE] / [TICK_SIZE] | USD/oz / 0.01 (tick) | M1 default |
| [MINIMUM_SOURCE_COUNT] | 6 | Met — 8 independent sources |
| [CONSENSUS_METHOD] | Weighted median | M1 default |
| Corroboration posture | LENIENT — user-authorised | USER OVERRIDE: strategies not suppressed on source corroboration |
| Weights basis | Defaults (0.25/0.20/0.10/0.15/0.15/0.15) | Locked — session 1 of 20 |

*Override note on [DAILY_OPEN_ANCHOR]: the instruction was to override the M1 value. The M1 Gold instance carries 00:00 UK. Per PATCHES P6, the anchor must match the asset's trading session — gold trades 23+ hours and 07:00 UK is not a session reset for spot. The only permitted alternatives under the P5 checklist are "00:00 UK" / "07:00 UK". The anchor is therefore explicitly re-affirmed and locked at 00:00 UK for the 16-Jul-2026 session; substituting 07:00 UK would place the entry mid-London-session and break the anchor's definition. This override action is logged in §20.*
# §1 Introduction
This report covers spot gold (XAU/USD, London Good Delivery 400-oz, loco London, T+2) for the trading session of 16 July 2026, anchored on the 15 July 2026 close. Scope is global; the decision use case is trading and risk review (forward-test). Counters are USDX (DX-Y.NYB), S&P 500 (^GSPC) and DAX 40 (^GDAXI). Silver (XAG/USD) is carried as the secondary precious-metals pair.
The session arrives with gold in a well-defined consolidation inside a larger corrective structure. Price is roughly 28% below the late-January 2026 all-time high near $5,595–5,608, but has stabilised above the psychologically and structurally important $4,000 handle across the last four sessions. Two soft US inflation prints — June CPI at 3.5% y/y and a June PPI that unexpectedly declined — have pulled the dollar off its early-July highs and materially reduced the market's implied odds of near-term Fed tightening. That is the bullish leg. Against it sits a still-hawkish Fed chair, a real-yield backdrop that remains punitive for a non-yielding asset, and ETF outflows. The result is a market with genuinely two-sided drivers and a directional score that lands close to zero.
# §2 Market Definition

| **Attribute** | **Specification** |
|---|---|
| Instrument | Gold spot, XAU/USD |
| Product spec | London Good Delivery bar, 99.99% pure, 400-oz quote convention |
| Price basis | Spot, immediate settlement (loco London) |
| Delivery basis | OTC London spot, T+2 |
| Unit / currency | USD per troy ounce / USD |
| Tick size / name | 0.01 / tick |
| Venues referenced | LBMA (London OTC), COMEX (CME GC=F), Singapore, Shanghai SGE |
| Session anchor | 00:00 UK — London/Asia handover reset |

# §3 Source Register
Eight independent sources were consulted against a [MINIMUM_SOURCE_COUNT] of 6. Tier ordering follows the M2 §A.2 evidence hierarchy: exchange-settled and benchmark-fixed reads outrank aggregators; retail FX broker spot quotes are excluded from the consensus build per [RESTRICTIONS], and CFD-derived prints are down-weighted to third-tier corroboration.

| **#** | **Source** | **Read (USD/oz)** | **Timestamp (15-Jul)** | **Tier / weight** |
|---|---|---|---|---|
| 1 | Bloomberg (XAU:CUR) | 4,060.55 | 16:59 EDT | Tier 1 — 1.0 |
| 2 | Investing.com XAU/USD | 4,073.65 | Intraday | Tier 1 — 1.0 |
| 3 | TradingEconomics (OTC/CFD benchmark) | 4,070.00 | Late session | Tier 1 — 1.0 |
| 4 | TradingView XAUUSD | 4,052.78 | Session | Tier 1 — 1.0 |
| 5 | CNBC XAU= | 4,023.84 | 03:48 EDT | Tier 1 — 1.0 |
| 6 | LiteFinance | 4,021.66 | Intraday | Tier 3 — 0.8 |
| 7 | Vantage XAUUSD CFD | 4,032.76 | 06:00 UTC | Tier 3 — 0.8 (CFD) |
| 8 | FXLeaders | 4,029.00 | European session | Tier 3 — 0.8 |

*Corroboration status: PARTIAL. All eight sources agree on the market's location — the $4,020–4,075 band — and on the direction of the drivers. They do not agree on a single settlement print, because spot gold has no single settlement print: each source stamps a different intraday moment across a 24-hour market, and the session itself ranged roughly $55. The dispersion of $51.99 between the lowest and highest read is therefore a timestamp artefact, not a data conflict. No source was excluded. Per the user's explicit instruction, strategies are NOT suppressed on this basis; the lenient-corroboration flag is carried on every trade card below.*
# §4 Benchmark Cross-Reference
LBMA AM/PM Fix, CME GC=F, Yahoo Finance, Investing.com, Twelve Data and Bloomberg consensus were the specified benchmark set. Bloomberg and Investing.com were obtained directly. LBMA fix values and a discrete GC=F settlement for 15-Jul were not independently retrievable within this run; the TradingEconomics OTC benchmark and TradingView composite stand in as proxies, and this substitution is flagged. Regional cross-reference (London / COMEX / Singapore / SGE) showed no evidence of an arbitrage gap or regional divergence beyond normal timing spread.
# §5 Consensus Price Build

| **Method** | **Value (USD/oz)** |
|---|---|
| Weighted median (M1 [CONSENSUS_METHOD]) | 4,052.78 |
| Simple median (reference) | 4,042.77 |
| Source range | 4,021.66 – 4,073.65 |
| Dispersion | 51.99 (1.28% of mid) |
| Adopted session close anchor | 4,070.00 |

The weighted median of $4,052.78 is the formal consensus under [CONSENSUS_METHOD]. However, the trade-construction anchor is the last close, not the intraday consensus: the M5 §5 entry is a market order at the 00:00 UK reset, which follows the 15-Jul close. The adopted close anchor of $4,070.00 is the late-session read corroborated by TradingEconomics and sits within one tick-cluster of the Investing.com $4,073.65 print. The $17 gap between weighted median and close anchor reflects gold firming into the late US session on the PPI miss.
# §6 OHLC — Primary and Secondary
**Gold (XAU/USD) — 5 sessions**

| **Date** | **Open** | **High** | **Low** | **Close** | **Chg %** |
|---|---|---|---|---|---|
| 09-Jul-26 | 4,105.00 | 4,132.00 | 4,070.00 | 4,088.00 | — |
| 10-Jul-26 | 4,088.00 | 4,110.00 | 4,035.00 | 4,044.00 | −1.08% |
| 13-Jul-26 | 4,044.00 | 4,058.00 | 3,985.80 | 4,001.79 | −1.04% |
| 14-Jul-26 | 4,001.13 | 4,102.72 | 3,985.76 | 4,053.56 | +1.29% |
| 15-Jul-26 | 4,052.96 | 4,090.00 | 4,017.50 | 4,070.00 | +0.41% |

*Reconstructed from corroborated multi-source reads (Investing.com historical, TradingEconomics, Vantage, LiteFinance). Intraday extremes are composite across venues; treat highs/lows as ±$5 indicative. SINGLE-SOURCE-INDICATIVE on the 09–10 Jul rows.*

**Silver (XAG/USD) — secondary pair**

| **Date** | **Close** | **Chg %** | **Note** |
|---|---|---|---|
| 13-Jul-26 | 57.62 | — | Pre-CPI |
| 14-Jul-26 | 58.81 | +2.06% | CPI-driven rally |
| 15-Jul-26 | 58.41 | −0.46% | Rejected at $59.00 |

Gold/Silver ratio: 69.04 on 15-Jul, essentially unchanged from 69.05 on 14-Jul. The ratio's stability through a 2% silver move confirms the precious complex is trading as a bloc on a common macro driver (the inflation print) rather than on metal-specific flow. Silver's rejection at $59.00 while gold held $4,000+ is a mild relative-strength tell in gold's favour.

# §7 Short-Window Technical Structure (5-day)

| **Metric** | **Value** | **Read** |
|---|---|---|
| Swing high (5d) | 4,132.00 | 09-Jul intraday |
| Swing low (5d) | 3,985.76 | 14-Jul intraday |
| 5-day range | 146.24 (1.86 × ATR) | Compressed |
| Net 5-day change | −18.00 (−0.44%) | Flat |
| Path length (sum \|Δclose\|) | 153.77 | High churn |
| Position in range | 57.6% | Upper half |

The short window is the clearest single fact in this report: gold has travelled 153.77 points of path to end 18 points lower. That is a market working hard to go nowhere. Price closed at 4,070.00, in the upper half of a 146-point range, having twice defended the 3,985–4,000 zone (13-Jul and 14-Jul lows within four cents of each other at 3,985.80 / 3,985.76). A double-tap that precise is a real bid, not noise. The 5-day bias is therefore modestly constructive: +0.30 on the short-technical axis, driven by the defended low and the close in the upper half, tempered by the failure to hold above 4,100 on 09-Jul and again on 14-Jul.
RSI(14) is reported between 40 and 42 across independent sources (FXLeaders 42, LiteFinance 42, RoboForex 40.5) — below neutral, not oversold, with no divergence. MACD is negative but with a narrowing histogram, the classic signature of exhausting downside momentum inside a base rather than an impulse leg. VWAP and SMA20 sit above spot, which is the counterweight: rallies are selling into overhead supply.
# §8 Short-Term Bias & RSI2
Directional bias (5-day): MODESTLY LONG (+0.30). RSI(2) is not independently reported by any consulted source and is not reconstructible to tick precision from composite OHLC; it is therefore excluded from the score rather than fabricated. The §8 contribution rests on the M3 §2a structural read alone. This is a documented degradation of the short-tech input and is flagged in §20.
# §9 Medium-Window Structural Regime (5-week)

| **Metric** | **Value** | **Read** |
|---|---|---|
| 25-day trend | Down | Corrective |
| 1-month change | −5.94% | Material decline |
| 12-month change | +21.90% | Structural bull intact |
| Distance from ATH (5,608, Jan-26) | −27.4% | Deep correction |
| 50-day EMA | ~4,730 (JPM read) | Price far below |
| 200-day EMA | ~4,340 (JPM read) | Price far below |
| 25-day swing high / low | ~4,310 / 3,985.76 | Range boundaries |

The medium window is unambiguously bearish and it is the single heaviest negative in the score at −0.55. Price trades below both the 50-day and 200-day moving averages — the definition of a downtrend on any conventional reading — and has shed nearly 6% in a month. J.P. Morgan's Greg Shearer characterised gold as caught in technical no-man's-land, above the 200-day and below the 50-day; the market has since resolved that ambiguity to the downside by breaking beneath the 200-day. The structural multi-year uptrend from 2022 remains intact on weekly and monthly moving averages, but that operates on a timescale irrelevant to a next-session trade card. For a 16-Jul session, the medium regime says: this is a bear-trend consolidation, and consolidations in bear trends resolve lower more often than not.
# §10 Cross-Asset Counters

| **Counter** | **Level (15-Jul)** | **Direction** | **Correlation to Gold** | **Read for Gold** |
|---|---|---|---|---|
| DX-Y.NYB (USDX) | 100.76–100.90 | Falling (−0.33%) | Strong inverse | POSITIVE |
| ^GSPC (S&P 500) | 7,556–7,570 | Rising (+0.36/+0.55%) | Weak / regime-dependent | MILDLY NEGATIVE |
| ^GDAXI (DAX 40) | 25,147 | Rising (+0.13%) | Weak | NEUTRAL |
| US 10Y yield | 4.587% | Easing marginally | Inverse (real-yield channel) | MILDLY POSITIVE |
| WTI crude | 79.87 (+2.22%) | Rising, 1-mo high | Inflation-hedge channel | POSITIVE (indirect) |
| XAG/USD (secondary) | 58.41 | Flat/soft | Strong positive | NEUTRAL |

Cross-asset confirmation scores +0.45 — the strongest positive input in the model, and it is carried almost entirely by the dollar. USDX fell 0.33% to ~100.76–100.90 on the CPI miss and now trades below both its 50-period (100.835) and 200-period (100.664) moving averages, with a sell signal on Investing.com's daily aggregate. Gold's dominant mechanism is the inverse dollar link, and that link is currently pointing up for gold.
The equity counters cut the other way but weakly. S&P 500 at 7,556–7,570 and DAX at 25,147 both closed higher, which is a risk-on tape and therefore a mild drag on safe-haven demand. Their correlation to gold is regime-dependent and currently loose — in the present configuration both gold and equities are rallying on the same dovish repricing, so the risk-on read should not be over-weighted as a gold negative. WTI at $79.87, a one-month high on the Strait of Hormuz disruption, is a genuine second-order positive: it keeps the inflation-hedge case alive even as it complicates the Fed path.
*Contradiction flag (M4 §12 requirement): the cross-asset block (+0.45) and the medium-term structural regime (−0.55) point in opposite directions. This contradiction is stated, not resolved. It is the reason the composite score sits near zero.*
# §11 Volatility Regime (VOLator) & Kaufman KER

| **Metric** | **Value** | **Classification** |
|---|---|---|
| True ranges (last 4 sessions) | 75.0 / 72.2 / 116.96 / 72.5 | — |
| ATR(5) | 84.16 | Elevated |
| ATR(14) estimate | 78.50 | ≈1.93% of spot |
| Current session range | 72.50 (0.92 × ATR14) | Contracting |
| VOLator regime | ELEVATED, contracting | Score −0.20 |
| Kaufman KER (13, EMA3) — 5d proxy | 0.117 | RANGING (below 0.13) |
| KER threshold band | Trend >0.13 / range-up 0.09 | Just inside range |

ATR(14) is estimated at 78.50 rather than computed from a full 14-session tick series, which was not retrievable; it is anchored to the observed 4-session ATR of 84.16 and adjusted toward the ~1.9% daily-range regime that has prevailed for three weeks. Treat it as ±5%. Every stop and target below scales off this number, so the caveat propagates.
KER at 0.117 lands below the 0.13 trend threshold and above the 0.09 range-up boundary — the market is RANGING, and it is ranging in the upper sub-band, which carries a marginal upward bias. This matters more than it looks: KER is measuring exactly what §7 observed qualitatively, that 153.77 points of path produced 18 points of displacement. Efficiency of 11.7% is a chop signature. Trend-following expressions are structurally disadvantaged here; mean-reversion and range expressions are favoured. The Kaufman axis contributes −0.10 (penalising directional conviction, not direction itself).
# §12 Pivot Levels (Classic, from 15-Jul OHLC)

| **Level** | **Price (USD/oz)** | **Distance from 4,070** | **Confluence** |
|---|---|---|---|
| R3 | 4,173.33 | +103.33 | — |
| R2 | 4,131.67 | +61.67 | 5d swing high 4,132.00 — STRONG |
| R1.5 | 4,116.25 | +46.25 | LiteFinance R 4,114.01 — STRONG |
| R1 | 4,100.83 | +30.83 | Psych 4,100 |
| Pivot (P) | 4,059.17 | −10.83 | Fib 50% (4,058.88) — STRONG |
| S1 | 4,028.33 | −41.67 | FXLeaders S 4,002 zone edge |
| S1.5 | 4,007.50 | −62.50 | LiteFinance S 4,007.83 — STRONG |
| S2 | 3,986.67 | −83.33 | 5d swing low 3,985.76 — VERY STRONG |
| S3 | 3,955.83 | −114.17 | — |

The pivot structure is unusually well-corroborated. Three levels show independent confluence: R2 at 4,131.67 sits within 0.33 of the 5-day swing high; S1.5 at 4,007.50 sits within 0.33 of LiteFinance's published support at 4,007.83; and S2 at 3,986.67 sits within 1 point of the twice-defended 5-day low. When a mechanically derived pivot and an independently published level land inside a dollar of each other, that level is real. The pivot itself at 4,059.17 coincides with the 50% fib of the 4-session swing at 4,058.88 — spot is currently sitting 11 points above its own pivot, which is the technical definition of a neutral-to-mildly-constructive open.
*Corroboration flag: pivots are derived from the composite 15-Jul OHLC (H 4,090.00 / L 4,017.50 / C 4,070.00). Because the high and low are composite across venues rather than a single exchange print, all pivot levels carry SINGLE-SOURCE-INDICATIVE status and inherit that flag into the R1.5 / S1.5 midpoints per M5 §4a.*
# §13 Fibonacci Swing Anchor (Adaptive)
Per M5 §4b, the default [FIB_RANGE_DAYS] = 4 lookback produced a swing of 3,985.76 → 4,132.00, magnitude 146.24 = 1.86 × ATR(14). That is below the 2 × ATR qualifying threshold. The lookback was extended in 1-session increments to 10 sessions, at which point the swing 3,985.76 → 4,310.00 qualifies with magnitude 324.24 = 4.13 × ATR(14).

| **Fib level** | **Price (USD/oz)** | **Position vs spot 4,070** |
|---|---|---|
| 0.000 (swing high, ~02-Jul) | 4,310.00 | +240.00 |
| 0.236 | 4,233.48 | +163.48 |
| 0.382 | 4,186.14 | +116.14 |
| 0.500 | 4,147.88 | +77.88 |
| 0.618 | 4,109.62 | +39.62 |
| 0.786 | 4,055.15 | −14.85 |
| 1.000 (swing low, 14-Jul) | 3,985.76 | −84.24 |

| **Anchor parameter** | **Value** |
|---|---|
| Lookback actually used | 10 sessions (extended from default 4) |
| Swing endpoints | 4,310.00 (high, ~02-Jul) → 3,985.76 (low, 14-Jul) |
| Swing magnitude in ATR units | 4.13 × ATR(14) |
| Active swing direction | DOWN (latest local low more recent than latest local high) |

Spot at 4,070.00 sits just above the 0.786 retracement at 4,055.15 — a shallow bounce off the low, consistent with a corrective rally inside a down-swing rather than a reversal. The 0.618 at 4,109.62 is the first level where a bounce would start to threaten the down-swing's integrity; it is also within 5 points of R1 and the 4,100 handle. That cluster is the session's decisive line.

# §14 Sentiment & Positioning

| **Input** | **Reading** | **Tilt** |
|---|---|---|
| Fed hike odds, July meeting | 16.6% (from 41.7% Monday) — CME FedWatch | STRONGLY POSITIVE |
| Fed hike odds, September | ~50% | NEGATIVE |
| June CPI y/y | 3.5% (vs 4.2% May, 3.8% forecast) | POSITIVE |
| June core CPI | 2.6% | POSITIVE |
| June CPI m/m | −0.4% — first decline since 2020 | STRONGLY POSITIVE |
| June PPI | Unexpected decline; core +0.2% (soft) | POSITIVE |
| Fed Chair Warsh testimony | Committed to price stability; no dovish pivot | NEGATIVE |
| ETF flows | Outflows on high real yields | NEGATIVE |
| Analyst technical ratings | Investing.com daily/weekly: Strong Sell | NEGATIVE |
| Sell-side targets | JPM $6,000/oz Q4-26; TE model $4,204 Q3-26 | POSITIVE (long-horizon) |
| Central bank demand | Cooled from 2025 pace but continuing | MILDLY POSITIVE |

Aggregate sentiment tilt: +0.35. The composition matters more than the number. The positive side is concentrated and recent — a genuine CPI shock (first monthly decline in six years), a PPI miss confirming it, and a collapse in July hike odds from 41.7% to 16.6% inside 48 hours. That is a real repricing, not a headline. The negative side is structural and persistent: Warsh explicitly declined to validate the dovish read in his first congressional testimony, September hike odds remain a coin-flip, real yields are still high enough to drive ETF redemptions, and the aggregated technical ratings sit at Strong Sell on both daily and weekly.
The honest characterisation is that sentiment has improved sharply from a low base without changing regime. Traders have priced out July, not the cycle. COT positioning data was not retrievable for this run and is excluded rather than estimated.
# §15 Event Calendar — Next 5 Sessions

| **Date** | **Event** | **Directional risk to Gold** |
|---|---|---|
| 15-Jul (done) | June PPI + Fed Beige Book | Resolved — PPI declined, gold supported |
| 16-Jul | Philadelphia Fed Manufacturing Index | Moderate — weak print = dovish = gold-positive |
| 16-Jul | Initial jobless claims | Moderate — a soft labour read compounds the CPI/PPI dovish case |
| 17-Jul | Univ. of Michigan inflation expectations | HIGH — the live risk. A hot expectations print re-arms the Sept hike case and directly hits gold |
| Ongoing | US–Iran strikes / Strait of Hormuz blockade | Two-sided — safe-haven bid vs energy-inflation-driven hawkishness |
| Ongoing | Central bank purchases (PBoC, RBI) | Slow-burn support; PBoC reserves 2,313.46t (Mar-26), still accumulating |

The 16-Jul session itself is data-light — Philly Fed and claims are second-tier. The asymmetry sits on 17-Jul with the Michigan inflation-expectations print. Gold's entire two-day rally is built on the premise that inflation is decelerating; a hot expectations number is the single cleanest way to falsify that premise, and it lands the session after this report's horizon. Trades held into 17-Jul carry event risk that the 16-Jul technical picture does not price.
# §16 Scenarios — Next 5 Trading Days

| **Scenario** | **Probability** | **Path** | **Trigger** | **Confidence** |
|---|---|---|---|---|
| Base — range persistence | 50% | Chop 4,007–4,132; no resolution | Data stays mixed; Michigan in line | M |
| Bull — dovish extension | 28% | Break 4,109.62 → 4,132 → 4,186 | Soft Philly Fed + soft Michigan; USDX breaks 100.25 | M |
| Bear — structural resumption | 22% | Break 3,985.76 → 3,951 → 3,894 | Hot Michigan; Sept hike odds >60%; USDX reclaims 100.835 | M |

The base case is deliberately the largest. KER of 0.117 says this market is not trending, ATR is contracting session-on-session, and the range boundaries at 4,132 and 3,985.76 have both been tested and held within the last five sessions. Ranges that have proven both edges tend to require an exogenous catalyst to break, and the only catalyst of that magnitude in the window (Michigan) falls on 17-Jul.
The bull case is given the edge over the bear case for the 5-day horizon on a specific mechanism: the dollar. USDX below both its 50- and 200-period MAs with a daily sell signal is the most technically damaged of any instrument in the counter set, and gold's inverse-dollar link is its most reliable transmission channel. The bear case is smaller in probability but larger in magnitude — a break of 3,985.76 has no meaningful structural support until 3,951.68, and the 3,900 zone below that is where multiple sources flag risk of deeper correction.
# §17 Forecast

| **Horizon** | **Central estimate** | **Range** | **Confidence** |
|---|---|---|---|
| 16-Jul-2026 close | 4,075 | 4,020 – 4,130 | M |
| 5 sessions (22-Jul-2026) | 4,085 | 3,950 – 4,190 | L |

The 5-day central estimate of 4,085 sits 15 points above spot and is, in substance, a call for continued consolidation with a marginal upward drift. Confidence is LOW at the 5-day horizon and MEDIUM at the next-session horizon, and that gap is the honest expression of the Michigan risk on 17-Jul. Directionally the forecast leans mildly constructive; structurally it does not contradict the bearish medium regime, because a 15-point drift inside a 240-point range from the 10-session swing high is consolidation, not reversal.
*Conflict check against §21a: the forecast leans mildly LONG; the direction score is +0.05, i.e. effectively NEUTRAL but positive-signed. These are consistent in sign. No conflict flag raised.*

# §18 Macro Narrative
Real yields and the Fed. This remains the dominant channel. The US 10Y sits at 4.587%, easing marginally, with fed funds at 3.75% and CPI at 3.5% — a real policy rate near zero but a real long-yield still meaningfully positive. That is the arithmetic behind the ETF outflows: a non-yielding asset competes badly against a positive real long rate. June's CPI and PPI both undershot, which lowers the near-term hike premium (July odds 16.6%), but Warsh's refusal to signal a dovish pivot means the September question (≈50%) stays open. Cross-referencing §10: the 10Y easing is a mild gold positive and does not contradict the USDX read.
Dollar liquidity. USDX at ~100.76–100.90, off early-July highs near 101.39, below its 50- and 200-period MAs, daily signal Sell. Mechanism for gold: direct and inverse — a weaker dollar mechanically raises the USD price of a globally-priced hard asset and lowers the hurdle for non-US buyers. This is the single most gold-supportive input on the board and is the reason the composite score is positive rather than negative.
Energy and inflation. WTI $79.87 (+2.22%) and Brent $85.28 (+2.38%) at one-month highs on renewed US strikes against Iran and the reinstated naval blockade near the Strait of Hormuz, with vessel transits reportedly down more than half week-on-week. This is genuinely two-sided for gold and must not be resolved silently: energy-driven inflation strengthens the hard-asset hedge case (positive) while simultaneously raising the odds the Fed must respond with hikes (negative). Shearer's framing — that hike worries have pushed gold to the back burner for most investors — captures why the second effect has been dominating the first.
Positioning and flows. ETF outflows on high real yields; central bank demand cooled from its 2025 pace but not stopped, with PBoC at 2,313.46t as of Mar-26 (up from 2,306.30t). COT data unavailable this run. VIX at 15.88 (−3.75%) — a benign risk backdrop, which is a mild safe-haven negative.
*Contradiction flag (mandatory per M4 §12): the macro narrative here is net constructive (dollar down, real yields easing, energy inflation live), while §10's equity counters read risk-on and §9's structural regime reads firmly bearish. These are not reconciled. The report carries the contradiction forward into the near-zero direction score rather than resolving it by preference.*
# §19 Key Risks
- Michigan inflation expectations (17-Jul) prints hot — re-arms the September hike case, breaks the entire dovish premise of the current bounce. Highest-probability single source of a bearish gap.
- Warsh or another FOMC member delivers explicit hawkish guidance intra-session — USDX reclaims 100.835, gold loses 4,007.50 support.
- Strait of Hormuz escalates to actual supply interruption — two-sided, but the first move is almost certainly a safe-haven spike, stopping shorts before the inflation-hawkish second-order effect arrives.
- Break below 3,985.76 with conviction — the twice-defended low fails, opening 3,951.68 and then the 3,900 zone where multiple sources flag deeper-correction risk.
- ATR(14) is estimated at 78.50, not computed from a full tick series. Every stop distance and target below scales off it. A 5% error moves R by ±4 points.
- All OHLC extremes and therefore all pivots are composite across venues. Levels are indicative to roughly ±$5.
- RSI(2) is unavailable and excluded — the short-tech input is running on structural read alone, degrading the highest-weighted axis in the model (0.25).
# §20 Agent Log

| **#** | **Entry** |
|---|---|
| 1 | [AS_OF_DATE] overridden from M1 value 29-Apr-2026 to 16-Jul-2026 per user instruction. |
| 2 | [DAILY_OPEN_ANCHOR] override instructed. M1 value = 00:00 UK. Permitted values under PATCHES P5 are 00:00 UK / 07:00 UK only. P6 requires the anchor to match the asset's trading session; gold trades 23+ hours and 07:00 UK is mid-London-session, not a reset. Anchor explicitly re-affirmed and locked at 00:00 UK. Action logged as an override event with no net value change. |
| 3 | Corroboration posture set to LENIENT per explicit user instruction. Strategies NOT suppressed despite PARTIAL corroboration on price sources. Lenient-corroboration flag carried on all three trade cards. |
| 4 | LBMA AM/PM Fix and discrete CME GC=F 15-Jul settlement not independently retrievable. TradingEconomics OTC benchmark and TradingView composite substituted as proxies. Benchmark set degraded from 6 specified to 4 obtained + 2 proxied; [MINIMUM_SOURCE_COUNT] of 6 still met on total independent sources (8). |
| 5 | RSI(2) unavailable from all consulted sources and not reconstructible from composite OHLC. Excluded from §8 rather than fabricated. [W_SHORT_TECH] (0.25) is running on M3 §2a structural read alone. |
| 6 | ATR(14) estimated at 78.50 (anchored to observed ATR(5) = 84.16 and the prevailing ~1.9% daily-range regime). Not computed from a full 14-session series. Confidence ±5%. |
| 7 | COT positioning data not retrievable. Excluded from §14 sentiment aggregate rather than estimated. |
| 8 | Fib swing anchor: default [FIB_RANGE_DAYS] = 4 produced magnitude 1.86 × ATR, below the 2 × ATR threshold. Lookback extended per M5 §4b to 10 sessions; qualifying swing found at 4.13 × ATR. Lookback actually used = 10. |
| 9 | Direction score = +0.05, below [CONVICTION_THRESHOLD] = 0.25. Trade 1 SUPPRESSED per M5 §5.1. Trades 2 and 3 produce regardless — they are regime-driven, not conviction-gated. A strategy is therefore delivered as instructed. |
| 10 | Direction-scoring weights at v2.1 defaults. No tuning applied. Forward-test session 1 of 20 — weights locked. |
| 11 | 5-session OHLC reconstructed from composite multi-source reads. Rows 09-Jul and 10-Jul flagged SINGLE-SOURCE-INDICATIVE. All derived pivots inherit the flag per M5 §4a. |

# §21 Strategy Recommendations (M5 Integration)
## §21a Directional Conviction

| **Axis** | **Weight** | **Signal** | **Contribution** |
|---|---|---|---|
| Short-term technical (§7–8) | 0.25 | +0.30 | +0.075 |
| Medium-term regime (§9) | 0.20 | −0.55 | −0.110 |
| VOLator (§11) | 0.10 | −0.20 | −0.020 |
| Kaufman KER (§11) | 0.15 | −0.10 | −0.015 |
| Sentiment (§14) | 0.15 | +0.35 | +0.053 |
| Cross-asset (§10) | 0.15 | +0.45 | +0.068 |
| COMPOSITE | 1.00 | — | +0.05 |

Direction: NEUTRAL (score +0.05, positive-signed). Weights basis: defaults.
The score of +0.05 is not a weak signal — it is the accurate measurement of a genuinely balanced book. Three of the six axes are positive and three are negative, and the two largest single contributors point in opposite directions: the medium-term structural regime at −0.110 and the cross-asset dollar read at +0.068, with sentiment at +0.053 close behind. The three highest-weighted contributing signals are the medium-term regime (§9, −0.110), the short-term technical bias (§7–8, +0.075) and cross-asset confirmation (§10, +0.068).
|0.05| < [CONVICTION_THRESHOLD] 0.25. Trade 1 is SUPPRESSED per M5 §5.1. This is the model working correctly: it declines to take a directional bet in a market with KER of 0.117, contradictory drivers, and a binary event two sessions out. Trades 2 and 3 are regime-driven and produce regardless — they are constructed below and are the actionable output of this report.
*Conflict flag: §17 Forecast leans mildly LONG; the direction score is NEUTRAL but positive-signed. Consistent in sign, no material conflict. Neither output has been changed.*
## §21b Trade Cards
**TRADE 1 — Daily Directional · SUPPRESSED**

| **Element** | **Value** |
|---|---|
| Status | SUPPRESSED — conviction threshold not met |
| Direction score | +0.05 vs threshold 0.25 |
| Rule invoked | M5 §5.1 — 'Suppressed if §2 score is NEUTRAL' |
| Reference construction (not actionable) | LONG @ 4,070.00 · SL 3,988.20 · R = 81.80 (8,180 ticks) · TP1 4,151.80 · TP2 4,233.59 · TP3 4,305.50 |
| Reference caveats | 'wide stop (R > 1 ATR)' would have flagged — R 81.80 vs ATR 78.50 |
| Note | Shown for audit transparency only. Do not execute. Trades 2 and 3 below are the actionable cards. |

**TRADE 2 — Regime-Aware Pivot · ACTIVE**

| **Element** | **Value** |
|---|---|
| Regime input | RANGING (KER 0.117, below 0.13 trend threshold; upper sub-band) |
| Expression | Fade the range edges. In a ranging regime the pivot trade is mean-reversion, not breakout. |
| Structure | Two independent legs. Both may be live simultaneously — [MAX_SIMULTANEOUS_LONG_SHORT] = YES. |

**Leg A — SHORT from resistance**

| **Element** | **Price (USD/oz)** | **Native (ticks)** | **Note** |
|---|---|---|---|
| Entry (limit) | 4,116.25 | — | R1.5 · confluence with published R 4,114.01 |
| Stop loss | 4,151.88 | 3,563 ticks | R2 4,131.67 + 0.25 × ATR (19.63) → 4,151.30, rounded to swing-high cover |
| R (risk) | 35.63 | 3,563 | 0.45 × ATR — tight, structurally justified |
| TP1 (Unit 1) | 4,080.62 | 3,563 | 1 × R |
| TP2 (Unit 2) | 4,045.00 | 7,125 | 2 × R · near pivot 4,059.17 / fib 50% |
| TP3 (Unit 3, runner) | 4,009.38 | 10,688 | 3 × R · at S1.5 4,007.50 confluence |
| Tranche management | 3 equal units | — | U1 at TP1; U2 at TP2; on U2 fill, U3 SL → entry − 0.2 × R = 4,109.12 |
| Thesis invalidation | 4,151.88 | — | Coincides with SL. A close above 4,132 breaks the range top and voids the fade. |

**Leg B — LONG from support**

| **Element** | **Price (USD/oz)** | **Native (ticks)** | **Note** |
|---|---|---|---|
| Entry (limit) | 4,007.50 | — | S1.5 · confluence with published S 4,007.83 |
| Stop loss | 3,966.13 | 4,137 ticks | S2 3,986.67 − 0.25 × ATR (19.63) → 3,967.04, set below twice-defended low 3,985.76 |
| R (risk) | 41.37 | 4,137 | 0.53 × ATR |
| TP1 (Unit 1) | 4,048.87 | 4,137 | 1 × R |
| TP2 (Unit 2) | 4,090.24 | 8,274 | 2 × R · at 15-Jul session high |
| TP3 (Unit 3, runner) | 4,131.61 | 12,411 | 3 × R · at R2 / 5d swing high 4,132.00 |
| Tranche management | 3 equal units | — | U1 at TP1; U2 at TP2; on U2 fill, U3 SL → entry + 0.2 × R = 4,015.77 |
| Thesis invalidation | 3,966.13 | — | Coincides with SL. Loss of 3,985.76 opens 3,951.68 — range thesis dead. |

Trade 2 rationale. This is the highest-quality setup in the report and it is not a directional call. The range edges are exceptionally well-corroborated: S1.5 at 4,007.50 lands within 0.33 of an independently published support at 4,007.83, and R1.5 at 4,116.25 sits within 2.24 of a published resistance at 4,114.01. Both fade legs risk under 0.55 × ATR to target 3 × R at the opposite range boundary — a structurally favourable geometry that exists precisely because KER is telling us this market reverts rather than trends. Leg B carries the better location: it sits above a low defended twice within four cents, with the dollar broken below its own moving averages providing tailwind.

**TRADE 3 — Regime-Driven Complex · FORK: 3C (Breakout)**

| **Element** | **Value** |
|---|---|
| Fork selection | 3C — Range Breakout. Regime is RANGING (KER 0.117), so 3A/3B trend-continuation forks do not apply. 3C's anchor is the 25-day range boundary, not the fib swing. |
| Range boundaries (M5 §4d) | swing_high_25d ≈ 4,310.00 · swing_low_25d = 3,985.76 |
| Confirmed-break requirement | Daily close beyond boundary by ≥ 0.25 × ATR(14) = 19.63 |
| Eligibility | CONDITIONAL — no confirming close exists at time of writing. The trade is armed, not live. |

| **Direction** | **Trigger (confirmed daily close)** | **Entry** | **Stop loss** | **TP1** | **TP2** | **TP3** |
|---|---|---|---|---|---|---|
| Upside | Close > 4,329.63 | 4,329.63 | 4,251.13 (1 × ATR) | 4,408.13 | 4,486.63 | 4,565.13 |
| Downside | Close < 3,966.13 | 3,966.13 | 4,044.63 (1 × ATR) | 3,887.63 | 3,809.13 | 3,730.63 |

| **Element** | **Value** |
|---|---|
| R (both directions) | 78.50 (7,850 ticks) = 1 × ATR(14) |
| Tranche management | 3 equal units. U1 at TP1 (1 × R); U2 at TP2 (2 × R); on U2 fill, U3 SL → entry ± 0.2 × R (15.70). |
| Thesis invalidation | Re-entry into the prior range — i.e. a close back inside 3,985.76 – 4,310.00 voids the breakout regardless of stop. |
| Near-term realism | The downside trigger at 3,966.13 sits 104 points below spot; the upside trigger at 4,329.63 sits 260 points above. Neither is a plausible 16-Jul close (ATR 78.50). This card is a 5-day contingency, most likely armed by the 17-Jul Michigan print. |

Trade 3 rationale. 3C is the correct fork and it is honest about being conditional. The engine will not manufacture a breakout in a market with 11.7% efficiency. What 3C does is pre-commit the response: if Michigan re-arms the September hike case and gold loses 3,985.76 on a close, the downside leg fires into a level with no structural support until 3,951.68 and a documented risk zone at 3,900. The asymmetry in trigger distance — 104 points down versus 260 points up — is itself informative: the range's floor is far closer than its ceiling, which is the geometry of a bear-trend consolidation.
## §21c No-Leakage Backtest — 5 Sessions
[BACKTEST_LOOKBACK_DAYS] = 5. Each session replayed using only information available at that session's 00:00 UK anchor. No forward data used in any signal construction.

| **Session** | **Anchor entry** | **Signal state** | **Outcome** | **R result** |
|---|---|---|---|---|
| 09-Jul | 4,105.00 | Trade 1 LONG (score est. +0.31) | Closed 4,088.00 — adverse | −0.4R |
| 10-Jul | 4,088.00 | Trade 1 SHORT (score est. −0.28) | Closed 4,044.00 — favourable | +0.9R |
| 13-Jul | 4,044.00 | Trade 1 SHORT (score est. −0.34) | Closed 4,001.79 — favourable, TP1 hit | +1.0R |
| 14-Jul | 4,001.13 | SUPPRESSED (score est. +0.09) | Would have been LONG; closed 4,053.56 | 0.0R (missed +1.3R) |
| 15-Jul | 4,052.96 | SUPPRESSED (score est. +0.12) | Would have been LONG; closed 4,070.00 | 0.0R (missed +0.2R) |

| **Metric** | **Value** |
|---|---|
| Sessions traded | 3 of 5 (2 suppressed on conviction) |
| Wins / losses | 2 / 1 |
| Cumulative R (traded only) | +1.5R |
| Win rate (traded) | 66.7% |
| Suppression cost | −1.5R of forgone gain across 2 suppressed sessions |
| Net including forgone | +1.5R realised vs +3.0R theoretical maximum |

*Backtest caveat: signal states for prior sessions are reconstructed estimates, not logged live outputs — this is forward-test session 1, so no prior session logs exist. Scores are re-derived from the OHLC and the macro state as it stood at each anchor. Treat the R figures as indicative of model behaviour, not as an audited track record.*
## §21d What Is Working
- Conviction gating cost 1.5R of forgone gain across the two suppressed sessions (14-Jul and 15-Jul), both of which would have been profitable longs. Two observations is not a sample. But the direction of the error is worth logging: the gate is currently suppressing on the same low-conviction readings that immediately preceded the CPI-driven bounce. If this pattern repeats across sessions 3–8, the threshold — not the weights — is the parameter to examine at session 20.
- Short-side Trade 1 signals worked (10-Jul +0.9R, 13-Jul +1.0R) and the long-side signal did not (09-Jul −0.4R). That is consistent with the bearish medium regime dominating the sample and argues the model's [W_MEDIUM_REGIME] axis is correctly signed.
- Pivot-level corroboration is the standout technical positive this session: mechanically derived R1.5 and S1.5 landed within 2.24 and 0.33 respectively of independently published levels. That confluence is what makes Trade 2's geometry defensible despite the composite-OHLC caveat.
- Weights remain at v2.1 defaults and locked. 19 sessions remain before any tuning is permitted under the §H.3 lock rule.

*Disclaimer. This report is a forward-test output of an automated analytical framework and is provided for research and risk-review purposes. It is not investment advice, and it is not a recommendation to buy or sell any instrument. Price data is composite across venues and indicative; ATR(14), RSI(2), COT positioning and LBMA/GC=F benchmark values were unavailable or estimated as documented in §20. Corroboration posture was set to LENIENT at the user's explicit instruction, meaning trade cards were produced despite only PARTIAL price-source corroboration — the resulting levels carry correspondingly wider uncertainty than a fully corroborated run. Anyone acting on this material does so at their own risk and should size positions accordingly.*
Modular Prompt Architecture v2.1 · M1 Gold (Spot) instance · Report date 16 July 2026 · Forward-test session 1 of 20
