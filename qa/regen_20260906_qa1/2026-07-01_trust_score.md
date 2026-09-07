# Trust Score — 2026-07-01 — SP500_Report_01Jul2026.md

Run: regen_20260906_qa1 · Asset US500 · D = 2026-07-01 · D-1 = 2026-06-30
Evidence base: report text; `data/slices/US500/US500_upto_2026-06-30.csv` (via `engine/qa_slice_stats.py`);
VIX/USDX/NEWS slices to 2026-06-30; `qa/regen_20260906_qa1/lint_static/2026-07-01.csv`;
`cards/baseline/by_date/2026-07-01.json`; prior-dated report `reports/md/SP500_Report_30Jun2026.md`.

**Headline finding.** The report's as-of session is **29 June 2026**, but D-1 is **30 June 2026**. The
D-1 slice contains a complete 30 June cash session (26 M15 bars 16:30–22:45 broker = 09:30–16:00 ET,
identical bar count to every other full session in the block; O 7446.20 H 7513.40 L 7441.70 C 7493.30).
The report's claim that "the 30 June session was still open at the time of analysis" is therefore false,
and the report is one full session stale on every price, pivot, RSI2 and card level.

## 1. Section 7 checklist

| Item | Reviewer notes | Evidence observed | Score 0–5 | Action required |
|---|---|---|---|---|
| 1.1 Variables respected | Asset = S&P 500 cash index (^GSPC), not ES futures — correct. Counters USDX · VIX · DAX 40 in the required order — correct. Unit/currency index points/USD, tick 0.01 — correct. Six sources in §4 — meets the ≥6 requirement by count. **Fails on the as-of variable**: as-of is 29 Jun, not the NY close of D-1 (30 Jun), and the 5-session lookback is 23–29 Jun instead of 24–30 Jun. The 07:00 UK daily-open anchor is never stated in the report; the header instead calls the anchor "overridden to 01 July 2026", which is a date, not the anchor time. (Baseline card `anchor_broker` 09:00 = 07:00 UK is correct, but the report body does not say so.) | Header lines 5–11; §2 Market Definition (As-of date, Lookback window); §4; §10; §21b Trade 1 Entry | 1 | Rebuild on the 30 Jun cash session; state the 07:00 UK anchor explicitly in §21b and §20. |
| 1.2 Coverage & currency consistent | Mixed-date basis. §19/§20 assert 30 Jun is "excluded — had not closed", yet §13a cites a **30 Jun** Schwab article quoting "best quarter for the S&P 500 in six years" (a claim that requires the quarter to be complete), and §13d lists **30 Jun JOLTS** as an upcoming event when the NEWS slice shows it released 30 Jun 17:00 broker with actual 7.594m. §10/§12/§14 quote VIX 17.6 and USDX ~101.2 — the 30 Jun cash closes (VIX 17.54, USDX 101.134), not the 29 Jun closes (VIX 18.03, USDX 101.087) — so cross-asset data is D-1 while equity data is D-2. No unit drift. | Header; §10; §12; §13a Schwab row; §13d 30 Jun row; §14; §19; NEWS slice 2026-06-30 17:00 | 1 | Put every §2/§6/§10/§13 date on the same basis: data ≤ D-1 = 30 Jun, session = D. |
| 1.3 Audience & tone | Byline "Senior US Equity Strategist" present; institutional register throughout (§1, §18); no retail tone, no promotional language. Minor: the "trading & risk review" use statement carried by prior reports in the series (e.g. 30 Jun report line 5) is dropped here. | Header line 5; §1; §18 | 4 | Restore the trading-and-risk-review use line. |
| 2.1 Sections present & ordered | All of §1–§21 present in order, with §13a/b/c/d and §21a/b/c/d all present and correctly labelled. §17 is a single sentence. §21d carries the limitations boilerplate. | Headings throughout | 5 | None. |
| 2.2 Scorecard as a table | §6 is a proper table carrying Date/O/H/L/C/RSI2/Trend/Source A/Source B/Final/Validation — compliant. §11 is not: the **daily** pivot block is a malformed two-column grid (R3/R2/R1 in one column, P/S1/S2/S3 in another) rather than an R3→P→S3 ordered table; the **weekly** block is ordered R1→R3 ascending rather than R3→P→S3; the **monthly** pivot table is missing entirely (three timeframes required). | §6; §11 daily table; §11 weekly table; no monthly table | 2 | Re-emit §11 as three R3→P→S3 tables (daily, weekly, monthly), 3 levels each side. |
| 2.3 Method steps visible | §4 observations → §5 classification (official vs CFD/OTC) → consensus build with a stated down-weighting rule. §8 is candle-by-candle across all five sessions plus an explicit sequence assessment. §9 gives regime with persistence, range-position, overlap ratio and VOLator. §7 carries five chart placeholders with captions (pandoc has dropped the images — accepted as evidence per protocol, noted). | §4–§9; §7 captions | 4 | None material; confirm charts render in the source deliverable. |
| 3.1 Quantitative claims sourced | Numbers in §12 and §14 carry no citation and no pointer to §4/§6/§13: breadth "≈64% of members above their 50-day average, up from ~50%", "May CPI ~3.8%", "core PCE ~3.3%", "funds rate 3.50–3.75%", "WTI ~$70", "USDX ~101.2", "retail the most consistent buyer in 2026 per sell-side desks" (no desk named). §1's figures do point back to §6/§13. §13d's "JOLTS ~7.3m expected" matches neither the calendar consensus (6.822) nor the previous (7.618) in the NEWS slice. | §12 all four bullets; §14 all five bullets; §13d 30 Jun row vs NEWS slice | 1 | Source or delete every §12/§14 figure; correct the JOLTS consensus. |
| 3.2 Citations exist & contain data | Three spot-checks. (a) **CNBC**, URL `cnbc.com/2026/06/25`, Date column "26 Jun" — the URL's own date path contradicts the stated article date, and the **identical URL** is given as the source for a second, different article (Goldman/Flood, class Institutional, different headline and quote). One URL cannot host two articles by two authors in two source classes; per brief §3.2 a self-contradictory URL with a wrong date counts as fabricated. (b) **Trading Economics**, 29 Jun, "S&P 500 rising 1.2%" — internally consistent with §1's +1.18% and with §4's ≈7,439 quote. (c) **Schwab**, 30 Jun, "best quarter... in six years" — the source itself is coherent, but it is dated on a session §19 says was unavailable, so the report cites what it claims it could not see. Compounding: §6 attributes the 26 Jun close to Source B "Yahoo/StreetStats" and the 29 Jun close to Source A "S&P DJI / CNBC", but §4 contains **no Yahoo row for 26 Jun and no CNBC row for 29 Jun** — attributions asserted for date/source pairs the report's own evidence table does not hold. | §13a CNBC row; §13a Goldman row (same URL); §13a Schwab row; §4 vs §6 Source A/B columns; §19 | 0 | Hallucinated-source override applies (see §3). Replace the duplicated URL with two distinct permalinks; align §6 Source A/B with §4 rows. |
| 3.3 Calculations transparent | RSI2 formula is not written out but the arithmetic **reproduces exactly** from the report's own close column: helper recomputation on (7365.46, 7358.22, 7357.74, 7354.02, 7440.43) returns 0.0 / 0.0 / 95.9 for 25 / 26 / 29 Jun, matching §6. Trend labels follow the stated rule (23 Jun is labelled Bearish with RSI2 "---", so it is asserted, not derived). §11 pivots reproduce exactly from the report's own 29 Jun H/L/C (7445 / 7355 / 7440.43): P 7413.48, R1 7471.95, S1 7381.95, R2 7503.48, S2 7323.48, R3 7561.95, S3 7291.97 → all match the printed values. **ATR(14) is not stated** — a "5-session proxy ~73 pts" is substituted (slice ATR14 = 97.47 cash / 105.34 full-day). KER is given as "0.77" with "KER(13-proxy)" and no inputs; the required KER(13, EMA 3) specification is not shown. §21a contributions (0.15 + 0.115 + 0.08 + 0.045 + 0.03 − 0.01) sum to exactly +0.41, but the six signals are not mapped to the fixed 0.25/0.20/0.10/0.15/0.15/0.15 weight slots. | §6 note; helper `--closes` output; §11 vs §6 recomputation; §6 note (ATR proxy); §9 KER; §20; §21a | 2 | State ATR(14) on the 14-session block, state KER(13, EMA 3) inputs, and map each §21a signal to its weight slot. |
| 3.4 Numbers reconcile | Internal: 7,440.43 is identical in §1, §3, §4, §6 and §18 — good. But §21b Trade 2 TP3 and Trade 3A TP3 both quote **7,531** as "Daily R2", while §11 gives R2 = **7,503** (Δ 28 pts); the baseline card JSON carries the same 7531. §9's ATR proxy (~73) is never restated in §21 where R is sized. Against the slice, the OHLC block does not reconcile: closes are wrong by −14.08 (24 Jun), +18.22 (26 Jun) — both beyond the 10-pt Category-3 failure threshold — and by −8.94 / −8.16 on 23 / 25 Jun; opens are wrong by −67.90 (25 Jun), +33.20 (26 Jun), −31.00 (29 Jun), −18.12 (24 Jun); lows by +38.90 (26 Jun); highs by −42.60 (25 Jun). The 29 Jun close itself is fine (Δ −2.57). RSI2 in §6 (95.9) versus the slice-close RSI2 for the same session (78.08) differs by 17.8. Full log in §5 below. | §11 vs §21b Trade 2/3A; §6 vs helper cash-session table; baseline card JSON tp3 | 1 | Rebuild §6 from the 24–30 Jun cash sessions; make every card level trace to a §11 number. |
| 4.1 Pillars conclude | §8 ends "Bullish continuation — with exhaustion risk"; §9 "Bias: Bullish"; §10 carries per-counter implications plus a contradiction flag; §12 tags each bullet (price-supportive / neutral-to-negative / mildly supportive); §14 tags each macro block. All five conclude. The strategy pillar, however, does not conclude to a compliant construction: Trade 1 is required to be a **market order at the 07:00 UK daily-open anchor** and is instead a buy limit at daily P with a second, alternative entry ("or market on a hold above 7,440") on the same card. | §8; §9; §10; §12; §14; §21b Trade 1 Entry row | 3 | Single entry per card; Trade 1 = market at anchor. |
| 4.2 Peer/cross-asset interpreted | §10 gives real mechanisms, not a correlation list: dollar → multinational-earnings translation; implied vol → equity multiples; DAX as the common global-risk factor, with an explicit "Contradicts (mild)" and a divergence flag carried forward into §15/§16. Deducted one level because the levels the mechanisms are anchored on (VIX 17.6, USDX ~101.2) are 30 Jun values presented under a 29 Jun as-of, and the DAX level (~24,627) cannot be checked in the permitted slices. | §10 table; §10 contradiction flag; VIX/USDX slices to 2026-06-30 | 4 | Re-quote counters at the 30 Jun close. |
| 4.3 Synthesis reconciles tensions | The prose does reconcile: §15 sets overbought RSI2 and the DAX divergence against the reclaim; §16 defers explicitly to the payroll risk; §21a states the §17-vs-score check. But the execution layer contradicts the synthesis and the M5 templates. §9 concludes "trend-with-pullback longs preferred over fresh breakout chasing", while Trade 3A is a **breakout stop-entry** above the prior high — the 3C construction, not the 3A 57.5%-retrace rule, with no swing endpoints or ≥2×ATR magnitude logged. Trade 2 is labelled TREND but violates the TREND template on entry (7,413 = P, rule requires P + 0.10×(R1−P) = 7,419.3), on stop (7,382 = S1, rule requires P − 0.8×(P−S1) = 7,388.3) and on all three targets (7,444 / 7,472 / 7,531 versus the required R1 / R1.5 / R2 = 7,472 / 7,487.7 / 7,503.5). Trade 2's R = 31 pts = 0.29×ATR14, below the 0.3×ATR floor (linter WARN_R_TINY). Trade 3A carries no break-even rule (`be_rule: NONE`) though the three-unit model requires U3 → entry ± 0.2R on U2 fill. No card states stops and targets in both price and points beyond the R figure. | §9 "Preferred trade protocol"; §21b all three cards; §11; lint row Trade_2; baseline card JSON `be_rule` | 2 | Rebuild all three cards to the M5 templates — numeric conditions in the feedback file. |
| 4.4 Calibrated language | §17 is exactly one sentence with a stated condition, no hedge stacking. Confidence "Medium" is stated in both §3 and §18. §21a states a conflict flag rather than asserting agreement. Deducted for §21a asserting per-signal contributions without exposing the weight mapping, and for "well above threshold" / "13-month" style qualifiers used without the threshold value in §1. | §3 Confidence; §17; §18; §21a | 4 | Expose the weight mapping in §21a. |
| 5.1 Data dated; staleness flagged | Every §6 row and every §13a article carries a date; the single-source-indicative flags are present in §6, restated in §11's source-status note, itemised in §19 and propagated into all three card caveat rows — that part is done well. The row nevertheless fails on its substance: the report is a full session stale, and the staleness statement given ("the 30 June session was still open at the time of analysis") is contradicted by the D-1 slice (complete 30 Jun cash session, 26 bars, close 7493.30) and by the report's own 30 Jun-dated citations. | Header lines 8–11; §6 note; §11 source status; §19; §20 bullet 1; helper output "D-1 session used for daily pivots: 2026-06-30" | 1 | Anchor to the 30 Jun close and remove the incorrect staleness claim. |
| 5.2 Assumptions up front | The anchor-override caveat appears in the header, §19 ("Corroboration override") and §20 ("Override applied"). The ATR-proxy assumption is stated in the §6 note, §19 and §20. Single-source pivot propagation to the cards is stated in §11 and repeated in each card's Caveats row. Deducted because the override is described only as a date change with no method, and the 07:00 UK anchor time is never stated. | Header; §6 note; §11 source status; §19; §20; §21b Caveats rows | 4 | State the anchor time and the override method. |
| 5.3 Red flags surfaced | §12 and §15 both carry risks with direction tags; the RSI2 exhaustion risk is raised in §1, §8, §15 and the Trade 3A caveat; the DAX divergence is flagged in §10 and carried to §15/§16; the §13d payroll collision is carried into the Caveats row of all three cards, which is exactly the required propagation. | §12; §15; §13d; §21b Caveats rows on Trades 1, 2, 3A | 5 | None. |
| 5.4 Restrictions honoured | **Breach.** (i) §5 states that CFD/OTC aggregator prints "were down-weighted to directional-only and excluded from the accepted close", yet §6 accepts Investing.com US500 CFD values as the **Final** OHLC for 23, 24 and 25 Jun — retail CFD quotes are in the OHLC basis, and the report contradicts its own stated rule. (ii) §19 states the 25 Jun close is "derived from the 26 June −0.05% change" — a synthesised/interpolated price — yet §6 presents that row under a source attribution ("Investing US500") in the *Validated* OHLC table, with round-number O/H/L (7,360.00 / 7,390.00 / 7,330.00) that carry no source at all. Clean on the remaining restrictions: no ES-futures pricing, no bracketed variable names, no module codes (M1–M5), no framework name, instrument common names used throughout. | §5 versus §6 Final column rows 23/24/25 Jun; §6 25 Jun row; §19 "Single-source indicative fields" | 0 | Restriction-breach override applies (see §3). Exclude CFD prints from Final, or drop the sessions. |

