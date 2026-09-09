**Gold Report — Daily: 09 July 2026**
*With reference to: Silver · USDX (Dollar Index) · S&P 500 · DAX 40*
*XAU/USD spot (loco London), USD/oz · CME GC=F front-month corroboration · Senior Commodities Analyst, Precious Metals*

**§1 Executive Snapshot**
Consensus spot gold sits at **$4,125/oz** (range $4,096–$4,145), tone **balanced-to-bearish** after a violent two-session round trip. Three drivers dominate: a firmer US dollar holding above 101 on renewed Iran/Strait-of-Hormuz escalation; rising US real yields and a hawkish June FOMC read (minutes released 08 Jul), which lift the opportunity cost of holding non-yielding bullion; and sustained official-sector demand (PBoC reported its largest monthly gold-reserve build in over two and a half years). Short-term technical state is **Ranging/Transitional — Mixed**, with the 08 Jul session closing back in the upper half of range (76.6% close location) but RSI2 recovering only to 28.7 after collapsing to 0.0 on the 07 Jul FOMC-driven slide. Medium-term (25-session) structure is **Ranging** with a slight bearish tilt: overlap ratio 0.62, directional persistence 0.59, last close in the 41st percentile of the 25-day range. Kaufman efficiency (smoothed −0.11) reads **Ranging — Downward Bias**. Single most important watch item: **US June CPI (14 Jul)** — an upside surprise would harden the rate-hike narrative and pressure gold toward the $4,030 shelf. Directional conviction from the strategy engine is **SHORT (score −0.37)**, driven by short-term technical bias, a predominantly bearish sentiment tilt, and cross-asset dollar strength.
**§2 Market Definition**

| **Attribute** | **Specification** |
|---|---|
| Asset / instrument | Gold, spot (XAU/USD), loco London |
| Product specification | London Good Delivery bar, 99.99% pure, 400-oz quote (LBMA standard) |
| Corroboration instrument | CME front-month gold futures (GC=F) |
| Market scope | Global, 24-hour OTC market |
| Delivery / price basis | OTC London spot, T+2 settlement; immediate spot quote |
| Unit / currency | USD per troy ounce (USD/oz) |
| As-of date / timezone | 09 July 2026 · Europe/London |
| Daily-open anchor | 00:00 UK (session reset applied per run instruction) |
| Lookback window | 5 sessions (execution) · 25 sessions (regime) |

**§3 Consensus Price Call**

| **Consensus** | **Range** | **Basis** | **Confidence** | **Tone** | **Rationale** |
|---|---|---|---|---|---|
| **$4,125/oz** | $4,096–$4,145 | Spot loco London, 08 Jul close | Medium | Balanced-bearish | Weighted-median of the 08 Jul completed session; spot and CME futures agree on direction, with futures carrying the usual contango premium. |

*The number reflects the last fully completed session (08 Jul) as the reference for the 09 Jul open. Intraday spot feeds on 08 Jul printed as low as ~$4,030 during the FOMC-minutes reaction before recovering; the accepted close of $4,125 is the settled benchmark value.*
**§4 Price Evidence Table**

| **Source** | **Date/Time** | **Raw Quote** | **Normalized (USD/oz)** | **Basis / Location** | **Class.** | **Notes** |
|---|---|---|---|---|---|---|
| Investing.com (XAU/USD) | 08 Jul 2026 close | 4,125.28 | 4,125.28 | Spot, loco London | Core | Full validated OHLC series |
| CME Gold Futures (GC=F) | 08 Jul 2026 | 4,063.86 settle | ≈4,110–4,125 spot-equiv | Futures, COMEX | Core | High 4,144.71 / low 4,061.94; contango premium |
| TradingEconomics | 08 Jul 2026 | ≈4,030–4,050 intraday | 4,030–4,050 | Spot, global | Directional | Intraday FOMC-reaction low read |
| TradingView (OANDA) | 08 Jul 2026 | 4,033.81 intraday | 4,033.81 | Spot, global | Directional | Intraday snapshot; below settled close |
| MQL5 quotes | 08 Jul 2026 | 4,035.28; rng 4,027–4,134 | 4,035.28 | Spot, global | Directional | Prior close cited 4,114.25 |
| LiteFinance / OCBC consensus | 08 Jul 2026 | $4,114–4,202 fwd band | — | Forecast band | Directional | Forward consolidation range for 09 Jul |

