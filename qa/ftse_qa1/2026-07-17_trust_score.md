# Trust Score v3.7 — FTSE 100 daily report, D = 2026-07-17 (run ftse_qa1)

Report: `reports/md/FTSE_EuroStoxx_Report_17Jul2026.md`
Level file: `data/levels/UK100_by_date/2026-07-17.csv` — `last_bar_date` = 2026-07-16 < D (leak-free, checked). Slice last bar 2026-07-16 22:45 broker.
Data basis used: `_cash` (the report claims "cash index close, LSE regular session"). Full-broker-day values shown where they change the verdict.
Stats run: `engine/qa_slice_stats.py --cash-open 10:00 --cash-close 18:30`, plus `--closes` with the report's five closes.

## Machine-readable result
```
c1=4
c2=5
c3=0
c4=3
c5=3
total=59
band=Low
override=hallucinated_source
card_integrity=96.7
n_cards=3
n_duds=0
n_warns=1
```
(Raw weighted total before the override cap = 60, Moderate; the hallucinated-source override caps it at 59 and sets C3 to 0. Without the override C3 would be about 2 on the row scores, and the report would still sit at the Moderate/Low boundary.)

## 1. Category 3 data check (report D-1 numbers vs level file, cash basis)

Tolerances (brief §4): close |Δ| <= 5, open/high/low |Δ| <= 10; close off by > 15 is a Category 3 failure.

| Date | Field | Report | Data (cash) | Δ (report − data) | Verdict |
|---|---|---|---|---|---|
| 10 Jul | O / H / L / C | 10502.10 / 10529.80 / 10465.30 / 10497.29 | 10490.1 / 10504.8 / 10451.1 / 10487.2 | +12.0 / +25.0 / +14.2 / +10.1 | all four out of tolerance |
| 13 Jul | O / H / L / C | 10498.05 / 10532.10 / 10478.40 / 10515.71 | 10488.1 / 10526.4 / 10455.7 / 10487.4 | +9.95 / +5.7 / +22.7 / +28.3 | L and C out; C > 15 |
| 14 Jul | O / H / L / C | 10512.40 / 10529.40 / 10424.60 / 10437.85 | 10460.4 / 10545.8 / 10411.5 / 10507.0 | +52.0 / −16.4 / +13.1 / −69.2 | O, H, L, C out; candle direction reversed (report: down 74.55; data: up 46.6) |
| 15 Jul | O / H / L / C | 10441.20 / 10529.00 / 10430.10 / 10515.92 | 10460.7 / 10536.2 / 10431.0 / 10498.7 | −19.5 / −7.2 / −0.9 / +17.2 | O and C out; C > 15 |
| 16 Jul (D-1) | O / H / L / C | 10470.77 / 10585.40 / 10462.90 / 10572.24 | 10453.9 / 10550.5 / 10429.4 / 10540.4 | +16.9 / +34.9 / +33.5 / +31.8 | all four out; C > 15 |

- Full-broker-day basis for 16 Jul (10475.9 / 10576.4 / 10426.3 / 10558.9): Δ = −5.1 / +9.0 / +36.6 / +13.3. The low is still 36.6 off and the close 13.3 off. The report matches neither basis.
- Tally (cash basis): 11 of 15 O/H/L cells out of tolerance; 5 of 5 closes out of the 5-pt tolerance; 4 of 5 closes off by more than 15 pts (14 Jul by 69.2).
- Every row is labelled "CORROBORATED (Δ 0.00)" with two named sources. A zero-delta corroboration that is 30–70 pts from the tape is not credible.
- RSI2: arithmetic reproduces from the report's own closes (19.1 / 50.1 / 100.0, tested with `--closes`), so the method is right. Against the data: 14 Jul 100.0 (report 19.1), 15 Jul 70.25 (report 50.1), 16 Jul 83.4 cash / 93.1 full (report 100.0). The 14 Jul Trend label "Bearish" is wrong on the data (close above open, RSI2 100).
- ATR14: report implies 88.88 (cards: "0.15 × ATR (13.33)", "88.88-point average range"; never stated as ATR14 in §9). Data 117.24 cash / 128.5 full. The report is 24% / 31% low. The 3×ATR cap, the 3.5×ATR cap, the R/ATR multiples and the 0.15×ATR confluence tolerance all inherit this error.
- Daily pivots (§11 vs data cash / full):

| Level | Report | Cash | Δ vs cash | Full | Δ vs full |
|---|---|---|---|---|---|
| R3 | 10739.96 | 10705.23 | +34.7 | 10764.87 | −24.9 |
| R2 | 10662.68 | 10627.87 | +34.8 | 10670.63 | −8.0 |
| R1 | 10617.46 | 10584.13 | +33.3 | 10614.77 | +2.7 |
| P | 10540.18 | 10506.77 | +33.4 | 10520.53 | +19.7 |
| S1 | 10494.96 | 10463.03 | +33.9 | 10464.67 | +30.3 |
| S2 | 10417.68 | 10385.67 | +32.0 | 10370.43 | +47.3 |
| S3 | 10372.46 | 10341.93 | +30.5 | 10314.57 | +57.9 |

  The report's pivots are arithmetically correct from its own H/L/C (checked: P, R1–R3, S1–S3 all reproduce); the error is in the inputs.
