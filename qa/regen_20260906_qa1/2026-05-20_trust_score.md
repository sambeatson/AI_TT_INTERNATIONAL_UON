# Trust Score — 2026-05-20 — SP500_Daily_Report_20May2026.md

Run: regen_20260906_qa1 · D = 2026-05-20 · D-1 slice = data/slices/US500/US500_upto_2026-05-19.csv · Lint: qa/regen_20260906_qa1/lint_static/2026-05-20.csv

Report's stated D-1 basis (19 May): O 7399.50 · H 7402.90 · L 7349.50 · C 7353.61 · RSI2 column 88.4 / 71.2 / 28.6 / 22.4 / 9.8 · ATR(14) 78.4 (stated only inside the Trade 2 card) · daily P 7368.67 (R1 7387.84 / S1 7334.44 / R2 7422.07 / S2 7315.27 / R3 7441.24 / S3 7281.04) · weekly P 7437.01 (R1 7488.61 / S1 7356.89) · monthly P 7066.67 (approximate April H/L/C) · direction score +0.02 → NEUTRAL · regime Trending-bullish (first pullback), KER 0.21 · cards: Trade 1 SUPPRESSED; Trade 2 LONG buy-stop 7442.17 / SL 7372.92 / TP 7488.61-7528.67-7568.73; Trade 3A LONG buy-limit 7360.00 / SL 7325.00 / TP 7395.00-7433.31-7453.09.

Slice (helper, cash session 16:30–23:00 broker): 19 May O 7371.0 · H 7399.8 · L 7339.1 · C 7362.3 · RSI2 0.00 · ATR14 76.13 (full-day 83.28) · daily P 7367.07 / R1 7395.03 / S1 7334.33 / R2 7427.77 / S2 7306.37 / R3 7455.73 / S3 7273.63 · weekly P 7428.07 / R1 7510.83 / S1 7333.23 · 5d swing H 7522.90 (14 May) L 7339.10 (19 May).

## 1. Section 7 checklist

