# Trust Score — 2026-06-05 — SP500_Report_05Jun2026.md

Run: regen_20260906_qa1 · Asset US500 · D = 2026-06-05 · D-1 slice = `data/slices/US500/US500_upto_2026-06-04.csv` (last bar 2026-06-04 23:45 broker).
Reviewer inputs: the report, `cards/baseline/by_date/2026-06-05.json`, `qa/regen_20260906_qa1/lint_static/2026-06-05.csv`, the D-1 slices (US500, VIX, USDX, NEWS), reports dated 29 May / 02 Jun / 04 Jun 2026 for cross-report consistency, and `engine/qa_slice_stats.py`.

Helper output (slice, cash session 16:30–23:00 broker): D-1 (04 Jun) cash O/H/L/C 7541.3 / 7604.3 / 7535.0 / 7592.7; full-day close 7582.1; ATR14 cash 60.39 (full-day 71.46); daily pivots from D-1 cash P 7577.33 · R1 7619.67 · R2 7646.63 · R3 7688.97 · S1 7550.37 · S2 7508.03 · S3 7481.07; weekly (25–29 May) P 7563.63; 5-day swing 7624.60 (02 Jun) / 7535.00 (04 Jun); RSI2 on slice cash closes 100 / 100 / 100 / 16.23 / 35.21; RSI2 recomputed from the report's own closes (simple-mean method) n/a / n/a / 100.0 / 14.9 / 35.3.

Report's stated values: D-1 (Thu 04 Jun) O 7,558* · H 7,592* · L 7,548* · C 7,584.31; RSI2 column 100.0 / 100.0 / 100.0 / 20.8 / 57.5; ATR(14) not stated anywhere; daily pivots (built from the 03 Jun session, i.e. D-2) P 7,570.08 · R1 7,588.95 · R2 7,624.21 · R3 7,643.08 · S1 7,534.82 · S2 7,515.95 · S3 7,480.69 (plus R4/R5/S4/S5); direction score +0.22 LONG (below 0.25 → Trade 1 suppressed); regime §9 "Trending (Bullish)", consolidated to "TRANSITION with upward bias"; cards: Trade 1 SUPPRESSED; Trade 2 BUY LIMIT 7,570 / SL 7,512 / TP1 7,589 / TP2 7,624 / TP3 trail (R = 58); Trade 3A BUY STOP 7,593 / SL 7,548 / TP1 7,621 / TP2 7,643 / TP3 7,697 (R = 45).

## 1. Section 7 checklist

