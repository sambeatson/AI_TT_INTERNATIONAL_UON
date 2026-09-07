# Trust Score — 2026-05-27 — SP500_Report_27-May-2026.md

Inputs: report for D; slice `US500_upto_2026-05-26.csv` (cash session 16:30–23:00 broker, Memorial Day 25 May excluded from the session count as the report does); helper `qa_slice_stats.py --closes 7353.61 7431.10 7445.72 7473.47 7519.12`; lint rows `lint_static/2026-05-27.csv`; VIX/USDX slices for §10 direction only. No file dated on or after D was opened.

## 1. Section 7 checklist

| Item | Reviewer notes | Evidence observed | Score 0–5 | Action required |
|---|---|---|---|---|
| 1.1 Variables respected | Asset = S&P 500 cash index; counters USDX/VIX/DAX present (§10 lists USDX first; title line lists "VIX · DAX 40 · USDX"); as-of NY close 26 May, tz America/New_York; 5-session lookback; USD, index points (tick 0.01 not stated). Six-source claim in §4 is padded: S&P DJI row has no quote ("live page not parsed") and CME ES is excluded, so only five rows carry data. Trade 1 anchor overridden from 07:00 UK to 14:30 UK (cash open) — disclosed as a run override on the card and in §20, a deviation from the standing variable. | §2 table, §4 table + note, §10, §20 override bullet, §21b Trade 1 Entry | 3 | Restore 07:00 UK anchor or keep override with caveat; state tick size; count only sources that carry data toward the six-source minimum |
| 1.2 Coverage & currency consistent | All data dates ≤ 26 May; session date 27 May; §13d starts 27 May; §21c t−5..t−1 = 18–22 May; units are index points throughout; no currency drift. | §2, §6, §13c/d, §21c | 5 | None |
| 1.3 Audience & tone | Senior US Equity Strategist masthead; trading-and-risk-review use; §18 is a judgement with three reasons and one watch item; no retail tone. | Masthead, §2 "Decision use case", §18 | 5 | None |
| 2.1 Sections present & ordered | §1–§21 all present in the mandated order; §13a/b/c/d and §21a/b/c/d all present; §21d carries the limitations boilerplate. | Headings §1–§21 | 5 | None |
| 2.2 Scorecard as a table | §6 is a table with Date/O/H/L/C/RSI2/Trend/Source A/Source B/Validation. §11 daily/weekly/monthly tables show resistance top, P, support bottom, but extend to R5/S5 with R1.5/S1.5 appended below the ladder (monthly has no 1.5 tiers) — order requirement met, layout inconsistent across the three tables. | §6 table; §11 three tables | 4 | Present R3→P→S3 as the core ladder consistently; put 1.5 tiers in ladder position |
| 2.3 Method steps visible | §4 observations → classification (Core/Directional/Excluded) → §5 weighted-median consensus; §8 five candle notes + sequence classification; §9 regime table (overlap, persistence, directional mean, VOLator slope, KER 13/EMA3); §7 five charts present as image references with captions (pandoc dropped the images — accepted as evidence). | §4–§9 | 5 | None (note: chart images not rendered in md) |
| 3.1 Quantitative claims sourced | §1 figures trace to §4/§6/§21. §12 figures partly traced via §13 (Nvidia EPS $1.87/$1.76, Micron $1tn, Nasdaq +1.19% via TheStreet headline) but Russell 2,900, Dow −0.23%, hyperscaler capex $725bn carry no source; §14 Brent $95–100 and gold $4,505 are unsourced (no §4/§13 entry). | §12 "Substitution/Spreads", §14 "Energy", "Safe-haven" | 3 | Attach a §4/§13 source to every number in §12 and §14 |
| 3.2 Citations exist & contain data | Three spot-checks: (a) CNBC 26 May, 7,519.12, +0.61% — 7,519.12/7,473.47 − 1 = +0.61% ✓, quote used consistently in §1/§13c; (b) TheStreet 26 May 17:24 ET, 7,519.12, Nasdaq +1% headline — matches §12 Nasdaq +1.19% ✓; (c) FRED 22 May 7,473.47 — matches §6 22 May close ✓, and 22 May +0.37% ✓. Minor internal slips: §13c 20 May "+1.08%" vs own closes +1.05%; 21 May "+0.17%" vs own closes +0.20%. Reuters survey and Kiplinger dated "May 2026" only. Nothing self-contradictory or impossible — no fabrication finding. | §4 rows 1–3, 5; §13a; §13c | 3 | Date every article to the day; make §13c percentage moves agree with §6 closes |
| 3.3 Calculations transparent | Pivots reproduce exactly from the report's own D-1 H/L/C (P 7,504.71, R1 7,539.41, S1 7,484.41, R2 7,559.71, S2 7,449.71, R3 7,594.41, S3 7,429.41) and weekly from H 7,506.32/L 7,345.00/C 7,473.47. §21a score reproduces (0.25+0.20+0.05+0.042+0.069+0.15 = 0.761). KER stated. **RSI2 does not reproduce**: with the report's own closes rising on every row, the stated 2-period convention gives 100.0/100.0/100.0 for 21, 22, 26 May; the report states 70.0/82.4/92.6 (a Wilder-smoothed variant gets ≈85/93 — still not the stated numbers, and not the stated method). ATR(14) ≈ 58.6 is stated only in §21b with no derivation and no value in §9. Sentiment tilt: formula yields +0.64, then "reported conservatively at +0.46" with no rule — the number fed to §21a is not reproducible. | §6 RSI2 column vs helper output; §11; §13b; §21a table; §21b Trade 1 Stop | 1 | Recompute RSI2 with the stated method (or state the smoothing used and show it); show ATR(14) derivation in §9; report the tilt the formula produces |
| 3.4 Numbers reconcile | Internal: D-1 close 7,519.12 identical in §1/§3/§4/§6/§18/§21b ✓; §11 pivots = card levels ✓; RSI2 §6 = §8 ✓; ATR 58.6 consistent across Trade 1/3A arithmetic ✓ (absent from §9). External (slice, cash session): D-1 close 7,519.12 vs 7,527.5 (Δ −8.4, > 3-pt tolerance, < 10-pt failure line); 4 of 5 closes off by 4.6–8.7 pts; every O/H/L across five rows off by 10–48 pts except three fields; ATR 58.6 vs 71.84 (Δ −13.2); monthly pivots imply an April low of 7,012 vs slice April cash low 6,471.7 (Δ +540) — monthly ladder does not reconcile. Full log in §5. | §6 vs helper; §11 monthly vs slice April | 2 | Rebuild §6 O/H/L from a corroborated cash feed; recompute ATR and monthly pivots from validated data |
| 4.1 Pillars conclude | §8 "Bullish continuation"; §9 "Trending (Bullish bias)" with protocol; §10 "CONFIRM"; §12 each block labelled (structural/cyclical/neutral) with no aggregate label; §14 ends with an event cross-reference and "no contradiction", no direction label. Labels consistent with content. | End of §8, §9, §10, §12, §14 | 4 | Add a one-line direction label at the end of §12 and §14 |
| 4.2 Peer/cross-asset interpreted | Mechanisms given for each counter (dollar/financial conditions, VIX/fear regime, DAX/global risk factor). VIX row is self-contradictory: labelled "Falling" while quoting "≈16.6 → ≈17.0" (a rise); slice VIX 18.67 → 17.72 over five sessions is falling with an uptick on 26 May, so the label is right and the quoted levels are wrong/undated. USDX "flat-to-easing" agrees with slice (98.99 → 99.14, flat). DAX not verifiable here. | §10 table | 3 | Quote dated VIX/USDX levels that agree with the stated direction |
| 4.3 Synthesis reconciles tensions (incl. card construction) | §15/§16 reconcile extended RSI2 and Range-Top against the trend; §20/§21a address §17 vs §21a. Card construction (M5): Trade 1 stop takes the 5-day swing low (R 188.8 = 3.2× report ATR) instead of the mandated tighter of swing/nearest S/R (§8 support 7,470 → R ≈ 64) — rule violated, and the resulting 3×ATR runner cap (7,694.93) sits below TP1 (7,707.89) and TP2 (7,896.66) so Unit 3 exits before Unit 1 (lint WARN_TP3_ORDER). Trade 2 entry text "buy-stop / limit" is ambiguous (level is below the close, so it is a limit); arithmetic P+0.1(R1−P), P−0.8(P−S1), R1/R1.5/R2 correct; single-source flag propagated. Trade 3A arithmetic correct (57.5%, 38.2%, 0%, 100% ext, stop 0.25×ATR beyond anchor); BE level on TP2 fill not stated numerically; invalidation coincides with the stop anchor. Limit cards state no valid-from anchor time. | §15, §16, §20, §21a, §21b all three cards | 3 | Rebuild Trade 1 stop per M5 tighter-of rule; single entry mode on Trade 2; explicit anchor times and BE levels |
| 4.4 Calibrated language | §17 is one sentence, conditional but not hedge-stacked; §3 confidence Medium with a reason; §18 confidence Medium. §21a states "comfortably above" threshold. | §3, §17, §18 | 4 | None material |
| 5.1 Data dated; staleness flagged | Every price in §4/§6 dated; single-source O/H/L flagged on every §6 row, in the masthead, §19 and §11; Stooq/Investing.com staleness logged in §20. Reuters survey and Kiplinger articles dated only "May 2026"; VIX/USDX levels in §10 undated. | §4, §6, §10, §13a, §19, §20 | 4 | Day-date the two undated articles and the §10 counter levels |
| 5.2 Assumptions up front | Anchor-override caveat on the Trade 1 card and in §20 ✓; single-source pivot propagation stated in §19, §11 and on Trade 2 ✓; run-instruction lifting suppression stated ✓; futures exclusion stated ✓. | Masthead notes, §19, §20, §21b | 5 | None |
| 5.3 Red flags surfaced | §12/§15 risks (PCE, FOMC minutes, Iran, RSI2 extension, R1 confluence); §13d 28 May PCE collision carried into all three card caveats ✓. | §12, §13d note, §15, §21b Caveats | 5 | None |
| 5.4 Restrictions honoured | Module code appears in the report: §20 "Strategy layer (M5) trace" and "default v2.1 weights", §21a "v2.1 baseline vector" — a stated restriction (no module codes) is openly breached. Investing.com US500 range (a retail index-CFD quote) supplies the 22 May High in the OHLC basis. §6 O/H/L values are round numbers attributed to single media sources and are implausible against the slice (e.g. 26 May O 7,475 vs slice cash O 7,522.8 / L 7,505.5) — cannot prove synthesis, noted. ES futures confirmation-only ✓; no bracketed variable names; framework name absent. | §20 bullet "Strategy layer (M5) trace"; §21a; §4 Investing.com row; §6 | 2 | Remove module codes/version tags from the report body; drop retail CFD quotes from the OHLC basis |

