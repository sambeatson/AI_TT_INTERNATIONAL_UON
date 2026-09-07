# Trust Score — 2026-07-02 — SP500_Report_02Jul2026.md

Reviewer run: `regen_20260906_qa1` · Asset US500 · D = 2026-07-02 · D-1 = 2026-07-01
Evidence base: the report, reports dated before D, `data/slices/US500/US500_upto_2026-07-01.csv`
(plus VIX / USDX / NEWS slices to D-1), `cards/baseline/by_date/2026-07-02.json`, and
`qa/regen_20260906_qa1/lint_static/2026-07-02.csv`. Helper output from
`engine/qa_slice_stats.py --date 2026-07-02 --closes 7358.22 7357.49 7354.02 7440.43 7499.36`.

**Headline finding.** The report's declared as-of session is **30 Jun 2026**, but D-1 is
**01 Jul 2026**, and the slice contains a complete 01 Jul cash session (O 7478.6 · H 7525.4 ·
L 7452.6 · C 7489.1 · RSI2 92.29). The report is one session stale on every derived quantity —
the §6 table, the §11 daily pivots, the §21b entries and the backtest window all end at 30 Jun —
while §3 and §4 nonetheless quote 01 Jul intraday prints as confirmation. The staleness is never
flagged as such.

## 1. Section 7 checklist

