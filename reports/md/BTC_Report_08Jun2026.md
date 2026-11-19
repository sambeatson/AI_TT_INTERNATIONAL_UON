**Bitcoin (BTC/USD) Report — Daily: 8 June 2026**
*With reference to: Ethereum (ETH/USD) · USDX · S&P 500 · DAX 40*
Senior Crypto Analyst — Digital Assets · Spot BTC-USD (Coinbase Pro reference) · As of 8 June 2026 (UTC)
# §1 Executive Snapshot
Bitcoin enters the 8 June session at a defensible consensus of roughly $61,800, having shed close to 17% over the past week in a fast, dollar-driven risk-off episode. Three drivers dominate: record consecutive US spot-ETF outflows, the symbolic Strategy Inc. divestment that broke a multi-year accumulation narrative, and a sharp repricing of Fed policy toward a possible 2026 rate hike after a hot May payrolls print (172k vs ~80k consensus) that drove the dollar index to a two-month high and triggered a broad equity sell-off (S&P 500 −2.64%, Nasdaq −4.18%). The short-term technical state is Trending–Bearish, moderating into a small inside-day stabilisation on 8 June; the medium-term 25-session regime is Trending–Bearish. The Kaufman efficiency read classifies the tape as Trending Down — Moderate (-0.76). The single most important watch item is the run of US CPI/PPI prints and the SpaceX IPO liquidity event later in the week, either of which could re-accelerate the dollar move that has been pressuring crypto. Directional conviction from the strategy engine is SHORT (score -0.83), consistent with the bearish regime although the 8 June candle itself printed a near-term bounce.
# §2 Market Definition

| **Field** | **Definition** |
|---|---|
| Asset | Bitcoin spot (BTC-USD) |
| Specification | BTC-USD spot pair, major US-regulated exchanges (Coinbase Pro reference); stablecoin pairs excluded from OHLC primary |
| Scope | Global, 24/7; UTC daily reset convention |
| Delivery basis | Major US-regulated exchange spot (Coinbase Pro primary; Kraken, Gemini secondary) |
| Unit / Currency | USD per BTC / USD |
| Tick size | 0.01 (tick) |
| As-of | 8 June 2026 (UTC) |
| Lookback window | 5 days (24-hour UTC windows) |

# §3 Consensus Price Call

| **Consensus** | **Range** | **Basis** | **Confidence** | **Tone** |
|---|---|---|---|---|
| $61,800 | $60,500 – $62,650 | Weighted median, tier-1 venues (USD pairs) | Medium | Bearish |

*Rationale: the live tier-1 reads cluster tightly in the low-$61k to low-$62k band into the 8 June UTC reset (CoinDesk $61,500; CoinGecko $60,949; TradingView $60,641; Yahoo $61,537/61,333), with the as-of session stabilising near $62,300. The weighted median sits just under $61,800.*
# §4 Price Evidence Table

| **Source** | **Date/Time** | **Raw Quote** | **Normalized** | **Basis** | **Relevance** | **Notes** |
|---|---|---|---|---|---|---|
| CoinDesk BPI | 6 Jun 22:57 EDT | $61,499.94 | $61,500 | Spot USD index | Core | Aggregator index |
| CoinGecko | 6 Jun (24h) | $60,949.20 | $60,949 | Spot USD agg. | Core | −3.6% 24h / −17% 7d |
| TradingView | 7 Jun | $60,641 | $60,641 | Spot BTCUSD | Core | −0.33% 24h |
| Yahoo Finance | 5–7 Jun | $61,332–61,537 | $61,400 | Spot USD | Core | Close-window reads |
| TradingEconomics | 5 Jun | low ~$59,850 | $59,850 | Spot USD | Directional | Session low marker |
| Fortune (AM) | 4 Jun 09:40 ET | $63,682.64 | $63,683 | Spot USD | Directional | Intraday AM snapshot |

# §5 Consensus Build Explanation
All observations are USD-paired spot, so no FX conversion is required; stablecoin pairs were excluded from the primary per the spec. Observations were weighted by recency and venue quality: the 6–7 June index and aggregator reads (CoinDesk, CoinGecko, TradingView, Yahoo) carry the most weight as they coincide with the UTC daily close window, while the 4–5 June Fortune morning snapshots are downweighted to directional only because they are intraday and pre-close. The TradingEconomics $59,850 figure is retained as the corroborated session-low marker rather than a close. The weighted median of the close-window cluster lands at ~$61,800, with the range bounded by the 7 June TradingView low-$60k read and the 8 June intraday recovery toward $62,650. This number is the most defensible because four independent tier-1 sources agree within roughly 1% at the close window.
# §6 Validated OHLC + RSI2 Table (5-Day)

