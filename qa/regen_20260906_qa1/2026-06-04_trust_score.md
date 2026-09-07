# Trust Score — 2026-06-04 — SP500_Report_04Jun2026.md

Run: regen_20260906_qa1 · D = 2026-06-04 · D-1 = 2026-06-03 · Slice: `data/slices/US500/US500_upto_2026-06-03.csv` (cash session 16:30–23:00 broker). Helper run with the report's five §6 closes (7563, 7563, 7580.06, 7599.96, 7609.78).

Headline defect: the report is built on the **2 June** session as its "last validated settlement" and explicitly treats 3 June as "in progress at time of run" (§2, §3, §20 timestamp "generated 3 June 2026 (UK)"). For D = 4 June the required data basis is the NY close of D-1 = **3 June**, which the slice holds in full (cash O 7602.0 / H 7608.0 / L 7556.0 / C 7565.2, RSI2 16.23). Every level in the report — consensus close, pivots, RSI2 state, direction score and all three cards — is therefore one session stale, and the true D-1 close (7565.2) sits 44.6 pts below the report's reference level and below the report's own S2 invalidation (7566.65).

## 1. Section 7 checklist

| Item | Reviewer notes | Evidence observed | Score 0–5 | Action required |
|---|---|---|---|---|
| 1.1 Variables respected | Asset = S&P 500 cash index ✓; counters USDX/VIX/DAX with USDX first ✓; currency/units ✓; lookback 5 sessions ✓ in count but the window is 27 May–2 Jun (should end at D-1 = 3 Jun); **as-of NY close of D-1 not respected** (report as-of 2 Jun, "3 June in progress"); anchor **overridden 07:00 UK → 00:00 UK** (disclosed in §20 and on the card but still a deviation); ≥6 sources by count but none from the index-provider/exchange tier — all media/aggregator (Stooq/Investing logged as failed). | §2 As-of row, §3 rationale, §20 bullets 1–3, §4 table | 2 | Variables not respected: as-of date (D-1 = 3 Jun), daily-open anchor (07:00 UK), source tiers. |
| 1.2 Coverage & currency consistent | No date on or after D appears in data tables ✓; no currency/unit drift ✓. But the coverage period is shifted one session early throughout (§2 lookback 27 May–2 Jun; §6 ends 2 Jun; §11 pivots from 2 Jun; §21c backtest t−1 = 2 Jun). §3/§4 quote a 3 Jun "~7,567 intraday" figure that is neither in §6 nor used. | §2, §6, §11, §21b/c | 2 | Rebase the whole report to D-1 = 3 Jun; add the 3 Jun row to §6; drop 27 May. |
| 1.3 Audience & tone | Senior-strategist register, trading/risk-review framing, no retail language. | §1, §18, §21d limitations boilerplate | 5 | None. |
| 2.1 Sections present & ordered | All of §1–§21 present in order; §13a–d and §21a–d all present. §7 charts appear as pandoc image placeholders (5 captions) — accepted as evidence, noted. | Headings §1–§21; §7 lines 151–176 | 5 | None. |
| 2.2 Scorecard as a table | §6 is a table with Date/O/H/L/C/RSI2/Trend and a combined "Source A × B / Outcome" column (Source A, Source B, Final and Validation are merged into one cell rather than four columns). §11: daily pivots only, rendered R5→S5 (5 levels a side, brief asks R3→P→S3); **weekly and monthly pivot tables absent** (stated as indicative and omitted). | §6 lines 115–141; §11 lines 258–272, 276–279 | 3 | Add weekly and monthly pivot tables (flagged indicative if need be); split §6 source/validation columns. |
| 2.3 Method steps visible | §4 observations → §5 classification/consensus ✓; §8 candle-by-candle + sequence label ✓; §9 regime with persistence/overlap/VOLator/KER ✓; §7 five chart placeholders. | §4–§9 | 4 | None material; charts unverifiable in md. |
| 3.1 Quantitative claims sourced | §1 numbers point to §6/§13; §12/§14 figures (PCE ~3.8%, Dell ~33%, breadth ~206/503, VIX ~16) are unsourced in place and not all appear in §13a/§13c (breadth and Dell have no article behind them). | §12 paras 1, 4; §14 bullets 1, 6 | 3 | Attach a §13a article or a §4/§10 row to breadth, Dell and VIX figures. |
| 3.2 Citations exist & contain data | Spot-checks (cannot fetch): (i) CNBC 1 Jun "Record close to kick off June…" — date and quote consistent with §6 1 Jun record close; (ii) Benzinga 3 Jun pre-open article giving 2 Jun close 7,609.78 and open 7,595.40 — consistent with §6 2 Jun row and §20 pair; (iii) Yahoo 29 May "cap winning month" — 29 May was month-end, matches §13c. No impossible/self-contradictory source → no hallucination override. **But** §6 cites "CNBC × TheStreet" as corroborating a 27 May close of 7,563 — that value contradicts the slice (7528.5) and the prior report (SP500_Report_02Jun2026.md §6: 27 May 7,520.36; 28 May 7,563.63 sourced to TheStreet). The 27 May "corroboration" is a misattributed 28 May figure. TheStreet and BBN appear in §6/§13a but not in the §4 evidence table. | §4, §6 row 1, §13a; prior report §6 lines 133–137 | 2 | Re-source the 27 May row (or drop it once rebased); list every §6 source in §4. |
| 3.3 Calculations transparent | RSI2: formula stated; helper recomputation from the report's own closes gives 100/100/100 for the last three rows = report ✓. Pivots: all ten §11 levels reproduce exactly from the report's own 2 Jun H/L/C (P 7604.56, R1 7626.12, S1 7588.21, R2 7642.47, S2 7566.65, R3 7664.03, S3 7550.30) ✓. ATR(14) stated only as "~58, indicative" with no window/derivation (3A implies 57.95). KER ≈ 0.31 stated, not derived. §21a: only three components shown (0.25 + 0.20 + 0.06 = 0.51); the remaining +0.15 to reach +0.66 is attributed to "Kaufman and cross-asset (MIXED)" without values, and the sixth weighted signal is never named. | §6 footnote, §11, §19, §21a | 3 | Show the six signal×weight terms of the direction score; state the ATR window and value. |
| 3.4 Numbers reconcile | Internally: D-1 close 7,609.78 identical in §1/§3/§4/§6/§21b ✓; §11 pivots = card pivots ✓; RSI2 §6 = §8 = §21a ✓; ATR §19 = 3A ✓. Against the slice: **27 May close 7,563 vs 7528.5 (Δ +34.5) — Category 3 failure (>10 pts)**; 28 May 7,563 vs 7572.5 (Δ −9.5); 29 May −4.7; 1 Jun −6.0; 2 Jun −6.0; all beyond the 3-pt close tolerance. 27 May and 28 May closes are identical (7,563) and the 1 Jun and 2 Jun lows are identical (7,582.99) — copy errors. The true D-1 (3 Jun) row is absent. Full log in §5 below. | §6; helper output; §5 log | 1 | Rebuild §6 from D-1 = 3 Jun backwards; remove duplicated values. |
| 4.1 Pillars conclude | §8 "Bullish continuation" ✓; §9 "Bias: Bullish" ✓; §10 "MIXED" ✓; §12 and §14 carry per-item tags but no closing direction label. Cards: each card reaches a level set, but Trade 2's entry is labelled "Stop/limit" (order type undefined) and sits below the report's own reference close while the JSON extracts it as BUY STOP. | §8 end, §9, §10 end, §12, §14, §21b | 3 | Add a closing direction label to §12 and §14; fix Trade 2 order type. |
| 4.2 Peer/cross-asset interpreted | §10 gives a mechanism per counter (dollar translation headwind, VIX/multiples, DAX common risk factor) and an aggregate read carried to §15/§16. VIX "~16" undated/unsourced (slice VIX 3 Jun close 17.0 — consistent within basis). | §10 table and aggregate paragraph | 4 | Date/source the VIX and USDX readings. |
| 4.3 Synthesis reconciles tensions | §15/§16 address overbought-vs-trend, MIXED cross-asset and the NFP catalyst. **Not reconciled**: §3 itself reports 3 Jun trading "~7,567 intraday", i.e. at the report's own S2 invalidation (7,566.65, §16 "would neutralise the bullish structure"), yet §17/§18/§21a proceed with a High-confidence LONG at +0.66 without addressing it. Card construction (M5): Trade 1 MARKET entry equals the report's close, not the D-1 close (7565.2, Δ 44.6); Trade 2 BUY STOP at 7,606.72 is *below* the report's own reference close 7,609.78 (wrong side for a stop order on the report's basis) and R = 0.24×ATR14(slice) is below the 0.3×ATR floor; Trade 3A's swing low 7,505 is a misattributed value (prior report: 27 May low 7,505.4; slice 28 May cash low 7515.5) and the swing qualifies only exactly at 2.00× an indicative ATR — on the slice cash basis it is 1.73×ATR and does not qualify. | §3 rationale, §16, §17, §21a, §21b | 2 | Reconcile the D-1 close with the invalidation level before issuing cards; rebuild cards per feedback. |
| 4.4 Calibrated language | §17 is exactly one sentence with one conditional ✓; confidence "High" stated in §3/§18. "High" is over-stated for a level that is one session stale and for closes that all sit 4.7–34.5 pts from the data basis. | §3, §17, §18 | 3 | Downgrade confidence or rebase the level. |
| 5.1 Data dated; staleness flagged | Every price and article carries a date ✓; single-source O/H/L asterisked ✓; the 3 Jun staleness *is* flagged (§2, §3) but then ignored rather than resolved; ATR flagged indicative ✓. | §2, §3, §6 footnote, §13a, §19 | 3 | Add the 3 Jun row; once rebased the staleness flag disappears. |
| 5.2 Assumptions up front | Anchor-override caveat on Trade 1 card and in §20 ✓; single-source propagation on Trade 2 (weekly/monthly excluded) and Trade 3A ("swing low partly indicative") ✓; analyst-directed non-suppression logged ✓. | §21b caveat rows, §19, §20 | 4 | None. |
| 5.3 Red flags surfaced | §12/§15 list overbought, NFP, breadth, Iran/Hormuz, dollar ✓. §13d NFP (5 Jun, High impact) is named the highest-impact event but is **not carried into any card caveat**; Trade 1 caveat only mentions overbought RSI2. | §13d, §21b caveats | 3 | Add the 5 Jun NFP collision to each card's caveats. |
| 5.4 Restrictions honoured | No module codes, no bracketed variable names, no framework name (grep clean) ✓; CFD/retail quotes excluded ✓; ES futures not used ✓; instrument common names ✓. Weakness: duplicated values (27 May close = 28 May close; 1 Jun low = 2 Jun low) are presented as CORROBORATED/sourced — an error rather than an open violation of the no-synthesis rule, so no override. Anchor override was disclosed, not concealed. | Whole report; grep for `M1..M5`, `[...]`, "Trust Score" | 3 | Remove duplicated values; restore 07:00 UK anchor or keep the disclosure. |

