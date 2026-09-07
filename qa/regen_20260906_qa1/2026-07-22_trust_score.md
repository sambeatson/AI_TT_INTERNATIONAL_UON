# Trust Score — 2026-07-22 — SP500_Report_22Jul2026.md

Reviewer inputs: report for D = 2026-07-22; slice `data/slices/US500/US500_upto_2026-07-21.csv` (last bar
2026-07-21 23:45, cash session 16:30–23:00 broker); `engine/qa_slice_stats.py` run with the report's own five
§6 closes; `cards/baseline/by_date/2026-07-22.json`; `qa/regen_20260906_qa1/lint_static/2026-07-22.csv`;
cross-report check against `reports/md/SP500_Report_21-Jul-2026.md` (dated before D). Tolerances per the
reviewer brief: |Δ| ≤ 3 pts on a close, ≤ 8 pts on an open/high/low.

Helper reference values (cash session unless stated): ATR14 69.44 (full-day 78.02) · D-1 close 7508.00 ·
D-1 pivots P 7496.73 R1 7526.97 R2 7545.93 R3 7576.17 S1 7477.77 S2 7447.53 S3 7428.57 ·
5-day swing high 7582.80 (15 Jul) / low 7431.60 (17 Jul) · 25-day high 7582.80 / low 7303.10 (width 279.70).

## 1. Section 7 checklist

