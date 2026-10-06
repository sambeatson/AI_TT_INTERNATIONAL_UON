# Trust Score v3.7 — FTSE 100 / Euro Stoxx 50 Daily, D = 2026-05-19
Report: `reports/md/FTSE_EuroStoxx_Daily_19May2026.md`  ·  Reviewer run: ftse_qa1
Level file check: `last_bar_date` = 2026-05-18 < D (2026-05-19). Leak-free; used as-is.
Basis used for Category 3: the report states it is a **cash index** report, so the `_cash` fields (10:00–18:30 broker = 08:00–16:30 London) are the primary comparison; `_full` shown where it changes the verdict.

## Score line
```
c1=2
c2=4
c3=0
c4=2
c5=3
total=43
band=Low
override=hallucinated_source
card_integrity=86.7
n_cards=3
n_duds=1
n_warns=0
```
`restriction_breach` ALSO applies (module codes in the report body; see 5.4). Only one value may be recorded on the `override=` line; `hallucinated_source` is the stricter (cap 59, C3=0) and is the one recorded. Both force C1 down at least one level (applied once: raw mean 3.0 -> 2).

## 1. Section 7 checklist

### Category 1 — Prompt adherence (20)
| Row | Notes | Evidence | Score |
|---|---|---|---|
| 1.1 Variables respected | FTSE 100 cash index primary, Euro Stoxx reference only (OK). Lookback 5 sessions, GBP/points (OK). Daily-open anchor overridden 07:00 -> 08:00 UK "by analyst" (disclosed at top, §20, Trade 1 card — but it is a deviation from the configured 07:00 anchor). Counter set: USDX, S&P 500, DAX shown, but all counters stop at Fri 15 May, not the D-1 (18 May) close. Source list: 7 rows, but they are aggregators/media (Yahoo, Investing.com, Trading Economics, AJ Bell, Fidelity); no index-provider or exchange figure actually obtained (LSE/FTSE Russell shown "Pending"), no sell-side price source. | header; §2; §4; §10; §20 | 3 |
| 1.2 Coverage & currency consistent | Weekday labels in §6/§8/§13d are wrong for 2026: 12 May is a Tuesday, not "Mon"; 15 May is a Friday, but §6, §8, §13d label it "Thu 15 May" while §1/§3/§4/§7 call it Friday. The five §6 sessions are 12/13/14/15/18 May but labelled Mon/Tue/Wed/Thu/Mon. Counters in §10/§14 are as of 15 May (DXY 99.27, SPX 7,408.50, VIX 18.43) although D-1 = 18 May data exists. Calendar events misdated (see 3.1). | §6, §8, §10, §13d, §14 | 2 |
| 1.3 Audience & tone | Strategist/risk-review tone throughout; no retail language. Minor: §7 tells the reader to "run the companion engine with --produce-images YES", §20 "lenient corroboration mode … by analyst instruction" — tooling/prompt leakage, not tone. | §1, §18 | 4 |
Raw mean = 3.0 -> level 3. Override (restriction breach and hallucinated source both apply): C1 reduced one level -> **c1 = 2**.

### Category 2 — Structural alignment (20)
| Row | Notes | Evidence | Score |
|---|---|---|---|
| 2.1 Sections present & ordered | §1–§21 all present in order; §21a/b/c/d present, §21d carries the limitations boilerplate. §13 sub-structure differs from the brief: §13c is a "Divergence flag" and the two calendars (previous, upcoming) are both under §13d — brief expects §13c previous / §13d upcoming. §17 is one sentence. | headings | 4 |
| 2.2 Scorecard as a table | §6.1 is a full table with Date/O/H/L/C/RSI2/Trend/Source A/Source B/Validation. §11 daily/weekly/monthly pivot tables ordered R3 -> S3, three levels each side (daily adds R1.5/S1.5). | §6, §11 | 5 |
| 2.3 Method steps visible | §4–§5 show observations -> consensus; §8 is candle-by-candle with a sequence assessment; §9 gives overlap 0.51, persistence 0.46, range position, VOLator slope. Missing: ATR(14) value is never stated anywhere; KER(13, EMA3) value/derivation never shown (only "-0.4" in §20, and §1 says "Kaufman … Trending Down — Moderate" while §9 says Transitional/Ranging). §7 charts are text placeholders ("not rendered") — accepted as caption per brief, noted. | §7–§9 | 3 |
Mean 4.0 -> **c2 = 4**.

