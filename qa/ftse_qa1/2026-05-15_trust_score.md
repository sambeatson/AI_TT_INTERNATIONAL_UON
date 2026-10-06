# Trust Score v3.7 — FTSE 100 daily report, D = 2026-05-15

Report: `reports/md/FTSE_EuroStoxx_Report_15May2026.md` · run ftse_qa1 · reviewer: independent session (stage 1)
Leak check: `data/levels/UK100_by_date/2026-05-15.csv` has `last_bar_date = 2026-05-14` (< D); slice last bar 2026-05-14 22:45 broker. OK.
Basis used: report claims the cash index, so the `_cash` columns (broker 10:00–18:30 = London 08:00–16:30) are the primary comparison; `_full` shown where it changes the verdict.

## Score line

```
c1=2
c2=4
c3=1
c4=2
c5=3
total=48
band=Low
override=restriction_breach
card_integrity=100
n_cards=3
n_duds=0
n_warns=0
```

## 1. Section 7 checklist

| Row | Score | Reviewer notes | Evidence (location) |
|---|---|---|---|
| 1.1 Variables respected | 3 | Asset = FTSE 100 cash (primary), Euro Stoxx 50 reference only; counters USDX / S&P 500 / DAX 40; GBP, points, Europe/London, 5/25-day lookback, 07:00 UK anchor stated. Weak points: only three usable named sources (Yahoo = Tier 3, Trading Economics, Investing.com); both Tier-1 sources failed or were "not attempted", so the "≥ 6 sources from index provider / exchange / sell-side tiers" requirement is not met. Cards give no clock-time anchor. | §2, §10, §20 source table |
| 1.2 Coverage & currency consistent | 2 | Weekday/date drift: "Thu 8 May" is Fri 8 May 2026; "Wed 21 May" is Thu; "Thu 22 May" is Fri; "Mon 26 May — UK bank holiday" is Tue (the bank holiday is Mon 25 May). §13d lists "UK Q1 GDP detail data" as a 15 May event although the calendar slice shows UK GDP q/q/m/m/y/y already published 14 May 09:00 broker (07:00 UK). §13d omits every event the calendar slice schedules for D (EUR CPI/HICP, ECB Economic Bulletin, US Empire State, US Industrial Production, Barr speech). STOXX 14 May "open 6,044.36" is a stale 8 May-level print (8 May close 6,045.98). | §6, §13d, §6 STOXX table |
| 1.3 Audience & tone | 4 | Strategist register, trading/risk-review framing. Minor: "textbook", "rear-view mirror", "unusually clean". | §1, §8, §18 |
| 2.1 Sections present & ordered | 4 | §1–§21 all present in order incl. §21a/b/c/d. §13 has per-article table, aggregate tilt, forward calendar, but no previous-period calendar (§13c missing: 14 May UK GDP, US retail sales 0.5 vs 1.2 consensus, jobless claims, Pill/Lagarde speeches). Charts are a described table of five, not rendered (accepted as placeholder; the report says the engine was "not physically invoked"). | §7, §13 |
| 2.2 Scorecard as a table | 4 | §6 is a table with Date/O/H/L/C/RSI2/Trend/Source A/Source B/Validation; no "Final" column. §11 gives daily/weekly/monthly pivot tables, ordered R5→S5 (5 levels each side; brief expects R3→S3 — extra levels are harmless). | §6, §11 |
| 2.3 Method steps visible | 3 | §8 candle-by-candle + sequence present. §5 states a "weighted median" but shows no computation. §9 regime shows KER/VOLator but no persistence/overlap evidence. Charts not produced. | §5, §8, §9, §7 |
| 3.1 Quantitative claims sourced | 2 | §4 sources the FTSE closes. Unsourced / undated: all-time high 10,934.94 (27 Feb), "energy ~15% of index", "~80% offshore revenue", BoE/ECB/Fed rates, CPI path, HICP 2.4–2.6%, Fed QT/T-bill purchases, FX levels, Brent "$100–101" (cited only as "Reuters/WSJ" with no date/quote). §12 and §14 carry almost no source tags. 8 May and 11 May closes have no §4 evidence row at all. | §12, §14, §4 |
| 3.2 Citations exist & contain data | 1 | Spot-checks: (a) Yahoo 14 May close 10,372.93 @16:40 vs slice cash close 10,355.8 (Δ +17.1; full-day 10,352.0, Δ +20.9) and above the Investing.com session high the report itself quotes (10,360.51). (b) Investing.com range 10,266.14–10,360.51: §6 and §19 attribute a "high ~10,400" to this source, which does not match its own quoted high 10,360.51; §3 lists the session low as 10,318.66, which is the open. (c) STOXX "Investing.com open 6,044.36" sits above the same row's high (~5,950): impossible. No source is shown to be non-existent and the STOXX material carries no cards, so the hallucinated-source override is NOT triggered, but figures do not match their own quotes. | §3, §4, §6, §19 |
| 3.3 Calculations transparent | 1 | RSI2 given only as "~" approximations "derived from the observed close sequence"; from the report's own five closes the tool returns 0.0 / 94.2 / 100.0 for 12/13/14 May versus stated ~7 / ~68 / ~88. Monthly pivots do not follow from the stated basis (~10,800/~10,150/10,425 gives P 10,458.3, R1 10,766.7, S1 10,116.7, not 10,400/10,500/10,250). ATR(14) "estimated ~95" and KER "estimated +0.18" with no inputs. Daily pivots and the §21a score (+0.6865 → 0.687) DO reproduce exactly. | §6, §9, §11, §21a |
| 3.4 Numbers reconcile | 1 | D-1 close 10,372.93 identical in §1/§3/§4/§6/§18 (good). Breaks: §7.5 weekly P ~10,290 / R1 ~10,420 vs §11 weekly P 10,428 / R1 10,491; §1 "above 25-session midpoints" vs §7.3 midpoint ~10,400 > close 10,372.93 yet "upper third"; §4 Investing high 10,360.51 vs §6 high 10,400; §21b Trade 1 entry 10,370 vs close 10,372.93, stated R 81 vs 10,370−10,292 = 78, TP1 +84 not +81, TP3 +246 not +243; §21c 8 May Trade 1 stopped at 10,355 although §6 8 May low is 10,365; §21c 12 May Trade 2 exits at 10,375 though §6 highs for 12/13 May are 10,290/10,330. | whole report |
| 4.1 Pillars conclude | 3 | §8, §9, §10, §12 end in direction labels. §14 Macro is descriptive only (no closing direction). | §14 |
| 4.2 Cross-asset interpreted | 3 | §10 gives mechanisms (USD/offshore earnings, US beta, DAX read-across). USDX row contradicts §14 ("sterling firm against a generally stronger dollar") and the "GBP weakness" mechanism; Brent is argued in §1/§12/§15 but is not a §10 row. | §10, §14 |
| 4.3 Synthesis reconciles tensions | 2 | Short-term bull vs medium-term neutral is addressed and §17 vs §21a agree. The regime and KER read is not reconciled with the level file: 25-day range 10,145.9–10,666.5 (mid 10,406.2), D-1 cash close at 40.3% of the range, 25-day low printed on 12 May (not "mid-April ~10,150"); 13-session close displacement is negative (−30.2 raw; −123.8 on EMA(3)-smoothed closes, ER 0.236) so a "TRENDING UP" KER label is unsupported. "KER AGREES with regime" is asserted, not shown. | §1, §7.3, §9 |
| 4.4 Calibrated language | 3 | §17 is exactly one sentence; confidence MEDIUM stated in §3/§18. Over-confident phrasing on indicative data ("textbook", "convincingly bullish"); close/high labelled "Corroborated (close ±0.10)" on rows that are marked "~" or "(indic.)". | §6, §8, §17 |
| 4.5 Card construction (protocol add-on) | 1 | None of the three cards follows the fixed M5 construction: Trade 1 management/runner/entry/arithmetic; Trade 2 uses a TREND label with a RANGE-style S1 limit and 0.57R/1.44R/2.01R targets; Trade 3A is a stop-entry breakout, not a 57.5% retrace, with no logged swing and a runner stop (10,800) above TP2 (10,615). Linter = CLEAN (static checks only). See feedback. | §21b |
| 5.1 Data dated; staleness flagged | 3 | Most items dated; STOXX and 14 May H/L flagged single-source. Not flagged: "~" O/H/L for 8/11/12 May, identical 12 May and 13 May open (10,264.91), stale STOXX open. | §4, §6, §19 |
| 5.2 Assumptions up front | 3 | Anchor override and no-suppress override stated in §20 / §3, but §20 is self-contradictory ("anchor moved forward to 07:00" yet "no time-of-day change"), not in §1, and not on the cards. | §20, §21b |
| 5.3 Red flags surfaced | 4 | §12/§15 elevate CPI, RSI2 stretch, political-tax risk; CPI collision carried into card invalidations. Missed: 14 May US retail sales miss; D-day event list. | §12, §15, §21b |
| 5.4 Restrictions honoured | 1 | Module code leaked: "Sentiment tilt (M2 §13b aggregate)" in §21a (restriction: no module codes M1..M5). Internal variable names leaked ("sentiment_tilt", "cross_asset_confirm = CONFIRM", "Strategies surface"). §5 itself suspects Investing.com is a "CFD reference" yet that source supplies the open/low/range. Rounded "~" values presented as "Corroborated". → restriction override. | §21a, §13b, §5, §6 |

