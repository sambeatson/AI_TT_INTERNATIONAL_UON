# Trust Score — 2026-05-21 — SP500_Report_21May2026.md

Run: regen_20260906_qa1 · D = 2026-05-21 · D-1 slice = data/slices/US500/US500_upto_2026-05-20.csv (cash session 16:30–23:00 broker).
Helper output used: D-1 cash O/H/L/C 7379.9 / 7443.0 / 7362.3 / 7436.8 · ATR14 cash 75.18 (full-day 82.07) · daily pivots from D-1 cash P 7414.03 R1 7465.77 S1 7385.07 R2 7494.73 S2 7333.33 R3 7546.47 S3 7304.37 · weekly (11–15 May cash) P 7428.07 R1 7510.83 S1 7333.23 · 5d swing 7522.90 / 7339.10 · 25d swing 7522.90 / 7012.10.
Report states: D-1 (Wed 20 May) O 7369.19 H 7440.85 L 7360.10 C 7432.97; RSI2 column 82.3 / 17.9 / 16.4 / 6.4 / 68.2; ATR(14) "≈60 pts" (only in §21b caveat; implied 59.84 from stop arithmetic); daily pivots labelled "from Tue 19 May H/L/C" P 7366.80 R1 7392.41 S1 7328.01 R2 7431.20 S2 7302.40 R3 7456.81 S3 7263.61; weekly P 7437.51 R1 7486.61 S1 7359.39 R2 7564.73 S2 7310.29; direction score +0.30 LONG; regime TRANSITION (short-term Transitional over medium-term Trending-Bullish, KER +0.27); cards: Trade 1 LONG market 7432.97 / SL 7326.24 / TP 7539.70, 7646.43, runner cap 7612.49; Trade 2 LONG buy-stop 7442.42 / SL 7375.01 / TP 7486.61, 7525.67, 7564.73; Trade 3C LONG conditional close > 7515.81 / SL 7225.11 / TP 7960.42, 8190.21.

## 1. Section 7 checklist

