# Trust Score — 2026-06-18 — SP500_Report_18Jun2026.md

Reviewed under `docs/AI_Output_Trust_Score_Framework_v3.7.txt` §4–§7 with the anchors in
`qa/regen_20260906_qa1/REVIEWER_BRIEF.md`. Data basis: `data/slices/US500/US500_upto_2026-06-17.csv`
(cash session 16:30–23:00 broker), plus VIX/USDX/NEWS slices to D-1. Helper run:
`engine/qa_slice_stats.py --date 2026-06-18 --closes 7394.30 7445.00 7554.29 7511.35 7420.43`.

## 1. Section 7 checklist

| Item | Reviewer notes | Evidence observed | Score 0–5 | Action required |
|---|---|---|---|---|
| 1.1 Variables respected | Asset is the S&P 500 cash index and explicitly "not the ES futures contract"; counters are Dollar Index · VIX · DAX 40 with USDX first; as-of 17 Jun close, America/New_York; lookback 5 sessions (execution) + 25 (regime); index points · USD; daily-open anchor 07:00 UK stated in §2 and §20 and carried onto the Trade 1 card. Gaps: tick size 0.01 is never stated anywhere; §2's anchor wording "(overridden as instructed for the 18 June run)" does not say what was overridden to what; a build tag "v2.1" leaks into §20. Source count met (6 rows in §4, 7 in §13a, sell-side tier present via Goldman/JPMorgan/Principal). | §2, §4, §10, §13a, §20, §21b | 4 | Add tick size to §2; restate the anchor line as a plain statement of the 07:00 UK anchor; drop the internal version tag. |
| 1.2 Coverage & currency consistent | All price/data dates are D-1 or earlier; §13c is previous-period, §13d forward-only; units stay index points/USD throughout. Drift: §6's 15–16 Jun O/H/L contradict the 17 Jun report's own table for the same sessions (16 Jun H 7,551.0 vs 7,588.9; L 7,470.0 vs 7,536.4); §14's "USDX firm near 99.5–99.9" is stale against the D-1 USDX close of 100.425; §9's "1 Jun 7,600 print" does not match the 25-day high of 7,624.60 dated 2 Jun in the slice. | §6, §9, §14; cross-check `reports/md/SP500_Report_17Jun2026.md` §6 | 3 | Re-cut §6 O/H/L from one basis and reconcile against the prior report; re-date/re-level the USDX and 25-day-high references. |
| 1.3 Audience & tone | Senior US Equity Strategist register held throughout; framed for trading and risk review; no retail promotional tone; the "not investment advice / forward-test output for risk review" boilerplate closes §21d. | §1, §18, §21d | 5 | None. |
| 2.1 Sections present & ordered | §1–§21 all present in order, including §13a per-article, §13b aggregate with a numeric tilt (−1.00), §13c previous-period and §13d upcoming calendars, and §21a/§21b/§21c/§21d. §17 is a single sentence. | headings, whole report | 5 | None. |
| 2.2 Scorecard as a table | §6 is a table but is missing the Source A, Source B and Final columns the structure requires — it carries only Date/O/H/L/C/RSI2/Trend/Validation, so per-row provenance is collapsed into one free-text cell. All three §11 pivot tables (daily, weekly, monthly) are ordered R3→S2 and omit S3 entirely, i.e. three levels above the pivot but only two below, not the required three per side. | §6, §11 | 2 | Restore Source A / Source B / Final columns in §6; add the S3 row to the daily, weekly and monthly pivot tables. |
| 2.3 Method steps visible | §4 lists raw observations with basis and classification, §5 explains the normalisation and the reconciliation to the accepted close; §8 is candle-by-candle for all five sessions and ends in an explicit sequence assessment; §9 gives regime, range-position, persistence proxy and VOLator; §7 carries five captioned chart placeholders (pandoc has dropped the images — captions accepted as evidence and noted here). | §4–§9 | 5 | None; re-attach chart images if the deliverable is rendered outside pandoc. |
| 3.1 Quantitative claims sourced | The §6/§4/§13 chain is pointed to for prices, and Oppenheimer is named for the earnings figures. But a large block of numbers carries no source and no pointer: VIX "16.1 lows" and "collapsing from 22 on 10 June" (§9), USDX "99.5–99.9" (§14), 2-year "~14–16 bp toward 4.2%" and 10-year "~4.47%" (§14), PCE 3.6% and median funds rate 3.8% (§12), PPI 6.5% y/y (§12/§14), median 25-day RSI2 69.1, directional-persistence proxy 0.72 and the 41st-percentile range position (§9), and ATR≈94 (§21b). Several of these are also wrong against the slice (see §5 below). | §1, §9, §12, §14, §21b | 2 | Attach a source or an internal §4/§6/§13 pointer to every number in §1, §9, §12 and §14, or delete the number. |
| 3.2 Citations exist & contain data | Three spot-checks. (i) S&P Dow Jones (via FRED), 16 Jun close 7,511.35 — used identically in §6 and matched by the §20 corroboration line (FRED × Yahoo, Δ 0.00): internally consistent. (ii) Investing.com, 17 Jun O 7,524.50 / H 7,532.17 / L 7,402.61 — carried verbatim into the §6 17 Jun row and into §8's "gap-up open to 7,524.5": internally consistent, but §19 simultaneously states the Investing.com history tables "did not return machine-readable OHLC at run time", which sits awkwardly with a three-field decimal quote. (iii) GuruFocus / TheStreet, 15 Jun close "7,554.29 (+1.60%)" — the +1.60% inside the quote implies a prior close of 7,435.3, not the 7,445.00 the report's own §6 carries for 12 Jun; and §4 classifies this row "Directional" while §6 validates the same session as "Corroborated (Δ<0.10)". Two further provenance breaks: §3 and §19 assert the 17 Jun close is corroborated by the S&P Dow Jones official series via FRED, but §4 has no FRED/S&P DJI row for 17 Jun and §20 records the corroboration as "Traders Union × TradingKey" only; and §4 contains no source row at all for the 12 Jun close, which §6 nonetheless marks "Close corrob.". No cited source is demonstrably fabricated or impossible, so the hallucination override is NOT triggered, but the provenance chain is unreliable. | §3, §4, §6, §19, §20 | 2 | Add a §4 evidence row for every close that §6 marks corroborated (12 Jun missing); align §3/§19/§20 provenance claims with what §4 actually contains; reconcile the 15 Jun "+1.60%" with the stated 12 Jun close. |
| 3.3 Calculations transparent | RSI2 does not reproduce from the report's own close column on any of the three testable rows: helper recomputation from 7394.30 / 7445.00 / 7554.29 / 7511.35 / 7420.43 gives 100.0 / 71.8 / 0.0 for 15, 16 and 17 Jun against the stated 88.9 / 60.4 / 25.6. This is the explicit Category 3 failure named in the brief. Trend labels are, however, self-consistent with the stated RSI2 and would survive correction. §11 daily pivots DO reproduce exactly from the report's own 17 Jun H/L/C (P 7451.74→7452, R1 7500.89→7501, R2 7581.34→7581, R3 7630.49→7630, S1 7371.29→7371, S2 7322.14→7322); weekly and monthly tables are internally consistent (implied weekly H 7,461 / L 7,256; monthly H 7,585 / L 7,353), but S3 is computed nowhere. ATR(14) is never stated in §9 and appears only as "ATR≈94" on the Trade 1 card. KER is given as "smoothed efficiency ratio −0.13" without the (13, EMA 3) parameters. §21a shows only three of six weighted components (−0.21 + −0.15 + −0.15 = −0.51) against a stated score of −0.68 — the remaining −0.17 is unexplained. | §6, §8, §9, §11, §21a | 1 | Recompute the RSI2 column from the accepted closes and propagate to §8; state ATR(14) and the KER parameters in §9; publish all six weighted components of the §21a score; add S3. |
| 3.4 Numbers reconcile | The D-1 close 7,420.43 is identical in §1, §3, §4, §6 and the §21b Trade 1 entry; §11 pivots are quoted correctly on all three cards (Trade 1 stop 7,501 = daily R1; Trade 2 stop 7,506 = monthly P; Trade 3C stop 7,427 = monthly S1, TP1 7,322 = daily S2, TP2 7,275 = monthly S2, TP3 7,182 = weekly S2); §6 RSI2 = §8 RSI2; the range-position percentages in §1/§8 (14%, 96%, 79%, 95%, 51%) all reproduce from the stated OHLC. Breaks: ATR appears only in §21b, never in §9; the 15 Jun "+1.60%" is inconsistent with the stated 12 Jun close; §6's 15–16 Jun O/H/L contradict the immediately preceding report; the extracted Trade 1 card carries tp3 = 7,180, a level that appears nowhere in the report text. | cross-section; `cards/baseline/by_date/2026-06-18.json` | 2 | State ATR(14) in §9 and reuse the same figure in §21b; state Trade 1 TP3 as a price in the report; fix the 12/15 Jun close-vs-percentage break. |
| 4.1 Pillars conclude | §8 ends "Judgement label: Exhaustion — reversal risk"; §9 ends "Bias: Bearish (short-term) within a maturing medium-term uptrend"; §10 gives an aggregate cross-asset read; §12 labels each driver price-negative/supportive/two-sided; §14 argues a direction but never states a label. The §9 conclusion is internally inconsistent with its own input: a smoothed efficiency ratio of −0.13 (slice EMA3 of the signed ER13 = −0.114, so the value itself is fine) is a low-efficiency, choppy reading, yet it is labelled "Trending Down — Strong" and then fed into §21a at full weight (−0.15 on a 0.15 weight = a −1.0 signal). The same section simultaneously calls the regime "Transitional". | §8, §9, §10, §12, §14 | 3 | Give §14 an explicit label; re-derive the Kaufman classification from the stated ER magnitude and re-weight the §21a Kaufman signal accordingly. |
| 4.2 Peer/cross-asset interpreted | §10 is a mechanism table, not a correlation list: rate-differential USD strength as a translation headwind for multinational earnings, an implied-vol bid as risk-premium expansion, and the DAX as a common global-risk factor with named idiosyncratic drags. It closes with an aggregate read that is carried into §15 and §18. | §10, §15, §18 | 5 | None. |
| 4.3 Synthesis reconciles tensions & card construction | §15 sets bull/bear against named level triggers, §16 states a base case with an explicit invalidation, §18 gives three ranked reasons, §21a asserts no conflict with §17. But the central tension — a "maturing uptrend"/"Transitional" medium term versus a "Trending Down — Strong" Kaufman label — is asserted as agreement rather than reconciled, and the earnings cushion is listed rather than weighed. Card construction (scored here per the QA protocol) is the larger failure: Trade 1's stop is daily R1 (7,501) rather than the M5 "tighter of (5-day swing extreme, nearest S/R) + 0.25×ATR" construction; Trade 2 is a mean-reversion limit fade taken under a regime the report itself calls Transitional (M5: transition → breakout side only) and its 7,450 limit sits on no R-tier at all; Trade 3C is labelled a 25-day momentum breakout but is built off daily S1, not the 25-day boundary, with TP1/TP2 of 47/94 points against a 25-day width of 381.5; Trade 2 and Trade 3C both state an invalidation identical to their stop, violating "thesis invalidation separate from the stop"; Trade 3C carries no 0.2R break-even rule (card `be_rule: NONE`); Trade 2 and Trade 3C have no Confluences field; targets are given in price only, not price and points. | §15–§18, §21a, §21b | 2 | Rebuild all three cards to the M5 constructions with the numeric conditions listed in the feedback file; reconcile the KER label against the regime call. |
| 4.4 Calibrated language | §17 is exactly one sentence and does not stack hedges; §3 states confidence "High (close)"; §21a states the conviction and the threshold test. But "High" confidence is asserted for a level whose evidence chain is uncorroborated for four of five rows, and "Trending Down — Strong" overstates a −0.13 efficiency reading; §9's "increasing downside confidence" compounds it. | §3, §9, §17, §21a | 3 | Downgrade the stated confidence to match the corroboration actually shown in §4, and soften the Kaufman strength label. |
| 5.1 Data dated; staleness flagged | Every §6 row and every §4 observation is dated; §13c/§13d entries are dated. Two gaps: §13a has no date column at all — the seven articles are undated, so recency cannot be judged; and the single-source-indicative flag is applied to the 11–12 Jun High/Low and the weekly prior-week High/Low but NOT to the 11–12 Jun Opens, nor to the 15–16 Jun O/H/L, which are equally unsupported by §4 yet validated as "Corroborated". | §4, §6, §13a, §19 | 2 | Add a date column to §13a; extend the indicative flag to every O/H/L field that §4 does not source. |
| 5.2 Assumptions up front | The anchor override is stated twice (§2 and the §20 Agent Log) and the card entry reads "Market at 07:00 UK", matching the extracted card (`anchor_broker: 09:00` = 07:00 UK). Single-source propagation is disclosed in §19 and carried into the caveat line of all three cards. The direction-score weights are stated and declared untuned. | §19, §20, §21b | 4 | Say explicitly in §2 what the anchor was overridden from. |
| 5.3 Red flags surfaced | §12 and §15 carry the policy, inflation and geopolitical risks with a two-sided treatment of the Iran MoU; §13d event collisions are carried into the Trade 1 and Trade 3C caveats. Gaps against the calendar slice: §13d omits two HIGH-impact events scheduled for D — the BoE Interest Rate Decision (18 Jun 14:00 broker) and the Philadelphia Fed Manufacturing Index (18 Jun 15:30 broker) — and grades Initial Jobless Claims "Med" where the calendar grades it HIGH. Trade 2's caveat covers fill risk but no event collision. | §12, §13d, §15, §21b; `data/slices/NEWS/news_upto_2026-06-17.csv` | 3 | Add the two omitted HIGH-impact D-session events to §13d, correct the claims impact grade, and propagate the collision to the Trade 2 caveat. |
| 5.4 Restrictions honoured | BREACH. The no-synthesis restriction ("no synthesised/interpolated price presented as sourced") is openly violated in §6: the 15 Jun and 16 Jun rows are validated "Corroborated (Δ<0.10)" and "Corroborated (Δ 0.00)" although §4 sources only their closes and provides no O/H/L for either session; the values presented (7,455.0 / 7,560.0 / 7,450.0 and 7,548.0 / 7,551.0 / 7,470.0) are round-number reconstructions that miss the slice by up to 83.6 points, and the 12 Jun close is marked "Close corrob." with no §4 source at all. Second breach: the sole basis given for the D-1 close in §4 is "Traders Union / TradingKey", retail broker-facing outlets, against the restriction on retail quotes in the OHLC basis — §20 confirms this was the only corroboration pair used. Honoured: ES futures excluded and named as excluded; no bracketed variable names, module codes or framework name (only a stray "v2.1" build tag in §20); instrument common names used throughout. | §4, §6, §19, §20 | 1 | Remove the "Corroborated" validation from any row whose O/H/L §4 does not source, or source them; replace the retail-outlet corroboration of the D-1 close with an index-provider/exchange tier source. |

