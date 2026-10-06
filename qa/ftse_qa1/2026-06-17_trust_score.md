# Trust Score v3.7 QA - FTSE 100 daily report, D = 2026-06-17 (run ftse_qa1)

Report: `reports/md/FTSE100_Report_17Jun2026.md`
Data basis: `data/levels/UK100_by_date/2026-06-17.csv` (last_bar_date = 2026-06-16 < D, checked) and the UK100 / USDX / US500 / VIX / NEWS slices up to 2026-06-16.
The report states a cash-index basis, so the `_cash` columns are the primary comparison and `_full` is given in brackets. Tolerances are the brief's: close within 5 points, O/H/L within 10 points. A close more than 15 points out, or an RSI2 that does not reproduce, is a Category 3 failure.

## Scores (machine-readable)
```
c1=2
c2=3
c3=2
c4=3
c5=3
total=54
band=Low
override=restriction_breach
card_integrity=100
n_cards=3
n_duds=0
n_warns=0
```
The override is the breach of the no-module-codes restriction (row 5.4). C1 was 3 before the override and is lowered one level to 2. The Moderate cap of 74 is not binding at 54. No fabricated source was established, so the hallucinated-source override is not applied (see 3.2).

## 1. Section 7 checklist

| Row | Notes | Evidence (location) | Score |
|---|---|---|---|
| 1.1 Variables respected | FTSE 100 cash is the asset, with Euro Stoxx 50 as a reference and no cards on it. Counters are USDX, S&P 500 and DAX 40, all defined in the header and §10. As-of is London D-1, lookback is 5 sessions (10-16 Jun), and units are GBP index points. The daily-open anchor was "overridden" from 07:00 UK, but the replacement time is never stated (§20, §21b Trade 1). The §4 "six independent observations" are really TE (twice, on different dates), Investing, Yahoo, 30rates and a quote-less LSE widget. Only two sources cover D-1, and there is no sell-side or index-provider quote. Trading Economics is labelled "CFD-tracked cash" and is Source A for the 15 and 16 Jun closes. | §2, §4, §6, §20, §21b | 3 |
| 1.2 Coverage and currency consistent | §2/§4/§6 are consistent on 16 Jun as D-1. Drift points: (a) §21c lists "Wed 17 Jun (t-1)", which is D itself, and labels 16 Jun as t-2, so the t-N labels are shifted by one session; (b) §13d dates UK April GDP -0.1% to Mon 15 Jun, but the calendar slice has it on Fri 12 Jun 09:00 broker; (c) §16 base range 10,360-10,490 differs from the §17 range 10,415-10,490. | §21c, §13d, §16/§17 | 3 |
| 1.3 Audience and tone | Professional risk-review tone. There is no retail language, and the disclaimer is present. | whole report | 4 |
| 2.1 Sections present and ordered | §1-§21 are all present and in order, including §21a-d with the limitations boilerplate. §13 is mis-structured: 13a is per-article, 13b is aggregate, but "13c" is a divergence flag and "13d" is the previous-period calendar with an unlabelled upcoming table. The brief expects 13c = previous-period calendar and 13d = upcoming calendar. | headings | 4 |
| 2.2 Scorecard as a table / pivot tables | §6 is a table but has no "Final" column. §11 gives only S2/S1/P/R1/R2 in ascending order. The brief requires R3 to S3 (three levels each side) for each timeframe. The monthly row has blanks for S2 and R2. | §6, §11 | 2 |
| 2.3 Method steps visible | §4-§5 show observations to consensus. §8 is candle-by-candle with a sequence read. §9 gives KER 0.45 and a "flat" VOLator slope but no numbers, ATR value, persistence or overlap figures. §7 describes five chart surfaces in prose and refers to a "companion CSV / PNG" that is not in the deliverable. A caption placeholder is acceptable to the brief but the numbers it describes are wrong (see 3.4). | §4-§9 | 3 |
| 3.1 Quantitative claims sourced | Many figures are unsourced: "+17% YoY", "~0.5% from February record", gilt 4.88%, GBP/USD 1.334, EUR/USD 1.152, CPI 2.8%, Bank Rate 3.75%, bank moves "+0.4-0.6%", and counters "≈7,384" and "≈23,950" with no source. The §10 S&P 500 level and move are wrong against the feed (see 3.4). | §1, §10, §12, §14 | 2 |
| 3.2 Citations exist and contain data | I cannot fetch. Three spot checks: (i) TE 15 Jun "FTSE decreased 38 points" is consistent with the report's own 10,433 / 10,471.72. (ii) Yahoo and 30rates 12 Jun 10,471.72 are identical and self-consistent with +1.63%. (iii) TE 16 Jun "+12 pts / flat to slightly higher" is consistent with the report's own 10,445, but not with the feed (+69 cash). No source is self-contradictory or impossible, so no fabrication is established. However, every close except 11 Jun is outside tolerance against the feed (see 3.4). TE 16 Jun is counted twice in 13a (Bullish and Neutral), which inflates the article count. | §4, §13a | 2 |
| 3.3 Calculations transparent | RSI2 reproduces from the report's own closes (85.2 / 81.3 / 23.7, checked with `--closes`), and the Trend labels follow the rule. §21a is Σ signal × weight with the locked weights, which sum to 1.00 and total +0.098, so +0.10 is correct. Failures: (a) the daily pivots do not reproduce from the report's own H/L/C (10,468 / 10,412 / 10,445), which give P 10,441.7, R1 10,471.3, S1 10,415.3, R2 10,497.7, S2 10,385.7, against the report's 10,444 / 10,469 / 10,421 / 10,492 / 10,396; (b) ATR(14) is never stated anywhere; (c) KER 0.45 and the EMA 3 are asserted without working; (d) the 13b tilt +0.20 has no derivation (a simple count gives +0.33). | §6, §9, §11, §13b, §21a | 3 |
| 3.4 Numbers reconcile (internal and to feed) | Internal: D-1 close 10,445 is consistent in §1/§3/§4/§6/§18, and the §11 pivots are the ones quoted on the cards. Breaks: §3 range top 10,470 vs §6 high 10,468; §16 vs §17 ranges; the §21c 11 Jun Trade 3C exit 10,471 exceeds the report's own 11 Jun high of 10,420; Trade 3C TP1 "100%" hit-rate vs a +0.1R result; Trade 2 "1/2 triggered" with one row. The §6/§19 text says the 16 Jun H/L is corroborated, but §11 says every pivot tier is indicative. Against the feed (cash basis, brackets = full): the D-1 close is 10,445 vs 10,510.1 (10,472.3), a miss of 65.1 (27.3). The 10 Jun close misses by 76.7 (138.4). The 16 Jun high is 61.6 low, and 15 Jun O/H is 97.6 / 100.6 low. RSI2 on 16 Jun is 23.7 vs 79.0 cash (55.6 full). S&P 500 is "≈7,384, -2.6%" vs a 16 Jun close of 7,517.4 and a move of -0.56% (7,383.6 was the 9 Jun close). Full table in section 2 below. | §1, §3, §6, §10, §11, §21c | 2 |
| 4.1 Pillars conclude | §8 ends "neutral with mild downward tilt", §9 TRANSITION, §10 CONTRADICT. §12 carries per-bullet tags but no closing direction. §14 ends on watch items with no direction label. | §8-§14 | 3 |
| 4.2 Cross-asset interpreted | §10 gives mechanisms (global beta; defensive/energy weight) but they rest on wrong counter data (S&P 500 and the DAX "rout"). The FX logic is internally contradictory: §10/§12/§14 call a softer dollar a tailwind for FTSE overseas-earnings translation, while §12/§13d/§15 say a stronger GBP is a translation drag. A weaker USD (GBP/USD ~1.334) is a headwind for dollar earnings. No oil counter is tabled although oil is the first driver in §1. | §10, §12, §14 | 2 |
| 4.3 Synthesis reconciles tensions | §21a explicitly addresses the §17 vs conviction conflict. Short-term stall vs medium-term uptrend and KER vs VOLator are resolved to TRANSITION. The §13c sentiment vs cross-asset divergence is weighed. The tension is resolved only on the report's own (mis-stated) inputs. | §9, §13c, §15-§18, §21a | 4 |
| 4.4 Calibrated language | §17 is one sentence with no hedge stacking. Confidence is stated in §3 (Medium) and §18. §17 has no confidence tag, and its range differs from §16. | §3, §16-§18 | 4 |
| Card construction (M5; C4 protocol row) | See section 4 and the feedback file. Trade 1 suppression is arithmetically correct on the report's inputs. Trade 2 stages two-sided reaction entries in a TRANSITION regime, which should be breakout side only. Its R of about 30 is below 0.3 × ATR14 (34.0 cash / 41.8 full), it has no numeric TP2/TP3, and TP1 = P 10,444 is +23, not +1R (+30). Trade 3C uses an invented 25-day range, TP = 1R/2R instead of 1.0 / 1.5 × width, stop = daily P instead of low + 0.40 × width, and the invalidation level equals the stop. Entry sits 3-4 points beyond the boundary instead of ≥ 0.25 × ATR14. | §21b | 2 |
| 5.1 Data dated; staleness flagged | Prices and articles are dated except the AJ Bell "ctx" row in 13a. Single-source O/H/L are flagged. Staleness of the S&P 500 and DAX counters is not recognised (S&P 7,384 is the 9 Jun close). | §4, §6, §13a, §19 | 4 |
| 5.2 Assumptions up front | The anchor-override caveat is present in §20 and on the Trade 1 row, but the override time is never given and it is absent from §1. The pivot-indicative flag does propagate to the §21 cards. | §20, §21b, §19 | 3 |
| 5.3 Red flags surfaced | §12/§15 give the CPI/BoE risks, and the §13d collision is carried into the 3C caveat. The calendar slice shows D events omitted from §13d: the Fed rate decision (21:00 broker = 19:00 UK) with FOMC statement and 21:30 press conference, US retail sales (15:30 broker), euro-area flash CPI (12:00 broker) and Lagarde (13:50 broker). The BoE 18 Jun date cannot be confirmed from the supplied calendar, which ends at D. | §13d, §15 | 3 |
| 5.4 Restrictions honoured | Breach: bracketed module codes "[M3]", "[UPD]", "[M5]" appear in the headings of §6-§9, §10-§14, §20 and §21, and §19 says "the contract M5 reads". The brief prohibits bracketed variable names and module codes. Also, a CFD-tracked source is used as Source A in the OHLC basis. | headings, §19, §6 | 1 |

