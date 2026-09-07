# Trust Score — 2026-06-01 — SP500_Report_2026-06-01.md

Basis: D = 2026-06-01, D-1 = Fri 29 May 2026. Slice `data/slices/US500/US500_upto_2026-05-31.csv` (broker CFD M15; cash session 16:30–23:00 broker). Helper run with the report's §6 closes (7473.47, 7519.12, 7520.36, 7563.63, 7580.06). Slice reference values: D-1 cash OHLC 7581.1 / 7601.8 / 7567.9 / 7584.8 (full-day close 7581.1); ATR14 cash 68.68, full-day 76.37 (the linter's basis: 18 / 0.24 ≈ 75); daily pivots (cash) P 7584.83 R1 7601.77 S1 7567.87 R2 7618.73 S2 7550.93; 5-session cash swing 7601.8 (29 May) / 7504.3 (27 May); 10-session low 7339.1 (19 May). 25 May is a CFD-only bar (US holiday) and is excluded from session-based comparisons.

Report statements noted (step 1): D-1 OHLC 7579.33 / 7599.38 / 7563.55 / 7580.06; RSI2 column 81.5 / 94.3 / 94.5 / 98.5 / 99; ATR(14) ≈ 39; daily pivots P 7581.00 R1 7598.44 S1 7562.61 R2 7616.83 S2 7545.17 R3 7634.27 S3 7526.78 (plus R4/R5/S4/S5); direction score +0.46 LONG; regime TREND_UP (KER +0.66); cards: Trade 1 buy-stop 7599.5 / SL 7562.6 / TP 7636.5, 7673.5, runner 3×ATR; Trade 2 buy-limit 7581.0 / SL 7545.2 / TP 7617, 7653, runner to 7670; Trade 3A buy-limit ~7538 / SL 7520 / TP 7580, 7599, ~7690+.

## 1. Section 7 checklist

