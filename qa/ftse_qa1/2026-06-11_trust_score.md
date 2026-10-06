# Trust Score v3.7 - FTSE 100 daily report, D = 2026-06-11 (run ftse_qa1)

Report: `reports/md/FTSE_EuroStoxx_Report_11Jun2026.md`
Data basis: `data/levels/UK100_by_date/2026-06-11.csv` (`last_bar_date` = 2026-06-10, which is < D, so the file is leak-free). Slice last bar 2026-06-10 22:45 broker. Stats run with `--cash-open 10:00 --cash-close 18:30`. The report states a cash index, so the `_cash` basis is used throughout.

## Machine-readable result
```
c1=3
c2=3
c3=2
c4=3
c5=3
total=59
band=Low
override=none
card_integrity=80.0
n_cards=3
n_duds=1
n_warns=0
```
(`n_cards` counts all three card rows, including the suppressed Trade 2. Card Integrity is the mean over the 2 non-suppressed cards.)

## 1. Section 7 checklist

| Row | Reviewer notes | Evidence (location) | Score |
|---|---|---|---|
| 1.1 Variables respected | Asset (FTSE 100 cash, Euro Stoxx as reference only), as-of D, tz Europe/London, 5-session lookback, GBP/index points are all right. Counters USDX/S&P 500/DAX are named. Not met: (a) the source mix has no index-provider, exchange or sell-side tier (only Investing.com, Yahoo, Trading Economics, a BBN Times wrap, HoC Library, Newsquawk, AJ Bell), and §20 says "Barchart/Stooq not reached - proceeded on two-source corroboration"; (b) the 07:00 UK anchor was replaced by "European pre-open" with no clock time (§20, §21b). | §2, §4, §10, §20, §21b | 3 |
| 1.2 Coverage and currency consistent | Currency consistent. Dates drift: the 10-Jun close 10,243.00 is sourced to an "intraday" Investing.com quote (§4). Trading Economics "9 Jun close ≈10,243" is the same number as the report's 10-Jun close (§4). The §10 S&P 500 ≈7,387 / −0.26% is the 9-Jun level (slice: 9 Jun close 7,383.6, −0.31%; 10 Jun close 7,261.5, −1.65%), so it is stale by a session and undated. | §4, §6, §10 | 3 |
| 1.3 Audience and tone | Strategist tone, trading and risk-review framing, disclaimer present, no retail tone. | §1, §18, §21d | 4 |
| 2.1 Sections present and ordered | §1-§21 and 21a-d are all present in order. Deviations: §7 has a bare heading with no caption or placeholder (charts not evidenced); §13 is lettered 13a aggregate / 13c divergence / 13d (previous and upcoming merged) instead of 13b numeric tilt / 13c previous-period calendar / 13d upcoming calendar; §6 has no separate Source A / Source B / Final columns. | headings | 4 |
| 2.2 Scorecard as a table | §6 is a table, but Sources A and B are merged into one column and there is no Final column. §11: daily table runs S3→R3 (brief wants R3→P→S3); weekly has only S2..R2 (R3 and S3 missing); monthly pivots are absent altogether. | §6, §11 | 2 |
| 2.3 Method steps visible | §4-§5 show observations to consensus. §8 discusses only 4 of the 5 candles and never lists the 4 Jun candle. §9 gives KER and VOLator qualitatively, with no persistence/overlap evidence and no ATR value. §9 cites "25-session structure (see §7)" but §7 is empty. | §4-§9 | 3 |
| 3.1 Quantitative claims sourced | Unsourced or undated: §10 counter levels (USDX ≈99.3, S&P ≈7,387, DAX ≈24,433); GBP/USD 1.337 and GBP/EUR ~1.159 (§12, §14); GSK -0.3% / AZN -1-2%; ECB staff 2.6%; BoE/UK CPI timing. UK CPI "~3.3%" cites no source, while the cited HoC quote says 3.1% for Q2. §19 admits the counters are "single-quote directional reads". | §10, §12, §14, §19 | 2 |
| 3.2 Citations exist and contain data | Three spot-checks. (i) Investing.com 10-Jun "10,243 / range 10,128-10,264": the range reproduces against the slice's 10-Jun cash low/high (10,126.2 / 10,267.5, Δ −2 / −4), so the source appears genuine. But §5 and §6 then quote the same session's low as ~10,180, a self-contradiction inside the report. (ii) Trading Economics "9 Jun close ≈10,243 / 10,227": 10,243 is the report's own 10-Jun close, so the item is mis-dated. (iii) HoC Library "CPI projected 3.1% Q2": is a projection and is not reconcilable with the "3.3%" used in §12/§14. Yahoo's 9-Jun low of 10,127.60 does not exist on 9 Jun in the slice (9-Jun cash low 10,240.5, full-day 10,183.4); the figure matches the 10-Jun low and was attributed to the wrong day. I judged this misdating and not an invented source, so the hallucinated-source override is not applied, but it is borderline. | §4, §5, §6, §13a | 2 |
| 3.3 Calculations transparent | RSI2 for 8, 9, 10 Jun reproduces exactly from the report's own closes (84.2 / 0.0 / 9.7). The 4 and 5 Jun values cannot be tested. Trend labels follow the stated rule. Daily pivots are reproducible from the stated 10-Jun H/L/C (P 10,228.9 etc.). KER ≈0.40 reproduces on cash closes (0.416, 13 sessions), but the EMA(3) smoothing is not shown. Missing: ATR(14) is never stated (cash 96.72 / full 123.02); §21a gives "≈ -0.30" with no signal × weight table (weights 0.25/0.20/0.10/0.15/0.15/0.15 not shown). | §6, §9, §11, §21a | 2 |
| 3.4 Numbers reconcile | D-1 close 10,243 is identical in §1, §3, §4, §6, §21b entry. Breaks: (1) §3 says the anchor is "just under the 10,228 daily pivot" and §11/§21b say "just above the daily pivot (10,229)"; (2) §16 quotes S2 10,075 / S3 10,023 while §11 gives S2 10,145 / S3 10,110; (3) 10-Jun low is 10,128 (§4), ~10,180 (§5, §6); (4) stop 10,361 is described as "above R3" but §11 R3 = 10,362; (5) §11 calls ~10,128 "S3 region" while S3 = 10,110; (6) the implied prior-week high from the §11 weekly tiers is ≈10,451, above any high in §6 for 1-5 Jun (max 10,402); (7) §21d hit rate TP1 75% against §21c (only one of four triggered trades reaches ≥ +1R); (8) §21c 10 Jun row "Triggered NO" yet "OPEN @ +0.1R". Against the slice (section 2 below), only 4 of 20 OHLC fields are within tolerance, with 4 Jun and 5 Jun closes off by −57.6 and +19.2 (> 15 pts, a Category 3 failure) and the 9-Jun low off by −112.9. | whole report | 1 |
| 4.1 Pillars conclude | §8 and §9 conclude (TRANSITION, base-building); §10 gives an aggregate signal; §12 and §14 end on the ECB watch item and have no direction label. | §8-§14 | 3 |
| 4.2 Cross-asset interpreted | §10 gives a short mechanism per counter (dollar translation, risk-off alignment), but S&P 500 and DAX reads are close to correlation statements. There is no dollar-earner, energy-weight or oil counter link, and the USDX "soft" read is not supported by the slice (D-1 close 100.06). | §10 | 3 |
| 4.3 Synthesis reconciles tensions | §15/§16/§18 address oversold RSI2 against the bearish tilt, and §21a states "no conflict" with §17. But §21a counts the oversold RSI2 as a bearish contributor without a number, and the §3 vs §11 pivot-position contradiction is never reconciled. §16 range 10,150-10,360 and S2/S3 are inconsistent with §11. | §15-§18, §21a | 3 |
| 4.4 Calibrated language | §17 is one sentence with a confidence frame (H on level / M on direction in §3/§18). It carries a lead-in clause and mild hedging ("most likely", "modestly lower-biased"). | §3, §17, §18 | 4 |
| 4.5 (protocol) Card construction | Trade 1 passes the linter but does not follow the M5 stop rule (stop 10,361 equals R3 less 1, no 0.25×ATR buffer, no ATR stated), offers two entry modes, and has no clock time on the anchor. Trade 2 suppression logic is wrong (S-tiers only, whereas every daily tier depends on the D-1 low, and TRANSITION is breakout-side-only anyway). Trade 3C is a linter DUD: no stop price, two-sided direction, range 10,128-10,371 is not the 25-day range (cash 10,126.2-10,560.0), TP2 missing. Details in the feedback file. | §21b | 2 |
| 5.1 Data dated; staleness flagged | The single-source low is flagged. Counters are undated and the S&P level is one session stale. The 10-Jun close is cited to an intraday print. | §4, §6, §10, §19 | 3 |
| 5.2 Assumptions up front | The anchor override is mentioned only in §20 ("European pre-open ... per run instruction") with no clock time and not on the card. Single-source propagation to the card caveat is present. | §20, §21b | 3 |
| 5.3 Red flags surfaced | ECB, oversold RSI2, bank selloff and the weekly-pivot invalidation are surfaced. Carried into cards: ECB only. Omitted from §13d and the card caveats: US PPI m/m and Initial Jobless Claims (HIGH, 13:30 UK on 11 Jun), US CPI on 10 Jun (HIGH, previous period), ECB press conference 13:45 UK and Lagarde speech 15:15 UK, US 30-Year Bond Auction (HIGH, 18:00 UK). All fall inside or adjacent to the 07:00-16:30 UK holding window. | §12, §13d, §21b | 3 |
| 5.4 Restrictions honoured | No bracketed variable names, no framework name, FTSE futures not used, no synthetic prices evidenced. Concerns: "M-downstream strategy logic" (§19) is a module-code fragment; "Step-4", "dual-gate" are prompt-internal jargon; Trading Economics, self-described "Cash CFD-tracked", is used as Source B for the 9 and 10 Jun closes; the 10-Jun close is presented as validated from an intraday quote. Assessed as minor and not an open breach. | §6, §9, §19 | 3 |

