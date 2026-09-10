# Trust Score v3.7 — Gold Daily Report, 28 May 2026

Run: `gold_regen_qa1` · Report: `reports/md/Gold_Daily_Report_28May2026.md` · Asset: XAUUSD · D = 2026-05-28
Level file: `data/levels/XAUUSD_by_date/2026-05-28.csv` (`last_bar_date=2026-05-27` < `date=2026-05-28`, confirmed leak-free)
Basis used for Category 3 checks: `_full` (report states "Spot, immediate settlement (loco London)" / "24-hour spot market" in §2, i.e. a continuous/full-day basis, not the `_cash` US session).

## 1. Section 7 checklist

| Item | Notes | Evidence | Score |
|---|---|---|---|
| 1.1 Variables respected | Asset framed correctly as XAU/USD spot, not COMEX (§2); GC=F kept corroboration-only, not blended (§19); USDX is the first row of §10 (mandatory-first-counter honoured); lookback 5d/25d stated (§2); USD/oz used throughout; tick (USD 0.01) stated and used consistently across all three cards. But: bracketed prompt-variable names and module codes appear repeatedly in the report body (§20, §21b) — an explicit restriction breach (see 5.4) that also reads as an unhonoured prompt-level restriction under this row. | §2, §10, §19, §20, §21b | 3 |
| 1.2 Coverage & currency consistent | Every dated figure in §2/§4/§6/§13 is D-1 (27 May) or earlier; §1/§3 describe 28 May (D) forward-looking only. No USD/oz vs tick vs "points" unit drift — conversions (USD ↔ ticks) shown consistently on every card. | whole report | 4 |
| 1.3 Audience & tone | Institutional register throughout (position-sizing note, ATR-cap language, structured pivot/confluence tables); no retail tone. Audience not explicitly named but tone matches "Senior Commodities Analyst" register implied by §1/§18/§21. | §1, §18, §21 | 4 |
| 2.1 Sections present & ordered | All of §1–§21 present in order, including §13a–d and §21a–d. | headings | 5 |
| 2.2 Scorecard as a table | §6 is a real table but uses a single "Corrob." text column instead of the specified Source A / Source B / Validation columns. §11's three pivot tables list **five** levels per side (R5→S5) instead of the specified three (R3→P→S3) — extra content, but a format deviation from the fixed spec. | §6, §11 | 3 |
| 2.3 Method steps visible | §4→§5 show observation→consensus clearly; §8 is candle-by-candle; §9 states persistence/overlap-ratio/VOLator explicitly. Gap: §2/§19 declare GC=F futures as a corroboration source, but no futures price or futures-to-spot adjustment ever appears anywhere in the report — the declared corroboration channel is never actually demonstrated. | §4–§9, §19 | 4 |
| 3.1 Quantitative claims sourced | Most §12/§14 figures carry a named source (Trading Economics, Deloitte/CNBC, FXStreet). A few (VIX 16.87, the raw S&P/DAX prints) rely on the blanket "Yahoo composite" note in §19 rather than a per-figure citation. | §12, §14, §19 | 4 |
| 3.2 Citations exist & contain data | Spot-checked Investing.com, CNBC, LiteFinance (§4/§13a): all named, dated, internally self-consistent (e.g. CNBC's −62.32/−1.38% reconciles to its own open/close). No fabricated source found. One reconciliation gap: LiteFinance's cited 26 May close (4,493.94, §4) does not match the report's own §6 table value for 26 May (4,508) — not fabrication, but an unresolved conflict between a cited source and the report's own validated table. | §4, §13a, §6 | 3 |
| 3.3 Calculations transparent | Daily-pivot formula is demonstrable from the report's own (though wrong, see 3.4) H/L/C. §20's M5 direction-score trace shows every weight and signal. **RSI2 does not reproduce from the report's own stated 5-day close series for 2 of 5 tabled dates**: recomputing RS = mean gain / mean loss over the report's own closes gives 23 May RSI2 = 65.0 (report states 39, diff 26 pts) and 26 May RSI2 = 36.4 (report states 44, diff 7.6 pts); only 27 May reproduces closely (computed 11.0 vs stated 12). Per the brief this is a Category 3 failure regardless of magnitude. ATR is only ever given as an unlabelled "ATR(14)-est ≈ 70" in the Trade 1 card, with no derivation shown, and no KER derivation shown beyond the asserted value. | §6, §21b, §20 | 1 |
| 3.4 Numbers reconcile — incl. vs level file | Internally: D-1 close is ~4,440–4,443 across §1/§3/§4/§6, reasonably consistent. Externally, against `data/levels/XAUUSD_by_date/2026-05-28.csv` (`_full`, ATR14=96.3007): D-1 **close** 4,443 vs 4,456.29 (diff 13.29 > 11.07 tol) **FAIL**; D-1 **low** 4,425 vs 4,401.48 (diff 23.52 > 19.26 tol) **FAIL**; open 4,506 vs 4,515.43 (diff 9.43, discrepancy band); ATR-est 70 vs atr14_full 96.30 (27.3% rel., >25% tol) **FAIL**. Daily pivots: R1/R2/R3/S2/S3 all fail tolerance (diffs 16.9–40.6 vs 11.07 threshold); only P and (marginally) S1 are within band. **Weekly pivots fail on all seven levels** (diffs 25.5–86.7 vs 11.07 threshold) — the report built its weekly P/R/S off a "partial current week" H/L/C (H 4,540/L 4,425/C 4,443) rather than the last **completed** week (2026-W21) the level file uses, so the whole weekly table is built off the wrong period. **Monthly pivots fail on all seven levels** (diffs 65.2–188.2) — the report's April H/L/C (4,773/4,353/≈4,500) diverges materially from the leak-free monthly H/L/C behind the level file. | cross-section + level file | 0 |
| 4.1 Pillars conclude | §8/§9/§10/§12/§14 each end in a clear, consistent direction label. Card construction (folded into C4 per protocol) shows real defects: Trade 1's stop rationale cites "prior-session close 4,508" when the report's own §6 gives the D-1 close as 4,443 (4,508 is actually the D-2/26 May close); Trade 1 and Trade 3C both invert the sign of the fixed 0.2R runner-stop rule (see 4.4); Trade 2's header figure for Weekly R1 (4,492) contradicts its own Confluences-cell figure (4,513). | §8–§14, §21b | 2 |
| 4.2 Peer/cross-asset interpreted | §10 gives an explicit mechanism for every counter (inverse purchasing-power channel for DXY, risk-on flow for equities, precious-metals beta for silver) — genuinely interpreted, not just listed. | §10 | 5 |
| 4.3 Synthesis reconciles tensions | §9 explicitly reconciles KER (Trending Down) vs the TRANSITIONAL label; §15/§18 lay out bull vs bear tension (RSI2 divergence vs the breakdown) rather than averaging it away; §20 explicitly checks §17 vs §21a for conflict. | §9, §15–§18, §21a | 4 |
| 4.4 Calibrated language | §17 is technically one sentence but is a long hedge-stacked run-on packing four qualifiers together. More materially, the wrong-signed 0.2R runner-stop calculation is stated with full confidence and no caveat on two of three live cards — an overconfident presentation of an incorrect figure. | §17, §21b | 3 |
| 5.1 Data dated; staleness flagged | Virtually every price/article is dated; 21–26 May OHLC explicitly flagged "indicative" pending full corroboration (§19); 27 May close explicitly flagged as pre-PM-Fix. | §4, §6, §13, §19 | 5 |
| 5.2 Assumptions up front | Anchor override stated explicitly and up front (§2) and logged again in §20. Futures non-blending stated (§19). No sizeable futures-to-spot normalisation was actually needed since GC=F was never numerically used. | §2, §19, §20 | 4 |
| 5.3 Red flags surfaced | §12/§15 surface speculative-long capitulation, Iran-talks reversal risk, and the RSI2/divergence bull case in the Risks table itself, not buried. Trade 3C's caveat explicitly carries the 29 May PCE event-collision into the card. | §12, §15, §21b | 4 |
| 5.4 Restrictions honoured | **Openly violated.** Bracketed prompt-variable names and module codes appear repeatedly in the report body: `[DAILY_OPEN_ANCHOR]`, `[CONVICTION_THRESHOLD]`, `[MAX_SIMULTANEOUS_LONG_SHORT]` (×2), `[PRODUCE_STRATEGY_RECOMMENDATIONS]` in §20; "M2 §9c weighted-mean formula" and four separate "M5 trace —" labels plus "M5 §7a limitation" in §20; `[MAX_SIMULTANEOUS_LONG_SHORT]` again in the §21b cross-card note. This is exactly the restriction the brief's row 5.4 names ("no bracketed variable names, no module codes (M1..M5)... in the report body") and triggers the framework's restriction-breach override. | §20, §21b | 0 |

## 2. Category roll-up

| Category | Row mean | Rubric level | Multiplier | Max | Points | Justification |
|---|---|---|---|---|---|---|
| 1. Prompt Adherence | (3+4+4)/3=3.67→4, reduced 1 level for restriction-breach override | **3** | 0.65 | 20 | 13.00 | Variables well respected; reduced from 4 by the mandatory restriction-breach override. |
| 2. Structural Alignment | (5+3+4)/3=4.0 | **4** | 0.85 | 20 | 17.00 | All 21 sections present/ordered; scorecard/pivot tables deviate from the specified column/level format. |
| 3. Accuracy & Evidence | (4+3+1+0)/4=2.0 | **2** | 0.40 | 25 | 10.00 | RSI2 fails to reproduce on 2/5 dates; D-1 close/low, ATR-est, and nearly every daily/weekly/monthly pivot fail tolerance against the leak-free level file. |
| 4. Reasoning & Judgment | (2+5+4+3)/4=3.5→3 (rounded down per "pick the lower level when in doubt") | **3** | 0.65 | 20 | 13.00 | Strong narrative pillars and cross-asset mechanism; offset by repeated card-construction defects (sign error, wrong-close stop rationale, self-contradictory confluence figure). |
| 5. Currency & Transparency | (5+4+4+0)/4=3.25→3 | **3** | 0.65 | 15 | 9.75 | Data well dated, assumptions and red flags handled well; dragged down by the open restriction breach (row 5.4). |

**Total = 13.00 + 17.00 + 10.00 + 13.00 + 9.75 = 62.75 → 63 / 100**

## 3. Band & override

- **Band: Moderate Trust (60–74)** — 63 falls naturally in this band.
- **Override check:**
  - Hallucinated-source override: **not triggered.** Three-source spot-check (Investing.com, CNBC, LiteFinance) found no fabricated source; the LiteFinance/§6 conflict is a reconciliation gap (scored under 3.2/3.4), not a self-contradictory or impossible source.
  - Restriction-breach override: **triggered.** Bracketed prompt-variable names and module codes (`M2`, `M5` ×5, four `[VARIABLE]` tokens) appear repeatedly in the report body (§20, §21b). Per framework §6 this caps the band at Moderate Trust (60–74) and reduces Category 1 by at least one rubric level — both already applied above. The cap does not change the band here since the computed total (63) already sits inside Moderate Trust.

## 4. Card Integrity (from `qa/gold_regen_qa1/lint_static/2026-05-28.csv`, copied verbatim)

| card_id | flags | dud | Card Integrity (100 − 40·DUD − 10·WARN) |
|---|---|---|---|
| 2026-05-28_Trade_1 | CLEAN | False | 100 |
| 2026-05-28_Trade_2 | CLEAN | False | 100 |
| 2026-05-28_Trade_3C | CLEAN | False | 100 |

Report-level Card Integrity = mean over 3 non-suppressed cards = **100**.
(Card Integrity is static-linter-only and does not capture the sign-error and cross-reference defects found in the manual review — those are scored under Category 4 / 3.4 above and detailed in `2026-05-28_feedback.md`.)

## 5. Score line

```
c1=3
c2=4
c3=2
c4=3
c5=3
total=63
band=Moderate Trust (60-74)
override=restriction_breach
card_integrity=100
n_cards=3
n_duds=0
n_warns=0
```

Feedback: see `qa/gold_regen_qa1/2026-05-28_feedback.md`.
