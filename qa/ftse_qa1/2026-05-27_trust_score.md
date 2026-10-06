# Trust Score v3.7 — FTSE 100 daily report, 27 May 2026 (run ftse_qa1)

Report: `reports/md/FTSE_EuroStoxx_Report_27May2026.md` · D = 2026-05-27 · D-1 = 2026-05-26 (Tue; Mon 25 May was a UK bank holiday)
Level file check: `last_bar_date = 2026-05-26 < D` (leak-free, confirmed). Slice last bar 2026-05-26 22:45 broker.

## Result (machine-readable lines)

c1=3
c2=4
c3=1
c4=3
c5=3
total=58
band=Low
override=restriction_breach
card_integrity=100.0
n_cards=3
n_duds=0
n_warns=0

## 1. Section 7 checklist

| Row | Reviewer notes | Evidence (location) | Score |
|---|---|---|---|
| 1.1 Variables respected | Asset (FTSE 100 cash), counters (USDX, S&P 500, DAX 40, Euro Stoxx 50 reference), as-of 26 May London close, 5-session lookback, GBP / index points all respected. Deviations: (a) daily-open anchor overridden 07:00 -> 00:00 UK (disclosed, "per engagement instruction"); (b) the six §4 sources are consumer aggregators / media (Yahoo, CNBC, Trading Economics, AJ Bell/Alliance, Investing.com) - no index-provider/exchange (FTSE Russell, LSE) or sell-side tier source, and the Investing.com row quotes no value, so the usable source count is 5 and the tier requirement is unmet. | §2, §4, §20, §21b | 3 |
| 1.2 Coverage & currency consistent | All data dates are 26 May or earlier; session date 27 May; GBP / EUR kept separate. Minor: Morningstar item dated only "Feb (context)" and a Euro Stoxx article are counted in the FTSE aggregate; Euro Stoxx block uses six sessions (explained). | §2, §6, §13a | 4 |
| 1.3 Audience & tone | Strategist register, trading-and-risk-review framing, no retail tone. | §1, §18 | 4 |
| 2.1 Sections present & ordered | §1-§21 all present and in order incl. §13a-d and §21a-d. Backtest §21c covers t-4..t-1 (four sessions, not five) and omits some strategy rows rather than showing SUPPRESSED rows. | headings, §21c | 4 |
| 2.2 Scorecard as a table | §6 is a table but Source A / Source B columns are collapsed into one "Validation" column. §11 daily and weekly tables run R5->S5 (five levels each side, brief asks three); monthly is R3->S3; order R->S is correct. | §6, §11 | 3 |
| 2.3 Method steps visible | Observation -> consensus (§4-§5), candle-by-candle + sequence (§8), regime / persistence / overlap / VOLator (§9) all present. Chart images absent (pandoc drop; captions accepted). No numeric ATR(14), KER(13,EMA3) or VOLator value anywhere. | §4-§9 | 4 |
| 3.1 Quantitative claims sourced | Brent ">104 -> high-90s -> ~98", GBP/USD 1.348, gold 4,520-4,535, "retail sales -1.3% vs -0.6% expected", "highest close since the February record sequence" carry no source and several are not traceable to §4/§6/§13a. The calendar slice gives 22 May UK Retail Sales m/m -1.3 with consensus 0.0 (not -0.6). | §1, §12, §14 | 2 |
| 3.2 Citations exist & contain data | Spot-check of three: (1) Yahoo/CNBC 22 May close 10,466.26 (+22.79) - consistent with §6 and within 4.1 pts of the CFD cash close 10,470.4: PASS. (2) AJ Bell midday 10,534.43 (+68.17) - arithmetic consistent with 10,466.26: PASS. (3) Alliance News late roundup 26 May - raw quote "ended higher, limited gains" contains no figure, yet is normalised to "~10,524" and then to 10,523.85 to two decimals; CFD cash close is 10,500.7 (+23.1): FAIL - the cited source cannot be the origin of the number. Also `cnbc.com/quotes/.FTSE` is a quote page, not an article that could carry the dated 26 May headline in §13a. Treated as unsupported/synthesised, not as an invented URL (no override C3=0 invoked). | §4, §13a | 1 |
| 3.3 Calculations transparent | RSI2 reproducible from the report's own closes (100.0 on last three; matches level file rsi2_cash 100.0). §11 pivots reproduce exactly from the report's own H/L/C (daily P 10,514.22, R1 10,558.23, S1 10,479.83 etc.). Failures: ATR(14) never stated; KER(13) not stated (self-admitted compressed sample); §21a composite +0.63 has no signal x weight table and the six-signal 0.25/0.20/0.10/0.15/0.15/0.15 weighting is not shown; §13b tilt arithmetic is wrong (bullish weights 0.5+0.7+0.7+0.5 = 2.4 over total weight 4.6 = +0.52, report says 1.9/4.4 = +0.43). | §6, §9, §11, §13b, §21a | 2 |
| 3.4 Numbers reconcile | Internal: D-1 close 10,523.85 identical in §1/§3/§4/§6/§21b; §11 pivots = card pivots; RSI2 consistent. Breaks: §3 "session range 10,500-10,549" vs §6 low 10,470.20; §3 "+1.09% vs 19 May open" is +1.09% vs the 19 May CLOSE (vs open 10,388.05 it is +1.31%); §1 "highest close since February" vs §13a "highest since April 22"; §1 "daily-directional and momentum-pullback strongest" vs §21d "weakest is Trade 1"; §21c 26 May Trade 3A entry 10,455 is below the report's own 26 May low 10,470.20 yet shown as filled. External (vs level file): D-1 close wrong by 23.1 pts (cash) / 16.9 (full) - over the 15-pt failure line; opens/lows of 19, 20, 21 May off by 40-157 pts; weekly and monthly pivots off by 50-400 pts (see §3 below). | whole report | 1 |
| 4.1 Pillars conclude | §8 "Bullish continuation", §9 "Bias Bullish", §10 "CONFIRM-leaning-MIXED / Mixed". §12 sub-sections carry "price-supportive/two-way" tags but no closing direction label; §14 ends on a cross-reference, not a label. | §8-§14 | 3 |
| 4.2 Cross-asset interpreted | Mechanism given per counter (overseas revenue translation, risk appetite, DAX industrial vs FTSE energy/financials, calendar artefact for the 26 May divergence). Weakness: USDX "Rising / Flat" and "firm-to-rising" is loosely supported (slice: 99.34 on 22 May -> 99.14 on 26 May); S&P 500 -0.4% on 26 May and the CB Consumer Confidence miss (93.1 vs 99.7 cons.) not used. | §10 | 4 |
| 4.3 Synthesis reconciles tensions | RSI2 100 vs Range-Top, divergence vs Continental, BoE risk are addressed. Not reconciled: confidence "Medium"/"high-conviction trend continuation" despite 4 of 5 sessions single-source; exec summary vs §21d contradiction; §21a +0.63 unexplained. | §15-§18 | 3 |
| 4.4 Calibrated language | §17 is exactly one sentence, no hedge stacking; confidence stated in §3 (Medium). | §3, §17 | 4 |
| 4.5 Card construction (protocol Cat. 4) | See §4 below: Trade 2 produced although the rule requires suppression (all pivot tiers single-source); Trade 2 entry arithmetic wrong by 10.00 pts; Trade 2 stop and TP ladder do not follow the TREND rule; Trade 1 stop text contradicts its own number and the wide-stop flag is misapplied; Trade 1 TP3 has no price; Trade 3A swing and TP3 do not satisfy the rule against the level file; ATR never quoted. | §21b | 2 |
| 5.1 Data dated; staleness flagged | Prices and articles dated; single-source O/H/L flagged row by row. Morningstar "Feb" undated. | §4, §6, §13, §19 | 4 |
| 5.2 Assumptions up front | Anchor override stated in §20 and on Trade 1, but Trade 2 and Trade 3A cards state no anchor time; single-source flag propagated to all cards. | §20, §21b | 4 |
| 5.3 Red flags surfaced | Risks in §12/§15; 28 May BoE collision carried onto all three cards. Omits 27 May calendar items present in the slice (ECB Financial Stability Review 09:00 UK, EUR Consumer Confidence, Fed Governor Cook speech) and the 26 May US consumer-confidence miss. | §12, §13c-d, §21b | 4 |
| 5.4 Restrictions honoured | BREACH. (a) A synthesised close is presented as sourced: 10,523.85 is "reconciled from the midday level and a verbal statement" (§4 note, §19), then shown to the cent as Close in §6/§3/§21b; §20 asserts "No price ... was synthesised, interpolated or invented" - self-contradictory. (b) Chart 3 uses a "reconstructed medium-term path" and Chart 4 "reconstructed counter histories". (c) Euro Stoxx opens equal the prior close on every row and FTSE 20/21/22 May opens equal the prior close (copied, not sourced). (d) Trade 2 produced against the fixed M5 suppression rule. | §4, §6, §7, §19, §20 | 1 |