| Item | Reviewer notes | Evidence observed | Score 0–5 | Action required |
|---|---|---|---|---|
| 1.1 Variables respected | Asset is the S&P 500 cash index, not ES (§2) ✓. Counters USDX · VIX · DAX 40 with USDX first ✓. USD / index points ✓ (tick 0.01 not stated, but stops and targets are rendered in points). Lookback is 5 sessions ✓ in count. **Two material variables missed:** as-of is 30 Jun, not the D-1 NY close of 01 Jul; and the daily-open anchor is moved off the M1 `[DAILY_OPEN_ANCHOR]` 07:00 UK to the 02 Jul cash open (disclosed in §20, but it also contradicts the card object, which records `MARKET @ session open 07:00 UK`, `anchor_broker 09:00`). Source count is 6 ✓ but the roster drifts from the prescribed benchmark list (Bloomberg, Twelve Data, CME ES absent; CNBC, TheStreet, StreetStats substituted) with no substitution note. | Header line 5; §2 As-of/Lookback rows; §4; §20 anchor-override bullet; `cards/baseline/by_date/2026-07-02.json` Trade_1 `entry_mode_text` | 2 | Re-anchor the whole report to the 01 Jul cash close; reconcile the anchor statement with the card object; note the source substitutions. |
| 1.2 Coverage & currency consistent | Currency and unit are stable throughout ✓. Dates are not: §6/§8/§11/§21c stop at 30 Jun while §3/§4 quote 01 Jul intraday; §13c dates PCE to 26 Jun when the calendar carries it on 25 Jun; §13d lists "Wed 01 Jul ISM Manufacturing PMI" as an **upcoming** event inside a table headed "Upcoming (02–08 Jul)" — that release is already on the D-1 calendar. | §3 rationale; §4 rows 5–6; §13c row 3; §13d row 2; NEWS slice rows 2026-06-25 and 2026-07-01 | 2 | Rebuild §6/§11/§21c on the 25 Jun–01 Jul window; move ISM to §13c; correct the PCE date. |
| 1.3 Audience & tone | Consistent Senior US Equity Strategist register; framed for trading and risk review; no retail tone, no promotional language; caveats are stated in professional terms. | §1, §5, §16, §18, closing rule line | 5 | None. |
| 2.1 Sections present & ordered | §1–§21 all present in the mandated order; §13a/b/c/d all present; §21a/b/c/d all present; §17 is a single sentence; §19 and §20 present with substantive content. Trade 2 appears as a SUPPRESSED row, not an omission ✓. | Headings throughout | 5 | None. |
| 2.2 Scorecard as a table | §6 is a genuine table carrying Date/O/H/L/C/RSI2/Trend/Src A/Src B/Final/Validation ✓. §11 gives three pivot tables (daily, weekly, monthly) in descending order through P; the report renders R5→S5 rather than R3→S3, a superset consistent with the M5 floor-pivot glossary. | §6; §11 three tables | 5 | None (optionally trim to R3→S3). |
| 2.3 Method steps visible | §4 observations → §5 classification and weighted-median consensus ✓. §8 is candle-by-candle with an explicit sequence assessment ✓. §9 states regime with overlap ratio, persistence and VOLator slope ✓. Five charts present as captioned image placeholders (pandoc-dropped images accepted per protocol). One weakness: the §7 note concedes the 25-session and VOLator series use "documented June context" rather than the measured block, so those two panels do not evidence a method step. | §4–§9; §7 captions and note | 4 | State the 25-session block explicitly from the data. |
| 3.1 Quantitative claims sourced | Most §1 figures point back to §6/§21a ✓. Uncited and load-bearing: **VIX "≈16.4"** (§1, §10, §14) — the slice never trades there in the window (D-1 close 17.71, 30 Jun close 17.54, window low 17.44); **DAX "≈24,996, +1.5% on 30 Jun"** (§10); **"~78% market-implied probability of further 2026 easing"** (§12 and §14); **"Brent back toward the low-$70s"** (§12, §14). These four carry no source and no §4/§6/§13 pointer. | §1 ¶1; §10 all three rows; §12 bullets 2–3; §14 bullets 1, 4 | 2 | Source or drop each; correct the VIX level to the D-1 close. |
| 3.2 Citations exist & contain data | Three spot-checks. **(a) TheStreet SMT** — the in-text figure 7,449.36 is declared a typo and reconciled via +0.79% from 7,440.43 → 7,499.31 ≈ 7,499.36; the reconciliation is arithmetically sound and disclosed, so **not fabricated**, but the "Raw Quote" cell prints the corrected value rather than the raw one. **(b) Investing.com, 01 Jul intraday 7,449.63–7,521.81, open 7,478.84** — the slice's 01 Jul cash session is O 7478.6 / H 7525.4 / L 7452.6, i.e. Δ 0.24 / −3.59 / −2.97: consistent. **(c) StreetStats, 01 Jul 11:51 ET = 18:51 broker, 7,512.18** — the slice's 18:45 bar is 7,514.6–7,520.1, Δ ≈ −7 on a quote self-described as delayed: consistent. No cited source is impossible or self-contradictory, so **no fabricated-source override**. Deduction: §6 assigns the 30 Jun high as 7,521.81, the identical figure §4 attributes to the **01 Jul** session high — one session's print is re-used as another's. | §4 rows 4–6; §5 ¶2; §6 row 5; US500 slice 2026-07-01 18:30–19:15 bars | 3 | Put the raw quote in the raw column; stop carrying the 01 Jul high into the 30 Jun row. |
| 3.3 Calculations transparent | **Reproduces:** RSI2 recomputed from the report's own five closes returns 0.0 / 96.1 / 100.0 for 26/29/30 Jun — an exact match to the printed column, so the RSI2 arithmetic is correct. The Trend column follows the stated rule on all five rows (26 Jun correctly Neutral: C>O but RSI2 ≯ 50). Daily pivots reproduce to the cent from the report's own 30 Jun H/L/C (P 7,486.76 · R1 7,534.41 · S1 7,451.70 · R2 7,569.47 · S2 7,404.05 · R3 7,617.12 · S3 7,368.99). **Does not reproduce:** **ATR(14) is never stated numerically anywhere in the report**, so the 3×ATR runner cap, the 3.5×ATR stop cap, the 0.25×ATR buffers and the wide-stop test are all unverifiable. KER is given as a value but not with its (13, EMA 3) parameters. §13b tilt: the shown computation yields Σw·s = +1.5, Σw = 3.5 → **+0.43**, then "moderated to +0.34 after the two bearish media prints" — those prints are already inside the numerator, so the moderation double-counts and +0.34 is unreproducible. §21a: listed contributions (+0.20, +0.07, +0.068, +0.051) sum to +0.389, not the stated **+0.42**; on the declared default weights (0.25/0.20/0.10/0.15/0.15/0.15) with Bullish short-term, TRANSITION medium (±0.5), expansion VOLator, KER −0.01, tilt +0.34 and CONFIRM cross-asset the score is ≈ **+0.60**. Neither figure reconciles. | §6 RSI2 and Trend columns; §11 daily table; §13b computation line; §21a; §9 KER bullet; absence of any ATR figure | 2 | State ATR(14) and KER parameters; re-derive the tilt and the §21a score from the shown weights. |
| 3.4 Numbers reconcile | Internally the anchor close 7,499.36 is identical in §1, §3, §4, §6 and the §21b Trade 1 entry ✓; §11 pivots match the levels quoted on the cards ✓; RSI2 agrees across §6, §8 and the §21a input ✓. Against the slice it does not: two closes miss by more than 10 pts (24 Jun −14.08, 26 Jun +18.22) and six of the ten open/high values miss the 8-pt tolerance, the largest being the 25 Jun open at −67.00. ATR cannot reconcile between §9 and §21 because it is never stated. §11's position narrative is self-contradictory: "sitting just above the monthly R1 (7,646.56 above; monthly P 7,473.70 below)" — 7,499.36 is below monthly R1. | §6 vs slice cash sessions (see §5 log); §11 position narrative; §9 vs §21b | 2 | Rebuild §6 on D-1 data; state ATR; fix the monthly R1 sentence. |
| 4.1 Pillars conclude | Every pillar ends in a direction label: §8 "Bullish continuation", §9 "Mildly Bullish", §10 "CONFIRM", §12 per-bullet labels, §14 per-bullet labels ✓. Two problems. §10's CONFIRM rests on a VIX level (16.4) that does not exist in the window and on a USDX level (101.1) that is the 30 Jun close, whereas D-1 USDX closed 101.401 — firmer, not softer. And the strategy layer's conclusions violate their own inputs: §9 declares regime **TRANSITION**, and M5 §3/§5.3c maps TRANSITION to **Trade 3C**, yet §21b builds **Trade 3A**, justifying it by a RANGE dual-gate that is not the gate in question. | §8 judgement line; §9 bias; §10 aggregate line; §12/§14 bullets; §21b Trade 3 "Trade type" cell; VIX/USDX slices | 2 | Correct the counter levels; take the Trade 3 variant from `regime_label`. |
| 4.2 Peer/cross-asset interpreted | §10 gives real mechanisms rather than a correlation list — softer dollar → easier financial conditions and earnings translation; lower implied vol → compressed equity risk premium; DAX as the global risk-appetite common factor. This is the intended shape of the section. Marked down only because two of the three mechanisms are driven off unsourced or stale levels (see 3.1). | §10 table, Mechanism column | 4 | Re-run the mechanisms on D-1 counter closes. |
| 4.3 Synthesis reconciles tensions | The KER-vs-thrust conflict is named and carried consistently through §1, §8, §9, §15, §16, §18 and §21a, with an explicit precedence rule ("price/RSI2 thrust leads for the execution window; treat the breakout as unconfirmed until a close holds above 7,521") — genuinely well handled. But the §21a/§17 reconciliation is asserted rather than shown (the score does not reproduce, see 3.3), and the Trade 3 card resolves the regime tension by contradicting the regime label it cites. | §9 Kaufman bullet; §15 both columns; §16; §18; §21a conflict flag; §21b Trade 3 | 3 | Reconcile §21a arithmetic; do not resolve a regime tension by re-labelling the fork. |
| 4.4 Calibrated language | §17 is exactly one sentence ✓ and confidence Medium is stated in both §3 and §18 ✓. Mild hedge stacking within that sentence ("grinds modestly higher … while holding … unless …"), and no H/M/L confidence is attached to the §16 forward view. | §17; §3 Confidence cell; §18 opening line; §16 | 4 | Attach a confidence label to §16. |
| 5.1 Data dated; staleness flagged | Every price row and every article carries a date ✓, and the reconstructed O/H/L are explicitly flagged single-source-indicative in both the §6 note and §19 ✓ — the disclosure discipline itself is good. The failure is that the report presents 30 Jun as the current session while quoting 01 Jul prints in §3/§4, and never flags that the 01 Jul cash session has closed and been excluded. The VIX figure carries neither date nor source. | §6 note; §19 bullets 1–2; §3 rationale; §4 rows 5–6; §1/§10/§14 VIX references | 2 | Flag the excluded session or, preferably, include it. |
| 5.2 Assumptions up front | The anchor override is stated in §20 **and** on the Trade 1 card ✓. The single-source-indicative pivot flag is raised in §11, restated in §19, and propagated into §21b — it is the stated ground for the Trade 2 SUPPRESSED row and appears in the Trade 3A caveat line ✓. Weight basis ("DEFAULTS, no tuning") and the 20-session lock are logged ✓, and the backtest's no-leakage reconstruction is described ✓. This is the report's strongest category row. | §20 all bullets; §11 source-status paragraph; §19; §21b Trade 2 and Trade 3A caveats | 5 | None. |
| 5.3 Red flags surfaced | §12 carries the breadth-quality caveat and the catalyst risk; §15 gives four balanced downside risks including the overbought extreme, the KER mismatch and holiday-thinned liquidity; the §13d payrolls collision is carried explicitly into the Trade 1 caveat line ("holding period collides with §13d Tier-1 payrolls"). Red-flag propagation into the cards is done properly. | §12 bullets 4–5; §15 right column; §13d; §21b Trade 1 Caveats row | 5 | None. |
| 5.4 Restrictions honoured | No retail CFD quotes in the OHLC basis ✓; ES futures not used for anything ✓; instrument common names used ✓; no module codes and no framework name ✓. **Breaches:** (i) the §6 Validation column reads "CORROBORATED (Δ 0.00)" and the row carries named Src A / Src B, yet the O/H/L cells in those same rows are, by the report's own footnote, "reconstructed from reported percentage moves and intraday session context" — synthesised prices presented as sourced and corroborated, and materially wrong (up to −67.00 on the 25 Jun open); (ii) a leaked variable token, "a quality-of-rally caveat vs **COMPARISON** breadth", survives into §12; (iii) the anchor departs from `[DAILY_OPEN_ANCHOR]` = 07:00 UK and contradicts the card object's own 07:00 UK entry. | §6 Validation and Src columns vs §6 note; §12 bullet 4 (line 394); §20 anchor bullet vs card JSON | 1 | Restrict the CORROBORATED label to the close cells; remove the leaked token; align the anchor. |