| Item | Reviewer notes | Evidence observed | Score 0–5 | Action required |
|---|---|---|---|---|
| 1.1 Variables respected | Asset = cash index, counters USDX/VIX/DAX in the right order, NY-close as-of, 5-session lookback, USD/index points all correct. Tick size not stated. Sources ≥ 6 but no exchange-tier source. The 07:00 UK daily-open anchor for Trade 1 is never stated; Trade 1 is a stop-entry (or "market on a hold of P") rather than market at the anchor. | §2 table; §4 (8 rows, 6 distinct sources); §21b Trade 1 Entry row; grep for "07:00" returns nothing | 3 | State the 07:00 UK (09:00 broker) anchor on Trade 1 and in §20; make Trade 1 a market entry at the anchor; state tick 0.01 |
| 1.2 Coverage & currency consistent | Data dates all ≤ 29 May, session = 1 June, units consistent. But §11 weekly pivots use "week ending 22 May" when the prior completed week is 25–29 May, and monthly pivots use April when the prior month is May — coverage drift on both indicative sets, and the stale weekly R2 (7,595.8) is cited as a Trade 1 confluence. | §11 headings; §21b Trade 1 Confluences | 3 | Rebuild weekly pivots from 25–29 May and monthly from May |
| 1.3 Audience & tone | Senior-strategist register, trading/risk-review framing, no retail tone. | §1, §18 | 5 | none |
| 2.1 Sections present & ordered | All 21 sections present in order, §13a–d and §21a–d present. | Headings | 5 | none |
| 2.2 Scorecard as a table | §6 carries Date/O/H/L/C/RSI2/Trend/Src A/Src B/Final/Validation. §11 tables ordered top-down but show five levels each side (R5…S5) instead of three. | §6; §11 | 4 | Trim §11 to R3→P→S3 |
| 2.3 Method steps visible | §4 observations → §5 classification/consensus → §6; §8 candle-by-candle with close-location %, sequence assessment; §9 overlap/persistence/VOLator/KER. §7 charts survive only as pandoc image placeholders (accepted, noted). | §4–§9; §7 five `![](media/…)` placeholders | 5 | none (chart images lost in conversion) |
| 3.1 Quantitative claims sourced | §1 and §12 figures trace to §4/§6/§13 (close, %, VIX to §19 FRED×Yahoo, PCE 3.8% to TheStreet, Goldman 8,000 to TipRanks). §14 "gold ~4,590" and "3.5%→3.8%" carry no source; Dell "+33–37%" range unsourced. | §14 Safe-haven / Inflation paragraphs; §12 Demand | 3 | Source the gold level and the prior PCE print or drop them |
| 3.2 Citations exist & contain data | Three spot-checks: CNBC 29 May "closed at record highs… boosted by technology" (consistent with 7,580.06, +0.22%, record); TheStreet 28 May PCE "highest in nearly three years" (consistent with §12/§14 3.8%); TipRanks/Goldman 27 May 8,000 target (used in §15). All named, dated, figures reused consistently. One tension: Motley Fool 22 May "eighth straight week of gains" makes 29 May the ninth, yet §1 says "fifth consecutive higher weekly close". Nothing impossible or self-contradictory within a source. | §13a rows 1, 3, 4, 6; §1 | 4 | Reconcile the weekly-streak count in §1 with §13a |
| 3.3 Calculations transparent | Daily pivots reproduce exactly from the report's own H/L/C (P 7581.00, R1 7598.44, S1 7562.61, R2 7616.83, S2 7545.17; R3/S3 off by 0.01). RSI2 does NOT reproduce with the stated 2-period method: from the report's own closes the last three rows must be 100 / 100 / 100 (two consecutive gains ⇒ mean loss = 0), report shows 94.5 / 98.5 / 99; the column matches a Wilder-smoothed RSI2 (slice: 84.8/94.3/94.5/98.2/98.7) but no smoothing is disclosed. ATR(14) stated ≈ 39 vs slice ATR14 68.68 (cash) / 76.37 (full-day); 39 matches a 5-day mean cash range (41.8), not a 14-period ATR. §21a score +0.46 is not derivable: the three named contributions alone (0.25 + 0.20 + 0.15) sum to 0.60 > 0.46. §13b headline "≈ +0.41" vs its own worked +0.375. KER stated. | §6 footnote; §9; §16; §21a; §13b | 2 | State the RSI2 smoothing and warm-up or restate as simple 2-period; recompute ATR14 from 14 true ranges; show the §21a Σ signal×weight line; use one tilt figure |
| 3.4 Numbers reconcile | D-1 close 7,580.06 identical in §1/§3/§4/§6/§18. Card levels match §11 (S1 7562.6, S2 7545.2, R2 7616.8, R3 7634, R4 7670). ATR 39 consistent §16 ↔ §21 (3×ATR = 116). RSI2 §6 ↔ §8 (~99). Mismatches: §13b +0.41 vs +0.38 used in §18/§20/§21a; §21d Trade 1 TP1 hit rate "80%" vs §21c table (3 of 5 rows ≥ +1R = 60%); §21b Trade 2 entry 7581.0 vs close 7580.06 (by design, at P). | cross-section | 3 | Fix §13b headline and §21d hit rate |
| 4.1 Pillars conclude | §8 "Bullish continuation", §9 "Trending — Bullish", §10 "CONFIRM", §12 per-item tags. §14 ends on a watch item without an aggregate direction label. | §8–§14 | 4 | Add a net label to §14 |
| 4.2 Peer/cross-asset interpreted | Mechanism given per counter (translation channel for USDX, fear/multiples for VIX, shared risk-appetite factor for DAX) and a net verdict. | §10 table | 5 | none |
| 4.3 Synthesis reconciles tensions (incl. card construction) | §15/§16/§18 address overbought-vs-trend, hot PCE vs calm VIX, and §17 vs §21a (no conflict). Card construction against M5 (brief §3): Trade 1 is a stop-entry at the record high, not market at the anchor; stop sits exactly on S1 with no 0.25×ATR buffer. Trade 2 in TREND_UP ignores the TREND protocol (entry P + 0.10×(R1−P), stop P − 0.8×(P−S1), TPs R1/R1.5/R2) and builds a RANGE-style limit at P with S2 stop and 1R/2R ladder. Trade 3A enters at the 38.2% retrace instead of 57.5%, stops at 7,520 instead of beyond the 0% anchor by 0.25×ATR, and its TP1 "38.2% target" coincides with its own entry level; the swing low 7,440 is a reconstructed 22 May value (slice 7,464.5), contradicting §5's claim that indicative O/H/L are excluded from stop/entry pricing; no 0.2R rule on the 3A card. | §15–§18; §21b three cards | 3 | See feedback file, items 1–3 |
| 4.4 Calibrated language | §17 is one sentence with a stated condition; confidence H/M given in §3/§18; tone "bullish but stretched" is calibrated. Trade 1 offers two alternative entries in one field, which is a hedge in an execution instruction. | §17; §3; §18; §21b Trade 1 Entry | 4 | One entry per card |
| 5.1 Data dated; staleness flagged | Every price and article dated; O/H/L single-source flag on four §6 rows; weekly/monthly indicative flags present. Not flagged: that the weekly and monthly pivot periods are stale (wrong week/month). | §4, §6, §11, §13, §19 | 4 | Flag or fix pivot periods |
| 5.2 Assumptions up front | No daily-open anchor (or override) is stated anywhere for Trade 1 or in §20. Single-source propagation: Trade 1 and 2 carry the weekly/monthly caveat; Trade 3A's fib anchor (22 May low 7,440, single-source/reconstructed) is not flagged on the card. Data-gap deviation is declared in §19/§20 (good). | §21b caveats; §19; §20 | 3 | State the anchor; flag the 3A swing anchor as indicative |
| 5.3 Red flags surfaced | §12/§15 risks listed; §13d payrolls collision carried into Trade 1 and 3A caveats, not Trade 2. | §12, §15, §21b | 4 | Add the event caveat to Trade 2 |
| 5.4 Restrictions honoured | No module codes, no framework name, no bracketed variable names, common instrument names, no ES data, retail CFD (Trading Economics) explicitly discarded. Breach: §4 states the 22/26/27/28 May O/H/L were "reconstructed from corroborated closes plus reported session moves", yet §6 lists them under Src A = CNBC / Src B = Motley Fool/Investing with the validation label "single-source", §19 repeats "single-source", §8 analyses them candle-by-candle, and the reconstructed 22 May low (7,440) prices the Trade 3A swing. Slice deltas confirm they are not quotes: 22 May O/H/L off by 34.5 / 30.7 / 24.5 pts, 26 May by 36.8 / 18.5 / 25.5 pts. This is a synthesised price presented as sourced. | §4 italic note; §6 rows 1–4; §19; §21b Trade 3A | 1 | Either drop reconstructed O/H/L from §6 (leave cells blank / "n.a.") or label them "reconstructed — not sourced" and remove them from §8 close-location arithmetic and from any card level |

