# Trust Score — 2026-05-19 — SP500_Daily_Report_19May2026.md

Run: regen_20260906_qa1 · Asset: US500 · D-1 slice: `data/slices/US500/US500_upto_2026-05-18.csv` · Linter: `qa/regen_20260906_qa1/lint_static/2026-05-19.csv`

Report anchors noted (step 1): D-1 (18 May) OHLC 7,415.07 / 7,434.06 / 7,371.75 / 7,403.05; RSI2 column 100.0 / 100.0 / 100.0 / 8.3 / 7.5; ATR(14) ≈ 68; daily pivots P 7,402.95 · R1 7,434.16 · S1 7,371.85 · R2 7,465.26 · S2 7,340.64 · R3 7,496.47 · S3 7,309.54; weekly P 7,434.67 (R1 7,490.95 / S1 7,352.23); monthly P 7,117.00 (R2 7,430.80); direction score +0.158 (§20) / +0.16 (§21a); regime: short-term Transitional Bearish, medium-term Trending Up — Moderate (KER +0.17); cards: T1 LONG market 7,403.05 / SL 7,335 / TP 7,434–7,490–7,573; T2 LONG limit 7,371.85 / SL 7,348 / TP 7,403–7,434–7,490; T3A LONG layered limits 7,444.43 & 7,427.32 (blended 7,435.50) / SL 7,360 / TP 7,490–7,517–7,573. No card suppressed.

Slice anchors (helper, cash session 16:30–23:00 broker): D-1 O/H/L/C 7,423.0 / 7,438.5 / 7,358.0 / 7,411.0 (full-day close 7,405.2); RSI2 on cash closes 65.86 / 80.81 / 100.00 / 38.22 / 0.00; ATR14 73.69 (cash) / 81.34 (full-day); daily pivots P 7,402.50 · R1 7,447.00 · S1 7,366.50 · R2 7,483.00 · S2 7,322.00 · R3 7,527.50 · S3 7,286.00; weekly P 7,428.07 · R1 7,510.83 · S1 7,333.23; 5-d swing 7,522.9 (14 May) / 7,345.3 (12 May). RSI2 recomputed from the report's own closes: n/a, n/a, 100.0, 6.1, 0.0.

## 1. Section 7 checklist

