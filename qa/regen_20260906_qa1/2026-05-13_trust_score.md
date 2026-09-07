# Trust Score — 2026-05-13 — SP500_Daily_Report_13May2026.md

Run: regen_20260906_qa1 · D = 2026-05-13 · D-1 slice = data/slices/US500/US500_upto_2026-05-12.csv (cash session 16:30–23:00 broker) · Helper: `engine/qa_slice_stats.py --closes 7337.11 7337.11 7398.93 7412.84 7400.96`

Reference values from the slice (D-1 = 2026-05-12): cash O/H/L/C 7396.3 / 7415.5 / 7345.3 / 7409.8 · full-day close 7402.0 · ATR14 67.35 (cash) / 76.55 (full-day; the basis the linter's ATR warnings use) · daily pivots (cash) P 7390.20 R1 7435.10 S1 7364.90 R2 7460.40 S2 7320.00 R3 7505.30 S3 7294.70 · weekly (04–08 May cash) P 7328.53 R1 7479.57 S1 7249.57 · 5d swing 7435.0 (11 May) / 7306.9 (06 May) · 25d swing 7435.0 (11 May) / 6742.3 (08 Apr).

Report's stated values: D-1 O/H/L/C 7390.63 / 7403.00 / 7338.54 / 7400.96 · RSI2 column ≈67 / ≈58 / ≈88 / ≈71 / ≈33 · ATR(14) never stated numerically (implied ≈60 from "3.5 × ATR(14) ≈ 210 pts", §21b) · daily pivots P 7380.83 R1 7423.12 S1 7358.66 R2 7445.29 S2 7316.37 R3 7487.58 S3 7294.20 · direction score +0.12 (LONG weak) · regime: short-term TRANSITIONAL (bearish lean), medium-term TRENDING BULLISH, KER TRENDING (no value) · cards: Trade 1 SUPPRESSED; Trade 2 TREND long, buy stop 7385.06 / SL 7363.09 / TP 7423.12–7434.21–7445.29, R 21.97; Trade 3C long, buy stop 7432.00 / SL 7335.00 / TP 7529–7626–7606, R 97.

## 1. Section 7 checklist

| Item | Reviewer notes | Evidence observed | Score 0–5 | Action required |
|---|---|---|---|---|
| 1.1 Variables respected | Asset = S&P 500 cash (not ES); counters USDX·VIX·DAX in the required order; USD / index points / tick 0.01; 5-session lookback; 6 price sources claimed; 07:00 UK anchor stated. Minor: "As-of date 13 May 2026" is given as D rather than the NY close of D-1. | §2 table, header, §10, §19, §20 | 4 | State as-of as the D-1 NY close. |
| 1.2 Coverage & currency consistent | No unit/currency drift. Date drift: §21c labels 06–09 May as "Tue…Fri" (06 May 2026 is a Wednesday; 09 May is a Saturday and is used as a backtest session); §11 weekly grid labelled "week ending 09 May" but built from 11 May H and 12 May C; §6 06 May close (7,337.11) contradicts the prior report's 7,365.1 for the same session. | §21c dates; §11 weekly table; §6 vs reports/md/SP500_Report_12May2026.md §6 | 2 | Fix weekday labels; rebuild weekly grid from 04–08 May only; reconcile 06 May close with the prior report. |
| 1.3 Audience & tone | Strategist register throughout; no retail tone. Template jargon leaks ("populated-instance baseline", "Updated spec") in headings/§20. | §1, §18, §20 | 4 | Strip template artefacts from headings. |
| 2.1 Sections present & ordered | §1–§21 all present and in order; §21a–d present. §13 has only 13a/13b and a "§13c News calendar — next 5 sessions": the previous-period calendar (13c) is missing and the upcoming calendar is mislabelled (should be 13d). Duplicate/placeholder headings ("§6 TECHNICAL" then "§6 Validated…", "§12 FUNDAMENTALS (Updated spec)"). §18 titled "Conclusion". | headings | 3 | Add §13c previous-period calendar; relabel upcoming as §13d; remove duplicate headings. |
| 2.2 Scorecard as a table | §6 is a table but columns are Date/O/H/L/C/RSI2/Candle read — Trend, Source A, Source B, Final and Validation columns are absent (single-source status carried by asterisks instead). §11: three grids, 3 levels each side, R3→P→S3 ordering satisfied. | §6, §11 | 3 | Rebuild §6 with the required 11 columns. |
| 2.3 Method steps visible | §4 observations → §5 consensus build present; §8 candle-by-candle + sequence [Bull×4, Bear-reversal] + persistence; §9 overlap (≈0.20) / persistence (≈0.75) / VOLator slope; §7 charts are textual placeholders (pandoc drop accepted, noted). | §4–§9 | 4 | Embed chart captions as figures where possible. |
| 3.1 Quantitative claims sourced | Many §1/§12/§14 numbers carry no source: "+7.3% m/m, +25.7% y/y", "~30% Dec hike probability", "84% beat rate per trade-press summaries", FactSet +18.6%/+24.6%/+15.9% undated, "$670bn hyperscaler capex", 10-yr "~4.24% … not directly snapped". CPI/NFP/oil figures are attributed. | §1, §12, §14, §15 | 2 | Attach source + date to each figure or point to §4/§13. |
| 3.2 Citations exist & contain data | Spot-checks: (a) FRED/S&P DJI 11 May close 7,412.84 — used identically in §4/§6/§19/§21b; slice cash 7,419.7 (Δ −6.9, basis-plausible). (b) CNBC 11 May "first close above 7,400" — consistent with §6 (08 May 7,398.93 < 7,400 < 11 May 7,412.84). (c) Investing.com 12 May O/H/L 7,390.63/7,403.00/7,338.54 — used consistently in §6/§8/§11; slice H 7,415.5 (Δ −12.5). Also: Goldman "climb 6% to 7,600" implies ≈7,170 base on 24 Apr; slice 24 Apr close 7,167 — consistent. CPI 3.8/3.7 and core 2.8/2.7 match the news slice. No impossible/self-contradictory citation found. | §4, §13a, news slice | 4 | None (no override). |
| 3.3 Calculations transparent | RSI2 not shown and does NOT reproduce: from the report's own closes the last three values are 100.0 / 100.0 / 53.9 vs stated ≈88 / ≈71 / ≈33 (Category 3 failure per brief §4). Trend column absent; candle labels contradict the rule (07 May C<O labelled "Bullish"; 12 May C 7,400.96 > O 7,390.63 labelled "Bearish reversal"). Daily pivots reproduce exactly from own H/L/C. Weekly grid does not reproduce from its own inputs (H 7,428.97 L 7,255 C 7,400.96 → S1 7,294.32 not 7,263.45; S2 7,187.67 not 7,127.98; R3 7,642.26 not 7,672.46; S3 7,120.35 not 7,058.96). Monthly grid does not reproduce (P 7,219.98 not ≈7,170; R1 7,609.95 not ≈7,539; S1 7,010.98 not ≈6,940). ATR(14) never stated; KER value never stated. §21a: five listed terms sum to +0.1185; the 0.10-weight VOLator term is omitted; stated +0.12. | §6, §11, §9, §21a, helper output | 1 | Rebuild RSI2 from the close series with arithmetic shown; state ATR(14) and KER; rebuild weekly/monthly grids; list all six §21a terms. |
| 3.4 Numbers reconcile | D-1 close 7,400.96 identical in §1/§3/§4/§6/§11/§21b; §11 pivots = card levels; RSI2 33 consistent §6=§8=§21a. Breaks: 06 May close 7,337.11 exceeds its own high 7,309.50 and equals the 07 May close; 07 May close is back-derived (footnote) but carries no flag and §20 says "no price was synthesised"; §7 "~6,830 low" vs "+13% from 30 March" (implies ≈6,550); §21c hit rates (Trade 1 TP1 4/5, Trade 2 5/5) contradict its own rows (time-stop / −1R rows); §16 base-case range 7,360–7,450 cites weekly S1 7,263 as its lower oscillation bound; Trade 3C TP3 7,606 < TP2 7,626; §21a says "no conflict with §17" while §17 is not one sentence. | §6, §7, §16, §21b, §21c | 1 | Fix the 06/07 May rows, §21c tallies, TP3 ordering. |
| 4.1 Pillars conclude | §8 → TRANSITIONAL/bearish lean; §9 → TRENDING BULLISH + "wait for confirmation"; §10 → NEUTRAL/mild contradict; §12 sub-blocks each labelled PRICE-SUPPORTIVE/NEGATIVE; §14 rates PRICE-NEGATIVE, FX "small headwind", energy labelled. | §8–§14 | 4 | Label §14 Positioning explicitly. |
| 4.2 Peer/cross-asset interpreted | Mechanisms given (USD safe-haven + CPI → Fed path; VIX >20 boundary → single-session spike vs regime change; DAX common-risk factor muted). Slice check: USDX 97.92→98.27 (report 97.84→98.28) consistent; VIX slice 19.22/19.52/19.06 vs report 17.19/18.41/17.99 (Δ ≈ −2, plausible spot-vs-CFD basis; direction and 20.2 vs 20.0 spike consistent). | §10, VIX/USDX slices | 4 | None. |
| 4.3 Synthesis reconciles tensions (incl. card construction) | §9 short×medium synthesis and §15/§16/§18 address CPI/oil vs earnings; §21a flags no §17 conflict. Card construction (M5): Trade 1 suppression correct (|0.12|<0.25) but the score omits the VOLator term. Trade 2: entry/stop/TPs follow §5.2b arithmetic exactly, but it is labelled "Buy stop @ 7,385.06" while 7,385.06 sits BELOW the D-1 close 7,400.96 (a buy stop must be above; at this level it is a limit) and R = 21.97 = 0.29×ATR14 (below the 0.3×ATR floor); short-term regime is TRANSITIONAL so the §5.2c branch applies, not "TREND". Trade 3C: M5 §4d/§5.3c require a confirmed daily close beyond the 25-day boundary by ≥0.25×ATR — none exists (D-1 close 7,400.96 < 7,428.97 ATH), so 3C is not eligible and should be suppressed; stop uses "below 12 May low" instead of range_low + 0.40×width; TPs use 1R/2R instead of +1.0×width / 1.5×MM; TP3 < TP2; "3.5×ATR cap" is a Trade 1 rule; boundary taken from the 5-day not 25-day swing. The "wait for confirmation" regime read (§9/§18) is not reconciled with two unconfirmed long-breakout cards. | §9, §15–§18, §21a–b, M5 §4d/§5.2b/§5.3c | 2 | Suppress 3C (no confirmed break) or rebuild per §5.3c; relabel Trade 2 order type and widen R to ≥0.3×ATR. |
| 4.4 Calibrated language | §17 is five sentences (must be ONE) with stacked conditionals ("either… or…", "conditional on…"). Confidence stated: §3 High, §17 Medium. | §3, §17 | 1 | Rewrite §17 as one calibrated sentence. |
| 5.1 Data dated; staleness flagged | All prices and articles dated; single-source cells asterisked; "10-yr not directly snapped" flagged. Gap: 07 May close is back-derived but unflagged in the table; RSI2 flagged analyst-derived. | §4, §6, §13a, §14, §19 | 4 | Flag the 07 May close. |
| 5.2 Assumptions up front | §20 states the 07:00 UK anchor retained and the as-of override; single-source flags propagated to card caveats and §19; Trade 1 suppressed so no anchor caveat needed. Gaps: §20 "no price was synthesised" contradicts the §6 footnote; 3C "ATR(14) estimated" without the value. | §19, §20, §21b | 3 | State ATR(14) value; correct §20 synthesis statement. |
| 5.3 Red flags surfaced | §12/§15 risks (CPI, Hormuz, breadth, chip rotation); PPI and Iran collisions from §13 carried into both card caveats. | §12, §13, §15, §21b | 5 | None. |
| 5.4 Restrictions honoured | ES confirmation-only honoured; no CFD quotes. Breach: the "Validated OHLC" table carries a synthesised close (07 May back-derived from the +0.84% print, unflagged) and a 06 May close (7,337.11) that exceeds the row's own high and duplicates 07 May — a non-sourced price presented as validated data, while §20 asserts none was synthesised. Also module/version references in the report body ("v2.1 defaults", "strategies module ENABLED", "framework's calibration"). | §6 footnote, §20, §10, §21d | 1 | Restriction override applied (see §3). Remove derived closes or mark them explicitly as derived and exclude from "validated"; strip module references. |

## 2. Category roll-up

| Category | Level | Multiplier | Points | Justification |
|---|---|---|---|---|
| C1 Prompt adherence (20) | 2 (rows 4,2,4 → mean 3.33 → 3; −1 for restriction override) | 0.40 | 8.0 | Variables respected, but date/label drift and the restriction breach (synthesised close in the validated table) drop it one level. |
| C2 Structure (20) | 3 (rows 3,3,4 → 3.33) | 0.65 | 13.0 | All 21 sections present; §13c/§13d incomplete, §6 lacks required columns, duplicate headings. |
| C3 Accuracy & evidence (25) | 2 (rows 2,4,1,1 → 2.0) | 0.40 | 10.0 | Sources internally consistent, but RSI2 does not reproduce, 06 May bar impossible, weekly/monthly pivots do not reproduce, ATR/KER unstated. |
| C4 Reasoning & judgment (20) | 3 (rows 4,4,2,1 → 2.75) | 0.65 | 13.0 | Pillars and cross-asset mechanism sound; card construction breaks M5 (3C ineligible, Trade 2 order type/R floor); §17 not one sentence. |
| C5 Currency, restrictions & transparency (15) | 3 (rows 4,3,5,1 → 3.25) | 0.65 | 9.75 | Dating and red flags strong; restriction breach and §20 contradiction. |
| **Total** | | | **53.75 → 54** | |

## 3. Total, band, override check

Total 54/100 · Band: **Low** (40–59).

Overrides: **restriction_breach** — a synthesised/back-derived price is presented inside the "Validated OHLC" table (07 May close unflagged; 06 May close above its own high and identical to 07 May) while §20 states "No price was synthesised" (brief §2 row 5.4; framework §6). Effect: cap at Moderate (60–74) — not binding since 54 < 60 — and Category 1 reduced from 3 to 2 (applied). No hallucinated-source override: the three spot-checked citations are internally consistent and agree with the slice within basis.

## 4. Card Integrity

Lint rows (qa/regen_20260906_qa1/lint_static/2026-05-13.csv, verbatim):

| card_id | report_date | strategy | flags | dud |
|---|---|---|---|---|
| 2026-05-13_Trade_1 | 2026-05-13 | Trade 1 - Daily Directional | SUPPRESSED | False |
| 2026-05-13_Trade_2 | 2026-05-13 | Trade 2 - Pivot (TREND breakout, buy stop) | WARN_R_TINY(0.29xATR) | False |
| 2026-05-13_Trade_3C | 2026-05-13 | Trade 3C - Momentum-Breakout (buy stop) | WARN_TP3_ORDER | False |

Per-card integrity (100 − 40·#DUD − 10·#WARN, floor 0):
- Trade 1: SUPPRESSED — excluded from the mean (suppression is correct: |+0.12| < 0.25).
- Trade 2: 0 DUD, 1 WARN → **90**.
- Trade 3C: 0 DUD, 1 WARN → **90**.
- Report-level mean (non-suppressed): **90.0** · n_cards 3 · n_duds 0 · n_warns 2.

M5 assessment (feeds row 4.3, not the integrity number): Trade 2 — levels follow §5.2b arithmetic from the report's pivots, but order type mislabelled (buy stop below D-1 close), R below the 0.3×ATR floor, branch should be §5.2c (TRANSITION). Trade 3C — no confirmed break per §4d (should be suppressed); stop, TP1/TP2 and TP3 all off-rule; boundary from 5-day not 25-day swing. Details in the feedback file.

## 5. Data reconciliation log

Slice = cash session (16:30–23:00 broker) unless noted. Tolerance (brief §4): close ≤3 pts, O/H/L ≤8 pts consistent; close >10 pts = failure.

| Section | Field | Report value | Slice value | Delta | Verdict |
|---|---|---|---|---|---|
| §6 | 06 May Open | 7,269.20* | 7,310.4 (full-day 7,275.5) | −41.2 (−6.3 vs full-day) | Discrepancy — matches pre-market/full-day open, not cash |
| §6 | 06 May High | 7,309.50* | 7,374.9 | −65.4 | Discrepancy |
| §6 | 06 May Low | 7,255.10* | 7,306.9 (full-day 7,272.9) | −51.8 | Discrepancy |
| §6 | 06 May Close | 7,337.11* | 7,366.4 | −29.3 | **FAIL** (>10 pts); also exceeds the row's own high 7,309.50; prior report (12 May) stated 7,365.1 |
| §6 | 07 May Open | 7,346.30* | 7,379.6 (full-day 7,359.7) | −33.3 | Discrepancy |
| §6 | 07 May High | 7,380.40* | 7,389.6 | −9.2 | Discrepancy (marginal) |
| §6 | 07 May Low | 7,328.20* | 7,325.6 | +2.6 | Consistent |
| §6 | 07 May Close | 7,337.11 | 7,344.6 (full-day 7,332.8) | −7.5 | Discrepancy; back-derived value, unflagged |
| §6 | 08 May Open | 7,343.05 | 7,375.6 (full-day 7,323.1) | −32.6 | Discrepancy |
| §6 | 08 May High | 7,401.50 | 7,407.5 | −6.0 | Consistent |
| §6 | 08 May Low | 7,335.10 | 7,371.8 (full-day 7,323.1) | −36.7 | Discrepancy |
| §6 | 08 May Close | 7,398.93 | 7,400.6 | −1.7 | Consistent |
| §6 | 11 May Open | 7,393.00 | 7,391.3 | +1.7 | Consistent |
| §6 | 11 May High | 7,428.97 | 7,435.0 | −6.0 | Consistent |
| §6 | 11 May Low | 7,388.00 | 7,391.3 | −3.3 | Consistent |
| §6 | 11 May Close | 7,412.84 | 7,419.7 | −6.9 | Discrepancy (>3) |
| §6/§11 | 12 May (D-1) Open | 7,390.63 | 7,396.3 | −5.7 | Consistent |
| §6/§11 | 12 May High | 7,403.00 | 7,415.5 | −12.5 | Discrepancy |
| §6/§11 | 12 May Low | 7,338.54 | 7,345.3 | −6.8 | Consistent |
| §6/§11/§21b | 12 May Close | 7,400.96 | 7,409.8 (full-day 7,402.0) | −8.8 (−1.0 vs full-day) | Discrepancy (>3, <10) |
| §6 | RSI2 column | ≈67 / ≈58 / ≈88 / ≈71 / ≈33 | slice closes: 100.0 / 82.2 / 72.0 / 100.0 / 65.9 | — | **FAIL** vs slice |
| §6 | RSI2 from report's own closes | ≈88 / ≈71 / ≈33 (last three) | helper: 100.0 / 100.0 / 53.9 | −12 / −29 / −21 | **FAIL** — arithmetic does not reproduce |
| §6 | Trend/candle label | 07 May "Bullish" (C<O); 12 May "Bearish" (C>O) | rule: Neutral / Neutral | — | Label rule not applied |
| §9/§21b | ATR(14) | not stated (implied ≈60 from 3.5×ATR≈210) | 67.35 cash / 76.55 full-day | ≈ −7 to −17 | Discrepancy; value must be stated |
| §11 | Daily pivots from own H/L/C | P 7380.83 R1 7423.12 S1 7358.66 R2 7445.29 S2 7316.37 R3 7487.58 S3 7294.20 | recomputed 7380.83 / 7423.13 / 7358.67 / 7445.29 / 7316.37 / 7487.59 / 7294.21 | ≤0.01 | Reproduces |
| §11 | Daily pivots vs slice | P 7380.83 / R1 7423.12 / S1 7358.66 | 7390.20 / 7435.10 / 7364.90 | −9.4 / −12.0 / −6.2 | Discrepancy (inherits H/C basis gap) |
| §11 | Weekly pivots from own inputs (H 7428.97, L 7255, C 7400.96) | P 7361.62 R1 7467.95 S1 7263.45 R2 7536.98 S2 7127.98 R3 7672.46 S3 7058.96 | 7361.64 / 7468.29 / 7294.32 / 7535.61 / 7187.67 / 7642.26 / 7120.35 | S1 −30.9, S2 −59.7, R3 +30.2, S3 −61.4 | **FAIL** to reproduce; inputs also drawn from 11–12 May under a "week ending 09 May" label (slice 04–08 May weekly P 7328.53) |
| §11 | Monthly pivots from own inputs (H 7428.97, L 6830, C 7400.96) | P ≈7170 R1 ≈7539 S1 ≈6940 R2 ≈7650 S2 ≈6720 R3 ≈7872 S3 ≈6510 | 7219.98 / 7609.95 / 7010.98 / 7818.95 / 6621.01 / 8208.92 / 6412.01 | −50 / −71 / −71 / −169 / +99 / −337 / +98 | **FAIL** to reproduce |
| §7/§9/§11 | 25-session low | ≈6,830 (early April) | 6,742.3 (08 Apr) | +88 | Discrepancy; §7 also says "+13% from 30 March" (implies ≈6,550) |
| §9/§21b | 5-day swing low | 7,338.54 (12 May) | 7,306.9 (06 May); report's own §6 low 7,255.10 (06 May) | — | Inconsistent with own table |
| §21a | Direction score | +0.12 | listed terms sum +0.1185; VOLator (w 0.10) term absent | — | Approximately traceable; incomplete |
| §10/§14 | USDX 12 May | 97.84 → 98.28 | 97.92 → 98.27 | ≤0.08 | Consistent |
| §7/§10 | VIX 08/11/12 May close; 12 May high | 17.19 / 18.41 / 17.99; 20.20 | 19.22 / 19.52 / 19.06; 20.01 | ≈ −2.0 / −1.1 / −1.1; +0.2 | Basis-level gap (spot vs CFD); direction consistent |
| §8/§12 | CPI y/y, core y/y | 3.8 vs 3.7; 2.8 vs 2.7 | news slice 3.8 (cons 3.7); 2.8 (cons 2.7) | 0 | Consistent |
| §8 | NFP 08 May | 115k vs 62k expected | news slice 115 (cons 90) | consensus differs | Minor (provider) |
| §13c | PPI 13 May | listed | news slice: PPI m/m 13 May 15:30 broker, scheduled | — | Consistent |
| §21c | Session labels | "Tue 06 May … Fri 09 May" | 06 May = Wed; 09 May = Saturday (no session) | — | Date labelling error |