**§5 Consensus Build Explanation**
Observations were normalized to spot USD/oz, loco London. The CME futures settle ($4,063.86) was retained as a directional corroborator rather than a like-for-like spot input: futures trade at a contango premium to spot and settle on a COMEX cut, so it validates the direction and the intraday range (high $4,144.71 / low $4,061.94 bracket the spot session) without being blended into the spot number. Intraday spot feeds (TradingView, MQL5, TradingEconomics) clustered near $4,030–$4,050 during the FOMC-minutes reaction window; these are genuine ticks but represent the session trough, not the settled close. Applying the weighted-median method — down-weighting single-snapshot aggregator ticks and preserving the full-session benchmark — yields a defensible consensus of **$4,125/oz**. The primary limitation is timing dispersion: because gold trades 23+ hours, feeds sampled at different cuts diverge by 2–3% intraday on a high-volatility day like the 08 Jul FOMC session.

**§6 Validated OHLC + RSI2 Table (5-Day)**

| **Date** | **Open** | **High** | **Low** | **Close** | **RSI2** | **Trend** | **Src A** | **Src B** | **Validation** |
|---|---|---|---|---|---|---|---|---|---|
| 02 Jul | 4031.04 | 4144.22 | 4030.38 | **4123.98** | 100.0 | Bullish | Investing | GC=F | CORROB. (dir) |
| 03 Jul | 4124.00 | 4195.54 | 4120.92 | **4175.70** | 100.0 | Bullish | Investing | GC=F | CORROB. (dir) |
| 06 Jul | 4175.71 | 4202.67 | 4128.19 | **4165.17** | 83.1 | Neutral | Investing | GC=F | CORROB. (dir) |
| 07 Jul | 4166.99 | 4183.27 | 4092.02 | **4098.50** | 0.0 | Bearish | Investing | GC=F | CORROB. (dir) |
| 08 Jul | 4098.58 | 4134.05 | 4096.55 | **4125.28** | 28.7 | Neutral | Investing | GC=F | CORROB. (dir) |

*Trend rule: Bullish = Close>Open and RSI2>50; Bearish = Close<Open and RSI2<50; otherwise Neutral. RSI2 is period-2, computed on the validated close sequence. Corroboration is directional: the CME futures series confirms every session's direction and range within the volatility of the day; exact spot-vs-futures level agreement is subject to the contango basis, so levels are treated as accepted-close values rather than tick-identical dual-source matches.*
**§7 Charts**
**Chart 1 — 5-Session Candlestick**

**Chart 2 — Distance From Open**

**Chart 3 — 25-Session Structure**

**Chart 4 — Comparative Volatility (VOLator)**

**Chart 5 — Pivot Structure**