| Item | Reviewer notes | Evidence observed | Score 0–5 | Action required |
|---|---|---|---|---|
| 1.1 Variables respected | Asset = S&P 500 cash index; counters USDX·VIX·DAX 40 in order; as-of NY tz; 5-session lookback; USD / index points / 0.01 tick; six sources in §4. Deviations: Trade 1 anchor 00:00 UK instead of the instance's 07:00 UK (disclosed as a "runtime user instruction", not in the fixed variables); Trade 1 card quotes an ES-futures entry price (7,425.25) and ES tick/$ sizing although ES is confirmation-only; Trade 1 presented despite score < 0.25. | §2 table; §4 six rows; §20 anomaly 1; §21b Trade 1 "Entry trigger"/"Stop loss" rows | 3 | Restore 07:00 UK anchor (or document the override in the variables block); strip ES price/sizing from the cash-index card; apply the suppression rule. |
| 1.2 Coverage & currency consistent | All data dates ≤ 18 May; session = 19 May. Unit drift: the "Native unit" column reports −6,805 / +3,095 / +8,695 / +16,995 "points" for 68.05 / 30.95 / 86.95 / 169.95-point distances (×100, ticks presented as points) on all three cards; ES $/tick mixed into a cash-index card. | §21b all three cards, third column | 3 | Fix native-unit column (points, two decimals); remove ES dollar sizing. |
| 1.3 Audience & tone | Senior-strategist register throughout; trading/risk-review framing; no retail tone. Minor over-claim "Trade 2 is the clear winner" on one closed trade (limitations boilerplate does follow). | §1, §18, §21d | 4 | None material. |
| 2.1 Sections present & ordered | §1–§21 all present in order; §13a–d and §21a–d present; §17 is one sentence; limitations boilerplate verbatim. | Headings | 5 | None. |
| 2.2 Scorecard as a table | §6 has Date/O/H/L/C/RSI2/Trend/Source A/Source B/Final/Validation; §11 daily, weekly, monthly tables each R3→P→S3 with distance column. | §6, §11 | 5 | None. |
| 2.3 Method steps visible | §4 observations → §5 weighted-median consensus; §8 candle-by-candle + sequence; §9 regime with persistence, VOLator z-score/slope, KER; §7 five chart placeholders (pandoc image refs — accepted per brief, noted). | §4–§9 | 5 | None (charts are placeholders only). |
| 3.1 Quantitative claims sourced | Price figures point to §4/§6; §12 blocks name sources (Oppenheimer/ycharts, TradingEconomics, Barchart). Unsourced: §9 "19 of 25 sessions closed above open" (slice: 16 of 25), "closes from ≈7,081" (slice first cash close of the 25-session block 6,970.5), "DXY +1.24% over 4 weeks", §13d "YTD +8.70%", §14 "70th–80th percentile" positioning attributed to unnamed "sell-side desks", DAX level sourced only generically in §19. | §9 para 1, §12 Macro/FX, §13d, §14 Positioning | 3 | Source or drop the unsourced figures; correct the 25-session statistics. |
| 3.2 Citations exist & contain data | Spot-check 1: CNBC 18 May 16:00 ET 7,403.05 with H 7,434.06 / L 7,371.75 / O 7,415.07 — used identically in §6, §8, §11 and the cards: consistent. Spot-check 2: FRED 15 May 7,408.50 — used identically in §6/§8/§21c; Yahoo's −92.74 = 7,501.24 − 7,408.50 and §13c's "1.24% selloff" both reproduce: consistent. Spot-check 3: §13c Empire State 19.6 (15 May) — matches the calendar slice. No self-contradictory or impossible citation found. However the Investing.com-attributed 12–13 May rows carry figures that contradict both the slice and the prior report (see 3.4). | §4, §13a, §13c | 3 | Re-source the 12–13 May OHLC rows. |
| 3.3 Calculations transparent | Daily/weekly/monthly pivots reproduce exactly from the report's own H/L/C. ATR, KER, VOLator stated. Sentiment tilt 0.8/4.2 = 0.19 reproduces. Direction-score components sum to +0.1535, not the stated +0.158 (minor). RSI2 derivation not shown and does NOT reproduce from the report's own closes: 15 May 8.3 vs 6.1; 18 May 7.5 vs 0.0 (two consecutive down closes give RSI2 = 0 under the stated mean-gain/mean-loss convention). | §6 note, §11, §20 strategy trace, helper output | 2 | Rebuild RSI2 from the validated closes and show RS; correct the score sum. |
| 3.4 Numbers reconcile | Internally: D-1 close 7,403.05 identical in §1/§3/§4/§6/§21b; §11 pivots = card levels; ATR 68 in §9 and §21; RSI2 7.5 in §6/§8/§21a. Externally: 12 May close 7,488.62 vs slice 7,409.8 (Δ +78.8; prior report gave 7,400.96) and 13 May close 7,495.18 vs 7,451.5 (Δ +43.7; prior report 7,444.25) — both > 10 pts = Category 3 failures; D-1 close Δ −7.95, D-1 low Δ +13.75; monthly pivots rest on an April low of 6,920.4 vs slice 6,471.7, so the "monthly R2 / daily R1 confluence" in §11/§18/§21b does not exist on the slice basis; §11 note says S1 is "10 points above the Mon low" (actual 0.10); §8 calls 18 May an "inside-day" that "held the prior session's low" while stating it traded 21 pts below Friday's low; §13c dates CPI 14 May (calendar slice: 12 May). | §6, §8, §11, §13c; §5 Data reconciliation log | 1 | Replace the 12–13 May rows with corroborated values; re-derive monthly pivots from verified April H/L/C; fix §8/§11/§13c statements. |
| 4.1 Pillars conclude | §9 → Trending Bullish; §10 → MIXED leaning bearish; §12 each block labelled; §8 ends in a "mean-reversion setup" read with no explicit short-term label (label appears only in §1); §14 ends on "rate channel dominant headwind" without an aggregate label. Card construction (scored here per protocol): T1 TP1/TP2 at +0.45R/+1.28R instead of ±1R/±2R and stop anchored to S2 rather than the tighter-of(swing, S/R)+0.25×ATR rule; T2 uses a RANGE-style S1 limit under a TREND_UP label (rule: P + 0.10×(R1−P), stop P − 0.8×(P−S1), TPs R1/R1.5/R2), stop has no 0.25×ATR buffer, R = 0.29×ATR (linter WARN); T3A anchors its fib on the high→low leg for a LONG (rule: swing low → swing high), layers 50%/61.8% instead of the single 57.5% entry, TPs at weekly R1/ATH instead of 38.2%/0%, and its buy limits (7,444.43 / 7,427.32, blended 7,435.50) sit ABOVE the D-1 close 7,403.05 (slice 7,411.0). | §8–§14; §21b; brief §3 | 3 | Rebuild the three cards to the M5 templates (see feedback). |
| 4.2 Peer/cross-asset interpreted | Mechanisms given: USD → multinational EPS translation; VIX inverse / vol-of-vol normalising; DAX as common global-risk factor. USDX "Rising" read rests on 15 May data only (no 18 May print; slice 18 May close 98.985, −0.32). | §10 table and aggregate note | 4 | Add the 18 May USDX print. |
| 4.3 Synthesis reconciles tensions | §16 explicitly treats short-term bearish vs medium-term trend as a within-trend pullback; §21a addresses §17 conflict; §15 balanced. Not reconciled: a "Medium-High" conviction T3A pullback-buy whose limits sit above the market; a LONG Trade 1 issued on a +0.16 score the report itself calls sub-threshold; §18 "monthly-R2/daily-R1 confluence" as Reason 2 rests on unverified April inputs. | §15–§18, §21a–b | 3 | Reconcile card conviction with the score and the construction. |
| 4.4 Calibrated language | §17 is one sentence with a stated base case; confidence stated in §3/§18. Over-confidence: T3A "Medium-High" conviction; §21d "clear winner" on one closed trade; §16 "likely" bounce stated without probability language elsewhere. | §17, §18, §21b/d | 3 | Tone down card conviction labels to match the score. |
| 5.1 Data dated; staleness flagged | All prices and articles dated; single-source rows flagged in §6/§19. Staleness not flagged: USDX and DAX carried at 15 May values into an 18 May-basis report; §14 positioning undated; 12–13 May opens equal the prior close exactly (interpolation signature) yet are presented as sourced values. | §4, §6, §10, §14, §19 | 3 | Add 18 May USDX/DAX prints or flag as stale; date positioning data. |
| 5.2 Assumptions up front | Anchor override stated on the T1 card and in §20 anomaly 1; single-source flag propagated to T2 caveats and via §19 reference on T1; T3A caveat states the fib lookback. Suppression override and lenient-corroboration assumptions disclosed in §20 (though attributed to unverifiable runtime instructions). | §20, §21b caveats | 4 | Move the override disclosures to §2/§19 as explicit assumptions. |
| 5.3 Red flags surfaced | §12/§15 carry oil, rates, USD, Nvidia risks; §13d flags Nvidia as highest impact; carried into T1 caveat only — T2 and T3A caveats omit the Wed FOMC minutes / Thu Nvidia collision. | §12, §13d, §15, §21b | 3 | Add the event-collision caveat to T2 and T3A. |
| 5.4 Restrictions honoured | Breaches: (a) module code in the report text — §6 note "(M3 convention; fixed)"; (b) ES futures used beyond confirmation — an ES entry price and ES tick/$ risk on the Trade 1 card; (c) Trade 1 issued with |score| = 0.16 < 0.25 contrary to the fixed suppression rule; (d) 12–13 May OHLC presented as sourced although the values contradict the slice and prior report and show an interpolation signature (open = prior close). Also §20 leaks prompt-internal state ("Weights basis: DEFAULT (locked, session 1 of 20)"). | §6 note, §21b Trade 1, §20 | 1 | Remove module codes/prompt state; ES confirmation-only; apply suppression; re-source or drop 12–13 May rows. |

