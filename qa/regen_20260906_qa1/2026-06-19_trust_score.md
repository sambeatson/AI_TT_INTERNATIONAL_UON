# Trust Score — 2026-06-19 — SP500_Report_19Jun2026.md

Run: `regen_20260906_qa1` · Asset: US500 (S&P 500 cash) · D = 2026-06-19 (US holiday, Juneteenth) · D-1 slice = `data/slices/US500/US500_upto_2026-06-18.csv` (last bar 2026-06-18 23:45 broker).
Basis tolerances applied per REVIEWER_BRIEF §4: |Δ| ≤ 3 pts on a close, ≤ 8 pts on an open/high/low.

## 1. Section 7 checklist

| Item | Reviewer notes | Evidence observed | Score 0–5 | Action required |
|---|---|---|---|---|
| 1.1 Variables respected | Asset correctly the S&P 500 cash index (503 constituents), not ES futures. Counters USDX · VIX · DAX 40 in the required order, USDX first. As-of NY close of D-1 with the holiday handled. Lookback 5 sessions, USD / index points, tick 0.01 all stated. Weak on two points: only 5 distinct price providers appear in §4 (one of them excluded), short of the ≥6 tiered-source requirement once §13a's Schwab is set aside; and the daily-open anchor is never given as a time — the header and §20 say only "anchor overridden to 19 Jun 2026", a date, so the 07:00 UK M1 anchor is nowhere on the card. | §2 table; masthead line "With reference to: USDX · VIX · DAX 40"; §4 rows; §20 anchor line; §21b Trade 1 "Entry: Market on next open" | 3 | State the anchor explicitly as 07:00 UK on the Trade 1 card and in §20; add a sixth independent index-provider/exchange/sell-side price source to §4. |
| 1.2 Coverage & currency consistent | All price and article dates in §2/§4/§6/§13 are D-1 or earlier; the session referenced is D and the pivot session Mon 22 Jun is correct given the Juneteenth holiday. Units are index points/USD throughout with no drift. One real defect: §20 stamps the report "generated 21 Jun 2026 (UK)", two days AFTER the D = 19 Jun reference date, which breaks the currency chain for a report presented as the 19 Jun product. | §20 final line "Timestamp: generated 21 Jun 2026 (UK)"; §2 as-of row; §11 "next session (Mon 22 Jun)" | 3 | Correct the §20 generation timestamp to a time on or before D (19 Jun 2026), or state why the product post-dates its own reference date. |
| 1.3 Audience & tone | Written throughout for a senior US equity strategist in a trading-and-risk-review setting: pillar labels, explicit confidence, invalidation levels, no retail framing, no promotional language, and a "Not investment advice" close. §18 delivers a decision-grade judgement with three named reasons and a single watch item. | §1, §18, §21d closing paragraph | 5 | None. |
| 2.1 Sections present & ordered | All of §1–§21 present and in the prescribed order. §13 carries all four sub-blocks (§13a per-article table, §13b aggregate with a numeric tilt, §13c previous-period calendar, §13d upcoming calendar). §21 carries §21a conviction, §21b cards, §21c 5-session backtest, §21d what-is-working plus the limitations boilerplate. §17 is a single sentence. | Headings §1 through §21d | 5 | None. |
| 2.2 Scorecard as a table | §6 is a proper table and carries all ten required columns (Date/O/H/L/C/RSI2/Trend/Source A/Source B/Validation). §11 is malformed against spec: the daily table lists eleven levels R5→S5 instead of the specified R3→P→S3 three-a-side, and the weekly and monthly pivot tables are absent entirely (disclosed as suppressed for want of corroborated higher-timeframe H/L/C, but the protocol expects the tables with a SUPPRESSED marking, not omission). | §6 table; §11 table R5 7,646.58 … S5 7,347.33; §11 closing line "Weekly/monthly pivot tables are omitted" | 3 | Trim the daily pivot table to R3→P→S3 and add weekly and monthly pivot tables as explicit SUPPRESSED rows rather than omitting them. |
| 2.3 Method steps visible | §4→§5 does run observations → classification → consensus with an explicit exclusion rationale. §8 is candle-by-candle plus a sequence assessment, but only for the two corroborated sessions. §9 states the regime with persistence and overlap reasoning. §7 carries three chart placeholders (pandoc image drops — accepted as evidence, noted). Shortfalls: the VOLator quantitative panel and the 5-week structure chart are both suppressed, §9's Kaufman call is asserted with no KER(13, EMA 3) value, and ATR(14) is never given a number anywhere in the report despite being used in the Trade 1 runner rule. | §4–§5; §8; §9 "VOLator: a fully corroborated … panel could not be built"; §7 three `![](media/…)` placeholders plus the suppression note | 3 | State ATR(14) and KER(13, EMA 3) numerically in §9 and carry the ATR value onto every card; restore the VOLator panel or mark it SUPPRESSED with the inputs that were missing. |
| 3.1 Quantitative claims sourced | Most §1/§12/§14 numbers point back to §6, §10 or §13 (+1.08%, 7,500.58, 7,420.10, the 3.50–3.75% Fed corridor, USDX 100.6–100.9). Weaknesses: the VIX pair 18.44 → 16.78 and DAX 24,985.82 are sourced only to a §20 log line, and the 18-Jun VIX value does not survive the slice check (below); §13b's own arithmetic narrative is self-inconsistent — it attributes bearish weight to an "institutional" article when the only institutional item (Schwab) is classed Mixed, and it reports a tilt of −0.03 after stating a range of "+0.00 to −0.05" without showing the class weights. | §1; §9; §10; §14; §20 counters line; §13b | 3 | Show the source-class weights behind the §13b tilt and give the VIX/DAX prints a dated in-table source rather than a log mention. |
| 3.2 Citations exist & contain data | Three sources spot-checked for internal consistency. (a) Trading Economics 18 Jun, "S&P 500 advanced 1%… tech strength and optimism over the US-Iran deal" — consistent with the report's own +1.08% and with §4: PASS. (b) CNBC 17 Jun, "S&P 500 closes higher, Nasdaq climbs nearly 2% as chips fuel comeback", classed Bullish — impossible against the report's own record: the same report has 17 Jun closing DOWN at 7,420.10 (§6, §13c "index sold off into close"), attributes the chip-led ~2% Nasdaq move to 18 Jun (§1, §12, §13c), and carries a second CNBC 17 Jun article ("The market didn't like what it heard from the Fed", Bearish) that flatly contradicts it. The cited figure does not match its own quote's date. (c) Wikipedia/market 18 Jun, "record closing high of 6,932.05 set December 24, 2025" — impossible: a record closing high cannot sit 568.53 points BELOW a subsequent close that the same report certifies as corroborated (7,500.58 on 18 Jun 2026). Per REVIEWER_BRIEF §2 row 3.2, a citation that is self-contradictory or impossible counts as fabricated. Two such citations. | §13a rows 4 and 6; cross-read against §6, §12, §13c | 0 | Remove or re-date the CNBC "chips fuel comeback" item (it belongs to 18 Jun, not 17 Jun) and drop or correct the 6,932.05 "record closing high" figure; re-derive the §13b counts and tilt afterwards. |
| 3.3 Calculations transparent | Pivots reproduce exactly: from the report's own 18-Jun H/L/C (7,511.07 / 7,468.32 / 7,500.58) every one of the eleven printed levels is correct to 0.01 (P 7,493.32, R1 7,518.33, S1 7,475.58, R2 7,536.07, S2 7,450.57, R3 7,561.08, S3 7,432.83, and the R4/R5/S4/S5 extensions). Everything else fails. RSI2: no formula is shown and the printed values do not reproduce from the report's own close sequence — the helper recomputes 15.7 for 17 Jun (report "~12") and 100.0 for 18 Jun (report "~88"), and on slice closes the same dates give 0.00 and 43.95. ATR(14) is never stated. KER(13, EMA 3) is never stated. §21a's direction score is not reconstructable: only three of the six weighted signals are disclosed, the sentiment line quotes a raw tilt (−0.03) rather than signal×weight, and the three disclosed contributions sum to +0.37 against a stated score of +0.27. | §6 RSI2 column; §11 vs hand recomputation; §9; §21a "Score ≈ +0.27 … +0.25 … +0.15 … −0.03" | 1 | Show the RSI2 derivation (RS = mean gain / mean loss over 2 periods) and correct the two printed values to the ones that follow from the tabulated closes; state ATR(14) and KER numerically; list all six §21a signals with signal × weight so the score sums. |
| 3.4 Numbers reconcile | Good: 7,500.58 is identical in §1, §3, §4, §6 and the §21b Trade 1 entry; §11 pivots match every level quoted on the cards (S1 7,475.58, S2 7,450.57, R2 7,536 as Trade 1 TP1, R3 7,561, R4 7,603). Failures: ATR is absent so the §9↔§21 ATR reconciliation cannot be performed at all; the §6 RSI2 values are not carried into §21a as an input; the 17-Jun close 7,420.10 conflicts with the corroborated 7,420.43 used in the immediately prior report (Δ 0.33), which exceeds the ±0.10 pt tolerance this report itself invokes while §19/§20 assert "delta 0.00"; and §4 labels 16-Jun 7,511.35 "Derived/CFD — Excluded" when the prior report sourced the identical figure from S&P Dow Jones and Yahoo Finance as an official cash close. | §1/§3/§4/§6/§21b close; §11 vs §21b; §4 Investing.com row; `reports/md/SP500_Report_18Jun2026.md` §4/§6 | 1 | Reconcile the 17-Jun close to 7,420.43 or justify 7,420.10; reclassify the 16-Jun 7,511.35 print as the official cash close it is; state ATR once and quote it in both §9 and §21b. |
| 4.1 Pillars conclude | §8 ends "Bullish continuation (low-confidence sample)", §9 "Transitional … Neutral-to-mildly-bullish", §10 "MIXED with a risk-on tilt", §12 tags every consideration price-negative/supportive/neutral, §14 ends "price-negative bias". All present and internally consistent with their own content. Deduction: §9 prescribes "reduced-conviction / pullback-buy" as the preferred protocol, and the §21b card set then issues a breakout stop-entry (Trade 3) that contradicts it. | §8, §9, §10, §12, §14 closing labels; §9 "Preferred trade protocol" vs §21b Trade 3 | 4 | Align §9's stated trade protocol with the cards actually issued, or change the cards. |
| 4.2 Peer/cross-asset interpreted | §10 gives a real transmission mechanism per counter rather than a correlation list — USD translation into multinational earnings, implied volatility into equity multiples, DAX as a common global-risk proxy — and aggregates to a labelled read with a "no hard contradiction" statement. The reasoning is sound but rests on a VIX print that does not survive the slice check (16.78 stated vs 17.85 cash close on the slice), which overstates the vol-contraction leg of the argument. | §10 table and aggregate line; §14 volatility paragraph; VIX slice | 4 | Restate the 18-Jun VIX to the corroborated value and re-weight the "supportive" call accordingly. |
| 4.3 Synthesis reconciles tensions | The narrative layer does this well — §15/§16 set the rebound against the transition regime, §16 gives a base case with an explicit invalidation, §13b reconciles balanced sentiment against an up day, §21a checks §17 against the score. The strategy layer contradicts it. §9 declares the regime Transitional and Kaufman Transition, but Trade 2 is built as a RANGE card (buy limit at daily S1) and Trade 3 as a 3A TREND card, when M5 requires breakout-side-only construction in TRANSITION. Trade 3 is not even a 3A: it is a stop-entry breakout above the 18-Jun high, not a 57.5% retrace of a qualifying swing, its stop is "mid-body of the 18-Jun candle" rather than beyond the 0% anchor by 0.25×ATR, its swing endpoints are unlogged, and no qualifying swing exists on the slice (the 5-session swing 7,363.90 → 7,583.40 is 219.50 pts, below 2×ATR14 = 224.30). Trade 2's invalidation (daily close below S2 7,450.57) is the stop level itself, not a separate thesis invalidation. | §9 regime label; §21b all three cards; slice 5d swing and ATR14 | 1 | Rebuild the card set for the declared regime: TRANSITION → breakout side only for Trade 2, 3C (or SUPPRESSED) for Trade 3; separate Trade 2's thesis invalidation from its stop. |
| 4.4 Calibrated language | §17 is exactly one sentence with a single conditional and no hedge stacking. Confidence is stated where required: §3 High (close) / Medium (intraday), §18 Medium, §21a "low-to-moderate conviction", §8 "low-confidence sample". Deduction: §21d asserts the 17→18-Jun long "would have resolved positively (~+2R)" without disclosing the R it is measured against, and §13b's "low-confidence-adjacent … but ≥3 articles, so not flagged low-confidence" is a hedge that avoids a required flag decision. | §17; §3; §18; §21a; §21d; §13b | 4 | State the R used in the §21c/§21d backtest so the "+2R" figure is checkable. |
| 5.1 Data dated; staleness flagged | Every price row and every article carries a date, and the single-source-indicative O/H/L rows are asterisked in §6 with a footnote and re-explained in §19 with the reason the second corroborator could not be obtained. §4 marks basis per row and flags the excluded print. Deduction: the §20 generation timestamp post-dates D, and the 12/15/16-Jun rows are dated but carry a source label ("Cash fam.") that cannot be reconciled to any named provider. | §6 asterisks and footnote; §19; §4 Basis column; §20 timestamp | 4 | Timestamp the report on or before D; name the specific provider behind the "Cash fam." attribution for each indicative row. |
| 5.2 Assumptions up front | The anchor-override caveat is carried in the masthead and repeated in §20; §19 states plainly that pivots use only the corroborated 18-Jun session, so single-source propagation into pivot-derived card levels is bounded and disclosed; §6's footnote states the indicative rows are "not used for pivot inputs or definitive entries"; the run-instruction deviation (retaining strategies where the module would halt) is disclosed in §6, §19 and §20. Deduction: the override is stated as a date only, never as the 07:00 UK time, and no card names its anchor. | Masthead lines 5–7; §19; §20; §6 footnote; §21b Caveats rows | 4 | Give the anchor as a time on the card, not just as a date in the header. |
| 5.3 Red flags surfaced | §12 tags each consideration with direction and horizon; §15 gives three-a-side upside/downside risks with cross-references; §16 names an explicit base-case invalidation; §13d identifies May PCE as the highest-impact upcoming event. Deduction: the §13d event collision is carried into only one card caveat (Trade 3 "holding period spans pre-PCE risk"); Trades 1 and 2 caveat corroboration only and are silent on the Micron/FedEx and PCE event risk inside their holding windows. | §12; §15; §16; §13d; §21b Caveats rows | 4 | Propagate the §13d event risk into the Trade 1 and Trade 2 caveats. |
| 5.4 Restrictions honoured | Clean on four restrictions: no bracketed variable names, no module codes, no framework name, instrument common names used throughout; ES futures are not used for anything; the derived/CFD print is explicitly excluded from the OHLC basis rather than folded into it. Breached on the no-synthesis restriction. §5 states flatly "No values were synthesized", yet §6 presents 12/15/16-Jun OHLC attributed to the cash source family that cannot be reconciled to any cash source: against the slice the closes are off by −16.9, −103.4 and −111.9 points, and against the corroborated values used one day earlier in `SP500_Report_18Jun2026.md` they are off by −30.00, −94.29 and −100.35 points. The printed levels recycle the two corroborated anchors (the 15-Jun "open" 7,420 is the 17-Jun close; the 15-Jun "high" 7,468 is the 18-Jun low), which is the signature of interpolation between the corroborated sessions, presented under a source label. A price presented as sourced that is not sourced is the restriction this rule names. | §5 "No values were synthesized"; §6 rows 12/15/16 Jun; slice cash-session OHLC; `reports/md/SP500_Report_18Jun2026.md` §4/§6 | 1 | Either name the cash-family provider and the retrieved values for each of the 12/15/16-Jun rows, or replace the rows with an explicit NOT AVAILABLE marking. Do not print unsourced levels under a source label. |

