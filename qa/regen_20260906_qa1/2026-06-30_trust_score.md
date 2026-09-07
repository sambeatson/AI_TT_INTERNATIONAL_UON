# Trust Score — 2026-06-30 — SP500_Report_30Jun2026.md

Run: `regen_20260906_qa1` · D = 2026-06-30 · asset US500 · D-1 = 2026-06-29 (Monday, a completed
cash session present in `data/slices/US500/US500_upto_2026-06-29.csv`).

**Headline finding.** The report's entire validated block is one session stale. It declares
(§2) that "the validated completed-session block ends Friday 26 June 2026" and builds §6, §8,
§9, §11, §16 and all three §21b cards on 22–26 Jun. The slice contains a complete 29 Jun cash
session (O 7403.0 / H 7450.6 / L 7355.1 / C 7443.00, RSI2 78.08). Every D-1-dependent number in
the report is therefore taken from the wrong session. The report also quotes a "30 June
in-progress" price of ~7,436 (+1.1%) in §1, §3, §16 and §19; 7436.1 is a 29 June 20:00-broker
print in the slice, i.e. D-1 data relabelled as live D-session data.

Helper output used throughout (verbatim):

```
LAST 5 SESSIONS - cash-session OHLC (16:30-23:00 broker) with RSI2 on cash closes:
2026-06-23  7370.4 7431.8 7356.2 7374.4   0.00
2026-06-24  7389.0 7438.0 7346.0 7372.3   0.00
2026-06-25  7427.9 7432.6 7332.9 7365.9   0.00
2026-06-26  7323.8 7402.1 7303.1 7335.8   0.00
2026-06-29  7403.0 7450.6 7355.1 7443.0  78.08
D-1 session used for daily pivots: 2026-06-29
ATR14 (cash-session bars): 101.58    ATR14 (full-day bars): 109.81
DAILY PIVOTS from D-1 cash session:  P 7416.23 R1 7477.37 S1 7381.87 R2 7511.73 S2 7320.73 R3 7572.87 S3 7286.37
WEEKLY PIVOTS from prior week (2026-06-22..2026-06-26, cash): P 7392.57 R1 7482.03 S1 7246.33 R2 7628.27 S2 7156.87 R3 7717.73 S3 7010.63
SWING 5d  (cash): high 7450.60 (2026-06-29)  low 7303.10 (2026-06-26)
SWING 25d (cash): high 7624.60 (2026-06-02)  low 7243.10 (2026-06-09)
D-1 cash close 7443.00   D-1 full-day close (23:45 bar) 7440.30
RSI2 recomputed from the REPORT'S OWN closes (7448.30, 7365.46, 7358.22, 7357.49, 7354.02): n/a, n/a, 0.0, 0.0, 0.0
```

