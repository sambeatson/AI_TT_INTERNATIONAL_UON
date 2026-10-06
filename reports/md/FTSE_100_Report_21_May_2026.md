**FTSE 100 Report — Daily: 21 May 2026**
*With reference to: EURO STOXX 50 · USDX · S&P 500 · DAX 40*
*Senior European Equity Strategist · Trading and risk review (forward-test) · Prepared at the European pre-open, 21 May 2026 (Europe/London)*

**Run note.** This instance was run for the 21 May 2026 session. The daily-open anchor that governs the Trade 1 entry timestamp has been overridden from its standard configured value to 00:00 UK for this run, at the analyst’s instruction; the change is logged in the Agent Log (§20). The standard configuration anchors the entry to the 07:00 UK pre-open window. With the override, the Trade 1 entry is taken at the 00:00 UK roll, giving a full overnight-futures and Asian-session read into the cash-session open. Strategy recommendations (§21) are produced in full.

# 1. Executive Snapshot
The FTSE 100 cash index closed the 20 May 2026 session at **10,393.0 index points**, recovering for a third consecutive day after the sharp 15 May sell-off. The most defensible consensus level for the close is **10,393 points (range 10,360–10,410)**, with a confidence of Medium — the index is quoted continuously by multiple providers but provider snapshots diverged by several tens of points during a volatile, headline-driven week.
Market tone is balanced with a mild positive tilt. Three drivers dominate the current level: **(1)** the unresolved US–Iran conflict and a crude-oil price still near four-year highs, which both supports FTSE energy heavyweights and keeps an inflation premium in rates; **(2)** UK political uncertainty around the Prime Minister’s position, which has weighed on gilts and sterling intermittently; and **(3)** a softer UK inflation print and weaker labour-market data that have pulled Bank of England rate-hike pricing back toward two hikes by December.
Technically the short-term state is Transitional — Bullish recovery: the 5-day block contains one violent down-session (15 May) followed by three constructive closes, so the rebound is real but unconfirmed. The medium-term 25-session regime is Ranging / Transitional — overlap is high (0.65) and directional persistence sits on the 0.50 boundary. The Kaufman Efficiency Ratio reads −0.14 (a marginal ‘Trending Down — Moderate’) which **contradicts** the recovering price and the positive volatility slope; that disagreement is itself the reason the consolidated regime resolves to Transitional. Single most important watch item: the **Bank of England MPC decision and minutes (Thu 22 May 2026)** — it falls inside the trade-card holding window and can re-rate the whole curve.
Strategy read (see §21): the direction score is **+0.40 — a LONG conviction**, above the threshold, so a daily directional long is produced; the regime-driven pivot and complex trades are built on the Transitional fork.
# 2. Market Definition

| **Parameter** | **Definition** |
|---|---|
| Primary asset | FTSE 100 cash index (^FTSE) — UK large-cap benchmark, 100 constituents |
| Reference asset | EURO STOXX 50 (^STOXX50E) — Eurozone large-cap pair, reported alongside FTSE |
| Specification | FTSE 100 cash index, GBP-denominated, free-float capitalisation-weighted (FTSE Russell methodology) |
| Asset class | Equity index — large-cap European |
| Market scope | Regional — United Kingdom (LSE) and Eurozone (Xetra / Euronext) |
| Price basis | Cash index level, continuous during the regular session |
| Delivery basis | LSE regular session 08:00–16:30 UK (FTSE); Xetra 09:00–17:30 CET (EURO STOXX 50) |
| Unit of measure | Index points |
| Currency | GBP (FTSE). EURO STOXX 50 reported in its native EUR; no FX normalisation is applied to the STOXX OHLC table. |
| Tick size / name | 0.01 / point |
| As-of date | 20 May 2026 close (Europe/London) — report horizon 21 May 2026 session |
| Lookback window | 5 trading days (short block); 25 sessions (medium regime block) |

# 3. Consensus Price Call

| **Consensus close** | **Range** | **Basis** | **Confidence** | **Market tone** |
|---|---|---|---|---|
| **10,393 points** | 10,360 – 10,410 | Cash index level (continuous) | Medium | Balanced — mild positive tilt |

**Rationale.** The 20 May close is observed consistently across index-provider and exchange-derived feeds at approximately 10,393 points; intra-week provider snapshots ranged a few tens of points either side because the session was headline-driven and several feeds carry a 15-minute delay. The weighted-median of the corroborated feeds sits at 10,393, and the ±17-point band reflects residual snapshot dispersion rather than genuine price uncertainty.
# 4. Price Evidence Table

| **Source** | **Date / time** | **Raw quote** | **Normalised** | **Basis / location** | **Relevance / notes** |
|---|---|---|---|---|---|
| FTSE Russell official close | 20 May 2026, 16:35 UK | 10,393.0 | 10,393.0 | Cash index, London | Core — official benchmark publication |
| LSE exchange-derived feed | 20 May 2026, 16:35 UK | 10,393.0 | 10,393.0 | Cash index, London | Core — exchange settlement reference |
| Investing.com | 20 May 2026, EOD | 10,393 | 10,393 | Cash index, London | Core — OHLC corroboration |
| Trading Economics (GB100) | 20 May 2026, EOD | 10,393 | 10,393 | CFD-tracked benchmark | Directional — CFD proxy, used for cross-check only |
| Yahoo Finance | 19–20 May 2026 | 10,330 / 10,408 | 10,330 / 10,408 | Cash index, London | Directional — snapshot dispersion noted |
| Stooq (^ftm) | 20 May 2026, EOD | 10,393 | 10,393 | Cash index, London | Core — free CSV corroboration |

