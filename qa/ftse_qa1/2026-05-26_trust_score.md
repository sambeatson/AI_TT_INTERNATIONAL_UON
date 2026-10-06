# Trust Score v3.7 — FTSE 100 report dated 2026-05-26 (run ftse_qa1)

Report: `reports/md/FTSE_EuroStoxx_Report_26May2026.md` · D = 2026-05-26 · D-1 data session = 2026-05-22 (25 May UK bank holiday).
Level file `data/levels/UK100_by_date/2026-05-26.csv`: `last_bar_date` = 2026-05-22 < D, so it is leak-free. Basis used: cash window 10:00–18:30 broker (`_cash`); `_full` shown where it matters. The report does not state a basis, so it is read as a cash-index report.
Tolerances (brief §4): close ≤ 5 pts, open/high/low ≤ 10 pts. A close off by more than 15 pts, or an RSI2 that does not reproduce, is a Category 3 failure.

## Machine-readable result
```
c1=4
c2=4
c3=2
c4=3
c5=3
total=67
band=Moderate
override=none
card_integrity=95.0
n_cards=3
n_duds=0
n_warns=1
```
(`n_cards=3` counts the linter rows; 2 are scored for Card Integrity and 1, Trade 3C, is SUPPRESSED and excluded from the mean.)

## 1. Section 7 checklist (0–5)

