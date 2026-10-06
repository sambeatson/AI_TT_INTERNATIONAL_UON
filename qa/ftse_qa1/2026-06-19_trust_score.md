# Trust Score v3.7 QA — FTSE100_Report_19-Jun-2026.md (D = 2026-06-19)

Data basis: `data/levels/UK100_by_date/2026-06-19.csv` (`last_bar_date` = 2026-06-18 < D, checked). Cash-session figures (08:00–16:30 London, 10:00–18:30 broker) are the reference; full-day figures quoted where they differ. D-1 = Thu 18 Jun 2026.

## Score line

```
c1=3
c2=3
c3=2
c4=3
c5=3
total=59
band=Low
override=none
card_integrity=100.0
n_cards=3
n_duds=0
n_warns=0
```

## 1. Section 7 checklist

| Row | Item | Notes / evidence location | Score |
|---|---|---|---|
| 1.1 | Variables respected | Asset is the FTSE 100 cash index with Euro Stoxx 50 as a reference, counters USDX / S&P 500 / DAX 40, GBP and index points (§2). Defects: (a) as-of is 19 Jun (D) and the lookback is 15–19 Jun (§2, §6), where the brief requires an as-of of the London close of D-1 (18 Jun) and a 12–18 Jun window; (b) daily-open anchor is 00:00 UK, not 07:00 UK (disclosed in §2/§20 as an override "as requested"; the brief calls it a deviation to note); (c) §4 lists six sources: AJ Bell, Yahoo, Trading Economics, Fidelity/Sharecast, Investing.com, MarketScreener. None is an index-provider or exchange source. The sell-side tier appears only in §13a (UBS); (d) §10/§14 use a "WSJ Dollar Index ≈ 97.15" figure for the USDX counter, while the slice USDX is ~100.9. | 2 |
| 1.2 | Coverage & currency consistent | The report's data runs through D itself (Fri 19 Jun row in §6, §11 daily pivots "from 19 Jun H/L/C", §13c Fri row, §21c Fri 19 labelled t−1). The §20 timestamp says "generated 21 Jun 2026", after D. The brief requires data dated D-1 or earlier. The D row cannot be verified from the slice, and I make no statement about it. The calendar slice lists 19 Jun as a USD holiday (Juneteenth), yet §10/§15 cite an "S&P 500 firm Friday close (+1.08%)" without comment. Currency and units are consistent (GBP, points). | 2 |
| 1.3 | Audience & tone | Professional strategist tone, trading-and-risk language, Tier-1 event and invalidation vocabulary, no retail tone. Closing disclaimer is generic but acceptable. | 4 |
| 2.1 | Sections present & ordered | §1–§21 all present in order, including §13a–d and §21a–d. §7 carries five chart headings with no images or captions except Chart 3 (accepted per the brief note on pandoc). | 4 |
| 2.2 | Scorecard as a table | §6 is a table, but "Sources" is a single combined column, not separate Source A / Source B / Final columns. §11 daily pivots run R5→S5 (five each side). Weekly and monthly tables show only R1/P/S1 (weekly adds S2), not the required R3→P→S3. | 3 |
| 2.3 | Method steps visible | §4 observations, §5 consensus build and §8 candle-by-candle sequence are visible. §9 gives thresholds only (">0.55", "<0.50"), no measured overlap/persistence values and no VOLator numbers. The §9 percentile claim does not reproduce (see 3.4). | 3 |
| 3.1 | Quantitative claims sourced | §1, §12, §14 carry unsourced figures with no pointer to §4/§6/§13a: Antofagasta −6.2%, Fresnillo −5.4%, Lloyds −1.8%, £23.3bn PSNB, retail +1.2%, Brent 80.17, WTI 76.14, GBP/USD 1.3237, 10Y gilt 4.95%, "WSJ Dollar Index 97.15", "+21% YoY". | 2 |
| 3.2 | Citations exist & contain data | No URLs given. Three spot-checked: (1) AJ Bell / Yahoo / TE 19 Jun closes are mutually consistent and arithmetically coherent (−36.43 pts = −0.350%). (2) Investing.com 18 Jun "UK shares lower **at close**; UK100 −0.40%" contradicts the report's own Thu close (−1.04% in §6; −1.08% on the cash slice). (3) Fidelity/Sharecast "FTSE −1.2% Thu" matches neither the §6 move (−1.04%) nor the Investing.com −0.40% for the same day. UBS "wk" is undated. The contradictions are serious but do not establish a fabricated source (they could be stale intraday snapshots), so no override is applied. | 2 |
| 3.3 | Calculations transparent | RSI2 for Wed/Thu/Fri (100.0 / 17.8 / 0.0) reproduces exactly from the report's own closes. Pivot arithmetic in the daily table is correct from the report's own H/L/C (P 10,378.25, R1 10,403.60, S1 10,337.92, R2 10,443.93, S2 10,312.57, R3 10,469.28, S3 10,272.24 all verified). Failures: ATR(14) stated ≈74.5 vs 113.4 (cash) / 139.6 (full), −34% / −47%. Mon RSI2 0.0 vs slice 89.71 and Tue 66.8 vs 79.01. Thu RSI2 17.8 vs level-file 2.74 (cash) / 0.0 (full), Δ +15.1. KER(13) stated +0.058; my EMA3-smoothed cash-close reproduction gives 0.166 (raw 0.111), not reproducible. Tue close is wrong by 25.1 pts (>15, a Category 3 failure per brief §4). | 2 |
| 3.4 | Numbers reconcile | Close 10,363.27 is consistent in §1/§3/§4/§6/§11/§21. Failures: §13c Wed "+0.14%" vs §6 +0.23% (10,485.00 → 10,508.61). §13c/§13a Thu "−1.2%" vs §6 −1.04%. §9 range top "~10,570" (slice 25-d high 10,574.6 on 15 Jun) lies inside the 15–19 Jun window, but §6 shows a 5-day max high of 10,520, and §8/§15/§16 treat 10,520 as the week high. §9 "latest close around 40–45th percentile" does not reproduce (own numbers: (10,363.27−10,127)/(10,570−10,127) = 53%; level file: D-1 close 10,399.6 sits at 61%). §21a score is −0.297 (−0.20−0.057−0.04) and is shown as −0.29. Trade 1 BE stop and "within ~0.15×ATR of Fri low" wording are inconsistent with the table (see §4). Card pivot confluence relies on report pivots that do not match the level file (see §3 below). | 2 |
| 4.1 | Pillars conclude | §8 ("Exhaustion — reversal risk, bearish tilt") and §9 ("Neutral-to-bearish") end in labels consistent with their content. §10 gives per-counter status/implication but no net label. §12 tags each block price-negative/supportive but has no net direction. §14 ends on a watch item with no direction label. | 3 |
| 4.2 | Peer / cross-asset interpreted | A mechanism column is given for USDX, S&P 500 and DAX, and the S&P divergence is flagged. Weaknesses: the lead driver (oil / Brent, dollar-earner and energy weight) has no §10 counter row. The USDX read ("flat / +0.1%") contradicts the slice (USDX +0.86% Wed 17 Jun and +0.45% Thu 18 Jun, ≈+1.1% 12→18 Jun close-to-close), so the stated "no tailwind" mechanism rests on a wrong premise. DAX mechanism is generic. | 2 |
| 4.3 | Synthesis reconciles tensions | §15/§16/§18 reconcile the short-term bearish vs ranging regime and flag the S&P contradiction. They do not reconcile: the Trade 3B RANGE gate that §21b itself says is only partly met ("treat as transitional"); the report's 5-day high 10,520 vs its 25-day range top; or the BoE decision on 18 Jun. | 3 |
| 4.4 | Calibrated language | §17 is exactly one sentence with a single conditional. Confidence (Medium) is stated in §1/§3/§18. | 4 |
| 4.5 | Card construction (protocol) | All three cards deviate from fixed M5 rules: Trade 1 is a sell-stop, not market at the anchor, and its stop buffer is 1.4 pts instead of 0.25×ATR. Trade 2 enters between P and R1 instead of at R1/R1.5/R2, and its stop is neither 3.5×ATR nor structural+0.25×ATR. Trade 3B enters at ~60% of the 25-d range instead of 78.6–88.6%, and its TP2 is not the far side −10%. The U3 breakeven stop is on the adverse side on Trade 1 and Trade 2. Sell-limits at 10,388 and 10,395 are below the D-1 close of 10,399.6. Detail in feedback. | 1 |
| 5.1 | Data dated; staleness flagged | Single-source O/H/L carry asterisks, and weekly/monthly pivots are flagged INDICATIVE (good). Gaps: UBS "wk" undated. §12/§14 figures lack as-of stamps. §13d is entirely undated ("Wk ahead"). | 3 |
| 5.2 | Assumptions up front | The anchor override is stated in §2, §20 and on every card. Default weights, sentiment-0.0 backtest fallback and the lock-window status are disclosed in §20. Single-source flags are carried onto Trade 2/3B. | 4 |
| 5.3 | Red flags surfaced | Tier-1 collision with the US–Iran signing is carried into card caveats. Missed from the slice calendar: BoE Interest Rate Decision 18 Jun (HIGH, 14:00 broker = 12:00 London; rate 3.75% unchanged, MPC vote 7 unchanged / 2 hike, previous 8/1), which the report mentions only as a "conflicting narrative" in §20; UK labour data on 18 Jun 09:00 broker (unemployment 4.9% vs 5.3% consensus, employment change +100k vs +239k); euro-area CPI y/y 3.2% vs 2.6% consensus on 17 Jun (HIGH). The USD holiday on 19 Jun is not flagged. | 3 |
| 5.4 | Restrictions honoured | No bracketed variable names, module codes or framework name seen. Futures not used. Concerns: Fri open (10,399.70) equals the Thu close to the cent and is presented as CORROBORATED (Δ 0.00) and un-starred, which looks derived rather than sourced. A different index (WSJ Dollar Index) substitutes for the USDX counter. Internal process wording ("forward-test session 1 of the 20-session lock window", "v2.1 baseline") leaks into the report. | 3 |