- Weekly pivots (6–10 Jul): report P 10506.13, R1 10609.56, S1 10393.86, R3 10825.26, S3 10178.16. Data cash P 10535.73, R1 10691.07, S1 10331.87, R3 11050.27, S3 9972.67. Δ: P −29.6, R1 −81.5, S1 +62.0, R3 −225.0, S3 +205.5. The report's implied week high is 10618.40; the data week high is 10739.6 (7 Jul). Weekly levels are mis-stated by far more than any tolerance.
- Monthly pivots (June): report P 10468.80, R1 10749.30, S1 10149.10 (implies June H 10788.50, L 10188.30, C 10429.60). Data cash June H 10608.8, L 10126.2, C 10501.5, P 10412.17, R1 10698.13, S1 10215.53. Δ P +56.6, R1 +51.2, S1 −66.4.
- Structure: report §9 says the 25 sessions peak at 10788.50 in June and July oscillates in a 10424–10585 band. Data: 25-session high 10739.6 on 7 Jul, low 10328.1 on 23 Jun; the 8 Jul close (10457.0) was 223.1 pts below the 7 Jul close (10680.1) and made a 10380.4 low on 9 Jul. The 2–9 Jul swing is absent from the report. Close sits at 51.6% of the 25-day range.
- KER: report 0.45 (net +209.74 / sum-abs 462.46). Recomputed on 13 sessions of cash closes: raw 0.07 (net +42.6 / 602.4), EMA(3)-smoothed 0.05; full-day closes 0.06 / 0.07. Both are below the report's own 0.13 trending threshold. The "efficiency confirms an upward transition" argument (§1, §9, §15, §16, §18, §21a) rests on a number the data does not support.
- Counters: USDX report "Rising, 100.73, CONFIRMS". Data daily closes: 10 Jul 100.976, 13 Jul 101.308, 14 Jul 100.910, 15 Jul 100.492, 16 Jul 100.709 — a five-session fall of 0.26% from 10 Jul, and 0.59% from the 13 Jul peak. The 16 Jul level (100.71) matches. S&P 500 CFD 16 Jul close 7526.2 vs report 7533.77: basis-level, consistent; five-day direction (falling) is right. VIX CFD 16 Jul close 17.6 vs report "16.4–16.9": about 1 pt low.
- Calendar (NEWS slice): US CPI (HIGH; y/y 3.5 vs 3.8 consensus, core 2.6 vs 2.9) was released 14 Jul 15:30 broker, not 15 Jul as in §13c. US PPI m/m (−0.3 vs +1.6 consensus) was released 15 Jul, not 16 Jul. 16 Jul US retail sales and Philadelphia Fed (41.4 vs 10.3) are not in §13c. For D itself the calendar has Eurozone CPI y/y (HIGH, 12:00 broker = 10:00 UK, consensus 3.0) and US Michigan sentiment (17:00 broker = 15:00 UK); §13d starts on Mon 20 Jul and omits D entirely. UK GDP (May) is not in the calendar slice (not corroborated, not counted as an error).

## 2. Section 7 checklist (every row)

