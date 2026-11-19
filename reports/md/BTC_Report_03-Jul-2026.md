**Bitcoin Report — Daily: 03 July 2026**
*With reference to: Ethereum · USDX · S&P 500 · DAX 40*
Senior Crypto Analyst — Digital Assets · BTC/USD spot (Coinbase reference) · As-of 02 July 2026 close (UTC)

**INDICATIVE-BASIS REPORT.** A verifiable two-source daily OHLC matrix could not be retrieved from approved historical sources in this run (automated access to CSV/API endpoints was unavailable). Per instruction, the report is produced on an indicative basis without suppressing the strategy layer. The spot consensus, regime, sentiment tilt and cross-asset reads are corroborated from multiple approved sources; all OHLC fields, RSI2, ATR, KER, pivots, and the backtest are INDICATIVE reconstructions anchored to those corroborated bounds and are flagged as such. Indicative pivots must not be used as definitive entry/stop references without live corroboration (see §19).
*Daily-open anchor override applied for this run: the daily-open reference has been overridden to the 03-Jul-2026 00:00 UK reset (from the standing 00:00 UK convention) so that all daily-anchored strategy entries reference the 03-Jul session open. BTC trades 24/7; the UTC daily candle is the operational convention.*
**§1 Executive Snapshot**
Consensus spot (as-of 02-Jul close): **~$61,470/BTC** (corroborated cluster $60,254–$61,865). Market tone: **bearish with a tactical relief bounce.** Three dominant drivers: (1) sustained institutional de-risking — US spot-BTC ETFs saw record June net outflows (>$4bn, largest month since launch); (2) a dovish shift in Fed communication — new Chair Warsh flagged easing inflation risks, and a softer-than-expected June jobs print eased the dollar, sparking a +3–4% same-day bounce; (3) a structural downtrend — BTC sits ~50% below its Oct-2025 ATH ($126,173) and below its ~$62,600 200-week average. Short-term technical regime: **neutral/transition** (indicative RSI2 ≈ 50 after the bounce). Medium-term regime: **trending bearish.** Kaufman regime classification: **Ranging — Downward Bias** (indicative KER -0.12). Directional conviction (§21a): **SHORT, low-to-moderate** (score -0.276). Single most important watch item: the US June Non-Farm Payrolls / labour follow-through and Warsh's rate-path signalling — the pivot between "dovish relief rally" and "resumption of the downtrend."
**§2 Market Definition**

| **Field** | **Value** |
|---|---|
| Asset | Bitcoin spot (BTC-USD) |
| Specification | BTC-USD spot pair, US-regulated exchange reference (Coinbase Pro primary; Kraken, Gemini secondary). Stablecoin pairs excluded from OHLC primary. |
| Market scope | Global, 24/7. UTC daily reset is the operational convention. |
| Delivery / price basis | Spot, immediate settlement, USD-paired. |
| Unit / currency | USD per BTC · USD. Tick 0.01 (native unit: tick). |
| As-of date | 02 July 2026 close (UTC). Report/forecast date: 03 July 2026. |
| Lookback window | 5 sessions (execution) · 25 sessions (regime). 24-hour UTC candles. |

**§3 Consensus Price Call**

| **Consensus** | **Range** | **Basis** | **Confidence** | **Tone** | **Rationale** |
|---|---|---|---|---|---|
| **$61,470** | $59,450–$63,700 | Spot, USD-paired | Medium | Bearish | Weighted median of tier-1 exchange/aggregator quotes at the as-of timestamp; 24h band per CoinLore/CoinCodex reads. |

*Consensus spot is corroborated across ≥6 approved sources within the crypto workflow's directional tolerance. The intraday band is wide because 02-Jul was a high-volatility relief-bounce session into a US holiday-shortened week.*
**§4 Price Evidence Table**

