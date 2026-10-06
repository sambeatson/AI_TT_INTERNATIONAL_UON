# Trust Score v3.7 — FTSE 100 Daily, 1 July 2026 (run ftse_qa1)

Report: `reports/md/FTSE_100_Daily_1_July_2026.md` · D = 2026-07-01 · D-1 = 2026-06-30
Level file `data/levels/UK100_by_date/2026-07-01.csv`: `last_bar_date` = 2026-06-30 < D (leak check passed). Slice last bar 2026-06-30 22:45 broker. The report claims a cash basis, so comparisons use the `_cash` columns (`qa_slice_stats.py --cash-open 10:00 --cash-close 18:30`). `_full` is given where useful.

## Score line (machine-readable)
```
c1=4
c2=3
c3=0
c4=3
c5=3
total=53
band=Low
override=hallucinated_source
card_integrity=100
n_cards=3
n_duds=0
n_warns=0
```

## 1. Section 7 checklist

| Row | Reviewer notes | Evidence (location) | Score |
|---|---|---|---|
| 1.1 Variables respected | Asset (FTSE 100 cash, Euro Stoxx 50 as reference with no cards), counters (USDX / S&P 500 / DAX 40), as-of 30 Jun London close, 5-session lookback and GBP/points are all right. Two gaps. (a) The ≥ 6 sources are meant to come from index-provider, exchange and sell-side tiers. §4 lists aggregators and media (Trading Economics, Investing.com, TradingView, Yahoo, MarketScreener). The one index-provider row ("FTSE Russell / LSE", "Official close basis") has no quote, no figure and no time. (b) Trade 1 anchor is 08:00 UK, not 07:00 UK. This is disclosed as "per run instruction" on the card and in §20, but it is still a departure from the variable. | §4, §20, §21b T1 Entry | 3 |
| 1.2 Coverage and currency consistent | All data dates are ≤ 30 Jun, the session is 1 Jul, and units are consistent. Drift points: the §21c rows are labelled t−5..t−2 and cover only 25, 26, 29 and 30 Jun, so "5-session" is 4 rows and t−1 is skipped. The §11 weekly pivots are built from 23–26 Jun only (22 Jun is missing from the week). "US payrolls ~3 Jul" is undated and not on the calendar slice. | §11, §13d, §21c | 4 |
| 1.3 Audience and tone | Professional, strategist register, no retail tone. | §1, §18 | 4 |
| 2.1 Sections present and ordered | §1–§21 all present and in order, including §13a–d and §21a–d. §7 Charts is a bare heading with no caption or placeholder (images dropped by pandoc; noted, not penalised heavily). | headings | 4 |
| 2.2 Scorecard and pivots as tables | §6 is a table, with a Euro Stoxx table as well. The §11 daily and weekly tables are ordered R3→S3. The **monthly pivot table is missing** (the brief requires daily, weekly and monthly). §6 has no ATR14 or KER columns or lines. | §6, §11 | 3 |
| 2.3 Method steps visible | §4→§5 shows observations, normalisation and consensus. §8 reads candle by candle. §9 names the regime but shows no numbers: no KER value, no ATR14 value (only "~1.1% of price"), no persistence or overlap figures. | §4, §5, §8, §9 | 3 |
| 3.1 Quantitative claims sourced | §12 and §14 quote GBP/USD ~1.334, EUR/USD ~1.15, WTI ~70, Bank Rate 3.75%, CPI ~2.8%, "~+20% y/y" and "+2% month" with no source and no date. DAX "~24,620–25,006" is unsourced. S&P "~7,354–7,440" is a stale range (see 3.4). §13a has no dates. | §1, §10, §12, §14, §13a | 2 |
| 3.2 Citations exist and contain the data | **FAIL. Three self-contradictory citations**, verbatim. (1) §4 "Trading Economics … 10,519 … +0.33% session": +0.33% implies a prior close of about 10,484.4, but the report's own 29 Jun close is 10,412.7, which gives +1.02%. (2) §4 "Investing.com … 10,530.18 open; 10,404.73–10,530.18" with normalized "10,468–10,575 (session)": the quoted high 10,530.18 is below the normalized and §6 high of 10,575.3, and the quoted low 10,404.73 is below the §6 low of 10,468.0. (3) §4 "MarketScreener … 29 Jun close 'closes lower' → 10,412.7": the quote contains no figure, so the precise 10,412.7 is unsupported (slice 29 Jun cash close is 10,497.8). Also "FTSE Russell / LSE … Official close basis → 10,519" has no quote at all. §19 and §20 claim every row is "dual-source corroborated within ±0.10 pt", which the above and the slice contradict. | §4, §6, §19, §20 | 0 |
| 3.3 Calculations transparent | RSI2 reproduces from the report's own closes (0.0 / 63.9 / 42.9 / 59.6 re-checked). The Trend labels follow the rule. Pivot arithmetic reproduces exactly from the report's stated H/L/C (daily P 10,520.8; weekly P 10,484.3 from the 23–26 Jun rows). Gaps: ATR14 is never printed (only "~1.1%" and an "indicative ATR proxy" built on 5 sessions, per §19). KER is never given numerically. §21a shows "score ≈ +0.30" with no per-signal values, so Σ signal×weight cannot be reproduced. The weekly H/L/C inputs are not shown. | §6, §9, §11, §19, §21a | 2 |
| 3.4 Numbers reconcile | D-1 close 10,519 is consistent across §1, §3, §4, §6 and §21b. The daily pivots on the cards match §11. Breaks: "+0.33%" vs the own-table +1.02% (§1, §4 vs §6). The §21c 30 Jun Trade 3C row says triggered at 10,576, but the report's own 30 Jun high is 10,575.3, so it cannot have triggered. It also shows "open @ +0.3R" although the 30 Jun close of 10,519 is 57 pts below the 10,576 entry. The §21c 30 Jun Trade 2 row says filled at 10,466, but the report's own 30 Jun low is 10,468.0. The §21d "TP2 hit 50%" cannot be reconciled with the §21c outcomes (no row reaches +2R). The §11 position text "just above the weekly R1 (10,566 is overhead…)" is garbled (10,519 is below weekly R1). The 3C TP3 "weekly R2 10,648–10,730" conflates weekly R2 and R3. | §1, §4, §6, §11, §21b–d | 2 |
| 4.1 Pillars conclude | §9 (TRANSITION) and §10 (CONFIRM) give labels. §8 ends on levels with no direction label. §12 has per-bullet labels but no net label. §14 has none. | §8, §12, §14 | 3 |
| 4.2 Cross-asset interpreted | There is a mechanism for each counter, but thin. The USDX row says "firm" yet argues "softer sterling"; the slice has USDX falling through the last four London closes (101.61 → 101.14). DAX is a "proxy" with no mechanism. No oil or energy-weight mechanism in §10. | §10 | 3 |
| 4.3 Synthesis reconciles tensions | §15, §16 and §18 reconcile TRANSITION vs uptrend bias at low conviction. Not reconciled: the §9 regime is TRANSITION, yet Trade 2 is a RANGE-style pullback limit at S1, and Trade 3C is a LONG breakout. Two opposite-style LONG expressions sit side by side with no reasoning. §21a "no conflict with §17" ignores that low KER caps conviction. | §9, §15–§18, §21 | 2 |
| 4.4 Calibrated language | §17 is exactly one sentence, conditional, with no hedge stacking. Confidence "High" on the close level is not calibrated: see §3 of this file, the close is off the slice by +17.5 pts and the series is off by up to 107 pts. | §3, §17 | 3 |
| 4.5 Card construction (protocol) | See the feedback file. T1: stop has no 0.25×ATR buffer, takes the wider anchor, and the wide-stop flag is missing. T2: a pullback limit under a TRANSITION label, TP2 is ~1.6R not 2R, and no ATR buffer on the stop. T3C: uses the 30 Jun high, not the 25-day boundary. Its stop, TP1 and TP2 are not width-based, TP3 is null and sits below TP2 (zone), and there is no entry+0.2R rule. The direction score cannot be reproduced. | §21a, §21b | 2 |
| 5.1 Data dated; staleness flagged | OHLC rows and the §4 evidence table are dated. §13a has no per-article dates. GBP/USD, WTI, Bank Rate, CPI and the S&P / DAX levels are undated "~" figures. The S&P range quoted is the 23–29 Jun range, presented as current. | §4, §10, §12, §13a | 3 |
| 5.2 Assumptions up front | The 08:00 anchor override is stated on the T1 card and in §20. The ATR-proxy limitation and the Yahoo divergence are disclosed in §19. Not disclosed: the weekly pivot rests on 4 sessions. | §19, §20, §21b | 4 |
| 5.3 Red flags surfaced | §13d carries only the PMIs and the payrolls. The calendar slice for D shows HIGH-impact events that are omitted from §13d, §12 and every card caveat: BoE Bailey speech 16:00 broker (14:00 UK), ECB Lagarde speeches 16:00 and 17:00 broker, US ADP 15:15, US S&P Global Mfg PMI 16:45 and ISM Mfg 17:00 broker. The UK/EZ PMIs are tagged MODERATE on the calendar, yet the report calls them "High". The D-1 upper-wick reversal is missed (see 3.x discrepancies). No collision caveat sits on any card. | §12, §13d, §21b | 2 |
| 5.4 Restrictions honoured | No module codes, bracketed variables, framework name or futures quotes were found. The report says "No prices were synthesised", but the 23–29 Jun O/H/L/C values are labelled CORROB. with named sources, and nothing in §4 supports them and the slice contradicts them. This is a serious transparency failure, but whether it is synthesis or mis-sourcing cannot be established from the file alone, so it is **not** separately scored as a restriction breach (override already capped by the source finding). | whole report, §6, §19 | 2 |

