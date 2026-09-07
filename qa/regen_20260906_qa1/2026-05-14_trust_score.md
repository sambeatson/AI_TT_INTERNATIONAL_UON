# Trust Score — 2026-05-14 — SP500_Report_14May2026.md

Run: regen_20260906_qa1 · D = 2026-05-14 · D-1 = 2026-05-13 · Data basis: `data/slices/US500/US500_upto_2026-05-13.csv` (broker CFD M15; cash session 16:30–23:00 broker). Helper run with `--closes 7444.25 7419.5 7395.6 7412.84 7400.96`.

Slice anchors used throughout: D-1 cash close 7,451.5 (full-day 7,458.5) · ATR14 cash 66.15 (full-day 75.35) · daily pivots from D-1 cash P 7,433.0 / R1 7,484.5 / S1 7,400.0 / R2 7,517.5 / S2 7,348.5 / R3 7,569.0 / S3 7,315.5 · weekly (04–08 May, cash) P 7,328.5 / R1 7,479.6 / S1 7,249.6 / R2 7,558.5 / S2 7,098.5 / R3 7,709.6 / S3 7,019.6 · monthly (April, cash) P 6,970.7 / R1 7,469.7 / S1 6,714.7 / R2 7,725.7 / S2 6,215.7 / R3 8,224.7 / S3 5,959.7 · 5-day swing H 7,466.0 (13 May) / L 7,325.6 (07 May) · 25-day H 7,466.0 / L 6,763.4 (09 Apr) · RSI2 on slice cash closes 07–13 May: 82.2 / 72.0 / 100.0 / 65.9 / 80.8 (06 May: 100.0).

## 1. Section 7 checklist

