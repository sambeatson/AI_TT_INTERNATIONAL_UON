# Trust Score v3.7 — FTSE 100 Daily Report, 5 June 2026 (run ftse_qa1)

Report: `reports/md/FTSE100_Report_05Jun2026.md` · D = 2026-06-05 · D-1 = Thu 2026-06-04
Data check: level file `last_bar_date` = 2026-06-04 < D (leak-free). Slice stats run with `--cash-open 10:00 --cash-close 18:30`. Basis claimed by the report: cash index (§2, §3, §4).

## Machine-readable result
```
c1=3
c2=4
c3=0
c4=3
c5=2
total=49
band=Low
override=hallucinated_source
card_integrity=96.7
n_cards=3
n_duds=0
n_warns=1
```
Override note: `hallucinated_source` is the binding override (cap Low 40–59, C3 forced to 0). A `restriction_breach` is ALSO present (see 5.4: reconstructed OHLC presented as corroborated; module code "M5" in §20), so C1 is taken one level down (4 → 3). Pre-override C3 would have been 1.

## 1. Section 7 checklist

| Row | Notes | Evidence | Score |
|---|---|---|---|
| 1.1 Variables respected | FTSE 100 cash primary, STOXX reference only; counters USDX/S&P/DAX (+STOXX) present; as-of/tz/lookback correct; GBP points. Source list has 6 rows but 2 are Trading Economics, Kalkine and Yahoo are aggregators; no sell-side/exchange-tier evidence beyond an unspecified "FTSE Russell / LSE" row. §20 calls the 07:00 UK anchor both "overridden per analyst instruction" and "retained"; 07:00 is the configured anchor, so the "override" wording is confused. | §2, §4, §10, §20 | 3 |
| 1.2 Coverage & currency consistent | Data dates are D-1 or earlier, session D. But §13d "next 5 sessions" lists 18 Jun BoE and "~11–18 Jun" CPI (outside the window, undated), and "Early Jun payrolls follow-through" in place of the actual Fri 5 Jun NFP. No currency drift. | §13d | 4 |
| 1.3 Audience & tone | Strategist tone, no retail language. | §1, §18 | 4 |
| 2.1 Sections ordered | §1–§21 all present and in order, §13a–d and §21a–d present. §7 has five chart captions, no images (accepted as placeholder; noted). | headings | 4 |
| 2.2 Scorecard as table | §6 is a proper table with all columns. §11 has weekly and monthly tables only: NO daily pivot table. Tables run R5→S5 (5 per side) not R3→S3 (3 per side). | §6, §11 | 3 |
| 2.3 Method steps visible | §4→§5 observations to consensus; §8 candle-by-candle plus sequence; §9 overlap, persistence, VOLator, KER. | §4–§9 | 4 |
| 3.1 Quantitative claims sourced | §12 numbers (AstraZeneca/GSK, record ~£88bn dividends, ~80% overseas revenue, Brent "high-90s", CPI 3.3% / 2.8%) carry no source or section pointer. §14 "VIX rose ~3% on 3 Jun" is wrong (see 3.4). | §12, §14 | 2 |
| 3.2 Citations exist & contain data | Three sources checked. (a) TE 3 Jun: quote "fell 32 points or 0.30 percent", normalized 10,342, implies prior close ≈10,374; the report's own §6 gives 2 Jun close 10,421 (move −79 pts / −0.76%). Figure does not match its own quote. (b) Yahoo 3 Jun 10,303.12 "−0.28%" implies prior ≈10,332, matches no close in §6; and it contradicts TE's same-day, same-basis 10,342 by 39 pts (slice cash 3 Jun close 10,341.7). (c) Investing.com 4 Jun "Open 10,373.9; 10,322–10,383" vs slice cash 4 Jun open 10,301.0, range 10,236.5–10,360.2 (open +73, low +85.5). Also "FTSE Russell / LSE official close ≈10,315" vs slice cash close 10,343.3 (−28.3). Under brief §2 row 3.2 (figure not matching its own quote = fabricated) this fails. | §4, §6, §13a | 0 |
| 3.3 Calculations transparent | RSI2 reproduces from the report's own closes (43.1/24.0/0.0 vs shown 43.7/24.1/0.0) so the arithmetic is sound; but inputs are wrong. ATR(14) given only in §20 as ≈66.7 (slice cash 113.73, full 137.39; −47.0 / −41%); not reproducible. Weekly and monthly pivots do not reproduce from the real period H/L/C (see §3 below). KER stated; §21a score reproduces only once the unlisted VOLator term (−0.05) is added. | §6, §11, §20, §21a | 2 |
| 3.4 Numbers reconcile | Internally the 10,315 close is identical in §1, §3, §4, §6, §21b and pivots on cards = §11. But vs the slice D-1 cash close 10,343.3 it is off by −28.3 (>15 pt Category 3 failure); 29 May close +19.0, 1 Jun +71.5, 2 Jun +45.4. §21d does not reconcile to §21c (mean R, hit rates). §14 VIX claim wrong (slice: 3 Jun 16.85→17.00 = +0.9%; 4 Jun 17.00→16.36 = −3.8%). | cross-section | 1 |
| 4.1 Pillars conclude | §8 "Bearish continuation", §9 Bearish, §10 MIXED, §12 per-bullet tags only (no section-level label), §14 no direction label. | §8–§14 | 3 |
| 4.2 Cross-asset interpreted | §10 gives mechanisms (dollar-earner translation, energy weight, cross-Atlantic beta). Good. Inputs partly wrong: S&P 500 fell −1.1% on 3 Jun (7,621.3→7,538.7) and is summarised "Flat → up". | §10 | 4 |
| 4.3 Synthesis reconciles | §15/§16/§18 address short vs medium term and KER vs overlap. But "Range-Bottom Bias (close in lower third of 25-session range)" is contradicted by the level file: close 10,343.3 sits at 48% of the 25d range 10,141.2–10,560.0. A full-size market SHORT under TRANSITION with "reduced-conviction" protocol in §9 is not reconciled. | §9, §15–§18, §21a | 3 |
| 4.4 Calibrated language | §3 confidence Medium; §17 is one sentence but carries two stacked scenario branches ("only on a confirmed close beneath it … and a mechanical bounce … if that shelf holds"). | §3, §17 | 3 |
| 4.5 Card construction (protocol) | Trade 1: stop ignores nearest resistance (tighter-of rule), TP3 cap sits inside TP2, "TP1 below monthly S5" false. Trade 2: uses a custom confluence stop-entry with 1R/2R TPs instead of the §5.2c breakout geometry; "SL above weekly S1 (10,388)" false (10,375 < 10,388); "0.25×ATR ≈17 pts beyond" does not match 10,296→10,290 (6 pts). 3C: TP1/TP2 mislabelled, stop not at high − 0.40×width, 25d floor/ceiling wrong. No card prints D-1 reference close with date and signed gap (M5 §5.0). All levels built on a wrong close, ATR and pivots. | §21b | 2 |
| 5.1 Data dated; staleness | Most points dated. Vague dates remain ("late May", "~11–18 Jun", "Early Jun", "Mid-Jun"). §19 says some intraday OHLC was "reconstructed" but does not say which fields. | §4, §13, §19 | 3 |
| 5.2 Assumptions up front | Anchor caveat in §20 only, confused wording; absent from Trade 2 and 3C cards. Partial-corroboration caveat on cards is generic. | §20, §21b | 3 |
| 5.3 Red flags surfaced | Mid-June CPI/BoE and oil headlines carried; BUT the D-day event collision is missing: US Nonfarm Payrolls 15:30 broker = 13:30 UK on D (consensus 77.0 vs prior 115.0), plus Unemployment Rate and Average Hourly Earnings, all HIGH, and BoE Governor Bailey speech 21:00 broker = 19:00 UK. None appears in §13d or on any card caveat. | §13d, §21b | 2 |
| 5.4 Restrictions honoured | BREACH: §19 states intraday OHLC "was reconstructed within the documented trajectory" while §6 labels every row CORROBORATED with two named sources and §19 says "no field fell to single-source indicative" (synthesised price presented as sourced). A 39-pt gap is labelled CORROBORATED. "median-reconciled" is wrong (a median of 10,303 and 10,342 is not 10,342). Module code "M5 trace" appears in §20. Trading Economics "Cash/CFD" row used in the cash basis. | §6, §19, §20 | 1 |