## 2. Category roll-up

| Category | Level | Multiplier | Points | Justification |
|---|---|---|---|---|
| C1 Prompt adherence (20) | 3 | 0.65 | 13.00 | Rows 2/2/5 → mean 3.0. Asset, counters, units and tone respected; as-of session, anchor and source tiers not. |
| C2 Structure (20) | 4 | 0.85 | 17.00 | Rows 5/3/4 → mean 4.0. All sections present and ordered; weekly/monthly pivot tables missing, §6 columns merged. |
| C3 Accuracy & evidence (25) | 2 | 0.40 | 10.00 | Rows 3/2/3/1 → mean 2.25 → 2. 27 May close wrong by 34.5 pts and contradicts the prior report; D-1 row absent; all closes outside tolerance; RSI2 and pivots do reproduce internally. |
| C4 Reasoning & judgment (20) | 3 | 0.65 | 13.00 | Rows 3/4/2/3 → mean 3.0. Cross-asset mechanism good; synthesis ignores its own S2 invalidation at the 3 Jun print; card construction defects on all three cards. |
| C5 Currency, restrictions & transparency (15) | 3 | 0.65 | 9.75 | Rows 3/4/3/3 → mean 3.25 → 3. Everything dated and caveated, but staleness flagged rather than fixed and NFP not on cards. |
| **Total** | | | **62.75 → 63** | |