Supplementary (same slice, same method, extending the helper's window): 22 Jun cash session
O 7513.1 / H 7538.8 / L 7467.3 / C 7479.3, RSI2 0.00; 6–8-session swing high 7538.80 (22 Jun),
low 7303.10 (26 Jun), magnitude 235.7; June-to-29 cash H 7624.60 / L 7243.10 / C 7443.00.

## 1. Section 7 checklist

| Item | Reviewer notes | Evidence observed | Score 0–5 | Action required |
|---|---|---|---|---|
| 1.1 Variables respected | Asset correct (S&P 500 cash index, 503 constituents; ES explicitly confirmation-only). Counters correct and in order (USDX · VIX · DAX 40). Currency/unit correct (index points · USD); tick 0.01 never stated and §6 O/H/L are given to whole points while closes are to 2dp. Six sources listed. **Breach: as-of is the 26 Jun NY close, not D-1 (29 Jun).** Daily-open anchor overridden to 00:00 UK against the 07:00 UK M1 instance value — disclosed, but a deviation. | §2 (Market Definition table, "As-of date", "Daily-open anchor", closing note); §4; §10; §20 bullet 1; §13 header | 1 | Rebuild the whole report as-of the 29 Jun NY close. Restore the 07:00 UK anchor or carry a verifiable override authority. State tick 0.01 and use one price precision. |
| 1.2 Coverage & currency consistent | Units/currency consistent everywhere (no FX or unit drift). Dates are not: §6, §8, §11, §13c and §21c all run 22–26 Jun, so the five-session window ends two calendar days before D and omits the completed D-1 session. §1/§3/§16/§19 additionally present a live in-progress **30 June** quote (~7,436, +1.1%) as evidence; that value corresponds to a 29 June intraday print in the slice. | §1 para 1 and closing sentence; §3 rationale; §6 rows; §13c/§13d; §16 para 2; §19 bullet 4 | 1 | Shift the five-session window to 23–29 Jun. Remove all D-session (30 Jun) price references; the report may not know them. |
| 1.3 Audience & tone | Consistently senior-institutional. Byline states Senior US Equity Strategist · Trading & risk review. No retail framing, no promotional language, risk-first phrasing throughout §15/§18/§21. | Header line 3; §1; §18; §21d limitations boilerplate | 5 | None. |
| 2.1 Sections present & ordered | All of §1–§21 present in order. §13 carries a, b, c and d; §21 carries a, b, c and d including the limitations boilerplate. Nothing omitted, nothing transposed. | Headings §1…§21d | 5 | None. |
| 2.2 Scorecard as a table | §6 is a proper table with Date/O/H/L/C/RSI2/Trend/Sources/Validation, but collapses Source A and Source B into one "Sources" column. §11 daily table is R5→S5 (five levels a side) instead of the specified R3→P→S3; the monthly table omits R3 entirely (R2→S3 only); the weekly table is correct at three a side. | §6 header row; §11 daily / weekly / monthly tables | 3 | Split §6 into Source A and Source B columns. Emit exactly R3/R2/R1/P/S1/S2/S3 for all three pivot timeframes. |
| 2.3 Method steps visible | §4 lists observations, §5 explains normalization and the weighted-median consensus build, so observations→classification→consensus is visible. §8 is candle-by-candle across all five sessions and ends in an explicit sequence assessment with an overlap/range-collapse justification. §9 gives regime with overlap, persistence, range-position, VOLator slope and KER. Five chart references present as pandoc-dropped image placeholders with captions — accepted as evidence, noted. | §4→§5; §8 per-session paragraphs + "Sequence assessment"; §9; §7 captions Chart 1–5 | 5 | None (chart images dropped by pandoc — no action). |
| 3.1 Quantitative claims sourced | Large numbers in §1, §12 and §14 carry no source and no pointer to §4/§6/§13: "Apple −6%", "Microsoft −3%", "roughly three rate hikes", "dollar 13-month highs near 101.3", "Q2 earnings growth ~23%", "first-move odds ~60% by September", "PCE 4.1%", "28% foreign revenue base", "index underperformed peers −2% on the week", "10-year yield easing toward 4.4%", "Brent −4.3% on 24 Jun", "VIX ~18.4". §13c states Micron "Rev $41.5bn, EPS $25.11" with no source and no use anywhere else. | §1; §12 all six blocks; §14 all six bullets; §13c row 2 | 1 | Attach a named, dated source or an explicit §4/§6/§13a cross-reference to every number in §1, §12, §14 and §13c. |
| 3.2 Citations exist & contain data | Structure is good: §4 and §13a both give named, dated sources with ≤15-word derivation quotes. Content is not. Three §13a rows dated the same 26 Jun describe mutually exclusive tape — CNBC "Nasdaq posts fifth losing session as chip stocks tumble", Bloomberg "S&P halts four-day drop to end jittery week", Schwab "Stocks rebound early". The report's own §6 and §13c make 26 Jun a down day (−0.05%), and the slice makes it a down day too (7365.9→7335.8); the Bloomberg and Schwab claims are false for their stated date and match the omitted 29 Jun session (7335.8→7443.0, +1.5%). §13b never reconciles the three. Separately, §4 presents six "independent" observations that all agree to the cent at 7,354.02, including a delayed Yahoo web quote and a Bloomberg TV value quoted as "≈7,354" but normalized to 7,354.02 — precision the cited source does not carry. Spot-check verdicts: Schwab "3% off all-time highs" is internally consistent with the report's own 7,570 June peak (−2.85%) — PASS; Bloomberg — FAIL (claim impossible for its stated date on both the report's data and the slice); §4 Bloomberg TV "≈7,354"→7,354.02 — FAIL (manufactured precision). | §13a rows 1, 3, 6; §13b; §4 rows 4 and 6 with the six-observation footnote | 1 | Re-date or drop the two §13a rows whose content belongs to 29 Jun. Do not normalize an approximate quote to two decimals. Reconcile same-date contradictory headlines in §13b or drop them. |
| 3.3 Calculations transparent | Reproduces: RSI2 method stated and the report's own closes give 0.0/0.0/0.0 for rows 3–5 (helper `--closes`) — self-consistent arithmetic. All three §11 pivot sets reproduce exactly from the report's own H/L/C (daily P 7,352.34→7,352.3, R1 7,373.68→7,373.7, S1 7,332.68→7,332.7, R2 7,393.34, S2 7,311.34, R3 7,414.68, S3 7,291.68; weekly and monthly likewise from implied H/L/C of 7,485.9/7,330.9/7,354.1 and 7,569.9/7,330.9/7,354.1). §21a score reproduces: −0.25−0.20−0.15−0.045−0.078−0.05 = −0.773 → −0.77, weights sum to 1.00. Does not reproduce: **ATR(14) is never stated as a number** — it is only inferrable as 56 from "3.5×ATR cap of 196 pts" and "+0.25×ATR" = 14; the slice ATR14 is 101.58 (cash) / 109.81 (full-day). **KER(13, EMA 3) parameters not stated**, only the value −0.52. **§13b tilt does not reproduce from its own stated weights**: institutional 1.0 × 2 bullish, media 0.5 × 2 bearish, 2 mixed at 0 gives (+2.0 −1.0)/4.0 = **+0.25**, not −0.30 — the sign is inverted against the method the report itself states. **§21c R denominator is inconsistent**: rows 1–2 imply R≈145 (26 pts→+0.18R, 82 pts→+0.56R) while rows 3–5 imply R≈50–57 (12 pts→+0.21R, 4 pts→+0.07R, 1 pt→+0.02R). | §6 footnote; §11 all three tables; §20 bullets 3–5; §21a; §13b; §21c rows | 2 | State ATR(14) and KER(13, EMA 3) as numbers in §9 and reuse them in §21b. Recompute §13b from the stated class weights or restate the weights. Make the §21c R denominator explicit per row. |
| 3.4 Numbers reconcile | Internal cross-section reconciliation is clean: 7,354.02 is identical in §1, §3, §4, §6 and the §21b Trade 1 entry; §11 daily P/R1/S1 (7,352.3 / 7,373.7 / 7,332.7) are exactly the levels quoted on the Trade 2 card; RSI2 0 in §6 matches §8 and the §21a input. But the reconciled value is the wrong session's: D-1 cash close is 7,443.00, so the anchor is off by **−88.98 pts** — far past the 10-pt Category 3 failure threshold. ATR cannot be reconciled between §9 and §21 because §9 never states it. 23 of the 25 O/H/L/C values in §6 are outside the brief's basis tolerance (≤3 pts close, ≤8 pts O/H/L) — see §5 below. §6's 22 Jun row also contradicts the immediately preceding report (`SP500_Daily_Report_29Jun2026.md`) for the same session: close 7,448.30 vs 7,472.79 there, RSI2 0 vs 74.3 there, and 26 Jun low 7,331 vs 7,294.18 there. | §1/§3/§4/§6/§21b entry; §11 vs Trade 2 card; §9 (no ATR); §6 vs slice; `reports/md/SP500_Daily_Report_29Jun2026.md` §6 | 1 | Rebuild §6 from the 23–29 Jun cash sessions and re-derive every downstream number. Reconcile the 22–26 Jun block against the 29 Jun report before publishing. |
| 4.1 Pillars conclude | Every pillar ends in an explicit label: §8 "Judgement label: Bearish continuation", §9 "Bias: Bearish", §10 "Aggregate cross-asset confirmation: CONFIRM", §12 an italic Direction line on all six blocks, §14 a direction on each bullet. Labels match their own content. Two internal blemishes: §9 writes "VIX elevated near 18.4 (above the 'elevated' 20 watch line is not yet breached but it is rising)", which is self-contradictory as written; and §9 asserts TREND_DOWN on an overlap ratio of 0.63 without showing the gate arithmetic that makes a range-like overlap compatible with a trend label (§20 only asserts "dual-gate not engaged"). | §8 final line; §9 "Bias" and VOLator para; §10 aggregate line; §12 italic Direction lines; §14 bullets | 4 | Fix the §9 VIX sentence. Show the dual-gate test explicitly when overlap exceeds the range threshold. |
| 4.2 Peer/cross-asset interpreted | §10 gives a real transmission mechanism per counter, not a correlation list: USDX → tighter global financial conditions plus lower multinational earnings translation; VIX → demand for downside protection / risk-off positioning; DAX → common global-risk factor testing whether the read is US-idiosyncratic. Each row carries a status and an implication for the index, and the aggregate is stated. Weakness: no counter carries a dated numeric observation (only "Rising" / "Falling/Flat"), so none of the three mechanisms is tied to a sourced level or move. | §10 table (Mechanism and Implication columns); §10 aggregate line | 4 | Add a dated 5-day numeric move for each counter and source it. |
| 4.3 Synthesis reconciles tensions | The report does reconcile the tensions it can see: §9 explicitly resolves KER against the regime ("agrees, raises confidence, no contradiction to resolve"); §13b explicitly resolves the institutional-vs-price divergence and rules price/tape more reliable near-term; §15 is a genuine two-sided balance; §16 names its own invalidation (daily close above weekly P 7,390) and the counter-trend bounce; §21a explicitly checks itself against §17. **Card construction (scored here) is where the synthesis fails.** All three cards inherit the 26 Jun anchor rather than the D-1 close 7,443.00. All three are built on an implied ATR of 56 against a slice ATR14 of 101.58, so every ATR-derived buffer, cap and qualification test is understated by ~45%. Trade 3A's qualifying swing (7,486→7,331, 155 pts) fails the M5 "≥2×ATR" gate on the true ATR (2×101.58 = 203.2). Trade 2 should be suppressed under M5 because §19 declares every pivot tier single-source-indicative; the report waives the rule via a "corroboration-leniency directive" recorded in §20 rather than emitting a SUPPRESSED row. Trade 1's TP3 (7,186) is not beyond TP2 (7,062) — the linter's WARN_TP3_ORDER. Trade 2's R of 19 pts is 0.17×ATR, under the 0.3×ATR floor. Trade 1's Unit-3 rule is labelled "entry +0.2R" while its stated level 7,325 is entry −0.2R (correct for a short) — the sign label is wrong. Trade 2's entry is written "Sell stop/limit", leaving the entry mode ambiguous where the two modes sit on opposite sides of the close. | §9 Kaufman para; §13b divergence flag; §15; §16 para 2; §21a; §21b all three cards; §19 bullet 3; §20 final bullet; lint rows | 2 | Rebuild all three cards from the D-1 session (see the feedback file for the numeric conditions). Emit a SUPPRESSED row rather than waiving the M5 suppression rule. Fix the Unit-3 sign label and the Trade 2 entry mode. |
| 4.4 Calibrated language | §17 is exactly one sentence, no hedge stacking. Confidence is stated where required — §3 "High", repeated in §18. §16 gives a directional expectation with an explicit invalidation level rather than a bare assertion. But the calibration is wrong for the evidence: "High" confidence and a "confirmed Trending–Bearish regime across both windows" rest on an anchor that is a full session stale, and §15 leans on "RSI2 pinned at 0" when the D-1 RSI2 on the slice is 78.08. High confidence is not supportable on inputs the report has not actually observed. | §17; §3 Confidence cell; §18 first line; §15 upside-risk cell | 3 | Downgrade confidence, or restate it after rebuilding on D-1 data. |
| 5.1 Data dated; staleness flagged | Dating discipline is present in form: every §6 row, every §4 row (with time), and every §13a article is dated; single-source-indicative O/H/L are flagged in §6, §11 and §19 and propagated onto every card. The staleness that actually matters is not flagged but affirmatively mis-stated: §2 asserts the completed block ends Friday 26 June, and §19 labels a 29 June price as "the 30 June in-progress quote (~7,436)". The report never tells the reader that a completed 29 June session exists and was not used. | §6 Date column; §4 Date/Time column; §13a Date column; §2 closing note; §19 bullets 1, 2 and 4 | 2 | Flag the true last completed session (29 Jun) and use it, or state explicitly why it is excluded. |
| 5.2 Assumptions up front | Strong. The anchor override is stated twice, in §2 and again in §20 with the instance default named. The single-source-indicative pivot propagation is stated in §11 ("propagated to the §21 strategy suppression logic"), §19 and §20, and repeated in the Caveats row of all three cards. The consensus method and its down-weighting are explained in §5. The backtest states its own assumptions (frozen at t−1, SL-first tick priority, slippage 0). Weight basis and the weight-lock window are declared in §20. | §2 anchor row; §20 bullets 1, 2, 3 and 7; §11 source-status para; §19; §21b Caveats rows; §5; §21c footnote | 5 | None. |
| 5.3 Red flags surfaced | §12 carries a two-way-risk block and §15 is a full bull/bear balance with four downside items including the specific 7,331→7,311→7,295 break sequence. The §13d highest-impact event (2 Jul NFP) is carried into the Caveats of all three cards as a collision. The wide-stop condition (1R > 1×ATR) is surfaced on Trade 1. The live counter-trend bounce is surfaced on every card and in §16 and §21a. The reversal risk from the 26 Jun compression doji is raised in §8 despite cutting against the report's own bearish call. | §12 catalysts block; §15 both columns; §13d; §21b Caveats × 3; §8 judgement line; §16 para 2 | 5 | None. |
| 5.4 Restrictions honoured | Honoured: ES futures marked confirmation-only; no retail CFD quotes in the OHLC basis; instrument common names used; no bracketed variable names; framework name absent. **Breached, three ways.** (i) Module/stage codes leak into the report body: §20 "M-stage §13b primary-asset value −0.30" and "Step-4 synthesis". (ii) Synthesised price is presented as sourced: §4's footnote states the five sessions' intraday high/low are "reconstructed from session reporting", yet those same values sit in a table headed "Validated OHLC + RSI2" with a Validation column reading "CORROBORATED (close Δ0.00)" on all five rows — and they then drive every §11 pivot and every card level. Reconstructed values do not belong in a table that certifies corroboration. (iii) The as-of specification (NY close of D-1) is overridden in practice by using the 26 Jun close, while live in-progress D-session prices (~7,436, +1.1%) are used as evidence in §1, §3 and §16. | §20 bullets 5 and 6; §4 footnote vs §6 title and Validation column; §2 as-of row; §1, §3, §16, §19 bullet 4 | 1 | Strip "M-stage" and "Step-4". Keep reconstructed O/H/L out of the validated/corroborated table or re-title the column per value. Remove D-session prices. |

## 2. Category roll-up

| Category | Level | Multiplier | Points | Justification |
|---|---|---|---|---|
| C1 Prompt adherence (max 20) | 1 | 0.20 | 4.00 | Rows 1.1/1.2/1.3 = 1/1/5, mean 2.33 → level 2; the restriction-breach override (row 5.4) drops C1 one level to 1. Asset, counters, currency and source count are right; the as-of session, the coverage window and the daily-open anchor are all wrong. |
| C2 Structure (max 20) | 4 | 0.85 | 17.00 | Rows 2.1/2.2/2.3 = 5/3/5, mean 4.33 → 4. Every section and sub-section present and ordered and every method step visible; the only structural defects are §6's merged source column and §11's non-standard pivot ladders (R5–S5 daily, missing monthly R3). |
| C3 Accuracy & evidence (max 25) | 1 | 0.20 | 5.00 | Rows 3.1/3.2/3.3/3.4 = 1/1/2/1, mean 1.25 → 1. The stated anchor is 88.98 pts from the D-1 cash close, 23 of 25 §6 OHLC values fall outside basis tolerance, §13b's tilt contradicts its own weighting, ATR is never stated, and two §13a citations are impossible for their stated date. Internal arithmetic (pivots, RSI2, §21a) does reproduce, which is what keeps this above 0. |
| C4 Reasoning & judgment (max 20) | 3 | 0.65 | 13.00 | Rows 4.1/4.2/4.3/4.4 = 4/4/2/3, mean 3.25 → 3. Pillar labels, the cross-asset mechanism and the explicit tension-resolution passages are genuinely good; card construction (scored here) inherits the wrong anchor and a ~45%-understated ATR, and "High" confidence is not calibrated to inputs the report never observed. |
| C5 Currency, restrictions & transparency (max 15) | 3 | 0.65 | 9.75 | Rows 5.1/5.2/5.3/5.4 = 2/5/5/1, mean 3.25 → 3. Assumption disclosure and red-flag surfacing are exemplary; the staleness that matters is mis-stated rather than flagged, and three restrictions are breached. |
| **Total** | — | — | **48.75 → 49** | Sum of category points, rounded to a whole number. |

## 3. Total, band, override check

- Raw total: 4.00 + 17.00 + 5.00 + 13.00 + 9.75 = **48.75 → 49**.
- Band for 49: **Low Trust (40–59)**.
- **Restriction breach override: APPLIED.** Framework §6 restriction-breach rule. Three stated
  restrictions are openly violated (§5.4 above): module/stage codes in §20; reconstructed
  intraday O/H/L presented inside a "Validated … CORROBORATED" table and used as pivot and card
  inputs; and D-session prices used as evidence against an as-of-D-1-close specification. Effects:
  C1 reduced by one level (2 → 1, already applied in the roll-up above) and the total capped at
  Moderate Trust (74). **The cap is not binding** — 49 already sits below it. Final total **49**,
  band **Low**.
- **Hallucinated-source override: CONSIDERED, NOT APPLIED.** Two §13a citations (Bloomberg
  "S&P halts four-day drop", Schwab "Stocks rebound early") describe a session that did not occur
  on their stated date of 26 Jun and does match the omitted 29 Jun session, and §4 normalizes a
  Bloomberg TV "≈7,354" to 7,354.02. These are scored hard under row 3.2 (score 1). I did not fire
  the override because the sources are named, real outlets carrying plausible content, and a single
  consistent one-session date shift explains all of it — the diagnosis is systematic staleness, not
  invention. Firing the override would zero C3 and hide the reconciliation findings that the
  regeneration agent actually needs. Recorded here so the call is auditable.
- Override recorded for the roll-up CSV: `restriction_breach`.

## 4. Card Integrity

Linter rows, verbatim from `qa/regen_20260906_qa1/lint_static/2026-06-30.csv`:

| card_id | report_date | strategy | flags | dud |
|---|---|---|---|---|
| 2026-06-30_Trade_1 | 2026-06-30 | Trade 1 - Daily Directional | WARN_TP3_ORDER | False |
| 2026-06-30_Trade_2 | 2026-06-30 | Trade 2 - Pivot (sell stop below P) | WARN_R_TINY(0.17xATR) | False |
| 2026-06-30_Trade_3A | 2026-06-30 | Trade 3A - Momentum-Pullback (57.5% rally-sell) | CLEAN | False |

Per-card integrity — 100 − 40·(#DUD) − 10·(#WARN), floored at 0:

| Card | #DUD | #WARN | Integrity |
|---|---|---|---|
| 2026-06-30_Trade_1 | 0 | 1 | 100 − 10 = **90** |
| 2026-06-30_Trade_2 | 0 | 1 | 100 − 10 = **90** |
| 2026-06-30_Trade_3A | 0 | 0 | **100** |

Non-suppressed cards: 3 of 3 (no card is marked suppressed in the report or the baseline).
**Report Card Integrity = (90 + 90 + 100) / 3 = 93.3.**

Counts for the roll-up: n_cards 3 · n_duds 0 · n_warns 2.

Note the separation the protocol requires: 93.3 measures only the static geometry the linter
enforces. It does not measure whether the cards are built on the right session — they are not, and
that is scored under row 4.3 and detailed in the feedback file.

## 5. Data reconciliation log

Basis tolerance per the brief: |Δ| ≤ 3 pts on a close, ≤ 8 pts on an open/high/low is consistent.
Slice values are cash-session (16:30–23:00 broker = 09:30–16:00 ET). Δ = report − slice.

### 5.1 As-of session

| Section | Report value | Slice value | Delta | Verdict |
|---|---|---|---|---|
| §2 "validated completed-session block ends Friday 26 June 2026" | last completed session = 2026-06-26 | last completed session = 2026-06-29 (392 M15 bars, cash session complete) | one full session | **FAIL** — the as-of session is not D-1. Root cause of every row below. |
| §1/§3/§4/§6/§21b anchor close | 7,354.02 (26 Jun) | 7,443.00 (29 Jun cash close; 7,440.30 full-day) | −88.98 | **FAIL** — >10 pts, Category 3 failure. |
| §1/§3/§16/§19 "30 June in-progress quote ~7,436, +1.1%" | ~7,436 attributed to 30 Jun intraday | 7,436.1 is the 2026-06-29 20:00 broker bar close | same value, wrong date | **FAIL** — D-1 data presented as live D-session data. |

### 5.2 §6 Validated OHLC table, row by row

| Section | Report value | Slice value | Delta | Verdict |
|---|---|---|---|---|
| §6 22 Jun Open | 7,474 | 7,513.1 | −39.1 | FAIL (>8) |
| §6 22 Jun High | 7,486 | 7,538.8 | −52.8 | FAIL (>8) |
| §6 22 Jun Low | 7,420 | 7,467.3 | −47.3 | FAIL (>8) |
| §6 22 Jun Close | 7,448.30 | 7,479.3 | −31.00 | FAIL (>10, Cat-3 failure) |
| §6 23 Jun Open | 7,447 | 7,370.4 | +76.6 | FAIL (>8) |
| §6 23 Jun High | 7,458 | 7,431.8 | +26.2 | FAIL (>8) |
| §6 23 Jun Low | 7,350 | 7,356.2 | −6.2 | PASS (≤8) |
| §6 23 Jun Close | 7,365.46 | 7,374.4 | −8.94 | FAIL (>3) |
| §6 24 Jun Open | 7,370 | 7,389.0 | −19.0 | FAIL (>8) |
| §6 24 Jun High | 7,405 | 7,438.0 | −33.0 | FAIL (>8) |
| §6 24 Jun Low | 7,352 | 7,346.0 | +6.0 | PASS (≤8) |
| §6 24 Jun Close | 7,358.22 | 7,372.3 | −14.08 | FAIL (>10, Cat-3 failure) |
| §6 25 Jun Open | 7,361 | 7,427.9 | −66.9 | FAIL (>8) |
| §6 25 Jun High | 7,411 | 7,432.6 | −21.6 | FAIL (>8) |
| §6 25 Jun Low | 7,351 | 7,332.9 | +18.1 | FAIL (>8) |
| §6 25 Jun Close | 7,357.49 | 7,365.9 | −8.41 | FAIL (>3) |
| §6 26 Jun Open | 7,355 | 7,323.8 | +31.2 | FAIL (>8) |
| §6 26 Jun High | 7,372 | 7,402.1 | −30.1 | FAIL (>8) |
| §6 26 Jun Low | 7,331 | 7,303.1 | +27.9 | FAIL (>8) |
| §6 26 Jun Close | 7,354.02 | 7,335.8 | +18.22 | FAIL (>10, Cat-3 failure) |
| §6 29 Jun row (O/H/L/C) | **absent** | 7,403.0 / 7,450.6 / 7,355.1 / 7,443.0 | whole row missing | **FAIL** — the D-1 session is not in the table at all. |

23 of 25 stated values are outside tolerance; four of the five closes fail; three closes fail by
more than 10 pts. The two passes (23 Jun and 24 Jun lows) are within 6.2 pts.

### 5.3 RSI2

| Section | Report value | Slice value | Delta | Verdict |
|---|---|---|---|---|
| §6 RSI2, 22 Jun | 0 | 0.00 (cash closes 7,502.3 → 7,494.2 → 7,479.3, mean gain 0) | 0.0 | PASS |
| §6 RSI2, 23–26 Jun | 0, 0, 0, 0 | 0.00, 0.00, 0.00, 0.00 | 0.0 | PASS |
| §6 RSI2 recomputed from the report's own closes (helper `--closes`) | 0, 0, 0, 0, 0 | rows 3–5 = 0.0, 0.0, 0.0 (rows 1–2 need prior closes) | 0.0 | PASS — the report's RSI2 arithmetic is self-consistent. |
| D-1 RSI2 (the value that should drive §8/§9/§15/§21a) | 0, described as "deeply oversold" and "pinned at 0" | 78.08 (29 Jun) | −78.08 | **FAIL** — the oversold premise of §1, §9, §15 and §21a does not hold at D-1. |
| §6 22 Jun RSI2 vs the preceding report | 0 | `SP500_Daily_Report_29Jun2026.md` §6 states 74.3 for the same session | 74.3 | Cross-report inconsistency — the slice supports this report's 0, not the 29 Jun report's 74.3, but the two reports must not disagree on a settled session. |

### 5.4 §11 pivots

Reproduction from the report's own inputs (the brief's test) — all three timeframes pass:

| Section | Report value | Recomputed from the report's own H/L/C | Delta | Verdict |
|---|---|---|---|---|
| §11 daily P (from 26 Jun H 7,372 / L 7,331 / C 7,354.02) | 7,352.3 | (7,372+7,331+7,354.02)/3 = 7,352.34 | 0.04 | PASS |
| §11 daily R1 / S1 | 7,373.7 / 7,332.7 | 2P−L = 7,373.68 · 2P−H = 7,332.68 | 0.02 | PASS |
| §11 daily R2 / S2 | 7,393.3 / 7,311.3 | P±(H−L) = 7,393.34 / 7,311.34 | 0.04 | PASS |
| §11 daily R3 / S3 | 7,414.7 / 7,291.7 | H+2(P−L) = 7,414.68 · L−2(H−P) = 7,291.68 | 0.02 | PASS |
| §11 weekly (implied H 7,485.9 / L 7,330.9 / C 7,354.1) | P 7,390.3, R1 7,449.7, S1 7,294.7, R2 7,545.3, S2 7,235.3, R3 7,604.7, S3 7,139.7 | all seven reproduce to ≤0.1 | ≤0.1 | PASS |
| §11 monthly (implied H 7,569.9 / L 7,330.9 / C 7,354.1) | P 7,418.3, R1 7,505.7, S1 7,266.7, R2 7,657.3, S2 7,179.3, S3 7,027.7 | all six reproduce to ≤0.1; **R3 not published** | ≤0.1 | PASS on arithmetic, FAIL on completeness (missing R3; daily table adds non-standard R4/R5/S4/S5). |

Pivot inputs and outputs against the slice — all fail, because the source session is wrong:

| Section | Report value | Slice value | Delta | Verdict |
|---|---|---|---|---|
| §11 daily P | 7,352.3 (from 26 Jun) | 7,416.23 (from 29 Jun cash) | −63.93 | FAIL |
| §11 daily R1 | 7,373.7 | 7,477.37 | −103.67 | FAIL |
| §11 daily S1 | 7,332.7 | 7,381.87 | −49.17 | FAIL |
| §11 daily R2 / S2 | 7,393.3 / 7,311.3 | 7,511.73 / 7,320.73 | −118.43 / −9.43 | FAIL |
| §11 daily R3 / S3 | 7,414.7 / 7,291.7 | 7,572.87 / 7,286.37 | −158.17 / +5.33 | FAIL / marginal |
| §11 weekly P | 7,390.3 | 7,392.57 (22–26 Jun cash week) | −2.27 | PASS |
| §11 weekly R1 / S1 | 7,449.7 / 7,294.7 | 7,482.03 / 7,246.33 | −32.33 / +48.37 | FAIL — the weekly high/low inputs are wrong (report implies H 7,485.9 / L 7,330.9 vs slice week H 7,438.0 / L 7,303.1) even though P happens to land close. |
| §11 monthly P | 7,418.3 | 7,436.90 (June-to-29 cash H 7,624.60 / L 7,243.10 / C 7,443.00) | −18.60 | FAIL |
| §11 monthly implied H / L | 7,569.9 / 7,330.9 | 7,624.60 / 7,243.10 | −54.70 / +87.80 | FAIL |

### 5.5 ATR, KER and swings

| Section | Report value | Slice value | Delta | Verdict |
|---|---|---|---|---|
| ATR(14) — never stated; implied by "3.5×ATR cap of 196 pts" (§21b Trade 1) and "+0.25×ATR" = 14 pts | 56 (implied) | 101.58 cash / 109.81 full-day | −45.6 (−45%) | **FAIL** — and a stated-value omission under row 3.3. Every ATR-derived buffer, cap and gate on all three cards is understated. |
| §8/§21b 5-day swing high | 7,486 (22 Jun) | 7,450.60 (29 Jun) — 22 Jun is no longer in the 5-session window | +35.40 | FAIL |
| §8/§21b 5-day swing low | 7,331 (26 Jun) | 7,303.10 (26 Jun) | +27.90 | FAIL — right session, wrong level. |
| §9 25-session range top ("17 June peak 7,570") | 7,570 | 7,624.60 (2 Jun) | −54.60 | FAIL |
| §9 25-session range bottom (implied by "bottom decile", 7,331–7,354 zone) | ~7,331 | 7,243.10 (9 Jun) | +87.90 | FAIL — with the D-1 close at 7,443.00 and the 25-day range 7,243.10–7,624.60, the range position is ~52nd percentile, not the bottom decile. |
| §9 KER(13, EMA 3) | −0.52, "Trending Down — Strong" | parameters not stated by the report; not independently reproducible from the slice via the helper | n/a | Cannot verify — scored as a transparency gap under row 3.3, not as a numeric discrepancy. |
| §21b Trade 3A swing magnitude vs the M5 ≥2×ATR gate | 155 pts (7,486→7,331), asserted "≥2×ATR" | 2×ATR14 = 203.2 (cash) / 219.6 (full-day) | −48.2 | **FAIL** — the report's own swing does not qualify on the true ATR. The qualifying 4–10-session swing is 7,538.80 (22 Jun) → 7,303.10 (26 Jun), magnitude 235.7. |

### 5.6 Derived quantities

| Section | Report value | Recomputed | Delta | Verdict |
|---|---|---|---|---|
| §21a direction score | −0.77 | −0.25 −0.20 −0.15 −0.045 −0.078 −0.05 = −0.773 | 0.003 | PASS — reproduces from §20's stated contributions; weights sum to 1.00. |
| §13b sentiment tilt | −0.30 | From the report's own class weights (institutional 1.0, media 0.5): (2×1.0 −2×0.5)/4.0 = **+0.25** | 0.55, sign inverted | **FAIL** — does not reproduce from the stated method; propagates into §21a (−0.30×0.15 = −0.045). |
| §21c Trade 1 mean R | +0.21 | (0.18+0.56+0.21+0.07+0.02)/5 = 0.208 | 0.002 | PASS |
| §21c implied R per row | rows 1–2 imply R ≈ 144–146; rows 3–5 imply R ≈ 50–57 | 26/0.18=144, 82/0.56=146, 12/0.21=57, 4/0.07=57, 1/0.02=50 | up to 96 pts | FAIL — the R denominator is not consistent across the replay and is never stated. |
