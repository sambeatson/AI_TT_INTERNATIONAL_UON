# Trust Score v3.7 — FTSE 100 daily report, D = 2026-05-13 (run ftse_qa1)

Report: `reports/md/FTSE100_EuroStoxx_Daily_Report_13May2026.md`
Data basis: `data/levels/UK100_by_date/2026-05-13.csv` (`last_bar_date` = 2026-05-12 < D, leak-free, checked). Cash-session basis (`_cash`, 08:00–16:30 London) because the report claims a cash-index basis; full-day (`_full`) shown where it explains a figure. `engine/qa_slice_stats.py --cash-open 10:00 --cash-close 18:30` run with the report's five closes.

## Machine-readable result
```
c1=2
c2=4
c3=0
c4=3
c5=2
total=44
band=Low
override=hallucinated_source
card_integrity=100
n_cards=3
n_duds=0
n_warns=0
```
Secondary finding: a restriction breach is also present (module codes, variable names, numeric weights in the body; see 5.4). It lowers C1 by one level (3 → 2). The cap applied is the stricter one (Low, 40–59). Raw arithmetic before override: C1 8 + C2 17 + C3 0 + C4 13 + C5 6 = 44.

## 1. Section 7 checklist

| Row | Notes | Evidence (location) | Score |
|---|---|---|---|
| 1.1 Variables respected | FTSE 100 cash primary, Euro Stoxx reference only; counters USDX / S&P 500 / DAX 40 present; 5-session lookback; London tz; 07:00 UK anchor stated on Trade 1. Sources are aggregators and media (Trading Economics, Yahoo, Investing.com, Fidelity/Sharecast, Google Finance, CNBC, a Wikipedia reference); no index-provider or exchange primary in §4 (FTSE Russell is asserted in §5 but is not in the §4 table or the §20 source list). Investing.com is described in §5 as CFD quotes yet is used to "verify H/L" in §4. | §2, §4, §5, §20 | 3 |
| 1.2 Coverage and currency consistent | Currency fine. Calendar weekday labels drift: §13d "Wed 14 May" (14 May 2026 is Thursday), "Thu 15 May" (Friday), "Fri 16 May" (Saturday), "Mon 19 May" (Tuesday), "Wednesday 21 May" (Thursday); §12 "Tuesday 13 May" vs §13d "Wed 13 May" (13 May is Wednesday). §1 says the downtrend runs over "the last 25 sessions, having peaked ... 27 February", but §9 admits that peak is outside the 25-session window. | §1, §9, §12, §13d | 2 |
| 1.3 Audience and tone | Professional strategist register, trading-and-risk use. | §1, §18 | 4 |
| 2.1 Sections present and ordered | §1–§21 all present and in order, §13a–d and §21a–d present. §7 is a narrative placeholder (no figure; accepted per brief, noted). | headings | 4 |
| 2.2 Scorecard as table | §6 is a table but has no Trend column (has Δ% instead); §11 daily/weekly/monthly tables ordered R3→S3. | §6, §11 | 4 |
| 2.3 Method steps visible | §8 candle-by-candle plus sequence present. §5 consensus build is prose with no weighted-median working. §9 gives no KER(13, EMA 3) value although §1 and §20 rely on a KER label. §9 regime has persistence/overlap in words only. | §5, §8, §9 | 3 |
| 3.1 Quantitative claims sourced | §1, §12, §14 carry many unsourced figures: gilt 10y 5.13% / +12bp, Brent >$100, WTI $99–102, "70 Labour MPs", Vodafone FY26 figures, VIX 18.38 (+6.92%), GBP/USD −0.6%, "~80% non-UK revenue". None points to a §4/§13 row. | §1, §12, §14 | 2 |
| 3.2 Citations exist and contain data | (a) CNBC `cnbc.com/2026/05/10/stock-market-today` is attributed to an article of Mon 11 May (S&P close 7,412.84); 10 May 2026 is a Sunday, so URL date and article date are impossible together. (b) CNBC `cnbc.com/2026/05/12/europe-markets...` is a truncated, non-resolvable URL. (c) Fidelity/Sharecast 12 May 14:20 "10,231.23, −0.4%" is consistent with the feed (bars near 10,218–10,234 at 14:20 UK) and passes. Under the brief's rule a self-contradictory dated source counts as fabricated. In addition §6 marks 6–8 May OHLC "✓ within tol" against two named sources while the bars differ from the feed by up to 370 pts (see §2). | §4, §13a, §6 | 0 |
| 3.3 Calculations transparent | RSI2 not shown, and it does not reproduce from the report's own closes (see §2). KER not stated. ATR(14) stated (95) but 28% below feed. Pivot arithmetic wrong in 5 of 6 daily levels, 4 of 6 weekly, 1 of 6 monthly (see §2). §21a does not sum correctly (see 4.6). | §6, §9, §11, §21a | 1 |
| 3.4 Numbers reconcile | The D-1 close 10,265.32 is identical in §1, §3, §4, §6. Pivot levels on the cards match §11 values (R2 10,327, weekly P 10,356, weekly S1 9,967). Trade 1 entry 10,250 differs from the stated D-1 close; Trade 1 stop buffer does not equal 0.25×ATR; Trade 3 "midpoint" claims conflict with its own swing; §21d TP1 hit rate (3/4) conflicts with §21c (2 of 4 closed trades hit TP1). | §1–§6, §11, §21 | 2 |
| 4.1 Pillars conclude | §8, §9, §10 carry labels. §12 and §14 sub-blocks carry directions; §12 closes with "BINARY". | §8–§14 | 4 |
| 4.2 Cross-asset interpreted | §10 gives mechanisms (earnings translation for USDX, energy weight). The 5-day labels disagree with the feed: USDX "Up — Strong" (close 98.49 on 5 May → 98.27 on 12 May, −0.2%); S&P 500 "Sideways → Down" (7,274 → 7,402, +1.8%, near highs). VIX in §14 quoted 18.38 (+6.92%); feed shows 19.06 (−2.4% on the day). | §10, §14 | 3 |
| 4.3 Synthesis reconciles tensions | §15/§16/§18 reconcile range vs downward bias. Not reconciled: §9 states VOLator slope positive (expanding, "regime in transition") yet labels RANGE and builds a range-fade card; §8 says "slight upside skew" while §21a scores the short-term signal −0.6; calendar claim that a UK labour print is the main event is not on the D calendar (see 5.3). | §8, §9, §21a | 2 |
| 4.4 Calibrated language | §17 is exactly one sentence, no hedge stacking. §3 Confidence High vs §18 Medium for the same call is a mild inconsistency. | §3, §17, §18 | 4 |
| 4.5 Card construction (protocol) | Trade 1 not a market entry at D-1 close, runner stop on the wrong side, no reference close/gap, no R/ATR multiple; Trade 2 TP1/TP2 are not 1R/2R, tier selection ignored, invalidation inside stop; Trade 3B uses 3A fib geometry on a 5-day swing, TP1 mislabelled as mid-range, invalidation equals stop, 3B gate (VOLator ≤ 0) fails on the report's own §9. The static linter reports CLEAN; it does not test these (see §4). | §21b | 1 |
| 4.6 §21a derivation traceable | Medium-regime term written −0.20 × 0.5 (the signal is −0.20 and the weight 0.5; the rule weight is 0.20 and a Range maps to 0). Only four of six signals shown (VOLator and KER absent); the four shown sum to −0.343, which is the quoted total only if the other two are zero. Weights-basis line correct ("defaults") but numeric weights appear in §20 body. | §21a, §20 | 2 |
| 5.1 Data dated, staleness flagged | Most rows dated; Yahoo STOXX row "Reference" undated; no single-source-indicative flag anywhere although 6–8 May O/H/L are unsupported by the feed. | §4, §6, §19 | 3 |
| 5.2 Assumptions up front | The "anchor override" is stated in §19/§20 but is vacuous (the anchor is 07:00 UK, i.e. the default, so nothing is overridden) and no card carries an anchor caveat. Trade 1 entry is an "anchor-adjusted expected open" price, i.e. a synthesised level, not stated up front. | §19, §20, §21b | 2 |
| 5.3 Red flags surfaced | §12/§15 risks surfaced. §13d event collisions not carried to cards. The D calendar (leak-free slice) lists no UK labour/claimant release on 13 May; it lists US PPI (HIGH, 13:30 UK), EIA crude stocks (HIGH, 15:30 UK), US 30-Year auction (HIGH, 18:00 UK), Lagarde speech (HIGH, 20:50 UK), euro-area GDP/industrial production (10:00 UK). None of these is named; the report's "single highest-impact event" is absent from the D calendar. | §13d, §21b | 3 |
| 5.4 Restrictions honoured | Breaches: module codes in the body ("M3-derived regime classification" §16, "M5 §21a" and "M5 trace" §20, "per §7d" and "X9" references); variable-name tokens (W_SHORT_TECH, W_MEDIUM_REGIME, W_VOLATOR, W_KAUFMAN, W_SENTIMENT, W_CROSS_ASSET) and numeric weights printed in §20 (M4 says weights never appear in the body); §21a states "Strategies are not suppressed in this run per explicit instruction" although the 3B gate fails on the report's own §9; §5 uses CFD (Investing.com) quotes for intraday range; Wikipedia used as a price-evidence source; Trade 1 entry 10,250 is a synthesised "expected open zone" price. | §5, §16, §20, §21 | 1 |

