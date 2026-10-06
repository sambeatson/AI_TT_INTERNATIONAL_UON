# Trust Score v3.7 — FTSE 100 daily report, D = 2026-07-20 (run ftse_qa1)

Report: `reports/md/FTSE_EuroStoxx_Report_20Jul2026.md`
Level file: `data/levels/UK100_by_date/2026-07-20.csv` — `last_bar_date` = 2026-07-17 < D (checked). Slice last bar 2026-07-17 22:45 broker.
Basis claimed by the report: official FTSE cash index (so compared with the `_cash` fields; full-day `_full` fields noted where useful).
Stats command run: `qa_slice_stats.py --cash-open 10:00 --cash-close 18:30 --closes 10515.71 10529.39 10541.00 10572.24 10600.37`.

## Score line (machine-readable, one per line)
c1=4
c2=3
c3=0
c4=2
c5=3
total=48
band=Low
override=hallucinated_source
card_integrity=96.7
n_cards=3
n_duds=0
n_warns=1

## 0. Category 3 data checks (report vs level file / slice, cash basis)

### 0a. D-1 (Fri 17 Jul) and the five-day table. Tolerance: close ±5, open/high/low ±10 (brief §4)
| Session | Field | Report | Slice (cash) | Δ (report − slice) | Verdict |
|---|---|---|---|---|---|
| Fri 17 (D-1) | Open | 10,572.39 | 10,534.1 | +38.3 | FAIL |
| Fri 17 | High | 10,623.69 | 10,616.2 | +7.5 | ok |
| Fri 17 | Low | 10,527.65 | 10,514.9 | +12.8 | FAIL |
| Fri 17 | Close | 10,600.37 | 10,573.4 | +27.0 | FAIL (>15: Category 3 failure; full-day close 10,568.6 gives +31.8) |
| Thu 16 | O / H / L / C | 10,541.00 / 10,572.24 / 10,447.55 / 10,572.24 | 10,453.9 / 10,550.5 / 10,429.4 / 10,540.4 | +87.1 / +21.7 / +18.2 / +31.8 | all FAIL |
| Wed 15 | O / H / L / C | 10,529 / 10,560 / 10,500 / 10,541 | 10,460.7 / 10,536.2 / 10,431.0 / 10,498.7 | +68.3 / +23.8 / +69.0 / +42.3 | all FAIL (report flags the day single-source indicative) |
| Tue 14 | O / H / L / C | 10,515.00 / 10,545.00 / 10,433.12 / 10,529.39 | 10,460.4 / 10,545.8 / 10,411.5 / 10,507.0 | +54.6 / −0.8 / +21.6 / +22.4 | O, L, C FAIL |
| Mon 13 | O / H / L / C | 10,498.05 / 10,532.10 / 10,478.40 / 10,515.71 | 10,488.1 / 10,526.4 / 10,455.7 / 10,487.4 | +10.0 / +5.7 / +22.7 / +28.3 | L, C FAIL |