## 2. Category roll-up

| Category | Level | Multiplier | Points | Justification |
|---|---|---|---|---|
| C1 Prompt adherence (20) | 3 | 0.65 | 13.00 | Rows 1.1/1.2/1.3 = 4/3/5, mean 4.0 → level 4; reduced one level to 3 by the restriction-breach override (row 5.4). |
| C2 Structural alignment (20) | 4 | 0.85 | 17.00 | Rows 2.1/2.2/2.3 = 5/2/5, mean 4.0. Every section present and ordered and the method chain fully visible; the §6 table is missing its Source A/B/Final columns and all three §11 tables omit S3. |
| C3 Accuracy & evidence (25) | 2 | 0.40 | 10.00 | Rows 3.1/3.2/3.3/3.4 = 2/2/1/2, mean 1.75 → level 2. RSI2 fails to reproduce from the report's own closes on all three testable rows; two closes are wrong by more than 10 points against the slice; 14 of 20 §6 OHLC fields sit outside tolerance; provenance claims exceed what §4 contains. |
| C4 Reasoning & judgment (20) | 3 | 0.65 | 13.00 | Rows 4.1/4.2/4.3/4.4 = 3/5/2/3, mean 3.25 → level 3. Cross-asset reasoning is genuinely mechanistic, but the Kaufman label contradicts its own input and all three cards depart from the M5 constructions. |
| C5 Currency, restrictions & transparency (15) | 3 | 0.65 | 9.75 | Rows 5.1/5.2/5.3/5.4 = 2/4/3/1, mean 2.5 → level 3 (half rounded up). Anchor and single-source caveats are properly disclosed and propagated; undated §13a, unflagged synthesised O/H/L and the restriction breach pull it down. |
| **Total** | | | **62.75 → 63** | Sum of the five weighted contributions, rounded to the nearest whole number. |

