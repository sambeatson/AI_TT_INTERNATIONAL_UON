# Trust Score — Gold_Report_02-Jun-2026.md (D = 2026-06-02)

Run: `gold_regen_qa1` · Asset: XAUUSD · Reviewer basis: level file `data/levels/XAUUSD_by_date/2026-06-02.csv`
(`last_bar_date` = 2026-06-01, strictly < D — verified leak-free). Report claims continuous loco-London
spot ("Global 24-hour spot market", "OTC London spot, T+2") → checked against the **`_full`** columns;
`_cash` shown too where it changes the verdict.

## 1. Section 7 checklist

| Item | Notes | Evidence | Score |
|---|---|---|---|
| 1.1 All variables respected | XAU/USD spot, loco-London stated (not COMEX); USDX is first counter in §10; USD/oz throughout; 6 sources in §4 (meets "≥6" exactly); tick (0.01) stated and used consistently in every card's R-in-ticks conversion. Minor: §2 "As-of date" is labelled "2 June 2026" (= D) though all data actually used is D−1 or earlier — a labelling ambiguity, not a real leak. | §2, §4, §21b | 4 |
| 1.2 Coverage & currency consistent | No USD/oz vs tick/point drift found; the one soft spot is the §2 as-of-date label above. | whole report | 4 |
| 1.3 Audience & tone | Institutional register throughout ("Senior Commodities Analyst — Precious Metals"), no retail tone. | §1, §18 | 5 |
| 2.1 Sections present & ordered | All of §1–§21 present, correctly ordered, including 13a–d and 21a–d. §7 is an accepted placeholder (docx→md image drop, per brief). | headings | 4 |
| 2.2 Scorecard as table | §6 is a table but merges "Source A/Source B" into one "Sources" column and adds an unlisted "Trend" column. §11 weekly table matches the spec R3→P→S3 exactly; the **daily table uses 5 levels/side (R5..S5)**, not the specified 3; **the monthly pivot table is entirely absent** (explicitly omitted, see 3.4/5.1 below). | §6, §11 | 3 |
| 2.3 Method steps visible | §4→§5 show observation→normalisation→consensus with the futures-contango adjustment stated; §8 is candle-by-candle; §9 shows persistence/overlap/VOLator/KER explicitly. | §4–§9 | 5 |
| 3.1 Quantitative claims sourced | Most §1/§12/§14 figures point to §4/§6/§13, but several of the sourced figures are themselves incorrect (see 3.4) — sourcing discipline is good, reliability of what's sourced is not. | text | 3 |
| 3.2 Citations exist & contain data | Spot-checked 3 (Reuters "Asian share markets firmed"; TradingEconomics "higher for longer"; Bloomberg "–1.53%" — this last is internally reproducible: (4,470.78−4,539.27)/4,539.27 = −1.51%, close to the quoted −1.53%). All 3 are named, dated, self-consistent — no fabrication found. One core figure (Monday's low, used as the literal Trade 1 entry trigger) cannot be reconciled to the leak-free feed at the needed precision (see 3.4), which is a reliability gap, not evidence of a fabricated citation. | §4, §13a | 3 |
| 3.3 Calculations transparent | Pivot formula and RSI2 method are stated and mostly reproduce (see 3.4 for the one that doesn't); ATR is quoted only approximately ("≈110") in §21b Trade 1 rather than stated once with precision. | §6, §11, §21 | 3 |
| 3.4 Numbers reconcile — internal AND vs level file | **Internally**: D−1 close (4,500.92) identical across §1/§3/§4/§6/§21c — fine. **Externally, against the file, this is the report's core failure**: Monday(D−1) Low 4,489.86 vs file `prev_low_full` 4,447.71 → Δ=42.15 (0.42×ATR14_full, more than 2× the >0.115×ATR "failure" line, and >2× the >0.20×ATR OHLC-failure line too) — undisclosed, and it is the literal break-trigger for Trade 1's entry. Close 4,500.92 vs `prev_close_full` 4,484.78 → Δ=16.14 (>0.115×ATR failure line); vs `prev_close_cash` 4,481.20 → Δ=19.72, also fails. Open 4,539.79 vs `prev_open_full` 4,521.93 → Δ=17.86 (discrepancy band, not failure). Cascading into daily pivots (file `_full`): P 4,512.27 vs 4,492.7867 (Δ19.48, FAIL); R1 4,534.68 vs 4,537.8633 (Δ3.18, consistent); R2 4,568.44 vs 4,590.9467 (Δ22.51, FAIL); R3 4,590.85 vs 4,636.0233 (Δ45.17, FAIL); S1 4,478.51 vs 4,439.7033 (Δ38.81, FAIL); S2 4,456.10 vs 4,394.6267 (Δ61.47, FAIL); S3 4,422.34 vs 4,341.5433 (Δ80.80, FAIL) — 5 of 7 daily pivots fail tolerance; the `_cash` basis fails worse, so basis choice does not rescue this. Weekly pivots, by contrast, are excellent (all ≤0.5 vs `w_full_*`, well inside the ≤0.04×ATR band) and the 5-day/25-day swing figures the report quotes narratively (mid-May high "≈4,775" vs `swing_high_25d_full` 4,773.37; Friday high 4,595.31 vs `swing_high_5d_full` 4,595.21; Friday low 4,366.41 vs `swing_low_5d_full` 4,366.35) all match closely. **RSI2 arithmetic error, independent of the file**: 28-May RSI2 is stated 100.0 but does not reproduce from the report's own stated closes — using 26/27/28 May closes (4,507.51 → 4,458.21 → 4,494.93), mean gain=(0+36.72)/2=18.36, mean loss=(49.30+0)/2=24.65, RS=0.745, RSI2=100−100/1.745=42.7, not 100.0 (the value the report shows one row earlier, at 27 May — the column looks off-by-one for this one row). The 1-Jun RSI2 (53.6) *does* reproduce from the report's own closes, and lands in the discrepancy (not failure) band vs the file (Δ9.1 vs `rsi2_full` 44.507, Δ11.1 vs `rsi2_cash` 42.5103) — a natural consequence of the report's own OHLC/close series diverging from the ground truth, not a fresh error. | cross-section + level file | 0 |
| 4.1 Pillars conclude | §8 "Indecision — reversal risk"; §9 "Bearish"; §10 per-row Confirms/Neutral; §12 per-factor supportive/negative labels; §14 per-line price-negative/two-sided labels — all present. | those sections | 5 |
| 4.2 Peer/cross-asset interpreted | §10 gives a mechanism for each counter (opportunity cost, real-yield/appetite channel), not a bare correlation list. | §10 | 5 |
| 4.3 Synthesis reconciles tensions | §15/§16/§18 explicitly address the short- vs medium-term tension and state "Conflict flag: none" between §17 and §21a — coherent, but the synthesis never addresses the card-construction departures below, which the QA protocol folds into this category. | §15–§18, §21a | 4 |
| 4.4 Calibrated language | §17 is one sentence; H/M/L confidence stated in §3/§18; "likely"/"may" used appropriately. | §3, §17 | 4 |
| **Card construction (folded into C4 per `QA_PROTOCOL_TRADE_CARDS.md` §"Category anchors")** | **Trade 1** is built as a dual-branch STOP/LIMIT order ("sell stop at 4,488 … or sell-limit into 4,535") — M5 fixes Trade 1 as **market at the daily-open anchor**, not a conditional stop/limit. **Trade 2** fades into daily R1 (RANGE-regime construction: limit at R1, tiered) while the report's own §9 regime call is **Transitional**, for which M5 specifies **breakout side only**, not a resistance fade — the card contradicts the report's own regime label. **Trade 3B**'s entry band (4,535–4,560) sits at only ~41–48% of the 25-day range from the low (using file `swing_low_25d_full` 4,366.35 / `swing_high_25d_full` 4,773.37, width 407.02: (4,535−4,366.35)/407.02=41.4%, (4,560−4,366.35)/407.02=47.6%) — M5 fixes the 3B short-fade zone at **78.6–88.6%** of the range (≈4,686.25–4,726.95 here); TP1 "range mid ≈4,480" is also well off the file-derived true midpoint (4,366.35+407.02/2=4,569.86). All 3 cards pass the static linter (structurally CLEAN, 0 DUD/WARN) because the linter's leak-free static mode cannot see market-relative placement — these are placement-logic failures a static check cannot catch. | §21b, M5 rules (brief §3) | 1 |
| 5.1 Data dated; staleness flagged | Every price/article dated; Monday's close cross-source delta is flagged indicative (§6, §11, §19) — but the (larger) Low discrepancy that drives the Trade 1 trigger is never flagged. | §4, §6, §13, §19 | 4 |
| 5.2 Assumptions up front | Futures-to-spot normalisation stated with size (§5, "~+USD 25–55"); anchor override stated explicitly as a **logged non-conformance** in §2 and §20, with the same 02:00-broker time carried onto all 3 cards (`anchor_broker`) — this is the compliant handling the brief asks reviewers to check for, and it passes. Single-source pivot propagation (Monday-anchored daily levels) is carried into the card caveats. | §21b, §19, §20 | 5 |
| 5.3 Red flags surfaced | §12/§15 carry explicit risk factors; §13d jobs-report collision is carried into every card's Caveats row. | §12, §15, §21b | 5 |
| 5.4 Restrictions honoured | No bracketed variable names or module codes (M1..M5) found in body text; no synthesised price presented as sourced; futures used corroboration-only and normalised; instrument common names used throughout. No breach found. | whole report | 5 |

## 2. Category roll-up

| Category | Max | Row mean → level | Multiplier | Points | Justification |
|---|---|---|---|---|---|
| C1 Prompt adherence | 20 | (4+4+5)/3=4.33→4 | 0.85 | 17.0 | Variables respected; only a labelling ambiguity on the as-of date. |
| C2 Structure | 20 | (4+3+5)/3=4.0→4 | 0.85 | 17.0 | All sections present/ordered; Scorecard column spec drift + missing monthly pivot table pull 2.2 down. |
| C3 Accuracy & evidence | 25 | (3+3+3+0)/4=2.25→2 | 0.40 | 10.0 | Sourcing and calc-transparency are genuinely good (rows 3.1–3.3), but row 3.4's external reconciliation is a severe, multi-point failure (D−1 Low off 0.42×ATR, 5/7 daily pivots fail tolerance, one RSI2 value doesn't reproduce) that feeds directly into Trade 1's entry trigger — this single row is weighted enough by the brief's own emphasis ("the main accuracy test") to hold the category at Weak despite the surrounding rows. |
| C4 Reasoning & judgment | 20 | narrative rows avg 4.5, but card construction=1 → capped 2 | 0.40 | 8.0 | Narrative synthesis/pillars/cross-asset reasoning are strong (rows 4.1–4.4 ≈4.5), but per the protocol card construction is scored in this category and **all 3 cards** carry identifiable M5 rule departures (Trade 1 wrong entry type, Trade 2 regime/construction mismatch, Trade 3B entry band ~40pp outside the specified zone) — analogous to the framework's own precedent that a category caps low when a majority of its checked items fail regardless of strength elsewhere. |
| C5 Currency & transparency | 15 | (4+5+5+5)/4=4.75→5, held to 4 | 0.85 | 12.75 | Excellent dating/assumption/red-flag practice and a textbook-compliant anchor-override disclosure; held one level below the row mean because the Trade-1-critical Low discrepancy (row 3.4/5.1) is never flagged despite being larger than the one that is. |

**Total = 17.0 + 17.0 + 10.0 + 8.0 + 12.75 = 64.75 → 65**

## 3. Total, band, override

```
c1=4
c2=4
c3=2
c4=2
c5=4
total=65
band=Moderate Trust (60-74)
override=none
```
No cited source was found fabricated or self-contradictory on spot-check (override 1 not triggered). No prompt-level restriction was openly violated — the card-construction departures are M5 mechanics failures (scored in C4), not a violated prompt restriction (override 2 not triggered).

## 4. Card Integrity (linter rows, copied verbatim from `qa/gold_regen_qa1/lint_static/2026-06-02.csv`)

| card_id | strategy | flags | dud | integrity (100−40·dud−10·warn) |
|---|---|---|---|---|
| 2026-06-02_Trade_1 | Trade 1 - Daily Directional (SHORT) | CLEAN | False | 100 |
| 2026-06-02_Trade_2 | Trade 2 - Pivot, regime-aware (SHORT-from-resistance) | CLEAN | False | 100 |
| 2026-06-02_Trade_3B | Trade 3 - Regime-driven complex → fork 3B (Mean-Reversion) | CLEAN | False | 100 |

```
card_integrity=100
n_cards=3
n_duds=0
n_warns=0
```
Note: the linter's static (leak-free) mode confirms only structural integrity (stop side, TP ordering, R-bounds) — it cannot see the market-relative placement failures documented under "Card construction" above (Trade 1's entry type, Trade 2's regime mismatch, Trade 3B's range-percentile placement), which is why Card Integrity is 100 even though the reviewer's cross-check against the level file finds real construction defects. See `2026-06-02_feedback.md`.
