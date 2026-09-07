# Trust Score — 2026-07-31 — SP500_Report_31Jul2026.md

Run: regen_20260906_qa1 · Asset: US500 (S&P 500 cash) · D = 2026-07-31 · D-1 = 2026-07-30
Evidence basis: the report; reports dated before D (30 Jul report used for cross-report consistency);
`data/slices/US500/US500_upto_2026-07-30.csv` (+ VIX, USDX slices) via `engine/qa_slice_stats.py`;
`cards/baseline/by_date/2026-07-31.json`; `qa/regen_20260906_qa1/lint_static/2026-07-31.csv`.

Helper output used throughout (cash session 16:30–23:00 broker):
D-1 cash O/H/L/C 7383.2 / 7447.4 / 7368.2 / 7439.70 · ATR14 81.46 ·
daily pivots P 7418.43 R1 7468.67 S1 7389.47 R2 7497.63 S2 7339.23 R3 7547.87 S3 7310.27 ·
weekly (prior week) P 7437.53 R1 7499.77 S1 7349.57 R2 7587.73 S2 7287.33 ·
5d swing high 7480.30 (27 Jul) low 7314.50 (29 Jul) · 25d high 7582.80 (15 Jul) low 7303.10 (26 Jun) ·
RSI2 on slice closes 6.33 / 100.00 / 100.00 / 13.49 / 51.28 ·
RSI2 recomputed from the report's OWN closes: n/a, n/a, 100.0, 12.2, 51.9.

## 1. Section 7 checklist

