# Trust Score v3.7 - FTSE 100 Daily Report, 29 May 2026 (run ftse_qa1)

Report: `reports/md/FTSE_100_Daily_Report_29May2026.md` - D = 2026-05-29, D-1 = 2026-05-28.
Level file check: `last_bar_date` = 2026-05-28 < D (leak-free). Basis used: cash (`_cash`), because the report states "Cash index, LSE session 08:00-16:30 UK". Full-day values are cited only where they explain a mismatch.

## Result lines
```
c1=2
c2=3
c3=2
c4=3
c5=2
total=50
band=Low
override=restriction_breach
card_integrity=100
n_cards=3
n_duds=0
n_warns=0
```
C1 raw checklist mean rounds to 3; the restriction-breach override lowers it one level to 2. Total is 8 + 13 + 10 + 13 + 6 = 50. The Moderate cap (74) is not binding. n_cards counts the Trade 1 SUPPRESSED row; Card Integrity is the mean over the 2 non-suppressed cards.

## 1. Section 7 checklist

| Row | Reviewer notes | Evidence observed (location) | Score |
|---|---|---|---|
| 1.1 Variables respected | Asset (FTSE 100 cash, Euro Stoxx 50 reference only), counters (USDX, S&P 500, DAX 40), as-of London close D-1, 5-session lookback with 25 May holiday excluded, GBP/index points and the 07:00 UK anchor all honoured. Source mix fails the brief: all 7 named sources are media/aggregators (Investing, Yahoo, Trading Economics, Sharecast/Fidelity, bbntimes/Alliance, CNBC, Morningstar). None is an index provider, exchange or sell-side source. | §2, §4, §10, §20 | 3 |
| 1.2 Coverage and currency consistent | Currency consistent. Date drift: US PCE is treated as a 29 May event but the calendar shows it released 28 May 15:30 broker (13:30 UK). Euro-area CPI/HICP is placed "Early Jun" but is scheduled 29 May. Daily pivots are drawn from 27 May (D-2) rather than the D-1 session. | §1, §11, §13d, §14 | 3 |
| 1.3 Audience and tone | Strategist register, no retail tone. | §1, §18 | 4 |
| 2.1 Sections present and ordered | §1-§21 all present and in order, including 13a-13d and 21a-21d. §11 omits monthly pivots and the printed prior-period H/L/C inputs M4 asks for. | headings | 4 |
| 2.2 Scorecard/pivots as tables | §6 is a proper table with all required columns (RSI2 blank on two rows). §11: daily is a table, weekly is a single line of text with only 2 levels per side (R3/S3 missing), monthly is absent. | §6, §11 | 2 |
| 2.3 Method steps visible | §4-§5 observation to consensus, §8 candle-by-candle plus sequence, §9 regime with overlap/persistence/VOLator, §7 chart captions (5; images not preserved, accepted as placeholders). Content of §8 contains factual slips (see 3.4). | §4-§9 | 4 |
| 3.1 Quantitative claims sourced | Sector weights (energy 12-15%, banks ~25%), Fed-hike odds ~50%, gilt 10Y 4.57%, GBP/USD 1.330, BoE 3.75%, Brent range, Cboe UK 100 move are unsourced or point to nothing in §4/§13. The 26 May and 21 May OHLC and the 10,405 close have no source quote in §4. | §12, §14, §4, §6 | 2 |
| 3.2 Citations exist and contain data | Three spot checks. (a) Investing.com 28 May "range 10,381.12-10,447.89; open 10,437.20": consistent with the slice (cash H 10,446.6 / L 10,378.8 / O 10,434.1). But the row quotes no close, and §3 says sources place the close in "10,390-10,418" while no §4 row contains 10,418. (b) Sharecast/Fidelity 27 May "flat at 10,487.29 (afternoon)": an intraday print used as the 27 May close and labelled CORROBORATED, with Sharecast and Fidelity counted as two sources. (c) CNBC 26 May "European stocks edge lower amid peace-talk uncertainty" is cited as Bearish, while §13c describes 26 May as "peace-talk optimism ... risk-on, five-week high". Nothing is impossible on its face, so no hallucinated-source override. The corroboration claims are not supported by the quoted figures. | §4, §13a, §13c, §19 | 2 |
| 3.3 Calculations transparent | RSI2 reproduces from the report's own closes (100.0 / 74.8 / 0.0, engine `--closes`), Trend labels follow the rule, and the daily pivots reproduce arithmetically from the stated 27 May H/L/C. ATR(14) is never stated (cash 117.33, full 134.7). KER -0.11 has no inputs and does not reproduce: 13-session cash-close KER is +0.27 raw (+0.45 on an EMA3-smoothed series), opposite sign and above the 0.13 trend threshold. §21a score -0.18 has no term-by-term derivation. RSI2 missing for 21/22 May. Weekly H/L inputs not shown. | §6, §9, §11, §21a | 2 |
| 3.4 Numbers reconcile | See section 2. The close 10,405 is identical across §1, §3, §4, §6, §21b. Level-file comparison: 10 of 20 OHLC fields fail tolerance, 3 of 5 closes are off by more than 15 pts, every daily and weekly pivot is outside tolerance. Internal breaks: "eight-session winning streak" snapped on 28 May while the report's own table has 27 May (10,487.29) below 26 May (10,498); §8 says 21 May closed "~85%" up the range, the table gives (10,423-10,388)/(10,470-10,388) = 43%; §8 calls 28 May "marubozu-style" with a 24-pt lower wick on a 67-pt range; §21c/§21d show a 28 May entry "open 5+ days" and a "closed legs" mean that includes open legs. | §1, §6, §8, §11, §21 | 1 |
| 4.1 Pillars conclude | §8 (Exhaustion), §9 (Neutral, short-term bearish tilt) and §10 (MIXED) end in labels. §12 and §14 end in per-item tags and a watch item but no section-level direction label. | §8-§14 | 3 |
| 4.2 Cross-asset interpreted | Mechanisms given for USDX (translation vs Fed-hike risk), S&P (risk beta) and DAX (oil/geopolitics). The dollar read is contradicted by the slice (USDX 28 May open 99.308 to close 99.023, -0.29% on the day; 21 May close 99.237 to 99.023 over the window, not "flat/firm"). Oil/energy channel appears in §12 only, not in the cross-asset table. | §10, §12 | 3 |
| 4.3 Synthesis reconciles tensions | §15/§16/§18 flag the S&P contradiction and give KER precedence over the residual bullish read. The tension between a Transitional regime with expanding VOLator (§9) and RANGE-branch cards (§21b) is not reconciled. | §9, §15-§18, §21 | 3 |
| 4.4 Calibrated language | §17 is one sentence; confidence stated Medium in §3/§18. Slight hedge via "unless". | §3, §17 | 4 |
| 4.x Card construction (protocol) | Trade 2 and Trade 3B are built on the RANGE branch although §9 labels the regime Transitional and reports VOLator expanding (+0.45); M5 requires one regime label governing the run (Transition = breakout side only, Trade 3C). Trade 2 TP2 is +1.57R, not +2R. Trade 2 entry is not on any pivot tier of the data. Trade 2 should have been SUPPRESSED under the report's own §19 flag. Trade 3B entry sits at 63.0% of the 25-day range, outside the 11.4-21.4% band, and its invalidation equals its stop. Details in feedback. | §21b | 2 |
| 5.1 Data dated, staleness flagged | Articles and quotes dated; single-source O/H/L flagged. The 27 May "afternoon" print is presented as a close; Morningstar ETF note is an evergreen page dated 28 May. USDX 99.28 is an intraday print, not the D-1 close (99.023). | §4, §6, §10, §13a | 3 |
| 5.2 Assumptions up front | Indicative-pivot propagation to cards present; instruction to produce cards despite the flag is disclosed. Anchor/assumption caveat for Trade 3B and the proxy-open anchor is not stated on the cards or in §20 (07:00 UK appears only as the report timestamp). | §19, §20, §21b | 3 |
| 5.3 Red flags surfaced | Risk table present. The Tier-1 event named for D (US PCE) was already released on D-1 (Core PCE y/y 3.3 vs 3.1 consensus). Calendar rows scheduled for D that are missed: BoE Governor Bailey speech (HIGH, 12:10 broker = 10:10 UK), Euro-area CPI/HICP flash prints (10:00 broker = 08:00 UK), MNI Chicago Business Barometer (HIGH, 16:45 broker = 14:45 UK). Card caveats carry the wrong collision. | §13c, §13d, §21b | 2 |
| 5.4 Restrictions honoured | Breach. The 28 May close of 10,405 is a "weighted-median reference" built from range and intraday quotes; no source quotes it, yet it is labelled CORROBORATED (§6, §19) - a synthesised price presented as sourced (No-Synthesis rule). §19 itself says the close agrees only "within ~15 pts". Trade 2 is issued although §19 states every pivot tier is single-source-indicative, which M5 §5.2a requires to be suppressed. No module codes or bracketed variables found; counters and common names OK. | §3, §5, §6, §19, §21b | 1 |