### Category 3 evidence — report vs slice (cash basis, `_cash` columns; tolerance ≤ 5 pts close, ≤ 10 pts O/H/L)

| Date | Field | Report | Slice (cash) | Δ | Within tol.? |
|---|---|---|---|---|---|
| 23 Jun | O / H / L / C | 10498.0 / 10546.2 / 10470.5 / 10532.4 | 10329.6 / 10461.5 / 10328.1 / 10453.0 | +168.4 / +84.7 / +142.4 / +79.4 | none |
| 24 Jun | O / H / L / C | 10535.0 / 10565.8 / 10448.9 / 10461.3 | 10422.2 / 10468.6 / 10400.6 / 10455.1 | +112.8 / +97.2 / +48.3 / +6.2 | none |
| 25 Jun | O / H / L / C | 10460.0 / 10498.6 / 10402.1 / 10430.7 | 10427.6 / 10577.7 / 10413.8 / 10538.0 | +32.4 / −79.1 / −11.7 / −107.3 | none |
| 26 Jun | O / H / L / C | 10433.0 / 10489.4 / 10405.0 / 10484.9 | 10498.3 / 10516.4 / 10401.4 / 10516.4 | −65.3 / −27.0 / +3.6 / −31.5 | L only |
| 29 Jun | O / H / L / C | 10487.0 / 10512.7 / 10404.7 / 10412.7 | 10505.9 / 10524.3 / 10468.8 / 10497.8 | −18.9 / −11.6 / −64.1 / −85.1 | none |
| **30 Jun (D-1)** | **O / H / L / C** | **10530.2 / 10575.3 / 10468.0 / 10519.0** | **10509.5 / 10608.8 / 10490.6 / 10501.5** (full-day C 10506.2) | **+20.7 / −33.5 / −22.6 / +17.5** (vs full-day C: +12.8) | none |

