# Trust Score v3.7 — FTSE 100 daily report, D = 2026-07-14 (run ftse_qa1)

Report: `reports/md/FTSE_EuroStoxx_Report_14Jul2026.md`. Level file `data/levels/UK100_by_date/2026-07-14.csv` has `last_bar_date=2026-07-13` < D (checked); slice last bar 2026-07-13 22:45 broker. Review used the CFD-derived slice, so the report's cash-basis figures are compared to both `_cash` and `_full` fields (brief §4 tolerances: close ±5, O/H/L ±10).

## Score line
c1=3
c2=4
c3=2
c4=3
c5=3
total=63
band=Moderate
override=none
card_integrity=100
n_cards=3
n_duds=0
n_warns=0

(`n_cards=3` counts the three linter rows; Trade 1 is SUPPRESSED and not scored, so Card Integrity is the mean over the 2 non-suppressed cards.)

## 1. Section 7 checklist

| Row | Notes | Evidence (location) | Score |
|---|---|---|---|
| 1.1 Variables respected | FTSE 100 cash primary, Euro Stoxx 50 reference only and carries no card; USDX/S&P 500/DAX counters present; 5/25-session lookbacks; GBP points; 9 sources attempted. Daily-open anchor overridden 07:00 to 00:00 UK "per analyst instruction" (disclosed, but a deviation from the 07:00 standard). Report's D-1 close basis is stated as cash close. The §2 currency cell has a stray bracket ("native EUR)"). | §2 note, §20, §4 | 3 |
| 1.2 Coverage & currency consistent | Dates are D-1 and earlier for data. Drift points: (a) UK CPI is dated "Wed 16 Jul" and Eurozone CPI "Thu 17 Jul", but 16 Jul 2026 is a Thursday and 17 Jul a Friday; the "14–18 Jul" window ends on a Saturday (§1, §12, §13d, §15, §16, §18, §21b). (b) §3 cites an "Asian-session risk tone (Nikkei −1.9%)" as an input to the 14 Jul open; if that is the 14 Jul Asian session it post-dates the D-1 as-of cut. (c) §13d omits the scheduled D events listed in the calendar slice (see 5.3). | §3, §13d | 3 |
| 1.3 Audience & tone | Senior strategist tone, trading/risk use. One garbled token in §13d ("Confirms/638 disputes"). | §1, §13d, §18 | 4 |
| 2.1 Sections present & ordered | §1–§21 all present in order, §13a–d, §21a–d present, §17 a single sentence. §21c collapses Trade 2 and 3C into one aggregate row each instead of per-session rows. | headings | 4 |
| 2.2 Scorecard as table | §6 is a table but has no "Final" column and merges Source A/B. §11 pivots are tables, but daily is laid out as two side-by-side columns (R5..R1 next to P..S5) rather than one R3→P→S3 ladder, and the monthly table has only R2/R1/P/S1/S2 (no R3/S3), against 3 levels each side. | §6, §11 | 3 |
| 2.3 Method steps visible | §4→§5 observations to consensus; §8 candle-by-candle plus sequence; §9 regime with overlap/persistence/VOLator/KER. §7 has five chart headings with no images (pandoc drop; accepted as placeholder). §7 note says the counter volatility curves are "illustrative overlays". | §4–§9 | 4 |
| 3.1 Quantitative claims sourced | §1 and the card numbers point to §4/§6/§11. §10, §12, §14 figures carry no source or date: DAX ~24,917 and −0.6%, S&P −0.79%, Dollar Index ~99–100, VIX ~15–17, Brent $75.86/$79.4, US 10-yr 4.61%, GBP $1.34, "~15% energy weight". Several conflict with the slice (3.4/Cat 3 detail). | §10, §12, §14 | 2 |
| 3.2 Citations exist & consistent | Three spot checks: BBN Times 13 Jul 17:00 close 10,498.29 (used consistently in §1/§3/§4/§6); Share Talk 13 Jul 17:28 "+1.00 pt" (consistent with 10,497.29→10,498.29); Sharecast 10 Jul 17:05 "10,497 (+25)" (consistent with 10,472.45→10,497.29). None is self-contradictory on its face, so no fabrication is established. Weaknesses: §4 prints "Investing.com … 10,498.05 (open)" in the Close column; §4 states a 0.29 delta is "within the ±0.10 tolerance"; §6 claims "CORROBORATED (Δ≈0.0)" for 7–9 Jul with no §4 evidence rows for those dates. | §4, §6 | 3 |
| 3.3 Calculations transparent | RSI2 of 10 Jul is 78.5 in §6 and ~78 in §8, but the report's own closes (10,489.04, 10,472.45, 10,497.29) give 60.0 (mean gain 12.42 / mean loss 8.295). 9 Jul shows 2.0, the report's own closes give 0.0. 13 Jul (100.0) reproduces. §13b tilt arithmetic: the stated Σw·s = −1.70 and Σw = 3.9 give −0.436, not the printed −0.10. ATR(14) is never stated as a number; the cards imply ~92–93 (69 pts = "0.74 ATR"; 0.25 ATR "~23") and §21c implies ~94–100, against slice ATR14 117.8 (cash) / 128.4 (full). KER = −0.20 is not reproducible (see Cat 3 detail). Pivot formulas reproduce from the report's own H/L/C. §21a composite sums to +0.18 only with unrounded terms (printed terms sum to +0.17). | §6, §8, §9, §13b, §21 | 2 |
| 3.4 Numbers reconcile | D-1 close 10,498 is identical in §1/§3/§4/§6/§11. Breaks: card TP1 "daily R3 10,602" vs §11 R3 10,599; ATR implied differently on the cards (~93) and §21c (~94–100); 7 Jul read in §8 ("closing 14 points higher … close in the upper half of range") contradicts §6 (open 10,679.03 > close 10,665.30; close at 38% of range; Trend Bearish); §21c and §21d mix "R" and "ATR" units. Monthly/weekly pivot inputs reconcile internally but not to the slice (below). | cross-section | 2 |
| 4.1 Pillars conclude | §8 "Indecision", §9 Neutral/Transitional, §10 net risk-off contradiction flag. §12 and §14 end without a direction label (§12 ends on a catalyst list; §14 on a watch item). | §8–§14 | 3 |
| 4.2 Cross-asset interpreted | Mechanisms given (energy weighting vs DAX, dollar-earner translation, risk beta). But the S&P 500 is labelled "Falling" over five days while the slice shows 7 Jul close 7,502.5 → 13 Jul 7,510.2 (flat/up; only 13 Jul fell, −0.92%), and the Dollar Index level is misquoted (slice 101.31, not ~99–100). | §10 | 4 |
| 4.3 Synthesis reconciles tensions | §21a gives short-term technical +1.0×0.25 = +0.25 while §8 concludes "Indecision" and flags RSI2 = 100 as whipsaw-prone. §21a dismisses the sign conflict between a +0.18 score and the bearish-skew §17/§16 as "no material conflict". Both cards are LONG while §17/§15/§18 lean mildly bearish. KER-vs-drift tension is addressed, but on an incorrect KER sign. | §8, §17, §21a | 3 |
| 4.4 Calibrated language | §17 is one sentence; confidence Medium stated (§3, §18). The §17 sentence is long but not hedge-stacked. | §3, §17 | 4 |
| 4.x Card construction (protocol Cat 4) | Trade 1 suppressed correctly (|0.18| < 0.25). Trade 2: stop buffer is 1 pt (S1 10,465 → 10,464) versus the required 0.25×ATR14 (≈29.5 pts); R/ATR mis-stated (69/117.8 = 0.59, not 0.74); TP3 is a range, not a price; no anchor time. Trade 3C: R = 396 pts = 3.36×ATR14 (cap 3.0×); TP1 = 598 pts from entry = 5.1×ATR14 (cap 2.5×); no R or point distances on the card; inputs (swing 10,749/10,128, ATR ~92) differ from the slice (10,739.6/10,126.2, ATR 117.8). Both cards are statically clean per the linter. | §21b | 2 |
| 5.1 Data dated; staleness flagged | Prices and articles dated; single-source flags on 7 Jul H/L and all Euro Stoxx rows; counter-curve overlay flagged as illustrative. Weekday labels wrong (1.2). | §4, §6, §7, §19 | 4 |
| 5.2 Assumptions up front | Anchor override stated in §2 and §20. Neither card states an anchor or clock time (linter notes "No clock time stated"), and the §21a note on the analyst directive about corroboration is not carried onto the cards. | §2, §20, §21b | 3 |
| 5.3 Red flags surfaced | UK CPI and oil/Hormuz are surfaced and carried into both card caveats. The calendar slice lists HIGH events on D that are missing from §13d and the cards: US CPI (13:30 UK; y/y consensus 3.8, prior 4.2; m/m 0.5), BoE Governor Bailey speeches (09:45 and 15:00 UK), ECB Lagarde speech (14:00 UK). These fall inside the Trade 2 and 3C holding window. | §13d, §21b | 3 |
| 5.4 Restrictions honoured | No retail CFD quote presented as the OHLC basis; FTSE futures confirmation-only; Euro Stoxx carries no card. Minor leaks of internal pipeline jargon into a client report: "SurfaceContract RANGE / SurfaceContractError", "v2.1 baseline", "20-session lock", "Source Discipline protocol §4–5" (§20). No M1..M5 codes or bracketed variable names. "Corroborated" is applied to rows with no evidence in §4. No override triggered. | §20, §6 | 3 |

