# Trust Score v3.7 — FTSE 100 daily report, D = 2026-07-31 (run ftse_qa1)

Report: `reports/md/FTSE_EuroStoxx_Report_31Jul2026.md`
Level file check: `last_bar_date` = 2026-07-30 < D (leak-free). Slice last bar 2026-07-30 22:45 broker. Basis the report claims: cash index, London session, so the `_cash` columns are the comparator (`_full` shown where useful).

## Machine-readable result

```
c1=3
c2=4
c3=0
c4=2
c5=3
total=48
band=Low
override=hallucinated_source
card_integrity=96.7
n_cards=3
n_duds=0
n_warns=1
```

Note on the override: C3 is forced to 0 and the band capped at Low (40-59) by the self-contradicted corroboration source in row 3.2. Without the override C3 would be level 2 (row mean 1.5, rounds to 2), total 58, which is still Low, so the band does not depend on the override call.

## 1. Section 7 checklist

| Row | Reviewer notes | Evidence observed | Score |
|---|---|---|---|
| 1.1 Variables respected | Asset (FTSE 100 cash), counters (USDX, S&P 500, DAX 40; Euro Stoxx as reference without cards), as-of 30 Jul London close, 5-session lookback, GBP/points, Trade 1 anchor 07:00 UK all respected. Weaknesses: the named sources are all media/aggregator/wire (Alliance News, AOL, LBC, BBN Times, Proactive, Sunday Guardian, Trading Economics, Yahoo, Investing.com, EBC/Reuters, Global Banking & Finance); none from the index-provider / exchange / sell-side tiers. Trade 2 and Trade 3A cards carry no anchor time. Daily pivots were built from the wrong session (see 3.4). | §2, §4, §10, §21b | 3 |
| 1.2 Coverage and currency consistent | Date drift: §13d lists "Thu 30 Jul (after close) US PCE / GDP + Apple & Amazon" as an UPCOMING event for 31 Jul-6 Aug, but the calendar slice shows Core PCE, PCE and GDP released 30 Jul 15:30 broker (13:30 London) with values populated; it belongs in §13c, not §13d. "Fri 1 Aug US ISM / jobs" is wrong: 1 Aug 2026 is a Saturday (31 Jul is the Friday). §11 daily pivots are from 29 Jul (D-2) although the report states a 30 Jul as-of. §12/§14 quote DXY ~100.7-100.9 while the USDX slice closes 30 Jul at 99.97 (29 Jul 100.82), so the dollar level is one session stale. Scheduled events for D itself are mostly missing (BoJ decision and press conference, China PMIs, Tokyo CPI, UK Nationwide HPI; only Eurozone flash CPI is listed). | §11, §12, §13c/d, §14 vs news and USDX slices | 2 |
| 1.3 Audience and tone | Strategist tone, trading and risk review, no retail language. Small blemishes: unresolved drafting residue in §11 narrative ("weekly R3 (10,923? — just under)") and a reference to "the instance restriction" in §5. | §1, §5, §11, §18 | 4 |
| 2.1 Sections present and ordered | §1-§21 all present in order, with §13a-d and §21a-d. §7 is five caption-only chart placeholders (accepted, pandoc drops images). §9 omits the KER numeric value and ATR(14); §11 shows R5..S5 (5 levels each side) instead of 3 each side. | headings | 4 |
| 2.2 Scorecard as a table | §6 is a table with Date/O/H/L/C/RSI2/Trend/Source A/Source B/Validation. No separate "Final" column (close is bolded). §11 pivots are tables but run R5 to S5 rather than R3 to S3. | §6, §11 | 4 |
| 2.3 Method steps visible | §4-§5 show observations, classification and consensus; §8 is candle-by-candle with a sequence assessment; §9 shows persistence 0.67, overlap 0.64, range position 0.85, VOLator slope. KER value and ATR(14) are not shown in §9. Range position 0.85 is consistent with the level file (0.84 on the cash 25-day range). | §4-§9 | 4 |
| 3.1 Quantitative claims sourced | §12 and §14 carry many bare figures with no source or section pointer: Brent "$90", "+~8%" spike, BoE 6-3 vote, Fed 3 dissents, Rentokil -21%, LSE -7%, DXY 101.5 to 100.7-100.9, 30-year yield ~5.2%, VIX 17-18, S&P +1.7%. §1 numbers largely point to §4/§6. | §1, §12, §14 | 2 |
| 3.2 Citations exist and contain the data | Three checked. (a) Alliance News 30 Jul close 10,897.27, -11.14 pts, -0.1%: arithmetically consistent with the 29 Jul close 10,908.41 (-0.102%). PASS. (b) Trading Economics 30 Jul 10,890 (-0.17%): consistent with a 29 Jul base of 10,908.41. PASS. (c) Investing.com is cited in §6 as Source B for the 24 Jul row, "CORROBORATED (Δ<0.1)", but §20 states the Investing.com historical table "returned a stale May-Jun window" plus a derived real-time widget "used for range context only". It cannot have supplied a 24 Jul OHLC corroboration. FAIL: self-contradictory source. Also: Sunday Guardian is Source B for the 27 Jul close, yet §4 has no 27 Jul evidence row and the Sunday Guardian only appears in §13a as a 30 Jul article; BBN Times is Source A for 24, 27, 28 and 29 Jul but §4 lists it only for 29 Jul; §20 lists the corroborated pairs as 30, 29 and 28 Jul only, so the 24 Jul and 27 Jul "CORROBORATED" labels have no recorded pair. Hallucinated-source override triggered. | §4, §6, §19, §20 | 0 |
| 3.3 Calculations transparent | RSI2 reproduces from the report's own closes: 28 Jul 100.0, 29 Jul 100.0, 30 Jul 77.0 (engine `--closes` check; 24 and 27 Jul need earlier closes and cannot be tested). Trend labels follow the rule. Pivot formulas reproduce exactly from the inputs used (P=(H+L+C)/3 from 29 Jul = 10,907.86), but the inputs are wrong (3.4). §21a sum reproduces: 0.25+0.20+0.05+0.116+0.045+0.15 = 0.811. ATR(14)=80.3 appears only in §20 and is wrong (level file 115.5 cash / 144.79 full). KER value never stated. §13b tilt arithmetic is wrong: it prints Σw·s ≈ 2.5 / Σw ≈ 3.9 ≈ +0.30, but 2.5/3.9 = 0.64. The +0.30 tilt feeds the §21a sentiment contribution (0.045). | §6, §9, §11, §13b, §20, §21a | 3 |
| 3.4 Numbers reconcile | Internally the 10,897 close is consistent across §1, §3, §4, §6 and §21b, and §11 pivots equal the pivots quoted on the cards. Against the data the report fails: the D-1 close is +20.9 pts from the cash slice close (threshold for a Category 3 failure is more than 15), the weekly pivots are not weekly (see §3 below), the daily pivots are D-2, ATR is 30% low, and the claimed "CORROBORATED" levels mostly sit outside the brief's tolerances. Internal breaks: Trade 1 R stated 52.7 vs entry-stop 52.41 vs entry-TP1 52.95; §21c/§21d backtest R-multiples are not reproducible from the stated entries and exits (see feedback item 13); §3 range 10,890-10,908 upper bound is the 29 Jul close, not a 30 Jul value. | whole report | 1 |
| 4.1 Pillars conclude | §8 ("Bullish continuation"), §9 (Bias Bullish, Trending), §10 (Aggregate CONFIRM) end in labels. §12 and §14 give per-paragraph tags but no single concluding direction label; §14 ends on a watch item. | §8-§14 | 3 |
| 4.2 Cross-asset interpreted | A mechanism is given, but its sign is wrong for a dollar-earner index. §1, §10, §12, §14, §15 and §17 treat a falling dollar as a translation tailwind for FTSE multinationals ("soft-dollar translation gains"). Dollar-denominated overseas earnings translate into fewer pounds when USD weakens, so a soft dollar (stronger sterling) is a translation headwind; the supportive channel is dollar-priced commodities, which the report covers separately. §10 even concedes "GBP strength is offset by the translation tailwind", which is contradictory. The +0.15 cross-asset signal in §21a rests on this. Direction of USDX (falling) and S&P (rising) over 5 days is correct against the slices. | §10, §14, §17, §21a | 2 |
| 4.3 Synthesis reconciles tensions | §15/§16/§18 do weigh record-high exhaustion (RSI2 100 to 77, upper-wick rejection) against the trend and carry the invalidation at the daily pivot. §16 invalidation mixes levels ("weekly R1 / daily S1 (~10,864-10,784)"). §11 narrative position text is garbled. Trade 1's thesis invalidation (10,907.86) sits above its own entry (10,897), contradicting the long thesis. | §11, §15-§18, §21b | 3 |
| 4.4 Calibrated language | §17 is exactly one sentence with a stated condition. Confidence "High" in §3/§18 is asserted on the basis of corroboration that §20 contradicts. | §3, §17, §18 | 3 |
| 4.5 Card construction (protocol: scored under Category 4) | Material M5 violations on all three cards: Trade 2 buy LIMIT 10,907.86 sits above the D-1 close; Trade 2 stop, TPs and invalidation not per the TREND branch; Trade 3A entry at 38.2% instead of 57.5%, stop not beyond the swing low, TPs shifted, wrong invalidation; Trade 1 stop built on a stale S1 and an ATR buffer from the wrong ATR; no R/ATR sanity print or wide-stop test on any card; no D-1 reference close with session date and signed gap on any card. Details in feedback. | §21b | 1 |
| 5.1 Data dated; staleness flagged | Prices and articles are dated; the single-source 27 Jul H/L and the CFD basis split are flagged. Not flagged: the PCE/GDP release already out (30 Jul), DXY stale by a session, daily pivots from D-2. | §4, §6, §13, §19 | 3 |
| 5.2 Assumptions up front | Monthly single-source flag propagated to §19 and to the Trade 2 caveat. Anchor stated on Trade 1 (07:00 UK) but absent on Trades 2 and 3A, and the basis assumption (cash vs the broker execution series) is not stated at the top. | §2, §19, §20, §21b | 3 |
| 5.3 Red flags surfaced | Exhaustion and the PCE/Apple/Amazon collision are carried into all three card caveats. The D-day BoJ decision/press conference, the China PMIs and the Eurozone flash CPI are not carried into card caveats. | §12, §15, §21b | 4 |
| 5.4 Restrictions honoured | No bracketed variable names, module codes or framework name seen; FTSE futures not used; STOXX has no card. Concerns: (i) the Open column on 27, 28 and 29 Jul equals the prior close plus about 0.1 (10,736.10 vs 10,736.23; 10,781.87 vs 10,781.75; 10,871.16 vs 10,871.02) while the slice shows real gaps (cash opens 10,803.7, 10,795.7, 10,895.9 against prior cash closes 10,728.0, 10,795.0, 10,874.0), which looks synthesised/interpolated yet is labelled CORROBORATED; (ii) 27 Jul H/L 10,800.00 and 10,730.00 are round placeholders (flagged single-source); (iii) the CFD-referenced Trading Economics quote supplies the lower bound of the consensus range (10,890). I treat these as a weakening of 5.4 and as supporting evidence for the 3.2 override, not as a separate restriction-breach override because the synthesis cannot be proven from the supplied material. | §3, §5, §6 | 2 |