| Item | Reviewer notes | Evidence observed | Score 0–5 | Action required |
|---|---|---|---|---|
| 1.1 All seven Variables visibly respected | Asset = S&P 500 cash index; counters USDX, VIX, DAX 40 in that order; lookback 5; USD / index points / tick 0.01; 07:00 UK anchor named. As-of variable NOT respected: §2 gives as-of "14 May 2026 (07:00 UK pre-NY-open anchor)" and §3/§5/§11/§19 state the 13 May session was still open at time of write, so the report was built without the NY close of D-1. Six providers claimed only by counting Trading Economics from §12/§14 (§4 has five). | §2 table; §3 "close-of-day 13 May is intraday at time of write"; §11 daily-pivot note; §20 source list | 3 | Variable not respected: as-of NY close of D-1 (13 May). Rebuild §4/§6/§11 from the settled 13 May close. |
| 1.2 Coverage Period and currency consistent throughout | Units consistent (pts/USD). Coverage drifts: §6 window is 06–12 May, so D-1 (13 May) has no row; §1 says "as of the 13 May 2026 close" while §3 says 13 May is intraday; §13a heading says 6 articles, table has 7; §13d places US Retail Sales on Fri 15 May but the calendar slice lists Retail Sales m/m and Initial Claims at 15:30 broker on Thu 14 May. | §1 line 1; §3 Confidence; §6 table rows; §13a heading vs rows; §13d vs `news_upto_2026-05-13.csv` | 2 | Drift points: §1 vs §3 as-of statement; missing 13 May row in §6; §13a count; §13d Retail Sales date. |
| 1.3 Audience and tone match Purpose & Audience field | Strategist register, risk-review framing in §18 (position sizing vs event-risk premium). Process language leaks into the deliverable ("the user has directed", "per direct instruction" ×4). | §1, §18, §6 preamble, §19, §21a/b | 4 | Remove process/instruction language from the client-facing text. |
| 2.1 All sections present and correctly ordered | §1–§21 present and in order; §13a–d and §21a–d all present; §21d carries the limitations boilerplate. | Headings throughout | 5 | None. |
| 2.2 Key Metrics Scorecard rendered as a table | §6 is a table but lacks the Trend column and separates Source A/B/Final into one merged column ("Source A × B") plus Validation. §11 daily and weekly tables run R3→P→S3; monthly shows only R2/R1/P/S1/S2 (two levels, not three). | §6 header row; §11 monthly table | 3 | Add Trend and Source A / Source B / Final columns to §6; add monthly R3/S3. |
| 2.3 Method steps visibly addressed | §4→§5 observations → classification → weighted-median consensus shown; §8 candle-by-candle plus sequence; §9 regime with persistence and VOLator slope. §7 charts are text placeholders (pandoc/text-only delivery — accepted, noted). KER value never stated (only "KER moderate" in §20); no overlap statistic. | §4–§9, §20 | 4 | State KER(13, EMA 3) value in §9. |
| 3.1 Every quantitative claim sourced | Unsourced: §1 "S&P futures +0.16% at 7,438.5"; §12 "AAPL touched $300", "two-thirds of constituents lower"; §14 "June cut probability collapsed", 2Y/10Y moves, "16 of last 25 sessions higher", "+5.8% from ~6,995 on 09 April". Sourced: CPI/PPI (BLS/TE), WTI (EIA/TE), VIX (TE), closes (FRED/Yahoo). | §1, §9, §12, §14 | 2 | Flag listed claims for sourcing or removal. |
| 3.2 Spot-checked citations exist and contain the cited data | (a) S&P DJI/FRED 11 May close 7,412.84 — used identically in §4/§5/§6/§8/§19/§20 and in the 13 May report; slice cash 7,419.7 (Δ −6.9, CFD basis) — PASS. (b) CNBC 13 May "PPI +1.4% MoM, biggest since March 2022" — figure used consistently in §12/§13c/§14; calendar slice PPI m/m actual 1.4 (consensus 0.4, report says 0.5) — PASS. (c) CNBC "06 May — S&P 500 rose to new all-time high" and §4 "CNBC market wrap 13 May AM: raw quote '06 May high 7,444.25', basis 'recent record close reference'" — FAIL: the raw quote calls 7,444.25 a high while §6 lists the 06 May high as 7,449.1 and the close as 7,444.25 (figure does not match its own quote); slice 06 May cash O/H/L/C 7,310.4/7,374.9/7,306.9/7,366.4, i.e. no 7,444 level traded on 06 May on any basis (Δ +77.85 on the close, +74.2 on the high); the immediately prior report (13 May) records the record close as 11 May 7,412.84 and the intraday ATH as 7,428.97, contradicting a 06 May record close of 7,444.25. Fabricated figure attributed to a named source. Verbatim: "CNBC market wrap · 13 May AM · 06 May high 7,444.25 · 7,444.25 pts · Recent record close reference". | §4 row 3; §6 row 1; §13a row 1; `SP500_Daily_Report_13May2026.md` §6/§8; slice 06 May | 0 | Hallucinated-source override triggered (framework §6). |
| 3.3 Calculations transparent | RSI2 formula not shown and does not reproduce: from the report's own closes the helper gives 08 May 0.0 / 11 May 41.9 / 12 May 59.2 vs stated 38.2 / 57.1 / 36.0. Daily pivots from the report's own inputs (H 7,425 L 7,348 C 7,405): P 7,392.7 ✓ but R1 7,437.3 (stated 7,416), S1 7,360.3 (7,371), R2 7,469.7 (7,453), S2 7,315.7 (7,348), R3 7,514.3 (7,470), S3 7,283.3 (7,311) — six of seven levels fail. Weekly P from the report's own 07–08 May H/L/C (7,450.2 / 7,389.4 / 7,395.6) is 7,411.7, not 7,402. Monthly P 7,235 implies April H 7,335 / L 7,032 while §7 Chart 3 says the April low was ~6,748 — internally impossible. ATR(14) never stated (only "2×ATR(14) ≈ 56" in §21b → ATR ≈ 28 vs slice 66.15). KER not stated. §21a score +0.18 not traceable: listed contributions +0.05 +0.20 +0.10 sum to +0.35 with the cross-asset and remaining signals given no numeric value. | §6, §11, §21a, §21b 3A preamble; helper output | 1 | Derivation rebuild required for RSI2, all pivot tiers, ATR(14), KER, §21a score. |
| 3.4 Numbers reconcile across sections | D-1 close is not a single number: §1 "7,406 as of 13 May close", §3 consensus 7,406 (13 May intraday), §11 pivot input C 7,405, §6 has no 13 May row. Pivots on cards match §11 ✓ (weekly P 7,402 / S1 7,368 / R1 7,429 / R2 7,463 / R3 7,495; monthly R2 7,540). RSI2 36 consistent §6 = §8 = §21a ✓. ATR absent from §9. "Net 5-day change −0.45%" does not follow from 7,444.25→7,400.96 (−0.58%). §1 "record close 06 May 7,444.25" vs 13 May report "11 May record close 7,412.84". Cross-asset: USDX ~98.59 vs slice 13 May close 98.478 ✓; VIX 17.9–18.38 vs slice 13 May 18.94–19.49 / close 19.34 (Δ ≈ −1.0 to −1.4, VIX "5-week mean ~16.9" vs slice May readings all ≥ 18.8). | §1, §3, §6, §9, §11, §21b; VIX/USDX slices | 1 | Reconciliation breaks: D-1 close, ATR, net-5-day %, VIX level, record-close date. |
| 4.1 Each pillar reaches a defended conclusion | §8 "ranging-with-downside-tilt"; §9 "Trending Bullish, persistence high"; §10 "MIXED" with per-counter confirm/contradict; §12 sub-labels (supportive/neutral/negative/mixed); §14 has no explicit direction label but each paragraph concludes. | §8–§14 closing lines | 4 | Add a direction label to §14. |
| 4.2 Peer/cross-asset interpreted, not listed | Mechanism column present for each counter (USD translation/financial conditions, hedge demand, common-risk-factor confirmation) and a net read tied to the call. | §10 table and footnote | 4 | None. |
| 4.3 Synthesis reconciles tensions | Short- vs medium-term tension is addressed in §15/§16/§18 and §17 vs §21a is explicitly compared. Not reconciled: regime label is "Trending Up — Moderate" (§1), "Trending Bullish" (§9), "TRANSITION" forwarded to strategies (§20), and "TRENDING BULLISH" on the Trade 2/3A cards. Card construction against M5 (brief §3): Trade 2 uses a buy limit AT weekly P with 1R/2R targets, which is neither the TREND template (entry P+0.10×(R1−P), stop P−0.8×(P−S1), TPs R1/R1.5/R2), the RANGE template (limits at S1/S1.5/S2), nor TRANSITION (breakout only); Trade 3A enters at the 38.2% retrace instead of 57.5%, places the stop exactly at the 0% anchor with no 0.25×ATR buffer, uses TP1 = 0% / TP2 = 161.8% instead of TP1 38.2% / TP2 0%, and the qualifying-swing test (≥2×ATR) passes only because ATR is understated (70.6 pts vs 2×66.15 = 132.3 on the slice). Trade 1 correctly reported as a SUPPRESSED row (score +0.18 < 0.25). | §1, §9, §20, §21a, §21b | 2 | Regenerate §21b to the M5 templates after fixing the regime label. |
| 4.4 Calibrated language used appropriately | §17 is exactly one sentence; §3 confidence Medium; §16 gives case probabilities. Over-confident labels: "STRONG CONFLUENCE" is asserted on entry/stop/TP clusters whose constituent levels (weekly P 7,402, daily R1 7,416, swing low 7,378.5) do not reproduce. | §3, §16, §17, §21b confluence rows | 3 | Re-state confluence claims once levels are rebuilt. |
| 5.1 Data points dated; staleness flagged | All closes and articles dated; OHL fields flagged single-source indicative in §6/§19; 13 May intraday status flagged in §3/§11/§19. Undated/unsourced: §1 futures reading; monthly-pivot inputs ("April, settled") not shown. | §4, §6, §13a, §19 | 3 | Show the H/L/C inputs for weekly and monthly pivots with dates. |
| 5.2 Material assumptions stated up front | 07:00 UK anchor stated in §2/§20 and on Trade 1; single-source daily-pivot flag propagated to Trade 2 caveats and §19/§20. Not propagated: Trade 3A's swing high/low (7,449.1 / 7,378.5) come from OHL fields the report itself flags single-source, but the card carries no flag. §19 says flagged OHL "are NOT used for pivot prior-period H/L/C" yet §11 daily pivots use exactly such values. | §2, §19, §20, §21b | 3 | Propagate the single-source flag to 3A; resolve the §19 vs §11 contradiction. |
| 5.3 Red flags surfaced | §12/§15 carry the inflation, oil, breadth and summit risks; §13d summit collision is carried into the Trade 2 caveat. Not carried into 3A caveats (which span 14–15 May, including the Retail Sales print). §13d Retail Sales date wrong vs calendar. | §12, §15, §21b caveats, §13d | 3 | Add event-collision caveat to 3A; correct §13d dates. |
| 5.4 All prompt restrictions honoured | Honoured: Investing.com CFD quote excluded from the consensus; ES futures used as pre-open reference only; no bracketed variable names; no framework name. Breached: 06–07 May OHLC (all four fields ~60–98 pts above the slice) presented as "FRED × Yahoo close corroborated"; §19 references "Modules A and B of the approved stack" and "protocol §10 of the strategies module" (prompt-stack references in the deliverable); repeated "per direct instruction / the user has directed". | §4, §6, §19, §21a | 2 | Remove module/protocol references; rebuild 06–07 May rows from sourced data. |

