# Trust Score — 2026-05-29 — SP500_Report_29May2026.md

Run: regen_20260906_qa1 · Asset US500 · D = 2026-05-29 · D-1 slice = `data/slices/US500/US500_upto_2026-05-28.csv`
Framework: `docs/AI_Output_Trust_Score_Framework_v3.7.txt` §4–§7, anchored by `qa/regen_20260906_qa1/REVIEWER_BRIEF.md`.

Helper basis (verbatim from `engine/qa_slice_stats.py`): D-1 cash close **7572.50**, ATR14 cash **69.38**,
daily pivots from D-1 cash P **7554.73** / R1 **7593.97** / S1 **7533.27** / R2 **7615.43** / S2 **7494.03** / R3 **7654.67** / S3 **7472.57**,
weekly pivots (prior week 18–22 May, cash) P **7441.33** / R1 **7543.57** / S1 **7373.47** / R2 **7611.43** / S2 **7271.23** / R3 **7713.67** / S3 **7203.37**,
5-day swing high **7576.20** (28 May) / low **7464.50** (22 May), 25-day swing low **7112.40** (29 Apr).

## 1. Section 7 checklist

| Item | Reviewer notes | Evidence observed | Score 0–5 | Action required |
|---|---|---|---|---|
| 1.1 Variables respected | Asset is the S&P 500 cash index (503 constituents), not ES futures; counters listed USDX · VIX · DAX 40 in the required order; as-of NY close of D-1 with America/New_York stated; 5-session lookback; index points / USD / tick 0.01; six named sources. **Fails on the daily-open anchor**: M1 fixes Trade 1 at the 07:00 UK daily open, and the report never states it — the Trade 1 card offers "market at NY open if gap-and-hold above 7,564", a different anchor (the extracted card carries `anchor_broker 09:00`, i.e. 07:00 UK, so report text and card metadata disagree). Source tiering is also thin: of six rows, three are media/aggregator (CNBC, Trading Economics, TheStreet/Motley Fool) and no exchange or sell-side tier appears. | §2 field table; §4 source table; §21b Trade 1 "Entry" row; `cards/baseline/by_date/2026-05-29.json` | 2 | State the 07:00 UK daily-open anchor explicitly on Trade 1 and remove the NY-open alternative; add at least one exchange/sell-side-tier source to §4. |
| 1.2 Coverage & currency consistent | No forward-dated data: every price and article is 28 May or earlier and the session is 29 May. No currency or unit drift (points/USD throughout). Two coverage defects: §13c is headed "Previous Period (21–28 May)" but its first row is dated **Mon 18 May**; and the 5-session window disagrees with the previous report — `SP500_Daily_Report_28May2026.md` states 21 May close **7,445.74** and RSI2 **80.6**, 22 May RSI2 **89.1**, 26 May RSI2 **94.4**, against **7,445.93 / 86.8 / 91.5 / 96.1** here. The 0.19 pt close difference exceeds the ±0.10 pt tolerance the report itself claims. Exclusion of 25 May as Memorial Day is correct — the slice's 25 May cash bars carry 4,217 ticks against 18–26k on ordinary days. | §2, §13c, §6; prior report `reports/md/SP500_Daily_Report_28May2026.md` §6 | 3 | Re-date the §13c header to cover 18–28 May or drop the 18 May row; reconcile the 21 May close and the RSI2 column against the prior report. |
| 1.3 Audience & tone | Consistently senior-strategist register: consensus/confidence framing, explicit contradiction flags, risk-review vocabulary, no retail promotion, "not investment advice" boilerplate retained. | §1, §18, §21d | 5 | None. |
| 2.1 Sections present & ordered | All of §1–§21 present in the mandated order, with §13a/b/c/d and §21a/b/c/d all present. §17 is a single sentence; §21d carries the limitations boilerplate verbatim. | Headings, whole report | 5 | None. |
| 2.2 Scorecard as a table | §6 is a table but is **missing the Final and Validation columns** — validation is prose beneath the table instead. §11 is worse: only a **weekly** table is given, it runs **R5→P→S5** (five levels a side, not the required three, and laid out in two side-by-side columns rather than R3→P→S3), the **daily pivots appear only as a prose sentence**, and the **monthly pivot table is absent entirely**. | §6 table header; §11 | 1 | Add Final + Validation columns to §6; replace §11 with three tables (daily, weekly, monthly), each R3→P→S3. |
| 2.3 Method steps visible | §4 lists observations with class and basis, §5 explains the weighted-median build and the exclusion decision, §8 is candle-by-candle plus a sequence assessment, §9 states regime with persistence / overlap / VOLator / KER. §7 charts survive as five captioned image placeholders (pandoc drops the raster) — accepted as evidence, noted. | §4–§9 | 5 | None (chart images are pandoc placeholders — noted, not penalised). |
| 3.1 Quantitative claims sourced | The close and the OHLC column trace to §4/§6. A large block of §9/§12/§14 numbers carries no source and appears nowhere in §4 or §13a: KER **0.663**, the four VOLator readings (−0.15/−0.10/−0.45/−0.05), "pullback to ~7,353" (§8), Snowflake **+30%**, Nvidia **−1%**, WTI **$88–90**, Russell 2000 **>2,900**, "~50% odds of a December hike". §13c also mis-characterises a checkable print: it calls 28 May jobless claims "firm" when the calendar has Initial Claims **215.0** against consensus **203.0** and previous **209.0** — claims rose and missed. | §8, §9, §12, §14; `data/slices/NEWS/news_upto_2026-05-28.csv` 2026-05-28 15:30 rows | 2 | Source or delete the unsourced §9/§12/§14 figures; correct the jobless-claims characterisation. |
| 3.2 Citations exist & contain data | Three spot-checks. **(a) S&P Dow Jones Indices, 28 May, 7,564.51** — internally consistent, used identically in §1/§3/§6/§18. **(b) FRED (St. Louis Fed)** — its §4 row is dated **27 May** quoting **7,520.36**, yet §5 says "FRED, CNBC and Yahoo independently reproduce it [the 28 May close] within the ±0.10-point tolerance" and §20 logs "28 May close corroborated (SPDJI × FRED/Yahoo/CNBC), **delta 0.00 pt**". On the report's own table that delta is **44.15 pt** on a different date — the corroboration claim is impossible against the cited row. **(c) Trading Economics, 28 May** — raw quote is the non-numeric phrase "record high", normalised to 7,564.51 and then counted in §1's "six independent sources place the close within a 0.10-point band"; a source with no numeric quote cannot sit inside a 0.10 pt band. The §13a Reuters survey row is additionally **undated** (date column "---") and its headline figure "~7,490 in 2026" is absent from its own derivation quote ("eight see higher odds of a near-term pullback"). | §4 rows 1/2/5; §5; §20 bullet 1; §1; §13a row 6 | 1 | Redate/replace the FRED row with a 28 May observation or withdraw the FRED corroboration claim in §5/§20; give Trading Economics a numeric quote or reclassify it out of the close consensus; date the Reuters row and align its headline to its quote. |
| 3.3 Calculations transparent | **RSI2 does not reproduce.** The report's five closes rise monotonically, so under the protocol formula (RS = mean gain / mean loss over 2 periods) the 26/27/28 May values are exactly **100.0 / 100.0 / 100.0**; the report states **96.1 / 96.2 / 98.7**. (Those figures are consistent with an undisclosed Wilder-smoothed variant, but the report never says which method it used, so they are not reproducible as specified.) Against the slice the same column reads 75.34 / 3.82 / 100.00 — confounded by the 25 May holiday bar the report legitimately excludes, so the decisive test is the report's own closes. **Weekly pivots do reproduce**: P 7,417.49 with R1 7,534.98 and S1 7,355.98 implies H 7,479.00 / L 7,300.00 / C 7,473.47, and R2/S2/R3/S3 and the non-standard R4/R5/S4/S5 all follow exactly. **Daily pivots do not**: §11 gives "first daily support ≈ 7,519, first daily resistance ≈ 7,569", but from the report's own D-1 H 7,569.00 / L 7,519.00 / C 7,564.51 the true levels are **S1 7,532.67** and **R1 7,582.67** — 7,519/7,569 are simply the D-1 low and high relabelled as pivots (P ≈ 7,551 is correct at 7,550.84). **ATR(14) is never stated numerically** — only implied at ≈44.7 by the "3×ATR cap (~+134 pts)" on Trade 1, against a slice ATR14 of 69.38. KER is given as ≈0.663 with no window or inputs. **§21a is not reproducible**: the listed contributions 0.25 + 0.20 + 0.15 + 0.05 + 0.15 = 0.80 with an unquantified "DAX drag" cannot be shown to yield **+0.46**, and the 0.05 sentiment term is not a member of the fixed 0.25/0.20/0.10/0.15/0.15/0.15 weight vector. Trend labels are the one clean item — all five follow the Close-vs-Open / RSI2-vs-50 rule given the stated RSI2. | §6 RSI2 column; §11; §9; §21a; §21b TP3 row | 1 | State the RSI2 method and recompute; replace the §11 daily S1/R1 with the computed values; state ATR(14) and KER(13, EMA 3) numerically in §9; show the §21a signal×weight arithmetic. |
| 3.4 Numbers reconcile | The D-1 close **7,564.51** is identical in §1, §3, §4, §6 and §18 — but it appears in **no card entry**, because Trade 1 was built as a limit rather than the required market-at-anchor. §11's daily P 7,551 does match the Trade 2 entry, yet the "daily S1" cited as the stop anchor on Trades 1 and 2 is **7,519**, which is not S1 under any basis (7,532.67 report-derived, 7,533.27 slice). ATR appears in §21b only (implied 44.7) and never in §9. §3's quoted range "7,519 – 7,569 (last 2 sessions)" contradicts §6, whose last two sessions span **7,499.70 – 7,569.00**. §1's "six independent sources … within a 0.10-point band" contradicts §4, which carries only three numeric 28 May quotes. §21c/§21d do reconcile internally (Trade 1 4/5 triggered, mean R 3.5/4 ≈ +0.9; Trade 2 3/3, mean +1.67 ≈ +1.7; Trade 3A 1/2, +1.4; the open t−1 card's +0.6R matches (7,564.51−7,540)/40). | §1, §3, §6, §11, §21a–d | 1 | Fix the §3 range, the §1 source count, the "daily S1" anchor on both cards, and surface ATR14 in §9. |
| 4.1 Pillars conclude | Each pillar ends in a label consistent with its body: §8 "Bullish continuation", §9 "Trending / Bullish", §10 per-counter confirmation plus an explicit contradiction flag, §12 every bullet tagged price-supportive/price-negative, §14 directional per theme. Marked down only because §9's supporting metrics (persistence, overlap ratio, range position) are asserted qualitatively with no values behind them. | §8, §9, §10, §12, §14 | 4 | Give §9's persistence / overlap / range-position metrics numeric values. |
| 4.2 Peer/cross-asset interpreted | §10 gives real mechanisms — dollar translation drag on multinational earnings, vol compression endorsing risk-on, DAX catch-down risk — rather than a correlation list, and the DAX non-confirmation is carried into §15/§16. But two of the three counter reads do not survive the slice: **VIX** is stated at ~15.61, −4.2% from 16.51, against slice 28 May close **16.83** from **17.18** (−2.04%); **USDX** is stated "+0.06% on 28 May to 99.28 — mildly firmer", against slice close **99.023**, **−0.19%** — the direction is inverted. §15/§17's "VIX <16" / "sub-16 VIX" claims fail on the slice. A cross-asset pillar with an inverted sign on one of three counters is materially defective however good the narrative. | §10 table; §14, §15, §17; `data/slices/VIX/...`, `data/slices/USDX/...` | 2 | Restate the VIX level/change and the USDX level/direction from the D-1 session, and re-derive the "sub-16 VIX" claims in §15/§17. |
| 4.3 Synthesis reconciles tensions | Prose synthesis is genuinely good: §15 balances trend/breadth/vol against overbought + hawkish PCE + DAX non-confirmation, §16 states an expected range and a named invalidation (close below 7,473), §18 gives three reasons and one watch item, §21a reconciles with §17. Scored down because the strategy layer this synthesis feeds violates its own construction rules on **all three cards**: Trade 1 is a limit rather than market at the daily-open anchor and its 7,495 stop matches neither the 5-day-swing nor the nearest-S/R + 0.25×ATR derivation; Trade 2 is declared TREND yet is built with the RANGE geometry (limit at P, ±1R/±2R targets) instead of entry P + 0.10×(R1−P), stop P − 0.8×(P−S1), TPs R1/R1.5/R2; Trade 3A is a breakout buy-stop (a 3C construction) rather than a 57.5% retrace of a logged qualifying swing, and it has **no invalidation row at all** — the brief requires thesis invalidation separate from the stop on every card. | §15, §16, §18, §21a; §21b all three cards | 2 | Rebuild all three cards to their family rules (numbers in the feedback file) and add an invalidation line to Trade 3A. |
| 4.4 Calibrated language | §17 is exactly one sentence, with a single direction, a level band and one caveat — no hedge stacking. Confidence "High" is stated in §3 and repeated in §18. §21a states a conviction score and an explicit conflict flag. | §3, §17, §18, §21a | 5 | None. |
| 5.1 Data dated; staleness flagged | Every §4 row and every §6 row is dated; the single-source-indicative status of the O/H/L fields is flagged in §6, in the §7 chart note and again in §19. Two gaps: the §13a **Reuters survey row has no date** ("---"), and §19 discloses that intraday OHLC was unretrievable without saying that the §6 O/H/L were therefore *constructed* from percentage moves — the §6 note says it, §19 does not. | §4, §6, §13a, §19 | 3 | Date the Reuters row; state the O/H/L derivation method in §19 as well as §6. |
| 5.2 Assumptions up front | §20 logs the anchor override ("the daily-open anchor value supplied in the instance file was overridden at run time") and the failed Stooq / Twelve Data endpoints; single-source pivot propagation is carried onto both pivot-dependent cards ("weekly pivots single-source indicative", "Pivot tiers single-source indicative — treat limit as discretionary"). But the anchor caveat is **not carried onto the Trade 1 card**, which instead names a different anchor (NY open), so the reader of the card cannot see which anchor governs. | §19, §20, §21b | 3 | Repeat the anchor-override caveat on the Trade 1 card and name the governing anchor there. |
| 5.3 Red flags surfaced | Risks are surfaced thoroughly and consistently: §12 flags the headline-fragile Iran deal and the PCE counterweight, §15 gives three downside risks including the overbought RSI2 and the DAX non-confirmation, §13d names the Fedspeak/PCE collision as the top event, and that collision is carried into the caveat row of **all three** cards. §20 logs the DAX anomaly as unresolved. | §12, §15, §13d, §21b, §20 | 5 | None. |
| 5.4 Restrictions honoured | Clean on most restrictions: no module codes, no framework name, no bracketed variable names, no ES-futures basis, no retail CFD quotes in the OHLC basis, instrument common names used. **Breach on synthesised price presented as sourced, and on the report's own use restriction.** §6 attributes every row — including the Open/High/Low columns — to "Source A: SPDJI / FRED" and "Source B: Yahoo / CNBC", while §6's own note says those O/H/L are "derived from corroborated session ranges and percentage moves" and §19 concedes "full intraday OHLC were not retrievable in this environment". Constructed levels are therefore presented under named provider attribution. The same note states the indicative O/H/L "are not used as definitive pivot inputs" — and the report then uses exactly them: §11's daily pivot is computed from H 7,569 / L 7,519 / C 7,564.51, and the derived 7,519 / 7,569 levels become the stop anchor on Trade 1, the stop anchor on Trade 2 and the breakout trigger on Trade 3A. | §6 Source A/B columns and validation note; §19 data-gaps bullet; §11; §21b all three cards | 1 | Remove provider attribution from the constructed O/H/L (or mark those cells "derived — no source"), and either stop using them as pivot/card inputs or delete the claim that they are not so used. |