## 2. Category roll-up

| Cat | Rows | Mean | Level | Multiplier | Points (of max) | Justification |
|---|---|---|---|---|---|---|
| C1 Prompt adherence | 3, 2, 4 | 3.00 → 3 | **2** (override −1) | 0.40 | 8.00 / 20 | Variables mostly respected but sources thin, date drift; restriction breach (M2 module code) forces one level down. |
| C2 Structure | 4, 4, 3 | 3.67 → 4 | **4** | 0.85 | 17.00 / 20 | All 21 sections in order; §13c missing; charts only described. |
| C3 Accuracy & evidence | 2, 1, 1, 1 | 1.25 → 1 | **1** | 0.20 | 5.00 / 25 | Only 2 of 20 OHLC fields within tolerance; D-1 close +17.1; RSI2 does not reproduce from own closes; ATR14 −29%; weekly/monthly pivots off by up to 377 pts. Brief §4: close > 15 pts out and non-reproducing RSI2 are scored failures. |
| C4 Reasoning & judgment | 3, 3, 2, 3, 1 | 2.40 → 2 | **2** | 0.40 | 8.00 / 20 | Mechanisms present but regime/KER contradict level file; card construction departs from M5 on all three cards. |
| C5 Currency & transparency | 3, 3, 4, 1 | 2.75 → 3 | **3** | 0.65 | 9.75 / 15 | Dated and flagged for the most part; restriction breach and approximations labelled corroborated. |