## 3. Total, band, override check

- **Total: 63/100** (13.00 + 17.00 + 10.00 + 13.00 + 9.75 = 62.75, rounded).
- **Band: Moderate** (60–74) — must not be used as-is; targeted regeneration of C3 (data basis) and the cards.
- **Overrides: none.** No cited source is impossible or self-contradictory (the 27 May "CNBC × TheStreet" figure is a real 28 May figure misattributed to 27 May — an accuracy failure scored in 3.2/3.4, not a fabricated source). No enumerated restriction (brief §2 row 5.4) is openly violated. The as-of-date and anchor deviations are Variables failures (rows 1.1/1.2) and were disclosed in §20; they are not treated as a restriction breach. Note for the run owner: if the project treats "as-of NY close of D-1" as a restriction rather than a variable, the restriction override would apply — the cap at 74 would not bind, but C1 would drop to level 2 (8.00 pts) giving 58 → Low.

## 4. Card Integrity

Lint rows (`qa/regen_20260906_qa1/lint_static/2026-06-04.csv`), verbatim:

| card_id | report_date | strategy | flags | dud |
|---|---|---|---|---|
| 2026-06-04_Trade_1 | 2026-06-04 | Trade 1 - Daily Directional | CLEAN | False |
| 2026-06-04_Trade_2 | 2026-06-04 | Trade 2 - Pivot (TREND_UP breakout) | WARN_R_TINY(0.21xATR) | False |
| 2026-06-04_Trade_3A | 2026-06-04 | Trade 3A - Momentum-Pullback (57.5% fib) | CLEAN | False |