| Item | Reviewer notes | Evidence observed | Score 0–5 | Action required |
|---|---|---|---|---|
| 1.1 Variables respected | Asset is the S&P 500 cash index (not ES); counters USDX/VIX/DAX 40 present; as-of NY close of D-1, tz America/New_York; 5-session lookback; USD, index points, tick 0.01; six sources listed. Deviations: (a) Trade 1 daily-open anchor is not 07:00 UK — it is an "anchored-open proxy = 20 May close" (card JSON anchor 02:00 broker = 00:00 UK), disclosed as an operator override in §20/§21b; (b) title line lists counters as "VIX · DAX 40 · USDX" (USDX not first; §10 table has USDX first). | §2 table, §4 (6 rows), §10, §20 "As-of override", §21b Trade 1 Entry | 4 | Restore the 07:00 UK daily-open anchor for Trade 1 or keep the override caveat; put USDX first in the header counter list |
| 1.2 Coverage & currency consistent | All data dates are 14–20 May (≤ D-1); session date is 21 May; §21c backtest uses only sessions ≤ 20 May; no currency/unit drift (index points, USD throughout). | §2, §6, §13a/c/d, §21c | 5 | none |
| 1.3 Audience & tone | "Senior US Equity Strategist · Trading & Risk Review (Forward-Test)" register maintained; no retail tone; §18 gives a three-reason judgement and a single watch item. | §1, §18, footer | 5 | none |
| 2.1 Sections present & ordered | §1–§21 all present in order; §13a/b/c/d and §21a/b/c/d present; §17 is one sentence; §21d carries the limitations boilerplate. | Headings §1…§21d | 5 | none |
| 2.2 Scorecard as a table | §6 is a table with Date/O/H/L/C/RSI2/Trend/Source A/Source B/Final/Validation. §11 tables ordered high→P→low, but daily and weekly tables carry R5…S5 (five levels each side) instead of R3→P→S3; monthly is R3→S3. R4/R5/S4/S5 are outside the specified formula set. | §6 table; §11 three tables | 4 | Trim daily/weekly pivot tables to R3→P→S3 |
| 2.3 Method steps visible | §4 observations → §5 classification/weighted-median consensus → §6 validated table; §8 candle-by-candle plus sequence assessment; §9 regime with overlap 0.49, persistence 0.52, VOLator slope, KER; §7 shows five chart image placeholders (pandoc dropped the images — accepted as evidence of presence, noted). Weighted-median weights in §5 not shown numerically. | §4–§9 | 4 | State the §5 source weights |
| 3.1 Quantitative claims sourced | Closes, % changes and pivots trace to §4/§6/§13a. Unsourced figures: 30Y yield "5.19%, ~19-year high" (§1/§12/§14 — no §13a article carries it), 10Y "~1-year high" (§13c), WTI −5.7% (§13c/§14), Russell 2000 four-week low (§12/§14), "options pricing a several-hundred-billion swing" (§12), Reuters "median target near 7,490" dated only "mid-May". | §1, §12, §13c, §14 | 3 | Attach a §13a row or §4 source to each macro figure |
| 3.2 Citations exist & contain data | Spot-check 1: CNBC 20 May "Stocks jump as oil prices and yields slide", +1.08% — consistent with §6 (7353.61→7432.97 = +1.079%); URL path is /2026/05/19 for a 20 May session piece (plausible for a CNBC live blog, not impossible). Spot-check 2: TheStreet 19 May "falls for third consecutive day… Treasurys take off", −0.67% — consistent with §6 (−0.671%) and §13c. Spot-check 3: FRED 19 May 7,353.61 — identical to §6 19 May close. Reuters strategist survey is cited "via coinotag", undated ("mid-May"); TipRanks/Goldman row points to a quote page rather than an article. Nothing self-contradictory or impossible; no fabrication finding. | §4 rows 1–4; §13a rows 1–4 | 4 | Give the Reuters/TipRanks rows a date and a real article URL |
| 3.3 Calculations transparent | RSI2 formula not shown and does NOT reproduce from the report's own closes with the specified method (2-period mean gain / mean loss): report 16.4 / 6.4 / 68.2 for 18/19/20 May vs 0.0 / 0.0 / 61.5 recomputed (helper). Trend labels are consistent with the report's own C-vs-O and RSI2. ATR(14) is never stated as a number in §9; only "≈60 pts" appears in the §21b caveat (implied 59.84 from 0.25×ATR = 14.96) — 20% below the slice 75.18 and below the ≈78 implied by the previous day's report. Pivot formulas reproduce exactly from the stated inputs (daily from the 19 May row; weekly from H 7515.62 / L 7388.40 / C 7408.50). KER stated (+0.27, threshold +0.13). Direction score shown per signal (0 + 0.20 + 0 + 0.041 + 0.018 + 0.045 = 0.304 ✓) with default weights. Tilt arithmetic shown (+0.5/4.0 = 0.125 ✓). | §6 note, §9, §11, §13b, §20, §21a/b | 2 | Show RSI2 numerator/denominator and use the specified 2-period mean method; state ATR(14) in §9 with its value |
| 3.4 Numbers reconcile | D-1 close 7,432.97 identical in §1, §3, §4, §6, §18, §21b Trade 1 entry ✓. RSI2 §6 = §8 (rounded) ✓. Pivots on cards = §11 ✓. FAILS: (i) §11 daily pivots are built from the Tue 19 May row, not the D-1 (Wed 20 May) row — from the report's own D-1 H/L/C they should be P 7411.31 R1 7462.51 S1 7381.76 R2 7492.06 S2 7330.56 R3 7543.26 S3 7301.01; the §11 "position narrative" (close "just below daily R2 7,431.20"), §15/§16 invalidation levels (daily S1 7,328) and the Trade 1 invalidation/confluence all inherit the stale basis; (ii) ATR absent from §9 while §21b uses ≈60; (iii) Trade 3C calls 7,500.85 the "25-session high" while §6/§8 give the 14 May high as 7,515.62 and the card itself says the trigger "sits just above the 14 May swing high (7,515.62)"; (iv) §13c says 15 May −1.24% whereas §6 closes give −1.23%. | §11 daily header "from Tue 19 May H/L/C"; §21b | 2 | Rebuild daily pivots from the D-1 row and re-anchor §11/§15/§16/§21b to them; state ATR in §9; define the 25-session boundary consistently |
| 4.1 Pillars conclude | §8 → "Judgement label: Indecision"; §9 → "Bias: Bullish" + protocol cell; §10 → "MIXED"; §12 → each theme labelled (supportive/negative/neutral) but no closing net label; §14 ends on a watch item without an explicit direction label. | ends of §8, §9, §10, §12, §14 | 4 | Add a one-line net direction label to §12 and §14 |
| 4.2 Peer/cross-asset interpreted | §10 gives a mechanism per counter (dollar → financial conditions/translation; VIX → hedge unwind; DAX → common risk factor) and a contradiction flag (long-end yields) that is carried into §14/§15. | §10 table + contradiction flag | 5 | none |
| 4.3 Synthesis reconciles tensions | §15/§16/§18 address short-term whipsaw vs medium-term trend, KER vs TRANSITION label (§9), rates vs risk-on (§10/§14), and §17 vs §21a (explicit conflict flag: none). Card construction (scored here per protocol): Trade 1 stop uses the 5-day swing low rather than the "tighter of (swing extreme, nearest S/R)" rule; Trade 1 runner 3×ATR cap (7,612.49) sits below TP2 (7,646.43) so the ladder is internally inconsistent; Trade 2 applies the TREND entry formula to weekly pivots under a TRANSITION label without stating the breakout-side rule used; Trade 3C follows the 3C formula mechanically to an R of 3.5–3.9×ATR and a TP1 5.4–5.9×ATR away, drops the Unit-3 +0.2R rule (Unit 3 stop moves to 7,500.85, below entry), and defines the range boundary on closes. | §15–§18, §21a, §21b | 3 | Rebuild the three cards per the feedback file |
| 4.4 Calibrated language | §17 is exactly one sentence with one condition (Nvidia) — no hedge stacking; §3 confidence Medium with a stated reason; §16 gives a range and an invalidation level. §8 "historically precedes a mean-reversion bounce" is an unquantified claim. | §3, §16, §17 | 4 | none material |
| 5.1 Data dated; staleness flagged | Every price row dated; articles dated except Reuters ("mid-May"); §6/§19 flag single-source intraday H/L generically ("where only one aggregator carried a given extreme") without saying which rows; monthly pivots explicitly flagged single-source-indicative; ATR carries no date or window statement. | §4, §6 note, §13a, §19 | 4 | Name the single-source H/L rows; date the Reuters item |
| 5.2 Assumptions up front | Anchor-override / proxy-open caveat is on the Trade 1 card and in §20 ✓; single-source monthly-pivot propagation stated in §11, §19, §20 and on Trade 2 ✓. Not surfaced: the ATR value used for every buffer/cap, and the fact that daily pivots are one session stale. | §20, §21b | 4 | State ATR and the pivot session basis explicitly |
| 5.3 Red flags surfaced | §12/§15 list rates, Nvidia, US–Iran, breadth risks; §13d Nvidia collision is carried into all three card caveats. | §12, §15, §21b caveats | 5 | none |
| 5.4 Restrictions honoured | Proxy open is disclosed, not presented as sourced ✓; CFD quote kept directional-only ✓; ES not used ✓; no bracketed variable names; no framework name. BREACH: module code "(M5)" appears in §20 ("Strategy trace (M5)"), contrary to the no-module-codes restriction. Single token; also present in earlier reports (systematic). | §20 line "Strategy trace (M5)" | 2 | Remove "(M5)" (and "Strategy module is active" meta-wording in §1) — triggers the restriction override |