## 3. Total, band, override

Total = 8.00 + 17.00 + 5.00 + 8.00 + 9.75 = 47.75 → **48** → band **Low** (40–59).
Override check: restriction breach (M2 module code in §21a, internal variable names) → cap Moderate (60–74) and C1 down one level: applied to C1 (3→2); the cap does not bind (48 < 60). Hallucinated-source override: not triggered (see 3.2 note); C3 not forced to 0.

### Category 3 detail — report vs level file (Δ = report − slice, cash basis; tolerance close ≤ 5, O/H/L ≤ 10)

| Date | Field | Report | Slice cash | Δ | Verdict |
|---|---|---|---|---|---|
| 8 May | O / H / L / C | ~10,425 / ~10,440 / ~10,365 / 10,379.51 | 10,189.8 / 10,271.7 / 10,174.8 / 10,222.4 | +235.2 / +168.3 / +190.2 / +157.1 | all fail |
| 11 May | O / H / L / C | ~10,355 / ~10,365 / ~10,250 / 10,269 | 10,254.8 / 10,284.2 / 10,221.9 / 10,264.1 | +100.2 / +80.8 / +28.1 / +4.9 | C pass, rest fail |
| 12 May | O / H / L / C | 10,264.91 / 10,290 / 10,250 / 10,265.32 | 10,190.5 / 10,250.3 / 10,145.9 / 10,250.1 | +74.4 / +39.7 / +104.1 / +15.2 | all fail (C > 15) |
| 13 May | O / H / L / C | 10,264.91 / 10,330 / 10,260 / 10,325.35 | 10,314.9 / 10,357.0 / 10,234.8 / 10,293.6 | −50.0 / −27.0 / +25.2 / +31.8 | all fail |
| 14 May (D−1) | O / H / L / C | 10,318.66 / 10,400 / 10,266.14 / 10,372.93 | 10,319.3 / 10,371.1 / 10,301.1 / 10,355.8 | −0.6 / +28.9 / −35.0 / +17.1 | O pass; H, L, C fail (full-day C 10,352.0: +20.9) |