## 2. Category roll-up

| Cat | Rows | Mean | Level | Multiplier | Points | Justification |
|---|---|---|---|---|---|---|
| 1 Prompt adherence (20) | 3,3,4 | 3.33 | 3 | 0.65 | 13.00 | Variables mostly respected; 00:00 anchor override disclosed; weekday/date drift on the headline catalyst. |
| 2 Structure (20) | 4,3,4 | 3.67 | 4 | 0.85 | 17.00 | All 21 sections and sub-sections ordered; §6/§11 table layouts incomplete. |
| 3 Accuracy & evidence (25) | 2,3,2,2 | 2.25 | 2 | 0.40 | 10.00 | See Category 3 detail: 11 of 20 OHLC fields outside tolerance on both bases, one close off by 15.45, monthly pivots wrong by up to 193 pts, RSI2/KER/tilt not reproducible. |
| 4 Reasoning (20) | 3,4,3,4,2 | 3.20 | 3 | 0.65 | 13.00 | Good mechanisms and a coherent regime story; short-tech signal vs §8 label, wrong KER sign, both cards LONG against bearish skew; card construction defects. |
| 5 Currency & transparency (15) | 4,3,3,3 | 3.25 | 3 | 0.65 | 9.75 | Dated and flagged; D-day HIGH events omitted; anchor not on cards; jargon leak. |