### Category 3 — Accuracy & evidence (25)
| Row | Notes | Evidence | Score |
|---|---|---|---|
| 3.1 Quantitative claims sourced | §1/§12/§14 numbers mostly point to §4/§13, but several are wrong vs the calendar slice: US CPI April placed on "Wed 14 May, 3.1% est / 3.4% actual" — slice calendar has US CPI on Tue 12 May, y/y 3.8 actual vs 3.7 consensus (prior 3.3). US PPI placed on "Thu 15 May"; slice has it on Wed 13 May (PPI m/m 1.4 vs 0.4 cons). "UK Average Earnings Tue 13 May, 5.4% est" is not in the slice calendar; UK Average Earnings are scheduled for D itself (19 May 07:00 UK, regular pay cons 5.0, total pay 5.2). UK GDP (HIGH, Thu 14 May 07:00 UK) and US Retail Sales (HIGH, 14 May) are absent from the previous-period table. Eurozone CPI "3.0% flash" vs slice 2.9% y/y. VIX "18.43, +6.78% Friday" vs slice daily closes 14 May 18.98, 15 May 19.06 (+0.4%), 18 May 18.67. S&P "Fri -1.24% to 7,408.50" vs slice 15 May close 7,400.8 (-1.38%); 7,408.5 is the 18 May 23:30 bar. DXY "rising 99.27 -> 99.35" omits that D-1 closed 98.985 (-0.32% on the day, 99.303 on 15 May). | §1, §10, §12–§14 | 2 |
| 3.2 Citations exist & contain data | Three spot checks: (a) Yahoo Finance UK 18 May 15:26 BST: raw quote 10,331.45, "normalised" 10,323.75, no reconciliation; the same table then uses a 15:26 snapshot (LSE still open to 16:30) as the "close" — self-contradictory. (b) LSE/FTSE Russell official, 15 May EOD, status "Pending T+1" while the run is dated 18 May late session and §6 treats 15 May as CORROBORATED — impossible/inconsistent. (c) Fidelity/Sharecast 15 May 14:52 "10,186.43 Friday low-print" while §6 gives the Friday low as 10,151.45 (lower) — figure contradicts the report's own table. In addition §6 marks 12/13/14 May "CORROBORATED (Δ ≈ 0.04–0.10 pts)" by Yahoo x Investing.com, but those OHLC are 100–195 pts away from the slice (12 May) and the Opens equal the prior Close almost to the cent (13 May open 10,374.36 = 12 May close; 15 May open 10,372.90 = 14 May close; 18 May low 10,151.45 = identical to 15 May low) — the stated two-source agreement is not credible. Treated as fabricated per brief §2 row 3.2. | §4, §6, §19 | 0 |
| 3.3 Calculations transparent | RSI2 arithmetic reproduces from the report's own closes (`--closes`: 49.0, 16.1, 42.0 match §6; first two rows n/a — the 12 May seed 10,302 is "inferred from -0.37%", i.e. a synthesised price, disclosed). But narrative RSI2 contradicts the table: §6 text "Monday … back into mid-50s", §8 "recovers to ~58" vs table 42.0; §6 text "single-digits" and §8 "~6" for Friday vs table 16.1; §8 "Mon 12 May RSI2 ~80" vs "—". Pivot formulas reproduce from the report's own H/L/C. ATR(14) never stated; implied by the Trade 1 card (0.25×ATR = 22.5; 3×ATR = 270) as 90 pts, vs 147.4 (cash) / 161.4 (full) in the level file. KER not shown. §21a score arithmetic: Σ = -0.3725 reproduces from §20, but §1/§21b say -0.43, and the sentiment input is -0.55 (the Euro Stoxx estimate) rather than the FTSE tilt -0.81 computed in §13b. | §6, §8, §9, §20, §21a | 2 |
| 3.4 Numbers reconcile | D-1 close 10,323.75 is consistent across §1/§3/§4/§6/§21b (but see data check below). Breaks: direction score -0.372 (§21a/§20) vs -0.430 (§1, §21b Trade 1); "weekly P" quoted as 10,420 (§1) vs 10,256.31 (§11.2); "weekly R1" 10,361.16 (§11, §8) vs "weekly R1 (10,420)" (§12, §13d, §15, §16); "daily R1 = 10,449 / S1 = 10,269" (§7, §15) vs §11 daily R1 10,386.32 / S1 10,206.32 (10,449 is R2, 10,269 is P); §11.4 "weekly R1 sits ~38 points above" daily R1 — it is 25 below; Friday candle "body ~98% of the 221-pt range, negligible lower wick" vs own numbers 177.5/221.75 = 80% with 43.9 lower wick; Monday "lower wick ~170 pts" vs own numbers 43.3; open-zero net "−221+129 = −92" vs Friday body −177.5; §21d "Trade 2 triggered 2/5" vs §21c table YES on 12, 14, 15 May (3/5); Trade 2 card text says 3C "confirmed" downside break while the 3C card says NOT-YET-ELIGIBLE and cites a nonexistent "§4d". | cross-section | 1 |
Raw row mean (2+0+2+1)/4 = 1.25 -> 1. **Override: fabricated/self-contradictory sources -> C3 = 0.**