## 2. Category roll-up

| Cat | Max | Rows | Mean | Level | Multiplier | Points | Justification |
|---|---|---|---|---|---|---|---|
| C1 Prompt adherence | 20 | 3, 2, 4 | 3.00 | 3 | 0.65 | 13.00 | Core variables respected; source tiers, date drift in the calendar and the wrong-session pivots are visible weaknesses. |
| C2 Structure | 20 | 4, 4, 4 | 4.00 | 4 | 0.85 | 17.00 | All sections present and ordered; minor format deviations (R5..S5, no Final column, no KER/ATR in §9). |
| C3 Accuracy and evidence | 25 | 2, 0, 3, 1 | 1.50 | 0 (override) | 0.00 | 0.00 | Hallucinated-source override: Investing.com cited as 24 Jul corroborator but self-reported as unusable. Underlying accuracy is also poor (close +20.9, weekly pivots not weekly, ATR 30% low). |
| C4 Reasoning and judgment | 20 | 3, 2, 3, 3, 1 | 2.40 | 2 | 0.40 | 8.00 | Dollar-translation mechanism has the wrong sign; card construction fails multiple M5 rules. |
| C5 Currency and transparency | 15 | 3, 3, 4, 2 | 3.00 | 3 | 0.65 | 9.75 | Dated and mostly transparent; stale calendar and dollar levels, probable synthesised opens. |