## 2. Category roll-up

| Category | Level | Multiplier | Points | Justification |
|---|---|---|---|---|
| C1 Prompt adherence (max 20) | **2** | 0.40 | 8.00 | Rows 1.1/1.2/1.3 = 2/3/5, mean 3.33 → level **3**; the §5.4 restriction breach forces C1 down one level under the framework override → **2**. Driver: the 07:00 UK daily-open anchor is never stated and the card names a different one. |
| C2 Structure (max 20) | **4** | 0.85 | 17.00 | Rows 2.1/2.2/2.3 = 5/5/1, mean 3.67 → **4**. Every section and sub-section is present and ordered; the loss is entirely in §11 (weekly-only, R5→S5, no daily or monthly table) and the two missing §6 columns. |
| C3 Accuracy & evidence (max 25) | **1** | 0.20 | 5.00 | Rows 3.1/3.2/3.3/3.4 = 2/1/1/1, mean 1.25 → **1**. RSI2 does not reproduce from the report's own closes; §11 daily S1/R1 are the D-1 low/high relabelled; ATR14 never stated; the §20 "delta 0.00 pt" FRED corroboration is impossible against §4; four of five closes miss the slice by more than the 3 pt tolerance and 11 of 15 O/H/L fields miss by more than 8 pt. |
| C4 Reasoning & judgment (max 20) | **3** | 0.65 | 13.00 | Rows 4.1/4.2/4.3/4.4 = 4/2/2/5, mean 3.25 → **3**. Pillars conclude and the language is calibrated, but the cross-asset pillar has an inverted USDX sign and a wrong VIX level, and all three cards depart from their M5 constructions (card construction scored here per brief §2, not in the integrity number). |
| C5 Currency, restrictions & transparency (max 15) | **3** | 0.65 | 9.75 | Rows 5.1/5.2/5.3/5.4 = 3/3/5/1, mean 3.00 → **3**. Excellent red-flag discipline and a real agent log, undermined by an undated source row, an anchor caveat that never reaches the card, and the synthesised-price-as-sourced breach. |
| **Total** | — | — | **52.75 → 53** | Sum of category points, rounded to a whole number. |