**Data check vs level file / slice (D-1 = 2026-05-18, cash basis; tolerance close ±5, O/H/L ±10).** Δ = report − slice cash [full in brackets].
| Date (report label) | Field | Report | Slice cash | Δ cash | Slice full | Δ full | Verdict |
|---|---|---|---|---|---|---|---|
| 18 May (D-1) | O | 10,194.75 | 10,144.5 | +50.25 | 10,170.8 | +23.95 | FAIL |
| | H | 10,331.45 | 10,336.3 | -4.85 | 10,347.7 | -16.25 | ok (cash) |
| | L | 10,151.45 | 10,141.2 | +10.25 | 10,107.0 | +44.45 | marginal / fail (full) |
| | C | 10,323.75 | 10,290.8 | **+32.95** | 10,347.6 | -23.85 | **FAIL >15 on both bases** |
| 15 May ("Thu") | O | 10,372.90 | 10,299.0 | +73.9 | 10,352.9 | +20.0 | FAIL |
| | H | 10,373.20 | 10,309.4 | +63.8 | 10,362.3 | +10.9 | FAIL |
| | L | 10,151.45 | 10,154.9 | -3.45 | 10,152.3 | -0.85 | ok |
| | C | 10,195.37 | 10,167.0 | +28.37 | 10,187.0 | +8.37 | FAIL (>15) |
| 14 May ("Wed") | O/H/L/C | 10,338.61 / 10,378.04 / 10,324.72 / 10,372.90 | 10,319.3 / 10,371.1 / 10,301.1 / 10,355.8 | +19.3 / +6.9 / +23.6 / +17.1 | 10,349.3 / 10,397.3 / 10,298.8 / 10,352.0 | -10.7 / -19.3 / +25.9 / +20.9 | O,L,C FAIL |
| 13 May ("Tue") | O/H/L/C | 10,374.36 / 10,398.55 / 10,310.40 / 10,338.80 | 10,314.9 / 10,357.0 / 10,234.8 / 10,293.6 | +59.5 / +41.6 / +75.6 / +45.2 | 10,270.8 / 10,357.0 / 10,234.8 / 10,352.4 | +103.6 / +41.6 / +75.6 / -13.6 | FAIL |
| 12 May ("Mon") | O/H/L/C | 10,380.65 / 10,422.10 / 10,341.20 / 10,374.36 | 10,190.5 / 10,250.3 / 10,145.9 / 10,250.1 | +190.2 / +171.8 / +195.3 / +124.3 | 10,233.5 / 10,291.6 / 10,145.9 / 10,277.0 | +147.2 / +130.5 / +195.3 / +97.4 | FAIL (all fields) |
RSI2 (D-1): report 42.0 (reproduces from its own closes) vs slice 39.60 cash / 49.32 full — within 3 pts of cash, acceptable. ATR14: not stated; implied 90 vs 147.4 cash / 161.4 full (understated ~39–44%).