## 3. Total, band, override

- Total = 13.00 + 17.00 + 0.00 + 8.00 + 9.75 = 47.75, rounded to **48**.
- Band: **Low** (40-59).
- Override check: hallucinated-source override triggered (row 3.2), cap Low, C3 = 0. Restriction-breach override: not applied (synthesised opens suspected but not provable from the permitted material).

### Category 3 data comparison (report vs `UK100_by_date/2026-07-31.csv` and slice, cash basis)

Tolerances from brief §4: close |Δ| <= 5, open/high/low |Δ| <= 10; close error > 15 or non-reproducible RSI2 is a Category 3 failure.

| Session | Field | Report | Slice (cash) | Δ | Within tolerance |
|---|---|---|---|---|---|
| 30 Jul (D-1) | Open | 10,869.50 | 10,867.5 | +2.0 | yes |
| 30 Jul | High | 10,979.60 | 10,969.3 | +10.3 | marginal no |
| 30 Jul | Low | 10,851.50 | 10,836.2 | +15.3 | no |
| 30 Jul | Close | 10,897.27 | 10,876.4 | +20.9 | no (> 15, failure) |
| 30 Jul | RSI2 | 77.0 | 54.76 (cash) / 59.47 (full) | +22.2 | no (arithmetic from own closes reproduces) |
| 30 Jul | ATR(14) | 80.3 (§20) | 115.5 (cash) / 144.79 (full) | -35.2 | no |
| 29 Jul | O / H / L / C | 10,871.16 / 10,951.06 / 10,864.11 / 10,908.41 | 10,895.9 / 10,945.6 / 10,855.2 / 10,887.8 | -24.7 / +5.5 / +8.9 / +20.6 | O no, H yes, L yes, C no (> 15) |
| 28 Jul | O / H / L / C | 10,781.87 / 10,884.32 / 10,770.29 / 10,871.02 | 10,795.7 / 10,878.7 / 10,762.8 / 10,874.0 | -13.8 / +5.6 / +7.5 / -3.0 | O no, H yes, L yes, C yes |
| 27 Jul | O / H / L / C | 10,736.10 / 10,800.00 / 10,730.00 / 10,781.75 | 10,803.7 / 10,816.3 / 10,747.1 / 10,795.0 | -67.6 / -16.3 / -17.1 / -13.3 | all no (close just under the 15 mark but above 5) |
| 24 Jul | O / H / L / C | 10,638.86 / 10,738.83 / 10,599.10 / 10,736.23 | 10,582.2 / 10,728.2 / 10,580.9 / 10,728.0 | +56.7 / +10.6 / +18.2 / +8.2 | all no |