Category means: C1 = (2+2+4)/3 = 2.67 → 3. C2 = (4+3+3)/3 = 3.33 → 3. C3 = (2+2+2+2)/4 = 2.0 → 2. C4 = (3+2+3+4+1)/5 = 2.6 → 3. C5 = (3+4+3+3)/4 = 3.25 → 3.

## 2. Category roll-up

| # | Category | Level | Multiplier | Points | Justification |
|---|---|---|---|---|---|
| 1 | Prompt adherence (20) | 3 | 0.65 | 13.00 | Right asset/counters/currency. As-of is D not D-1, anchor 00:00 not 07:00, no index-provider/exchange source, WSJ index substituted for USDX. |
| 2 | Structural alignment (20) | 3 | 0.65 | 13.00 | All 21 sections present and ordered. Scorecard source columns merged, weekly/monthly pivots incomplete, §9 shows thresholds not measurements. |
| 3 | Accuracy & evidence (25) | 2 | 0.40 | 10.00 | Tue close −25.1 pts; Mon O/H −97.6/−99.6; Thu O/H +44.7/+36.2; ATR14 −34%; weekly P/S1/S2 and monthly S1 off; USDX direction wrong; self-contradicting sentiment sources. |
| 4 | Reasoning & judgment (20) | 3 | 0.65 | 13.00 | Sound narrative structure and a single-sentence forecast, but the cross-asset premise is wrong and card construction fails M5 on all three cards. |
| 5 | Currency & transparency (15) | 3 | 0.65 | 9.75 | Override and single-source caveats well disclosed. Missing BoE/EUR CPI/US-holiday red flags, undated forward calendar, report as-of past D-1. |