Daily pivots (report §11.1, own H/L/C: P=(10,331.45+10,151.45+10,323.75)/3 reproduces) vs level file cash [full]: P 10,268.88 vs 10,256.1 (+12.8) [10,267.43, +1.5]; R1 10,386.32 vs 10,371.0 (+15.3) [10,427.87, -41.6]; S1 10,206.32 vs 10,175.9 (+30.4) [10,187.17, +19.2]; R2 10,448.88 vs 10,451.2 (-2.3) [10,508.13]; S2 10,088.88 vs 10,061.0 (+27.9) [10,026.73]; R3 10,566.32 vs 10,566.1 (+0.2) [10,668.57]; S3 10,026.32 vs 9,980.8 (+45.5) [9,946.47].
Weekly pivots (report §11.2) vs cash week 2026-W20 (11–15 May) [full]: P 10,256.31 vs 10,228.0 (+28.3) [10,243.4]; R1 10,361.16 vs 10,310.1 (+51.1); S1 10,090.51 vs 10,084.9 (+5.6); R2 10,526.96 vs 10,453.2 (+73.8); S2 9,985.66 vs 10,002.8 (-17.1); R3 10,631.81 vs 10,535.3 (+96.5); S3 9,819.86 vs 9,859.7 (-39.8). Report weekly P reproduces from its own (wrong) 12 May high 10,422.10 and omits 11 May.
Monthly pivots (report §11.3, "April 2026", labelled CORROBORATED) vs level file cash [full]: P 10,547.88 vs 10,418.8 (**+129.1**) [10,421.17]; R1 10,695.77 vs 10,650.0 (+45.8); S1 10,412.12 vs 10,140.1 (+272.0); R2 10,831.53 vs 10,928.7 (-97.2); S2 10,264.23 vs 9,908.9 (+355.3); R3 10,979.42 vs 11,159.9 (-180.5); S3 10,128.47 vs 9,630.2 (+498.3). The report's monthly set implies an April range of ~284 pts (H 10,683.64 / L 10,399.99); the level file implies ~510 pts (H 10,697.5 / L 10,187.6). Monthly P 10,547.88 is used as Trade 1 thesis invalidation and across §1/§13/§15/§16.
Swings: report 5-day swing high 10,422.10 vs 10,371.1 cash (+51.0) [10,397.3 full, +24.8]; 5-day swing low 10,151.45 vs 10,141.2 (+10.3) [10,107.0, +44.5]; 25-day high 10,683 vs 10,666.5 (+16.5) [10,698.0]; 25-day low 10,151 vs 10,141.2 (+9.8) [10,107.0].
Counters: see 3.1.

### Category 4 — Reasoning & judgment (20)
| Row | Notes | Evidence | Score |
|---|---|---|---|
| 4.1 Pillars conclude | §8 Transitional-bearish, §9 Transitional/Ranging with downward drift, §10 per-counter confirm labels + aggregate MIXED, §12 each paragraph labelled Negative/Mixed-Supportive, §14 ends "risk-off, USD-supportive, equity-negative". All pillars end in a label, but §1 says Kaufman "Trending Down — Moderate" against §9 "Transitional / Ranging" and no KER figure supports either. | §1, §8–§14 | 3 |
| 4.2 Cross-asset interpreted | Mechanisms given (USD translation, risk transmission, DAX as continental floor, energy weight ~12%). But the dollar mechanism is internally muddled (USD strength described as removing a GBP-weakness tailwind), the VIX is not interpreted in §10, and the inputs are stale: D-1 saw USDX -0.32% and S&P +0.06% per slice, so "Confirms (bearish)" on both counters rests on the 15 May reading. | §10 | 3 |
| 4.3 Synthesis reconciles tensions | §16 forecasts range-with-downside-bias and §18 prefers "hedged exposure over directional commitment", yet §21a/b issue a SHORT with a downside-breakout Trade 2 described as "confirmed", while Trade 3C is "not yet eligible". §21a asserts "no conflict with §17" although §17 gives two different ranges (10,150–10,420 and between weekly P 10,256 and daily R1 10,449, which is R2). Direction score -0.372 vs -0.430 not reconciled; sentiment input uses the Euro Stoxx figure. | §16–§18, §20, §21 | 2 |
| 4.4 Calibrated language | §17 is one sentence; confidence Medium stated in §3/§18. The sentence stacks two overlapping ranges and a bias clause. Confidence "High (more than three articles)" in §13b is an article-count rule, with only 5 articles. | §3, §13b, §17 | 3 |
| Direction-score derivation traceable | Weights 0.25/0.20/0.10/0.15/0.15/0.15 correct and Σ = -0.3725 reproduces; but §21b/§1 quote -0.430; sentiment input -0.55 not -0.81; cross-asset -0.5 although §10 says "sign × 0.3"; KER -0.4 with no KER shown. | §20, §21a | 2 |
| Card construction (protocol) | Trade 1: ATR understated (90 vs 147.4), swing high wrong (10,422.10 vs 10,371.1), confluence claims false, wide-stop flag omitted by its own ATR. Trade 2: TP1 labelled 1R is 0.91R; TP2 = 1.62R. Trade 3C: entry unpriced (DUD), Unit-3 stop rule wrong for a short. Details in feedback. | §21b | 1 |
Mean (3+3+2+3+2+1)/6 = 2.33 -> **c4 = 2**.