## 3. Total, band, override
Total = 13.00 + 17.00 + 10.00 + 13.00 + 9.75 = 62.75, rounded to **63**, band **Moderate** (60–74). Override check: no fabricated source established (3.2 spot checks internally consistent; sources cannot be fetched), so no hallucinated-source cap; no openly violated prompt restriction, so no restriction cap. `override=none`. The Moderate band follows from the total itself.

## 4. Category 3 detail (D-1 = Mon 13 Jul 2026)

### 4a. Report §6 vs slice (points; Δ = report − slice). "Out" = outside tolerance versus BOTH the cash and the full-day basis.

| Date | Field | Report | Cash | Δ cash | Full | Δ full | Status |
|---|---|---|---|---|---|---|---|
| 7 Jul | O | 10,679.03 | 10,657.8 | +21.2 | 10,653.8 | +25.2 | Out |
| 7 Jul | H | 10,704.10 | 10,739.6 | −35.5 | 10,739.6 | −35.5 | Out |
| 7 Jul | L | 10,641.80 | 10,639.1 | +2.7 | 10,631.9 | +9.9 | ok |
| 7 Jul | C | 10,665.30 | 10,680.1 | −14.8 | 10,650.5 | +14.8 | Out |
| 8 Jul | O | 10,665.30 | 10,634.1 | +31.2 | 10,638.9 | +26.4 | Out |
| 8 Jul | H | 10,672.50 | 10,636.3 | +36.2 | 10,674.1 | −1.6 | ok (full) |
| 8 Jul | L | 10,470.20 | 10,454.7 | +15.5 | 10,454.7 | +15.5 | Out |
| 8 Jul | C | 10,489.04 | 10,457.0 | +32.0 | 10,492.6 | −3.6 | ok (full) |
| 9 Jul | O | 10,489.04 | 10,439.2 | +49.8 | 10,492.0 | −3.0 | ok (full) |
| 9 Jul | H | 10,505.80 | 10,468.9 | +36.9 | 10,514.2 | −8.4 | ok (full) |
| 9 Jul | L | 10,420.30 | 10,380.4 | +39.9 | 10,380.4 | +39.9 | Out |
| 9 Jul | C | 10,472.45 | 10,457.0 | **+15.5** | 10,457.0 | **+15.5** | Out (>15) |
| 10 Jul | O | 10,471.94 | 10,490.1 | −18.2 | 10,461.6 | +10.3 | Out (marginal) |
| 10 Jul | H | 10,513.90 | 10,504.8 | +9.1 | 10,537.3 | −23.4 | ok (cash) |
| 10 Jul | L | 10,462.75 | 10,451.1 | +11.7 | 10,438.8 | +24.0 | Out |
| 10 Jul | C | 10,497.29 | 10,487.2 | +10.1 | 10,522.4 | −25.1 | Out |
| 13 Jul | O | 10,498.05 | 10,488.1 | +10.0 | 10,498.1 | 0.0 | ok (full) |
| 13 Jul | H | 10,532.10 | 10,526.4 | +5.7 | 10,526.4 | +5.7 | ok |
| 13 Jul | L | 10,465.00 | 10,455.7 | +9.3 | 10,443.2 | +21.8 | ok (cash) |
| 13 Jul | C | 10,498.29 | 10,487.4 | +10.9 | 10,491.2 | +7.1 | Out (>5, <15) |