## 2. Category roll-up

| Category | Level | Multiplier | Points | Justification |
|---|---|---|---|---|
| C1 Prompt adherence (20) | 2 | 0.40 | 8.00 | Rows 1.1–1.3 mean 3.33 → 3; restriction-breach override drops one level to 2. Variables mostly respected but anchor, ES-confirmation-only, suppression rule and unit discipline all deviate. |
| C2 Structure (20) | 5 | 1.00 | 20.00 | Rows 2.1–2.3 mean 5.0. All 21 sections, sub-sections and tables present and ordered. |
| C3 Accuracy & evidence (25) | 2 | 0.40 | 10.00 | Rows 3.1–3.4 mean 2.25 → 2. Two §6 closes wrong by 44–79 pts, RSI2 not reproducible from own closes, monthly pivot inputs unverified; sources internally consistent, none fabricated. |
| C4 Reasoning & judgment (20) | 3 | 0.65 | 13.00 | Rows 4.1–4.4 mean 3.25 → 3. Mechanisms and synthesis present; all three cards depart from the M5 construction rules, T3A limits sit above the market. |
| C5 Currency & transparency (15) | 3 | 0.65 | 9.75 | Rows 5.1–5.4 mean 2.75 → 3. Overrides disclosed, but restrictions breached (module code, ES use, suppression) and stale cross-asset prints unflagged. |
| **Total** | | | **60.75 → 61** | |