| Row | Reviewer notes | Evidence location | Score | Action required |
|---|---|---|---|---|
| 1.1 Variables respected | FTSE 100 cash is the primary asset, GBP and index points, 5-session lookback, London tz, counters USDX/S&P/DAX plus Euro Stoxx as reference. Two gaps. (a) The daily-open anchor was overridden from 07:00 UK to the "26 May session open" (disclosed in §20, "per the run instruction"). (b) The named sources are retail aggregators and media (Yahoo, Investing, Trading Economics, BBN Times, MarketScreener, IBTimes, Fidelity). None is an index provider, exchange or sell-side source, and Trading Economics is itself described as "CFD-tracked". | §2, §4, §10, §20, §21b | 3 | Restore the 07:00 UK anchor or caveat it on the card. Add tier-correct sources. |
| 1.2 Coverage & currency consistent | Data dates are 18–22 May, plus Euro Stoxx 25 May (D-1 calendar day), and the session is 26 May. GBP/points throughout, Euro Stoxx in EUR. No unit drift. Minor: "six sources" in §3 against "five close observations" in §5. | §2, §3, §5, §6, §13 | 4 | Fix the six-versus-five count. |
| 1.3 Audience & tone | Strategist register, trading and risk review. A few colloquial phrases ("perversely", "textbook"). | §1, §18 | 4 | None material. |
| 2.1 Sections present & ordered | §1–§21 all present and in order. §13a–d and §21a–d present. §17 is one sentence. Five charts versus the two the protocol expects (images dropped by pandoc; captions accepted as evidence). | headings | 5 | None. |
| 2.2 Scorecard as a table | §6 is a table but merges "Sources A / B" into one column and has no "Final" column. §11 pivot tables are ordered R→S but give 5 levels each side (R5–S5) where 3 are specified (R3→S3). | §6, §11 | 3 | Add the Source A, Source B and Final columns. Cut §11 to R3–S3. |
| 2.3 Method steps visible | §4→§5 show observations, a weighted median and the consensus. §8 is candle-by-candle with a sequence call. §9 shows overlap, persistence, range bias, KER and VOLator. Chart captions present. The classification step in §4 is thin (quote type only). | §4–§9 | 4 | None material. |
| 3.1 Quantitative claims sourced | Many figures in §1/§12/§14 carry no source or pointer: oil near $100, ~20% 12-month return, ~80% non-UK revenue, £24.3bn borrowing, sterling at $1.34, Waller and Pantheon remarks. UK CPI is given as "consensus ~3.0%, prior 3.3%". The calendar slice shows consensus 3.8 and prior 3.4 (actual 2.8 agrees). | §1, §12, §14, §13c | 2 | Source or point to §4/§13 for each figure. Fix the CPI consensus and prior. |
| 3.2 Citations exist & contain data | No fabricated URLs. Spot checks: (1) Trading Economics 22 May, "about 0.2% up at 10,466", consistent with the stated closes (+0.22%). (2) BBN Times "advanced 0.41%" conflicts with the report's own closes (10,443.47 → 10,466.26 = +0.22%) and is not reconciled against TE's 0.2%. (3) Fidelity 10,470.09 at 14:53 is consistent. §4 quotes are integers ("10,466 area", "~10,466") yet the report claims agreement within ±0.10 pt. Fidelity is excluded from close consensus in §4 but used as Source B for the 21 May close in §6. | §4, §6, §13a | 3 | Reconcile the BBN % figure. Do not use an excluded intraday source as a close corroborator. |
| 3.3 Calculations transparent | Daily pivot arithmetic reproduces exactly from the stated 22 May H/L/C. RSI2 for 19–22 May reproduces (100.0) from the report's closes with slice 14–15 May closes. RSI2 for 18 May = 64.8 does not. With the slice's 14 and 15 May closes (10,355.8 and 10,167.0) and the report's 10,323.75 it is 45.4, and the slice cash value is 39.6. ATR(14) appears only on Trade 1, "≈124", against 143.99 cash / 163.72 full (−20 / −40 pts). KER is stated (+0.23). The weekly and monthly pivot inputs are not shown and are not reproducible. §21a gives contributions that sum to +0.56 but not the per-signal values or weights, and the "three highest" contributors it names (+0.25, +0.15, +0.06) skip the +0.10 regime term. | §6, §9, §11, §21a, §21b | 2 | Show the per-signal table. Reproduce 18 May RSI2. State ATR(14) in §9. |
| 3.4 Numbers reconcile | D-1 close 10,466.26 is identical in §1, §3, §4, §6 and the §21b entry. Daily pivots in §11 equal the pivots on the cards. Against the slice, three of five closes miss by more than 15 pts, the weekly and monthly pivots are far off, and the five-day swing low is wrong (details in section 2). Internal conflicts: Trade 1 text says the swing-low anchor (10,240.30) was tighter, but the stop 10,235.03 = 10,266.14 − 0.25×124.45, i.e. it is built from the support level. "Early-May trough near 10,000" against a data 25-day low of 10,141.2 cash (10,107.0 full) on 18 May. The §21c backtest rows use inconsistent entry bases (opens for 18 and 19 May, closes for 20 and 21 May). | cross-section | 1 | See feedback items 1–10. |
| 4.1 Pillars conclude | §8 "Bullish continuation", §9 "Transitional / Bullish", §10 "Mixed". §12 and §14 end in per-paragraph labels or a partial net assessment but give no single direction label per pillar. | §8–§14 | 3 | Add one closing direction label to §12 and §14. |
| 4.2 Cross-asset interpreted | Mechanisms given (translation on ~80% non-UK revenue, global risk beta, European breadth, oil). One mislabel: USDX is called "Rising", but the slice closes are 99.303 (15 May) → 99.344 (22 May), +0.04%, i.e. flat. | §10 | 4 | Reword the USDX 5-day direction. |
| 4.3 Synthesis reconciles tensions | KER versus VOLator and USDX versus equities are carried through §15–§18. §17 and §21a agree. Unreconciled: §9 prescribes confirmation-led, conservatively sized entries while Trade 1 is a market order at the open with a score of +0.56 "comfortably above threshold"; §16 is "low conviction". The §19 sentence "applies the suppression rules transparently" is contradicted by Trade 2 being produced. | §9, §16, §19, §21 | 3 | Reconcile the conviction level with the sizing guidance. |
| 4.4 Calibrated language | §17 is one sentence. Confidence is stated (Medium in §3, low in §16). The "Medium" and "low conviction" labels are not reconciled. | §3, §16, §17 | 4 | None material. |
| 4.x Card construction (protocol) | Linter: Trade 1 WARN_TP3_ORDER. The runner cap (10,839.61) is below TP2 (10,928.73). The 5-day swing low is wrong (10,240.30 against 10,141.2 cash). The stop-anchor description contradicts the arithmetic. Trade 2 is built although §11/§19 flag every pivot tier single-source (M5 requires suppression). Its TP labels +1R/+2R do not match distances (+23.73 = 1.08R, +35.77 = 1.63R). R = 22 pts is 0.15×ATR cash, below the 0.3×ATR floor (43.2), although the static linter shows CLEAN. Trade 3C is correctly suppressed, but its boundary inputs are wrong (10,623 against 10,666.5 cash). | §21b | 2 | See feedback cards. |
| 5.1 Data dated; staleness flagged | Prices and articles are dated. The bank-holiday staleness is flagged. The single-source pivot flag is present. Contradiction: §6 says "no single-source-only fields remain" while §19 calls the 18 and 19 May O/H/L "indicative-grade". The weekly and monthly pivots use stale or unidentified windows without a flag. | §3, §6, §11, §19 | 3 | Make §6 and §19 consistent. Flag the pivot windows. |
| 5.2 Assumptions up front | The anchor override is in §20 and the proxy entry is on the card, but the card's Caveats cell does not name the anchor override. The single-source flag is propagated to Trade 2 but not to Trade 1 (stop and ATR) or Trade 3C. | §20, §21b | 4 | Add the override caveat to the Trade 1 card. |
| 5.3 Red flags surfaced | Iran headlines and PCE are carried into the card caveats. The 26 May calendar rows in the slice include a HIGH event, USD CB Consumer Confidence (17:00 broker = 15:00 UK, consensus 99.7, prior 92.8), and an ECB Financial Stability Review (MODERATE). Neither appears in §13d or on the cards. §13c omits the UK PMI miss on 21 May (Composite 48.5, Services 47.9, MODERATE). | §13c, §13d, §21b | 3 | Add the missing events. |
| 5.4 Restrictions honoured | No module codes, no bracketed variable names, no framework name. Euro Stoxx carries no cards. Points against: Trading Economics ("CFD-tracked benchmark") used as a core close comparable; Yahoo-style tickers (^FTSE, ^STOXX50E) in §2; reference to "the run instruction" in the report body; the M5 single-source suppression rule bypassed (disclosed, citing a run instruction I cannot verify). Not scored as an open breach. | §2, §4, §19, §21 | 3 | Remove the CFD-tracked source from the close basis. Drop tickers and the "run instruction" wording. |

