# Trust Score — 2026-06-25 — SP500_Report_25Jun2026.md

Run: regen_20260906_qa1 · Asset US500 · D = 2026-06-25 · D-1 slice = 2026-06-24
Evidence base: the report, reports dated before D, `data/slices/US500/US500_upto_2026-06-24.csv`
(plus VIX/USDX/NEWS slices to D-1), `cards/baseline/by_date/2026-06-25.json`,
`qa/regen_20260906_qa1/lint_static/2026-06-25.csv`, and `engine/qa_slice_stats.py`.

Helper output used throughout (cash session 16:30–23:00 broker):

```
2026-06-18  O 7514.1  H 7518.3  L 7472.6  C 7502.3  RSI2 43.95
2026-06-19  O 7496.5  H 7506.0  L 7491.6  C 7494.2  RSI2 90.23
2026-06-22  O 7513.1  H 7538.8  L 7467.3  C 7479.3  RSI2  0.00
2026-06-23  O 7370.4  H 7431.8  L 7356.2  C 7374.4  RSI2  0.00
2026-06-24  O 7389.0  H 7438.0  L 7346.0  C 7372.3  RSI2  0.00
ATR14 cash 117.90 · ATR14 full-day 130.02
Daily pivots (D-1 cash): P 7385.43 R1 7424.87 S1 7332.87 R2 7477.43 S2 7293.43 R3 7516.87 S3 7240.87
Weekly pivots (2026-06-15..19, cash): P 7495.37 R1 7582.23 S1 7407.33 R2 7670.27 S2 7320.47 R3 7757.13 S3 7232.43
Swing 5d high 7538.80 (22 Jun) low 7346.00 (24 Jun) · Swing 25d high 7624.60 (02 Jun) low 7243.10 (09 Jun)
D-1 cash close 7372.30
RSI2 recomputed from the REPORT'S OWN closes (7500.58, 7475.34, 7472.79, 7365.46, 7358.22):
  n/a, n/a, 0.0, 0.0, 0.0
```

As-of session check: the slice's last bar is 2026-06-24 23:45 broker and the report is built on the
24 June completed cash session. The as-of session is genuinely D-1, not an earlier one. PASS.

## 1. Section 7 checklist

