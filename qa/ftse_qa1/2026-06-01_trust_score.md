# Trust Score v3.7 — FTSE 100 daily report, D = 2026-06-01 (run ftse_qa1)

Report: `reports/md/FTSE_EuroStoxx_Report_01Jun2026.md`
Level file check: `last_bar_date` = 2026-05-29 < D (leak-free). Slice last bar 2026-05-29 22:45 broker.
Basis claimed by the report: cash. Compared against `_cash` fields (cash window 10:00-18:30 broker, `qa_slice_stats.py` run with that window).

## Result lines
```
c1=1
c2=3
c3=1
c4=3
c5=3
total=45
band=Low
override=restriction_breach
card_integrity=100
n_cards=2
n_duds=0
n_warns=0
```
(n_cards counts non-suppressed cards; the linter returned 3 rows, 1 of them SUPPRESSED.)

## 1. Section 7 checklist

| Row | Reviewer notes | Evidence location | Score |
|---|---|---|---|
| 1.1 Variables respected | Asset = FTSE 100 cash, GBP points, Europe/London, 5-session lookback stated, counters USDX / S&P 500 / DAX 40 present, retail-CFD feed excluded (all met). Not met: (a) daily-open anchor is "01 June pre-open window" with no clock time, not 07:00 UK; (b) price sources are anonymised "provider A / provider B", so the >=6 named index-provider / exchange / sell-side sources are not demonstrable; (c) the 5-session window is wrong (see 1.2). | §1, §2, §4, §20, §21b | 2 |
| 1.2 Coverage & currency consistent | D (01 Jun 2026) is called a Sunday in §2 note, §20 anomaly (2) and the card notes; it is a Monday (the news slice schedules D events, e.g. ISM Manufacturing PMI, S&P Global PMIs, Fed Chair Powell speech). Weekday labels in §6 are wrong: "Tue 27 May" and "Wed 28 May" are Wed 27 / Thu 28; there are two rows dated 29 May ("Thu 29 May*" phantom and "Fri 29 May"); the real Tue 26 May session is omitted. Weekly pivots are taken from "week of 18-22 May" instead of the last completed week (26-29 May). A 04 May article sits in a 5-session sentiment set. Units/currency are consistent. | §2, §6, §11, §13a, §20 | 1 |
| 1.3 Audience & tone | Professional strategist register, no retail tone. | §1, §18 | 4 |
| 2.1 Sections present & ordered | §1-§21 all present and in order, §13a-d and §21a-d present, §17 is one sentence. Gaps: §7 has no charts (caption/placeholder only, accepted per brief but five charts are promised and none exist); §11 has no monthly pivots and the weekly table stops at R2/S2 (no R3/S3); §21c grid is incomplete (Trade 2 and 3C not listed for each session). | headings, §7, §11, §21c | 3 |
| 2.2 Scorecard as a table | §6 is a table, but it lacks the Source A / Source B columns (has "Final used" and "Validation" only). §11 daily table is R3->S3 (with derived 1.5 tiers), weekly is R2->S2 only, monthly is absent. | §6, §11 | 2 |
| 2.3 Method steps visible | §4 evidence table to §5 consensus to §8 candle-by-candle sequence is visible; §9 shows regime, overlap, persistence, VOLator and Kaufman, but only qualitatively: no ATR(14) value, no KER(13) value, no VOLator number anywhere. Charts absent (placeholder note). | §4-§9 | 3 |
| 3.1 Quantitative claims sourced (and agree with the slice) | Brent ~$91, WTI ~$87, DE HICP 2.7%, "5-week pivot", VIX ~15.3, DXY ~98.85 carry no source or only an anonymised provider. Slice checks: VIX D-1 close is 16.53 (report 15.3, -1.2); DXY D-1 close 98.956 (report ~98.85); S&P 500 D-1 close 7,581.1 (report 7,580, ok). The core FTSE price claims are materially wrong against the slice (see §2 below). | §1, §4, §10, §12, §14 | 1 |
| 3.2 Citations exist & contain data | Three spot-checks: Trading Economics 29 May (DAX +3.4% May) is consistent with §4/§12; Trading Economics 29 May (DE/FR CPI softer) is consistent with the calendar slice (29 May 15:00 broker HICP y/y 2.7 vs consensus 3.2, prior 2.9); Reuters (archive) 04 May is 25 sessions outside the lookback and unverifiable. No URLs; price providers A/B are unnamed so cannot be spot-checked. No self-contradictory or impossible source found, so no hallucinated-source override. | §4, §13a | 2 |
| 3.3 Calculations transparent | Daily pivot arithmetic reproduces from the report's own 29 May H/L/C (P 10,409.43, R2 10,465.63, R3 10,493.65 verified). §21a sum 0.20+0.15+0.045+0.045 = 0.44 reproduces. RSI2 does NOT reproduce: from the report's own closes (10371.40, 10421.55, 10448.30, 10426.10, 10409.28) the exact tests give 100.0 / 54.6 / 0.0 vs the report's 100.0 / 61.0 / 40.7. ATR(14) and KER(13, EMA3) are never stated; the cards imply ATR of about 60 (stop buffer), 62.7 (3xATR cap 10,597) and 64 (3C trigger buffer) against slice ATR14 113.4. Weekly pivots back-solve to a one-day H/L/C (10,488 / 10,298 / 10,371.4), not a weekly bar. | §6, §9, §11, §21a, §21b | 1 |
| 3.4 Numbers reconcile | D-1 close 10,409 / 10,409.28 is consistent across §1, §3, §4, §6, §21b; daily pivots in §11 match the cards; RSI2 matches between §6 and §8. Breaks: implied ATR differs between cards (60 / 62.7 / 64); Trade 1 TP1 10,453 is +44 and TP2 10,497 is +88 but the card says +43 / +87; §11 says the 29 May close (10,409.28) is "above" the daily pivot 10,409.43 (it is 0.15 below); §8 says the 29 May close is at ~38% of range (the report's own H/L/C give 49.6%); §21c claims Wed 28 May Trade 1 hit +1R with entry 10,421.55 -> TP1 about 10,464.5, but the report's own 28 May high is 10,455.10. | §8, §11, §21b, §21c | 1 |
| 4.1 Pillars conclude | §8 Indecision, §9 Bias Bullish, §10 CONFIRM-with-one-contradiction, §12 and §14 item-level direction tags, §15 table. Each ends in a label; §12/§14 label items rather than the pillar as a whole. | §8-§14 | 4 |
| 4.2 Cross-asset interpreted | Mechanisms given (USD strength/GBP translation of overseas earnings, US beta, DAX read-across, energy weight Shell/BP). Not a correlation list. | §10, §12 | 4 |
| 4.3 Synthesis reconciles tensions | §15/§16/§18 address short vs medium term and the DXY contradiction. Weaknesses: §21a gives cross-asset a full +0.15 "confirm" despite the flagged contradiction; 3C direction trigger says "recent retests faded at the upper boundary" and calls that Upside (a fade is a rejection); Trade 1 LONG and a 3C breakout-long both sit on an "Indecision" short-term read. | §15-§18, §21a | 3 |
| 4.4 Calibrated language | §17 exactly one sentence; confidence "Low" stated in §3/§18; some stacked qualifiers ("balanced-to-mildly-constructive", "mildly bullish bias ... provided ... and ..."). | §1, §3, §17 | 4 |
| Card construction (protocol: scored under C4) | Anchor time never stated (07:00 UK expected). Trade 1 stop buffer, cap and 3C trigger built on ATR of about 60-64, not 113.4. 3C range 10,180-10,612 vs slice 25-day cash range 10,141.2-10,560.0. 3C has no R in points and no points on stop/TP. Arithmetic slips on Trade 1 TP1/TP2. Single-source propagation and event collision are carried (positive). Trade 2 suppression is correct under the rule. | §21b | 2 |
| 5.1 Data dated; staleness flagged | INDICATIVE / SINGLE-SOURCE flags on every row and level (strong). Dating defects: duplicate 29 May, wrong weekdays, weekly pivot from the wrong week, 04 May article. | §4, §6, §11, §13, §19 | 3 |
| 5.2 Assumptions up front | Provenance banner is the first line of the report; anchor override stated in the §6 header, the §21b entry and §20; proxy-open assumption present. Clock time of the override is missing. | banner, §20, §21b | 4 |
| 5.3 Red flags surfaced | Iran sign-off carried to §12/§15/§21b caveats; pivots-indicative carried. Missed: scheduled D events in the calendar slice (ISM Manufacturing PMI and Prices Paid, S&P Global US Manufacturing PMI, Fed Chair Powell speech, UK/EZ manufacturing PMIs) are absent from §13d and from the card caveats. | §12, §13d, §21b | 3 |
| 5.4 Restrictions honoured | Retail CFD feed excluded; no module codes or bracketed variable names; instrument common names used. Breach: five sessions of O/H/L and a phantom "Thu 29 May" row are synthesised ("reconstructed", "reconstruction artefact") and carried in the "Validated" table's "Final used" column into RSI2, pivots and the cards. §20 also leaks process text ("v2.1 baseline, locked, session 1 of 20"). | §6, §19, §20 | 1 |

## 2. Category 3 data checks against `data/levels/UK100_by_date/2026-06-01.csv` (cash basis)

D-1 (29 May) row:

| Field | Report | Slice (cash) | Delta | Verdict |
|---|---|---|---|---|
| Open | 10,425.85 | 10,434.7 | -8.85 | within 10 |
| High | 10,437.60 | 10,462.0 | -24.4 | discrepancy |
| Low | 10,381.40 | 10,409.2 | -27.8 | discrepancy |
| Close | 10,409.28 | 10,410.0 | -0.72 | within 5 |
| RSI2 | 40.7 | 0.0 | +40.7 | fails (also fails reproduction from own closes: 0.0) |
| ATR14 | not stated (implied about 60-64) | 113.4 | about -50 | discrepancy |

Earlier sessions (report row vs the real session on that date):

| Report row | Report O/H/L/C | Slice cash O/H/L/C | Delta O/H/L/C |
|---|---|---|---|
| Fri 22 May | 10362.10 / 10388.40 / 10318.55 / 10371.40 | 10492.6 / 10494.5 / 10446.0 / 10470.4 | -130.5 / -106.1 / -127.5 / -99.0 |
| "Tue 27 May" (real Wed 27) | 10360.20 / 10428.70 / 10351.30 / 10421.55 | 10487.7 / 10523.5 / 10460.6 / 10507.9 | -127.5 / -94.8 / -109.3 / -86.4 |
| "Wed 28 May" (real Thu 28) | 10421.55 / 10455.10 / 10401.20 / 10448.30 | 10434.1 / 10446.6 / 10378.8 / 10432.4 | -12.6 / +8.5 / +22.4 / +15.9 |
| "Thu 29 May*" | 10448.30 / 10463.90 / 10402.60 / 10426.10 | no such session | phantom row |
| (missing) Tue 26 May | not in report | 10531.9 / 10560.0 / 10498.0 / 10500.7 | omitted |

Slice RSI2 (cash closes): 100.0, 100.0 (26 May), 100.0, 8.71, 0.0 vs report 42.7, 83.4, 100.0, 61.0, 40.7.
Three closes are wrong by more than 15 pts (-99.0, -86.4, +15.9), and RSI2 does not reproduce from the report's own closes, so this is a Category 3 failure, not a note.

Derived levels:

| Item | Report | Slice (cash) | Delta |
|---|---|---|---|
| Daily P / R1 / S1 | 10,409.43 / 10,437.45 / 10,381.25 | 10,427.07 / 10,444.93 / 10,392.13 | -17.6 / -7.5 / -10.9 |
| Daily R2 / S2 | 10,465.63 / 10,353.23 | 10,479.87 / 10,374.27 | -14.2 / -21.0 |
| Daily R3 / S3 | 10,493.65 / 10,325.05 | 10,497.73 / 10,339.33 | -4.1 / -14.3 |
| Weekly P / R1 / S1 | 10,385.80 / 10,473.60 / 10,283.60 | 10,449.60 / 10,520.40 / 10,339.20 | -63.8 / -46.8 / -55.6 |
| Weekly R2 / S2 | 10,575.80 / 10,195.80 | 10,630.80 / 10,268.40 | -55.0 / -72.6 |
| Weekly R3 / S3 | absent | 10,701.60 / 10,158.00 | missing |
| Monthly P R1 S1 R2 S2 R3 S3 | absent | 10,370.4 / 10,599.6 / 10,180.8 / 10,789.2 / 9,951.6 / 11,018.4 / 9,762.0 | missing |
| 5-day swing high / low | 10,464 / 10,342 | 10,560.0 (26 May) / 10,378.8 (28 May) | -96 / -37 |
| 25-day range | 10,180-10,612 | 10,141.2-10,560.0 | +38.8 / +52 |

Consequence for reading: D-1 cash close 10,410.0 is below the slice weekly pivot 10,449.6 (-39.6), whereas §11/§16/§21b treat the close as above the weekly pivot.

## 3. Category roll-up

| Cat | Max | Rows | Mean | Level | Multiplier | Points | Justification |
|---|---|---|---|---|---|---|---|
| C1 | 20 | 2,1,4 | 2.33 | 2, then 1 after breach override | 0.20 | 4.00 | Asset/tz/counters right; anchor time, sources, 5-session window and the weekday of D wrong; synthesised price rows breach the no-synthesis restriction (level cut one) |
| C2 | 20 | 3,2,3 | 2.67 | 3 | 0.65 | 13.00 | All 21 sections present and ordered; no charts, no monthly pivots, weekly incomplete, no Source A/B columns |
| C3 | 25 | 1,2,1,1 | 1.25 | 1 | 0.20 | 5.00 | Three of five closes off by 16-99 pts, RSI2 not reproducible, ATR/KER unstated, pivots from wrong week; arithmetic that is shown is correct |
| C4 | 20 | 4,4,3,4,2 | 3.40 | 3 | 0.65 | 13.00 | Good mechanism and synthesis layout; card levels use wrong ATR and wrong 25-day range |
| C5 | 15 | 3,4,3,1 | 2.75 | 3 | 0.65 | 9.75 | Up-front banner and heavy INDICATIVE tagging are strong; dating errors, missed D events, synthesised prices |

## 4. Total, band, override

- Total = 4.00 + 13.00 + 5.00 + 13.00 + 9.75 = 44.75, rounded to **45**.
- Band: **Low** (40-59).
- Override check: hallucinated source: none (no cited source found impossible or self-contradictory; spot-checks 3.2 consistent where checkable). Restriction breach: **yes**, row 5.4 (synthesised/reconstructed O/H/L and a phantom session used as the "Final used" basis). It caps at Moderate (60-74), which does not bind at 45, and C1 was reduced one level (2 to 1). `override=restriction_breach`.

## 5. Card Integrity (linter rows copied verbatim from `qa/ftse_qa1/lint_static/2026-06-01.csv`)

| card_id | report_date | strategy | flags | dud |
|---|---|---|---|---|
| 2026-06-01_Trade_1 | 2026-06-01 | Trade 1 - Daily Directional (LONG - Transitional-bullish lean) | CLEAN | False |
| 2026-06-01_Trade_2 | 2026-06-01 | Trade 2 - Pivot (regime-aware) | SUPPRESSED | False |
| 2026-06-01_Trade_3C | 2026-06-01 | Trade 3 - Momentum-Breakout (3C - Transitional regime) | CLEAN | False |

Per card: Trade 1 = 100, Trade 3C = 100, Trade 2 suppressed (excluded). Report level = mean over 2 non-suppressed cards = **100**. n_cards=2, n_duds=0, n_warns=0. Card Integrity is separate from the 100 and says nothing about the construction defects scored in C4 (see feedback file): it is a static check with no market data.

## 6. Feedback
See `qa/ftse_qa1/2026-06-01_feedback.md`.
