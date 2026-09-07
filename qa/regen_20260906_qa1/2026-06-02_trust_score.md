# Trust Score — 2026-06-02 — SP500_Report_02Jun2026.md

Run: regen_20260906_qa1 · D = 2026-06-02 · D-1 slice = data/slices/US500/US500_upto_2026-06-01.csv · Helper run with `--closes 7519.12 7520.36 7563.63 7580.06 7599.96`.
Slice reference values (cash session 16:30–23:00 broker): D-1 (01 Jun) O 7575.2 / H 7623.6 / L 7568.5 / C 7606.0 (full-day close 7600.2); ATR14 cash 67.30 (full-day 74.58); D-1 cash pivots P 7599.37 · R1 7630.23 · S1 7575.13 · R2 7654.47 · S2 7544.27 · R3 7685.33 · S3 7520.03; weekly (25–29 May) P 7563.63; 5-day swing 7504.3 (27 May) → 7623.6 (01 Jun).
Report statements noted: D-1 O 7582.29 / H 7603.44 / L 7562.61 / C 7599.96; RSI2 column ≈50, 100, 100, 100, 100; ATR(14) never stated numerically (implied ≈45.97 from 3×ATR = 137.91 and 0.25×ATR = 11.49 on the cards); daily pivots P 7580.81 · R1 7598.63 · S1 7562.25 · R2 7617.19 · S2 7544.43 · R3 7635.01 · S3 7525.87 (built from 29 May, not D-1); weekly P 7551.20; direction score +0.65 LONG; regime TREND_UP; three cards (Trade 1 market long 7599.96, Trade 2 buy-limit 7580.81, Trade 3A buy-limit 7552.50).

## 1. Section 7 checklist