## 2. Category roll-up

| Category | Level | Multiplier | Points | Justification |
|---|---|---|---|---|
| C1 Prompt adherence (20) | 3 | 0.65 | 13.00 | Rows 3, 3, 5 → mean 3.67 → level 4; restriction-breach override drops one level to 3 |
| C2 Structure (20) | 5 | 1.00 | 20.00 | Rows 5, 4, 5 → mean 4.67 → 5 |
| C3 Accuracy & evidence (25) | 3 | 0.65 | 16.25 | Rows 3, 4, 2, 3 → mean 3.0 → 3 (RSI2 method and ATR14 value do not reproduce; §21a not derivable) |
| C4 Reasoning & judgment (20) | 4 | 0.85 | 17.00 | Rows 4, 5, 3, 4 → mean 4.0 → 4 (card construction deviates from M5 on all three cards) |
| C5 Currency, restrictions & transparency (15) | 3 | 0.65 | 9.75 | Rows 4, 3, 4, 1 → mean 3.0 → 3 |
| **Total** | | | **76.00 → capped 74** | Pre-override arithmetic (C1 at 4): 80; after C1 drop: 76; restriction-breach cap: 74 |

## 3. Total, band, override check

- Total: **74/100** (uncapped arithmetic 76 after the C1 drop; 80 before any override).
- Band: **Moderate** (60–74).
- Overrides: **restriction_breach** — reconstructed/synthesised O/H/L for 22, 26, 27, 28 May are presented in the validated table (§6) with source attributions and the label "single-source", contrary to the "no synthesised/interpolated price presented as sourced" restriction (brief row 5.4), and one of those values (22 May low 7,440) prices a card. Per brief §1: cap at Moderate (74) and C1 down one level (4 → 3). No fabricated source found (three spot-checks consistent), so no hallucinated-source override.

## 4. Card Integrity