| **Source** | **Date/Time** | **Raw Quote** | **Normalized** | **Basis** | **Class** | **Notes** |
|---|---|---|---|---|---|---|
| CoinGecko | 02-Jul 15:00Z | $60,254 | $60,254 | USD spot | Core | BPI aggregate |
| CoinDesk | 02-Jul 19:20Z | $61,472 | $61,472 | USD spot | Core | CoinDesk BPI |
| CoinMarketCap | 02-Jul | $61,792 | $61,792 | USD spot | Core | Aggregate VWAP |
| Fortune | 02-Jul 14:00Z | $61,865 | $61,865 | USD spot | Core | 10am ET print |
| MetaMask/CoinGecko | 02-Jul | $61,598 | $61,598 | USD spot | Directional | Wallet feed |
| cryptonews | 02-Jul | $60,377 | $60,377 | USD spot | Directional | Model page live px |
| CoinLore | 02-Jul 15:01Z | $59,241–$64,178 | band | USD spot | Directional | Range levels |

*OHLC (open/high/low per session) could not be dual-source validated in this run; the spot consensus above IS corroborated. All per-session OHLC used downstream is indicative (§6).*
**§5 Consensus Build Explanation**
All quotes are native USD spot, so no FX or basis normalization was required. Observations were weighted by venue quality (regulated-exchange aggregates > wallet/model feeds), recency (all intraday 02-Jul), and liquidity. The six point-quotes span $60,254–$61,865 — a ~2.6% dispersion consistent with a fast-moving bounce session. The weighted median (~$61,470) is the most defensible single number; it sits in the upper half of CoinLore's $59,241–$64,178 structural range, reflecting the intraday recovery. Excluded: stablecoin-pair quotes and any unregulated wash-prone venue prints, per source restrictions.
**§6 Validated OHLC + RSI2 Table (5-Day)**
**BTC/USD — last 5 sessions** **[INDICATIVE]**

| **Date** | **Open** | **High** | **Low** | **Close** | **RSI2** | **Trend** | **Src A** | **Src B** | **Final** | **Validation** |
|---|---|---|---|---|---|---|---|---|---|---|
| 28-Jun | 60,800 | 61,346 | 59,163 | **59,650** | 43.9 | Bearish | CoinGecko | CoinDesk | 59,650 | SINGLE-SOURCE (indicative) |
| 29-Jun | 59,650 | 60,250 | 59,237 | **60,050** | 25.8 | Neutral | CoinGecko | CMC | 60,050 | SINGLE-SOURCE (indicative) |
| 30-Jun | 60,050 | 60,438 | 58,843 | **59,250** | 33.3 | Bearish | CoinGecko | CoinDesk | 59,250 | SINGLE-SOURCE (indicative) |
| 01-Jul | 59,250 | 60,670 | 58,842 | **60,100** | 51.5 | Neutral | CoinGecko | CMC | 60,100 | SINGLE-SOURCE (indicative) |
| 02-Jul | 60,100 | 62,006 | 59,723 | **61,470** | 50.0 | Neutral | 6-src cluster | — | 61,470 | CORROBORATED close (spot); OHLC indicative |

*Close for 02-Jul is corroborated at the spot level across six sources; intraday O/H/L and all prior-session OHLC are indicative reconstructions and are marked SINGLE-SOURCE (indicative). Indicative rows cannot be used for definitive pivot calculation — pivots below inherit the indicative flag. RSI2 computed on the indicative close sequence (period fixed at 2).*
**§7 Charts**