## 3. Total, band, override

- Total = 13.00 + 13.00 + 10.00 + 13.00 + 9.75 = 58.75 → **59**
- Band: **Low** (40–59)
- Override check: hallucinated source: none (the contradictions in 3.2 are reconciliation defects, not proven fabrication). Restriction breach: none identified (the anchor override and as-of choice are disclosed and attributed to a run instruction, so they are scored under C1 rows). **override=none**

## 4. Category 3 data comparison (report vs level file, cash basis; |Δ| thresholds: close 5, O/H/L 10)

| Day | Field | Report | Slice cash | Δ | Verdict |
|---|---|---|---|---|---|
| Mon 15 | O | 10,460* | 10,557.6 | −97.6 | Discrepancy |
| Mon 15 | H | 10,475* | 10,574.6 | −99.6 | Discrepancy |
| Mon 15 | L | 10,422* | 10,422.8 | −0.8 | OK |
| Mon 15 | C | 10,435.69 | 10,441.2 | −5.5 | Marginal discrepancy |
| Tue 16 | O | 10,440* | 10,449.3 | −9.3 | OK |
| Tue 16 | H | 10,498* | 10,529.6 | −31.6 | Discrepancy |
| Tue 16 | L | 10,433* | 10,434.9 | −1.9 | OK |
| Tue 16 | C | 10,485.00* | 10,510.1 | −25.1 | **Failure (>15)** |
| Wed 17 | O | 10,494 | 10,494.9 | −0.9 | OK |
| Wed 17 | H | 10,520* | 10,513.3 | +6.7 | OK |
| Wed 17 | L | 10,468 | 10,470.9 | −2.9 | OK |
| Wed 17 | C | 10,508.61 | 10,513.3 | −4.7 | OK |
| Thu 18 (D-1) | O | 10,505* | 10,460.3 | +44.7 | Discrepancy |
| Thu 18 (D-1) | H | 10,512* | 10,475.8 | +36.2 | Discrepancy |
| Thu 18 (D-1) | L | 10,379* | 10,372.6 | +6.4 | OK |
| Thu 18 (D-1) | C | 10,399.70 | 10,399.6 | +0.1 | OK |
| RSI2 Mon / Tue / Wed / Thu | | 0.0 / 66.8 / 100.0 / 17.8 | 89.71 / 79.01 / 100.0 / 2.74 | −89.7 / −12.2 / 0 / +15.1 | Mon, Thu discrepant (Thu full-day: 0.0) |
| Trend label Mon | | Bearish | Neutral by the stated rule (C<O, RSI2 89.7) | | Discrepancy |
| ATR14 | | ≈74.5 | 113.4 cash / 139.62 full | −38.9 / −65.1 | Discrepancy |

