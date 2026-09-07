# Trust Score — 2026-07-23 — SP500_Report_23Jul2026.md

Reviewer inputs: report for D = 2026-07-23; slice `data/slices/US500/US500_upto_2026-07-22.csv` (last bar
2026-07-22 23:45 broker, cash session 16:30–23:00 broker); `engine/qa_slice_stats.py` run with the report's
own five §6 closes; counter slices `VIX/VIX_upto_2026-07-22.csv` and `USDX/USDX_upto_2026-07-22.csv`;
`cards/baseline/by_date/2026-07-23.json`; `qa/regen_20260906_qa1/lint_static/2026-07-23.csv`; cross-report
check against `reports/md/SP500_Report_22Jul2026.md` and `reports/md/SP500_Report_20Jul2026.md` (both dated
before D). Tolerances per the reviewer brief: |Δ| ≤ 3 pts on a close, ≤ 8 pts on an open/high/low.

Helper reference values (cash session unless stated): ATR14 63.97 (full-day 74.00) · D-1 cash close 7498.80
(full-day 7506.50) · D-1 daily pivots P 7504.10 R1 7520.20 R2 7541.60 R3 7557.70 S1 7482.70 S2 7466.60
S3 7445.20 · weekly (13–17 Jul) P 7490.33 R1 7549.07 S1 7397.87 · 5-day swing high 7572.20 (16 Jul) / low
7431.60 (17 Jul) · 25-day high 7582.80 (15 Jul) / low 7303.10 (26 Jun), width 279.70 ·
RSI2 recomputed from the report's own five closes: n/a, n/a, 0.0, 82.4, 86.6.

As-of check: the report's declared as-of session is "Close of 22 July 2026 (America/New_York)", the §6 table
terminates on 22 Jul, and the last bar in the slice is 2026-07-22 23:45 broker. The as-of session is
genuinely D-1. No §4, §6, §11, §13a or §21c data item is dated on or after D; §13d entries dated 23–30 Jul
are forward calendar items, which is correct.

## 1. Section 7 checklist