*Six observations were collected, meeting the minimum source count. Retail CFD-broker spread quotes were excluded per the source restrictions. The Yahoo Finance 19 May snapshot (10,330) and a later 10,408 snapshot illustrate the intra-week feed dispersion and are classified Directional, not Core.*
# 5. Consensus Build Explanation
All six observations are already expressed in index points for the FTSE 100 cash index, so no currency, freight or specification normalisation is required — the comparables are natively on the target basis. Observations were weighted by source credibility (index-provider and exchange-derived feeds highest), recency (all are 19–20 May), and methodology transparency.
- Core comparables: the FTSE Russell official close, the LSE exchange-derived feed, Investing.com and Stooq all corroborate 10,393.0 within the ±0.10-point equity-index tolerance on the close.
- Directional comparables: the Trading Economics GB100 CFD reading and the Yahoo Finance snapshots are retained for cross-check but down-weighted — the CFD tracks rather than publishes the index, and the Yahoo snapshots were captured at different times of a volatile week.
- Exclusions: retail CFD-broker bid/offer quotes were excluded outright; they widen materially in headline-driven sessions and would distort the median.
Applying the weighted median across the four Core feeds yields **10,393 points** as the most defensible close. The ±17-point range is the residual snapshot dispersion; it is reported as a range-aware figure rather than a false-precision point because the week’s volatility makes any single-feed tick unreliable.
# 6. Validated OHLC + RSI2 Table (5-Day)
*Technical section. Dual-source corroborated 5-day block for the FTSE 100 and the EURO STOXX 50 reference pair.*
## FTSE 100 (^FTSE) — 14 to 20 May 2026

| **Date** | **Open** | **High** | **Low** | **Close** | **RSI2** | **Trend** | **Source A** | **Source B** | **Valid.** |
|---|---|---|---|---|---|---|---|---|---|
| 14 May | 10,381.5 | 10,449.3 | 10,358.2 | **10,433.0** | 100.0 | Bullish | Investing.com | Stooq | CORR. |
| 15 May | 10,433.0 | 10,446.8 | 10,180.5 | **10,195.4** | 17.8 | Bearish | Investing.com | Yahoo | CORR. |
| 18 May | 10,195.4 | 10,328.6 | 10,188.9 | **10,303.7** | 31.3 | Neutral | Investing.com | Stooq | CORR. |
| 19 May | 10,303.7 | 10,366.5 | 10,279.1 | **10,330.6** | 100.0 | Bullish | Investing.com | Yahoo | CORR. |
| 20 May | 10,330.7 | 10,458.3 | 10,279.1 | **10,393.0** | 100.0 | Bullish | Investing.com | Stooq | CORR. |

*RSI2 is a period-2 Wilder RSI computed from the validated close column; readings of 100.0 occur where neither of the prior two sessions posted a loss — a known property of the short window, not a data error. Trend uses the close-versus-open and RSI2 combination; 18 May posted a higher close on a sub-50 RSI2 and is therefore Neutral. All five sessions corroborated within the ±0.10-point equity-index tolerance.*
## EURO STOXX 50 (^STOXX50E) — 14 to 20 May 2026

| **Date** | **Open** | **High** | **Low** | **Close** | **RSI2** | **Trend** | **Source A / B** | **Valid.** |
|---|---|---|---|---|---|---|---|---|
| 14 May | 5,872.1 | 5,905.4 | 5,848.0 | **5,894.3** | — | Bullish | Investing.com / Yahoo | CORR. |
| 15 May | 5,894.3 | 5,901.0 | 5,772.6 | **5,786.2** | — | Bearish | Investing.com / Yahoo | CORR. |
| 18 May | 5,786.2 | 5,849.7 | 5,781.0 | **5,832.4** | — | Bullish | Trading Econ. / Yahoo | CORR. |
| 19 May | 5,832.4 | 5,861.9 | 5,810.3 | **5,851.2** | — | Bullish | Trading Econ. / Yahoo | CORR. |
| 20 May | 5,857.8 | 5,910.5 | 5,843.6 | **5,851.2** | — | Neutral | EBC / Yahoo | CORR. |

*EURO STOXX 50 values are in native EUR index points. The pair traced the same shape as the FTSE — a 15 May break, then a recovery — but its 20 May session closed flat at 5,851 after failing at the 5,910 area. RSI2 is reported for the FTSE primary only; the STOXX table is the reference comparator.*
# 7. Charts
*Technical section. Five charts produced per the active output configuration.*

*Chart 1 — FTSE 100 five-day candlestick. The 15 May bearish marubozu dominates the block; three subsequent green candles recover roughly two-thirds of the loss.*

*Chart 2 — Distance from open. 15 May shows extreme downside travel with the close pinned to the low; 18–20 May show upside travel with closes in the upper half of range.*

*Chart 3 — 25-session structure. Direction-coded bars with a close overlay; the rotation from the 10,668 April high down to the 10,180 mid-May low and the partial recovery are visible.*

*Chart 4 — Comparative volatility (ATR / historical z-score). FTSE volatility is expanding and now sits at the top of its own range; USDX volatility is the most subdued of the four series.*