## 2. Category 3 evidence — report versus level file (cash basis; `_full` where noted)

| Session | Field | Report | Cash | Δ | Verdict (tol.) |
|---|---|---|---|---|---|
| 18 May | Open | 10,262.10 | 10,144.5 | +117.6 | FAIL |
| 18 May | High | 10,341.50 | 10,336.3 | +5.2 | ok |
| 18 May | Low | 10,240.30 | 10,141.2 | +99.1 | FAIL |
| 18 May | Close | 10,323.75 | 10,290.8 | +33.0 | FAIL (>15; full 10,347.6, −23.9) |
| 19 May | Open | 10,322.40 | 10,339.9 | −17.5 | FAIL |
| 19 May | High | 10,366.80 | 10,408.9 | −42.1 | FAIL |
| 19 May | Low | 10,298.10 | 10,313.0 | −14.9 | FAIL |
| 19 May | Close | 10,330.55 | 10,325.1 | +5.5 | marginal (>5) |
| 20 May | Open | 10,291.00 | 10,274.4 | +16.6 | FAIL |
| 20 May | High | 10,402.60 | 10,458.8 | −56.2 | FAIL |
| 20 May | Low | 10,266.14 | 10,272.8 | −6.7 | ok |
| 20 May | Close | 10,393.20 | 10,422.9 | −29.7 | FAIL (>15) |
| 21 May | Open | 10,394.50 | 10,371.1 | +23.4 | FAIL |
| 21 May | High | 10,472.30 | 10,469.1 | +3.2 | ok |
| 21 May | Low | 10,381.20 | 10,344.7 | +36.5 | FAIL |
| 21 May | Close | 10,443.47 | 10,462.3 | −18.8 | FAIL (>15) |
| 22 May | Open | 10,449.80 | 10,492.6 | −42.8 | FAIL |
| 22 May | High | 10,488.05 | 10,494.5 | −6.5 | ok |
| 22 May | Low | 10,437.60 | 10,446.0 | −8.4 | ok |
| 22 May | Close (D-1) | 10,466.26 | 10,470.4 | −4.1 | ok |

Result: 6 of 20 fields are within tolerance and one is marginal. Three of the five closes (18, 20, 21 May) exceed the 15-pt failure threshold. The D-1 close itself is consistent.