- Only 1 of 24 stated O/H/L/C values is within tolerance.
- **The D-1 close is wrong by more than 15 pts (+17.5 cash).** Per brief §4 this is a Category 3 failure.
- The direction of the day-on-day change differs from the slice on 24, 25 and 26 Jun.
- **The D-1 session is mischaracterised.** The report says "wide-range up day… closing mid-range (48%)… reclaiming 10,500". The slice shows a spike to 10,608.8 and a close of 10,501.5 below the open (10,509.5), at 9% of the day's range, with a 107.3-pt upper wick.
- The 29 Jun "weakest close of the window (7% of range)" is 52% of range in the slice.
- **RSI2 (D-1).** The report states 59.6. The slice gives 16.59 on cash closes and 86.30 on full-day closes. The report's arithmetic is internally sound; the closes it feeds are wrong.
- **ATR14.** The report prints no number. The cards imply about 113–115 (115 = "≈1.0×ATR", 3×ATR ≈ 340), consistent with the slice's cash ATR14 113.16 (full-day 127.94). OK once converted, but not stated.
- **Daily pivots (report vs cash):**

| Level | Report | Slice (cash) | Δ | Tol. |
|---|---|---|---|---|
| P | 10520.8 | 10533.6 | −12.8 | out |
| R1 | 10573.5 | 10576.7 | −3.2 | ok |
| S1 | 10466.2 | 10458.5 | +7.7 | ok |
| R2 | 10628.1 | 10651.8 | −23.7 | out |
| S2 | 10413.5 | 10415.4 | −1.9 | ok |
| R3 | 10680.8 | 10694.9 | −14.1 | out |
| S3 | 10358.9 | 10340.3 | +18.6 | out |

- The agreement on R1, S1 and S2 is coincidental, from offsetting errors in H/L/C.
- **Weekly pivots (report vs cash, week 2026-W26):**