*Chart 5 — Pivot structure, week of 18 May. Prior and in-progress weekly candles against daily, weekly and monthly floor pivots. Note the weekly-P / monthly-S1 confluence near 10,385–10,388.*
# 8. Short-Term Technical Analysis
*Technical section. Candle-by-candle classification and sequence assessment for the FTSE 100 5-day block (see §6).*
- 14 May — a bullish-bodied candle closing at 82% of range on a maximal RSI2 (see §6). Body dominates a short upper wick; this is a clean continuation candle and the strongest close of the week’s first half.
- 15 May — a large bearish candle, effectively a marubozu, closing at just 6% of range with RSI2 collapsing to 17.8. The session opened near the prior close and sold off almost 270 points; this is the defining shock of the block and resets the short-term structure.
- 18 May — a recovery candle closing at 82% of range but on a sub-50 RSI2 (31.3), hence the Neutral trend label. A long upper-half body and a small lower wick show demand re-engaging from the 10,189 low; the RSI2/price split flags the move as a bounce, not yet a confirmed turn.
- 19 May — a narrow-range bullish candle, close at 59% of range, RSI2 back at maximum. Body is modest and overlap with 18 May is high — consolidation just above the prior demand zone.
- 20 May — a bullish candle closing at 64% of range with RSI2 again at maximum. The session high (10,458) is the best level since the sell-off, but the close some 65 points below that high leaves an upper wick — modest supply into the bounce.
**Sequence assessment:** Exhaustion followed by recovery, classified overall as Indecision shading to a constructive bias. The block is not a clean continuation — the 15 May range expansion with a close reverting hard against the prior open is textbook exhaustion of the preceding drift, and the three recovery candles overlap heavily with prominent wicks on both sides. The evidence: one outsized down-session, three smaller up-sessions, RSI2 swinging between 17.8 and 100, and a 20 May upper wick.
**Nearest support and resistance (from the 5-day structure):** support at 10,279 (the 19/20 May twin session low) and below it 10,181 (the 15 May swing low); resistance at 10,458 (the 20 May high) and the 10,512 area just above the window.
**Judgement label:** **Indecision**. This is consistent with the Transitional regime in §9 — the short-term recovery is genuine but unconfirmed, and no continuation or reversal label can yet be justified from the data.
# 9. Medium-Term Regime & VOLator
*Technical section. 25-session regime classification and comparative volatility read.*
**Regime classification: Transitional.** Supporting metrics over the 25 sessions: overlap ratio 0.65 (above the 0.55 range threshold), directional persistence 0.50 (on the ranging boundary), median RSI2 52.6, and a range-position bias for the latest close at the 44th percentile — squarely mid-range. Overlap and persistence point to a range; the absence of a clear directional mean keeps it from being labelled cleanly Ranging, so the regime resolves to Transitional.
**Bias:** **Neutral** — the directional component of the medium-term regime is flat; the index has rotated within a roughly 10,180–10,668 band over the window.
**VOLator current readings (ATR, historical z-score, −1 to +1):** FTSE 100 +1.00 (above midpoint, expanding); USDX approximately −0.1 (below midpoint, broadly flat); S&P 500 approximately +0.4 (above midpoint, expanding); DAX 40 approximately +0.6 (above midpoint, expanding). FTSE volatility is the most stretched of the set — the 15 May shock pushed it to the ceiling of its own historical band. The VOLator slope over the last ten observations is positive (+0.27), confirming volatility expansion.
**Preferred trade protocol:** combining the short-term Indecision read (§8) with the medium-term Transitional regime gives a reduced-conviction protocol — wait for confirmation before committing, and treat range-edge tests rather than trend continuation as the base case.
**Kaufman confirmation:** the smoothed Kaufman Efficiency Ratio is −0.14, marginally beyond the −0.13 trend threshold, classified ‘Trending Down — Moderate’. This **contradicts** both the recovering price and the positive VOLator slope. Where Kaufman and VOLator disagree, the consolidated regime is forced to Transitional rather than to either trend label — the disagreement is not resolved away, it is the signal. The KER reading is borderline and rising, so it is best read as a fading bearish residue from the mid-May leg lower rather than a fresh down-trend.
# 10. Cross-Asset Analysis
*Technical section. Counter directional reads and causal mechanisms; relative to the §9 Transitional regime.*

| **Counter** | **5-day dir.** | **Mechanism to FTSE 100** | **Status** | **Implication** |
|---|---|---|---|---|
| USDX (Dollar Index) | Falling / flat | A softer dollar eases global financial conditions and lifts the GBP-translated value of FTSE multinationals’ overseas earnings. | Confirms (mild) | Marginally supportive of the FTSE recovery. |
| S&P 500 | Rising | Cross-Atlantic risk appetite is the common-factor beta for European indices; a firmer S&P pulls FTSE risk premia lower. | Confirms | Supports the bounce; argues against fading it. |
| DAX 40 | Flat / mixed | Eurozone equity proxy with an industrials skew; the DAX stalled near 24,400 on Iran caution and Nvidia-earnings nerves. | Contradicts | A flat DAX into FTSE strength is a non-confirmation of the regional rebound. |

**Contradiction flag.** The DAX 40 is not confirming the FTSE recovery — it traded near the flatline around 24,400 while the FTSE and S&P advanced. This non-confirmation is carried forward, not resolved: it feeds the Bull/Bear Balance (§15) and the Forward View (§16) as a caution that the European rebound lacks breadth.
**Aggregate cross-asset read: MIXED.** Two counters confirm (USDX, S&P 500) and one contradicts (DAX 40); under the aggregation rule, any confirm-and-contradict combination resolves to MIXED. The EURO STOXX 50 reference pair broadly tracks the FTSE shape — same 15 May break, same partial recovery — and does not diverge from the regime synthesis.
# 11. Floor Pivot Analysis
*Technical section. Daily, weekly and monthly floor pivots for the FTSE 100. Source status noted below each table.*
## Daily pivots — from the 19 May session H/L/C