| Item | Reviewer notes | Evidence observed | Score 0–5 | Action required |
|---|---|---|---|---|
| 1.1 Variables respected | Asset is the S&P 500 cash index, not ES; counters USDX · VIX · DAX 40 with USDX first; as-of "Tue 21 Jul 2026 close (America/New_York)" is genuinely D-1 (21 Jul is a Tuesday) and the 5-session block correctly skips the weekend; lookback 5 (execution) / 25 (regime); USD, index points, tick 0.01 stated; six §4 sources but two of the six (Motley Fool, SPDR/Tiingo ETF proxy) sit outside the index-provider / exchange / sell-side tiers. Two real deviations: (a) §2 declares the basis "cash only; no pre/after-market OHLC" yet three §6 opens (15, 17, 21 Jul) match the broker **full-day** open, not the cash open — see §5 log; (b) the daily-open anchor is overridden from the instance default 07:00 UK to 00:00 UK (§20), while the extracted card record carries `anchor_broker 09:00` (= 07:00 UK), so the report and the card disagree about the anchor actually used. | Header; §2; §4; §6; §20 anchor-override bullet; `cards/baseline/by_date/2026-07-22.json` | 2 | Rebuild §6 O/H/L on the cash session only; state one anchor consistently across §20 and §21b. |
| 1.2 Coverage & currency consistent | No data item is dated on or after D; every §4/§6/§13a source is 17–21 Jul; the session under review is 22 Jul. No currency or unit drift (USD / index points throughout; Brent quoted as USD in §12 and not mixed into the index basis). Two coverage defects: §11 daily pivots are built from **Mon 20 Jul** (D-2) rather than D-1, and §21c reports "5+ (open)" days to resolution for a t−3 entry when only three sessions (17, 20, 21 Jul) exist inside the window. | §11 heading "Daily pivots (from Mon 20 Jul H/L/C)"; §21c row 3 | 3 | Rebase daily pivots on 21 Jul; cap §21c resolution counts at the sessions available. |
| 1.3 Audience & tone | Consistent senior-strategist register: pre-open trading-and-risk-review framing, explicit conviction/confidence language, invalidation levels, no retail promotion, no return promises. §18 is a proper analyst judgement with three ranked reasons and a single watch item. | §1; §16; §18 | 5 | None. |
| 2.1 Sections present & ordered | All of §1–§21 present in the prescribed order, including §13a per-article table, §13b aggregate with a numeric tilt (+0.65), §13c previous-period and §13d upcoming calendars, and §21a–§21d with the limitations boilerplate. §17 is exactly one sentence. | Headings throughout | 5 | None. |
| 2.2 Scorecard as a table | §6 is a table carrying Date/O/H/L/C/RSI2/Trend/Source A/Source B/Final/Validation. §11 gives daily, weekly and monthly frames ordered high→low. Two blemishes: the pivot tables run R5→S5 (five levels each side) where the spec is R3→P→S3 (three), and the 21 Jul Validation cell reads "CORROBORATED (Δ close)" with the delta figure missing, unlike the other four rows which state "(Δ0.00)". | §6 row 5; §11 three tables | 4 | Trim pivot tables to R3→P→S3; supply the numeric Δ on every Validation cell. |
| 2.3 Method steps visible | §4 observations → §5 classification and consensus build with the tolerance and exclusion rule stated; §8 is candle-by-candle across all five sessions followed by an explicit sequence assessment; §9 states overlap ratio, directional persistence, absolute directional mean, median RSI2 and VOLator slope before naming the regime; §7 charts survive as five captioned image placeholders (pandoc drops the images — captions accepted as evidence and noted here). | §4–§9 | 5 | None. |
| 3.1 Quantitative claims sourced | Sourced: Q2 blended earnings growth ~24.7% (FactSet) and the ~88% beat rate, which is corroborated by the §13a CNBC quote. Unsourced and not pointed to §4/§6/§13: ex-chips growth ~16.8%, "the bulk of the beat is concentrated in Micron and Nvidia", decliners ~64%, 10-year ~4.55% (twice), Fed funds 3.75%, "VIX in the 17–19 area", Brent "above ~$89" (only loosely supported by the §13c row). §12 also carries 88% (CNBC) and §13a carries 82.3% (Zacks) as beat rates without reconciling them. | §12 bullets 1, 4, 5; §14 bullets 1, 5; §13a rows 3 and 6 | 2 | Attach a source or an internal §4/§6/§13 pointer to every number in §12 and §14; reconcile 88% vs 82.3%. |
| 3.2 Citations exist & contain data | All cited sources are named, dated (all ≤ D-1) and quote a figure; §13a carries a ≤15-word derivation quote per row. Three spot-checks: (a) S&P Dow Jones via FRED, 17 Jul close 7,457.69 — matches §6 and the §13c "risk-off close at 7,458" narrative, consistent; (b) Benzinga, 20 Jul open 7,489.18 — matches the §6 20 Jul open exactly, consistent; (c) SPDR S&P 500 ETF (Tiingo), 21 Jul close 748.19 → "7,481.9 (×10 proxy)" — the arithmetic of the quote is correct, but §6 then uses it as **Source B corroborating a 7,506.47 close**, a 24.57-point gap, under §5's claimed "±0.10-point equity-index tolerance", while §4 itself labels the same source "Directional / Shape-scale corroborator only". The figure is coherent with itself, so this is a misuse of a real source, **not** a fabricated one — no hallucination override. | §4 rows 1, 4, 5; §5; §6 row 5 | 3 | Replace the SPY proxy as Source B for the 21 Jul close with a second cash-index source, or re-label the row as single-source. |
| 3.3 Calculations transparent | RSI2 reproduces **exactly** from the report's own closes for 17 Jul (0.0), 20 Jul (0.0) and 21 Jul (81.4) — helper output "n/a, n/a, 0.0, 0.0, 81.4". The 15 Jul RSI2 of 42.7 is wrong: it duplicates the 16 Jul value, the slice gives 100.00, and the 21 Jul report gives 100.0 for the same session; the error propagates to the Trend cell (should be Bullish: close 7,572.40 > open, RSI2 > 50) and to the §8 "RSI2 mid-40s — early loss of upside momentum" narrative. Pivots: all three frames reproduce exactly from the H/L/C they declare and satisfy R2−P = P−S2 (daily 69.70 = 69.70; weekly 133.70 = 133.70; monthly 196.30 = 196.30) — but the daily frame is built on D-2. **ATR(14) is never stated anywhere in the report**, although the card's stop sizing and the Trade 1 runner cap both depend on it. KER stated (+0.06). §21a arithmetic checks (+0.0975 − 0.075 + 0.009 = +0.0315 ≈ +0.03) but only three of the six weighted components are shown; the other three are dismissed as "net to zero" without signals. | §6 RSI2 column; §11 three tables; §9; §20 direction-score bullet; §21a | 2 | Correct the 15 Jul RSI2 and Trend; state ATR(14) numerically; show all six weighted signals. |
| 3.4 Numbers reconcile | Reconciles: D-1 close 7,506.47 identical in §1, §3, §4, §6 and §18; §11 daily R2 7,528.63 matches the card's "daily R2 (7,529)"; §6 RSI2 matches §8 (mid-40s, 0, 81) and the §21a input. Fails: ATR is absent so §9 and §21 cannot be reconciled at all; §1 labels the short-term state "Transitional — Bearish" while §8's judgement label is "Exhaustion — reversal risk"; the card's confluence line calls 7,364 "weekly S3" when §11 weekly S3 is 7,277.26 (7,364.23 is weekly S2); the card claims the short zone "overlaps ... the 15 Jul swing high (7,585)" when the zone tops out at 7,552.5, 32.4 points away; §21a states the cross-asset contribution as −0.08 while §20 states −0.075; the extracted card carries tp3 = 7,300.9, a level the report text never states. | §1 vs §8; §21b Confluences row; §21a vs §20; card JSON | 2 | Fix the four cross-references above and publish a TP3 price (or an explicit null) in §21b. |
| 4.1 Pillars conclude | §8 ends "Exhaustion — reversal risk"; §9 ends "Ranging" with a top-sell bias and a preferred protocol; §10 ends "Aggregate cross-asset read = CONTRADICT"; each §12 driver carries a direction tag (price-supportive / event-driven / reversible / neutral); §14 bullets each close on a direction. Labels are consistent with the content beneath them. Only defect: §1's short-term label does not match §8's. | §8–§10; §12; §14 | 4 | Carry §8's label verbatim into §1. |
| 4.2 Peer/cross-asset interpreted | §10 supplies a transmission mechanism per counter — dollar → global financial conditions and multinational earnings translation; VIX → implied vol → equity multiples; DAX → common global risk-appetite factor — rather than a correlation list, and states a status and an implication for each. The two-against-one contradiction is named and then carried forward into §15, §16 and the §21a score rather than being dropped. | §10; §15; §16; §21a | 5 | None. |
| 4.3 Synthesis reconciles tensions | The narrative synthesis is genuinely good: §13b flags the sentiment-vs-technical divergence and rules for the technicals; §15/§16 hold the 21 Jul reversal bar against the ranging regime; §16 gives two-sided invalidation levels; §21a flags the conflict and explains why conviction does not clear ±0.25. The **card layer** is where synthesis fails: Trade 2 is suppressed with the reason "TRANSITION/ranging tape", but §9 and §1 both call the regime RANGING, and under the range rule a Trade 2 must be posted as limits at R1/R1.5/R2 (top-sell side) unless every pivot tier is single-source-indicative — §19 explicitly states the pivots are corroborated, so the suppression is not available; the stated 3B entry bands admit fills where R = 4.0 points, below 0.3×ATR14 = 20.83; no TP3 price is given; the Unit-3 rule on Unit-2 fill is written as "mid ± 0.05 × width" instead of entry ± 0.2R; and the card carries an anchor caveat ("executed at the overridden 00:00 UK anchor / 22 Jul cash open") that is meaningless on a pair of limit orders. | §13b; §15; §16; §21a; §21b Trade 2 line and 3B table | 2 | Post a rule-conformant Trade 2 or suppress it on a permitted ground; constrain the 3B entry bands; restore the entry ± 0.2R unit rule. |
| 4.4 Calibrated language | §17 is exactly one sentence, directional but bounded, with no hedge stacking; confidence Medium is stated in §3 and repeated in §18; §16 separates base case from invalidation. Weaker in §21b, where "BIDIRECTIONAL — analyst selects the side that price reaches first" pushes the direction decision back to the reader, and "Risk ≈ 4–32 points depending on fill" leaves R an eightfold range instead of a defined number. | §3; §17; §18; §21b Direction and SHORT stop rows | 3 | Define R per tier rather than as a range; state a primary side. |
| 5.1 Data dated; staleness flagged | Every price row and every article carries a date. But §19 asserts "all five session closes are exchange-official and dual-source corroborated" and "none are single-source-only for pivot inputs", which contradicts §6's own 21 Jul row (Source B = "SPY proxy", a source §4 restricts to directional use) and contradicts the 21 Jul report, which classified the identical 15–20 Jul O/H/L rows as "single-src" and expressly barred them from pivot corroboration. The status flip between the two reports is unexplained. The D-2 pivot base is also used without any staleness flag. | §6 row 5; §19 bullets 1–2; §11 heading; `SP500_Report_21-Jul-2026.md` §6/§11 | 2 | Reconcile the corroboration status of the 15–20 Jul O/H/L with the prior report or explain the upgrade. |
| 5.2 Assumptions up front | The anchor override is disclosed twice — logged in §20 under the change-control rule with the cash-session-hours caveat spelled out, and repeated in the card's Caveats row — which is the right handling of a deviation. §19 states the exclusion rule and the ~86-point CFD divergence that triggered it. Gaps: the ATR assumption underpinning every stop is never surfaced; the §6 High/Low construction ("official day-range plus scaled ETF shape") is stated but its effect on the pivots is not; §19's claim that no strategy was suppressed for corroboration is true but silently leaves the Trade 2 regime suppression unjustified. | §19; §20; §21b Caveats | 3 | Surface ATR(14) and the H/L construction as explicit assumptions. |
| 5.3 Red flags surfaced | Strong. §12 carries concentration, geopolitical-reversal and breadth flags; §15 gives three upside and three downside risks with levels; §13b flags the sentiment/price divergence; §10 flags the cross-asset contradiction; §13d's Tier-1 Alphabet/Tesla collision is carried into the card's Caveats row with an explicit size-down / stand-aside instruction; §21d states the five-session sample limitation. | §12; §13b; §13d; §15; §21b Caveats; §21d | 5 | None. |
| 5.4 Restrictions honoured | Honoured: retail CFD quotes are explicitly excluded from the OHLC basis with the divergence quantified (§4 note, §5, §19); ES/pre-open futures appear only as context in §3, never as a price basis; no bracketed variable names, no module codes, no framework name; instrument common names used throughout. Weakness: the intraday High/Low are partly derived from a ×10-scaled ETF shape, and §19 then presents them as corroborated with none single-source — a derived input carried into the pivot chain as though independently sourced. The 07:00 → 00:00 UK anchor change is a deviation from the instance default, but it is disclosed and change-controlled in §20, so it is recorded as a deviation, not scored as a breach. | §4 note; §5; §19; §20 | 3 | Do not present ETF-scaled H/L as independent corroboration; label it as derived. |