## 2. Category roll-up

| Category | Level | Multiplier | Points | Justification |
|---|---|---|---|---|
| C1 Prompt adherence (20) | 4 (rows 4/5/5 → mean 4.67 → 5, reduced one level by the restriction override) | 0.85 | 17.0 | Variables respected; anchor override disclosed; header counter order; override applied for the "(M5)" module-code breach |
| C2 Structure (20) | 4 (5/4/4 → 4.33) | 0.85 | 17.0 | All sections present and ordered; §11 daily/weekly tables carry extra R4/R5/S4/S5 levels; §5 weights not shown |
| C3 Accuracy & evidence (25) | 3 (3/4/2/2 → 2.75) | 0.65 | 16.25 | Closes within 3.8–8.7 pts of slice (basis-consistent, none >10); RSI2 does not reproduce with the specified method; ATR unstated in §9 and 20% below slice; daily pivots built from the wrong session; no fabricated source |
| C4 Reasoning & judgment (20) | 4 (4/5/3/4 → 4.0) | 0.85 | 17.0 | Mechanisms and synthesis good; card construction defects (Trade 1 stop/runner order, Trade 3C R and BE rule) |
| C5 Currency & transparency (15) | 4 (4/4/5/2 → 3.75) | 0.85 | 12.75 | Dating and caveats mostly present; module-code restriction breached |
| **Total** | | | **80.0 → capped 74** | Uncapped 80.0 (pre-override, with C1 = 5, 83.0); restriction override caps the report at Moderate (74) |