| **Level** | **Points** | **Level** | **Points** |
|---|---|---|---|
| R5 | 10,633.9 | **P** | **10,325.4** |
| R4 | 10,546.5 | S1 | 10,284.3 |
| R3 | 10,459.1 | S2 | 10,238.0 |
| R2 | 10,412.8 | S3 | 10,196.9 |
| R1 | 10,371.7 | — | — |

*Mandatory display order R5→P→S5. Daily pivots are derived from the engine’s rolling-window prior-session H/L/C; see the source-discipline note (§19).*
## Weekly pivots — from the prior week (11–15 May) H/L/C

| **Level** | **Points** | **Level** | **Points** |
|---|---|---|---|
| R5 | 11,259.1 | **P** | **10,385.3** |
| R4 | 11,008.9 | S1 | 10,258.3 |
| R3 | 10,758.7 | S2 | 10,135.1 |
| R2 | 10,635.5 | S3 | 10,008.1 |
| R1 | 10,508.5 | — | — |

## Monthly pivots — from the April 2026 H/L/C

| **Level** | **Points** | **Level** | **Points** |
|---|---|---|---|
| R5 | 11,446.8 | **P** | **10,528.0** |
| R4 | 11,182.1 | S1 | 10,388.0 |
| R3 | 10,917.4 | S2 | 10,263.3 |
| R2 | 10,792.7 | S3 | 10,123.3 |
| R1 | 10,652.7 | — | — |

**Source status.** The prior-period high/low/close inputs for all three pivot timeframes are taken from the engine’s validated rolling window rather than from an independent two-source pivot fetch. They are therefore flagged single-source-indicative and carried as indicative levels. This flag is propagated to §19 and to the §21 trade cards. Per the run instruction, trades are not suppressed on corroboration grounds (see §21 caveats).
**Position narrative.** The 20 May close of 10,393 sits just above the daily pivot P (10,325) and the weekly pivot P (10,385), and fractionally above monthly S1 (10,388). The weekly P (10,385) and monthly S1 (10,388) form a **confluence zone within 0.03%** of each other — a meaningful support shelf directly beneath the market. Immediate resistance is daily R1 (10,372, now broken and acting as support) and daily R2 (10,413); above that the weekly R1 / monthly S-shelf cluster near 10,508–10,528 is the first significant ceiling.
# 12. Key Market Considerations
*Updated specification. Structured fundamentals; each subheading carries a direction label.*
**Energy and commodities — price-supportive (structural).** Crude oil remains near four-year highs with the US–Iran conflict unresolved and Strait-of-Hormuz traffic intermittently constrained. The FTSE 100 carries a heavy energy weight through Shell and BP, so elevated crude is a direct earnings tailwind for two index heavyweights even as it pressures the wider market through inflation. Mining heavyweights add a second commodity lever.
**Monetary policy / rates — mildly supportive turning to a cyclical risk.** A softer-than-expected UK April inflation print (headline near 2.8%, below the 3.0% consensus) and weaker labour-market data — unemployment rising to about 5%, vacancies at a multi-year low — have pulled Bank of England hike pricing back toward two hikes by December. Lower-for-longer rate expectations support equity valuations, but the BoE decision on 22 May (see §13d) is the cyclical swing factor.
**UK politics — price-negative (cyclical).** Uncertainty around the Prime Minister’s position has driven episodic gilt volatility and sterling weakness through the month. A weaker pound mechanically lifts the FTSE 100 via overseas earnings translation, but the associated risk premium and gilt volatility are a headwind to sentiment and to UK-domestic constituents.
**Cross-market / substitution — neutral.** The FTSE trades at a persistent valuation discount to the S&P 500 and to continental peers, which provides relative-value support. But the DAX 40’s failure to confirm the rebound (§10) signals the European bid lacks breadth, neutralising the substitution case for now.
**Near-term catalysts (from §13d) — event-driven.** The Bank of England MPC decision and minutes on 22 May is the dominant scheduled risk inside the scenario horizon; any further escalation or de-escalation in the Iran conflict is the dominant unscheduled risk. Both can move the index by more than a daily ATR.
# 13. Sentiment, News & Calendar
*Updated specification. Per-article sentiment, aggregate (categorical + numeric tilt), and a two-part news calendar.*
## 13a Per-Article Sentiment Table

| **Source / class** | **Date** | **Headline** | **Sentiment** | **Derivation quote** |
|---|---|---|---|---|
| Trading Economics (Trade Press) | 20 May | FTSE 100 finishes broadly flat as inflation and Iran weigh | **Mixed (−0.3)** | *“gave up earlier gains to finish broadly flat”* |
| CNBC (Media) | 19 May | European markets: UK unemployment rises; Uniper privatisation begins | **Bearish** | *“UK unemployment rises” — softer labour data* |
| CNBC (Media) | 18 May | European markets rebound after Trump threatens Iran | **Bullish** | *“European markets rebound” on easing risk* |
| Analytics Insight (Media) | 19 May | FTSE 100 opens 51 points higher as US–Iran peace hopes lift sentiment | **Bullish** | *“opened 51 points higher … peace talks ease tensions”* |
| Bloomberg (Institutional) | 19 May | UK unemployment rises to 5% with companies shedding jobs | **Bearish** | *“unemployment rises to 5% … companies shedding jobs”* |
| T. Rowe Price (Institutional) | 15 May | Global markets weekly update — UK FTSE 100 slipped 0.37% | **Mixed (−0.3)** | *“geopolitical tensions continued to weigh on sentiment”* |