## 2. Category 3 discrepancy log (report vs level file / slice)

Deltas are report minus feed, in points. The cash column is the stated basis and the full column is in brackets.

| Date | Field | Report | Cash (Full) | Δ cash (Δ full) | Verdict |
|---|---|---|---|---|---|
| 16 Jun (D-1) | Open | 10,433 | 10,449.3 (10,411.0) | -16.3 (+22.0) | outside 10 |
| 16 Jun | High | 10,468 | 10,529.6 (10,529.6) | -61.6 (-61.6) | outside |
| 16 Jun | Low | 10,412 | 10,434.9 (10,409.4) | -22.9 (+2.6) | outside on cash |
| 16 Jun | Close | 10,445 | 10,510.1 (10,472.3) | -65.1 (-27.3) | fail (>15) |
| 16 Jun | RSI2 | 23.7 | 79.0 (55.6) | -55.3 (-31.9) | fail |
| 15 Jun | O / H / L / C | 10,460 / 10,474 / 10,405 / 10,433 | 10,557.6 / 10,574.6 / 10,422.8 / 10,441.2 | -97.6 / -100.6 / -17.8 / -8.2 | O, H, L outside; C in 5-15 band |
| 12 Jun | O / H / L / C | 10,310 / 10,485 / 10,300 / 10,471.72 | 10,368.9 / 10,473.5 / 10,368.3 / 10,459.5 | -58.9 / +11.5 / -68.3 / +12.2 | O, L, H outside; C in 5-15 band |
| 11 Jun | O / H / L / C | 10,333 / 10,420 / 10,295 / 10,303.7 | 10,238.9 / 10,373.4 / 10,235.8 / 10,299.9 | +94.1 / +46.6 / +59.2 / +3.8 | only C within tolerance |
| 10 Jun | O / H / L / C | 10,318 / 10,360 / 10,288 / 10,333 | 10,251.2 / 10,267.5 / 10,126.2 / 10,256.3 | +66.8 / +92.5 / +161.8 / +76.7 | fail |
| ATR14 | - | not stated | 113.31 (139.49) | n/a | missing |
| Daily P / R1 / R2 / S1 / S2 | §11 | 10,444 / 10,469 / 10,492 / 10,421 / 10,396 | 10,491.5 / 10,548.2 / 10,586.2 / 10,453.5 / 10,396.8 | -47.5 / -79.2 / -94.2 / -32.5 / -0.8 | fail except S2 |
| Weekly P / R1 / R2 / S1 / S2 | §11 | 10,415 / 10,542 / 10,612 / 10,345 / 10,218 | 10,353.1 / 10,579.9 / 10,700.4 / 10,232.6 / 10,005.8 | +61.9 / -37.9 / -88.4 / +112.4 / +212.2 | fail |
| Monthly P / S1 / R1 | §11 | 10,360 / 10,180 / 10,720 | 10,370.4 / 10,180.8 / 10,599.6 | -10.4 / -0.8 / +120.4 | R1 fails, P borderline |
| R3 / S3 (all timeframes) | §11 | absent | present in feed | n/a | missing rows |
| 25-day range | §7 / §21b | 10,300-10,485 | 10,126.2-10,574.6 (cash) | low +173.8 / high -89.6 | wrong |
| 5-day swing high | §1, §7, §21b | "10,470-10,485 supply" | 10,574.6 on 15 Jun | the 10,485 shelf was exceeded by 89.6 on 15 Jun and by 44.6 on 16 Jun | narrative contradicted |
| USDX | §10 | 99.57, -0.06% | 99.573, -0.11% | ok / -0.05 pp | consistent |
| S&P 500 | §10 | ≈7,384, -2.6% | 7,517.4, -0.56% (15 Jun +1.69%) | -133.4 pts | wrong and stale |
| DAX 40 | §10 | ≈23,950, -2.1% | no DAX slice supplied | n/a | cannot verify (this contradicts the S&P move) |
| KER(13) | §9 | ≈0.45 | ≈0.10 (my rough recompute from cash closes, using a simple 13-session net/path ratio, not the engine's EMA-3 form) | n/a | indicative only; below the 0.13 trend threshold the report cites |

No bars after D-1 were used.

## 3. Category roll-up

| # | Category | Level | Multiplier | Points | Justification |
|---|---|---|---|---|---|
| 1 | Prompt adherence (20) | 2 (3 before override) | 0.40 | 8.00 | The variables are mostly respected, but the anchor override time is unstated and the source count is padded. The module-code breach lowers it one level. |
| 2 | Structure (20) | 3 | 0.65 | 13.00 | All sections are present. The pivot tables lack R3/S3 and the ordering, §13 sub-sections are mislabelled, and the §6 table lacks its Final column. |
| 3 | Accuracy and evidence (25) | 2 | 0.40 | 10.00 | The D-1 close is 27-65 points off and RSI2 differs by 32-55 points. Daily, weekly and monthly pivots are all wrong. The S&P 500 counter is stale or wrong. The daily pivot arithmetic does not reproduce, and ATR is missing. RSI2 arithmetic and the §21a sum are correct. |
| 4 | Reasoning and judgment (20) | 3 | 0.65 | 13.00 | The synthesis and regime logic are coherent but rest on wrong inputs. The FX mechanism is contradictory, and card construction is non-compliant. |
| 5 | Currency and transparency (15) | 3 | 0.65 | 9.75 | Data are dated and indicative flags are propagated. The restriction is breached (module codes), the override time is missing, and D-day Fed/US/EZ events are omitted. |

Total = 8.00 + 13.00 + 10.00 + 13.00 + 9.75 = 53.75, rounded to **54**.
Band: **Low (40-59)**.
Override check: restriction_breach applied (C1 lowered 3 to 2). The Moderate cap (≤74) is not binding. Hallucinated source: not triggered, because no source was shown to be fabricated or impossible.

## 4. Card Integrity (linter rows, copied verbatim; separate from the 100)

| card_id | strategy | flags | dud |
|---|---|---|---|
| 2026-06-17_Trade_1 | Trade 1 - Daily Directional | SUPPRESSED | False |
| 2026-06-17_Trade_2 | Trade 2 - Regime-Aware Pivot (TRANSITION) | SUPPRESSED | False |
| 2026-06-17_Trade_3C | Trade 3C - TRANSITION Breakout | CLEAN | False |

Per card: Trade 1 and Trade 2 are suppressed and excluded; Trade 3C scores 100 − 40·0 − 10·0 = 100.
Report-level Card Integrity (mean over non-suppressed cards) = **100**. n_cards = 3, n_duds = 0, n_warns = 0.

The static linter only checks internal geometry on the long variant that was transcribed. It cannot see the rule-level defects in the feedback file: the wrong range, TP and stop formulas, invalidation equal to stop, and a trigger that sits below the cash close. The 100 is therefore not evidence that the card is compliant. These defects are scored under Category 4.

## 5. Feedback
See `qa/ftse_qa1/2026-06-17_feedback.md`.
