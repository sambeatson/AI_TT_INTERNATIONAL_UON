# Trust Score — 2026-07-28 — SP500_Daily_Report_28-Jul-2026.md

Reviewer run: `regen_20260906_qa1`. Asset US500. Report date D = 2026-07-28 (Tuesday); required
as-of session D-1 = **Monday 2026-07-27**. Evidence base: `data/slices/US500/US500_upto_2026-07-27.csv`
via `engine/qa_slice_stats.py` (cash session 16:30–23:00 broker = 09:30–16:00 ET), the VIX/USDX/NEWS
slices to the same date, `cards/baseline/by_date/2026-07-28.json`, and the leak-free linter rows in
`qa/regen_20260906_qa1/lint_static/2026-07-28.csv`.

**Headline finding.** The report's declared as-of session is **Friday 24 July 2026**, not D-1
(Mon 27 Jul). A complete 27 Jul cash session exists in the slice (O 7473.8 · H 7480.3 · L 7382.9 ·
C 7415.5, RSI2 100.00) and is absent from every section of the report. The prior report
(`SP500_Report_27Jul2026.md`) already carried "As-of session: 24 July 2026 close", so this report
repeats an as-of that was correct one session earlier. Everything downstream — §6 window, §11 daily
pivots, §21 card levels, §21c backtest indexing — is anchored one session behind.

---

## 1. Section 7 checklist

