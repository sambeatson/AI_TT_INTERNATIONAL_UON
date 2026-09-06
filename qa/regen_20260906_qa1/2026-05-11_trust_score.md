# Trust Score — 2026-05-11 — SP500_Report_11May2026__2_.md

Run: regen_20260906_qa1 · D = 2026-05-11 (Mon) · D-1 = 2026-05-08 (Fri) · Slice: data/slices/US500/US500_upto_2026-05-10.csv (last bar 2026-05-08 23:45 broker) · Helper: `engine/qa_slice_stats.py --date 2026-05-11 --closes 7200.75 7259.22 7365.12 7337.11 7398.93`.

Report-stated basis noted in step 1: D-1 O/H/L/C = 7,344.7 / 7,401.5 / 7,340.2 / 7,398.93; RSI2 column 66.6 / 100.0 / 79.1 / 68.8 / 89.4; ATR(14) never printed as a figure, implied 76.0 (0.25×ATR = 19.0, 3×ATR = 228); daily pivots R3 7,481.52 / R2 7,441.51 / R1 7,420.22 / P 7,380.21 / S1 7,358.92 / S2 7,318.91 / S3 7,297.62; direction score +0.695 LONG; regime TREND_UP (KER ≈ 0.52 "Trending Up — Strong", VOLator slope mildly negative); cards: Trade 1 LONG market 7,398.93 @ 00:00 UK, Trade 2 LONG limit 7,358.92 (daily S1), Trade 3A LONG limit 7,316.24 (38.2% retrace).
Slice basis (cash session 16:30–23:00 broker): D-1 O/H/L/C = 7,375.6 / 7,407.5 / 7,371.8 / 7,400.6; ATR14 cash 70.36 (full-day 76.88); cash pivots P 7,393.30 / R1 7,414.80 / S1 7,379.10 / R2 7,429.00 / S2 7,357.60 / R3 7,450.50 / S3 7,343.40; 5d swing 7,177.5 → 7,407.5.

## 1. Section 7 checklist

