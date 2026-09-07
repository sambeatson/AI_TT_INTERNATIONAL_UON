# Trust Score — 2026-05-22 — SP500_Report_22May2026.md

Run: regen_20260906_qa1 · D = 2026-05-22 · D-1 slice = `data/slices/US500/US500_upto_2026-05-21.csv` (cash session 16:30–23:00 broker). Helper run with the report's §6 closes (7396.80, 7358.60, 7353.61, 7432.97, 7400.30). Slice reference values used below: D-1 cash O/H/L/C 7408.6 / 7471.8 / 7394.1 / 7450.3; ATR14 76.24 (cash) / 83.79 (full-day); daily pivots (cash) P 7438.73 R1 7483.37 S1 7405.67 R2 7516.43 S2 7361.03; 5-day swing 7471.80 / 7339.10; 25-day swing 7522.90 / 7050.70.

## 1. Section 7 checklist

| Item | Reviewer notes | Evidence observed | Score 0–5 | Action required |
|---|---|---|---|---|
| 1.1 Variables respected | Asset is the cash index, counters USDX·VIX·DAX 40 in the required order, as-of 21 May NY close, 5-session lookback, USD / index points / tick 0.01, six §4 observations. The daily-open anchor is stated as **00:00 UK**, not the 07:00 UK M1 setting; the report itself acknowledges this as a deviation read against ES as a proxy. | §2 table and italic note ("anchor has been set to 00:00 UK ... standing configuration ... 07:00 UK"); §5 header line; §4 six rows | 3 | Restore the 07:00 UK anchor (09:00 broker); remove the ES-proxy reading of the anchor. |
| 1.2 Coverage & currency consistent | All price/article dates are 14–21 May (≤ D-1); session date is 22 May. Units are index points / USD throughout, no drift. Reuters survey row dated only "May"; §13d rows are undated ("Within horizon", "Ongoing"). | §2, §4, §6, §13a–d, §21c | 4 | Date the Reuters survey and the §13d rows. |
| 1.3 Audience & tone | Senior US Equity Strategist, trading-and-risk-review framing; institutional tone, no retail language. The "Contents" heading is empty. | §1 byline, §18 | 5 | None (optional: populate or remove the empty "Contents" heading). |
| 2.1 Sections present & ordered | All 21 headings appear in order, but **§13b Aggregate Sentiment Summary is an empty heading** (the counts and −0.19 tilt live only in §20) and **§21a Directional Conviction is an empty heading** (score and contributions live only in §1 and §20). §7 carries five chart placeholders with captions. | Lines "13b Aggregate Sentiment Summary" → immediately "13c"; "21a Directional Conviction" → immediately "21b" | 2 | Populate §13b (counts, weighted tilt, confidence) and §21a (score table with signal × weight rows). |
| 2.2 Scorecard as a table | §6 is a table with Date/O/H/L/C/RSI2/Trend/Validation but **lacks the Source A / Source B / Final columns**; the pairing is described only in a footnote. §11 daily/weekly/monthly tables are ordered R5→P→S5 (3+ levels each side) as required. | §6 header row; §11 three tables | 3 | Add Source A, Source B and Final columns per row to §6. |
| 2.3 Method steps visible | §4 observations → §5 weighted-median consensus; §8 candle-by-candle with close-in-range % and sequence assessment; §9 regime with overlap 0.47, persistence 0.50, range position, VOLator slope. Charts are placeholders (pandoc-dropped images with captions) — accepted, noted. | §4, §5, §8, §9, §7.1–7.5 | 4 | None beyond restoring chart images if the pipeline allows. |
| 3.1 Quantitative claims sourced | §1 cites the 14 May record 7,501.24 / 7,517.12 with no §4 row or source; §13c "WTI fell ~5.7%" and "yields ~1-yr high" unsourced; §14 "VIX in the high-teens" unsourced. The §1 close (7,400) and 20 May close (7,432.97) do point to §4/§6. | §1 para 1, §13c rows 1–2, §14 Positioning | 2 | Give every number in §1/§12/§13c/§14 a source row or a §4/§6/§13 pointer. |
| 3.2 Citations exist & contain data | Spot-check 1 — CNBC 20 May "7,432.97 (+1.08%)": consistent with §6 and §13c. Spot-check 2 — Trading Economics 21 May "~7,400 (−0.44%)": arithmetic consistent (7,432.97 × 0.9956 = 7,400.26) but labelled "CFD proxy" while used as a "Core" close corroborator, contradicting the §4 exclusion note. Spot-check 3 — §13a row 6 cites `cnbc.com/quotes/.SPX` (a quote page, not an article) as the source of a dated headline "A market correction may be looming" — self-contradictory citation. Also: **no source in §4 states the D-1 close at the 7,400.30 precision used in §6**; every 21 May observation is "~7,400" or an intraday band. Not treated as a fabricated source (cannot fetch), but the D-1 close is not evidenced at its stated precision. | §4 rows 2, 4; §13a rows 1, 6; §6 row 5 | 1 | Cite a source that states the 21 May close to 0.01; replace the quotes-page URL with an article URL; do not label a CFD proxy as a core close-basis corroborator. |
| 3.3 Calculations transparent | RSI2 reproduces exactly from the report's own closes (helper: 0.0, 94.1, 70.8 for 19/20/21 May); Trend labels follow the rule (21 May Close<Open with RSI2 70.8 → Neutral). Daily pivots reproduce from the report's own 21 May H/L/C (P 7412.37, R1 7436.53, S1 7376.13, R2 7472.77, S2 7351.97, R3 7496.93, S3 7315.73). Weekly and monthly tables are internally consistent. **ATR(14) is never stated** — it is only implied (§21b: "0.25×ATR ≈ 22 points" ⇒ ATR ≈ 88). KER value stated (+0.20) but not its parameters. §21a per-signal contributions (−0.25, −0.10, +0.05, +0.15, −0.03, −0.05) sum to **−0.23**, not the stated −0.22. | §6 footnote; §11; §20 "Strategy module trace"; §21b Trade 3C | 2 | State ATR(14) in §9 and §21; state KER parameters; correct the direction-score sum. |
| 3.4 Numbers reconcile | Internally: D-1 close 7,400 (§1/§3/§4) vs 7,400.30 (§6) — rounding only; §11 pivots = card pivots (7,412 / 7,437); RSI2 §6 = §8; median RSI2 31.9 correct. Against the slice: **21 May close 7,400.30 vs cash 7,450.3 (Δ −50.0)**, **18 May close 7,358.60 vs 7,411.0 (Δ −52.4)**, 15 May close 7,396.80 vs 7,416.0 (Δ −19.2) — three closes wrong by > 10 pts (brief §4: Category 3 failure). The report's RSI2 column (31.9/0/0/94.1/70.8) therefore does not match the slice's (38.2/0/0/60.5/100.0). Trade 2 card labels TP1 as "+1R, +60 points" but 7,437 − 7,415 = +22 pts (0.37R); TP2 "+2R, +120" but 7,475 − 7,415 = +60 (1.0R). | §6 rows 1, 2, 5; helper output; §21b Trade 2 TP rows | 0 | Rebuild §6 from a source that matches the cash session (see §5 log); recompute RSI2, pivots and cards from the corrected closes; fix the R-multiple labels on Trade 2. |
| 4.1 Pillars conclude | §8 ends in "Indecision — reversal risk"; §9 ends in "Transitional" with a preferred protocol; §10 has per-counter status but no overall direction label; §12 gives per-factor labels but no closing direction; §14 closes with a watch item rather than a direction label. | §8 box, §9 box, §10 table, §12, §14 box | 3 | Add a one-line direction conclusion to §10, §12 and §14. |
| 4.2 Peer/cross-asset interpreted | §10 gives a mechanism per counter (financial conditions, risk premium, common global-risk factor). However the VIX row says "Rising / re-expanding" and §14 says "rising slope": the VIX slice cash closes over the five sessions are 19.06 → 18.62 → 18.80 → 18.40 → 17.86 (falling, −1.20). USDX "flat / mild up" is consistent (98.87 → 99.20). DAX not verifiable here. | §10 VIX row, §7.4, §9 VOLator text, §14 Positioning; VIX slice | 3 | Re-state the VIX 5-day direction from the data; re-check the cross-asset contribution sign in §21a. |
| 4.3 Synthesis reconciles tensions | KER (+0.20, Trending Up) vs Transitional regime is explicitly reconciled in §9 and §20; §17 (lower half of 7,351–7,440) is consistent with score −0.22 and §16. Card construction (scored here per brief §3): Trade 2 is built under a TRANSITION label using the **TREND entry formula** P + 0.10×(R1−P) with a structural stop rather than the TREND stop P − 0.8×(P−S1) = 7,383.4, and its TP ladder is labelled with wrong R-multiples; Trade 3C follows the 3C formula (stop = low + 0.40×width, TP1 = +1.0×width, TP2 = 1.5×) but yields R = 346 pts = 4.13×ATR14 and TP1 518 pts away (linter WARN_R_HUGE, WARN_TARGET_FAR). On the slice basis the Trade 2 buy stop (7,415) sits **below** the D-1 cash close 7,450.3. | §9 Kaufman box; §16–§18; §21b both cards; lint row 3 | 2 | See feedback file: rebuild Trade 2 on the correct D-1 close and one consistent rule set; bring 3C risk inside 3.0×ATR14 or state the exception explicitly. |
| 4.4 Calibrated language | §17 is exactly one sentence, no hedge stacking; §3 confidence Medium with reason; §1 states the mixed KER signal plainly. | §17 box, §3 | 5 | None. |
| 5.1 Data dated; staleness flagged | Every §4/§6 price dated; single-source O/H/L flagged in §5, §6, §11, §19, §20 and carried on the cards. Reuters survey undated; §13d rows undated. §19 states that the CSV endpoints were unreachable (data gap disclosed). | §6 Validation column; §11 source-status lines; §19; §13a row 4 | 4 | Date the Reuters row and the §13d events. |
| 5.2 Assumptions up front | Anchor override (00:00 UK vs 07:00 UK, ES proxy) stated in §2 and §20; single-source pivot propagation stated on Trade 2 caveats. Trade 2 card carries no anchor/time-of-validity field; the anchor-override caveat is not on any card (Trade 1 suppressed). | §2 note; §20 "Strategy module trace"; §21b Trade 2 Caveats | 3 | Put the anchor and the anchor-override caveat on each live card. |
| 5.3 Red flags surfaced | §12 near-term catalysts, §15 two-sided table, §13d core PCE flagged High and carried as an event-collision flag on both live cards. | §12, §15, §13d, §21b Caveats rows | 5 | None. |
| 5.4 Restrictions honoured | (a) A close of **7,400.30** is presented as "corroborated" in §6 although every 21 May source in §4 is "~7,400" / an intraday band — a synthesised precision presented as sourced. (b) Trading Economics is labelled "CFD proxy" and used as a **Core** close-basis corroborator, contradicting the report's own exclusion of CFD quotes from the OHLC basis. (c) Internal configuration language leaks into the report: "Master switch ON", "weights at the v2.1 baseline", "Weight-lock ... first 20 sessions". (d) Anchor moved to 00:00 UK. ES futures kept confirmation-only (compliant); no bracketed variable names, no M1..M5 codes, no framework name. | §4 row 4 and exclusion note; §6 row 5 and footnote; §20 Strategy module trace; §2 note | 1 | Remove synthesised precision or source it; drop CFD proxies from the close basis; strip configuration/version language from §20; restore the 07:00 UK anchor. |