Row note for 3.4: the OHLC comparison against the slice is tabulated in section 2 and is the main evidence for the 3.4 score.

## 2. Category 3 evidence - report vs level file (cash basis; Δ = report − file)

OHLC (tolerance: close ±5, open/high/low ±10):

| Date | Field | Report | Cash file | Δ | In tol. |
|---|---|---|---|---|---|
| 04 Jun | O / H / L / C | 10,318 / 10,358 / 10,268 / 10,285.66 | 10,301.0 / 10,360.2 / 10,236.5 / 10,343.3 | +17.0 / −2.2 / +31.5 / −57.6 | N / Y / N / N |
| 05 Jun | O / H / L / C | 10,286 / 10,402 / 10,280 / 10,393.40 | 10,383.0 / 10,417.0 / 10,331.9 / 10,374.2 | −97.0 / −15.0 / −51.9 / +19.2 | N / N / N / N |
| 08 Jun | O / H / L / C | 10,393 / 10,430 / 10,358 / 10,373.20 | 10,309.9 / 10,412.8 / 10,307.1 / 10,370.4 | +83.1 / +17.2 / +50.9 / +2.8 | N / N / N / Y |
| 09 Jun | O / H / L / C | 10,372.77 / 10,372.77 / 10,127.60 / 10,227.33 | 10,353.9 / 10,368.7 / 10,240.5 / 10,240.7 | +18.9 / +4.1 / −112.9 / −13.4 | N / Y / N / N |
| 10 Jun (D-1) | O / H / L / C | 10,227.38 / 10,263.81 / 10,180 / 10,243.00 | 10,251.2 / 10,267.5 / 10,126.2 / 10,256.3 | −23.8 / −3.7 / +53.8 / −13.3 | N / Y / N / N |

