# Trust Score — Gold_Report_07Jul2026.md (XAUUSD, D = 2026-07-07)

Run: `gold_regen_qa1`. Scored against `docs/AI_Output_Trust_Score_Framework_v3.7.txt` §4–7 as
anchored by `docs/QA_PROTOCOL_TRADE_CARDS.md` and amended by `qa/gold_regen_qa1/REVIEWER_BRIEF.md`.

Leak-safety check performed: `data/levels/XAUUSD_by_date/2026-07-07.csv` → `last_bar_date =
2026-07-06` < `date = 2026-07-07`. OK to use. Basis used throughout: `_full` (report claims "Spot
XAU/USD · loco London" / "Global 24-hour market", a continuous basis, not the US cash session).

**Known source defect, not scored as a conversion artefact (per task instructions):** all three
§21b trade-card tables render as `[object Object]` in every cell in the report itself. Additionally,
independently found here: §3's "Consensus price" table cell is *also* `[object Object]` (the
Consensus range/Confidence/Tone cells in the same row are intact, and the number itself,
US$4,158/oz, is recoverable from §1, §5 and §18, so this one is a structural defect rather than a
total information loss like the three cards).

## 1. Section 7 checklist

| Row | Notes | Evidence | Score |
|---|---|---|---|
| 1.1 Variables respected | Asset correct (XAU/USD spot, loco London; GC=F named as corroboration-only and never actually cited/blended — compliant). USDX is the mandatory first §10 counter ✓. Lookback 5d/25d both used consistently ✓. Three failures: (a) **§2 "As-of date" = 07 Jul 2026, i.e. D itself** — `M1_Variables_v2_1.md` fixes AS_OF_DATE to "the last completed regular session… that closed strictly before the report date," which for D=07 Jul is 06 Jul, not 07 Jul; (b) **TICK_SIZE / TICK_NAME are never stated anywhere** (required once strategy cards are produced) — only a generic "tick-level fills" phrase appears, no value; (c) **the ≥6-independent-source requirement is claimed but not met**: §1/§4/§5 all assert "weighted median of six independent feeds," but §5's own text and §20's Agent Log show only Investing.com and Twelve Data are actually blended into the central tendency — TradingEconomics and LBMA are "directional anchors… down-weighted," and TradingView/Bloomberg are "excluded from the central tendency" — i.e. 2 of 6 genuinely feed the consensus PRICE build, not 6. | §2, §4, §5, §20 | 2 |
| 1.2 Coverage & currency consistent | No USD/oz vs tick vs "points" drift anywhere. But directly downstream of 1.1(a): §11's daily pivots are built on "prior session: 03 Jul" even though the leak-free level file proves 06 Jul (D−1) was a genuine completed, corroborable session (`last_bar_date`=2026-07-06). The report's own §6/§19 misclassify that completed D−1 session as "still in-progress… single-source indicative" and exclude it from the daily pivot prior-period, so §11's daily table is built on stale D−3 data instead of the correct D−1 base. | §2, §6, §11, §19, level file | 2 |
| 1.3 Audience & tone | Senior Commodities Analyst register throughout; institutional, no retail framing. | §1, §18 | 5 |
| 2.1 Sections present & ordered | All 21 top-level sections present, correctly numbered/ordered, including 13a–d and 21a–d. | headings | 5 |
| 2.2 Scorecard as a table | §6 is a proper table with the required fields. §11's daily/weekly/monthly pivot tables are rendered as tables but show **R5→P→S5 (five levels/side)**, not the specified R3→P→S3, on all three timeframes. §3's Consensus Price cell is corrupted (see note above) — the table structure survives but one cell is unreadable. | §3, §6, §11 | 3 |
| 2.3 Method steps visible | §4–§5 show observations→normalisation→(claimed) consensus, though the "six independent feeds" narrative is internally inconsistent with its own down-weighting/exclusion text (see 1.1c). §8 gives a genuine candle-by-candle walk ✓. §9 is fully populated with regime/persistence/VOLator/KER — good. **§7 Charts has zero captions or placeholders under any of its five headings** — worse than "accept a caption or placeholder as evidence"; here there is no evidence at all, not even one generic note. | §4–§9 | 2 |
| 3.1 Quantitative claims sourced | §12 figures are mostly sourced (WGC, JPMorgan/TE, payrolls via §13c). **§14 Macro Context is a run of bare, unsourced figures** — Fed funds 3.50–3.75%, CPI 4.2%, US 10Y ≈4.47%, WTI/Brent, VIX ≈15.8 — none carries a named source or a pointer back to §4/§6/§13. | §1, §12, §14 | 2 |
| 3.2 Citations exist & contain data | Spot-checked 3: Reuters (03 Jul, "weak US jobs data reduced expectations," matches §12's payrolls driver), JPMorgan via TE (03 Jul, "$4,300" cap, verbatim-consistent with §12), LiteFinance/OCBC (05–06 Jul, dated and named). All named, dated, self-consistent; no fabrication found. | §4, §13a | 4 |
| 3.3 Calculations transparent | RSI2 for 06 Jul (67.4) approximately reproduces (≈70.5) from the report's own last two stated closes (Jul02→Jul03 +51.72, Jul03→Jul06 −21.68; RS=2.385) — within a few points, acceptable. Daily pivots reproduce exactly from the report's own stated 03 Jul H/L/C via the standard formulas. **ATR14 is never stated as a number anywhere in the report** (required by the checklist and needed to size stops/R — the linter itself has to infer it externally). §21a's direction score (+0.36) names only 3 of 6 signal×weight contributors numerically; the rest are "partly offset" with no figures. | §6, §11, §9, §21a | 2 |
| 3.4 Numbers reconcile — incl. level file | Internal: §1/§4/§5/§18 agree on the $4,158 consensus; §9's "swing is up (3,944 → **4,195**)" conflicts with §8's own citation of "**4,202** (Jul 06 high)" as the recent swing top — a small internal reconciliation slip. **External, vs `data/levels/XAUUSD_by_date/2026-07-07.csv` (`_full`):** 06-Jul Low $4,152.25 vs file $4,128.51 → diff $23.74 > 0.20×ATR14 ($22.10) — **Category-3 FAILURE**. 06-Jul Close $4,154.02 vs file $4,164.93 → diff $10.91, discrepancy band. RSI2 67.4 vs file 83.6001 → diff 16.2 > 15 — **Category-3 FAILURE**. Weekly pivots (built on the correct completed week ending 03 Jul, matching the file's `w_full_period`=2026-W27) reconcile tightly (all diffs <$1.2, consistent). **Monthly pivots fail badly on every level**: P $4,112.10 vs file $4,165.51 (diff $53.41), R1 $4,279.98 vs $4,387.95 (diff $107.97), S1 $3,840.61 vs $3,785.16 (diff $55.45) — all far past the $12.71 (0.115×ATR) failure line, and R2/S2/R3/S3 are off by $65–205. Back-solving the report's own P/R1/S1 implies it used a June high of ≈$4,383.59 against the level file's implied true June high of ≈$4,519.28 (both apparently share the same ≈$3,943–3,944 low and ≈$4,008.48 close) — i.e. the defect isolates to an understated June high, not the whole month's data. Daily pivots happen to land close to the file despite being built on the wrong (03 Jul, not 06 Jul) prior period — per the brief's explicit guidance this coincidence is not credited; the stated basis is unsound. | cross-section + level file | 1 |
| 4.1 Pillars conclude | §8 ("Bullish continuation — reversal risk"), §9 (TRANSITION, neutral-to-bullish), §10 (CONFIRM), §12 (each item tagged) all reach explicit labels. §14 lists items with individual leans but no single closing direction tag. | §8–§14 | 4 |
| 4.2 Peer/cross-asset interpreted | §10 states a mechanism per counter (USDX real-cost/real-yield channel, S&P/DAX easier-policy offset to risk-on, silver-beta confirmation) — not a bare correlation list. | §10 | 5 |
| 4.3 Synthesis reconciles tensions | §9 explicitly reconciles the KER-vs-short-term-momentum tension into the TRANSITION call; §15/§16/§18 state an explicit invalidation level (weekly P, $4,105); §21a explicitly flags "no conflict" with §17. The report never surfaces its own 1.1(c)/3.4 data-quality tensions as a limitation anywhere (see 5.3). | §15–§18, §21a | 4 |
| 4.4 Calibrated language | §17 is exactly one sentence, conditionally hedged ("contingent on… not surprising hawkish"), no stacking. Confidence (Medium) stated in §3/§18. | §3, §17 | 5 |
| 4.5 Card construction (M5, folded into C4 per protocol) | All three §21b cards are 100% `[object Object]` — no entry, stop, TP1–3, R, confluence or management text survives for any card, so essentially none of the M5 price-level rules (stop derivation, TP1/TP2/TP3 formula, Unit-3 BE-trail, wide-stop flag) can be checked at all — total evidence loss, worse than any partial-defect case. What does survive and is correctly applied: the conviction-threshold gate (§21a: score +0.36 > 0.25, correctly not suppressed), the Trade-3C conditional-breakout gate (§20: "no confirmed daily close above 4,544 → not yet triggered… presented as an armed conditional," correctly not falsely triggered — and cross-checked here against the level file, 4,544 sits only $2.43 above the true `swing_high_25d_full` = 4,541.57, i.e. well-grounded despite looking odd against the report's own broken monthly-pivot table), and the anchor-override logging (see 5.2). | §21a, §20, §21b, linter | 1 |
| 5.1 Data dated; staleness flagged | Most data dated. The core defect: a genuinely completed D−1 session (06 Jul, per the leak-free file) is mis-flagged as "still in-progress / single-source indicative," the opposite-direction staleness-handling error from the usual "stale presented as current." | §2, §6, §19 | 2 |
| 5.2 Assumptions up front | Daily-open-anchor override (07:00 UK vs the M1 00:00 UK default) is stated explicitly in §20, correctly labelled as an override with the default named — compliant handling per the brief's anchor-override guidance. Futures-to-spot normalisation N/A — no futures print is actually used anywhere despite GC=F being named. The single-source-Jul06-exclusion assumption is stated (§19), but it rests on the incorrect premise that 06 Jul was still open (see 1.2/5.1) — the disclosure itself is good, the fact it discloses is wrong. | §21b, §19, §20 | 3 |
| 5.3 Red flags surfaced | §12/§15 surface the JPMorgan/OCBC caution, hawkish-surprise risk and dollar-bounce risk well; §13d's FOMC-minutes collision is carried through §1/§12/§15/§16/§18 consistently. The report's own sourcing shortfall (1.1c) and stale-session mis-handling (1.2/5.1/3.4) are never surfaced anywhere as a limitation. | §12, §15, §21b | 3 |
| 5.4 Restrictions honoured | No bracketed variable names or module codes (M1..M5) found anywhere in the body (checked). No retail-dealer premium left un-normalised. Futures (GC=F) kept corroboration-only and in fact unused. Instrument common names used throughout. No enumerated 5.4 restriction openly breached. | whole report | 5 |

## 2. Category roll-up

| Cat | Rows | Mean | Level | Multiplier | Max | Points | Justification |
|---|---|---|---|---|---|---|---|
| C1 Prompt adherence | 1.1,1.2,1.3 | (2+2+5)/3=3.00 | 3 | 0.65 | 20 | 13.00 | Asset/tone/lookback right; as-of date set to D not D−1, tick spec never stated, claimed 6-source consensus is really 2. |
| C2 Structure | 2.1,2.2,2.3 | (5+3+2)/3=3.33 | 3 | 0.65 | 20 | 13.00 | All sections present/ordered; pivot tables show 5 levels/side not 3; §7 Charts has zero evidence under any heading. |
| C3 Accuracy & evidence | 3.1,3.2,3.3,3.4 | (2+4+2+1)/4=2.25 | 2 | 0.40 | 25 | 10.00 | §14 largely unsourced; ATR14 never stated; 06-Jul Low and RSI2 both fail the level-file tolerance; monthly pivots fail on every level by $53–205. |
| C4 Reasoning & judgment | 4.1,4.2,4.3,4.4,4.5 | (4+5+4+5+1)/5=3.80 | 4 | 0.85 | 20 | 17.00 | Pillar reasoning, cross-asset mechanism and calibration are strong; card construction (scored here per protocol) is pulled down hard by total evidence loss on all three cards' price levels. |
| C5 Currency & transparency | 5.1,5.2,5.3,5.4 | (2+3+3+5)/4=3.25 | 3 | 0.65 | 15 | 9.75 | Anchor-override logging and restriction discipline are clean; the mis-flagged-as-stale D−1 session and unsurfaced sourcing shortfall pull this down. |

## 3. Total, band, override

```
total = 13.00 + 13.00 + 10.00 + 17.00 + 9.75 = 62.75 → 63
band  = Moderate Trust (60-74)
override = none  (no fabricated source found on 3-citation spot-check; no enumerated 5.4
            restriction openly breached — the as-of-date/source-count problems are §1.1
            variable-adherence failures, not restriction breaches)
```

c1=3
c2=3
c3=2
c4=4
c5=3
total=63
band=Moderate
override=none
card_integrity=60.0
n_cards=3
n_duds=3
n_warns=0

## 4. Card Integrity (from `qa/gold_regen_qa1/lint_static/2026-07-07.csv`, verbatim)

| card_id | strategy | flags | dud | score = 100 − 40·#DUD − 10·#WARN |
|---|---|---|---|---|
| 2026-07-07_Trade_1 | Trade 1 - Daily Directional (LONG) | UNPRICED | True | 60 |
| 2026-07-07_Trade_2 | Trade 2 - Pivot, TRANSITION (breakout-side only) | UNPRICED | True | 60 |
| 2026-07-07_Trade_3C | Trade 3 - Momentum-Breakout 3C (TRANSITION, armed) | UNPRICED | True | 60 |

Report-level Card Integrity = mean(60, 60, 60) = **60.0** (n_cards=3, n_duds=3, n_warns=0; no
suppressed cards). This is a direct, mechanical consequence of the `[object Object]` corruption —
every card is UNPRICED because no entry/stop is machine-readable — and is unrelated to (and does
not double-count with) the qualitative card-construction discussion at row 4.5 above, which scores
the (very limited) surviving procedural evidence rather than the destroyed price fields.