## 2. Category roll-up

| Category | Level | Multiplier | Points | Justification |
|---|---|---|---|---|
| C1 Prompt adherence (20) | 3 (mean 4.33 → 4, −1 for restriction breach) | 0.65 | 13.00 | Variables largely respected; anchor overridden; source count padded; level dropped one step under the restriction-breach override (module code in §20/§21a) |
| C2 Structure (20) | 5 (mean 4.67) | 1.00 | 20.00 | All 21 sections and sub-sections present and ordered; tables and charts present |
| C3 Accuracy & evidence (25) | 2 (mean 2.25) | 0.40 | 10.00 | RSI2 does not reproduce from the report's own closes; every O/H/L row and 4/5 closes outside tolerance vs slice; ATR and monthly pivots do not reconcile; unsourced §12/§14 figures; sentiment tilt adjusted off-formula |
| C4 Reasoning & judgment (20) | 4 (mean 3.50) | 0.85 | 17.00 | Pillars conclude and synthesis is coherent; VIX row self-contradictory; Trade 1 stop rule violated and runner cap below TP1; Trade 2 entry mode ambiguous |
| C5 Currency, restrictions & transparency (15) | 4 (mean 4.00) | 0.85 | 12.75 | Dating and caveats strong; module-code restriction breached; retail CFD range in OHLC basis |
| **Total** | | | **72.75 → 73** | |

