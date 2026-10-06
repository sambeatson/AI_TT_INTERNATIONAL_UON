# Trust Score v3.7 QA — FTSE 100 daily report, D = 2026-06-08

Report: `reports/md/FTSE_EuroStoxx_Report_08Jun2026.md` · Run: ftse_qa1 · Basis checked: `_cash` (the report claims the cash index)
Level file `data/levels/UK100_by_date/2026-06-08.csv`: `last_bar_date` = 2026-06-05 < D, so it is leak-free and was used.
Slice files used are the `upto_2026-06-07` ones (the calendar day before D), the last bar is 2026-06-05 22:45 broker.
Tolerances (brief §4): close |Δ| ≤ 5 pts, open/high/low |Δ| ≤ 10 pts. Pivots are derived from H/L/C, so I applied 10 pts to pivots. The brief gives no explicit pivot tolerance.

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
n_cards=2
n_duds=0
n_warns=0
```

`n_cards=2` is the count of non-suppressed cards the integrity mean is taken over. The linter returned 3 rows, and Trade 1 is SUPPRESSED.

## 1. Section 7 checklist

| Row | Reviewer notes | Evidence observed | Score |
|---|---|---|---|
| 1.1 Variables respected | Asset (FTSE 100 cash), counters (USDX, S&P 500, DAX 40, Euro Stoxx 50 as reference), as-of close Fri 5 Jun, 5-session lookback, GBP/index points and Europe/London are all honoured. Gaps: (a) the 07:00 UK daily-open anchor was overridden "per request" (§20), so it is a disclosed deviation; (b) the source tier mix is thin, because the §4 "LSE / FTSE Russell" row is context only and quotes no close, there is no sell-side row, and an IG retail-quote row is present; (c) §2 does not define the counter set. | §2, §4, §20 | 3 |
| 1.2 Coverage and currency consistent | Data dates are D-1 or earlier and the session is D. Drift points: the "prior week" weekly pivots do not correspond to the 1–5 Jun week in the report's own §6 (see 3.3); the §1 52-week range 8,707.65–10,934.94 differs from the §4 one-year range 8,718.75–10,910.55 (plausibly intraday vs close basis, but not stated); "near record territory" (§1, §9) sits against a 25-day high of 10,560.0 (185.8 pts above the close). | §1, §4, §9, §11 | 3 |
| 1.3 Audience and tone | Institutional strategist tone, no retail language. Small blemish: process meta-text leaks into the deliverable ("per user instruction", "per request", "forward-test session"). | §19, §20 | 4 |
| 2.1 Sections present and ordered | §1–§21 present, in order, with §13a–d and §21a–d. | headings | 4 |
| 2.2 Scorecard as a table | §6 is a table, but the required Source A / Source B / Final columns are absent (only Date/O/H/L/C/RSI2/Trend/Validation). §11 daily is a table running R5→S5 with a malformed "Level / Price / Level" header. Weekly shows R3→S3. Monthly shows only R2/R1/P/S1/S2, with R3 and S3 missing (3 levels each side required). | §6, §11 | 3 |
| 2.3 Method steps visible | §4→§5 observations to consensus is visible. §8 is candle by candle with a sequence call, and §9 gives a regime. §9 has no persistence or overlap numbers, and no ATR(14) or KER values. §7 has no charts, only a text placeholder explaining the adapters were unreachable (accepted as a caption, noted). §7 says the Investing.com adapter was unreachable while §4/§20 list Investing.com as a quote source. | §7–§9 | 3 |
| 3.1 Quantitative claims sourced | The headline numbers in §1/§12/§14 mostly carry no source and do not point to §4/§13: Nasdaq −4.2%, VIX +39.7% to 21.5, DXY ~99.4 / +0.66%, the miner percentages, US CPI ~3.8%, UK CPI ~3.3%, Bank Rate 3.75%, "~80% overseas revenue", the 52-week range. | §1, §12, §14 | 2 |
| 3.2 Citations exist and contain data | Three checked. Yahoo 10,368.05 is consistent with Investing's 10,360.32 plus +7.73. Trading Economics "gained 15 points … down 0.3% for the week" is consistent with 10,375 / +0.14% and with the slice (29 May cash close 10,410.0 to 10,374.2 is −0.35%). BBN agrees with the figure. None is self-contradictory, so no fabrication is established. Weaknesses: AJ Bell "recent" and Cambridge "≈30 May" are not dated precisely, "CNBC / TE" is a merged citation, and the Sunday Guardian is dated Fri 5 Jun. The 10,368.05 close is 6.15 pts below the slice cash close (just outside tolerance). | §4, §13a | 3 |
| 3.3 Calculations transparent | RSI2 reproduces from the report's own closes for Wed/Thu/Fri (37.0 / 0.0 / 21.3 confirmed with `--closes`); Mon/Tue (100) cannot be tested (no pre-window closes). Daily pivots reproduce exactly from the stated Fri H/L/C. Not transparent or reproducible: weekly pivots, which back out to H 10,484.9 / L 10,354.9 / C 10,400.0, not the §6 week (H 10,440.0 / L 10,238.6 / C 10,368.05 would give P 10,348.9); monthly pivots back out to H 10,579.9 / L 10,119.9 / C 10,402.1; ATR(14) and KER are never stated numerically (§19: "estimated"), and the cards imply ATR ≈ 78–80; §21a shows three of six signal×weight terms; the −0.21 sentiment tilt is "source-class-weighted" with no weights (an unweighted mean is −0.167). | §6, §9, §11, §13b, §21a | 2 |
| 3.4 Numbers reconcile | The D-1 close 10,368.05 is identical in §1/§3/§4/§6, and RSI2 in §6 equals §8. Breaks: Trade 2 entry 10,420 contradicts its own stated formula ("10% of the way P→R1" = 10,375.8); 3C TP1 10,642 and stop ~10,340 do not follow the card's own formulas (10,662 / 10,319); §21d reports Trade 1 hit rates TP1/TP2/TP3 = 100%/50%/0% on a single triggered trade; §8 calls Mon "a modest up-day" while §6 shows Close 10,398.6 < Open 10,402.0; Tue/Wed/Fri opens equal the prior close exactly (§6), while Thu opens 55.9 below Wed's close. | §6, §8, §21b, §21d | 2 |
| 4.1 Pillars conclude | §8 Indecision, §9 Neutral/Transitional and §10 MIXED conclude. §12 has per-bullet tags but no overall direction. §14 ends on a watch item with no direction label. | §8–§14 | 3 |
| 4.2 Cross-asset interpreted | §10 gives mechanisms (USD translation vs risk-off, global beta, Eurozone proxy, low tech weight). It lacks an oil/Brent mechanism row (the energy weight is argued in §12). | §10 | 4 |
| 4.3 Synthesis reconciles tensions | Not reconciled. §21a score −0.13, §16/§17 mild downside skew and §13b bearish tilt sit against a LONG Trade 2 and an "upside" 3C trigger, with no rationale for the side. The 3C rationale "recent retests failed at the highs" argues against an upside trigger. §21a's "no material conflict" is not defended. | §16–§18, §21 | 2 |
| 4.4 Calibrated language | §17 is exactly one sentence. Confidence Medium is stated in §3 with a reason. | §3, §17 | 4 |
| 4.5 Card construction (protocol row, scored in Category 4) | Trade 1 SUPPRESSED is correct (\|−0.13\| < 0.25). Trade 2: entry contradicts its formula, TP1 = +14 pts (0.15R) and TP2 = +36 pts (0.38R) instead of 1R/2R, and it uses a stale weekly pivot as "strong confluence". 3C: the range is the 5-day band, not the 25-day range, the 25-day boundaries are mis-stated, it has arithmetic errors, it is two-sided with "e.g." entries, and it has no TP3 price. The linter is CLEAN because its static checks cannot see these rule violations. | §21b | 1 |
| 5.1 Data dated, staleness flagged | Mon–Wed O/H/L are flagged single-source indicative, and the §4 dates are given. Undated or approximate: AJ Bell "recent", Cambridge "≈30 May"; the weekly/monthly pivot periods are mislabelled. | §4, §6, §13a | 3 |
| 5.2 Assumptions up front | The anchor override is recorded only in §20 (not in §1 or on any card), and the ATR/KER estimation is disclosed only in §19. §7 states the missing charts. | §19, §20, §21b | 3 |
| 5.3 Red flags surfaced | §12/§15 give two-sided risks. 3C carries the 17–18 Jun central-bank collision and Trade 2 notes it. §13c omits high-impact events from the calendar slice (see feedback 9) and lists non-calendar items instead. | §12, §13, §15, §21b | 4 |
| 5.4 Restrictions honoured | No module codes, bracketed variables or framework name. Issues: §4 says retail CFD-broker spreads are excluded yet lists an "IG / CNBC live quotes — Spread/quote" row; "v2.1 baseline" and "per user instruction" leak prompt internals; Tue/Wed/Fri opens equal the prior close exactly, which looks interpolated but is labelled indicative rather than presented as sourced. I judged this not an open breach (IG is not used in the consensus), so no override. | §4, §6, §20 | 3 |

Category means: C1 = (3+3+4)/3 = 3.33 → 3 · C2 = (4+3+3)/3 = 3.33 → 3 · C3 = (2+3+2+2)/4 = 2.25 → 2 · C4 = (3+4+2+4+1)/5 = 2.8 → 3 · C5 = (3+3+4+3)/4 = 3.25 → 3

### Category 3 data reconciliation (report §6/§11 vs level file `_cash` and slice cash-session bars)

Daily OHLC, report minus slice cash session:

| Date | Open | High | Low | Close | RSI2 (report / slice cash) |
|---|---|---|---|---|---|
| Mon 1 Jun | 10,402.0 vs 10,371.9: **+30.1** | 10,421.5 vs 10,410.4: **+11.1** | 10,360.0 vs 10,286.2: **+73.8** | 10,398.6 vs 10,324.5: **+74.1** | 100 / 0.00 |
| Tue 2 Jun | 10,398.6 vs 10,360.7: **+37.9** | 10,430.2 vs 10,398.1: **+32.1** | 10,371.0 vs 10,332.5: **+38.5** | 10,412.4 vs 10,375.6: **+36.8** | 100 / 37.41 |
| Wed 3 Jun | 10,412.4 vs 10,351.4: **+61.0** | 10,440.0 vs 10,384.0: **+56.0** | 10,366.0 vs 10,320.7: **+45.3** | 10,388.9 vs 10,341.7: **+47.2** | 37.0 / 60.12 |
| Thu 4 Jun | 10,332.5 vs 10,301.0: **+31.5** | 10,360.3 vs 10,360.2: +0.1 ok | 10,238.6 vs 10,236.5: +2.1 ok | 10,360.3 vs 10,343.3: **+17.0** | 0.0 / 4.51 |
| Fri 5 Jun (D-1) | 10,360.3 vs 10,383.0: **−22.7** | 10,415.7 vs 10,417.0: −1.3 ok | 10,331.5 vs 10,331.9: −0.4 ok | 10,368.05 vs 10,374.2: **−6.15** | 21.3 / 100.00 |

- Four of the five closes are more than 15 pts from the slice (Mon +74.1, Tue +36.8, Wed +47.2, Thu +17.0), and the D-1 close is just outside the 5-pt tolerance. This is scored as a Category 3 failure.
- The Fri RSI2 of 21.3 is arithmetically right for the report's closes but wrong against the level file (`rsi2_cash` = 100.0, `rsi2_full` = 60.0). The wrong closes change the oscillator regime.
- Fri's day change is stated as +7.73 pts / +0.07% (§1), against +30.9 pts on the slice cash closes (10,343.3 → 10,374.2).
- swing_high_5d = 10,440.0 vs 10,417.0 (**+23.0**); swing_low_5d = 10,238.6 vs 10,236.5 (+2.1, ok).
- ATR(14) is not stated. The cards imply ≈ 78–80, against `atr14_cash` 105.46 (`atr14_full` 129.74), about 25% low.

Daily pivots (report from stated Fri H/L/C, minus `d_cash_*`): P 10,371.8 vs 10,374.37 (−2.6) · R1 10,412.0 vs 10,416.83 (−4.8) · R2 10,456.0 vs 10,459.47 (−3.5) · R3 10,496.2 vs 10,501.93 (−5.7) · S1 10,327.8 vs 10,331.73 (−3.9) · S2 10,287.6 vs 10,289.27 (−1.7) · S3 10,243.6 vs 10,246.63 (−3.0). All within tolerance, so daily pivots are consistent.

Weekly pivots vs `w_cash_*` (W23 = 1–5 Jun): P 10,413.3 vs 10,342.57 (**+70.7**) · R1 10,471.7 vs 10,448.63 (**+23.1**) · R2 10,543.3 vs 10,523.07 (**+20.2**) · R3 10,601.7 vs 10,629.13 (**−27.4**) · S1 10,341.7 vs 10,268.13 (**+73.6**) · S2 10,283.3 vs 10,162.07 (**+121.2**) · S3 10,211.7 vs 10,087.63 (**+124.1**). All seven are outside tolerance.

Monthly pivots vs `m_cash_*` (May 2026): P 10,367.3 vs 10,370.4 (−3.1, ok) · R1 10,614.7 vs 10,599.6 (**+15.1**) · R2 10,827.3 vs 10,789.2 (**+38.1**) · S1 10,154.7 vs 10,180.8 (**−26.1**) · S2 9,907.3 vs 9,951.6 (**−44.3**) · R3/S3 not given (11,018.4 / 9,762.0 in level file). The report's implied May range is 459.9 pts (H 10,579.9 / L 10,119.9), against 418.8 (10,560.0 / 10,141.2).

Counters vs slices (CFD feeds, Fri 5 Jun):
- USDX close 100.087 (+0.63% on the day), against "DXY ~99.4, +0.66%" (§12/§14). The percentage matches, but 99.4 is Thursday's level (99.46).
- VIX close 18.96 (+15.9% on the day, from 16.36), against "+39.7% to 21.5" (§1/§9/§14). The headline volatility claim does not reconcile (Δ level −2.5, Δ move +24 pts of percent).
- S&P 500 −2.90% against −2.6% (provider basis, minor). Nasdaq and DAX have no slice and are unverifiable.
- The Fri payrolls event is confirmed by the NEWS slice (NFP actual 172 vs consensus 77, unemployment 4.3%). Halifax −0.1% m/m is confirmed.

## 2. Category roll-up

| Cat | Level | Multiplier | Points | Justification |
|---|---|---|---|---|
| 1 Prompt adherence (20) | 3 | 0.65 | 13.00 | Variables mostly respected; anchor override, thin source tiering and an IG retail row against the stated exclusion. |
| 2 Structure (20) | 3 | 0.65 | 13.00 | All 21 sections present and ordered; §6 lacks Source A/B/Final, monthly pivots lack R3/S3, charts absent. |
| 3 Accuracy (25) | 2 | 0.40 | 10.00 | Four of five closes off the slice by 17–74 pts, Fri RSI2 21.3 vs 100, weekly/monthly pivots mismatched, ATR/KER unstated. |
| 4 Reasoning (20) | 3 | 0.65 | 13.00 | Good cross-asset mechanisms and a correct §17, but card construction and synthesis are weak. |
| 5 Currency (15) | 3 | 0.65 | 9.75 | Staleness flagged for Mon–Wed; undated items; anchor override caveat only in §20; the exclusion statement contradicts the IG row. |

## 3. Total, band, override

Total = 13.00 + 13.00 + 10.00 + 13.00 + 9.75 = 58.75 → **59** → **Low** (40–59).
Override check: none.
- Hallucinated source: not established. The three spot-checked citations are internally consistent, and no source is impossible or self-contradictory on the evidence available.
- Restriction breach: the IG row and the leaked process text are minor. Nothing is an open breach of a stated restriction that would trigger the Moderate cap, and C1 was not lowered.

## 4. Card Integrity (linter rows, verbatim from `qa/ftse_qa1/lint_static/2026-06-08.csv`)

| card_id | report_date | strategy | flags | dud |
|---|---|---|---|---|
| 2026-06-08_Trade_1 | 2026-06-08 | Trade 1 - Daily Directional | SUPPRESSED | False |
| 2026-06-08_Trade_2 | 2026-06-08 | Trade 2 - Pivot, regime-aware (TRANSITION → breakout side only, aligned with Trade 3C upside trigger) | CLEAN | False |
| 2026-06-08_Trade_3C | 2026-06-08 | Trade 3 - Momentum-Breakout (3C); regime_label = TRANSITION | CLEAN | False |

Per card: Trade 1 suppressed (excluded) · Trade 2 = 100 · Trade 3C = 100. Report-level Card Integrity = mean(100, 100) = **100.0**; n_cards = 2, n_duds = 0, n_warns = 0.
Card Integrity is separate from the 100. The static linter being CLEAN does not clear the rule-level construction defects scored in row 4.5 and listed in the feedback.
