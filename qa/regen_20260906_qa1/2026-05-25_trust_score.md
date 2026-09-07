# Trust Score — 2026-05-25 — SP500_Daily_Report_25May2026.md

Run: regen_20260906_qa1 · D = 2026-05-25 (US holiday; last completed session Fri 22 May) · D-1 slice: `data/slices/US500/US500_upto_2026-05-24.csv` (last bar 2026-05-22 23:45 broker) · Asset US500.
Helper: `engine/qa_slice_stats.py --date 2026-05-25 --closes 7403.21 7353.61 7432.97 7445.72 7473.47`.
Slice anchors (cash session 16:30–23:00 broker): D-1 O/H/L/C 7482.5 / 7509.2 / 7464.5 / 7475.7 · ATR14 75.35 · daily pivots from D-1 cash P 7483.13 R1 7501.77 S1 7457.07 R2 7527.83 S2 7438.43 · weekly (18–22 May) P 7441.33 R1 7543.57 S1 7373.47 · 5-day swing 7339.10 (19 May) → 7509.20 (22 May) · 25-day range 7050.7–7522.9.
Report anchors: D-1 (22 May) O/H/L/C 7449.80 / 7484.60 / 7446.90 / 7473.47 · RSI2 column 3.1 / 1.8 / 72.4 / 78.9 / 86.3 · ATR14 ≈ 72 · daily pivots (labelled "from 21 May") P 7445.14 R1 7468.98 S1 7421.88 R2 7492.24 S2 7398.04 · weekly (w/e 15 May) P 7436.30 · direction score +0.60 LONG · regime Trending–Bullish (TREND_UP) · anchor 07:00 UK · cards: Trade 1 MARKET LONG 7473.47 / SL 7403.30 / TP 7543.64–7613.81–7689; Trade 2 BUY STOP 7447.53 / SL 7426.43 / TP 7468.98–7480.61–7492.24; Trade 3A BUY LIMIT 7400.82 / SL 7320.90 / TP 7428.94–7484.60–7630.30.

## 1. Section 7 checklist