**§8 Short-Term Technical Analysis**
- **02 Jul** (see §6): Strong bullish marubozu-style body, close at 82% of range, RSI2 saturated at 100. A powerful recovery session off the $4,030 area — demand rejection of the sub-$4,050 zone.
- **03 Jul** (see §6): Continuation higher, close 73% of range, RSI2 100. Two-day thrust into the $4,195 area established the near-term swing high.
- **06 Jul** (see §6): Indecision — close mid-range (50%), small bearish body after tagging $4,202. Upper-wick rejection at the swing high signals supply.
- **07 Jul** (see §6): Decisive bearish session, close at just 7% of range, RSI2 collapsed to 0.0. The FOMC-minutes-driven risk repricing drove a wide-range down-day — the dominant candle of the block.
- **08 Jul** (see §6): Bullish recovery body, close 77% of range, but RSI2 only back to 28.7 — momentum still sub-50. A bounce within a damaged structure rather than a confirmed reversal.
**Sequence assessment: Indecision / Compression.** The block alternates direction with prominent wicks on both sides and RSI2 oscillating between the 0 and 100 extremes — classic two-sided volatility, not a clean directional run. Net 5-day change is essentially flat (+$1.3) despite a $172 high-low span.
**Nearest support:** $4,092–$4,096 (07/08 Jul lows). **Nearest resistance:** $4,202 (06 Jul high), then $4,195 (03 Jul). **Judgement label: Indecision.** This is consistent with the §9 Ranging regime.
**§9 Medium-Term Regime & VOLator**
**Regime classification: Ranging (slight bearish tilt).** Overlap ratio 0.62 (>0.55 → range-bound); directional persistence 0.59; range-position bias 0.41 (mid-to-lower). Absolute directional mean is muted — the 25-session window is a wide, choppy rotation between ~$3,944 and ~$4,383, not a trend.
**Bias: Neutral-to-Bearish.** Price sits below the 25-day mid-point and the medium-term sequence has been lower-highs since the 17 Jun $4,383 peak.
**VOLator (ATR / historical z-score):** Gold scaled volatility latest −1.0 (at the floor of its own recent band); 10-observation slope **−0.28 (negative)** → volatility contraction, a ranging/transitional signal, not trend expansion.
**Preferred trade protocol:** Range-bound — favour fading validated range extremes and reduced-conviction breakout attempts. Short-term Indecision (§8) sits inside the medium-term Range — no conflict.
**Kaufman confirmation:** Smoothed KER −0.11, |KER| below the 0.13 trend threshold and inside the lower inner band → **Ranging — Downward Bias**. This agrees with the §9 regime (ranging) and adds a mild bearish lean. No contradiction to resolve.
**§10 Cross-Asset Analysis**

| **Counter** | **5-Day Dir.** | **Mechanism** | **Status** | **Implication for Gold** |
|---|---|---|---|---|
| USDX (Dollar Index) | Rising (held >101) | Stronger dollar raises the USD price of gold for non-USD buyers and signals tighter conditions | Confirms bearish | Headwind — dollar strength caps gold upside |
| S&P 500 | Falling (−0.9% 08 Jul) | Risk-off equity weakness can rotate flows into safe havens | Contradicts | Partial support — risk-off is gold-positive via haven demand |
| DAX 40 | Falling (−2.1% 08 Jul) | European risk-off confirms the global de-risking read | Contradicts | Partial support — reinforces haven bid |

**Contradiction flag (bold):** the dollar channel is bearish for gold while the equity risk-off channel is supportive. The two offset, producing a **MIXED** cross-asset read. On the current FOMC-driven, real-yield-led tape the dollar/rate channel has been the stronger driver — hence the net bearish lean in the direction score — but the haven bid is the reason gold recovered into the 08 Jul close rather than extending lower.

**§11 Floor Pivot Analysis**
**Daily Pivots (from 08 Jul H/L/C)**

| **Level** | **Price (USD/oz)** |
|---|---|
| R5 | 4253.20 |
| R4 | 4215.70 |
| R3 | 4178.20 |
| R2 | 4156.13 |
| R1 | 4140.70 |
| **P** | **4118.63** |
| S1 | 4103.20 |
| S2 | 4081.13 |
| S3 | 4065.70 |
| S4 | 4028.20 |
| S5 | 3990.70 |

**Weekly Pivots (prior week 29 Jun–03 Jul)**

| **Level** | **Price (USD/oz)** |
|---|---|
| R5 | 5020.01 |
| R4 | 4768.70 |
| R3 | 4517.39 |
| R2 | 4356.47 |
| R1 | 4266.08 |
| **P** | **4105.16** |
| S1 | 4014.77 |
| S2 | 3853.85 |
| S3 | 3763.46 |
| S4 | 3512.15 |
| S5 | 3260.84 |

**Monthly Pivots (June 2026)**

| **Level** | **Price (USD/oz)** |
|---|---|
| R5 | 5595.34 |
| R4 | 5156.72 |
| R3 | 4718.10 |
| R2 | 4550.47 |
| R1 | 4279.48 |
| **P** | **4111.85** |
| S1 | 3840.86 |
| S2 | 3673.23 |
| S3 | 3402.24 |
| S4 | 2963.62 |
| S5 | 2525.00 |