## 2. Category roll-up

| Category | Level | Multiplier | Points | Justification |
|---|---|---|---|---|
| C1 Prompt adherence (max 20) | 3 | 0.65 | 13.00 | Rows 1.1–1.3 = 3, 4, 5 → mean 4.0 → level 4; **reduced one level to 3 by the restriction-breach override** (5.4). |
| C2 Structure (max 20) | 3 | 0.65 | 13.00 | Rows 2.1–2.3 = 2, 3, 4 → mean 3.0 → level 3. Empty §13b and §21a; §6 missing source columns. |
| C3 Accuracy & evidence (max 25) | 1 | 0.20 | 5.00 | Rows 3.1–3.4 = 2, 1, 2, 0 → mean 1.25 → level 1. D-1 close off by 50 pts and 18 May close off by 52 pts versus the cash session; D-1 close not sourced at its stated precision; ATR unstated. |
| C4 Reasoning & judgment (max 20) | 3 | 0.65 | 13.00 | Rows 4.1–4.4 = 3, 3, 2, 5 → mean 3.25 → level 3. Good KER/regime reconciliation and calibrated forecast; card construction mixes rule sets and mislabels R-multiples; VIX direction misread. |
| C5 Currency, restrictions & transparency (max 15) | 3 | 0.65 | 9.75 | Rows 5.1–5.4 = 4, 3, 5, 1 → mean 3.25 → level 3. Strong dating and red-flag discipline; restriction breaches in 5.4. |
| **Total** | | | **53.75 → 54** | |