## 2. Category roll-up

| Category | Level | Multiplier | Points | Justification |
|---|---|---|---|---|
| C1 Prompt adherence (max 20) | 1 | 0.20 | 4.00 | Rows 1.1/1.2/1.3 = 1/1/4, mean 2.00 → level 2; the restriction-breach override (row 5.4) reduces C1 by one level to 1. Wrong as-of session, wrong 5-session window, anchor time never stated, mixed D-1/D-2 currency. |
| C2 Structure (max 20) | 4 | 0.85 | 17.00 | Rows 2.1/2.2/2.3 = 5/2/4, mean 3.67 → 4. Every section and sub-section present and ordered; §6 is a correct table; §11 is malformed and the monthly pivot table is missing. |
| C3 Accuracy & evidence (max 25) | 0 | 0.00 | 0.00 | Rows 3.1/3.2/3.3/3.4 = 1/0/2/1, mean 1.00 → level 1; the hallucinated-source override sets C3 = 0. Two closes wrong by >10 pts, opens wrong by up to 67.9 pts, RSI2 17.8 off the slice, ATR(14) not computed, one URL cited for two different articles with a contradicting date. |
| C4 Reasoning & judgment (max 20) | 3 | 0.65 | 13.00 | Rows 4.1/4.2/4.3/4.4 = 3/4/2/4, mean 3.25 → 3. Cross-asset mechanism and calibrated language are genuinely strong; the card layer contradicts §9's own preferred protocol and breaks the Trade 1, Trade 2 (TREND) and Trade 3A templates. |
| C5 Currency, restrictions & transparency (max 15) | 3 | 0.65 | 9.75 | Rows 5.1/5.2/5.3/5.4 = 1/4/5/0, mean 2.50 → 3 (half rounded up). Flag discipline and red-flag propagation are good; the report is a session stale on a false staleness claim, and the CFD/derived-price restriction is breached. |
| **Total** | — | — | **43.75 → 44** | Sum of weighted points, rounded to a whole number. |