| Item | Reviewer notes | Evidence observed | Score 0–5 | Action required |
|---|---|---|---|---|
| 1.1 Variables respected | Asset is the S&P 500 cash index `^GSPC`, not ES futures. Counters are USDX · VIX · DAX 40 with USDX first, in both the strapline and the §10 table. As-of is the NY close of D-1, tz America/New_York. Lookback 5 sessions (execution) + 25 sessions (regime). Units index points / USD / tick 0.01. Six observations in §4 meets the ≥6 source minimum across index-provider, aggregator and sell-side tiers. **Breach: the fixed 07:00 UK daily-open anchor was overridden to the US cash open (NY 09:30 ET / 14:30 UK).** The override also contradicts the card metadata, which carries `anchor_broker` 09:00 = 07:00 UK. | §2, §3 strapline, §4, §10, §20 "Daily-open anchor override"; `cards/baseline/by_date/2026-06-25.json` | 2 | Restore the 07:00 UK anchor, or reconcile §20 with the card anchor field so one anchor is stated in both places. |
| 1.2 Coverage & currency consistent | No currency or unit drift anywhere; everything is index points / USD. §6, §11, §13a and §13c all sit at D-1 or earlier. **Defect: §13d "Upcoming Period" contains "24 Jun Fed bank stress-test results" — a D-1 event listed as upcoming**, and §12 repeats it as a near-term catalyst. §12 also uses 24 Jun Micron after-hours data (EPS \$25.11, shares +6% after-hours), which post-dates the D-1 cash close that defines the as-of. §2 states the as-of date as 25 June while the header states as-of close 24 June — tolerable but inconsistent phrasing. | §12, §13d, §2, header | 3 | Move the 24 Jun stress-test row from §13d into §13c; either drop the post-close Micron after-hours datapoint or label it explicitly as after the as-of. |
| 1.3 Audience & tone | Written throughout as a Senior US Equity Strategist for trading and risk review: regime language, pivot structure, size and invalidation discipline, explicit conviction scoring. No retail tone, no promotional language. Closing disclaimer states the research-artifact purpose. | §1, §18, §21d closing note | 5 | None. |
| 2.1 Sections present & ordered | All of §1–§21 are present in the mandated order. §13 carries all four sub-blocks (13a per-article table, 13b aggregate with a numeric tilt, 13c previous-period calendar, 13d upcoming calendar). §21 carries 21a conviction, 21b cards, 21c 5-session backtest, 21d what-is-working plus the limitations boilerplate. §19 and §20 both present. | headings throughout | 5 | None. |
| 2.2 Scorecard as a table | §6 is a genuine table but **omits three mandated columns: Source A, Source B and Final** — it runs Date/O/H/L/C/RSI2/Trend/Validation only. The prior-day report (`SP500_Report_24Jun2026.md` §6) carries Src A / Src B, so the columns were dropped, not never specified. §11 fails the 3-levels-each-side rule: daily runs R5→R1, P, S1→S4 (five up, four down); weekly gives only R2→S2 (two a side); monthly gives R1, P, S1→S3 (one resistance level). The §11 caption claims "Mandatory order R5→P→S5 preserved" while S5 is absent. | §6 header row; §11.1, §11.2 and caption | 2 | Restore Source A / Source B / Final in §6; render all three pivot tables symmetrically as R3→P→S3. |
| 2.3 Method steps visible | §4 lists observations with basis and relevance, §5 explains the weighted-median build to the consensus — observation → classification → consensus is visible. §8 is candle-by-candle across all five sessions and closes with an explicit sequence assessment. §9 gives regime with overlap ratio, directional persistence, range position and VOLator, plus a KER confirmation line. §7 carries five chart blocks; pandoc has dropped the images to `media/*.png` references, accepted as evidence per the brief and noted here. | §4, §5, §7, §8, §9 | 4 | None blocking; note that chart content itself could not be inspected. |
| 3.1 Quantitative claims sourced | **§1 "roughly 130 points off the index from the 18 June swing high" does not reconcile with the report's own §6**: 7,511.07 − 7,358.22 = 152.85 pts (from the 18 Jun close, 142.36; over the two-session 23–24 Jun leg, 114.57). No stated basis gives ~130. **§1 and §3 both claim the 24 June close was corroborated "across the official index publisher and two market data aggregators", but §4 dates the only S&P DJI observation to 23 June and §20 names the 24 Jun corroborating pair as CNBC × Yahoo** — the official publisher is not in the 24 Jun evidence set. §12 and §14 carry Micron EPS, chip-ETF −7%, Russell 2000 outperformance, Dow +0.35% / Nasdaq −0.43%, the BofA three-hike note, WTI −3.9% ~\$70 and Brent −4.3% ~\$73.74 with no source column and no pointer to §4/§6/§13. | §1, §3 rationale, §4, §12, §14, §20 | 2 | Recompute the §1 drawdown from §6 and state its endpoints; correct the §1/§3 corroboration claim to name the actual pair; attach a source or a §4/§13 pointer to every §12 and §14 figure. |
| 3.2 Citations exist & contain data | Three sources spot-checked for internal consistency. **(a) Trading Economics, 23–24 Jun, −1.44% / −0.10% — PASSES exactly**: from §6 closes, 7,365.46/7,472.79 − 1 = −1.436% and 7,358.22/7,365.46 − 1 = −0.098%. **(b) Investing.com, 18–22 Jun, 7,500.58 / 7,472.79 — figures match §6, but it is the only §4 observation covering 18 June**, which contradicts §6's "CORROBORATED (Δ0.00)" and §19's claim that 18 June is "fully two-source corroborated across OHLC". **(c) S&P DJI (via FRED), 23 Jun, 7,365.46 — internally consistent** with §6 and with TradingView's 7,365.45 at Δ0.01, matching §6's stated Δ; but §20 names the 23 Jun pair as "S&P DJI × CNBC-derived" while §4's CNBC row is dated 24 June. Every source is named, dated and quotes a figure used elsewhere; none is impossible or self-contradictory on its own terms. **No fabricated source — the hallucinated-source override does not fire.** The defects are misattribution of which pair corroborated which date, and an unsupported two-source claim for 18 June. | §4 rows 1, 4, 6; §6 Validation column; §19; §20 | 3 | Name a genuine second 18 June observation in §4 or downgrade 18 June to single-source; make §20's corroborating pairs match the dates in §4. |
| 3.3 Calculations transparent | **Pivots PASS**: all seven §11.1 daily levels reproduce exactly from the report's own 24 Jun H/L/C (7,424.50 / 7,355.80 / 7,358.22) — P 7,379.51, R1 7,403.21, S1 7,334.51, R2 7,448.21, S2 7,310.81, R3 7,471.91, S3 7,265.81. **RSI2 FAILS**: the report's own closes give RSI2 = 0.0 for 22 June (18→19 and 19→22 are both down closes, so mean gain = 0 and RS = 0), against the stated "~30"; "~30" is also an approximation where a computed value is required. **Trend column misapplies the report's own stated rule on 3 of 5 rows**: 18 Jun (C 7,500.58 > O 7,487.36, RSI2 76.1 > 50) should be Bullish, 19 Jun (C < O, RSI2 46.9 < 50) and 22 Jun (C < O, RSI2 < 50) should be Bearish — all three are labelled Neutral. **§21a direction score not reproducible**: the three quoted contributions (−0.20, −0.10, −0.09) sum to −0.39, not the stated −0.21, and the six 0.25/0.20/0.10/0.15/0.15/0.15 weights are never shown against their signals. **§13b tilt not reproducible**: the stated numerator (−1.0×0.5×2 + 1.0×0.5 = −0.5) yields −0.21 only if Σweights = 2.38, which leaves 0.38 for the trade-press and institutional sources combined after 4 media at 0.5 — the weights are never stated. ATR(14) = 116 appears only inside a Trade 2 caveat, not in §9 where the regime block sits. KER stated correctly (smoothed −0.10 within ±0.13). Weekly and monthly pivots are not reproducible because their prior-period H/L/C are never given. | §6 RSI2 and Trend columns; §11.1; §9; §13b; §21a; §21b caveat | 1 | Recompute the RSI2 column from the validated closes and print exact values; re-derive the Trend column from the stated rule; show the six signal×weight terms behind −0.21; state ATR(14) in §9; state the prior-period H/L/C behind the weekly and monthly pivots. |
| 3.4 Numbers reconcile | Internal: the D-1 close 7,358.22 is identical in §1, §3, §4, §6 and §18 (Trade 1 is suppressed, so there is no §21b entry to match). All pivot levels quoted on the cards (7,403.21, 7,379.51, 7,355.80, 7,334.51, 7,265.81, 7,309.98, 7,485.29) match §11. **Internal failures:** §8 puts the 18 Jun close at "~94% of range" where §6 gives (7,500.58 − 7,468.32)/(7,511.07 − 7,468.32) = 75.5%; §8 lists nearest support as "7,347.60 then 7,355.80", inverted relative to spot 7,358.22; §8 calls 7,475 the "22 Jun close" when §6 gives 7,472.79 (7,475.34 is the 19 Jun close); §11 says the close is "~0.3% of weekly S1 (7,392.66) above" when the actual gap is 0.47%. **Against the slice: two closes fail the 10-pt threshold** — 24 Jun 7,358.22 vs 7,372.30 (Δ −14.08) and 19 Jun 7,475.34 vs 7,494.20 (Δ −18.86) — and 13 of 20 stated OHLC values exceed the basis tolerance, the largest being 22 Jun H at Δ −40.40 and 19 Jun L at Δ −32.70. **Cross-report:** the same 23 June session is published as O 7,462 / H 7,478.45 / L 7,349.31 in `SP500_Report_24Jun2026.md` §6 and as O 7,366.51 / H 7,424.17 / L 7,347.60 here, both marked CORROBORATED; the May monthly pivot P is 7,465.95 there and 7,547.58 here; weekly P for the same W/E 19 Jun week is 7,487.19 there and 7,485.29 here. See §5 for the full log. | §1, §3, §4, §6, §8, §11, §18; slice; `SP500_Report_24Jun2026.md` §6, §11 | 1 | Rebuild §6 from the validated feed; propagate the corrected D-1 H/L/C into §11 and every card level; fix the four §8/§11 internal arithmetic errors; reconcile the 23 Jun row and the weekly/monthly pivots against the prior report. |
| 4.1 Pillars conclude | §8 closes on "Exhaustion — reversal risk"; §10 closes on "CONFIRM (bearish-leaning) — two of three confirm, none contradict"; §12 tags every driver cyclical/structural with a price sign; §15 is a balanced two-column risk table. **§9 concludes twice and inconsistently**: the table header classifies the regime as "RANGING (range-bottom bias)" while the closing conflict note declares "The composite consolidated label is therefore TRANSITION, not a clean RANGE". §14 offers a watch item but no direction label of its own. | §8, §9 table vs conflict note, §10, §12, §14 | 3 | Resolve §9 to a single regime label and use it consistently in §16 and §21; add a direction label to §14. |
| 4.2 Peer/cross-asset interpreted | §10 supplies a genuine transmission mechanism per counter rather than a correlation list: USDX via earnings-translation on foreign revenues and tighter global financial conditions; VIX as an implied-vol / risk-regime gauge with a spike-and-ease path; DAX 40 as European equity beta loading on a common global-risk factor. Each row carries direction, status and implication, and §14 re-uses the USDX and VIX reads by explicit cross-reference. The USDX direction is corroborated by the slice (24 Jun close 101.636, rising every session from 100.51 on 17 Jun). | §10, §14 cross-references | 5 | None. |
| 4.3 Synthesis reconciles tensions | The report does surface its tensions well: §9's conflict note sets the expanding VOLator slope against the ranging overlap and KER read and resolves to TRANSITION; §21a flags that the §17 two-way forecast conflicts with the tactical short read; §15 balances both sides. **But the resolution is not carried into execution, and card construction is scored here.** §9 declares TRANSITION, under which M5 permits the breakout side only, yet **Trade 2 is a RANGE limit fade at daily R1**. **Trade 3A is labelled Momentum-Pullback but built as a breakout** — a sell stop at 7,346.00 on a break of the 23 Jun low — with no 57.5% retrace entry, no logged swing endpoints, a stop anchored to daily P rather than beyond the 0% anchor, TP2 at weekly S2 rather than the 0% level, and **no qualifying swing available**: the largest 4–10 session swing on the slice is 7,538.80 → 7,346.00 = 192.80 pts against a 2×ATR14 requirement of 235.80 (cash) or 260.04 (full-day). **Both live cards carry R below the M5 floor** — Trade 2 at 26.79 pts (0.21×ATR) and Trade 3A at 39.0 pts (0.30×ATR), both flagged WARN_R_TINY by the linter. Trade 2's TP1 and TP2 are pivot levels labelled "≈ +1R / ≈ +2R" but are actually 0.89R and 1.77R. Trade 1's suppression is correct and well handled. | §9 conflict note, §21a, §21b Trade 2 and Trade 3A, lint rows, slice swing/ATR | 2 | Rebuild both live cards to the M5 geometry for the declared regime — see the feedback file for the exact numeric conditions. |
| 4.4 Calibrated language | §17 is exactly one sentence, as required. Confidence is stated where the framework asks: §3 gives High, §18 gives "High on price; Medium on direction", §21a gives "SHORT (low conviction)". **However the single §17 sentence hedges in both directions at once** — chop with a mild downward bias, reverse up on a cool print, break down on a hot print — which leaves no falsifiable central case; §1's "balanced-to-cautious" and §16's "two-way around the 7,335–7,485 band" repeat the same two-sided framing. | §1, §3, §16, §17, §18, §21a | 3 | Commit §17 to one central case with the conditional as a named invalidation rather than a co-equal branch. |
| 5.1 Data dated; staleness flagged | Every §6 row is dated, every §13a article carries a source, class, date and derivation quote, and every §13c/§13d event is dated. Single-source intraday High/Low is flagged with an asterisk on the three affected rows, explained in the §6 caption, and expanded in §19 with the specific fields (19 Jun H/L, 22 Jun H/L, 24 Jun H/L) repeated in §20. Counter-instrument corroboration status is disclosed in §7.4 and §19. Gaps: the §12 and §14 figures carry loose dating and no source, and the 24 Jun Micron after-hours datapoint post-dates the as-of close without being labelled as such. | §6 caption, §7.4 note, §12, §13, §14, §19, §20 | 4 | Date and source the §12/§14 figures; label the after-hours datapoint. |
| 5.2 Assumptions up front | Single-source pivot propagation is handled correctly and visibly: §11.1 carries the caveat, §19 states that daily pivots inherit the flag, and the Trade 2 card repeats "single-source-indicative daily pivots (§19)". **The anchor-override caveat is stated in §20 but does not appear on either card**, and the §20 override (NY 09:30 ET / 14:30 UK) contradicts the `anchor_broker` 09:00 (= 07:00 UK) held in the card record, so the two disclosures cannot both be true. §20 otherwise logs the as-of override, the sources attempted, the single-source fields, the sentiment derivation, the weights basis and the composite regime. | §11.1, §19, §20, §21b caveats, `cards/baseline/by_date/2026-06-25.json` | 3 | Put the anchor-override caveat on every card and make it agree with the card anchor field. |
| 5.3 Red flags surfaced | §12 carries five drivers with explicit price signs including two price-negative structural risks. §15 gives four upside and four downside risks with levels attached. The §13d PCE collision is carried into both live card caveats ("holding period collides with 25 Jun PCE (§13d)" on Trade 2; "PCE-driven whipsaw risk (§13d)" on Trade 3A). §9's VOLator-vs-KER conflict is flagged in-section and again in §20. Trade 2 additionally flags "ATR(14)=116 is wide vs 27-pt stop — reduce size", which is the correct risk to surface. The §13d event set is corroborated by the calendar slice, which schedules Core PCE, GDP and Durable Goods for 25 Jun. | §9 conflict note, §12, §13d, §15, §20, §21b caveats; NEWS slice | 5 | None. |
| 5.4 Restrictions honoured | No synthesised or interpolated price is presented as sourced — §19 states plainly "No values were synthesised; gaps are disclosed rather than filled", and the single-source fields are disclosed rather than filled in. Retail/CFD material is kept out of the OHLC basis: Trading Economics is marked "CFD-reference / Directional" in §4 and the caption restates that CFD references are "used for directional confirmation only, per the restriction on retail/CFD quotes entering OHLC". No ES futures values enter the basis. No bracketed variable names, no M1–M5 module codes and no framework name appear anywhere in the text. Instrument common names are used throughout (S&P 500 cash index, Dollar Index, VIX, DAX 40). Only leak: §20's "Defaults (v2.1 baseline)" exposes an internal module version tag. **No listed restriction is breached — the restriction-breach override does not fire.** | §4 caption, §19, §20, whole report | 4 | Remove the "v2.1 baseline" version tag from §20. |