Pattern: every report close is 22–42 pts above the slice (not a "few points" basis effect). Every report open from Tue to Fri sits within 0.7 pt of the previous report close (10,515.00 vs 10,515.71; 10,529 vs 10,529.39; 10,541 vs 10,541.00; 10,572.39 vs 10,572.24), whereas the slice opens differ from the prior close by 27–55 pts. The opens read as carried-forward closes, not as sourced opens. Wed 15 O/H/L are round numbers (10,529 / 10,560 / 10,500). EURO STOXX Fri 17 open 6,270.94 = high 6,270.94 = Thu low 6,270.94 (report's own table).

### 0b. RSI2
| Session | Report | Cash-close RSI2 (slice) | Reproduces from the report's own closes? |
|---|---|---|---|
| Mon 13 | 100.0 | 100.00 | not testable (needs earlier closes) |
| Tue 14 | 100.0 | 100.00 | not testable |
| Wed 15 | 100.0 | 70.25 (Δ −29.8) | yes, 100 (arithmetic fine on report's closes; the closes themselves are wrong) |
| Thu 16 | 100.0 | 83.40 (Δ −16.6) | yes, 100 |
| Fri 17 | 100.0 | 100.00 | yes, 100 |

D-1 RSI2 = 100 agrees with `rsi2_cash` / `rsi2_full` = 100.0. Wed/Thu RSI2 do not agree: on the slice the 15 Jul cash close (10,498.7) is BELOW 14 Jul (10,507.0), so "five consecutive higher closes" (§1, §8, §20) and "RSI2 pinned at 100 for five sessions" (§1, §6, §15) are not supported. Report's EURO STOXX RSI2 values (57.2 / ~0 / 84.9 / 79.8 / ~0) reproduce from its own closes where testable (Wed 84.9, Thu 79.8, Fri ~0). Trend label error: FTSE Wed 15 is Close>Open with RSI2 100 but labelled Neutral (rule gives Bullish).

### 0c. ATR14 and KER
| Item | Report | Level file / slice | Δ |
|---|---|---|---|
| ATR(14) value | not stated anywhere in §9 or §21 | 120.51 (cash daily), 133.16 (full day) | missing |
| Card ATR (implied) | Trade 1: R = 84 "0.85 ATR" ⇒ ATR ≈ 98.8 | 120.51 | −21.7 (−18%); R = 0.70 ATR on the level file |
| KER(13, EMA3) value | not stated; described as "firmly in trending territory … approaches its upper bound" | raw KER13 = 0.114; smoothed (EMA3) = 0.086 cash, 0.069 full-day. Trend threshold is 0.13, neutral band ±0.09 | contradicts: smoothed KER sits in "Ranging — Neutral" |

### 0d. Pivots
Daily (report from 17 Jul H/L/C; the arithmetic reproduces exactly from the report's own H 10,623.69 / L 10,527.65 / C 10,600.37, so the error is the inputs):
| Level | Report | Level file `d_cash_*` | Δ |
|---|---|---|---|
| R3 | 10,736 | 10,722.7 | +13.3 |
| R2 | 10,680 | 10,669.5 | +10.5 |
| R1 | 10,640 | 10,621.4 | +18.6 |
| P | 10,584 | 10,568.2 | +15.8 |
| S1 | 10,544 | 10,520.1 | +23.9 |
| S2 | 10,488 | 10,466.9 | +21.1 |
| S3 | 10,448 | 10,418.8 | +29.2 |

Weekly (prior week 13–17 Jul = 2026-W29): 
| Level | Report | `w_cash_*` | Δ |
|---|---|---|---|
| R3 | absent | 10,860.6 | missing |
| R2 | 10,622 | 10,738.4 | −116.4 |
| R1 | 10,560 | 10,655.9 | −95.9 |
| P | 10,470 | 10,533.7 | −63.7 |
| S1 | 10,408 | 10,451.2 | −43.2 |
| S2 | 10,318 | 10,329.0 | −11.0 |
| S3 | absent | 10,246.5 | missing |

The weekly set does not reproduce even from the report's own week extremes (H 10,623.69, L 10,433.12, C 10,600.37 give P 10,552.4, R1 10,671.7, S1 10,481.1). Monthly pivots: ABSENT (level file June 2026: P 10,412.2, R1 10,698.1, S1 10,215.5, R2 10,894.8, S2 9,929.6, R3 11,180.7, S3 9,732.9). §11 tables are ordered S3→R3 (brief: R3→P→S3).

### 0e. Other claims checked against data
| Claim (location) | Data | Finding |
|---|---|---|
| "highest close of the month" (§1) | cash closes 2 Jul 10,654.0; 3 Jul 10,660.5; 7 Jul 10,680.1 (all above 10,573.4 and above the report's 10,600.37) | false |
| "five consecutive higher closes" (§1, §8, §20) | 15 Jul cash close 10,498.7 < 14 Jul 10,507.0 | false |
| Price "in the upper third" of 25-session range (§7) | 25d cash range 10,328.1–10,739.6; 10,573.4 is at 59.6% (upper third needs ≥ 10,602.6) | wrong |
| Close "just above weekly R1 (10,560)" (§11) | `w_cash_R1` = 10,655.9; close is 82.5 below it | wrong |
| VIX 18.77, +12% (§10, §14) | slice 17 Jul close 18.17, +3.2% (day high 18.57) | level above the day's high; move overstated ~4x |
| Dollar Index 100.76, −0.01% (§10) | slice 100.751, +0.04% | within noise |
| S&P 500 7,457.69, −1.01% (§10) | slice US500 7,455.3, −0.94% | within noise |
| "Wed 15 Softer US CPI" / "Tue 14 pre-US CPI caution" (§13c) | calendar: US CPI released Tue 14 Jul 15:30 broker (m/m −0.4 vs +0.5 consensus) | misdated by one session |
| §13c omits | BoE Bailey speeches 14 Jul (HIGH), US retail sales / Philly Fed 16 Jul (HIGH), EUR CPI y/y 17 Jul (2.8 vs 3.0) | calendar thin |
| DAX move −0.34% (§10) vs −0.35% (§12) | internal | minor mismatch |

## 1. Section 7 checklist
| Row | Notes | Evidence | Score |
|---|---|---|---|
| 1.1 Variables respected | FTSE 100 cash primary, Euro Stoxx reference only, 07:00 UK anchor, 5-session lookback, GBP/points, USDX/S&P/DAX counters present. Not met: sources are aggregators/media only (Yahoo, Trading Economics, Investing, Sharecast, "Sund.Guard."), no index-provider / exchange tier; Brent used heavily in §1/§12 but absent from §10 | §2, §4, §10, §20 | 3 |
| 1.2 Coverage & currency consistent | D-1 = 17 Jul throughout, lookback 13–17 Jul, GBP/points. Drift: US CPI placed on 15 Jul (was 14 Jul) | §2, §13c | 4 |
| 1.3 Audience & tone | Strategist / risk-review tone throughout; no retail language | §1, §18 | 4 |
| 2.1 Sections present & ordered | §1–§21 all present in order; §13a–d, §21a–d present; §17 is one sentence | headings | 5 |
| 2.2 Tables | §6 is a proper table with all required columns. §11 daily table has 3 levels each side but is ordered S3→R3; weekly table has only S2–R2; monthly pivots missing entirely | §6, §11 | 2 |
| 2.3 Method steps visible | §4–§5 observations → consensus shown; §8 candle-by-candle + sequence; §9 regime stated qualitatively with no numbers (no KER, ATR, overlap or VOLator figures); §7 charts are a prose list of "accompanying images" with no per-chart caption (accepted as placeholder, noted) | §4–§9 | 3 |
| 3.1 Quantitative claims sourced | §1 "highest close of the month" false; 52-week high 10,935 (§1, §7, §8, §15) has no source anywhere; Brent +4.6%, stock moves in §12, "80% overseas revenue" unsourced; VIX +12% wrong | §1, §12, §14 | 2 |
| 3.2 Citations exist & contain data | (i) Newsquawk quote "FTSE 100 +0.54% at 10,572" (§13a): the report's own table has Wed 10,541.00 → Thu 10,572.24 = +0.30%; +0.54% at 10,572 implies a prior close of ~10,515, which is Monday's close; Friday's level is 10,600. Quote cannot match any session in the report. (ii) "Sund.Guard." is Src A for Mon–Wed intraday O/H/L/C: a weekly Sunday title cannot be the source of Wed 15 Jul intraday figures; Wed values are round numbers. (iii) Trading Economics "~10,600" is described as corroborating 10,600.37 at "Δ<0.4" while §3/§20 state a ±0.10 tolerance: self-contradictory corroboration. Yahoo 17 Jul and Sharecast 16 Jul rows are consistent with §6 internally (but 27–32 pts above the slice) | §4, §6, §13a, §20 | 0 (hallucinated-source override) |
| 3.3 Calculations transparent | RSI2 reproducible from the report's closes (Wed–Fri); trend labels follow the rule except Wed 15; daily pivots reproduce from stated H/L/C; §21a score arithmetic checks (0.25+0.20+0.05+0.12+0.045+0.045 = 0.71). ATR(14) never stated as a number; KER(13,EMA3) never stated; weekly pivots do not reproduce from own H/L/C; Fri 17 Trade 2 backtest "P 10,505" does not equal Thu's own (H+L+C)/3 = 10,530.7 | §6, §9, §11, §21 | 3 |
| 3.4 Numbers reconcile | Close 10,600.37 consistent in §1/§3/§4/§6/§21b; daily pivots §11 = cards. Breaks: Trade 1 stop labelled "15 Jul close cluster" 10,516 but the report's 15 Jul close is 10,541 (10,516 ≈ 13 Jul close), and §19 says 15 Jul is excluded from entry/stop calcs; Trade 1 R "0.85 ATR" with no ATR stated (implies 98.8 vs 120.5); Trade 2 R = 96 vs stated "~106 pts" stop distance; Trade 1 TP1 10,685 described as "at daily R1 10,640" (45 pts away); §7 "modest upper wicks" Thu while Thu H = C = 10,572.24; DAX −0.34 vs −0.35 | cross-section | 2 |
| 4.1 Pillars conclude | §9 TREND UP and §10 MIXED labelled; §12 sub-items each labelled; §8 ends on levels with no explicit direction label; §14 ends on a VIX caution with no direction label | §8–§14 | 3 |
| 4.2 Cross-asset interpreted | Mechanisms given for USD, S&P, DAX (composition, dollar-earners, energy). Brent/oil, the driver of the thesis, is not a §10 row; cross-asset scored +0.30 (supportive) in §21a although §10 says two of three counters "contradict" and "contribute a mild drag" | §10, §20, §21a | 3 |
| 4.3 Synthesis reconciles tensions | RSI2 overbought vs trend addressed. Not reconciled: three different invalidation levels (§16 weekly pivot 10,470; Trade 1 10,544; Trade 2 10,488); KER vs regime (KER not shown, and slice KER is 0.086); sign of cross-asset signal vs §10 text | §15, §16, §18, §21 | 2 |
| 4.4 Calibrated language | §17 exactly one sentence, no stacked hedges; Confidence "High" in §3 is unsupported given Δ<0.4 vs ±0.10 tolerance and single-source O/H/L | §3, §17 | 3 |
| 4.x Card construction (protocol table) | Trade 1: no 0.25×ATR stop buffer; entry "≈10,600" not an explicit D-1 close; TP1 confluence claim wrong. Trade 2 built as a TREND card but violates the TREND formula (entry at P not P+0.10×(R1−P); stop S2-based not P−0.8×(P−S1); TPs not R1/R1.5/R2; TP3 R3 10,736 below TP2 10,776; R 96 vs 106). Trade 3A: entry at 38.2% not 57.5%; TP1/TP2 are 0%/extension not 38.2%/0%; stop not beyond the 0% anchor; swing below 2×ATR. Regime TREND_UP contradicted by KER. Detail in feedback | §21b | 1 |
| 5.1 Data dated; staleness flagged | Prices dated; Wed single-source flagged. §13a articles carry no dates; Mon/Tue/Thu/Fri O/H/L carried as CORROBORATED while opens equal prior closes | §4, §6, §13a | 3 |
| 5.2 Assumptions up front | 07:00 anchor and "Friday close reference" stated on Trade 1 and in §20; pivot-corroboration statement present. But entry/stop for Trade 1 use a 15 Jul level the report says is excluded; anchor-override (proxy open) caveat is not labelled as such | §19, §20, §21b | 3 |
| 5.3 Red flags surfaced | RSI2 overbought, PM transition, VIX, fragile global backdrop in §12/§15; PM event carried into all three card caveats | §12, §15, §21b | 4 |
| 5.4 Restrictions honoured | No bracketed names, no module codes, no framework name seen; futures/CFD not used. Concern: Tue–Fri opens equal the previous close and Wed 15 OHLC are round numbers (interpolated-looking prices tabled with named Src A); EURO STOXX Fri open = high = Thu low. Treated as a likely no-synthesis breach but reported as a concern only, because the hallucinated-source override already binds | §6 | 2 |

Category levels (mean of rows, rounded): C1 = (3+4+4)/3 = 3.67 → 4 · C2 = (5+2+3)/3 = 3.33 → 3 · C3 = (2+0+3+2)/4 = 1.75 → 2 before override, 0 after · C4 = (3+3+2+3+1)/5 = 2.4 → 2 · C5 = (3+3+4+2)/4 = 3.0 → 3.

## 2. Category roll-up
| Category | Level | Multiplier | Points / max | Justification |
|---|---|---|---|---|
| C1 Prompt adherence | 4 | 0.85 | 17.00 / 20 | Variables, anchor, lookback, currency honoured; source tiers are aggregator-only |
| C2 Structure | 3 | 0.65 | 13.00 / 20 | All 21 sections in order; pivot tables incomplete (weekly 2+2, monthly missing, wrong order); method numbers not shown |
| C3 Accuracy & evidence | 0 | 0.00 | 0.00 / 25 | Override: self-contradictory citations. Independently, D-1 close +27.0 vs slice, all five closes +22 to +42, weekly pivots off by up to 116 |
| C4 Reasoning & judgment | 2 | 0.40 | 8.00 / 20 | TREND_UP unsupported by KER; card levels break M5 formulas |
| C5 Currency & transparency | 3 | 0.65 | 9.75 / 15 | Dated and flagged in part; carried-forward opens and round Wed values; assumptions partly stated |

## 3. Total, band, override
Total = 17.00 + 13.00 + 0.00 + 8.00 + 9.75 = 47.75, rounded 48. Band Low (40–59). Cap check: Low cap (59) not binding.
Override: hallucinated_source (checklist 3.2 — Newsquawk quote impossible against the report's own figures; "Sund.Guard." cited as source of intraday figures for sessions it cannot have covered; TE "~10,600" accepted as corroboration beyond the report's stated tolerance). C3 set to 0. A restriction-breach (synthesised prices) concern is recorded under 5.4 but not applied separately.

## 4. Card Integrity (linter rows copied verbatim from `qa/ftse_qa1/lint_static/2026-07-20.csv`; separate from the 100)
| card_id | strategy | flags | dud | score |
|---|---|---|---|---|
| 2026-07-20_Trade_1 | Trade 1 - Daily Directional (LONG - TREND_UP regime) | CLEAN | False | 100 |
| 2026-07-20_Trade_2 | Trade 2 - Pivot (trend-pullback, TREND_UP) | WARN_TP3_ORDER | False | 90 |
| 2026-07-20_Trade_3A | Trade 3A - Momentum-Pullback (complex, TREND_UP fork) | CLEAN | False | 100 |

n_cards=3 (none suppressed), n_duds=0, n_warns=1, report-level Card Integrity = (100+90+100)/3 = 96.7.
Note: the linter is static (no market data). The CLEAN flags on Trade 1 and 3A do not mean the levels are compliant with M5; see the feedback file for the construction failures the static linter cannot see.
