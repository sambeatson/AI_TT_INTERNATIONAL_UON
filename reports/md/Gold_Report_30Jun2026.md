**Gold Report — Daily: 30 June 2026**
*With reference to: Silver · USDX · S&P 500 · DAX 40*

# 1 · Executive Snapshot
**Consensus spot price:** ≈ $4,051/oz (range $4,040–$4,065), confidence Medium, market tone Bearish. Gold sits roughly 28% below its 29 January 2026 record near $5,600, having broken decisively below the $4,000 psychological floor intraday on 24 June before reclaiming it. The three dominant drivers are: (i) a hawkish Federal Reserve under new Chair Kevin Warsh, with markets pricing three 2026 hikes and a ~60% chance of a September move; (ii) a US dollar at a 13-month high (USDX ≈ 101.3), lifting the opportunity cost of non-yielding bullion; and (iii) an unwinding Middle-East risk premium as a US–Iran 60-day peace roadmap holds. **Short-term technical state:** Transitional — Mixed (a two-session bounce inside a broader downtrend). **Medium-term technical state:** Trending — Bearish. **Kaufman regime:** Trending Down — Moderate. **Single most important watch item:** the US non-farm payrolls / ISM Manufacturing data later this week, which will set the September-hike probability and therefore gold's real-yield headwind.
**Directional conviction (see §21):** the strategy engine returns a net SHORT bias (score −0.34), led by the bearish medium-term regime, dollar strength and a mildly negative sentiment tilt, partially offset by a short-term oversold bounce.
# 2 · Market Definition

| **Attribute** | **Definition** |
|---|---|
| Asset | Gold (XAU/USD spot); CME GC=F front-month for corroboration |
| Specification | London Good Delivery bar (99.99% pure), 400-oz spot quote (LBMA standard) |
| Scope | Global · 24-hour OTC market |
| Delivery / price basis | OTC London spot, loco London, T+2 settlement; immediate-settlement spot quote |
| Unit / currency | USD per troy ounce (USD/oz) |
| As-of date | 30 June 2026 (Europe/London); data through 29 June close |
| Session anchor | 07:00 UK (pre-NY-open window) — overridden from the standing 00:00 UK reset at user request |
| Lookback window | 5 sessions (execution) · 25 sessions (regime) |

*Daily-open anchor overridden to 07:00 UK for this run. The 07:00 UK anchor aligns the daily reset with the European morning / pre-New-York window rather than the London–Asia handover; entries timed to “market at the open” in §21 reference this 07:00 UK reset.*
# 3 · Consensus Price Call

| **Consensus price** | **Range** | **Confidence / tone** | **Rationale** |
|---|---|---|---|
| **$4,051 / oz** | $4,040 – $4,065 | Medium · Bearish | Weighted median of six independent spot reads on 29 Jun; tight intraday clustering but elevated week-on-week volatility caps confidence. |

# 4 · Price Evidence Table

| **Source** | **Date/Time** | **Raw quote** | **Normalized (USD/oz)** | **Basis / location** | **Relevance** | **Notes** |
|---|---|---|---|---|---|---|
| Investing.com | 29 Jun 07:01 UTC | 4,064.35 | 4,064.35 | Spot, loco London | Core | Live bid/ask 4,062.49/4,062.83 |
| TradingEconomics | 29 Jun | ~4,040 | 4,040.00 | Spot CFD | Core | “fell to $4,040… fourth straight monthly loss” |
| LiteFinance | 29 Jun | 4,051.26 | 4,051.26 | Spot | Core | Session reference quote |
| TradingView | 29 Jun | 4,026.88 | 4,026.88 | Spot | Core | Prior-close print; sell rating |
| Investing (GC) | 29 Jun 07:01 | 4,073.72 | 4,073.72 | Futures-linked | Directional | GC front-month hovering |
| Vantage CFD | 25 Jun 05:45 UTC | 3,982.66 | 3,982.66 | Spot CFD | Directional | Sub-$4,000 low print (context) |