## 3. Total, band, override check

- Total: **61/100** (8.00 + 20.00 + 10.00 + 13.00 + 9.75 = 60.75, rounded to 61).
- Band: **Moderate** (60–74).
- Overrides: **restriction_breach** — the report prints a module code in the body (§6 note "M3 convention; fixed"), uses ES futures beyond confirmation-only (entry price and $-sizing on the Trade 1 card) and issues Trade 1 against the fixed |score| < 0.25 suppression rule. Cap at 74 is not binding; C1 reduced from 3 to 2 as required. No fabricated source detected on the three spot-checks (CNBC 18 May, FRED 15 May, Empire State 19.6 all internally consistent / matching the slice), so the hallucinated-source override is not triggered; the incorrect 12–13 May figures are scored as factual errors under C3.

## 4. Card Integrity

Linter rows (verbatim from `qa/regen_20260906_qa1/lint_static/2026-05-19.csv`):

| card_id | report_date | strategy | flags | dud |
|---|---|---|---|---|
| 2026-05-19_Trade_1 | 2026-05-19 | Trade 1 - Daily Directional (mean-reversion) | CLEAN | False |
| 2026-05-19_Trade_2 | 2026-05-19 | Trade 2 - Pivot (buy limit daily S1) | WARN_R_TINY(0.29xATR) | False |
| 2026-05-19_Trade_3A | 2026-05-19 | Trade 3A - Momentum-Pullback (layered fib limits) | CLEAN | False |

| Card | #DUD | #WARN | Integrity = 100 − 40·DUD − 10·WARN |
|---|---|---|---|
| 2026-05-19_Trade_1 | 0 | 0 | 100 |
| 2026-05-19_Trade_2 | 0 | 1 | 90 |
| 2026-05-19_Trade_3A | 0 | 0 | 100 |
| **Report mean (3 non-suppressed cards)** | 0 | 1 | **96.7** |