## 2. Category roll-up

| Category | Level | Multiplier | Points | Justification |
|---|---|---|---|---|
| C1 Prompt adherence & instruction compliance (max 20) | 3 | 0.65 | 13.00 | Rows 1.1 / 1.2 / 1.3 = 2 / 3 / 5, mean 3.33 → 3. Asset, counters, window, units and audience are right and the as-of session is genuinely D-1, but the declared cash-only OHLC basis is not held (three full-day opens), the daily pivot frame is D-2, and the report and the card record disagree on the execution anchor. |
| C2 Structural & modular framework alignment (max 20) | 5 | 1.00 | 20.00 | Rows 2.1 / 2.2 / 2.3 = 5 / 4 / 5, mean 4.67 → 5. Every section and sub-section is present, ordered and populated; the method chain §4→§5→§8→§9 is fully visible; only the pivot-table depth and one incomplete Validation cell fall short. |
| C3 Accuracy, evidence & factual reliability (max 25) | 2 | 0.40 | 10.00 | Rows 3.1 / 3.2 / 3.3 / 3.4 = 2 / 3 / 2 / 2, mean 2.25 → 2. Closes are sound (max |Δ| 3.32) and three of five RSI2 values reproduce exactly, but nine of fifteen O/H/L values breach the basis tolerance, the 15 Jul RSI2 is wrong by 57 points and mis-labels the Trend, the daily pivots are off a D-2 base, ATR(14) is never stated, and several cross-references (weekly S3, swing-high confluence, §1 vs §8) do not reconcile. |
| C4 Reasoning, judgment & evaluation quality (max 20) | 4 | 0.85 | 17.00 | Rows 4.1 / 4.2 / 4.3 / 4.4 = 4 / 5 / 2 / 3, mean 3.50 → 4. The analytic layer is the report's strongest work — genuine cross-asset mechanisms, pillar labels that follow their evidence, tensions held open rather than smoothed — but the card layer suppresses Trade 2 on a ground the range rule does not allow and ships a 3B card whose permissive end sizes R below the engine's floor. |
| C5 Currency, restrictions & transparency (max 15) | 3 | 0.65 | 9.75 | Rows 5.1 / 5.2 / 5.3 / 5.4 = 2 / 3 / 5 / 3, mean 3.25 → 3. Red-flag surfacing and the change-controlled anchor disclosure are exemplary; against that, §19's corroboration claim contradicts the report's own §6 row and the prior day's classification of the same sessions, and ETF-scaled H/L are presented as independent corroboration. |
| **Total** | — | — | **69.75 → 70** | Σ(multiplier × max) = 13.00 + 20.00 + 10.00 + 17.00 + 9.75 = 69.75, rounded to 70. |