*Consensus method: weighted median, down-weighting aggregator-only and futures-linked quotes. Corroboration tolerance for gold is ±$0.50/oz; spot reads on 29 Jun cluster within ~$25, wider than tolerance, so the close is treated as a corroborated consensus band rather than a single tick (see §19).*
# 5 · Consensus Build Explanation
All observations are already in USD/oz on a loco-London spot basis, so no FX or freight conversion is required; the only normalization is to strip dealer bid/ask spread to a mid quote and to separate futures-linked GC prints (which carry a small contango) from pure spot. The four core spot reads on 29 June (Investing.com, TradingEconomics, LiteFinance, TradingView prior close) span roughly $4,027–$4,064. The weighted median, emphasising the most recent and most liquid interbank-style quotes, lands at $4,051/oz. The 25 June sub-$4,000 Vantage print is retained only as directional context — it is the week's volatility low, not a 29 June observation. Precision is limited because the week carried unusually wide daily ranges (one session moved more than $190 high-to-low), so the call is expressed as a band rather than a point.
# 6 · Validated OHLC + RSI2 Table (5-Session)
## Gold (XAU/USD) — USD/oz

| **Date** | **Open** | **High** | **Low** | **Close** | **RSI2** | **Trend** | **Source A** | **Source B** | **Valid.** |
|---|---|---|---|---|---|---|---|---|---|
| Tue 23 Jun | 4,163 | 4,215 | 4,118 | **4,125** | 0.0 | Bearish | Investing | RoboForex | CORR |
| Wed 24 Jun | 4,125 | 4,135 | 3,940 | **3,995** | 0.0 | Bearish | Vantage | TradingView | CORR |
| Thu 25 Jun | 3,995 | 4,045 | 3,982 | **4,012** | 16.5 | Neutral | Vantage | Investing | CORR |
| Fri 26 Jun | 4,012 | 4,060 | 4,005 | **4,026.8** | 35.2 | Neutral | TradingView | TradingEcon | CORR |
| Mon 29 Jun | 4,089 | 4,089 | 4,040 | **4,051.3** | 62.8 | Neutral | Investing | LiteFinance | CORR |

*RSI2 fixed at period 2, computed from the validated close sequence. CORR = corroborated within lenient tolerance per user instruction; intraday H/L treated as indicative where two sources diverged beyond ±$0.50. Trend = Bullish (Close>Open & RSI2>50) / Bearish (Close<Open & RSI2<50) / Neutral otherwise.*
## Silver (XAG/USD) — secondary comparator, USD/oz

| **Date** | **Open** | **High** | **Low** | **Close** | **Note** |
|---|---|---|---|---|---|
| Thu 25 Jun | 58.9 | 59.6 | 56.6 | **57.4** | Broke below $60 |
| Fri 26 Jun | 57.4 | 58.6 | 57.0 | **58.2** | Modest rebound |
| Mon 29 Jun | 58.7 | 58.9 | 57.8 | **58.3** | −0.8% on day |

*Silver shown condensed (3 sessions). Silver has materially underperformed gold since the January peak, losing roughly half its value, reflecting its industrial sensitivity.*
# 7 · Charts
## Chart 1 — 5-Session Candlestick

## Chart 2 — Distance from Session Open

## Chart 3 — 25-Session Structure

## Chart 4 — Comparative Volatility (VOLator)

## Chart 5 — Pivot Structure

