# Trust Score v3.7 — FTSE 100 Daily Report, 18 June 2026 (run ftse_qa1)

Report: `reports/md/FTSE_EuroStoxx_Report_18Jun2026.md` · D = 2026-06-18 · D-1 = 2026-06-17
Level file check: `last_bar_date` = 2026-06-17 < D (leak-free, OK). Basis claimed by the report: GBP cash index, so `_cash` fields used (full-day shown where it helps).

## Result (machine-readable)
```
c1=2
c2=4
c3=2
c4=3
c5=2
total=54
band=Low
override=restriction_breach
card_integrity=100
n_cards=3
n_duds=0
n_warns=0
```
Override note: restriction_breach caps the band at Moderate (60-74) and drops C1 one level (3 -> 2). The raw total of 54 is already below that cap, so the cap does not bind. No hallucinated-source override (see 3.2).

## 1. Section 7 checklist

| Row | Reviewer notes | Evidence (location) | Score |
|---|---|---|---|
| 1.1 Variables respected | Asset is the FTSE 100 cash index, with Euro Stoxx 50 as reference only: OK. Counters USDX, S&P 500, DAX 40 and Euro Stoxx 50 are used: OK. Lookback is 5 sessions: OK. GBP and index points: OK. Header and §2 give the as-of as 18 Jun, but the as-of must be the London close of D-1 (17 Jun). The price evidence relies on Investing.com, Trading Economics and Yahoo (retail aggregators, one labelled "CFD-tracked") rather than index-provider or exchange tier. The only provider row (LSE/FTSE Russell, 29 May) carries no figure. The 07:00 UK daily-open anchor is never stated: Trade 1 says "18 Jun session open (pre-open anchor overridden to 18 Jun)" with no clock time, and the Agent Log repeats the override with no time. Oil is WTI with no Brent. | header, §2, §4, §20, §21b | 3 |
| 1.2 Coverage and currency consistent | Data window 11-17 Jun is correct and currency is GBP throughout. Drift points: as-of 18 Jun used as the data date; §3 says the consensus is a "17 Jun session" median while the "most recent corroborated" close is 16 Jun; §21c labels 16 Jun "t-1" and the backtest stops at 16 Jun although D-1 is 17 Jun; the Fed decision is placed on 18 Jun (the calendar has it 17 Jun, 21:00 broker = 19:00 UK); the ECB hike is dated 12 Jun (calendar: 11 Jun); UK GDP is dated 15 Jun (calendar: 12 Jun). | header, §3, §13c/d, §21c | 3 |
| 1.3 Audience and tone | Professional, strategist register, no retail tone. | §1, §18 | 4 |
| 2.1 Sections present and ordered | All 21 headings are present and in order, and §17 is a single sentence. §13b (aggregate sentiment with numeric tilt) and §21a (conviction) render as bare headings with no content. The +0.43 tilt appears only in §17 and the score only in §1/§20. Charts are headings/captions only (image drop accepted as a placeholder, noted). | §7, §13b, §21a | 3 |
| 2.2 Scorecard as table | §6 is a table with O/H/L/C/RSI2/Trend/Validation. It has a single merged "Sources A/B" column and no "Final" column. §11 is a table but runs R5 to S5, not R3 to S3, and daily/weekly/monthly share one table. Cosmetic or minor. | §6, §11 | 4 |
| 2.3 Method steps visible | Observations to consensus (§4-§5), candle-by-candle (§8; the body-position percentages reproduce from the report's own OHLC), and regime with overlap/persistence/VOLator (§9) are all shown. §5 asserts two-source corroboration of 16 Jun while §4 lists only one source for that date. | §4-§9 | 4 |
| 3.1 Quantitative claims sourced | Unsourced or wrong: "roughly 3% fall in crude" (§1, §12, §14, no source, not in §13a); "VIX low (~16)" (§14; slice shows 18.43 on 17 Jun); "BMW profit warning" (§10); "US-Iran interim agreement", "Chair Warsh"; "Dollar Index soft/flat" (§1, §10, §14; slice shows USDX +0.86% on 17 Jun and +0.71% over 11-17 Jun); "US equities rallied" (§1; S&P 500 proxy -0.94% on 17 Jun and -1.5% over the last two sessions). | §1, §10, §12, §14 | 2 |
| 3.2 Citations exist and contain the data | Spot-check: (1) Trading Economics 17 Jun, 10,504 and the "CFD-tracked" note, used consistently, passes. (2) Investing.com 15 Jun, 10,430.62 with High 10,570.09, matches §6, passes. (3) LSEG/FTSE Russell 16 Jun, "data ranges ... to 10,910": the 10,910 figure appears nowhere else, the quote is not a sentiment derivation, and the "near record territory" claim conflicts with the report's own 10,570 25-session high. Weak, not provably fabricated, so no override. §4's LSE/FTSE Russell 29 May row carries no figure. | §4, §13a | 3 |
| 3.3 Calculations transparent | RSI2 reproduces from the report's own closes (80.3 / 29.4 / 100.0 verified with `--closes`). Daily, weekly and monthly pivots reproduce exactly from the report's own implied H/L/C. ATR(14) is never stated as a number (only implied: 363/3.5 = 103.7, and "≈0.85 ATR"). The KER value is given but not its window or EMA. The sentiment tilt (+0.43) has no per-article weights and §21a is empty; the +0.72 derivation is only in §20. | §6, §9, §11, §13b, §20, §21 | 3 |
| 3.4 Numbers reconcile | The D-1 close 10,504 is the same in §1, §3, §4, §6 and §21b. §11 pivots equal the card pivots. RSI2 in §6 equals §8. Breaks: §3 anchors on 17 Jun while calling 16 Jun the last corroborated close. Trade 1 says TP1 10,589 is "inside 10,553-10,570", but it is 19 pts above 10,570. Trade 2 says weekly P (10,390) is "just above monthly P (10,373)"; on the cash level file weekly P 10,353.07 is 17.3 below monthly P 10,370.40. The medium-regime term is +0.20 where the M5 rule table gives +0.10 for TRANSITION. §9 says "Trending" and then TRANSITION, while §16/§17 say "trending". | cross-section | 3 |
| 3.5 (brief §4) Report vs level file | See section 2. 13 of 20 OHLC fields are outside tolerance (9 of them by more than 15 pts: e.g. 12 Jun O/L -66, 15 Jun O -86, 16 Jun H -71, 16 Jun C -62). 4 of 5 closes are outside the 5-pt tolerance and the 16 Jun close is 62.4 pts off, which is over the 15-pt failure line. The 16 Jun RSI2 is 29.4 against 79.0 in the slice. Daily pivots are 14-91 pts off, weekly 27-179, monthly P/R1/S1 within 7. | §6, §11 | 1 |
| 4.1 Pillars conclude | §8 ends in "Continuation"; §9 in "Bias: Bullish" then TRANSITION; §10 ends CONFIRM (but on wrong USDX/S&P facts). §12 and §14 are bullet lists with per-bullet tags and no closing direction label. | §8-§14 | 3 |
| 4.2 Cross-asset interpreted | Mechanisms are stated (USD translation, risk beta, eurozone read-through, energy weight). The statuses rest on misread counters: USDX is called soft when it rose; S&P is called rising when the last two sessions fell. The aggregate "three of four confirm, none contradict" is therefore unsupported. The factual error is booked in C3. | §10 | 3 |
| 4.3 Synthesis reconciles tensions | KER vs trend is acknowledged. Not reconciled: the label stays "Trending" in §1/§9/§16/§17 while the cards run under TRANSITION; Trade 2 is a pullback long under a regime that permits breakout-side only; the medium-regime term is scored as a full +0.20; the report says the 17 Jun close is indicative yet uses it as the Trade 1 entry. | §9, §15-§18, §20, §21 | 2 |
| 4.4 Calibrated language | §17 is exactly one sentence with a single contingency; confidence is stated (Medium) in §3 and §18. | §3, §17 | 4 |
| 4.5 Card construction (protocol) | All three cards break fixed M5 rules (detail in the feedback file). Trade 1: the stop is described as a "5-day swing low" but is the lowest low of only the last 3 sessions, and it has no 0.25×ATR buffer. Trade 2: a pullback limit at weekly P is borrowed geometry under a TRANSITION label, and the branch is not named. Trade 3C: not eligible (no daily close ≥ 0.25 ATR beyond the 25-day boundary), uses a pivot stop instead of low + 0.40×width, TP1 is +1R and not the measured move, and invalidation equals the stop. None of the cards prints the D-1 reference close and signed gap or R/ATR to two decimals. The linter shows all three CLEAN, so these defects are not visible in Card Integrity. | §21b | 1 |
| 5.1 Data dated, staleness flagged | Prices and articles are dated and the 17 Jun indicative flag is shown. Not flagged: the 12 Jun / 15 Jun / 16 Jun opens and the 16 Jun range are marked CORROBORATED despite the mismatches in 3.5; the STOXX 16 Jun H/L are round numbers (6,260 / 6,210) marked CORROBORATED; three events are misdated (see 1.2). | §4, §6, §13 | 3 |
| 5.2 Assumptions up front | The anchor-override caveat is on Trade 1 and in §20, but without a clock time. §20 admits that corroboration was "relaxed for the 17 Jun close per instruction so the strategy section is not suppressed", which is not stated in §1/§3. Single-source propagation: Trade 1 and Trade 2 carry it; Trade 3C's stop (daily pivot 10,485) is the indicative tier and its caveats omit this. | §20, §21b | 3 |
| 5.3 Red flags surfaced | The BoE decision is surfaced and carried into the Trade 1 and 3C caveats; it is missing from Trade 2. The Fed "collision" is a misdated non-event for D. Omitted from §13d: UK labour data at 09:00 broker (07:00 UK = the anchor time), US jobless claims and Philly Fed (15:30 broker). | §12, §13d, §21b | 3 |
| 5.4 Restrictions honoured | Retail CFD quotes are in the price basis: TE 17 Jun is labelled "CFD-tracked close" and sets the headline consensus and the Trade 1 entry; the STOXX 15 Jun close is "6,274 (CFD)"; §5 nevertheless says retail CFD spreads were excluded. The opens of 12, 15, 16 and 17 Jun each sit within 11 pts of the previous report close (12 Jun open 10,302.68 vs 11 Jun close 10,303.88; 15 Jun 10,471.37 vs 10,471.72; 16 Jun 10,441.09 vs 10,430.62; 17 Jun 10,444.18 vs 10,447.74) while the slice shows real gaps (e.g. 15 Jun open 10,557.6 vs 12 Jun close 10,459.5). That is consistent with a prior-close-derived value presented as a corroborated observation (M3 forbids this). 12 Jun is shown as O=L and C=H to the cent. No module codes, bracketed variables or framework name; no futures. | §4, §5, §6 | 1 |

Category roll-up (level = rounded mean of rows; ties round down per framework §9):

| Cat | Rows | Mean | Level | Note |
|---|---|---|---|---|
| C1 | 3, 3, 4 | 3.33 | 3 -> 2 | Reduced one level by the restriction-breach override |
| C2 | 3, 4, 4 | 3.67 | 4 | |
| C3 | 2, 3, 3, 3, 1 | 2.40 | 2 | 3.5 included because brief §4 makes the slice comparison the main accuracy test |
| C4 | 3, 3, 2, 4, 1 | 2.60 | 3 | 4.5 (card construction) included per the protocol |
| C5 | 3, 3, 3, 1 | 2.50 | 2 | Tie rounded down |

## 2. Category 3 comparison with the level file (cash basis, UK window)

Tolerance (brief §4): close ≤ 5 pts, open/high/low ≤ 10 pts, close > 15 = failure. Delta = report − slice cash. "X" = outside tolerance.

| Date | Field | Report | Slice cash | Δ | Slice full-day | Δ full | Flag |
|---|---|---|---|---|---|---|---|
| 11 Jun | Open | 10,255.16 | 10,238.9 | +16.3 | 10,182.2 | +73.0 | X |
| 11 Jun | High | 10,370.15 | 10,373.4 | -3.2 | 10,419.6 | -49.5 | ok |
| 11 Jun | Low | 10,252.27 | 10,235.8 | +16.5 | 10,152.8 | +99.5 | X |
| 11 Jun | Close | 10,303.88 | 10,299.9 | +4.0 | 10,410.7 | -106.8 | ok |
| 12 Jun | Open | 10,302.68 | 10,368.9 | -66.2 | 10,414.6 | -111.9 | X |
| 12 Jun | High | 10,471.72 | 10,473.5 | -1.8 | 10,485.4 | -13.7 | ok |
| 12 Jun | Low | 10,302.68 | 10,368.3 | -65.6 | 10,367.9 | -65.2 | X |
| 12 Jun | Close | 10,471.72 | 10,459.5 | +12.2 | 10,460.9 | +10.8 | X |
| 15 Jun | Open | 10,471.37 | 10,557.6 | -86.2 | 10,507.0 | -35.6 | X |
| 15 Jun | High | 10,570.09 | 10,574.6 | -4.5 | 10,574.6 | -4.5 | ok |
| 15 Jun | Low | 10,419.22 | 10,422.8 | -3.6 | 10,404.6 | +14.6 | ok |
| 15 Jun | Close | 10,430.62 | 10,441.2 | -10.6 | 10,415.6 | +15.0 | X |
| 16 Jun | Open | 10,441.09 | 10,449.3 | -8.2 | 10,411.0 | +30.1 | ok |
| 16 Jun | High | 10,458.95 | 10,529.6 | -70.6 | 10,529.6 | -70.6 | X |
| 16 Jun | Low | 10,438.09 | 10,434.9 | +3.2 | 10,409.4 | +28.7 | ok |
| 16 Jun | Close | 10,447.74 | 10,510.1 | -62.4 | 10,472.3 | -24.6 | X (>15, failure) |
| 17 Jun | Open | 10,444.18 | 10,494.9 | -50.7 | 10,477.7 | -33.5 | X |
| 17 Jun | High | 10,523.51 | 10,513.3 | +10.2 | 10,516.0 | +7.5 | X (marginal) |
| 17 Jun | Low | 10,428.56 | 10,470.9 | -42.3 | 10,434.9 | -6.3 | X |
| 17 Jun | Close | 10,504.00 | 10,513.3 | -9.3 | 10,445.4 | +58.6 | X (flagged indicative by report) |

The report's values fit neither the cash nor the full-day basis consistently, so this is not a basis gap. 13 of 20 fields fail tolerance on the claimed cash basis.

RSI2: report 100.0 / 100.0 / 80.3 / 29.4 / 100.0 vs slice cash 100.0 / 100.0 / 89.71 / 79.01 / 100.0. The arithmetic reproduces from the report's own closes (80.3, 29.4, 100.0 verified), but the 15 Jun (Δ -9.4) and 16 Jun (Δ -49.6) values do not match the slice. At 79.0 the slice's 16 Jun trend label would be Bullish (C > O, RSI2 > 50); the report prints Neutral.

ATR14: not stated in the report. Implied 103.7 (363/3.5) vs slice cash 107.12 (full 137.46): consistent but undeclared.

Pivots (report vs level file `_cash`):

| Level | Daily rep | Daily slice | Δ | Weekly rep | Weekly slice | Δ | Monthly rep | Monthly slice | Δ |
|---|---|---|---|---|---|---|---|---|---|
| R3 | 10,637 | 10,569.8 | +67.2 | 10,798 | 10,927.2 | -129.2 | 11,000 | 11,018.4 | -18.4 |
| R2 | 10,580 | 10,541.6 | +38.4 | 10,635 | 10,700.4 | -65.4 | 10,778 | 10,789.2 | -11.2 |
| R1 | 10,542 | 10,527.4 | +14.6 | 10,553 | 10,579.9 | -26.9 | 10,594 | 10,599.6 | -5.6 |
| P | 10,485 | 10,499.2 | -14.2 | 10,390 | 10,353.1 | +36.9 | 10,373 | 10,370.4 | +2.6 |
| S1 | 10,447 | 10,485.0 | -38.0 | 10,309 | 10,232.6 | +76.4 | 10,188 | 10,180.8 | +7.2 |
| S2 | 10,390 | 10,456.8 | -66.8 | 10,146 | 10,005.8 | +140.2 | 9,967 | 9,951.6 | +15.4 |
| S3 | 10,352 | 10,442.6 | -90.6 | 10,064 | 9,885.3 | +178.7 | 9,782 | 9,762.0 | +20.0 |

Cause of the weekly gap: the report's weekly inputs back-solve to H 10,471 / L 10,227 / C 10,472 (range 244). The slice week 8-12 Jun is H 10,473.5 / L 10,126.2 / C 10,459.5 (range 347.3); the 10 Jun low falls outside the report's 11-17 Jun table. The daily gap comes from the wrong 17 Jun H/L/C inputs (report range 95 vs slice cash range 42.4, full-day range 81.1). Monthly R2-S3 drift (11-20 pts) reflects a May range 26 pts narrower than the slice.

## 3. Card Integrity (linter rows, copied verbatim from `lint_static/2026-06-18.csv`)

| card_id | strategy | flags | dud | per-card score |
|---|---|---|---|---|
| 2026-06-18_Trade_1 | Trade 1 - Daily Directional (LONG) | CLEAN | False | 100 |
| 2026-06-18_Trade_2 | Trade 2 - Pivot (regime-aware, weekly-anchored LONG) | CLEAN | False | 100 |
| 2026-06-18_Trade_3C | Trade 3 - Momentum-Breakout (3C, TRANSITION fork, LONG) | CLEAN | False | 100 |

Report-level Card Integrity = 100 (n_cards=3, n_duds=0, n_warns=0, none suppressed). This is separate from the 100-point Trust Score. The linter is static (stop side, TP order, R band); the construction defects in 4.5 are outside what it tests, so a CLEAN row here does not mean the card satisfies M5.

## 4. Total, band, override

Points: C1 level 2 = 0.40×20 = 8.0 · C2 level 4 = 0.85×20 = 17.0 · C3 level 2 = 0.40×25 = 10.0 · C4 level 3 = 0.65×20 = 13.0 · C5 level 2 = 0.40×15 = 6.0.
Total = 54.0 -> 54/100 -> Low Trust (40-59).
Override check: restriction_breach applied (retail CFD quote in the price basis, in contradiction with §5; opens consistent with prior-close derivation labelled CORROBORATED). Hallucinated-source override not applied: no cited source was shown to be impossible; the 16 Jun and 12 Jun "corroborated" values are scored as accuracy and restriction failures.

Feedback: `qa/ftse_qa1/2026-06-18_feedback.md`.