Other Category 3 comparisons:
- RSI2: report 18 May 64.8 is not reproducible (45.4 from slice 14–15 May closes plus the report's 18 May close; cash slice 39.6). Report values for 19–22 May (100.0) reproduce. The 18 May Trend label is Bullish in the report, but the cash RSI2 of 39.6 is below 50, which gives Neutral.
- ATR14: report ≈124 (card text; 3×ATR = 373.35 implies 124.45) against 143.99 cash (−20.0, −13.9%) and 163.72 full (−39.3).
- Daily pivots (report P 10,463.97 / R1 10,490.34 / S1 10,439.89 / R2 10,514.42 / S2 10,413.52 / R3 10,540.79 / S3 10,389.44) against cash P 10,470.3 / 10,494.6 / 10,446.1 / 10,518.8 / 10,421.8 / 10,543.1 / 10,397.6: Δ −6.3 / −4.3 / −6.2 / −4.4 / −8.3 / −2.3 / −8.2, within basis. The report's P equals `d_full_P` (10,463.97) exactly; its other levels sit between the two bases.
- Weekly pivots (report P 10,205.67 / R1 10,404.93 / S1 9,999.03 / R2 10,611.57 / S2 9,799.77 / R3 10,810.83 / S3 9,593.13) against cash P 10,368.7 / 10,596.2 / 10,242.9 / 10,722.0 / 10,015.4 / 10,949.5 / 9,889.6: Δ −163.0 / −191.3 / −243.9 / −110.4 / −215.6 / −138.7 / −296.5. FAIL. The implied inputs (H≈10,412, L≈10,006, C≈10,198) match neither the 18–22 May week (cash H 10,494.5 / L 10,141.2 / C 10,470.4) nor the 11–15 May week (H 10,371.1 / L 10,145.9 / C 10,167.0).
- Monthly pivots (report P 10,328.70 / R1 10,652.20 / S1 9,964.90 / R2 11,016.00 / S2 9,641.40 / R3 11,339.50 / S3 9,277.60) against April cash P 10,418.8 / 10,650.0 / 10,140.1 / 10,928.7 / 9,908.9 / 11,159.9 / 9,630.2: Δ −90.1 / +2.2 / −175.2 / +87.3 / −267.5 / +179.6 / −352.6. FAIL (R1 is the only close match).
- Swings: report five-day high/low 10,488.05 / 10,240.30 against cash 10,494.5 / 10,141.2 (full 10,519.7 / 10,107.0). The low is off by 99 pts. The 25-day range implied by 3C (high 10,623, "trough ~10,000") compares with cash 10,666.5 / 10,141.2 (full 10,698.0 / 10,107.0).
- Counters (slice): S&P 500 22 May close 7,470.9 against the report's 7,473 (ok). USDX 22 May close 99.344 against "~99.3" (ok), but the 5-day move is flat (+0.04%).
- No fabricated URL or source was identified. The BBN Times 0.41% against +0.22% conflict and the use of Fidelity (excluded as intraday) as a close corroborator are recorded as reconciliation failures, not fabrication. No Category 3 override applies.

## 3. Category roll-up

| Category | Max | Level | Multiplier | Points | Justification |
|---|---|---|---|---|---|
| 1 Prompt adherence | 20 | 4 | 0.85 | 17.00 | Variables respected, with a disclosed anchor override and a weak source tier. |
| 2 Structural alignment | 20 | 4 | 0.85 | 17.00 | All 21 sections and sub-sections present. §6 columns and §11 depth deviate. |
| 3 Accuracy & evidence | 25 | 2 | 0.40 | 10.00 | D-1 close and daily pivots are fine. Three closes off by more than 15 pts, weekly and monthly pivots off by 90–350 pts, the 18 May RSI2 not reproducible, ATR understated, swing low wrong. |
| 4 Reasoning & judgment | 20 | 3 | 0.65 | 13.00 | Good cross-asset and regime reasoning. Card construction is defective and the M5 single-source suppression is bypassed. |
| 5 Currency & transparency | 15 | 3 | 0.65 | 9.75 | Staleness flagged. Gaps in the 26 May HIGH event, the card-level override caveat, and a §6/§19 contradiction. |

## 4. Total, band, override
- Total = 17.00 + 17.00 + 10.00 + 13.00 + 9.75 = 66.75, rounded to **67**. Band **Moderate** (60–74).
- Hallucinated-source override: not triggered (no fabricated source identified).
- Restriction-breach override: not triggered. The M5 single-source suppression bypass and the anchor override are disclosed in the report, which attributes them to a run instruction not visible to this reviewer. They are scored in Categories 1, 4 and 5 instead.
- `override=none`.

## 5. Card Integrity (linter rows copied verbatim from `qa/ftse_qa1/lint_static/2026-05-26.csv`)

| card_id | strategy | flags | dud | per-card score |
|---|---|---|---|---|
| 2026-05-26_Trade_1 | Trade 1 — Daily Directional | WARN_TP3_ORDER | False | 90 |
| 2026-05-26_Trade_2 | Trade 2 — Pivot, regime-aware. Regime TRANSITION — breakout-side configuration, upside only. | CLEAN | False | 100 |
| 2026-05-26_Trade_3C | Trade 3C — Momentum-Breakout | SUPPRESSED | False | excluded |

Report-level Card Integrity = mean(90, 100) = **95.0** (separate from the 100). n_cards = 3 (2 scored, 1 suppressed), n_duds = 0, n_warns = 1.

Reviewer observation, not a re-derivation: Trade 2's R of 22 pts is below 0.3×ATR14 on the level file (43.2 cash, 49.1 full) and on the report's own ATR (≈124 → 37.3). The linter row stays CLEAN as supplied.

## 6. Process disclosure
While checking that the forbidden trees were absent, I ran an `ls` that also listed `cards/regenerated`, which exists in the tree. I saw only the directory name `regen_20260906_qa1` and did not open anything in it. `results/`, `data/raw/` and `data/levels/*_levels.csv` are absent, as expected. No other date's files were opened. Scratch work was done in memory only. Feedback is in `qa/ftse_qa1/2026-05-26_feedback.md`.
