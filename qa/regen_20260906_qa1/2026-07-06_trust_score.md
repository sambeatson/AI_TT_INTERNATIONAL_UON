# Trust Score v3.7 — S&P 500 Daily Report, 06 July 2026 (`SP500_Report_06Jul2026.md`)

Reviewer inputs: REVIEWER_BRIEF, framework §4–7, QA protocol, the report, slice `US500_upto_2026-07-05.csv`
(`engine/qa_slice_stats.py --date 2026-07-06 --closes 7354.02 7440.43 7499.36 7483.23 7483.24`), baseline card JSON, static linter rows.

Basis note: the report's D-1 is Thu 02 Jul (US cash closed Fri 03 Jul, Independence Day observed; 04-05 Jul weekend). That is the correct
as-of session for the cash index. The slice carries a short CFD stub on 03 Jul (broker-day open 7474.7, close 7504.6, range 7472.2–7513.1) which is
NOT a cash session; the tool's "D-1 pivots from 2026-07-03" are therefore not used. Reference cash-session numbers below are the 02 Jul session.

Reference numbers (slice, 16:30–23:00 broker): 02 Jul O 7502.2 H 7541.0 L 7427.0 C 7472.8; ATR14 full-day bars 90.87, cash-session bars 84.66
(report states 96.3 — ~93 on daily cash bars with the 03 Jul stub excluded); 25d cash high 7624.6 (02 Jun) / low 7243.1 (09 Jun), width 381.5;
5d swing 7541.0 / 7355.1. Own-close RSI2 test: last three rows reproduce exactly (100.0 / 78.5 / 0.1); first two rows need unprinted seeding closes.

## 1. Section 7 checklist