## 3. Total, band, override check

- **Raw total: 69.75 → 70 / 100. Band: Moderate Trust (60–74).**
- **Hallucinated-source override: NOT triggered.** Three cited sources were spot-checked (S&P DJ via FRED 17 Jul 7,457.69; Benzinga 20 Jul open 7,489.18; SPDR/Tiingo 21 Jul 748.19 → 7,481.9). Each is named, dated ≤ D-1, and each quoted figure is arithmetically coherent with its own text and used consistently elsewhere in the report. The SPY-proxy defect is a **misuse** of a genuine source — a directional-only corroborator promoted to Source B for a close it misses by 24.57 points — not a source that is impossible or self-contradictory on its own terms. No cap at 59, C3 is not forced to 0.
- **Restriction-breach override: NOT triggered.** The listed restrictions hold: no retail CFD quotes in the OHLC basis (excluded explicitly, with the ~86-pt divergence quantified), ES/pre-open futures used for context only, no bracketed variable names, no module codes, no framework name, instrument common names throughout. The 07:00 UK → 00:00 UK daily-open anchor change is a **deviation** — it is logged in §20 under the change-control rule with the cash-session caveat stated, and Trade 1 is suppressed so no entry actually executes on it — and is scored down in rows 1.1, 5.2 and 5.4 rather than treated as a breach. The ETF-scaled High/Low presented as corroborated in §19 is the closest call; it is recorded as a transparency failure under 5.1/5.4 because §4 and §6 both disclose the proxy on the face of the report. No cap at 74, no forced C1 downgrade.
- **Final Trust Score: 70 — Moderate Trust. Override: none.** Operational meaning: must not be used as-is; suitable as an input to a corrected regeneration. The remediation set is in `2026-07-22_feedback.md`.