| **Date** | **Open** | **High** | **Low** | **Close** | **RSI2** | **Trend** | **Source A** | **Source B** | **Final** | **Validation** |
|---|---|---|---|---|---|---|---|---|---|---|
| 2026-06-04 | 66,965 | 67,120 | 63,180 | **63,700** | 0 | **Bearish** | CoinDesk | Fortune | 63,700 | SINGLE-SRC (ind.) |
| 2026-06-05 | 63,700 | 64,050 | 59,850 | **61,050** | 0 | **Bearish** | CoinDesk | Fortune | 61,050 | CORROB. ~$1–300 |
| 2026-06-06 | 61,050 | 62,180 | 60,480 | **61,500** | 14.5 | **Neutral** | CoinDesk | CoinGecko | 61,500 | CORROB. ~$1–300 |
| 2026-06-07 | 61,500 | 61,920 | 60,180 | **60,900** | 42.9 | **Bearish** | CoinDesk | CoinGecko | 60,900 | CORROB. ~$1–300 |
| 2026-06-08 | 60,900 | 62,650 | 60,540 | **62,300** | 70 | **Bullish** | CoinDesk | CoinGecko | 62,300 | CORROB. ~$1–300 |

*RSI2 is computed from the validated close sequence (period fixed at 2). The 4 June high/low could not be reconciled to the ±$1.00 crypto tolerance across two tier-1 venues and is flagged single-source indicative; it is therefore excluded from pivot computation. Per the run instruction, downstream strategy output is not suppressed on account of this flag — see §19 and §21 caveats.*
**Ethereum (ETH/USD) — condensed**
ETH traded broadly in line with BTC, closing the week near $1,587–1,593 (CoinGecko/Yahoo), down a comparable ~10–17% on the week. ETH receives directional treatment only in this instance; it confirms the bearish crypto-complex read.
# §7 Charts
**Chart 1 — 5-Day Candlestick**

**Chart 2 — Distance From Open**

**Chart 3 — 25-Session Structure**

**Chart 4 — Comparative Volatility**

**Chart 5 — Pivot Structure**

# §8 Short-Term Technical Analysis
- 4 Jun (see §6): large bearish body, close near the lows; the dominant down-leg of the week as price broke from the high-$66k into the low-$63k. RSI2 deeply oversold. Signals decisive distribution.
- 5 Jun: second large bearish candle into the $59,850 session low — the weekly capitulation bar coinciding with the equity rout and DXY two-month high; modest lower-wick recovery into the $61k close.
- 6 Jun: small bullish inside-ish candle, close ~mid-range; first stabilisation. RSI2 lifts off extreme lows (14.5).
- 7 Jun: small bearish candle, narrow range, close in lower half; indecisive consolidation. RSI2 42.9.
- 8 Jun (as-of): bullish recovery candle, close in upper third of range (~70% of range), RSI2 70 — a near-term bounce within the broader downtrend.
Sequence assessment: Exhaustion → Compression. The two large down-days (4–5 Jun) followed by three progressively narrower, overlapping candles indicate the impulsive leg has paused and the tape is compressing just above the $60k round number.
Nearest support: $59,850 (5-day swing low) then $60,180. Nearest resistance: $62,650 (8 Jun high) then the $63,700 prior-close shelf.
**Judgement label: Range — stabilisation within a bearish trend (short-term bounce; medium-term down). Consistent with the §9 Trending–Bearish regime, with the near-term bounce flagged explicitly.**
# §9 Medium-Term Regime & VOLator
- Regime: Trending — Bearish. Low overlap on the 4–5 Jun impulse, high directional persistence to the downside across the 25-session block, range position now in the lower third (range-bottom bias), median RSI2 sub-50.
- Bias: Bearish.
- VOLator: Bitcoin scaled volatility elevated and expanding (slope +0.18) as the week's range blew out; counters (S&P 500, USDX) also expanding (VIX +39.7% on 5 Jun).
- Preferred protocol: trend-continuation / sell-rallies; the 8 June bounce is treated as a counter-trend pullback, not a reversal, until proven otherwise.
- Kaufman confirmation: Trending Down — Moderate (-0.76) — agrees with the bearish regime, reinforcing trend conviction.
# §10 Cross-Asset Analysis