## 3. Total, band, override check

- Total: **73/100** (72.75 rounded).
- Band: **Moderate** (60–74).
- Overrides: **restriction_breach** — the report body contains a module code and version tag ("Strategy layer (M5) trace", "v2.1 weights" in §20; "v2.1 baseline vector" in §21a), which the brief §2 row 5.4 lists as a prompt restriction. Applied: C1 reduced from 4 to 3; cap at 74 (not binding at 73). No fabricated source found: the three spot-checked citations are dated, carry figures used consistently, and none is self-contradictory or impossible — hallucinated-source override not applied.

## 4. Card Integrity

Lint rows (verbatim from `qa/regen_20260906_qa1/lint_static/2026-05-27.csv`):

| card_id | report_date | strategy | flags | dud |
|---|---|---|---|---|
| 2026-05-27_Trade_1 | 2026-05-27 | Trade 1 - Daily Directional | WARN_TP3_ORDER | False |
| 2026-05-27_Trade_2 | 2026-05-27 | Trade 2 - Pivot (TREND_UP) | CLEAN | False |
| 2026-05-27_Trade_3A | 2026-05-27 | Trade 3A - Momentum-Pullback (57.5% fib) | CLEAN | False |

Per-card integrity (100 − 40·#DUD − 10·#WARN, floor 0):

| Card | #DUD | #WARN | Integrity | Suppressed |
|---|---|---|---|---|
| Trade 1 | 0 | 1 | 90 | No |
| Trade 2 | 0 | 0 | 100 | No |
| Trade 3A | 0 | 0 | 100 | No |

Report-level Card Integrity (mean over non-suppressed cards): **96.7**. n_cards 3 · n_duds 0 · n_warns 1.

M5 construction assessment (feeds row 4.3, not the integrity number):
- Trade 1: MARKET entry = report D-1 close 7,519.12 ✓ (slice cash close 7,527.5, Δ −8.4); anchor explicit (14:30 UK, overridden) ✓; stop 7,330.35 = 5-day swing low 7,345 − 0.25×58.6 ✓ arithmetically, but M5 requires the tighter of swing extreme and nearest S/R — nearest support 7,470 (§8) would give 7,455.35 / R 63.8; card chose the wider anchor and set the wide-stop flag ✗; TP1/TP2 = ±1R/±2R ✓; Unit 3 stop entry+0.2R = 7,556.88 ✓; runner 3×ATR cap 7,694.93 < TP1 — ordering defect ✗; invalidation (weekly P 7,441.60) separate from stop ✓; single-source flag not restated on this card (stop anchor is a single-source low) ✗ minor; PCE collision caveat ✓.
- Trade 2 (TREND): entry P + 0.10×(R1−P) = 7,451.26 ✓ (weekly pivots); stop P − 0.8×(P−S1) = 7,389.82 ✓; TPs R1/R1.5/R2 ✓; R 61.4 = 0.86×slice ATR ✓; limit below D-1 close ✓; entry mode text "buy-stop / limit" ambiguous ✗; no valid-from anchor time on the card ✗; invalidation = close through P ✓; single-source flag propagated ✓; PCE caveat ✓.
- Trade 3A: swing 7,345 → 7,525 (5-session lookback, 3.07×ATR) endpoints logged ✓; entry 57.5% = 7,421.50 ✓; stop anchor − 0.25×ATR = 7,330.35 ✓; TP1 38.2% = 7,456.24 ✓; TP2 0% = 7,525.00 ✓; TP3 100% ext = 7,705.00 ✓; R 91.2 = 1.27×slice ATR ✓; limit below D-1 close ✓; BE level on TP2 fill not stated numerically (extracted JSON records be_rule NONE) ✗ minor; invalidation coincides with the stop anchor ✗ minor; no valid-from anchor time ✗; single-source flag not restated (swing high 7,525 is a single-source high) ✗ minor; PCE caveat ✓.

## 5. Data reconciliation log

Slice values are cash-session (16:30–23:00 broker) aggregates; 25 May (Memorial Day, 15 thin CFD bars) excluded to match the report's session calendar. Tolerance: close ≤ 3 pts, O/H/L ≤ 8 pts.

| Section / field | Report value | Slice value | Δ (report − slice) | Verdict |
|---|---|---|---|---|
| §6 19 May Open | 7,405.00 | 7,371.0 | +34.0 | Discrepancy |
| §6 19 May High | 7,421.00 | 7,399.8 | +21.2 | Discrepancy |
| §6 19 May Low | 7,345.00 | 7,339.1 | +5.9 | Consistent |
| §6 19 May Close | 7,353.61 | 7,362.3 | −8.7 | Discrepancy |
| §6 20 May Open | 7,358.00 | 7,379.9 | −21.9 | Discrepancy |
| §6 20 May High | 7,445.00 | 7,443.0 | +2.0 | Consistent |
| §6 20 May Low | 7,351.00 | 7,362.3 | −11.3 | Discrepancy |
| §6 20 May Close | 7,431.10 | 7,436.8 | −5.7 | Discrepancy |
| §6 21 May Open | 7,433.00 | 7,408.6 | +24.4 | Discrepancy |
| §6 21 May High | 7,461.00 | 7,471.8 | −10.8 | Discrepancy |
| §6 21 May Low | 7,421.00 | 7,394.1 | +26.9 | Discrepancy |
| §6 21 May Close | 7,445.72 | 7,450.3 | −4.6 | Discrepancy |
| §6 22 May Open | 7,448.00 | 7,482.5 | −34.5 | Discrepancy |
| §6 22 May High | 7,506.32 | 7,509.2 | −2.9 | Consistent |
| §6 22 May Low | 7,440.00 | 7,464.5 | −24.5 | Discrepancy |
| §6 22 May Close | 7,473.47 | 7,475.7 | −2.2 | Consistent |
| §6 26 May (D-1) Open | 7,475.00 | 7,522.8 | −47.8 | Discrepancy |
| §6 26 May (D-1) High | 7,525.00 | 7,543.5 | −18.5 | Discrepancy |
| §6 26 May (D-1) Low | 7,470.00 | 7,505.5 | −35.5 | Discrepancy |
| §6 / §1 / §3 / §21b 26 May (D-1) Close | 7,519.12 | 7,527.5 (full-day 23:45 close 7,521.5) | −8.4 (−2.4 vs full-day) | Discrepancy (below the 10-pt failure line) |
| §6 RSI2 column | 7.0 / 63.2 / 70.0 / 82.4 / 92.6 | (a) slice cash closes: 0.0 / 60.5 / 100.0 / 100.0 / 100.0; (b) helper on report's own closes: n/a / n/a / 100.0 / 100.0 / 100.0 | rows 3–5: −30.0 / −17.6 / −7.4 vs own closes | **Fail** — RSI2 does not reproduce under the stated 2-period method from the report's own closes |
| §21b ATR(14) (absent from §9) | ≈ 58.6 | 71.84 cash (78.76 full-day) | −13.2 | Discrepancy |
| §11 daily pivots vs report's own H/L/C | P 7,504.71 R1 7,539.41 S1 7,484.41 R2 7,559.71 S2 7,449.71 R3 7,594.41 S3 7,429.41 | recomputed from 7,525/7,470/7,519.12: identical | 0.00 | Reproduce |
| §11 daily P vs slice cash pivots | 7,504.71 | 7,525.50 (R1 7,545.50, S1 7,507.50) | −20.8 | Discrepancy (inherits the O/H/L error) |
| §11 weekly pivots vs report's own week H/L/C | P 7,441.60 R1 7,538.19 S1 7,376.87 R2 7,602.92 | from 7,506.32/7,345.00/7,473.47: 7,441.60 / 7,538.19 / 7,376.87 / 7,602.92 | 0.00 | Reproduce |
| §11 weekly P / R1 vs slice | 7,441.60 / 7,538.19 | 7,441.33 / 7,543.57 | +0.3 / −5.4 | Consistent |
| §11 monthly pivots (implied April H/L/C) | H 7,286.0 / L 7,012.0 / C 7,274.0 (back-solved from P 7,190.67, R1 7,369.33, S1 7,095.33) | April cash H 7,226.7 / L 6,471.7 / C 7,213.7 | +59 / +540 / +60 | Discrepancy — monthly ladder does not reconcile |
| §8 / §21b 5-day swing low | 7,345.00 (19 May) | 7,339.1 (19 May) | +5.9 | Consistent |
| §8 / §21b 5-day & 25-session swing high | 7,525.00 (26 May) | 7,543.5 (26 May) | −18.5 | Discrepancy |
| §21a direction score | +0.76 | Σ = 0.761 from the table | 0.00 | Reproduce |
| §13b sentiment tilt | +0.46 (formula shown yields +0.64) | — | −0.18 undocumented adjustment | Not reproducible |
| §13c 20 May move | +1.08% | 7,431.10/7,353.61 − 1 = +1.05% | +0.03 pp | Minor internal inconsistency |
| §13c 21 May move | +0.17% | 7,445.72/7,431.10 − 1 = +0.20% | −0.03 pp | Minor internal inconsistency |
| §13c 22 May / 26 May moves | +0.37% / +0.61% | +0.37% / +0.61% | 0 | Consistent |
| §10 VIX | "Falling (≈16.6 → ≈17.0)" | slice 18.67 (18 May) → 17.72 (26 May), uptick 17.52 → 17.72 on 26 May | levels ≈ −1 to −2; label contradicts quoted levels | Direction consistent; quoted levels inconsistent |
| §10 USDX | Flat-to-easing | 98.99 → 99.14 | — | Consistent |