## 2. Category roll-up

| Category | Level | Multiplier | Points | Justification |
|---|---|---|---|---|
| 1. Prompt adherence (20) | 3 (mean 3.00) | 0.65 | 13.00 | Asset, counters, units, lookback and 07:00 UK anchor respected; as-of NY close of D-1 not respected (13 May treated as intraday, no D-1 row); coverage drift in §1 vs §3, §13a count, §13d dates. |
| 2. Structure (20) | 4 (mean 4.00) | 0.85 | 17.00 | All 21 sections and sub-sections present and ordered; §6 lacks Trend/Final columns; monthly pivots two levels only; charts are text placeholders; KER value absent. |
| 3. Accuracy & evidence (25) | 0 (row mean 1.00; set to 0 by override) | 0.00 | 0.00 | Hallucinated-source override: 06 May "record close 7,444.25" attributed to CNBC/FRED×Yahoo cannot have traded (slice 06 May cash H 7,374.9, C 7,366.4) and contradicts the prior report; RSI2 and six of seven daily pivots do not reproduce; D-1 close absent; ATR understated. |
| 4. Reasoning & judgment (20) | 3 (mean 3.25) | 0.65 | 13.00 | Pillars conclude and cross-asset mechanism is given; regime label unreconciled across §1/§9/§20/§21b; Trade 2 and 3A do not follow the M5 templates; confluence language over-confident. |
| 5. Currency, restrictions & transparency (15) | 3 (mean 2.75) | 0.65 | 9.75 | Data dated and single-source flags present, but not propagated to 3A; §19 contradicts §11 on pivot inputs; module/protocol references and process language in the deliverable; synthesised 06–07 May prices presented as corroborated. |
| **Total** | | | **52.75 → 53** | |