## 2. Category roll-up

| Category | Level | Multiplier | Points | Justification |
|---|---|---|---|---|
| C1 Prompt adherence (max 20) | 3 | 0.65 | 13.00 | Rows 1.1–1.3 mean 3.67 → level 4, reduced one level to 3 by the restriction-breach override (row 5.4). Variables block is otherwise well respected; the anchor time and the sixth source are the standing gaps. |
| C2 Structural alignment (max 20) | 4 | 0.85 | 17.00 | Rows 2.1–2.3 mean 3.67 → 4. Every section and sub-block is present and ordered and §6 is a complete ten-column table; §11 is malformed (R5→S5, no weekly/monthly) and two chart/panel outputs are suppressed. |
| C3 Accuracy & evidence (max 25) | 0 | 0.00 | 0.00 | Rows 3.1–3.4 mean 1.25 → level 1, forced to 0 by the hallucinated-source override (two internally impossible citations in §13a). Independently: three of five §6 rows are 100+ points from the slice, RSI2 does not reproduce from the report's own closes, and ATR/KER are absent. |
| C4 Reasoning & judgment (max 20) | 3 | 0.65 | 13.00 | Rows 4.1–4.4 mean 3.25 → 3. Pillar logic, cross-asset mechanism and calibration are strong; the card set contradicts the report's own regime call and Trade 3 does not follow the method it names. |
| C5 Currency, restrictions & transparency (max 15) | 3 | 0.65 | 9.75 | Rows 5.1–5.4 mean 3.25 → 3. Dating, flagging and disclosure are unusually thorough, but the no-synthesis restriction is breached in §6 and the report is stamped after its own reference date. |
| **Total** | — | — | **52.75 → 53** | Sum of weighted points, rounded to a whole number. |