| Item | Reviewer notes | Evidence observed | Score 0–5 | Action required |
|---|---|---|---|---|
| 1.1 Variables respected | Asset = S&P 500 cash index; counters listed USDX first (Dollar Index · VIX · DAX 40); lookback 5 sessions; USD / index points / tick 0.01; 7 price sources across index-provider / exchange / aggregator tiers. Two deviations: as-of is stated as "20 May 2026 (pre-open)" rather than the NY close of D-1; the daily-open anchor is moved to the 20 May cash open (14:30 UK) instead of 07:00 UK, described in §20 as a "user override" with no basis given. | Header line 5; §2 rows Asset/As-of/Lookback/Currency/Tick; §4 (7 rows); §20 "M5 trace — daily-open anchor: User override applied" | 3 | Restore 07:00 UK anchor (or evidence the override); state as-of as NY close 19 May |
| 1.2 Coverage & currency consistent | All price/article dates are ≤ 19 May; §13d is a forward calendar (allowed). Units stable (USD points; DAX kept native EUR and disclosed). Two drift points: §20 says the report was "generated 19 May 2026 (US session in progress)" while every §4 row cites the 16:00 ET official close of 19 May — the stated generation time precedes the data it uses; and the 5-day window here re-dates the 7,501.24 close to 13 May whereas the 19 May report gave 14 May close = 7,501.24 (see §5 log). | §20 Timestamp bullet; §4; §6a vs 19 May report §6 | 3 | Fix generation timestamp; make the 13/14 May rows agree with the prior report or explain the revision |
| 1.3 Audience & tone | Senior-strategist register throughout; trading-and-risk-review use stated in §2; no retail phrasing. One unsourced folk-statistic in §15 ("RSI2 < 10 … positive 3-day returns >70% of the time") reads as retail colour but tone is otherwise consistent. | §1, §2 Use case, §18 | 5 | none |
| 2.1 Sections present & ordered | §1–§21 all present in order, including §13a/b/c/d and §21a/b/c/d; §21d carries the what-is-working summary and the verbatim limitations statement. | Headings §1…§21d | 5 | none |
| 2.2 Scorecard as a table | §6 is a table but its columns are Date/O/H/L/C/RSI2/Trend/Sources/Validation — the Source A / Source B / Final columns are merged into a single "Sources" cell and no "Final" column exists. §11 daily/weekly/monthly tables run R3→P→S3 with three levels each side (plus R1.5/S1.5). | §6a header row; §11a–c | 4 | Split §6 sources into Source A / Source B / Final |
| 2.3 Method steps visible | §4 observations → §5 classification/consensus shown; §8 candle-by-candle with sequence label; §9 gives overlap 0.32, persistence 0.71, VOLator series, KER 0.21. §7 charts are ASCII placeholders (pandoc-dropped PNGs acknowledged) — accepted as evidence, noted; the ASCII candles do not carry price labels that tie to §6. | §4–§9; §7 caption "standalone PNGs are produced to the session output folder" | 4 | none (charts accepted as placeholders) |
| 3.1 Quantitative claims sourced | §1 numbers trace to §6/§13. §12/§14 carry several figures with an institution named but no article in §13a (HSBC $325 / MS $285 targets, ~30x trailing P/E, fwd ~21x, tomato prices +15% m/m, Wolfe positioning); §15 bull-case statistic unsourced; §10 "USDX +0.5% on the week" not supported by §6c (98.92→99.06 = +0.14%). | §12 Valuation/Positioning rows; §14 Inflation row; §15 bull 2; §10 USDX row | 3 | Add sources for §12/§14 figures or point them to §13a |
| 3.2 Citations exist & contain data | Spot-checks: (a) CNBC 19 May "third straight losing session / 30Y briefly above 5.19%" — figure used consistently in §1, §12, §14: consistent. (b) Motley Fool 19 May "bull-case 7,750 / earnings $334" — consistent with §12: consistent. (c) Trading Economics 19 May "US500 falls 0.42%" — the report's own 19 May move is −0.67% (§13c, and 7403.05→7353.61); the quoted figure does not match the report's data (CFD basis could explain part, but the row is also the only CFD quote admitted into §4). (d) FRED is cited in §4 as the 19 May EOD source while §20 notes FRED carries a 1-business-day lag and that the report was generated 19 May during the session — the citation is self-contradictory on timing. (e) §19 sources the monthly pivots to "Wikipedia closing-milestones", not an approved tier. No citation is provably fabricated without fetching; the timing contradiction is recorded but not escalated to the hallucination override. | §13a rows 1, 3, 4; §4 FRED row; §20 Source attempts; §19 Monthly pivots | 2 | Reconcile TE figure; remove or re-date the FRED citation; replace Wikipedia |
| 3.3 Calculations transparent | Pivots: all §11a daily and §11b weekly levels reproduce exactly from the report's own H/L/C (P 7368.67, R1 7387.84, S1 7334.44, R2 7422.07, S2 7315.27, R3 7441.24, S3 7281.04; weekly P 7437.01 …); monthly levels reproduce from the stated approximate 7150/6950/7100. §21a score derivation shown and sums (+0.0225 → +0.02) with the correct weights. KER (13, EMA 3) stated. RSI2 is NOT shown and does NOT reproduce: from the report's own closes (7501.24, 7488.95, 7408.50, 7403.05, 7353.61) the helper gives 0.0 / 0.0 / 0.0 for 15/18/19 May (three consecutive down closes ⇒ mean gain 0) against the report's 28.6 / 22.4 / 9.8. ATR(14) is not stated in §9; it appears only inside the Trade 2 card (78.4) and implicitly in the 3A stop (0.25 × 78.4 = 19.6). | §11a/b/c; §20 direction-score bullet; §9 KER; helper output; §21b Trade 2 TP3 | 2 | Show RSI2 arithmetic and correct the column; state ATR(14) in §9 |
| 3.4 Numbers reconcile | Consistent: D-1 close 7,353.61 identical in §1/§3/§4/§6/§18/§21c; §11 pivots = card pivots; RSI2 9.8 in §6 = §8 = §15/§18. Breaks: (i) §6 closes vs slice cash closes off by +49.7 (13 May), −20.2 (14 May), −7.5, −8.0, −8.7 pts — two closes wrong by >10 pts; (ii) §1 "closed at 2.3% of the daily range" vs §8 "close at 7%" (own numbers give 7.7%); (iii) §1 DAX "+0.38%" vs §6d/§10 24308→24479 = +0.70%; (iv) Chart 3 "18.3% retracement" and §15 "only 18%" vs §9 "65% of range" — own numbers give 34.7% retraced; (v) §11 pivot read "Monthly R1=7183.33 aligns with the 7,353 area" — 170 pts apart; (vi) §1 and §15 place "weekly S1 / monthly R1" confluence at 7,150 while §11b weekly S1 = 7356.89; (vii) Trade 2 confluences: "daily R1=7387.84 sits ~2pts above the entry" — it is 54 pts below 7442.17; "SL between daily P and S1" — 7372.92 is above P 7368.67; (viii) §9 "score is mildly negative" vs §20/§21a +0.02; (ix) §13c "15 May −0.91%" vs own closes −1.07%; (x) 13/14 May rows contradict the 19 May report (7,501.24 was the 14 May close there; 15 and 18 May H/L differ by 14–19 pts; RSI2 8.3/7.5 there vs 28.6/22.4 here); (xi) ATR 78.4 here vs ≈68 in the 19 May report, unexplained. | §5 log below; §1 ll.10–35; §8 19 May bullet; §9; §11 pivot read; §15 bear 4; §21b Trade 2 Confluences | 1 | Rebuild §6 from corroborated cash prints; fix the nine internal breaks listed |
| 4.1 Pillars conclude | §8 ends "Exhaustion — reversal risk"; §9 "Bias: Bullish (medium-term)"; §10 ends with a mixed-but-interpreted summary; §12 carries a Direction per factor; §14 is readings only with no direction label. | §8 Judgement label; §9 Bias; §10 summary; §12 Direction column; §14 | 4 | Add a direction conclusion to §14 |
| 4.2 Peer/cross-asset interpreted | §10 gives a mechanism per counter (USD → foreign revenue; VIX inverse; DAX as common-factor gauge → "localised US weakness") and a confirm/contradict verdict; the DAX divergence argument is carried into §18. The USDX read quotes +0.5% on the week that §6c does not support. | §10 Mechanism/Read/Confirm columns; §18 Reason 2 | 4 | Correct the USDX weekly change |
| 4.3 Synthesis reconciles tensions | §15/§16/§18 reconcile short-term exhaustion vs medium-term uptrend, and §21a addresses §17 vs the cards. Card construction (scored here per protocol) is weak: Trade 3A is labelled Momentum-Pullback but its entry (7360, "demand-zone retest") is not the 57.5% retrace of any logged swing — the logged swing 7517.12→7349.50 is the down-leg, which yields no long fib entry; its TP ladder is +1R / 50% / 61.8% instead of 38.2% / 0% / 100%+; TP3 carries two values (7453.09 and an "override" to 7517.12); the stop is "≈7,330 … rounded conservatively to 7,325" (arbitrary 5-pt extension); thesis invalidation "coincides with SL" (rule requires separation); the limit 7360 sits above the report's own D-1 close 7353.61. Trade 2 levels follow the TREND formula from the report's weekly pivots (7437.01 + 0.10×51.60 = 7442.17; 7437.01 − 0.8×80.12 = 7372.91) but TP1 is labelled "+1R structural" while 7488.61 − 7442.17 = 46.44 = 0.67R, the confluence text is wrong (see 3.4 vii), and the invalidation logic is inverted (a close back through 7437.01 occurs before a 7372.92 stop, not after). §9 also says Trade 1 carries a "SHORT signal … mildly negative" while §20 derives +0.02 NEUTRAL. | §21b Trade 3A Entry/Stop/TP/Invalidation rows; §20 Trade 3 gate; §21b Trade 2 TP1/Confluences/Invalidation; §9 Preferred trade protocol | 2 | Rebuild Trade 3A to the 3A rule; fix Trade 2 labels/confluences/invalidation |
| 4.4 Calibrated language | §17 is exactly one sentence, no hedge stacking; §16 scenario probabilities sum to 100%. Confidence is stated as "Medium-High" in §3 and "Medium" in §18 — inconsistent. | §17; §3 Confidence; §18 Confidence | 3 | Align §3 and §18 confidence labels |
| 5.1 Data dated; staleness flagged | Every price row and article carries a date; monthly pivots flagged single-source-indicative and excluded from entries. But §19 asserts "all OHLC fields fully corroborated within ±0.10pt for all five sessions" and "No data gaps. No fabricated data." while two closes differ from the slice by 20–50 pts and the 13/14 May rows contradict the prior report; FRED's 1-day lag is noted only in §20, not on the §4 row. | §6, §13a, §19 bullets 1 and 10, §20 | 3 | Downgrade §19 corroboration claims to what the evidence supports |
| 5.2 Assumptions up front | Anchor override is stated in the header, on the Trade 2 card ("anchor override applied") and in §20; single-source flag on monthly pivots propagated to the Trade 2 caveat. The override's justification ("User override") is asserted, not shown. | Header l.5; §21b Trade 2 Entry/Caveats; §20 anchor bullet; §11 pivot read | 4 | State the basis for the anchor override |
| 5.3 Red flags surfaced | §12 and §15 enumerate rates, NVDA, positioning, geopolitics; the §13d NVDA collision is carried onto both live cards as a caveat with a management instruction. | §12; §15; §13d row 1; §21b Caveats on Trade 2 and 3A | 5 | none |
| 5.4 Restrictions honoured | Breached: module codes appear openly — "M5 trace" ×6 and "this M1 instance" in §20, "v2.1 baseline / v2.1 weights" in §20/§21a — and a raw variable name "MAX_SIMULTANEOUS_LONG_SHORT = YES" in §20. Also: a CFD-tracked quote (TradingEconomics) is admitted into the §4 OHLC evidence table (disclosed, corroboration-only); §11c presents pivots built from synthesised "approximate" April H/L/C (flagged); Wikipedia used as a pivot source. ES futures are confirmation-only (§3) — compliant. No framework name in the report. | §20 bullets 6–10; §21a Score basis; §4 TradingEconomics row; §11c Notes; §19 Monthly pivots | 1 | Strip module codes / variable names from §20–§21; move CFD row out of §4; restriction override applies |