| Item | Reviewer notes | Evidence observed | Score 0–5 | Action required |
|---|---|---|---|---|
| 1.1 Variables respected | Asset is the S&P 500 cash index and §2 states explicitly "not the E-mini futures contract"; counters are USDX · VIX · DAX 40 in that order with USDX first; as-of is the 22 Jul close in America/New_York (genuinely D-1, and the five-session block correctly skips 18–19 Jul); lookback 5 sessions short-term plus 25 structural; USD and index points declared in §2. Seven accepted §4 source rows (≥ 6) spanning index provider, media of record, institutional and aggregator tiers. Three deviations: (a) **tick size 0.01 is never stated** anywhere in §2 or elsewhere; (b) the daily-open execution anchor is **23:00 UK**, not the standing 07:00 UK — a variable deviation that the report itself concedes is not a tradeable moment on this instrument ("the cash index does not trade at 23:00 UK"), forcing every Trade 1 market order to be re-expressed as an opening-session order; (c) the extracted card record carries `anchor_broker` 16:30 for Trade 1 and 09:00 for Trades 2 and 3 (= 14:30 UK and 07:00 UK), so neither matches the 23:00 UK anchor the report declares, and the two cards disagree with each other. | Header block; §2; §4; §20 anchor rows; §21 execution notice; `cards/baseline/by_date/2026-07-23.json` | 2 | State the tick size; carry one anchor consistently across the header, §2, §20, §21b and the card record. |
| 1.2 Coverage & currency consistent | No data item is dated on or after D; every §4 price row and every §13a article is 21–22 Jul or earlier; the session under review is 23 Jul. No currency or unit drift — USD and index points throughout, with Brent/WTI quoted in USD in §12/§14 and never mixed into the index basis. Three coverage defects: (a) §9's 25-session low of 7,189.38 does not come from the 25-session window at all — it is identical to the low implied by the June monthly pivots in §11, so a monthly series has been imported into a 25-session field (slice 25-day low is 7,303.10, a 113.72-point error); (b) the USDX level quoted in §10 and §14 (100.98) is the **20 Jul** close on the counter slice, presented as current without a staleness flag (D-1 close 101.10); (c) the 16, 17 and 21 Jul closes are asserted corroborated at Δ0.00 while the 22 Jul report asserts the same status for different values on the identical sessions. | §9 regime table; §11 monthly table; §10 and §14 FX rows; `SP500_Report_22Jul2026.md` §6 | 3 | Rebuild the 25-session range from the 25-session window; date the counter-asset levels to D-1 or flag them stale. |
| 1.3 Audience & tone | Consistent senior US Equity Strategist register: trading-and-risk-review framing in the header, mechanism-led explanation rather than description, explicit invalidation levels, conviction and confidence language, no retail promotion and no return promises. §18 is a proper analyst judgement with three ranked reasons and a single named watch item; §21's execution notice reads as a risk-desk memo. One blemish: "the module's own gate rates its directional premise as noise" in §21b leaks build machinery into the deliverable. | §1; §16; §18; §21 execution notice; §21b Trade 1 preamble | 5 | Replace "the module's own gate" with analyst-facing language. |
| 2.1 Sections present & ordered | §1–§21 are all present and in the prescribed order, including §7 charts, §11's three pivot frames, §21a conviction, §21b cards, §21c backtest and §21d what-is-working with a limitations paragraph. §13a is a proper per-article table with a derivation quote per row; §13b carries a numeric tilt (−0.10); §17 is exactly one sentence. Structural defect: the **previous-period calendar is absent**. §13c is occupied by a "Sentiment derivation method" note, and §13d carries only forward events (Part 1 = the 23 Jul holding period, Part 2 = the five-day horizon), so no completed-period calendar exists anywhere in §13. | Headings throughout; §13a–§13d | 3 | Restore the previous-period calendar as §13c and move the derivation method to a note under §13b. |
| 2.2 Scorecard as a table | §6 is a table but carries only Date / Open / High / Low / Close / RSI2 / Trend / Validation outcome — **Source A, Source B and Final are missing**, three of the eleven specified columns. The corroboration detail is compressed into prose inside the Validation cell ("CORROBORATED on close (delta 0.00); OHLC indicative"), which is informative but is not the per-source scorecard the spec asks for; the prior day's report carried the full column set, so this is a regression. §11 is correct: three frames (daily, weekly, monthly), each ordered R3 → P → S3 with exactly three levels a side. | §6 header row; §11 three tables; `SP500_Report_22Jul2026.md` §6 for comparison | 3 | Restore Source A / Source B / Final as discrete columns in §6. |
| 2.3 Method steps visible | §4 lists eight observations with raw quote, basis, tier and note; §5 then shows normalisation (the ×10.0329 tracker scale factor with its three constituent ratios), weighting, the exclusion and its rationale, and a defensibility statement — the observation → classification → consensus chain is fully visible. §8 is candle-by-candle across all five sessions followed by an explicit sequence assessment with range contraction quantified. §9 states overlap, directional persistence, median RSI2, net displacement and the 25-session range before naming the regime, then adds the efficiency confirmation with an explicit precedence rule and the VOLator slope. §7 survives pandoc as five captioned image placeholders — accepted as evidence and noted here. | §4; §5; §7.1–§7.5; §8; §9 | 5 | None. |
| 3.1 Quantitative claims sourced | A large volume of §1, §12 and §14 numbers carries neither a source nor a pointer into §4/§6/§13: Brent 94.07 and WTI 86.83 (and the "roughly 3.4% and 3%" moves), the ~88% beat rate, ~23% blended growth, the 10% → 34% July hike odds and 78% September figure, GM +5%, Schwab −2.5%, IBM −25%, the 52-week high of 7,620.90, DAX ~25,150, USDX 100.98, VIX 18.65 → 17.05, and the §14 liquidity line (16.14 bn shares against a twenty-session average of 19.56 bn). §19 flags the counter-asset levels as single-source indicative, which is a status flag rather than a source. Sourced correctly: every index level in §1, §3 and §6 traces to a named §4 row; the −0.10 sentiment tilt traces to §13a/§13b. | §1 paragraph 1; §12 all five drivers; §14 rows 1–5; §19 bullet 2 | 2 | Attach a named source or an internal §4/§6/§13 pointer to every number in §1, §12 and §14. |
| 3.2 Citations exist & contain data | Every §4 and §13a source is named, dated ≤ D-1, and quotes a figure; §13a rows carry short derivation quotes. Three spot-checks, all internally coherent and used consistently: (a) **index provider release via FRED, 21 Jul, 7,509.20** — matches §6's 21 Jul close and §1's "down 10.24 points", since 7,509.20 − 7,498.96 = 10.24 exactly; (b) **CNBC market report, 22 Jul, "−0.14% on the session"** — (7,498.96 − 7,509.20)/7,509.20 = −0.1364%, which rounds to −0.14%, and the level is the one used everywhere; (c) **Trading Economics, 21 Jul, "+0.89%"** normalised to 7,509.20 — (7,509.20 − 7,443.28)/7,443.28 = +0.8857%, which rounds to +0.89% and matches §8's "the strongest session of the window at +0.89%". The rejected Investing.com row (7,543.59 dated 14 Jul) is documented with a stated rationale in §4, §5 and §20. Two dating blemishes: the CNBC §13a URL slug reads 2026/07/21 against an article date of 22 Jul, and the Schwab row is dated 21 Jul while its quote ("climbed above 7,500 … but closed below it") describes a session closing below 7,500 — 21 Jul closed at 7,509.20, so the quote fits the 20 Jul session (high 7,511.93, close 7,443.28) as reported in a 21 Jul morning piece. Both are reconcilable dating ambiguities, not impossible sources. **No fabrication found; hallucination override not triggered.** | §4 rows 1, 2, 6, 8; §5 exclusion bullet; §13a rows 1 and 8; §20 sources-rejected row | 4 | Make the §13a Schwab row state which session its quote describes; align the CNBC URL slug with the article date. |
| 3.3 Calculations transparent | **RSI2 fails.** The method is named ("computed at a fixed period of two from the validated close sequence") but the column does not reproduce from the report's own closes: the helper returns 0.0 / 82.4 / 86.6 for 20, 21 and 22 Jul against the stated 9.3 / 68.5 / 57.0 — deltas +9.3, −13.9 and −29.6 — and the slice independently returns 0.00 / 85.99 / 86.97, corroborating the recomputation. The stated Trend rule is then broken twice: 17 Jul is labelled Bearish although its close (7,457.35) is **above** its open (7,445.21), and 22 Jul is labelled Neutral although close > open with RSI2 57.0 > 50, which is Bullish on either the stated or the corrected RSI2. Pivots are the opposite case and are exact: all seven daily levels reproduce to the cent from the report's own 22 Jul H/L/C (7,524.88 / 7,488.26 / 7,498.96) and the floor identity holds, R2 − P = 36.62 = P − S2; the weekly frame reproduces from H 7,580.67 / L 7,432.38 / C 7,457.34 — the last being the report's own 17 Jul close — with identity 148.29 = 148.29; the monthly frame satisfies 439.64 = 439.64. ATR(14) is stated once, in §3 (70.91), and every card ratio recomputes from it exactly (0.25× = 17.73, 0.15× = 10.64, 3× = 212.74, 3.5× = 248.19). KER is given as +0.0488 but its parameters (13, EMA 3) are not stated. §21a sums exactly to −0.0187 and implies the default weight vector 0.25 / 0.20 / 0.10 / 0.15 / 0.15 / 0.15. §19 states the scale-factor dispersion as "0.0051 (0.05 basis points)" — 0.0051 on a factor of 10.0329 is 5.08 bp, a 100× unit error. | §6 RSI2 and Trend columns; helper output; §11 three tables; §3 ATR line; §9 KER paragraph; §19 bullet 1; §21a | 2 | Recompute the RSI2 column from the stated closes; correct the 17 and 22 Jul Trend cells; state the KER parameters; fix the basis-point conversion in §19. |
| 3.4 Numbers reconcile | Reconciles well: the D-1 close 7,498.96 is identical in §1, §3, §4, §6, the §11 position narrative, §18 and the Trade 1 entry; §11's daily levels are the exact levels quoted on the cards (S1 7,483.19 = Trade 2 entry, R2 7,540.65 = Trade 3 entry, P 7,504.03 = Trade 3 TP1, weekly P 7,490.13 = Trade 3 TP2); the §3 ATR of 70.91 is the ATR implied by every card ratio; RSI2 57.0 propagates consistently into §8, §9's median and §21a's short-term component; and §21c's prior-session S1/R1 pairs reproduce exactly from §6's own H/L/C for 17, 20, 21 and 22 Jul, with every fill / no-fill call matching §6's highs and lows and the net R figures summing correctly (−0.12 − 1.00 = −1.12; +0.85 − 0.34 = +0.51). Fails: the 25-session low of 7,189.38 in §9 is inherited by §15 ("the upper half of the 25-session range at 79.1%") and by the §21b Trade 3B fork rationale ("price at 79.1% of the 25-session range"), so one bad input drives three sections; §3's confidence cell reads "High" while its own rationale reads "high on the level and deliberately moderate on the band" and §18 reads "Medium … High on the level and the band; low on direction" — three statements of one quantity; and the card record contradicts §21b on three points (Trade 1 `suppressed: false` against a card headed "SUPPRESSED BY CONVICTION RULE", Trade 3 `be_rule: NONE` against a stated "Unit 3 stop moves to entry +0.2R (7,550.17)", and the anchor mismatch recorded under 1.1). | §9 vs §15 vs §21b; §3 vs §18; §21c vs §6; card JSON vs §21b | 2 | Correct the 25-session low and propagate; state one confidence; align the card record with §21b on suppression, BE rule and anchor. |
| 4.1 Pillars conclude | §9 closes on "Classification: transitional, with a mild upward bias" with both gate failures argued; §10 closes on "the cross-asset aggregate is therefore recorded as mixed rather than confirming"; §12 tags each of its five drivers with a direction and a horizon (price-supportive cyclical, price-negative cyclical escalating, price-negative fast-moving, mildly price-negative, neutral structural); §14's six rows each end on a direction. Every label follows the evidence beneath it. Only shortfall: §8 ends on a sequence assessment and support/resistance levels but never states a one-line direction label as the other pillars do — the reader must infer "alternating bias rather than trend". | §8 sequence assessment; §9 classification; §10 contradiction flag; §12 headings; §14 rows | 4 | Add an explicit closing direction label to §8. |
| 4.2 Peer/cross-asset interpreted | §10 supplies a genuine transmission mechanism per counter rather than a correlation list: USDX → translation of overseas revenue for multinational constituents plus global financial conditions; VIX → the market's price for downside insurance, so a falling level means reduced hedging demand; DAX 40 → a shared global growth and risk-appetite factor, with divergence used diagnostically to isolate a US-specific driver. Each row then carries a confirmation status and an implication, and the qualification on VIX ("a VIX this low into a heavy earnings docket is complacency as much as calm") is a real reading rather than a hedge. The two-against-one contradiction is named explicitly, attributed to megacap concentration, and carried forward into §15, §16 and a zero cross-asset contribution in §21a rather than being dropped. | §10 table and contradiction flag; §15; §21a cross-asset row | 5 | None. |
| 4.3 Synthesis reconciles tensions | The narrative layer is strong: §9 sets an explicit precedence rule between the efficiency ratio and the regime read rather than leaving them in conflict; §15 balances four upside against four downside factors with levels; §16 asserts consistency with the regime and gives two-sided invalidation; the §17-versus-§21a tension (a neutral-to-mildly-positive forecast against a nominal short score) is handled by labelling Trade 1's direction "nominal … not a regime-endorsed direction" and suppressing it. The **card layer fails**. (a) §9 classifies the regime TRANSITIONAL, under which Trade 2 is breakout-side only, yet Trade 2 is a buy limit at daily S1 with ±1R/±2R targets — the RANGE construction — presented under an invented label, "transitional-regime variant (fade the inner band toward the pivot)". (b) The Trade 3 fork should be 3C on a transitional label, but 3B is selected, and 3B's own geometry is then not applied at all: the entry is daily R2 rather than the 78.6–88.6% band of the 25-day range, the stop is the 16 Jul high + 0.25 ATR rather than 10% of width, and TP1/TP2 are the daily and weekly pivots rather than the range midpoint and far side − 10%. On the report's own 25-session range the R2 entry sits at 89.8%, outside the 78.6–88.6% band, so the card is non-conformant even on its own numbers. (c) §19 states that every pivot tier carries the single-source indicative flag, which under the pivot rule suppresses Trade 2 — the suppression was relaxed on instruction (§20) and is disclosed, but the resulting card is not rule-conformant. | §9 classification vs §21b Trade 2 "Trade type" row; §21b Trade 3B entry/stop/TP rows; §19 bullet 3; §20 corroboration-leniency row | 2 | Rebuild Trade 2 on the breakout side (or re-label the regime with evidence) and rebuild Trade 3 on the 3C fork, or apply 3B's stated geometry in full. |
| 4.4 Calibrated language | §17 is exactly one sentence, bounded by a stated range, with a named resolution mechanism and no hedge stacking. §16 separates the base case from two-sided invalidation with explicit levels. §21a states conviction LOW and quantifies it against the threshold ("approximately 7.5% of the level required"). The card caveats are unusually honest and quantified — the 0.31 ATR stop is called out as noise-prone, TP3 at 3× ATR is called unreachable at current compression, and Trade 3's fill condition is stated as most likely on a bullish earnings gap. Defect: the confidence statement is inconsistent three ways between §3's table cell (High), §3's own rationale (high on level, moderate on band) and §18 (Medium; high on level and band, low on direction). | §3 table and rationale; §17; §18; §21a; §21b Caveats rows | 4 | State one confidence value and one decomposition of it. |
| 5.1 Data dated; staleness flagged | Every §4 price row and every §13a article is dated, and the single-source-indicative treatment is the report's best transparency work: §6 flags it per row, the §6 footnote states the constraint that indicative highs and lows cannot be the sole basis for pivots, §11 repeats the source status under each of the three frames, §19 devotes a bullet to it, and each card's caveats carry it. Against that: the 16, 17 and 21 Jul closes are asserted "corroborated, delta 0.00" while the 22 Jul report asserts the same status on the same sessions for 7,533.77 / 7,457.69 / 7,506.47 — deltas of 1.87, 0.34 and 2.73 against this report — and the flip is unexplained; the USDX 100.98 is a 20 Jul close used as current with no staleness flag; and the VIX anchor of 18.65 is undated and does not occur anywhere on the counter slice across 16–22 Jul (window maximum 18.52). | §6 Validation column and footnote; §11 source-status notes; §19 bullets 1–3; §10/§14 counter levels; `SP500_Report_22Jul2026.md` §6 | 3 | Reconcile the corroboration status with the prior report; date the USDX and VIX anchors to D-1 or flag them. |
| 5.2 Assumptions up front | The anchor override is disclosed four times — in the header block, in §2's Session anchor row, in §20 with a full consequence note explaining why the standing anchor exists and what 23:00 UK costs, and again in a bold execution notice placed before any card, which states that market-at-anchor entries are not executable on this instrument and have been converted. That is the right handling of a deviation. Single-source pivot propagation is stated in §6, in each §11 frame, in §19 bullet 3 and in each card's caveats. The corroboration-leniency relaxation and the Trade 1 suppression retention are both logged in §20 with their reasons. The tracker scale factor is explicitly described as "an assumption and not a measurement". Gaps: the 25-session range inputs are used with no note of their provenance, and ATR(14) — which sizes every stop, buffer and cap — appears numerically only in §3 and is never restated in §9 or §21b. | §20 anchor-deviation and leniency rows; §21 execution notice; §19 bullets 3 and 5; §21b Caveats rows | 4 | Restate ATR(14) numerically where it is used, and state the provenance of the 25-session range. |
| 5.3 Red flags surfaced | Comprehensive. §12 carries the asymmetric-reaction risk, the crude/inflation escalation channel and the hawkish repricing, each with a direction and a horizon, followed by a dated catalyst list. §15 gives four upside and four downside risks with levels attached. §10 raises the cross-asset contradiction explicitly. §13d grades collision risk HIGH for the megacap earnings block and MEDIUM for the ECB decision, and that HIGH is carried verbatim into the caveats of all three cards ("Holding-period collision: HIGH"), which is exactly the propagation the checklist asks for. §20 logs three named anomalies. §21d states the sample-size limitation and refuses to let the backtest override the structural logic. | §12; §13d Part 1; §15; §20 anomalies row; §21b Caveats rows; §21d bullet 4 | 5 | None. |
| 5.4 Restrictions honoured | Honoured: no synthesised price is presented as sourced — the reconstructed opens, highs and lows are labelled INDICATIVE at every point of use and the constraint on their downstream use is stated; no retail CFD quotes enter the cash basis, and the one CFD-derived table encountered is rejected outright with the restriction cited; ES futures are excluded from the definition in §2 and confined to "confirmation and narrative context only, never as a price source" in §19; a grep of the whole report finds no bracketed variable names, no module codes (M1–M5) and no framework name; instrument common names are used throughout. Weaknesses, all disclosed rather than covert: the 07:00 → 23:00 UK anchor change is a deviation from the instance variable, logged under change control in §20; the conviction-based suppression of Trade 1 and the corroboration-based suppression of Trade 2 were both relaxed on instruction, with the flags preserved; and "the module's own gate" in §21b is build language surfacing in the deliverable. | §2; §5 exclusion bullet; §19 bullet 6; §20 anchor and leniency rows; §21b Trade 1 preamble | 4 | Remove the build-language phrase; otherwise the restriction set holds. |