Eleven of 20 fields are out on both bases, and the report mixes bases from row to row (several rows agree with the full-day figures and others with the cash figures). The 9 Jul close (10,472.45 against 10,457.0) is wrong by 15.45 pts, which exceeds the 15 pt failure line. The D-1 close of 10,498.29 is 10.9 above the cash close and 7.1 above the full-day close (outside ±5, inside 15); every pivot and card level inherits it. The 8 Jul and 9 Jul opens equal the prior close to the penny (10,665.30 and 10,489.04), which looks like a continuity fill, yet those rows are labelled CORROBORATED.

### 4b. RSI2
Report RSI2 against the report's own closes (`--closes`): 9 Jul 2.0 vs 0.0; **10 Jul 78.5 vs 60.0 (does not reproduce)**; 13 Jul 100.0 vs 100.0 (ok). Against the slice on cash closes: 8 Jul 14.88 (report 27.5), 9 Jul 0.00 (2.0), 10 Jul 100.00 (78.5), 13 Jul 100.00 (100.0). Level-file `rsi2_cash` = 100.0, `rsi2_full` = 67.70.

### 4c. ATR14, KER, swings
- ATR14: not stated as a number in the report. Implied ~92–93 on the cards (69 pts "0.74 ATR"; 0.25 ATR "~23 pts") and ~94–100 in §21c; slice 117.8 (cash) / 128.44 (full), 21–28% higher.
- KER(13, EMA3), recomputed from the slice's 13-session cash closes: raw +0.05, smoothed +0.07 (positive; |KER| < 0.09, "Ranging — Neutral" band). The report's smoothed −0.20 "Trending Down — Moderate" has the wrong sign and magnitude. This feeds §9, the §21a Kaufman term (−0.03) and the TRANSITION call. The regime call itself is left at Transitional, since §9's other gate inputs cannot be reproduced from the slice.
- 25-session net change: report "~271 pts"; slice cash close 25 sessions back 10,370.4 → 10,487.4 = +117.0.
- Swings: report 10,749 / 10,128 against slice 25d cash 10,739.6 (7 Jul) / 10,126.2 (10 Jun): +9.4 / +1.8. 25d range position 58.9% (report "~60th", ok).

### 4d. Pivots (report vs `_cash`; `_full` in brackets)