## 2. Category roll-up

| Category | Level | Multiplier | Points | Justification |
|---|---|---|---|---|
| C1 Prompt adherence (20) | 3 | 0.65 | 13.00 | Rows 3/3/5 → mean 3.67 → 4; reduced one level to 3 by the restriction-breach override (module codes and variable name in §20/§21a). Anchor moved to 14:30 UK without basis; as-of drift. |
| C2 Structure (20) | 4 | 0.85 | 17.00 | Rows 5/4/4 → mean 4.33 → 4. All 21 sections and sub-sections in order; §6 lacks Source A/B/Final columns; charts are placeholders. |
| C3 Accuracy & evidence (25) | 2 | 0.40 | 10.00 | Rows 3/2/2/1 → mean 2.0 → 2. RSI2 column does not reproduce from the report's own closes; 13 May close 49.7 pts and 14 May close 20.2 pts off the slice; nine internal reconciliation breaks; FRED/TE citations internally inconsistent. |
| C4 Reasoning & judgment (20) | 3 | 0.65 | 13.00 | Rows 4/4/2/3 → mean 3.25 → 3. Pillars conclude and cross-asset is interpreted; Trade 3A is not built to the 3A rule and Trade 2 carries wrong labels/confluences; confidence label inconsistent. |
| C5 Currency, restrictions & transparency (15) | 3 | 0.65 | 9.75 | Rows 3/4/5/1 → mean 3.25 → 3. Data dated and red flags carried to cards, but §19 overstates corroboration and prompt restrictions are openly breached. |
| **Total** | | | **62.75 → 63** | |