## 2. Category roll-up

| Category | Level | Multiplier | Points | Justification |
|---|---|---|---|---|
| C1 Prompt adherence & instruction compliance (max 20) | 3 | 0.65 | 13.00 | Rows 1.1 / 1.2 / 1.3 = 2 / 3 / 5, mean 3.33 → 3. Asset, counters and their order, the D-1 as-of session, the 5/25 lookbacks, the currency and the audience register are all correct, and the source count clears six. Against that the tick size is never stated, the execution anchor is moved to a time at which the instrument does not trade, the card record carries two further anchors that match neither the declaration nor each other, and a monthly-series low has been imported into the 25-session field. |
| C2 Structural & modular framework alignment (max 20) | 4 | 0.85 | 17.00 | Rows 2.1 / 2.2 / 2.3 = 3 / 3 / 5, mean 3.67 → 4. The method chain §4 → §5 → §8 → §9 is fully visible and unusually explicit about normalisation and precedence, and §11's three frames are correctly shaped R3 → P → S3. Two structural shortfalls hold the category below 5: the previous-period calendar is missing from §13 entirely, and §6 has dropped the Source A / Source B / Final columns that the prior day's report carried. |
| C3 Accuracy, evidence & factual reliability (max 25) | 3 | 0.65 | 16.25 | Rows 3.1 / 3.2 / 3.3 / 3.4 = 2 / 4 / 2 / 2, mean 2.50, which rounds up to 3. The category sits exactly on the 2/3 boundary and is recorded here on the round-half-up convention, so the reviewer note matters more than the level: the OHLC grid is genuinely accurate (thirteen of fifteen O/H/L/C values inside tolerance, worst close error 4.30), all twenty-one pivot levels reproduce to the cent from the report's own inputs with the floor identity holding on all three frames, and the §21c backtest reproduces exactly from §6 with no leakage. The offsetting failures are material: the RSI2 column does not reproduce from the report's own closes (worst delta 29.6), two Trend cells break the stated rule, a monthly low is used as the 25-session low and drives three sections, and §1/§12/§14 carry a long list of unsourced numbers. |
| C4 Reasoning, judgment & evaluation quality (max 20) | 4 | 0.85 | 17.00 | Rows 4.1 / 4.2 / 4.3 / 4.4 = 4 / 5 / 2 / 4, mean 3.75 → 4. The analytical layer is the report's strongest work: real transmission mechanisms per counter, an explicit precedence rule where the efficiency ratio and the regime read disagree, a cross-asset contradiction that is named and carried through to a zero score contribution, and card caveats that quantify their own weaknesses. The card construction layer is where it fails — Trade 2 uses the range construction under a transitional label, and Trade 3 selects the 3B fork and then does not apply 3B's geometry. |
| C5 Currency, restrictions & transparency (max 15) | 4 | 0.85 | 12.75 | Rows 5.1 / 5.2 / 5.3 / 5.4 = 3 / 4 / 5 / 4, mean 4.00 → 4. Disclosure is the report's defining strength: the anchor deviation is stated four times with its execution consequence spelled out before any card, the single-source indicative flag is propagated from §6 through §11 and §19 into every card caveat, the leniency relaxations are logged with reasons, and the §13d collision grade is carried verbatim onto the cards. Held to 4 by the unexplained corroboration-status conflict with the 22 Jul report and by counter-asset levels used without dates. |
| **Total** | — | — | **76.00 → 76** | Σ(multiplier × max) = 13.00 + 17.00 + 16.25 + 17.00 + 12.75 = 76.00. |