| Item | Reviewer notes | Evidence observed | Score 0–5 | Action required |
|---|---|---|---|---|
| 1.1 Variables respected | Asset = S&P 500 cash index (^GSPC), not ES futures ✓. Counters listed USDX · VIX · DAX 40, USDX first ✓. As-of 31 Jul America/New_York, last completed session 30 Jul ✓. Lookback 5 sessions (24/27/28/29/30 Jul) ✓. USD / index points ✓ (tick 0.01 never stated). 7 price sources + 7 news sources ≥ 6 ✓. Daily-open anchor 07:00 UK stated ✓ and matches the baseline card's 09:00 broker time. BUT two fixed M5 rules are openly overridden: Trade 1 issued with score +0.08 against the 0.25 conviction gate, and Trade 2 issued although §19 declares every pivot tier single-source-indicative. | §2, §4, §10, §13a, §20, §21a/b | 2 | Restore the deterministic suppression rules; state tick size in §2. |
| 1.2 Coverage & currency consistent | All price dates are D-1 or earlier; the session label is D ✓. No currency/unit drift (index points throughout) ✓. Defect: the "weekly pivots (prior-week H/L/C)" table implies inputs H 7540.75 / L 7307.90, and 7307.90 is the report's own 29 Jul low — i.e. current-week data used in a prior-week table. §9 dates the 25-session high to 10 Jul at 7,579.93 while the slice puts it at 7,582.80 on 15 Jul. | §11 weekly, §9 | 3 | Rebuild weekly pivots from 20–24 Jul only; correct the §9 window-high date. |
| 1.3 Audience & tone | Written for a senior US equity strategist / trading-and-risk review: regime language, conviction gate, invalidation levels, no retail framing, no solicitation. Footer role line present. | §1, §18, footer | 5 | None. |
| 2.1 Sections present & ordered | §1–§21 all present in order, including §13a/b/c/d and §21a/b/c/d, §19 Source Discipline and §20 Agent Log. §21d carries the limitations boilerplate. | headings throughout | 5 | None. |
| 2.2 Scorecard as a table | §6 is a table with Date/O/H/L/C/RSI2/Trend/Src A/Src B/Final/Validation ✓. §11 has daily, weekly and monthly pivot tables, ordered top-down. Deviation: 5 levels each side (R5→S5) instead of the specified 3 (R3→P→S3). | §6, §11 | 4 | Trim pivot tables to R3→P→S3. |
| 2.3 Method steps visible | §4 observations → §5 classification/consensus build with an explicit tolerance and exclusion rule ✓. §8 is candle-by-candle for all five sessions plus a sequence assessment ✓. §9 gives persistence, overlap, VOLator slope and a Kaufman confirmation ✓. §7 charts are pandoc image placeholders (5), accepted as evidence and noted. | §4–§9 | 5 | None (charts noted as pandoc placeholders). |
| 3.1 Quantitative claims sourced | Index levels in §1/§12 trace to §4/§6 ✓ and sentiment to §13a ✓. Unsourced quantitative claims: 30-year yield ">5.2% (highest since 2007)", "~one-third tail on a September hike", core PCE 3.4% y/y, gold "~4,162", "Micron, Sandisk +9%", "8% semiconductor bounce", Microsoft "~43% cloud-revenue growth". None of these appears in §4, §13a or the §20 source list. | §1, §12, §14 vs §4/§13a/§20 | 2 | Cite or drop each macro/single-stock figure. |
| 3.2 Citations exist & contain data | Spot-check 1 — S&P Dow Jones, 30 Jul close 7,437.63: used identically in §1/§3/§4/§6/§11/§18 ✓. Spot-check 2 — Yahoo Finance 30 Jul "7,437.63 (+121.48)": 7,437.63 − 7,316.15 = 121.48, internally consistent ✓. Spot-check 3 — CNBC dated **28 Jul**, "Dow drops 1,100 points for worst day since April 2025", quote "fear the Fed is falling behind on inflation": impossible as dated. The report's own §13c records 28 Jul as **+0.21% to 7,428.78** and places the FOMC hawkish hold and the −1.52% worst-day-since-April-2025 on **29 Jul**; the 30 Jul report cites the same CNBC piece at 29 Jul. A cited source carrying a wrong date and a figure that contradicts the report's own record counts as fabricated. Compounding: the Baltimore Sun/AP 30 Jul quote calls the same selloff "worst in seven weeks" while CNBC calls it worst since April 2025. | §13a rows 3 and 4 vs §13c, §8, §12; 30 Jul report §4 | 0 | Re-date the CNBC article to 29 Jul (or remove it) and reconcile the two conflicting "worst day" characterisations. **Triggers the hallucinated-source override.** |
| 3.3 Calculations transparent | Pivots: §11 daily levels reproduce exactly from the report's own 30 Jul H/L/C (7443.90/7333.50/7437.63) — P 7405.01, R1 7476.52, S1 7366.12, R2 7515.41, S2 7294.61, R3 7586.92, S3 7255.72 all match to the cent, and the floor identity holds (R2−P = 110.40 = P−S2) ✓; weekly and monthly tables are also internally self-consistent ✓. ATR ≈ 82 stated and matches slice ATR14 81.46 ✓. FAILURES: RSI2 does not reproduce from the report's own close sequence — 28 Jul should be 100.0 (stated 37.2), 29 Jul 12.2 (stated 7.7), 30 Jul 51.9 (stated 66.0); the Trend rule is then misapplied (27 and 28 Jul, close > open with RSI2 = 100, are labelled Neutral). §13b tilt: with the stated weights and counts Σw·s = 0.5×4 + 0.7 − 0.5 − 0.7 = +1.50, Σw = 3.9, tilt = +0.38, not the stated +1.20 / +0.31. §21a: the listed contributions (+0.11, +0.075, +0.03, −0.05, −0.06) sum to +0.105, not the stated +0.08, and only 5 of the 6 weighted signals are shown. KER −0.16 asserted with no 13-period / EMA-3 derivation. | §6, §11, §13b, §21a, §9 | 1 | Recompute RSI2 and Trend from the validated closes; fix the §13b tilt; show all six weighted signals summing to the stated score. |
| 3.4 Numbers reconcile | D-1 close 7,437.63 identical in §1, §3, §4, §6, §18 and ≈7,438 on the Trade 1 card ✓; §11 daily P/S1/R1/R2 are quoted verbatim on the cards ✓. BREAKS: Trade 1 shows two entries (buy stop 7,455 and market ≈7,438) with R = 72 pts computed off 7,438 while the baseline card records entry 7,455 / R 89; TP1 7,510 is +1R from 7,438 but only +55 from 7,455. Trade 1 TP2 7,582 is labelled "monthly R3" but §11 monthly R3 = 7,824.02 (7,582 sits near monthly R1 7,588.19). Trade 1 confluences say "TP1 near weekly R1 7,532" while TP1 = 7,510. Trade 3A calls its entry the "38.2% fib" but 38.2% of the 7,308→7,444 leg is 7,391.95, not 7,412 (that is 23.5%). §21d claims Trade 1 "triggered 3/5" while §21c shows 2 triggers (28 and 30 Jul). §13b class counts "(3 media, 1 media, 1 trade press)" is malformed. ATR is quoted in §21b but never stated in §9. | §21b, §21c/d, §11, §13b | 2 | Re-derive every card level from one declared entry; fix the level labels and the §21d trigger counts. |
| 4.1 Pillars conclude | §8 ends in an explicit judgement label; §9 ends in a bias plus a Kaufman precedence rule; §10 ends in an aggregate CONFIRM; §12 labels each consideration cyclical/structural with a price sign; §14 gives a net read per block and a watch item. Labels are consistent with the content of each section. | §8–§14 | 4 | Give §14 a single closing direction label. |
| 4.2 Peer/cross-asset interpreted | §10 supplies genuine mechanisms (dollar → multinational translation, VIX → fear unwind/re-risking, DAX → European contagion proxy) rather than a correlation list, and the aggregate CONFIRM is carried into §21a ✓. Weakened by the inputs: VIX is quoted 20.66 → 17.09 while the slice shows 19.59 → 18.02 and a 29 Jul VIX high of only 19.89, so the "collapse from above the 20 threshold" is not supported; USDX ~100.98 vs slice close 99.97. | §10, §14 vs VIX/USDX slices | 3 | Restate the VIX and USDX levels from the corroborated feed. |
| 4.3 Synthesis reconciles tensions | The short-term bullish reversal vs the bearish medium-term structure is named in §9, given a precedence rule (KER over the one-day candle), carried into §16 with two-sided invalidations (7,366 down / 7,532 up), restated in §18, and reflected in §21a's low-conviction handling. §15 is balanced four-for-four. §13b explicitly flags the sentiment-vs-regime divergence. | §9, §13b, §15–§18, §21a | 5 | None. |
| 4.4 Calibrated language | §17 is exactly one sentence, directional, with a single conditioning clause and no hedge stacking ✓. §3 states confidence High, §21a states conviction LOW ✓. Mild overstatement: §3 "High" confidence sits beside §6 rows whose O/H/L are indicative and, in the case of 30 Jul, materially wrong. | §3, §17, §21a | 4 | Align the §3 confidence with the corroboration actually achieved. |
| 5.1 Data dated; staleness flagged | Every §6 row, §4 row and §13a article is dated ✓; single-source O/H/L for 24/27/28 Jul carry an asterisk and a footnote ✓; §19 gives corroboration status per instrument ✓. Inconsistency: the 30 Jul row is stamped CORROBORATED Δ≤0.10 across the whole row, yet §11 calls the 30 Jul high/low indicative and §19 calls all pivot prior-period high/low single-source indicative — and the 30 Jul open and low are both given as 7,333.50 against slice values 7,383.2 and 7,368.2. | §6, §11, §19 | 3 | Flag 30 Jul O/H/L at its true corroboration level and correct the values. |
| 5.2 Assumptions up front | The 07:00 UK anchor is stated in §2, in §20 ("Daily-open anchor override applied: 07:00 UK") and on the Trade 1 card ✓. Single-source-indicative pivot propagation is stated in §5, §6 footnote, §11, §19 and repeated as a caveat on Trades 2 and 3 ✓. The below-threshold discretionary override is disclosed in §20 and §21a ✓ (disclosure does not cure the breach). | §2, §19, §20, §21b | 4 | None beyond the breach itself. |
| 5.3 Red flags surfaced | §12 gives five risk blocks with signs; §15 is a four-row bull/bear balance; §13d event collisions (June PCE 31 Jul, Apple/Amazon post-close) are carried explicitly into the caveat line of all three cards and into §16's invalidation. | §12, §15, §13d, §21b | 5 | None. |
| 5.4 Restrictions honoured | Honoured: CFD/US500 spread quotes explicitly excluded from the cash basis (§5, §19); no ES futures in the OHLC basis; no bracketed variable names, no module codes (M1–M5), no framework name; instrument common names used ✓. BREACHED: (a) Trade 1 issued at score +0.08 although the fixed rule suppresses Trade 1 when |score| < 0.25 — §20 states the suppression "was OVERRIDDEN"; (b) Trade 2 issued although §19 declares every pivot tier SINGLE-SOURCE INDICATIVE, the stated condition for suppressing Trade 2 entirely; (c) Trade 2 carries a counter-side sell limit at R2 in a regime the report itself labels TRANSITION, where only the breakout side is permitted; (d) the 30 Jul open and low, both given as 7,333.50, are presented as corroborated cash values when they reconcile to nothing in the session data. | §20, §21a, §21b, §6/§19 | 1 | Emit SUPPRESSED rows where the rules require them; remove the counter-side limit; do not present unreproducible intraday values as corroborated. **Triggers the restriction-breach override.** |

