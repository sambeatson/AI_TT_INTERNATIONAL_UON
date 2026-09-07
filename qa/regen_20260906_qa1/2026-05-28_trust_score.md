# Trust Score — 2026-05-28 — SP500_Daily_Report_28May2026.md

Run: regen_20260906_qa1 · D = 2026-05-28 · D-1 slice date = 2026-05-27 · Data basis: `data/slices/US500/US500_upto_2026-05-27.csv` (cash session 16:30–23:00 broker), helper `engine/qa_slice_stats.py`.

Helper anchors used throughout: D-1 (27 May) cash O 7531.0 / H 7536.0 / L 7504.3 / C 7528.5 · ATR14 (cash bars) 69.54 · daily pivots from D-1 cash P 7522.93, R1 7541.57, S1 7509.87, R2 7554.63, S2 7491.23, R3 7573.27, S3 7478.17 · weekly (18–22 May, cash) P 7441.33, R1 7543.57, S1 7373.47, R2 7611.43 · 5d swing H 7557.40 (25 May) / L 7394.10 (21 May) · 25d swing H 7557.40 / L 7050.70 (23 Apr).

Report anchors as stated: D-1 = 26 May (O 7480.65 / H 7539.09 / L 7471.20 / C 7519.12), RSI2 column 78.0 / 83.2 / 80.6 / 89.1 / 94.4, ATR(14) 48.58 (§21b only), daily P 7509.80 / R1 7548.41 / S1 7480.52 / R2 7577.69 / S2 7441.91 / R3 7616.30 / S3 7412.63, weekly P 7448.86 / R1 7509.51 / R2 7545.56 / R3 7606.21, direction score +0.71 LONG, regime Trending Up — Strong (KER agrees), three cards produced, none suppressed.

## 1. Section 7 checklist

