# Trust Score v3.7 QA — FTSE 100 report dated 3 June 2026 (run ftse_qa1)

Report: `reports/md/FTSE_EuroStoxx_Report_03Jun2026.md` · D = 2026-06-03 · D-1 = 2026-06-02
Reference data: `data/levels/UK100_by_date/2026-06-03.csv` (`last_bar_date` = 2026-06-02 < D, checked) and `engine/qa_slice_stats.py --cash-open 10:00 --cash-close 18:30` (slice ends 2026-06-02 22:45 broker). The report claims a **cash index** basis, so the `_cash` columns are the primary comparison; `_full` is shown where it changes the verdict. Scratch in `/tmp/claude-0/qa_2026-06-03/`.

## Result lines
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

| Row | Reviewer notes | Evidence (location) | Score |
|---|---|---|---|
| 1.1 Variables respected | Asset (FTSE 100 cash) and counters (USDX, S&P 500, DAX 40, Euro Stoxx 50; VIX in §14) correct; GBP / index points; no futures used. **As-of is 1 Jun, not D-1 = 2 Jun** (the 2 Jun session is never reported, though §11, §4 Yahoo row and the §20 timestamp all know about 2 Jun). Source list has 6 names but all are media/aggregators (Trading Economics, Sharecast, Investing.com, "Twelfth Magpie", Yahoo, CNBC): none from index provider / exchange / sell-side tier. Daily-open anchor is 00:00 UK, not the 07:00 UK required for Trade 1 (deviation, disclosed in §20 only). | header, §2, §4, §20 | 2 |
| 1.2 Coverage & currency consistent | Whole report keyed to the 1 Jun close (10,324) while the forward session is 3 Jun; true D-1 cash close is 10,375.6 (+51.1 vs 1 Jun). Internal drift: §11 says "prior day 2 Jun" but §1/§3/§6/§21 use 1 Jun; §21c labels 1 Jun as t-1 although the session is 3 Jun; §4 calls 2 Jun Yahoo data "next-day". §13c row "25 May … FTSE firm": 25 May was a UK bank holiday, no LSE session. §2 promises "GBP-equivalent noted" for Stoxx; none given. | header, §1, §3, §6, §11, §13c, §21c | 2 |
| 1.3 Audience & tone | Strategist register, trading/risk use. Minor leakage of internal vocabulary ("v2.1 defaults", "weight-lock", "DAILY_OPEN_ANCHOR", "regime fork → 3A"). | §1, §18, §20, §21b | 4 |
| 2.1 Sections present & ordered | §1–§21 all present and in order; §13a–d and §21a–d present; §17 present. §7 shows chart headings only (images dropped by conversion; accepted as placeholders). | headings | 5 |
| 2.2 Scorecard as a table | §6 is a table but: no 2 Jun row, RSI2 blank for 26/27 May, no distinct Final/Validation columns (one "Outcome"). §11 has daily and weekly pivot tables (R3→S3, 3 each side) but **no monthly pivot table**. | §6, §11 | 3 |
| 2.3 Method steps visible | §4→§5 observation/consensus and §8 candle-by-candle + sequence present. §9 regime is qualitative only: no persistence/overlap values, no KER number, no ATR(14) figure; VOLator given as "~" values. | §4–§9 | 3 |
| 3.1 Quantitative claims sourced | §14 states BoE 3.75%, UK CPI ~3.4%, GBP/USD 1.33–1.34, "hawkish Fed pricing" with no source; §13d "ISM Mfg 54 (4-yr high)" unsourced and does not reconcile with the calendar slice (ISM Manufacturing PMI consensus 50.3, previous 52.7; S&P Global Mfg PMI actual 55.1). §12 sourced only generically ("CNBC/Trading Economics market reports"). §1 numbers mostly point back to §4/§6. | §12, §13d, §14 | 2 |
| 3.2 Citations exist & contain data | Three checked. (a) Trading Economics 1 Jun 10,324 (−0.82%, "85 points"): consistent (10,409.28 − 85 = 10,324.3; −0.82% ✓). (b) Investing.com 29 May 10,409.28, "day range to 10,462.22": consistent with §6 high 10,462 and slice 29 May cash high 10,462.0, close 10,410.0. (c) CNBC 1 Jun "day low 10,333": conflicts with the report's own 1 Jun close (10,324) and low (10,301) — a day low above the close is impossible as a final figure; at best an intraday print, but §6/§8 use it as a corroborating source. Also Reuters 29 May "Dollar rises" and §13c 29 May "Dollar up": USDX slice shows 29 May close 98.956 vs 99.023 prior (down). Goldman ("~late May") and AJ Bell ("early 2026") are undated. No source is demonstrably fabricated, so override not triggered; (c) and the Reuters headline need human verification. | §4, §6, §13a, §13c | 3 |
| 3.3 Calculations transparent | RSI2 "~0" for 28 May/29 May/1 Jun **reproduces** from the report's own closes (10,505, 10,498, 10,421, 10,409, 10,324 → 0.0, 0.0, 0.0 per `--closes`) but no gains/losses are shown and 26/27 May are blank. ATR(14) and KER(13, EMA3) are never stated numerically (card implies ATR=95; slice ATR14 = 114.64 cash / 135.36 full). Daily-pivot inputs (2 Jun H/L/C) are not shown anywhere (implied H≈10,395, L≈10,300, C≈10,373). §21a score reproduces: 0.25(−0.8)+0.20(−0.4)+0.10(−0.3)+0.15(−0.4)+0.15(+0.02)+0.15(−0.2) = −0.397 ≈ −0.40 ✓. §13b tilt +0.02 has no weights shown. §21c/§21d R-multiples not reproducible (see 3.4). | §6, §9, §11, §13b, §21 | 2 |
| 3.4 Numbers reconcile | Within-report: 10,324 consistent in §1/§3/§4/§6/§21; weekly P 10,442, daily S1 10,317, daily S3 10,222, weekly S3 10,130 on cards match §11. Against data: see Category 3 comparison below — D-1 close wrong by −51.6 vs the true D-1 (10,375.6); opens wrong by up to 64 pts, highs by up to 65, ATR 95 vs 114.6. §21d "TP1 hit rate 33%" but no §21c outcome reaches +1R (0.5R, 0.4R, 0.6R open); §21c Trade 3A "10,470→10,324 = +1.2R" is 146 pts against a 58-pt card R (2.5R), and 10,324 is a mark-to-market, not an exit. §21a "three highest-weighted" signals omit KER (−0.06) in favour of cross-asset (−0.03). | cross-section | 1 |
| 4.1 Pillars conclude | §8 "Bearish continuation", §9 "Transitional bearish tilt", §10 "MIXED". §12 and §14 end in a watch item / tags (Cyclical/Structural) rather than a direction label. | §8–§14 | 3 |
| 4.2 Cross-asset interpreted | Mechanisms stated (USD translation vs risk-off, common-factor beta, European risk premium) and the S&P divergence is not resolved away. But USDX called "Rising" when the slice shows 26 May 99.144 → 2 Jun 99.220 (flat); oil/Brent is discussed in §12/§14 but absent from the §10 table; S&P mechanism generic. | §10 | 3 |
| 4.3 Synthesis reconciles tensions | §13b, §15, §16 address sentiment-vs-price, S&P divergence and oil two-way risk. Unreconciled: §9 regime is Transitional yet Trade 3A is the trend family ("regime fork → 3A") and Trade 2 is a fade rather than the breakout-only transition rule; "bearish continuation" narrative is blind to the 2 Jun session. | §9, §15, §16, §21b | 3 |
| 4.4 Calibrated language | §17 is exactly one sentence, no hedge stack; confidence Medium stated in §3/§18. | §3, §17, §18 | 4 |
| 4.5 Card construction (protocol: scored under C4) | Multiple M5 departures on all three cards (market-at-anchor not used, no 0.25×ATR stop buffers, BE-stop sign error, wrong fib entry level, regime/family mismatch, 3A swing below 2×ATR, 3A sell-limit on the wrong side of the true D-1 close). Detail in feedback. Linter CLEAN is static only. | §21b | 2 |
| 5.1 Data dated; staleness flagged | Most data points dated; single-source O/H/L flagged with asterisks. Goldman and AJ Bell articles undated ("~late May", "early 2026"); report's own staleness (missing 2 Jun) not flagged. | §4, §6, §13a | 3 |
| 5.2 Assumptions up front | Lenient-corroboration authorisation and 00:00 anchor override disclosed in §5/§19/§20, but not on Trade 1's card (anchor) and not in §1. | §5, §19, §20, §21b | 3 |
| 5.3 Red flags surfaced | §12/§15 carry oil, ECB and defence risks. Event collisions in card caveats are wrong/incomplete: Trade 1 cites "eurozone CPI" (flash CPI was published on 2 Jun) and omits the 3 Jun scheduled UK/EZ services PMIs, ADP, ISM services and EIA crude. | §13d, §21b | 3 |
| 5.4 Restrictions honoured | Pattern consistent with proxied opens: 27 May open (10,505) = 26 May close exactly; 28 May open (10,498) = 27 May close exactly, while true 28 May open gapped to 10,434.1 — while §19 asserts "No prices were synthesised". Internal tokens exposed (DAILY_OPEN_ANCHOR, v2.1, weight-lock). Corroboration "leniency" used to keep Trade 2 alive on indicative pivots (disclosed). No futures/CFD quotes, no framework name, no M-codes. | §6, §19, §20 | 3 |