## 3. Total, band, override check

- **Total: 54/100** (53.75 rounded).
- **Band: Low** (40–59).
- **Overrides:** `restriction_breach` — applied. Grounds: a synthesised D-1 close (7,400.30) presented as a corroborated, sourced value when no §4 observation states it at that precision (all 21 May quotes are "~7,400" or an intraday band); a CFD-proxy quote (Trading Economics, §4 row 4) used as a Core corroborator in the cash close basis despite the report's own exclusion rule; internal configuration/version language in §20. Effect: C1 reduced from level 4 to level 3 (−4 points); the Moderate cap (≤ 74) is not binding because the total is already below 60. Without the override the total would have been 58 (still Low).
- `hallucinated_source` — **not applied**. The `cnbc.com/quotes/.SPX` citation in §13a is self-contradictory (a quote page cited as a dated article) and the Reuters survey is undated, but neither can be shown impossible without fetching; they are scored down in 3.2 rather than treated as fabricated. If a later fetch shows the quote-page article does not exist, C3 goes to 0 and the band caps at Low (no change to the band).

## 4. Card Integrity

Linter rows (`qa/regen_20260906_qa1/lint_static/2026-05-22.csv`), verbatim:

| card_id | report_date | strategy | flags | dud |
|---|---|---|---|---|
| 2026-05-22_Trade_1 | 2026-05-22 | Trade 1 - Daily Directional | SUPPRESSED | False |
| 2026-05-22_Trade_2 | 2026-05-22 | Trade 2 - Pivot (TRANSITION breakout side) | CLEAN | False |
| 2026-05-22_Trade_3C | 2026-05-22 | Trade 3C - Momentum-Breakout (conditional) | WARN_R_HUGE(4.13xATR)\|WARN_TARGET_FAR(6.18xATR) | False |