| Item | Reviewer notes | Evidence observed | Score 0–5 | Action required |
|---|---|---|---|---|
| 1.1 Variables respected | Asset is the S&P 500 cash index (503 constituents, 09:30–16:00 ET), not ES futures — correct. Counters named as USDX · VIX · DAX 40 with USDX first — correct. USD / index points / tick 0.01 — correct. Lookback 5 sessions (plus 25-session regime block) — correct. §4 carries six observation rows — count met. **Two variables breached:** (a) as-of is the NY close of 24 Jul, not of D-1 27 Jul; (b) the 07:00 UK daily-open anchor for Trade 1 is declared "overridden" with no replacement clock and the Trade 1 card is a resting buy limit at a price level, not an entry at the anchor. | §1 header ("Basis date … Friday 24 July 2026 close"); §2 As-of date row; §4 six rows; §20 "Daily-open-anchor override"; §21b Trade 1 Entry row | 2 | Re-anchor the whole report to the 27 Jul NY close; state the daily-open anchor explicitly as 07:00 UK on the Trade 1 card and enter at that anchor. |
| 1.2 Coverage & currency consistent | No currency or unit drift anywhere — all levels in index points, USD, 0.01 tick. All stated dates are ≤ D-1, so nothing leaks forward. But the 5-session window is 20–24 Jul when a D-1 anchor requires 21–27 Jul; §13c "Previous Period" is captioned 20–24 Jul and omits Mon 27 Jul entirely; §21c labels **Thu 23 Jul as t−1** while the report claims a Fri 24 Jul as-of, so the backtest is off by one even against the report's own (already stale) anchor. | §6 table; §13c caption; §21c rows "Thu 23 Jul (t−1)" … "Fri 17 Jul (t−5)" | 2 | Shift §6 to 21–27 Jul, §13c to 21–27 Jul, and re-index §21c so t−1 = the as-of session. |
| 1.3 Audience & tone | Byline "Senior US Equity Strategist"; register is institutional throughout; §18 is a proper three-reason analyst judgement with a single watch item; no retail framing, no promotional language, no "you should". | §1 header; §18 | 5 | None. |
| 2.1 Sections present & ordered | All 21 sections present in order, with §13 fully decomposed (13a per-article table, 13b aggregate with a numeric tilt of −0.15, 13c previous-period calendar, 13d upcoming calendar) and §21 fully decomposed (21a conviction, 21b cards, 21c 5-session backtest, 21d what-is-working plus the limitations boilerplate). §17 is exactly one sentence. | Headings throughout; §13a–d; §21a–d; §17 | 5 | None. |
| 2.2 Scorecard as a table | §6 is a table but carries only Date/Open/High/Low/Close/RSI2/Trend/Validation — the **Source A, Source B and Final columns are absent**, so per-row corroboration is asserted in prose ("Close corrob.") rather than shown. §11 gives three pivot tables but each runs **five levels per side (R5→R1, S1→S5)** in a two-column layout with P stranded at the foot of the left column, instead of the required three levels per side ordered R3→P→S3. | §6 header row; §11 daily / weekly / monthly tables | 3 | Add Source A / Source B / Final columns to §6; re-cut §11 to R3→P→S3, three levels each side, P in sequence. |
| 2.3 Method steps visible | §4 lists observations with class and note, §5 explains normalization, weighting method (weighted median) and why the final number is defensible — the observation → classification → consensus chain is visible. §8 is candle-by-candle for all five sessions and ends in a sequence assessment with overlap 0.43 / persistence 0.22. §9 states the regime with overlap, persistence, median RSI2, range position and VOLator slope. §7 carries five captioned chart placeholders (pandoc has dropped the images; captions accepted as evidence and noted here). | §4–§5; §8 bullets + "Sequence assessment"; §9 bullets; §7 captions | 4 | Nothing structural; charts unverifiable in the markdown render. |
| 3.1 Quantitative claims sourced | §1 numbers all resolve to §6/§4. §12 and §14, however, carry a run of unsourced quantitative claims that appear nowhere in §4 or §13a: Brent "above $100", WTI "near $85", "10-year yield at a two-month high", "USDJPY above 163", "VVIX ~96–103", "SKEW ~146–152", "equal-weight S&P lagged all week". Core PCE 3.4% y/y is the one §14 figure that checks out against the calendar feed. | §12 bullets 3, 5, 6; §14 bullets 2, 4, 5; NEWS slice row 3306 (Core PCE y/y 3.4) | 2 | Attribute every §12/§14 figure to a §4/§13a row or a named dated source, or delete it. |
| 3.2 Citations exist & contain data | Three spot-checks, all internally consistent: (a) **S&P DJI via FRED**, 24 Jul, 7,411.98 "official index close" — reused unchanged in §1, §3, §6, §18, and §20 logs the corroborating pair (S&P DJI × CNBC, delta 0.00); (b) **Capis / Vantage**, 23 Jul, 7,408.30 "−1.21%" — 7,408.30 from 7,498.96 is −1.209%, and the §13a Capis quote "second loss for the month of more than −1%" agrees; (c) **Saxo desk**, 21 Jul, 7,509.20 "+0.89%" — 7,509.20 from 7,443.28 is +0.886%. No fabricated, impossible or self-contradictory citation found, so no hallucinated-source override. Deducted because two §4 rows pair two houses in one cell ("Capis / Vantage"), so "six independent observations" is really five rows, and §13a quotes are paraphrases rather than verbatim extracts. | §4 rows 1, 5, 6; §13a Capis/Saxo rows; §20 "Validation method" | 4 | Split paired sources into separate rows so the count of six is literal. |
| 3.3 Calculations transparent | RSI2 rows 3–5 reproduce **exactly** from the report's own close column (86.6 / 0.0 / 3.9 recomputed = 86.6 / 0.0 / 3.9). Rows 1–2 do not: back-solving 39.7 on 21 Jul from the +65.92 gain forces a 20 Jul loss of 100.13, i.e. an implied 17 Jul close of **7,543.41**, which contradicts the report's own "−0.19%" for 20 Jul (that implies 7,457.45) and the slice (7,447.10). Trend labels follow the stated rule on all five rows. Daily pivots reproduce exactly from the report's own 24 Jul H/L/C and satisfy R2−P = P−S2 = 48.00; weekly (58.96) and monthly (283.74) identities also hold. ATR(14) = 77.65 and KER(13/3, thr 0.13/0.09) are stated. **§21a is not reproducible:** the rule is score = Σ signal×weight with signals in {−1, 0, +1}, so with weights 0.25/0.15/0.15 the stated contributions −0.09, −0.02 and +0.02 are arithmetically impossible, and the three listed contributions sum to −0.09 against a headline score of −0.10. | §6 RSI2 column; §8 "−0.19%"; §11 all three tables; §20 "Indicator basis"; §21a | 2 | Rebuild the RSI2 chain from the true 21–27 Jul closes and publish the seed close; show the six signal/weight pairs so the direction score sums. |
| 3.4 Numbers reconcile | 7,411.98 is identical in §1, §3, §4, §6 and §18 — but **no card entry equals the close** (Trade 1 is a limit at 7,392), and the close itself is the wrong session's. §11 pivots are quoted consistently on the cards. Cross-section contradictions found: §1 "price sits just below the daily pivot" vs §11 "sits fractionally above the daily pivot (7,410.66)"; §9 "VIX **fell** across the week" against its own quoted 17.05 → 18.58 (a rise) and against the slice (17.43 → 18.36, up 0.93); §21d "Trade 3B … mean R ≈ +0.80 on closed" against its own §21c closed rows (+0.4, +1.5 → +0.95); §21b Trade 2 "7,387 = daily S1 + weekly S4" against §11 weekly S4 = 7,393.62; §8 "two-way 140-point swing" matches neither the close range (100.90) nor the H/L range (187.00). | §1 vs §11; §9 vs §10/§14 and VIX slice; §21c vs §21d; §21b Trade 2 Confluences vs §11; §8 | 1 | Fix the pivot-side statement in §1, the VIX direction in §9/§10/§14/§15, the §21d 3B mean, the weekly S4 label and the 140-point figure. |
| 4.1 Pillars conclude | Every pillar ends in an explicit label: §8 "Judgement label: Indecision"; §9 "Consolidated regime label: RANGE"; §10 "Aggregate cross-asset: MIXED"; §12 tags each driver price-supportive / price-negative / watch item; §14 bullets are each directionally labelled. Deducted because §10's VIX row is labelled "Falling → Confirms" on a counter that rose over the window, so the MIXED aggregate rests on an inverted input. | §8 label line; §9 last bullet; §10 aggregate paragraph; §12; §14 | 3 | Re-label the VIX row and re-run the aggregation. |
| 4.2 Peer/cross-asset interpreted | §10 supplies a genuine transmission mechanism per counter rather than a correlation list: dollar → multinational translation drag; implied vol → removal of the risk-off impulse; DAX → common global risk factor. The aggregation rule (any confirm + contradict co-occurrence → MIXED) is stated and applied. Deducted because the mechanism is applied to a wrong-signed VIX input, and the USDX detail is wrong twice (the stated "~100.6–101.0" band understates the actual 100.96–101.47, and 22 Jul was a down session so "fifth straight up session" fails). | §10 table and aggregate; §14 "Liquidity & FX"; USDX slice 20–27 Jul | 3 | Correct the VIX sign and the USDX streak/band before re-deriving the aggregate. |
| 4.3 Synthesis reconciles tensions | §15 is genuinely two-sided and event-gated, §16 explicitly states it "respects — does not contradict" the §9 Ranging classification, §18 names three reasons plus one watch item, and §21a runs an explicit score-vs-§17 conflict check. Heavily deducted for card construction, which is scored here: **Trade 1 must be a SUPPRESSED row** (score −0.10, |0.10| < 0.25 conviction threshold) and is instead published as an active card; **Trade 2 must be suppressed entirely** because §19 declares every accessible daily and weekly pivot tier SINGLE-SOURCE-INDICATIVE; Trade 1 uses a resting buy limit instead of an entry at the daily-open anchor; **Trade 3B is built with 3A machinery** (buy stop on a pivot reclaim plus a 38.2% Fibonacci target) rather than the 25-day-range limits the range fork requires; Trades 1 and 2 set thesis invalidation **equal to the stop** (7,357 and 7,362) when the rule requires it to be separate; Trade 2's stop sits on daily S2 with no 0.25×ATR buffer. Additionally all three cards are LONG while the direction score is negative, and that tension is never addressed. | §15–§16; §18; §21a conflict paragraph; §21b all three cards; §19 corroboration paragraph | 2 | Suppress Trades 1 and 2 as SUPPRESSED rows, rebuild 3B on range mechanics, separate invalidations from stops. |
| 4.4 Calibrated language | §17 is exactly one sentence with a single directional claim, a named range and a named trigger — no hedge stacking. §3 states Confidence "High" with a rationale. §21a states "NEUTRAL (low conviction)" and does not overclaim. §21d closes with the required limitations boilerplate on sample size, fills, slippage and commission. | §17; §3 Confidence column; §21a; §21d limitations italic | 5 | None. |
| 5.1 Data dated; staleness flagged | Every price row and every article in §13a carries a date, and the single-source status of all intraday O/H/L is flagged in the header note, in the §6 validation column, in the §6 footnote and again in §19 — the flagging discipline itself is good. The failure is that the report is **a full session stale** and does not say so: it presents 24 Jul as "the last corroborated session" for a 28 Jul report without acknowledging that a 27 Jul session exists (slice: O 7473.8 H 7480.3 L 7382.9 C 7415.5). The staleness is explained (egress block) but never identified as staleness. | §1 data note; §2 As-of date; §6 footnote; §19; slice bar 2026-07-27 | 2 | State the gap explicitly: name 27 Jul as the missing session and either source it or flag the report as one session behind. |
| 5.2 Assumptions up front | Single-source pivot propagation is stated in §19 and carried into the Caveats line of all three cards — that chain is intact. The anchor-override caveat, however, appears **only in §20** and not on the Trade 1 card, which says merely "pre-NY-open working order" and never names a clock; the baseline card object records anchor_broker 09:00 (= 07:00 UK), so the card text is less explicit than the object behind it. | §19 final italic; §21b Caveats rows; §20 "Daily-open-anchor override"; `cards/baseline/by_date/2026-07-28.json` | 3 | Put the anchor-override caveat and the explicit anchor time on the Trade 1 card. |
| 5.3 Red flags surfaced | §12 surfaces six labelled risk drivers, §15 is a balanced upside/downside table naming the FOMC and Core PCE as the break risks, and the 29 Jul FOMC collision is carried into the Caveats line of **all three** cards, which is what the protocol asks for. §13d flags the event cluster. Gap: §13c omits Mon 27 Jul, and with it a HIGH-impact US Durable Goods Orders print (actual 0.300 vs consensus 1.700) that sat in the calendar feed on D-1. | §12; §15; §21b Caveats × 3; §13d; NEWS slice row 4346 | 4 | Extend §13c through D-1 and carry the 27 Jul durable-goods miss into the drivers. |
| 5.4 Restrictions honoured | **BREACHED.** §20 writes "**M5 trace:**" and "The **M1** daily-open anchor value was overridden", naming internal modules in the report body — the presentation rules forbid referencing M1–M5 anywhere in the report, Agent Log included. §20 also prints the raw direction-score weights ("0.25 / 0.20 / 0.10 / 0.15 / 0.15 / 0.15") and §21a repeats one of them ("−0.15 tilt × 0.15 weight"), where only the qualitative "defaults" label may appear. Separately, the two suppression rules (Trade 1 on sub-threshold conviction, Trade 2 on all-indicative pivot tiers) are openly overridden. Clean on the other restrictions: no retail CFD quotes in the OHLC basis, no ES futures in the cash basis, no bracketed variable names, no framework name, instrument common names used throughout. | §20 lines "M5 trace" and "The M1 daily-open anchor value"; §20 weights list; §21a weight arithmetic; §19/§20 suppression override | 0 | Strip all module codes and numeric weights from the report body; restore the suppression rules. |