| Item | Reviewer notes | Evidence observed | Score 0–5 | Action required |
|---|---|---|---|---|
| 1.1 Variables respected | Asset = S&P 500 cash index; counters USDX · VIX · DAX 40 in the required order; as-of NY close of D-1 with tz America/New_York; 5-session execution block, 25-session regime block; USD / index points. Gaps: tick 0.01 not stated; §4 has six observations but only four distinct providers (FRED, Yahoo, CNBC, TheStreet) with no exchange or sell-side price source; the 07:00 UK daily-open anchor is never stated — §2 says only "Daily-open anchor overridden for this run to the 05 June 2026 session per the analyst request" with no time. | §2 table; §4 table; §10 header; §2 italic note; §21b cards (no anchor time) | 3 | State the anchor time (07:00 UK) in §2, §20 and on every card; add tick size; add at least one exchange/index-provider or sell-side price source so that six distinct sources are met. |
| 1.2 Coverage & currency consistent | All prices dated ≤ D-1 and the session is D; units are index points/USD throughout. Drift points: §11 daily pivots are built from the 03 Jun session (D-2) instead of the D-1 session (04 Jun) — the "prior session" is mis-assigned; §11 monthly pivots imply a May high of 7,620.90 (solve H = 2P − S1 = 7,620.90) which the report itself dates to 02 June as a fresh all-time high — a June print used as a May input. | §11 headings and tables; §1/§6 (7,620.90 on 02 Jun) | 3 | Rebuild daily pivots from the 04 Jun H/L/C; rebuild monthly pivots from May-only H/L/C. |
| 1.3 Audience & tone | Senior US Equity Strategist byline; trading-and-risk-review framing; institutional register throughout; no retail phrasing. | Byline; §1; §18 | 5 | None. |
| 2.1 Sections present & ordered | §1–§21 all present, in order; §13a–d present with numeric tilt in §13b; §21a–d present including the limitations boilerplate. Defect: §11 opens with an empty stray table (header "Level" with no rows) before the daily pivot table — malformed rendering. | Headings §1–§21; §11 first table | 4 | Remove the empty table in §11. |
| 2.2 Scorecard as a table | §6 is a table with Date/O/H/L/C/RSI2/Trend/Source A/Source B/Final/Validation — compliant. §11: daily table shows R5→P→S5 (five levels each side, not the specified three), weekly and monthly tables are R3→P→S3 as required; the malformed empty table sits above the daily one. | §6; §11 | 3 | Trim the daily pivot table to R3→P→S3; remove the empty table. |
| 2.3 Method steps visible | §4 observations → §5 classification/consensus (weighted median) → §6 validated table; §8 candle-by-candle with sequence assessment and judgement label; §9 regime with persistence/overlap/range-position stated qualitatively (no numeric values) and VOLator readings numeric; §7 has five chart captions with image placeholders (pandoc-dropped images accepted as evidence). | §4–§9 | 4 | Give numeric persistence / overlap / KER values in §9. |
| 3.1 Quantitative claims sourced | Most §1/§12 figures carry a source (FactSet 85% beat, Goldman 8,000/EPS $340, Shiller P/E 42.78 → 24/7 Wall St). Unsourced: "~85% odds of a quarter-point hike (up from ~60%)", "21× forward multiple", "top-10 ≈ 35–36% of weight", all §10 counter levels (USDX ~99.5, VIX ~16.5, DAX 24,800–24,950) — §19 says "single aggregator each" without naming it. Slice check: VIX 04 Jun close 16.36 (report ~16.5, consistent); USDX 04 Jun close 99.46 / 03 Jun high 99.578 (report ~99.5, consistent), but "two-month high" is loose — the slice shows 100.336 on 06 Apr, inside a two-month window. | §1, §10, §12, §14; VIX/USDX slices | 3 | Attach a named, dated source to the Fed-odds, multiple, concentration and counter-level figures. |
| 3.2 Citations exist & contain data | Cannot fetch. Spot-checked: (a) FRED S&P DJI, 03 Jun 19:01 CDT, 7,553.68 — the figure is reused identically in §6 and as the pivot close in §11; (b) TheStreet, 02 Jun, "closed above 7,600 for the first time", 7,609.78 — matches §6, §8 and §13a; (c) CNBC, 04 Jun session wrap, 7,584.31 — matches §1, §3, §6, §13a, §13c. Goldman 26 May 8,000 target and 24/7 Wall St Shiller 42.78 are also used consistently (§12, §15). No impossible dates and no self-contradictory quotes → no hallucination override. Weakness: the single-source O/H/L attributed to CNBC disagree with the corroborated values the 02 Jun report printed for the same days (29 May H 7,599.38 vs 7,588 here; 01 Jun L 7,562.61 vs 7,578 here). | §4, §6, §13a; `SP500_Report_02Jun2026.md` §6 | 4 | Reconcile 29 May / 01 Jun O/H/L with the values corroborated in earlier reports. |
| 3.3 Calculations transparent | RSI2: §6 states the method ("fixed at period 2, computed from the validated close sequence") but the column does NOT reproduce under the fixed definition (RS = mean gain / mean loss over 2 periods): from the report's own closes the 03 Jun and 04 Jun values are 14.9 and 35.3, not 20.8 and 57.5 (helper and independent recomputation agree). The stated values do reproduce under an unstated Wilder-style smoothing (20.9 / 57.6), so the method deviates from the standard and the seed is not shown. Trend labels happen to be unchanged (Bearish / Neutral). Pivots: §11 daily levels reproduce exactly from the stated 03 Jun H/L/C (P 7,570.08, R1 7,588.95, S1 7,534.82, R2 7,624.21, S2 7,515.95, R3 7,643.08, S3 7,480.69) — but that is the wrong session. ATR(14) is never stated (only "ATR ... recomputed" in §20). KER(13, EMA 3) is given only as "upper inner band", no value. §21a gives the score (+0.22) with no signal × weight table and does not print the 0.25/0.20/0.10/0.15/0.15/0.15 weights. | §6 footnote and column; §11; §9; §21a; helper output | 2 | Rebuild RSI2 with the simple-mean definition (or show the smoothing and seed); state ATR(14) and KER numerically; print the §21a signal × weight table. |
| 3.4 Numbers reconcile | Internally: D-1 close 7,584.31 is identical in §1, §3, §4, §6, §11 narrative, §21c; pivots quoted on cards (P 7,570, R1 7,589, R2 7,624, S2 7,516, R3 7,643, R4 7,697, weekly P 7,546, R1 7,622) match §11; RSI2 in §6 = §8 ("~21", "~58"). Against the slice: D-1 close 7,584.31 vs cash 7,592.7 (Δ −8.4, above the 3-pt tolerance; full-day 7,582.1 is within 2.2); 03 Jun close 7,553.68 vs cash 7,565.2 (Δ −11.5 — beyond the 10-pt line, a Category 3 failure per the brief; the direction of the basis is the same on all five days, 4.7–11.5 below the CFD, so it reads as a systematic basis rather than a single wrong figure, but it exceeds tolerance and it is the close the pivots were built from); every D-1 O/H/L is 12–17 pts off (O 7,558 vs 7,541.3; H 7,592 vs 7,604.3; L 7,548 vs 7,535.0); pivots cannot reconcile to the D-1 session (report P 7,570.08 vs slice cash P 7,577.33 / report-own D-1 P 7,574.77; R1 7,588.95 vs 7,619.67 / 7,601.54). Cross-report: 29 May H and 01 Jun H/L contradict the 02 Jun and 04 Jun reports. ATR absent so §9/§21 ATR reconciliation is impossible. Minor text: "recovering roughly two-thirds of the prior day's loss" is 55% by the report's own closes. | §1, §3, §4, §6, §8, §11, §21b/c; helper; prior reports | 2 | Re-source D-1 O/H/L; rebuild pivots from D-1; state ATR; align 29 May / 01 Jun rows with prior reports. |
| 4.1 Pillars conclude | §8 ends "Indecision"; §9 ends "Trending (Bullish)" then consolidates to "TRANSITION with an upward bias" (two labels, but the reconciliation is written out); §10 ends "MIXED"; §12 labels each sub-pillar; §14 has no closing direction label (headwind is implicit). Strategy pillar (§21, scored here per the protocol): Trade 2 is labelled "regime: TRANSITION" yet is a pullback buy-limit at P — under the fixed rules TRANSITION → breakout side only, TREND → entry P + 0.10×(R1 − P) with stop P − 0.8×(P − S1) and TPs R1/R1.5/R2, RANGE → limits at S1/S1.5/S2; the card matches none. TP1 = +0.33R and TP2 = +0.9R instead of a 1R/2R ladder. Trade 3A is a breakout buy-stop, not the 57.5% retrace of a qualifying swing (≥ 2×ATR, 4–10 sessions, endpoints logged); its TP1 (7,621) is the swing's 0% anchor, i.e. the level the rule assigns to TP2; the stop (7,548) sits at the stated 04 Jun low with no 0.25×ATR buffer. Because ATR is not stated, the wide-stop flag, the 0.25×ATR buffer and the 3×ATR runner cap cannot be shown. Both live cards are built off D-2 pivots. | §8–§10, §12, §14, §21b | 2 | Rebuild Trade 2 to the template that matches the declared regime; rebuild 3A as a retrace entry with logged swing endpoints; state ATR. |
| 4.2 Peer/cross-asset interpreted | §10 gives a mechanism per counter (dollar → financial conditions and translation; VIX → risk regime; DAX → global risk factor), a confirmation column and an explicit contradiction flag carried to §14/§15. Minor: VIX "Rising (mildly)" over five sessions — the slice shows 16.53 (29 May) → 16.36 (04 Jun), lower on net with a mid-week bump. | §10; VIX slice | 4 | Align the VIX 5-day direction with the data. |
| 4.3 Synthesis reconciles tensions | KER vs regime is addressed in §9; §17-vs-§21a conflict is flagged in §21a; §16 addresses short-term indecision vs medium-term trend and gives an invalidation. Not reconciled: §16 says the view "respects the §9 Trending-Bullish regime" while the cards are built on the "TRANSITION" fork — and then the Trade 2 construction follows neither; §21a calls the direction "LONG (low conviction)" while its own score is below the threshold that defines a direction. | §9, §15–§18, §21a/b | 3 | Fix one regime label for the strategy block and construct cards to it. |
| 4.4 Calibrated language | §17 is exactly one sentence with one conditional clause; §3/§18 state confidence Medium; §13b tilt numeric. Mild over-statement: §1 "mildly LONG" and §21a "LONG (low conviction)" for a sub-threshold score. | §1, §3, §17, §18, §21a | 4 | Label a sub-threshold score NEUTRAL / no directional call. |
| 5.1 Data dated; staleness flagged | Every §4/§6 price dated; every §13a article dated; single-source O/H/L flagged with * in §6 and listed in §19/§20; weekly/monthly pivot inputs flagged single-source. Counter readings in §9/§10 (VIX, USDX, DAX) are approximate and undated beyond "04 June". | §4, §6, §9, §10, §13, §19, §20 | 4 | Date and source the counter levels. |
| 5.2 Assumptions up front | Anchor-override caveat exists in §2 and §20 but without the anchor time and it is not repeated on the cards; single-source propagation to cards is present ("weekly/monthly tiers single-source-indicative"); the choice to build daily pivots from the 03 Jun session is stated in §5/§11 but its consequence (stale pivot set for the 05 Jun session) is not surfaced. | §2, §5, §11, §19, §20, §21b caveats | 3 | Put the anchor time on the cards; state that the pivot set is D-2 if that choice is kept (better: rebuild from D-1). |
| 5.3 Red flags surfaced | §12 and §15 carry the risks (valuation, breadth, dollar, oil, hike odds); the §13d NFP collision is carried into both card caveat rows; NFP named the single watch item in §18. | §12, §13d, §15, §18, §21b | 5 | None. |
| 5.4 Restrictions honoured | No bracketed variable names, no module codes (M1–M5), no framework name, no ES-futures content, no CFD/retail quotes in the OHLC basis, instrument common names used. Single-source O/H/L are attributed (CNBC) and flagged, so they are not presented as corroborated. Concern short of a breach: the monthly pivot input H = 7,620.90 is a June print used as May's high, and the §6 O/H/L conflict with corroborated values in earlier reports — inputs of uncertain provenance, but flagged as indicative. No open breach → no override. | Whole report; §11 monthly; §6 | 4 | Fix the monthly pivot inputs; reconcile O/H/L provenance. |