## 3. Total, band, override check

- Raw total: 8.00 + 17.00 + 5.00 + 13.00 + 9.75 = **52.75 → 53**.
- Band: **Low** (40–59).
- **Restriction breach: YES.** Row 5.4 — synthesised Open/High/Low presented under named provider attribution in §6 while §19 records that intraday OHLC was unretrievable, and those same indicative levels are then used as the definitive daily-pivot and card-anchor inputs in direct contradiction of the report's own statement that they are not. Effect: total capped at 74 (not binding at 53) and C1 dropped one level, from 3 to 2. That drop is already reflected above and costs 9.0 points.
- **Fabricated source: NO — considered and declined.** Three citations are misused rather than invented: FRED is dated 27 May yet §5/§20 claim it corroborates the 28 May close at delta 0.00 pt; Trading Economics contributes a non-numeric "record high" that is counted inside a ±0.10 pt band; the §13a Reuters survey row is undated and its headline figure is absent from its own quote. Each cited outlet and each quoted value is individually plausible and internally coherent on its own row — the impossibility lives in the report's claims *about* the sources (§1, §5, §20), not inside any source row. Under brief §1 the hallucinated-source override (cap 59, C3 = 0) is therefore **not** invoked; the defects are scored in rows 3.2 and 3.4, which already sit at 1. Had it been invoked the total would have been capped at 59 with C3 = 0, giving 48 — i.e. the outcome is not sensitive enough to this call to change the band.
- Final: **53 / 100 — Low**, override `restriction_breach`.