## 3. Total, band, override check

- Raw weighted total: 4.00 + 17.00 + 0.00 + 13.00 + 9.75 = **43.75 → 44**.
- **Hallucinated-source override: APPLIED.** §13a gives `cnbc.com/2026/06/25` as the URL for a 26 Jun-dated CNBC article and, in the very next row, gives the same URL for a different article (Goldman/Flood, Institutional class, different headline and quote). A single URL cannot be both; the URL's own date also contradicts the stated article date. Per framework §6 and brief §3.2 ("a URL/source that is self-contradictory or impossible (wrong date, figure not matching its own quote) counts as fabricated"), the total is capped at the Low band (40–59) and **C3 is set to 0**. The cap is not binding here — 44 already sits inside Low — but C3 = 0 is applied and costs 5 points against the level-1 mean.
- **Restriction-breach override: ALSO APPLIED.** CFD aggregator prints are carried as the Final OHLC for 23–25 Jun after §5 states they were excluded, and a derived 25 Jun close is presented under a source attribution in the Validated table. Caps the total at Moderate (60–74) — not binding at 44 — and reduces **C1 by one level, from 2 to 1**, which is applied above.
- Both overrides are recorded; the roll-up CSV carries the more consequential one (`hallucinated_source`).
- **Final Trust Score: 44 / 100 — Band: Low Trust (40–59).** Required action: reject and regenerate; do not use as a deliverable.