4 of 20 fields in tolerance. Closes off by more than 15 pts: 4 Jun (−57.6), 5 Jun (+19.2). Other claims: "245-point range on 9 Jun" against a cash range of 128.2 (full day 192.2); "1.4% drop on 9 Jun" against −1.25% cash; "swing high 10,430" against the 5-day cash swing high 10,417.0; 10-Jun low "~10,180, demand re-emerging" against a D-1 cash low of 10,126.2. The report's 9-Jun low (10,127.60) matches the D-1 low and appears shifted a day.

RSI2: report 61.2 / 70.8 / 84.2 / 0.0 / 9.7 against cash-slice 4.51 / 100.00 / 89.05 / 0.00 / 10.74. The last three reproduce from the report's own closes (84.2, 0.0, 9.7 exact). ATR14 not stated (file: cash 96.72, full 123.02).

Daily pivots (report from 10-Jun H/L/C vs cash file):

| | S3 | S2 | S1 | P | R1 | R2 | R3 |
|---|---|---|---|---|---|---|---|
| Report | 10,110 | 10,145 | 10,194 | 10,229 | 10,278 | 10,313 | 10,362 |
| Cash file | 10,024.53 | 10,075.37 | 10,165.83 | 10,216.67 | 10,307.13 | 10,357.97 | 10,448.43 |
| Δ | +85.5 | +69.6 | +28.2 | +12.3 | −29.1 | −45.0 | −86.4 |

