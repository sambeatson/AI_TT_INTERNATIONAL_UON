# Trust Score — Gold_Report_27Jul2026.md (D = 2026-07-27) — run gold_regen_qa1

Basis claimed by report: "spot, loco London" (continuous OTC market) → checked against `_full` columns
of `data/levels/XAUUSD_by_date/2026-07-27.csv` (last_bar_date 2026-07-24 < D, confirmed). `_cash` columns
cross-checked as a sanity check; the report fails against both.

## 1. Section 7 checklist

| Row | Notes | Evidence | Score |
|---|---|---|---|
| 1.1 Variables respected | Asset/product/unit/lookback/≥6-sources/tick all correctly stated and used. Session anchor stated plainly as 00:00 UK in header/§2, but §20 separately calls it "[session anchor] override to 00:00 UK" — a bracketed placeholder, not a proper non-conformance log entry stating what value it overrides from. Ambiguous, undisclosed anchor handling. | header, §2, §20 | 4 |
| 1.2 Coverage & currency consistent | Daily block uses 24 Jul (correct, D−1). Weekly pivots explicitly labelled "(from W/E 17 Jul H/L/C)" — one full week stale; the correct completed week (W/E 24 Jul) is available and used for the daily block in the same section. No unit drift elsewhere. | §11 | 3 |
| 1.3 Audience & tone | Institutional Senior Commodities Analyst register maintained throughout; no retail tone. | §1, §18 | 5 |
| 2.1 Sections present & ordered | All 21 top-level sections (§1–§21, with 13a–d and 21a–d) present and correctly ordered. | headings | 5 |
| 2.2 Scorecard as table | §6 is a real table but merges "Source A"/"Source B" into one "Source A × B" column instead of the two named columns. §11 gives daily and weekly pivot tables but as 5-tier (R5…S5) not the specified 3-tier (R3→P→S3); **no monthly pivot table is rendered at all** — only a narrative sentence in "Source status." | §6, §11 | 3 |
| 2.3 Method steps visible | §4–§5 show observation→normalization→consensus and §8 is candle-by-candle; §9 gives regime/persistence/overlap/VOLator/KER. But the masthead and §2 both claim "GC=F used for cross-validation" and no futures quote or futures-to-spot contango adjustment appears anywhere in §4/§5 — the claimed corroboration step is never actually shown. | §2, §4–§5 | 3 |
| 3.1 Quantitative claims sourced | Most §1/§12/§14 claims point to §4/§13. The "GC=F cross-validation" claim in §2 is never backed by a cited figure anywhere in the report. | §2, §12, §14 | 4 |
| 3.2 Citations exist & contain data | Spot-checked Investing.com (§4), MyGoldCalc archive (§4/§6), and OCBC/LiteFinance (§13a): each is named, dated, and quotes a figure used consistently elsewhere. No fabrication found; no override triggered. | §4, §13a | 4 |
| 3.3 Calculations transparent | RSI2 (16.3) reproduces exactly from the report's own five stated closes (RS from the last two changes: gain 19.07, loss 98.16 → RSI2≈16.3). Daily pivots reproduce exactly from the report's own stated 24 Jul H/L/C via the standard floor formula. **ATR(14) itself is never stated as a number anywhere in the report body** (only used implicitly, e.g. "0.15×ATR"), contrary to the M5 requirement that ATR(14) be stated. | §6, §11, §21b | 3 |
| 3.4 Numbers reconcile — incl. vs level file | Internally, D−1 close (4068.20) is consistent across §1/§3/§4/§6/§21. Externally, against `XAUUSD_by_date/2026-07-27.csv` (_full, atr14_full=86.9436): **Open** 4027.58 vs 4049.18 → Δ21.60 (>0.20×ATR=17.39 → FAIL). **Close** 4068.20 vs 4053.47 → Δ14.73 (>0.115×ATR=10.00 → FAIL). High/Low individually inside tolerance. **Weekly pivots** (from the stale W/E-17-Jul week) vs `w_full_*`: P 4022.9 vs 4067.44 (Δ44.5), R1 4080.2 vs 4152.1 (Δ71.9), R2 4142.3 vs 4250.73 (Δ108.4), R3 4199.6 vs 4335.39 (Δ135.8), S2 3903.5 vs 3884.15 (Δ19.4), S3 3841.4 vs 3785.52 (Δ55.9) — all far beyond the 0.115×ATR≈10 failure line, and these feed Trade 2 (entry, invalidation) and Trade 3A (entry trigger, TP2) directly. Daily S1 (4034.9 vs 4022.98, Δ11.9) also fails. 25-day swing band ($3,965–$4,181 vs level-file $3,943.08–$4,220.62, Δ21.9/39.6) and 5-day swing low (4003.72 vs 3982.78, Δ20.9) both exceed the open/high/low failure line. | §1,§4,§6,§9,§11 vs level file | 1 |

## 2. Category roll-up