M5 rule assessment (feeds row 4.1, not the integrity number):
- Trade 1 — entry MARKET = report D-1 close (ok vs its own §6); anchor 00:00 UK (deviation from 07:00 UK); stop 7,335 derived from "below daily S2" rather than tighter-of(5-d swing low 7,371.75, S1 7,371.85) + 0.25×ATR (= 7,354.85 on the report's numbers); R = 68.05 = 1.0×ATR(68) → no wide-stop flag raised although R > 1×ATR by 0.05; TP1/TP2 at +0.45R/+1.28R instead of ±1R/±2R; TP3 within the 3×ATR runner cap; invalidation stated but equals the stop level (not separate); Nvidia caveat present; issued despite |score| < 0.25.
- Trade 2 — labelled TREND_UP but built as a RANGE fade at S1; under TREND the entry is P + 0.10×(R1−P), stop P − 0.8×(P−S1), TPs R1/R1.5/R2; the stated stop (4 pts under weekly S1) carries no 0.25×ATR buffer; R = 23.85 = 0.29×ATR (linter WARN); TPs at P/R1/weekly R1 are not ±1R/±2R either; invalidation = stop (not separate); single-source flag propagated; event caveat missing.
- Trade 3A — fib anchored on the 14-May high → 18-May low (the pullback, not the impulse) for a LONG; entries layered at 50%/61.8% (blended 7,435.50, arithmetic midpoint 7,435.88) rather than the single 57.5% level; both limits sit above the D-1 close (7,403.05 report / 7,411.0 slice), i.e. a resting buy limit on the wrong side; stop 7,360 is 11.75 pts (0.17×ATR) beyond the 0% anchor instead of 0.25×ATR; TPs at weekly R1 / ATH / weekly R2 instead of 38.2% / 0% / 100%+; invalidation = stop; swing endpoints logged; event caveat missing.

## 5. Data reconciliation log

Tolerances (brief §4): close |Δ| ≤ 3 pts and open/high/low |Δ| ≤ 8 pts = consistent; larger = discrepancy; close > 10 pts or RSI2 not reproducing from own closes = Category 3 failure.

| Section | Field | Report value | Slice value (cash session) | Delta | Verdict |
|---|---|---|---|---|---|
| §6 | 12 May Open | 7,472.10 | 7,396.3 | +75.8 | Discrepancy |
| §6 | 12 May High | 7,491.40 | 7,415.5 | +75.9 | Discrepancy |
| §6 | 12 May Low | 7,455.85 | 7,345.3 | +110.55 | Discrepancy |
| §6 | 12 May Close | 7,488.62 | 7,409.8 | +78.82 | **Failure** (>10); prior report (18 May) stated 7,400.96 |
| §6 | 13 May Open | 7,488.62 | 7,412.0 | +76.62 | Discrepancy (= prior report close exactly; interpolation signature) |
| §6 | 13 May High | 7,508.30 | 7,466.0 | +42.30 | Discrepancy |
| §6 | 13 May Low | 7,470.05 | 7,381.5 | +88.55 | Discrepancy |
| §6 | 13 May Close | 7,495.18 | 7,451.5 | +43.68 | **Failure** (>10); prior report stated 7,444.25 |
| §6 | 14 May Open | 7,495.18 | 7,463.9 | +31.28 | Discrepancy |
| §6 | 14 May High | 7,517.12 | 7,522.9 | −5.78 | Consistent |
| §6 | 14 May Low | 7,488.40 | 7,462.9 | +25.50 | Discrepancy |
| §6 | 14 May Close | 7,501.24 | 7,509.1 | −7.86 | Discrepancy (>3, <10) |
| §6 | 15 May Open | 7,497.50 | 7,442.3 (full-day 7,505.5) | +55.20 | Discrepancy on cash basis (matches full-day/overnight basis within 8) |
| §6 | 15 May High | 7,506.80 | 7,458.0 (full-day 7,510.5) | +48.80 | Discrepancy on cash basis |
| §6 | 15 May Low | 7,392.65 | 7,402.8 (full-day 7,391.9) | −10.15 | Discrepancy on cash basis |
| §6 | 15 May Close | 7,408.50 | 7,416.0 | −7.50 | Discrepancy (>3, <10) |
| §6 / §4 / §19 | 18 May (D-1) Open | 7,415.07 | 7,423.0 | −7.93 | Consistent |
| §6 / §4 / §19 | 18 May (D-1) High | 7,434.06 | 7,438.5 | −4.44 | Consistent |
| §6 / §4 / §19 | 18 May (D-1) Low | 7,371.75 | 7,358.0 | +13.75 | Discrepancy |
| §1/§3/§4/§6/§21b | 18 May (D-1) Close | 7,403.05 | 7,411.0 (full-day 7,405.2) | −7.95 | Discrepancy (>3, <10) |
| §6 | RSI2 12 / 13 / 14 / 15 / 18 May vs slice closes | 100.0 / 100.0 / 100.0 / 8.3 / 7.5 | 65.86 / 80.81 / 100.00 / 38.22 / 0.00 | −34.1 / −19.2 / 0 / −29.9 / +7.5 | Discrepancy (basis + wrong closes) |
| §6 | RSI2 recomputed from the report's own closes | 14 May 100.0 · 15 May 8.3 · 18 May 7.5 | 100.0 · 6.1 · 0.0 | 0 / +2.2 / +7.5 | **Failure** — 15 and 18 May do not reproduce |
| §11 | Daily pivots from report H/L/C | P 7,402.95 R1 7,434.16 S1 7,371.85 R2 7,465.26 S2 7,340.64 R3 7,496.47 S3 7,309.54 | recomputed identical (≤0.01) | 0 | Reproduces |
| §11 | Daily pivots vs slice cash | P 7,402.95 / R1 7,434.16 / S1 7,371.85 / R2 7,465.26 / S2 7,340.64 | P 7,402.50 / R1 7,447.00 / S1 7,366.50 / R2 7,483.00 / S2 7,322.00 | +0.45 / −12.84 / +5.35 / −17.74 / +18.64 | Discrepancy on R1/R2/S2 (report D-1 range 62.3 vs slice 80.5) |
| §11 / §6 note | Weekly pivot inputs: prior-week low | 7,378.40 | 7,345.3 (12 May cash) | +33.10 | Discrepancy; weekly pivots reproduce from the stated inputs (P 7,434.67 vs slice 7,428.07; R1 7,490.95 vs 7,510.83; S1 7,352.23 vs 7,333.23) |
| §11 | Monthly pivot inputs (back-solved from the table: April H 7,234.2 / L 6,920.4 / C 7,196.4; internally consistent) | P 7,117.00 · R2 7,430.80 | April cash H 7,226.7 / L 6,471.7 / C 7,213.7 → P 6,970.70 · R2 7,725.70 | P +146.3 · R2 −294.9 (April low +448.7) | Discrepancy — the "monthly R2 / daily R1 confluence" cited in §11, §18, §21b is not present on the slice basis |
| §9 / §21 | ATR(14) | ≈68 | 73.69 cash / 81.34 full-day | −5.69 / −13.34 | Note (within basis tolerance; linter uses 81.34) |
| §9 | 25-session block first close / net advance / up-sessions | ≈7,081 / +4.5% / 19 of 25 | 6,970.5 (14 Apr) / +6.3% / 16 of 25 | +110 / −1.8 pp / +3 | Discrepancy (unsourced statistics) |
| §20 / §21a | Direction score | +0.158 / +0.16 | components sum to +0.1535 | +0.0045 | Minor arithmetic; conclusion (< 0.25) unchanged |
| §13b / §20 | Sentiment tilt | +0.19 (0.8/4.2) | recomputed 0.190 | 0 | Reproduces |
| §21b T3A | 61.8% / 78.6% / blended entry | 7,427.32 / 7,403.05 / 7,435.50 | 7,427.28 / 7,402.86 / 7,435.88 | +0.04 / +0.19 / −0.38 | Minor arithmetic |
| §11 note | "S1 sits 10 points above the Mon low" | 10 | 7,371.85 − 7,371.75 = 0.10 | — | Internal error |
| §8 | 18 May "inside-day … held the prior session's low" vs "below Fri's low by 21 points" (same paragraph) | — | — | — | Internal contradiction |
| §13c | US CPI date | 14 May | calendar slice: 12 May 15:30 broker (PPI 13 May correct) | — | Discrepancy; §13c 12 May row mislabelled as "earnings finale" |
| §13c | Empire State Mfg | 19.6 (15 May) | 19.6 | 0 | Consistent |
| §10 / §14 | USDX week-end / intra-week high | 99.21 / 99.35 | 15 May close 99.303 / high 99.343 | −0.09 / +0.01 | Consistent; no 18 May print given (slice 18 May close 98.985) — stale "Rising" read |
| §10 / §14 | VIX 15 May / 18 May | 18.43 (+6.78%) / 17.82 (−3.31%) | VIX CFD close 19.06 (+0.42%) / 18.67 (−2.05%) | −0.63 / −0.85 | Basis note (cash VIX vs CFD); 18 May easing direction agrees; the 15 May +6.78% jump is not reproduced on this basis |
| §4 / §13c | Yahoo −92.74; "1.24% selloff" | −92.74 / 1.24% | 7,501.24 − 7,408.50 = 92.74; 92.74/7,501.24 = 1.236% | 0 | Consistent |
