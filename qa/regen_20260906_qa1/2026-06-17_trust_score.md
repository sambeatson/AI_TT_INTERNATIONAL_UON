# Trust Score — 2026-06-17 — SP500_Report_17Jun2026.md

Reference basis: `data/slices/US500/US500_upto_2026-06-16.csv` via `engine/qa_slice_stats.py`
(cash session 16:30–23:00 broker). D-1 = 2026-06-16: cash O 7,562.90 / H 7,571.40 / L 7,518.20 /
C 7,522.90; ATR14 cash 103.03 (full-day 117.14); daily pivots P 7,537.50, R1 7,556.80, R2 7,590.70,
R3 7,610.00, S1 7,503.60, S2 7,484.30, S3 7,450.40; weekly (08–12 Jun) P 7,387.13, R1 7,531.17,
R2 7,630.43; 5-day swing 7,260.00 (11 Jun) → 7,583.40 (15 Jun); 25-day 7,243.10 (9 Jun) → 7,624.60
(2 Jun), width 381.50; May monthly P 7,454.70, R1 7,731.90.

## 1. Section 7 checklist

| Item | Reviewer notes | Evidence observed | Score 0–5 | Action required |
|---|---|---|---|---|
| 1.1 Variables respected | Asset is the cash index (503 constituents), not ES; ES/Barchart is explicitly confirmation-only. Counters USDX · VIX · DAX 40 with USDX first. USD / index points, 5-session lookback (10–16 Jun), tz America/New_York. Daily-open anchor is 07:00 UK, stated in §2 and §20, and the extracted cards carry anchor_broker 09:00 (= 07:00 UK). Weak points: §4 claims "six independent observations for the 16 June close" but only two rows (Yahoo, TheStreet) actually observe the 16 Jun close — two quote the 15 Jun close, one is a futures confirmation, one an intraday range; and the As-of row reads "17 June 2026" where the standing basis is the D-1 NY close (§3 does state the correct basis). | §2 table and session-anchor note; §4 six rows; §10 counter order; §21b card anchor | 3 | Re-state §4 so six observations bear on the D-1 close, or re-label the header; set the As-of row to the 16 Jun NY close. |
| 1.2 Coverage & currency consistent | All price/article dates are D-1 or earlier and the session traded is D. Two coverage errors: §21c is labelled a 5-session backtest but runs 09–15 Jun and maps 10 Jun to t−4, 11 Jun t−3, 12 Jun t−2, 15 Jun t−1 — the whole ladder is shifted one session and D-1 (16 Jun) is absent; §13d's first row (the 17 Jun session itself) renders as [object Object], so the horizon's own day is missing from the forward calendar. No currency or unit drift. | §21c rows; §13d row 1 | 2 | Re-index §21c to t−1 = 16 Jun … t−5 = 10 Jun; restore the 17 Jun row in §13d. |
| 1.3 Audience & tone | Consistent senior-strategist register aimed at trading and risk review: regime language, event gating, explicit conviction score, no retail framing, no promotional language, risk stated alongside every recommendation. | §1, §18, §21a | 5 | None. |
| 2.1 Sections present & ordered | §1–§21 are all present in order, including 13a–13d and 21a–21d. But five tables carry unresolved [object Object] cells: §3 (one whole Field/Value row), §6 (the entire Close column and the entire Validation column, 5 rows each), §11 (the R1, P and S1 rows), §13d (the 17 Jun row), and §15 (both cells — the Bull/Bear table has no content at all, only a Balance paragraph). §15 is effectively a missing section. | 6 [object Object] cells across §3, §6, §11, §13d, §15 | 2 | Re-render all five tables with values; §15 must carry at least three upside and three downside items. |
| 2.2 Scorecard as a table | §6 is a table but lacks Source A, Source B and Final columns (sources appear only as a footnote list) and its Close and Validation columns are empty, so the validated close series — the input to every other number in the report — is never shown. §11 is not the specified R3→P→S3 three-levels-a-side layout: it runs R5→S5 (five levels), its P/R1/S1 rows are blank, and the monthly pivots appear only as prose. | §6 header row; §11 table | 1 | Rebuild §6 with Close/Source A/Source B/Final/Validation populated; rebuild §11 as R3→P→S3 for daily, weekly and monthly. |
| 2.3 Method steps visible | §4 lists observations with basis and relevance, §5 explains normalisation, weighting and the exclusion of futures/CFD/aggregator prints — a genuine observation → classification → consensus chain. §8 is candle-by-candle with an explicit sequence assessment. §9 gives overlap 0.52, persistence 0.52, VOLator readings per instrument and a KER dual-gate resolution. §7 carries five image references with descriptive captions (pandoc drops images; captions accepted as evidence and noted). | §4–§9 | 4 | None blocking; state the numeric inputs behind overlap/persistence. |
| 3.1 Quantitative claims sourced | §1 numbers trace to §4/§6/§21a. §12 and §14 are largely unsourced: "~97% odds of a hold", "PPI jumped to ~6.5% y/y", "roughly 85% of Q1 reporters beat", "8–4 dissent in May", "crude back toward $80" carry no citation, and FactSet's 21.9% is named but undated. The PPI figure also contradicts the reference calendar (PPI y/y 3.900 on 10 Jun). §8's "SpaceX IPO session" has no corresponding §13a row. | §12 all five blocks; §14 bullets; §8 Fri 12 Jun | 2 | Attach a dated source to each §12/§14 figure or delete it; correct or drop the 6.5% PPI claim. |
| 3.2 Citations exist & contain data | Three spot-checks. (a) CNBC 15 Jun "climbed 1.65% to 7,554.29" — the quote, §4 row, §13a row and §13c row agree, and 7,554.29/1.0165 = 7,431.47 matches the 12 Jun close published in the 16 Jun report (7,431.46). Internally consistent. (b) TheStreet 16 Jun 16:05 ET, 7,548.60 (−0.08%) — 7,554.29 × 0.99925 = 7,548.6; consistent with its own quote and with §13a/§13c. (c) S&P DJ Indices (FRED) is dated 15 Jun and quotes 7,554.29, yet §3 calls the (16 Jun) consensus close "triple-corroborated (S&P DJI via FRED, Yahoo, CNBC)" while §5 and §19 both say the 16 Jun close is dual-source — FRED and CNBC are being credited for a close they do not quote. Separately, the report's own Investing.com row (16 Jun range 7,516.75–7,577.92) contradicts §6's 16 Jun H/L of 7,588.9/7,536.4. No source is impossible or self-contradictory in its own quote, so no fabrication finding; the defect is attribution. | §3 Rationale vs §5 and §19; §4 rows 1/3/5 vs §6 | 3 | Change §3 to "dual-source corroborated"; reconcile §6's 16 Jun H/L against the Investing.com range the report itself cites. |
| 3.3 Calculations transparent | RSI2 definition and Trend rule are stated and the arithmetic checks out: the helper, fed the report's own close chain (7,266.99 / 7,394.16 / 7,431.47 / 7,554.29 / 7,548.60 — reconstructed from §1, §13c percentages and §8 range positions because the §6 Close column is empty), returns 100.0 / 100.0 / 95.6 for 12/15/16 Jun, exactly the reported values. Pivots reproduce exactly from the report's own 16 Jun H/L/C: P 7,557.97, R1 7,579.53, S1 7,527.03, R2 7,610.47, S2 7,505.47, R3 7,632.04, S3 7,474.54 vs the quoted 7,558 / 7,580 / 7,527 / 7,610 / 7,505 / 7,632 / 7,475. Against this: ATR(14) is asserted at ~150 with no derivation and is 46% above the slice (103.03 cash / 117.14 full-day); §9 states no ATR at all; and §21a discloses only three of the six weighted components (0.18 + 0.07 + 0.05 = 0.30), so the Σ signal×weight cannot be checked — the sentiment tilt of +0.20 does not reproduce 0.05 at the sentiment weight in the stated default set except at 0.25. | Helper --closes output; §11 vs §6; §21b Risk row; §21a contributor list | 3 | Publish the close column; derive ATR(14) and correct it; list all six signal×weight terms. |
| 3.4 Numbers reconcile | Internally the report is tight — 7,548.60 appears identically in §1, §3, §4, §18, §19 and drives §11 and every card level, and §6 RSI2 95.6 matches §8's "~96". Against the slice it fails: the D-1 close is 7,548.60 vs 7,522.90 (Δ +25.70, tolerance 3), the 15 Jun close 7,554.29 vs 7,563.40 (Δ −9.11), the 15 Jun open/low are off by −63.50/−65.40 and the 10 Jun open by +88.90; §6's 16 Jun RSI2 of 95.6 vs 76.45 on slice closes (Δ 19.15). The USDX direction underpinning §10/§14/§15/§18 is inverted (slice USDX 10 Jun close 100.02 → 16 Jun 99.58, i.e. falling). Three §21c backtest rows quote exits above their own session's stated high: 12 Jun exit 7,554 vs §6 high 7,449.9; 11 Jun Trade 3A exit 7,431 vs high 7,400.2; 15 Jun Trade 3A exit 7,589 vs high 7,561.8. | §5 full reconciliation log below; helper output; §21c rows | 1 | Re-derive the whole §6 table from a corroborated cash source; re-check the USDX direction; rebuild §21c so no fill sits outside its session range. |
| 4.1 Pillars conclude | §8 ends "Indecision — bullish recovery decelerating at resistance", §9 "Transitional / bullish within a transitional structure", §10 "Net cross-asset read is MIXED (one contradict, two confirm)", §12 tags each block price-negative/price-supportive. §14 concludes per bullet but carries no overall macro label. | §8–§10, §12, §14 | 4 | Add a single directional label at the end of §14. |
| 4.2 Peer/cross-asset interpreted | §10 supplies real mechanisms rather than a correlation list — dollar translation drag on multinational earnings, implied-vol collapse removing a tail risk and enabling dip-buying, DAX as a common global-risk factor — and the contradiction flag is carried explicitly into §15 and §18. The mechanism is sound but its premise is wrong: USDX fell over the window on the slice, so the "firm dollar" brake propagates a false input through §14, §15, §18 and the §21a cross-asset dampener. VIX endpoints also overstate ("22.2 spike to ~16" vs slice max 20.86 and D-1 close 17.73). | §10 table and contradiction flag; USDX/VIX slices | 3 | Re-establish the 5-day USDX direction from data before rebuilding the contradiction narrative. |
| 4.3 Synthesis reconciles tensions | §16 does explicitly hold the KER/regime and USDX conflicts open rather than resolving them, and §21a names the KER read as the main internal dissent — good. Against that: §15, the designated bull/bear reconciliation, is entirely empty ([object Object] in both cells), so the Balance paragraph asserts a conclusion with no items behind it; and the cards, which are scored here, break the M5 forks. Trade 1 is issued as a BUY LIMIT at 7,558 — above both its own stated D-1 close (7,548.60) and the slice close (7,522.90), i.e. the wrong side for a buy limit, where M5 specifies market at the 07:00 UK anchor. Trade 2 is a mean-reversion limit at daily S1 under a regime the report itself resolves to TRANSITION, where M5 allows the breakout side only, and its TP2 of 7,610 is +1.46R, not the +2R (7,641) the rule requires. Trade 3 is labelled 3A but built as a breakout stop-entry (a 3C shape), the TRANSITION fork is 3C not 3A, and its TP1 line is self-contradictory on its face ("38.2% extension … ≈ 7,512 below — n/a for long; structural TP1 = 7,653"). | §15 empty table; §16; §21b all three cards vs brief §3 | 1 | Populate §15; rebuild all three cards on the declared regime fork (see feedback file for the numeric conditions). |
| 4.4 Calibrated language | §17 is exactly one sentence, conditional but without hedge stacking. Confidence is stated where required: §3 Medium (split High on the close, Medium on the forward range), §18 Medium (event-gated). Forward range in §16 is bounded and given an explicit invalidation level in both directions. | §3, §16, §17, §18 | 5 | None. |
| 5.1 Data dated; staleness flagged | Every §4 row carries a date and, where relevant, a timestamp; all six §13a articles are dated; §19 gives corroboration status per instrument (close CORROBORATED, intraday H/L SINGLE-SOURCE INDICATIVE, counters directional only) and names the failed sources. Deduction: the per-row Validation column in §6 is empty, so the indicative flag is not visible at row level where it matters. | §4, §13a, §19, §6 Validation column | 4 | Populate §6's Validation column per row. |
| 5.2 Assumptions up front | The 07:00 UK anchor override is stated as an override in the §2 note and logged again in §20; the single-source-indicative pivot inputs and their propagation into Trade 2 are stated in §19 and repeated in the Trade 1 and Trade 2 caveats; the weights basis is logged as unchanged defaults with the lock rule cited. | §2 note, §19, §20, §21b caveats | 5 | None. |
| 5.3 Red flags surfaced | §12 carries the policy, inflation and breadth risks; the FOMC collision is carried into all three card caveat rows; §14 flags VIX complacency into a binary event. Against that, §15 has no risk items at all, and §13d omits the 17 Jun row entirely — the calendar for that session also carries HIGH-impact Retail Sales m/m and Core Retail Sales m/m alongside the FOMC statement, projections and press conference, none of which appear anywhere in the report. | §12; §21b caveats; §13d row 1; NEWS slice 2026-06-17 | 3 | Restore the 17 Jun §13d row with the FOMC block and the retail-sales prints. |
| 5.4 Restrictions honoured | Futures are used for direction only and excluded from the cash OHLC (§4 basis column, §5); retail CFD quotes and after-hours indications are explicitly excluded; instruments are named in common form; no module codes, no framework name, no bracketed variable placeholders. The reconstructed intraday O/H/L are interpolated but are disclosed as such in the §6 header, in §19 and in the card caveats, so they are not presented as sourced — no restriction breach. Residual friction: the §6 footnote "Sources A/B by row" sits directly under a table whose O/H/L are reconstructed, which reads as sourcing them. | §5, §6 header and footnote, §19 | 4 | Move the Sources A/B footnote to close-only, or mark the reconstructed fields inline. |