## 2. Category roll-up

| Category | Level | Multiplier | Points | Justification |
|---|---|---|---|---|
| C1 Prompt adherence and instruction compliance (max 20) | 3 | 0.65 | 13.00 | Rows 1.1–1.3 mean (2+3+5)/3 = 3.33 → 3. Asset, counters, window, units, timezone and source count are all correct and the tone is right, but the fixed 07:00 UK daily-open anchor was overridden and the override contradicts the card anchor field, and a D-1 event sits in the upcoming calendar. |
| C2 Structural and modular framework alignment (max 20) | 4 | 0.85 | 17.00 | Rows 2.1–2.3 mean (5+2+4)/3 = 3.67 → 4. Every section and sub-block is present and correctly ordered and the method steps are visible; the loss is confined to malformed tables — §6 missing three mandated columns and all three §11 pivot tables asymmetric. |
| C3 Accuracy, evidence and factual reliability (max 25) | 2 | 0.40 | 10.00 | Rows 3.1–3.4 mean (2+3+1+1)/4 = 1.75 → 2. Pivots reproduce exactly and one cited source reconciles to the decimal, but two stated closes miss the slice by more than 10 pts, 13 of 20 OHLC values exceed basis tolerance, the RSI2 column does not reproduce from the report's own closes, the Trend column misapplies its own stated rule on three rows, and the §21a and §13b scores are not derivable from what is shown. No source is fabricated. |
| C4 Reasoning, judgment and evaluation quality (max 20) | 3 | 0.65 | 13.00 | Rows 4.1–4.4 mean (3+5+2+3)/4 = 3.25 → 3. Cross-asset mechanism is genuinely strong and the tensions are surfaced honestly, but the TRANSITION resolution is not carried into execution: Trade 2 runs range logic under a declared transition regime, Trade 3A is a breakout wearing a momentum-pullback label with no qualifying swing, both live cards sit below the R floor, and §17 hedges both ways. |
| C5 Currency, restrictions and transparency (max 15) | 4 | 0.85 | 12.75 | Rows 5.1–5.4 mean (4+3+5+4)/4 = 4.00 → 4. Dating, single-source flagging, no-synthesis discipline, CFD exclusion from OHLC and red-flag surfacing are all handled well and the PCE collision reaches the card caveats; the anchor-override caveat is missing from the cards and contradicts the card record, and an internal version tag leaks into §20. |
| **Total** | — | — | **65.75 → 66** | Σ(multiplier × max) = 13.00 + 17.00 + 10.00 + 13.00 + 12.75 = 65.75, rounded to 66. |