## 2. Category roll-up

| Category | Level | Multiplier | Points | Justification |
|---|---|---|---|---|
| C1 Prompt adherence (max 20) | 2 | 0.40 | 8.00 | Rows 1.1–1.3 mean (2+3+5)/3 = 3.33 → 3; reduced one level to 2 by the restriction-breach override. Variables and anchor are respected, but two deterministic suppression rules are openly overridden and the weekly pivot window is wrong. |
| C2 Structural alignment (max 20) | 5 | 1.00 | 20.00 | Rows 2.1–2.3 mean (5+4+5)/3 = 4.67 → 5. Every section §1–§21 present and ordered, §6 and §11 are proper tables, method steps visible; only the 5-deep pivot ladder deviates. |
| C3 Accuracy & evidence (max 25) | 0 | 0.00 | 0.00 | Rows 3.1–3.4 mean (2+0+1+2)/4 = 1.25 → 1; set to 0 by the hallucinated-source override (mis-dated CNBC citation). Independently: RSI2 fails to reproduce from the report's own closes, and the 27 and 30 Jul open/low miss the slice by 34–62 points. |
| C4 Reasoning & judgment (max 20) | 4 | 0.85 | 17.00 | Rows 4.1–4.4 mean (4+3+5+4)/4 = 4.0 → 4. Pillars conclude, the cross-asset section gives mechanisms, and the short/medium-term conflict is genuinely reconciled; card construction defects are scored at 3.4/5.4 and the counter-asset levels are off. |
| C5 Currency, restrictions & transparency (max 15) | 3 | 0.65 | 9.75 | Rows 5.1–5.4 mean (3+4+5+1)/4 = 3.25 → 3. Dating, assumptions and red flags are strong; restrictions row is a 1 because three fixed strategy rules are overridden and unreproducible intraday values are stamped corroborated. |
| **Total** | — | — | **54.75 → 55** | Sum of category points, rounded. |