| Cat | Rows averaged | Mean → level | Multiplier | Points (of max) | Justification |
|---|---|---|---|---|---|
| C1 Prompt adherence | 1.1=4, 1.2=3, 1.3=5 → 4.0→4, **restriction breach reduces ≥1 level** | **3** | 0.65 | 13.0 / 20 | Variables and tone mostly respected; anchor handling ambiguous; restriction breach (below) forces a further step down from 4. |
| C2 Structure | 2.1=5, 2.2=3, 2.3=3 → 3.67→4 | **4** | 0.85 | 17.0 / 20 | All sections present and ordered; scorecard/pivot tables present but non-conforming (merged source columns, 5-tier not 3-tier, monthly pivot table missing); claimed futures step never executed. |
| C3 Accuracy & evidence | 3.1=4, 3.2=4, 3.3=3, 3.4=1 → 3.0→3 | **3** | 0.65 | 16.25 / 25 | Sourcing and citation integrity are fine and calculations shown are reproducible, but 3.4 (reconciliation against the level file) fails severely: a stale week feeding weekly pivots used live in two trade cards, plus D−1 open/close and both swing bands outside tolerance. |
| C4 Reasoning & judgment (incl. card construction) | 4.1=4, 4.2=5, 4.3=4, 4.4=4 → 4.25→4, **pulled down by card-construction defects** | **3** | 0.65 | 13.0 / 20 | Pillar reasoning, cross-asset mechanism, and synthesis are good. But: Trade 2's TP2 ($4,023, ~1.8R) is not entry±2R as the fixed rule requires for RANGE Trade 2; Trade 3A's entry ($4,020 stop-entry on a weekly-P break) does not follow the declared 3A recipe (57.5% retrace of a logged qualifying swing) at all; Trade 3A's U3 stop parenthetical ($4,028 = entry+0.2R) is on the wrong side of entry for a SHORT (rule requires entry−0.2R ≈ $4,012.4). |
| C5 Currency & transparency | 5.1=4, 5.2=2, 5.3=4, 5.4=1 → 2.75→3 | **3** | 0.65 | 9.75 / 15 | Data mostly dated and red flags surfaced (incl. FOMC collision on the Trade 3A card). 5.2 weak: futures-to-spot normalisation claimed but never shown; the "corroborated" label on the weekly pivots overstates confidence in a stale week. 5.4 fails outright — restriction breach (below). |

**Total = 13.0 + 17.0 + 16.25 + 13.0 + 9.75 = 69.0 → 69**

## 3. Total, band, override

- **total = 69**
- **band = Moderate (60–74)**
- **override = restriction_breach** — §20 Agent Log states, in the report body: *"Sentiment derivation: 7 articles, source-class weighted (**M2** §9c)"* and *"**M5** trace: direction-score weights..."*, and *"...with **[session anchor]** override to 00:00 UK"*. Row 5.4 explicitly forbids "bracketed variable names," "module codes (M1..M5)," and "the framework name" in the report body — all three appear. Per framework §6, this caps the band at Moderate (60–74) and drops Category 1 at least one rubric level. The unoverridden band would also have been Moderate at total=69, so the override is confirmatory here, not decisive on the band — but it is decisive on the C1 level (4→3) and is recorded as the binding override per the protocol's "override=" field.
- No hallucinated-source override: the three spot-checked citations (row 3.2) all exist, are dated, and quote figures used consistently elsewhere.

## 4. Card Integrity (linter rows, copied verbatim from `qa/gold_regen_qa1/lint_static/2026-07-27.csv`)

| card_id | report_date | strategy | flags | dud | per-card score |
|---|---|---|---|---|---|
| 2026-07-27_Trade_1 | 2026-07-27 | Trade 1 - Daily Directional | SUPPRESSED | False | — (suppressed, excluded from mean) |
| 2026-07-27_Trade_2 | 2026-07-27 | Trade 2 - Pivot fade at validated range extreme (Ranging regime). | CLEAN | False | 100 |
| 2026-07-27_Trade_3A | 2026-07-27 | Trade 3A - Momentum-Pullback. RANGE dual-gate fails (VOLator slope +0.01 not ≤ 0) → fork falls through to 3A. | CLEAN | False | 100 |

`card_integrity = 100 - 40*(#DUD) - 10*(#WARN)`, floored at 0, per card; report level = mean over the two
non-suppressed cards = (100 + 100) / 2 = **100**. Note: static integrity (stop side, TP ordering, R
bounds) is clean, but this does **not** certify the M5 *construction-recipe* defects recorded under C4
above (TP2 not exactly 2R on Trade 2; Trade 3A entry not a 57.5%-retrace of a logged swing; Trade 3A's
U3 stop on the wrong side of entry) — the linter does not check recipe conformance, only static
arithmetic integrity.

## Summary line

```
c1=3  c2=4  c3=3  c4=3  c5=3
total=69
band=Moderate
override=restriction_breach
card_integrity=100
n_cards=3
n_duds=0
n_warns=0
```