## 2. Category 3 data comparison (report minus level file, cash basis)

OHLC (tolerance: close 5 pts, open/high/low 10 pts; a close beyond 15 pts is a Category 3 failure):

| Session | Open | High | Low | Close |
|---|---|---|---|---|
| Thu 21 May | 10,432 vs 10,371.1 = +60.9 FAIL | 10,470 vs 10,469.1 = +0.9 | 10,388 vs 10,344.7 = +43.3 FAIL | 10,423 vs 10,462.3 = -39.3 FAIL |
| Fri 22 May | 10,425 vs 10,492.6 = -67.6 FAIL | 10,488 vs 10,494.5 = -6.5 | 10,405 vs 10,446.0 = -41.0 FAIL | 10,466.26 vs 10,470.4 = -4.1 |
| Tue 26 May | 10,470 vs 10,531.9 = -61.9 FAIL | 10,520 vs 10,560.0 = -40.0 FAIL | 10,455 vs 10,498.0 = -43.0 FAIL | 10,498 vs 10,500.7 = -2.7 |
| Wed 27 May | 10,495 vs 10,487.7 = +7.3 | 10,515 vs 10,523.5 = -8.5 | 10,460 vs 10,460.6 = -0.6 | 10,487.29 vs 10,507.9 = -20.6 FAIL |
| Thu 28 May (D-1) | 10,437 vs 10,434.1 = +2.9 | 10,448 vs 10,446.6 = +1.4 | 10,381 vs 10,378.8 = +2.2 | 10,405 vs 10,432.4 = -27.4 FAIL |