## 2. Category roll-up

| Category | Level | Multiplier | Points | Justification |
|---|---|---|---|---|
| C1 Prompt adherence (max 20) | 3 | 0.65 | 13.00 | Rows 1.1/1.2/1.3 = 3/2/5, mean 3.33 → 3. Variables, counters, units, anchor and audience are respected; the deductions are the mis-indexed §21c session ladder, the missing 17 Jun §13d row, and a §4 source count that does not bear on the D-1 close as claimed. |
| C2 Structure & completeness (max 20) | 2 | 0.40 | 8.00 | Rows 2.1/2.2/2.3 = 2/1/4, mean 2.33 → 2. Every section exists and the method chain is visible, but six [object Object] cells gut §3, §6, §11, §13d and §15, and §6/§11 do not meet the specified column and level layouts. |
| C3 Accuracy & evidence (max 25) | 2 | 0.40 | 10.00 | Rows 3.1/3.2/3.3/3.4 = 2/3/3/1, mean 2.25 → 2. RSI2 and pivots reproduce from the report's own inputs, but the inputs themselves miss the slice by up to 88.9 pts, the D-1 close is +25.70 against a 3-pt tolerance, ATR(14) is 46% high, USDX direction is inverted, and §12/§14 numbers are unsourced. |
| C4 Reasoning & judgment (max 20) | 3 | 0.65 | 13.00 | Rows 4.1/4.2/4.3/4.4 = 4/3/1/5, mean 3.25 → 3. Pillar labels and calibration are strong and the KER/USDX tensions are held open honestly; the empty §15 and three cards that contradict the report's own TRANSITION fork and the M5 geometry pull 4.3 to 1. |
| C5 Currency, restrictions & transparency (max 15) | 4 | 0.85 | 12.75 | Rows 5.1/5.2/5.3/5.4 = 4/5/3/4, mean 4.0 → 4. Dating, the anchor-override disclosure and the single-source-indicative propagation are handled well and no restriction is breached; deductions for the empty §6 Validation column, the empty §15 risk table and the missing 17 Jun calendar row. |
| **Total** | — | — | **56.75 → 57** | Sum of category points, rounded to a whole number. |