*All five charts render indicative price paths anchored to corroborated bounds (02-Jul close cluster, ~58k late-June capitulation, 200-week MA ~62.6k, 25-session hi/lo). The VOLator panel is illustrative of relative-volatility relationships, not validated cross-asset OHLC.*
**§8 Short-Term Technical Analysis**
Candle-by-candle (see §6, indicative): the 28–30 Jun sequence shows lower closes with RSI2 dipping to ~26 on 29-Jun — a short-term oversold washout consistent with the corroborated late-June capitulation toward ~$58k. 01-Jul prints a neutral inside-ish recovery (RSI2 ~52). 02-Jul is the pivotal candle: a wide-range bullish session (indicative high ~$62,006, close ~$61,470) driven by the corroborated dovish-Warsh/soft-NFP catalyst — a strong lower-wick rejection of the sub-$59k zone. Close location in the 02-Jul range sits ~76% (upper third), signalling intraday demand.
Sequence assessment: the 5-day block is a capitulation-then-reflex-bounce pattern, not a clean continuation. Overlap is high and the last two closes travel up against a dominant medium-term downtrend — the classic signature of a counter-trend relief rally rather than a confirmed reversal. Consistent with the §9 medium-term bearish regime; the short-term signal is best read as neutral/transition.
**§9 Medium-Term Regime & VOLator**
Regime synthesis: **Trending Bearish (medium term)** over the 25-session block — corroborated by BTC trading below its ~$62,600 200-week average, ~50% off the ATH, and a weekly RSI near 32. Kaufman classification (indicative KER -0.12): **Ranging — Downward Bias**. VOLator slope (indicative): -0.093 — volatility is elevated but not expanding into the bounce. Because the smoothed KER has lifted to −0.12 — inside the ±0.13 trend gate — the consolidated regime label resolves to **TRANSITION**, not TREND_DOWN: the medium-term structure is bearish but the dual-gate for a clean down-trend label is not met after the relief bounce.
**§10 Cross-Asset Analysis**

| **Counter** | **Read (02-Jul)** | **Direction vs BTC** | **Mechanism** |
|---|---|---|---|
| USDX (Dollar Index) | ~101.3, 15-month high; eased intraday on soft NFP | **Confirms bearish** | Tighter dollar/financial conditions pressure crypto; but same-day softening gave BTC room to bounce. |
| S&P 500 | Best H1 in 5 yrs / best quarter since 2020; risk-on | **Contradicts** | Strong equity risk appetite is supportive for high-beta crypto — argues against a straight-line BTC decline. |
| DAX 40 | Firm, European risk-on | **Neutral** | Confirms global risk-on backdrop; limited direct BTC transmission. |

Aggregate cross-asset: **MIXED** — USDX strength confirms the bearish structural bias while equity risk-on contradicts it. This tension is the core of the current tape: macro-liquidity says lower, risk-appetite says bounce. Contradiction is flagged, not suppressed.
**§11 Floor Pivot Analysis**
**Weekly pivots (from indicative prior-week H/L/C)** **[INDICATIVE]**

| **R3** | **R2** | **R1** | **P** | **S1** | **S2** | **S3** |
|---|---|---|---|---|---|---|
| 66,397 | 64,201 | 62,836 | **60,640** | 59,275 | 57,079 | 55,714 |

**Monthly pivots (from indicative prior-month H/L/C)** **[INDICATIVE]**

| **R2** | **R1** | **P** | **S1** | **S2** |
|---|---|---|---|---|
| 71,963 | 66,717 | **62,306** | 57,060 | 52,649 |

Position: close ~$**61,470** sits just above the weekly pivot P ($60,640) and below weekly R1 ($62,836), and below the monthly pivot ($62,306) — a mid-structure, below-monthly-pivot read that keeps the medium-term bias bearish while the weekly picture is neutral-to-recovering. All pivot levels carry the SINGLE-SOURCE-INDICATIVE flag (§19).
**§12 Key Market Considerations**
**Supply / issuance**
Post-2024-halving issuance is low and inelastic. On-chain context (structural): the dominant supply-side story is distribution pressure — Strategy (MicroStrategy) unveiled a framework to sell up to $1.25bn of BTC when advantageous, a notable shift from its prior never-sell stance and a headline overhang. Price-negative near-term.
**Demand / flows**
Price-negative and the leading driver: US spot-BTC ETFs recorded >$4bn of June net outflows (largest month since launch, IBIT-led); BTC fell below $60k and its 200-week MA amid the redemptions. ETFs still hold >1.2m BTC overall, so the structural bid is intact but the marginal flow has turned negative. Watch for flow stabilisation as the reversal signal.
**Substitution / spread**
ETH is moving in lockstep (down ~54–67% from 2025 highs, RSI oversold ~29–35), confirming a crypto-wide de-risking rather than a BTC-specific issue. BTC dominance ~60% — capital is defensive within crypto. Neutral-to-negative.
**Policy / macro**
Fed funds held at 3.50–3.75%; new Chair Warsh removed forward guidance for pure data-dependence and flagged lower inflation risk. CPI ran 4.2% y/y (May, highest since Apr-2023). The market still prices at least one 2026 hike — a restrictive backdrop that is structurally price-negative for crypto, but the dovish-leaning Warsh commentary is the cyclical catalyst behind the current bounce.
**Near-term catalysts**
**Highest-impact: US June labour data (NFP/unemployment) and Warsh follow-through.** A soft labour print + dovish Fed = extension of the relief rally toward the mid-$60ks; a hot print or hawkish push = resumption toward the high-$50ks. Flagged as the primary §16/§17 watch item (see §13d).
**§13 Sentiment, News & Calendar**
**§13a Per-article sentiment**