| Item | Reviewer notes | Evidence observed | Score 0–5 | Action required |
|---|---|---|---|---|
| 1.1 Variables respected | Asset = S&P 500 cash index; counters USDX, VIX, DAX 40 in that order; as-of NY close of D-1; 5-session lookback; USD / index points / tick 0.01; six sources in §4 (index provider + aggregators/media, no exchange or sell-side tier). Daily-open anchor is 00:00 UK, not the fixed 07:00 UK — a moderate deviation presented as an "analyst override" that the fixed prompt stack does not provide for. | §2 table (anchor row), §2 note, §4, §10, §21b Trade 1 "Market at 00:00 UK", §20 | 3 | Restore the 07:00 UK anchor for Trade 1; add an exchange/sell-side tier source. |
| 1.2 Coverage & currency consistent | All prices dated D-1 or earlier; §13d correctly forward-dated. Units consistent. But daily pivots are built "from prior session 29 May" although the prior session is 01 Jun — a stale coverage basis for §11 and both pivot-referencing cards. | §11 heading "from prior session 29 May H/L/C"; §6 shows 01 Jun as the latest session | 3 | Rebuild daily pivots from the D-1 (01 Jun) H/L/C. |
| 1.3 Audience & tone | Senior US Equity Strategist register throughout; trading-and-risk-review framing; no retail language. | §1, §18, §21d limitations boilerplate | 5 | None. |
| 2.1 Sections present & ordered | §1–§21 all present and in order; §13a–d and §21a–d all present; §17 is a single sentence; §21d carries the limitations boilerplate. | Headings lines 8–789 | 5 | None. |
| 2.2 Scorecard as a table | §6 is a table with Date/O/H/L/C/RSI2/Trend/Src A/Src B/Final/Validation. §11 daily table has R3→S3 (3 levels each side) but the weekly table stops at R2/S2 (2 levels) and there is no monthly pivot table at all. | §6; §11 daily and weekly tables | 3 | Add R3/S3 to the weekly table and a monthly pivot table (R3→P→S3). |
| 2.3 Method steps visible | §4 observations → §5 classification/consensus; §8 candle-by-candle plus sequence assessment; §9 persistence/overlap/VOLator/Kaufman. §7 shows five image placeholders (pandoc-dropped images) — accepted as evidence, noted. Weekly/monthly pivot steps are incomplete. | §4–§9 | 4 | None material (see 2.2). |
| 3.1 Quantitative claims sourced | Price figures in §1/§3 trace to §4/§6. §12/§14 carry unsourced figures: 10-year yield "near 4.44%", WTI "~$88", DAX "25,104, +0.05%", VIX 15.32 (no §4/§13 row). Core PCE 3.3% is sourced to CNBC (§13a). | §12 Macro/Policy bullets, §10 DAX/VIX rows, §14 | 3 | Add sources (or §4/§13 rows) for the yield, WTI, DAX and VIX figures. |
| 3.2 Citations exist & contain data | Spot-check (a) TheStreet 28 May 7,563.63 (+0.58% / +43.27): internally consistent (7563.63 − 7520.36 = 43.27; +0.575%), but the 29 May report cited the same close as 7,564.51 (Δ 0.88, beyond the report's own ±0.10 tolerance). (b) Investing.com 01 Jun range 7,562.61–7,603.44 / open 7,582.29: consistent with §6, but the slice cash high is 7,623.6 (Δ −20.2), so the "corroborated" range is doubtful. (c) CNBC core PCE 3.3% "as expected": the calendar slice shows actual 3.3 vs consensus 3.1 — the "as expected" characterisation conflicts with the slice. (d) Yahoo 29 May 17:03 ET 7,580.06: consistent. No source is impossible, undated or self-contradictory → no fabrication override. | §4 rows; §13a rows; §13c 28 May row; slice/NEWS slice | 3 | Reconcile the 01 Jun high and the 28 May close with the prior report; correct the PCE "as expected" wording or cite the consensus used. |
| 3.3 Calculations transparent | RSI2 method described (period 2 on validated closes) and the last three rows reproduce exactly from the report's own closes (100/100/100); first two rows cannot be tested without earlier closes. ATR(14) is used on every card (0.25×ATR, 3×ATR) but never stated as a number anywhere (§9 has no ATR line). KER stated as "≈1.0" with no period/EMA parameters and an implausible value given the flat 27 May session. Daily pivots reproduce from the stated 29 May H/L/C (but see 1.2). Weekly pivots do NOT reproduce from the report's own prior-week H/L/C (7599.38/7470.1/7580.06 → P 7549.85, not 7551.20; 7551.20 only reproduces if H = 7603.44, the 01 Jun high, which is outside "prior week ending 29 May"). §21a contributions (0.25+0.20+0.15+0.058+0.045−0.05 = 0.653) reconcile. | §6 note, §9, §11, §20 weights bullet, helper output | 2 | State ATR(14) with its value and basis in §9; state KER(13, EMA 3) parameters and value; rebuild weekly pivots from the correct H/L/C. |
| 3.4 Numbers reconcile | D-1 close 7,599.96 identical in §1, §3, §4, §6, §11 narrative, §21b Trade 1 entry. §11 pivots = card pivots. RSI2 §6 = §8 = §21a input. Failures: ATR absent from §9 so the §21 ATR usage cannot be reconciled; pivots reconcile to the wrong session; §21d "TP1 hit ≈40%" vs §21c (one TP1 hit in five). Against the slice: every close is 4.7–8.9 pts below the cash close (all beyond the 3-pt tolerance, none beyond the 10-pt failure line) and several O/H/L rows differ by 10–42 pts (see §5 log). | cross-section; §5 log below | 3 | Fix the §9 ATR line, pivot session and §21d hit-rate; re-check the 26 May O/H/L and the 01 Jun high against a second feed. |
| 4.1 Pillars conclude (incl. §21b card construction under the M5 logic) | §8 "Bullish continuation", §9 "TREND_UP", §10 "MIXED" with contradiction flag — all defended. §12 and §14 end without an explicit direction label. Card construction (Category 4 per the protocol): Trade 1 follows the market/stop/TP ladder shape but omits the mandatory "wide stop" flag (R 48.45 > implied ATR 45.97) and uses the wrong anchor; Trade 2 ignores the TREND template entirely (entry at P instead of P + 0.10×(R1−P); stop S1 − 0.25×ATR instead of P − 0.8×(P−S1); TPs ±1R/±2R instead of R1/R1.5/R2; runner exit at R1 7598.63 sits below TP1); Trade 3A places the entry at the 38.2% retrace instead of 57.5%, the stop below the 50% level instead of beyond the swing low, TP1 at 0% instead of 38.2%, TP2 at a 27.2% extension instead of 0%, and omits the universal BE+0.2R rule. Two of three cards are not the M5 constructions. | §8, §9, §10, §12, §14, §21b; M5 §5.1/§5.2b/§5.3a | 2 | Rebuild Trade 2 and Trade 3A to the M5 templates; add the wide-stop flag to Trade 1; add direction labels to §12/§14. |
| 4.2 Peer/cross-asset interpreted | §10 gives a mechanism per counter (translation headwind, risk-on/multiple support, common risk factor) and carries the USDX contradiction to §15/§16 rather than resolving it silently. The VIX "falling → 15.32" input conflicts with the slice (VIX proxy closed 16.53 on 29 May and rose to 17.14 on 01 Jun), so the interpretation rests on a questionable D-1 reading. | §10 table and aggregate; VIX slice | 4 | Re-check the VIX D-1 level/direction. |
| 4.3 Synthesis reconciles tensions | §15 balances RSI2 saturation and the 7,600 wick against the trend; §16 states invalidation (weekly P / daily S2) and names USDX + NFP as explicit risks; §21a flags no conflict with §17 and both respect the overbought caution. KER ≈ 1.0 vs the flat 27 May session is asserted, not reconciled. | §15–§18, §21a | 4 | Reconcile the KER value with the observed sequence. |
| 4.4 Calibrated language | §17 is exactly one sentence with a range and a named interruption; confidence stated High in §3 and §18. "High" in §18 sits uneasily with single-source-indicative pivots, indicative O/H/L and RSI2 at the ceiling, but no hedge stacking. | §3, §17, §18 | 4 | Consider Medium confidence in §18 or justify High against the indicative flags. |
| 5.1 Data dated; staleness flagged | Every price row dated; single-source-indicative O/H/L marked with an asterisk and explained; §19 splits live vs indicative. §13a articles carry no dates (only §13c dates the events). | §4, §6, §13a, §19 | 3 | Date every §13a article. |
| 5.2 Assumptions up front | Anchor override stated in §2 (table + note), on the Trade 1 card and in §20; single-source pivot propagation stated on all three cards and in §19. Not stated: that the Trade 3A swing endpoint (26 May low 7,470.1) is itself a single-source-indicative value. | §2, §19, §20, §21b caveats | 4 | Flag the 3A swing anchor as indicative or use a corroborated endpoint. |
| 5.3 Red flags surfaced | §12 positioning caution, §15 bear list, §13d highest-impact event (NFP 05 Jun) all present. The NFP collision is not carried into any §21b card caveat (caveats mention only RSI2, pivots, round number, fill risk). | §12, §13d, §15, §21b caveat rows | 3 | Add the 05 Jun NFP event-risk caveat to each card. |
| 5.4 Restrictions honoured | §20 prints the bracketed variable name `[DAILY_OPEN_ANCHOR]` — an open breach of the "no bracketed variable names" restriction. §20 also cites "v2.1 baseline" (module-version reference). No CFD quotes in the OHLC basis, no ES futures, no framework name, instruments by common name. Single-source O/H/L are flagged rather than presented as sourced. | §20 line 604 ("\[DAILY_OPEN_ANCHOR\]"), line 598 ("v2.1 baseline") | 2 | Remove the bracketed token and the module-version reference from §20. Triggers the restriction-breach override. |

## 2. Category roll-up

| Category | Level | Multiplier | Points | Justification |
|---|---|---|---|---|
| C1 Prompt adherence (20) | 3 (rows 3/3/5 → 4, reduced one level by the restriction-breach override) | 0.65 | 13.00 | Anchor overridden to 00:00 UK against the fixed 07:00 UK; pivots on a stale session; bracketed variable name printed in §20. |
| C2 Structure (20) | 4 (5/3/4) | 0.85 | 17.00 | All 21 sections and sub-sections present and ordered; weekly pivots truncated to two levels and monthly pivots missing. |
| C3 Accuracy & evidence (25) | 3 (3/3/2/3) | 0.65 | 16.25 | RSI2 reproduces and the close chain is internally consistent, but ATR(14) is never stated, weekly pivots do not reproduce, daily pivots use the wrong session, closes sit 4.7–8.9 pts under the cash slice and several O/H/L values are 10–42 pts off. |
| C4 Reasoning & judgment (20) | 4 (2/4/4/4) | 0.85 | 17.00 | Cross-asset mechanism and synthesis are sound; Trade 2 and Trade 3A are not built to the M5 templates and Trade 1 lacks the wide-stop flag. |
| C5 Currency, restrictions & transparency (15) | 3 (3/4/3/2) | 0.65 | 9.75 | Override and indicative flags stated up front; articles undated; NFP not carried to cards; bracketed token breaches a stated restriction. |
| **Total** | | | **73** | 13.00 + 17.00 + 16.25 + 17.00 + 9.75 = 73.0 → 73 |

## 3. Total, band, override check

- Total: **73/100** (pre-override arithmetic with C1 = 4 would have been 77; the override reduces C1 to 3 → 73, which is already inside the Moderate cap of 74).
- Band: **Moderate** (60–74).
- Overrides: **restriction_breach** — §20 line 604 prints the bracketed variable name `[DAILY_OPEN_ANCHOR]`, openly violating the "no bracketed variable names" restriction (brief §2 row 5.4). Applied: total capped at 74 (not binding) and C1 reduced from 4 to 3. Hallucinated-source override: **not triggered** — the three spot-checked citations are named, dated and internally consistent; discrepancies are basis/precision issues, not fabrications.

## 4. Card Integrity

Lint rows (qa/regen_20260906_qa1/lint_static/2026-06-02.csv, verbatim):

| card_id | report_date | strategy | flags | dud |
|---|---|---|---|---|
| 2026-06-02_Trade_1 | 2026-06-02 | Trade 1 - Daily Directional | CLEAN | False |
| 2026-06-02_Trade_2 | 2026-06-02 | Trade 2 - Pivot (buy limit daily P) | WARN_TP3_ORDER | False |
| 2026-06-02_Trade_3A | 2026-06-02 | Trade 3A - Momentum-Pullback (38.2% fib) | CLEAN | False |

Per-card integrity (100 − 40·#DUD − 10·#WARN, floor 0):

| Card | #DUD | #WARN | Integrity | Suppressed |
|---|---|---|---|---|
| Trade 1 | 0 | 0 | 100 | No |
| Trade 2 | 0 | 1 (TP3 7598.63 below TP1 7610.86) | 90 | No |
| Trade 3A | 0 | 0 | 100 | No |

Report-level Card Integrity (mean over non-suppressed cards): **96.7**. n_cards 3 · n_duds 0 · n_warns 1.

M5-rule assessment (feeds row 4.1, not the integrity number):
- Trade 1: market entry = report D-1 close (7,599.96); anchor 00:00 UK (deviation from 07:00 UK); stop = nearest support 7,563.0 − 0.25×ATR = 7,551.51 (tighter than the 5-day swing low 7,470.1 route — correct choice); R 48.45 > implied ATR 45.97 so the mandatory "wide stop" flag is missing; TP1/TP2 = +1R/+2R correct; TP3 = 3×ATR cap correct; BE+0.2R on Unit 2 fill stated; invalidation separate (weekly P 7,551.20) although it "≈ coincides with SL"; indicative flag propagated.
- Trade 2: regime TREND_UP but the RANGE-style construction is used: entry at P (7,580.81) instead of P + 0.10×(R1−P) = 7,582.59 on the report's pivots; stop S1 − 0.25×ATR (7,550.76) instead of P − 0.8×(P−S1) = 7,565.96; TPs +1R/+2R (7,610.86/7,640.92) instead of R1/R1.5/R2 (7,598.63/7,607.91/7,617.19); runner exit at R1 7,598.63 below TP1 (linter WARN); pivots from the wrong session; invalidation separate (S2 7,544.43); indicative flag propagated.
- Trade 3A: swing 7,470.1 → 7,603.44 (133.34 pts ≥ 2×45.97 on the report's implied ATR; the low endpoint is a single-source-indicative value 35 pts off the slice); entry at 38.2% (7,552.50) instead of 57.5% (7,526.77); stop at 50% − 0.25×ATR (7,525.28) instead of swing low − 0.25×ATR (7,458.61); TP1 at 0% (7,603.44) instead of 38.2%; TP2 at a 27.2% extension (7,639.71) instead of 0% (7,603.44); no BE+0.2R rule (only the 100%-extension structural pull); invalidation separate (61.8% ≈ 7,521.0); indicative flag propagated for pivots but not for the swing anchor.

## 5. Data reconciliation log

Tolerances (brief §4): |Δ| ≤ 3 pts on a close and ≤ 8 pts on an open/high/low = consistent; larger = discrepancy; close |Δ| > 10 or non-reproducing RSI2 = Category 3 failure. Slice values are the cash session (16:30–23:00 broker) from the helper.

| # | Section / field | Report value | Slice value | Δ (report − slice) | Verdict |
|---|---|---|---|---|---|
| 1 | §6 26 May Open | 7,480.5* | 7,522.8 | −42.3 | Discrepancy (>8) — single-source-indicative row |
| 2 | §6 26 May High | 7,525.3* | 7,543.5 | −18.2 | Discrepancy (>8) |
| 3 | §6 26 May Low | 7,470.1* | 7,505.5 | −35.4 | Discrepancy (>8); this value is the Trade 3A swing anchor |
| 4 | §6 26 May Close | 7,519.12 | 7,527.5 (full-day 7,521.5) | −8.38 (−2.38) | Discrepancy (>3, <10) — not a failure |
| 5 | §6 27 May Open | 7,521.0* | 7,531.0 | −10.0 | Discrepancy (>8) |
| 6 | §6 27 May High | 7,548.7* | 7,536.0 | +12.7 | Discrepancy (>8) |
| 7 | §6 27 May Low | 7,505.4* | 7,504.3 | +1.1 | Consistent |
| 8 | §6 27 May Close | 7,520.36 | 7,528.5 (full-day 7,543.0) | −8.14 (−22.6) | Discrepancy (>3, <10) — not a failure |
| 9 | §6 28 May Open | 7,528.0* | 7,525.0 | +3.0 | Consistent |
| 10 | §6 28 May High | 7,571.2* | 7,576.2 | −5.0 | Consistent |
| 11 | §6 28 May Low | 7,522.6* | 7,515.5 | +7.1 | Consistent |
| 12 | §6 28 May Close | 7,563.63 | 7,572.5 (full-day 7,578.2) | −8.87 (−14.6) | Discrepancy (>3, <10) — not a failure; also differs from the 29 May report's 7,564.51 by −0.88 |
| 13 | §6 29 May Open | 7,566.0* | 7,581.1 | −15.1 | Discrepancy (>8) |
| 14 | §6 29 May High | 7,599.38 | 7,601.8 | −2.42 | Consistent |
| 15 | §6 29 May Low | 7,563.0* | 7,567.9 | −4.9 | Consistent |
| 16 | §6 29 May Close | 7,580.06 | 7,584.8 (full-day 7,581.1) | −4.74 (−1.04) | Discrepancy (>3, <10) — not a failure |
| 17 | §6 / §1 / §3 / §21b 01 Jun (D-1) Open | 7,582.29 | 7,575.2 | +7.09 | Consistent |
| 18 | §6 01 Jun (D-1) High | 7,603.44 | 7,623.6 | −20.16 | Discrepancy (>8) on a row the report calls "range corroborated" |
| 19 | §6 01 Jun (D-1) Low | 7,562.61 | 7,568.5 | −5.89 | Consistent |
| 20 | §6 01 Jun (D-1) Close (= §1, §3, §4, §21b entry) | 7,599.96 | 7,606.0 (full-day 7,600.2) | −6.04 (−0.24) | Discrepancy vs cash (>3, <10) — not a failure; matches the full-day close |
| 21 | §6 RSI2 column | ≈50, 100, 100, 100, 100 | slice cash closes: 75.34, 3.82, 100, 100, 100 (slice includes a 25 May holiday CFD session, which drives the 3.82) | rows 3–5 match | Consistent; helper recomputation from the report's own closes = n/a, n/a, 100, 100, 100 → arithmetic reproduces for all testable rows |
| 22 | §11 daily pivots basis | "from prior session 29 May" (H 7,599.38 / L 7,563.0 / C 7,580.06) | prior session is 01 Jun | wrong session | Failure of basis; values reproduce from the stated 29 May H/L/C (P 7,580.81, R1 7,598.63, S1 7,562.25, R2 7,617.19, S2 7,544.43, R3 7,635.01, S3 7,525.87) |
| 23 | §11 daily pivots vs D-1 | P 7,580.81 / R1 7,598.63 / S1 7,562.25 | from the report's own 01 Jun H/L/C: P 7,588.67 / R1 7,614.73 / S1 7,573.90 / R2 7,629.50 / S2 7,547.84 / R3 7,655.56 / S3 7,533.07; from the slice cash D-1: P 7,599.37 / R1 7,630.23 / S1 7,575.13 / R2 7,654.47 / S2 7,544.27 | P −7.86 (own data) / −18.56 (slice) | Discrepancy |
| 24 | §11 weekly P | 7,551.20 | from the report's own prior-week H/L/C (7,599.38 / 7,470.1 / 7,580.06): 7,549.85; slice weekly (cash): 7,563.63 | +1.35 / −12.43 | Does not reproduce from the report's own inputs (reproduces only with H = 7,603.44, the 01 Jun high) |
| 25 | §9 / §21 ATR(14) | not stated; implied 45.97 (3×ATR = 137.91; 0.25×ATR = 11.49) | 67.30 cash / 74.58 full-day | ≈ −21.3 | Discrepancy; ATR must be stated and reconciled |
| 26 | §10 / §1 VIX | 15.32, "four-month low", "falling" | VIX slice close 16.53 (29 May, window low), 17.14 (01 Jun, up on the day) | −1.21 / −1.82 | Discrepancy in level and D-1 direction (proxy basis may explain part of the level gap) |
| 27 | §10 USDX | ≈98.8 → 99.1 rising | 98.996 (25 May) → 99.193 (01 Jun) | ≈ −0.1 | Consistent |
| 28 | §13c / §12 core PCE 28 May | 3.3% "as expected" | NEWS slice: actual 3.3, consensus 3.1, previous 3.2 | 0.0 on actual; +0.2 vs consensus | Actual consistent; "as expected" conflicts with the slice consensus |
| 29 | §21b Trade 3A fib levels | 38.2% 7,552.50 / 50% 7,536.77 / 61.8% ≈7,521.0 / 27.2% ext 7,639.71 on swing 7,470.1 → 7,603.44 | recomputed: 7,552.50 / 7,536.77 / 7,521.04 / 7,639.71 | 0 | Arithmetic reproduces (on an indicative swing anchor) |
| 30 | §20 / §21a direction score | +0.65 | 0.25 + 0.20 + 0.15 + 0.058 + 0.045 − 0.05 = 0.653 | 0 | Reproduces with the default weight vector |