## 2. Category roll-up

| Category | Level | Multiplier | Points | Justification |
|---|---|---|---|---|
| C1 Prompt adherence (20) | 4 (mean 3.67 of 3, 3, 5) | 0.85 | 17.00 | Variables largely respected; anchor time absent, only four distinct price providers, pivot session and monthly input drift. |
| C2 Structure (20) | 4 (mean 3.67 of 4, 3, 4) | 0.85 | 17.00 | All 21 sections present and ordered; §11 has a malformed empty table and a five-level daily pivot table; §9 metrics qualitative. |
| C3 Accuracy & evidence (25) | 3 (mean 2.75 of 3, 4, 2, 2) | 0.65 | 16.25 | Sources internally consistent (no fabrication), but RSI2 does not reproduce under the fixed method, ATR is not stated, pivots are built from D-2, D-1 O/H/L are 12–17 pts off the slice, the 03 Jun close is 11.5 pts off, and O/H/L contradict earlier reports. |
| C4 Reasoning & judgment (20) | 3 (mean 3.25 of 2, 4, 3, 4) | 0.65 | 13.00 | Cross-asset mechanism and synthesis are sound; both live cards depart from their M5 templates, regime label for the strategy block is inconsistent, ATR-dependent checks impossible. |
| C5 Currency & transparency (15) | 4 (mean 4.00 of 4, 3, 5, 4) | 0.85 | 12.75 | Data dated and single-source flags propagated; anchor time missing on cards; counter levels unsourced; no restriction breach. |
| **Total** | | | **76.00** | 17.00 + 17.00 + 16.25 + 13.00 + 12.75 = 76.00 → 76 |