| Item | Reviewer notes | Evidence observed | Score 0–5 | Action required |
|---|---|---|---|---|
| 1.1 Variables respected | Asset (S&P 500 cash), counters USDX·VIX·DAX 40 in that order, 5-session lookback, USD/points/0.01 tick, six price-evidence sources and the 07:00 UK anchor are all honoured. The as-of variable is not: the report's "latest official cash close" is Tue 26 May (D-2). The run timestamp is 27 May 21:00 UK (= 16:00 ET) and the report itself cites the completed 27 May session (§13a "Dow sets new record close", §12 gold −1.56% on 27 May), yet no 27 May row exists in §6/§8/§11. | §2 as-of table; §3 "Tue 26 May 2026"; §20 run timestamp; §13a row 2 | 2 | Rebuild §6/§8/§11/§21 on the 27 May session as D-1. |
| 1.2 Coverage & currency consistent | Data window is one session stale (19–26 May instead of 20–27 May). Event dates conflict internally: §1/§10/§12/§14/§16 say "Thursday 29 May" PCE while §13d labels 29 May "Fri" (29 May 2026 is a Friday); §12 says "Q2 2026 GDP second estimate (also Thursday)" while §13d says Q1 GDP on 28 May Thu; §12 says PCE is "pre-market on the 28 May report-date session" and "released Thursday 29 May" in the same sentence. The calendar slice schedules Core PCE m/m, GDP q/q, claims, durable goods and personal income/spending all at 28 May 15:30 broker (08:30 ET, D pre-open). No currency/unit drift. | §1 lines 21–25, §12 "Near-term catalysts", §13d table, §16, §17 | 1 | Correct the event calendar to the slice: PCE/GDP/claims/durables/income all 28 May 08:30 ET. Add the 27 May session. |
| 1.3 Audience & tone | Senior-strategist register, no retail tone; a few garbled sentences (§1 "pre-released ahead of US markets opening on the report date"). | §1, §18 | 4 | Tidy §1 sentence. |
| 2.1 Sections present & ordered | All 21 sections present in the prescribed order; §13a–d, §21a–d all present; limitations boilerplate present in §21d. | Headings 1–21 | 5 | None. |
| 2.2 Scorecard as a table | §6 has Date/O/H/L/C/RSI2/Source A/Source B/Validation/Trend. §11 daily/weekly/monthly tables are ordered high→low but carry R5…S5 (five levels each side) rather than the R3→P→S3 three-level layout; the R3–S3 subset is present and correctly ordered. | §6, §11 | 4 | Trim §11 to R3–S3 or state the R4/R5 formula. |
| 2.3 Method steps visible | §4→§5 show observation, classification, consensus. §8 is candle-by-candle with a sequence assessment. §9 gives overlap 0.18, persistence 22/25, VOLator slope −0.20 and the comparative-vol table. §7 shows five pandoc image placeholders (accepted as evidence of charts). Minor internal slips: §8 says 21 May body 0.46 (own numbers give 0.54); §8 "each session's low (excl. 19 May) held above the prior open" fails for 21 May (L 7421.40 < 20 May O 7424.10). | §4–§9 | 4 | Fix the two §8 slips. |
| 3.1 Quantitative claims sourced | §1 numbers trace to §6/§13. §12 carries unsourced figures: NASDAQ 26,656.18, Russell 2,920.54, WTI ~$94, gold $4,464 (−1.56%), 84% beat rate, 27.5% EPS growth, Polymarket distribution. §14 VIX 16.92 traces to §19 (Yahoo/FRED). | §12 Supply/Substitution/Macro paragraphs | 2 | Attach a source and date to each §12 figure or point to §13. |
| 3.2 Citations exist & contain data | Three spot-checks: (a) FRED SP500 22 May 7,473.47 — reused identically in §4 and §6, and within 2.2 pts of the slice cash close 7475.7: consistent. (b) Barchart 22 May "consumer sentiment revised to a record low" — calendar slice shows Michigan sentiment 44.8 vs 48.2 consensus on 22 May, matching §13c/§14 (44.8, 1-yr expectations 4.8%): consistent. (c) TheStreet 26 May "Conference Board confidence eased 0.7 to 93.1, beat consensus 92" — calendar slice: actual 93.1, consensus 99.7, previous 92.8, i.e. a rise of 0.3 and a miss, not a beat: figure/quote mismatch. Also the Goldman 8,000 target is dated 26 May in §3/§12/§13c but 27 May in §13a. No source is impossible on its face; none is judged fabricated. | §4 rows 4; §13a rows 4–6; §13c | 3 | Reconcile the CB confidence figures and the Goldman article date. |
| 3.3 Calculations transparent | RSI2 does NOT reproduce. From the report's own five closes the helper gives 98.4 / 98.7 / 100.0 for 21, 22, 26 May against the stated 80.6 / 89.1 / 94.4 (the 21 May row: gain 22.25, loss 0.36 → RS 61.8 → RSI2 98.4). The Trend rule is misapplied on 21 May (Close 7445.74 > Open 7445.20 and RSI2 > 50 → Bullish, labelled Neutral). Daily pivots reproduce exactly from the report's own 26 May H/L/C; weekly pivots reproduce from the 19–22 May rows. ATR(14) is stated only in §21b, not in §9. KER: threshold +0.13 given, no value. §21a contributions sum to +0.71. | §6 RSI2 column, §11, §9, §21a; helper output | 1 | Recompute RSI2 with RS = mean gain / mean loss over 2 periods and show the arithmetic; re-label Trend; state ATR(14) and the KER value in §9. |
| 3.4 Numbers reconcile | D-1 close 7,519.12 is identical in §1/§3/§4/§6 and the Trade 1 reference (7,519) — but it is the 26 May close, 9.38 pts from the slice D-1 cash close 7528.5, and the true D-1 session is absent. Against the slice basis: 19 May close +61.55 pts, 19 May low +49.1, 20 May O/L +44.2, 26 May O −42.15 / L −34.3 (see §5 log). Card arithmetic: Trade 3A "39.9-point swing" is 98.99 from its own endpoints and 7,495 is a 44.5% retrace, not 38.2%; Trade 2 stop 7,479 described as "below the 26 May low 7,471.20 by 8.20" is 7.80 above it; Trade 1 R stated 47.92 vs 7519 − 7471.20 = 47.80; §21d aggregate mean +1.71R recomputes to +1.76R and TP2 hits 5/9 not 6/9. Pivots §11 = cards ✓; RSI2 §6 = §8 = §21a ✓; ATR §21b = 48.58 vs slice 69.54. | §6 vs slice; §21b; §21d | 1 | Rebuild §6 from the data basis; fix the card arithmetic listed. |
| 4.1 Pillars conclude | §8 "Bullish continuation", §9 "Bias: Bullish", §10 per-counter confirmation status, §12 sub-paragraphs each end with a read; §14 ends with an asymmetric-risk watch item rather than a direction label. | §8–§14 | 4 | Add a direction label to §14. |
| 4.2 Peer/cross-asset interpreted | Mechanisms are given (earnings translation/FCI for USDX, hedge demand for VIX, common risk factor for DAX). The VIX narrative (16.59 → 16.92, "bounced" into the new high, "divergence") is contradicted by the slice (cash closes 18.06 → 17.72 → 17.18, falling); the USDX "gave back the gain on Friday 22 May" is contradicted (close 99.237 → 99.344, up). Levels differ by ~1.5 VIX pts (basis) but the directional claims fail. | §10, §14, §20 anomalies | 3 | Re-derive VIX/USDX 5-session direction from dated closes. |
| 4.3 Synthesis reconciles tensions (incl. card construction) | §15/§16/§18 address the extreme-RSI vs trend tension and the PCE event; KER vs regime and §17 vs §21a are consistent. Card construction diverges from the M5 rules: Trade 1 TP ladder uses pivots (TP1 = 0.61R) instead of entry ± 1R/2R, stop has no 0.25×ATR buffer, break-even moved on TP1 rather than Unit 3 stop → entry+0.2R on the Unit 2 fill, no session-close/3×ATR runner rule; Trade 2 is built as a range-style retest limit at P under a TREND regime instead of P + 0.10×(R1−P) with stop P − 0.8×(P−S1) and TPs R1/R1.5/R2; Trade 3A uses a "38.2%" entry (M5: 57.5%), a stop under the 26 May low instead of 0.25×ATR beyond the 0% anchor, a swing spanning 2 sessions (22→26 May) against the 4–10 session lookback, and extension levels that do not match their own labels. §9's "avoid chasing into extreme RSI" is not reconciled with a Trade 1 market buy at RSI2 94.4 beyond a sizing cut. | §21b all three cards; §9 protocol paragraph | 2 | Rebuild the three cards to the M5 rules (see feedback file). |
| 4.4 Calibrated language | §17 is one sentence but stacks three conditional outcomes and a date at odds with §13d. Confidence stated High in §3 and Medium-High in §18 — inconsistent. | §3, §17, §18 | 3 | Align confidence across §3/§18; simplify §17. |
| 5.1 Data dated; staleness flagged | Every price and article is dated; 19–22 May H/L flagged single-source-indicative in §6/§19; monthly tier flagged. The one-session staleness (27 May closed at run time, not tabulated) is not flagged anywhere — it is presented as current. | §6 note, §19, §20 | 2 | Either tabulate 27 May or flag the report as stale. |
| 5.2 Assumptions up front | Anchor caveat on the Trade 1 card ("Reference price 7,519 (prior cash close) ± futures-implied open") and in §20 ("anchor confirmed at 07:00 UK"); single-source pivot propagation to Trade 2 caveat; corroboration waiver documented in §19/§20. | §21b Trade 1, §19, §20 | 4 | State the proxy-open rule more precisely. |
| 5.3 Red flags surfaced | §12/§15 risks are concrete. The §13d collision is mis-timed: the slice calendar puts Core PCE, GDP 2nd est., claims, durables and income/spending at 08:30 ET on D (28 May), before the cash open, whereas the report puts PCE on 29 May and the Trade 1 caveat only tightens "if not closed by 28 May NY close". The event therefore lands inside every card's holding window without a caveat. | §13d, §21b caveats | 2 | Carry the 28 May 08:30 ET release cluster into all three card caveats. |
| 5.4 Restrictions honoured | No bracketed variable names, no M1–M5 module codes, no framework name; instrument common names used; ES futures directional-only; no retail CFD quotes in the OHLC basis. Internal identifiers do leak ("DataCorroborationError", "TREND_UP regime → 3A active", "Simultaneous long/short policy YES", "Tier 3 since 2025 demotion", "weights locked… forward-test deployment per protocol"). §19 states "No fields were synthesised" while §11/§19 describe the monthly pivots as derived from a "constructed April 2026 H/L/C set" that is then used for Trade 1 TP2 (monthly R3) — disclosed and flagged, so not treated as a breach. The 19 May row (close +61.55 vs basis) is labelled "Close corroborated" by two sources; cannot be proven synthesised, treated as a Category 3 failure. | §20, §21b Trade 3A, §19, §6 | 3 | Remove internal identifiers; reconcile the "no synthesis" statement with the constructed monthly set. |