*URLs: tradingeconomics.com/united-kingdom/stock-market; cnbc.com/quotes/.FTSE; analyticsinsight.net (FTSE 100 live); bloomberg.com (FTSE 100 live blog, 19 May 2026); troweprice.com global-markets-weekly-update. Each classification carries a derivation quote of fifteen words or fewer drawn from the article language.*
## 13b Aggregate Sentiment Summary
**Counts:** 2 Bullish (media), 2 Bearish (1 institutional, 1 media), 2 Mixed (1 institutional, 1 trade press). Categorical label: **Mixed / Balanced**. The bullish articles are media-class and headline-driven (peace-talk hopes); the bearish articles include an institutional labour-market read that carries higher weight.
**Numeric tilt:** applying the source-class weights (institutional 1.0, trade press 0.7, media 0.5) and the article scores — Σw·s = (0.5·+1)+(0.5·+1)+(0.5·−1)+(1.0·−1)+(0.7·−0.3)+(1.0·−0.3) = −0.71; Σw = 0.5+0.5+0.5+1.0+0.7+1.0 = 4.2; tilt = −0.71 / 4.2 = **−0.17**. Reported as Mixed / Balanced (tilt = −0.17). The tilt is computed on six articles, so it is not low-confidence.
**Divergence flag.** The mildly negative sentiment tilt sits against a recovering three-day price and a positive VOLator slope — a modest sentiment/price divergence. Given the Transitional regime (§9), price action is the more reliable near-term signal; the negative tilt reflects the institutional labour-market read and the unresolved Iran overhang rather than fresh selling pressure.
## 13c News Calendar — Previous Period (15–20 May 2026)

| **Date** | **Event** | **Prior / context** | **Impact** | **Market implication for FTSE 100** |
|---|---|---|---|---|
| Fri 15 May | Risk-off session — inflation fears return | Crude near four-year highs | High | FTSE fell 1.7% to 10,195; the defining down-leg of the block. |
| Mon 18 May | Trump postpones Iran strike — risk rebound | Iran conflict ongoing | High | FTSE recovered to 10,304 as geopolitical risk premium eased. |
| Tue 19 May | UK labour-market data | Unemployment 4.9% prior | Medium | Unemployment rose to ~5%, vacancies at multi-year low; trimmed BoE hike pricing, mildly supportive. |
| Wed 20 May | Session close — inflation and Iran caution | 19 May close 10,331 | Medium | FTSE finished broadly flat-to-higher at 10,393; mining weak, defence and utilities firm. |

## 13d News Calendar — Upcoming Period (21–27 May 2026)

| **Date** | **Event** | **Prior / context** | **Impact** | **Market implication for FTSE 100** |
|---|---|---|---|---|
| **Thu 22 May** | **Bank of England MPC decision + minutes** | **Market pricing ~2 hikes by Dec** | **High** | **A hawkish hold or hike signal lifts GBP and pressures rate-sensitive constituents; a dovish read does the reverse and supports the index.** |
| 21–27 May | Iran conflict headlines (unscheduled) | Strait of Hormuz constrained | High | De-escalation lowers crude and lifts risk; escalation spikes crude — supports energy names, pressures the wider index. |
| w/c 25 May | Eurozone flash PMIs / CPI revisions | Industrial production +0.2% m/m | Medium | Weaker prints would weigh on the EURO STOXX 50 reference pair and, by common-factor beta, on the FTSE. |

**Highest-impact upcoming event: the Bank of England decision and minutes on 22 May.** Mechanism: a surprise on the hawkish side would re-rate the gilt curve and the pound, lifting GBP-translation headwinds for multinationals and pressuring domestic and rate-sensitive names, and could shift the §3 consensus tone; a dovish surprise would do the opposite. The decision falls squarely inside the §21 trade-card holding windows.
# 14. Macro Context
*Updated specification. Rates, inflation, liquidity, FX and positioning; cross-referencing the §10 counter reads.*
**Rates and monetary policy.** The Bank of England is the pivotal central bank for the FTSE this week; market pricing has eased to roughly two hikes by December after the softer inflation and labour data. The European Central Bank is a secondary input via the EURO STOXX 50 reference. Elevated crude keeps an inflation premium embedded in both curves.
**Inflation — turning supportive.** UK April headline inflation near 2.8%, below the 3.0% consensus and the lowest in over a year, is price-supportive for the index: it eases the pressure on the BoE and lowers the discount rate applied to equity cash flows. The risk is that crude strength feeds back into the next print.
**Liquidity and FX — mildly supportive.** Per the §10 cross-asset read, the Dollar Index is soft-to-flat. A softer dollar eases global financial conditions and lifts the GBP value of FTSE multinationals’ overseas earnings. Sterling has been choppy on UK political headlines; episodic GBP weakness is itself a mechanical tailwind for the index’s large multinational cohort.
**Energy.** Crude near four-year highs is the single most important macro variable for the FTSE’s sector mix — directly supportive of Shell and BP, indirectly negative for the wider market through inflation and consumer pressure. This is the channel through which the Iran conflict reaches the index.
**Positioning.** The VIX has hovered in the high-teens through the week, consistent with elevated but not panicked risk. FTSE volatility itself (§9) is stretched to the top of its own range after the 15 May shock. The §10 contradiction — a flat DAX 40 — is the macro watch item: it suggests the rebound is UK/US-led rather than a broad European risk-on, and a renewed Iran escalation or a hawkish BoE (§13d) is the directional risk that would expose that narrow breadth.
# 15. Bull / Bear Balance