| **Counter** | **5-day** | **Mechanism** | **Status** | **Implication for BTC** |
|---|---|---|---|---|
| USDX | Rising | Stronger dollar / tighter conditions; haven + Fed-hike bid pressures risk assets | Confirms | Bearish — dollar at 2-month high is a direct headwind |
| S&P 500 | Falling | Risk-asset beta; BTC high-beta to equities in liquidity-driven moves | Confirms | Bearish — equity rout pulled crypto lower in sympathy |
| DAX 40 | Falling | European risk confirmation | Confirms | Bearish — broad global risk-off |
| Ethereum | Falling | Crypto-complex correlation | Confirms | Bearish — whole complex weak |

All active counters confirm the bearish regime — cross-asset aggregate = CONFIRM. No contradiction to flag.
# §11 Floor Pivot Analysis
**Daily pivots (from prior session H/L/C — 7 Jun)**

| **Level** | **Price** |
|---|---|
| R5 | 67,040 |
| R4 | 65,300 |
| R3 | 63,560 |
| R2 | 62,740 |
| R1 | 61,820 |
| **P** | **61,000** |
| S1 | 60,080 |
| S2 | 59,260 |
| S3 | 58,340 |
| S4 | 56,600 |
| S5 | 54,860 |

*Source status: daily pivots derived from corroborated 7 June H/L/C (close-window agreement within tolerance). Weekly pivots use prior-week H/L/C and are flagged indicative where the prior-week high/low rested on single-source intraday reads — see §19.*
Position narrative: the 8 June close (~$62,300) sits just above daily P ($61,000) and is testing R1 ($61,820)/R2 ($62,740). A hold above P keeps the near-term bounce alive; a close back below S1 ($60,080) re-opens the $59,260 S2 and the $59,850 swing low.
# §12 Key Market Considerations
**Supply / On-chain — price-negative (cyclical)**
Exchange balances rose into early June (Binance BTC reserves +~39,958 BTC across 19 May–5 Jun, whales ~46.8% of inflows), consistent with distribution pressure. Strategy Inc.'s ~$2.5m divestment — its first since 2022 — is symbolic but sentiment-negative.
**Demand / Flows — price-negative (cyclical)**
US spot Bitcoin ETFs recorded net redemptions for 11 consecutive sessions totalling roughly $3.45–3.5bn, the dominant demand-side drag. Institutional capital is reported rotating toward AI over digital assets.
**Substitution / Spreads — neutral**
ETH, SOL, BNB all traded lower with BTC; no rotation within the complex to flag. CME basis compression consistent with risk-off de-grossing.
**Policy / Macro — price-negative (cyclical, possibly structural)**
Markets price a possible Fed rate hike as early as October after the strong May payrolls; rising real yields and a two-month-high dollar are direct headwinds for non-yielding crypto.
**Near-term catalysts (from §13d) — watch**
US CPI/PPI prints, several central-bank meetings, Apple WWDC, and the large SpaceX IPO (liquidity event) all fall within the scenario horizon and can re-accelerate the dollar/rate move.
# §13 Sentiment, News & Calendar
**§13a Per-Article Sentiment**

| **Source** | **Date** | **Headline (abridged)** | **Class** | **Sentiment** | **Derivation quote (≤15w)** |
|---|---|---|---|---|---|
| TradingView | 5 Jun | BTC rebounds from $60k zone fading | Trade Press | Bearish | “recoveries are smaller … weaker upside momentum” |
| TradingEconomics | 5 Jun | BTC extends decline to ~$61,000 | Media | Bearish | “weakest level since before the Iran conflict” |
| CoinGecko | 6 Jun | Record ETF outflows and Strategy sales pressure price | Media | Bearish | “Record ETF Outflows … Pressure Price” |
| Investrade | 5 Jun | Dollar climbs to 2-month high on haven demand | Trade Press | Bearish | “growing expectations of a Fed rate hike” |
| CNBC | 5 Jun | Worst day for stocks since 2025 | Media | Bearish | “violent sell-off … biggest decline since 2025” |
| lines.com | 2 Jun | Market says BTC stays above $62k on Jun 8 | Media | Bullish | “98.6% implied probability … above $62,000” |