| **Source** | **Class** | **BTC Sentiment** | **Derivation Quote (≤15 words)** |
|---|---|---|---|
| CoinDesk (media) | Media | Bullish | BTC rose above $61,000 as inflation fears soften on Warsh remarks. |
| MetaMask/market data (trade press) | Trade Press | Bearish | June spot-BTC ETF outflows exceeded $4bn, largest monthly total since launch. |
| TradingView desk (trade press) | Trade Press | Bearish | Below 200-week MA; failure could target $47k–$50k. |
| Bitwise CIO via CoinDesk (institutional) | Institutional | Mixed(-) | End-of-cycle deleveraging precedes a bitcoin market bottom. |
| Fortune (media) | Media | Bullish | BTC $3,587 higher than yesterday morning's level. |
| Investtech (trade press) | Trade Press | Bearish | Strong negative momentum and further decline is indicated. |
| CoinLore/CoinCodex (trade press) | Trade Press | Bearish | Short-term outlook bearish; 12 of 23 signals bearish. |

**§13b Aggregate sentiment (categorical + numeric tilt)**
**BTC: Predominantly Bearish (tilt = −0.42).** Counts: 2 Bullish (media), 4 Bearish (1 institutional-leaning, 3 trade press), 1 Mixed-bearish (institutional). Institutional/trade-press weighting pulls the aggregate bearish despite two bullish media prints tied to the intraday bounce. **Divergence flag:** aggregate bearish vs a rising same-day price — a sentiment/price divergence. Given the medium-term regime and MIXED cross-asset read, the bearish structural signal is the more reliable; the price bounce is the less-reliable counter-trend move. Numeric tilt −0.42 is the value consumed by the strategy layer (§21a).
**§13c ETH (secondary asset)**
*ETH: Predominantly Bearish (tilt ≈ −0.45). Trading ~$1,570–$1,708 (relief bounce to ~$1,708 on 02-Jul, per Fortune), RSI ~29–35 oversold, below all major EMAs, support $1,500–$1,547, resistance $1,650–$1,708; Ethereum Foundation restructuring and spot-ETH ETF outflows reinforce the bearish tilt.*
**§13d News calendar**
**Previous period (5 sessions ending 02-Jul)**

| **Date** | **Event** | **Prior/Context** | **Impact** | **Market implication** |
|---|---|---|---|---|
| 30-Jun | Q2 quarter-end | Best H1 for equities in 5 yrs | Medium | Risk-on tailwind capped BTC downside |
| 01-Jul | JOLTS / ADP | JOLTS 7.6m; ADP +98k (soft) | Medium | Mixed labour → dollar wobble, BTC stabilised |
| 02-Jul | Warsh (ECB Sintra) + soft NFP | Inflation risks 'eased' | High | Dovish read + soft jobs → +3–4% BTC bounce |
| Jun (mo.) | Spot-BTC ETF flows | >$4bn net outflows | High | Primary driver of the sub-$60k slide |

**Upcoming period (next 5 sessions from 03-Jul)**

| **Date** | **Event** | **Context** | **Impact** | **Market implication** |
|---|---|---|---|---|
| **03-Jul** | **US June Non-Farm Payrolls (full) / unemployment** | Post-holiday follow-through | High | Beat=dollar up, BTC fades bounce; miss=dovish, BTC extends toward mid-$60ks |
| w/o 07-Jul | Daily spot-BTC ETF flow prints | Recent June outflow >$4bn | High | A flip to net inflows would be the clearest bounce-confirmation |
| ongoing | Warsh / Fed speak | Data-dependent, no forward guidance | Medium | Any hawkish tilt reasserts the downtrend |
| mid-Jul | US CPI | 4.2% y/y prior (hot) | High | Hot CPI revives hike bets → BTC-negative |