### Category 5 — Currency, restrictions & transparency (15)
| Row | Notes | Evidence | Score |
|---|---|---|---|
| 5.1 Data dated; staleness flagged | Prices and articles carry dates; the 18 May single-source status is flagged consistently. But the weekday errors (1.2), counters not rolled to D-1, and a 15:26 BST snapshot presented as "close" weaken dating. §19 flags 18 May only; 12–14 May are labelled CORROBORATED despite the slice gap. | §4, §6, §19 | 3 |
| 5.2 Assumptions up front | Anchor-override caveat is stated at the top, in §20 and on the Trade 1 card; single-source propagation to Trade 2/3C stated; lenient-corroboration mode disclosed. | header, §19, §20, §21b | 4 |
| 5.3 Red flags surfaced | CPI collision on 20 May carried into all three cards. Not surfaced: D's own UK labour-market release (Average Earnings, Claimant Count, Unemployment — scheduled 07:00 UK on 19 May, i.e. before the 08:00 entry) is absent from §13d and from every card caveat; the §13d "Upcoming" table starts on 20 May. Trade 1 caveat says the stop anchor is "fully corroborated" when the swing high is 51 pts off the slice. | §12, §13d, §21b | 3 |
| 5.4 Restrictions honoured | Module codes appear in the report body: "M3 §11 regime_label" (§9), "M3 §11 cross_asset_confirm" and "M5 weighs" (§10), "M3 technical regime", "M2 aggregate sentiment" (§16), "M5 §2" (§20), "per the M5 …" style references; internal variable names in code style (`regime_label`, `cross_asset_confirm`, `swing_high_25d`); tooling flag "--produce-images YES" (§7); reference to a nonexistent "§4d" (§21b). A synthesised price (11 May seed 10,302, "inferred") feeds RSI2, and opens equal to prior closes suggest interpolation presented as sourced. No retail CFD quotes in the OHLC basis (stated excluded). | §7, §9, §10, §16, §20 | 1 |
Mean 2.75 -> **c5 = 3**.

## 2. Category roll-up
| Cat | Level | Multiplier | Max | Points | Justification |
|---|---|---|---|---|---|
| C1 Prompt adherence | 2 | 0.40 | 20 | 8.00 | Raw 3.0 reduced one level by overrides; anchor shifted to 08:00, counters stale, weekday labels wrong |
| C2 Structure | 4 | 0.85 | 20 | 17.00 | All 21 sections present and ordered; ATR/KER absent, charts are placeholders, §13 sub-numbering differs |
| C3 Accuracy & evidence | 0 | 0.00 | 25 | 0.00 | Override: self-contradictory/impossible citations; 12–18 May OHLC up to 195 pts off the slice, monthly pivots 129–498 pts off |
| C4 Reasoning & judgment | 2 | 0.40 | 20 | 8.00 | Direction score and sentiment input unreconciled; one DUD card and mis-specified numbers on the other two |
| C5 Currency & transparency | 3 | 0.65 | 15 | 9.75 | Assumptions disclosed well; module codes, inferred price and missed D-day UK data release |
| **Total** | | | 100 | **42.75 -> 43** | |

## 3. Total, band, override
total=43 · band=**Low** (40–59) · override check: hallucinated_source TRIGGERED (cap 59 not binding at 43; C3 set to 0); restriction_breach ALSO triggered (cap 74 not binding; C1 reduced). Without the C3 override the raw C3 level would have been 1 (20% x 25 = 5 pts), total 48 — still Low.

## 4. Card Integrity (linter rows copied verbatim from `qa/ftse_qa1/lint_static/2026-05-19.csv`)
| card_id | report_date | strategy | flags | dud | per-card score |
|---|---|---|---|---|---|
| 2026-05-19_Trade_1 | 2026-05-19 | Trade 1 — Daily Directional (SHORT) | CLEAN | False | 100 |
| 2026-05-19_Trade_2 | 2026-05-19 | Trade 2 — Pivot (TRANSITION regime — breakout-side only) | CLEAN | False | 100 |
| 2026-05-19_Trade_3C | 2026-05-19 | Trade 3 — Regime-driven Complex (3C — Momentum-Breakout, TRANSITION regime) | UNPRICED | True | 60 |

```
card_integrity=86.7
n_cards=3
n_duds=1
n_warns=0
```
Report-level = mean(100, 100, 60) = 86.67. No suppressed cards. Separate from the 100.

## 5. Feedback
See `qa/ftse_qa1/2026-05-19_feedback.md`.