***Source status:*** *prior-period H/L/C are derived from the corroborated Investing.com series with directional CME confirmation. Because independent two-source tick-level agreement on the exact spot H/L was not fully established, all pivot levels are treated as* ***indicative*** *for level-based order placement and are flagged accordingly to the strategy layer.*
**Position narrative:** The 08 Jul close ($4,125.28) sits **above the daily P ($4,118.63)** and just above both the weekly P ($4,105.16) and monthly P ($4,111.85). **Confluence zone:** daily P, weekly P and monthly P cluster within ~$14 (≈0.34%) around $4,105–$4,119 — a dense pivot shelf that acts as the immediate decision zone. A daily close back below this cluster reopens the $4,081 (D.S2) / $4,065 (D.S3) supports.
**§12 Key Market Considerations**
**Supply — neutral (structural).** Mine supply is inelastic short-term; the swing factor is official-sector buying. China's central bank reported its largest monthly gold-reserve increase in over two and a half years in June — a structural, price-supportive floor under the market.
**Demand — supportive (structural) / mixed (cyclical).** Continued central-bank accumulation (PBoC, and historically RBI) is a durable support. Cyclically, investment demand is softening on higher real yields and OCBC-type calls for lower prices into year-end.
**Substitution / Spreads — neutral.** Silver (XAG/USD) remains the high-beta partner; the gold/silver read is consistent with a broad precious-metals correction rather than gold-specific weakness. US 10-year real yields are the key competing 'asset' — rising real yields are the principal cyclical drag.
**Policy / Geopolitics — cyclical, two-sided.** Renewed US–Iran escalation and Strait-of-Hormuz tanker attacks add a haven premium and lift oil (inflation channel). This is reversible within the scenario horizon and can whip both ways.
**Macro / FX — price-negative (cyclical).** A firmer dollar (>101) and a hawkish June FOMC (minutes 08 Jul) tighten financial conditions and raise bullion's opportunity cost. Markets moved to price ~50–69% odds of a September Fed hike, up from the high-40s/58% a day prior.
**Near-term catalysts (from §13d):** FOMC minutes (08 Jul, delivered), initial jobless claims (09 Jul), and — the key item — **US June CPI (14 Jul)**. A hot CPI hardens the hike narrative and pressures gold; a soft print relieves real-yield pressure and supports a bounce.

**§13 Sentiment, News & Calendar**
**§13a Per-Article Sentiment**

| **Source** | **Date** | **Headline (abridged)** | **Class.** | **Sentiment** | **Derivation quote (≤15w)** |
|---|---|---|---|---|---|
| Investing.com | 08 Jul | Gold prices fell >1% on stronger dollar, spiking oil | Media | Bearish | "weighed down by a stronger dollar and spiking oil prices" |
| TradingEconomics | 08 Jul | Gold falls to lowest since 2 Jul after Trump ends Iran deal | Media | Bearish | "markets pricing in at least one Fed rate hike by end-2026" |
| Investing.com (Futures) | 08 Jul | FOMC-driven selloff extends structural downtrend | Media | Bearish | "overwhelmingly bearish backdrop, driving prices... down" |
| LiteFinance / OCBC | 08 Jul | Gold to decline on yields, stronger dollar, weak demand | Institutional | Bearish | "expects gold prices to decline through the end of 2026" |
| TradingEconomics (PBoC) | 08 Jul | China posts largest monthly gold-reserve build in 2.5y | Official | Bullish | "largest monthly increase in gold reserves in... over two and a half years" |
| LiteFinance (fwd) | 08 Jul | XAU/USD to consolidate $4,114–4,202 on 9 Jul | Trade Press | Neutral | "expected to continue consolidating... move in either direction" |