| Item | Reviewer notes | Evidence observed | Score 0–5 | Action required |
|---|---|---|---|---|
| 1.1 Variables respected | Asset = S&P 500 cash index; counters Dollar Index · VIX · DAX 40 in the required order; as-of NY close Fri 8 May, tz America/New_York; 5-session lookback; USD / index points / tick 0.01; six §4 sources incl. index provider (FRED/S&P DJI) and exchange-derived (Yahoo). Daily-open anchor is 00:00 UK, not the 07:00 UK fixed in the instance; the report attributes this to a "user override" that is not part of the fixed prompt stack, and the entry is a synthetic mark (prior close) rather than a traded open. | §2 table; §4 six rows; §20 "Daily-open anchor override"; §21b Trade 1 "Market at 00:00 UK" | 3 | Restore 07:00 UK anchor; drop the override narrative. |
| 1.2 Coverage & currency consistent | All prices dated D-1 or earlier; units consistent (points/USD). Defects: §11 weekly pivots for the week of 11 May are derived from 28 Apr–1 May, i.e. the week before the prior week (should be 4–8 May); §13d labels 15 May 2026 as "Thu" (it is Friday); two §13a articles carry only "early May 2026" as a date; §4 FXLeaders row dated 10 May (after the as-of snapshot, before D — acceptable, noted). | §11 "derived from prior week 28 Apr – 1 May 2026"; §13d last row; §13a rows 4 and 6 | 3 | Rebuild weekly pivots from 4–8 May; fix the 15 May weekday; date the two articles. |
| 1.3 Audience & tone | Senior-strategist register, risk-review framing, no retail language. Engineering/meta language leaks into the deliverable ("Per user instruction", "M3 §11b", "OPEN-008", `produce_strategy_recommendations`). | §1, §18 tone; §7, §9, §19, §20 meta wording | 4 | Remove process/meta commentary from reader-facing sections. |
| 2.1 Sections present & ordered | §1–§21 all present, in order, with §13a–d and §21a–d sub-sections; §17 is one sentence; §19 and §20 present. | Headings throughout | 5 | None. |
| 2.2 Scorecard as a table | §6 is a table with Date/O/H/L/C/RSI2/Trend/Source A/Source B/Final/Validation. §11 daily and weekly tables run R3→P→S3 (3 each side). Monthly table has only MR2/MR1/MP/MS1 — MR3, MS2, MS3 missing. | §6 table; §11 three tables | 4 | Complete the monthly pivot table to 3 levels each side. |
| 2.3 Method steps visible | §4 observations → §5 classification/consensus shown. §8 candle-by-candle plus sequence assessment; §9 persistence, overlap, KER, VOLator present. §7 has NO charts — the report states charts "would render in a normal engine run" and substitutes prose (not a pandoc image drop; the deliverable itself omits them). §21c backtest table is internally contradictory ("NO … corrected: YES"; "Stopped … OPEN @ +0.5R"). | §7 first paragraph; §21c rows Mon 4 May Trade 2, Thu 7 May Trade 1 | 3 | Render the two charts (or explicit captioned placeholders); clean the §21c rows so each has one trigger state and one outcome. |
| 3.1 Quantitative claims sourced | §1 and §12 FactSet figures (27.7%, 84%, 13.4%, P/E 21.0) sourced. Unsourced: NFP +115k vs +60k consensus (no publisher), March CPI 3.3%, FOMC 3.50–3.75% with four dissents, WTI 95.42 / Brent ~100 / WTI >106 peaks, "83% beat by an average of 11%" (conflicts with the sourced 84%), Mag-7 "more than 40%", "SOX up 65% YTD", the §13d "15% vs 0.0% rate-cut probability" line, "10y up ~40 bp" (Wolfe named only for the 4.15–4.40% range). NFP consensus in the calendar slice is 90k, not 60k (source-dependent, noted). | §1 (ii); §12 paras 3–6; §13d Tue row; §14 paras 1–2; §15 | 2 | Attach a named, dated source to every figure in §1/§12/§14 or point it to §4/§13. |
| 3.2 Citations exist & contain data | Spot-check (1) FRED/S&P DJI 8 May 7,398.93 — figure used identically in §1/§3/§6/§19/§21b; (2) CNBC 8 May "advanced 0.84% to 7,398.93" — 7,398.93 / 7,337.11 = +0.84%, consistent with the §6 Thursday close; weekly +2.3% consistent with the §11 prior-Friday close 7,230.12; (3) TradingEconomics DAX "−325 pts / −1.32% to 24,339" — 325/24,664 = 1.32%, consistent; USDX 97.84 matches the slice (97.841). No self-contradictory or date-impossible citation found. §14 "May ISM Manufacturing prices index 84.6" is the 1 May release (April data) — mislabelled, but the figure is real (slice calendar 84.6). | §4 rows 1–3; §10; §13a; §14 | 4 | Relabel the ISM release month. |
| 3.3 Calculations transparent | RSI2 not shown and does NOT reproduce: helper recomputation from the report's own closes gives Wed 100.0 / Thu 79.1 / Fri 68.8, and Tue 66.6 when the report's own prior-Friday close 7,230.12 is used; the report prints 66.6 / 100.0 / 79.1 / 68.8 / 89.4 — the column is displaced one row upward and the D-1 value 89.4 does not exist in the series. Thu Trend label "Bearish" violates the rule (Close<Open but RSI2 68.8 > 50 → Neutral). Daily/weekly/monthly pivots reproduce exactly from the stated inputs. ATR(14) never stated as a figure (only 0.25×ATR = 19.0 and 3×ATR = 228). KER stated (≈0.52) but the §21a Kaufman input is +0.78 with no mapping shown. §21a Σ signal×weight = 0.250+0.200+0+0.117+0.083+0.045 = 0.695 reproduces; §13b tilt 3.0/5.4 = 0.56 reproduces. | §6 RSI2/Trend columns; §11; §9; §21a; §21b Trade 1 | 2 | Recompute RSI2 from the five closes plus the two preceding closes; relabel Thu Trend; print ATR(14); show the KER→signal mapping. |
| 3.4 Numbers reconcile | D-1 close 7,398.93 identical in §1/§3/§4/§6/§18/§21b; §11 pivots = card pivots; RSI2 §6 = §8 (both carry the displaced values). Against the slice: three of five closes exceed the 3-pt tolerance (Mon −8.45, Tue −6.58, Thu −7.49; none > 10); D-1 open −30.9 and low −31.6 vs cash session; Tue/Wed opens and lows off by 40–47 pts; April low used for monthly pivots 5,760 vs slice 6,471.7 (−712); VIX 17.19 vs slice 19.22 (−2.03, CFD basis caveat); weekly pivot inputs off 27–33 pts and from the wrong week. Internal arithmetic errors: Trade 2 "TP2 7,420.22 within 21 pts of daily R3 7,481.52" (actual 61.3); Trade 1 "TP1 clears daily R3 by ~5 pts" (TP1 is 4.86 pts below R3); §7 "+168 pts above the Monday open" (7,398.93 − 7,235.0 = 163.9); §21a sentiment input 0.55 vs §13b 0.56. | §5 log below; §21b Trade 1/2 confluence rows; §7 | 2 | Re-source O/H/L from a real OHLC feed; correct the confluence arithmetic; align §21a tilt with §13b. |
| 4.1 Pillars conclude | §8 ends "Short-term technical bias: Bullish"; §9 ends "Consolidated regime label: TREND_UP"; §10 ends "cross_asset_confirm = MIXED" (consistent with 2 confirm / 1 contradict). §12 tags each paragraph but gives no closing direction label; §14 ends on positioning with no label. | §8, §9, §10 closing lines; §12, §14 endings | 3 | Add a closing direction label to §12 and §14. |
| 4.2 Peer/cross-asset interpreted | §10 gives mechanisms: USD → multinational EPS translation; VIX → risk-premium regime; DAX weakness explained as idiosyncratic (tariff threat, Rheinmetall) rather than global risk-off, with the contradiction flagged not suppressed. VIX mechanism is thin ("historically aligns"). | §10 table and aggregate paragraph | 4 | Strengthen the VIX mechanism beyond correlation. |
| 4.3 Synthesis reconciles tensions (incl. card construction vs M5) | §15/§16/§18 handle the CPI binary, the DAX contradiction, VOLator-compression-in-trend vs regime, and §17 vs §21a (agree). Card construction is weak: Trade 2 is built with RANGE geometry (limit at S1, stop at S2, TP1 at P = 0.53R by admitted "analyst override") in a TREND_UP regime whose M5 branch is entry P+0.10×(R1−P), stop P−0.8×(P−S1), TPs R1/R1.5/R2 — and the card should be SUPPRESSED because every pivot tier is flagged SINGLE-SOURCE-INDICATIVE (M5 §10), an override the report attributes to a user instruction absent from the fixed stack. Trade 3A enters at the 38.2% retrace instead of 57.5%, uses a 5-pt buffer below 61.8% instead of 0.25×ATR beyond the swing low, sets invalidation = SL, pulls the runner stop toward the swing LOW (7,247.27) instead of halfway between entry and the swing high, and omits the BE+0.2R step on Unit-2 fill. Trade 1 omits the required 'wide stop' flag (R 77.7 > ATR 76). §21c backtest rows contradict themselves and Fri Trade 2 "partial fill near S1" is impossible on the report's own numbers (Thu-derived S1 = 7,315.5 vs Fri low 7,340.2). | §15–§18; §21b all three cards; §21c | 2 | Rebuild Trade 2 and Trade 3A per M5 (see feedback); add the wide-stop flag on Trade 1; fix §21c. |
| 4.4 Calibrated language | §17 is one sentence with a range and a stated catalyst; §3/§18 confidence H/M stated. But §17 asserts "cross-asset confirmation aligned bullish" while §10 aggregates to MIXED — overstatement; "trades higher on Monday" is unhedged given the report's own "stretched RSI2" caveat. | §17; §10; §8 last line | 3 | Make §17 consistent with §10 (MIXED) and the §8 stretch caveat. |
| 5.1 Data dated; staleness flagged | Every price row dated; O/H/L single-source-indicative status stated in §6, §11, §19 and on cards; ATR flagged indicative. Two §13a articles undated ("early May 2026"); §13d weekday error; ISM month mislabelled. | §6 validation note; §19; §13a rows 4, 6; §13d | 4 | Date the two articles; fix labels. |
| 5.2 Assumptions up front | Anchor-override caveat present on the Trade 1 card and in §20; single-source pivot flag propagated to all three cards; weekly/monthly pivot inputs marked "≈"/indicative. The two "user instruction" overrides (anchor, Trade 2 suppression) are asserted without any trace in the fixed stack — the assumption is visible but unjustified. | §20 "Daily-open anchor override", "M5 trace"; §19 para 4; §21b caveat rows | 4 | Remove unverifiable override claims or cite the instruction. |
| 5.3 Red flags surfaced | §12 and §15 enumerate CPI, ceasefire/oil, Fed transition, concentration/Nvidia; §13d CPI collision carried into every card's caveat; DAX contradiction carried to cards. | §12; §15; §21b caveats | 5 | None. |
| 5.4 Restrictions honoured | O/H/L are narrative-derived estimates presented in a "Source A/Source B … CORROBORATED" table — flagged as indicative, so not concealed synthesis; no CFD quotes in the OHLC basis; no ES futures used as basis. BREACH: module codes and internal variable names appear throughout the deliverable — "M3 §11b", "M3 §11c", "M2 §9c" (×2), "M5 §10", "M5 §5.3", "M5 trace", "M1 instance", "M3 regime classification", "Step 4" (×4), "OPEN-008" (×2), W_SHORT_TECH/W_MEDIUM_REGIME/W_VOLATOR/W_KAUFMAN/W_SENTIMENT/W_CROSS_ASSET, `produce_strategy_recommendations` (21 hits). No bracketed variable names; framework name not present. | §7 para 1; §9 para 4; §10; §13b; §16; §19; §20; §21b Trade 2/3A | 1 | Strip every module code, step number, ticket id and weight-variable name from the report body. |