## 3. Total, band, override check

- Total: **63/100** (13 + 17 + 10 + 13 + 9.75 = 62.75, rounded to 63).
- Band: **Moderate** (60–74).
- Overrides: **restriction_breach** — §20 contains six "M5 trace" bullets, "this M1 instance", "v2.1 baseline" and the raw variable name "MAX_SIMULTANEOUS_LONG_SHORT = YES"; §21a repeats "v2.1 weights". Per framework §6 the output is capped at Moderate (already inside the cap) and Category 1 is reduced by one level (4 → 3, applied above). Hallucinated-source override not triggered: the FRED-lag/timestamp contradiction and the TradingEconomics −0.42% figure are recorded as citation-consistency failures in row 3.2, not as proven fabrication.

## 4. Card Integrity

Linter rows (qa/regen_20260906_qa1/lint_static/2026-05-20.csv, verbatim):

| card_id | report_date | strategy | flags | dud |
|---|---|---|---|---|
| 2026-05-20_Trade_1 | 2026-05-20 | Trade 1 - Daily Directional | SUPPRESSED | False |
| 2026-05-20_Trade_2 | 2026-05-20 | Trade 2 - Pivot (weekly TREND breakout) | CLEAN | False |
| 2026-05-20_Trade_3A | 2026-05-20 | Trade 3A - Momentum-Pullback (demand-zone retest) | CLEAN | False |