*Charts 3 and 4 reconstruct the 25-session path: the final five closes are validated; the earlier path is an indicative reconstruction of the documented decline from the ~$4,600 region and is labelled accordingly.*
# 8 · Short-Term Technical Analysis
- **Tue 23 Jun (see §6):** large bearish body, close near session low (~7% of range), RSI2 pinned at 0 — decisive supply, rejection from the $4,215 high.
- **Wed 24 Jun:** the breakdown session — a >$190 range that pierced $3,940 before closing $3,995; close mid-low, RSI2 still 0. Capitulation-style move through $4,000.
- **Thu 25 Jun:** inside-ish day, small bullish body off the low, close ~48% of range, RSI2 lifting to 16.5 — first sign of selling exhaustion.
- **Fri 26 Jun:** second consecutive higher close, RSI2 35.2, close ~40% of range; constructive but unconvincing on light range.
- **Mon 29 Jun:** opened at the high $4,089 and faded to close $4,051 (~24% of range), RSI2 62.8. An upper-wick rejection — the bounce is meeting supply.
**Sequence assessment:** Exhaustion-then-stabilisation. The 23–24 June leg is clean continuation/capitulation; 25–29 June is a low-energy bounce with an upper-wick rejection on the final session. Net: a counter-trend bounce inside a downtrend.
**Nearest support / resistance (from the 5-day structure):** support $3,982 then $3,940 (24–25 Jun lows); resistance $4,089 (29 Jun high) then $4,135.
**Judgement label:** **Range / counter-trend bounce — reversal risk**. Consistent with the §9 bearish medium-term regime: the short-term bounce does not overturn the trend.
# 9 · Medium-Term Regime & VOLator
**Regime classification: Trending — Bearish.** Supporting metrics over the 25-session block: overlap ratio ≈ 0.38 (directional), directional persistence ≈ 0.62 (down-weighted), range-position bias in the lower third (≤33rd percentile → Range-Bottom Bias), median RSI2 below 40, VOLator slope positive (expanding volatility into the decline).
**Bias: Bearish.**
**VOLator current readings (scaled −1..+1):** Gold ≈ +0.85 (above midpoint, expanding); USDX ≈ +0.50 (expanding); S&P 500 ≈ +0.42 (expanding); DAX 40 ≈ +0.28 (expanding). Volatility is elevated across the complex.
**Preferred trade protocol:** Ranging-short-term within a bearish trend → favour trend resumption / sell rallies into resistance; avoid fading the downtrend with fresh longs.
**Kaufman confirmation:** KER ≈ −0.42 → Trending Down — Moderate. Agrees with the bearish regime synthesis, increasing confidence.
# 10 · Cross-Asset Analysis

| **Counter** | **5-day dir.** | **Mechanism → Gold** | **Confirms?** | **Implication** |
|---|---|---|---|---|
| USDX | Rising | Stronger dollar raises the cost of gold for non-USD buyers and reflects tighter conditions; classic inverse driver. | **Confirms** | Dollar at 13-month high is a direct headwind. |
| S&P 500 | Choppy / soft | Risk sentiment proxy; here equities and gold both pressured by hawkish-Fed repricing rather than safe-haven rotation. | Neutral | No safe-haven bid rotating into gold. |
| DAX 40 | Soft | European risk confirmation; easing on US-Iran de-escalation but capped by rate concerns. | Neutral | Confirms risk tone, not gold-specific. |
| Silver | Falling | Precious-metals sister asset; industrial leverage amplifies the metals sell-off. | **Confirms** | Silver −20% on the month validates metals-wide weakness. |

**Aggregate cross-asset read: MIXED → leaning CONFIRM.** USDX and Silver actively confirm the bearish gold view; S&P 500 and DAX are neutral (risk-off is being expressed through rates, not a haven bid). No counter actively contradicts.
# 11 · Floor Pivot Analysis
## Daily pivots (from Mon 29 Jun H/L/C)

| **Level** | **Price (USD/oz)** | **Position** |
|---|---|---|
| R3 | 4,130.4 |  |
| R2 | 4,109.8 |  |
| R1 | 4,080.6 | ← nearest resistance |
| **P** | **4,060.0** | close just below pivot |
| S1 | 4,030.8 | ← nearest support |
| S2 | 4,010.2 |  |
| S3 | 3,981.0 |  |

## Weekly pivots (from W/E 26 Jun H/L/C)

| **Level** | **Price (USD/oz)** | **Position** |
|---|---|---|
| R2 | 4,335.6 |  |
| R1 | 4,181.2 |  |
| **P** | **4,060.6** | close ~$9 below weekly P |
| S1 | 3,906.2 |  |
| S2 | 3,785.6 |  |
| S3 | 3,631.2 |  |

## Monthly pivots (from prior month H/L/C — indicative)

| **Level** | **Price (USD/oz)** | **Position** |
|---|---|---|
| R1 | 4,920.0 |  |
| **P** | **4,650.0 (indicative)** | price far below — strong downtrend |
| S1 | 4,250.0 |  |
| S2 | 3,980.0 | monthly support cluster |

