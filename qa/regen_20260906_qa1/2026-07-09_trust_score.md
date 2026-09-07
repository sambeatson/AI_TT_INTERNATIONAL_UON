# Trust Score — 2026-07-09 — SP500_Daily_Report_09Jul2026.md

Run: regen_20260906_qa1 · Asset: US500 · D = 2026-07-09 · D-1 slice = 2026-07-08
Basis for Category 3: `data/slices/US500/US500_upto_2026-07-08.csv` via `engine/qa_slice_stats.py`
(cash session 16:30–23:00 broker = 09:30–16:00 ET). Tolerance per brief §4: |Δ| ≤ 3 pts on a close,
≤ 8 pts on an open/high/low.

## 1. Section 7 checklist

| Item | Reviewer notes | Evidence observed | Score 0–5 | Action required |
|---|---|---|---|---|
| 1.1 Variables respected | Asset correctly the S&P 500 cash index (503 constituents, 09:30–16:00 ET, pre/after-market excluded). Counters USDX · VIX · DAX 40 with USDX first. Units index points/USD, tick 0.01, lookback 5 sessions — all as required. Six sources in §4 (index provider, two media wraps, two aggregators, one macro-data site). Two deviations: the 07:00 UK daily-open anchor is explicitly overridden ("anchored to the 9 July session per the run instruction rather than the standing 07:00 UK European pre-open convention"), and although the as-of is declared as D-1 (8 Jul), the operative basis for §3, §11 and §18 is the 7 Jul (D-2) session because the 8 Jul row is self-declared single-source. | §2 table; masthead line 3; §3 Note; §4 six rows; §19; §20 | 2 | Restore the 07:00 UK anchor or justify the override on the card itself; build §11 and the §3 consensus on the D-1 (8 Jul) session. |
| 1.2 Coverage & currency consistent | All data dates are D-1 or earlier and the session is D; no currency or unit drift (native index points throughout, §5 states no conversion needed). Two dating/coverage errors: §13c gives the trade-deficit prior as $54.6bn where the calendar previous is $55.881bn; §13d dates a CPI print at "~9–10 Jul" and makes it the highest-impact event, but no US CPI appears on the 9 Jul calendar in the news slice. | §2, §6, §13a–d, §21; `news_upto_2026-07-08.csv` rows for 2026-07-07 and 2026-07-09 | 3 | Correct the trade-deficit prior to $55.9bn; re-derive §13d from the calendar actually scheduled for 9 Jul. |
| 1.3 Audience & tone | Senior US Equity Strategist register held throughout; framing is trading-and-risk-review (invalidation levels, tranche management, corroboration status). No retail tone, no promotional language, no advice framing. | §1, §18, §21b, footer | 5 | None. |
| 2.1 Sections present & ordered | §1–§21 all present in the prescribed order. §13 carries all four sub-sections (13a per-article table, 13b aggregate with numeric tilt −0.38, 13c previous-period calendar, 13d upcoming calendar). §21 carries 21a conviction, 21b cards, 21c 5-session backtest, 21d what-is-working plus the limitations boilerplate. | Headings throughout | 5 | None. |
| 2.2 Scorecard as a table | §6 is a table with Date/Open/High/Low/Close/RSI2/Trend/Source A/Source B/Final/Validation — all required columns present. §11 daily and weekly tables are ordered R3→P→S3 with three levels each side. **Monthly pivots are entirely absent** (grep for "monthly" returns nothing); the brief requires daily, weekly and monthly. | §6; §11 (two tables only) | 3 | Add the monthly floor-pivot table, R3→P→S3, from the prior calendar month's H/L/C. |
| 2.3 Method steps visible | §4 observations → §5 classification and weighted-median consensus → §3 consensus level: the chain is visible and the no-blend rule is stated. §8 is candle-by-candle across all five sessions with an explicit sequence assessment. §9 gives regime with overlap ratio, directional persistence, VOLator slope and scaled VOLator readings for all four instruments. §7 charts are image placeholders (pandoc drops images) with captions — accepted as evidence per the brief, noted. KER is named but never given a numeric value, and ATR(14) is never stated at all, so two of the declared method steps are not inspectable. | §4–§9; §7 five captions | 4 | State ATR(14) and KER(13, EMA 3) as numbers in §9. |
| 3.1 Quantitative claims sourced | §1 and §18 point back to §4/§6 for price. But several load-bearing numbers carry no source and appear nowhere else: September-hike odds "~69–70%" attributed only to "FOMC minutes as reported"; crude "up ~10% over two sessions"; single-stock moves (Broadcom +~5%, Nvidia +~1%, hyperscalers "down ~1%+"); and §14's VIX "prior close 16.13", which matches no close in the VIX slice (6 Jul 16.89, 7 Jul 17.26, 8 Jul 17.92). | §1, §12 (four paragraphs), §14; `VIX_upto_2026-07-08.csv` | 2 | Source or delete the unsourced figures; correct the VIX prior close to the slice value. |
| 3.2 Citations exist & contain data | Three sources spot-checked for internal consistency, two fail. **Yahoo Finance (^GSPC/^SPX), 8 Jul:** raw quote "7,439–7,463", normalized "~7,455", but the same row's Notes read "Open 7,476.54; day range 7,439–7,479" — an open of 7,476.54 cannot lie above the top of the range quoted for the same source and date, and the report then lifts O 7,476.54 and H 7,479.0 into §6 from the note rather than from the source's own quote. **CNBC market wrap, 7 Jul:** quotes 7,503.85 and annotates "(−0.45%)"; against the report's own 6 Jul close of 7,483.24 that move is +0.28%, and −0.45% would require a prior close of ~7,537.8, which the report nowhere states. **Investing.com, 8 Jul:** listed as Source B for the 8 Jul §6 row yet its Normalized column is "—" and its quote is labelled prior-session with a high of 7,536.06 that contradicts the report's own 7 Jul high of 7,545.0. Per brief §3.2 ("a figure not matching its own quote counts as fabricated"), this is a fabricated-source finding. **S&P Dow Jones (via FRED), 7 Jul, 7,503.85** checks out and reconciles to the slice (7,504.3, Δ −0.45). | §4 rows 2, 3, 4; §6 8 Jul row; slice 7 Jul cash close | 0 | Fabricated-source override applies. Re-fetch and re-quote every §4 row so the raw quote, the normalized value and any note agree, and so §6 draws only on figures that appear in the quote. |
| 3.3 Calculations transparent | **RSI2 does not reproduce from the report's own closes.** Helper recomputation on the report's stated closes (7,549.50 / 7,527.00 / 7,483.24 / 7,503.85 / 7,455.00) gives 0.0 / 32.0 / 29.7 for the last three rows against the report's 8 / 55 / 9. **Trend labels violate the report's own stated rule on three of five rows:** 2 Jul (C 7,549.5 < O 7,561.0, RSI2 34 → Bearish, labelled Neutral); 6 Jul (C 7,483.24 > O 7,470.0, RSI2 8 → Neutral, labelled Bearish); 7 Jul (C 7,503.85 > O 7,490.5, RSI2 55 > 50 → Bullish, labelled Neutral). **§11 daily pivots do reproduce exactly** from the report's own 7 Jul H 7,545.0 / L 7,478.0 / C 7,503.85 (P 7,508.95; R1 7,539.9; S1 7,472.9; R2 7,575.95; S2 7,441.95; R3 7,606.9; S3 7,405.9). ATR(14) is never stated; KER is never given a value. **§21a is not reproducible:** the four listed contributions (−0.25, −0.20, −0.15, −0.06) sum to −0.66, not the stated −0.22, and only four of the six weighted terms are shown. | §6 RSI2/Trend columns; helper output; §11 arithmetic; §9; §21a | 1 | Recompute RSI2 from the corrected close sequence; re-derive all five Trend labels from the stated rule; show all six weighted terms in §21a summing to the stated score; state ATR(14) and KER. |
| 3.4 Numbers reconcile | Good: the D-1 reference 7,455 is identical in §1, §3, §4 and §6; the §11 daily levels are quoted unchanged on the Trade 2 card (entry 7,508.9 = P; TP1 7,472.9 = S1; TP2 7,441.9 = S2; TP3 7,405.9 = S3). Failures: ATR appears in §21b ("3×ATR cap") but is stated nowhere, so it cannot reconcile against §9. §21d claims Trade 2 TP1 hit-rate ≈100% while four of the five §21c outcomes (+0.5R, +0.8R, +0.3R, +0.9R) are below TP1 = +1R; same contradiction for Trade 3A (+0.6R, +0.7R, +0.7R all below 1R, TP1 claimed 100%). §21c's 6 Jul row is 7,491 → 7,483 = 8 pts, which is 0.22R against R = 36.1, not the claimed +0.3R. The §11 weekly set back-solves to H 7,620.9 / L 7,521.0 / C 7,527.0, but §1 states 7,620.90 was the cycle high printed "roughly a month earlier" and §6 puts the 2 Jul high at 7,595.0 — the weekly pivots are built on a high that the report's own text places outside the prior week. | §1/§3/§4/§6 vs §11 vs §21b/c/d; weekly back-solve | 1 | Rebuild the weekly pivots from the prior week's actual H/L/C; state ATR(14); recompute §21d hit-rates from the §21c outcome column. |
| 4.1 Pillars conclude | Every analytical pillar ends in an explicit direction label consistent with its own content: §8 "Judgement label: Bearish continuation"; §9 "Bias: Neutral-to-Bearish"; §10 "No counter contradicts the regime synthesis"; §12 tags each of four considerations price-negative / supportive / neutral-to-negative; §14 closes each of four macro strands with a direction and cross-reference. | §8, §9, §10, §12, §14 | 5 | None. |
| 4.2 Peer/cross-asset interpreted | §10 is built as a mechanism table (translation drag, discount-rate channel, European beta to the same oil/rates shock), not a correlation list, and each row carries a confirmation verdict and an implication for the call. USDX and VIX 5-day directions verify against the slices: USDX 100.858 (2 Jul) → 101.052 (8 Jul) rising; VIX 17.58 → 17.92 rising. DAX 40 "Falling" is asserted without a source and there is no DAX slice to check it against. | §10; `USDX_upto_2026-07-08.csv`, `VIX_upto_2026-07-08.csv` | 4 | Source the DAX 40 5-day direction. |
| 4.3 Synthesis reconciles tensions | §15 is genuinely two-sided, §16 states a base case with an explicit invalidation (close above weekly P 7,556), and §18 names three reasons and one watch item; §17 and §21a both lean lower with the conflict flag correctly set to none. But the card layer is not reconciled with the analysis and breaks M5: §9's preferred protocol is "fade rallies toward resistance / **avoid chasing breakdowns into support given oversold RSI2**", while Trade 3A is precisely a sell-stop breakdown entry at 7,438.0 below the 8 Jul low, with no reconciliation offered. Trade 2 is a fade limit at daily P under a self-declared Transitional regime, where M5 permits the breakout side only; its TP2 is +1.9R where M5 requires exactly 2R; and its stop sits on the 7 Jul swing high with no 0.25×ATR buffer. Trade 3A is a breakout entry filed under the 3A Momentum-Pullback family, which requires a 57.5% retrace limit with logged swing endpoints — none are logged, and on slice numbers no qualifying swing exists (5-session swing 7,552.40 → 7,421.10 = 131.3 pts vs the required ≥ 2×ATR14 = 157.9). | §15–§18, §21a; §9 protocol vs §21b Trade 3A; brief §3 M5 rules; helper swing/ATR output | 2 | Rebuild both cards to the M5 family rules (see feedback file) or suppress Trade 3A for want of a qualifying swing. |
| 4.4 Calibrated language | §17 is exactly one sentence. No hedge stacking anywhere in the forecast or judgement. Confidence is stated as Medium in both §3 and §18, and §21a states the conviction score against the |0.25| threshold and its suppression consequence. | §3, §17, §18, §21a | 5 | None. |
| 5.1 Data dated; staleness flagged | Every §6 row is dated; the 8 Jul row is flagged SINGLE-SOURCE (indicative only) in §6 and the flag is restated in §11, §19 and both card Caveats — the propagation is done properly. Weaker: §13a dates the BofA and Yardeni entries only as "Jul 2026" with no day; §4's Bloomberg row is dated "7–8 Jul", spanning two sessions for a single quote; §14's VIX 16.13 carries neither a date nor a source. | §6 note; §19; §13a rows 2–3; §4 row 6; §14 | 3 | Give BofA, Yardeni and the Bloomberg wrap exact dates; date and source the VIX reference. |
| 5.2 Assumptions up front | The anchor-override caveat is stated twice — §3 Note and §20 Anomalies — and the single-source pivot propagation is carried into both card Caveat lines. But the brief requires the anchor-override caveat on the card, and neither card states an entry anchor at all; the static-integrity requirement "anchor explicit" therefore fails on both live cards. | §3 Note, §20; §21b Trade 2 and Trade 3A Caveats (no anchor line) | 3 | Add an explicit anchor line and the anchor-override caveat to each card. |
| 5.3 Red flags surfaced | §12 surfaces four risk strands, §15 is balanced three-and-three, and the §13d CPI collision is carried into both card Caveats along with the oversold-RSI2 bounce risk — the collision-to-caveat path works. However §13d omits every HIGH-impact US event actually on the 9 Jul calendar (Initial Jobless Claims, Existing Home Sales, 30-Year Bond Auction) and hangs the entire risk frame on a CPI print that is not on that calendar. | §12, §15, §21b Caveats; `news_upto_2026-07-08.csv` rows dated 2026-07-09 | 3 | Rebuild §13d from the scheduled 9 Jul calendar and re-point §15/§16/§17 at the events that are actually listed. |
| 5.4 Restrictions honoured | Clean on most restrictions: no module codes (M1–M5), no framework name, no bracketed variable names, no ES-futures reliance, instrument common names used throughout, and the OTC/CFD read (Trading Economics) is explicitly marked "excluded from OHLC per basis rules". **Breach:** §5 states the 8 Jul reference is a *weighted median* constructed from an intraday band, and §6 then places that constructed value, 7,455.0, in the Close column of the "Validated OHLC" table with Source A = Yahoo, Source B = Investing.com and a Final column — a synthesised price presented as sourced. The same row's O 7,476.54 and H 7,479.0 come from a source note that contradicts that source's own quoted range. Minor: prompt-machinery phrasing leaks into the prose ("per the run instruction" §19, "per instruction" §20, "from the instance context" §14). | §5 vs §6 8 Jul row; §4 Yahoo row; lines 449, 510, 529 | 1 | Restriction breach — do not place a constructed consensus level in the OHLC Close column; carry it in §3 only, and leave §6's 8 Jul row blank or genuinely sourced. Strip the prompt-machinery phrasing. |