| Card | #DUD | #WARN | Integrity |
|---|---|---|---|
| 2026-05-20_Trade_1 | — | — | suppressed (excluded from mean) |
| 2026-05-20_Trade_2 | 0 | 0 | 100 |
| 2026-05-20_Trade_3A | 0 | 0 | 100 |
| **Report mean (non-suppressed)** | 0 | 0 | **100.0** |

n_cards = 3 (incl. suppressed) · n_duds = 0 · n_warns = 0. Note: the static linter tests levels against the slice close (7362.30); against the report's own stated close (7353.61) the Trade 3A buy-limit at 7360.00 would sit on the wrong side — this is recorded under row 4.3 and in the feedback, not in the integrity number.

## 5. Data reconciliation log

Slice = cash session 16:30–23:00 broker (helper output). Tolerance per brief: |Δ| ≤ 3 pts on a close, ≤ 8 pts on O/H/L = consistent.

| # | Section / field | Report value | Slice value | Δ (report − slice) | Verdict |
|---|---|---|---|---|---|
| 1 | §6a 13 May Open | 7440.10 | 7412.0 | +28.1 | discrepancy |
| 2 | §6a 13 May High | 7510.50 | 7466.0 | +44.5 | discrepancy |
| 3 | §6a 13 May Low | 7430.80 | 7381.5 | +49.3 | discrepancy |
| 4 | §6a 13 May Close | 7501.24 | 7451.5 | +49.7 | **Category 3 failure (>10 pts)**; also contradicts 19 May report (14 May close = 7,501.24 there) |
| 5 | §6a 14 May Open | 7505.40 | 7463.9 | +41.5 | discrepancy |
| 6 | §6a 14 May High | 7517.12 | 7522.9 | −5.8 | consistent |
| 7 | §6a 14 May Low | 7470.20 | 7462.9 | +7.3 | consistent |
| 8 | §6a 14 May Close | 7488.95 | 7509.1 | −20.2 | **Category 3 failure (>10 pts)** |
| 9 | §6a 15 May Open | 7484.30 | 7442.3 | +42.0 | discrepancy |
| 10 | §6a 15 May High | 7491.60 | 7458.0 | +33.6 | discrepancy |
| 11 | §6a 15 May Low | 7385.40 | 7402.8 | −17.4 | discrepancy |
| 12 | §6a 15 May Close | 7408.50 | 7416.0 | −7.5 | discrepancy (3–10 pts) |
| 13 | §6a 18 May Open | 7402.80 | 7423.0 | −20.2 | discrepancy |
| 14 | §6a 18 May High | 7415.20 | 7438.5 | −23.3 | discrepancy |
| 15 | §6a 18 May Low | 7385.50 | 7358.0 | +27.5 | discrepancy |
| 16 | §6a 18 May Close | 7403.05 | 7411.0 | −8.0 | discrepancy (3–10 pts) |
| 17 | §6a 19 May Open (D-1) | 7399.50 | 7371.0 | +28.5 | discrepancy |
| 18 | §6a 19 May High (D-1) | 7402.90 | 7399.8 | +3.1 | consistent |
| 19 | §6a 19 May Low (D-1) | 7349.50 | 7339.1 | +10.4 | discrepancy |
| 20 | §6a 19 May Close (D-1; also §1/§3/§4/§18) | 7353.61 | 7362.3 (full-day 7356.3) | −8.7 (−2.7 vs full-day) | discrepancy vs cash basis (3–10 pts) |
| 21 | §6a RSI2 13/14/15/18/19 May vs slice-close RSI2 | 88.4 / 71.2 / 28.6 / 22.4 / 9.8 | 80.81 / 100.00 / 38.22 / 0.00 / 0.00 | +7.6 / −28.8 / −9.6 / +22.4 / +9.8 | discrepancy |
| 22 | §6a RSI2 15/18/19 May vs recomputation from the report's OWN closes | 28.6 / 22.4 / 9.8 | 0.0 / 0.0 / 0.0 | +28.6 / +22.4 / +9.8 | **Category 3 failure — RSI2 does not reproduce** |
| 23 | §6a Trend labels vs report's own O/C/RSI2 | Bullish / Neutral / Bearish ×3 | rule applied to report's own numbers gives the same | 0 | consistent (internally) |
| 24 | §11a daily pivots vs report's own 19 May H/L/C | P 7368.67 R1 7387.84 S1 7334.44 R2 7422.07 S2 7315.27 R3 7441.24 S3 7281.04 | recomputed: identical | 0.00 | reproduces |
| 25 | §11a daily pivots vs slice cash pivots | P 7368.67 / R1 7387.84 / S1 7334.44 | P 7367.07 / R1 7395.03 / S1 7334.33 | +1.6 / −7.2 / +0.1 | consistent (basis) |
| 26 | §11b weekly pivots vs report's own W/E 15 May H/L/C (7517.12/7385.40/7408.50) | P 7437.01 R1 7488.61 S1 7356.89 R2 7568.73 S2 7305.29 R3 7620.33 S3 7225.17 | recomputed: identical (R3 7620.34, S3 7225.18 rounding) | ≤0.01 | reproduces |
| 27 | §11b weekly pivots vs slice weekly (cash) | P 7437.01 / R1 7488.61 / S1 7356.89 | P 7428.07 / R1 7510.83 / S1 7333.23 | +8.9 / −22.2 / +23.7 | discrepancy (inputs: prior-week H/L/C differ from slice) |
| 28 | §11c monthly pivots vs stated April 7150/6950/7100 | P 7066.67 R1 7183.33 … | recomputed: identical | 0 | reproduces (inputs are synthesised "approximate" values) |
| 29 | ATR(14) (Trade 2 card, "3 × 78.4") | 78.4 | 76.13 cash / 83.28 full-day | +2.3 / −4.9 | consistent; not stated in §9; 19 May report gave ≈68 |
| 30 | §1 close position in 19 May range | 2.3% | 7.7% from report's own O/H/L/C (§8 says 7%) | — | internal break |
| 31 | §1 DAX 40 daily change | +0.38% | +0.70% from §6d (24308→24479; §10 says +0.7%) | — | internal break |
| 32 | Chart 3 / §15 retracement of 25-day move | 18.3% / "18%" | 34.7% from report's own 7046.55/7517.12/7353.61 (§9's "65% of range" agrees with 34.7%) | — | internal break |
| 33 | §11 pivot read "Monthly R1=7183.33 aligns with 7,353 area" | 7183.33 ≈ 7353 | 170 pts apart | — | internal break |
| 34 | §1 / §15 "7,150 … weekly S1 / monthly R1" | weekly S1 at ~7,150 | §11b weekly S1 = 7356.89 | — | internal break |
| 35 | §21b Trade 2 confluence "daily R1=7387.84 ~2pts above entry 7442.17" | +2 | −54.3 | — | internal break |
| 36 | §21b Trade 2 "SL between daily P 7368.67 and S1 7334.44" | between | 7372.92 is above P | — | internal break |
| 37 | §21b Trade 2 "TP1 … (+1R structural)" | 1R = 69.25 | 7488.61 − 7442.17 = 46.44 = 0.67R | — | internal break |
| 38 | §9 "Trade 1 SHORT signal … score mildly negative" vs §20/§21a | negative | +0.02 | — | internal break |
| 39 | §10 USDX "+0.5% on the week" vs §6c | +0.5% | 98.92→99.06 = +0.14% | — | internal break |
| 40 | §13c "15 May SPX −0.91%" vs §6a closes | −0.91% | 7488.95→7408.50 = −1.07% | — | internal break |
| 41 | §13a TradingEconomics "US500 falls 0.42%" (19 May) vs §13c "Index −0.67%" | −0.42% | −0.67% | — | citation-consistency break |
| 42 | §3 vs §18 confidence | Medium-High | Medium | — | internal break |
| 43 | §6b VIX 19 May close | 18.61 | 18.75 (slice) | −0.14 | consistent (counter, basis) |
| 44 | §6c USDX 19 May close | 99.06 | 99.337 (slice) | −0.28 | discrepancy (counter; >0.05 tolerance the report itself claims) |
| 45 | §6a 13/14 May vs 19 May report §6 | 13 May C 7501.24; 14 May C 7488.95; 15 May O/H/L 7484.30/7491.60/7385.40; 18 May O/H/L 7402.80/7415.20/7385.50; RSI2 15/18 May 28.6/22.4 | 19 May report: 14 May C 7501.24 (RSI2 100); 15 May O/H/L 7497.50/7506.80/7392.65; 18 May O/H/L 7415.07/7434.06/7371.75; RSI2 8.3/7.5 | up to 19 pts; RSI2 +20/+15 | cross-report inconsistency |