## 2. Category 3 data comparison (report vs `qa_slice_stats` / level file)

D-1 per data = **2 Jun**. Report's "D-1" = 1 Jun.

| Field | Report | Slice (cash) | Δ (report − slice) | Verdict |
|---|---|---|---|---|
| D-1 (2 Jun) close | not reported; headline 10,324 | 10,375.6 (full 10,382.5) | −51.6 | FAIL (>15; stale as-of) |
| D-1 (2 Jun) O/H/L | not reported | 10,360.7 / 10,398.1 / 10,332.5 | n/a | missing |
| D-1 RSI2 | not reported (1 Jun "~0") | 37.41 (full 57.76) | n/a | missing |
| ATR14 | 95 (implied by "1×ATR") | 114.64 (full 135.36) | −19.6 / −40.4 | discrepancy |
| 26 May O/H/L/C | 10,472 / 10,520 / 10,448 / 10,505 | 10,531.9 / 10,560.0 / 10,498.0 / 10,500.7 | −59.9 / −40.0 / −50.0 / +4.3 | O,H,L out |
| 27 May O/H/L/C | 10,505 / 10,548 / 10,470 / 10,498 | 10,487.7 / 10,523.5 / 10,460.6 / 10,507.9 | +17.3 / +24.5 / +9.4 / −9.9 | O,H,C out |
| 28 May O/H/L/C | 10,498 / 10,512 / 10,380 / 10,421 | 10,434.1 / 10,446.6 / 10,378.8 / 10,432.4 | +63.9 / +65.4 / +1.2 / −11.4 | O,H,C out |
| 29 May O/H/L/C | 10,430 / 10,462 / 10,360 / 10,409 | 10,434.7 / 10,462.0 / 10,409.2 / 10,410.0 | −4.7 / 0.0 / −49.2 / −1.0 | L out on cash (full-day low 10,367.6: −7.6, i.e. an overnight low) |
| 1 Jun O/H/L/C | 10,405 / 10,412 / 10,301 / 10,324 | 10,371.9 / 10,410.4 / 10,286.2 / 10,324.5 | +33.1 / +1.6 / +14.8 / −0.5 | O,L out; close good |
| RSI2 28/29 May, 1 Jun | ~0 / ~0 / ~0 | 8.71 / 0.00 / 0.00 | arithmetic OK from own closes | pass on reproducibility |
| Candle descriptions | 26 May "close near the high"; 28 May "close in lower third" | 26 May close 10,500.7 vs range 10,498.0–10,560.0 (bottom of range, close < open); 28 May close at 79% of 10,378.8–10,446.6 (upper part) | n/a | narrative contradicts slice |

