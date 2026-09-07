# Trust Score — 2026-07-20 — SP500_Report_20Jul2026.md

Run: `regen_20260906_qa1` · Asset: US500 (S&P 500 cash) · D = 2026-07-20 · D-1 slice = 2026-07-19
(D-1 is a Sunday; the last completed cash session is **Friday 17 July 2026**, and all anchors are checked on that session.)
Evidence base: the report, reports dated before D, `data/slices/US500/US500_upto_2026-07-19.csv` (+ VIX/USDX/NEWS slices),
`cards/baseline/by_date/2026-07-20.json`, `qa/regen_20260906_qa1/lint_static/2026-07-20.csv`, `engine/qa_slice_stats.py`.

## 1. Section 7 checklist

| Item | Reviewer notes | Evidence observed | Score 0–5 | Action required |
|---|---|---|---|---|
| 1.1 Variables respected | Asset is the S&P 500 **cash** index (^GSPC), not ES; counters USDX · VIX · DAX 40 with USDX first in both the masthead and the §10 table; as-of close 17 Jul 2026 America/New_York, issued for the 20 Jul session; lookback 5 sessions (execution) + 25 (regime); USD / index points / tick 0.01; daily-open anchor stated as **07:00 UK** in §2 and used on the Trade 1 card. Shortfall: §4 carries six rows but only **four distinct** price sources (S&P DJI-via-FRED, Investing.com, Yahoo, CNBC) and none from a sell-side tier, against a ≥6-source requirement. | §2 table + anchor note (ll. 34–63); §4 table; §10; §21b Trade 1 Entry | 4 | Add at least two further index-provider / exchange / sell-side price sources so §4 carries ≥6 distinct names. |
| 1.2 Coverage & currency consistent | All price data is 13–17 Jul (D-1 or earlier); §13d is correctly forward-looking; units are index points/USD throughout with no drift. Two coverage failures: the Reuters survey in §13a is dated only **"Jul"** with no day and is in fact a **May** survey (identically quoted at "~7,490 by end-2026" in this family's 21 May and 22 May reports); and the §11 "Monthly pivots (June 2026)" back-solve to H 7,577.91 / L 7,294.17 / C 7,499.37, which is not June (slice June cash H 7,624.60 / L 7,243.10 / C 7,493.30) — the implied low 7,294.17 is instead the report's own 25-session low 7,294.18, i.e. the wrong window was used. | §13a Reuters row; §11 monthly table; cross-ref `SP500_Report_22May2026.md`; slice June recomputation | 2 | Date every article to the day; recompute the monthly pivot block from actual June 2026 H/L/C and state those inputs. |
| 1.3 Audience & tone | Written to a Senior US Equity Strategist register for trading-and-risk review: §1 leads with level, driver ranking and a single watch item; §18 is a "Final Analyst Judgement". No retail framing, no promotional language, no "you should buy". | §1; §18; §16 | 5 | None. |
| 2.1 Sections present & ordered | §1–§21 all present and in order. §13 fully decomposed into 13a per-article / 13b aggregate with numeric tilt (−0.36) / 13c previous-period calendar / 13d upcoming calendar. §21 fully decomposed into 21a conviction / 21b cards / 21c 5-session backtest / 21d what-is-working plus the limitations boilerplate. §19 Source Discipline and §20 Agent Log both present. | Headings throughout; §13a–d (ll. 403–496); §21a–d (ll. 613–786) | 5 | None. |
| 2.2 Scorecard as a table | §6 is a proper table but is **missing the "Final Used" column** required by the structure (the 17 Jul report carries it); it has Date/O/H/L/C/RSI2/Trend/Sources A-B/Validation only. §11 pivot tables are correctly ordered high→low (R…P…S) for daily, weekly and monthly, but publish **five levels each side (R5–S5) instead of the specified three (R3→P→S3)**. | §6 header row (ll. 126–129); §11 three tables (ll. 278–363) | 3 | Restore the "Final Used" column in §6; trim the §11 tables to R3→P→S3 on all three timeframes. |
| 2.3 Method steps visible | §4 lists raw observations → §5 states the classification and consensus method explicitly (weighted median, official-source overweight, CFD/after-hours excluded, ±0.10 pt tolerance, Δ0.00 achieved). §8 is candle-by-candle across all five sessions and closes with a named sequence ("Exhaustion following a failed push to new highs") plus S/R. §9 gives the regime with overlap 0.54, persistence 0.50, VOLator slope −0.30, median RSI2 42.7, range position 55th pct. All five charts are present as image references with captions (pandoc renders them as `![](media/…)` placeholders — accepted as evidence, noted). | §4–§5; §8; §9; §7 (ll. 152–186) | 5 | None. Charts verified only as captioned placeholders. |
| 3.1 Quantitative claims sourced | §12's earnings figures are attributed ("per LSEG about 90% of the ~49 early reporters beat; growth revised toward 26% from ~19%"). But a run of load-bearing numbers carries no source and no pointer: the chip gauge "down ~20% from its high", "VanEck Semiconductor ETF off ~8–9% on the week", "oil back above $80", §14's "gold was firm (~$4,019)", and the §10 counter levels (VIX 18.77 / +12%, DAX 24,831, USDX ~100.6) — §19 calls the counters single-source but never names the source. §1 repeats the 20% and 26% figures without pointing to §12. | §12 (ll. 375–401); §14 (ll. 498–516); §10 table; §19 counters line | 2 | Attach a named, dated source (or an explicit §4/§13 pointer) to every number in §1, §10, §12 and §14. |
| 3.2 Citations exist & contain data | Three spot-checks. (a) **Invezz 17 Jul** ("Dow falls ~400 pts as chip selloff deepens") — the paired §13c/§4 figure "−1.01% close" reconciles exactly with the report's own 16→17 Jul closes (7,457.69 / 7,533.77 − 1 = −1.008%): consistent. (b) **Invezz 01 Jul** ("If SPX clears 7,621, push toward 8,000") — dated, coherent, and the 7,621 trigger sits plausibly above the report's 25-session high: consistent. (c) **Reuters survey, dated "Jul"** — quote "median target near 7,490… up ~12%". "Up ~12%" to 7,490 implies a spot of ≈6,687, which is impossible against this report's own consensus of 7,457.69 (7,490 is +0.44%) or against any level in the 25-session window (low 7,294). The identical survey ("median target near 7,490 points… by end-2026") is cited in `SP500_Report_21May2026.md` and `SP500_Report_22May2026.md` as a **mid-May** survey. Wrong date **and** a figure that does not match its own quote → **fabricated** under the protocol. | §13a Reuters row (ll. 432–434); §3/§4 close 7,457.69; `SP500_Report_21May2026.md`, `SP500_Report_22May2026.md` | 0 | **Hallucinated-source override.** Remove or correctly re-date and re-quote the Reuters survey; the "+12%" upside figure must be recomputed against the current index level or dropped. |
| 3.3 Calculations transparent | RSI2 reproduces **exactly** from the report's own closes for the three testable rows: helper returns 100.0 / 42.7 / 0.0 against the report's 100.0 / 42.7 / 0.0 for 15/16/17 Jul. The Trend rule is applied correctly on all five rows (13 Jul C<O & RSI2 34.6 → Bearish; 14 Jul C>O but RSI2 32.0 → Neutral; 15 Jul C>O & 100 → Bullish; 16 Jul C<O & 42.7 → Bearish; 17 Jul C<O & 0.0 → Bearish). Daily and weekly pivots reproduce to the cent from the report's own H/L/C on all eleven levels each, and the floor identity holds (daily R2−P = P−S2 = 67.21; weekly = 157.34). §21a arithmetic is traceable: −0.25 −0.15 −0.10 −0.054 −0.05 +0.03 = −0.574 → −0.57, and the implied signals are coherent (sentiment −0.36 × 0.15 = −0.054 matches §13b; KER +0.20 × 0.15 = +0.03 matches §9). Failures: **ATR(14) is never stated as a number anywhere** — it is only recoverable as ≈72.2 from "cap 252.7 pts" (÷3.5) and the 3×ATR runner (216.56); the 13/14 Jul RSI2 values (34.6, 32.0) cannot be reproduced from the stated 5-close window and contradict the 17 Jul report's 33.8 and 58.0 for the same sessions on identical closes; the monthly pivot inputs are never stated. | Helper output; §6; §11; §21a (ll. 615–625); §20; `SP500_Report_17Jul2026.md` §6 | 3 | State ATR(14) explicitly in §9 and on each card; publish the pre-window closes (or the seed) that produce the 13–14 Jul RSI2; state the monthly pivot H/L/C inputs. |
| 3.4 Numbers reconcile | D-1 close 7,457.69 is identical in §1, §3, §4, §6, §11, §16, §18 and the §21b Trade 1 entry. §11 pivots equal the levels quoted on the cards (P 7,462.47; S1 7,426.48; S2 7,395.26). §6 RSI2 equals §8 on every session and equals the §21a input. Reconciliation failures: (i) §1 says "a three-session slide" but §6 shows only two consecutive lower closes (16 and 17 Jul; 15 Jul closed up at 7,572.40 from 7,543.59); (ii) §8 lists "support at 7,431.26 (Friday's low), then the swing low 7,431" — the same number presented as two distinct levels; (iii) §6 and §19 both state the 15–16 Jul H/L are excluded from pivot inputs beyond the daily timeframe, yet the weekly pivots require the 15 Jul indicative high 7,588.60 (weekly P 7,492.52 back-solves to exactly that H); (iv) ATR has no stated value in §9 to reconcile against the §21 usage. | §1 (l. 12); §8 (ll. 209–211); §6 note vs §11 weekly; §19 | 2 | Correct §1 to a two-session slide; give §8 two distinct S/R levels; either drop the indicative high from the weekly pivot or withdraw the exclusion claim; state ATR once and reference it. |
| 4.1 Pillars conclude | §8 → "Exhaustion — reversal risk"; §9 → "Bias: Bearish" with regime Transitional; §10 → "Aggregate: CONFIRM"; §12 labels each block price-supportive/price-negative; §14 closes on a risk-off read with named watch items. All labels follow from their own content. The **strategy pillar (§21b) is where this category weakens**: two of three cards violate a stated M5 level rule — Trade 2's SELL STOP at 7,458.87 sits 1.18 pts **above** the D-1 close 7,457.69 (2.27 above the slice cash close 7,456.60), so the breakout entry is on the wrong side of the reference; and Trade 3C's stop 7,470.83 is midpoint + 0.10×width rather than the 3C rule's range low + 0.40×width (= 7,411.95), inflating R from 135.8 to 194.7 pts. Trade 1 is rule-compliant throughout. Also, §9's VOLator read ("at the −1.0 floor and contracting") sits awkwardly against §8's "expanding range on the final session" while still being counted as a bearish −0.05 contributor. | §8 l. 212; §9 l. 223; §10 l. 273; §12; §21b all three cards; M5 rules in brief §3 | 3 | Rebuild the Trade 2 entry below the D-1 close and the Trade 3C stop from the 3C formula; reconcile the VOLator floor/contracting statement with the expanding-range finding. |
| 4.2 Peer/cross-asset interpreted | §10 gives a real transmission mechanism for each counter rather than a correlation list: dollar → global financial conditions and multinational earnings translation; VIX → demand for downside protection and de-grossing; DAX → European beta to the same global-risk and tech factors. Status and implication columns are populated, and the single contradiction (soft USDX) is explicitly carried into §15 and §16 instead of resolved away. Weakness: the magnitudes do not reconcile — the report's "VIX 18.77, +12%" against the VIX slice's 17 Jul close 18.27 (Δ 0.50) and a +5.0% day-on-day / +9.7% week move; USDX "~100.6" against the slice's 100.73. Directions are right; the numbers are not sourced. | §10 table (ll. 250–276); §15; §16; VIX/USDX slices | 4 | Source and correct the counter levels and the +12% VIX change figure. |
| 4.3 Synthesis reconciles tensions | §9 explicitly preserves rather than resolves the KER-vs-price-action conflict and states the precedence rule (live price action and VOLator slope over a 13-session lagged EMA measure), then routes it into a TRANSITION label instead of a clean TREND_UP. §15 sets the oversold RSI2=0 bounce risk and the pivot-confluence shelf against the chip drawdown and the S1 loss path. §16 names the two live tensions (soft dollar, longer-horizon bullish survey) and gives an explicit base-case invalidation at a close above 7,533. §21a states directly that §17 and §21a agree in direction. §20 logs the fall-through logic. | §9 KER block (ll. 237–246); §15; §16 (ll. 546–550); §21a (ll. 622–625); §20 | 5 | None. |
| 4.4 Calibrated language | §17 is exactly one sentence, carrying a direction, a named support band, the pivot level and a single conditional invalidation, with no stacked hedges. §3 states Confidence = High and its basis. §21a states the score, the threshold it clears and the sign convention. §16 distinguishes base case from invalidation cleanly. | §17 (ll. 552–557); §3 table; §21a l. 615 | 5 | None. |
| 5.1 Data dated; staleness flagged | Every §6 row and §4 row is dated; the 15–16 Jul opens and H/L carry an explicit single-source-indicative flag in both the §6 note and §19; the counters are flagged single-source, directional-use only, not used for pivots; §13b notes that the bullish views are "either older or longer-horizon". Failures: the Reuters row carries no day-level date; and §19 asserts "The 13 Jul, 14 Jul and **17 Jul** full OHLC rows are corroborated" while the 17 Jul **open** of 7,490.30 is 46.6 pts from the slice cash open (7,443.70) and matches neither the cash open nor the broker full-day open (7,531.20) — a corroboration label on a value that reconciles to nothing. | §6 note (ll. 146–150); §19 (ll. 571–585); §13a; helper cash/full-day tables | 2 | Re-source the 17 Jul open or downgrade its validation label; date the Reuters item. |
| 5.2 Assumptions up front | §2 states the 07:00 UK anchor and its rationale before any use. §20 is a genuinely strong agent log: sources attempted with ranks, the three corroboration pairs with deltas, the single-source fields, the ±0.10 pt validation method, weights basis = DEFAULTS under a forward-test weight lock, backtest construction (t−1 reconstruction, sentiment frozen, SL-first tick priority), and the compile timestamp. §19 records the data gap. Gaps: the anchor-override / proxy-open caveat is not stated **on the Trade 1 card** — the card only says "last cash close as the pre-NY reference", which is itself an unlabelled proxy-open assumption; the single-source-indicative propagation is stated on Trade 2 but **not on Trade 3C**, whose range high 7,588.60 is one of the flagged indicative values; ATR(14) is used on all three cards but never declared. | §2 note; §20 (ll. 587–611); §19; §21b Trade 1 Entry, Trade 3C Range definition | 3 | Put the proxy-open caveat on the Trade 1 card; propagate the indicative flag to Trade 3C; declare ATR(14). |
| 5.3 Red flags surfaced | §12 and §15 both carry the downside set (chip drawdown and index concentration, oil>$80 rate-hold risk, S1/weekly-S1 loss path) and the upside set. The §13d event collision is carried into the Caveats line of **all three** cards ("earnings-week collision (§13d)"). §9 flags the KER anomaly and §20 logs it as an anomaly. Trade 2 flags "invalidation ahead of stop"; Trade 3C flags "not yet triggered" and "wide structural stop — position size reduced"; Trade 1 flags the pivot-magnet whipsaw risk. §21d carries the small-sample limitations boilerplate verbatim. | §12; §15; §13d note; §21b Caveats rows; §21d (ll. 783–786) | 5 | None. |
| 5.4 Restrictions honoured | Clean on the explicit prohibitions: no bracketed variable names, no module codes (M1–M5), no framework name anywhere in the report; CFD-derived and after-hours indications are explicitly **excluded** from the OHLC basis in §5; the basis is the cash index, not ES, and ES appears nowhere as a price source (§2's "futures-led re-pricing" is anchor rationale only); instrument common names are used throughout (Dollar Index, VIX, DAX 40). Weaknesses short of an open breach: the 17 Jul open 7,490.30 is presented as sourced and CORROBORATED while reconciling to neither the cash nor the full-day open, which is the signature of an interpolated value carrying a corroboration label; and the report performs the exact operation it says it excludes by computing the weekly pivots off the 15 Jul indicative high. | grep of the full report; §5 (l. 114); §2; §19 vs §11 weekly | 3 | Re-source or re-label the 17 Jul open; align the weekly pivot construction with the stated exclusion. |

## 2. Category roll-up

| Category | Level | Multiplier | Points | Justification |
|---|---|---|---|---|
| C1 Prompt adherence & instruction compliance (max 20) | 4 | 0.85 | 17.00 | Mean of 1.1–1.3 = (4+2+5)/3 = 3.67 → 4. Asset, counters, anchor, window, units and audience are all correct and explicit; pulled down by only four distinct price sources against ≥6 and by two dating/window errors (undated Reuters item, a "June" monthly pivot block computed off the wrong window). |
| C2 Structural & modular alignment (max 20) | 4 | 0.85 | 17.00 | Mean of 2.1–2.3 = (5+3+5)/3 = 4.33 → 4. Every section and sub-section is present and correctly ordered and the method chain §4→§5→§8→§9 is fully visible; the only structural defects are the missing "Final Used" column in §6 and five-deep pivot ladders where three were specified. |
| C3 Accuracy, evidence & factual reliability (max 25) | 0 | 0.00 | 0.00 | Checklist mean would be (2+0+3+2)/4 = 1.75 → 2, but the **hallucinated-source override sets C3 = 0**: the §13a Reuters survey is mis-dated and its "up ~12%" figure is impossible against the report's own 7,457.69 consensus. Independently, five §6 O/H/L values breach the basis tolerance (17 Jul open by 46.6 pts) and several §1/§12/§14 numbers are unsourced. |
| C4 Reasoning, judgment & evaluation quality (max 20) | 4 | 0.85 | 17.00 | Mean of 4.1–4.4 = (3+4+5+5)/4 = 4.25 → 4. Genuinely strong synthesis: the KER conflict is preserved not resolved, cross-asset is mechanism-based, §17 is one calibrated sentence, and the §21a score derivation is fully traceable. Held down by card construction — Trade 2's entry sits on the wrong side of the D-1 close and Trade 3C's stop is not the 3C formula. |
| C5 Currency, restrictions & transparency (max 15) | 3 | 0.65 | 9.75 | Mean of 5.1–5.4 = (2+3+5+3)/4 = 3.25 → 3. Red-flag surfacing and the §20 agent log are exemplary, but a corroboration label sits on a 17 Jul open that reconciles to nothing, an article is undated, the proxy-open caveat is missing from the Trade 1 card, the indicative flag is not propagated to Trade 3C, and the weekly pivots contradict the report's own stated exclusion. |
| **Total (pre-cap)** | — | — | **60.75 → 61** | Σ(multiplier × max) = 17.00 + 17.00 + 0.00 + 17.00 + 9.75 = 60.75, rounded to 61. |

## 3. Total, band, override check

- **Raw weighted total:** 60.75 → **61** (would band as Moderate Trust, 60–74).
- **Hallucinated-source override — FIRED.** The §13a "Reuters survey" row is dated only "Jul" and quotes "median target near 7,490… up ~12%". Against this report's own consensus close of 7,457.69, a 7,490 target is **+0.44%**, not ~12%; "up ~12%" to 7,490 requires a spot of ≈6,687, a level that appears nowhere in the report's 25-session window (low 7,294.18). The identical survey — same "~7,490 by end-2026" median — is cited in `SP500_Report_21May2026.md` and `SP500_Report_22May2026.md` as a **mid-May** survey. Wrong date plus a figure that does not match its own quote meets the protocol definition of a fabricated source.
  - Effect: **Category 3 set to 0** (applied above) and the **total capped at the Low Trust band (40–59)**.
- **Restriction-breach override — NOT fired.** No prompt restriction is *openly* violated: no module codes, no framework name, no bracketed variables, cash basis only, CFD/after-hours explicitly excluded, ES used nowhere as a price source. The 17 Jul open anomaly and the weekly-pivot-vs-exclusion contradiction are recorded as Category 3/5 defects, not as an open breach. C1 is therefore not reduced on this ground.
- **Final Trust Score: 59 / 100 — band: Low Trust.** (60.75 → 61, capped to 59 by the hallucinated-source override.)
- **Required action per the band:** not suitable for use; full prompt review and regeneration. May be salvaged for skeleton and framing only.

## 4. Card Integrity

Linter rows copied verbatim from `qa/regen_20260906_qa1/lint_static/2026-07-20.csv` (static, leak-free; not re-derived):

| card_id | report_date | strategy | flags | dud |
|---|---|---|---|---|
| 2026-07-20_Trade_1 | 2026-07-20 | Trade 1 - Daily Directional | CLEAN | False |
| 2026-07-20_Trade_2 | 2026-07-20 | Trade 2 - Pivot (TRANSITION down-break side) | CLEAN | False |
| 2026-07-20_Trade_3C | 2026-07-20 | Trade 3C - Momentum-Breakout (conditional) | WARN_TARGET_FAR(3.53xATR) | False |

Per-card integrity (100 − 40·#DUD − 10·#WARN, floored at 0):

| Card | #DUD | #WARN | Integrity |
|---|---|---|---|
| 2026-07-20_Trade_1 | 0 | 0 | 100 |
| 2026-07-20_Trade_2 | 0 | 0 | 100 |
| 2026-07-20_Trade_3C | 0 | 1 | 90 |

- Cards in file: **3** · suppressed: **0** · non-suppressed scored: **3** · total DUD flags: **0** · total WARN flags: **1**.
- **Report-level Card Integrity = (100 + 100 + 90) / 3 = 96.7.**

Note: Card Integrity is deterministic and static-mode only. The M5 construction defects assessed below feed Section 7 row 4.1, **not** this number — Trade 2 scores 100 here while still carrying a wrong-side entry, because the static linter has no D-1 close to test the entry side against.

M5 assessment behind row 4.1 (not part of the integrity number):

| Card | M5 check | Result |
|---|---|---|
| Trade 1 | MARKET entry = D-1 close (7,457.69 = §6 close) | Pass |
| Trade 1 | Stop = tighter of (5-day swing high 7,588.60, nearest resistance 7,498.47) + 0.25×ATR → 7,498.47 + 18.05 = 7,516.52 | Pass |
| Trade 1 | R 58.83 within 0.3–3.0×ATR14 (21.7–216.6 on the report's implied ATR 72.2; 20.9–208.7 on slice ATR 69.57) | Pass |
| Trade 1 | Wide-stop flag if R > 1×ATR — 58.83 < 72.2, correctly not flagged | Pass |
| Trade 1 | TP1 = entry −1R = 7,398.86; TP2 = entry −2R should be 7,340.03 (card 7,340.04); BE = entry +0.2R should be 7,469.46 (card 7,469.45) | Pass with 0.01-pt rounding drift |
| Trade 1 | TP3 = 3×ATR runner cap with session-close time-stop; three equal units; thesis invalidation (7,533 close) separate from the stop; anchor explicit (07:00 UK) | Pass |
| Trade 1 | Indicative flag on the 5-day swing high 7,588.60 used in the stop comparison | Not propagated |
| Trade 2 | TRANSITION → breakout side only, counter-side suppressed | Pass |
| Trade 2 | STOP entry on the correct side of the D-1 close — SELL STOP 7,458.87 sits **1.18 pts above** the D-1 close 7,457.69 (2.27 above slice cash 7,456.60) | **Fail** |
| Trade 2 | Stop derivation — card says "structural, above daily P"; M5 gives structural + 0.25×ATR = 7,462.47 + 18.05 = 7,480.52; the card's 7,487.44 is P + 0.8×(R1−P), the mirrored TREND formula, undisclosed | **Fail (undisclosed derivation)** |
| Trade 2 | R 28.57 within 0.3–3.0×ATR14; TP ladder S1 7,426.48 / S1.5 7,410.87 / S2 7,395.26 correctly ordered and on the short side; S1.5 = midpoint of S1/S2 | Pass |
| Trade 2 | Pivot-source flag propagated ("Daily pivot inputs CORROBORATED, 17 Jul H/L/C") | Pass |
| Trade 3C | Confirmed break = range low − 0.25×ATR = 7,294.18 − 18.05 = 7,276.13; entry stop-side correct (below D-1 close); armed-not-live status stated | Pass |
| Trade 3C | Stop = range low + 0.40×width = 7,294.18 + 117.77 = **7,411.95**; card uses 7,470.83 (= midpoint + 0.10×width), inflating R from 135.82 to 194.70 pts | **Fail** |
| Trade 3C | TP1 = range low − 1.0×width = 6,999.76; TP2 = 1.5×MM = 6,852.55; TP3 null/discretionary | Pass |
| Trade 3C | TP1 within 2.5×ATR14 of entry — 276.37 pts = 3.53×ATR (linter) / 3.83×ATR on the report's implied 72.2 | **Fail (WARN)** |
| Trade 3C | Range inputs vs slice: low 7,294.18 vs 7,303.10 (Δ 8.92, beyond the 8-pt tolerance); high 7,588.60 vs 7,583.40 and flagged single-source-indicative without propagation | **Fail** |
| All cards | Stops/targets in **both** price and points — stops and R are given in points, TP levels are price-only on all three cards | **Fail** |

## 5. Data reconciliation log

Basis: slice cash session 16:30–23:00 broker (09:30–16:00 ET). Tolerance per the brief: |Δ| ≤ 3 pts on a close, ≤ 8 pts on an open/high/low.

### §6 — Validated OHLC, five rows, all four fields

| Section | Field | Report value | Slice (cash) value | Delta | Verdict |
|---|---|---|---|---|---|
| §6 | 13 Jul Open | 7,547.53 | 7,550.80 | −3.27 | Consistent (basis) |
| §6 | 13 Jul High | 7,565.37 | 7,565.80 | −0.43 | Consistent |
| §6 | 13 Jul Low | 7,506.41 | 7,507.00 | −0.59 | Consistent |
| §6 | 13 Jul Close | 7,515.34 | 7,518.20 | −2.86 | Consistent (inside 3 pts) |
| §6 | 14 Jul Open | 7,536.70 | 7,535.70 | +1.00 | Consistent |
| §6 | 14 Jul High | 7,557.44 | 7,559.70 | −2.26 | Consistent |
| §6 | 14 Jul Low | 7,513.23 | 7,512.90 | +0.33 | Consistent |
| §6 | 14 Jul Close | 7,543.59 | 7,546.40 | −2.81 | Consistent (inside 3 pts) |
| §6 | 15 Jul Open | 7,550.10 | 7,569.10 | **−19.00** | **Discrepancy** (>8 pts) |
| §6 | 15 Jul High | 7,588.60 | 7,582.80 | +5.80 | Within tolerance, but this value is the report's 5-day and 25-session swing high and is self-flagged indicative |
| §6 | 15 Jul Low | 7,546.80 | 7,528.60 | **+18.20** | **Discrepancy** (>8 pts) |
| §6 | 15 Jul Close | 7,572.40 | 7,573.90 | −1.50 | Consistent |
| §6 | 16 Jul Open | 7,561.20 | 7,554.00 | +7.20 | Within tolerance |
| §6 | 16 Jul High | 7,566.90 | 7,572.20 | −5.30 | Within tolerance |
| §6 | 16 Jul Low | 7,519.40 | 7,506.00 | **+13.40** | **Discrepancy** (>8 pts) |
| §6 | 16 Jul Close | 7,533.77 | 7,536.20 | −2.43 | Consistent |
| §6 | 17 Jul Open | 7,490.30 | 7,443.70 | **+46.60** | **Category 3 failure** — also fails against the broker full-day open 7,531.20 (−40.90); reconciles to neither basis, yet §19 labels the 17 Jul row fully corroborated |
| §6 | 17 Jul High | 7,498.47 | 7,497.30 | +1.17 | Consistent |
| §6 | 17 Jul Low | 7,431.26 | 7,431.60 | −0.34 | Consistent |
| §6 | 17 Jul Close (D-1) | 7,457.69 | 7,456.60 | +1.09 | Consistent — anchors §1/§3/§4/§11/§18 and the Trade 1 entry |

### §6 — RSI2

| Section | Field | Report value | Reference value | Delta | Verdict |
|---|---|---|---|---|---|
| §6 | 13 Jul RSI2 | 34.6 | 35.93 (slice closes) / n-a (report's own closes — window too short) | −1.33 / untestable | Not reproducible from the report's own data; also contradicts `SP500_Report_17Jul2026.md`, which states 33.8 for the same session on the identical close |
| §6 | 14 Jul RSI2 | 32.0 | 33.49 (slice closes) / n-a (report's own closes) | −1.49 / untestable | Not reproducible; `SP500_Report_17Jul2026.md` states **58.0** for the same session on the identical close — a 26-point cross-report divergence in the same series |
| §6 | 15 Jul RSI2 | 100.0 | 100.00 (slice) / **100.0** (report's own closes) | 0.00 / 0.00 | Exact — arithmetic verified |
| §6 | 16 Jul RSI2 | 42.7 | 42.18 (slice) / **42.7** (report's own closes) | +0.52 / 0.00 | Exact — arithmetic verified |
| §6 | 17 Jul RSI2 | 0.0 | 0.00 (slice) / **0.0** (report's own closes) | 0.00 / 0.00 | Exact — arithmetic verified |
| §6 | Trend labels (all 5) | Bearish / Neutral / Bullish / Bearish / Bearish | Rule applied to the report's own O, C and RSI2 | — | All five correct |

### §11 — Pivots (reproduction from the report's own H/L/C, then slice comparison)

| Section | Field | Report value | Reference value | Delta | Verdict |
|---|---|---|---|---|---|
| §11 daily | P, R1–R5, S1–S5 (11 levels) | 7,462.47 / 7,493.69 / 7,529.68 / 7,560.90 / 7,628.11 / 7,695.32 / 7,426.48 / 7,395.26 / 7,359.27 / 7,292.06 / 7,224.85 | Recomputed from the report's own 17 Jul H 7,498.47 / L 7,431.26 / C 7,457.69 | 0.00 on all 11 | Reproduces exactly |
| §11 daily | Floor identity R2−P vs P−S2 | 67.21 vs 67.21 | — | 0.00 | Identity holds |
| §11 daily | P | 7,462.47 | 7,461.83 (slice cash) | +0.64 | Consistent |
| §11 daily | R1 / S1 | 7,493.69 / 7,426.48 | 7,492.07 / 7,426.37 | +1.62 / +0.11 | Consistent |
| §11 daily | R2 / S2 | 7,529.68 / 7,395.26 | 7,527.53 / 7,396.13 | +2.15 / −0.87 | Consistent |
| §11 daily | R3 / S3 | 7,560.90 / 7,359.27 | 7,557.77 / 7,360.67 | +3.13 / −1.40 | Consistent |
| §11 weekly | P, R1–R5, S1–S5 (11 levels) | 7,492.52 / 7,553.77 / 7,649.86 / 7,711.11 / 7,868.45 / 8,025.79 / 7,396.43 / 7,335.18 / 7,239.09 / 7,081.75 / 6,924.41 | Recomputed from the report's own week H 7,588.60 / L 7,431.26 / C 7,457.69 | 0.00 on all 11 | Reproduces exactly — **but the H input is the 15 Jul single-source-indicative high the report says it excludes from pivots beyond the daily timeframe** |
| §11 weekly | Floor identity R2−P vs P−S2 | 157.34 vs 157.34 | — | 0.00 | Identity holds |
| §11 weekly | P / R1 / S1 | 7,492.52 / 7,553.77 / 7,396.43 | 7,490.33 / 7,549.07 / 7,397.87 (slice) | +2.19 / +4.70 / −1.44 | Consistent |
| §11 weekly | R2 / R3 | 7,649.86 / 7,711.11 | 7,641.53 / 7,700.27 (slice) | +8.33 / **+10.84** | **Discrepancy** — the indicative 15 Jul high propagates outward through the ladder |
| §11 monthly | Implied inputs (back-solved) | H 7,577.91 / L 7,294.17 / C 7,499.37 | June 2026 cash H 7,624.60 / L 7,243.10 / C 7,493.30 | −46.69 / +51.07 / +6.07 | **Discrepancy** — not the June window; the implied low equals the report's own 25-session low 7,294.18. Inputs are never stated in §11 |
| §11 monthly | Internal identities (R2−P = P−S2; R3, S3) | 283.74 / 283.74; R3 7,903.87; S3 7,052.65 | Recomputed from the implied H/L/C | 0.00 | Internally self-consistent |

### Other cross-checks

| Section | Field | Report value | Reference value | Delta | Verdict |
|---|---|---|---|---|---|
| §21b / §9 | ATR(14) | Never stated; implied 72.19 (from TP3 = entry − 216.56) and 72.20 (from cap 252.7 ÷ 3.5) | 69.57 (slice cash) / 78.22 (slice full-day) | +2.6 / −6.0 | Value is plausible but undeclared; the linter's 3.53×ATR WARN is computed on 78.22 |
| §21b 3C | 25-session range low / high / width | 7,294.18 / 7,588.60 / 294.4 | 7,303.10 / 7,583.40 / 280.3 (slice, window 15 Jun–17 Jul) | −8.92 / +5.20 / +14.1 | **Low breaches the 8-pt tolerance**; width overstated by 14.1 pts, which propagates into the 3C stop, TP1 and TP2 |
| §21b T1 | Entry (MARKET) | 7,457.69 | D-1 close 7,456.60 (slice) | +1.09 | Consistent; equals the report's own §6 close as required |
| §21b T2 | Sell-stop entry | 7,458.87 | D-1 close 7,457.69 (report) / 7,456.60 (slice) | +1.18 / +2.27 | **Wrong side** — a sell-stop must sit below the reference close |
| §1 | "three-session slide" | 3 sessions | §6 shows 2 consecutive lower closes (16, 17 Jul); 15 Jul closed up | −1 session | **Internal contradiction** |
| §1 | "down roughly 1.6% on the week" | ≈ −1.6% | −1.55% (slice, 10 Jul close 7,574.20 → 17 Jul 7,456.60) | 0.05 pp | Consistent |
| §4 / §13c | 17 Jul session change "−1.01%" | −1.01% | −1.008% from the report's own 7,533.77 → 7,457.69; −1.056% on the slice | 0.00 / 0.05 pp | Consistent |
| §10 / §14 | VIX level | 18.77 | 18.27 (VIX slice, 17 Jul cash close) | +0.50 | Discrepancy on an unsourced counter; direction (rising) is correct |
| §10 | VIX change "+12%" | +12% | +5.0% day-on-day (17.40 → 18.27); +9.7% on the week (16.66 → 18.27) | +7.0 / +2.3 pp | **Discrepancy** — reconciles on no basis |
| §10 / §14 | USDX level | ~100.6 | 100.73 (USDX slice, 17 Jul cash close) | −0.13 | Consistent; "falling" holds over the week (100.97 → 100.73) |
| §13c | 14 Jul "June CPI", High impact | Listed | NEWS slice: USD CPI / Core CPI, 2026-07-14, HIGH | — | Consistent |
| §13a | Reuters survey date and "up ~12%" | "Jul"; 7,490 median = "up ~12%" | 7,490 vs the report's own 7,457.69 = +0.44%; identical survey cited as **mid-May** in the 21 May and 22 May reports | +11.6 pp; ~2 months | **Fabricated source — override fired** |
| §21c | Backtest R values | −0.72 / −0.15 / +0.50 / −0.61 / +1.00 | Recomputed from the report's own opens/closes at a fixed ±45-pt R | ≤0.005 each | Arithmetic consistent — but the 15 Jul and 17 Jul entries inherit the §6 open errors (−19.00 and +46.60 pts) |
| §21d | Sum / mean R | +0.02 / ≈0.00; TP1 hit rate 20% | Recomputed: sum +0.02, mean +0.004, 1 of 5 = 20% | 0.00 | Consistent |
| §21a / §20 | Direction score | −0.57 | Σ of the six stated contributions = −0.574 | 0.004 | Consistent; implied signals coherent (sentiment −0.36 × 0.15; KER +0.20 × 0.15) |