## 3. Total, band, override check

- **Raw total: 62.75 → 63.**
- **Band: Moderate Trust (60–74).** Output must not be used as-is; suitable as an input to human-led analysis, with targeted regeneration of the weakest categories (C3 and C4).
- **Hallucinated-source override: NOT triggered.** All three spot-checked citations are named, carry a figure, and that figure is used consistently in the body. The defects found are unsupported provenance claims (§3/§19 assert FRED corroboration of the 17 Jun close that §4 and §20 do not show; §4 carries no source row for the 12 Jun close that §6 validates) and one quote-internal inconsistency (15 Jun "+1.60%" implies a prior close of 7,435.3 against the stated 7,445.00). No cited source is fabricated or impossible, so C3 is scored on the rubric rather than zeroed. This call should be revisited if the regeneration cannot produce the FRED 17 Jun and 12 Jun close rows it claims to have used.
- **Restriction-breach override: TRIGGERED.** The no-synthesised-price-presented-as-sourced restriction is openly violated in §6 (15 and 16 Jun rows validated "Corroborated" with no §4 O/H/L behind them and slice deltas up to 83.6 points; 12 Jun close marked "Close corrob." with no §4 source), and the retail-quote restriction is violated by using Traders Union / TradingKey as the only corroboration pair for the D-1 close. Effect: total capped at 74 and C1 reduced one rubric level (4 → 3). The cap is not numerically binding — 63 already sits inside the Moderate band — but C1 was reduced as required, which is reflected in the 13.00 points above.
- **Override recorded for the roll-up CSV: `restriction_breach`.**