## 3. Total, band, override check

- Raw total: 8.00 + 20.00 + 0.00 + 17.00 + 9.75 = **54.75 → 55**.
- **Hallucinated-source override — APPLIES.** §13a cites CNBC dated 28 Jul for "Dow drops 1,100 points for worst day since April 2025" with a Fed-fear quote. The report's own §13c records 28 Jul as +0.21% to 7,428.78 and places the FOMC hawkish hold and the −1.52% worst-day-since-April-2025 on 29 Jul; the 30 Jul report cites the same CNBC piece at 29 Jul. A cited source that is impossible as dated counts as fabricated: total capped at the Low band (40–59) and C3 set to 0.
- **Restriction-breach override — ALSO APPLIES.** Trade 1 issued below the 0.25 conviction gate, Trade 2 issued despite all pivot tiers being single-source-indicative, and a counter-side limit placed in a TRANSITION regime. Cap at Moderate (60–74) and C1 reduced by one level (3 → 2). The Low-band cap is the binding constraint.
- Post-override total: **55** (already ≤ 59, so no further reduction is needed).
- **Band: Low (40–59).**
- Override recorded in the roll-up CSV: `hallucinated_source` (the binding cap; the restriction breach is applied through C1 and noted here).

## 4. Card Integrity

Linter rows, verbatim from `qa/regen_20260906_qa1/lint_static/2026-07-31.csv`:

| card_id | report_date | strategy | flags | dud |
|---|---|---|---|---|
| 2026-07-31_Trade_1 | 2026-07-31 | Trade 1 - Daily Directional (breakout stop) | CLEAN | False |
| 2026-07-31_Trade_2 | 2026-07-31 | Trade 2 - Pivot (buy limit daily P) | CLEAN | False |
| 2026-07-31_Trade_3A | 2026-07-31 | Trade 3A - Momentum-Pullback (38.2% fib) | CLEAN | False |