## 2. Category roll-up

| Category | Level | Multiplier | Points | Justification |
|---|---|---|---|---|
| C1 Prompt adherence (20) | 2 | 0.40 | 8.0 | Rows 1.1–1.3 = 3, 3, 4 → mean 3.33 → 3; restriction-breach override reduces C1 by one level → 2. Anchor deviates from the 07:00 UK instance value; weekly pivots from the wrong week; meta language in the deliverable. |
| C2 Structure (20) | 4 | 0.85 | 17.0 | Rows 2.1–2.3 = 5, 4, 3 → mean 4.0. All 21 sections present and ordered; monthly pivot table incomplete; charts absent; §21c malformed rows. |
| C3 Accuracy & evidence (25) | 2 | 0.40 | 10.0 | Rows 3.1–3.4 = 2, 4, 2, 2 → mean 2.5 → 2 (framework §9: lower level when in doubt). RSI2 column does not reproduce from the report's own closes (Category 3 failure per brief §4); three closes 6.6–8.5 pts off the slice; D-1 O/L ~31 pts off; April low off by ~712 pts; many unsourced macro figures. No fabricated source detected. |
| C4 Reasoning & judgment (20) | 3 | 0.65 | 13.0 | Rows 4.1–4.4 = 3, 4, 2, 3 → mean 3.0. Cross-asset mechanism and synthesis adequate; card construction departs from M5 on Trade 2 (wrong regime branch, not suppressed) and Trade 3A (wrong retrace, stop, invalidation, runner rule); §17 overstates cross-asset alignment. |
| C5 Currency, restrictions & transparency (15) | 3 | 0.65 | 9.75 | Rows 5.1–5.4 = 4, 4, 5, 1 → mean 3.5 → 3 (lower level when in doubt; the breach is material). Dating and caveats largely good; module-code restriction breached 21 times. |
| **Total** | | | **57.75 → 58** | |