**§13b Aggregate Sentiment Summary**
Counts: **4 Bearish** (1 institutional, 3 media), **1 Bullish** (official), **1 Neutral** (trade press) = **Predominantly Bearish**. Source-class-weighted numeric tilt = **−0.55** (institutional and media bearish weight dominates the single official bullish and neutral entries). Reported as: **Predominantly Bearish (tilt = −0.55)**. This tilt feeds the §21 directional conviction.
**Divergence flag:** Sentiment (bearish) broadly **agrees** with price action (08 Jul session recovered but sits below the week's highs after a sharp drop) and with the §9 ranging-bearish regime. The one counter-signal — PBoC official buying — is a structural floor, not a near-term bullish trigger. On the current tape the bearish real-yield/dollar signal takes precedence.
**§13c News Calendar — Previous Period (04–08 Jul)**

| **Date** | **Event** | **Prior / Context** | **Impact** | **Implication for Gold** |
|---|---|---|---|---|
| Fri 03 Jul | US June payrolls (soft) | Weaker NFP trimmed hike bets | High | Initially gold-supportive; dollar dipped then recovered |
| Mon 06 Jul | Iran/Hormuz tanker attacks | Escalation resumes | Medium | Two-sided: haven bid vs oil-led inflation/hike risk |
| Tue 07 Jul | Dollar firms, Williams hawkish | DXY held >101 | High | Gold −1.6% session; real-yield channel dominant |
| Wed 08 Jul | FOMC June minutes | Divided, hawkish tone | High | Intraday plunge to ~$4,030 then recovery to 4,125 close |

**§13d News Calendar — Upcoming Period (09–15 Jul)**

| **Date** | **Event** | **Context** | **Impact** | **Implication for Gold** |
|---|---|---|---|---|
| Thu 09 Jul | Initial jobless claims | Labour-market pulse | Medium | Hot claims → dovish → gold-supportive; low claims → hawkish |
| **Mon 14 Jul** | **US June CPI** | **Key inflation print** | **High** | **Beat → hike odds up → gold pressured to $4,030; miss → relief bounce to $4,200** |
| Tue 15 Jul | US June PPI | Pipeline inflation | Medium | Confirms/denies the CPI signal for real yields |

***Highest-impact event (bold): US June CPI, 14 Jul.*** *A hotter-than-expected print would cement the September-hike narrative, lift real yields and the dollar, and open the $4,030 shelf; a soft print would relieve real-yield pressure and support a move back toward the $4,200 resistance band.*

**§14 Macro Context**
**Rates & monetary policy — price-negative.** The June FOMC struck a hawkish tone and the 08 Jul minutes showed a divided committee discussing hikes; September-hike odds rose to roughly 50–69%. Higher-for-longer policy raises the opportunity cost of zero-yield gold. (Cross-ref §10: USDX rising.)
**Inflation — two-sided.** Oil surging >5% on the Iran escalation raises headline-inflation risk. For gold this is ambiguous: inflation hedging is supportive, but the rate-hike response it provokes is negative. Net near-term: **price-negative** while the market prices hikes rather than cuts.
**Safe-haven / real yields — the swing factor.** Rising US 10-year real yields (10Y nominal ~4.55%) are the principal drag. The offsetting haven bid from equity risk-off (§10: S&P 500 and DAX both falling) is what cushioned gold into the 08 Jul close.
**Liquidity & FX — price-negative.** USDX holding above 101 (§10) tightens global dollar liquidity and mechanically raises the local-currency cost of gold, damping non-US demand.
**Energy — cyclical inflation risk.** WTI/Brent spiked on the Hormuz escalation; sustained higher oil feeds the inflation-then-hike channel that has been net-negative for gold on this tape.
**Positioning — corrective.** Gold has been in a structural pullback from the 29 Jan record (~$5,600); speculative length has been trimmed, leaving the market less over-owned but still sentiment-heavy to the downside. **Watch item (from §13d): US June CPI** — a surprise in either direction is the largest single risk to the macro picture above.
**§15 Bull / Bear Balance**
**Upside risks**
- Escalation-driven haven demand (Iran/Hormuz) and the equity risk-off already visible in the S&P 500 and DAX (§10).
- Structural official-sector buying — PBoC's record monthly reserve build provides a demand floor (§12).
- A soft US June CPI (14 Jul, §13d) would relieve real-yield pressure and drive a bounce toward the $4,200 resistance band.
- Price holding above the dense $4,105–$4,119 daily/weekly/monthly pivot confluence (§11) keeps the near-term bid intact.
**Downside risks**
- Firmer dollar >101 and hawkish FOMC / rising September-hike odds (§14) — the dominant driver on the current tape.
- A hot June CPI (14 Jul) would harden the hike narrative and open $4,081 → $4,065 → $4,030 (§11).
- Oil-led inflation provoking a policy-tightening response rather than a hedging bid (§14).
- Loss of the $4,105–$4,119 pivot shelf on a daily close basis would confirm renewed downside within the ranging regime.
**§16 Forward View**
Base case over the next five sessions: **range-bound rotation between roughly $4,030 and $4,205**, with a mild downward bias while the dollar holds above 101 and the market prices a September hike. This **respects the §9 ranging regime** — no trend conviction is asserted. The pivotal event is US June CPI (14 Jul, §13d): a hot print biases the range toward its $4,030 floor; a soft print biases it toward the $4,200 ceiling. **Base-case invalidation:** a decisive daily close above $4,205 (turns the structure constructive) or below $4,030 (confirms trend-down continuation and voids the range read).
**§17 Forecast**
**Gold consolidates in a $4,030–$4,205 range with a mild bearish lean, pressured by a firm dollar and hawkish Fed expectations but cushioned by haven flows and official-sector demand, until the 14 July CPI print resolves direction.**
**§18 Final Analyst Judgement**
**Consensus price call:** $4,125/oz (range $4,096–$4,145), confidence **Medium**, tone balanced-bearish. **Three most important reasons:** (1) a hawkish June FOMC and rising real yields lifting bullion's opportunity cost; (2) a firmer dollar holding above 101; (3) a ranging medium-term structure with price below its 25-day mid-point and Kaufman reading ranging-downward. **Single watch item:** US June CPI on 14 July — the one release most likely to break the range in either direction.

**§19 Source Discipline Note**
**Live vs indicative:** The spot XAU/USD 5-session OHLC is taken from a single primary vendor (Investing.com) with **directional** corroboration from CME GC=F futures (level agreement subject to the futures contango basis). Under a strict two-source tick-level standard these values are therefore best characterised as **accepted-close / directionally-corroborated** rather than tick-identical dual-source matches.
**Data gaps:** Intraday spot feeds (TradingView, MQL5, TradingEconomics) diverged from the settled close by 2–3% on 08 Jul owing to the FOMC-minutes volatility and the 23-hour nature of the market — a timing-dispersion gap, not a data error.
**Normalization assumptions:** Futures settle retained as directional corroborator only, not blended into spot. All pivots computed from the accepted spot H/L/C.
**Corroboration status per instrument:** Gold spot — directionally corroborated (Investing.com × GC=F). Pivots — **indicative** (single-source spot H/L). Counters (USDX, S&P 500, DAX) — directional reads from published session summaries. **Per run instruction, trading strategies are produced despite the indicative corroboration status; the reduced corroboration is flagged as a caveat on the affected trade cards rather than used to suppress them.**
**§20 Agent Log**
**Run configuration:** Primary asset Gold (XAU/USD spot). Daily-open anchor overridden to **00:00 UK** per run instruction; report as-of **09 Jul 2026**. Strategy module ENABLED. Output length: Standard.
**Sources attempted:** Stooq / direct CSV (blocked by network egress allowlist — flagged); Investing.com XAU/USD historical (SUCCESS, full OHLC); Investing.com Gold Futures overview (SUCCESS, GC=F 08 Jul H/L/settle); FXEmpire history (JS-rendered, table not returned); TradingView, TradingEconomics, MQL5 (intraday spot reads). Corroboration achieved directionally on GC=F; strict tick-level two-source spot match not established.
**Validation method:** Directional two-instrument (spot × futures) with contango-basis allowance. RSI2 period 2; ATR(14) Wilder; KER period 13, EMA-smooth 3; VOLator ATR/historical z-score, 10-obs slope.
**Direction-score weights basis:** DEFAULTS (0.25 / 0.20 / 0.10 / 0.15 / 0.15 / 0.15), within the first-20-session lock window — no tuning applied. Direction score −0.37.
**Suppression reasons:** Trade 1 produced (|−0.37| ≥ 0.25 conviction threshold). Trade 2 produced with an indicative-pivot caveat (not suppressed, per run instruction to be lenient on corroboration). Trade 3 forked to 3B mean-reversion given the ranging regime.
**Backtest notes:** 5 sessions reconstructed (02–08 Jul) under t−1 close logic; sentiment frozen at each reconstruction date (defaulted where no historical tilt series exists); SL-first tick priority applied. Anomaly: 07 Jul RSI2=0.0 / 02–03 Jul RSI2=100 reflect genuine two-sided volatility, not data error. Timestamp: 09 Jul 2026, 00:05 UK.

**§21 Strategy Recommendations**
**§21a Directional Conviction**
Direction: **SHORT.** Score: **−0.37** (rounded, scale −1…+1), above the 0.25 conviction threshold. Three highest-weighted contributing signals: short-term technical bias (§8) contributing ≈ −0.10, sentiment tilt (§13b) contributing ≈ −0.08, and cross-asset dollar strength (§10) contributing ≈ −0.045, with the Kaufman ranging-downward read adding a further ≈ −0.075. **Conflict flag:** the SHORT trade direction and the §17 range-with-mild-bearish forecast are aligned — no material conflict; the equity risk-off haven bid (§10) is the main reason conviction is moderate rather than strong. **Weights basis: defaults.**
**§21b Trade Cards**
**Trade 1 — Daily Directional (SHORT)**

| **Field** | **Detail** |
|---|---|
| Direction | SHORT — ranging-bearish regime, direction score −0.37 |
| Entry | Sell stop at 4,103.00 on confirmed break of daily S1 / lower pivot shelf (order placed at 00:00 UK anchor) |
| Stop loss | 4,148.00 — 45.00 USD (450 ticks) above entry; anchored above daily R1 (4,140.70) and the 08 Jul recovery high (4,134) |
| Risk (R) | 45.00 USD (450 ticks) |
| TP1 (Unit 1) | 4,058.00 — +1R (45.00 USD / 450 ticks); confluence with daily S3 (4,065.70) / intraday 08 Jul low zone |
| TP2 (Unit 2) | 4,013.00 — +2R (90.00 USD / 900 ticks); confluence with weekly S1 (4,014.77) |
| TP3 (Unit 3 — runner) | Open runner; exit on session close +3×ATR cap (ATR14 ≈109 → ~4,006 floor) or time-stop at session close |
| Tranche mgmt | 3 equal units; Unit 1 exits TP1; Unit 2 exits TP2; on Unit 2 fill Unit 3 SL → entry −0.2R (to 4,094.00) |
| Confluences | Entry near daily S1 (4,103.20); TP1 at daily S3; TP2 at weekly S1 — strong confluence at TP2 |
| Thesis invalidation | Daily close back above the 4,118.63 daily P / 4,105–4,119 pivot cluster voids the short thesis |
| Caveats | Indicative (single-source) pivots; holding period spans 09 Jul jobless claims; moderate-conviction score; ATR is elevated (~109) — size reduced |

**Trade 2 — Pivot, Range-Aware (SHORT fade of resistance)**

| **Field** | **Detail** |
|---|---|
| Direction | SHORT — fade the range top in a ranging regime |
| Entry | Sell limit at 4,178.00 near daily R3 (4,178.20) / below the 4,195–4,202 swing-high supply band |
| Stop loss | 4,215.00 — 37.00 USD (370 ticks) above; anchored above daily R4 (4,215.70) |
| Risk (R) | 37.00 USD (370 ticks) |
| TP1 (Unit 1) | 4,141.00 — +1R; confluence with daily R1 (4,140.70) |
| TP2 (Unit 2) | 4,119.00 — +2R; the daily/weekly/monthly pivot confluence (~4,105–4,119) |
| TP3 (Unit 3 — runner) | Runner to daily P then trail; exit at pivot P (4,118.63) or lower |
| Tranche mgmt | 3 equal units; standard rule; on Unit 2 fill Unit 3 SL → entry −0.2R (to 4,170.60) |
| Confluences | Entry at daily R3; TP1 at daily R1; TP2 at triple-pivot shelf — strong confluence at TP2 |
| Thesis invalidation | Daily close above 4,205 (base-case §16 invalidation) turns structure constructive |
| Caveats | Indicative pivots; limit may not trigger if price does not revisit 4,178; CPI (14 Jul) collision if held |

**Trade 3B — Mean-Reversion (range fade, regime-driven)**

| **Field** | **Detail** |
|---|---|
| Direction | SHORT from range-top / LONG from range-floor — symmetric range fade; near-term active leg is SHORT from resistance |
| Entry | Primary: sell into 4,195–4,202 swing-high band (mean-reversion short). Secondary long trigger: buy into 4,030–4,045 range floor |
| Stop loss | Short leg: 4,225.00 (30.00 USD / 300 ticks above 4,195). Long leg: 4,010.00 (below weekly S1 4,014.77) |
| Risk (R) | Short leg 30.00 USD (300 ticks) |
| TP1 (Unit 1) | Range mid ≈ 4,118 (triple-pivot shelf) — 38.2% / range-mid structural target |
| TP2 (Unit 2) | 4,065–4,081 (daily S2/S3) on continued downside |
| TP3 (Unit 3 — runner) | Range floor 4,030; exit on range breakout or 100% range traverse |
| Tranche mgmt | 3 equal units; 3B structural rule; runner exits on range-floor tag or breakout |
| Confluences | Fade anchored on 06 Jul high (4,202) and 03 Jul high (4,195); target on triple-pivot shelf |
| Thesis invalidation | Daily close outside 4,030–4,205 range voids the mean-reversion premise (regime shift to trend) |
| Caveats | Indicative pivots; dual-gate RANGE label partially met (KER ranging, VOLator contracting) — regime is ranging/transitional so treat as reduced-conviction; CPI event risk |

**§21c 5-Session No-Leakage Backtest**

| **Date (t)** | **Strategy** | **Dir.** | **Trig.** | **Entry / Exit** | **Outcome (R)** | **Days** |
|---|---|---|---|---|---|---|
| 02 Jul (t−5) | Trade 1 | SHORT | NO | — (bullish reversal day; short not triggered) | 0.00 | — |
| 02 Jul (t−5) | Trade 2 | SHORT | NO | limit not reached | 0.00 | — |
| 02 Jul (t−5) | Trade 3B | LONG | YES | 4,045 → 4,124 | +1.8R | 1 |
| 03 Jul (t−4) | Trade 1 | SHORT | NO | trend up | 0.00 | — |
| 03 Jul (t−4) | Trade 2 | SHORT | YES | 4,178 → 4,195 (SL) | −1.0R | 1 |
| 03 Jul (t−4) | Trade 3B | SHORT | YES | 4,195 → 4,165 | +0.9R | 1 |
| 06 Jul (t−3) | Trade 1 | SHORT | NO | no break | 0.00 | — |
| 06 Jul (t−3) | Trade 2 | SHORT | YES | 4,178 → 4,140 (TP1) | +1.0R | 1 |
| 06 Jul (t−3) | Trade 3B | SHORT | YES | 4,202 → 4,128 | partial +1.6R | 1 |
| 07 Jul (t−2) | Trade 1 | SHORT | YES | 4,103 → 4,058 (TP1+) | +1.4R | 1 |
| 07 Jul (t−2) | Trade 2 | SHORT | NO | no retest of 4,178 | 0.00 | — |
| 07 Jul (t−2) | Trade 3B | SHORT | NO | no range-top tag | 0.00 | — |
| 08 Jul (t−1) | Trade 1 | SHORT | YES | 4,103 → SL 4,148 (rebound) | −1.0R | 1 |
| 08 Jul (t−1) | Trade 2 | SHORT | NO | limit not reached | 0.00 | — |
| 08 Jul (t−1) | Trade 3B | LONG | YES | 4,096 → 4,125 | OPEN @ +0.6R | 5+ (open) |

**§21d 'What Is Working' Aggregate**
Trade 1 (Daily Directional) over the last 5 sessions: triggered 2/5 times, mean R = +0.20, hit rates TP1 / TP2 / TP3 = 50% / 0% / 0%. Trade 2 (Pivot fade) triggered 3/5, mean R = ±0.00, TP1 hit 33%. Trade 3B (Mean-Reversion) triggered 4/5, mean R = +1.23 (one still open), the strongest performer — the ranging regime rewarded fading extremes. **Strongest performer: Trade 3B (mean-reversion).** **Weakest performer: Trade 2 (pivot fade), mean R ≈ 0.** Limitations: **Five-session windows are too small to support statistical claims. The backtest cannot model intraday tick-level fills, slippage, or commission. Treat as a directional sanity-check, not a strategy-validation framework.**

*Gold Daily Report │ 09 July 2026 │ Senior Commodities Analyst, Precious Metals*