## 2. Category roll-up

| Category | Level | Multiplier | Points | Justification |
|---|---|---|---|---|
| C1 Prompt adherence (max 20) | 2 | 0.40 | 8.00 | Rows 1.1–1.3 = 2, 1, 4 → mean 2.33 → 2. As-of variable (NY close of D-1) not met; window one session stale; event dates internally inconsistent. |
| C2 Structure (max 20) | 4 | 0.85 | 17.00 | Rows 2.1–2.3 = 5, 4, 4 → mean 4.33 → 4. All sections present and ordered; pivot tables over-extended; minor §8 slips. |
| C3 Accuracy & evidence (max 25) | 2 | 0.40 | 10.00 | Rows 3.1–3.4 = 2, 3, 1, 1 → mean 1.75 → 2. RSI2 not reproducible from own closes; 19 May close 61.55 pts off basis; D-1 session missing; several card arithmetic errors. |
| C4 Reasoning & judgment (max 20) | 3 | 0.65 | 13.00 | Rows 4.1–4.4 = 4, 3, 2, 3 → mean 3.00 → 3. Pillars conclude and mechanisms are given; VIX/USDX direction claims contradicted; cards depart from M5 construction rules. |
| C5 Currency, restrictions & transparency (max 15) | 3 | 0.65 | 9.75 | Rows 5.1–5.4 = 2, 4, 2, 3 → mean 2.75 → 3. Staleness unflagged; PCE collision mis-timed; internal identifiers leak; assumptions otherwise documented. |
| **Total** | | | **57.75 → 58** | |