Weekly pivots (report vs cash file, week 2026-W23): P 10,371 vs 10,342.57 (+28.4); R1 10,473 vs 10,448.63 (+24.4); S1 10,291 vs 10,268.13 (+22.9); R2 10,553 vs 10,523.07 (+29.9); S2 10,189 vs 10,162.07 (+26.9). R3/S3 (10,629.13 / 10,087.63) not given. Monthly pivots (May cash: P 10,370.40, R1 10,599.60, S1 10,180.80, R2 10,789.20, S2 9,951.60, R3 11,018.40, S3 9,762.00) are absent.

Counters against slices (broker-feed CFD): USDX D-1 close 100.059 against report ≈99.3 (Δ ≈ −0.76); S&P 500 report ≈7,387 / −0.26% equals the 9-Jun close (7,383.6), D-1 close 7,261.5. DAX not in the slices (not checked).

## 3. Category roll-up

| # | Category | Level | Multiplier | Max | Points | Justification |
|---|---|---|---|---|---|---|
| 1 | Prompt adherence | 3 | 0.65 | 20 | 13.00 | Right asset/window/currency; sources lack index/exchange/sell-side tiers; 07:00 UK anchor replaced by an untimed "pre-open" |
| 2 | Structural alignment | 3 | 0.65 | 20 | 13.00 | All sections present; pivot tables incomplete (weekly R3/S3, monthly missing), §7 empty, §13 re-lettered |
| 3 | Accuracy and evidence | 2 | 0.40 | 25 | 10.00 | 4 of 20 OHLC fields in tolerance, two closes > 15 pts wrong, 9-Jun low wrong by 113, pivots up to 86 pts off, many internal reconciliation breaks, no ATR, no §21a derivation |
| 4 | Reasoning and judgment | 3 | 0.65 | 20 | 13.00 | Regime and synthesis reasonable; card construction weak (one DUD, unsound Trade 2 suppression) |
| 5 | Currency, restrictions, transparency | 3 | 0.65 | 15 | 9.75 | Single-source flag good; stale/undated counters, vague anchor caveat, missed Tier-1 US data collisions |

## 4. Total, band, override
Total = 13.00 + 13.00 + 10.00 + 13.00 + 9.75 = 58.75, rounded to **59**. Band: **Low** (40-59).
Override check: none. No source established as invented (the cited Investing.com range reproduces against the slice), and no restriction judged openly breached (see rows 3.2 and 5.4 for the borderline items).

## 5. Card Integrity (linter rows copied verbatim from `qa/ftse_qa1/lint_static/2026-06-11.csv`)

| card_id | strategy | flags | dud | per-card score |
|---|---|---|---|---|
| 2026-06-11_Trade_1 | Trade 1 - Daily Directional (SHORT - TRANSITION/bearish tilt) | CLEAN | False | 100 |
| 2026-06-11_Trade_2 | Trade 2 - Pivot (regime-aware) | SUPPRESSED | False | excluded |
| 2026-06-11_Trade_3C | Trade 3 - Complex (regime-driven, TRANSITION -> 3C breakout-side) | UNPRICED | True | 60 |

Report-level Card Integrity = mean(100, 60) = **80.0** (separate from the 100). n_cards=3, n_duds=1, n_warns=0.

Feedback: `qa/ftse_qa1/2026-06-11_feedback.md`.