| Level | Report | Slice (cash) | Δ |
|---|---|---|---|
| P | 10484.3 | 10474.1 | +10.2 |
| R1 | 10566.4 | 10620.0 | −53.6 |
| S1 | 10402.7 | 10370.4 | +32.3 |
| R2 | 10648.0 | 10723.7 | −75.7 |
| S2 | 10320.6 | 10224.5 | +96.1 |
| R3 | 10730.1 | 10869.6 | −139.5 |
| S3 | 10239.0 | 10120.8 | +118.2 |

  The report's weekly range (163.7) is too narrow versus the slice (249.6) because it is built from the report's own 23–26 Jun rows and omits 22 Jun.
- **Monthly pivots.** None are given. The slice's June cash set is P 10,412.2, R1 10,698.1, S1 10,215.5, R2 10,894.8, S2 9,929.6, R3 11,180.7, S3 9,732.9.
- **Swings.** The report's "early-June base near 10,360" conflicts with the 25-day cash low of 10,126.2 (10 Jun). The 5-day cash swing low is 10,400.6 (24 Jun) and the 5-day high is 10,608.8 (30 Jun).
- **Counters (London close, 30 Jun).**
  - USDX 101.14 matches "~101", but it has fallen four sessions in a row from 101.61 (24 Jun) while the report says "firm".
  - The S&P 500 is 7,486.4. The report's "~7,354–7,440" is stale and misses the +1.0% day move (7,412.8 → 7,486.4).
  - VIX 17.74 matches "toward 17".
  - DAX 40 cannot be checked (no slice).
- **Calendar for D.** The UK and EZ manufacturing PMIs are confirmed as scheduled (UK 11:30 broker, consensus 53.1). The HIGH events omitted from the report are listed under 5.3.

## 2. Category roll-up

| Cat | Rows → mean | Level | Multiplier | Points | One-line justification |
|---|---|---|---|---|---|
| C1 Prompt adherence (20) | 3, 4, 4 → 3.67 | 4 | 0.85 | 17.00 | Variables mostly respected; the 08:00 anchor (disclosed) and the missing provider-tier sources hold it from 5. |
| C2 Structure (20) | 4, 3, 3 → 3.33 | 3 | 0.65 | 13.00 | All 21 sections present; the monthly pivots, ATR/KER lines and the chart placeholder are missing. |
| C3 Accuracy and evidence (25) | 2, 0, 2, 2 → 1.5 (→ 2) | **0** | 0.00 | 0.00 | **Set to 0 by the hallucinated-source override.** Self-contradictory citations; the D-1 close is off by +17.5 pts and the series by up to 168 pts. |
| C4 Reasoning and judgment (20) | 3, 3, 2, 3, 2 → 2.6 | 3 | 0.65 | 13.00 | Narrative is coherent and §17 is one sentence, but the cards contradict the regime label and the score is not derivable. |
| C5 Currency and transparency (15) | 3, 4, 2, 2 → 2.75 | 3 | 0.65 | 9.75 | Anchor and proxy caveats stated; D calendar red flags are omitted and sources are undated. |

## 3. Total, band, override
- Total = 17.00 + 13.00 + 0.00 + 13.00 + 9.75 = 52.75, rounded to **53**. That is already inside Low (40–59), so the cap makes no difference to the number.
- **Band: Low Trust (40–59).**
- **Override: `hallucinated_source`.** Row 3.2 fails on three citations that contradict their own quotes (verbatim above). C3 is set to 0 and the report is capped at Low.
- A restriction breach is not separately triggered (see row 5.4). If a second reviewer reads 5.4 as a breach, C1 would drop to 3 (−3.00 points); the band would stay Low.

## 4. Card Integrity (linter rows, copied verbatim; separate from the 100)

| card_id | report_date | strategy | flags | dud |
|---|---|---|---|---|
| 2026-07-01_Trade_1 | 2026-07-01 | Trade 1 - Daily Directional (LONG) | CLEAN | False |
| 2026-07-01_Trade_2 | 2026-07-01 | Trade 2 - Pivot (regime-aware, LONG-from-support) | CLEAN | False |
| 2026-07-01_Trade_3C | 2026-07-01 | Trade 3 - Complex (regime: TRANSITION → 3C breakout) | CLEAN | False |

- Per card: 100 − 40×0 − 10×0 = 100, 100 and 100.
- **Report-level Card Integrity = 100** (n_cards 3, n_duds 0, n_warns 0, none suppressed).
- The static linter checks side, order and R-size only. It does not check M5 construction rules, so a CLEAN row does not mean the cards are compliant. That is scored under 4.5 and detailed in `2026-07-01_feedback.md`.

## 5. Feedback
See `qa/ftse_qa1/2026-07-01_feedback.md`.