## 4. Card Integrity

Linter rows, copied verbatim from `qa/regen_20260906_qa1/lint_static/2026-06-18.csv`:

| card_id | report_date | strategy | flags | dud |
|---|---|---|---|---|
| 2026-06-18_Trade_1 | 2026-06-18 | Trade 1 - Daily Directional | CLEAN | False |
| 2026-06-18_Trade_2 | 2026-06-18 | Trade 2 - Pivot (sell limit monthly S1 / daily P) | CLEAN | False |
| 2026-06-18_Trade_3C | 2026-06-18 | Trade 3C - Momentum-Breakout (sell stop) | CLEAN | False |

Per-card integrity, `100 − 40·(#DUD) − 10·(#WARN)`, floored at 0:

| Card | #DUD | #WARN | Integrity |
|---|---|---|---|
| 2026-06-18_Trade_1 | 0 | 0 | 100 |
| 2026-06-18_Trade_2 | 0 | 0 | 100 |
| 2026-06-18_Trade_3C | 0 | 0 | 100 |

**Report mean over non-suppressed cards (3 of 3): 100.0.** No card is suppressed in this report.

All three cards clear the static geometry the engine enforces — stop on the correct side of entry for a
short, TP1 beyond entry, TP2 beyond TP1, TP3 beyond TP2, R within 0.3–3.0×ATR14 (slice ATR14 = 108.09, so
32.4 ≤ R ≤ 324.3; the cards run 81, 56 and 58 points), TP1 within 2.5×ATR14 (270.2) of entry, the MARKET
entry equal to the stated D-1 close, the LIMIT at 7,450 and the STOP at 7,369 on the correct sides of that
close, and an explicit anchor. A clean integrity score is therefore not a statement that the cards are
M5-compliant: the construction defects recorded under row 4.3 and itemised in the feedback file are
invisible to the static linter by design.