## 2. Category roll-up

| Category | Level | Multiplier | Points | Justification |
|---|---|---|---|---|
| C1 Prompt adherence (max 20) | 2 | 0.40 | 8.00 | Rows 1.1 = 2, 1.2 = 3, 1.3 = 5 → mean 3.33 → level 3. The §5.4 restriction breach (synthesised price presented as sourced in the §6 Close column) drops C1 one level, per framework §4 → level 2. |
| C2 Structure (max 20) | 4 | 0.85 | 17.00 | Rows 2.1 = 5, 2.2 = 3, 2.3 = 4 → mean 4.00 → level 4. All sections and sub-sections present and ordered; §6 fully columned; deductions for the missing monthly pivot table and for ATR/KER being named but never valued. |
| C3 Accuracy & evidence (max 25) | 0 | 0.00 | 0.00 | Rows 3.1 = 2, 3.2 = 0, 3.3 = 1, 3.4 = 1 → mean 1.00 → level 1. The fabricated-source finding at row 3.2 forces C3 = 0 per framework §4. Independently, four of five stated closes fail the ≤3-pt tolerance (2 Jul +76.7, 3 Jul +22.4, 6 Jul −59.4, 8 Jul −23.6) and RSI2 does not reproduce from the report's own closes. |
| C4 Reasoning & judgment (max 20) | 4 | 0.85 | 17.00 | Rows 4.1 = 5, 4.2 = 4, 4.3 = 2, 4.4 = 5 → mean 4.00 → level 4. Pillar logic, cross-asset mechanism and calibration are all sound; the entire deduction sits in 4.3, where the two live cards break their M5 family rules and Trade 3A contradicts §9's own stated protocol. |
| C5 Currency, restrictions & transparency (max 15) | 3 | 0.65 | 9.75 | Rows 5.1 = 3, 5.2 = 3, 5.3 = 3, 5.4 = 1 → mean 2.50 → rounds to level 3. Single-source flagging and propagation are handled well; the restriction breach and the incomplete §13d calendar are the drag. |
| **Total** | — | — | **51.75 → 52** | Sum of category points, rounded to a whole number. |