## 3. Total, band, override check

- **Raw total: 65.75 → 66.**
- **Band: Moderate** (60–74).
- **Hallucinated-source override: does not fire.** Three cited sources were spot-checked for internal
  consistency (row 3.2). Trading Economics' −1.44% / −0.10% reproduces exactly from the report's own §6
  closes; Investing.com's 7,500.58 / 7,472.79 match §6; S&P DJI (via FRED) at 7,365.46 for 23 June is
  consistent with §6 and sits Δ0.01 from TradingView's 7,365.45, exactly as §6 states. Every source is
  named, dated and quotes a figure used consistently elsewhere. The real defects are misattribution —
  §1 and §3 credit the official index publisher with corroborating a 24 June close it has no observation
  for, §20 names a 23 June pair whose second member is dated 24 June in §4, and §19 claims two-source
  corroboration for 18 June where §4 shows only one observation. That is incorrect attribution of
  existing sources, not an invented or impossible one, so C3 is scored on its merits rather than zeroed.
- **Restriction-breach override: does not fire.** The restriction list at checklist row 5.4 is
  no synthesised price presented as sourced, no retail CFD quotes in the OHLC basis, ES futures
  confirmation-only, no bracketed variable names, no module codes, no framework name, and instrument
  common names. Every one of these is honoured (row 5.4). The 07:00 UK daily-open anchor override is a
  breach of a **prompt variable** under row 1.1, which the brief treats as a deviation to note rather
  than a listed restriction; it is penalised at row 1.1 (score 2) and dragged C1 to level 3 on the mean.
  The only residual leak is the "v2.1 baseline" version tag in §20, which is not a module code (M1–M5)
  and not the framework name.