| Row | Reviewer notes | Evidence | Score |
|---|---|---|---|
| 1.1 Variables respected | Asset (cash index, not ES), counters in order USDX/VIX/DAX, USD/points/tick 0.01, 5/25-session lookbacks all correct. Anchor misread: §2/§20 say the "daily-open anchor was overridden to 06 July 2026" (a date), but the anchor is a time of day (07:00 UK); 07:00 UK appears nowhere in the report or on any card. Source set nominally 6 rows but only 2 yield a usable close; no sell-side tier in the price table; S&P DJI row has no observed figure. | §2, §4, §20, §21b | 3 |
| 1.2 Coverage and currency consistent | D-1 holiday handling correct and stated. Weekly pivots built on W/E 26 Jun (22–26 Jun) although the last fully completed week is 29 Jun–02 Jul. §21c backtest window is 25 Jun–01 Jul (t-5..t-1) while §6 covers 26 Jun–02 Jul — shifted one session. | §11, §21c vs §6 | 3 |
| 1.3 Audience and tone | Strategist register, trading/risk-review framing, no retail tone. Odd disclosure in §19 ("lenient on corroboration so a strategy can be produced"). | §1, §18, §19 | 4 |
| 2.1 Sections present and ordered | §1–§21 all present in order incl. §13a–d, §21a–d and boilerplate. §7 shows five chart headings with no images (pandoc drop; accepted as placeholders). | headings | 5 |
| 2.2 Scorecard as table | §6 is a table but lacks the Source A / Source B / Final columns. §11 daily table is complete (R1–R5/S1–S5); weekly and monthly tables show only R3, R1, P, S1 (R2, S2, S3 missing) although §16 cites weekly R2 7,629. | §6, §11 | 3 |
| 2.3 Method steps visible | §4→§5 observation→consensus visible; §8 candle-by-candle with sequence; §9 overlap/persistence/VOLator/KER shown. Missing: KER window/smoothing, ATR14 value in §9, RSI2 working line, seeding closes. §8 contains factual slips (below). | §5, §8, §9 | 4 |
| 3.1 Quantitative claims sourced | Unsourced figures: Fed 4.25–4.50% and 60–65% Sept-cut odds, "~354 advancers", Micron/Intel/Tesla/SanDisk/KLA/Lam % moves, VIX 52-wk 13.38/35.30, USDX ~100.5, "VIX mid-16s". Only the strategist quotes carry attribution. | §1, §10, §12, §14 | 3 |
| 3.2 Citations exist and contain data | (i) TheStreet quote "S&P 500 gained 0.49%" (02 Jul) does not match the report's own closes 7,483.23 → 7,483.24 (+0.00%). (ii) "CME ES futures … 7,499.1 (US500 cash CFD)" — label and basis self-contradictory; figure dated 02 Jul is 27 pts from the slice's 02 Jul CFD close (7,470.8–7,472.8). (iii) Yahoo is "via Motley Fool" (one remove) and §20 admits it supplied close corroboration only, yet §6 prints OHLC "CORROBORATED Δ0.00" for all five sessions. Multpl 7,524.59 and Lines.com 62% are consistent with the report. Recorded as defects, not as proven fabrication (cannot be fetched; sources are named and plausible, excluded rows are not used for the consensus). | §4, §6, §13a, §20 | 2 |
| 3.3 Calculations transparent | Pivot arithmetic from 02 Jul H/L/C reproduces (P 7,483.85, R1 7,540.15, S1 7,426.95, R2 7,597.05, S2 7,370.65, R3 7,653.35, S3 7,313.75). RSI2 reproduces for 30 Jun/01 Jul/02 Jul. Defects: Trend column wrong on 01 Jul (C>O, RSI2 78.5 → Bullish, printed Neutral) and 02 Jul (C<O, RSI2 0.1 → Bearish, printed Neutral); sentiment tilt +0.29 weights not shown (unweighted would be +0.50); KER parameters absent. | §6, §11, §13b | 3 |
| 3.4 Numbers reconcile | D-1 close 7,483.24 identical in §1/§3/§4/§6/§18/§21. Failures: (a) cash-basis deltas vs slice: 26 Jun close +18.2 and 02 Jul close +10.4 (both >10), 26 Jun O −11.1 / H −9.2 / L −8.9, 29 Jun O −11.1 (all >8), 30 Jun close +6.1, 01 Jul close −5.9; (b) 25-day high 7,605 vs the report's own 52-wk high 7,620.90 and slice 7,624.6; (c) §11 says close is "fractionally above weekly R1 (7,491)" while 7,483.24 < 7,491.29; (d) §8 puts the 02 Jul close "in the lower third (~49%)" (49% is mid-range) and the 26 Jun close "near range top" (61%); (e) 01 Jul and 02 Jul closes differ by 0.01 while §13a quotes +0.49% for 02 Jul; (f) ATR14 appears only on cards (96.3), not in §9. | cross-section | 2 |
| 4.1 Pillars conclude | §8 Indecision, §9 Neutral-to-mild-bullish / Ranging, §10 CONFIRM, §12 and §14 bullets each carry a direction label. §8 "Compression" conflicts with its own "wide range" 02 Jul bar (113 pts, widest of the five). | §8–§14 | 4 |
| 4.2 Cross-asset interpreted | Mechanism column present for USDX and VIX; DAX mechanism is a correlation statement ("common global-risk factor"). Aggregate CONFIRM explained. | §10 | 4 |
| 4.3 Synthesis reconciles tensions | §16/§18 reconcile regime, KER and VOLator. §21a leaves the §17 mild-upward vs score +0.06 conflict "reported, not reconciled"; §13b divergence handled. Compression vs wide-range bar not addressed. | §15–§18, §21a | 3 |
| 4.4 Calibrated language | §17 is exactly one sentence; confidence Medium stated in §3 and §18. | §3, §17 | 4 |
| Card construction (C4, protocol) | Trade 1 correctly SUPPRESSED (|0.06| < 0.25; contributions sum +0.055). Trade 2 stops not built to the RANGE rule (structural tier + 0.25×ATR) and anchored on the stale weekly P; invalidation sits at the entry, not beyond the stop. Trade 3B is built from daily/weekly pivots instead of the 25-day range (entry at 55% of range vs required 11.4–21.4%; TP1 not range mid; stop/invalidation coincide at ~7,392). No reference close / signed gap or anchor time on any card. Static integrity clean (linter). | §21b | 2 |
| 5.1 Data dated, staleness flagged | Prices and articles dated; counters flagged single-source. O/H/L for 26 Jun–01 Jul labelled CORROBORATED without a second source (§20 contradicts); unresolved placeholder "index +? held" in §13c; weekly pivot period not flagged as a prior-prior week. | §6, §13c, §19 | 3 |
| 5.2 Assumptions up front | Anchor override caveat present but describes a date, not the 07:00 UK time; absent from the cards. Single-source flag stated in §19, carried to 3B caveat ("counters indicative") but not to Trade 2. | §2, §19, §20, §21b | 3 |
| 5.3 Red flags surfaced | Reopen-gap risk, semiconductor de-rating, CPI/FOMC, earnings run all surfaced in §12/§13d/§15 and carried into both live-card caveats. | §12, §15, §21b | 4 |
| 5.4 Restrictions honoured | Futures/CFD excluded from OHLC; no bracketed variable names or M-codes. Leaks: "v2.1 baseline" version string (§20) and three "per instruction" statements (§2, §19, §20); "Core" S&P DJI row with no observed value; "≈7,483" normalised to a 2-dp figure. Treated as minor leaks, not an open breach. | §2, §4, §19, §20 | 3 |