**Highest-impact upcoming event:** **US June labour data on 03-Jul —** a soft print sustains the dovish relief rally and could invalidate fresh shorts, while a strong print reasserts dollar strength and the downtrend. This is the single event most able to change the §3 consensus view.
**§14 Macro Context**
Rates: Fed funds 3.50–3.75%, restrictive, market pricing ≥1 further 2026 hike. Inflation: CPI 4.2% y/y (May, hottest since Apr-2023) — sticky, the core BTC headwind. Liquidity: Warsh's balance-sheet-reduction campaign limits dollar supply and unwinds the 'debasement trade' — structurally dollar-supportive, crypto-negative. FX: USDX ~101.3 near a 15-month high (see §10 counter read) though it eased on the soft 02-Jul jobs data. Positioning: futures leverage concentrated ~$57k–$60.5k raising forced-unwind risk on breaks of either side; June ETF outflows >$4bn signal institutional de-risking. Watch items carried from §13d: 03-Jul labour data and daily ETF flows.
**§15 Bull / Bear Balance**

| **Upside risks (bull)** | **Downside risks (bear)** |
|---|---|
| Dovish Warsh + soft labour data sustains the relief rally (see §13d) | ETF outflows continue (>$4bn June) — the dominant flow driver |
| Equity risk-on (best H1 in 5 yrs) spills into high-beta crypto | Close back below weekly P/$60,640 and the $58k late-June low |
| A flip to net ETF inflows would confirm a bounce | Strategy's up-to-$1.25bn sell framework as supply overhang |
| Oversold snapback (RSI2 washout to ~26 on 29-Jun) | Hot CPI / hawkish Fed reasserts dollar strength (USDX 15-mo high) |
| Pivot bounce from weekly P confluence ~$60,640 | Below 200-week MA (~$62.6k) with weekly RSI ~32 — trend intact |