## 2. Category roll-up

| Category | Level | Multiplier | Points | Justification |
|---|---|---|---|---|
| C1 Prompt adherence (max 20) | 2 | 0.40 | 8.00 | Rows 1.1/1.2/1.3 = 2/2/5, mean 3.00 → level 3; the restriction breach at 5.4 drops C1 one level to **2**. Wrong as-of session and a non-conforming, card-contradicting anchor are the two driving deviations. |
| C2 Structural alignment (max 20) | 5 | 1.00 | 20.00 | Rows 2.1/2.2/2.3 = 5/5/4, mean 4.67 → level 5. Every mandated section, sub-section and table is present, ordered and correctly typed; suppression is expressed as a row. |
| C3 Accuracy & evidence (max 25) | 2 | 0.40 | 10.00 | Rows 3.1/3.2/3.3/3.4 = 2/3/2/2, mean 2.25 → level 2. Two closes wrong by >10 pts, six of ten open/high values outside tolerance, the D-1 session missing entirely, ATR never stated, and the §13b and §21a scores unreproducible. No fabricated source, so C3 is not zeroed. |
| C4 Reasoning & judgment (max 20) | 3 | 0.65 | 13.00 | Rows 4.1/4.2/4.3/4.4 = 2/4/3/4, mean 3.25 → level 3. The narrative reasoning is genuinely good — real cross-asset mechanisms and an honestly carried KER tension — but the card layer contradicts its own regime label and breaks four M5 construction rules. |
| C5 Currency, restrictions & transparency (max 15) | 3 | 0.65 | 9.75 | Rows 5.1/5.2/5.3/5.4 = 2/5/5/1, mean 3.25 → level 3. Assumption and red-flag disclosure are exemplary; dating of the as-of session and the no-synthesis restriction are not. |
| **Total** | — | — | **60.75 → 61** | Sum of category points, rounded to a whole number. |