| Item | Reviewer notes | Evidence observed | Score 0–5 | Action required |
|---|---|---|---|---|
| 1.1 Variables respected | Asset = S&P 500 cash index (^GSPC), not ES; USD / index points; lookback 5 sessions 18–22 May; tz America/New_York; six sources across provider/aggregator/sell-side wrap tiers; Trade 1 anchored 07:00 UK. Gaps: counters listed VIX first in the header ("VIX · USDX · DAX 40") although §10 table puts USDX first; tick 0.01 not stated; as-of given as the report date (25 May) rather than the NY close of D-1, though the D-1 session is identified. | §2 table, header line 3, §4 (6 rows), §10, §21b Trade 1 entry, run note | 4 | Put USDX first in the counter list; state tick size; as-of = NY close 22 May |
| 1.2 Coverage & currency consistent | All price data dated 22 May or earlier; §13d forward items dated from D. Units consistent (points/USD). Drift: daily pivots built from the 21 May session rather than the last completed session (22 May) while the cards are for the 26 May session; weekly pivots from w/e 15 May instead of the just-completed week 18–22 May. | §11 column headers "Daily (from 21 May H/L/C)", "Weekly (from w/e 15 May)"; §21b card levels | 4 | Rebuild daily pivots from 22 May and weekly from 18–22 May |
| 1.3 Audience & tone | Senior US Equity Strategist voice, trading-and-risk-review framing, no retail tone; watch item and invalidation stated in analyst terms. | §1, §18 | 5 | — |
| 2.1 Sections present & ordered | §1–§21 all present in order; §13a–d and §21a–d present; §17 single sentence in its own block. | Headings 1–21, 13a/b/c/d, 21a/b/c/d | 5 | — |
| 2.2 Scorecard as a table | §6 is a table with Date/O/H/L/C/RSI2/Trend/Validation outcome but lacks the Source A / Source B / Final columns (corroboration pair only named in the footnote). §11 pivot table ordered R5→P→S5 for daily/weekly/monthly (superset of the R3→S3 requirement). | §6 table header row; §11 table | 4 | Add Source A / Source B / Final columns to §6 |
| 2.3 Method steps visible | §4 observations → §5 classification (core/directional) → weighted-median consensus; §8 candle-by-candle plus sequence assessment; §9 persistence (~0.91), overlap, range position, VOLator per counter, KER; §7 five chart captions present (pandoc dropped the images — captions accepted as evidence, noted). | §4–§9 | 5 | — |
| 3.1 Quantitative claims sourced | Price figures point to §4/§6; UMich 44.8 / 4.8%, FOMC minutes and Waller commentary are consistent with the §13a/§13c items. Unsourced numbers: 30-yr "5.19%", 10-yr "4.56%", "$725bn" hyperscaler capex "+77%", December hike "~40% priced", WTI "$96", "tech sector fell ~2.3%", persistence "~0.91", KER "+0.35". | §1, §8, §9, §12, §14 | 3 | Attach a source (or a §13a row) to each macro figure |
| 3.2 Citations exist & contain data | Spot-checks: (a) S&P Dow Jones via FRED 22 May close 7,473.47 — same figure in §1/§3/§4/§6/§18/§21b; (b) Motley Fool/Yahoo "+0.37% on day" — reproduces from §6 closes (7473.47/7445.72 − 1 = +0.373%); (c) CNBC wrap 20–22 May closes 7,432.97 / 7,445.72 — match §6 and §13c ("+1.08%" = 7432.97/7353.61 − 1 reproduces). No self-contradictory or impossible citation → no fabrication. Weaknesses: no URLs/locators; Reuters survey dated only "May"; Goldman cited second-hand "via wrap". | §4, §13a, §13c | 3 | Date the Reuters item; cite Goldman directly or mark as second-hand |
| 3.3 Calculations transparent | FAIL on RSI2: from the report's own closes the 2-period method in the brief gives 61.5 / 100.0 / 100.0 for 20–22 May; report shows 72.4 / 78.9 / 86.3 (two consecutive up closes cannot yield RSI2 < 100 under the stated method; values resemble a Wilder-smoothed series on a longer history, which is neither the stated method nor reproducible from the stated 15 May anchor). 18 May Trend label "Neutral" contradicts the rule (Close<Open and RSI2<50 → Bearish). §13b tilt formula omits the bearish media article: from the table Σ(w·s) = +0.70, Σw = 4.7, tilt = +0.15, not +0.30. §21a lists five contributions (0.25+0.20+0.045+0.045+0.06 = 0.60) but does not map them to the six weights, and a MIXED cross-asset read is scored +0.30 without explanation. Pivots do reproduce from the report's 21 May row (P = (7468.40+7421.30+7445.72)/3 = 7445.14, R1 7468.98, S1 7421.88, R2 7492.24, S2 7398.04, R3 7516.08, S3 7374.78); weekly/monthly tables reproduce internally. ATR(14) ≈ 72 and KER ≈ +0.35 stated. | §6 RSI2 column and footnote; §13b; §21a; §11 | 1 | Rebuild RSI2 from the stated closes with the stated method; correct the 18 May Trend label; recompute the tilt; show the six-weight mapping |
| 3.4 Numbers reconcile | Reconciles: D-1 close 7,473.47 identical in §1/§3/§4/§6/§21b; §11 pivots = card pivots; ATR 72 in §20/§21b; RSI2 §6 = §8 narrative = §21a input. Breaks: Trade 2 stop 7,426.43 vs its own formula 7,426.53 (R 21.0 not 21.1); §13b counts (2 Bearish incl. 1 media) vs formula (one bearish term); §21d "Trade 3 triggered 3/5" vs §21c table 4/5; "mean R ≈ +1.07" vs (1.2+1.0)/2 = 1.10; "every Trade 2 fill reached TP1" vs 19 May exit at P (+0.6R); "5+ (open)" days on trades opened 21/22 May. Against the slice: closes 18/19/20/21 May low by 7.8/8.7/3.8/4.6 pts (outside ±3, inside the 10-pt failure line); 21–22 May O/L/H off by 17–33 pts; daily P 38 pts below the slice D-1 P because the wrong session was used. Cross-report: the 22 May report's "21 May H/L/C" imply C 7,400.2, this report states 7,445.72 for the same session — revision not flagged. | §21b, §13b, §21c/d; §5 reconciliation log below | 2 | Fix the Trade 2 stop arithmetic and §21c/d counts; rebuild §6 O/H/L on a corroborated basis; note the 21 May revision |
| 4.1 Pillars conclude | §8 "Bullish continuation"; §9 "Trending — Bullish" + protocol; §10 "MIXED" with contradiction flag; §12 each item labelled supportive/negative/mixed; §14 per-paragraph labels. §21 as a pillar: Trade 2 is a BUY STOP at 7,447.53, 26 pts BELOW the D-1 close it quotes (7,473.47) — a buy stop cannot rest below market; both pivot-based cards rest on 21 May pivots for a 26 May session; Trade 1 stop uses the Thu low rather than the "tighter of" nearest S/R (Fri low 7,446.90). Trade 3A construction reproduces exactly (57.5%, 38.2%, 0%, 100% ext., stop = low − 0.25×ATR). | §8–§14 closing labels; §21b Trade 2 Entry row | 3 | Reconstruct Trade 2 on D-1 pivots with the entry above the D-1 close (see feedback) |
| 4.2 Peer/cross-asset interpreted | Each counter given a mechanism (dollar → financial conditions / translation; VIX → hedging demand / risk-on; DAX → common-factor read), status and implication; USDX contradiction carried to §15/§16 rather than resolved away. | §10 table and contradiction paragraph | 5 | — |
| 4.3 Synthesis reconciles tensions | §15 balances earnings/regime/VIX against PCE, Goldman/Reuters caution and USDX; §16 respects §9 and states invalidation (weekly pivot 7,436.30 / ~7,420); §18 single watch item; §20 states §17/§16 independent of §21; §21a notes no conflict with §17. Not addressed: the stretched/overbought read (RSI2 mid-80s, 92nd percentile) versus a market entry into the stated resistance band is only a card caveat, not reconciled in §16. | §15, §16, §18, §20, §21a | 4 | Reconcile the overbought read with the market-entry timing in §16 |
| 4.4 Calibrated language | §17 exactly one sentence with a single conditional ("provided the PCE print…"); confidence High stated in §3; "comfortably above threshold" for a +0.60 score is proportionate. "High" confidence sits uneasily with single-source O/H/L and unreproducible RSI2 inputs. | §3, §17, §21a | 4 | Qualify §3 confidence given indicative O/H/L |
| 5.1 Data dated; staleness flagged | Every price row dated; article dates in §13a (one "May" only); O/H/L single-source-indicative flagged in §6, §11, §19 and on every card; Stooq/Investing.com stale pages disclosed in §20. §13d events given as weekday ranges ("Wed–Thu", "Thu–Fri") rather than dates. | §6 footnote, §13a, §13d, §19, §20 | 4 | Date the Reuters item and the §13d rows |
| 5.2 Assumptions up front | 07:00 UK anchor and the post-holiday 26 May first-executable note stated in the run note, §20 and on the Trade 1 card; single-source pivot propagation to cards stated (§11, §19, §20, card caveats); weighted-median consensus described. Not surfaced: the choice to build daily pivots from 21 May instead of the last session, and the RSI2 method actually used. | Run note, §5, §11, §19, §20, §21b | 4 | State the pivot session and the RSI2 method explicitly |
| 5.3 Red flags surfaced | §12/§15 carry PCE, hawkish Fed, USDX, Iran/oil, Goldman/Reuters caution; §13d highest-impact event named. The PCE collision and the post-holiday gap risk (§13d) are not carried into any card caveat — cards mention only indicative pivots, resistance band and noise-exit risk. | §12, §13d, §15, §21b Caveats rows | 4 | Add the PCE/gap-risk collision to the card caveats |
| 5.4 Restrictions honoured | No synthesised price presented as sourced (O/H/L flagged indicative); no retail CFD quote in the OHLC basis; ES futures not used; no bracketed variable names, no M1..M5 codes, no framework name; instrument common names used. Minor leakage: internal identifiers "regime_label = TREND_UP", "cross_asset_confirm", "sentiment_tilt" in §20/§21 and "v2.1 baseline" version reference. Not a breach. | Whole report; §20 strategy trace; §21b | 4 | Replace internal identifiers with prose |