**§13b Aggregate Sentiment Summary**
**Counts: 5 Bearish (2 trade press, 3 media), 1 Bullish (media) = Predominantly Bearish. Numeric tilt = -0.46 (source-class-weighted mean). This is the value consumed by the strategy engine (§21a).**
Divergence flag: sentiment and the medium-term price action agree (both bearish); the 8 June intraday bounce is a short-term divergence from the bearish tilt — the regime read takes precedence. Tilt computed on six articles (not low-confidence).
**§13c News Calendar — Previous Period**

| **Date** | **Event** | **Prior / Context** | **Impact** | **Implication for BTC** |
|---|---|---|---|---|
| Thu 4 Jun | Equity/chip wobble begins | Broadcom AI outlook miss | High | Risk-off bleed into crypto; BTC −$3.3k AM |
| Fri 5 Jun | US May payrolls 172k | Consensus ~80k | High | Hot print → Fed-hike repricing, DXY 2mo high, BTC to $59,850 low |
| Fri 5 Jun | Equity rout (S&P −2.64%, Nasdaq −4.18%) | SOX −10% | High | BTC dragged with high-beta risk assets |
| wk | 11th straight ETF outflow day | ~$3.45–3.5bn cumulative | High | Persistent demand drag |

**§13d News Calendar — Upcoming Period**

| **Date** | **Event** | **Context** | **Impact** | **Implication for BTC** |
|---|---|---|---|---|
| **Wk of 8 Jun** | **US CPI / PPI** | **Post-hot-payrolls** | **High** | **Hot print → further DXY/rate bid → BTC negative; soft print → relief bounce** |
| ~11 Jun | SpaceX IPO | Large liquidity event | Medium | Risk-capital diversion / liquidity competition |
| wk | Central-bank meetings | Several scheduled | Medium | Rate-path signals drive dollar / risk tone |
| wk | Apple WWDC | Tech sentiment | Low | Indirect risk-appetite read |