## 4. Card Integrity

Linter rows copied verbatim from `qa/regen_20260906_qa1/lint_static/2026-07-22.csv`:

| card_id | report_date | strategy | flags | dud |
|---|---|---|---|---|
| 2026-07-22_Trade_1 | 2026-07-22 | Trade 1 - Daily Directional | SUPPRESSED | False |
| 2026-07-22_Trade_2 | 2026-07-22 | Trade 2 - Pivot (regime-aware) | SUPPRESSED | False |
| 2026-07-22_Trade_3B | 2026-07-22 | Trade 3B - Mean-Reversion (range fade, short leg) | CLEAN | False |

Per-card integrity, 100 − 40·(#DUD) − 10·(#WARN), floored at 0:

| Card | #DUD_* | #WARN_* | Integrity | Counted in the mean |
|---|---|---|---|---|
| 2026-07-22_Trade_1 | 0 | 0 | 100 | No — SUPPRESSED |
| 2026-07-22_Trade_2 | 0 | 0 | 100 | No — SUPPRESSED |
| 2026-07-22_Trade_3B | 0 | 0 | 100 | Yes |

**Report Card Integrity = 100.0** (mean over non-suppressed cards; n = 1). Cards in the lint file: 3. DUD flags: 0. WARN flags: 0.

Note — the integrity number is a static-lint result only and is **not** an endorsement of the cards. The M5 assessment behind row 4.3 is separate and found: Trade 1 correctly suppressed (|+0.03| < 0.25, posted as a SUPPRESSED row rather than omitted); Trade 2 suppressed on a ground the RANGE rule does not permit, with the regime mis-named "TRANSITION" in the suppression line; Trade 3B linted CLEAN only because the extracted record pins the entry at the zone floor 7,524.1 (R = 32.4, inside 0.3–3.0 × ATR14), whereas the report text authorises fills to 7,552.5 where R falls to 4.0 points — below the 20.83-point floor — and the same 4.0-point minimum applies to the long leg, which the linter never sees because only the short leg is extracted.

## 5. Data reconciliation log

Cash-session basis (16:30–23:00 broker). Tolerance: close |Δ| ≤ 3, open/high/low |Δ| ≤ 8.

| Section | Report value | Slice value | Delta | Verdict |
|---|---|---|---|---|
| §6 15 Jul Open | 7548.10 | 7569.10 | −21.00 | FAIL — matches the broker full-day open (7547.4), not the cash open |
| §6 15 Jul High | 7584.90 | 7582.80 | +2.10 | OK |
| §6 15 Jul Low | 7541.20 | 7528.60 | +12.60 | FAIL |
| §6 15 Jul Close | 7572.40 | 7573.90 | −1.50 | OK |
| §6 15 Jul RSI2 | 42.7 | 100.00 | −57.30 | FAIL — duplicates the 16 Jul value; the 21 Jul report also states 100.0; Trend should be Bullish, not Neutral |
| §6 16 Jul Open | 7566.30 | 7554.00 | +12.30 | FAIL |
| §6 16 Jul High | 7571.80 | 7572.20 | −0.40 | OK |
| §6 16 Jul Low | 7503.40 | 7506.00 | −2.60 | OK |
| §6 16 Jul Close | 7533.77 | 7536.20 | −2.43 | OK |
| §6 16 Jul RSI2 | 42.7 | 42.18 | +0.52 | OK |
| §6 17 Jul Open | 7528.90 | 7443.70 | +85.20 | FAIL — matches the full-day open (7531.2) |
| §6 17 Jul High | 7534.10 | 7497.30 | +36.80 | FAIL — matches the full-day high (7533.1) |
| §6 17 Jul Low | 7451.20 | 7431.60 | +19.60 | FAIL |
| §6 17 Jul Close | 7457.69 | 7456.60 | +1.09 | OK |
| §6 17 Jul RSI2 | 0.0 | 0.00 | 0.00 | OK — reproduces exactly from the report's own closes |
| §6 20 Jul Open | 7489.18 | 7495.30 | −6.12 | OK |
| §6 20 Jul High | 7501.60 | 7512.80 | −11.20 | FAIL |
| §6 20 Jul Low | 7431.90 | 7439.30 | −7.40 | OK |
| §6 20 Jul Close | 7443.28 | 7446.60 | −3.32 | FAIL (marginal, tolerance 3.00) |
| §6 20 Jul RSI2 | 0.0 | 0.00 | 0.00 | OK — reproduces exactly from the report's own closes |
| §6 21 Jul Open | 7451.30 | 7487.70 | −36.40 | FAIL — matches the full-day open (7447.5) |
| §6 21 Jul High | 7519.40 | 7515.70 | +3.70 | OK |
| §6 21 Jul Low | 7448.70 | 7466.50 | −17.80 | FAIL |
| §6 21 Jul Close (D-1) | 7506.47 | 7508.00 | −1.53 | OK — and identical in §1, §3, §4, §18 |
| §6 21 Jul RSI2 | 81.4 | 85.99 | −4.59 | OK — basis difference only; recomputation from the report's own closes returns 81.4 exactly |
| §11 Daily P | 7458.93 | 7496.73 | −37.80 | FAIL — built from 20 Jul (D-2); reproduces exactly from 20 Jul H/L/C and satisfies R2−P = P−S2 = 69.70 |
| §11 Daily R1 | 7485.95 | 7526.97 | −41.02 | FAIL — wrong base session |
| §11 Daily R2 | 7528.63 | 7545.93 | −17.30 | FAIL — wrong base session |
| §11 Daily R3 | 7555.65 | 7576.17 | −20.52 | FAIL — wrong base session |
| §11 Daily S1 | 7416.25 | 7477.77 | −61.52 | FAIL — wrong base session |
| §11 Daily S2 | 7389.23 | 7447.53 | −58.30 | FAIL — wrong base session |
| §11 Daily S3 | 7346.55 | 7428.57 | −82.02 | FAIL — wrong base session |
| §11 Weekly P (W/E 17 Jul) | 7497.93 | 7490.33 | +7.60 | OK — reproduces exactly from H 7584.90 / L 7451.20 / C 7457.69; identity R2−P = P−S2 = 133.70 holds |
| §11 Weekly R1 | 7544.66 | 7549.07 | −4.41 | OK |
| §11 Weekly R2 | 7631.63 | 7641.53 | −9.90 | Note — inherited from the +19.60 error in the weekly low input |
| §11 Weekly S1 | 7410.96 | 7397.87 | +13.09 | FAIL — inherited from the weekly low input |
| §11 Weekly S2 | 7364.23 | 7339.13 | +25.10 | FAIL — inherited from the weekly low input |
| §11 Weekly S3 | 7277.26 | 7246.67 | +30.59 | FAIL — inherited from the weekly low input |
| §11 Monthly (June) | P 7428.17 | not in slice | n/a | Unverifiable against the slice; internally consistent — implies H 7497.21 / L 7300.91 / C 7486.39, and identity R2−P = P−S2 = 196.30 holds |
| §21b 25-session range low | 7300.90 | 7303.10 | −2.20 | OK |
| §21b 25-session range high | 7584.90 | 7582.80 | +2.10 | OK |
| §21b range width | 284.00 | 279.70 | +4.30 | OK — all four 3B zone boundaries and both stops recompute exactly from the report's own low/width |
| §9 / §21 ATR(14) | not stated | 69.44 (cash) / 78.02 (full day) | n/a | FAIL — required by 3.3; every stop and the Trade 1 runner cap depend on it |
| §8 "nearest support 7,432 (21 Jul / 20 Jul low cluster)" | 7432 | 20 Jul low 7439.30; 21 Jul low 7466.50 | −7.30 / −34.50 | Note — the 20 Jul leg is inside tolerance, the 21 Jul leg is not; it is not a two-session cluster |
| §21b confluence "weekly S3 7,364" | 7364 | §11 weekly S3 = 7277.26 | +86.74 | FAIL — 7,364.23 is weekly **S2**, mis-labelled on the card |
| §21b confluence "short zone overlaps the 15 Jul swing high (7,585)" | zone top 7552.50 | 5-day swing high 7582.80 | −30.30 | FAIL — the zone does not reach the swing high |
| §21a vs §20 cross-asset contribution | −0.08 (§21a) | −0.075 (§20) | −0.005 | Note — rounding inconsistency between the two statements of the same term |
| §21c "days to resolution" for the t−3 entry | 5+ | at most 3 sessions exist (17, 20, 21 Jul) | +2 | FAIL — impossible inside the stated window |