## 4. Card Integrity

Linter rows, verbatim from `qa/regen_20260906_qa1/lint_static/2026-05-29.csv`:

| card_id | report_date | strategy | flags | dud |
|---|---|---|---|---|
| 2026-05-29_Trade_1 | 2026-05-29 | Trade 1 - Daily Directional | CLEAN | False |
| 2026-05-29_Trade_2 | 2026-05-29 | Trade 2 - Pivot (buy limit daily P) | CLEAN | False |
| 2026-05-29_Trade_3A | 2026-05-29 | Trade 3A - Momentum-Pullback (breakout stop) | CLEAN | False |

Per-card integrity, 100 − 40·(#DUD) − 10·(#WARN), floored at 0:

| Card | #DUD | #WARN | Integrity |
|---|---|---|---|
| 2026-05-29_Trade_1 | 0 | 0 | 100 |
| 2026-05-29_Trade_2 | 0 | 0 | 100 |
| 2026-05-29_Trade_3A | 0 | 0 | 100 |

Cards: 3 total, 0 suppressed. **Report mean over non-suppressed cards = 100.0.**

The static engine is satisfied on every card: stops on the correct side of entry (all long, stop below), TP1 beyond entry, TP2 beyond TP1, TP3 beyond TP2, R of 40 / 34 / 44 pts all inside 0.3×ATR14 (20.81) to 3.0×ATR14 (208.14), TP1 within 2.5×ATR14 (173.45) of entry, and `anchor_broker 09:00` explicit on all three.

M5 construction assessment (feeds row 4.3, **not** the integrity number above):
- **Trade 1** — must be market at the 07:00 UK daily open; issued as a limit at 7,535 with a "market at NY open" alternative, so neither the anchor nor the market-entry-equals-D-1-close rule is met. The 7,495 stop is not the tighter of (5-day swing extreme, nearest S/R) + 0.25×ATR under either basis: from the slice's nearest support the buffer gives 7,515.92, from the 5-day swing low 7,447.15; 7,495 is neither. Runner cap quoted at ~134 pts implies ATR ≈ 44.7 against slice ATR14 69.38 (3×ATR = 208.14). Tranche split, BE-on-TP2 rule and ±1R/±2R spacing are correct.
- **Trade 2** — declared TREND but built with the RANGE geometry (limit at P, targets at entry ±1R/±2R). TREND requires entry P + 0.10×(R1−P), stop P − 0.8×(P−S1), targets R1/R1.5/R2. The stop anchor is named "daily S1 / 7,519 shelf"; 7,519 is the D-1 low, not S1 (7,533.27 slice, 7,532.67 from the report's own H/L/C).
- **Trade 3A** — built as a confirmed-breakout buy stop, which is the 3C construction, not 3A. No swing endpoints are logged, no ≥2×ATR magnitude test is shown, and the 5-day swing (7,464.50 → 7,576.20 = 111.70 pts) fails the 2×ATR14 = 138.76 pt threshold. TP1/TP2 are quoted as +1R/+2R rather than the 38.2% level and the 0% anchor. No invalidation row — every card must carry a thesis invalidation separate from the stop. The 7,572 trigger is also below the slice D-1 cash close (7,572.50) and below the D-1 high (7,576.20), so on slice numbers it is not a break of anything.

## 5. Data reconciliation log

Tolerances per brief §4: |Δ| ≤ 3 pt on a close, ≤ 8 pt on an open/high/low. Δ = report − slice. Slice values are cash-session (16:30–23:00 broker).

| Section | Report value | Slice value | Delta | Verdict |
|---|---|---|---|---|
| §6 Thu 21 May Open | 7468.00 | 7408.60 | +59.40 | FAIL |
| §6 Thu 21 May High | 7472.00 | 7471.80 | +0.20 | PASS |
| §6 Thu 21 May Low | 7430.00 | 7394.10 | +35.90 | FAIL |
| §6 Thu 21 May Close | 7445.93 | 7450.30 | −4.37 | FAIL |
| §6 Fri 22 May Open | 7449.00 | 7482.50 | −33.50 | FAIL |
| §6 Fri 22 May High | 7479.00 | 7509.20 | −30.20 | FAIL |
| §6 Fri 22 May Low | 7445.00 | 7464.50 | −19.50 | FAIL |
| §6 Fri 22 May Close | 7473.47 | 7475.70 | −2.23 | PASS |
| §6 Tue 26 May Open | 7486.00 | 7522.80 | −36.80 | FAIL |
| §6 Tue 26 May High | 7522.50 | 7543.50 | −21.00 | FAIL |
| §6 Tue 26 May Low | 7484.00 | 7505.50 | −21.50 | FAIL |
| §6 Tue 26 May Close | 7519.12 | 7527.50 | −8.38 | FAIL |
| §6 Wed 27 May Open | 7521.00 | 7531.00 | −10.00 | FAIL |
| §6 Wed 27 May High | 7530.70 | 7536.00 | −5.30 | PASS |
| §6 Wed 27 May Low | 7499.70 | 7504.30 | −4.60 | PASS |
| §6 Wed 27 May Close | 7520.36 | 7528.50 | −8.14 | FAIL |
| §6 Thu 28 May Open | 7526.00 | 7525.00 | +1.00 | PASS |
| §6 Thu 28 May High | 7569.00 | 7576.20 | −7.20 | PASS |
| §6 Thu 28 May Low | 7519.00 | 7515.50 | +3.50 | PASS |
| §6 Thu 28 May Close (D-1 anchor) | 7564.51 | 7572.50 | −7.99 | FAIL |
| §6 RSI2 26 May | 96.1 | 100.0 (from report's own closes) / 75.34 (slice closes) | −3.9 / +20.8 | FAIL — does not reproduce from the report's own closes |
| §6 RSI2 27 May | 96.2 | 100.0 (own closes) / 3.82 (slice closes) | −3.8 / +92.4 | FAIL — slice figure confounded by the 25 May holiday bar; own-closes test is decisive |
| §6 RSI2 28 May | 98.7 | 100.0 (own closes) / 100.00 (slice closes) | −1.3 / −1.3 | FAIL |
| §6 RSI2 21 & 22 May | 86.8 / 91.5 | not valuable (needs closes before the window) | — | UNTESTABLE — but both differ from the prior report's 80.6 / 89.1 for the same sessions |
| §6 Trend column (all 5 rows) | Neutral/Bullish/Bullish/Neutral/Bullish | same under the Close-vs-Open + RSI2-vs-50 rule | 0 | PASS (given the stated RSI2) |
| §6 session set | 21, 22, 26, 27, 28 May (25 May excluded as Memorial Day) | slice has a thin 25 May session (4,217 ticks vs 18–26k) | — | PASS — exclusion is correct for the cash index; noted because it shifts every slice-based RSI2/pivot comparison |
| §11 Weekly P | 7417.49 | 7441.33 | −23.84 | FAIL |
| §11 Weekly R1 | 7534.98 | 7543.57 | −8.59 | FAIL |
| §11 Weekly S1 | 7355.98 | 7373.47 | −17.49 | FAIL |
| §11 Weekly R2 | 7596.49 | 7611.43 | −14.94 | FAIL |
| §11 Weekly S2 | 7238.49 | 7271.23 | −32.74 | FAIL |
| §11 Weekly R3 | 7713.98 | 7713.67 | +0.31 | PASS (coincidental — the inputs differ) |
| §11 Weekly S3 | 7176.98 | 7203.37 | −26.39 | FAIL |
| §11 Weekly pivot internal reproduction | P/R1..R5/S1..S5 from implied H 7479.00 / L 7300.00 / C 7473.47 | all eleven levels reproduce exactly | 0.00 | PASS — internally consistent; the implied prior-week H/L are 30.19 and 39.09 pt off the slice |
| §11 Daily P (29 May) | ≈7551 | 7550.84 from the report's own D-1 H/L/C; 7554.73 from the slice | −0.16 / −3.73 | PASS internally; marginal vs slice |
| §11 "first daily resistance" | ≈7569 | R1 = 7582.67 from the report's own H/L/C; 7593.97 slice | −13.67 / −24.97 | FAIL — 7,569 is the D-1 high relabelled as R1 |
| §11 "first daily support" | ≈7519 | S1 = 7532.67 from the report's own H/L/C; 7533.27 slice | −13.67 / −14.27 | FAIL — 7,519 is the D-1 low relabelled as S1 |
| §11/§21b Monthly pivots | absent | — | — | FAIL — required table missing |
| §9 / §21b ATR(14) | never stated; ≈44.7 implied by "3×ATR cap (~+134 pts)" | 69.38 (cash) / 78.09 (full day) | −24.7 implied | FAIL |
| §10 VIX 28 May level | ~15.61 | 16.83 | −1.22 | FAIL |
| §10 VIX 28 May change | −4.2% (from 16.51) | −2.04% (from 17.18) | −2.2 pp | FAIL |
| §15/§17 "VIX <16 / sub-16" | <16 | 16.83 | — | FAIL |
| §10 USDX 28 May level | 99.28 | 99.023 | +0.257 | FAIL |
| §10 USDX 28 May change | +0.06% ("mildly firmer") | −0.19% | sign inverted | FAIL |
| §10 DAX 40 | 25,062–25,092, −0.3 to −0.5% | no DAX slice available in this run | — | UNTESTABLE |
| §3 quoted range "last 2 sessions" | 7,519 – 7,569 | 7,499.70 – 7,569.00 from the report's own §6 | +19.30 on the low | FAIL — internal |
| §1 "six sources within a 0.10-point band" | six | three numeric 28 May quotes in §4 (SPDJI, CNBC, Yahoo) | −3 | FAIL — internal |
| §20 "SPDJI × FRED delta 0.00 pt" | 0.00 pt | §4 FRED row is 27 May at 7,520.36 → 44.15 pt, different date | +44.15 | FAIL — internal, impossible as stated |
| §13c 28 May "jobless claims firm" | firm | Initial Claims 215.0 vs consensus 203.0, previous 209.0 | — | FAIL — claims rose and missed |
| §13c 28 May "PCE 3-yr high" | 3-yr high | Core PCE y/y 3.3 vs previous 3.2, consensus 3.1; headline PCE y/y 3.8 vs previous 3.5 | — | PASS on direction; the "three-year" span is outside the slice window and untested |
| §21c / §21d backtest arithmetic | 4/5, +0.9 · 3/3, +1.7 · 1/2, +1.4; open card +0.6R | recomputed from the table: 3.5/4 = +0.875, 5.0/3 = +1.667, +1.4; (7564.51−7540)/40 = +0.61R | ≈0 | PASS — internally consistent |
| Prior report cross-check (21 May close) | 7,445.93 | 7,445.74 in `SP500_Daily_Report_28May2026.md` | +0.19 | FAIL — exceeds the ±0.10 pt tolerance the report itself claims |