## 3. Total, band, override check

- Total: **58/100**
- Band: **Low** (40–59)
- Overrides: **none**. Fabricated-source check: the three spot-checked sources are named, dated and reuse their figures consistently (one figure mismatch on the CB confidence article, one date inconsistency on the Goldman article); nothing is impossible on its face, so no hallucinated-source cap. Restriction-breach check: no module codes, bracketed variable names or framework name; the "constructed" monthly H/L/C set is disclosed and flagged indicative; the 19 May OHLC row is far off the data basis but is scored as the brief's Category 3 failure rather than proven synthesis. No cap applied; the total already sits in Low.

## 4. Card Integrity

Lint rows (`qa/regen_20260906_qa1/lint_static/2026-05-28.csv`, verbatim):

| card_id | report_date | strategy | flags | dud |
|---|---|---|---|---|
| 2026-05-28_Trade_1 | 2026-05-28 | Trade 1 - Daily Directional | CLEAN | False |
| 2026-05-28_Trade_2 | 2026-05-28 | Trade 2 - Pivot (daily P / weekly R1 retest) | CLEAN | False |
| 2026-05-28_Trade_3A | 2026-05-28 | Trade 3A - Momentum-Pullback | CLEAN | False |

Per-card integrity (100 − 40·#DUD − 10·#WARN, floor 0):

| Card | #DUD | #WARN | Integrity |
|---|---|---|---|
| 2026-05-28_Trade_1 | 0 | 0 | 100 |
| 2026-05-28_Trade_2 | 0 | 0 | 100 |
| 2026-05-28_Trade_3A | 0 | 0 | 100 |

Report-level Card Integrity (mean over 3 non-suppressed cards): **100.0**. Suppressed cards: none. Note: the integrity number reflects the static linter only; the M5 construction defects are scored under row 4.3 and listed in the feedback file.

## 5. Data reconciliation log

Tolerances (brief §4): close |Δ| ≤ 3 consistent; open/high/low |Δ| ≤ 8 consistent; close |Δ| > 10 or non-reproducing RSI2 = Category 3 failure. Slice values are cash-session (16:30–23:00 broker) from the helper and a direct read of the same slice for 19–20 May.

| # | Section | Field | Report value | Slice value | Delta | Verdict |
|---|---|---|---|---|---|---|
| 1 | §6 19 May | Open | 7405.40 | 7371.0 | +34.40 | Discrepancy |
| 2 | §6 19 May | High | 7430.55 | 7399.8 | +30.75 | Discrepancy |
| 3 | §6 19 May | Low | 7388.20 | 7339.1 | +49.10 | Discrepancy |
| 4 | §6 19 May | Close | 7423.85 | 7362.3 | +61.55 | **FAIL** (> 10 pts) |
| 5 | §6 20 May | Open | 7424.10 | 7379.9 | +44.20 | Discrepancy |
| 6 | §6 20 May | High | 7461.80 | 7443.0 | +18.80 | Discrepancy |
| 7 | §6 20 May | Low | 7406.50 | 7362.3 | +44.20 | Discrepancy |
| 8 | §6 20 May | Close | 7446.10 | 7436.8 | +9.30 | Discrepancy (> 3, < 10) |
| 9 | §6 21 May | Open | 7445.20 | 7408.6 | +36.60 | Discrepancy |
| 10 | §6 21 May | High | 7458.30 | 7471.8 | −13.50 | Discrepancy |
| 11 | §6 21 May | Low | 7421.40 | 7394.1 | +27.30 | Discrepancy |
| 12 | §6 21 May | Close | 7445.74 | 7450.3 | −4.56 | Discrepancy (> 3) |
| 13 | §6 22 May | Open | 7446.05 | 7482.5 | −36.45 | Discrepancy |
| 14 | §6 22 May | High | 7484.90 | 7509.2 | −24.30 | Discrepancy |
| 15 | §6 22 May | Low | 7440.10 | 7464.5 | −24.40 | Discrepancy |
| 16 | §6 22 May | Close | 7473.47 | 7475.7 | −2.23 | Consistent |
| 17 | §6 26 May | Open | 7480.65 | 7522.8 | −42.15 | Discrepancy |
| 18 | §6 26 May | High | 7539.09 | 7543.5 | −4.41 | Consistent |
| 19 | §6 26 May | Low | 7471.20 | 7505.5 | −34.30 | Discrepancy |
| 20 | §6 26 May | Close | 7519.12 | 7527.5 | −8.38 | Discrepancy (> 3, < 10) |
| 21 | §6 / §8 / §11 | D-1 session (27 May) | absent | O 7531.0 H 7536.0 L 7504.3 C 7528.5 | n/a | **FAIL** — D-1 session not tabulated; report treats 26 May as D-1 |
| 22 | §1, §3, §4, §21b | D-1 close used as reference | 7519.12 (26 May) | 7528.5 (27 May cash) | −9.38 | Discrepancy — wrong session |
| 23 | §6 RSI2 | 21 / 22 / 26 May | 80.6 / 89.1 / 94.4 | from report's own closes: 98.4 / 98.7 / 100.0 | −17.8 / −9.6 / −5.6 | **FAIL** — does not reproduce from own closes |
| 24 | §6 RSI2 | vs slice cash closes (21, 22, 25, 26, 27 May) | 80.6 / 89.1 / — / 94.4 / — | 100.00 / 100.00 / 100.00 / 75.34 / 3.82 | sessions differ | Not comparable session-for-session; recorded for completeness |
| 25 | §6 Trend | 21 May | Neutral | rule (C>O, RSI2>50) → Bullish | — | Rule misapplied |
| 26 | §11 daily pivots | reproduction from report's own 26 May H/L/C | P 7509.80 R1 7548.41 S1 7480.52 R2 7577.69 S2 7441.91 R3 7616.30 S3 7412.63 | recomputed 7509.80 / 7548.41 / 7480.52 / 7577.69 / 7441.91 / 7616.30 / 7412.63 | 0.00 | Reproduces |
| 27 | §11 daily pivots | vs slice D-1 (27 May) cash pivots | P 7509.80 / R1 7548.41 / S1 7480.52 / R2 7577.69 / S2 7441.91 / R3 7616.30 / S3 7412.63 | P 7522.93 / R1 7541.57 / S1 7509.87 / R2 7554.63 / S2 7491.23 / R3 7573.27 / S3 7478.17 | −13.13 / +6.84 / −29.35 / +23.06 / −49.32 / +43.03 / −65.54 | Discrepancy — built on the wrong session |
| 28 | §11 weekly pivots | reproduction from own 19–22 May rows (H 7484.90, L 7388.20, C 7473.47) | P 7448.86 R1 7509.51 R2 7545.56 | recomputed 7448.86 / 7509.51 / 7545.56 | 0.00 | Reproduces (18 May excluded from the week) |
| 29 | §11 weekly pivots | vs slice prior-week cash pivots | P 7448.86 / R1 7509.51 / S1 7412.81 / R2 7545.56 | P 7441.33 / R1 7543.57 / S1 7373.47 / R2 7611.43 | +7.53 / −34.06 / +39.34 / −65.87 | Discrepancy (weekly H/L basis) |
| 30 | §11 monthly pivots | internal consistency | P 7206.95, R1 7351.81, S1 7127.81, R2 7430.95 | implies H 7286.09, L 7062.09, C 7272.67; R2 check 7206.95 + 224.00 = 7430.95 | 0.00 | Internally consistent; flagged indicative (slice 25d low 7050.70 on 23 Apr) |
| 31 | §21b (Trade 1) | ATR(14) | 48.58 | 69.54 (cash bars); 78.06 (full day) | −20.96 | Discrepancy (−30%) |
| 32 | §10 / §14 | VIX 22 May close | 16.59 | 18.06 | −1.47 | Discrepancy (basis) |
| 33 | §10 / §14 | VIX 26 May close | 16.92 | 17.72 | −0.80 | Discrepancy (basis) |
| 34 | §10 / §20 | VIX direction 22→26 May | "bounced" (rising) | 18.06 → 17.72 (→ 17.18 on 27 May), falling | — | Discrepancy — direction contradicted |
| 35 | §10 | USDX 22 May | "gave back the gain" | close 99.237 → 99.344 (+0.107) | — | Discrepancy — direction contradicted |
| 36 | §10 | USDX 5-session direction | Rising, modest | 20 May 99.115 → 27 May 99.211 (+0.096) | — | Consistent |
| 37 | §13a / §13c | CB Consumer Confidence 26 May | 93.1, "eased 0.7", "beat consensus 92" | 93.1 actual, consensus 99.7, previous 92.8 | level 0.00; change/consensus differ | Discrepancy — figure matches, narrative does not |
| 38 | §13c / §14 | Michigan sentiment 22 May / 1-yr expectations | 44.8 / +4.8% | 44.8 / 4.8 | 0.00 | Consistent |
| 39 | §1, §12, §13d, §14, §16 | Core PCE release date | 29 May ("Thursday 29 May"; §13d "29 May Fri") | 2026-05-28 15:30 broker = 28 May 08:30 ET (D, pre-open) | one session | **Discrepancy** — event mis-dated; 29 May 2026 is a Friday |
| 40 | §12 vs §13d | GDP second estimate | §12 "Q2 2026 GDP (also Thursday)" | §13d "Q1 2026 GDP 28 May Thu"; slice GDP q/q 28 May 08:30 ET | — | Internal inconsistency |
| 41 | §13d | Personal income & spending | 29 May | slice 28 May 08:30 ET | one session | Discrepancy |
| 42 | §21b Trade 3A | swing magnitude | "39.9-point swing" | own endpoints 7539.09 − 7440.10 = 98.99 | −59.09 | Internal arithmetic error |
| 43 | §21b Trade 3A | entry level | 7495.00 "38.2% retracement" | 38.2% = 7501.28; 61.8% = 7477.91; 7495 = 44.5% | −6.28 vs 38.2% | Internal arithmetic error |
| 44 | §21b Trade 3A | TP2 "138.2% extension" / TP3 "161.8%" | 7567.00 / 7597.00 | 7576.90 / 7600.27 | −9.90 / −3.27 | Internal arithmetic error |
| 45 | §21b Trade 2 | stop vs 26 May low | "below the 26 May low 7,471.20 by 8.20" | 7479.00 is 7.80 above 7471.20 | — | Internal error |
| 46 | §21b Trade 1 | R | 47.92 | 7519 − 7471.20 = 47.80 (cards JSON 47.8) | +0.12 | Minor |
| 47 | §21d | aggregate mean R / TP2 hit rate | +1.71R / 6 of 9 | (7.8 + 4.3 + 3.7)/9 = +1.76R / 5 of 9 from §21c | −0.05R / +1 | Internal arithmetic error |
| 48 | §8 | 21 May body; low-vs-prior-open claim | 0.46; "every low (excl. 19 May) held above prior open" | 0.54; 21 May L 7421.40 < 20 May O 7424.10 | — | Minor internal slips |