Pivots (report vs level file, cash). Note the report's daily pivots come from the 19 Jun H/L/C, whereas the session-D pivots must come from D-1 (18 Jun).

| Level | Report | Level file | Δ |
|---|---|---|---|
| Daily P | 10,378.25 | 10,416.0 | −37.8 |
| Daily R1 / S1 | 10,403.60 / 10,337.92 | 10,459.4 / 10,356.2 | −55.8 / −18.3 |
| Daily R2 / S2 | 10,443.93 / 10,312.57 | 10,519.2 / 10,312.8 | −75.3 / −0.2 |
| Daily R3 / S3 | 10,469.28 / 10,272.24 | 10,562.6 / 10,253.0 | −93.3 / +19.2 |
| Weekly P | 10,390.26 | 10,353.07 | +37.2 |
| Weekly R1 / S1 | 10,553.18 / 10,308.79 | 10,579.93 / 10,232.63 | −26.8 / +76.2 |
| Weekly S2 | 10,145.87 | 10,005.77 | +140.1 |
| Monthly (May) P | 10,387.27 | 10,370.4 | +16.9 |
| Monthly R1 / S1 | 10,579.17 / 10,217.38 | 10,599.6 / 10,180.8 | −20.4 / +36.6 |

Back-solving the report's weekly pivots gives a prior-week low of ≈10,227.3 against 10,126.2 on the slice (+101.1). Back-solving the monthly pivots gives a May low of ≈10,195.4 against 10,141.2 (+54.2).

The D (Fri 19 Jun) row, the Fri-based daily pivots, the "+1.08%" S&P figure and the UK fiscal data are dated on D and cannot be verified from D-1 data. They are not scored as accurate or inaccurate.

## 5. Card Integrity (linter rows copied verbatim from `qa/ftse_qa1/lint_static/2026-06-19.csv`)

| card_id | strategy | flags | dud | integrity |
|---|---|---|---|---|
| 2026-06-19_Trade_1 | Trade 1 - Daily Directional (SHORT) | CLEAN | False | 100 |
| 2026-06-19_Trade_2 | Trade 2 - Pivot, RANGE regime (sell-high / buy-low at extremes) | CLEAN | False | 100 |
| 2026-06-19_Trade_3B | Trade 3B - Mean-Reversion (RANGE regime, KER Ranging-Neutral, VOLator slope positive but downside-driven) | CLEAN | False | 100 |

Report-level Card Integrity = mean(100, 100, 100) = 100.0 (3 non-suppressed cards, 0 DUD, 0 WARN). The linter is static and the rows were not re-derived. The CLEAN result does not cover the M5 construction defects scored under row 4.5 (entry type, stop rule, tier placement, breakeven side), which the static linter does not test.