| Item | Reviewer notes | Evidence observed | Score |
|---|---|---|---|
| 1.1 Variables respected | FTSE 100 cash primary, Euro Stoxx secondary with no cards; counters USDX / S&P 500 / DAX 40 (+ Brent in §12); Europe/London, D-1 as-of, 5-session lookback, GBP / points, 07:00 UK anchor on Trade 1. Weak points: the six sources are Tier 1 index provider plus media/aggregators, with no exchange or sell-side source; DAX single-source; Trade 1 "market at 07:00 anchor" but entry priced at the D-1 close. | §2, §4, §10, §21b | 4 |
| 1.2 Coverage & currency consistent | Data dates are D-1 or earlier and currency is consistent. Drift: the holding window is treated as starting Mon 20 Jul ("Monday's binary sits at the very start of the window", "pullback entries may not fill until after Monday"), §13d omits D (Fri 17 Jul, which carries Eurozone CPI y/y at 10:00 UK), while Trade 1 triggers at the 08:00 open on 17 Jul. | §12, §13d, §21b caveats | 3 |
| 1.3 Audience & tone | Senior strategist register, trading-and-risk-review footer, no retail tone. | whole report | 4 |
| 2.1 Sections present & ordered | §1–§21 present in order; §13a–d and §21a–d present; §17 is one sentence. | headings | 5 |
| 2.2 Scorecard as a table | §6 is a full table with every required column; §11 daily / weekly / monthly tables R3→P→S3. | §6, §11 | 5 |
| 2.3 Method steps visible | §4→§5 observation to consensus; §8 candle-by-candle plus sequence; §9 regime, VOLator, KER with numerator and denominator. ATR14 value never stated in §9; persistence/overlap not quantified; five chart captions present (images dropped, accepted). | §4–§9 | 4 |
| 3.1 Quantitative claims sourced | §12 and §14 attribute many figures by name (Peel Hunt, XTB, Deutsche Bank, ONS) but few appear in §4 or §13a; Brent, gilt, Fed-odds and ECB-rate figures carry no link; VIX "16.4–16.9" does not match the feed (17.6); USDX direction wrong. | §1, §12, §14 | 3 |
| 3.2 Citations exist & contain data | Three spot-checks all fail (see §3 below): Newsquawk row, CNBC URL date, Sunday Guardian headline. | §4, §13a | 0 |
| 3.3 Calculations transparent | RSI2 reproduces from the report's closes; every pivot reproduces from its stated H/L/C; §21a sum (+0.496) and weights (0.25/0.20/0.10/0.15/0.15/0.15) reproduce. Against that: ATR14 value not stated as such (implied 88.88 vs data 117.24); KER 0.45 not reproducible (data 0.05–0.07) and "EMA 3" not stated; sentiment tilt +0.22 has no formula (raw balance is 0). | §6, §9, §11, §21a | 3 |
| 3.4 Numbers reconcile | D-1 close 10,572.24 identical in §1/§3/§4/§6/§21b; §11 pivots equal card pivots; §6 RSI2 = §8 = §21a input. Breaks: §21d "twelve fills" vs 9 fills in the §21c table; Trade 2 "aggregate +0.2R" vs +1.2R summed from the table (−0.4, +0.6, −1.0, +1.0, +1.0); "two winners, one full stop, two marginal" vs three winners, one stop, one −0.4R; 3A swing endpoints (10,388.20, 10,618.40) lie outside every high/low in §6 and contradict §9's "10,424–10,585 band"; Newsquawk 14 Jul 10,529 vs §6 10,437.85. | §6, §9, §21c–d | 2 |
| 4.1 Pillars conclude | §9 and §10 end in labels (transition resolving upward; MIXED). §8 ends on a caveat without an explicit direction label; §12 has per-driver tags but no pillar conclusion; §14 table has no direction label. | §8, §9, §10, §12, §14 | 3 |
| 4.2 Cross-asset interpreted | Good mechanisms (80% overseas earnings, US risk beta, ECB path, Shell/BP weight, decoupling analysis). Marked down because the USDX row says "Rising / CONFIRMS" while the feed shows the dollar falling over the window, and its own text says the channel was "muted"; Brent has no counter row. | §10 | 4 |
| 4.3 Synthesis reconciles tensions | KER-vs-regime contradiction and the cross-asset contradiction are named and given a precedence rule. Not reconciled: §17 / §16 forecast ceiling (10,609–10,617 band; range top 10,660) vs Trade 1 TP1 10,681.58 and TP2 10,790.92; TRANSITION regime vs trend-style Trade 3A and support-buy Trade 2; §16 "low conviction" vs §16/§18 "MEDIUM". | §15–§18, §21 | 3 |
| 4.4 Calibrated language | §17 is exactly one sentence; HIGH/MEDIUM stated in §3, §16, §18. "HIGH confidence" on a price the data contradicts is mis-calibrated; the low/medium mismatch is minor. | §3, §16, §17, §18 | 4 |
| 4.5 Card construction (protocol) | All three cards break fixed M5 rules (detail in feedback): T1 stop has no 0.25×ATR buffer and entry text is both "market" and "pending buy"; T2 buys the pivot as support under a TRANSITION label (rule: breakout side only), TP3 below TP2, entry equals invalidation; T3A uses the trend fork under TRANSITION (rule: 3C), enters at 38.2% not 57.5%, stops at the 61.8% retrace not beyond the swing origin, TP1 at 23.6% not 38.2%, and the swing endpoints do not exist in the data (no up-swing >= 2×ATR14 = 234.5 with an intact origin). | §21b | 2 |
| 5.1 Data dated; staleness flagged | Prices and articles dated; 10/13 Jul H/L, weekly/monthly extremes and DAX flagged single-source. The Newsquawk row is dated "16 Jul (prior session)" yet quotes a 14 Jul level. | §4, §6, §13, §19 | 4 |
| 5.2 Assumptions up front | Pivot single-source flag propagates to the cards. The key assumption (no data feed reached; OHLC "assembled from published reporting"; 25-session series reconstructed) sits in §19/§20 only, while §3 and §5 present the close as "a published index close, not a derived quote" at HIGH confidence. No anchor-override (proxy open) caveat on the cards. | §3, §5, §19, §20, §21b | 3 |
| 5.3 Red flags surfaced | §12/§15 carry the Mahmood binary, CPI, ECB, narrow participation, cross-asset contradiction; §13d collisions carried into card caveats. Omits D-day events (Eurozone CPI y/y 10:00 UK; US Michigan 15:00 UK). | §12, §13d, §15, §21b | 4 |
| 5.4 Restrictions honoured | No bracketed variable names, module codes or framework name found (the "v2.1 baseline" mention is the only meta reference). CFD quotes excluded in text. Concerns: closes and the 25-session series are presented as sourced / "exact and multiply corroborated" when §19 admits they were reconstructed from reporting, and the numbers do not match the tape; futures are used as an explanatory driver ("softer futures") rather than confirmation only. Treated as a concern here; the stricter hallucinated-source cap already governs. | whole report | 2 |