## 3. Total, band, override check

- **Total: 58/100.** 8.0 + 17.0 + 10.0 + 13.0 + 9.75 = 57.75 → 58.
- **Band: Low (40–59).**
- **Overrides:** `restriction_breach` — the report body contains module codes and internal variable names (M1/M2/M3/M5 section references, "Step 4", "OPEN-008", W_* weight names, an engine function name), breaching the "no module codes (M1..M5)" restriction (brief §2 row 5.4). Applied: C1 reduced one level (3 → 2); cap at Moderate (≤ 74) is not binding at 58. No hallucinated source detected on the three-source spot-check, so the `hallucinated_source` override does not apply and C3 is scored on its merits (2, not 0). The 00:00 UK anchor and the un-suppressed Trade 2 are recorded as deviations (rows 1.1 and 4.3), not as separate overrides.

## 4. Card Integrity

Linter rows (`qa/regen_20260906_qa1/lint_static/2026-05-11.csv`, verbatim):

| card_id | report_date | strategy | flags | dud |
|---|---|---|---|---|
| 2026-05-11_Trade_1 | 2026-05-11 | Trade 1 - Daily Directional | CLEAN | False |
| 2026-05-11_Trade_2 | 2026-05-11 | Trade 2 - Pivot pullback (buy daily-S1) | CLEAN | False |
| 2026-05-11_Trade_3A | 2026-05-11 | Trade 3A - Momentum-Pullback (38.2% fib) | CLEAN | False |