## 3. Total, band, override check

- Raw total: 13.00 + 8.00 + 10.00 + 13.00 + 12.75 = **56.75 → 57**.
- Band: **Low** (40–59).
- Hallucinated-source override: **not triggered**. Three cited sources were spot-checked (CNBC 15 Jun, TheStreet 16 Jun, S&P DJ Indices/FRED 15 Jun). Each is named, dated and quotes a figure that is used consistently where it appears; the CNBC and TheStreet figures also chain arithmetically (7,554.29 × 0.99925 → 7,548.60) and the implied 12 Jun close of 7,431.47 matches the 12 Jun close published in the report dated 16 Jun (7,431.46). The defect found is misattribution in §3 ("triple-corroborated" for a close that §5 and §19 both call dual-source), not an impossible or invented source. C3 therefore stays at its checklist level of 2 rather than being forced to 0.
- Restriction-breach override: **not triggered**. ES futures are confirmation-only and excluded from the cash OHLC; retail CFD quotes and after-hours indications are explicitly excluded; no module codes, framework name or bracketed variable names appear; instruments use common names. The interpolated intraday O/H/L are the one candidate, but they are disclosed as reconstructed and flagged indicative in §6, §19 and the card caveats, so they are not presented as sourced. The [object Object] cells are a rendering failure, scored under 2.1/2.2, not a variable-name leak.
- No cap applied; final Trust Score **57 (Low)**.

