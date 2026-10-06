# Trust Score v3.7 — FTSE 100 daily report, D = 2026-07-30

Report: `reports/md/FTSE_EuroStoxx_Report_30Jul2026.md`
Level file: `data/levels/UK100_by_date/2026-07-30.csv` (`last_bar_date` = 2026-07-29 < D: leak-free, accepted). Slice stats from `engine/qa_slice_stats.py --cash-open 10:00 --cash-close 18:30`.
Basis claimed by the report: cash index, LSE session 08:00-16:30 UK (§2), so the `_cash` columns are the comparator.

## Machine-readable result
```
c1=2
c2=3
c3=2
c4=3
c5=2
total=50
band=Low
override=restriction_breach
card_integrity=100
n_cards=3
n_duds=0
n_warns=0
```

## 1. Section 7 checklist

| Row | Score | Notes | Evidence (location) |
|---|---|---|---|
| 1.1 Variables respected | 3 | FTSE 100 cash index primary, GBP/points, as-of 29 Jul London close, 5/25 lookback, 07:00 UK anchor all respected. Weak points: §4 has 6 rows but only 5 distinct sources and only two (Reuters, Trading Economics) price the D-1 close; no index-provider or exchange quote is cited (LSE appears only as "attempted" in §20); Trading Economics is labelled "CFD proxy" yet classed Core and used as Source B for 28/29 Jul. Data-provider tickers `^FTSE`, `^STOXX50E` appear in §2 (Rule 5 bars them). | §2, §4, §6, §20 |
| 1.2 Coverage and currency consistent | 2 | Price data stops at D-1, but event dating drifts. §13d puts the Fed decision on 30 Jul; the calendar slice has it at 2026-07-29 21:00 broker (19:00 UK), after the London close and before the D session. §13d puts the BoE decision on 31 Jul; the calendar has it at 2026-07-30 14:00 broker (12:00 UK), inside the D session. §13d lists "1 Aug US labour data", a Saturday. §21c carries an outcome for a card entered at the 29 Jul close (see 3.4/5.4). | §13c, §13d, §21c |
| 1.3 Audience and tone | 4 | Strategist register, trading/risk-review framing, no retail tone. Minor: "melt-up", "textbook pivot-straddle". | §1, §11, §18 |
| 2.1 Sections present and ordered | 4 | All 21 sections present in order; §13a-d and §21a-d present; five chart headings with no image (accepted as pandoc loss, noted). §6 omits the required "Final Value Used" column and the one-line RSI2 working beneath the table. | headings; §6 |
| 2.2 Scorecard/pivots as tables | 2 | §6 is a table but missing the Final Value Used column. §11 daily table is not R3→P→S3: it prints R5/R4/R3/R2/R1 beside P/S1..S5 in a two-column grid, so P sits on the R5 row; five levels each side instead of three. Weekly table has no S3; monthly table has only R2/R1/P/S1 (no R3, S2, S3). | §6, §11 |
| 2.3 Method steps visible | 4 | §4-§5 observations → consensus visible; §8 candle by candle with sequence call; §9 gives overlap 0.54, persistence 0.58, VOLator, KER 0.45. §8 omits close-location % and RSI2 on some sessions; no RSI2 working. KER 0.45 is reproducible (my smoothed KER on cash closes: 0.45 on 28 Jul, 0.52 on 29 Jul). | §8, §9 |
| 3.1 Quantitative claims sourced | 2 | §12 (Shell +2.8%, BP +3.4%, Standard Chartered +3.8%, Reckitt +4.3%, Brent ~+7%), §1 (~80% overseas earnings, +270 pts) and §14 (VIX near 18, USDX "15-month high") carry no source or pointer to §4/§6/§13. ATR(14) = 78.1 appears only in §20 with no derivation or source. | §1, §12, §14, §20 |
| 3.2 Citations exist and contain data | 3 | Cannot fetch. Three spot-checks: (a) Reuters "touched an intraday record high… surge in oil stocks" with 10,908.41 close and 10,951 high: consistent (slice cash high 10,945.6, delta +5.5). (b) Trading Economics "rose 27 points to close at 10898": implies a prior close of 10,871, but the report's 28-Jul close is 10,878.85 (7.85 pt gap) and the same row is later marked CORROB against Reuters 10,908.41 (10.41 pt gap vs the stated ±0.10 tolerance). (c) STL.news "DXY softened overnight to 101.38": consistent with USDX ~101.4 in the slice. No source is self-impossible, so no hallucinated-source override, but (b) is an unreconciled figure. | §4, §6, §13a |
| 3.3 Calculations transparent | 2 | Daily pivots reproduce arithmetically from the stated 29-Jul H/L/C (P 10,909.46 etc.). RSI2 for 27-29 Jul reproduces (100.0) from the report's own closes; the 24-Jul value 84.5 cannot be reproduced (seed closes not printed; script gives 53.25 on cash closes) and no working line is shown. ATR14 78.1 is not reproducible: the report's own five ranges average ~96.8 and the level file gives 109.83 (cash) / 138.48 (full). §21a components (+0.25, +0.20, +0.15, +0.045, +0.07 = 0.715) do not sum to the stated +0.76; the sixth signal is missing. Weekly pivots computed from two sessions only (see Cat. 3 table). | §6, §9, §11, §20, §21a |
| 3.4 Numbers reconcile | 1 | Internal: D-1 close 10,908 is identical in §1/§3/§4/§6/§21b. But: "five green-bodied sessions" (§1) vs 23-Jul red body in §6/§8; prior close 10,878.85 (§3) vs 10,871.02 snapshot row (§4); STOXX 29-Jul move quoted as -0.5% (§13a), -0.85% (implied by §6) and -0.99% (§6 note); §11 narrative says close is "well above weekly R3" while quoting R3 at 10,924 overhead; §21d TP2 hit rate 80% vs 3 of 5 in §21c. Against the slice: 14 of 20 OHLC fields outside tolerance, two closes wrong by more than 15 pts (23 Jul +21.1, 29 Jul +20.6), weekly pivots off by 39-199 pts, ATR off by 31.7 pts. | §1, §3, §4, §6, §11, §13a, §21c-d |
| 4.1 Pillars conclude | 3 | §8 "Bullish continuation", §9 "Bias: Bullish", §10 "CONFIRM" are explicit. §12 bullets carry a supportive/neutral tag but no pillar conclusion; §14 ends "net near-term supportive, medium-term two-sided" with no direction label. §10's CONFIRM is contradicted by the slice (see Cat. 4 notes). | §8-§10, §12, §14 |
| 4.2 Cross-asset interpreted | 3 | Mechanisms are given (dollar translation for overseas earners, risk appetite, energy weight). The reads they rest on do not match the slice: S&P 500 labelled "Rising" but falls 7,436.6→7,368.3 (-0.9%) between 28 and 29 Jul at the 16:30 UK mark and is -0.2% over the five sessions; USDX labelled "soft" but is 101.495 (23 Jul) → 101.448 (29 Jul), flat, and +0.14% on the day; VIX described as "near 18 and easing" but is 18.05 → 19.09 (+5.8%) on 29 Jul. | §10, §14 |
| 4.3 Synthesis reconciles tensions | 3 | Fed-event conditionality, stretched 92nd-percentile position and STOXX divergence are flagged. Not reconciled: RSI2 pinned at 100 for three sessions vs a "Continuation" call and a +0.76 score; §11 resistance-shelf narrative contradicts its own tables; §11/§19 state every pivot tier is single-source-indicative while §20 says Trade 2 is not suppressed. | §11, §15-§18, §20, §21a |
| 4.4 Calibrated language | 4 | §17 is exactly one sentence with one conditional; confidence Medium stated in §3/§18. A +0.76 score and "high-conviction" wording sit awkwardly beside Medium confidence and indicative inputs. | §3, §9, §17 |
| 4.5 Card construction (protocol) | 1 | Trade 2 emitted against a fired suppression gate; ATR 78.1 drives every stop, cap and swing test; Trade 3A swing low and the market-entry reference differ from the data; weekly-pivot confluences are wrong; see Feedback. Linter is static and reports CLEAN, which does not cover these. | §21b |
| 5.1 Data dated, staleness flagged | 3 | Prices and articles are dated; single-source O/H/L flagged in §6/§19. Undated: USDX "15-month high", "80% overseas", VIX "near 18". Calendar rows misdated (1.2). | §4, §6, §13, §19 |
| 5.2 Assumptions up front | 3 | 07:00 UK anchor stated in §2 and on Trade 1. Single-source caveat on Trade 1 and Trade 2 but not on Trade 3A, whose swing low (23-Jul 10,598) comes from a row marked SINGLE (ind.). No statement of the ATR basis. | §2, §21b |
| 5.3 Red flags surfaced | 2 | The Fed event is surfaced. Omitted: BoE decision at 12:00 UK on D and US data/PCE/GDP/jobless claims at 13:30 UK on D (all inside the holding period) are absent from §13d and from every card caveat; rising VIX and falling S&P 500 on 29 Jul are reported as the opposite. | §13d, §21b |
| 5.4 Restrictions honoured | 0 | Breached: (i) Trade 2 emitted although §11 and §19 state every pivot tier is single-source-indicative, and §20/§19 cite a "leniency directive" and "per instruction" as authority (M5 gate non-overridable; citing such an instruction is itself barred). (ii) Naming scan hits: "M5" (§11), "Step-4" and "v2.1 baseline", "regime_label" (§20), `^FTSE`, `^STOXX50E` (§2). (iii) Retail-CFD quote (Trading Economics "CFD proxy") used as a Core source and as Source B in §6. (iv) §21c reports an outcome for the 29-Jul card, which needs bars after the as-of close. | §2, §6, §11, §19, §20, §21c |