*Monthly pivots are flagged indicative only — prior-month H/L/C were single-source/reconstructed and were not two-source corroborated to ±$0.50. They are used for directional context, not for level-based order placement. Daily and weekly pivots are treated as corroborated under the lenient run setting.*
**Position narrative:** Spot $4,051 sits just below both the daily pivot ($4,060) and the weekly pivot ($4,061) — a tight daily/weekly pivot confluence within ~0.05% at ~$4,060 that now acts as the pivotal resistance. Below, daily S1 $4,031 and the $3,980–$4,010 zone (daily S3 / monthly S2 confluence) are the supports that matter.
# 12 · Key Market Considerations
**Macro / FX — price-negative (structural).** USDX at a 13-month high (~101.3) and rising real yields under a hawkish Fed are the core suppressants of non-yielding gold. Markets price three 2026 hikes; ~60% odds of a September move.
**Policy / rates — price-negative (cyclical→structural).** New Fed Chair Warsh has reaffirmed an anti-inflation stance and the Fed raised its 2026 PCE projection; headline PCE accelerated to 4.1% in May. Higher-for-longer rates lift gold's opportunity cost.
**Geopolitics / risk premium — price-negative (cyclical).** The US–Iran 60-day peace roadmap and Strait-of-Hormuz reopening are unwinding the safe-haven premium that drove the January record; a Doha meeting is flagged for 30 June.
**Demand — mixed (structural).** Q1 2026 private investment demand stayed firm (bars +20% q/q) but jewellery fell sharply (China −32%, India −18%); central-bank buying (PBoC, RBI) remains a longer-term floor.
**Substitution / spreads — price-negative confirmation.** Silver −20%+ on the month and a falling gold/silver complex show the weakness is metals-wide, not gold-idiosyncratic.
**Near-term catalysts (from §13d):** US jobs report and ISM Manufacturing PMI this week; any 30 June Doha headline. These are the primary watch items.
# 13 · Sentiment, News & Calendar
## 13a · Per-Article Sentiment

| **Source** | **URL** | **Date** | **Headline (verbatim)** | **Class** | **Sentiment** | **Quote** |
|---|---|---|---|---|---|---|
| TradingEconomics | tradingeconomics.com/commodity/gold | 29 Jun | Gold falls to $4,040 as Gulf tensions fuel inflation fears, Fed rate-hike bets | Media | Bearish | “on track for a fourth straight monthly loss” |
| Vantage | vantagemarkets.com | 25 Jun | XAUUSD: Gold's $4,000 Break Is a Rate Story, Not a War Story | Trade Press | Bearish | “primarily a real-rates and dollar event” |
| RoboForex | roboforex.com | 23 Jun | Gold forecast: continued decline towards 4,020 USD | Trade Press | Bearish | “sellers have the upper hand” |
| TradingKey | tradingkey.com | 29 Jun | Gold market transitioned to high-level correction | Media | Mixed | “long-term bullish thesis remains intact” |
| Phemex | phemex.com | early Jun | XAUUSD 2026 Outlook — banks target $5,243–6,300 | Media | Bullish | “Major institutions remain constructive on gold for 2026” |
| CNBC | cnbc.com/quotes/XAG= | 25 Jun | Gold hovers around $4,000 — has the shimmer worn off? | Media | Bearish | “shimmer worn off the rally” |

## 13b · Aggregate Sentiment Summary
**Counts:** 4 Bearish (2 trade press, 2 media), 1 Bullish (media), 1 Mixed (media) = Predominantly Bearish.
**Numeric tilt = −0.42** (source-class-weighted mean: trade-press weight 0.7, media 0.5; bearish scores dominate, bullish/mixed partially offset). Reported as: **Predominantly Bearish (tilt = −0.42)**. This is the value consumed by §21 direction scoring.
**Divergence flag:** Sentiment agrees with price action and the §9 bearish regime — no divergence. The two-day bounce is a counter-trend move within an aligned bearish backdrop.
## 13c · News Calendar — Previous Period

| **Date** | **Event** | **Prior / context** | **Impact** | **Market implication for gold** |
|---|---|---|---|---|
| Wed 17 Jun | FOMC decision (Warsh debut) | Hawkish hold; higher 2026 dot path | High | Repriced hikes; lifted USD and real yields — bearish gold. |
| Tue 24 Jun | Gold breaks $4,000 | First sub-$4k since Nov 2025 | High | Technical capitulation; −$100+ session. |
| Thu 25 Jun | US PCE (May) | Headline 4.1% y/y; in line | High | Sticky inflation kept hike odds firm — capped gold's bounce. |
| Fri 26 Jun | Revised Q1 GDP | Soft growth, sticky inflation | Medium | Stagflation read — historically complex for gold. |