## 2. Category roll-up

| # | Category | Rows | Mean | Level | Multiplier | Points | Justification |
|---|---|---|---|---|---|---|---|
| 1 | Prompt adherence (20) | 3,4,4 | 3.67→4, restriction-breach −1 | 3 | 0.65 | 13.0 | Variables mostly respected; breach override drops one level. |
| 2 | Structure (20) | 4,3,4 | 3.67→4 | 4 | 0.85 | 17.0 | Complete and ordered; daily pivot table missing, 5 levels per side. |
| 3 | Accuracy & evidence (25) | 2,0,2,1 | 1.25→1, override → 0 | 0 | 0.00 | 0.0 | Source-figure contradictions; 15 of 20 OHLC fields outside tolerance. |
| 4 | Reasoning & judgment (20) | 3,4,3,3,2 | 3.0→3 | 3 | 0.65 | 13.0 | Good mechanisms; regime/range position contradicted by levels; cards defective. |
| 5 | Currency & transparency (15) | 3,3,2,1 | 2.25→2 | 2 | 0.40 | 6.0 | Reconstructed prices shown as sourced; NFP on D missing. |

## 3. Category 3 discrepancy log (report §6 and §11 vs level file / slice, cash basis)

Tolerance (brief §4): |Δ| ≤ 5 on close, ≤ 10 on O/H/L. Δ = report − slice cash.