## 3. Total, band, override check

- Uncapped arithmetic: 17.0 + 17.0 + 16.25 + 17.0 + 12.75 = 80.0 (would be High). With C1 at its pre-override level 5 the sum is 83.0.
- **Override: restriction_breach** — "(M5)" module code in §20 breaches the no-module-codes restriction (row 5.4). Per framework/brief: C1 reduced one level (5 → 4) and the total capped at the top of Moderate.
- **Total: 74/100 · Band: Moderate.**
- Hallucinated-source override: not triggered — three spot-checked sources are internally consistent and dated; no impossible URL/date/figure combination found.

## 4. Card Integrity

Linter rows (qa/regen_20260906_qa1/lint_static/2026-05-21.csv, verbatim):

| card_id | report_date | strategy | flags | dud |
|---|---|---|---|---|
| 2026-05-21_Trade_1 | 2026-05-21 | Trade 1 - Daily Directional | WARN_TP3_ORDER | False |
| 2026-05-21_Trade_2 | 2026-05-21 | Trade 2 - Pivot (TRANSITION breakout side) | CLEAN | False |
| 2026-05-21_Trade_3C | 2026-05-21 | Trade 3C - Range Breakout (conditional) | WARN_R_HUGE(3.54xATR)\|WARN_TARGET_FAR(5.42xATR) | False |