| Card | #DUD | #WARN | Integrity = 100 − 40·DUD − 10·WARN |
|---|---|---|---|
| Trade 1 | 0 | 0 | 100 |
| Trade 2 | 0 | 1 | 90 |
| Trade 3A | 0 | 0 | 100 |
| **Report mean (3 non-suppressed cards)** | 0 | 1 | **96.7** |

The static linter cannot see the data basis; the M5-rule assessment of each card (entry anchor vs D-1 close, order side, swing qualification) is recorded in row 4.3 above and in the feedback file — it feeds Category 4, not the integrity number.

## 5. Data reconciliation log

Tolerances (brief §4): close |Δ| ≤ 3 pts, open/high/low |Δ| ≤ 8 pts = consistent; larger = discrepancy; close >10 pts or RSI2 not reproducing = Category 3 failure. Slice values are cash-session (16:30–23:00 broker) from `US500_upto_2026-06-03.csv`.

| Section / field | Report value | Slice value | Δ (report − slice) | Verdict |
|---|---|---|---|---|
| §6 27 May Open | 7,565* | 7531.0 | +34.0 | Discrepancy |
| §6 27 May High | 7,575* | 7536.0 | +39.0 | Discrepancy |
| §6 27 May Low | 7,548* | 7504.3 | +43.7 | Discrepancy |
| §6 27 May Close | 7,563 (CORROBORATED) | 7528.5 | **+34.5** | **Category 3 failure** (>10 pts); value equals the 28 May close; prior report gives 7,520.36 |
| §6 27 May RSI2 | 61.3 | 3.82 | +57.5 | Discrepancy (prior report: 100); not reproducible from the report because 25–26 May closes are not stated |
| §6 28 May Open | 7,560* | 7525.0 | +35.0 | Discrepancy |
| §6 28 May High | 7,588* | 7576.2 | +11.8 | Discrepancy |
| §6 28 May Low | 7,505* | 7515.5 | −10.5 | Discrepancy (7,505 matches the prior report's *27 May* low 7,505.4 — misdated) |
| §6 28 May Close | 7,563 | 7572.5 | −9.5 | Discrepancy (just inside the 10-pt failure line; prior report 7,563.63) |
| §6 28 May RSI2 | 100 | 100.00 | 0 | Consistent |
| §6 29 May Open | 7,568* | 7581.1 | −13.1 | Discrepancy |
| §6 29 May High | 7,600* | 7601.8 | −1.8 | Consistent |
| §6 29 May Low | 7,560* | 7567.9 | −7.9 | Consistent (at tolerance) |
| §6 29 May Close | 7,580.06 | 7584.8 | −4.74 | Discrepancy (basis-sized, >3) |
| §6 29 May RSI2 | 100 | 100.00 | 0 | Consistent |
| §6 1 Jun Open | 7,585* | 7575.2 | +9.8 | Discrepancy |
| §6 1 Jun High | 7,617.66 | 7623.6 | −5.94 | Consistent (prior report had 7,603.44 — cross-report break of 14.2) |
| §6 1 Jun Low | 7,582.99 | 7568.5 | +14.49 | Discrepancy; identical to the 2 Jun low — duplicate (prior report 7,562.61) |
| §6 1 Jun Close | 7,599.96 | 7606.0 | −6.04 | Discrepancy (basis-sized, >3) |
| §6 1 Jun RSI2 | 100 | 100.00 | 0 | Consistent |
| §6 2 Jun Open | 7,595.40 | 7590.8 | +4.6 | Consistent |
| §6 2 Jun High | 7,620.90 | 7624.6 | −3.7 | Consistent |
| §6 2 Jun Low | 7,582.99 | 7588.3 | −5.31 | Consistent |
| §6 / §1 / §3 / §4 / §21b 2 Jun Close (report's reference level) | 7,609.78 | 7615.8 | −6.02 | Discrepancy (basis-sized, >3) |
| §6 2 Jun RSI2 | 100 | 100.00 | 0 | Consistent |
| §6 3 Jun row (true D-1) | absent ("in progress"; §3 "~7,567 intraday") | O 7602.0 H 7608.0 L 7556.0 C 7565.2, RSI2 16.23 | — | **Missing D-1 row**; report reference close 7,609.78 is 44.58 pts above the D-1 cash close |
| RSI2 from report's own closes (helper) | 100 / 100 / 100 (29 May, 1 Jun, 2 Jun) | 100 / 100 / 100 | 0 | Arithmetic reproduces |
| §19 / §21b ATR(14) | ~58 (indicative; 3A implies 57.95) | 63.03 cash / 73.75 full-day | −5.0 / −15.8 | Basis-sized; no derivation shown |
| §11 pivots from report's own 2 Jun H/L/C | P 7604.56 R1 7626.12 S1 7588.21 R2 7642.47 S2 7566.65 R3 7664.03 S3 7550.30 | recomputed from 7620.90/7582.99/7609.78: identical to 0.01 | 0 | Reproduce; R4/R5/S4/S5 also reproduce |
| §11 daily P vs slice D-1 (3 Jun) pivot | 7,604.56 | 7576.40 (R1 7596.80, S1 7544.80, R2 7628.40, S2 7524.40) | +28.16 | Wrong session — pivots built on D-2 |
| §21b 3A swing (5-day) | low 7,505.0 (28 May) → high 7,620.90 (2 Jun), 115.9 pts | cash low 7515.5 (28 May) → high 7624.6 (2 Jun), 109.1 pts | −10.5 / −3.7 | Swing low is a misattributed value; magnitude 1.73×ATR14 on slice basis |
| §10 / §14 VIX "~16" | ~16 (undated) | 3 Jun close 17.0 | ≈ −1 | Consistent within basis; undated |
| §3 "3 Jun ~7,567 intraday" | ~7,567 | 3 Jun cash range 7556.0–7608.0, close 7565.2 | — | Consistent as an intraday print; should have been the settled D-1 close |