Pattern: 4 of 5 closes outside the 5-pt tolerance (two beyond 15); 4 of 5 opens outside 10 pts; the 27-29 Jul opens equal the prior close within 0.14 pt.

Daily pivots (report §11 vs level file `d_cash_*`):

| Level | Report | Level file | Δ |
|---|---|---|---|
| R3 | 11,038.56 | 11,084.83 | -46.3 |
| R2 | 10,994.81 | 11,027.07 | -32.3 |
| R1 | 10,951.61 | 10,951.73 | -0.1 (coincidence) |
| P | 10,907.86 | 10,893.97 | +13.9 |
| S1 | 10,864.66 | 10,818.63 | +46.0 |
| S2 | 10,820.91 | 10,760.87 | +60.0 |
| S3 | 10,777.71 | 10,685.53 | +92.2 |

Cause: the report states "from 29 Jul H/L/C" (10,951.06 / 10,864.11 / 10,908.41 reproduces P exactly). The D-1 session is 30 Jul. Even on the report's own 30 Jul row the pivots would be P 10,909.46, R1 10,967.41, S1 10,839.31.

Weekly pivots (report §11 vs `w_cash_*`, prior week 20-24 Jul):

| Level | Report | Level file | Δ |
|---|---|---|---|
| R3 | 10,923.40 | 11,123.37 | -200.0 |
| R2 | 10,831.12 | 10,941.13 | -110.0 |
| R1 | 10,783.67 | 10,834.57 | -50.9 |
| P | 10,691.39 | 10,652.33 | +39.1 |
| S1 | 10,643.94 | 10,545.77 | +98.2 |
| S2 | 10,551.66 | 10,363.53 | +188.1 |
| S3 | 10,504.21 | 10,256.97 | +247.2 |

