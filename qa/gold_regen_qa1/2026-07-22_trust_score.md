# Trust Score — XAUUSD Gold Report, 22 Jul 2026 (`Gold_Report_22Jul2026.md`)
Run: gold_regen_qa1 · Reviewer basis: report claims spot/loco-London, continuous 24h quoting ("Spot, loco
London, immediate settlement", §3; "Global 24-hour market", §2) → checked against the `_full` columns of
`data/levels/XAUUSD_by_date/2026-07-22.csv` (`last_bar_date=2026-07-21 < 2026-07-22`, confirmed leak-free).

## 1. Section 7 checklist

| Row | Reviewer notes | Evidence observed | Score (0–5) |
|---|---|---|---|
| 1.1 Variables respected | Asset = XAU/USD spot loco London, GC=F corroboration-only ✓; USDX first counter in §10 ✓; as-of = 21 Jul (last completed session) ✓; lookback 5/25 ✓; USD/oz ✓; 6 named sources in §4 (minimum met) ✓; tick size used consistently ($0.01, implied by every ticks/USD conversion) but never spelled out as a definition. Anchor is named (07:00 UK) and its override from the 00:00 UK reset is logged correctly as a non-conformance — not silently presented as the instance value — in §2, §19 and §20 (§20: "anchor overridden to 07:00 UK per instruction"). But the same converted time is never carried onto either live card in §21b, contrary to the module's explicit three-place requirement (card / handoff / body). | §2, §10, §19, §20, §21b | 4 |
| 1.2 Coverage & currency consistent | D-1 close (~$4,066.74) used identically wherever quoted (§1, §3, §4, §6); no USD/oz unit drift; ticks appear only inside §21b and always convert back to USD/oz consistently. | whole report | 5 |
| 1.3 Audience & tone | Consistently institutional register ("Senior Commodities Analyst — Precious Metals"); no retail tone anywhere. | §1, header | 5 |
| 2.1 Sections present & ordered | §1–§21 all present in order, incl. §13a–d and §21a–d. | headings | 5 |
| 2.2 Scorecard as table | §6 is a proper 10-column table ✓. §11, however: the **Monthly pivot table is missing entirely** — only Daily and Weekly tables are printed, contrary to the M4 spec requiring daily/weekly/monthly. The Daily table that is present also prints 5 levels/side (R5…S5, 11 rows) instead of the specified 3-levels/side R3→P→S3 format; the Weekly table alone matches the specified 3-level format. | §11 | 2 |
| 2.3 Method steps visible | §4–§5 show observation→normalisation→consensus with the (non-)adjustment stated; §8 is candle-by-candle; §9 gives explicit overlap/persistence/VOLator/KER numbers; §7 charts present as captions (docx→md image drop, per brief, not scored). No unrendered template artifacts found (checked for `{...}` / bracketed-variable leakage — none). | §4–§9 | 5 |
| 3.1 Quantitative claims sourced | §1/§4/§6 figures are well sourced. But several §12/§14 quantitative claims carry no source or date at all: "US 10Y ~4.59%", "PBoC, RBI" central-bank buying, "gold-silver ratio breaking below ~69 from >70" — none is tied to a named/dated source or to §4/§6/§13 the way the gold OHLC figures are. Cross-asset levels in §10 (USDX ~100.6, S&P ~7,543, DAX ~24,840) are likewise stated without a source line. | §10, §12, §14 | 3 |
| 3.2 Citations exist & contain data | Spot-checked Investing.com (21 Jul), TradingEconomics (21 Jul), USAGOLD (21 Jul) — all named and dated. TradingEconomics' own "+1.86% on day" reproduces almost exactly from the report's own 20 Jul close (4,082.73/1.0186=4,008.30 vs stated 4,008.37). USAGOLD's own "+$51.43 (+1.28%)" implies a ~$4,015.31 baseline that does not match either tabulated prior close (4,008.37 or 4,016.69) — a minor, not impossible, provider-basis inconsistency, and the report already discloses elevated provider dispersion (§3) as the reason a strict two-source fix could not be reached. No source is self-contradictory to the fabrication threshold. | §4, §13a | 4 |
| 3.3 Calculations transparent | RSI2 (87.5) reproduces exactly from the report's own 5 closes (RS=29.185/4.16=7.016→RSI2=87.5 ✓). The daily-pivot arithmetic is mechanically correct: P=(4036.49+3996.64+4008.37)/3=4013.833 and every R/S level reproduces exactly from that P with the stated H/L — the formulas are transparent and correctly applied, only to the wrong input period (see 3.4). ATR(14)=$94.36 and KER≈−0.07 are both stated (§20/§9); §21a's score = Σ(signal×weight) sums exactly to +0.21 as printed. | §6, §9, §11, §20, §21a | 5 |
| 3.4 Numbers reconcile — incl. level file | Internally consistent (D-1 close identical across §1/§3/§4/§6; §11 pivots match the cards that cite them). **Externally, against the leak-free level file, this is the report's dominant failure:** (a) §11's header states the daily pivots are "from 20 Jul H/L/C" — i.e. D-2, not D-1 (21 Jul) as the report's own §2 as-of date requires. Reproducing the formula confirms it: P=4,013.83 matches 20 Jul's own H/L/C exactly, not 21 Jul's. Vs `d_full_P`=4,054.6933 the miss is 40.86 (0.47×ATR14); R1 misses by 78.61 (0.90×ATR14); R2 by 87.78 (1.0×ATR14); R3 by 125.53 (1.43×ATR14); S1 by 31.69 (0.36×ATR14); S3 by 15.23 (0.17×ATR14) — every daily level fails the 0.115×ATR14 threshold except S2 (Δ6.06, in-tolerance by luck). (b) Weekly pivots use the correct period (W/E 17 Jul matches `w_full_period`=2026-W29) but the levels still miss badly: R1 Δ14.65 (0.167×ATR, FAIL), R2 Δ29.11 (0.332×ATR, FAIL), R3 Δ38.76 (0.442×ATR, FAIL), S2 Δ19.11 (0.218×ATR, FAIL), S3 Δ33.57 (0.382×ATR, FAIL); only P (Δ5.00) and S1 (Δ9.46) stay inside the discrepancy band. (c) The 21 Jul close itself, used throughout §1/§3/§4/§6, is $4,066.74 vs `prev_close_full`=$4,077.81 — Δ11.07 = 0.126×ATR14, just over the 0.115×ATR14 (≈$10.09) failure threshold. O/H/L are all within tolerance (Δ1.65/2.39/0.08). ATR14 ($94.36 vs `atr14_full`=87.7621, 7.5% relative) and RSI2 are both within tolerance. Swing 5d low ($3,955 vs `swing_low_5d_full`=3,959.65, Δ4.65) is a recordable discrepancy, not a failure; swing 25d high/low match closely. The wrong-period daily pivots feed directly into Trade 2's tier selection (see Card feedback). | §6, §11 vs level file | 1 |
| 4.1 Each pillar concludes | §8 ends "Range (short-term bullish tilt)"; §9 ends "Consolidated regime label: RANGE"; §10 ends "Aggregate cross-asset read: MIXED" — all crisp. §12/§14 tag each bullet price-negative/-supportive inline but never roll up to one closing direction label for the section as a whole. | §8–§10, §12, §14 | 4 |
| 4.2 Peer/cross-asset interpreted | §10 states a mechanism for each counter (USD opportunity-cost, equity-risk-on vs haven demand, DAX as neutral barometer) rather than a bare correlation list. | §10 | 5 |
| 4.3 Synthesis reconciles tensions | §15's Balance line and §16 explicitly hold the short-/medium-term and cross-asset tensions open rather than averaging them away, and §21a flags the §17-vs-score conflict explicitly ("noted, not resolved"). But the synthesis never catches that Trade 2's R3 tier is not a valid RANGE-short tier under M5, or that its own TP3 sits on the wrong side of TP1 for a short — reasoning is not applied to the card outputs it produced. | §15–§18, §21a, §21b | 3 |
| 4.4 Calibrated language | §17 is exactly one sentence, no hedge stacking; confidence stated as Medium in §3. | §3, §17 | 5 |
| 5.1 Data dated; staleness flagged | Every price/article dated; §6/§19 explicitly flag the 16/17/20 Jul OHLC rows as single-source indicative. | §4, §6, §13, §19 | 5 |
| 5.2 Assumptions up front | Futures-to-spot non-adjustment stated with its rationale (§5). Single-source pivot propagation is correctly carried into both live cards' Caveats rows (§21b: "Single-source-indicative pivots (§19)" / "Single-source-indicative range boundaries (§19)"). But the anchor override, while logged compliantly in the report body and the §20 handoff record, is never carried onto either card as the module requires — no clock time appears on either card table at all. Separately, the §19 "single-source-indicative" caveat on the pivots describes source-count only; it does not disclose the more material defect that the daily pivots were built from the wrong (D-2) period — a different and more serious staleness that goes unflagged as such. | §19, §20, §21b | 3 |
| 5.3 Red flags surfaced | §12/§15 carry substantive risks (FOMC, real yields, de-escalation unwind); §13d's FOMC collision is explicitly carried into both live cards' Caveats rows. | §12, §15, §21b | 5 |
| 5.4 Restrictions honoured | No module codes, bracketed variable names, or framework name found in the body (checked). GC=F used corroboration-only, never as the priced basis. Instrument common names used throughout. | whole report | 5 |

## 2. Category roll-up

| Cat | Level (mean of rows, rounded) | Multiplier | Max | Points | Justification |
|---|---|---|---|---|---|
| C1 Prompt adherence | 5 | 1.00 | 20 | 20.00 | Mean of 4/5/5=4.67→5; all Variables respected, minor anchor-on-card gap the only blemish |
| C2 Structure | 4 | 0.85 | 20 | 17.00 | Mean of 5/2/5=4.0; sections all present and ordered, but the Monthly pivot table is missing outright and the Daily table's level-count doesn't match spec |
| C3 Accuracy & evidence | 3 | 0.65 | 25 | 16.25 | Mean of 3/4/5/1=3.25→3; RSI2 and formula transparency are excellent, but the daily pivots are built from the wrong (D-2) session, most weekly pivot levels miss tolerance, and the D-1 close itself narrowly fails tolerance |
| C4 Reasoning & judgment | 4 | 0.85 | 20 | 17.00 | Mean of 4/5/3/5=4.25→4; pillar conclusions and cross-asset mechanism are strong, but synthesis does not catch the card-construction rule violation it produced |
| C5 Currency & transparency | 4 | 0.85 | 15 | 12.75 | Mean of 5/3/5/5=4.5→4 (rounded down per framework guidance on ties); dating and red-flag surfacing are strong, anchor-on-card and pivot-staleness disclosure are the gaps |

## 3. Total, band, override

```
total = round(20.00+17.00+16.25+17.00+12.75) = 83
band  = High Trust (75-89)
override = none   (no fabricated/self-contradictory source found on spot-check; the anchor override is
                    logged as a non-conformance in the report body and handoff record, not silently
                    presented as the instance anchor, so no restriction-breach override applies)
```

## 4. Card Integrity (from `qa/gold_regen_qa1/lint_static/2026-07-22.csv`, copied verbatim)

| card_id | strategy | flags | dud | integrity (100−40·#DUD−10·#WARN) |
|---|---|---|---|---|
| 2026-07-22_Trade_1 | Trade 1 — Daily Directional | SUPPRESSED | False | excluded (suppressed) |
| 2026-07-22_Trade_2 | Trade 2 — Pivot (RANGE mean-reversion) | WARN_TP3_ORDER | False | 90 |
| 2026-07-22_Trade_3B | Trade 3 — Mean-Reversion (3B, RANGE) | CLEAN | False | 100 |

Report-level Card Integrity = mean over non-suppressed cards = mean(90, 100) = **95**.

Note for the regeneration agent: the static linter only checks stop/TP/side ordering, so it correctly
flags Trade 2's TP3 order and passes Trade 3B as clean. It cannot see the semantic M5-rule violations
below (Trade 2's tier choice, Trade 3B's stop-formula mislabel) — those must be fixed independently of
the Card Integrity number.

## 5. Explicit score lines

c1=5
c2=4
c3=3
c4=4
c5=4
total=83
band=High Trust (75-89)
override=none
card_integrity=95
n_cards=3
n_duds=0
n_warns=1