## 3. Total, band, override check

- **Raw total: 76.00 → 76 / 100. Band: High Trust (75–89).** The score sits one point above the Moderate/High
  boundary and is sensitive to the C3 rounding: C3's row mean is exactly 2.50, and had it been taken down to
  level 2 the total would be 69.75 → 70 (Moderate). The round-half-up convention is applied as stated in the
  reviewer brief, and the sensitivity is recorded here so the operational decision is made with it in view.
- **Hallucinated-source override: NOT triggered.** Three cited sources were spot-checked — the index provider
  release via FRED (21 Jul, 7,509.20), the CNBC market report (22 Jul, −0.14%) and Trading Economics (21 Jul,
  +0.89%). Each is named, dated ≤ D-1, and each quoted figure is arithmetically coherent with its own text and
  used consistently elsewhere: 7,509.20 − 7,498.96 = 10.24 exactly as §1 states; (7,498.96 − 7,509.20)/7,509.20
  = −0.1364% ≈ −0.14%; (7,509.20 − 7,443.28)/7,443.28 = +0.8857% ≈ +0.89%, matching §8. The rejected
  Investing.com row is documented as rejected with a stated rationale in §4, §5 and §20, which is correct
  handling rather than a fabrication. The two dating blemishes found (the CNBC §13a URL slug dated 2026/07/21
  against a 22 Jul article date; the Schwab row dated 21 Jul whose quote describes a session closing below
  7,500, which on the report's own closes is 20 Jul) are **reconcilable** — a live-blog slug carrying the
  prior evening's date, and a 21 Jul morning piece recapping the 20 Jul session — so neither source is
  impossible or self-contradictory on its own terms. No cap at 59; C3 is not forced to 0.
- **Restriction-breach override: NOT triggered.** The listed restrictions hold. No synthesised or interpolated
  price is presented as sourced — the reconstructed O/H/L are labelled INDICATIVE in §6, §11, §19 and on every
  card. No retail CFD quotes enter the OHLC basis; the one CFD-derived table encountered is rejected with the
  restriction cited. ES futures are excluded from the §2 definition and confined in §19 to confirmation and
  narrative context. A grep of the full report returns no bracketed variable names, no module codes (M1–M5)
  and no framework name; instrument common names are used throughout. The 07:00 UK → 23:00 UK anchor change
  is a **deviation from a Variable, not a violation of a restriction**: it is instructed, logged under change
  control in §20 with its consequence quantified, and repeated in a bold execution notice before any card —
  the same handling pattern the 22 Jul report applied to its 00:00 UK override. It is scored down in rows 1.1,
  1.2 and 5.4 rather than treated as a breach. The two suppression relaxations (Trade 1 on conviction, Trade 2
  on corroboration) are likewise instructed and disclosed, and are scored in row 4.3. No cap at 74; no forced
  C1 downgrade.
- **Final Trust Score: 76 — High Trust. Override: none.** Operational meaning: usable with the corrections in
  `2026-07-23_feedback.md` applied. The RSI2 column, the 25-session low, and the Trade 2 / Trade 3 fork
  selection are the three items that must be fixed before the output is relied on.

## 4. Card Integrity

Linter rows copied verbatim from `qa/regen_20260906_qa1/lint_static/2026-07-23.csv`:

| card_id | report_date | strategy | flags | dud |
|---|---|---|---|---|
| 2026-07-23_Trade_1 | 2026-07-23 | Trade 1 - Daily Directional | WARN_R_TINY(0.30xATR) | False |
| 2026-07-23_Trade_2 | 2026-07-23 | Trade 2 - Pivot (buy limit daily S1) | CLEAN | False |
| 2026-07-23_Trade_3 | 2026-07-23 | Trade 3 - Pivot fade (sell limit daily R2) | CLEAN | False |

Per-card integrity, 100 − 40·(#DUD) − 10·(#WARN), floored at 0:

| card_id | #DUD | #WARN | Integrity |
|---|---|---|---|
| 2026-07-23_Trade_1 | 0 | 1 | 90 |
| 2026-07-23_Trade_2 | 0 | 0 | 100 |
| 2026-07-23_Trade_3 | 0 | 0 | 100 |

**Report mean over non-suppressed cards: (90 + 100 + 100) / 3 = 96.7.** No card is marked suppressed in the
lint file or the card record, so all three enter the mean. Totals: 3 cards, 0 DUD flags, 1 WARN flag.

Assessment against the card-construction rules (feeds row 4.3, **not** the integrity number above):

- **Trade 1 — Daily Directional (SHORT).** Static geometry is sound: the MARKET entry equals the D-1 close
  (7,498.96 against a slice cash close of 7,498.80, Δ 0.16), the stop is on the correct side, TP1 is beyond
  entry, TP2 beyond TP1, TP3 beyond TP2, TP1 sits well inside 2.5 × ATR14, and the anchor is explicit. R of
  22.18 points is 0.31 × the report's ATR and 0.35 × the slice cash ATR14 of 63.97 — above the 0.3 floor but
  close enough to it that WARN_R_TINY fires correctly. Two rule defects the linter cannot see: the stated
  structural anchor, "nearest resistance at 7,503.41", is the **16 Jul low** taken from the report's own §6
  table, not a resistance level, and the stop rule requires the tighter of the 5-day swing extreme (7,570.53
  on the report's numbers, 7,572.20 on the slice) and the nearest S/R; and the direction score magnitude
  0.0187 is below the 0.25 conviction threshold, so the card record must carry `suppressed: true` — it
  currently carries `false` while §21b heads the card "SUPPRESSED BY CONVICTION RULE".
- **Trade 2 — buy limit at daily S1 (LONG).** Static geometry is clean and the limit sits on the correct side
  of the D-1 close. Rule defects: the regime label in §9 is TRANSITIONAL, under which Trade 2 is breakout-side
  only, yet the card is a mean-reversion limit at S1 with ±1R/±2R targets — the RANGE construction — issued
  under an invented "transitional-regime variant" label; and §19 states that every pivot tier carries the
  single-source indicative flag, which under the pivot rule suppresses the card outright. R of 68.55 points is
  1.07 × the slice cash ATR14, above 1 × ATR, so the wide-stop flag is mandatory on the slice basis even
  though the card computes 0.97 × ATR from its own figure.
- **Trade 3B — sell limit at daily R2 (SHORT).** Static geometry is clean. Rule defects: on a TRANSITIONAL
  regime label the 3C fork applies, not 3B; and 3B's own geometry is not used anywhere on the card — the entry
  is daily R2 rather than the 78.6–88.6% band of the 25-day range, the stop is the 16 Jul high + 0.25 ATR
  rather than 10% of width, and TP1/TP2/TP3 are the daily pivot, weekly pivot and daily S1 rather than the
  range midpoint and the far side − 10%. On the report's own 25-session range the R2 entry sits at 89.8%, above
  the 88.6% ceiling of the permitted band. The card record also states `be_rule: NONE` while the card text
  specifies "Unit 3 stop moves to entry +0.2R (7,550.17)" on TP2 fill.

## 5. Data reconciliation log

| Section | Report value | Slice value | Delta | Verdict |
|---|---|---|---|---|
| §6 16 Jul Open | 7,552.37 | 7,554.00 | −1.63 | OK |
| §6 16 Jul High | 7,570.53 | 7,572.20 | −1.67 | OK |
| §6 16 Jul Low | 7,503.41 | 7,506.00 | −2.59 | OK |
| §6 16 Jul Close | 7,531.90 | 7,536.20 | −4.30 | FAIL — close tolerance is 3.00 |
| §6 16 Jul RSI2 | 34.6 | 42.18 | −7.58 | Note — not testable from the report's own closes (needs prior-window closes) |
| §6 17 Jul Open | 7,445.21 | 7,443.70 | +1.51 | OK |
| §6 17 Jul High | 7,497.49 | 7,497.30 | +0.19 | OK |
| §6 17 Jul Low | 7,432.37 | 7,431.60 | +0.77 | OK |
| §6 17 Jul Close | 7,457.35 | 7,456.60 | +0.75 | OK |
| §6 17 Jul RSI2 | 11.6 | 0.00 | +11.60 | Note — not testable from the report's own closes; slice returns 0.00 |
| §6 17 Jul Trend | Bearish | close 7,457.35 > open 7,445.21 | — | FAIL — Bearish requires Close < Open; the rule admits Neutral only |
| §6 20 Jul Open | 7,495.18 | 7,495.30 | −0.12 | OK |
| §6 20 Jul High | 7,511.93 | 7,512.80 | −0.87 | OK |
| §6 20 Jul Low | 7,439.50 | 7,439.30 | +0.20 | OK |
| §6 20 Jul Close | 7,443.28 | 7,446.60 | −3.32 | FAIL (marginal, tolerance 3.00) |
| §6 20 Jul RSI2 | 9.3 | 0.00 (slice); 0.0 from the report's own closes | +9.30 | FAIL — does not reproduce from the report's own closes |
| §6 21 Jul Open | 7,487.45 | 7,487.70 | −0.25 | OK |
| §6 21 Jul High | 7,515.04 | 7,515.70 | −0.66 | OK |
| §6 21 Jul Low | 7,466.28 | 7,466.50 | −0.22 | OK |
| §6 21 Jul Close | 7,509.20 | 7,508.00 | +1.20 | OK |
| §6 21 Jul RSI2 | 68.5 | 85.99 (slice); 82.4 from the report's own closes | −13.90 vs own closes | FAIL — does not reproduce from the report's own closes |
| §6 22 Jul Open (D-1) | 7,490.76 | 7,490.30 | +0.46 | OK |
| §6 22 Jul High (D-1) | 7,524.88 | 7,525.50 | −0.62 | OK |
| §6 22 Jul Low (D-1) | 7,488.26 | 7,488.00 | +0.26 | OK |
| §6 22 Jul Close (D-1) | 7,498.96 | 7,498.80 | +0.16 | OK — and identical in §1, §3, §4, §11, §18 and the Trade 1 entry |
| §6 22 Jul RSI2 (D-1) | 57.0 | 86.97 (slice); 86.6 from the report's own closes | −29.60 vs own closes | FAIL — largest arithmetic error in the report; propagates to §8, §9 median and §21a |
| §6 22 Jul Trend | Neutral | close 7,498.96 > open 7,490.76, RSI2 57.0 > 50 | — | FAIL — the stated rule gives Bullish on either the stated or the corrected RSI2 |
| §11 Daily P | 7,504.03 | 7,504.10 | −0.07 | OK — reproduces to the cent from the report's own 22 Jul H/L/C |
| §11 Daily R1 | 7,519.81 | 7,520.20 | −0.39 | OK — reproduces exactly (2P − L) |
| §11 Daily R2 | 7,540.65 | 7,541.60 | −0.95 | OK — reproduces exactly (P + (H−L)) |
| §11 Daily R3 | 7,556.43 | 7,557.70 | −1.27 | OK — reproduces exactly (H + 2(P−L)) |
| §11 Daily S1 | 7,483.19 | 7,482.70 | +0.49 | OK — reproduces exactly (2P − H) |
| §11 Daily S2 | 7,467.41 | 7,466.60 | +0.81 | OK — reproduces exactly (P − (H−L)) |
| §11 Daily S3 | 7,446.57 | 7,445.20 | +1.37 | OK — reproduces exactly (L − 2(H−P)) |
| §11 Daily floor identity | R2 − P = 36.62 | P − S2 = 36.62 | 0.00 | OK — identity holds |
| §11 Weekly P (w/e 17 Jul) | 7,490.13 | 7,490.33 | −0.20 | OK — reproduces from implied H 7,580.67 / L 7,432.38 / C 7,457.34, the last matching the report's own 17 Jul close |
| §11 Weekly R1 | 7,547.88 | 7,549.07 | −1.19 | OK |
| §11 Weekly R2 | 7,638.42 | 7,641.53 | −3.11 | OK |
| §11 Weekly R3 | 7,696.17 | 7,700.27 | −4.10 | OK |
| §11 Weekly S1 | 7,399.59 | 7,397.87 | +1.72 | OK |
| §11 Weekly S2 | 7,341.84 | 7,339.13 | +2.71 | OK |
| §11 Weekly S3 | 7,251.30 | 7,246.67 | +4.63 | OK |
| §11 Weekly floor identity | R2 − P = 148.29 | P − S2 = 148.29 | 0.00 | OK — identity holds |
| §11 Monthly (June) P | 7,436.89 | not in slice | n/a | Unverifiable against the slice; internally consistent — implies H 7,629.02 / L 7,189.38 / C 7,492.27, and identity R2 − P = P − S2 = 439.64 holds |
| §9 25-session low | 7,189.38 | 7,303.10 (26 Jun) | −113.72 | FAIL — equals the low implied by the June monthly pivots; a monthly series in a 25-session field |
| §9 25-session high | 7,580.66 | 7,582.80 (15 Jul) | −2.14 | OK |
| §9 25-session width | 391.28 | 279.70 | +111.58 | FAIL — inherited from the low |
| §9 / §15 / §21b position in 25-session range | 79.1% | (7,498.96 − 7,303.10)/279.70 = 70.0% | +9.1 pp | FAIL — drives the §15 "upper half" claim and the §21b 3B fork rationale |
| §3 / §21b ATR(14) | 70.91 (implied by every card ratio: 0.25× = 17.73, 3.5× = 248.19) | 63.97 (cash) / 74.00 (full day) | +6.94 / −3.09 | Note — sits between the two bases, closer to full-day; not reproducible from cash-session bars |
| §8 / §16 support shelf | 7,432.37 (17 Jul low), retest 7,439.50 (20 Jul) | 7,431.60 / 7,439.30 | +0.77 / +0.20 | OK |
| §8 / §16 resistance | 7,570.53 (16 Jul high) | 7,572.20 | −1.67 | OK |
| §10 / §14 USDX level | 100.98 | D-1 close 101.102 (100.968 is the 20 Jul close) | −0.12 | Note — the figure is the 20 Jul close presented as current, undated |
| §10 / §14 VIX range | "18.65 to 17.05", easing to 17.2–17.4 | D-1 close 17.40; window 16–22 Jul high 18.52, low 17.00 | 18.65 not observed | Note — the D-1 level and the falling direction are right; the 18.65 anchor is undated and above any value in the window |
| §10 DAX 40 level | ~25,150 | no DAX slice available | n/a | Unverifiable |
| §4 Tiingo row normalisation | 747.41 → 7,498.96 | 747.41 × 10.0329 = 7,498.69 | +0.27 | Note — explained by §19's rule that corroborated closes were pinned and not scaled, but the §4 row does not say so |
| §5 / §19 scale factor | 10.0329 = mean(10.0302, 10.0353, 10.0333) | mean = 10.03293 | 0.00 | OK — arithmetic exact |
| §19 scale-factor dispersion | 0.0051 = "0.05 basis points" | 0.0051 / 10.0329 = 5.08 bp | ×100 | FAIL — unit error |
| §21a component sum | −0.0187 | −0.0750 + 0.0500 − 0.0350 + 0.0563 − 0.0150 + 0.0000 = −0.0187 | 0.00 | OK — exact; implies the default weights 0.25 / 0.20 / 0.10 / 0.15 / 0.15 / 0.15, and the sentiment term 0.15 × (−0.10) matches §13b's tilt |
| §21c prior-session S1/R1, 22 Jul row | 7,478.64 / 7,527.40 | from 21 Jul H/L/C: 7,478.64 / 7,527.40 | 0.00 | OK — as do the 17, 20 and 21 Jul rows; every fill / no-fill call matches §6's highs and lows |
| §21c net R | −1.12 long / +0.51 short | −0.12 − 1.00 / +0.85 − 0.34 | 0.00 | OK |
| §1 session change | −10.24 points, −0.14% | 7,509.20 − 7,498.96 = 10.24; −0.1364% | 0.00 | OK |
| §8 five-session mean range | 58.0 | mean(67.12, 65.12, 72.43, 48.76, 36.62) = 58.01 | −0.01 | OK — every individual range reproduces from §6 |
| §8 RSI2 standard deviation | 26.5 | sample s.d. of 34.6, 11.6, 9.3, 68.5, 57.0 = 26.49 | +0.01 | OK on the stated values (which are themselves wrong) |
| §6 16/17/21 Jul closes vs 22 Jul report | 7,531.90 / 7,457.35 / 7,509.20 | prior report: 7,533.77 / 7,457.69 / 7,506.47, all "CORROBORATED Δ0.00" | −1.87 / −0.34 / +2.73 | FAIL — two reports claim zero-delta corroboration on the same sessions for different values |
| Card record vs §21b — Trade 1 suppression | §21b: "SUPPRESSED BY CONVICTION RULE" | `cards/baseline/by_date/2026-07-23.json`: `suppressed: false` | — | FAIL — the flag did not propagate to the machine-readable record |
| Card record vs §21b — Trade 3 BE rule | §21b: "Unit 3 stop moves to entry +0.2R (7,550.17)" | card record: `be_rule: NONE` | — | FAIL |
| Card record vs declared anchor | Header / §2 / §20: 23:00 UK (= 01:00 broker) | card record: `anchor_broker` 16:30 (Trade 1), 09:00 (Trades 2, 3) | — | FAIL — three anchors across the declaration and the two card groups |