- **Override applied: none. Total stands at 66, band Moderate.** No cap and no forced category level.

## 4. Card Integrity

Linter rows copied verbatim from `qa/regen_20260906_qa1/lint_static/2026-06-25.csv`:

| card_id | report_date | strategy | flags | dud |
|---|---|---|---|---|
| 2026-06-25_Trade_1 | 2026-06-25 | Trade 1 - Daily Directional | SUPPRESSED | False |
| 2026-06-25_Trade_2 | 2026-06-25 | Trade 2 - Pivot (range fade, sell limit daily R1) | WARN_R_TINY(0.21xATR) | False |
| 2026-06-25_Trade_3A | 2026-06-25 | Trade 3A - Momentum-Pullback (sell stop, break of 23 Jun low) | WARN_R_TINY(0.30xATR) | False |

Per-card integrity, 100 − 40·(#DUD) − 10·(#WARN), floored at 0:

| Card | #DUD | #WARN | Integrity | In report mean? |
|---|---|---|---|---|
| 2026-06-25_Trade_1 | 0 | 0 | 100 | No — SUPPRESSED |
| 2026-06-25_Trade_2 | 0 | 1 | 100 − 10 = **90** | Yes |
| 2026-06-25_Trade_3A | 0 | 1 | 100 − 10 = **90** | Yes |

**Report Card Integrity = mean over non-suppressed cards = (90 + 90) / 2 = 90.0**

Counts for the run row: n_cards = 3 (all rows in the lint file), n_duds = 0 (no DUD_* flags),
n_warns = 2 (two WARN_R_TINY flags). SUPPRESSED is a status, not a DUD or WARN flag.

M5 assessment of each card (feeds checklist row 4.3, **not** the integrity number above):

- **Trade 1 — correctly handled.** Direction score −0.21, |−0.21| < 0.25, so Trade 1 is suppressed and
  the suppression is published as a SUPPRESSED row rather than an omission, exactly as M5 requires.
  §21a states the threshold test explicitly. No defect. (Side note for row 3.3: the direction score
  −0.21 is numerically identical to the §13b sentiment tilt −0.21, which suggests the composite may
  have been set equal to one of its inputs rather than computed as Σ signal×weight.)
- **Trade 2 — regime mismatch and geometry defects.** §9's composite label is TRANSITION, under which
  M5 permits the breakout side only, yet this card is a RANGE limit fade at daily R1. R = 7,430.00 −
  7,403.21 = 26.79 pts = 0.21×ATR14 (130.02), below the 0.3×ATR14 floor — the linter's WARN_R_TINY.
  The stop is described as "24 Jun high 7,424.50 + buffer" but sits only 5.50 pts above that high,
  where M5 requires structural + 0.25×ATR or 3.5×ATR. TP1 7,379.51 is 23.70 pts = 0.89R and TP2
  7,355.80 is 47.41 pts = 1.77R, both labelled "≈ +1R" and "≈ +2R" where M5 requires exact 1R and 2R.
  The "TP3 (runner)" line mixes a daily-S1 target with a "weekly S1 7,392 trail" that sits above TP1
  and inside the entry, which is not a coherent trailing rule for a short. Point distances are given
  for the stop and TP1 only, not TP2 or TP3. Correct: entry above the D-1 close for a sell limit,
  stop on the correct side, TP ordering monotone, TP1 well within 2.5×ATR, invalidation stated
  separately from the stop, confluences listed, single-source flag propagated, PCE collision flagged.
- **Trade 3A — wrong strategy family and no qualifying swing.** M5 3A is a 57.5% retrace entry on a
  swing of magnitude ≥ 2×ATR14 within a 4–10 session lookback with endpoints logged. This card is a
  breakout: a sell stop at 7,346.00 on a confirmed break of the 23 Jun low. **No qualifying swing
  exists** — the largest 4–10 session swing on the slice is 7,538.80 (22 Jun) → 7,346.00 (24 Jun) =
  192.80 pts, and the report's own 7,511.07 → 7,347.60 = 163.47 pts, both short of 2×ATR14 = 235.80
  (cash) / 260.04 (full-day). The stop 7,385.00 is anchored to daily P, not beyond the 0% anchor by
  0.25×ATR; TP1 7,318.00 matches neither the 38.2% retrace (7,410.5) nor a 38.2% extension (7,285.6)
  of the swing it names; TP2 is weekly S2 rather than the 0% level; TP3 is daily S3 rather than a
  100%+ extension. R = 39.0 pts = 0.30×ATR14, at the floor — the linter's WARN_R_TINY. Correct: sell
  stop below the D-1 close, stop on the correct side, TP ordering monotone, TP1 within 2.5×ATR,
  invalidation separate from the stop, whipsaw and low-conviction caveats present.

## 5. Data reconciliation log

Tolerances per the brief: |Δ| ≤ 3 pts on a close and ≤ 8 pts on an open/high/low are consistent
(CFD-vs-cash basis); larger deltas are discrepancies; a close wrong by more than 10 pts, or an RSI2
that does not reproduce from the report's own closes, is a Category 3 failure. Slice values are the
cash-session (16:30–23:00 broker) figures from the helper. Δ = report − slice.

### 5.1 §6 Validated OHLC + RSI2 table — all five rows

| Section | Report value | Slice value | Delta | Verdict |
|---|---|---|---|---|
| §6 18 Jun Open | 7,487.36 | 7,514.10 | −26.74 | DISCREPANCY (>8) |
| §6 18 Jun High | 7,511.07 | 7,518.30 | −7.23 | Consistent (≤8) |
| §6 18 Jun Low | 7,468.32 | 7,472.60 | −4.28 | Consistent (≤8) |
| §6 18 Jun Close | 7,500.58 | 7,502.30 | −1.72 | Consistent (≤3) |
| §6 18 Jun RSI2 | 76.1 | 43.95 | −32.15 | UNVERIFIABLE from report closes (needs pre-window closes); far from slice RSI2 |
| §6 19 Jun Open | 7,494.50 | 7,496.50 | −2.00 | Consistent (≤8) |
| §6 19 Jun High | 7,505.10 | 7,506.00 | −0.90 | Consistent (≤8) |
| §6 19 Jun Low | 7,458.90 | 7,491.60 | −32.70 | DISCREPANCY (>8) |
| §6 19 Jun Close | 7,475.34 | 7,494.20 | −18.86 | **FAILURE (>10 pts on a close)** |
| §6 19 Jun RSI2 | 46.9 | 90.23 | −43.33 | UNVERIFIABLE from report closes; far from slice RSI2 |
| §6 22 Jun Open | 7,479.80 | 7,513.10 | −33.30 | DISCREPANCY (>8) |
| §6 22 Jun High | 7,498.40 | 7,538.80 | −40.40 | DISCREPANCY (>8) — largest OHLC delta in the table |
| §6 22 Jun Low | 7,455.10 | 7,467.30 | −12.20 | DISCREPANCY (>8) |
| §6 22 Jun Close | 7,472.79 | 7,479.30 | −6.51 | DISCREPANCY (>3) |
| §6 22 Jun RSI2 | ~30 | 0.00 | −30 | **FAILURE — does not reproduce from the report's own closes, which give 0.0** (18→19 and 19→22 are both down closes); also stated as an approximation |
| §6 23 Jun Open | 7,366.51 | 7,370.40 | −3.89 | Consistent (≤8) |
| §6 23 Jun High | 7,424.17 | 7,431.80 | −7.63 | Consistent (≤8) |
| §6 23 Jun Low | 7,347.60 | 7,356.20 | −8.60 | DISCREPANCY (marginally >8) |
| §6 23 Jun Close | 7,365.46 | 7,374.40 | −8.94 | DISCREPANCY (>3, below the 10-pt failure line) |
| §6 23 Jun RSI2 | 0.0 | 0.00 | 0.00 | PASS — matches slice and reproduces from the report's own closes |
| §6 24 Jun Open (D-1) | 7,369.20 | 7,389.00 | −19.80 | DISCREPANCY (>8) |
| §6 24 Jun High (D-1) | 7,424.50 | 7,438.00 | −13.50 | DISCREPANCY (>8) |
| §6 24 Jun Low (D-1) | 7,355.80 | 7,346.00 | +9.80 | DISCREPANCY (>8) |
| §6 24 Jun Close (D-1) | 7,358.22 | 7,372.30 | −14.08 | **FAILURE (>10 pts on a close)** |
| §6 24 Jun RSI2 (D-1) | 0.0 | 0.00 | 0.00 | PASS — matches slice and reproduces from the report's own closes |

Summary: 13 of 20 OHLC values exceed tolerance; 2 of 5 closes fail the 10-pt threshold; the whole
table carries a consistent downward bias against the slice (18 of 20 values sit below it). RSI2
reproduces on 2 of the 3 rows the report's own closes can test and fails on the third.

### 5.2 §11 pivots — reproduction from the report's own D-1 H/L/C, then against the slice

Recomputed from the report's own stated 24 Jun H 7,424.50 / L 7,355.80 / C 7,358.22:
P = 7,379.5067, R1 = 7,403.2133, S1 = 7,334.5133, R2 = 7,448.2067, S2 = 7,310.8067,
R3 = 7,471.9133, S3 = 7,265.8133.

| Section | Report value | Recomputed from report's own H/L/C | Slice value (D-1 cash) | Delta vs slice | Verdict |
|---|---|---|---|---|---|
| §11.1 Daily P | 7,379.51 | 7,379.51 | 7,385.43 | −5.92 | Formula PASS; inherits the wrong H/L/C |
| §11.1 Daily R1 | 7,403.21 | 7,403.21 | 7,424.87 | −21.66 | Formula PASS; DISCREPANCY vs slice |
| §11.1 Daily S1 | 7,334.51 | 7,334.51 | 7,332.87 | +1.64 | Formula PASS; consistent vs slice |
| §11.1 Daily R2 | 7,448.21 | 7,448.21 | 7,477.43 | −29.22 | Formula PASS; DISCREPANCY vs slice |
| §11.1 Daily S2 | 7,310.81 | 7,310.81 | 7,293.43 | +17.38 | Formula PASS; DISCREPANCY vs slice |
| §11.1 Daily R3 | 7,471.91 | 7,471.91 | 7,516.87 | −44.96 | Formula PASS; DISCREPANCY vs slice |
| §11.1 Daily S3 | 7,265.81 | 7,265.81 | 7,240.87 | +24.94 | Formula PASS; DISCREPANCY vs slice |
| §11.1 Daily R4 / R5 / S4 | 7,540.61 / 7,609.31 / 7,197.11 | n/a — outside the 3-a-side spec | n/a | n/a | STRUCTURE DEFECT — extra levels, asymmetric (5 up, 4 down), caption claims an S5 that is absent |
| §11.2 Weekly P | 7,485.29 | not reproducible — prior-period H/L/C never stated | 7,495.37 | −10.08 | DISCREPANCY |
| §11.2 Weekly R1 | 7,567.97 | not reproducible | 7,582.23 | −14.26 | DISCREPANCY |
| §11.2 Weekly S1 | 7,392.66 | not reproducible | 7,407.33 | −14.67 | DISCREPANCY |
| §11.2 Weekly R2 | 7,660.60 | not reproducible | 7,670.27 | −9.67 | DISCREPANCY |
| §11.2 Weekly S2 | 7,309.98 | not reproducible | 7,320.47 | −10.49 | DISCREPANCY |
| §11.2 Weekly R3 / S3 | absent | — | 7,757.13 / 7,232.43 | — | STRUCTURE DEFECT — only 2 levels a side |
| §11.2 Monthly (R1 7,631.86, P 7,547.58, S1 7,495.77, S2 7,411.49, S3 7,359.68) | as stated | not reproducible — prior-month H/L/C never stated | no monthly reference in the slice helper | — | UNVERIFIABLE; STRUCTURE DEFECT (one resistance level only); contradicts the prior report, which gives monthly P 7,465.95 |

**All seven core daily pivot levels reproduce exactly from the report's own D-1 H/L/C — the pivot
arithmetic is sound; the levels are wrong only because the D-1 H/L/C feeding them are wrong.**

### 5.3 Derived statistics, counters and cross-report consistency

| Section | Report value | Slice / cross-source value | Delta | Verdict |
|---|---|---|---|---|
| §21b caveat ATR(14) | 116 | 117.90 (cash) / 130.02 (full-day) | −1.90 / −14.02 | Consistent on the cash basis; note the linter's WARN thresholds are computed on 130.02 |
| §9 25-session range low | 7,237.85 | 7,243.10 (09 Jun) | −5.25 | Consistent (≤8) |
| §9 25-session range high | 7,620.90 | 7,624.60 (02 Jun) | −3.70 | Consistent (≤8) |
| §9 range position | 31st percentile | 31.4% from the report's own numbers; 33.9% on slice values | +0.4 / −2.9 | PASS — reproduces from the report's own inputs |
| §9 KER | −0.10, within ±0.13 | not independently derivable | — | Stated with its band, as required |
| §9 VOLator | scaled +1.0, slope +0.07 | not independently derivable | — | UNVERIFIABLE — no derivation shown |
| §1 drawdown "roughly 130 points" from the 18 Jun swing high | ~130 | 152.85 from the report's own §6 (7,511.07 − 7,358.22) | −22.85 | DISCREPANCY — internal, does not reconcile with §6 |
| §8 18 Jun close position in range | ~94% | 75.5% from the report's own §6 | −18.5 pp | DISCREPANCY — internal |
| §8 "7,475 (22 Jun close)" | 7,475 | §6 gives 22 Jun close 7,472.79 (7,475.34 is the 19 Jun close) | — | MISLABEL — internal |
| §8 nearest support ordering | "7,347.60 then 7,355.80" | 7,355.80 is nearer to spot 7,358.22 than 7,347.60 | — | INVERTED — internal |
| §11 "within ~0.3% of weekly S1" | ~0.3% | 0.47% (34.44 / 7,358.22) | −0.17 pp | DISCREPANCY — internal |
| §11 "within ~0.02% of monthly S3" | ~0.02% | 0.0198% (1.46 / 7,358.22) | ~0 | PASS — internal |
| §4 Trading Economics 23 Jun −1.44% | −1.44% | −1.436% from §6 closes | ~0 | PASS — source reconciles to the report's own data |
| §4 Trading Economics 24 Jun −0.10% | −0.10% | −0.098% from §6 closes | ~0 | PASS |
| §13c VIX "+12.8% to 19.49" on 23 Jun | 19.49, +12.8% | slice 23 Jun cash close 18.93, high 19.18; 22 Jun close 17.91 → +5.7% | −0.56 on level, −7.1 pp on the move | DISCREPANCY — the level was never printed in the D-1 cash session and the percentage does not follow from the slice |
| §14 VIX "~18.6" | ~18.6 | 18.55 (24 Jun cash close) | +0.05 | PASS |
| §1 / §10 USDX "fresh 2026 high above 101" | >101 | 101.636 close, 101.736 high (24 Jun), rising every session from 100.51 on 17 Jun | — | Direction PASS; level materially understated |
| §13d event set for 25 Jun | May PCE, Q1 GDP final, durable orders | NEWS slice schedules Core PCE y/y (HIGH), GDP q/q (HIGH), Durable Goods Orders m/m (HIGH) on 2026-06-25 | — | PASS |
| §13d "24 Jun Fed bank stress-test results" listed as upcoming | 24 Jun | 24 Jun is D-1; no such event in the calendar slice for that date | — | DATE DEFECT — a past event in the upcoming table |
| Cross-report: 23 Jun Open | 7,366.51 | `SP500_Report_24Jun2026.md` §6 gives 7,462 | −95.49 | CROSS-REPORT CONFLICT — both rows marked CORROBORATED |
| Cross-report: 23 Jun High | 7,424.17 | `SP500_Report_24Jun2026.md` §6 gives 7,478.45 | −54.28 | CROSS-REPORT CONFLICT |
| Cross-report: 23 Jun Low | 7,347.60 | `SP500_Report_24Jun2026.md` §6 gives 7,349.31 | −1.71 | Consistent |
| Cross-report: 18 Jun RSI2 | 76.1 | `SP500_Report_24Jun2026.md` §6 gives 46.9 for 18 Jun | +29.2 | CROSS-REPORT CONFLICT — and 46.9 is the value this report assigns to 19 Jun, suggesting a shifted column |
| Cross-report: 22 Jun RSI2 | ~30 | `SP500_Report_24Jun2026.md` §6 gives 74.3 for 22 Jun | −44.3 | CROSS-REPORT CONFLICT |
| Cross-report: weekly P (W/E 19 Jun) | 7,485.29 | `SP500_Report_24Jun2026.md` §11 gives 7,487.19 | −1.90 | Minor conflict — same prior period should give one value |
| Cross-report: monthly P (May) | 7,547.58 | `SP500_Report_24Jun2026.md` §11 gives 7,465.95 | +81.63 | CROSS-REPORT CONFLICT — the same prior month cannot yield two pivots |
| As-of session identity | 24 Jun cash session | slice last bar 2026-06-24 23:45 broker | — | PASS — the as-of session is genuinely D-1 |