## 2. Category 3 evidence: report vs level file (cash basis; tolerance close ±5, O/H/L ±10)

D-1 session (29 Jul) in the level file: O 10,895.9 · H 10,945.6 · L 10,855.2 · C 10,887.8 · RSI2 100.0 · ATR14 109.83 (full-day basis: O 10,906.0, H 10,945.6, L 10,813.2, C 10,817.9, ATR14 138.48).

| Session | Open (rep / slice / Δ) | High | Low | Close |
|---|---|---|---|---|
| 23 Jul | 10,665.10 / 10,704.0 / -38.9 X | 10,681.20 / 10,709.8 / -28.6 X | 10,598.40 / 10,597.3 / +1.1 | 10,639.17 / 10,618.1 / +21.1 X (>15) |
| 24 Jul | 10,638.86 / 10,582.2 / +56.7 X | 10,738.83 / 10,728.2 / +10.6 X | 10,599.10 / 10,580.9 / +18.2 X | 10,736.23 / 10,728.0 / +8.2 X |
| 27 Jul | 10,758.40 / 10,803.7 / -45.3 X | 10,812.60 / 10,816.3 / -3.7 | 10,740.10 / 10,747.1 / -7.0 | 10,784.50 / 10,795.0 / -10.5 X |
| 28 Jul | 10,800.20 / 10,795.7 / +4.5 | 10,902.40 / 10,878.7 / +23.7 X | 10,795.60 / 10,762.8 / +32.8 X | 10,878.85 / 10,874.0 / +4.9 |
| 29 Jul | 10,871.16 / 10,895.9 / -24.7 X | 10,951.06 / 10,945.6 / +5.5 | 10,868.90 / 10,855.2 / +13.7 X | 10,908.41 / 10,887.8 / +20.6 X (>15) |

