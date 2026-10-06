# Trust Score v3.7 - FTSE 100 daily report, 23 Jun 2026

Report: `reports/md/FTSE_EuroStoxx_Daily_23Jun2026.md` · D = 2026-06-23 · level file `last_bar_date` = 2026-06-22 (< D, leak-free) · basis claimed by the report: cash, D-1 = 22 Jun.

```
c1=3
c2=4
c3=2
c4=2
c5=3
total=58
band=Low
override=restriction_breach
card_integrity=100.0
n_cards=3
n_duds=0
n_warns=0
```

## 1. Category 3 data check (report vs `UK100_by_date/2026-06-23.csv`, cash basis; tolerance close 5 / O,H,L 10 pts)

| Item | Report | Level file (cash) | Delta | Verdict |
|---|---|---|---|---|
| D-1 (22 Jun) Open | 10,383 | 10,379.2 | +3.8 | OK |
| D-1 High | 10,439 | 10,441.4 | -2.4 | OK |
| D-1 Low | 10,346 | 10,343.2 | +2.8 | OK |
| D-1 Close | 10,439 | 10,440.9 | -1.9 | OK |
| D-1 RSI2 | 68.2 (reproduces from the report's own closes: 0.0, 0.0, 68.2) | 65.2 | +3.0 | OK on arithmetic; basis differs only because the earlier closes are wrong |
| ATR14 | not stated; "five-day true range ~84" in §9, and 3xATR = ~252 on Trade 1 (implies 84) | 111.26 (full-day 136.57) | -27 / -53 | DISCREPANCY: ATR(14) never stated; 84 used as ATR |
| 5-day swing high | 10,489 (§3, §7.3, §8, §15) | 10,529.6 (16 Jun) | -40.6 | DISCREPANCY |
| 5-day swing low | 10,346 | 10,343.2 | +2.8 | OK |
| 16 Jun O/H/L/C | 10,412 / 10,468 / 10,377 / 10,455 | 10,449.3 / 10,529.6 / 10,434.9 / 10,510.1 | -37 / -62 / -58 / -55 | FAIL (close > 15 pts) |
| 17 Jun O/H/L/C | 10,455 / 10,489 / 10,401 / 10,438 | 10,494.9 / 10,513.3 / 10,470.9 / 10,513.3 | -40 / -24 / -70 / -75 | FAIL |
| 18 Jun O/H/L/C | 10,438 / 10,452 / 10,362 / 10,399 | 10,460.3 / 10,475.8 / 10,372.6 / 10,399.6 | -22 / -24 / -11 / -0.6 | O, H, L discrepant; C OK |
| 19 Jun O/H/L/C | 10,399 / 10,418 / 10,353 / 10,364 | 10,383.1 / 10,417.4 / 10,347.8 / 10,352.3 | +16 / +0.6 / +5 / +11.7 | O and C discrepant (C is the one row labelled "CORROBORATED") |
| RSI2 18 Jun / 19 Jun | 0.0 / 0.0 | 2.74 / 0.00 | | consistent with report closes; 17 Jun "0.0" not reproducible (16 Jun RSI2 blank, no prior close shown) |
| Trend column 17 Jun | Neutral | rule: Close 10,438 < Open 10,455 and RSI2 0.0 < 50 = Bearish | | rule not applied |
| Daily P / R1 / S1 | 10,408 / 10,470 / 10,377 | 10,408.5 / 10,473.8 / 10,375.6 | -0.5 / -3.8 / +1.4 | OK; ladder reproduces from the report's own H/L/C |
| Daily R2 / S2 / R3 / S3 | 10,501 / 10,315 / 10,563 / 10,284 | 10,506.7 / 10,310.3 / 10,572.0 / 10,277.4 | -5.7 / +4.7 / -9.0 / +6.6 | OK (within 10) |
| Weekly H/L/C used | 10,489 / 10,353 / 10,364 | 10,574.6 / 10,347.8 / 10,352.3 (implied by level file) | -85.6 / +5.2 / +11.7 | week high wrong by 86 pts |
| Weekly P | 10,425 | 10,424.9 | +0.1 | matches the file, but does NOT follow from the report's own H/L/C (those give P = 10,402.0) |
| Weekly R1 / S1 | 10,503 / 10,360 | 10,502.0 / 10,275.2 | +1 / +84.8 | S1 FAIL |
| Weekly R2 / S2 | 10,568 / 10,282 | 10,651.7 / 10,198.1 | -83.7 / +83.9 | FAIL |
| Weekly R3 / S3 | 10,646 / 10,217 | 10,728.8 / 10,048.4 | -82.8 / +168.6 | FAIL |
| Monthly pivots | absent from §11 | May: P 10,370.4, R1 10,599.6, S1 10,180.8 | | MISSING |
| Counter: S&P 500 22 Jun | "closed up ~1%, near record" (§10) | US500 slice 22 Jun: 7,481.8 vs 7,494.2 = -0.17%; 15 Jun close 7,559.4 | ~+1.2 pp | CONTRADICTED |
| Counter: USDX | "broadly flat near 100" | 22 Jun close 101.02; 16 Jun 99.57 (+1.45% in five sessions); 17 Jun +0.86% | | MISDESCRIBED |
| 25-day range | "low-to-mid 10,300s-10,500s" (§9) | 10,126.2 - 10,574.6 | low end off by ~170 | MISDESCRIBED |

RSI2 independent test from `--closes 10455 10438 10399 10364 10439`: 0.0, 0.0, 68.2 for the last three rows, matching the report. The error is in the closes, not the arithmetic.

## 2. Section 7 checklist

| Row | Notes | Evidence | Score |
|---|---|---|---|
| 1.1 Variables respected | FTSE 100 cash primary, Euro Stoxx 50 reference, GBP/pts, as-of D-1, Europe/London, 5-day lookback all honoured. Anchor 00:00 UK instead of 07:00 UK: disclosed in header and card (a noted deviation). Source mix: only LSE is an exchange source and it carries no figure; the rest are aggregators/media; one "CFD-derived" source (Trading Economics) is rated Core while §4 footer says retail CFD quotes were excluded. Counters USDX/S&P/DAX present. | header, §2, §4, §21b | 3 |
| 1.2 Coverage and currency consistent | Dates consistent with D-1 data / D session. "Wk of 23 Jun" in §13d is undated although the calendar slice carries exact times (UK PMIs 23 Jun 09:30 UK). | §2, §6, §13d | 4 |
| 1.3 Audience and tone | Professional strategist tone. Report body repeatedly cites "run instruction"/"per run instruction" and "instructed to proceed", leaking prompt mechanics into a trading document. | §6 note, §19, §20, §21 | 4 |
| 2.1 Sections present and ordered | §1-§21 present and in order. §13c is a divergence flag and §13d holds both calendars (spec: 13c previous, 13d upcoming); no "21b" label (cards follow 21a unlabelled). | headings | 4 |
| 2.2 Scorecard as table | §6 is a table but lacks Source A / Source B columns. §11 has daily and weekly pivot tables only: monthly missing; tiers ordered S3 to R3 not R3 to P to S3. | §6, §11 | 3 |
| 2.3 Method steps visible | §4-§5 observations to consensus shown; §8 candle-by-candle and sequence; §9 regime with persistence/overlap/VOLator; five charts captioned (images dropped by conversion, accepted). KER and ATR(14) values never shown in §9. | §4-§9 | 4 |
| 3.1 Quantitative claims sourced | §1/§12/§14 carry unsourced figures: ECB 2.25%, BoE 7-2, CPI 2.8%, "~80% overseas revenue", record 10,910, S&P "+1%", USDX "near 100", oil headlines. §4/§6 history rows not tied to any named source. | §1, §10, §12, §14 | 2 |
| 3.2 Citations exist and contain data | Investing.com 22 Jun 10,439.40: consistent and used. Trading Economics 19 Jun 10,364: used consistently but is 11.7 pts from the feed and described as "CFD-derived/well corroborated". LSE "range to 22 Jun": no figure at all. Yahoo gives a range (10,439-10,471), MarketWatch "~10,400s": not quotes. §3/§19 cite reads "spanning ~10,250": below every session low in the feed (min 10,337.9) so impossible. §19/§20 claim two-provider STOXX corroboration but §4 lists one STOXX row and no Trading Economics STOXX row. Treated as weakly evidenced, not as fabricated URLs (none given). | §3, §4, §19, §20 | 2 |
| 3.3 Calculations transparent | Daily pivots and RSI2 (18, 19, 22 Jun) reproduce. Weekly pivots do not reproduce from the stated 10,489/10,353/10,364 (P would be 10,402.0; R1 10,451; S1 10,315). §13b tilt: Sigma(w*s) = 1.0 + 0.5 + 0.5 - 0.5 = 1.5 and Sigma(w) = 4.5, tilt +0.33, not +1.0/4.0 = +0.25. §21a gives only three of six signal contributions (+0.25, +0.15, +0.10 = 0.50) and cannot reach +0.61. ATR(14) and KER values not stated. | §11, §13b, §21a, §9 | 2 |
| 3.4 Numbers reconcile | D-1 close 10,439 identical in §1/§3/§4/§6/§21 and RSI2 68 in §1/§6/§8/§21a. Breaks: 5-day high 10,489 vs feed 10,529.6; ATR 84 (Trade 1 cap) vs 111.3; Trade 1 "entry at daily R1.5" while entry 10,439 is below R1 10,470 (R1.5 = 10,485.5); weekly S1 "confluence" 10,360 vs true 10,275.2; §21d "TP1 hit rate 40%" but no Trade 1 row in §21c reaches +1R; Trade 2 "2/3 accessible sessions" but §21c shows 2 triggers of 4 sessions; 22 Jun Trade 3A "Triggered NO" yet "OPEN"; 19 Jun Trade 2 exit 10,364 (-13 pts) booked as -1.00R "(SL)" against a 62-pt R. | cross-section | 2 |
| 4.1 Pillars conclude | §8, §9, §10, §15, §16 give labels. §12 and §14 end without a direction label. | §12, §14 | 3 |
| 4.2 Cross-asset interpreted | Mechanisms are written (USD translation, US beta, DAX risk-on), but the S&P read rests on a +1% move the feed does not show (-0.17%) and USDX is called flat when it rose 1.45% over five sessions. Oil, named the dominant driver, is not a counter. | §10 | 2 |
| 4.3 Synthesis reconciles tensions | Transition regime vs bullish short-term read, weak KER, indicative levels all addressed in §15/§16/§18. Not reconciled: +0.61 "comfortably above threshold" vs "mildly higher" forecast; low-confidence inputs vs high direction score. | §15-§18, §21a | 3 |
| 4.4 Calibrated language | §17 is one sentence with a falsifier (close below 10,360). Confidence L-M stated in §3; no confidence in §17. | §3, §17 | 4 |
| 5.1 Data dated, staleness flagged | Prices dated and single-source flags carried. §13a articles have no dates or URLs; Goldman item concerns STOXX 600, not FTSE. | §4, §6, §13a | 3 |
| 5.2 Assumptions up front | Anchor override and indicative status stated in header, §19 and on every card. §20 does not log the anchor override (only the corroboration override). | header, §19, §20, §21 | 4 |
| 5.3 Red flags surfaced | Oil/Middle East and BoE dissent surfaced. Event collisions inside the D session (UK flash PMIs 09:30 UK; Eurozone PMIs; Lane speech 09:30 UK) are not in §13d with times and not carried into any card caveat. FOMC hold 17 Jun, Eurozone CPI 3.2% vs 2.6% (17 Jun) and UK labour data 18 Jun (unemployment 4.9% vs 5.3% consensus) are missing from the previous-period calendar. | §13d, cards | 3 |
| 5.4 Restrictions honoured | Breaches: (a) Trade 2 kept although every pivot tier is declared single-source-indicative (fixed M5 rule: suppress) and explicitly "retained per run instruction"; (b) "Normalized" prices 10,420 (from "~10,400s") and 10,455 (midpoint of a 10,439-10,471 range) are synthesised values presented in the evidence table as sourced; (c) a CFD-derived series is used as a Core OHLC observation while the footer claims CFD quotes were excluded. No bracketed variable names, no M1..M5 codes, no framework name. | §4, §19, §21 | 1 |

## 3. Category roll-up

| Cat | Rows | Mean | Level | Multiplier | Max | Points | Justification |
|---|---|---|---|---|---|---|---|
| 1 Prompt adherence | 3, 4, 4 | 3.67 -> 4; restriction-breach override applies -1 | 3 | 0.65 | 20 | 13.00 | Variables largely honoured; anchor and source-tier deviations; prompt-mechanics leakage; lowered one level for the 5.4 breach |
| 2 Structure | 4, 3, 4 | 3.67 -> 4 | 4 | 0.85 | 20 | 17.00 | All 21 sections present; no monthly pivots, no Source A/B columns, 13c/13d merged |
| 3 Accuracy & evidence | 2, 2, 2, 2 | 2.0 | 2 | 0.40 | 25 | 10.00 | D-1 OHLC and daily pivots good; 16-19 Jun history, week high, weekly ladder, ATR, tilt and counters wrong |
| 4 Reasoning & judgment | 3, 2, 3, 4 (mean 3.0) then card construction | 3.0 -> 2 | 2 | 0.40 | 20 | 8.00 | All three cards break fixed M5 construction rules despite a clean linter (see feedback) |
| 5 Currency & transparency | 3, 4, 3, 1 | 2.75 -> 3 | 3 | 0.65 | 15 | 9.75 | Dating and caveats mostly present; synthesised "normalized" prices and Trade 2 retention |
| Total | | | | | 100 | 57.75 | |

## 4. Total, band, override
- Total = 13.00 + 17.00 + 10.00 + 8.00 + 9.75 = 57.75, rounded to **58**.
- Band: **Low (40-59)**.
- Override: **restriction_breach** (row 5.4: Trade 2 retained against the fixed suppression rule; synthesised normalised prices presented as sourced). Cap Moderate (60-74) not binding at 58; C1 lowered one level (4 to 3). Hallucinated-source override not applied: no URLs are given, the named sources are plausible, and the defects are unsupported/unrepresentative figures rather than invented sources.

## 5. Card Integrity (linter rows copied verbatim from `lint_static/2026-06-23.csv`)

| card_id | strategy | flags | dud | per-card score |
|---|---|---|---|---|
| 2026-06-23_Trade_1 | Trade 1 - Daily Directional (LONG - score +0.61, above threshold) | CLEAN | False | 100 |
| 2026-06-23_Trade_2 | Trade 2 - Regime-Aware Pivot (LONG bias - buy the dip to support) | CLEAN | False | 100 |
| 2026-06-23_Trade_3A | Trade 3A - Regime-Driven Complex: Momentum-Pullback (TRANSITION->bullish fork) | CLEAN | False | 100 |

Report-level Card Integrity = mean(100, 100, 100) = 100.0 · n_cards=3 · n_duds=0 · n_warns=0. The static linter passes all three cards; the construction defects in the feedback file are rule-level (M5) and are scored under Category 4, not here.