## 3. Total, band, override check

- **Total: 76/100**
- **Band: High Trust (75–89)** — usable after light human review focused on the weakest categories (C3, C4); the strategy block should not be used as-is because both live cards are built off the D-2 pivot set and depart from the fixed card templates.
- **Overrides: none.** Hallucinated-source override not triggered — three spot-checked citations are named, dated and internally consistent, none impossible. Restriction-breach override not triggered — no synthesised price presented as corroborated, no futures/CFD basis, no module codes, brackets or framework name in the report. No cap applied; C1 unchanged.

## 4. Card Integrity

Lint rows (`qa/regen_20260906_qa1/lint_static/2026-06-05.csv`, verbatim):

| card_id | report_date | strategy | flags | dud |
|---|---|---|---|---|
| 2026-06-05_Trade_1 | 2026-06-05 | Trade 1 - Daily Directional | SUPPRESSED | False |
| 2026-06-05_Trade_2 | 2026-06-05 | Trade 2 - Pivot (buy limit daily P) | CLEAN | False |
| 2026-06-05_Trade_3A | 2026-06-05 | Trade 3A - Momentum-Pullback (breakout stop) | CLEAN | False |

Per-card integrity (100 − 40·#DUD − 10·#WARN, floor 0):

| card | #DUD | #WARN | integrity |
|---|---|---|---|
| 2026-06-05_Trade_1 | — | — | suppressed (excluded from the mean; the SUPPRESSED row is the compliant response to a score of 0.22 < 0.25) |
| 2026-06-05_Trade_2 | 0 | 0 | 100 |
| 2026-06-05_Trade_3A | 0 | 0 | 100 |

**Report-level Card Integrity = 100.0** (mean over the two non-suppressed cards). n_cards = 3 (including the suppressed row), n_duds = 0, n_warns = 0.

M5 construction assessment (feeds rows 4.1/4.3 above, not the integrity number):
- Trade 2 — LIMIT 7,570 sits below the D-1 close (report 7,584.31; slice cash 7,592.7) ✓; R = 58 pts = 0.96×ATR14 (60.39), within [18.1, 181.2] ✓; TP1 19 pts from entry, within 151.0 ✓. Defects: regime template not followed (see 4.1); TP ladder is +0.33R / +0.9R, not 1R / 2R; entry anchor P is the D-2 pivot (D-1 P is 7,577.33 on the slice, 7,574.77 from the report's own D-1 H/L/C); no ATR stated, so the wide-stop test is not shown; thesis invalidation (weekly P 7,546) is distinct from the stop ✓; single-source propagation present ✓; Unit 3 → entry + 0.2R = 7,582 ✓ (58 × 0.2 = 11.6).
- Trade 3A — STOP 7,593 sits above the report's D-1 close ✓ but only 0.3 pts above the slice cash close 7,592.7; R = 45 pts = 0.75×ATR14, within bounds ✓; TP1 28 pts from entry ✓. Defects: not a 57.5% retrace entry, no swing endpoints logged, no ≥ 2×ATR magnitude test; TP1 is the swing's 0% anchor (the level the rule gives to TP2); stop 7,548 sits at the stated 04 Jun low with no 0.25×ATR buffer, and 13 pts above the slice's actual D-1 cash low (7,535.0); TP2 (7,643) and TP3 (7,697) are D-2 pivot levels (R3/R4), not swing-derived extensions; invalidation (close below 7,570) distinct from stop ✓; Unit 3 → 7,602 ✓ (45 × 0.2 = 9).
- Trade 1 — suppression rule applied correctly for |0.22| < 0.25 ✓; but the score's signal × weight derivation is not printed, so the suppression cannot be audited.

## 5. Data reconciliation log

Slice = cash session (16:30–23:00 broker) unless stated. Tolerances (brief §4): close ≤ 3 pts, open/high/low ≤ 8 pts; > 10 pts on a close is a Category 3 failure.

| # | Section | Field | Report value | Slice value | Δ (report − slice) | Verdict |
|---|---|---|---|---|---|---|
| 1 | §6 row Fri 29 May | Open | 7,567* | 7,581.1 | −14.1 | Discrepancy (> 8) |
| 2 | §6 row Fri 29 May | High | 7,588* | 7,601.8 | −13.8 | Discrepancy (> 8); also contradicts 02 Jun report (7,599.38) and 04 Jun report (7,600) |
| 3 | §6 row Fri 29 May | Low | 7,560* | 7,567.9 | −7.9 | Consistent (≤ 8) |
| 4 | §6 row Fri 29 May | Close | 7,580.06 | 7,584.8 | −4.7 | Discrepancy (> 3), basis-sized |
| 5 | §6 row Mon 01 Jun | Open | 7,584* | 7,575.2 | +8.8 | Discrepancy (> 8) |
| 6 | §6 row Mon 01 Jun | High | 7,607* | 7,623.6 | −16.6 | Discrepancy (> 8) |
| 7 | §6 row Mon 01 Jun | Low | 7,578* | 7,568.5 | +9.5 | Discrepancy (> 8); contradicts corroborated 7,562.61 in the 02 Jun report |
| 8 | §6 row Mon 01 Jun | Close | 7,599.96 | 7,606.0 | −6.0 | Discrepancy (> 3), basis-sized |
| 9 | §6 row Tue 02 Jun | Open | 7,601* | 7,590.8 | +10.2 | Discrepancy (> 8) |
| 10 | §6 row Tue 02 Jun | High | 7,620.90 | 7,624.6 | −3.7 | Consistent |
| 11 | §6 row Tue 02 Jun | Low | 7,595* | 7,588.3 | +6.7 | Consistent |
| 12 | §6 row Tue 02 Jun | Close | 7,609.78 | 7,615.8 | −6.0 | Discrepancy (> 3), basis-sized |
| 13 | §6 row Wed 03 Jun | Open | 7,605.31 | 7,602.0 | +3.3 | Consistent |
| 14 | §6 row Wed 03 Jun | High | 7,605.35 | 7,608.0 | −2.7 | Consistent |
| 15 | §6 row Wed 03 Jun | Low | 7,551.22 | 7,556.0 | −4.8 | Consistent |
| 16 | §6 row Wed 03 Jun | Close | 7,553.68 | 7,565.2 | −11.5 | **Failure (> 10 on a close)** — the close used as the §11 pivot input; same-sign basis as the other four days, so systematic, but outside tolerance |
| 17 | §6 row Thu 04 Jun (D-1) | Open | 7,558* | 7,541.3 | +16.7 | Discrepancy (> 8) |
| 18 | §6 row Thu 04 Jun (D-1) | High | 7,592* | 7,604.3 | −12.3 | Discrepancy (> 8); §8 "resistance 7,592 (Thu high)" and the 3A stop-entry rest on it |
| 19 | §6 row Thu 04 Jun (D-1) | Low | 7,548* | 7,535.0 | +13.0 | Discrepancy (> 8); §8 "support 7,548" and the 3A stop rest on it |
| 20 | §6 row Thu 04 Jun (D-1) | Close | 7,584.31 | 7,592.7 (full-day 7,582.1) | −8.4 (+2.2 vs full-day) | Discrepancy vs cash (> 3); within basis of the full-day close |
| 21 | §6 RSI2 column | 03 Jun / 04 Jun | 20.8 / 57.5 | Slice closes: 16.23 / 35.21 | — | Discrepancy on basis |
| 22 | §6 RSI2 column | 03 Jun / 04 Jun | 20.8 / 57.5 | From report's own closes (fixed method): 14.9 / 35.3 | +5.9 / +22.2 | **Failure — does not reproduce under the stated definition** (reproduces only under an unstated Wilder smoothing: 20.9 / 57.6) |
| 23 | §11 daily pivots | Session used | 03 Jun (D-2) H/L/C | D-1 = 04 Jun | — | Wrong session; levels reproduce exactly from the stated 03 Jun inputs (P 7,570.08 … S3 7,480.69) |
| 24 | §11 daily P | P | 7,570.08 | 7,577.33 (cash) · 7,574.77 (report-own D-1 H/L/C) | −7.3 / −4.7 | Discrepancy |
| 25 | §11 daily R1 | R1 | 7,588.95 | 7,619.67 (cash) · 7,601.54 (report-own D-1) | −30.7 / −12.6 | Discrepancy — Trade 2 TP1 and 3A entry anchor |
| 26 | §11 daily S1 / S2 | S1 / S2 | 7,534.82 / 7,515.95 | 7,550.37 / 7,508.03 (cash) | −15.6 / +7.9 | Discrepancy |
| 27 | §11 daily R2 / R3 | R2 / R3 | 7,624.21 / 7,643.08 | 7,646.63 / 7,688.97 (cash) | −22.4 / −45.9 | Discrepancy — Trade 2 TP2, 3A TP2 |
| 28 | §11 weekly P | P (W/E 29 May) | 7,546.02 (implied H 7,588 / L 7,470 / C 7,580.06) | 7,563.63 (cash) | −17.6 | Discrepancy; flagged single-source in the report |
| 29 | §11 monthly pivots | May H input | implied H = 7,620.90 | report's own §1/§6: 7,620.90 printed on 02 Jun | — | Internal contradiction — a June high used as the May input |
| 30 | §9 / §21 | ATR(14) | not stated | 60.39 cash / 71.46 full-day | — | Missing — cannot reconcile |
| 31 | §9 / §10 | VIX 04 Jun | ~16.5 | 16.36 close (VIX slice) | +0.1 | Consistent |
| 32 | §10 / §12 / §14 | USDX | ~99.5, "two-month high" | 99.46 close, 99.578 high 03 Jun; 100.336 on 06 Apr | ~0 | Level consistent; "two-month high" loose (7-week high) |
| 33 | §10 | VIX 5-day direction | Rising (mildly) | 16.53 → 16.36 | — | Mild mislabel |
| 34 | §8 | "recovering roughly two-thirds" | ⅔ | 30.63 / 56.10 = 55% by report closes | — | Minor text over-statement |
| 35 | §21b Trade 3A | Stop vs D-1 low | 7,548 | slice D-1 cash low 7,535.0 | +13.0 | Stop sits inside the actual D-1 range |
| 36 | §21b Trade 3A | Stop-entry vs D-1 close | 7,593 | 7,592.7 cash close | +0.3 | Marginal — effectively at the close on the slice basis |