| Level | Daily | Weekly (W28) | Monthly (June) |
|---|---|---|---|
| P | 10,498 vs 10,489.8: +8.2 (+11.1) | 10,550 vs 10,535.7: +14.3 (+2.5) | 10,507 vs 10,412.2: **+94.8** (+93.3) |
| R1 | 10,532 vs 10,524.0: +8.0 (+1.3) | 10,679 vs 10,691.1: −12.1 (−35.5) | 10,886 vs 10,698.1: **+187.9** (+184.7) |
| R2 | 10,566 vs 10,560.5: +5.5 (−4.1) | 10,861 vs 10,894.9: −33.9 (−45.7) | 11,088 vs 10,894.8: **+193.2** (+191.7) |
| R3 | 10,599 vs 10,594.7: +4.3 (−14.9) | 10,990 vs 11,050.3: −60.3 (−83.7) | not shown (slice 11,180.7) |
| S1 | 10,465 vs 10,453.3: +11.7 (+17.5) | 10,368 vs 10,331.9: +36.1 (+12.7) | 10,305 vs 10,215.5: **+89.5** (+86.3) |
| S2 | 10,431 vs 10,419.1: +11.9 (+27.3) | 10,238 vs 10,176.5: +61.5 (+49.7) | 9,926 vs 9,929.6: −3.6 (−5.1) |
| S3 | 10,398 vs 10,382.6: +15.4 (+33.7) | 10,057 vs 9,972.7: +84.3 (+60.9) | not shown (slice 9,732.9) |

- Daily pivots reproduce from the report's own H/L/C (formulas correct) and sit within ~12 pts of the cash set for P..S2; the whole ladder carries the +7–11 pt D-1 close/low offset.
- Weekly: the report's own R1/S1/P imply a week H 10,732, L 10,421, C 10,497; slice H 10,739.6, L 10,380.4, C 10,487.2. The weekly low is 40.6 pts too high (it reuses the report's wrong 9 Jul low of 10,420.3), which pushes S1–S3 up by 36–84 pts and R2/R3 down by 34–60 pts.
- Monthly (June 2026): the report's levels imply H 10,709, L 10,128, C 10,684. Slice June cash: H 10,608.8 (30 Jun), L 10,126.2 (10 Jun), C 10,501.5 (30 Jun). The June close is overstated by ~183 pts and the high by ~100 pts, so P/R1/R2/S1 are 90–193 pts too high. The §11 claim that all three timeframes are "two-source corroborated" is not supported. §11 and §15 use the monthly P (10,507) as a confluence with the daily P; with slice values the monthly P is 10,412.2 (cash), 77.6 below the daily cash P.

### 4e. Counters (slice, broker daily bars to 13 Jul)
- Dollar Index close 101.31 (7 Jul 101.06): rising mildly (report direction ok), but the report quotes "~99–100" (twice, §10 and §14), 1.3–2.3 below the slice level.
- S&P 500 (US500): 13 Jul −0.92% (report −0.79%, a basis-level difference); five-day (7 Jul→13 Jul) +0.10%, with +0.94% and +0.55% on 9 and 10 Jul. The report's "Falling" five-day label is not supported.
- VIX close 17.65 (range 16.61–18.57 over 8–13 Jul) vs report "~15–17".
- DAX and Euro Stoxx 50 have no slice here and cannot be checked.

## 5. Card Integrity (linter rows, copied verbatim; separate from the 100)

| card_id | report_date | strategy | flags | dud | Card score |
|---|---|---|---|---|---|
| 2026-07-14_Trade_1 | 2026-07-14 | Trade 1 - Daily Directional | SUPPRESSED | False | suppressed (excluded) |
| 2026-07-14_Trade_2 | 2026-07-14 | Trade 2 - Pivot, regime-aware (TRANSITION breakout side) | CLEAN | False | 100 |
| 2026-07-14_Trade_3C | 2026-07-14 | Trade 3C - Momentum-Breakout | CLEAN | False | 100 |

Report-level Card Integrity = mean(100, 100) = **100** (0 DUD, 0 WARN). Note for the reader: the static linter had no market data and card 3C carries no stated R, so the ATR-based tests (R within 0.3–3.0×ATR14, TP1 within 2.5×ATR14) were not exercised. With the slice ATR14 of 117.8 the 3C card is R 3.36×, TP1 5.1× (see feedback items 7–8). That is a Category 4 matter and does not change the copied linter score.