## 2. Category 3 reconciliation against the data (cash basis; tolerance close ±5, O/H/L ±10)

Bars, report vs `prev_*_cash` / slice cash session:

| Date | Field | Report | Cash feed | Δ (report − feed) | Note |
|---|---|---|---|---|---|
| 12 May | Open | 10,233.56 | 10,190.5 | +43.1 | equals the full-day open 10,233.5, not the cash open |
| 12 May | High | 10,286.57 | 10,250.3 | +36.3 | full-day high 10,291.6 (−5.0) |
| 12 May | Low | 10,226.50 | 10,145.9 | +80.6 | 10,145.9 on both bases; report's low is above the feed's low |
| 12 May | Close | 10,265.32 | 10,250.1 | +15.2 | full-day close 10,277.0 (−11.7); exceeds the 15-pt failure threshold |
| 11 May | O/H/L/C | 10,225 / 10,290 / 10,210 / 10,269.43 | 10,254.8 / 10,284.2 / 10,221.9 / 10,264.1 | −29.8 / +5.8 / −11.9 / +5.3 | open and low outside tolerance, close marginal |
| 8 May | O/H/L/C | 10,560 / 10,580 / 10,164 / 10,221 | 10,189.8 / 10,271.7 / 10,174.8 / 10,222.4 | +370.2 / +308.3 / −10.8 / −1.4 | open and high grossly wrong; the −3.26% "marubozu" is not in the feed (feed bar is open 10,189.8, close 10,222.4) |
| 7 May | O/H/L/C | 10,600 / 10,683 / 10,545 / 10,565 | 10,451.2 / 10,451.2 / 10,277.5 / 10,282.6 | +148.8 / +231.8 / +267.5 / +282.4 | every field outside tolerance |
| 6 May | O/H/L/C | 10,490 / 10,612 / 10,425 / 10,602 | 10,336.0 / 10,491.8 / 10,321.9 / 10,442.3 | +154.0 / +120.2 / +103.1 / +159.7 | every field outside tolerance |