## 3. Total, band, override check

- Raw total before overrides: 8.00 + 17.00 + 0.00 + 17.00 + 9.75 = **51.75 → 52**.
- **Override 1 — fabricated source (binding).** Row 3.2: the §4 Yahoo Finance row states an 8 Jul open of 7,476.54 and a day range top of 7,479 in its Notes while its own raw quote for the same source and date is 7,439–7,463; §6 then draws O and H from the note. The §4 CNBC row annotates 7,503.85 as "(−0.45%)", which is impossible against the report's own 6 Jul close of 7,483.24 (+0.28%). Per brief §3.2, a figure not matching its own quote counts as fabricated. Effect: **C3 forced to 0** and the total **capped at 59**.
- **Override 2 — restriction breach (also applies).** Row 5.4: §5 constructs 7,455 as a weighted median and §6 presents it as a validated Close with two named sources and a Final column. Effect: **C1 dropped one level (3 → 2)** and the total capped at 74.
- Both caps applied; the binding cap is 59. Computed total 52 already sits below it, so no truncation was needed.
- **Final Trust Score: 52 / 100.**
- **Band: Low (40–59).**
- Override recorded in the run row: `hallucinated_source` (the stricter, binding override; the restriction breach is applied to C1 as described above).

## 4. Card Integrity