Daily pivots (report states "prior day 2 Jun", basis unstated) vs level file:

| Level | Report | `_cash` | Δ cash | `_full` | Δ full |
|---|---|---|---|---|---|
| R3 | 10,507 | 10,470.6 | +36.4 | 10,519.7 | −12.7 |
| R2 | 10,451 | 10,434.3 | +16.7 | 10,458.9 | −7.9 |
| R1 | 10,412 | 10,405.0 | +7.0 | 10,420.7 | −8.7 |
| P | 10,356 | 10,368.7 | −12.7 | 10,359.9 | −3.9 |
| S1 | 10,317 | 10,339.4 | −22.4 | 10,321.7 | −4.7 |
| S2 | 10,261 | 10,303.1 | −42.1 | 10,260.9 | +0.1 |
| S3 | 10,222 | 10,273.8 | −51.8 | 10,222.7 | −0.7 |

The daily pivots track the full-day (24h) basis, not the cash basis the report claims. Pivots are internally consistent (R2 = P + (H−L), etc. with implied H≈10,395/L≈10,300), but inputs are not shown and §6 contains no 2 Jun row.

Weekly pivots (W22 = 26–29 May, correct period) vs level file:

| Level | Report | `_cash` | Δ cash | `_full` | Δ full |
|---|---|---|---|---|---|
| R3 | 10,722 | 10,701.6 | +20.4 | 10,688.7 | +33.3 |
| R2 | 10,639 | 10,630.8 | +8.2 | 10,624.3 | +14.7 |
| R1 | 10,524 | 10,520.4 | +3.6 | 10,496.3 | +27.7 |
| P | 10,442 | 10,449.6 | −7.6 | 10,431.9 | +10.1 |
| S1 | 10,327 | 10,339.2 | −12.2 | 10,303.9 | +23.1 |
| S2 | 10,245 | 10,268.4 | −23.4 | 10,239.5 | +5.5 |
| S3 | 10,130 | 10,158.0 | −28.0 | 10,111.5 | +18.5 |