## 3. Total, band, override check

- **Raw total:** 8.00 + 20.00 + 10.00 + 13.00 + 9.75 = **60.75 → 61**.
- **Band:** **Moderate** (60–74).
- **Fabricated-source override — NOT triggered.** Three cited sources were spot-checked for internal consistency (TheStreet SMT, Investing.com, StreetStats; see row 3.2). None is impossible or self-contradictory: the TheStreet discrepancy is disclosed and reconciles arithmetically, and both 01 Jul aggregator quotes sit within a few points of the slice's 01 Jul cash session. C3 is therefore scored on its merits (2), not zeroed, and no Low-Trust cap applies.
- **Restriction-breach override — TRIGGERED.** Row 5.4: synthesised O/H/L presented as source-attributed and "CORROBORATED (Δ 0.00)" in §6, plus the leaked `COMPARISON` variable token in §12 and an anchor that departs from `[DAILY_OPEN_ANCHOR]` while contradicting the card object. Effects applied: **C1 dropped one level (3 → 2)** and the **total capped at 74**. The cap is not binding here — the post-drop total of 61 already sits below it — but the C1 drop is included in the 61.
- **Final Trust Score: 61 / 100 — Moderate. Override: `restriction_breach`.**

## 4. Card Integrity

Linter rows copied verbatim from `qa/regen_20260906_qa1/lint_static/2026-07-02.csv`:

| card_id | report_date | strategy | flags | dud |
|---|---|---|---|---|
| 2026-07-02_Trade_1 | 2026-07-02 | Trade 1 - Daily Directional | CLEAN | False |
| 2026-07-02_Trade_2 | 2026-07-02 | Trade 2 - Pivot (regime-aware) | SUPPRESSED | False |
| 2026-07-02_Trade_3A | 2026-07-02 | Trade 3A - Momentum-Pullback (57.5% fib) | CLEAN | False |

Per-card integrity — 100 − 40·(#DUD) − 10·(#WARN), floored at 0:

| Card | #DUD | #WARN | Integrity |
|---|---|---|---|
| 2026-07-02_Trade_1 | 0 | 0 | 100 |
| 2026-07-02_Trade_2 | — | — | suppressed — excluded from the mean |
| 2026-07-02_Trade_3A | 0 | 0 | 100 |

**Report-level Card Integrity = 100.0** (mean over the two non-suppressed cards).
Counts for the roll-up CSV: n_cards = 3 (all rows in the lint file), n_duds = 0, n_warns = 0.

Note for the reader: the static linter is leak-free and checks only internal geometry — stop side,
TP ordering, R against ATR, target distance, duplicates. Both live cards pass that geometry. The
M5 construction defects recorded below are **not** visible to the static linter (they require the
D-1 slice) and are therefore scored under row 4.1 / 4.3, not against this 100.0.

## 5. Data reconciliation log

Convention per the reviewer brief: slice values are cash-session (16:30–23:00 broker = 09:30–16:00 ET).
Tolerance |Δ| ≤ 3 pts on a close, ≤ 8 pts on an open/high/low. A close wrong by > 10 pts, or an RSI2
that will not reproduce, is a Category 3 failure rather than a note.

### 5.1 §6 Validated OHLC table vs slice cash sessions

| Section | Report value | Slice value | Delta | Verdict |
|---|---|---|---|---|
| §6 24 Jun Open | 7,383.20 | 7,389.0 | −5.80 | OK (within 8) |
| §6 24 Jun High | 7,398.55 | 7,438.0 | −39.45 | DISCREPANCY |
| §6 24 Jun Low | 7,351.10 | 7,346.0 | +5.10 | OK |
| §6 24 Jun Close | 7,358.22 | 7,372.3 | −14.08 | **FAILURE (>10 pts)** |
| §6 25 Jun Open | 7,360.90 | 7,427.9 | −67.00 | **DISCREPANCY (largest)** |
| §6 25 Jun High | 7,388.40 | 7,432.6 | −44.20 | DISCREPANCY |
| §6 25 Jun Low | 7,332.75 | 7,332.9 | −0.15 | OK |
| §6 25 Jun Close | 7,357.49 | 7,365.9 | −8.41 | DISCREPANCY |
| §6 26 Jun Open | 7,351.00 | 7,323.8 | +27.20 | DISCREPANCY |
| §6 26 Jun High | 7,369.20 | 7,402.1 | −32.90 | DISCREPANCY |
| §6 26 Jun Low | 7,300.85 | 7,303.1 | −2.25 | OK |
| §6 26 Jun Close | 7,354.02 | 7,335.8 | +18.22 | **FAILURE (>10 pts)** |
| §6 29 Jun Open | 7,372.50 | 7,403.0 | −30.50 | DISCREPANCY |
| §6 29 Jun High | 7,445.90 | 7,450.6 | −4.70 | OK |
| §6 29 Jun Low | 7,360.20 | 7,355.1 | +5.10 | OK |
| §6 29 Jun Close | 7,440.43 | 7,443.0 | −2.57 | OK |
| §6 30 Jun Open | 7,441.10 | 7,446.2 | −5.10 | OK |
| §6 30 Jun High | 7,521.81 | 7,513.4 | +8.41 | DISCREPANCY (marginal; equals the slice's **01 Jul** high 7,525.4 far more closely than 30 Jun's) |
| §6 30 Jun Low | 7,439.10 | 7,441.7 | −2.60 | OK |
| §6 30 Jun Close | 7,499.36 | 7,493.3 | +6.06 | DISCREPANCY |
| §6 D-1 session (01 Jul) | *absent* | O 7,478.6 · H 7,525.4 · L 7,452.6 · C 7,489.1 | n/a | **FAILURE — the D-1 session is missing from the table entirely** |

Summary: 6 of 10 open/high values and 4 of 5 closes fall outside tolerance; the window is the wrong
five sessions (report 24–30 Jun; D-1 window is 25 Jun–01 Jul).

### 5.2 RSI2

| Section | Report value | Slice / recomputed value | Delta | Verdict |
|---|---|---|---|---|
| §6 26 Jun RSI2 | ~0 | 0.00 (slice) / 0.0 (from report's own closes) | 0.00 | OK |
| §6 29 Jun RSI2 | 96.1 | 78.08 (slice closes) | +18.02 | DISCREPANCY — caused by the wrong closes, not by the arithmetic |
| §6 29 Jun RSI2 | 96.1 | 96.1 (recomputed from the report's own closes) | 0.00 | OK — arithmetic verified |
| §6 30 Jun RSI2 | 100.0 | 100.00 (slice) and 100.0 (own closes) | 0.00 | OK |
| §6 D-1 (01 Jul) RSI2 | *absent* | 92.29 | n/a | MISSING — §1's "RSI2 pinned at 100" describes 30 Jun, not D-1 |

Verdict: the RSI2 **formula** is applied correctly (all three testable rows reproduce exactly from the
report's own close sequence); the **inputs** are the wrong sessions.

### 5.3 §11 Floor pivots

| Section | Report value | Slice value | Delta | Verdict |
|---|---|---|---|---|
| §11 daily — reproduction from the report's own 30 Jun H/L/C (7,521.81 / 7,439.10 / 7,499.36) | P 7,486.76 · R1 7,534.41 · S1 7,451.70 · R2 7,569.47 · S2 7,404.05 · R3 7,617.12 · S3 7,368.99 | recomputed: identical to the cent | 0.00 on all seven | OK — pivot formulae verified |
| §11 daily P | 7,486.76 | 7,489.03 (D-1 01 Jul cash) | −2.27 | Wrong input session |
| §11 daily R1 | 7,534.41 | 7,525.47 | +8.94 | DISCREPANCY |
| §11 daily S1 | 7,451.70 | 7,452.67 | −0.97 | OK |
| §11 daily R2 / S2 | 7,569.47 / 7,404.05 | 7,561.83 / 7,416.23 | +7.64 / −12.18 | DISCREPANCY on S2 |
| §11 daily R3 / S3 | 7,617.12 / 7,368.99 | 7,598.27 / 7,379.87 | +18.85 / −10.88 | DISCREPANCY |
| §11 weekly P | 7,351.14 | 7,392.57 (prior week 22–26 Jun cash) | −41.43 | **FAILURE** |
| §11 weekly inputs (back-solved from the report's own P/R1/S1) | H 7,398.55 · L 7,300.85 · C 7,354.02 | H 7,538.80 · L 7,303.10 · C 7,335.80 | H −140.25 · L −2.25 · C +18.22 | **FAILURE — the report used only the 24–26 Jun subset of its own §6 rows as "the week"** |
| §11 monthly P | 7,473.70 | 7,453.67 (June cash) | +20.03 | DISCREPANCY |
| §11 monthly inputs (back-solved) | H 7,620.89 · L 7,300.84 · C 7,499.37 | H 7,624.60 (02 Jun) · L 7,243.10 (09 Jun) · C 7,493.30 | H −3.71 · L **+57.74** · C +6.07 | DISCREPANCY — the June low is taken as the 26 Jun low, not the actual 09 Jun low |
| §11 position narrative | "sitting just above the monthly R1 (7,646.56 above…)" | 7,499.36 < 7,646.56 | n/a | **Internal contradiction** |

### 5.4 Volatility, swings and counters

| Section | Report value | Slice value | Delta | Verdict |
|---|---|---|---|---|
| §9 / §21b ATR(14) | *never stated numerically* | 91.49 (cash bars); 97.16 (full-day) | n/a | **FAILURE — required by row 3.3; every ATR-derived card rule is unverifiable** |
| §21b 5-day swing | low 7,354.02 → high 7,521.81 (167.79 pts) | low 7,303.10 (26 Jun) → high 7,525.40 (01 Jul) (222.30 pts) | magnitude −54.51 | DISCREPANCY — and 167.79 < 2×ATR (182.98), so the report's swing fails the M5 §4b qualifier |
| §8 25-session high | "early-June 7,620.90" | 7,624.60 (02 Jun) | −3.70 | OK (basis) |
| 25-session low (unstated) | *absent* | 7,243.10 (09 Jun) | n/a | Missing — needed for the 3B/3C range |
| §10 / §1 / §14 VIX | ≈ 16.4 | 17.71 (D-1 close); 17.54 (30 Jun); window low 17.44 | −1.31 vs D-1 | **DISCREPANCY — 16.4 does not occur anywhere in the window** |
| §10 VIX start of move | 18.9 | 18.90 (24 Jun close) | 0.00 | OK |
| §10 / §14 USDX | ≈ 101.1, "flat / soft" | 101.401 (D-1 close); 101.124 (30 Jun) | −0.30 vs D-1 | Stale — D-1 USDX closed firmer, not softer |
| §13d ADP | "printed weak (98k)" | 2026-07-01 ADP Nonfarm Employment Change, 98.0 vs previous 122.0 | 0.0 | OK — verified against the D-1 calendar |
| §13d Nonfarm Payrolls, Thu 02 Jul, High impact | as stated | calendar carries USD Nonfarm Payrolls, 2026-07-02, HIGH | n/a | OK — the headline catalyst claim is verified |
| §13c PCE | "26 Jun · softer-than-expected MoM" | 2026-06-25 Core PCE m/m: actual 0.3, consensus 0.1, previous 0.2 | date −1 session; direction inverted | **FAILURE — the release is dated 25 Jun and came in above both consensus and the prior print; §14's "keeps the easing narrative intact" rests on it** |
| §13d ISM Manufacturing PMI | listed as upcoming, "Wed 01 Jul" | released 2026-07-01 17:00 broker (D-1) | n/a | DISCREPANCY — a past release inside the "Upcoming (02–08 Jul)" table |

### 5.5 Cross-report consistency (reports dated before D only)

| Section | Report value | Prior-report value | Delta | Verdict |
|---|---|---|---|---|
| §6 25 Jun close | 7,357.49 | 7,357.74 (`SP500_Report_01Jul2026.md`); 7,357.49 (`SP500_Report_30Jun2026.md`) | −0.25 / 0.00 | Minor — the 01 Jul report disagrees with both others |
| §6 29 Jun RSI2 | 96.1 | 95.9 (`SP500_Report_01Jul2026.md`) | +0.20 | Minor |
| §6 24 / 26 / 29 Jun closes | 7,358.22 / 7,354.02 / 7,440.43 | identical in both prior reports | 0.00 | Consistent |
| As-of convention | "session data through 30 Jun" for D = 02 Jul | `SP500_Report_01Jul2026.md` uses 29 Jun for D = 01 Jul; `SP500_Report_30Jun2026.md` uses 30 Jun for D = 30 Jun | n/a | The one-session lag is a recurring pattern across this series, not a one-off — and the D-1 session is available in the slice in this case |