## 4. Card Integrity

Linter rows, verbatim from `qa/regen_20260906_qa1/lint_static/2026-06-17.csv`:

| card_id | report_date | strategy | flags | dud |
|---|---|---|---|---|
| 2026-06-17_Trade_1 | 2026-06-17 | Trade 1 - Daily Directional | CLEAN | False |
| 2026-06-17_Trade_2 | 2026-06-17 | Trade 2 - Pivot (buy limit daily S1) | CLEAN | False |
| 2026-06-17_Trade_3A | 2026-06-17 | Trade 3A - Momentum-Pullback (breakout stop) | CLEAN | False |

Per-card integrity (100 − 40·#DUD − 10·#WARN, floored at 0):

| Card | #DUD | #WARN | Integrity |
|---|---|---|---|
| 2026-06-17_Trade_1 | 0 | 0 | 100 |
| 2026-06-17_Trade_2 | 0 | 0 | 100 |
| 2026-06-17_Trade_3A | 0 | 0 | 100 |

Non-suppressed cards: 3. **Report mean Card Integrity = 100.0.**

M5 construction assessment (feeds checklist row 4.3, not the integrity number above):

| Card | M5 rule (brief §3) | Observed | Verdict |
|---|---|---|---|
| Trade 1 | Market at the daily-open anchor; a MARKET entry equals the D-1 close; a LIMIT sits on the correct side of the D-1 close | BUY LIMIT 7,558 (daily P) with a conditional "market at the 07:00 UK anchor if already above P"; 7,558 is 9.40 above its own stated close and 35.10 above the slice close 7,522.90 | FAIL — dual-mode entry, and the limit is on the wrong side for a long |
| Trade 1 | Stop = tighter of (5-day swing extreme, nearest S/R) + 0.25×ATR, capped 3.5×ATR; R bounds 0.3–3.0×ATR14; ATR stated | Stop 7,475 (daily S3), R = 83 pts, ATR(14) asserted ~150 vs slice 103.03 | PARTIAL — R sits inside 0.3–3.0×ATR on the true ATR, but the stated ATR is 46% high, so the 3×ATR runner cap and the 3.5×ATR stop cap are both mis-scaled |
| Trade 1 | TP1 = entry+1R, TP2 = entry+2R; TP3 in price and points | 7,641 (+1R) and 7,724 (+2R) reproduce exactly; TP3 is prose only ("trail"), yet the extracted card carries tp3 = 7,800, a level the report never states (3×ATR from 7,558 at the stated ATR would be 8,008) | PARTIAL — TP1/TP2 correct, TP3 unsourced |
| Trade 2 | TRANSITION → breakout side only | Buy limit at daily S1 7,527, a RANGE mean-reversion construction, under a regime §9 explicitly resolves to TRANSITION | FAIL — wrong regime branch |
| Trade 2 | RANGE TP2 = entry ± 2R; LIMIT on the correct side of the D-1 close | TP2 7,610 = entry + 83 = +1.46R (2R would be 7,641); entry 7,527 is 4.10 above the slice D-1 close 7,522.90 | FAIL on both |
| Trade 3A | TRANSITION forks to 3C, not 3A; 3A is a 57.5% retrace limit with stop 0.25×ATR beyond the anchor, TP1 38.2%, TP2 0%, TP3 100%+ | Labelled "3A — regime fork: TRANSITION → 3A" but built as a BUY STOP breakout at 7,590 over the 16 Jun high, with a TP1 row that states its own Fibonacci output is "n/a for long" and substitutes an unexplained "structural TP1 = 7,653" | FAIL — wrong fork, wrong geometry, self-contradictory TP1 |
| All cards | Thesis invalidation separate from the stop; confluences listed; single-source-indicative flag propagated; stops/targets in price and points | Invalidation and confluences present on all three; the indicative flag is carried on Trade 1 and Trade 2 but not on Trade 3A, whose entry 7,590 is derived from the indicative 16 Jun high 7,588.9; Trade 2 TP2 and both Trade 3A TPs are given in price only | PARTIAL |

## 5. Data reconciliation log

Tolerances per brief §4: |Δ| ≤ 3 pts on a close, ≤ 8 pts on an open/high/low. Slice values are cash-session.

| Section | Report value | Slice value | Delta | Verdict |
|---|---|---|---|---|
| §6 10 Jun Open | 7,440.0 | 7,351.10 | +88.90 | FAIL |
| §6 10 Jun High | 7,470.3 | 7,400.70 | +69.60 | FAIL |
| §6 10 Jun Low | 7,244.1 | 7,271.50 | −27.40 | FAIL |
| §6 10 Jun Close | not stated ([object Object]); §1 implies 7,266.99 | 7,271.70 | −4.71 | FAIL (marginal; and the column is empty) |
| §6 11 Jun Open | 7,286.5 | 7,305.00 | −18.50 | FAIL |
| §6 11 Jun High | 7,400.2 | 7,416.60 | −16.40 | FAIL |
| §6 11 Jun Low | 7,270.8 | 7,260.00 | +10.80 | FAIL |
| §6 11 Jun Close | not stated; §13c +1.75% implies 7,394.16 | 7,391.90 | +2.26 | PASS |
| §6 12 Jun Open | 7,402.1 | 7,420.90 | −18.80 | FAIL |
| §6 12 Jun High | 7,449.9 | 7,458.70 | −8.80 | FAIL (marginal) |
| §6 12 Jun Low | 7,388.4 | 7,363.90 | +24.50 | FAIL |
| §6 12 Jun Close | not stated; back-derived 7,431.47 from 15 Jun +1.65% | 7,431.90 | −0.43 | PASS |
| §6 15 Jun Open | 7,470.6 | 7,534.10 | −63.50 | FAIL |
| §6 15 Jun High | 7,561.8 | 7,583.40 | −21.60 | FAIL |
| §6 15 Jun Low | 7,468.2 | 7,533.60 | −65.40 | FAIL |
| §6 15 Jun Close (§4, §13c) | 7,554.29 | 7,563.40 | −9.11 | FAIL |
| §6 16 Jun Open | 7,555.1 | 7,562.90 | −7.80 | PASS |
| §6 16 Jun High | 7,588.9 | 7,571.40 | +17.50 | FAIL |
| §6 16 Jun Low | 7,536.4 | 7,518.20 | +18.20 | FAIL |
| §1/§3/§4/§6/§18/§19 D-1 close | 7,548.60 | 7,522.90 | +25.70 | FAIL — Category 3 failure (>10 pts) |
| §6 RSI2 10 Jun | 0.0 | 0.00 | 0.00 | PASS |
| §6 RSI2 11 Jun | 51.9 | 50.98 | +0.92 | PASS |
| §6 RSI2 12 Jun | 100.0 | 100.00 | 0.00 | PASS |
| §6 RSI2 15 Jun | 100.0 | 100.00 | 0.00 | PASS |
| §6 RSI2 16 Jun | 95.6 | 76.45 | +19.15 | FAIL (consequence of the +25.70 close error) |
| §6 RSI2 arithmetic from the report's own closes | 100.0 / 100.0 / 95.6 (12/15/16 Jun) | helper on 7,266.99 / 7,394.16 / 7,431.47 / 7,554.29 / 7,548.60 → 100.0 / 100.0 / 95.6 | 0.00 | PASS — the formula is applied correctly to the report's own inputs |
| §11 daily pivots from the report's own 16 Jun H/L/C | P 7,558 · R1 7,580 · S1 7,527 · R2 7,610 · S2 7,505 · R3 7,632 · S3 7,475 | recomputed 7,557.97 · 7,579.53 · 7,527.03 · 7,610.47 · 7,505.47 · 7,632.04 · 7,474.54 | ≤ 0.54 | PASS — internally reproducible (though the P/R1/S1 rows are blank in the table) |
| §11 daily P vs slice | 7,558 | 7,537.50 | +20.50 | FAIL |
| §11 daily R1 vs slice | 7,580 | 7,556.80 | +23.20 | FAIL |
| §11 daily S1 vs slice | 7,527 | 7,503.60 | +23.40 | FAIL |
| §11 daily R2 / S2 vs slice | 7,610 / 7,505 | 7,590.70 / 7,484.30 | +19.30 / +20.70 | FAIL |
| §11 daily R3 / S3 vs slice | 7,632 / 7,475 | 7,610.00 / 7,450.40 | +22.00 / +24.60 | FAIL |
| §11 weekly R2 / R3 | 7,608 / 7,746 | 7,630.43 / 7,774.47 | −22.43 / −28.47 | FAIL |
| §11 weekly S2 / S3 | 7,156 / 7,067 | 7,143.83 / 7,044.57 | +12.17 / +22.43 | FAIL |
| §11 weekly R1 (narrative band 7,520–7,608) | 7,520 | 7,531.17 | −11.17 | FAIL |
| §11 monthly P (May basis) | 7,460 | 7,454.70 | +5.30 | PASS |
| §11 monthly R1 (May basis) | 7,741 | 7,731.90 | +9.10 | PASS (marginal) |
| §21b ATR(14) | ~150 | 103.03 cash / 117.14 full-day | +46.97 / +32.86 | FAIL |
| §8/§21b 15 Jun swing low used as stop anchor | 7,468 | 15 Jun low 7,533.60; 5-day swing low 7,260.00 (11 Jun) | −65.60 | FAIL |
| §8/§16 "late-May 7,620 structural high" | 7,620 | late-May high 7,601.80; 25-day high 7,624.60 dated 2 Jun | +18.20 / mis-dated | FAIL |
| §9/§10/§14 VIX spike | 22.2 | slice max 20.86 (11 Jun high) | +1.34 | FAIL |
| §9/§10/§14 VIX current | ~16 | D-1 close 17.73 | −1.73 | FAIL |
| §10/§14/§15/§18 USDX 5-day direction | Rising | 10 Jun close 100.02 → 16 Jun close 99.58 (−0.44) | direction inverted | FAIL — material, propagates to the contradiction flag and §21a |
| §12/§13c May CPI y/y | 4.2% | calendar actual 4.200 (10 Jun) | 0.00 | PASS |
| §12 Core CPI | 0.2% m/m / 2.9% y/y | calendar actual 0.200 / 2.900 | 0.00 | PASS |
| §12/§13c PPI y/y | ~6.5% | calendar PPI y/y actual 3.900 (10 Jun) | +2.6 pp | FAIL |
| §13c housing starts m/m | −15.4% | calendar actual −15.400 (16 Jun) | 0.00 | PASS |
| §12 funds rate | 3.50–3.75% | calendar Fed rate previous 3.750 | 0.00 | PASS |
| §13d 17 Jun row | [object Object] | calendar 17 Jun: FOMC Statement, FOMC Economic Projections, Fed Rate Decision (HIGH), FOMC Press Conference (HIGH), Retail Sales m/m (HIGH), Core Retail Sales m/m (HIGH) | row absent | FAIL |
| §21c 12 Jun Trade 1 exit | 7,554 | report's own 12 Jun high 7,449.9 (slice 7,458.70) | +104.1 above the session high | FAIL — fill impossible on the report's own data |
| §21c 11 Jun Trade 3A exit | 7,431 | report's own 11 Jun high 7,400.2 (slice 7,416.60) | +30.8 above the session high | FAIL |
| §21c 15 Jun Trade 3A exit | 7,589 | report's own 15 Jun high 7,561.8 (slice 7,583.40) | +27.2 above the session high | FAIL |
| §3 corroboration claim | "Triple-corroborated close (S&P DJI via FRED, Yahoo, CNBC)" | §5 and §19 both state the 16 Jun close is dual-source (Yahoo, TheStreet); FRED and CNBC quote 15 Jun | contradiction | FAIL — internal |
| §4 Investing.com 16 Jun range vs §6 16 Jun H/L | 7,516.75–7,577.92 vs 7,588.9/7,536.4 | slice 7,518.20–7,571.40 | Investing.com is within 1.45 / 6.52 of the slice; §6 is not | FAIL — the report down-weighted the one source that reconciles |