## 3. Total, band, override check

Total: **53/100**. Band: **Low Trust (40–59)**.

Override: **hallucinated_source**. The §4 row "CNBC market wrap · 13 May AM · raw quote '06 May high 7,444.25' · normalised 7,444.25 pts · basis 'Recent record close reference'" and the §6 row "Wed 06 May · O 7,408.4 · H 7,449.1 · L 7,401.0 · C 7,444.25 · FRED × Yahoo (close corroborated)" attribute to named sources a figure that (i) does not match its own quote (high vs close, and §6 gives a different high), (ii) sits ~75 pts above every 06 May price in the slice (cash H 7,374.9), and (iii) is contradicted by the previous report, which records 11 May 7,412.84 as the record close. Per framework §6 the total is capped at Low (40–59) and Category 3 is set to 0; the uncapped total (with C3 at its row mean of 1 → 5.00 pts) would have been 58, so the cap does not bind. A restriction-breach override was considered for the §19 module references and the synthesised-as-sourced 06–07 May rows; it is subsumed here (both caps satisfied; C1 already scored at 3) and recorded in row 5.4 rather than as a second override, since the CSV carries one override field and the more severe one is reported.

## 4. Card Integrity

Linter rows (`qa/regen_20260906_qa1/lint_static/2026-05-14.csv`, verbatim):

| card_id | report_date | strategy | flags | dud |
|---|---|---|---|---|
| 2026-05-14_Trade_1 | 2026-05-14 | Trade 1 - Daily Directional | SUPPRESSED | False |
| 2026-05-14_Trade_2 | 2026-05-14 | Trade 2 - Pivot (buy limit weekly P) | CLEAN | False |
| 2026-05-14_Trade_3A | 2026-05-14 | Trade 3A - Momentum-Pullback (38.2% fib) | CLEAN | False |