## 5. Data reconciliation log

Slice basis: `data/slices/US500/US500_upto_2026-06-17.csv`, cash session 16:30–23:00 broker.
Tolerance per the brief: |Δ| ≤ 3.0 on a close, |Δ| ≤ 8.0 on an open/high/low.

| Section | Report value | Slice value | Delta | Verdict |
|---|---|---|---|---|
| §6 11 Jun Open | 7,270.0 | 7,305.0 | −35.0 | FAIL (>8) |
| §6 11 Jun High | 7,400.0 | 7,416.6 | −16.6 | FAIL (>8) |
| §6 11 Jun Low | 7,255.0 | 7,260.0 | −5.0 | Within tolerance |
| §6 11 Jun Close | 7,394.30 | 7,391.9 | +2.40 | Within tolerance |
| §6 12 Jun Open | 7,400.0 | 7,420.9 | −20.9 | FAIL (>8) |
| §6 12 Jun High | 7,460.0 | 7,458.7 | +1.30 | Within tolerance |
| §6 12 Jun Low | 7,390.0 | 7,363.9 | +26.1 | FAIL (>8) |
| §6 12 Jun Close | 7,445.00 | 7,431.9 | +13.10 | FAIL — close wrong by >10, Category 3 failure |
| §6 15 Jun Open | 7,455.0 | 7,534.1 | −79.1 | FAIL (>8) |
| §6 15 Jun High | 7,560.0 | 7,583.4 | −23.4 | FAIL (>8) |
| §6 15 Jun Low | 7,450.0 | 7,533.6 | −83.6 | FAIL (>8) — largest single-field error in the table |
| §6 15 Jun Close | 7,554.29 | 7,563.4 | −9.11 | FAIL (>3) |
| §6 16 Jun Open | 7,548.0 | 7,562.9 | −14.9 | FAIL (>8) |
| §6 16 Jun High | 7,551.0 | 7,571.4 | −20.4 | FAIL (>8) |
| §6 16 Jun Low | 7,470.0 | 7,518.2 | −48.2 | FAIL (>8) |
| §6 16 Jun Close | 7,511.35 | 7,522.9 | −11.55 | FAIL — close wrong by >10, Category 3 failure |
| §6 17 Jun Open (D-1) | 7,524.5 | 7,531.7 | −7.20 | Within tolerance |
| §6 17 Jun High (D-1) | 7,532.2 | 7,540.0 | −7.80 | Within tolerance |
| §6 17 Jun Low (D-1) | 7,402.6 | 7,408.5 | −5.90 | Within tolerance |
| §6 17 Jun Close (D-1) | 7,420.43 | 7,427.50 | −7.07 | FAIL (>3) — propagates to §1, §3, §18 and the Trade 1 entry |
| §6 RSI2 11 Jun | 57.3 | 50.98 (slice closes) | +6.32 | Not independently testable from report closes (window start) |
| §6 RSI2 12 Jun | 72.2 | 100.00 (slice closes) | −27.8 | Not independently testable from report closes (window start) |
| §6 RSI2 15 Jun | 88.9 | 100.00 slice / 100.0 from report's own closes | −11.1 | FAIL — does not reproduce from the report's own close column |
| §6 RSI2 16 Jun | 60.4 | 76.45 slice / 71.8 from report's own closes | −11.4 | FAIL — does not reproduce from the report's own close column |
| §6 RSI2 17 Jun | 25.6 | 0.00 slice / 0.0 from report's own closes | +25.6 | FAIL — two consecutive down closes force RSI2 = 0 |
| §6 Trend labels (all five rows) | Bullish/Bullish/Bullish/Neutral/Bearish | Rule applied to the report's own O/C and RSI2 | 0 | Consistent — labels survive the RSI2 correction |
| §11 daily P | 7,452 | 7,451.74 from report's own 17 Jun H/L/C (slice-derived P 7,458.67) | +0.26 / −6.67 | Reproduces from the report's own inputs; offset vs slice is basis-driven |
| §11 daily R1 / R2 / R3 | 7,501 / 7,581 / 7,630 | 7,500.89 / 7,581.34 / 7,630.49 from report's own H/L/C | ≤0.49 | Reproduces |
| §11 daily S1 / S2 | 7,371 / 7,322 | 7,371.29 / 7,322.14 from report's own H/L/C | ≤0.29 | Reproduces |
| §11 daily S3 | absent | 7,241.69 from report's own H/L/C (slice-derived 7,245.83) | n/a | FAIL — required level omitted from all three pivot tables |
| §11 weekly P | 7,387 | 7,387.13 (prior week 8–12 Jun, cash) | −0.13 | Consistent; R/S tiers are internally consistent with an implied H 7,461 / L 7,256 |
| §11 monthly (May) | P 7,506, R1 7,659, S1 7,427 | not derivable from the D-1 slice | n/a | Internally consistent (implied H 7,585 / L 7,353); left unverified |
| §21b ATR(14) | ≈94 | 108.09 (cash) / 121.07 (full broker day) | −14.09 | FAIL — understates risk scale by ~13%; also never stated in §9 |
| §9 smoothed efficiency ratio | −0.13 | −0.114 (EMA3 of the signed 13-period ER on cash closes) | −0.016 | Value consistent; the "Trending Down — Strong" label attached to it is not |
| §9 median 25-day RSI2 | 69.1 | 63.7 | +5.4 | Discrepancy |
| §9 range position of last close | 41st percentile | 46.5% using the report's own close / 48.6% using the slice close (25d high 7,624.60, low 7,243.10) | −5.5 to −7.6 | Discrepancy; the 25-day endpoints are never stated |
| §9 25-day high reference | "1 Jun 7,600 print" | 7,624.60 on 2 Jun | −24.6, date −1 session | Discrepancy |
| §9 17 Jun range | "130-point range" | 131.5 (cash) / report's own H−L 129.6 | ≤1.9 | Consistent |
| §9/§14 VIX low | "16.1 lows" | June low 16.16 on 4 Jun (5-session window low 17.58) | −0.06 | Value exists but is undated and sits outside the 5-session window |
| §9 VIX "collapsing from 22 on 10 June" | 22 on 10 Jun | 10 Jun H 20.63, C 20.43 (rose from 18.42); June maximum high 21.36 on 11 Jun | −1.37 vs the June max, and wrong date/direction | FAIL |
| §10 VIX direction | Rising | 17.73 → 18.43 on 17 Jun | — | Consistent |
| §10 USDX direction | Rising | 99.573 → 100.425 on 17 Jun | — | Consistent |
| §14 USDX level | "firm near 99.5–99.9" | D-1 close 100.425, D-1 high 100.62 | +0.53 to +0.93 above the band | FAIL — stale band |
| §13c 10 Jun May CPI | 4.2% y/y vs 3.8% prior | CPI y/y actual 4.2, previous 3.8 | 0 | Consistent |
| §13c 17 Jun FOMC | Hold 3.50–3.75% | Fed Interest Rate Decision actual 3.75, previous 3.75, 21:00 broker (14:00 ET) | 0 | Consistent |
| §13d 18 Jun jobless claims | 8:30 ET, impact "Med" | Initial Jobless Claims 15:30 broker (08:30 ET), impact HIGH | timing 0; grade understated | Timing consistent, impact grade FAIL |
| §13d coverage of D | claims, FOMC digestion, 19 Jun Iran MoU | Calendar also carries BoE Interest Rate Decision (18 Jun 14:00 broker) and Philadelphia Fed Manufacturing Index (18 Jun 15:30 broker), both HIGH | two HIGH events omitted | FAIL |
| §4 vs §6 15 Jun classification | §4 "Directional"; §6 "Corroborated (Δ<0.10)" | — | — | FAIL — internal contradiction |
| §4 15 Jun quote "+1.60%" | implies prior close 7,435.3 | report's own 12 Jun close 7,445.00 | −9.7 | FAIL — quote inconsistent with the report's own close column |
| §6 12 Jun provenance | "Close corrob." | §4 contains no 12 Jun source row | — | FAIL — corroboration claimed without evidence |
| §3/§19 17 Jun provenance | "corroborated across the S&P Dow Jones official series (via FRED)" | §4 has no FRED row for 17 Jun; §20 records Traders Union × TradingKey only | — | FAIL — provenance claim exceeds the evidence table |
| Cross-report 16 Jun H/L | 7,551.0 / 7,470.0 (this report) | 7,588.9 / 7,536.4 (`SP500_Report_17Jun2026.md` §6, same session) | −37.9 / −66.4 | FAIL — the two reports disagree about a settled session |
| Cross-report 15 Jun O/L | 7,455.0 / 7,450.0 (this report) | 7,470.6 / 7,468.2 (`SP500_Report_17Jun2026.md` §6) | −15.6 / −18.2 | FAIL — same |
| Card vs report Trade 1 TP3 | card `tp3: 7180.0` | report §21b states "Trail; time-stop at session close + 3×ATR cap", no price | n/a | FAIL — extracted level has no textual source |