| Card | #DUD | #WARN | Integrity = 100 − 40·DUD − 10·WARN |
|---|---|---|---|
| 2026-05-11_Trade_1 | 0 | 0 | 100 |
| 2026-05-11_Trade_2 | 0 | 0 | 100 |
| 2026-05-11_Trade_3A | 0 | 0 | 100 |

**Report-level Card Integrity = 100.0** (mean over 3 non-suppressed cards; 0 suppressed). n_cards = 3, n_duds = 0, n_warns = 0.

M5-rule assessment (feeds row 4.3, not the integrity number):
- Trade 1 — MARKET at 00:00 UK (instance anchor is 07:00 UK); entry = stated D-1 close 7,398.93 (slice cash close 7,400.60, Δ −1.67, consistent); stop = Fri low 7,340.2 − 0.25×ATR(19.0) = 7,321.2 (tighter than swing low 7,178.3 − 19.0; per §4c); R = 77.73 = 1.02×ATR(76) → 'wide stop' flag required by M5 §5.1 and absent; TP1 = +1R, TP2 = +2R, TP3 capped at 3×ATR — arithmetic correct; BE+0.2R on Unit-2 fill stated; invalidation (S1 7,358.92) is distinct from SL but sits inside the stop rather than "next structural level beyond SL"; single-source flag and CPI collision propagated. Mostly compliant; wide-stop flag missing; anchor deviation.
- Trade 2 — regime is TREND_UP but the card uses the RANGE geometry (buy limit at S1, stop at S2, TP1 at P). M5 §5.2b requires entry P+0.10×(R1−P), stop P−0.8×(P−S1), TPs R1/R1.5/R2, invalidation = daily close back through P. TP1 at +0.53R is an admitted override of the ladder. Invalidation is declared equal to the SL. All pivot tiers carry SINGLE-SOURCE-INDICATIVE → M5 §10 requires a SUPPRESSED row; the report overrides this citing a user instruction not in the fixed stack. Confluence arithmetic wrong (TP2 to R3 is 61.3 pts, not 21). Non-compliant.
- Trade 3A — swing endpoints logged (7,178.3 → 7,401.5, 223.2 pts ≥ 2×ATR, 5-session lookback: compliant). Entry at 38.2% retrace (7,316.24) instead of 57.5% (7,273.16 on the report's own swing); stop 5 pts below the 61.8% retrace instead of 0.25×ATR beyond the swing low (7,159.3 with ATR 76); TP1 should be the 38.2% level, TP2 the swing high (correct), TP3 an extension (138.2% given — acceptable); runner stop pull set to the midpoint of entry and swing LOW (7,247.27) whereas M5 §5.3a pulls to halfway between entry and TP2 (swing high); BE+0.2R on Unit-2 fill omitted (be_rule NONE); invalidation = SL at the 61.8% level instead of a daily close beyond the swing-low anchor. Non-compliant.

## 5. Data reconciliation log

Tolerances (brief §4): |Δ| ≤ 3 pts on a close, ≤ 8 pts on an open/high/low = consistent. Slice values are cash-session (16:30–23:00 broker) unless stated.

| # | Section / field | Report value | Slice value | Δ (report − slice) | Verdict |
|---|---|---|---|---|---|
| 1 | §6 Mon 04 May Close | 7,200.75 | 7,209.2 | −8.45 | Discrepancy (> 3) |
| 2 | §6 Tue 05 May Close | 7,259.22 | 7,265.8 | −6.58 | Discrepancy (> 3) |
| 3 | §6 Wed 06 May Close | 7,365.12 | 7,366.4 | −1.28 | Consistent |
| 4 | §6 Thu 07 May Close | 7,337.11 | 7,344.6 | −7.49 | Discrepancy (> 3) |
| 5 | §6/§1/§3/§4/§21b Fri 08 May Close (D-1) | 7,398.93 | 7,400.6 | −1.67 | Consistent |
| 6 | §6 Mon 04 May Open | 7,235.0 | 7,228.3 | +6.7 | Consistent |
| 7 | §6 Tue 05 May Open | 7,205.2 | 7,245.4 | −40.2 | Discrepancy (looks like prior close carried as open) |
| 8 | §6 Wed 06 May Open | 7,264.5 | 7,310.4 | −45.9 | Discrepancy |
| 9 | §6 Thu 07 May Open | 7,367.9 | 7,379.6 | −11.7 | Discrepancy |
| 10 | §6/§11 Fri 08 May Open (D-1) | 7,344.7 | 7,375.6 | −30.9 | Discrepancy |
| 11 | §6 Mon 04 May High | 7,240.5 | 7,248.8 | −8.3 | Discrepancy (marginal) |
| 12 | §6 Tue 05 May High | 7,265.8 | 7,278.1 | −12.3 | Discrepancy |
| 13 | §6 Wed 06 May High | 7,370.0 | 7,374.9 | −4.9 | Consistent |
| 14 | §6/§8 Thu 07 May High | 7,378.6 | 7,389.6 | −11.0 | Discrepancy |
| 15 | §6/§11 Fri 08 May High (D-1) | 7,401.5 | 7,407.5 | −6.0 | Consistent |
| 16 | §6/§7 Mon 04 May Low | 7,178.3 | 7,177.5 | +0.8 | Consistent |
| 17 | §6 Tue 05 May Low | 7,200.1 | 7,242.9 | −42.8 | Discrepancy |
| 18 | §6 Wed 06 May Low | 7,260.0 | 7,306.9 | −46.9 | Discrepancy |
| 19 | §6 Thu 07 May Low | 7,325.4 | 7,325.6 | −0.2 | Consistent |
| 20 | §6/§11/§21b Fri 08 May Low (D-1) | 7,340.2 | 7,371.8 (full-day 7,323.1) | −31.6 | Discrepancy — drives the Trade 1 stop and all daily pivots |
| 21 | §6 RSI2 column vs helper on slice closes | 66.6 / 100.0 / 79.1 / 68.8 / 89.4 | 44.85 / 70.14 / 100.00 / 82.19 / 71.98 | D-1: +17.4 | Discrepancy |
| 22 | §6 RSI2 column vs helper from the report's OWN closes | Tue 100.0 / Wed 79.1 / Thu 68.8 / Fri 89.4 | Tue 66.6 (using report's 7,230.12 prior close) / Wed 100.0 / Thu 79.1 / Fri 68.8 | column displaced one row; Fri +20.6 | FAIL — RSI2 does not reproduce (Category 3 failure, brief §4) |
| 23 | §6 Thu Trend label | Bearish | Rule: Close<Open & RSI2<50 → Bearish, else Neutral; RSI2 68.8 → Neutral | — | Discrepancy (rule misapplied) |
| 24 | §11 daily pivots from report's own H/L/C 7,401.5 / 7,340.2 / 7,398.93 | P 7,380.21 R1 7,420.22 S1 7,358.92 R2 7,441.51 S2 7,318.91 R3 7,481.52 S3 7,297.62 | Recomputed: identical to 0.01 | 0 | Reproduces |
| 25 | §11 daily pivots vs slice cash pivots | P 7,380.21 / R1 7,420.22 / S1 7,358.92 / S2 7,318.91 / R3 7,481.52 | P 7,393.30 / R1 7,414.80 / S1 7,379.10 / S2 7,357.60 / R3 7,450.50 | P −13.1; S1 −20.2; S2 −38.7; R3 +31.0 | Discrepancy (inherited from #10/#20) |
| 26 | §11 weekly pivot inputs — period | "prior week 28 Apr – 1 May 2026" | Prior week to D is 4–8 May 2026 | wrong week | Discrepancy (method) |
| 27 | §11 weekly pivot inputs H / L / C (27 Apr–1 May) | ≈7,250 / ≈7,079.6 / 7,230.12 | 7,276.6 / 7,112.4 / 7,233.3 | −26.6 / −32.8 / −3.2 | Discrepancy on H and L |
| 28 | §11 weekly pivots vs helper (4–8 May cash) | WP 7,186.57 WR1 7,293.55 WR2 7,356.97 | P 7,328.53 R1 7,479.57 R2 7,558.53 | WP −142.0 | Discrepancy — the "weekly R2 7,357 confluence" cited in §11/§15/§16/§21b Trade 2 does not exist on correct inputs |
| 29 | §11 monthly pivot inputs — April L | ≈5,760 | 6,471.7 (full-day 6,460.8) | −711.7 | Discrepancy (gross); April H 7,220 vs 7,226.7 and C 7,209 vs 7,213.7 consistent |
| 30 | §21b ATR(14) (implied from 19.0 = 0.25×ATR and 228 = 3×ATR) | 76.0 (never printed) | 70.36 cash / 76.88 full-day | −0.9 vs full-day | Consistent with full-day basis; figure must be stated |
| 31 | §7/§9 5-day swing endpoints | 7,178.3 / 7,401.5 | 7,177.5 / 7,407.5 | +0.8 / −6.0 | Consistent |
| 32 | §10/§19 VIX 8 May close (prev) | 17.19 (17.08) | 19.22 (19.08) | −2.03 (−2.00) | Discrepancy (VIX CFD basis may be futures-based; recorded, not scored as a close failure) |
| 33 | §10/§14/§19 USDX 8 May close | 97.84 | 97.841 | 0.00 | Consistent |
| 34 | §7 DXY weekly range | 97.83–98.28 | 97.591–98.569 (full-day) | narrower | Minor discrepancy |
| 35 | §1/§12/§13c NFP April | +115k vs +60k consensus; UR 4.3% | Calendar slice: 115.0 actual, 90.0 consensus, 178.0 prior; UR 4.3 | consensus −30k | Actual/UR consistent; consensus differs by source (unsourced in report) |
| 36 | §13c JOLTS | 6.87M | 6.866M | 0.00 | Consistent |
| 37 | §14 "May ISM Manufacturing prices index 84.6" | 84.6 | ISM Manufacturing Prices Paid 84.6 released 1 May 2026 (April data) | 0 | Figure consistent; month label wrong |
| 38 | §21b Trade 2 confluence "TP2 7,420.22 within 21 pts of daily R3 7,481.52" | 21 pts | 7,481.52 − 7,420.22 = 61.30 | +40.3 | Internal arithmetic error |
| 39 | §21b Trade 1 "TP1 7,476.66 clears daily R3 7,481.52 by ~5 pts" | "clears" | TP1 is 4.86 pts BELOW R3 | — | Internal wording/arithmetic contradiction |
| 40 | §7 "+168 pts above the Monday open" | 168 | 7,398.93 − 7,235.0 = 163.9 (168.8 is vs prior Fri close 7,230.12) | +4.1 | Minor internal inconsistency |
| 41 | §21a sentiment input vs §13b tilt | 0.55 (→ +0.083) | 0.56 (→ +0.084) | −0.01 | Minor internal inconsistency |
| 42 | §13d "Thu 15 May" | Thu | 15 May 2026 is a Friday | — | Date-label error |
| 43 | §21c Fri 8 May Trade 2 "partial fill near prior daily S1" | entry ~7,340 | S1 from report's own Thu H/L/C (7,378.6/7,325.4/7,337.11) = 7,315.47; Fri low 7,340.2 never reached it | +24.5 | Internal inconsistency (backtest row not reproducible) |
