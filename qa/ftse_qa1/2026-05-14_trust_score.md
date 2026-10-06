# Trust Score v3.7 — FTSE 100 Daily Report, 14 May 2026 (run ftse_qa1)

Report: `reports/md/FTSE_EuroStoxx_Daily_14_May_2026.md` · D = 2026-05-14 · Level file `last_bar_date` = 2026-05-13 (< D, verified) · Basis claimed by the report: cash index (`_cash` comparison used; `_full` shown where useful).

## Score block

```
c1=2
c2=3
c3=0
c4=3
c5=2
total=40
band=Low
override=hallucinated_source
card_integrity=100.0
n_cards=3
n_duds=0
n_warns=0
```

Notes on the block: `override=hallucinated_source` (C3 forced to 0, cap Low 40–59). A restriction breach is ALSO present (row 5.4: module codes M3/M5 and a bracketless variable name in the body); C1 was lowered one level for it (3 -> 2). The restriction cap (Moderate, 60–74) is looser than the Low cap, so the single `override=` value is the stricter one. `n_cards=3` counts card rows (1 SUPPRESSED, 2 scored); Card Integrity is the mean over the 2 non-suppressed cards.

## 1. Section 7 checklist

| Row | Reviewer notes | Evidence location | Score |
|---|---|---|---|
| 1.1 Variables respected | FTSE 100 cash primary, Euro Stoxx 50 secondary with no cards, counters USDX/S&P 500/DAX 40 (+ Brent/VIX in §14) as defined in §2/§10, tz Europe/London, 5/25-day lookback, GBP/points, 7 FTSE sources (>=6). Anchor: header says 07:00 UK but also "Run-time override: daily-open anchor advanced to the 14-May pre-open window" (leaks run mechanics; cards then say "working from 08:00 UK open", anchor_broker 10:00). §2 as-of is 14 May rather than D-1 close. Euro Stoxx given full OHLC + pivots. | header, §2, §10, §21b | 3 |
| 1.2 Coverage & currency consistent | Data dates are D-1 or earlier. Drift: §21c day names are wrong (06 May labelled Tue, 07 May Wed, 08 May Thu, 09 May Fri — 09 May is a Saturday, 12 May labelled Mon); §13d dates UK GDP to 15 May (calendar has it 14 May); STOXX "GBP-equivalent" column is a meaningless currency translation and the arithmetic is off (5,870/1.1528 = 5,092, report 5,072). | §21c, §13d, §4 | 3 |
| 1.3 Audience & tone | Strategist register, trading/risk-review framing, no retail tone. | §1, §18 | 4 |
| 2.1 Sections present & ordered | §1–§21 all present and in order, §13a–d and §21a–d present. §7 is prose only (five charts described; images dropped by conversion — accepted as caption per brief). §21c has impossible rows (see 3.4). | headings | 4 |
| 2.2 Scorecard as table | §6 is a table, but lacks the Trend, Final and Validation columns (only Date/O/H/L/C/Source A–B/RSI2). §11 pivots are tables ordered R3->S3 for daily/weekly/monthly (extra R1.5/S1.5 rows; STOXX stops at R2–S2). | §6, §11 | 3 |
| 2.3 Method steps visible | §4 observations -> §5 consensus visible; §8 candle-by-candle + sequence; §9 regime with KER/VOLator. §9 contradicts itself ("RANGE ... classified TRANSITION on the composite mapping rule" then "composite regime_label for FTSE is RANGE"). RSI2 is not shown with arithmetic; KER given as a signed value against an unsigned threshold. | §4–§9 | 3 |
| 3.1 Quantitative claims sourced | Many figures without a source or pointer: "10,197 support shelf (4 May effective close)", "10,375 last week's recovery high" (no such high in §6), ATR(14)≈78, 25-day low 10,184 / high 10,457, UK CPI 3.3%, Eurozone CPI 2.4%, UK10Y 4.8%, Gold $4,693, FOMC minutes 20 May, BoE hold 7 May. | §1, §8, §9, §12, §14, §13c/d | 2 |
| 3.2 Citations exist & contain data | Three spot-checks, all fail on self-consistency (see §3 below): (a) Yahoo ^FTSE "10,265.32 (−0.04%)"; (b) Trading Economics two incompatible 13 May quotes (10,325 +0.58% in §4; 10,297 +0.31% in §13a); (c) Yahoo ^STOXX50E "Zurich cash close"; also Investing.com "Open 10,318.66" vs §6 open 10,253.40. Treated as fabricated/impossible per brief §2 row 3.2. -> hallucinated-source override. | §4, §13a | 0 |
| 3.3 Calculations transparent | RSI2 not shown, and not reproducible from the report's own closes (3 of 4 testable rows off by 8–24 pts; table in §2 below). Pivot arithmetic does not follow from the stated H/L/C (daily R1/S1 off 13, weekly R3 off 79 and S3 off 54, monthly R1 off 57, R2 off 112, R3 off 113). ATR(14) ≈ 78 stated but 136.6 (cash) / 145.4 (full) in the level file. KER −0.12 stated without working. §21a component values given without signal × weight. | §6, §11, §9, §21a | 1 |
| 3.4 Numbers reconcile | D-1 close 10,265.32 is identical in §1/§3/§4/§6/§11 but conflicts with §13a (TE close 10,297; Sharecast 10,300.78 "intraday") and with §4's own −0.04% and Investing figures. Card pivots (10,355, 10,335, 10,285, 10,245) do reconcile to §11. §21c: short entries at 10,196 / 10,233 with exits at 10,221 / 10,247 booked as +0.5R / +0.4R (a short entered lower and marked higher is a loss); LONG fills on "Fri 09 May" (non-session); "TP1 hit Mon" with entries dated Fri while 12 May is called Mon. §12 STOXX "five consecutive lower closes from 6,045" — §6 shows three. §9 "stop 8 points above R2 (10,376)" — 10,388 is 12 above. | cross-section | 2 |
| 4.1 Pillars conclude | §8, §9, §10 conclude with direction labels; §12 and §14 are lists whose closing line is partly a direction ("CONTRADICTS bullish"), §12 has none. | §8–§14 | 3 |
| 4.2 Cross-asset interpreted | Mechanisms are given, but §10 asserts that a stronger USD is a headwind for the FTSE while §12 says the FTSE is a weak-GBP/dollar-earner beneficiary — unreconciled. S&P 500 is called "Falling −0.16% (7,400.96)" and VIX "17.99 (−2.1%)"; the slice shows US500 up 7,404.0 -> 7,458.5 (+0.7%) on 13 May and rising over the 5-day window (7,358.8 -> 7,458.5), VIX 19.04 -> 19.34. The direction used in §21a (−0.15 "cross-asset confirmation") rests on this. USDX "≈98.6" vs slice D-1 close 98.48 (acceptable; direction rising is right). | §10, §14, §21a | 2 |
| 4.3 Synthesis reconciles tensions | §16/§18 address §17 vs §21a. But the TRANSITION vs RANGE conflict in §9 (and §1's "short-term TRANSITION") is never resolved, and it decides which Trade 2/3 branch applies (TRANSITION = breakout side only / Trade 3C). The cross-asset "contradiction" is acknowledged against a wrongly-signed S&P read. | §9, §15–§18 | 2 |
| 4.4 Calibrated language | §17 is exactly one sentence; confidence Medium stated in §3 and §18; no hedge stacking. | §3, §17 | 4 |
| 4.5 Card construction (protocol: scored under C4) | Both scored cards put the 0.2R protective stop on the adverse side for a short (entry + 0.2R: 10,360 and 10,347). Trade 2 R = 35 = 0.26 × ATR14 (level file 136.59) — below the 0.3 × ATR floor; Trade 3B uses 3A language (38.2% retrace) instead of 3B rule (limit in 78.6–88.6% band; TP1 = mid; TP2 = far side −10%) and its "38.2% of 10,184–10,457" does not reproduce (=10,288 or 10,353, not 10,275). Entry tiers mislabelled against the level file. Companion Trade 2 cards (weekly R1.5 SHORT, S1.5 LONG) promised in prose but not tabulated. | §21b | 2 |
| 5.1 Data dated; staleness flagged | Prices and articles dated. But every pivot/OHLC input is declared CORROBORATED despite the §4 inconsistencies; no single-source flag raised where the sources contradict. The 06/07 May O/H/L/C are unreconcilable with the slice and unflagged. | §4, §6, §13, §19 | 3 |
| 5.2 Assumptions up front | Anchor-override caveat is in the header and §20, but absent from the cards (only "working from 08:00 UK open"). | header, §20, §21b | 3 |
| 5.3 Red flags surfaced | The central event risk is "UK CPI (April) 14 May, Tier-1". The scheduled calendar for D (rows are scheduled-only) shows UK GDP m/m, q/q, y/y (HIGH) at 07:00 UK, Business Investment, Trade Balance, Industrial/Manufacturing Production, Lagarde speech 10:15 UK, US Retail Sales/Core Retail/Jobless Claims (HIGH) 13:30 UK, EUR CPI/HICP y/y 08:00 UK; no UK CPI row. The report dates GDP to 15 May and omits US retail sales and Lagarde. The collision caveat on the cards therefore names the wrong event. | §13d, §15, §21b | 2 |
| 5.4 Restrictions honoured | Module codes in the body ("M5 strategies module trace", "M3 RANGE regime classification", "M5 §3a"), a variable-style token ("MAX_SIMULTANEOUS_LONG_SHORT = YES", "DEFAULTS", "v2.1 baseline"), a prompt-mechanics sentence in the header ("Run-time override ..."). A CFD quote (TE GB100 10,325) is tabled in §4 and "normalized" to 10,265.32 "cash equivalent" — a forced/synthesised price. Daily/rolled opens equal the prior close exactly on 07 May, 11 May and in the STOXX table (07 May, 11 May) — consistent with interpolated, not sourced, opens. -> restriction-breach override applies (C1 −1). | header, §4, §5, §6, §9, §20, §21b | 1 |

## 2. Category 3 data comparison (report vs level file, cash basis; tolerance ±5 close, ±10 O/H/L)

| Session | Field | Report | Slice (cash) | Δ | Verdict |
|---|---|---|---|---|---|
| Wed 13 May (D-1) | Open | 10,253.40 | 10,314.9 | −61.5 | FAIL |
| | High | 10,341.20 | 10,357.0 | −15.8 | FAIL |
| | Low | 10,248.30 | 10,234.8 | +13.5 | FAIL |
| | Close | 10,265.32 | 10,293.6 (full-day 10,352.4) | −28.3 | FAIL (>15) |
| Tue 12 May | O/H/L/C | 10,233.56 / 10,286.57 / 10,226.50 / 10,247.00 | 10,190.5 / 10,250.3 / 10,145.9 / 10,250.1 | +43.1 / +36.3 / +80.6 / −3.1 | O, H, L FAIL; C ok |
| Mon 11 May | O/H/L/C | 10,221.05 / 10,295.40 / 10,210.80 / 10,269.10 | 10,254.8 / 10,284.2 / 10,221.9 / 10,264.1 | −33.8 / +11.2 / −11.1 / +5.0 | O FAIL; H, L marginal; C borderline |
| Fri 08 May | O/H/L/C | 10,196.32 / 10,260.80 / 10,184.20 / 10,221.05 | 10,189.8 / 10,271.7 / 10,174.8 / 10,222.4 | +6.5 / −10.9 / +9.4 / −1.4 | H marginal; rest ok |
| Thu 07 May | O/H/L/C | 10,277.40 / 10,295.00 / 10,235.10 / 10,261.87 | 10,451.2 / 10,451.2 / 10,277.5 / 10,282.6 | −173.8 / −156.2 / −42.4 / −20.7 | FAIL all |
| Wed 06 May | O/H/L/C | 10,272.81 / 10,330.40 / 10,251.20 / 10,277.40 | 10,336.0 / 10,491.8 / 10,321.9 / 10,442.3 | −63.2 / −161.4 / −70.7 / −164.9 | FAIL all |

RSI2 from the report's own closes (10,277.40, 10,261.87, 10,221.05, 10,269.10, 10,247.00, 10,265.32), simple 2-period mean, via `--closes`:

| Date | Report RSI2 | Recomputed | Δ |
|---|---|---|---|
| 08 May | 27.6 | 0.0 | +27.6 |
| 11 May | 62.1 | 54.1 | +8.0 |
| 12 May | 44.7 | 68.5 | −23.8 (a +48.05 then −22.10 sequence cannot give <50) |
| 13 May | 52.3 | 45.3 | +7.0 |
| (06–07 May) | 62.4 / 48.9 | not testable (need earlier closes) | — |

Level file D-1 RSI2: cash 75.65, full 100.0 vs report 52.3.

ATR14: report ≈ 78 vs level file 136.59 (cash) / 145.41 (full): −43%.

Daily pivots (report vs level file `d_cash_*`; the report's own stated H/L/C give P 10,284.9, R1 10,321.6, S1 10,228.7, R2 10,377.8, S2 10,192.0):

| Level | Report | Level file cash | Δ |
|---|---|---|---|
| R3 | 10,418 | 10,477.7 | −59.7 |
| R2 | 10,376 | 10,417.3 | −41.3 |
| R1 | 10,335 | 10,355.5 | −20.5 |
| P | 10,285 | 10,295.1 | −10.1 |
| S1 | 10,242 | 10,233.3 | +8.7 |
| S2 | 10,194 | 10,172.9 | +21.1 |
| S3 | 10,151 | 10,111.1 | +39.9 |

Weekly pivots (report vs `w_cash_*`, W19): P 10,245 vs 10,292.3 (−47.3); R1 10,318 vs 10,421.9 (−103.9); R2 10,393 vs 10,621.3 (−228.3); R3 10,531 vs 10,750.9 (−219.9); S1 10,173 vs 10,092.9 (+80.1); S2 10,098 vs 9,963.3 (+134.7); S3 9,960 vs 9,763.9 (+196.1). The report's weekly H/L (10,330.40 / 10,184.20, range 146) omits the 7 May highs; level file weekly R1−S1 = 329.

Monthly pivots (report vs `m_cash_*`, 2026-04): P 10,257 vs 10,418.8 (−161.8); R1 10,473 vs 10,650.0 (−177.0); R2 10,617 vs 10,928.7 (−311.7); R3 10,889 vs 11,159.9 (−270.9); S1 10,041 vs 10,140.1 (−99.1); S2 9,785 vs 9,908.9 (−123.9); S3 9,513 vs 9,630.2 (−117.2). Report's April H/L/C (10,457 / 9,985 / 10,330) gives a range of 472; the level file's April range (R1−S1) is 509.9. The "late-April peak 10,457" matches the level file's 7 May 5-day swing high (10,451.2 cash), not April; the 25-day cash swing high is 10,697.5 (08 Apr), low 10,145.9 (12 May) vs the report's 25-day 10,184–10,457.

Counters (slice, UTC days): USDX D-1 close 98.478 (report ≈98.6); US500 D-1 close 7,458.5, +0.74% on the day (report −0.16% at 7,400.96); VIX D-1 close 19.34, +1.6% (report 17.99, −2.1%).

## 3. Citation spot-checks (row 3.2)

1. Yahoo Finance ^FTSE, 13 May: "10,265.32 (−0.04%)". The report's own §6 12 May close is 10,247.00, which makes the 13 May change +0.18%. A −0.04% change implies a prior close of about 10,269 (the 11 May close). Self-contradictory.
2. Trading Economics, 13 May: §4 quotes "10,325 CFD basis (+0.58%)" and §13a quotes "closes +32 pts (+0.31%) at 10,297" for the same source and day. Two incompatible closes; neither equals the 10,265.32 the report "normalizes" to. §13a's +32 / 10,297 also implies a prior close of 10,265, not the 10,247 in §6.
3. Yahoo Finance ^STOXX50E, "12 May 2026 18:00 CET ... Zurich cash close": the Euro Stoxx 50 cash close is not a Zurich print — impossible location; and the row is labelled "prior-day reference" while §6/§1 treat 5,808.45 as the 12 May close.
4. (Extra) Investing.com UK 100 "Open 10,318.66 / Close ~10,268" vs §6 13 May open 10,253.40 — same-day open differs by 65 pts inside the same report; "Bloomberg consensus ... 10,265 area" is not a price source.
Also: four providers (FTSE Russell, LSE, Yahoo, Bloomberg) are all quoted with the identical 16:35 close while the report's own Sharecast and TE items show ~10,297–10,301.

## 4. Category roll-up

| Cat | Level | Multiplier | Points | Justification |
|---|---|---|---|---|
| 1 Prompt adherence (20) | 2 | 0.40 | 8.0 | Row mean 3.33 -> 3, reduced one level for the 5.4 restriction breach (module codes, variable token, prompt-mechanics line, synthesised CFD "cash equivalent"). |
| 2 Structure (20) | 3 | 0.65 | 13.0 | All 21 sections present and ordered; §6 table missing Trend/Final/Validation; §7 prose only; §9 regime label self-contradicts; §21c day labels wrong. |
| 3 Accuracy & evidence (25) | 0 | 0.00 | 0.0 | Override: self-contradictory/impossible citations (row 3.2 = 0). Without the override the row mean (2,0,1,2 = 1.25) would give level 1. D-1 close off by 28 pts, RSI2 not reproducible, pivots off by 10–312 pts. |
| 4 Reasoning (20) | 3 | 0.65 | 13.0 | Row mean (3,2,2,4,2 = 2.6) -> 3. Cross-asset read built on wrongly-signed S&P/VIX; regime tension unresolved; card construction defects (4.5). |
| 5 Currency & transparency (15) | 2 | 0.40 | 6.0 | Row mean (3,3,2,1 = 2.25) -> 2. Wrong event carried into collision caveats; restriction breach; no single-source flag despite contradictions. |

## 5. Total, band, override

- Total = 8.0 + 13.0 + 0.0 + 13.0 + 6.0 = 40 -> band Low (40–59).
- Override check: hallucinated-source override TRIGGERED (cap Low, C3 = 0). Restriction-breach override ALSO triggered (cap Moderate, C1 −1 applied); the Low cap is the binding one. Recorded as `override=hallucinated_source`.
- Without any override the arithmetic would be C1 3 (12.0) + C2 3 + C3 1 (5.0) + C4 3 + C5 2 = 12+13+5+13+6 = 49 — still Low.

## 6. Card Integrity (linter rows copied verbatim from `qa/ftse_qa1/lint_static/2026-05-14.csv`)

| card_id | report_date | strategy | flags | dud | per-card score |
|---|---|---|---|---|---|
| 2026-05-14_Trade_1 | 2026-05-14 | Trade 1 - Daily Directional | SUPPRESSED | False | excluded |
| 2026-05-14_Trade_2 | 2026-05-14 | Trade 2 - Pivot (regime-aware, RANGE) | CLEAN | False | 100 |
| 2026-05-14_Trade_3B | 2026-05-14 | Trade 3B - Mean-Reversion (RANGE branch) | CLEAN | False | 100 |

card_integrity = mean over the 2 non-suppressed cards = 100.0 · n_cards = 3 (1 suppressed) · n_duds = 0 · n_warns = 0.

Reviewer note (not a linter re-run, not in the integrity number): the static linter does not test the 0.2R protective-stop side or the level-file ATR; the construction defects in rows 4.5 and in the feedback file are scored under Category 4 only.