## 2. Category roll-up

| Cat | Level | Multiplier | Points (max) | Justification |
|---|---|---|---|---|
| C1 Prompt adherence | 3 | 0.65 | 13.00 (20) | Row mean 3.67 -> 4, reduced one level by the restriction-breach override. Source tiers unmet, 00:00 anchor deviation. |
| C2 Structure | 4 | 0.85 | 17.00 (20) | All 21 sections present and ordered; §6 collapsed columns, pivot tables 5-deep, four-session backtest. |
| C3 Accuracy & evidence | 1 | 0.20 | 5.00 (25) | Row mean 1.5; set to 1 under the brief's failure rule: D-1 close off by 23.1 pts (>15), 4 of 5 sessions' open/low off by tens to >150 pts, weekly/monthly pivots badly wrong, ATR/KER absent, tilt arithmetic wrong. |
| C4 Reasoning & judgment | 3 | 0.65 | 13.00 (20) | Row mean 3.2. Sound cross-asset mechanism and one-sentence forecast; card construction defects and unreconciled synthesis. |
| C5 Currency, restrictions & transparency | 3 | 0.65 | 9.75 (15) | Row mean 3.25. Dating and flagging strong; restriction row scored 1. |

## 3. Category 3 data reconciliation (report vs `data/levels/UK100_by_date/2026-05-27.csv`)