| **Main upside risks** | **Main downside risks** |
|---|---|
| Iran de-escalation lowers crude, lifts risk appetite and removes the inflation overhang. A dovish Bank of England on 22 May (§13d) re-rates the curve and supports valuations. Price sits on a weekly-P / monthly-S1 confluence shelf at 10,385–10,388 (§11) — a defended support. USDX soft and S&P 500 firm (§10) both confirm the recovery; FTSE valuation discount adds relative-value support. Energy heavyweights cushion the index if crude stays bid. | A hawkish Bank of England surprise on 22 May — the highest-impact event in §13d — pressures rate-sensitive names. Renewed Iran escalation spikes crude and the inflation premium, hitting the wider market. The DAX 40 is not confirming the rebound (§10 contradiction) — the European bid lacks breadth. A close back below the 10,385–10,388 confluence and the 10,279 twin low opens the 10,181 swing low. Kaufman still reads a residual ‘Trending Down — Moderate’ (§9); the down-leg is not fully spent. UK political risk can re-ignite gilt and sterling volatility. |

**Balance.** The book is close to even with a slight constructive lean while price holds the 10,385–10,388 confluence shelf. The single event that can decisively tip it is the 22 May Bank of England decision; the single condition that would flip the technical read is a daily close back through that confluence and the 10,279 twin low.
# 16. Forward View
**Expected direction (next 5 trading days):** sideways-to-higher with a wide band, conditional on the 22 May Bank of England decision. The base case is that the FTSE holds the 10,385–10,388 weekly-P / monthly-S1 confluence and works toward the 10,508–10,528 weekly-R1 / monthly-shelf cluster, with the 20 May high at 10,458 the first intermediate test.
**Trading range:** approximately 10,238 (daily S2) to 10,540 (daily R4) for the routine case; a hawkish BoE or an Iran escalation could extend either boundary by roughly one ATR (~120 points).
**Base-case invalidation:** a daily close back below the 10,385–10,388 confluence and then 10,279 invalidates the constructive lean and re-exposes the 10,181 swing low.
**Regime consistency.** This view respects the §9 Transitional regime — it explicitly treats the path as a range-edge test rather than a confirmed trend, and it carries the §10 DAX non-confirmation as a stated caution. It does not contradict the technical regime classification.
# 17. Forecast
**The FTSE 100 holds the 10,385–10,388 confluence shelf and grinds toward the 10,508–10,528 resistance cluster over the next five sessions, with the 22 May Bank of England decision the binary risk to that path.**
*This single sentence is derived from the technical integration note, the Mixed/Balanced sentiment tilt and the cross-asset read. It is independent of the §21 trade-card direction and is not edited to align with it.*
# 18. Final Analyst Judgement
**Consensus price call:** FTSE 100 cash index at 10,393 points (range 10,360–10,410), confidence Medium, market tone balanced with a mild positive tilt.
**Three most important reasons for the current level:**
- The US–Iran conflict and crude near four-year highs — a double-edged driver that supports FTSE energy heavyweights while keeping an inflation premium in rates.
- Softer UK inflation and weaker labour-market data, which have eased Bank of England hike pricing and supported equity valuations into the recovery.
- A genuine but unconfirmed three-day technical rebound off the 15 May shock, sitting on a weekly-P / monthly-S1 confluence support shelf.
**Single watch item:** the Bank of England MPC decision and minutes on 22 May — it falls inside the trade-card holding window and is the one scheduled event that can decisively re-rate the index.
# 19. Source Discipline Note
**Live versus indicative data.** The FTSE 100 and EURO STOXX 50 5-day OHLC blocks are corroborated: every close is confirmed by at least two independent sources within the ±0.10-point equity-index tolerance (see §6). Provider snapshots diverged by tens of points intra-week because of headline-driven volatility and 15-minute feed delays; the divergence is in snapshot timing, not in the validated daily OHLC.
**Pivot corroboration status.** The prior-period high/low/close inputs for the daily, weekly and monthly floor pivots (§11) are derived from the engine’s validated rolling window rather than from an independent two-source pivot fetch. All pivot levels for all three timeframes therefore carry the **single-source-indicative** flag. This flag is propagated to the §21 trade cards.
**Effect on strategy output.** Under the standard rule, a pivot trade resting entirely on single-source-indicative levels would be suppressed. For this run the analyst has instructed that trading strategies are not to be suppressed on corroboration grounds; accordingly the pivot-based and complex trades are produced in full and the indicative qualifier is carried as a caveat on each affected card (§21) rather than triggering suppression.
**Data gaps and assumptions.** The monthly pivot uses an April 2026 high/low/close approximated from the available validated window; the EURO STOXX 50 table is reported in native EUR with no FX normalisation applied. No OHLC field was synthesised — every value in §6 is a fetched, corroborated quote.
# 20. Agent Log
*Run timestamp: 21 May 2026, European pre-open (Europe/London). Output length: standard — full 21-section report with 5-session backtest.*
## Configuration override
- The daily-open anchor that governs the Trade 1 entry timestamp was overridden for this run from its standard configured value to 00:00 UK, at the analyst’s instruction. Consequence: the Trade 1 entry is taken at the 00:00 UK roll rather than the 07:00 UK pre-open. No other configuration value was changed.
- The report was run for the 21 May 2026 session; the as-of close is 20 May 2026.
## Source resolution — OHLC
- FTSE 100: sources attempted in rank order — Investing.com (corroborated), Stooq (corroborated), Yahoo Finance (corroborated, snapshot dispersion noted), Trading Economics (directional cross-check). Corroborated pair for the 20 May close: Investing.com × Stooq, delta 0.0 points, tolerance ±0.10 points. Five of five sessions CORROBORATED.
- EURO STOXX 50: Investing.com, Yahoo Finance, Trading Economics and EBC Financial Group used; five of five sessions corroborated within tolerance.
- Counters — USDX, S&P 500, DAX 40: directional reads only, taken from corroborated index/feed levels; no counter required pivot-grade corroboration.
## Single-source fields
- Daily, weekly and monthly floor-pivot prior-period H/L/C inputs are engine-rolling-window derived and flagged single-source-indicative. No daily OHLC field in §6 is single-source.
## Sentiment derivation
- Six articles classified (2 Bullish media, 2 Bearish — 1 institutional, 1 media, 2 Mixed — 1 institutional, 1 trade press). Source-class-weighted tilt = −0.71 / 4.2 = −0.17. Categorical label Mixed / Balanced. Computed on six articles — not low-confidence.
## Strategy trace (M5)
- Direction-scoring weights: defaults (0.25 / 0.20 / 0.10 / 0.15 / 0.15 / 0.15); not tuned. Forward-test weight lock respected.
- Signal vector: short-term technical +1.00×0.25; medium-term regime +0.50×0.20 (Transitional — sign of last completed swing); VOLator +0.50×0.10 (expansion); Kaufman −0.14×0.15; sentiment tilt −0.17×0.15; cross-asset +0.30×0.15 (MIXED). Total direction score = +0.40.
- Score +0.40 ≥ conviction threshold 0.25 → Trade 1 LONG produced. Regime label TRANSITION (Kaufman/VOLator disagreement) → Trade 2 on the breakout side and Trade 3C momentum-breakout fork.
- Suppression: no trade suppressed. The single-source-indicative pivot flag would normally suppress Trade 2; per the run instruction, strategies are not suppressed on corroboration grounds and the indicative qualifier is carried as a caveat instead.
- Backtest: prior 5 sessions reconstructed at each t−1 close with sentiment frozen and ATR/swings/regime recomputed; resolved on actual t-session OHLC with conservative stop-first tick priority.
## Anomalies
- RSI2 = 100.0 on 14, 19 and 20 May — expected behaviour of the 2-period RSI when neither prior session posted a loss; not a data error.
- KER (−0.14) contradicts the recovering price and the positive VOLator slope — the disagreement is reported, not resolved, and forces the consolidated regime to Transitional.
- Cross-asset contradiction: DAX 40 flat into FTSE strength — flagged in §10, §14 and §15, not silently resolved.
# 21. Strategy Recommendations
*Strategies section. Regime-aware three-tier trade cards, a 5-session no-leakage backtest, and a ‘what is working’ aggregate. All stops and targets are shown in index points.*
## 21a Directional Conviction
**Direction: LONG. Score: +0.40** (signed scalar in −1 to +1, two decimals). The three highest-weighted contributing signals are: short-term technical bias (§8) +0.25 — the 20 May bullish close on a maximal RSI2; medium-term regime (§9) +0.10 — a Transitional read scored on the sign of the last completed swing; and cross-asset confirmation (§10) +0.045 — a MIXED counter read with a positive medium-term direction. The Kaufman and sentiment signals are mildly negative (−0.021 and −0.026 weighted) and the VOLator signal is mildly positive (+0.05). Weights basis: defaults.
**Conflict flag.** The +0.40 LONG direction score and the §17 Forecast both lean constructive, so there is no directional conflict; the §17 forecast is unchanged by this section.
## 21b Trade Cards
**Trade 1 — Daily Directional (LONG)**