Note: the 27 and 28 May closes (10,487.29 / 10,405) sit within 1-2 pts of the full-day CFD closes (10,488.2 / 10,407.1), but the report claims the cash basis, and the 21/22/26 May full-day values do not fit either. Basis is mixed, not consistently cash or full-day.

RSI2: report 0.0 for D-1; cash level file 8.71 (full-day 0.0). Arithmetic from the report's own closes reproduces (74.8, 0.0). ATR(14): not stated; cash 117.33, full 134.70.

Daily pivots (report built from 27 May H/L/C; level file is the D-1 cash session):

| Level | Report | Cash level file | Delta |
|---|---|---|---|
| R3 | 10,570 | 10,527.53 | +42.5 |
| R2 | 10,542 | 10,487.07 | +54.9 |
| R1 | 10,515 | 10,459.73 | +55.3 |
| P | 10,487 | 10,419.27 | +67.7 |
| S1 | 10,460 | 10,391.93 | +68.1 |
| S2 | 10,432 | 10,351.47 | +80.5 |
| S3 | 10,405 | 10,324.13 | +80.9 |

Weekly pivots (prior week 18-22 May): P 10,418 vs 10,368.7 (+49.3); R1 10,536 vs 10,596.2 (-60.2); R2 10,606 vs 10,722.0 (-116.0); S1 10,348 vs 10,242.9 (+105.1); S2 10,230 vs 10,015.4 (+214.6); R3/S3 not given (level file 10,949.5 / 9,889.6). The report's implied weekly H/L (10,488 / 10,300) excludes the 18 May low of 10,141.2 and the 22 May high of 10,494.5. Monthly pivots: absent (level file, April: P 10,418.8, R1 10,650.0, S1 10,140.1).

Counters (slice to D-1): USDX 28 May close 99.023 (report ~99.28, +0.26); S&P 500 close 7,578.2 (report "~7,520-7,563"); VIX 16.78 (report ~16-17, consistent).

## 3. Category roll-up

| Cat | Level | Multiplier | Points | Justification |
|---|---|---|---|---|
| C1 Prompt adherence (20) | 2 (raw 3, -1 override) | 0.40 | 8.0 | Variables mostly respected; no index/exchange/sell-side sources; date drift on PCE and pivot session; restriction breach lowers one level. |
| C2 Structure (20) | 3 | 0.65 | 13.0 | All 21 sections present and ordered; weekly pivots not a table, R3/S3 missing, monthly absent. |
| C3 Accuracy and evidence (25) | 2 | 0.40 | 10.0 | Half the OHLC fields and 3 of 5 closes outside tolerance, all daily/weekly pivots off, KER and ATR not reproducible, key figures unsourced; RSI2 arithmetic is sound. |
| C4 Reasoning and judgment (20) | 3 | 0.65 | 13.0 | Narrative reasoning is coherent and tensions flagged; cards built on a branch that contradicts the report's own regime label. |
| C5 Currency and transparency (15) | 2 | 0.40 | 6.0 | Dating is good; the Tier-1 catalyst is mis-dated, D events missed, a synthesised close is labelled corroborated. |

## 4. Total, band, override
Total = 8 + 13 + 10 + 13 + 6 = **50**. Band: **Low Trust (40-59)**.
Override: **restriction_breach** (synthesised 28 May close presented as corroborated; Trade 2 issued against the report's own all-indicative pivot flag). Category 1 reduced by one level; cap at Moderate (74) is not binding. No hallucinated-source override: no cited source is impossible on its face.

## 5. Card Integrity (linter rows copied verbatim from `qa/ftse_qa1/lint_static/2026-05-29.csv`)

| card_id | report_date | strategy | flags | dud | card score |
|---|---|---|---|---|---|
| 2026-05-29_Trade_1 | 2026-05-29 | Trade 1 - Daily Directional | SUPPRESSED | False | suppressed (excluded) |
| 2026-05-29_Trade_2 | 2026-05-29 | Trade 2 - Pivot, regime-aware (RANGE-fade) | CLEAN | False | 100 |
| 2026-05-29_Trade_3B | 2026-05-29 | Trade 3B - Mean-Reversion | CLEAN | False | 100 |

Report-level Card Integrity = mean(100, 100) = **100**; n_cards = 3 (2 scored), n_duds = 0, n_warns = 0. The static linter checks geometry only; the construction defects above (branch, TP2 = 2R, anchoring to the 25-day range, suppression gate) are scored in Category 4 and listed in the feedback.
