# Trust Score — Gold_Report_06Jul2026.md (D = 2026-07-06) · run gold_regen_qa1

Level file used: `data/levels/XAUUSD_by_date/2026-07-06.csv` (`last_bar_date=2026-07-03` < `date=2026-07-06`,
confirmed leak-free). Report claims basis "Spot, loco London, continuous" (§3, §2) → checked against
the `_full` columns throughout. Card linter rows copied verbatim from
`qa/gold_regen_qa1/lint_static/2026-07-06.csv`, not re-derived.

## 1. Section 7 checklist

| Row | Notes | Evidence observed | Score (0–5) | Action if below threshold |
|---|---|---|---|---|
| 1.1 Variables respected | Asset correctly XAU/USD spot, LBMA convention, GC futures corroboration-only and excluded from consensus (§2, §5, §19); USDX is the first cross-asset counter (§10); lookback 5/25 stated (§2); USD/oz throughout; tick (0.01 USD/oz) stated once (§21b) and used consistently. Gaps: the futures-to-spot basis is only described qualitatively ("small... basis"), never quantified in USD, unlike the module's expected stated-contango disclosure; the §5 weighted-median consensus itself draws on 4 of the 6 sources in §4 (GC futures and CNBC are context-only), so "≥6 independent sources for the consensus build" is met loosely (6 sources referenced) but not literally (6 feeding the blend). | §2, §5, §10, §19, §21b | 4 | — |
| 1.2 Coverage & currency consistent | D−1 close (4,180.06) identical across §1/§3/§4/§6/§21b MARKET entry — good. But §11's weekly pivot table is built from the wrong ISO week: it labels its input "prior week (22–26 Jun)" (ISO week 26) instead of the actually-prior completed week 29 Jun–3 Jul (ISO week 27), which is the week the report's own §6 table already covers. No unit drift elsewhere (USD/oz vs ticks kept consistent). | §6, §11, §16, §21b | 3 | List the drift point: §11 weekly pivots use week 26 data, one full week stale relative to D. |
| 1.3 Audience & tone | Institutional, Senior-Commodities-Analyst register maintained throughout; no retail tone. | §1, §18, whole report | 5 | — |
| 2.1 Sections present & ordered | All 21 top-level sections present, correctly ordered, with §13a–d and §21a–d all present. | headings | 5 | — |
| 2.2 Scorecard as table | §6 is a correctly-columned table (Session/O/H/L/C/RSI2/Src A/Src B/Validation). §11's daily pivot table is a real table (though it carries five levels each side, R5→S5, rather than the three-a-side R3→P→S3 the format specifies — more data, not less, so not scored down for that alone). §11's weekly and monthly pivots, however, are given only as inline prose sentences, not tables, and each is truncated to R1/R2/S1/S2 — the R3/S3 outer band is simply absent for both. | §11 | 3 | Convert weekly and monthly pivots to the same table format as daily, with all three levels each side. |
| 2.3 Method steps visible | §4→§5 show observation→normalisation→consensus; §8 candle-by-candle; §9 regime with persistence/overlap/VOLator/KER; §7 charts accepted as caption per the conversion-drop allowance. Gap: the futures-to-spot normalisation step is named but its magnitude is never shown. | §4–§9 | 4 | — |
| 3.1 Quantitative claims sourced | Several §12/§14 figures carry no named source or date: "Indian demand softened... Chinese buying improved slightly" (§12); US 10Y ~4.47%, WTI ~68.6, Brent ~71.9, CME FedWatch ~66% (§12, §14). These read as market-consensus figures with no citation, more than the "one or two" gaps that would keep this at Adequate. | §12, §14 | 2 | Flag for source verification: Indian/Chinese demand line, US10Y, WTI, Brent, FedWatch odds. |
| 3.2 Citations exist & contain data | Spot-checked 3: TradingEconomics 3 Jul (quote consistent with the report's own payrolls figures elsewhere); CNBC 1 Jul (quote consistent with "worst quarter" framing); LiteFinance 5 Jul (named, dated, quote used consistently as a mixed/near-term-recovery read). No internal contradiction or impossible date found in any of the three; no fabrication detected. | §4, §13a | 5 | — |
| 3.3 Calculations transparent | RSI2 reproduces exactly from the report's own five closes (verified by hand for Wed 1 Jul: RS = 22.56/9.09 = 2.482 → RSI2 = 71.28 ≈ the stated 71.3; Thu/Fri both-gain windows correctly give 100.0). Daily and monthly pivots reproduce exactly from the report's own stated H/L/C (P/R1/R2/R3/S1/S2/S3 all check out to the cent). But Trade 3C's TP1 (4,340) and TP2 (~4,430) are labelled "boundary + 1.0×width scaled to the operative shelf" without showing that scaling: applying the stated M5 formula (boundary 4,220 + 1.0×width 571.32) gives ≈4,791, not 4,340 — the actual derivation used is not shown or reproducible. | §6, §11, §21b (Trade 3) | 3 | Show the actual TP1/TP2 derivation for Trade 3C or replace with the formula as specified. |
| 3.4 Numbers reconcile — incl. vs level file | Internal reconciliation passes throughout. External, vs `2026-07-06.csv` (`_full`): D−1 close 4,180.06 vs file 4,174.97, diff $5.09 = 0.047×ATR14 (discrepancy-to-record band, not a failure); O/H/L all within tolerance. Daily pivots: P/R1/R2/R3 consistent; S1 diff $4.55 and S3 diff $6.17 both land just inside the discrepancy-to-record band. **Weekly pivots fail**: report P 4,089.82 vs file `w_full_P` 4,104.4633 (diff $14.64 = 0.135×ATR, > 0.115×ATR threshold); R1 4,220.26 vs 4,265.8467 (diff $45.59 = 0.42×ATR); S1 3,958.82 vs 4,013.5867 (diff $54.77 = 0.50×ATR); S2 3,828.38 vs 3,852.2033 (diff $23.82 = 0.22×ATR) — all Category-3 failures, traceable to the wrong-week input identified in row 1.2. **Monthly R1 also fails**: 4,367.94 vs `m_full_R1` 4,387.9467 (diff $20.00 = 0.184×ATR). The 25-day swing high used for Trade 3C's range and TP3 (4,515.55) vs `swing_high_25d_full` 4,545.87 (diff $30.32 = 0.279×ATR, > the 0.20×ATR high/low failure threshold). Daily pivots, OHLC, RSI2 and ATR14 (implied ≈110.0 vs file 108.7257, 1.2% relative) are all within tolerance. | §6, §11, §21b, level file | 2 | List the discrepancies above with location and size (done); regeneration must rebuild the weekly pivot table from the correct prior week and re-check the monthly R1 / 25d swing high inputs. |
| 4.1 Pillars conclude | §8, §9, §10 each end in an explicit direction/regime label. §12 and §14 close with a bullet (catalysts / positioning) rather than a synthesised directional line for the section as a whole — present as a list of considerations, not quite a "conclusion." | §8–§10, §12, §14 | 4 | — |
| 4.2 Peer/cross-asset interpreted | §10 gives a mechanism per counter (dollar pricing, real-yield headwind, haven-vs-risk-on ambiguity for equities) rather than a bare correlation list; the equity signal is explicitly flagged as ambiguous rather than resolved away. | §10 | 5 | — |
| 4.3 Synthesis reconciles tensions | §8/§9/§16/§18/§20 explicitly reconcile short-term-bullish vs medium-term-transitional, and KER-down vs price-up; §20 records an explicit §17-vs-§21a conflict check (none found). Card-construction quality (scored here per the brief) is undermined by the row-3.3 Trade 3C opacity — a real, if contained, reasoning-transparency gap in one of three cards. | §8, §9, §16, §18, §20, §21b | 4 | Same fix as 3.3: show the Trade 3C TP derivation. |
| 4.4 Calibrated language | §17 forecast is one sentence with a single conditional clause, not hedge-stacked; confidence stated as Medium (§1/§3); "likely"/"provided" used appropriately elsewhere. | §3, §17 | 5 | — |
| 5.1 Data dated; staleness flagged | Gold OHLC and every article dated; silver correctly flagged single-source-indicative (§19). But the weekly pivot input is one week stale (row 1.2/3.4) and this staleness is never flagged anywhere in the report — it is presented as "prior week" without qualification. | §11, §19 | 2 | Flag the weekly pivot staleness explicitly, or fix the underlying week. |
| 5.2 Assumptions up front | Daily-open anchor override stated in §20 and carried onto the Trade 1 card and caveats consistently (07:00 UK → 09:00 broker, matches the card's `anchor_broker`). Futures-to-spot normalisation named but not sized (row 1.1/2.3 gap). | §20, §21b, §19 | 4 | — |
| 5.3 Red flags surfaced | §12/§15 carry the relevant risks; the 8 Jul FOMC minutes event collision is explicitly carried into the Trade 3C card caveat. | §12, §15, §21b | 5 | — |
| 5.4 Restrictions honoured | No bracketed variable names, module codes, or framework name in the body; instrument common names used; futures kept corroboration-only and excluded from the spot consensus; retail (MQL5) feed kept out of the OHLC blend. One soft concern: the daily-open anchor deviation is disclosed and carried through consistently (§20, card, caveats), but is framed as "a configuration change... at the analyst's instruction... logged here per process" rather than as the module's own required framing — "a logged non-conformance, not an anchor." Disclosed, not hidden, so not treated as an open breach; noted rather than penalised heavily. | §20, §21b, whole report | 4 | Reframe the anchor deviation explicitly as a non-conformance, not a per-run configuration choice. |

## 2. Category roll-up

| Cat | Rows averaged | Mean | Level | Multiplier | Points (of max) | Justification |
|---|---|---|---|---|---|---|
| C1 Prompt adherence | 4,3,5 | 4.0 | 4 | 0.85 | 17.00 / 20 | Variables correctly scoped; weekly-period drift is the one moderate deviation. |
| C2 Structure | 5,3,4 | 4.0 | 4 | 0.85 | 17.00 / 20 | All sections present/ordered; two of three pivot tables not rendered as tables and missing outer bands. |
| C3 Accuracy & evidence | 2,5,3,2 | 3.0 | 3 | 0.65 | 16.25 / 25 | Daily-level numbers reconcile; weekly pivots, monthly R1, and the 25d swing high fail the level-file tolerance; several macro figures unsourced; one card's TP derivation not shown. |
| C4 Reasoning & judgment | 4,5,4,5 | 4.5→4 | 4 | 0.85 | 17.00 / 20 | Strong synthesis and mechanism-based cross-asset read; one contained card-construction transparency gap kept this off a 5. |
| C5 Currency & transparency | 2,4,5,4 | 3.75→4 | 4 | 0.85 | 12.75 / 15 | Good assumption and red-flag discipline; the one un-flagged data-staleness point (weekly pivots) is the main drag. |

**Total = 17.00 + 17.00 + 16.25 + 17.00 + 12.75 = 80** (rounded to nearest whole number: **80**)

## 3. Band and override check

- **Band: High Trust (75–89).**
- Hallucinated-source override: not triggered — three spot-checked citations (row 3.2) all named, dated, and internally consistent; no fabricated source found.
- Restriction-breach override: not triggered — the one candidate (daily-open anchor deviation) is disclosed and carried through consistently across §20, the card, and the caveats, which is the brief's "compliant handling" case, not a silent breach. Flagged as a wording/framing gap (row 5.4), not an override trigger.
- **override = none**

## 4. Card Integrity (linter rows, copied verbatim)

| card_id | flags | dud | Card Integrity = 100 − 40·#DUD − 10·#WARN |
|---|---|---|---|
| 2026-07-06_Trade_1 | CLEAN | False | 100 |
| 2026-07-06_Trade_2 | CLEAN | False | 100 |
| 2026-07-06_Trade_3C | CLEAN | False | 100 |

Report-level Card Integrity = mean(100, 100, 100) = **100**, over 3 non-suppressed cards, 0 DUD, 0 WARN.

## 5. Score-line summary

```
c1=4
c2=4
c3=3
c4=4
c5=4
total=80
band=High Trust
override=none
card_integrity=100
n_cards=3
n_duds=0
n_warns=0
```