14 of 20 fields outside tolerance; two closes off by more than 15 pts. The report's §3 consensus 10,908 (range 10,895-10,920) excludes the data close of 10,887.8. The Euro Stoxx and DAX values cannot be checked (no slice).

RSI2: report closes 10,784.50 / 10,878.85 / 10,908.41 give 100.0 on each of 27/28/29 Jul (matches report). 24 Jul 84.5 not reproducible; 23 Jul shown as "—" so its Neutral trend label cannot be tested. ATR14: report 78.1 vs 109.83 cash (-31.7, -29%) / 138.48 full.

Pivots (report vs level-file cash):

| Level | Daily rep / data / Δ | Weekly rep / data / Δ | Monthly rep / data / Δ |
|---|---|---|---|
| R3 | 11,032.17 / 11,027.6 / +4.6 | 10,924.34 / 11,123.37 / -199.0 | not given (data 11,180.73) |
| R2 | 10,991.62 / 10,986.6 / +5.0 | 10,831.58 / 10,941.13 / -109.6 | 10,854.69 / 10,894.77 / -40.1 |
| R1 | 10,950.01 / 10,937.2 / +12.8 | 10,783.91 / 10,834.57 / -50.7 | 10,696.79 / 10,698.13 / -1.3 |
| P | 10,909.46 / 10,896.2 / +13.3 | 10,691.15 / 10,652.33 / +38.8 | 10,412.20 / 10,412.17 / 0.0 |
| S1 | 10,867.85 / 10,846.8 / +21.1 | 10,643.48 / 10,545.77 / +97.7 | 10,254.30 / 10,215.53 / +38.8 |
| S2 | 10,827.30 / 10,805.8 / +21.5 | 10,550.72 / 10,363.53 / +187.2 | not given (data 9,929.57) |
| S3 | 10,785.69 / 10,756.4 / +29.3 | not given (data 10,256.97) | not given (data 9,732.93) |