Implied weekly inputs H≈10,557 / L≈10,360 / C≈10,409 mix bases (high ≈ 10,560 either basis; low ≈ full-day; close ≈ cash). Monthly pivots (May, `m_cash`: P 10,370.4, R1 10,599.6, S1 10,180.8, R2 10,789.2, S2 9,951.6, R3 11,018.4, S3 9,762.0) are absent from §11.

Counters (slice): USDX 26 May 99.144 → 2 Jun 99.220 (flat, "Rising" overstated; "above 99" ✓); US500 record 7,621.3 on 2 Jun ✓; VIX 16.85 on 2 Jun ✓ ("~16–17"). Calendar: Eurozone flash CPI y/y printed 2.6% on 2 Jun (consensus 2.6, previous 3.0) — §13d lists it as upcoming; 3 Jun scheduled items missing from §13d (UK/EZ services PMIs, Elderson speech, ADP, US services PMI/ISM services, EIA crude, Beige Book).

## 3. Category roll-up

| Cat | Level | Multiplier | Points | Justification |
|---|---|---|---|---|
| C1 Prompt adherence (max 20) | 3 | 0.65 | 13.00 | Right asset and counters, but as-of is a session stale, anchor is 00:00 not 07:00, no index-provider/exchange/sell-side sources. Rows 2/2/4. |
| C2 Structure (max 20) | 4 | 0.85 | 17.00 | All 21 sections and sub-sections present and ordered; monthly pivots missing, §6 columns/RSI2 incomplete, §9 lacks numbers. Rows 5/3/3. |
| C3 Accuracy & evidence (max 25) | 2 | 0.40 | 10.00 | Headline close stale by 51.6 pts vs true D-1; opens/highs off by up to 65 pts; ATR, KER absent; backtest figures irreconcilable; some unsourced §14 numbers. Citations (a)/(b) check out, (c) conflicts. Rows 2/3/2/1. |
| C4 Reasoning & judgment (max 20) | 3 | 0.65 | 13.00 | Pillars conclude and §17/§21a are coherent, but card construction is poor and regime/family mismatched. Rows 3/3/3/4 + card 2. |
| C5 Currency & transparency (max 15) | 3 | 0.65 | 9.75 | Single-source flags and one-sentence forecast good; anchor caveat off the card, undated articles, open-equals-prior-close pattern vs "no synthesis" claim, wrong event collisions. Rows 3/3/3/3. |

Sum = 62.75 → **total 63**.

## 4. Total, band, override
- Total = 63 → band **Moderate (60–74)**.
- Hallucinated-source override: not triggered (sources a/b verified consistent; CNBC "day low 10,333" and Reuters "Dollar rises" flagged for human verification but not demonstrably fabricated).
- Restriction-breach override: not triggered (00:00 anchor and corroboration leniency are disclosed as run-level instructions; the possible proxied opens are a pattern, not a proven breach).
- override=none

## 5. Card Integrity (linter rows copied verbatim from `qa/ftse_qa1/lint_static/2026-06-03.csv`)

| card_id | strategy | flags | dud | card score |
|---|---|---|---|---|
| 2026-06-03_Trade_1 | Trade 1 - Daily Directional (SHORT - bearish regime) | CLEAN | False | 100 |
| 2026-06-03_Trade_2 | Trade 2 - Pivot (regime-aware, SHORT-at-resistance) | CLEAN | False | 100 |
| 2026-06-03_Trade_3A | Trade 3A - Momentum-Pullback (SHORT) | CLEAN | False | 100 |

Report-level Card Integrity = 100 (3 cards, 0 DUD, 0 WARN, none suppressed). The linter is static and carries no market data, so market-relative defects (e.g. Trade 3A's sell limit at 10,357 sitting below the true D-1 close 10,375.6) are scored under C4 row 4.5 and listed in the feedback, not in this number. The Card Integrity figure is separate from the 100-point total.

## 6. Feedback
See `qa/ftse_qa1/2026-06-03_feedback.md`.