Per-card integrity (100 − 40·#DUD − 10·#WARN, floored at 0):

| Card | #DUD | #WARN | Integrity |
|---|---|---|---|
| 2026-07-31_Trade_1 | 0 | 0 | 100 |
| 2026-07-31_Trade_2 | 0 | 0 | 100 |
| 2026-07-31_Trade_3A | 0 | 0 | 100 |

Non-suppressed cards: 3. **Report-level Card Integrity = 100.0.**

Note: static integrity is clean — stops on the correct side, TP1/TP2/TP3 ordered, R within 0.3–3.0×ATR14
(89/65/52 pts against ATR14 81.46 = 1.09×, 0.80×, 0.64×), TP1 within 2.5×ATR of entry, limit/stop levels on
the correct side of the D-1 close, anchor explicit. The construction failures below are rule violations that
the static linter cannot see; they are scored in rows 3.4, 4.x and 5.4, not in this number.

## 5. Data reconciliation log

Tolerance per the brief: |Δ| ≤ 3.0 pts on a close, ≤ 8.0 pts on an open/high/low = consistent with the CFD-vs-cash basis.

| Section | Report value | Slice value (cash session) | Delta | Verdict |
|---|---|---|---|---|
| §6 24 Jul Open | 7409.30 | 7407.6 | +1.70 | OK |
| §6 24 Jul High | 7433.10 | 7460.2 | −27.10 | DISCREPANCY |
| §6 24 Jul Low | 7397.20 | 7395.6 | +1.60 | OK |
| §6 24 Jul Close | 7411.98 | 7411.8 | +0.18 | OK |
| §6 27 Jul Open | 7412.00 | 7473.8 | −61.80 | MAJOR DISCREPANCY |
| §6 27 Jul High | 7440.60 | 7480.3 | −39.70 | MAJOR DISCREPANCY |
| §6 27 Jul Low | 7401.50 | 7382.9 | +18.60 | DISCREPANCY |
| §6 27 Jul Close | 7413.18 | 7415.5 | −2.32 | OK |
| §6 28 Jul Open | 7418.00 | 7417.4 | +0.60 | OK |
| §6 28 Jul High | 7455.30 | 7452.9 | +2.40 | OK |
| §6 28 Jul Low | 7405.10 | 7384.6 | +20.50 | DISCREPANCY |
| §6 28 Jul Close | 7428.78 | 7433.6 | −4.82 | DISCREPANCY (close outside ±3) |
| §6 29 Jul Open | 7418.16 | 7424.5 | −6.34 | OK |
| §6 29 Jul High | 7433.60 | 7450.5 | −16.90 | DISCREPANCY |
| §6 29 Jul Low | 7307.90 | 7314.5 | −6.60 | OK |
| §6 29 Jul Close | 7316.15 | 7317.5 | −1.35 | OK |
| §6 30 Jul (D-1) Open | 7333.50 | 7383.2 | −49.70 | MAJOR DISCREPANCY |
| §6 30 Jul (D-1) High | 7443.90 | 7447.4 | −3.50 | OK |
| §6 30 Jul (D-1) Low | 7333.50 | 7368.2 | −34.70 | MAJOR DISCREPANCY |
| §6 30 Jul (D-1) Close | 7437.63 | 7439.70 | −2.07 | OK |
| §6 RSI2 24 Jul | 13.2 | 6.33 (slice) / n/a from report closes | +6.87 | Not verifiable from the report's own closes; inconsistent with the slice |
| §6 RSI2 27 Jul | 14.4 | 100.00 (slice) / n/a from report closes | −85.60 | Not verifiable from the report's own closes; inconsistent with the slice |
| §6 RSI2 28 Jul | 37.2 | 100.00 (slice) / **100.0 from the report's own closes** | −62.80 | FAIL — arithmetic does not reproduce (two consecutive gains ⇒ RSI2 = 100) |
| §6 RSI2 29 Jul | 7.7 | 13.49 (slice) / **12.2 from the report's own closes** | −4.50 | FAIL — arithmetic does not reproduce |
| §6 RSI2 30 Jul | 66.0 | 51.28 (slice) / **51.9 from the report's own closes** | +14.10 | FAIL — arithmetic does not reproduce |
| §6 Trend 27 Jul | Neutral | Close 7413.18 > Open 7412.00 and RSI2 = 100 ⇒ Bullish | — | FAIL — trend rule misapplied |
| §6 Trend 28 Jul | Neutral | Close 7428.78 > Open 7418.00 and RSI2 = 100 ⇒ Bullish | — | FAIL — trend rule misapplied |
| §11 daily P | 7405.01 | 7418.43 | −13.42 | Reproduces exactly from the report's own H/L/C (identity R2−P = P−S2 = 110.40 holds); the gap is inherited from the wrong 30 Jul open/low |
| §11 daily R1 | 7476.52 | 7468.67 | +7.85 | Internally correct, inherited input error |
| §11 daily S1 | 7366.12 | 7389.47 | −23.35 | Internally correct, inherited input error |
| §11 daily R2 / S2 | 7515.41 / 7294.61 | 7497.63 / 7339.23 | +17.78 / −44.62 | Internally correct, inherited input error |
| §11 daily R3 / S3 | 7586.92 / 7255.72 | 7547.87 / 7310.27 | +39.05 / −54.55 | Internally correct, inherited input error |
| §11 weekly P | 7420.21 | 7437.53 (20–24 Jul) | −17.32 | FAIL — implied inputs H 7540.75 / L 7307.90; the low is the report's own 29 Jul low, i.e. current-week data in a prior-week table |
| §9 25-session high | 7,579.93 on 10 Jul | 7582.80 on 15 Jul | −2.87 and wrong date | DISCREPANCY (date) |
| §8 nearest support (5d swing low) | 7,307.90 | 7314.50 | −6.60 | OK on value |
| §21b Trade 1 "28 Jul swing high" | 7,455 | 5-day swing high 7480.30 (27 Jul) | −25.30 | DISCREPANCY — wrong swing extreme and wrong session |
| §21b ATR(14) | ≈ 82 | 81.46 | +0.54 | OK |
| §21b Trade 3A qualifying leg | 7,308 → 7,444 = 136.0 pts | 2×ATR14 = 162.92 required | −26.92 | FAIL — leg does not qualify as a swing (slice up-leg 7314.50→7447.40 = 132.90 also fails) |
| §1/§10 VIX 29 Jul → 30 Jul | 20.66 → 17.09 | 19.59 → 18.02 (29 Jul high only 19.89) | +1.07 / −0.93 | DISCREPANCY — the "above 20, collapsed below 20" framing is not supported |
| §10/§14 USDX 30 Jul | ~100.98 (from a ~101.6 spike) | close 99.97 (28 Jul high 101.64) | +1.01 | DISCREPANCY on level; spike value OK, direction OK |
| §13b sentiment tilt | +1.20 / 3.9 = +0.31 | Report's own weights and counts give Σw·s = +1.50, tilt = +0.385 | −0.075 | FAIL — arithmetic error |
| §21a direction score | +0.08 | Listed contributions sum to +0.105 | −0.025 | FAIL — components do not sum to the stated score; 1 of 6 weighted signals not shown |
| §21d Trade 1 triggers | 3/5, mean +0.13 | §21c shows 2 triggers (28 Jul −1.0R, 30 Jul +1.4R), mean +0.20 | — | FAIL — a non-triggered row counted as a 0R trigger |
| Cross-report (30 Jul report §6) 29 Jul O/H/L | 7418.16 / 7433.60 / 7307.90 | 7405.0 / 7412.0 / 7315.3 as published one day earlier | +13.16 / +21.60 / −7.40 | INCONSISTENT across consecutive reports for the same session |
| Cross-report (30 Jul report §6) 28 Jul H/L | 7455.30 / 7405.10 | 7444.3 / 7391.9 | +11.00 / +13.20 | INCONSISTENT across consecutive reports |
| Cross-report (30 Jul report §6) 27 Jul O/H/L | 7412.00 / 7440.60 / 7401.50 | 7433.0 / 7450.6 / 7382.0 | −21.00 / −10.00 / +19.50 | INCONSISTENT across consecutive reports |
| Cross-report RSI2 28 / 29 Jul | 37.2 / 7.7 | 100.0 / 12.2 as published one day earlier | −62.8 / −4.5 | INCONSISTENT — the earlier report's values match the correct arithmetic |