The weekly table is built from only 23-24 Jul: weekly P 10,691.15 reproduces exactly from H 10,738.83 (24 Jul), L 10,598.40 (23 Jul, a SINGLE (ind.) row) and C 10,736.23. The prior week is 20-24 Jul; per the slice its high is 10,758.9 (22 Jul) and its low 10,470.1 (20 Jul). Daily pivots are arithmetically right for the report's own H/L/C and are off only because those inputs are off.

Other slice checks: 25-session range position on the data is 89.8% (report 92nd percentile, small); 5-day swing low on the data is 10,580.9 (24 Jul), not the 10,598 (23 Jul) the report uses.

## 3. Category roll-up

| Cat | Rows | Mean | Level | Multiplier | Points | Justification |
|---|---|---|---|---|---|---|
| 1 Prompt adherence (20) | 3, 2, 4 | 3.0 → 3, then -1 for the restriction breach | 2 | 0.40 | 8.0 | Core variables respected; source mix, tickers, event dating off; restriction override lowers the level by one. |
| 2 Structure (20) | 4, 2, 4 | 3.3 → 3 | 3 | 0.65 | 13.0 | 21 sections present; §6 and §11 tables malformed or incomplete. |
| 3 Accuracy and evidence (25) | 2, 3, 2, 1 | 2.0 | 2 | 0.40 | 10.0 | No fabricated source found, but multiple material numeric errors (closes, ATR, weekly pivots, calendar dates), unreproducible RSI2/score, unsourced §12 figures. |
| 4 Reasoning and judgment (20) | 3, 3, 3, 4, 1 | 2.8 → 3 | 3 | 0.65 | 13.0 | Sound structure and one-sentence forecast; cross-asset reads contradict the counters; card construction fails a hard gate. |
| 5 Currency and transparency (15) | 3, 3, 2, 0 | 2.0 | 2 | 0.40 | 6.0 | Dating and caveats partly present; red flags and calendar collisions missed; several restrictions breached. |

## 4. Total, band, override
Total = 8.0 + 13.0 + 10.0 + 13.0 + 6.0 = **50** → band **Low** (40-59).
Override check: restriction breach confirmed (row 5.4 items i-iv). Cap Moderate (60-74) is not binding at 50; Category 1 already reduced one level (3 → 2). Hallucinated-source override: not triggered (no source found to be self-impossible); C3 not forced to 0. `override=restriction_breach`.

## 5. Card Integrity (linter rows copied verbatim from `qa/ftse_qa1/lint_static/2026-07-30.csv`)

| card_id | strategy | flags | dud | Card score |
|---|---|---|---|---|
| 2026-07-30_Trade_1 | Trade 1 — Daily Directional (LONG · TREND_UP regime) | CLEAN | False | 100 |
| 2026-07-30_Trade_2 | Trade 2 — Pivot, regime-aware (LONG · TREND_UP pivot breakout) | CLEAN | False | 100 |
| 2026-07-30_Trade_3A | Trade 3 — Momentum-Pullback 3A (LONG · TREND_UP) | CLEAN | False | 100 |

Report-level Card Integrity = mean(100, 100, 100) = **100**; n_cards = 3 (none suppressed); n_duds = 0; n_warns = 0. The linter runs in static mode with no market data, so this score says nothing about the gate and basis defects set out in the feedback; those are scored in Category 4 row 4.5 and Category 5 row 5.4.

## 6. Notes for the roll-up
- Cards are all LONG and anchored at 07:00 UK (linter anchor_broker 09:00 on Trade 1), consistent with the instance anchor.
- Chart images are absent from the markdown; accepted as a conversion artefact.
