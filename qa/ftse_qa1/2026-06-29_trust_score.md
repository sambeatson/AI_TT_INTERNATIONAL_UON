# Trust Score v3.7 QA - FTSE 100 report dated 2026-06-29 (run ftse_qa1)

Report: `FTSE100_EuroStoxx_Report_29Jun2026.md` | D = 2026-06-29 | D-1 = Fri 2026-06-26
Data check: level file `last_bar_date` = 2026-06-26 < D, so it is leak-free. Basis compared: **cash** (the report states "cash close GBP", and §4 excludes CFD quotes). Full-day (`_full`) deltas are given where they change the picture. Tolerances: brief §4 (close <=5, O/H/L <=10; close >15 = Category 3 failure).

## Machine-readable lines
c1=3
c2=4
c3=2
c4=3
c5=3
total=63
band=Moderate
override=none
card_integrity=100
n_cards=3
n_duds=0
n_warns=0

## 1. Section 7 checklist

| Row | Reviewer notes | Evidence | Score |
|---|---|---|---|
| 1.1 Variables respected | Asset is the FTSE 100 cash index with STOXX 50 as comparator only (no cards): OK. Counters USDX / S&P 500 / DAX 40: OK. As-of London, 5/25-session lookback, GBP points: OK. "Six observations" in §4 are only five distinct providers (Yahoo is listed twice) and none is sell-side tier. Daily-open anchor overridden to 00:00 UK instead of 07:00 UK (disclosed, but a deviation). | §2, §4, §20, §21b | 3 |
| 1.2 Coverage & currency consistent | Closes and sessions are D-1 or earlier. But the "daily pivots" are built from Thu 25 Jun H/L/C (D-2), not D-1 Fri 26 Jun. Weekly / monthly pivots do not correspond to W26 / May level-file periods. §2 says STOXX has a "GBP-equivalent noted" and none appears. §1/§12 name "UK CPI" as a live catalyst but §13d has no UK CPI. | §11 header, §2, §1, §12, §13d | 3 |
| 1.3 Audience & tone | Strategist register, no retail tone. Minor leakage of internal process language ("operator instruction", "weight-lock", "instance default"). | §19, §20 | 4 |
| 2.1 Sections present & ordered | §1-§21 all present and in order, §13a-d and §21a-d present, five chart captions in §7 (images dropped by pandoc, accepted). | headings | 5 |
| 2.2 Scorecard as a table | §6 is a table but has no Source A / Source B columns (brief requires them). §11 pivot tables are ordered R->S but carry 5 levels each side for daily (R4/R5/S4/S5 beyond the 3-level spec). | §6, §11 | 4 |
| 2.3 Method steps visible | §4-§5 observation -> consensus visible. §8 candle-by-candle present but the Fri 26 Jun candle description contradicts the report's own table (see C3). §9 gives overlap / persistence / VOLator / KER values without derivation. RSI2 arithmetic not shown. | §4-§9 | 4 |
| 3.1 Quantitative claims sourced | Many §12 figures (AZN +1.4%, ULVR +0.7%, BATS +1.5%, HSBC >1.5%, Shell -2%, BP -0.8%, VW -3.9%, "~80% overseas revenue", VIX "high-teens to ~20") have no source or pointer to §4/§6/§13. "Strongest weekly close in about two months" in §1 is sourced elsewhere as "highest close in two months" (Thursday). ATR(14) ~58 appears only inside card text, unsourced. | §1, §12, §14, §21b | 3 |
| 3.2 Citations exist & contain data | Three checked: (a) Yahoo 10,508.02 - consistent; (b) Investing.com row quotes only a range (10,404.73-10,530.18) but is normalized to a close of 10,508 and used as the corroborating pair - no close figure in the quote; (c) Fidelity "10,486.81 intraday" is stamped 16:35 UK, the same time as the 10,508.02 close, a 21-pt contradiction. §3/§5/§19 claim two providers agree within +/-0.10 pt while §4/§6/§20 show the TE pair at Delta ~4 pts. LSE/FTSE Russell row has no figure ("close series"). Cannot fetch, so not asserted as fabricated; override not triggered, but the corroboration claim is unsupported. | §3, §4, §5, §6, §19, §20 | 2 |
| 3.3 Calculations transparent | Pivot arithmetic reproduces from the report's own (wrong-day) inputs. RSI2 reproduces for Wed (100), Thu (100), Fri (73.7) from the report's closes, but Tue 23 Jun RSI2 = 39.0 is impossible on two consecutive up closes (10,399.8 -> 10,455.6 after a 19 Jun cash close of 10,352.3 gives 100.0), and Mon shows "-" although prior closes exist. ATR(14) is not stated in §9 and the ~58 on the card is half the data value (cash 120.12 / full 141.24). §21a contributions sum to 0.62, not the stated +0.61; sentiment contribution 0.03 does not follow from tilt +0.10 x 0.15 = 0.015. KER 0.26 stated, not derived. | §6, §9, §11, §21a, §21b, §20 | 2 |
| 3.4 Numbers reconcile | D-1 close 10,508 is consistent across §1/§3/§4/§6/§21b; §11 pivots equal card pivots; RSI2 73.7 is consistent in §6 / §8. Breaks: §8 says Fri candle closed "~83% down the range with a dominant upper structure" while §6 puts the close at 82% UP the range (10,404.73 low, 10,508.02 close, 10,530.18 high); §21d says Trade 1 TP2 hit rate ~40% but no §21c row reaches +2R (max excursions from the §6 highs: +57, +65.5, +54.4, +77.4 pts vs 2R ~98); §9 "94th percentile" range position vs 86.4% from the 25-day cash swings (10,126.2 - 10,577.7); §11 header says Thu-derived pivots while §1/§16 treat them as D-1. | §8, §9, §11, §21c, §21d | 2 |
| 4.1 Pillars conclude | §8, §9, §10, §12 end in labels. §14 has no closing direction label. §8's label rests on a misread Friday candle. | §8-§14 | 4 |
| 4.2 Cross-asset interpreted | Mechanisms are given, but two observations are wrong against the slices: USDX rose over the 5 sessions (19 Jun close 100.82 -> 26 Jun 101.41, 22-25 Jun closes 101.02 / 101.39 / 101.59 / 101.48), yet §10 says "Falling / flat", §12/§14 repeat "soft/flat dollar", and §9 calls USDX VOLator "contracting"; S&P 500 fell on 4 of 5 sessions (7,494.2 -> 7,345.6, -2.0%) but is shown as "Falling (Fri)". The sign of the USD conclusion is therefore unsupported. | §9, §10, §12, §14 | 3 |
| 4.3 Synthesis reconciles tensions | Short- vs medium-term and §17 vs §21a are addressed explicitly. Weaknesses: the short-term signal is given the full +0.25 while §8 calls the tape exhaustion-prone; cross-asset +0.05 despite a MIXED read; the sum error (0.62 vs 0.61). | §15-§18, §21a | 3 |
| 4.4 Calibrated language | §17 is exactly one sentence with one condition; confidence stated (Medium) in §3. | §3, §17 | 4 |
| 4.5 Card construction (protocol) | Linter is clean, but construction fails M5 rules on all three cards (ATR 58 vs 120.12; Trade 2 not suppressed although every pivot tier is declared single-source indicative; 3A swing run low-after-high and sub-2xATR at true ATR; backtest Fri 3A uses Fri's own low). See feedback. | §21b, §21c, §20 | 2 |
| 5.1 Data dated; staleness flagged | Articles and prices dated; Mon-Thu O/H/L asterisked. Fri 26 Jun O/H/L are presented without a single-source flag (they come from one Investing.com range) and the open (10,530.18) is 31.9 pts above the cash open 10,498.3. §13c row "Fri 26 Jun euro-area inflation expectations" is not in the calendar for 26 Jun (EUR Consumer Price Expectations is scheduled 29 Jun). | §6, §13c | 3 |
| 5.2 Assumptions up front | Anchor override and single-source pivot propagation are stated in §19/§20 and on cards. The wrong-day pivot input and the "operator instruction" waiving suppression are not surfaced as assumptions up front. | §19, §20, §21b | 4 |
| 5.3 Red flags surfaced | Risks in §12/§15 and CPI collision carried into cards. The D calendar in the slice has HIGH EUR Consumer Price Expectations 12:00 broker (10:00 UK) and HIGH Lagarde speech 22:00 broker (20:00 UK), plus BoE Pill 08:00 broker (06:00 UK); none appear in §13d. CPI y/y / HICP are MODERATE in the feed, reported as High. | §13d, §15 | 3 |
| 5.4 Restrictions honoured | §4 says "Retail CFD spreads excluded" but the Trading Economics "CFD-tracked close" is a Core row and the Delta<4 validation in §6/§20 is against that CFD feed (down-weighted, so judged not an open breach). Futures kept as context only: OK. No module codes or bracketed names found. Trade 2 retained against the M5 suppression rule on an unverifiable "operator instruction". | §4, §6, §20, §21b | 3 |

## 2. Category 3 data reconciliation (report vs `UK100_by_date/2026-06-29.csv`, cash basis)

**D-1 and 5-day OHLC (report minus cash; tolerance close 5, O/H/L 10):**

| Date | dO | dH | dL | dC | Flag |
|---|---|---|---|---|---|
| Mon 22 Jun | -24.2 | -29.4 | -4.7 | **-41.1** | C >15 (failure); O, H out |
| Tue 23 Jun | **+72.9** | +6.5 | **+59.9** | +2.6 | O, L out (full-day low 10,318.1 also +69.9) |
| Wed 24 Jun | +26.0 | +34.0 | +30.4 | +13.4 | all out; C 5-15 |
| Thu 25 Jun | +43.3 | **-29.4** (report high 10,548.3 vs 10,577.7) | +41.3 | -8.1 | all out; C 5-15 |
| Fri 26 Jun | +31.9 | +13.8 | +3.3 | -8.4 | O, H out; C 5-15 |

Fri 26 Jun: the report's bar is bearish (O 10,530.18 > C 10,508.02, open = high). The cash bar is O 10,498.3, C 10,516.4 (close = high, close > open). The -0.21% day change is consistent in both (cash -0.205%).

**RSI2:** Wed 24 / Thu 25 / Fri 26 reproduce from the report's own closes (100 / 100 / 73.7). Tue 23 stated 39.0 vs 100.0 (cash 100.0 and reproduced from report closes + 19 Jun cash close 10,352.3). Mon 22 shown "-" vs cash 65.19. Fri 26 stated 73.7 vs cash 79.33 (basis, Delta 5.6). Trend label Mon "Bullish" with no RSI2 cannot be verified.

**ATR(14):** report ~58 (card, Trade 1) vs level file cash 120.12 / full 141.24 (-62 / -83 pts, about half). Not stated in §9.

**Daily pivots** (report built from Thu 25 Jun; level file uses Fri 26 Jun): report minus cash R3 -9.4, R2 +11.2, R1 +12.4, P +33.0, S1 +34.2, S2 +54.8, S3 +56.0. (Report minus full: R3 +0.2, R2 +10.8, R1 +32.4, P +43.0, S1 +64.6, S2 +75.2, S3 +96.8.)

**Weekly pivots** (level file W26 cash: P 10,474.07): report minus cash R3 +233.6, R2 +115.6, R1 +35.5, P -82.6, S1 -162.6, S2 -280.7, S3 -360.7. The report's implied weekly low is ~10,127.5 (from R1 = 2P - L) versus the W26 cash low 10,328.1.

**Monthly pivots** (level file 2026-05 cash: P 10,370.4): report minus cash R3 +174.9, R2 +167.5, R1 +123.7, P +116.3, S1 +72.5, S2 +65.1, S3 +21.3. Implied monthly H/L/C (~10,720 / ~10,250 / ~10,490) do not match May's cash H/L/C (~10,560 / ~10,141 / ~10,410).

**Other:** 25-day range position of the D-1 cash close is 86.4% (report: 94th percentile / "top decile"). Counters: USDX and S&P observations misdescribed (see 4.2). VIX ~18.4-19.5 on 26 Jun: consistent with "high-teens".

## 3. Category roll-up

| Cat | Level | Multiplier | Points | Justification |
|---|---|---|---|---|
| 1 Prompt adherence (20) | 3 | 0.65 | 13.00 | Asset/counters/lookback fine; 5 unique sources none sell-side, 00:00 anchor deviation, wrong-day pivot input. Mean of rows 3,3,4 = 3.33. |
| 2 Structure (20) | 4 | 0.85 | 17.00 | All sections present; table gaps (no Source A/B columns), derivations thin. Mean 4.33. |
| 3 Accuracy & evidence (25) | 2 | 0.40 | 10.00 | Mon close 41 pts off, most O/H/L 25-70 pts off, Tue RSI2 wrong, ATR half, every pivot set mismatched, ±0.10 corroboration claim unsupported. Mean of rows 3,2,2,2 = 2.25. |
| 4 Reasoning (20) | 3 | 0.65 | 13.00 | Prose reasoning coherent but USDX/S&P read wrong, Friday candle misread, card construction defective. Mean of 4,3,3,4,2 = 3.2. |
| 5 Currency & transparency (15) | 3 | 0.65 | 9.75 | Disclosures good; Fri O/H/L unflagged, D-calendar HIGH events missing, CFD feed used for corroboration. Mean of 3,4,3,3 = 3.25. |

## 4. Total, band, override

Total = 13.00 + 17.00 + 10.00 + 13.00 + 9.75 = 62.75, rounded **63**. Band: **Moderate Trust (60-74)**.
Override: **none**. No source is demonstrably fabricated (the reviewer cannot fetch; the Investing.com / Fidelity / LSE rows are weak but not impossible). No prompt restriction is openly breached (the TE CFD feed is declared down-weighted; futures are context only; no module codes or bracketed names).

## 5. Card Integrity (linter rows copied verbatim from `lint_static/2026-06-29.csv`)

| card_id | report_date | strategy | flags | dud | card score |
|---|---|---|---|---|---|
| 2026-06-29_Trade_1 | 2026-06-29 | Trade 1 - Daily Directional | CLEAN | False | 100 |
| 2026-06-29_Trade_2 | 2026-06-29 | Trade 2 - Pivot, TREND_UP (pivot breakout, long) | CLEAN | False | 100 |
| 2026-06-29_Trade_3A | 2026-06-29 | Trade 3 - Momentum-Pullback (3A), regime TREND_UP | CLEAN | False | 100 |

n_cards=3, n_duds=0, n_warns=0, report-level Card Integrity = 100 (separate from the 100-point total). Note: the static linter takes R/ATR from the report's own ATR (~58). On the level-file ATR (120.12 cash) Trade 2's R of 36 is 0.2997 ATR, below the 0.3 WARN floor. This is recorded in the feedback only; the linter row is not altered.