Derived quantities:

| Item | Report | Feed (cash) | Δ |
|---|---|---|---|
| RSI2 12 May | 29.8 | 74.87 (full 74.11) | −45.1 |
| RSI2 from the report's own closes (10,221 / 10,269.43 / 10,265.32) | 8.7 / 32.5 / 29.8 | 0.0 / 12.3 / 92.2 | arithmetic does not reproduce: 8 May −8.7, 11 May +20.2, 12 May −62.4 |
| ATR(14) | ≈95 | 131.94 (full 143.21) | −36.9 (−28%) |
| 5-day swing high / low | 10,683.65 / 10,164.26 | 10,491.8 / 10,145.9 | +191.9 / +18.4 |
| 25-day swing high / low | (10,910.55 on 27 Feb, outside window) / 10,164 | 10,697.5 (8 Apr) / 10,145.9 | |
| April monthly H / L / C | ~10,920 / ~10,170 / ~10,490 | full-day H 10,727.5, L 10,170.7 (monthly P 10,418.8 implies a lower close) | H +192 |
| Short-term candle read | 12 May "inside-flat, RSI2 exiting oversold" | cash bar: open 10,190.5, close 10,250.1, range 10,145.9–10,250.3, below the report's own "8 May low 10,164" | the support the report says was not breached is undercut by 18.4 pts in the feed |

Daily pivots (report's own H/L/C 10,286.57 / 10,226.50 / 10,265.32 recomputed with the brief's formulas, then vs the cash level file):

| Level | Report | Recomputed from report H/L/C | Cash file | Report − cash file |
|---|---|---|---|---|
| R3 | 10,386.96 | 10,352.50 | 10,389.37 | −2.4 |
| R2 | 10,326.61 | 10,319.53 | 10,319.83 | +6.8 |
| R1 | 10,295.94 | 10,292.43 | 10,284.97 | +11.0 |
| P | 10,259.46 | 10,259.46 | 10,215.43 | +44.0 |
| S1 | 10,229.27 | 10,232.36 | 10,180.57 | +48.7 |
| S2 | 10,199.39 | 10,199.39 | 10,111.03 | +88.4 |
| S3 | 10,168.71 | 10,172.29 | 10,076.17 | +92.5 |

Arithmetic errors in the report's own daily pivots: R1 (+3.5), S1 (−3.1), R2 (+7.1), R3 (+34.5), S3 (−3.6).