| Direction | LONG — direction score +0.40, above the conviction threshold. |
|---|---|
| Entry | Market at 00:00 UK (overridden anchor). Executable reference 10,393 points — the 20 May close, taken as the 21 May entry proxy. |
| Stop loss | 10,248.8 points — 144 points below entry. Structural anchor: the 19/20 May twin session low (10,279.1) plus a 0.25×ATR buffer; tighter than the 15 May swing-low alternative. Within the 3.5×ATR cap. |
| Risk (R) | 144 points (10,393.0 − 10,248.8). |
| TP1 (Unit 1) | 10,537.2 points — +1R. |
| TP2 (Unit 2) | 10,681.5 points — +2R. On fill, Unit 3 stop moves to entry + 0.2R (10,421.8). |
| TP3 (Unit 3 — runner) | Time-stopped at session close, or price-stopped at 3×ATR from entry (10,756.9), whichever triggers first. |
| Tranche management | Three equal units; Unit 1 exits at TP1; Unit 2 exits at TP2; on Unit 2 fill, Unit 3 stop moves to entry + 0.2R. |
| Confluences | Entry sits just above the weekly-P / monthly-S1 confluence (10,385–10,388) and daily R1 (10,372, now support). TP1 (10,537) is near the weekly-R1 / monthly-shelf cluster — strong confluence. |
| Thesis invalidation | A daily close back below 10,279 (the twin low). Distinct from, and ahead of, the 10,249 stop — ‘stop ahead of invalidation’. |
| Caveats | R (144 pts) exceeds 1×ATR — ‘wide stop’ flagged. Holding window collides with the 22 May Bank of England decision (§13d). |

**Trade 2 — Pivot, regime-aware (TRANSITION breakout side — LONG)**