Report claims a CASH-index basis. Cash = 08:00-16:30 London window; full = full broker day. Tolerances: |d| <= 5 close, <= 10 open/high/low.

### 3a. OHLC (report minus level file, points)

| Session | Field | Report | Cash level | d cash | Full level | d full | Verdict |
|---|---|---|---|---|---|---|---|
| 26 May (D-1) | Open | 10,473.10 | 10,531.9 | -58.8 | 10,537.8 | -64.7 | FAIL |
| | High | 10,548.60 | 10,560.0 | -11.4 | 10,560.0 | -11.4 | FAIL (marginal) |
| | Low | 10,470.20 | 10,498.0 | -27.8 | 10,481.4 | -11.2 | FAIL |
| | Close | 10,523.85 | 10,500.7 | +23.1 | 10,507.0 | +16.9 | FAIL (>15) |
| 22 May | Open | 10,443.47 | 10,492.6 | -49.1 | 10,514.6 | -71.1 | FAIL |
| | High | 10,497.22 | 10,494.5 | +2.7 | 10,519.7 | -22.5 | pass (cash) |
| | Low | 10,435.53 | 10,446.0 | -10.5 | 10,435.6 | -0.1 | marginal (cash) |
| | Close | 10,466.26 | 10,470.4 | -4.1 | 10,436.6 | +29.7 | pass (cash) |
| 21 May | Open | 10,443.47 | 10,371.1 | +72.4 | 10,403.9 | +39.6 | FAIL |
| | High | 10,485.30 | 10,469.1 | +16.2 | 10,518.3 | -33.0 | FAIL |
| | Low | 10,412.60 | 10,344.7 | +67.9 | 10,344.7 | +67.9 | FAIL |
| | Close | 10,443.47 | 10,462.3 | -18.8 | 10,490.5 | -47.0 | FAIL |
| 20 May | Open | 10,410.30 | 10,274.4 | +135.9 | 10,298.8 | +111.5 | FAIL |
| | High | 10,470.90 | 10,458.8 | +12.1 | 10,458.8 | +12.1 | FAIL (marginal) |
| | Low | 10,388.10 | 10,272.8 | +115.3 | 10,231.5 | +156.6 | FAIL |
| | Close | 10,443.47 | 10,422.9 | +20.6 | 10,443.3 | +0.2 | FAIL (cash) |
| 19 May | Open | 10,388.05 | 10,339.9 | +48.1 | 10,359.3 | +28.8 | FAIL |
| | High | 10,455.20 | 10,408.9 | +46.3 | 10,408.9 | +46.3 | FAIL |
| | Low | 10,360.40 | 10,313.0 | +47.4 | 10,285.7 | +74.7 | FAIL |
| | Close | 10,410.30 | 10,325.1 | +85.2 | 10,287.6 | +122.7 | FAIL |

Pattern: opens for 20/21/22 May equal the prior stated close exactly (and likewise every Euro Stoxx row), indicating copied rather than sourced values. 20 May and 21 May closes are both 10,443.47.

### 3b. Indicators

| Item | Report | Level file | Verdict |
|---|---|---|---|
| RSI2 (D-1) | 100.0 | cash 100.0 / full 56.64 | consistent with cash; reproduces from report's own closes (100.0, 100.0, 100.0) |
| ATR(14) | not stated anywhere | cash 135.44 / full 158.01 | MISSING |
| KER(13, EMA3) | "Trending Up - Strong", no value, shorter span than 13 | n/a | MISSING value |

### 3c. Pivots (report minus level file; note daily pivots are arithmetically correct on the report's own wrong H/L/C)