Trend labels vs slice-cash O/C/RSI2: 11 May report Bearish, slice Neutral (C>O, RSI2 40.9); 12 May report Neutral, slice Bullish (C>O, RSI2 74.9); 13 May report Bullish, slice Neutral (C<O, RSI2 75.7). 8 and 14 May agree.

RSI2: D-1 stated ~88 vs `rsi2_cash` 100.0 (Δ −12.0) / `rsi2_full` 99.47. From the report's own closes (10,379.51, 10,269.00, 10,265.32, 10,325.35, 10,372.93): 12 May 0.0 (stated ~7), 13 May 94.2 (stated ~68), 14 May 100.0 (stated ~88) — does not reproduce.
ATR14: stated ~95 vs 133.29 cash / 142.60 full (Δ −38.3 / −47.6; −29% / −33%).

Daily pivots (report basis H/L/C 10,400 / 10,266.14 / 10,372.93; formulae reproduce exactly) vs cash level file / full-day:

| Level | Report | Cash | Δ | Full | Δ |
|---|---|---|---|---|---|
| R3 | 10,560 | 10,454.2 | +105.8 | 10,498.4 | +61.6 |
| R2 | 10,480 | 10,412.7 | +67.3 | 10,447.9 | +32.1 |
| R1 | 10,427 | 10,384.2 | +42.8 | 10,399.9 | +27.1 |
| P | 10,346 | 10,342.7 | +3.3 | 10,349.4 | −3.4 |
| S1 | 10,293 | 10,314.2 | −21.2 | 10,301.4 | −8.4 |
| S2 | 10,212 | 10,272.7 | −60.7 | 10,250.9 | −38.9 |
| S3 | 10,159 | 10,244.2 | −85.2 | 10,202.9 | −43.9 |

Weekly pivots (report basis ~10,540 / ~10,365 / 10,379; slice cash prior week 5–8 May implies H 10,491.8, L 10,162.8, C 10,222.4): P 10,428 vs 10,292.3 (+135.7); R1 10,491 vs 10,421.9 (+69.1); R2 10,603 vs 10,621.3 (−18.3); R3 10,666 vs 10,750.9 (−84.9); S1 10,316 vs 10,092.9 (+223.1); S2 10,253 vs 9,963.3 (+289.7); S3 10,141 vs 9,763.9 (+377.1). Weekly S1 as a stop anchor is 223 pts out.
Monthly pivots (report basis ~10,800 / ~10,150 / 10,425; slice April cash implies H 10,697.5, L 10,187.6, C 10,371.3): P 10,400 vs 10,418.8 (−18.8); R1 10,500 vs 10,650.0 (−150.0); R2 10,650 vs 10,928.7 (−278.7); R3 10,800 vs 11,159.9 (−359.9); S1 10,250 vs 10,140.1 (+109.9); S2 10,100 vs 9,908.9 (+191.1); S3 9,950 vs 9,630.2 (+319.8). The report's monthly levels are also not derived from its own stated basis.
Counters (not penalised): S&P 500 7,501.24 vs slice 7,504.1; USDX 98.59 vs slice 98.875 (feed/time-of-day difference; "fourth day higher" is consistent with the slice closes).

## 4. Card Integrity (linter rows, copied verbatim from `qa/ftse_qa1/lint_static/2026-05-15.csv`)

| card_id | report_date | strategy | flags | dud | #DUD | #WARN | Integrity |
|---|---|---|---|---|---|---|---|
| 2026-05-15_Trade_1 | 2026-05-15 | Trend-following long (Trade 1) | CLEAN | False | 0 | 0 | 100 |
| 2026-05-15_Trade_2 | 2026-05-15 | Pivot trade - TREND_UP face-support buy (Trade 2) | CLEAN | False | 0 | 0 | 100 |
| 2026-05-15_Trade_3A | 2026-05-15 | Complex - Continuation breakout long (Trade 3A, TREND_UP fork) | CLEAN | False | 0 | 0 | 100 |

Report-level Card Integrity = mean(100, 100, 100) = **100**; n_cards = 3 (none suppressed), n_duds = 0, n_warns = 0.
Note: CLEAN is a static-geometry result only. The construction defects listed in the feedback (management text, runner rule, entry/R arithmetic, regime-rule mismatch, swing logging) are not linter checks and are scored under C4 row 4.5, not in Card Integrity.

## 5. Feedback

See `qa/ftse_qa1/2026-05-15_feedback.md`.