## 2. Category roll-up

| Cat | Rows (mean) | Level | Multiplier | Points | Justification |
|---|---|---|---|---|---|
| C1 Prompt adherence (20) | 3,3,4 = 3.33 | 3 | 0.65 | 13.00 | Anchor misread as a date, never given as 07:00 UK; stale weekly basis and shifted backtest window. |
| C2 Structure (20) | 5,3,4 = 4.00 | 4 | 0.85 | 17.00 | All sections present; §6 columns and weekly/monthly pivot rows incomplete. |
| C3 Accuracy and evidence (25) | 3,2,3,2 = 2.50 | 2 | 0.40 | 10.00 | Two closes >10 pts off the slice; wrong Trend labels; "CORROBORATED" OHLC unsupported by §20; quote/figure and weekly-R1 contradictions. Held at 2 because the brief makes a >10 pt close error a Category 3 failure. |
| C4 Reasoning and judgment (20) | 4,4,3,4,2 = 3.40 | 3 | 0.65 | 13.00 | Sound regime read and suppression of Trade 1; card construction off-rule on both live cards. |
| C5 Currency and transparency (15) | 3,3,4,3 = 3.25 | 3 | 0.65 | 9.75 | Dated and flagged overall; anchor caveat mis-stated; leaks and unsupported corroboration labels. |

c1=3
c2=4
c3=2
c4=3
c5=3
total=63
band=Moderate
override=none

Override check: no source proven fabricated (TheStreet-quote and CME-row contradictions recorded under 3.2/3.4 as defects; had they been judged fabricated the result would be capped at Low with C3=0). No open prompt-restriction breach (version-string and "per instruction" wording treated as minor leaks under 5.4).

## 3. Card Integrity (static linter, copied verbatim; separate from the 100)

| card_id | strategy | flags | dud |
|---|---|---|---|
| 2026-07-06_Trade_1 | Trade 1 — Daily Directional | SUPPRESSED | False |
| 2026-07-06_Trade_2 | Trade 2 — Pivot fade, RANGE regime | CLEAN | False |
| 2026-07-06_Trade_3B | Trade 3B — Mean-Reversion to range mid | CLEAN | False |

Per-card: Trade 1 suppressed (excluded) · Trade 2 100 · Trade 3B 100. Report-level mean over non-suppressed cards = 100.

card_integrity=100
n_cards=3
n_duds=0
n_warns=0

Static cleanliness does not imply the construction rules were met; see feedback items 12–15.
