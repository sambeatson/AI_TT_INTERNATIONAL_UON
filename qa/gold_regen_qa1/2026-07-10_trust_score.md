# Trust Score — XAUUSD Gold Report — 2026-07-10
Run: gold_regen_qa1 · Report: `reports/md/Gold_Report_10_July_2026.md`
Level file: `data/levels/XAUUSD_by_date/2026-07-10.csv` (last_bar_date 2026-07-09 < 2026-07-10, leak-free — verified)
Basis used for comparison: `_full` (the report's stated Open 4,077.52 matches `prev_open_full` 4,077.93 to within 0.41 USD, vs. 48.71 USD off `prev_open_cash`; the report's own basis line is "Spot, loco London, immediate settlement" — a continuous/full-day basis).

## 1. Section 7 checklist

| Item | Notes | Evidence | Score | Action if below threshold |
|---|---|---|---|---|
| 1.1 Variables respected | Asset correctly XAU/USD spot (not COMEX); futures used for corroboration only, normalised (+33.15 basis stated); USDX listed first among counters in §10; ≥6 sources (7 returned); tick (0.01 USD/oz) stated and used consistently (e.g. "57.23 USD/oz = 5,723 ticks"); lookback 5d/25d stated | §2, §4, §10, §21b | 5 | — |
| 1.2 Coverage & currency consistent | All data dated D−1 (9 Jul) or earlier, session dated D; USD/oz used throughout with no unit drift; ticks used consistently alongside price | whole report | 5 | — |
| 1.3 Audience & tone | Tone is institutional throughout (R-multiples, ATR, ticks, confluence bands) but no explicit "Senior Commodities Analyst" / audience line is stated anywhere in §1 or §18 | §1, §18 | 4 | minor — state audience explicitly |
| 2.1 Sections present & ordered | §1–§21 all present, correctly ordered, headings match spec including §13a–d and §21a–d | headings | 5 | — |
| 2.2 Scorecard as table | §6 is a real table (Session/O/H/L/C/Net Δ/RSI2/TR/Corroboration); §11 pivot tables run R5→P→S5, a superset of the required R3→P→S3, correctly ordered | §6, §11 | 5 | — |
| 2.3 Method steps visible | §4–§5 show observation→normalisation→consensus with the futures basis stated; §8 is candle-by-candle; §9 gives regime + Kaufman but does not use the term "VOLator" or explicitly name persistence/overlap tests, though a volatility table is present; charts absent but captioned per the documented .docx→.md conversion exemption | §4–§9 | 4 | note: name the VOLator/persistence/overlap steps explicitly |
| 3.1 Quantitative claims sourced | Figures in §1/§12/§14 point to §4/§13 sources | text | 4 | — |
| 3.2 Citations exist & are consistent | Spot-checked Kitco, TradingView, CME futures (§4/§5/§20): all named, dated, and used consistently with their own quoted figures. No fabrication found — **hallucinated-source override does NOT apply**. | §4, §13a, §20 | 5 | — |
| 3.3 Calculations transparent | RSI2, ATR, and pivots are shown with formulas reproducible from the report's own stated 5-day closes and H/L/C; however Trade 3A's TP1 is labelled "38.2% retracement" but the stated 56.49 USD distance from entry is actually 61.8% of the entry→swing-low leg (0.382×91.40=34.91≠56.49; 0.618×91.40=56.49) — an internal labelling/arithmetic inconsistency | §6, §11, §21b | 2 | rebuild the TP1 derivation and re-label |
| 3.4 Numbers reconcile — incl. vs. level file | Internally consistent (same D−1 close/pivots repeated in §1/§3/§4/§6/§21b). **Externally fails badly**: 9-Jul session Low stated 4,022.20 vs. `prev_low_full` 4,054.23 (diff 32.03 > 0.20×ATR14 threshold of 20.70 — FAIL); RSI2 stated 100.00 vs. `rsi2_full` 61.88 (diff 38.1 > 15-pt threshold — FAIL, though it does reproduce from the report's own five closes); daily pivots P/S1/R2/S2/R3/S3 (6 of 7 levels) exceed the 0.115×ATR14 pivot tolerance (only R1 is within tolerance); weekly R1 fails the same tolerance (diff 16.08 vs. 11.90 threshold) | level file cross-check | 0 | see feedback — material, report-wide reconciliation failure |
| 4.1 Pillars conclude | §8, §9, §10, §12, §14 each reach a direction-labelled conclusion | those sections | 5 | — |
| 4.2 Peer/cross-asset interpreted | §10 gives an explicit mechanism for each counter (dollar pricing/real yields, risk rotation, precious-complex beta), not a bare correlation list; the equity contradiction is named and carried forward rather than hidden | §10 | 5 | — |
| 4.3 Synthesis reconciles tensions | §15/§16/§18 explicitly address the equity-counter contradiction and the RSI2-vs-regime tension; §17 vs §21a agree and this is stated | §15–§18, §21a | 4 | — |
| 4.4 Calibrated language | §17 is one sentence; confidence stated MEDIUM with reasons in §16/§18 | §3, §17, §18 | 4 | — |
| — Card construction (M5, scored under Cat. 4 per brief §Card Integrity/§3) | Trade 3A entry uses a 50% fibonacci retracement (4,113.60) where the fixed M5 rule requires 57.5% (true level ≈ 4,127.31, computed from the report's own swing 4,205.00→4,022.20); both Trade 2 and Trade 3A stops use a 0.15×ATR buffer (13.88 USD) where the fixed rule requires 0.25×ATR (true buffer, even on the report's own flagged ATR of 92.50, = 23.13 USD); Trade 3A's "borderline pass" (shortfall 2.20 USD / 1.2%) on the 2×ATR swing-qualification test is computed on the report's own self-flagged-indicative ATR (92.50) — on the leak-free `atr14_full` (103.4821) the true requirement is 206.96 and the shortfall is 24.16 USD / 11.7%, not 1.2% | §21a, §21b, level file | 1 | rebuild all three cards to the fixed M5 coefficients |
| 5.1 Data dated; staleness flagged | All data points dated; monthly pivot tier and the ATR(14) estimate are both explicitly flagged as single-source/indicative | §4, §6, §11, §19 | 5 | — |
| 5.2 Assumptions up front | Futures-to-spot normalisation (+33.15) stated with size and mechanism; anchor override (07:00 UK) stated in the title line, §2, §20 and §21a as a logged non-conformance, not silently presented as the instance default — compliant handling per the module's own wording | §21b, §19, §20 | 5 | — |
| 5.3 Red flags surfaced | §12/§15 risks present; §13d Hormuz/CPI collision risk is explicitly carried into every card as a caveat | §12, §15, §21b | 5 | — |
| 5.4 Restrictions honoured | No synthesised/interpolated price presented as sourced (explicit statement in §19); futures corroboration-only, normalised; no module codes or bracketed variable names in the body; however §6/§19 confidently label the erroneous 9-Jul Low as "Two-source corroborated" / "verified double-bottom" when the report's own better-matching evidence (Kitco range low 4,053.60, Investing.com range low 4,054.37 — both close to the true 4,054.23) was available in the same §4 table and was not used | whole report | 3 | do not label a chosen figure "verified"/"two-source" when better-matching same-table evidence contradicts it |

## 2. Category roll-up

| # | Category | Level (0-5) | Multiplier | Max | Points | Justification |
|---|---|---|---|---|---|---|
| 1 | Prompt adherence | 4 | 0.85 | 20 | 17.0 | All variables respected; audience register implicit not explicit |
| 2 | Structural alignment | 5 | 1.00 | 20 | 20.0 | All sections present, correctly ordered, real tables |
| 3 | Accuracy & evidence | 1 | 0.20 | 25 | 5.0 | Sources real and internally consistent, but the report's chosen 9-Jul Low, RSI2, and 6/7 daily pivot levels fail external reconciliation against the leak-free level file by multiples of tolerance, cascading through the OHLC table, technical narrative, and pivot-anchored trade cards |
| 4 | Reasoning & judgment | 3 | 0.65 | 20 | 13.0 | Pillar/synthesis reasoning strong (would be 4-5 alone), but card construction breaches fixed M5 coefficients (retracement %, ATR buffer ×2, swing-qualification threshold) |
| 5 | Currency & transparency | 4 | 0.85 | 15 | 12.75 | Strong dating/assumption/red-flag discipline and compliant anchor-override handling, offset by overclaiming "verified"/"two-source" status for the Low that fails reconciliation |

## 3. Total, band, override

c1=4
c2=5
c3=1
c4=3
c5=4
total=68
band=Moderate
override=none
card_integrity=95
n_cards=3
n_duds=0
n_warns=1

(17.0+20.0+5.0+13.0+12.75 = 67.75 → 68. No fabricated source found on spot-check → hallucinated-source override does not apply. No prompt restriction was openly violated → restriction-breach override does not apply.)

## 4. Card Integrity (linter rows, copied verbatim from `qa/gold_regen_qa1/lint_static/2026-07-10.csv`)

| card_id | strategy | flags | dud | per-card integrity |
|---|---|---|---|---|
| 2026-07-10_Trade_1 | Trade 1 - Daily Directional | SUPPRESSED | False | n/a — suppressed, excluded from the mean |
| 2026-07-10_Trade_2 | Trade 2 - Pivot, regime-aware | WARN_TP3_ORDER | False | 100 − 10×1 = 90 |
| 2026-07-10_Trade_3A | Trade 3A - Momentum-Pullback | CLEAN | False | 100 |

Report-level Card Integrity = mean over non-suppressed cards = (90 + 100) / 2 = **95**. n_cards=3, n_duds=0, n_warns=1. Card Integrity is separate from the 100-point Trust Score total.

Feedback: `qa/gold_regen_qa1/2026-07-10_feedback.md`