| Session | Open (rep / slice / Δ) | High | Low | Close | Verdict |
|---|---|---|---|---|---|
| Fri 29 May | 10,443 / 10,434.7 / +8.3 | 10,468 / 10,462.0 / +6.0 | 10,410 / 10,409.2 / +0.8 | 10,429 / 10,410.0 / **+19.0** | close FAIL (>15) |
| Mon 1 Jun | 10,429 / 10,371.9 / **+57.1** | 10,456 / 10,410.4 / +45.6 | 10,388 / 10,286.2 / **+101.8** | 10,396 / 10,324.5 / **+71.5** | all 4 FAIL; open equals 29 May close |
| Tue 2 Jun | 10,397 / 10,360.7 / +36.3 | 10,435 / 10,398.1 / +36.9 | 10,372 / 10,332.5 / +39.5 | 10,421 / 10,375.6 / **+45.4** | all 4 FAIL |
| Wed 3 Jun | 10,422 / 10,351.4 / **+70.6** | 10,439 / 10,384.0 / +55.0 | 10,323 / 10,320.7 / +2.3 | 10,342 / 10,341.7 / +0.3 | O, H FAIL; L, C ok |
| Thu 4 Jun (D-1) | 10,374 / 10,301.0 / **+73.0** | 10,383 / 10,360.2 / +22.8 | 10,300 / 10,236.5 / **+63.5** | 10,315 / 10,343.3 / **−28.3** | all 4 FAIL |

15 of 20 fields out of tolerance; 4 of 5 closes out by >15 pts. Full-day basis does not rescue it (4 Jun full close 10,391.8).

RSI2 (report vs slice cash): 29 May 69.2 vs 0.0 · 1 Jun 0.0 vs 0.0 · 2 Jun 43.7 vs 37.4 · 3 Jun 24.1 vs 60.1 · 4 Jun 0.0 vs 4.5. Arithmetic from the report's own closes reproduces (Δ ≤ 0.6).
Trend labels using the slice: 29 May Bearish (report Neutral); 3 Jun Neutral (report Bearish); 4 Jun close 10,343.3 > open 10,301.0 and RSI2 4.5 → Neutral (report Bearish). The 4 Jun slice session closed +1.6 vs 3 Jun and at 86% of its range, against the report's "continuation lower … close near the low".
ATR(14): report ≈66.7; slice cash 113.73 / full 137.39.

Pivots:

| Level | Daily (cash, from 4 Jun) | Report | Weekly cash (W22) | Report | Δ | Monthly cash (May) | Report | Δ |
|---|---|---|---|---|---|---|---|---|
| R3 | 10,513.9 | **absent** | 10,701.6 | 10,552 | −149.6 | 11,018.4 | 10,681 | −337.4 |
| R2 | 10,437.0 | absent | 10,630.8 | 10,512 | −118.8 | 10,789.2 | 10,615 | −174.2 |
| R1 | 10,390.2 | absent | 10,520.4 | 10,470 | −50.4 | 10,599.6 | 10,522 | −77.6 |
| P | 10,313.3 | absent | 10,449.6 | 10,429 | −20.6 | 10,370.4 | 10,455 | +84.6 |
| S1 | 10,266.5 | absent | 10,339.2 | 10,388 | +48.8 | 10,180.8 | 10,362 | +181.2 |
| S2 | 10,189.6 | absent | 10,268.4 | 10,347 | +78.6 | 9,951.6 | 10,296 | +344.4 |
| S3 | 10,142.8 | absent | 10,158.0 | 10,306 | +148.0 | 9,762.0 | 10,296→10,203 | +441.0 |

(Monthly S3 report value 10,203.) The report's weekly set implies a week range of 82 pts (R1−S1) against the real 181.2 (10,560.0 high 26 May, 10,378.8 low 28 May); the monthly set implies 160 pts against the real 418.8 (10,560.0 / 10,141.2). The weekly set matches a single-bar H 10,470 / L 10,388 / C 10,429. The "10,296–10,306 confluence (weekly S3 / monthly S2)" that anchors §11, §15, §16, §17 and Trades 2/3C does not exist in the level file.
25-day range: real high 10,560.0 (26 May), low 10,141.2 (18 May); report uses 10,548 / 10,300 (the 4 Jun low). 5-day swing: 10,462.0 / 10,236.5 (report 10,468 / 10,300).

## 4. Total, band, override
Total = 13.0 + 17.0 + 0.0 + 13.0 + 6.0 = **49**. Band: **Low Trust (40–59)**. Override check: hallucinated-source override applied (cap Low, C3 = 0); restriction-breach also present (C1 −1). Score 49 is inside the cap.

## 5. Card Integrity (linter rows copied verbatim from `lint_static/2026-06-05.csv`)

| card_id | strategy | flags | dud | card score |
|---|---|---|---|---|
| 2026-06-05_Trade_1 | Trade 1 - Daily Directional (SHORT) | WARN_TP3_ORDER | False | 90 |
| 2026-06-05_Trade_2 | Trade 2 - Pivot, regime-aware (TRANSITION → breakout side only) | CLEAN | False | 100 |
| 2026-06-05_Trade_3C | Trade 3C - Momentum-Breakout (TRANSITION) | CLEAN | False | 100 |

n_cards = 3 · n_duds = 0 · n_warns = 1 · **Card Integrity = 96.7** (mean of 90, 100, 100). Separate from the 100. The static linter cannot see the data-level and rule-text defects listed in the feedback file; those are scored under 4.5.