## 2. Category roll-up

| Category | Level | Multiplier | Points | Justification |
|---|---|---|---|---|
| C1 Prompt adherence (20) | 4 | 0.85 | 17.00 | Rows 4/4/5 → 4.33 → 4. Variables respected; counter order, tick size, as-of wording and stale pivot sessions are minor gaps. |
| C2 Structure (20) | 5 | 1.00 | 20.00 | Rows 5/4/5 → 4.67 → 5. All 21 sections and sub-sections present and ordered; §6 lacks the source columns. |
| C3 Accuracy & evidence (25) | 2 | 0.40 | 10.00 | Rows 3/3/1/2 → 2.25 → 2. RSI2 does not reproduce from the report's own closes (Category 3 failure per brief §4); tilt arithmetic wrong; four closes outside ±3 pts and D-1 O/H/L off 18–33 pts vs slice; several reconciliation breaks. No fabricated source. |
| C4 Reasoning & judgment (20) | 4 | 0.85 | 17.00 | Rows 3/5/4/4 → 4.0 → 4. Cross-asset mechanism and synthesis are strong; card construction (Trade 2 buy stop below market, stale pivot session) pulls 4.1 down. |
| C5 Currency & transparency (15) | 4 | 0.85 | 12.75 | Rows 4/4/4/4 → 4. Well dated and flagged; PCE/gap collision not on cards; pivot-session and RSI2-method choices not surfaced. |
| **Total** | | | **76.75 → 77** | |