Per-card integrity (100 − 40·#DUD − 10·#WARN, floor 0):
- Trade 1: 0 DUD, 1 WARN → **90**
- Trade 2: 0 DUD, 0 WARN → **100**
- Trade 3C: 0 DUD, 2 WARN → **80**
- Suppressed cards: none (3 of 3 live). **Report mean = 90.0.** n_cards 3 · n_duds 0 · n_warns 3.

M5-rule assessment (feeds row 4.3, not the integrity number):
- Trade 1 — MARKET entry equals the report's D-1 close ✓ (7432.97; slice cash close 7436.80, Δ 3.83). Anchor is an overridden proxy (00:00 UK / 02:00 broker), not 07:00 UK — disclosed. Stop = 5-day swing low 7341.20 − 0.25×59.84 = 7326.24 ✓ arithmetic, but the rule is the TIGHTER of swing extreme and nearest S/R; nearest S/R below entry in the report's own levels is daily R1 7392.41 (or the 7360–7378 secondary support), which would give a tighter stop. TP1/TP2 = ±1R/±2R ✓; Unit 3 BE +0.2R ✓; runner cap 3×ATR = 7612.49 lies below TP2 7646.43 (WARN_TP3_ORDER). Wide-stop flag raised ✓. Invalidation separate (7328.01 daily S1 — stale-basis pivot). R = 106.73 = 1.42×ATR(slice cash) — inside [0.3, 3.0]×ATR.
- Trade 2 — TRANSITION → breakout side only ✓ (long, buy-stop above close). Entry formula is the TREND formula (P + 0.10×(R1−P)) applied to WEEKLY pivots; stop P − 0.8×(P−S1) weekly ✓; TPs R1/R1.5/R2 weekly ✓; BE +0.2R ✓; invalidation separate ✓; single-source monthly flag propagated ✓. Weekly inputs use L 7388.40 (15 May low only) whereas the slice week low is 7345.3 (12 May) — see §5. Static checks all pass.
- Trade 3C — Conditional close > 25-session boundary + 0.25×ATR ✓ form, but boundary taken as the 14 May CLOSE 7500.85 rather than the 25-session HIGH (report 7515.62; slice 7522.90). Stop = low + 0.40×width ✓ per rule, but the resulting R (290.7 pts = 3.54× full-day ATR / 3.87× cash ATR) breaches the static 3.0×ATR bound, and TP1 (+459.57) breaches the 2.5×ATR target bound. Unit-3 rule deviates (stop to 7500.85, below entry, instead of entry + 0.2R). TP3 null ✓ allowed. Invalidation (midpoint 7271.07) separate and above the stop ✓.

## 5. Data reconciliation log

Tolerances (brief §4): close |Δ| ≤ 3 pts consistent; open/high/low |Δ| ≤ 8 pts consistent; close wrong by >10 pts or non-reproducing RSI2 = Category 3 failure. Δ = report − slice (cash session).

| # | Section / field | Report value | Slice (cash) value | Δ | Verdict |
|---|---|---|---|---|---|
| 1 | §6 Thu 14 May Open | 7449.10 | 7463.9 | −14.8 | Discrepancy (>8) |
| 2 | §6 Thu 14 May High | 7515.62 | 7522.9 | −7.3 | Consistent (basis) |
| 3 | §6 Thu 14 May Low | 7447.80 | 7462.9 | −15.1 | Discrepancy (>8) |
| 4 | §6 Thu 14 May Close | 7500.85 | 7509.1 | −8.25 | Discrepancy (>3, <10) |
| 5 | §6 Fri 15 May Open | 7486.30 | 7442.3 | +44.0 | Discrepancy (>8, large) |
| 6 | §6 Fri 15 May High | 7491.05 | 7458.0 | +33.05 | Discrepancy (>8, large) |
| 7 | §6 Fri 15 May Low | 7388.40 | 7402.8 | −14.4 | Discrepancy (>8) |
| 8 | §6 Fri 15 May Close | 7408.50 | 7416.0 | −7.5 | Discrepancy (>3, <10) |
| 9 | §6 Mon 18 May Open | 7414.20 | 7423.0 | −8.8 | Discrepancy (marginal >8) |
| 10 | §6 Mon 18 May High | 7441.90 | 7438.5 | +3.4 | Consistent |
| 11 | §6 Mon 18 May Low | 7378.55 | 7358.0 | +20.55 | Discrepancy (>8) |
| 12 | §6 Mon 18 May Close | 7403.31 | 7411.0 | −7.69 | Discrepancy (>3, <10) |
| 13 | §6 Tue 19 May Open | 7398.05 | 7371.0 | +27.05 | Discrepancy (>8) |
| 14 | §6 Tue 19 May High | 7405.60 | 7399.8 | +5.8 | Consistent |
| 15 | §6 Tue 19 May Low | 7341.20 | 7339.1 | +2.1 | Consistent |
| 16 | §6 Tue 19 May Close | 7353.61 | 7362.3 | −8.69 | Discrepancy (>3, <10) |
| 17 | §6 Wed 20 May (D-1) Open | 7369.19 | 7379.9 | −10.71 | Discrepancy (>8) |
| 18 | §6 Wed 20 May (D-1) High | 7440.85 | 7443.0 | −2.15 | Consistent |
| 19 | §6 Wed 20 May (D-1) Low | 7360.10 | 7362.3 | −2.2 | Consistent |
| 20 | §6 Wed 20 May (D-1) Close (also §1/§3/§4/§21b entry) | 7432.97 | 7436.8 | −3.83 | Discrepancy (marginally >3; <10, not a failure). All five closes sit 3.8–8.7 below the CFD slice — a consistent basis offset |
| 21 | §6 RSI2 column vs slice RSI2 (helper) | 82.3 / 17.9 / 16.4 / 6.4 / 68.2 | 100.0 / 38.22 / 0.0 / 0.0 / 60.47 | — | Direction/shape agrees; levels differ (basis + method) |
| 22 | §6 RSI2 recomputed from the report's OWN closes (18/19/20 May) | 16.4 / 6.4 / 68.2 | 0.0 / 0.0 / 61.5 | +16.4 / +6.4 / +6.7 | FAIL — does not reproduce with the specified 2-period mean method (values look Wilder-smoothed); Category 3 failure per brief §4 |
| 23 | ATR(14) — §21b caveat "≈60 pts" (implied 59.84); not stated in §9 | ≈60 | 75.18 cash (82.07 full-day) | −15.3 | Discrepancy (−20%); previous day's report implied ≈78 |
| 24 | §11 daily pivot basis | "from Tue 19 May H/L/C" — P 7366.80 R1 7392.41 S1 7328.01 R2 7431.20 S2 7302.40 R3 7456.81 S3 7263.61 | D-1 must be Wed 20 May; from the report's own D-1 row: P 7411.31 R1 7462.51 S1 7381.76 R2 7492.06 S2 7330.56 R3 7543.26 S3 7301.01; slice cash D-1: P 7414.03 R1 7465.77 S1 7385.07 R2 7494.73 S2 7333.33 | P −44.5 vs own row | FAIL — wrong session; arithmetic on the 19 May inputs is exact, but the basis is stale by one session and propagates to §11 narrative, §15, §16, §17 (7,328), Trade 1 invalidation |
| 25 | §11 weekly pivots inputs | H 7515.62 / L 7388.40 / C 7408.50 → P 7437.51 R1 7486.61 S1 7359.39 | slice week 11–15 May cash H 7522.9 / L 7345.3 / C 7416.0 → P 7428.07 R1 7510.83 S1 7333.23 | L +43.1; P +9.4; R1 −24.2; S1 +26.2 | Discrepancy — weekly low appears to be the 15 May low only, not the week's low (12 May); Trade 2 entry/stop/TPs inherit this |
| 26 | §21b Trade 3C 25-session range | high 7500.85 / low 7041.28 / width 459.57 | slice cash H 7522.9 / L 7012.1 (width 510.8); close-based 7509.1 / 7042.1 | H −22.1 / L +29.2 (vs H/L); L −0.8 vs min close | Discrepancy — range defined on closes, not highs/lows; inconsistent with §8's swing high 7515.62 |
| 27 | Cross-report: §6 rows vs previous report (SP500_Daily_Report_20May2026.md) | 14 May O/H/L/C 7449.10/7515.62/7447.80/7500.85; 18 May 7414.20/7441.90/7378.55/7403.31; 19 May L 7341.20 | prior report: 14 May 7505.40/7517.12/7470.20/7488.95; 18 May 7402.80/7415.20/7385.50/7403.05; 19 May L 7349.50 | 14 May close +11.90; 14 May open −56.3; 18 May high +26.7 | Discrepancy — the same sessions are reported with different "CORROBORATED" values on consecutive days |
| 28 | §13c 15 May % change | −1.24% | from §6 closes: −1.23% | 0.01 pp | Minor rounding note |
| 29 | Direction score §21a/§20 | +0.30 | Σ = 0 + 0.20 + 0 + 0.041 + 0.018 + 0.045 = 0.304 | 0 | Reproduces |
| 30 | §13b tilt | +0.12 | +0.5/4.0 = 0.125 | 0 | Reproduces |
| 31 | Card arithmetic (Trade 1 R/TPs/BE, Trade 2 entry/stop/R/TPs, Trade 3C trigger/stop/TPs/midpoint) | as stated | recomputed from the report's inputs | ≤ 0.01 | Reproduces (given ATR ≈ 59.84) |