---

## 2. Category roll-up

| Category | Level | Multiplier | Points | Justification |
|---|---|---|---|---|
| C1 · Prompt adherence and instruction compliance (max 20) | **2** | 0.40 | **8.0** | Rows 1.1/1.2/1.3 = 2/2/5, mean 3.00 → level 3; the restriction-breach override then reduces C1 by one level to **2**. Asset, counters, units, tick, lookback and source count are respected, but the as-of session and the Trade 1 daily-open anchor — the two variables that drive every level in the report — are not. |
| C2 · Structural and modular framework alignment (max 20) | **4** | 0.85 | **17.0** | Rows 2.1/2.2/2.3 = 5/3/4, mean 4.00. All 21 sections present, correctly ordered and fully decomposed at §13 and §21; §17 is one sentence. The gaps are presentational: §6 lacks Source A/B/Final columns and §11 uses five pivot levels per side instead of R3→P→S3. |
| C3 · Accuracy, evidence and factual reliability (max 25) | **2** | 0.40 | **10.0** | Rows 3.1/3.2/3.3/3.4 = 2/4/2/1, mean 2.25 → level 2. Closes are accurate to ≤2.8 pts and the citations spot-check clean, but 11 of 15 stated O/H/L values sit outside the ±8 pt basis tolerance, two RSI2 cells imply a 17 Jul close 96 pts away from the feed, the daily and weekly pivots are drawn from the wrong sessions, the direction score does not sum, and five cross-section contradictions survive into the final text. |
| C4 · Reasoning, judgment and evaluation quality (max 20) | **3** | 0.65 | **13.0** | Rows 4.1/4.2/4.3/4.4 = 3/3/2/5, mean 3.25 → level 3. Every pillar concludes, §10 gives real mechanisms, §17 is well calibrated and the §15/§16/§18 synthesis is coherent — but the reasoning is applied to an inverted VIX read, and all three trade cards violate construction rules (two should be SUPPRESSED rows, one is built on the wrong fork's machinery). |
| C5 · Currency, restrictions and transparency (max 15) | **2** | 0.40 | **6.0** | Rows 5.1/5.2/5.3/5.4 = 2/3/4/0, mean 2.25 → level 2. Dating and single-source flagging are genuinely strong and event collisions reach every card, but the report is a full session stale without saying so, the anchor caveat never reaches the card, and §20/§21a expose module codes and raw weights that the presentation rules prohibit. |
| **Total** | — | — | **54.0 → 54** | Σ(multiplier × max) = 8.0 + 17.0 + 10.0 + 13.0 + 6.0 = 54.0, rounded to **54**. |

---

## 3. Total, band, override check

- **Raw total: 54** (8.0 + 17.0 + 10.0 + 13.0 + 6.0 = 54.0).
- **Hallucinated-source override: NOT triggered.** Three cited sources were spot-checked (S&P DJI via
  FRED · 24 Jul · 7,411.98; Capis / Vantage · 23 Jul · 7,408.30 / −1.21%; Saxo desk · 21 Jul · 7,509.20 /
  +0.89%). Each is named and dated, each quoted percentage reconciles with the report's own close series
  to within rounding (−1.209% and +0.886% respectively), and each figure is used consistently elsewhere
  in the report. No source is self-contradictory or impossible. C3 is therefore **not** forced to 0.
- **Restriction-breach override: TRIGGERED.** Two prompt-stated presentation restrictions are openly
  violated in §20 and §21a — internal module codes appear in the report body ("**M5 trace:**"; "The
  **M1** daily-open anchor value was overridden") and the raw direction-score weights are printed
  ("0.25 / 0.20 / 0.10 / 0.15 / 0.15 / 0.15", and "−0.15 tilt × 0.15 weight" in §21a) where only the
  qualitative "defaults" label is permitted. The two strategy-suppression rules are also overridden in
  the open. Consequences applied: the total is capped at the Moderate band (60–74) — **not binding
  here, since 54 already sits below the cap** — and C1 is reduced by one rubric level, from 3 to 2,
  which is reflected in the roll-up above and lowers the total from 62 to 54.
- **Final Trust Score: 54 · Band: Low Trust (40–59) · Override: restriction_breach.**
- **Required action for this band:** not suitable for use; salvageable for skeleton or framing only.
  Full prompt review and regeneration, with the as-of anchor and the presentation-rule filter checked
  before the run is accepted.

---

## 4. Card Integrity

Linter rows copied verbatim from `qa/regen_20260906_qa1/lint_static/2026-07-28.csv`:

| card_id | report_date | strategy | flags | dud |
|---|---|---|---|---|
| 2026-07-28_Trade_1 | 2026-07-28 | Trade 1 - Daily Directional | CLEAN | False |
| 2026-07-28_Trade_2 | 2026-07-28 | Trade 2 - Pivot (buy limit daily S1) | WARN_R_TINY(0.30xATR) | False |
| 2026-07-28_Trade_3 | 2026-07-28 | Trade 3 - Mean-Reversion (buy stop on P reclaim) | CLEAN | False |

Per-card integrity, 100 − 40·(#DUD) − 10·(#WARN), floored at 0:

| Card | #DUD | #WARN | Integrity |
|---|---|---|---|
| 2026-07-28_Trade_1 | 0 | 0 | 100 |
| 2026-07-28_Trade_2 | 0 | 1 | 90 |
| 2026-07-28_Trade_3 | 0 | 0 | 100 |
| **Report mean (3 non-suppressed cards)** | **0** | **1** | **96.7** |

Counts: n_cards = 3 · n_duds = 0 · n_warns = 1.

**Construction assessment (feeds row 4.3, not the integrity number).** The linter checks static
geometry only, and on that basis all three cards pass: stops are on the correct side, TP1 is beyond
entry, TP2 beyond TP1, TP3 beyond TP2, every R sits inside 0.3–3.0 × ATR14 (35 pts = 0.47×, 25 pts =
0.34×, 42 pts = 0.57× against the slice cash ATR14 of 73.73), every TP1 is within 2.5 × ATR14 of its
entry, and each entry sits on the correct side of the D-1 close (7,415.5 cash): buy limits at 7,392
and 7,387 below it, buy stop at 7,420 above it. The rule violations the linter cannot see are set out
in §21b of the checklist above and itemised in the feedback file — chiefly that Trade 1 and Trade 2
should both be SUPPRESSED rows, that Trade 1 is a resting limit rather than an entry at the
daily-open anchor, that Trade 3B uses trend-fork (3A) machinery instead of 25-day-range mechanics,
and that Trades 1 and 2 set thesis invalidation equal to the stop.

---

## 5. Data reconciliation log

Slice reference: `data/slices/US500/US500_upto_2026-07-27.csv`, cash session 16:30–23:00 broker, as
printed by `engine/qa_slice_stats.py` (the 20 Jul row is computed on the same cash window; the helper
prints only the last five sessions, which begin at 21 Jul). Tolerance per the brief: |Δ| ≤ 3.0 pts on
a close, ≤ 8.0 pts on an open/high/low.

### 5.1 §6 OHLC, row by row

| Section | Field | Report value | Slice value | Delta | Verdict |
|---|---|---|---|---|---|
| §6 Mon 20 Jul | Open | 7,549.00 | 7,495.30 | +53.70 | **DISCREPANCY** (6.7× tolerance) |
| §6 Mon 20 Jul | High | 7,557.00 | 7,512.80 | +44.20 | **DISCREPANCY** |
| §6 Mon 20 Jul | Low | 7,434.00 | 7,439.30 | −5.30 | Consistent |
| §6 Mon 20 Jul | Close | 7,443.28 | 7,442.80 | +0.48 | Consistent |
| §6 Tue 21 Jul | Open | 7,455.00 | 7,487.70 | −32.70 | **DISCREPANCY** |
| §6 Tue 21 Jul | High | 7,515.00 | 7,515.70 | −0.70 | Consistent |
| §6 Tue 21 Jul | Low | 7,451.00 | 7,466.50 | −15.50 | **DISCREPANCY** |
| §6 Tue 21 Jul | Close | 7,509.20 | 7,508.00 | +1.20 | Consistent |
| §6 Wed 22 Jul | Open | 7,512.00 | 7,490.30 | +21.70 | **DISCREPANCY** |
| §6 Wed 22 Jul | High | 7,540.00 | 7,525.50 | +14.50 | **DISCREPANCY** |
| §6 Wed 22 Jul | Low | 7,470.00 | 7,488.00 | −18.00 | **DISCREPANCY** |
| §6 Wed 22 Jul | Close | 7,498.96 | 7,498.80 | +0.16 | Consistent |
| §6 Thu 23 Jul | Open | 7,490.00 | 7,416.70 | +73.30 | **DISCREPANCY** (largest single error) |
| §6 Thu 23 Jul | High | 7,500.00 | 7,449.80 | +50.20 | **DISCREPANCY** |
| §6 Thu 23 Jul | Low | 7,370.00 | 7,375.30 | −5.30 | Consistent |
| §6 Thu 23 Jul | Close | 7,408.30 | 7,405.50 | +2.80 | Consistent (at the edge) |
| §6 Fri 24 Jul | Open | 7,409.00 | 7,407.60 | +1.40 | Consistent |
| §6 Fri 24 Jul | High | 7,434.00 | 7,460.20 | −26.20 | **DISCREPANCY** |
| §6 Fri 24 Jul | Low | 7,386.00 | 7,395.60 | −9.60 | **DISCREPANCY** |
| §6 Fri 24 Jul | Close | 7,411.98 | 7,411.80 | +0.18 | Consistent |
| §6 Mon 27 Jul (D-1) | O/H/L/C | **absent** | 7,473.8 / 7,480.3 / 7,382.9 / 7,415.5 | whole session | **FAILURE** — the required D-1 session is missing from the table |

Summary: **5 of 5 closes pass** (max |Δ| 2.80). **11 of 15 O/H/L values fail** the ±8 pt tolerance,
consistent with the report's own admission that the intraday values are single-source indicative —
but the magnitudes (up to 73.3 pts) exceed anything a CFD-vs-cash basis explains.

### 5.2 §6 RSI2

| Section | Field | Report value | Slice / recomputed value | Delta | Verdict |
|---|---|---|---|---|---|
| §6 Mon 20 Jul | RSI2 | 22.0 | not evaluable from the report's own closes (no prior close published); slice window starts 21 Jul | — | **Unverifiable / inconsistent** — see back-solve below |
| §6 Tue 21 Jul | RSI2 | 39.7 | 85.99 (helper, slice closes) | −46.29 | **DISCREPANCY** |
| §6 Wed 22 Jul | RSI2 | 86.6 | 86.97 (slice) / **86.6** (recomputed from the report's own closes) | −0.37 / **0.00** | Consistent; arithmetic exact |
| §6 Thu 23 Jul | RSI2 | 0.0 | 0.00 (slice) / **0.0** (report's own closes) | 0.00 / **0.00** | Consistent; arithmetic exact |
| §6 Fri 24 Jul | RSI2 | 3.9 | 6.33 (slice) / **3.9** (report's own closes) | −2.43 / **0.00** | Consistent; arithmetic exact |
| §6 Mon 27 Jul (D-1) | RSI2 | **absent** | 100.00 | — | **FAILURE** — the report's headline "RSI2 finished at 3.9 (deeply oversold)" is a stale session; on D-1 the same indicator reads 100.00 |
| §6 rows 1–2 | implied 17 Jul close | 7,543.41 (back-solved from RSI2 39.7 and the +65.92 gain on 21 Jul) | 7,447.10 | +96.31 | **DISCREPANCY** — and it also contradicts the report's own §8 "−0.19%" for 20 Jul, which implies 7,457.45 (Δ +85.96) |

Verdict on the arithmetic: RSI2 = 100 − 100/(1+RS) with RS = mean gain / mean loss over 2 periods is
applied **correctly** on every row that can be checked against the published close column. The failure
is in the inputs, not the formula — the first two rows require a prior close the report never states
and that no real session supports.

### 5.3 §11 pivots

Floor-pivot identity R2 − P = P − S2 holds on all three tables: daily 48.00 = 48.00, weekly
58.96 = 58.96, monthly 283.74 = 283.74. All seven daily levels reproduce exactly from the report's own
24 Jul H/L/C (7,434.00 / 7,386.00 / 7,411.98 → P = 7,410.66; R1 = 2P − L = 7,435.32; S1 = 2P − H =
7,387.32; R2 = P + (H−L) = 7,458.66; S2 = 7,362.66; R3 = H + 2(P−L) = 7,483.32; S3 = L − 2(H−P) =
7,339.32). The arithmetic is sound; the **session** is wrong.

| Section | Field | Report value | Slice value (D-1 = 27 Jul cash) | Delta | Verdict |
|---|---|---|---|---|---|
| §11 daily | P | 7,410.66 | 7,426.23 | −15.57 | **DISCREPANCY** — built from 24 Jul, not D-1 |
| §11 daily | R1 | 7,435.32 | 7,469.57 | −34.25 | **DISCREPANCY** |
| §11 daily | S1 | 7,387.32 | 7,372.17 | +15.15 | **DISCREPANCY** |
| §11 daily | R2 | 7,458.66 | 7,523.63 | −64.97 | **DISCREPANCY** |
| §11 daily | S2 | 7,362.66 | 7,328.83 | +33.83 | **DISCREPANCY** |
| §11 daily | R3 | 7,483.32 | 7,566.97 | −83.65 | **DISCREPANCY** |
| §11 daily | S3 | 7,339.32 | 7,274.77 | +64.55 | **DISCREPANCY** |
| §11 daily | R4 / R5 / S4 / S5 | 7,531.32 / 7,579.32 / 7,291.32 / 7,243.32 | n/a (floor set is R3→S3) | — | Out-of-spec extra tiers; internally consistent (±48.00 spacing) |
| §11 weekly | Prior week used | 13–17 Jul | 20–24 Jul (the week before D) | one week | **FAILURE** — wrong prior week |
| §11 weekly | P | 7,538.46 | 7,437.53 | +100.93 | **DISCREPANCY** |
| §11 weekly | implied High | 7,565.38 (back-solved) | 7,582.80 (13–17 Jul, the week it names) | −17.42 | **DISCREPANCY** |
| §11 weekly | implied Low | 7,506.42 (back-solved) | 7,431.60 (13–17 Jul) | +74.82 | **DISCREPANCY** |
| §11 weekly | implied Close | 7,543.58 (back-solved) | 7,447.10 (17 Jul) | +96.48 | **DISCREPANCY** — the weekly block matches no real week |
| §11 monthly | P | 7,457.15 | 7,452.97 (June cash) | +4.18 | Consistent |
| §11 monthly | implied High | 7,577.91 (back-solved) | 7,624.60 | −46.69 | **DISCREPANCY** |
| §11 monthly | implied Low | 7,294.17 (back-solved) | 7,243.10 | +51.07 | **DISCREPANCY** |
| §11 monthly | implied Close | 7,499.37 (back-solved) | 7,491.20 | +8.17 | Marginal |

Consequence: because the weekly block is taken from two weeks back, every weekly support level sits
**above** spot (weekly S1 = 7,511.54 vs a 7,411.98 close), which is why §21b Trade 2 ends up naming a
weekly *support* level as an upside runner target.

### 5.4 Other stated quantities

| Section | Field | Report value | Slice value | Delta | Verdict |
|---|---|---|---|---|---|
| §20 / §21b | ATR(14) | 77.65 | 73.73 (cash) · 83.47 (full broker day) | +3.92 / −5.82 | Consistent — sits between the two bases |
| §9 | VIX 21 Jul | 17.05 | 17.43 | −0.38 | Consistent |
| §9 | VIX 24 Jul | 18.58 | 18.36 | +0.22 | Consistent |
| §9 / §10 / §14 | VIX direction | "fell across the week" / "Falling" | rose: 17.43 → 18.36 close-to-close (D-1 27 Jul: 18.27) | sign inverted | **FAILURE** — the label contradicts both the slice and the report's own two figures |
| §10 / §14 | USDX level band | "~100.6–101.0" | 100.958 → 101.472 over 20–24 Jul (D-1: 101.503) | upper bound −0.47 | **DISCREPANCY** |
| §10 / §14 | USDX "fifth straight up session" | 5 consecutive up sessions | 22 Jul closed 101.097 vs 101.180 on 21 Jul — a down session | streak broken | **DISCREPANCY** |
| §10 | USDX direction | "Rising (mild)" | rising 20 → 27 Jul | — | Consistent |
| §14 | Core PCE y/y | 3.4% | 3.4 (calendar feed, released 25 Jun) | 0.00 | Consistent |
| §13c | Previous-period coverage | 20–24 Jul | should run to D-1 = 27 Jul; 27 Jul carried a HIGH-impact US Durable Goods Orders print (0.300 actual vs 1.700 consensus) | one session | **FAILURE** — D-1 session and its Tier-1 print omitted |
| §21a | Direction score | −0.10 | listed contributions −0.09 + (−0.02) + 0.02 = −0.09 | −0.01 | **DISCREPANCY** — and contributions of −0.09 / ±0.02 are impossible under score = Σ signal×weight with signals in {−1, 0, +1} |
| §21d | Trade 3B mean R (closed) | +0.80 | +0.95 from its own §21c rows (+0.4, +1.5) | −0.15 | **DISCREPANCY** |
| §1 vs §11 | Close vs daily pivot | §1 "just below the daily pivot" | §11 "fractionally above the daily pivot (7,410.66)"; 7,411.98 > 7,410.66 | contradiction | **FAILURE** — §1 is wrong |
| §8 | "two-way 140-point swing" | 140 pts | 100.90 pts on closes (7,509.20 → 7,408.30) or 187.00 pts on the stated H/L (7,557 → 7,370) | −46.10 / +47.00 | **DISCREPANCY** — matches neither basis |
| §21b Trade 2 | "7,387 = daily S1 + weekly S4" | weekly S4 = 7,387 | §11 weekly S4 = 7,393.62 | −6.62 | **DISCREPANCY** — label conflates two levels the report itself distinguishes in §11 |
| Header / §2 | As-of session | Fri 24 Jul 2026 close | D-1 = Mon 27 Jul 2026 (full cash session present in the slice) | one session | **FAILURE** — the governing defect; identical to the as-of used by the 27 Jul report |