Linter rows, verbatim from `qa/regen_20260906_qa1/lint_static/2026-07-09.csv`:

| card_id | report_date | strategy | flags | dud |
|---|---|---|---|---|
| 2026-07-09_Trade_1 | 2026-07-09 | Trade 1 - Daily Directional | SUPPRESSED | False |
| 2026-07-09_Trade_2 | 2026-07-09 | Trade 2 - Pivot (sell limit daily P) | CLEAN | False |
| 2026-07-09_Trade_3A | 2026-07-09 | Trade 3A - Momentum-Pullback (sell stop) | CLEAN | False |

Per-card integrity, 100 − 40·(#DUD) − 10·(#WARN), floored at 0:

| Card | #DUD_* | #WARN_* | Integrity | In mean? |
|---|---|---|---|---|
| 2026-07-09_Trade_1 | 0 | 0 | — | No (SUPPRESSED) |
| 2026-07-09_Trade_2 | 0 | 0 | 100 | Yes |
| 2026-07-09_Trade_3A | 0 | 0 | 100 | Yes |

**Report Card Integrity = 100.0** (mean over the two non-suppressed cards). Cards in lint file: 3. DUD flags: 0. WARN flags: 0.

Note on interpretation: the linter checks only static geometry, and both live cards pass it — stops on the correct side, TP1 beyond entry, TP2 beyond TP1, TP3 beyond TP2, R inside the 0.3–3.0×ATR14 band (Trade 2 R 36.1 and Trade 3A R 47.0 against ATR14 = 78.94, i.e. 0.46× and 0.60×), TP1 within 2.5×ATR14 (197.4 pts) of entry, and both order levels on the correct side of the D-1 close whether the report's 7,455.0 or the slice's 7,478.60 is used. The M5 construction failures described at row 4.3 are not static-geometry failures and therefore do not reduce this number; they are scored under Category 4 and itemised in the feedback file.

## 5. Data reconciliation log

Report value vs slice cash-session value (delta = report − slice). Tolerance: ≤3 pts on a close, ≤8 pts on an open/high/low.

| Section | Field | Report value | Slice value | Delta | Verdict |
|---|---|---|---|---|---|
| §6 | 2 Jul Open | 7,561.0 | 7,502.2 | +58.8 | DISCREPANCY |
| §6 | 2 Jul High | 7,595.0 | 7,541.0 | +54.0 | DISCREPANCY |
| §6 | 2 Jul Low | 7,539.0 | 7,427.0 | +112.0 | DISCREPANCY |
| §6 | 2 Jul Close | 7,549.5 | 7,472.8 | +76.7 | **FAIL (>10 pts)** |
| §6 | 3 Jul Open | 7,548.0 | 7,502.6 | +45.4 | DISCREPANCY |
| §6 | 3 Jul High | 7,566.0 | 7,509.6 | +56.4 | DISCREPANCY |
| §6 | 3 Jul Low | 7,521.0 | 7,497.4 | +23.6 | DISCREPANCY |
| §6 | 3 Jul Close | 7,527.0 | 7,504.6 | +22.4 | **FAIL (>10 pts)** |
| §6 | 6 Jul Open | 7,470.0 | 7,513.9 | −43.9 | DISCREPANCY |
| §6 | 6 Jul High | 7,498.0 | 7,552.4 | −54.4 | DISCREPANCY |
| §6 | 6 Jul Low | 7,455.0 | 7,502.4 | −47.4 | DISCREPANCY |
| §6 | 6 Jul Close | 7,483.24 | 7,542.6 | −59.36 | **FAIL (>10 pts)** |
| §6 | 7 Jul Open | 7,490.5 | 7,531.5 | −41.0 | DISCREPANCY |
| §6 | 7 Jul High | 7,545.0 | 7,538.4 | +6.6 | CONSISTENT |
| §6 | 7 Jul Low | 7,478.0 | 7,480.5 | −2.5 | CONSISTENT |
| §6 | 7 Jul Close | 7,503.85 | 7,504.3 | −0.45 | CONSISTENT |
| §6 | 8 Jul Open | 7,476.54 | 7,459.6 | +16.94 | DISCREPANCY |
| §6 | 8 Jul High | 7,479.0 | 7,488.1 | −9.1 | DISCREPANCY |
| §6 | 8 Jul Low | 7,439.0 | 7,421.1 | +17.9 | DISCREPANCY |
| §6 | 8 Jul Close (D-1) | 7,455.0 | 7,478.6 | −23.6 | **FAIL (>10 pts)** |
| §6 | 2 Jul RSI2 | 34 | 0.00 | +34.0 | DISCREPANCY (not testable from report's own closes — window too short) |
| §6 | 3 Jul RSI2 | 12 | 66.11 | −54.11 | DISCREPANCY (not testable from report's own closes) |
| §6 | 6 Jul RSI2 | 8 | 100.00 (slice) / 0.0 (from report's own closes) | −92.0 / +8.0 | **FAIL — does not reproduce from the report's own close column** |
| §6 | 7 Jul RSI2 | 55 | 49.80 (slice) / 32.0 (from report's own closes) | +5.2 / +23.0 | **FAIL — does not reproduce from the report's own close column** |
| §6 | 8 Jul RSI2 | 9 | 0.00 (slice) / 29.7 (from report's own closes) | +9.0 / −20.7 | **FAIL — does not reproduce from the report's own close column** |
| §6 | 2 Jul Trend | Neutral | Rule gives Bearish (C 7,549.5 < O 7,561.0, RSI2 34 < 50) | — | FAIL — violates the report's own Trend rule |
| §6 | 6 Jul Trend | Bearish | Rule gives Neutral (C 7,483.24 > O 7,470.0, RSI2 8 not > 50) | — | FAIL — violates the report's own Trend rule |
| §6 | 7 Jul Trend | Neutral | Rule gives Bullish (C 7,503.85 > O 7,490.5, RSI2 55 > 50) | — | FAIL — violates the report's own Trend rule |
| §11 | Daily P | 7,508.9 | 7,462.60 (D-1 cash) | +46.3 | DISCREPANCY — reproduces exactly from the report's own 7 Jul H/L/C (7,508.95), but is built on D-2, not D-1 |
| §11 | Daily R1 | 7,539.9 | 7,504.10 | +35.8 | DISCREPANCY (same cause) |
| §11 | Daily R2 | 7,575.9 | 7,529.60 | +46.3 | DISCREPANCY (same cause) |
| §11 | Daily R3 | 7,606.9 | 7,571.10 | +35.8 | DISCREPANCY (same cause) |
| §11 | Daily S1 | 7,472.9 | 7,437.10 | +35.8 | DISCREPANCY (same cause) |
| §11 | Daily S2 | 7,441.9 | 7,395.60 | +46.3 | DISCREPANCY (same cause) |
| §11 | Daily S3 | 7,405.9 | 7,370.10 | +35.8 | DISCREPANCY (same cause) |
| §11 | Weekly P | 7,556.3 | 7,466.90 | +89.4 | **FAIL** — back-solves to H 7,620.9 / L 7,521.0 / C 7,527.0; §1 places 7,620.90 a month earlier and §6 puts the 2 Jul high at 7,595.0 |
| §11 | Weekly R1 | 7,591.6 | 7,578.70 | +12.9 | DISCREPANCY (same cause) |
| §11 | Weekly S1 | 7,491.7 | 7,392.80 | +98.9 | **FAIL** (same cause) |
| §11 | Weekly S2 | 7,456.4 | 7,281.00 | +175.4 | **FAIL** (same cause) |
| §11 | Weekly S3 | 7,391.8 | 7,206.90 | +184.9 | **FAIL** (same cause) |
| §9 / §21b | ATR(14) | not stated (referenced as "3×ATR cap") | 78.94 (cash) / 87.54 (full-day) | n/a | FAIL — required value absent |
| §9 | KER(13, EMA 3) | not stated (qualitative only) | n/a | n/a | FAIL — required value absent |
| §11 | Monthly pivots | absent | n/a | n/a | FAIL — required table missing |
| §1 / §3 / §18 | D-1 reference close | 7,455 (indicative) | 7,478.60 | −23.6 | **FAIL (>10 pts)** — consistent across §1/§3/§4/§6, but wrong against the slice |
| §1 | Cycle high | 7,620.90 | 25-day high 7,604.30 (4 Jun) | +16.6 | DISCREPANCY |
| §14 | VIX prior close | 16.13 | 16.89 (6 Jul), 17.26 (7 Jul) | −0.76 vs nearest | DISCREPANCY — matches no close in the VIX slice |
| §14 | VIX current | ~17–18 | 17.92 (8 Jul close) | within range | CONSISTENT |
| §10 | USDX 5-day direction | Rising | 100.858 (2 Jul) → 101.052 (8 Jul) | +0.194 | CONSISTENT |
| §10 | VIX 5-day direction | Rising | 17.58 (2 Jul) → 17.92 (8 Jul) | +0.34 | CONSISTENT |
| §10 | DAX 40 5-day direction | Falling | no DAX slice available | n/a | UNVERIFIABLE — asserted without a source |
| §13c | Trade Balance actual | −$77.6bn | −77.585 (7 Jul calendar) | 0.015 | CONSISTENT |
| §13c | Trade Balance prior | −$54.6bn | −55.881 (7 Jul calendar, previous) | +1.28bn | DISCREPANCY |
| §13c | FOMC minutes, 8 Jul, Impact High | present | 2026-07-08 21:00, impact MODERATE | — | DATE CONSISTENT; impact overstated |
| §13d | "CPI print ~9–10 Jul", High, highest-impact | no US CPI on the 9 Jul calendar; the 9 Jul US HIGH rows are Initial Jobless Claims, Existing Home Sales, 30-Year Bond Auction | — | **FAIL for 9 Jul** — three scheduled HIGH-impact US events omitted from §13d; 10 Jul lies beyond the slice and is unverifiable |
| Cross-report | 2 Jul Close vs `SP500_Report_03Jul2026.md` §6 | 7,549.5 | 7,482.5 (corroborated there) | +67.0 | **FAIL** — direct contradiction with an earlier report; the earlier value is the one near the slice (Δ 9.7) |
| Cross-report | 2 Jul O / H / L vs `SP500_Report_03Jul2026.md` §6 | 7,561 / 7,595 / 7,539 | 7,479 / 7,508 / 7,450 | +82 / +87 / +89 | **FAIL** — same session, incompatible bars |
| §21a | Direction score | −0.22 | Sum of the report's own listed terms: −0.25 −0.20 −0.15 −0.06 = −0.66 | +0.44 | **FAIL** — score not reproducible; on the report's own components |score| ≥ 0.25 and Trade 1 would not qualify for suppression |
| §21c | 6 Jul Trade 2 row | 7,491 → 7,483 = 8 pts, "+0.3R" | 8 / 36.1 = 0.22R | +0.08R | DISCREPANCY |
| §21d | Trade 2 TP1 hit-rate | ≈100% | 1 of 5 §21c outcomes reaches +1R (TP1) | — | FAIL — contradicts §21c |
| §21d | Trade 3A TP1 hit-rate | ≈100% | 0 of 3 §21c outcomes reaches +1R | — | FAIL — contradicts §21c |
| As-of check | Declared as-of session | Close of 8 Jul 2026 (D-1) | Last slice bar 2026-07-08 23:45 | — | Declared as-of is genuinely D-1, but §3's consensus basis, §11's pivots and §18's judgement all rest on the 7 Jul (D-2) session, so the operative as-of is D-2 |