Per-card integrity (100 − 40·#DUD − 10·#WARN, floor 0):

| Card | #DUD | #WARN | Integrity | Note |
|---|---|---|---|---|
| Trade 1 | 0 | 0 | n/a (SUPPRESSED, excluded from mean) | Suppressed row correctly present; score +0.18 < 0.25. |
| Trade 2 | 0 | 0 | 100 | Static checks pass: long limit 7,402 < D-1 close; stop 7,367 below entry; TP1 7,437 < TP2 7,472 < TP3 7,540; R 35 pts = 0.53×ATR14(66.15), within [19.8, 198.5]; TP1 35 pts from entry < 165.4. |
| Trade 3A | 0 | 0 | 100 | Static checks pass: long limit 7,422 < D-1 close; stop 7,378 below entry; TP1 7,449 < TP2 7,495 < TP3 7,540; R 44 pts = 0.67×ATR14; TP1 27 pts from entry. |

Report-level Card Integrity (mean over non-suppressed cards): **100.0**. n_cards = 3 (incl. suppressed), n_duds = 0, n_warns = 0.

Note: integrity is a static-geometry score. The M5 template assessment (row 4.3) finds both live cards non-compliant in construction even though their geometry is internally consistent.

## 5. Data reconciliation log

Tolerances (brief §4): close |Δ| ≤ 3 consistent; open/high/low |Δ| ≤ 8 consistent; close wrong by > 10 or RSI2 not reproducing = Category 3 failure. Slice values are cash-session (16:30–23:00 broker). Sign of delta = report − slice.

| # | Section / field | Report value | Slice value | Δ (pts) | Verdict |
|---|---|---|---|---|---|
| 1 | §6 06 May Open | 7,408.4 | 7,310.4 | +98.0 | Discrepancy (far beyond basis) |
| 2 | §6 06 May High | 7,449.1 | 7,374.9 | +74.2 | Discrepancy |
| 3 | §6 06 May Low | 7,401.0 | 7,306.9 | +94.1 | Discrepancy |
| 4 | §6 / §1 / §3 / §8 / §19 06 May Close ("record close") | 7,444.25 | 7,366.4 | +77.85 | Category 3 failure; basis of the hallucinated-source override |
| 5 | §6 07 May Open | 7,447.0 | 7,379.6 | +67.4 | Discrepancy |
| 6 | §6 / §8 07 May High ("new intraday high") | 7,450.2 | 7,389.6 | +60.6 | Discrepancy |
| 7 | §6 07 May Low | 7,405.7 | 7,325.6 | +80.1 | Discrepancy |
| 8 | §6 / §19 07 May Close | 7,419.5 | 7,344.6 | +74.9 | Category 3 failure |
| 9 | §6 08 May Open | 7,418.0 | 7,375.6 | +42.4 | Discrepancy |
| 10 | §6 08 May High | 7,431.8 | 7,407.5 | +24.3 | Discrepancy |
| 11 | §6 08 May Low | 7,389.4 | 7,371.8 | +17.6 | Discrepancy |
| 12 | §6 / §8 / §11 / §19 08 May Close | 7,395.6 | 7,400.6 | −5.0 | Discrepancy (> 3, < 10); prior report states 7,398.93 |
| 13 | §6 11 May Open | 7,398.1 | 7,391.3 | +6.8 | Consistent |
| 14 | §6 / §21b 11 May High | 7,424.7 | 7,435.0 | −10.3 | Discrepancy |
| 15 | §6 11 May Low | 7,392.0 | 7,391.3 | +0.7 | Consistent |
| 16 | §4 / §5 / §6 / §8 / §19 11 May Close (FRED) | 7,412.84 | 7,419.7 | −6.86 | Discrepancy (> 3, < 10; CFD basis plausible, matches prior report) |
| 17 | §6 12 May Open | 7,415.0 | 7,396.3 | +18.7 | Discrepancy |
| 18 | §6 / §8 12 May High | 7,422.9 | 7,415.5 | +7.4 | Consistent |
| 19 | §6 / §8 / §21b 12 May Low ("5-day swing low", 3A stop anchor) | 7,378.5 | 7,345.3 | +33.2 | Discrepancy; prior report states 7,338.54 |
| 20 | §4 / §6 / §9 / §21b 12 May Close | 7,400.96 | 7,409.8 | −8.84 | Discrepancy (> 3, < 10; consistent with prior report) |
| 21 | §11 D-1 (13 May) High used for daily pivots | 7,425 | 7,466.0 | −41.0 | Discrepancy |
| 22 | §11 D-1 (13 May) Low used for daily pivots | 7,348 | 7,381.5 | −33.5 | Discrepancy |
| 23 | §11 D-1 (13 May) Close used for daily pivots | 7,405 | 7,451.5 | −46.5 | Category 3 failure (D-1 close) |
| 24 | §1 / §3 / §18 consensus "as of 13 May close" | 7,406 | 7,451.5 | −45.5 | Category 3 failure (D-1 close) |
| 25 | §6 D-1 (13 May) row | absent | O 7,412.0 H 7,466.0 L 7,381.5 C 7,451.5 | n/a | Missing D-1 row |
| 26 | §4 Yahoo 13 May intraday tick | 7,352.87 | 13 May full-day low 7,381.5 | −28.6 below the day's low | Discrepancy (tick not within the slice's 13 May range) |
| 27 | §4 Multpl 13 May (excluded by report) | 7,467.86 | 13 May cash close 7,451.5 / full-day 7,458.5 | +16.4 / +9.4 | Observation: the excluded print is the closest to the slice close |
| 28 | §6 RSI2 08 May | 38.2 | from report's own closes 0.0 · slice 72.0 | n/a | Category 3 failure (does not reproduce) |
| 29 | §6 RSI2 11 May | 57.1 | from report's own closes 41.9 · slice 100.0 | n/a | Category 3 failure |
| 30 | §6 / §8 / §21a RSI2 12 May | 36.0 | from report's own closes 59.2 · slice 65.9 | n/a | Category 3 failure |
| 31 | §6 RSI2 06 / 07 May | 78.4 / 63.9 | slice 100.0 / 82.2 (report's own chain not computable) | n/a | Not reproducible |
| 32 | §11 daily R1 / S1 / R2 / S2 / R3 / S3 from report's own H/L/C | 7,416 / 7,371 / 7,453 / 7,348 / 7,470 / 7,311 | 7,437.3 / 7,360.3 / 7,469.7 / 7,315.7 / 7,514.3 / 7,283.3 | −21 / +11 / −17 / +32 / −44 / +28 | Pivot formula failure (only P = 7,393 reproduces) |
| 33 | §11 daily pivots vs slice D-1 cash | P 7,393 R1 7,416 S1 7,371 | P 7,433.0 R1 7,484.5 S1 7,400.0 | −40 / −68.5 / −29 | Discrepancy |
| 34 | §11 / §21b weekly P / R1 / S1 / R2 / R3 | 7,402 / 7,429 / 7,368 / 7,463 / 7,495 | 7,328.5 / 7,479.6 / 7,249.6 / 7,558.5 / 7,709.6 | +73.5 / −50.6 / +118.4 / −95.5 / −214.6 | Discrepancy; weekly P also ≠ 7,411.7 from the report's own 07–08 May H/L/C |
| 35 | §11 / §21b monthly P / R1 / S1 / R2 / S2 | 7,235 / 7,438 / 7,135 / 7,540 / 6,968 | 6,970.7 / 7,469.7 / 6,714.7 / 7,725.7 / 6,215.7 | +264 / −32 / +420 / −186 / +752 | Discrepancy; implied April L 7,032 contradicts §7 "25-session low 6,748" |
| 36 | §21b 3A ATR(14) implied ("2×ATR ≈ 56") | ≈ 28 | 66.15 cash / 75.35 full-day | −38 | ATR understated; not stated explicitly anywhere |
| 37 | §6 / §21b 5-day swing high / low | 7,449.1 (06 May) / 7,378.5 (12 May) | 7,466.0 (13 May) / 7,325.6 (07 May) | −16.9 / +52.9 | Discrepancy (window also excludes D-1) |
| 38 | §7 Chart 3 25-session high / low | 7,449.1 / 6,748 | 7,466.0 / 6,763.4 | −16.9 / −15.4 | Discrepancy (modest; low within basis) |
| 39 | §9 25-session net change | ≈ +5.8% (from ~6,995 on 09 Apr) | +9.8% (from 6,784.6 on 08 Apr, cash) | n/a | Discrepancy |
| 40 | §6 net 5-day change | −0.45% | from report's own closes 7,444.25→7,400.96 = −0.58% | n/a | Internal arithmetic error |
| 41 | §10 / §12 / §14 VIX | 17.9–18.38; "5-week mean ~16.9" | 13 May H 19.49 L 18.94 C 19.34; May closes 19.06–19.71 | ≈ −1.0 to −1.4 | Discrepancy |
| 42 | §10 / §12 / §14 USDX | ~98.59 / ~98.6 | 13 May C 98.478 (H 98.613) | +0.1 | Consistent |
| 43 | §12 / §13c / §14 CPI y/y | 3.8% vs 3.7% cons. | calendar 3.8 vs 3.7 | 0 | Consistent |
| 44 | §12 / §13c / §14 PPI m/m | +1.4% vs 0.5% cons. | calendar 1.4 vs 0.4 (previous 0.5) | consensus +0.1 | Minor (consensus/previous swapped) |
| 45 | §13d Retail Sales / claims date | Fri 15 May | calendar Thu 14 May 15:30 broker | 1 day | Discrepancy |