Per-card integrity (100 − 40·#DUD − 10·#WARN, floor 0):

| Card | #DUD | #WARN | Integrity | Note |
|---|---|---|---|---|
| Trade 1 | 0 | 0 | — (suppressed, excluded from the mean) | Suppression is a compliant output: stated score −0.22 (|score| < 0.25). Note the §20 contributions sum to −0.23; either value suppresses. |
| Trade 2 | 0 | 0 | 100 | Linter CLEAN on the card's own numbers. Protocol assessment (row 4.3): entry formula and stop drawn from different rule sets; TP1/TP2 R-labels wrong; buy stop 7,415 is below the slice D-1 cash close 7,450.3. |
| Trade 3C | 0 | 2 | 80 | R = 346 pts = 4.13×ATR14 (limit 3.0×); TP1 518 pts from entry = 6.18×ATR14 (limit 2.5×). Formula-faithful to the 3C rule but outside the static integrity bounds. |

**Report-level Card Integrity (mean over non-suppressed cards): (100 + 80) / 2 = 90.0.**  n_cards = 3 (incl. suppressed), n_duds = 0, n_warns = 2.

## 5. Data reconciliation log

Slice values are the cash session (16:30–23:00 broker) from the helper unless marked "full-day". Tolerances (brief §4): close |Δ| ≤ 3 consistent; open/high/low |Δ| ≤ 8 consistent; close |Δ| > 10 = Category 3 failure.

| # | Section / field | Report value | Slice value | Δ (report − slice) | Verdict |
|---|---|---|---|---|---|
| 1 | §6 Fri 15 May Open | 7,488.30 | 7,442.3 (full-day 7,505.5) | +46.0 | Discrepancy (matches full-day/overnight open, not cash open) |
| 2 | §6 Fri 15 May High | 7,501.10 | 7,458.0 (full-day 7,510.5) | +43.1 | Discrepancy |
| 3 | §6 Fri 15 May Low | 7,388.40 | 7,402.8 | −14.4 | Discrepancy |
| 4 | §6 Fri 15 May Close | 7,396.80 | 7,416.0 (full-day 7,400.8) | −19.2 | **Failure (close > 10 pts)** |
| 5 | §6 Mon 18 May Open | 7,402.10 | 7,423.0 | −20.9 | Discrepancy |
| 6 | §6 Mon 18 May High | 7,430.50 | 7,438.5 | −8.0 | Consistent (at tolerance) |
| 7 | §6 Mon 18 May Low | 7,351.20 | 7,358.0 | −6.8 | Consistent |
| 8 | §6 Mon 18 May Close | 7,358.60 | 7,411.0 (full-day 7,405.2) | −52.4 | **Failure (close > 10 pts)** |
| 9 | §6 Tue 19 May Open | 7,361.40 | 7,371.0 | −9.6 | Discrepancy |
| 10 | §6 Tue 19 May High | 7,372.90 | 7,399.8 | −26.9 | Discrepancy |
| 11 | §6 Tue 19 May Low | 7,300.80 | 7,339.1 | −38.3 | Discrepancy (also drives the wrong "7,300 five-day low" in §8/§15/§16) |
| 12 | §6 Tue 19 May Close | 7,353.61 | 7,362.3 (full-day 7,356.3) | −8.7 | Discrepancy (consistent with full-day close, Δ −2.7) |
| 13 | §6 Wed 20 May Open | 7,372.50 | 7,379.9 | −7.4 | Consistent |
| 14 | §6 Wed 20 May High | 7,441.20 | 7,443.0 | −1.8 | Consistent |
| 15 | §6 Wed 20 May Low | 7,360.10 | 7,362.3 | −2.2 | Consistent |
| 16 | §6 Wed 20 May Close | 7,432.97 | 7,436.8 | −3.8 | Marginal (just outside the 3-pt close tolerance; basis-consistent) |
| 17 | §6 Thu 21 May (D-1) Open | 7,430.80 | 7,408.6 | +22.2 | Discrepancy |
| 18 | §6 Thu 21 May (D-1) High | 7,448.60 | 7,471.8 | −23.2 | Discrepancy |
| 19 | §6 Thu 21 May (D-1) Low | 7,388.20 | 7,394.1 | −5.9 | Consistent |
| 20 | §6 / §1 / §3 / §4 Thu 21 May (D-1) Close | 7,400.30 (7,400) | 7,450.3 (full-day 7,452.3) | −50.0 | **Failure (D-1 close > 10 pts; anchors every pivot and card)** |
| 21 | §6 RSI2 column vs slice closes | 31.9 / 0.0 / 0.0 / 94.1 / 70.8 | 38.22 / 0.00 / 0.00 / 60.47 / 100.00 | −6.3 / 0 / 0 / +33.6 / −29.2 | Fails on 20 and 21 May (input closes wrong) |
| 22 | §6 RSI2 column vs report's own closes | 0.0 / 94.1 / 70.8 (19–21 May) | helper recompute 0.0 / 94.1 / 70.8 | 0 | Arithmetic reproduces exactly |
| 23 | §11 daily pivots vs report's own D-1 H/L/C | P 7,412.4 R1 7,436.5 S1 7,376.1 R2 7,472.8 S2 7,352.0 R3 7,496.9 S3 7,315.7 | recomputed 7,412.37 / 7,436.53 / 7,376.13 / 7,472.77 / 7,351.97 / 7,496.93 / 7,315.73 | ≤ 0.05 | Reproduce |
| 24 | §11 daily P / R1 / S1 vs slice cash pivots | 7,412.4 / 7,436.5 / 7,376.1 | 7,438.73 / 7,483.37 / 7,405.67 | −26.3 / −46.9 / −29.6 | Discrepancy (inherited from wrong D-1 H/C) |
| 25 | §11 weekly P / R1 / S1 vs slice | 7,434.1 / 7,479.8 / 7,351.1 | 7,428.07 / 7,510.83 / 7,333.23 | +6.0 / −31.0 / +17.9 | P consistent; R1/S1 discrepant (report uses 15 May low 7,388.4 and close 7,396.8) |
| 26 | ATR(14) | not stated; implied ≈ 88 (§21b "0.25×ATR ≈ 22") | 76.24 cash / 83.79 full-day | ≈ +12 / +4 | Not stated (3.3); implied value near full-day ATR |
| 27 | §8 support "7,300.80 (19 May low)" / resistance "7,501.10 (15 May high)" | 7,300.80 / 7,501.10 | 5-day swing low 7,339.10 (19 May) / high 7,471.80 (21 May) | −38.3 / +29.3 | Discrepancy; the 5-day high is 21 May on the slice, not 15 May |
| 28 | §21b Trade 3C 25-session range | high 7,517 / low ≈ 6,977 / width ≈ 540 | 7,522.9 / 7,050.7 / 472.2 | −5.9 / −73.7 / +67.8 | High consistent; low and width discrepant |
| 29 | §10 / §14 VIX 5-day direction | "Rising / re-expanding", "rising slope" | VIX cash closes 19.06 → 18.62 → 18.80 → 18.40 → 17.86 | −1.20 over 5 sessions | Direction contradicted; level "high-teens" consistent |
| 30 | §10 USDX 5-day direction | "Flat / mild up" | 98.87 → 99.20 | +0.33 | Consistent |
| 31 | §20 direction score | −0.22 | sum of stated contributions −0.23 | 0.01 | Minor arithmetic error; suppression decision unchanged |
| 32 | §21b Trade 2 TP1 / TP2 labels | "+1R, +60 pts" at 7,437; "+2R, +120 pts" at 7,475 | 7,437 − 7,415 = +22 (0.37R); 7,475 − 7,415 = +60 (1.0R) | −38 / −60 | Card labels do not reconcile with the levels |
| 33 | Cross-report (SP500_Report_21May2026.md §6) 19 May O/H/L and RSI2; 20 May RSI2 | this report 7,361.40 / 7,372.90 / 7,300.80, RSI2 0.0; 20 May RSI2 94.1 | prior report 7,398.05 / 7,405.60 / 7,341.20, RSI2 6.4; 20 May RSI2 68.2 | O/H/L −37/−33/−40 | Consecutive reports disagree on the same sessions |