## 4. Card Integrity

Linter rows copied verbatim from `qa/regen_20260906_qa1/lint_static/2026-07-01.csv`:

| card_id | report_date | strategy | flags | dud |
|---|---|---|---|---|
| 2026-07-01_Trade_1 | 2026-07-01 | Trade 1 - Daily Directional (buy limit daily P) | CLEAN | False |
| 2026-07-01_Trade_2 | 2026-07-01 | Trade 2 - Pivot (buy limit daily P) | WARN_R_TINY(0.29xATR) | False |
| 2026-07-01_Trade_3A | 2026-07-01 | Trade 3A - Momentum-Pullback (breakout stop) | CLEAN | False |

Per-card integrity = 100 − 40·(#DUD) − 10·(#WARN), floored at 0:

| Card | #DUD | #WARN | Integrity |
|---|---|---|---|
| 2026-07-01_Trade_1 | 0 | 0 | 100 |
| 2026-07-01_Trade_2 | 0 | 1 | 90 |
| 2026-07-01_Trade_3A | 0 | 0 | 100 |
| **Report mean (3 non-suppressed cards)** | 0 | 1 | **96.7** |

Cards: 3 · suppressed: 0 · DUD flags: 0 · WARN flags: 1.

Note for the regeneration agent: the integrity number is high because the static linter checks level *geometry*
only. The M5 *construction* assessment — which feeds checklist row 4.3, not this number — fails on all three
cards, and the geometry itself passes only because it is measured against the report's own stale 29 Jun close.
Against the true D-1 close (7493.30), the Trade 3A buy stop at 7,446 sits **below** the market and would not be
a valid stop entry, and Trade 1's alternative "market on a hold above 7,440" is 53.3 pts under the D-1 close.

## 5. Data reconciliation log

Slice values are cash-session (16:30–22:45 broker = 09:30–16:00 ET) from `US500_upto_2026-06-30.csv` via
`engine/qa_slice_stats.py`. Tolerance per brief §4: |Δ| ≤ 3 pts on a close, ≤ 8 pts on an open/high/low = consistent.

### 5.1 §6 OHLC — every stated value against the slice

| Section | Field | Report value | Slice value | Delta | Verdict |
|---|---|---|---|---|---|
| §6 | 23 Jun Open | 7,366.51 | 7,370.40 | −3.89 | Consistent |
| §6 | 23 Jun High | 7,424.17 | 7,431.80 | −7.63 | Consistent (at tolerance) |
| §6 | 23 Jun Low | 7,347.60 | 7,356.20 | −8.60 | Discrepancy (>8) |
| §6 | 23 Jun Close | 7,365.46 | 7,374.40 | −8.94 | Discrepancy (>3) |
| §6 | 24 Jun Open | 7,370.88 | 7,389.00 | −18.12 | Discrepancy (>8) |
| §6 | 24 Jun High | 7,428.06 | 7,438.00 | −9.94 | Discrepancy (>8) |
| §6 | 24 Jun Low | 7,336.82 | 7,346.00 | −9.18 | Discrepancy (>8) |
| §6 | 24 Jun Close | 7,358.22 | 7,372.30 | −14.08 | **Category 3 failure (>10)** |
| §6 | 25 Jun Open | 7,360.00 | 7,427.90 | −67.90 | **Discrepancy — 8.5× tolerance; round number, no source** |
| §6 | 25 Jun High | 7,390.00 | 7,432.60 | −42.60 | **Discrepancy — 5.3× tolerance; round number** |
| §6 | 25 Jun Low | 7,330.00 | 7,332.90 | −2.90 | Consistent |
| §6 | 25 Jun Close | 7,357.74 | 7,365.90 | −8.16 | Discrepancy (>3); §19 states this close is *derived*, not sourced |
| §6 | 26 Jun Open | 7,357.00 | 7,323.80 | +33.20 | Discrepancy (>8) |
| §6 | 26 Jun High | 7,388.00 | 7,402.10 | −14.10 | Discrepancy (>8) |
| §6 | 26 Jun Low | 7,342.00 | 7,303.10 | +38.90 | Discrepancy (>8) |
| §6 | 26 Jun Close | 7,354.02 | 7,335.80 | +18.22 | **Category 3 failure (>10)** |
| §6 | 29 Jun Open | 7,372.00 | 7,403.00 | −31.00 | Discrepancy (>8) |
| §6 | 29 Jun High | 7,445.00 | 7,450.60 | −5.60 | Consistent |
| §6 | 29 Jun Low | 7,355.00 | 7,355.10 | −0.10 | Consistent |
| §6 | 29 Jun Close | 7,440.43 | 7,443.00 | −2.57 | Consistent |
| §6 | **30 Jun (D-1) full row** | **absent** | O 7,446.20 · H 7,513.40 · L 7,441.70 · C 7,493.30 | n/a | **Missing D-1 session — the report's window ends one session early** |

### 5.2 RSI2

| Section | Field | Report value | Reference value | Delta | Verdict |
|---|---|---|---|---|---|
| §6 | RSI2 25 Jun (from report's own closes) | 0.0 | 0.0 | 0.00 | Arithmetic correct |
| §6 | RSI2 26 Jun (from report's own closes) | 0.0 | 0.0 | 0.00 | Arithmetic correct |
| §6 / §1 / §8 / §15 | RSI2 29 Jun (from report's own closes) | 95.9 | 95.9 | 0.00 | Arithmetic correct — the RSI2 formula is applied correctly to the wrong inputs |
| §6 | RSI2 29 Jun vs slice closes | 95.9 | 78.08 | +17.82 | Discrepancy — driven entirely by the bad close column |
| §6 | RSI2 at D-1 (30 Jun) vs slice closes | not stated | 100.00 | n/a | Missing; the true D-1 momentum reading is the extreme, not 95.9 |
| §6 | RSI2 23 / 24 Jun | "---" / 0.0 | not testable (needs closes before the window) | n/a | Not testable; 23 Jun is labelled Bearish with no RSI2, so the Trend label is asserted |

### 5.3 §11 pivots — internal reproduction and slice reproduction

| Section | Field | Report value | Reference value | Delta | Verdict |
|---|---|---|---|---|---|
| §11 daily | P from report's own 29 Jun H/L/C (7445 / 7355 / 7440.43) | 7,413 | 7,413.48 | −0.48 | Reproduces (rounding) |
| §11 daily | R1 = 2P − L | 7,472 | 7,471.95 | +0.05 | Reproduces |
| §11 daily | S1 = 2P − H | 7,382 | 7,381.95 | +0.05 | Reproduces |
| §11 daily | R2 = P + (H−L) | 7,503 | 7,503.48 | −0.48 | Reproduces |
| §11 daily | S2 = P − (H−L) | 7,323 | 7,323.48 | −0.48 | Reproduces |
| §11 daily | R3 = H + 2(P−L) | 7,562 | 7,561.95 | +0.05 | Reproduces |
| §11 daily | S3 = L − 2(H−P) | 7,292 | 7,291.97 | +0.03 | Reproduces |
| §11 daily | P against the true D-1 (30 Jun) session | 7,413 | 7,482.80 | −69.80 | **Wrong prior period — every daily level is off by 34–89 pts** |
| §11 daily | R1 / R2 / R3 against D-1 | 7,472 / 7,503 / 7,562 | 7,523.90 / 7,554.50 / 7,595.60 | −51.90 / −51.50 / −33.60 | Wrong prior period |
| §11 daily | S1 / S2 / S3 against D-1 | 7,382 / 7,323 / 7,292 | 7,452.20 / 7,411.10 / 7,380.50 | −70.20 / −88.10 / −88.50 | Wrong prior period |
| §11 weekly | P against prior week (22–26 Jun cash) | 7,405 | 7,392.57 | +12.43 | Discrepancy |
| §11 weekly | S1 / S2 against prior week | 7,365 / 7,290 | 7,246.33 / 7,156.87 | +118.67 / +133.13 | **Discrepancy — the weekly set back-solves to H 7,445 / L 7,330 / C 7,440, i.e. the 29 Jun daily high and close, not the prior week's H/L/C (7,538.80 / 7,303.10 / 7,335.80). The "weekly" pivots are daily inputs relabelled.** |
| §11 monthly | monthly pivot table | absent | required (3 levels each side) | n/a | Missing section content |

### 5.4 ATR, cross-asset and calendar

| Section | Field | Report value | Slice value | Delta | Verdict |
|---|---|---|---|---|---|
| §6 note / §9 / §20 | ATR | "5-session proxy ~73 pts"; ATR(14) not computed | ATR14 = 97.47 (cash) / 105.34 (full-day) | −24.47 / −32.34 | Required metric not produced; all R-multiples in §21 are sized off the wrong denominator |
| §9 / §20 | KER | 0.77 ("13-proxy") | not reproducible — inputs not stated | n/a | Not verifiable as specified (KER(13, EMA 3)) |
| §1 / §10 / §14 | VIX | 17.6 | 18.03 (29 Jun cash close) · 17.54 (30 Jun cash close) | −0.43 vs stated as-of | Value is the D-1 close, not the stated 29 Jun as-of — currency drift |
| §10 / §12 / §14 | USDX | ~101.2 | 101.087 (29 Jun) · 101.134 (30 Jun) | +0.11 / +0.07 | Within reading tolerance; still quoted on a mixed basis |
| §10 | DAX 40 ~24,627 | ~24,627 | not in the permitted slice set | n/a | Unverifiable in this review — flagged, not scored as an error |
| §13d | JOLTS "30 Jun, ~7.3m expected", listed as upcoming | ~7.3m expected | NEWS slice: released 30 Jun 17:00 broker, actual 7.594m, consensus 6.822, previous 7.618 | consensus off by 0.478m | **Past event presented as upcoming; consensus figure matches nothing in the calendar** |
| §13c | previous-period calendar (23–29 Jun) | 3 rows, none from 30 Jun | NEWS slice 30 Jun: MNI Chicago 56.7 (cons 45.5), CB Consumer Confidence 91.2 (cons 88.8), JOLTS 7.594m | n/a | D-1 releases missing from the previous-period table |
| §13a | Schwab article dated 30 Jun | cited | §19 states 30 Jun "excluded — had not closed" | n/a | Internal contradiction |
| §21b | Trade 2 TP3 / Trade 3A TP3 "Daily R2 7,531" | 7,531 | §11 R2 = 7,503 | +28 | Card level does not exist in §11 |

### 5.5 Cross-report consistency (prior-dated reports only)

| Section | Field | This report (01 Jul) | `SP500_Report_30Jun2026.md` §6 | Delta | Verdict |
|---|---|---|---|---|---|
| §6 | 25 Jun close | 7,357.74 | 7,357.49 | +0.25 | Same session given two different "validated" closes across consecutive runs |
| §6 | 23 Jun Open / High / Low | 7,366.51 / 7,424.17 / 7,347.60 | 7,447 / 7,458 / 7,350 | −80.5 / −33.8 / −2.4 | Same session, materially different OHLC across consecutive runs |
| §6 | 23–26 Jun validation status | SINGLE-SOURCE (indic.), Investing US500 (CFD) | CORROBORATED (S&P DJI × CNBC / TheStreet / FRED), Δ0.00 | n/a | **Direct contradiction: sessions declared corroborated on 30 Jun are declared single-source CFD on 01 Jul.** At least one of the two source attributions is wrong. |