Linter rows (`qa/regen_20260906_qa1/lint_static/2026-06-01.csv`, verbatim):

| card_id | report_date | strategy | flags | dud |
|---|---|---|---|---|
| 2026-06-01_Trade_1 | 2026-06-01 | Trade 1 - Daily Directional (breakout stop) | CLEAN | False |
| 2026-06-01_Trade_2 | 2026-06-01 | Trade 2 - Pivot (buy limit daily P) | CLEAN | False |
| 2026-06-01_Trade_3A | 2026-06-01 | Trade 3A - Momentum-Pullback (38.2% fib) | WARN_R_TINY(0.24xATR) | False |

Per-card integrity (100 − 40·#DUD − 10·#WARN, floor 0):

| Card | #DUD | #WARN | Integrity |
|---|---|---|---|
| Trade 1 | 0 | 0 | 100 |
| Trade 2 | 0 | 0 | 100 |
| Trade 3A | 0 | 1 | 90 |

Report-level mean over non-suppressed cards (3 of 3): **96.7**. n_cards = 3, n_duds = 0, n_warns = 1.

M5 assessment (feeds row 4.3, not the integrity number): Trade 1 — wrong entry mode (stop vs market at anchor), anchor not stated, stop lacks the 0.25×ATR buffer, ladder and 3×ATR runner otherwise correct, invalidation separate. Trade 2 — TREND_UP protocol not applied (entry/stop/TP formulae), limit 7,581.0 sits 0.94 pts above the report's own D-1 close 7,580.06 (lint passes on the slice full-day close 7,581.1), invalidation separate. Trade 3A — wrong retrace level (38.2% vs 57.5%), stop not beyond the 0% anchor, TP1 collides with entry definition, swing anchor is a reconstructed value not flagged, no 0.2R rule, R = 18 pts = 0.24×ATR14 (linter WARN).

## 5. Data reconciliation log

Slice values are cash-session (16:30–23:00 broker) unless stated. Tolerances (brief §4): close |Δ| ≤ 3, O/H/L |Δ| ≤ 8 → consistent.

| Section | Field | Report | Slice | Δ (report − slice) | Verdict |
|---|---|---|---|---|---|
| §6 | 22 May Open | 7448.00 | 7482.5 | −34.5 | Discrepancy (reconstructed value) |
| §6 | 22 May High | 7478.50 | 7509.2 | −30.7 | Discrepancy (reconstructed) |
| §6 | 22 May Low | 7440.00 | 7464.5 | −24.5 | Discrepancy (reconstructed); also used as Trade 3A anchor |
| §6 | 22 May Close | 7473.47 | 7475.7 | −2.2 | Consistent |
| §6 | 26 May Open | 7486.00 | 7522.8 | −36.8 | Discrepancy (reconstructed) |
| §6 | 26 May High | 7525.00 | 7543.5 | −18.5 | Discrepancy (reconstructed) |
| §6 | 26 May Low | 7480.00 | 7505.5 | −25.5 | Discrepancy (reconstructed) |
| §6 | 26 May Close | 7519.12 | 7527.5 | −8.4 | Discrepancy (> 3, < 10) |
| §6 | 27 May Open | 7521.00 | 7531.0 | −10.0 | Discrepancy (> 8) |
| §6 | 27 May High | 7536.00 | 7536.0 | 0.0 | Consistent |
| §6 | 27 May Low | 7505.00 | 7504.3 | +0.7 | Consistent |
| §6 | 27 May Close | 7520.36 | 7528.5 | −8.1 | Discrepancy (> 3, < 10) |
| §6 | 28 May Open | 7527.00 | 7525.0 | +2.0 | Consistent |
| §6 | 28 May High | 7569.00 | 7576.2 | −7.2 | Consistent |
| §6 | 28 May Low | 7521.00 | 7515.5 | +5.5 | Consistent |
| §6 | 28 May Close | 7563.63 | 7572.5 | −8.9 | Discrepancy (> 3, < 10) |
| §6 / §4 | 29 May Open | 7579.33 | 7581.1 | −1.8 | Consistent |
| §6 / §4 | 29 May High | 7599.38 | 7601.8 | −2.4 | Consistent |
| §6 / §4 | 29 May Low | 7563.55 | 7567.9 | −4.4 | Consistent |
| §1/§3/§4/§6/§18 | 29 May Close | 7580.06 | 7584.8 (full-day 7581.1) | −4.7 (−1.0 vs full-day) | Discrepancy on cash basis (> 3, < 10); no close is off by > 10 → no close failure |
| §6 | RSI2 column | 81.5 / 94.3 / 94.5 / 98.5 / 99 | Helper simple RSI2 on slice cash closes: 100 / 100 / 100 / 100 / 100 (excl. 25 May CFD-only bar) | −18.5 / −5.7 / −5.5 / −1.5 / −1.0 | Method mismatch — see next row |
| §6 | RSI2 from report's own closes (simple 2-period) | 94.5 / 98.5 / 99 (rows 3–5) | 100 / 100 / 100 | −5.5 / −1.5 / −1.0 | Does not reproduce under the stated method; matches Wilder-smoothed RSI2 (slice: 84.8/94.3/94.5/98.2/98.7) — undisclosed smoothing → C3 failure recorded in 3.3 |
| §9/§16/§21b | ATR(14) | ≈ 39 | 68.68 cash / 76.37 full-day (linter basis) | −29.7 / −37.4 | Discrepancy; 39 ≈ 5-day mean cash range (41.8), not ATR14 |
| §11 | Daily pivots from report's own H/L/C | P 7581.00 R1 7598.44 S1 7562.61 R2 7616.83 S2 7545.17 R3 7634.27 S3 7526.78 | Recomputed: 7581.00 / 7598.44 / 7562.61 / 7616.83 / 7545.17 / 7634.28 / 7526.79 | ≤ 0.01 | Reproduce |
| §11 | Daily P vs slice cash pivots | 7581.00 | 7584.83 (full-day 7582.00) | −3.8 | Consistent (basis) |
| §11 | Weekly pivot inputs (implied from P/R1/S1: H 7478.49, L 7299.99, C 7473.48; week 18–22 May) | as implied | Slice week 18–22 May cash: H 7509.2, L 7339.1, C 7475.7 | −30.7 / −39.1 / −2.2 | Discrepancy on H/L; also wrong period — prior week is 25–29 May (slice weekly P 7563.63 vs report 7417.32, Δ −146.3) |
| §11 | Monthly pivot inputs (implied: H 7060.01, L 6720.01, C 7044.99; "April") | as implied | Slice April cash: H 7226.7, L 6471.7, C 7213.7 | −166.7 / +248.3 / −168.7 | Discrepancy; also wrong period — prior month is May (slice May cash H 7601.8, L 7177.5, C 7584.8 → P 7454.70 vs report 6941.67) |
| §10/§1 | VIX 29 May | 15.32 | 16.53 | −1.21 | Level differs (probable spot-vs-CFD basis); direction "falling" consistent (28 May 15.74 vs 16.78, Δ −1.04) |
| §10/§14 | USDX 29 May | "near 99" | 98.956 | ≈ 0 | Consistent |
| §21b Trade 3A | Swing low used (22 May) | 7440 | 5-session cash low 7504.3 (27 May); 22 May cash low 7464.5; 10-session low 7339.1 (19 May) | −24.5 vs 22 May | Discrepancy; anchor is a reconstructed value |
| Cross-report | 22 May row in SP500_Report_29May2026.md | O 7449 / H 7479 / L 7445 / RSI2 91.5 | this report: 7448 / 7478.5 / 7440 / 81.5 | −1 / −0.5 / −5 / −10 | Inconsistent between reports for the same session (indicative values drift) |
| §1 vs §13a | Weekly streak | "fifth consecutive higher weekly close" | Motley Fool 22 May: "eighth straight week" ⇒ ninth on 29 May | — | Internal contradiction |
| §13b | Sentiment tilt | headline ≈ +0.41 | own worked figure +0.375 (used as +0.38 in §18/§20/§21a) | +0.03 | Internal inconsistency |
| §21a | Direction score | +0.46 | named contributions 0.25 + 0.20 + 0.15 = 0.60 (+ sentiment 0.15×0.38 = 0.06 + KER term) | ≥ −0.14 | Not derivable from the shown components |
| §21d vs §21c | Trade 1 TP1 hit rate | 80% | 3 of 5 rows ≥ +1.0R = 60% | +20 pp | Internal inconsistency |