## 3. Spot-check of three cited sources (row 3.2)
1. Newsquawk (§4): "16 Jul (prior session)", raw quote 10,529 (+0.30%), note "Corroborates 14 Jul session". The report's own 14 Jul close is 10,437.85 (§6, "CORROBORATED, FTSE Russell × LSE tape") — a 91-pt contradiction; the row is still counted in the "six sources agree to the hundredth of a point" claim in §3 and §5 (two of the six are whole-point and one is a different day).
2. CNBC (§13a): URL path `/2026/07/15/` but dated "16 Jul 2026" with the quote "Stocks fell on Thursday" (16 Jul 2026 is a Thursday, 15 Jul a Wednesday). Wrong date against its own URL.
3. Sunday Guardian (§13a, and Source B for the 13 and 15 Jul closes in §6): headline "FTSE 100 Falls 0.37% While FTSE 250 Gains" dated 16 Jul, but the report has the FTSE 100 up 0.54% (+56.32) that day. A source whose own headline contradicts the figure it is cited for. Also the ONS "official" row reuses the Proactive URL, and the Trading Economics URL is a generic currency page.
Per brief §2 row 3.2 these self-contradictory / impossible citations count as fabricated. Together with "Δ 0.00" dual-source corroboration of five closes that the tape contradicts by 10–69 pts, the hallucinated-source override applies: C3 = 0, total capped at 59.

## 4. Category roll-up

| # | Category (max) | Row scores | Level | Multiplier | Points | Justification |
|---|---|---|---|---|---|---|
| 1 | Prompt adherence (20) | 4, 3, 4 | 4 | 0.85 | 17.00 | Variables largely respected; window drift to Monday and D omitted from §13d. Not reduced further because the override already applies. |
| 2 | Structure (20) | 5, 5, 4 | 5 | 1.00 | 20.00 | All sections, tables and ordering present. |
| 3 | Accuracy & evidence (25) | 3, 0, 3, 2 | 0 (override) | 0.00 | 0.00 | Fabricated-source override; independently OHLC, ATR, KER, pivots (all three timeframes) and USDX direction fail against the data. |
| 4 | Reasoning & judgment (20) | 3, 4, 3, 4, 2 | 3 | 0.65 | 13.00 | Good mechanism writing; synthesis gaps; all three cards break M5 construction rules. |
| 5 | Currency & transparency (15) | 4, 3, 4, 2 | 3 | 0.65 | 9.75 | Dated and flagged, but provenance caveat buried and reconstructed data presented as corroborated. |

Total = 17.00 + 20.00 + 0.00 + 13.00 + 9.75 = 59.75, rounded 60 (Moderate). Override cap: hallucinated source, Low band 40–59, so total = 59, band = Low.

## 5. Override check
- Hallucinated source: TRIGGERED (three failed spot-checks, section 3). C3 = 0; cap 59.
- Restriction breach: row 5.4 scored 2 (reconstructed / synthesised data presented as sourced). Not separately applied, because the hallucinated-source cap is the binding one.

## 6. Card Integrity (linter rows copied verbatim from `qa/ftse_qa1/lint_static/2026-07-17.csv`; not re-derived)

| card_id | strategy | flags | dud | Card score |
|---|---|---|---|---|
| 2026-07-17_Trade_1 | Trade 1 - Daily Directional | CLEAN | False | 100 |
| 2026-07-17_Trade_2 | Trade 2 - Pivot (regime-aware) | WARN_TP3_ORDER | False | 90 |
| 2026-07-17_Trade_3A | Trade 3 - Momentum-Pullback (variant 3A) | CLEAN | False | 100 |

Report-level Card Integrity = (100 + 90 + 100) / 3 = 96.7. n_cards = 3, n_duds = 0, n_warns = 1. Separate from the 100; note that static CLEAN does not cover the rule-construction defects scored in row 4.5.
