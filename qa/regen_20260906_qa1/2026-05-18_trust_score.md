# Trust Score — 2026-05-18 — SP500_Daily_18May2026.md

Reviewer basis: report for D = 2026-05-18; slice `data/slices/US500/US500_upto_2026-05-17.csv` (last bar 2026-05-15 23:45 broker); helper `engine/qa_slice_stats.py --date 2026-05-18 --closes 7412.84 7400.96 7444.25 7501.24 7408.50`; lint `qa/regen_20260906_qa1/lint_static/2026-05-18.csv`. Nothing on or after D was opened.

Report-stated anchors: D-1 (Fri 15 May) O 7,445.11 / H 7,454.85 / L 7,397.50 / C 7,408.50; RSI2 column 100 / 54 / 83 / 100 / 38; ATR(14) = 45.00 (implied only, via 0.25×ATR = 11.25 and "1 × ATR(14) (45.00)" in §21b; §5 separately says "true-range mean ~47"); daily pivots P 7420.28 · R1 7443.07 · S1 7385.72 · R2 7477.63 · S2 7362.93 · R3 7500.42 · S3 7328.37; direction score "approximately −0.22 (qualitative)", SHORT low conviction; regime TRENDING BULLISH medium / operationally TRANSITION; cards: T1 SHORT MARKET 7457.31 / SL 7466.10 / TP 7448.52 / 7439.73 / 7322.31; T2 SHORT LIMIT 7443.07 / SL 7482.13 / TP 7404.00 / 7420.28 / 7385.72; T3C SHORT STOP 7386.25 / SL 7459.35 / TP 7326.23 / 7229.13 / 7186.39.

Slice anchors (cash session 16:30–23:00 broker): D-1 O 7442.3 / H 7458.0 / L 7402.8 / C 7416.0; RSI2 on slice closes 100.00 / 65.86 / 80.81 / 100.00 / 38.22; ATR14 cash 72.23, full-day 81.06; daily pivots (cash) P 7425.60 · R1 7448.40 · S1 7393.20 · R2 7480.80 · S2 7370.40 · R3 7503.60 · S3 7338.00; swing 5d H 7522.90 / L 7345.30; swing 25d H 7522.90 / L 6790.60; weekly (prior week) P 7428.07.

## 1. Section 7 checklist