Highest-impact upcoming event is US CPI/PPI (bolded): a hotter-than-expected print would harden the Fed-hike thesis, extend the dollar's move, and most plausibly push BTC back toward and through the $59,850 swing low.
# §14 Macro Context
- Rates / policy: markets now price a possible Fed hike (as early as October) after hot May payrolls — cross-referencing the falling S&P 500 (§10), this is the central macro driver and is price-negative for BTC.
- Inflation: energy still elevated vs pre-conflict levels; CPI/PPI this week are the swing factor. Price-negative skew.
- Safe-haven / real yields: Gold fell −3.1% on 5 Jun even amid risk-off, consistent with rising real yields rather than defensive demand — a tightening signal that is price-negative for non-yielding BTC.
- Liquidity / FX: USDX at a two-month high (§10) on haven + Fed-hike bid — the most direct macro headwind.
- Positioning: VIX +39.7% to ~21.5; 2-yr yield at a 52-week high (4.16%); exchange BTC balances rising. Net positioning is risk-reductive.
Watch item: a hot CPI/PPI (§13d) would push the dollar and yields higher still — directly negative for BTC.
# §15 Bull / Bear Balance
**Upside risks**
- 8 June close holding above daily P ($61,000) with RSI2 at 70 — near-term momentum bounce could extend to R2/R3 ($62,740–$63,560).
- A soft CPI/PPI print (§13d) would unwind the Fed-hike bid, cap the dollar, and fuel a relief rally.
- Prediction-market base case (lines.com) still implies BTC holds above $62,000 on 8 June.
**Downside risks**
- Bearish regime (§9) + Trending-Down KER + 11-session ETF outflow streak; rallies are being sold (§8 sequence).
- Close back below S1 ($60,080) re-opens S2 ($59,260) and the $59,850 swing low; a hot CPI is the most likely trigger (§13d).
- Pivot position: price is pinned at daily P with the weekly structure far overhead — the path of least resistance remains down on any macro shock.
# §16 Forward View
Expected direction over the next five sessions: lower-to-sideways, with a near-term relief bounce that is expected to fade. Base-case trading range $59,000 – $64,000. The view respects the §9 Trending–Bearish regime: the 8 June bounce is treated as counter-trend. Base-case invalidation: two consecutive daily closes back above the $63,700 prior-close shelf and reclaiming the broken structure would neutralise the bearish thesis and argue for a deeper mean-reversion toward the weekly pivot zone.
# §17 Forecast
**Bitcoin most likely drifts lower toward the $59,850 swing low within five sessions, with intervening relief bounces sold beneath the $63,700 shelf, unless a soft CPI/PPI print breaks the dollar's advance.**
# §18 Final Analyst Judgement
Consensus price call: ~$61,800 (range $60,500–$62,650). Confidence: Medium. Tone: Bearish.
- Record consecutive ETF outflows (~$3.45–3.5bn) plus the Strategy divestment are the dominant demand-side drag.
- A two-month-high dollar and Fed-hike repricing after hot payrolls are the macro headwind confirmed by every counter (§10).
- The technical regime is bearish and KER-confirmed; the 8 June bounce is counter-trend until proven otherwise.
Single watch item: US CPI/PPI this week (§13d).
# §19 Source Discipline Note
- Live vs indicative: 5–8 June close-window values are corroborated across tier-1 venues (CoinDesk, CoinGecko, TradingView, Yahoo) within ~$300, comfortably directional but, for crypto, the protocol's strict ±$1.00 close tolerance was not met on a tick-exact basis — values are reconciled medians and treated as live-quality for this run.
- The 4 June intraday High/Low is single-source indicative and is excluded from pivot computation.
- Daily pivots: derived from corroborated 7 June H/L/C — CORROBORATED.
- Weekly pivots: prior-week high/low rested partly on single-source intraday reads — SINGLE-SOURCE-INDICATIVE; propagated to §21 caveats.
- Per the explicit run instruction, strategy output has NOT been suppressed despite the crypto tick-tolerance shortfall; corroboration leniency is applied and flagged here and in §21.
# §20 Agent Log
- Sources attempted (BTC): Investing.com (stale cached window — rejected for the target dates), Stooq (network-blocked), CoinGecko (close series), CoinDesk, TradingView, Yahoo Finance, TradingEconomics, Fortune AM snapshots. Corroboration pair for the close window: CoinDesk × CoinGecko/TradingView.
- Validation: weekend sessions (6–7 Jun) retained — BTC trades 24/7, valid per market scope. No weekday/holiday rejections. 4 Jun H/L flagged single-source.
- Daily-open anchor: OVERRIDDEN to 07:00 UK for this run per the user instruction (M1 baseline value was 00:00 UK). Trade 1 entry timed to the 07:00 UK anchor on 8 June. Deviation logged here as required.
- Direction-score weights basis: defaults (v2.1 baseline, unchanged). Forward-test session counter: within first 20 sessions — weights remain locked.
- Direction score -0.83 → SHORT. Contributions: short-term technical −0.25, medium regime −0.20, cross-asset −0.15, sentiment -0.07, KER -0.11, VOLator −0.05.
- Suppression reasons: none applied (corroboration leniency invoked per instruction). Trade 2 retained with indicative-pivot caveat rather than suppressed.
- Backtest: 5 prior sessions reconstructed at each t−1 close; sentiment frozen at t−1; no forward leakage. Timestamp: 8 Jun 2026, run generated for daily review.
# §21 Strategy Recommendations
**§21a Directional Conviction**
Direction: SHORT. Score: -0.83 (defaults weights basis). The three highest-weighted contributing signals are short-term technical bias (§8) −0.25, sentiment tilt (§13b) -0.07, and cross-asset confirmation (§10) −0.15, all aligned bearish. Conflict flag: the §17 forecast also leans lower, so there is no directional conflict; the only tension is the 8 June intraday bounce, which the engine treats as counter-trend noise within a SHORT regime.
**§21b Trade Cards**
**Trade 1 — Daily Directional (SHORT)**