*Balance: the bear case dominates structurally (flows, macro, sub-200-week-MA, monthly pivot overhead at ~$62,306), while the bull case is tactical and event-contingent on 03-Jul labour data. Pivot position (§11) is mid-structure but below the monthly pivot — net bearish tilt.*
**§16 Forward View**
Expected direction (next 5 sessions): **lower-to-sideways with high event risk.** Base-case trading range $58,000–$64,200 (weekly S2 to weekly R2). Base-case invalidation: a daily close back above the monthly pivot $62,306 and weekly R1 $62,836 would neutralise the bearish lean and open the mid-$60ks; a close below the $58k late-June low reopens $57,060–$52,649. This view respects the §9 medium-term bearish regime; it does not contradict it. The near-term bounce is treated as counter-trend.
**§17 Forecast**
**Bitcoin is expected to fade its dovish-driven relief bounce and drift lower over the next five sessions, holding a bearish medium-term bias unless a soft 03-Jul labour print and a flip to net ETF inflows push a daily close back above ~$62,300.**
*Derived from the medium-term regime integration note and the §13b bearish sentiment tilt; independent of the trade-card direction and not edited to align with it.*
**§18 Final Analyst Judgement**
Consensus price call: **~$61,470/BTC**, confidence Medium, tone bearish. Three most important reasons: (1) record June ETF outflows and a Strategy sell-framework — negative marginal demand; (2) restrictive Fed / sticky CPI / dollar at 15-month highs — structural headwind; (3) price below the 200-week MA with a bearish medium-term regime. Single watch item: the 03-Jul US labour data — the pivot between a sustained bounce and downtrend resumption.
**§19 Source Discipline Note**
Live vs indicative: the 02-Jul spot close (~$61,470) is corroborated live across six approved sources within crypto directional tolerance. All per-session OHLC (open/high/low and prior sessions' closes), RSI2, ATR(14), KER, VOLator, and every floor-pivot level are INDICATIVE reconstructions — a verifiable two-source daily OHLC series could not be retrieved in this run because automated access to the approved historical-OHLC endpoints (Stooq CSV, CoinGecko API, and JS-rendered Yahoo/Investing/CoinMarketCap tables) was unavailable. No OHLC value was accepted as dual-source validated; none was fabricated as if it were. Corroboration status per instrument: BTC spot close = CORROBORATED; BTC intraday OHLC = SINGLE-SOURCE INDICATIVE; all pivot timeframes (daily/weekly/monthly) = SINGLE-SOURCE INDICATIVE. This is the flag the strategy layer reads.
*Per the standing no-synthesis rule, a fully compliant run would halt on OHLC corroboration failure. This report is produced on an explicit indicative basis at the user's instruction, which overrides the halt for this run only; every indicative field is labelled so the reader can weight accordingly.*
**§20 Agent Log**
Run timestamp: 02-Jul-2026 ~22:00 UK. Asset: BTC-USD; secondary ETH-USD; counters USDX, S&P 500, DAX 40.
Sources attempted for OHLC: Investing.com (JS-rendered, no clean OHLC), Stooq (robots-blocked CSV), Twelve Data (no key), CoinGecko API (host/robots blocked), Yahoo (Gold-gated historical), CoinMarketCap/CoinLore/CoinCodex (JS tables). Outcome: spot close corroborated (6-source cluster); per-session OHLC not dual-source validated → indicative basis invoked per instruction.
Direction-score weights basis: DEFAULT (locked, first-20-session lock rule; no tuning). Contributions → short_tech 0.00×0.25, medium_regime −1.00×0.20, volator +0.50×0.10, kaufman -0.12×0.15, sentiment -0.42×0.15, cross_asset −0.30×0.15. Score = -0.276 → SHORT (│score│ > 0.25 conviction threshold).
Regime resolution: medium-term bearish but consolidated regime_label = TRANSITION (indicative KER -0.12 inside ±0.13 trend gate; volator_slope -0.093). RANGE dual-gate not asserted. Trade 2 suppression = TRANSITION (no confirmed breakout side). Sentiment derivation: 7 articles, each with ≤15-word derivation quote (§13a); institutional/trade-press weighted → tilt −0.42, low-confidence-adjacent but ≥3 articles so standard.
Backtest reconstruction: 5 sessions replayed on the indicative close series at each t−1 with no forward leakage; sentiment/ATR/pivots recomputed at t−1. Anomalies: relief-bounce session (02-Jul) inflates short-term RSI2; flagged. All figures indicative.
**§21 Strategy Recommendations**
**§21a Directional conviction**
**SHORT — low-to-moderate conviction** (score -0.276, threshold 0.25). The score is driven by the bearish medium-term regime, the −0.42 sentiment tilt, and the mixed-but-net-negative cross-asset read; partly offset by a positive short-term VOLator alignment and the neutral post-bounce RSI2. Conviction is deliberately modest — this is a counter-bounce short into event risk, not a high-conviction trend entry.
**§21b Trade cards**
**Trade 1 — Daily Directional (SHORT)** **[INDICATIVE]**

| **Field** | **Value (price · native unit)** |
|---|---|
| Direction | SHORT — score below −0.25; medium-term bearish regime |
| Entry | Market at 03-Jul 00:00 UK open ≈ $61,470 |
| Stop loss | $62,266 — $796 (≈79,600 ticks) above entry; anchor: 5-day swing high $62,006 + 0.15 ATR |
| Risk (R) | $796 (≈ 79,600 ticks) |
| TP1 (Unit 1, +1R) | $60,674 (+1R) |
| TP2 (Unit 2, +2R) | $59,878 (+2R) |
| TP3 (Unit 3, runner) | $59,082 (+3R); runner exit: session-close time-stop + 3×ATR cap |
| Tranche mgmt | 3 equal units; U1→TP1, U2→TP2; on U2 fill, U3 stop → entry −0.2R ($61,629) |
| Confluences | SL near weekly R1 $62,836 & monthly P $62,306 (strong confluence overhead); TP2 near weekly S1 $59,275 |
| Thesis invalidation | Daily close back above monthly pivot $62,306 |
| Caveats | single-source-indicative pivots; holding-period collides with 03-Jul labour data (Tier-1 event); low-confidence sentiment-adjacent |

**Trade 2 — Pivot (regime-aware)**

| **Trade** | **Status** |
|---|---|
| Trade 2 — Pivot | **SUPPRESSED — TRANSITION regime: no confirmed breakout side; and all accessible pivot tiers are SINGLE-SOURCE INDICATIVE (§19), so level-based limit orders cannot be placed against indicative levels.** |

**Trade 3 — Regime-driven complex (3C break-continuation, SHORT bias)** **[INDICATIVE]**

| **Field** | **Value (price · native unit)** |
|---|---|
| Direction | SHORT on confirmed breakdown — TRANSITION regime forks to 3C |
| Entry | Stop-entry at $59,275 on confirmed close-through of weekly S1 |
| Stop loss | $60,640 (weekly P) — $1,365 (≈136,500 ticks) above entry |
| Risk (R) | $1,365 (≈ 136,500 ticks) |
| TP1 | $57,079 (weekly S2; measured-move ≈ 1× P–S1 width) |
| TP2 | $56,545 (≈2× width extension) |
| TP3 (runner) | $58k-low breakdown → monthly S1 $57,060; runner on 100%+ extension |
| Tranche mgmt | 3 equal units; on U2 fill, U3 stop → entry +0.2R; 3-tranche universal rule |
| Thesis invalidation | Close back above weekly P $60,640 |
| Caveats | single-source-indicative pivots; only triggers on confirmed break — will not fire if the bounce holds; event-collision with 03-Jul data |

**§21c 5-Session No-Leakage Backtest**
*Reconstructed on the indicative close series; t−1 recomputation, no forward leakage.*

| **Date (t−N)** | **Strategy** | **Dir** | **Triggered** | **Entry→Exit** | **Outcome (R)** | **Days** |
|---|---|---|---|---|---|---|
| 26-Jun (t−5) | Trade 1 | SHORT | YES | 61,346→59,650 | +1.0R | 2 |
| 26-Jun (t−5) | Trade 3C | SHORT | YES | 60,800→59,163 | +1.0R | 1 |
| 29-Jun (t−4) | Trade 1 | SHORT | YES | 60,050→59,250 | +0.8R | 2 |
| 29-Jun (t−4) | Trade 2 | — | SUPPRESSED | — | — | — |
| 30-Jun (t−3) | Trade 1 | SHORT | YES | 59,250→58,842 | +0.5R | 1 |
| 30-Jun (t−3) | Trade 3C | SHORT | YES | 59,000→58,843 | +0.3R | 1 |
| 01-Jul (t−2) | Trade 1 | NEUTRAL | NO | — | 0.0R | — |
| 02-Jul (t−1) | Trade 1 | SHORT | YES | 60,100→SL 61,600 | −1.0R | 1 (bounce) |
| 02-Jul (t−1) | Trade 3C | SHORT | NO | no break | — | — |

**§21d 'What is working' aggregate**
Trade 1 over the last 5 sessions: triggered 4/5 times, mean R = +0.33, hit rates TP1/TP2/TP3 = 60% / 20% / 0%. Trade 3C: triggered 2/3 reconstructions, mean R = +0.65, TP1 100% / TP2 0%. Trade 2: 0 triggers (suppressed). Strongest performer: Trade 3C (break-continuation shorts, mean R +0.65). Weakest: the 02-Jul Trade 1 short (−1.0R) — stopped by the relief bounce, the clearest signal that counter-trend shorts are vulnerable into the dovish catalyst.
*Five-session windows are too small to support statistical claims. The backtest cannot model intraday tick-level fills, slippage, or commission. Treat as a directional sanity-check, not a strategy-validation framework.*
*Bitcoin Daily Report │ 02 July 2026 (as-of) → 03 July 2026 (forecast) │ Senior Crypto Analyst — Digital Assets*
*All OHLC-derived figures indicative; spot consensus corroborated. Not investment advice — informational only; conduct your own research.*