## 3. Total, band, override check

- Total: **77/100** (17.00 + 20.00 + 10.00 + 17.00 + 12.75 = 76.75, rounded to 77).
- Band: **High** (75–89).
- Overrides: **none**. Three spot-checked citations are internally consistent and reproduce their own figures (no hallucinated-source override). No prompt restriction is openly breached — O/H/L are honestly flagged indicative rather than presented as sourced; no ES, no retail quotes, no module codes or framework name (internal identifier leakage in §20/§21 is noted under 5.4 but does not rise to a breach). Total stands at 77.

## 4. Card Integrity

Linter rows (`qa/regen_20260906_qa1/lint_static/2026-05-25.csv`, verbatim):

| card_id | report_date | strategy | flags | dud |
|---|---|---|---|---|
| 2026-05-25_Trade_1 | 2026-05-25 | Trade 1 - Daily Directional | CLEAN | False |
| 2026-05-25_Trade_2 | 2026-05-25 | Trade 2 - Pivot (TREND breakout, buy stop) | WARN_R_TINY(0.26xATR) | False |
| 2026-05-25_Trade_3A | 2026-05-25 | Trade 3A - Momentum-Pullback (57.5% fib) | CLEAN | False |

Per-card integrity (100 − 40·#DUD − 10·#WARN, floor 0):

| Card | #DUD | #WARN | Integrity |
|---|---|---|---|
| Trade 1 | 0 | 0 | 100 |
| Trade 2 | 0 | 1 | 90 |
| Trade 3A | 0 | 0 | 100 |

Report-level mean (3 non-suppressed cards, none suppressed): **96.7**. Totals: n_cards 3, n_duds 0, n_warns 1.

M5 assessment (feeds row 4.1, not the integrity number):
- Trade 1: MARKET at 07:00 UK anchor, entry = report D-1 close 7,473.47 (slice cash close 7,475.7, Δ −2.2, consistent). Stop 7,403.30 = Thu low 7,421.30 − 0.25×72; R 70.17 = 0.97×ATR(72) / 0.93×ATR(75.35), inside [0.3, 3.0]×ATR; TP1/TP2 = ±1R/±2R exact; TP3 3×ATR ≈ 7,689; Unit-3 stop entry+0.2R = 7,487.51; runner time-stop/3×ATR cap; invalidation (weekly pivot 7,436.30) separate from and above the stop; single-source flag propagated. Deviation: the stop rule is "tighter of (5-day swing extreme, nearest S/R)" — nearest S/R in the report's own §8 is the Fri low 7,446.90, which would give 7,428.90 / R 44.6; the Thu low was chosen without stating why. The Thu low used (7,421.30) is 27 pts above the slice's Thursday cash low 7,394.1, so the stop 7,403.30 sits 9 pts above that slice low. No PCE/gap caveat.
- Trade 2: TREND rule applied (entry P + 0.10×(R1−P) = 7,447.52; TPs R1/R1.5/R2 exact; stop formula 7,426.53 stated as 7,426.43). Defects: (i) entry mode written "Stop/limit" — ambiguous; the card JSON reads BUY STOP, and a buy stop at 7,447.53 sits 25.9 pts BELOW the report's own D-1 close (7,473.47) and 28.2 pts below the slice close (7,475.7) — wrong side for a STOP entry; (ii) pivots are from 21 May, not D-1 (22 May); on D-1 slice pivots the same rule gives entry 7,484.99 > close; (iii) R 21.1 = 0.28×ATR(75.35) — WARN_R_TINY, below the 0.3×ATR floor of 22.6 pts. Invalidation (daily close through P 7,445.14) is not separate from the stop (stop 7,426.43 is 19 pts below P and inside the same structure) but is at least distinct.
- Trade 3A: swing 7,338.90 → 7,484.60 endpoints logged, lookback 4 sessions, magnitude 145.7 = 2.02×ATR(72) — qualifies on the report's ATR but is 1.93×ATR on the slice ATR (75.35) and the slice swing is 7,339.1 → 7,509.2 (170.1 pts). Entry 57.5% = 7,400.82 exact; stop 7,338.90 − 18 = 7,320.90 exact; TP1 38.2% 7,428.94, TP2 0% 7,484.60, TP3 100% ext 7,630.30 exact; R 79.9 = 1.06×ATR; buy limit below D-1 close (correct side); invalidation (close below 7,338.90) separate from and above the stop; single-source flag propagated; runner override stated. Clean.

## 5. Data reconciliation log

Tolerances (brief §4): |Δ| ≤ 3 pts on a close, ≤ 8 pts on O/H/L = consistent; larger = discrepancy; close > 10 pts or non-reproducing RSI2 = Category 3 failure. Slice values are cash-session (16:30–23:00 broker).

| Section | Field | Report | Slice / recomputed | Δ (report − slice) | Verdict |
|---|---|---|---|---|---|
| §6 | 18 May Open | 7,404.20 | 7,423.0 | −18.8 | Discrepancy (open) |
| §6 | 18 May High | 7,421.50 | 7,438.5 | −17.0 | Discrepancy |
| §6 | 18 May Low | 7,360.10 | 7,358.0 | +2.1 | Consistent |
| §6 | 18 May Close | 7,403.21 | 7,411.0 | −7.8 | Discrepancy (close > 3, < 10) |
| §6 | 19 May Open | 7,398.30 | 7,371.0 | +27.3 | Discrepancy |
| §6 | 19 May High | 7,404.60 | 7,399.8 | +4.8 | Consistent |
| §6 | 19 May Low | 7,338.90 | 7,339.1 | −0.2 | Consistent |
| §6 | 19 May Close | 7,353.61 | 7,362.3 | −8.7 | Discrepancy (close > 3, < 10) |
| §6 | 20 May Open | 7,361.40 | 7,379.9 | −18.5 | Discrepancy |
| §6 | 20 May High | 7,445.20 | 7,443.0 | +2.2 | Consistent |
| §6 | 20 May Low | 7,355.80 | 7,362.3 | −6.5 | Consistent |
| §6 | 20 May Close | 7,432.97 | 7,436.8 | −3.8 | Discrepancy (marginal) |
| §6 | 21 May Open | 7,441.10 | 7,408.6 | +32.5 | Discrepancy |
| §6 | 21 May High | 7,468.40 | 7,471.8 | −3.4 | Consistent |
| §6 | 21 May Low | 7,421.30 | 7,394.1 | +27.2 | Discrepancy (feeds Trade 1 stop and daily S1) |
| §6 | 21 May Close | 7,445.72 | 7,450.3 | −4.6 | Discrepancy (marginal) |
| §6 | 22 May (D-1) Open | 7,449.80 | 7,482.5 | −32.7 | Discrepancy |
| §6 | 22 May (D-1) High | 7,484.60 | 7,509.2 | −24.6 | Discrepancy (feeds "streak high", Trade 3A 0% anchor, R1 narrative) |
| §6 | 22 May (D-1) Low | 7,446.90 | 7,464.5 | −17.6 | Discrepancy |
| §6 | 22 May (D-1) Close | 7,473.47 | 7,475.7 | −2.2 | Consistent |
| §6 footnote | 15 May reference close | 7,408.40 | 7,416.0 | −7.6 | Discrepancy |
| §6 | RSI2 18 May | 3.1 | slice 0.00; own closes n/a | — | Not reproducible from stated anchor (direction consistent) |
| §6 | RSI2 19 May | 1.8 | slice 0.00; own closes n/a | — | Not reproducible (direction consistent) |
| §6 | RSI2 20 May | 72.4 | slice 60.47; own closes 61.5 | +10.9 | FAIL — does not reproduce |
| §6 | RSI2 21 May | 78.9 | slice 100.00; own closes 100.0 | −21.1 | FAIL — two up closes must give 100 |
| §6 | RSI2 22 May | 86.3 | slice 100.00; own closes 100.0 | −13.7 | FAIL — does not reproduce |
| §6 | Trend 18 May | Neutral | rule: C 7,403.21 < O 7,404.20 and RSI2 3.1 < 50 → Bearish | — | Label error |
| §9 / §20 | ATR(14) | ≈ 72 | 75.35 (cash) / 82.19 (full day) | −3.4 | Consistent |
| §9 | 25-session range percentile | ~92nd | 90.0% (7,475.7 in 7,050.7–7,522.9) | — | Consistent |
| §9 / §10 | VIX close 21 May | 16.76 | 17.91 | −1.15 | Basis (spot vs CFD) plausible; recorded |
| §9 / §10 | VIX close 22 May | 16.70 | 18.16 | −1.46 | As above; 5-day direction "falling" consistent (18.67 → 18.16) although the slice rose on 22 May |
| §9 / §12 / §14 | USDX | ~99.3 | 99.344 close, 99.45 high | ≈ 0 | Consistent |
| §12 / §13c | UMich sentiment / 1-yr expectations | 44.8 / 4.8% | 44.8 / 4.8 (calendar slice) | 0 | Consistent |
| §13c / §14 | FOMC minutes 20 May; Waller 19 & 22 May; Memorial Day 25 May | as stated | present in calendar slice | — | Consistent |
| §1 | "eighth consecutive weekly advance" | 8 | 7 consecutive up-weeks visible inside the slice window (10 Apr → 22 May) | — | Not contradicted; earlier weeks outside slice |
| §11 | Daily P | 7,445.14 (from 21 May) | D-1 cash P 7,483.13; from report's own 22 May H/L/C 7,468.32 | −38.0 / −23.2 | Discrepancy — wrong session used for the D pivots |
| §11 | Daily R1 / S1 | 7,468.98 / 7,421.88 | 7,501.77 / 7,457.07 | −32.8 / −35.2 | Discrepancy (same cause) |
| §11 | Daily pivots vs report's own 21 May row | P 7,445.14 R1 7,468.98 S1 7,421.88 R2 7,492.24 S2 7,398.04 R3 7,516.08 S3 7,374.78 | identical | 0 | Reproduce (from 21 May H/L/C) |
| §11 | Weekly P | 7,436.30 (w/e 15 May) | prior-week (18–22 May) P 7,441.33 | −5.0 | Wrong week (should be 18–22 May); numerically near |
| §11 | Weekly implied H/L/C (w/e 15 May) | 7,512.1 / 7,388.4 / 7,408.4 | 7,522.9 / 7,345.3 / 7,416.0 | −10.8 / +43.1 / −7.6 | Discrepancy on the weekly low |
| §11 | Monthly (April) implied H/L/C | 7,245.6 / 6,534.55 / 7,180.4 (from P 6,986.85, R1 7,439.15, S1 6,728.10) | 7,226.7 / 6,471.7 / 7,213.7 | +18.9 / +62.9 / −33.3 | Discrepancy (secondary; monthly levels far from market) |
| §13b | Sentiment tilt | +0.30 (Σw·s = 1.20, Σw = 4.2) | from the §13a table: Σw·s = +0.70, Σw = 4.7 → +0.15 | +0.15 | Arithmetic error (bearish media article omitted) |
| §21a | Direction score | +0.60 | 0.25+0.20+0.045+0.045+0.06 = 0.60; with tilt +0.15 → ≈ +0.58 | — | Sums; still LONG; weight mapping incomplete |
| §21b Trade 2 | Stop | 7,426.43 | P − 0.8×(P−S1) = 7,445.14 − 18.61 = 7,426.53 | −0.10 | Arithmetic slip (R 21.0 not 21.1) |
| §21b Trade 2 | Entry side | BUY STOP 7,447.53 | D-1 close 7,473.47 (report) / 7,475.7 (slice) | −25.9 / −28.2 | Wrong side for a buy stop |
| §21b Trade 3A | Swing magnitude / ATR | 145.7 = 2.02×ATR(72) | 145.7/75.35 = 1.93×; slice swing 170.1 = 2.26× | — | Qualifies only on the report's ATR |
| §21c / §21d | Trade 3 trigger count; mean R; Trade 2 TP1 rate; days open | 3/5; +1.07; 100%; "5+" | table: 4/5; (1.2+1.0)/2 = 1.10; 19 May exit at P (+0.6R); opened 21/22 May | — | Internal inconsistencies |
| Cross-report | 21 May H/L/C | 7,468.40 / 7,421.30 / 7,445.72 | 22 May report's daily pivots (P 7,412.4, R1 7,436.5, S1 7,376.1) imply 7,448.7 / 7,388.3 / 7,400.2 | +19.7 / +33.0 / +45.5 | Inconsistent between reports; this report is nearer the slice (C 7,450.3); revision unflagged |