Cause: the report's "weekly" P 10,691.39 reproduces exactly as (10,738.83 + 10,599.10 + 10,736.23)/3, i.e. the single-day 24 Jul H/L/C, and R2 - S2 = 279.46 = 2 x the 24 Jul day range (139.73). The true week range is 288.8 pts (cash 10,758.9 high, 10,470.1 low, 10,728.0 close). These are daily-of-Friday pivots mislabelled as weekly and labelled CORROBORATED.

Monthly pivots (report §11 vs `m_cash_*`, June 2026; report flags these single-source indicative): P 10,533.33 vs 10,412.17 (+121.2); R1 10,596.67 vs 10,698.13 (-101.5); S1 10,426.67 vs 10,215.53 (+211.1); R2 10,703.33 vs 10,894.77 (-191.4); S2 10,363.33 vs 9,929.57 (+433.8); R3 10,766.67 vs 11,180.73 (-414.1); S3 10,256.67 vs 9,732.93 (+523.7). The implied monthly range (170) is about one third of the level-file range (482.6).

Other checks: the 25-day range position 0.85 agrees with the level file (0.84). RSI2 sequence from the report's closes reproduces for 28/29/30 Jul. USDX falling and S&P rising over 5 days agree with the slices; VIX 17-18 agrees (18.02 at the last bar). DAX cannot be checked (no slice).

## 4. Card Integrity (linter rows, copied verbatim from `qa/ftse_qa1/lint_static/2026-07-31.csv`)

| card_id | report_date | strategy | flags | dud | Card Integrity |
|---|---|---|---|---|---|
| 2026-07-31_Trade_1 | 2026-07-31 | Trade 1 — Daily Directional (LONG · TREND_UP regime) | CLEAN | False | 100 |
| 2026-07-31_Trade_2 | 2026-07-31 | Trade 2 — Pivot (regime-aware · TREND_UP → pullback buy) | WARN_TP3_ORDER | False | 90 |
| 2026-07-31_Trade_3A | 2026-07-31 | Trade 3A — Momentum-Pullback (TREND_UP variant) | CLEAN | False | 100 |

n_cards=3 (none suppressed), n_duds=0, n_warns=1. Report-level Card Integrity = mean(100, 90, 100) = **96.7**. This is separate from the 100-point score; the linter is static and checks geometry only, so it does not capture the M5 rule defects listed in feedback (for example the wrong-side Trade 2 limit and the Trade 3A entry fraction).

## 5. Feedback

See `qa/ftse_qa1/2026-07-31_feedback.md`.