Weekly pivots (report inputs H 10,683 / L 10,164 / C 10,221): arithmetic correct for P, R2, S2 only; recomputed R1 10,548 (report 10,486), S1 10,029 (report 9,967), R3 11,067 (report 11,221), S3 9,510 (report 9,448). Versus the cash file (implied prior-week H 10,491.8, L about 10,162.8, C 10,222.4): P 10,356 vs 10,292.33 (+63.7); R1 10,486 vs 10,421.87 (+64.1); S1 9,967 vs 10,092.87 (−125.9); R2 10,875 vs 10,621.33 (+253.7); S2 9,837 vs 9,963.33 (−126.3); R3 11,221 vs 10,750.87 (+470.1); S3 9,448 vs 9,763.87 (−315.9). The weekly high input (10,683) is the root error.

Monthly pivots: R3 11,990 is an arithmetic error (recomputed 11,633 from the report's own H/L/C). Versus the cash file: P 10,527 vs 10,418.8 (+108.2); R1 10,883 vs 10,650.0 (+233); S1 10,134 vs 10,140.1 (−6.1); R2 11,277 vs 10,928.7 (+348); S2 9,777 vs 9,908.9 (−132); R3 11,990 vs 11,159.9 (+830); S3 9,384 vs 9,630.2 (−246).

Position statement in §11 ("below all pivots") is wrong on the cash file: D-1 cash close 10,250.1 is above daily P 10,215.43 and below weekly P 10,292.33.

§21c backtest rows rest on these bars: the 6, 7, 8 May entries (10,490 / 10,600 / 10,560) sit 150–370 pts from the feed's opens, so the aggregates in §21d are not reproducible. §21d also states a TP1 hit rate of 3/4 while only two of the four closed trades reach TP1; the limitations paragraph is not the mandatory verbatim text.

Calendar for D (leak-free slice, scheduled-only): no UK labour release; HIGH events are US PPI m/m 13:30 UK, EIA crude stocks 15:30 UK, US 30-Year bond auction 18:00 UK, ECB President Lagarde speech 20:50 UK.

## 3. Category roll-up

| Cat | Level | Multiplier | Points | Justification |
|---|---|---|---|---|
| 1 Prompt adherence (20) | 2 | 0.40 | 8 | Rows 3 / 2 / 4 average 3.0; restriction breach (module codes, variable names, forced strategies) lowers it one level. |
| 2 Structure (20) | 4 | 0.85 | 17 | All 21 sections and sub-sections present and ordered; §6 lacks Trend, §7 text-only, KER missing. |
| 3 Accuracy (25) | 0 | 0.00 | 0 | Rows 2 / 0 / 1 / 2 average 1.25 (level 1); hallucinated-source override sets 0. 6–8 May bars off by up to 370 pts, close off by 15.2, RSI2 does not reproduce, pivot arithmetic wrong, impossible CNBC URL date. |
| 4 Reasoning (20) | 3 | 0.65 | 13 | Rows 4 / 3 / 2 / 4 / 1 / 2 average 2.67. Mechanisms present; regime gate and card construction fail. |
| 5 Currency and transparency (15) | 2 | 0.40 | 6 | Rows 3 / 2 / 3 / 1 average 2.25. Vacuous override caveat, collisions not carried to cards, restrictions breached. |

## 4. Total, band, override
- Total = 8 + 17 + 0 + 13 + 6 = **44 → Low (40–59)**.
- Override check: hallucinated source — YES (CNBC URL dated 10 May, a Sunday, for a Monday 11 May article; truncated CNBC URL; OHLC marked "corroborated by two named sources" that cannot be matched to the feed). Cap Low and C3 = 0 applied. Restriction breach — also YES (row 5.4), C1 lowered one level; it would cap at Moderate, which is looser than the Low cap already applied.

## 5. Card Integrity (linter rows, copied verbatim from `qa/ftse_qa1/lint_static/2026-05-13.csv`)

| card_id | report_date | strategy | flags | dud |
|---|---|---|---|---|
| 2026-05-13_Trade_1 | 2026-05-13 | Trade Card 1 - Daily Directional (FTSE 100) | CLEAN | False |
| 2026-05-13_Trade_2 | 2026-05-13 | Trade Card 2 - Regime-Aware Pivot (FTSE 100) | CLEAN | False |
| 2026-05-13_Trade_3B | 2026-05-13 | Trade Card 3 - Complex (Regime Variant 3B: Range Mean-Reversion) | CLEAN | False |

Per card: 100 − 40·0 − 10·0 = 100 for each. Report level = mean = **100**; n_cards=3, n_duds=0, n_warns=0.

The static linter does not test order type, tier selection, TP1/TP2 = 1R/2R spacing, the regime gate, runner-stop side or invalidation distance. Those defects are scored under C4 row 4.5 and listed in the feedback file, not in Card Integrity.