| Daily | Report | Cash | d | Full | d |
|---|---|---|---|---|---|
| R3 | 10,636.63 | 10,603.13 | +33.5 | 10,629.47 | +7.2 |
| R2 | 10,592.62 | 10,581.57 | +11.1 | 10,594.73 | -2.1 |
| R1 | 10,558.23 | 10,541.13 | +17.1 | 10,550.87 | +7.4 |
| P | 10,514.22 | 10,519.57 | -5.3 | 10,516.13 | -1.9 |
| S1 | 10,479.83 | 10,479.13 | +0.7 | 10,472.27 | +7.6 |
| S2 | 10,435.82 | 10,457.57 | -21.7 | 10,437.53 | -1.7 |
| S3 | 10,401.43 | 10,417.13 | -15.7 | 10,393.67 | +7.8 |

| Weekly (W21, 18-22 May) | Report | Cash | d | Full | d |
|---|---|---|---|---|---|
| R3 | 10,739.41 | 10,949.5 | -210.1 | 11,014.57 | -275.2 |
| R2 | 10,618.31 | 10,722.0 | -103.7 | 10,767.13 | -148.8 |
| R1 | 10,542.29 | 10,596.2 | -53.9 | 10,601.87 | -59.6 |
| P | 10,421.19 | 10,368.7 | +52.5 | 10,354.43 | +66.8 |
| S1 | 10,345.17 | 10,242.9 | +102.3 | 10,189.17 | +156.0 |
| S2 | 10,224.07 | 10,015.4 | +208.7 | 9,941.73 | +282.3 |
| S3 | 10,148.05 | 9,889.6 | +258.4 | 9,776.47 | +371.6 |

The report's implied weekly range (R1-S1) is 197.1 pts versus 353.3 (cash) / 412.7 (full) in the level file.

| Monthly (Apr 2026) | Report | Cash | d | Full | d |
|---|---|---|---|---|---|
| R3 | 11,213.33 | 11,159.9 | +53.4 | 11,228.43 | -15.1 |
| R2 | 10,916.67 | 10,928.7 | -12.0 | 10,977.97 | -61.3 |
| R1 | 10,553.33 | 10,650.0 | -96.7 | 10,671.63 | -118.3 |
| P | 10,256.67 | 10,418.8 | -162.1 | 10,421.17 | -164.5 |
| S1 | 9,893.33 | 10,140.1 | -246.8 | 10,114.83 | -221.5 |
| S2 | 9,596.67 | 9,908.9 | -312.2 | 9,864.37 | -267.7 |
| S3 | 9,233.33 | 9,630.2 | -396.9 | 9,558.03 | -324.7 |

Consequence: the report's headline "triple confluence at 10,542-10,558 (daily R1 / weekly R1 / monthly R1)" does not exist in the level file (daily R1 10,541-10,551; weekly R1 10,596-10,602; monthly R1 10,650-10,672). The "weekly pivot 10,421" used as thesis invalidation is 10,368.7 (cash) / 10,354.4 (full).

Other claims against the data: §1 "highest close since the February record sequence" conflicts with the 25-day cash high of 10,638.9 on 2026-04-21 and with the report's own §13a "highest since April 22".

## 4. Card construction notes (Category 4; levels from the level file)

ATR14 cash 135.44 / full 158.01; 0.3xATR = 40.6 / 47.4; 3.0xATR = 406.3 / 474.0; 2xATR = 270.9 / 316.0.
Details and numeric conditions are in `2026-05-27_feedback.md`.

## 5. Card Integrity (linter rows copied verbatim from `qa/ftse_qa1/lint_static/2026-05-27.csv`)

| card_id | report_date | strategy | flags | dud | card score |
|---|---|---|---|---|---|
| 2026-05-27_Trade_1 | 2026-05-27 | Trade 1 - Daily Directional | CLEAN | False | 100 |
| 2026-05-27_Trade_2 | 2026-05-27 | Trade 2 - Pivot (regime-aware, TREND_UP -> LONG) | CLEAN | False | 100 |
| 2026-05-27_Trade_3A | 2026-05-27 | Trade 3A - Momentum-Pullback | CLEAN | False | 100 |

Card Integrity (report level, mean over 3 non-suppressed cards) = 100.0 · n_cards=3 · n_duds=0 · n_warns=0.
The static linter does not test rule-level construction (suppression, formula, ATR floors); those defects are scored in Category 4 row 4.5, not here.

## 6. Total, band, override

- Total = 13.00 + 17.00 + 5.00 + 13.00 + 9.75 = 57.75 -> **58**.
- Band: **Low (40-59)**.
- Override check: hallucinated source - not invoked (no impossible URL proven; the 26 May close is an unsupported, disclosed estimate, treated under restriction breach). Restriction breach - **invoked** (synthesised/reconstructed prices presented as sourced contrary to the no-synthesis restriction; §20 denies it; Trade 2 produced against the fixed suppression rule). Cap at Moderate (60-74) is not binding at 58; C1 lowered one level (4 -> 3).
- `override=restriction_breach`