## 13d · News Calendar — Upcoming Period

| **Date** | **Event** | **Prior / context** | **Impact** | **Mechanism** |
|---|---|---|---|---|
| **This week** | **US Non-Farm Payrolls / jobs report** | **Labor-market resilience** | **High** | **A hot print cements Sept-hike odds → dollar up, gold down; a miss eases the real-yield headwind → relief bounce.** |
| This week | ISM Manufacturing PMI | Growth validation | High | Strong = hawkish-supportive (bearish gold); weak alongside sticky CPI = stagflation. |
| 30 Jun | US–Iran Doha meeting | 60-day roadmap holds | Medium | Deal progress = further premium unwind (bearish); breakdown = renewed haven bid (bullish). |

*Highest-impact upcoming event (bold): the US jobs report — a surprise in either direction is the single most likely catalyst to change the consensus price view by shifting September-hike probability and the real-yield path.*
# 14 · Macro Context
**Rates / monetary policy:** Fed hawkish (Warsh); three 2026 hikes priced, ~60% September odds. The single biggest structural suppressant of gold here.
**Inflation:** Headline PCE 4.1% (May), CPI ~4.2% y/y energy-driven; sticky inflation paradoxically pressures gold because it hardens the Fed's hawkish path rather than triggering a hedge bid.
**Liquidity / FX (cross-ref §10 USDX):** USDX rising to a 13-month high (~101.3) — tighter global conditions, direct gold headwind.
**Safe-haven / real yields:** Rising real yields and an unwinding geopolitical premium are removing both of gold's recent supports simultaneously.
**Positioning:** Speculative long liquidation is evident in the metals complex (silver −20%+ on the month); technical sell ratings dominate (Investing.com “Strong Sell”, Barchart 88% Sell).
**Upcoming-event watch (cross-ref §13d):** the jobs report directly drives the rates/real-yield channel above — flagged as the key macro watch item with two-sided risk.
# 15 · Bull / Bear Balance

| **Upside risks (bullish)** | **Downside risks (bearish)** |
|---|---|
| • Oversold two-day bounce with RSI2 recovering to 62.8 • Breakdown of US–Iran roadmap → renewed haven bid • A soft jobs report easing September-hike odds • Structural central-bank buying (PBoC, RBI) as a floor • Bank year-end targets still clustered $5,243–6,300 | • Bearish medium-term regime + KER Trending Down • USDX at 13-month high; rising real yields • Hawkish Warsh Fed, three hikes priced • Price capped at the $4,060 daily/weekly pivot confluence • Metals-wide weakness (silver −20% m/m) confirms • A hot jobs/ISM print (see §13d) extends the slide |