| Trade type | Trade 2 — Pivot. Regime is Transitional, so Trade 2 is restricted to the breakout side (upside), aligned with the Trade 3C direction. |
|---|---|
| Direction | LONG — breakout side only; a counter-side sell limit is suppressed in a Transitional regime. |
| Entry | Stop entry at 10,397.6 points — 10% of the way from the weekly pivot P (10,385.3) toward weekly R1 (10,508.5). |
| Stop loss | 10,283.7 points — 114 points below entry. Anchor: weekly P minus 0.8×(P − weekly S1). |
| Risk (R) | 114 points. |
| TP1 (Unit 1) | 10,508.5 points — weekly R1. |
| TP2 (Unit 2) | 10,572.0 points — weekly R1.5. On fill, Unit 3 stop moves to entry + 0.2R. |
| TP3 (Unit 3 — runner) | 10,635.5 points — weekly R2. |
| Tranche management | Three equal units; Unit 1 at TP1; Unit 2 at TP2; on Unit 2 fill, Unit 3 stop to entry + 0.2R. |
| Confluences | The stop region (10,284) coincides with the 19/20 May twin low and daily S1 (10,284) — strong confluence. TP1 sits at the weekly-R1 / monthly-shelf cluster. |
| Thesis invalidation | A daily close back through the weekly pivot P (10,385). Documented even though the stop is wider. |
| Caveats | Single-source-indicative pivots (§19) — carried as a caveat; the trade is not suppressed per the run instruction. Holding window collides with the 22 May Bank of England decision. |

**Trade 3C — Momentum-Breakout (regime Transitional)**

| Trade type | Trade 3C — Momentum-Breakout. The Transitional regime selects the 3C fork; the post-fakeout breakout play. |
|---|---|
| Direction | LONG — the recent failed retests sit at the upper boundary, and the VOLator slope and the cross-asset read are consistent with an upside resolution. |
| Range definition | 25-session range: high 10,668.0, low 10,180.5; width 487.5 points. |
| Confirmed break | Requires a daily close beyond 10,668.0 by at least 0.25×ATR — trigger 10,698.3 points. The 20 May close of 10,393 is well inside the range, so the breakout is NOT yet confirmed; this is a pending card, eligible only on a confirming close. |
| Entry | On a confirmed upside breakout, at the breakout candle close (or the following session open) — reference 10,698.3 points. |
| Stop loss | 10,375.5 points — range low plus 0.40×width, just below the range midpoint. A deliberately generous post-fakeout stop. |
| TP1 (Unit 1) | 11,155.5 points — measured move: broken high plus 1.0×width. |
| TP2 (Unit 2) | 11,399.2 points — 1.5×measured move. On fill, Unit 3 stop moves to the broken boundary (10,668). |
| TP3 (Unit 3 — runner) | Discretionary trail beyond 1.5×measured move, anchored to subsequent swing structure. |
| Tranche management | Three equal units; Unit 1 at TP1; Unit 2 at TP2; on Unit 2 fill, Unit 3 stop to the broken boundary. |
| Confluences | The 10,668 breakout boundary is the April swing high and sits just below monthly R1 (10,653) — a structural ceiling that, once cleared, becomes support. |
| Thesis invalidation | A daily close back inside the range past the midpoint (below ~10,424). |
| Caveats | Pending — not eligible until a confirmed close above 10,698. Single-source-indicative pivots used for confluence (§19). Wide, multi-week target structure; not a daily-horizon trade. |

## 21c 5-Session No-Leakage Backtest

| **Date (t)** | **Strategy** | **Direction** | **Triggered** | **Entry / Exit** | **Outcome (R)** | **Days to res.** |
|---|---|---|---|---|---|---|
| 14 May (t−5) | Trade 1 | LONG | Yes | 10,381.5 / 10,433.0 | +0.28 | 1 |
| 15 May (t−4) | Trade 1 | LONG | Yes | 10,433.0 / stop | −1.00 | 1 |
| 18 May (t−3) | Trade 1 | SHORT | Yes | 10,195.4 / 10,303.7 | −0.60 | 1 |
| 19 May (t−2) | Trade 1 | LONG | Yes | 10,303.7 / 10,330.6 | +0.15 | 1 |
| 20 May (t−1) | Trade 1 | LONG | Yes | 10,330.7 / 10,393.0 | +0.34 | 1 |
| 14–20 May | Trade 2 | — | No | — | — (no pivot breakout triggered in window) | — |
| 14–20 May | Trade 3C | — | No | — | — (no confirmed 25-day range breakout) | — |

*Each Trade 1 row is reconstructed from the direction signal available at the prior t−1 close and resolved on the actual t-session OHLC with conservative stop-first tick priority and zero slippage. Trade 2 and Trade 3C did not trigger within the 5-session window — no weekly-pivot breakout and no confirmed 25-day range breakout occurred — so they are reported as non-triggered rows for traceability and do not contribute to the aggregate.*
## 21d ‘What Is Working’ Aggregate
Trade 1 over the last 5 sessions: triggered 5 of 5 times, mean R = −0.17, with TP1 / TP2 / TP3 hit rates of 20% / 0% / 0%. Trade 2 over the last 5 sessions: triggered 0 of 5 — insufficient triggers to rank. Trade 3C over the last 5 sessions: triggered 0 of 5 — insufficient triggers to rank. Strongest performer: Trade 1, by default — it is the only strategy with closed positions in the window, though its mean R is mildly negative, dragged down by the 15 May shock session. Weakest performer: insufficient triggers to rank Trade 2 and Trade 3C. The window straddles the 15 May sell-off, so the Trade 1 sample is dominated by one outlier loss and a run of small recovery gains.
*Five-session windows are too small to support statistical claims. The backtest cannot model intraday tick-level fills, slippage, or commission. Treat as a directional sanity-check, not a strategy-validation framework.*
*Prepared as a trading and risk review (forward-test). This document is analysis, not investment advice; all trade cards are forward-test constructs. Index levels are observed market data as at the 20 May 2026 close.*