## 3. Total, band, override check

- Raw weighted total: 13.00 + 17.00 + 0.00 + 13.00 + 9.75 = **52.75 → 53**.
- **Hallucinated-source override APPLIES.** Two §13a citations are internally impossible under REVIEWER_BRIEF §2 row 3.2: the CNBC 17 Jun "S&P 500 closes higher, Nasdaq climbs nearly 2% as chips fuel comeback" item (the report's own §6/§13c have 17 Jun closing down at 7,420.10 and place the chip rebound on 18 Jun, and a second CNBC 17 Jun item in the same table says the opposite), and the Wikipedia/market "record closing high of 6,932.05 set December 24, 2025" quote (a record high 568.53 points below a later close the report certifies as corroborated). Effect: C3 = 0 and the total is capped at the Low band (40–59).
- **Restriction-breach override APPLIES.** §5 asserts "No values were synthesized" while §6 prints 12/15/16-Jun OHLC under a cash-family source label that reconciles to no source (closes −16.9 / −103.4 / −111.9 pts vs the slice; −30.00 / −94.29 / −100.35 pts vs the corroborated values used in the 18 Jun report) and recycles the two corroborated anchors as the indicative rows' levels. Effect: C1 reduced one level (4 → 3) and the total capped at the Moderate band (60–74).
- **Binding result:** the tighter of the two caps governs. Total 53 already sits below both caps, so no numeric reduction is applied; the C3 = 0 and C1 −1 adjustments are already reflected in the roll-up above.
- **Final Trust Score: 53 / 100 — Band: Low.**
- Override recorded for the run row: `hallucinated_source` (the binding, more severe of the two; the restriction breach is recorded here in narrative and in row 5.4).

## 4. Card Integrity

Linter rows copied verbatim from `qa/regen_20260906_qa1/lint_static/2026-06-19.csv`:

| card_id | report_date | strategy | flags | dud |
|---|---|---|---|---|
| 2026-06-19_Trade_1 | 2026-06-19 | Trade 1 - Daily Directional | WARN_R_TINY(0.29xATR) | False |
| 2026-06-19_Trade_2 | 2026-06-19 | Trade 2 - Pivot (buy limit daily S1) | WARN_R_TINY(0.20xATR) | False |
| 2026-06-19_Trade_3A | 2026-06-19 | Trade 3A - Momentum-Pullback (breakout stop) | WARN_R_TINY(0.27xATR) | False |

Per-card integrity, 100 − 40·(#DUD) − 10·(#WARN), floored at 0:

| Card | #DUD | #WARN | Integrity |
|---|---|---|---|
| 2026-06-19_Trade_1 | 0 | 1 | 90 |
| 2026-06-19_Trade_2 | 0 | 1 | 90 |
| 2026-06-19_Trade_3A | 0 | 1 | 90 |

Non-suppressed cards: 3 of 3. **Report Card Integrity = 90.0** (mean). Totals across the lint rows: 3 cards, 0 DUD flags, 3 WARN flags.

Note for the record — the static linter is clean on side/order (stop on the correct side, TP1 beyond entry, TP2 beyond TP1, TP3 beyond TP2, MARKET entry equal to the stated D-1 close, LIMIT below and STOP above the D-1 close). The single recurring flag is risk sizing: all three cards carry R below the 0.3×ATR14 floor (ATR14 full-day 123.91 on the slice; 0.3×ATR14 = 37.17 pts, against R of 35.58 / 25.01 / 34.00). The M5 construction defects assessed in row 4.3 are deliberately NOT folded into this number.

## 5. Data reconciliation log

Helper run: `python3 engine/qa_slice_stats.py --slice data/slices/US500/US500_upto_2026-06-18.csv --date 2026-06-19 --closes 7415 7460 7411 7420.10 7500.58`

### 5.1 §6 OHLC vs slice cash-session (16:30–23:00 broker = 09:30–16:00 ET)

| Section | Field | Report value | Slice value | Delta | Verdict |
|---|---|---|---|---|---|
| §6 | 12 Jun Open | 7,387 | 7,420.9 | −33.9 | FAIL (>8 pt open tolerance) |
| §6 | 12 Jun High | 7,431 | 7,458.7 | −27.7 | FAIL (>8) |
| §6 | 12 Jun Low | 7,372 | 7,363.9 | +8.1 | FAIL (>8, marginal) |
| §6 | 12 Jun Close | 7,415 | 7,431.9 | −16.9 | FAIL — >10 pt close error, Category 3 failure |
| §6 | 15 Jun Open | 7,420 | 7,534.1 | −114.1 | FAIL |
| §6 | 15 Jun High | 7,468 | 7,583.4 | −115.4 | FAIL |
| §6 | 15 Jun Low | 7,405 | 7,533.6 | −128.6 | FAIL |
| §6 | 15 Jun Close | 7,460 | 7,563.4 | −103.4 | FAIL — >10 pt close error, Category 3 failure |
| §6 | 16 Jun Open | 7,455 | 7,562.9 | −107.9 | FAIL |
| §6 | 16 Jun High | 7,472 | 7,571.4 | −99.4 | FAIL |
| §6 | 16 Jun Low | 7,405 | 7,518.2 | −113.2 | FAIL |
| §6 | 16 Jun Close | 7,411 | 7,522.9 | −111.9 | FAIL — >10 pt close error, Category 3 failure |
| §6 | 17 Jun Open | 7,430 | 7,531.7 | −101.7 | FAIL |
| §6 | 17 Jun High | 7,455 | 7,540.0 | −85.0 | FAIL |
| §6 | 17 Jun Low | 7,388 | 7,408.5 | −20.5 | FAIL |
| §6 | 17 Jun Close | 7,420.10 | 7,427.5 | −7.4 | FAIL (>3 pt close tolerance; below the 10 pt hard-failure line) |
| §6 | 18 Jun Open | 7,487.36 | 7,514.1 | −26.74 | FAIL (>8) |
| §6 | 18 Jun High | 7,511.07 | 7,518.3 | −7.23 | PASS (≤8) |
| §6 | 18 Jun Low | 7,468.32 | 7,472.6 | −4.28 | PASS (≤8) |
| §6 | 18 Jun Close | 7,500.58 | 7,502.30 | −1.72 | PASS (≤3) — headline close is sound |

Summary: the corroborated 18-Jun close, high and low reconcile within CFD-vs-cash basis. Everything else does not. Four of five stated closes are outside the 3 pt tolerance and three of them are outside the 10 pt hard-failure line, three of those by 100+ points.

### 5.2 §6 RSI2

| Section | Field | Report value | Helper — RSI2 on slice closes | Helper — RSI2 from the report's OWN closes | Delta vs own closes | Verdict |
|---|---|---|---|---|---|---|
| §6 | 16 Jun RSI2 | — (blank) | 76.45 | 47.9 | n/a | Blank is disclosed, not an error |
| §6 | 17 Jun RSI2 | ~12 | 0.00 | 15.7 | −3.7 | FAIL — does not reproduce from the report's own closes |
| §6 | 18 Jun RSI2 | ~88 | 43.95 | 100.0 | −12.0 | FAIL — does not reproduce; Category 3 failure per brief §4 |

The report's own close sequence (7,415 → 7,460 → 7,411 → 7,420.10 → 7,500.58) gives two consecutive up-closes into 18 Jun, so RSI2 on that sequence is exactly 100.0, not ~88. Trend labels are nonetheless internally consistent with the printed RSI2 (17 Jun C<O and RSI2<50 → Bearish; 18 Jun C>O and RSI2>50 → Bullish).

### 5.3 §11 pivots — reproduction from the report's own D-1 H/L/C (7,511.07 / 7,468.32 / 7,500.58)

| Section | Level | Report value | Recomputed | Delta | Verdict |
|---|---|---|---|---|---|
| §11 | P = (H+L+C)/3 | 7,493.32 | 7,493.32 | 0.00 | PASS |
| §11 | R1 = 2P−L | 7,518.33 | 7,518.33 | 0.00 | PASS |
| §11 | S1 = 2P−H | 7,475.58 | 7,475.58 | 0.00 | PASS |
| §11 | R2 = P+(H−L) | 7,536.07 | 7,536.07 | 0.00 | PASS |
| §11 | S2 = P−(H−L) | 7,450.57 | 7,450.57 | 0.00 | PASS |
| §11 | R3 = H+2(P−L) | 7,561.08 | 7,561.08 | 0.00 | PASS |
| §11 | S3 = L−2(H−P) | 7,432.83 | 7,432.83 | 0.00 | PASS |
| §11 | R4 / R5 / S4 / S5 | 7,603.83 / 7,646.58 / 7,390.08 / 7,347.33 | 7,603.83 / 7,646.58 / 7,390.08 / 7,347.33 | 0.00 | PASS arithmetically; outside the R3→P→S3 spec (see row 2.2) |

Inherited-basis note (not scored as a pivot error — the report's arithmetic is exact; the input OHLC is what drifts): slice cash-session pivots are P 7,497.73 (Δ −4.41), R1 7,522.87 (Δ −4.54), S1 7,477.17 (Δ −1.59), R2 7,543.43 (Δ −7.36), S2 7,452.03 (Δ −1.46), R3 7,568.57 (Δ −7.49), S3 7,431.47 (Δ +1.36).

### 5.4 Derived quantities and counters

| Section | Field | Report value | Slice value | Delta | Verdict |
|---|---|---|---|---|---|
| §9 / §21b | ATR(14) | not stated anywhere | 112.15 (cash session) / 123.91 (full broker day) | n/a | FAIL — a value used by the Trade 1 runner rule is never disclosed |
| §9 | KER(13, EMA 3) | not stated (qualitative "efficiency is low") | n/a | n/a | FAIL — regime call asserted without the stated statistic |
| §9 / §10 / §14 | VIX 18 Jun close | 16.78 | 17.85 | −1.07 | FAIL — material on a 17–18 handle; the report's stated 1.66-point contraction is 0.68 on the slice |
| §20 | VIX 17 Jun close | 18.44 | 18.53 | −0.09 | PASS |
| §10 / §12 / §14 | USDX 18 Jun | ~100.6–100.9 | 100.878 (cash close) | within band | PASS |
| §1 / §9 / §21b | 25-session high "~7,620 (2 Jun)" | 7,620 | 7,624.60 on 2026-06-02 | −4.6 | PASS — date exact, level within basis |
| §8 / §21b | 5-session swing extremes implied by §6 | high 7,511.07 / low 7,372 | high 7,583.40 (15 Jun) / low 7,363.90 (12 Jun) | −72.33 / +8.10 | FAIL — the swing set the cards reference is not the slice's 5-session swing |
| §21a | Direction score | +0.27 | disclosed components sum to +0.37 | −0.10 | FAIL — score not reconstructable from the three disclosed signals; three of six weights undisclosed |
| §21b T1 | TP1 = entry + 1R | 7,536.0 | 7,500.58 + 35.58 = 7,536.16 | −0.16 | PASS (rounded to the R2 pivot) |
| §21b T1 | TP2 = entry + 2R | 7,571.0 | 7,500.58 + 71.16 = 7,571.74 | −0.74 | Minor — restate to the exact 2R level |
| §21b T1 | U3 stop = entry + 0.2R | 7,507.7 | 7,507.70 | 0.00 | PASS |
| §21b T1 | Runner = time-stop OR 3×ATR cap | 7,603 (daily R4) | 3×ATR14 = 7,837.03 (cash) / 7,872.31 (full day) | −234 / −269 | FAIL — R4 is neither of the two permitted runner rules |
| §21b T2 | TP1/TP2 = entry ± 1R/2R | 7,500.6 / 7,525.6 | 7,500.59 / 7,525.60 | 0.01 / 0.00 | PASS |

### 5.5 Cross-report consistency (reports dated strictly before D)

| Section | Field | Report value (19 Jun) | Value in `SP500_Report_18Jun2026.md` | Delta | Verdict |
|---|---|---|---|---|---|
| §4 / §6 | 17 Jun close | 7,420.10 (claimed "delta 0.00") | 7,420.43 (corroborated, Traders Union + independent reporters) | −0.33 | FAIL — exceeds the ±0.10 pt equity tolerance the report itself invokes |
| §4 / §6 | 16 Jun close | 7,411 (indicative) and 7,511.35 labelled "Derived/CFD — Excluded" | 7,511.35 (S&P Dow Jones + Yahoo Finance, official cash close, corroborated Δ 0.00) | −100.35 | FAIL — an official cash close is mislabelled as a derived/CFD basis and displaced by an unsourceable level |
| §6 | 15 Jun close | 7,460 | 7,554.29 (corroborated) | −94.29 | FAIL |
| §6 | 12 Jun close | 7,415 | 7,445.00 (close corroborated) | −30.00 | FAIL |
| §6 | 11 Jun close | not carried (5-session window starts 12 Jun) | 7,394.30 | n/a | n/a |