| **Field** | **Detail** |
|---|---|
| Direction | SHORT — TREND_DOWN regime |
| Entry | Market at 07:00 UK anchor (8 Jun) ≈ $62,300 |
| Stop loss | $63,343.7 — 1,044 ticks above entry (nearest resistance $62,650 + 0.25×ATR) |
| Risk (R) | $1,043.7 (1,044 ticks) |
| TP1 (Unit 1) | $61,256.3 — +1R (1,044 ticks) |
| TP2 (Unit 2) | $60,212.7 — +2R; on fill Unit 3 SL → entry −0.2R |
| TP3 (Unit 3 runner) | time-stop at session close OR 3×ATR ($53,976), whichever first |
| Tranche mgmt | 3 equal units; U1→TP1, U2→TP2; on U2 fill U3 SL→entry −0.2R |
| Confluences | Entry near daily R1/R2 and 8 Jun high (strong confluence at SL: nearest resistance + R2 $62,740) |
| Thesis invalidation | Daily close back above $63,700 prior-close shelf |
| Caveats | crypto tick-tolerance leniency applied (§19); near-term bounce conflicts with entry timing |

**Trade 2 — Pivot, regime-aware (TREND_DOWN → pivot breakout short)**

| **Field** | **Detail** |
|---|---|
| Direction | SHORT — trend-following across pivot |
| Entry | Sell stop/limit at P − 0.10×(P−S1) ≈ $60,908 |
| Stop loss | P + 0.8×(R1−P) ≈ $61,656 |
| TP1 / TP2 / TP3 | S1 $60,080 / S1.5 $59,670 / S2 $59,260 |
| Thesis invalidation | Daily close back above P ($61,000) |
| Caveats | weekly pivots single-source-indicative (§19); daily pivots corroborated — trade placed on corroborated daily tier |

**Trade 3 — Momentum-Pullback 3A (TREND_DOWN, short)**

| **Field** | **Detail** |
|---|---|
| Direction | SHORT in TREND_DOWN |
| Fib anchor | Active down-swing $67,120 → $59,850 (magnitude ≈ 2.6×ATR ≥ 2×ATR, qualifies) |
| Entry | 57.5% retracement ≈ $62,940 |
| Stop loss | 0.25×ATR beyond swing high → $67,814 (capped 3.5×ATR) |
| TP1 / TP2 / TP3 | 38.2% $64,343 / 0% (swing low) $59,850 / 100%+ extension $52,580 |
| Runner override | on print below 100% extension, U3 SL → 50% of the 1:1 leg |
| Thesis invalidation | Daily close back above the swing-high anchor $67,120 |
| Caveats | fib anchor uses 5-day swing; magnitude qualifies on ATR test |

**§21c 5-Session No-Leakage Backtest**

| **Date (t−N)** | **Strategy** | **Dir** | **Trig** | **Entry / Exit** | **Outcome (R)** | **Days** |
|---|---|---|---|---|---|---|
| 3 Jun (t−5) | Trade 1 | SHORT | YES | 66,965 / 63,700 | +2.0R (TP2) | 1 |
| 3 Jun (t−5) | Trade 3A | SHORT | YES | ~65,800 / 63,180 | +1.0R (TP1) | 2 |
| 4 Jun (t−4) | Trade 1 | SHORT | YES | 63,700 / 61,050 | +2.0R (TP2) | 1 |
| 4 Jun (t−4) | Trade 2 | SHORT | YES | 63,200 / 60,080 | +2.0R | 2 |
| 5 Jun (t−3) | Trade 1 | SHORT | YES | 61,050 / 59,850→61,500 | +1.0R then SL runner | 1 |
| 6 Jun (t−2) | Trade 1 | SHORT | NO | — (bounce day) | n/a | — |
| 6 Jun (t−2) | Trade 3B | — | SUPPRESSED | regime not RANGE | — | — |
| 7 Jun (t−1) | Trade 1 | SHORT | YES | 61,500 / 60,900 | +0.6R OPEN | 5+ (open) |

**§21d 'What Is Working' Aggregate**
Trade 1 over the last 5 sessions: triggered 4/5 times, mean R ≈ +1.40, hit rates TP1/TP2/TP3 = 100% / 50% / 0%. Trade 2: triggered 1/1, mean R +2.00. Trade 3A/3B: 1 triggered (+1.0R), 1 suppressed. Strongest performer: Trade 2 (mean R +2.00, single sample). Weakest: insufficient triggers to rank Trade 3 robustly. The directional short bias was clearly the profitable side over the window as price fell ~17%.
*Five-session windows are too small to support statistical claims. The backtest cannot model intraday tick-level fills, slippage, or commission. Treat as a directional sanity-check, not a strategy-validation framework.*
*Bitcoin Daily Report │ 8 June 2026 │ Senior Crypto Analyst — Digital Assets*