| Item | Reviewer notes | Evidence observed | Score 0–5 | Action required |
|---|---|---|---|---|
| 1.1 All Variables visibly respected | Asset = S&P 500 cash (^GSPC), counters USDX·VIX·DAX 40 with USDX first, lookback 5/25, USD / index points / tick 0.01, six sources — all respected. Not respected: (a) as-of stated as "18 May 2026 (Monday)" instead of the NY close of D-1; (b) daily-open anchor "overridden from the configured 07:00 UK baseline to a new anchor" — the override value is never printed anywhere in the report (the card extract carries 02:00 broker = 00:00 UK); (c) Trade 1 rendered despite |score| < 0.25 "per the report instruction" — no such variable exists in the instance (CONVICTION_THRESHOLD = 0.25, suppress). | §2 as-of row; §20 "M5 trace" bullet 2; §21 preamble; §21a suppression check; §21b Entry | 2 | State the anchor time explicitly (07:00 UK or the deviation), restore as-of = D-1 NY close, apply the suppression rule. |
| 1.2 Coverage Period and currency consistent | All prices/articles dated ≤ 15 May; currency/unit consistent throughout. Date drift inside D-week references: §12 "Near-term catalysts" lists Mon 19 May / Tue 20 May Walmart / Wed 21 May Nvidia / Thu 22 May, contradicting §13d (Mon 18 / Tue 19 / Wed 20 / Thu 21) and §1/§18 (Nvidia Wed 20 May). §8 cites "close 7 May ~7,398.93" then "8 May close 7,398.93" for the same level (slice: 8 May cash close 7400.3, 7 May 7349.3 — it is the 8 May close). | §12 catalysts list vs §13d table; §8 para 1 vs §8 support list | 3 | Fix the §12 weekday/date pairs to match §13d; fix 7 May → 8 May. |
| 1.3 Audience and tone | Senior US equity strategist register, trading-and-risk-review use; no retail tone. §21c/§21d slip into informal outcome talk ("T1 wins again", "would have been stopped"). | §1, §18, §21c–d | 4 | None material. |
| 2.1 Sections present and ordered | §1–§21 present in order; §13a/§13b (numeric tilt 0.00)/§13c/§13d present; §21a/b/c/d present. Gaps: §21d carries no limitations boilerplate; §7 charts are captions/placeholders only (accepted per brief, noted). | Headings; §7; §21d | 4 | Add the §21d limitations boilerplate. |
| 2.2 Scorecard as a table | §6 is a table with Date/O/H/L/C/RSI2/Trend/Source A/Source B/Validation. §11 daily, weekly, monthly tables ordered R5→P→S5 (superset of R3→P→S3). | §6, §11 | 5 | None. |
| 2.3 Method steps visible | §4 observations → §5 classification/weighted-median consensus shown; §8 candle-by-candle + sequence label; §9 regime with persistence/overlap ("estimated <0.45 / >0.55" — asserted, not computed) and VOLator (qualitative); chart substance summarised in §7. | §4–§9 | 4 | Print computed overlap/persistence values. |
| 3.1 Quantitative claims sourced | §1/§12/§14 numbers largely carry sources (Trading Economics, Equals Money/5paisa, CNBC-Yardeni, Goldman/Schneider, Citigroup/Chronert). Calendar prints in §12/§13c match the news slice exactly (CPI m/m 0.6, CPI index 332.4, PPI 1.4/core 1.0, retail sales 0.5, claims 211k, 10Y 4.47). Unsourced: CFTC DXY "18th percentile", Core PCE 129.28, "S&P 500 ~40% foreign revenue", Nikkei/HSI/Shanghai/FTSE/CAC/STOXX daily moves, "true-range mean ~47" (§5, which also conflicts with ATR 45 in §21). | §12, §14, §5 | 3 | Source or drop the unsourced §14 items; state one ATR value and its source. |
| 3.2 Citations exist and contain data | Cannot fetch. Spot-check (a) CNBC .SPX 15 May 16:00 ET — O 7,445.11 / H 7,454.85 / L 7,397.50 used consistently in §4/§6/§11/§19/§20 and within basis of slice (7442.3/7458.0/7402.8): consistent. (b) IndexBox 14 May close "7,502.04 (within tolerance of 7,501.24)" — stated tolerance is ±0.10 and Δ = 0.80, yet IndexBox is Source B "Corroborated" for 14 May in §6: internally contradictory corroboration claim. (c) TheStreet 13 May classified Bullish on the derivation quote "Treasurys rose to 2026 highs after disappointing inflation" — quote does not support the label. §20 attributes Friday O/H/L to Yahoo/Investing.com while §4 attributes them to CNBC (minor). No source is impossible or self-contradictory on date/figure → not fabricated. | §4, §6, §13a, §20 | 3 | Re-state the IndexBox corroboration honestly (it fails ±0.10); align §13a quote with class. |
| 3.3 Calculations transparent | RSI2 formula stated; from the report's own closes the helper reproduces 14 May 100.0 and 15 May 38.1 (report 100, 38) but 13 May gives 78.5 vs report 83 (Δ 4.5) — not reproducible under the stated formula; 12 May (54) untestable from five closes (slice 65.86). Daily, weekly, monthly pivots all reproduce exactly from the report's own H/L/C. ATR(14) never stated in §9 — only implied in §21b (45.00) and contradicted by §5 (~47). KER given as band only, no value. §21a direction score "approximately −0.22 (qualitative)" with no signal×weight arithmetic. §11 confluence arithmetic wrong: R1 7443.07 vs Fri high 7454.85 stated as "0.04%", actual 0.16%; weekly R1 vs 7501.24 is 0.055%, claimed within 0.05%. | §6 footnote; §11; §9; §21a; helper output | 2 | Show RSI2 gains/losses table; print ATR(14) in §9; show the six signal×weight terms. |
| 3.4 Numbers reconcile | D-1 close 7,408.50 identical in §1/§3/§4/§6/§11/§19/§20 and RSI2 38 identical in §6/§8/§18/§21a; §11 pivots = card pivots. Failures: Trade 1 MARKET entry 7457.31 ≠ D-1 close 7,408.50; §21b caveat "R (8.79) exceeds 1 × ATR(14) (45.00) — wide stop" is false; §16 "weekly S1 (~7,320)" vs §11 weekly S1 7339.96; §16 "weekly S2 / monthly R1 cluster (~7,200–7,300)" vs §11 weekly S2 7271.42 and monthly R1 7385.33 (114 pts apart); §11 R5 note "~7,627" vs R5 7615.12; §12 Nvidia "Wed 21 May" vs 20 May elsewhere; ATR §5 ~47 vs §21 45. | §21b T1 Entry/Caveats; §16; §11; §12 | 2 | Make the MARKET entry = D-1 close; correct the wide-stop caveat; align §16 levels to §11. |
| 4.1 Each pillar reaches a conclusion | §8 NEUTRAL-WITH-BEARISH-LEAN; §9 TRENDING BULLISH (medium) / operationally TRANSITION; §10 aggregate CONTRADICT; §12 each factor labelled (no aggregate label); §14 no closing direction label. Labels consistent with content. | §8, §9, §10, §12, §14 | 4 | Add a closing label to §12 and §14. |
| 4.2 Peer/cross-asset interpreted | §10 gives a transmission mechanism per counter (USD/EPS translation, VIX hedging demand, DAX energy/ECB cyclical exposure), not a correlation list. "CONTRADICTS" is measured against a trend-up continuation read while the trade direction is SHORT — the confirm status is not restated relative to the actual call. | §10 table and contradiction flag | 4 | State confirm status relative to the §21a direction. |
| 4.3 Synthesis reconciles tensions / card construction | Narrative synthesis is adequate (§15/§16/§18 address short-vs-medium, KER vs regime in §9, §17 vs §21a flagged). Card construction (scored here per protocol) fails M5 on all three cards: T1 rendered with |score| 0.22 < 0.25 (M5 §10 → SUPPRESSED row), MARKET entry 7457.31 is a synthesised "swing mid-point" not the D-1 close, anchor value unstated, wide-stop caveat false, confluences false (TP1 7448.52 is 51 pts from "Fri low 7,397.50"; TP2 7439.73 is 100 pts from "weekly S1 7339.96"); T2 is a counter-side sell limit at R1 in TRANSITION (M5 §5.2c: breakout side only — 3C is downside), TP2 7420.28 lies above TP1 7404.00 (DUD_TP2_ORDER), TP3 7385.72 between TP1 and TP2, stop buffer 0.10×ATR not 0.25×ATR, "TP2 is daily P — single-source structural" contradicts "CORROBORATED daily pivots"; T3C anchored on the 5-day low (Fri 7,397.50) instead of swing_low_25d (M5 §4d/§5.3c; slice 25d low 6790.60, report's own ~7,022), stop = Fri high + 0.10×ATR instead of boundary + 0.40×width, TP1 mislabelled "38.2% retracement" (it is entry − 0.382×157.12), TP2 "sits in the monthly R1 confluence band (7385.33)" is false (156 pts apart). All three invalidations "coincide with SL" — no separate thesis invalidation. | §21a–b; lint row for T2; M5 §4d, §5.1, §5.2c, §5.3c, §10 | 1 | Rebuild all three cards per feedback file. |
| 4.4 Calibrated language | §17 is exactly one sentence (long; "bearish-leaning balanced bias" is mild hedge stacking). Confidence Medium stated in §3 and §18; §21a SHORT (low conviction). | §3, §17, §18, §21a | 4 | Tighten §17 wording. |
| 5.1 Data points dated; staleness flagged | All prices and articles dated; 11–14 May O/H/L flagged single-source with * in §6 and in §19; weekly low and April H/L/C flagged indicative. Undated starting points for 5-day counter moves ("98.6 → 99.27", "~17 → 18.43"). | §4, §6, §13a, §19 | 4 | Date the counter start values. |
| 5.2 Material assumptions up front | Anchor-override caveat present on the card and §20, but the override VALUE is never given ("a new value", "a new anchor"); "trading strategies are NOT suppressed per the report instruction" is an assumption not traceable to any variable; single-source propagation to cards stated for weekly/monthly (not used), but T2 labels daily P "single-source structural" while daily pivots are CORROBORATED. | §20 M5 trace; §21 preamble; §21a; §21b T2 Confluences | 3 | Print the anchor time; remove or justify the no-suppression assumption. |
| 5.3 Red flags surfaced | §12/§15 risks structured; Nvidia 20 May AMC collision carried into all three card caveats and §13d flag; FOMC minutes (20 May) not carried to cards. T1 caveat carries a wrong flag (wide stop). | §12, §13d, §15, §21b | 4 | Carry FOMC minutes into card caveats; fix T1 flag. |
| 5.4 All prompt restrictions honoured | Breached: bracketed variable name "[MAX_SIMULTANEOUS_LONG_SHORT] = YES" printed in T3 caveats; module codes in the report ("M5 trace" heading §20, "Per the M5 contract" §21a, "Strategies module is ENABLED" §21); §19 admits April H/L/C are "reasonable approximations" (synthesised prior-period inputs presented in a pivot table, flagged but still shown); T1 entry 7457.31 is a synthesised price presented as the entry. ES futures not used in the basis; no retail CFD quotes in the OHLC basis (Trading Economics CFD is Directional only); common instrument names used. | §21b T3 Caveats; §20; §21a; §21 preamble; §19 | 1 | Remove bracketed names and module codes; do not print approximated monthly inputs as pivots. |

## 2. Category roll-up

| Category | Level | Multiplier | Points | Justification |
|---|---|---|---|---|
| C1 Prompt adherence (20) | 2 | 0.40 | 8.00 | Rows 2/3/4 → mean 3.0 → 3; reduced one level to 2 by the restriction-breach override (bracketed variable name, module codes). Anchor value unstated, as-of date wrong, suppression rule bypassed. |
| C2 Structure (20) | 4 | 0.85 | 17.00 | Rows 4/5/4 → 4.33 → 4. All 21 sections and sub-sections present and ordered; §21d boilerplate missing; charts as placeholders. |
| C3 Accuracy & evidence (25) | 2 | 0.40 | 10.00 | Rows 3/3/2/2 → 2.5; rounded down because the brief names an RSI2 that does not reproduce from the report's own closes (13 May 83 vs 78.5) as a Category 3 failure to score, and the MARKET entry does not reconcile to the D-1 close. All five closes sit 6.9–8.8 pts below slice cash closes (consistent basis, none > 10). |
| C4 Reasoning & judgment (20) | 3 | 0.65 | 13.00 | Rows 4/4/1/4 → 3.25 → 3. Narrative pillars and cross-asset mechanism sound; card construction violates M5 on all three cards. |
| C5 Currency & transparency (15) | 3 | 0.65 | 9.75 | Rows 4/3/4/1 → 3.0 → 3. Dating and flagging good; anchor value and suppression assumption opaque; restrictions breached. |
| **Total** | | | **57.75 → 58** | |

## 3. Total, band, override check

Total: **58/100**. Band: **Low** (40–59).

Overrides: **restriction_breach** — a prompt-stated restriction is openly violated (bracketed variable name "[MAX_SIMULTANEOUS_LONG_SHORT]" and module codes "M5" printed in the deliverable; §19 concedes approximated April H/L/C were used as pivot inputs). Applied: C1 reduced from 3 to 2; cap at Moderate (≤ 74) is not binding because the computed total (58) is already below it. No hallucinated-source override: the three spot-checked citations are internally consistent on date and figure and the calendar prints match the news slice; the IndexBox tolerance claim is wrong but the source itself is not shown to be fabricated.

## 4. Card Integrity

Lint rows (verbatim from `qa/regen_20260906_qa1/lint_static/2026-05-18.csv`):

| card_id | report_date | strategy | flags | dud |
|---|---|---|---|---|
| 2026-05-18_Trade_1 | 2026-05-18 | Trade 1 - Daily Directional | WARN_R_TINY(0.11xATR) | False |
| 2026-05-18_Trade_2 | 2026-05-18 | Trade 2 - Pivot fade (sell limit daily R1) | DUD_TP2_ORDER | True |
| 2026-05-18_Trade_3C | 2026-05-18 | Trade 3C - Transition Breakout (sell stop, conditional) | CLEAN | False |

Per-card integrity (100 − 40·#DUD − 10·#WARN, floor 0):

| Card | #DUD | #WARN | Integrity | Suppressed |
|---|---|---|---|---|
| 2026-05-18_Trade_1 | 0 | 1 | 90 | no |
| 2026-05-18_Trade_2 | 1 | 0 | 60 | no |
| 2026-05-18_Trade_3C | 0 | 0 | 100 | no |

Report-level Card Integrity (mean over 3 non-suppressed cards): **83.3**. n_cards = 3, n_duds = 1, n_warns = 1.

Note: the lint score is static; the M5 rule assessment in row 4.3 (suppression rule, entry ≠ close, regime-side rule, 25-day anchor) is not captured by the lint flags and is fed into Category 4 only.

## 5. Data reconciliation log

Slice = cash session (16:30–23:00 broker) unless stated. Tolerances per brief: close ≤ 3 pts, O/H/L ≤ 8 pts; close > 10 pts or non-reproducing RSI2 = C3 failure.

| # | Section / field | Report value | Slice value | Delta (report − slice) | Verdict |
|---|---|---|---|---|---|
| 1 | §6 Mon 11 May Open* | 7,398 | 7391.3 | +6.7 | consistent (≤ 8) |
| 2 | §6 Mon 11 May High* | 7,418 | 7435.0 | −17.0 | discrepancy (single-source, flagged *) |
| 3 | §6 Mon 11 May Low* | 7,393 | 7391.3 | +1.7 | consistent |
| 4 | §6 Mon 11 May Close | 7,412.84 | 7419.7 | −6.86 | discrepancy (> 3, < 10) |
| 5 | §6 Tue 12 May Open* | 7,412 | 7396.3 | +15.7 | discrepancy (flagged *) |
| 6 | §6 Tue 12 May High* | 7,418 | 7415.5 | +2.5 | consistent |
| 7 | §6 Tue 12 May Low* | 7,360 | 7345.3 | +14.7 | discrepancy (flagged *; also the weekly-pivot low input) |
| 8 | §6 Tue 12 May Close | 7,400.96 | 7409.8 | −8.84 | discrepancy (> 3, < 10) |
| 9 | §6 Wed 13 May Open* | 7,402 | 7412.0 | −10.0 | discrepancy (flagged *) |
| 10 | §6 Wed 13 May High* | 7,455 | 7466.0 | −11.0 | discrepancy (flagged *) |
| 11 | §6 Wed 13 May Low* | 7,398 | 7381.5 | +16.5 | discrepancy (flagged *) |
| 12 | §6 Wed 13 May Close | 7,444.25 | 7451.5 | −7.25 | discrepancy (> 3, < 10) |
| 13 | §6 Thu 14 May Open* | 7,447 | 7463.9 | −16.9 | discrepancy (flagged *) |
| 14 | §6 Thu 14 May High (ATH) | 7,517.12 | 7522.9 | −5.78 | consistent |
| 15 | §6 Thu 14 May Low* | 7,440 | 7462.9 | −22.9 | discrepancy (flagged *) |
| 16 | §6 Thu 14 May Close | 7,501.24 | 7509.1 | −7.86 | discrepancy (> 3, < 10) |
| 17 | §6/§4/§11 Fri 15 May Open (D-1) | 7,445.11 | 7442.3 | +2.81 | consistent |
| 18 | §6/§4/§11 Fri 15 May High (D-1) | 7,454.85 | 7458.0 | −3.15 | consistent |
| 19 | §6/§4/§11 Fri 15 May Low (D-1) | 7,397.50 | 7402.8 | −5.30 | consistent |
| 20 | §1/§3/§4/§6 Fri 15 May Close (D-1) | 7,408.50 | 7416.0 (full-day 7400.8) | −7.50 (+7.70 vs full-day) | discrepancy (> 3, < 10 — consistent CFD basis, not a failure) |
| 21 | §6 RSI2 Mon 11 May | 100 | 100.00 (slice); n/a from own closes | 0 | consistent |
| 22 | §6 RSI2 Tue 12 May | 54 | 65.86 (slice); n/a from own closes | −11.9 vs slice | untestable from own closes; differs from slice |
| 23 | §6 RSI2 Wed 13 May | 83 | 80.81 (slice); 78.5 from report's own closes | +4.5 vs own-close recomputation | FAIL — does not reproduce under stated formula |
| 24 | §6 RSI2 Thu 14 May | 100 | 100.00 (slice); 100.0 own closes | 0 | reproduces |
| 25 | §6/§8/§21a RSI2 Fri 15 May | 38 | 38.22 (slice); 38.1 own closes | −0.1 | reproduces |
| 26 | §21b ATR(14) (implied; §9 states none) | 45.00 (§5: ~47) | 72.23 cash / 81.06 full-day | −27.2 / −36.1 | discrepancy — ATR materially understated and not stated in §9 |
| 27 | §11 daily P/R1/S1/R2/S2/R3/S3 from report's own H/L/C | 7420.28 / 7443.07 / 7385.72 / 7477.63 / 7362.93 / 7500.42 / 7328.37 | recomputed from 7454.85/7397.50/7408.50: 7420.28 / 7443.07 / 7385.72 / 7477.63 / 7362.93 / 7500.42 / 7328.37 | 0.00 | reproduces exactly (slice-cash pivots differ by +5.3 to +9.6 through basis) |
| 28 | §11 weekly P/R1/S1/R2/S2/R3/S3 from report's own 7517.12/7360/7408.50 | 7428.54 / 7497.08 / 7339.96 / 7585.66 / 7271.42 / 7654.20 / 7182.84 | recomputed: identical | 0.00 | reproduces; weekly low input 7,360 vs slice 7345.3 (+14.7) — flagged indicative in report |
| 29 | §11 monthly inputs (April H/L/C) | ~7,257 / ~6,710 / ~7,176 | 7226.7 / 6471.7 / 7220.2 (April cash, slice from 1 Apr) | +30 / +238 / −44 | discrepancy — approximated inputs; monthly pivots reproduce arithmetically from the stated inputs but the inputs are not corroborated |
| 30 | §8 "close 7 May ~7,398.93" / "8 May close 7,398.93" | 7,398.93 | 7 May 7349.3; 8 May 7400.3 | −1.4 vs 8 May | date error — the level is the 8 May close |
| 31 | §7/§9/§10/§14/§19 VIX Fri close | 18.43 (+6.78% on day) | 19.11 at 23:00 broker (prior day 18.98 → +0.7%) | −0.68 | noted; VIX CFD vs cash basis, day-change claim not supported by slice |
| 32 | §7/§12/§14/§19 DXY Fri | 99.27 | 99.30 (23:45 broker) | −0.03 | consistent |
| 33 | §21b T1 MARKET entry vs D-1 close | 7457.31 | report close 7,408.50; slice cash 7416.0 | +48.81 / +41.31 | FAIL — MARKET entry must equal D-1 close |
| 34 | §11 confluence "R1 vs Fri high 0.04%" | 0.04% | 11.78/7443.07 = 0.16% | ×4 | arithmetic error |
| 35 | §16 "weekly S1 (~7,320)" vs §11 | ~7,320 | §11 weekly S1 7339.96 | −20 | internal inconsistency |
| 36 | §20 IndexBox 14 May close vs ±0.10 tolerance | 7,502.04 "within tolerance" | §6 close 7,501.24, tolerance ±0.10 | +0.80 | internal inconsistency in corroboration claim |