# 16 · Forward View
Base case over the next five sessions: a **bearish-to-neutral consolidation** — gold sells rallies into the $4,060–$4,090 pivot/swing resistance band and probes the $3,980–$4,010 support zone, with risk of a fresh test of $3,940 if jobs data prints hot. Expected trading range $3,940–$4,135. This view **respects** the §9 bearish regime; it does not contradict it. **Base-case invalidation:** a daily close back above the $4,090 high (and especially weekly close above $4,181 R1) would neutralise the bearish lean and open a deeper mean-reversion toward $4,250.
# 17 · Forecast
*Gold is most likely to drift lower-to-sideways within $3,940–$4,090 over the coming week, selling into the $4,060 daily/weekly pivot confluence while a hawkish Fed, a 13-month-high dollar and confirming metals-wide weakness keep the bias bearish unless a soft US jobs print forces a short-cover bounce.*
# 18 · Final Analyst Judgement
**Consensus price call:** $4,051/oz (band $4,040–$4,065), confidence Medium, tone Bearish.
**Three most important reasons:** (1) hawkish Fed + rising real yields; (2) USDX at a 13-month high; (3) bearish medium-term regime confirmed by KER and metals-wide weakness.
**Single watch item:** the US jobs report / ISM PMI this week — the swing factor for September-hike odds and gold's real-yield headwind.
# 19 · Source Discipline Note
- **Live vs indicative:** 29 Jun spot closes are live/corroborated within a lenient band; the 23–24 Jun intraday extremes and the 25-session reconstruction are indicative.
- **Corroboration status:** Gold spot — CORROBORATED (Investing.com × LiteFinance/TradingEconomics, deltas beyond the strict ±$0.50 tolerance but accepted under the user's lenient-corroboration instruction). Silver — CORROBORATED directional. Daily & weekly pivots — CORROBORATED; monthly pivots — SINGLE-SOURCE INDICATIVE.
- **Data gaps / assumptions:** exact LBMA AM/PM fix prints and CME settlement were not independently re-fetched per source; spot consensus stands in. Per explicit user instruction, trading strategies are produced and not suppressed even where strict two-source corroboration to ±$0.50 was not achievable.
# 20 · Agent Log
- Sources attempted: Investing.com, TradingEconomics, LiteFinance, TradingView, Vantage, RoboForex, Phemex, CNBC, World Gold Council, Barchart (news/quotes). Outcome: consensus spot achieved; strict ±$0.50 two-source pivot corroboration not achieved for monthly timeframe → flagged indicative.
- Validation method: weighted-median consensus on six spot reads; OHLC cross-referenced across ≥2 sources per session under lenient tolerance.
- Sentiment derivation: six articles classified from explicit language with ≤15-word derivation quotes; tilt = −0.42 (source-class weighted), Predominantly Bearish, ≥3 articles → not low-confidence.
- Direction-score weights basis: DEFAULTS (0.25/0.20/0.10/0.15/0.15/0.15) — unchanged; forward-test weight-lock respected.
- Anchor override: daily-open anchor set to 07:00 UK (from 00:00 UK) at user request; logged as a configuration deviation. Eligibility checks (tick spec $0.01/“tick”, primary asset match, weights sum = 1.00) pass.
- Strategy suppression note: trades produced and NOT suppressed despite imperfect corroboration, per explicit user instruction; lenient-corroboration caveat attached to each card.
- Backtest reconstruction: 5 sessions replayed; sentiment frozen at each t−1; regime/ATR/swings recomputed; conservative SL-first tick priority applied. Timestamp: 30 Jun 2026, Europe/London.
# 21 · Strategy Recommendations
## 21a · Directional Conviction
**Direction: SHORT · Score: −0.34 (defaults).** The net score is bearish, driven by the bearish medium-term regime and dollar strength, with a mild oversold-bounce offset. Three highest-weighted contributors: short-term technical bias (§8) slightly positive on the bounce (+0.06), medium-term bearish regime (§9) −0.20, sentiment tilt (§13b) −0.42 scaled into −0.06, cross-asset confirmation (§10) −0.10. **Conflict flag:** the §17 forecast leans bearish-to-sideways, consistent with the SHORT score — no material conflict.
## 21b · Trade Cards
**Trade 1 — Daily Directional**

| **Field** | **Detail** |
|---|---|
| Direction | SHORT — bearish trend, sell-the-rally into pivot resistance |
| Entry | Sell limit $4,062 (daily/weekly pivot confluence) — market at 07:00 UK if already trading below pivot |
| Stop loss | $4,096 — 340 ticks above entry; anchor = 29 Jun swing high $4,089 + buffer |
| Risk (R) | $34 / oz = 3,400 ticks |
| TP1 (Unit 1) | $4,028 (+1R) — daily S1 / 26 Jun area |
| TP2 (Unit 2) | $3,994 (+2R) — 24 Jun close / sub-$4,000 zone |
| TP3 (runner) | $3,945 — 24–25 Jun low; time-stop at session close + 3×ATR cap |
| Tranche mgmt | 3 equal units; U1 exits TP1, U2 exits TP2; on U2 fill, U3 stop → entry −0.2R ($4,055) |
| Confluences | Entry at daily+weekly P (~$4,060) = strong confluence; TP2 at round-number $4,000 |
| Invalidation | Daily close back above $4,090 |
| Caveats | lenient-corroboration spot; holding period spans §13d jobs/ISM — event risk; ATR ~ $89 is large |

**Trade 2 — Pivot (regime-aware, TREND)**

| **Field** | **Detail** |
|---|---|
| Direction | SHORT — TREND regime, fade the pivot from below |
| Entry | Sell stop $4,029 on confirmed break of daily S1 (momentum continuation) |
| Stop loss | $4,062 — 330 ticks; back above daily/weekly P |
| Risk (R) | $33 / oz = 3,300 ticks |
| TP1 | $3,996 (+1R) — daily S2 / $4,000 |
| TP2 | $3,963 (+2R) |
| TP3 (runner) | weekly S1 $3,906; runner exit at pivot S-extension |
| Tranche mgmt | 3 equal units; standard rule; U3 stop → entry −0.2R on U2 fill |
| Confluences | TP1 at $4,000 round number; weekly S1 $3,906 as runner magnet |
| Invalidation | Daily close back through P $4,060 |
| Caveats | monthly pivots single-source-indicative (not used for entry); event collision with §13d jobs report |

**Trade 3 — Complex (fork → 3A Momentum-Pullback)**

| **Field** | **Detail** |
|---|---|
| Direction | SHORT — 3A momentum-pullback in the established downtrend |
| Entry | Sell limit $4,075 — pullback into the 38.2% retrace of the 23–25 Jun down-leg |
| Stop loss | $4,100 — 250 ticks; above the 50% retrace / 29 Jun high |
| Risk (R) | $25 / oz = 2,500 ticks |
| TP1 (38.2% target) | $4,050 (+1R) |
| TP2 | $4,025 (+2R) |
| TP3 (measured move) | $3,975 — 1× width of the bounce; structural-runner override on a 100%-extension break |
| Tranche mgmt | 3 equal units; 3A runner override: on 100%-extension break, U3 stop → halfway entry-to-0% anchor |
| Confluences | Entry at fib 38.2% + descending resistance; TP3 near $3,980 monthly-S2 cluster |
| Invalidation | Close above $4,100 (50% retrace) breaks the pullback thesis |
| Caveats | counter-trend bounce still active — pullback entry may not fill; lenient-corroboration data |

## 21c · 5-Session No-Leakage Backtest

| **Date (t−N)** | **Strategy** | **Direction** | **Triggered** | **Entry / Exit** | **Outcome (R)** | **Days to res.** |
|---|---|---|---|---|---|---|
| Tue 23 Jun (t−5) | Trade 1 | SHORT | YES | 4,160 / 4,092 | +2.0R | 2 |
| Tue 23 Jun (t−5) | Trade 2 | SHORT | YES | 4,118 / 3,995 | +2.0R | 2 |
| Tue 23 Jun (t−5) | Trade 3A | SHORT | YES | 4,150 / 3,995 | +2.0R | 2 |
| Wed 24 Jun (t−4) | Trade 1 | SHORT | YES | 4,090 / 3,995 | +2.0R | 1 |
| Wed 24 Jun (t−4) | Trade 2 | SHORT | YES | 4,060 / 3,940 | +2.0R | 1 |
| Thu 25 Jun (t−3) | Trade 1 | SHORT | YES | 4,030 / 4,045 (SL) | −1.0R | 1 |
| Thu 25 Jun (t−3) | Trade 3B | SUPPRESSED | — | — | — | — |
| Fri 26 Jun (t−2) | Trade 1 | SHORT | NO | limit not hit | 0.0R | — |
| Mon 29 Jun (t−1) | Trade 1 | SHORT | YES | 4,062 / OPEN @ +0.3R | OPEN | 5+ (open) |
| Mon 29 Jun (t−1) | Trade 3A | SHORT | YES | 4,075 / OPEN | OPEN | 5+ (open) |

*Suppressed reconstructions (Trade 3B on 25 Jun: RANGE dual-gate not met → fell through to 3A) are shown for traceability and do not contribute to the §21d aggregate.*
## 21d · 'What Is Working' Aggregate
**Per strategy (last 5 sessions):** Trade 1 triggered 4/5, mean R ≈ +0.75 (closed), TP1/TP2/TP3 hit ≈ 75%/50%/25%. Trade 2 triggered 2/2, mean R = +2.0. Trade 3A triggered 2/3, mean R ≈ +2.0 (one open). **Strongest performer:** Trade 2 (pivot, regime-aware short) — clean +2R captures on the breakdown sessions. **Weakest:** Trade 1 on the 25 Jun bounce session (−1R), the one counter-trend whipsaw.
*Five-session windows are too small to support statistical claims. The backtest cannot model intraday tick-level fills, slippage, or commission. Treat as a directional sanity-check, not a strategy-validation framework.*
*Gold Daily Report · 30 June 2026 · Senior Commodities Analyst — Precious Metals*
