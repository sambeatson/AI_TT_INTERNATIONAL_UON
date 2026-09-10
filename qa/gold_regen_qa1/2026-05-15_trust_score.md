# Trust Score v3.7 — Gold_Daily_Report_15May2026.md (D = 2026-05-15)

Reviewer: gold_regen_qa1 session · ASSET = XAUUSD
Level file used: `data/levels/XAUUSD_by_date/2026-05-15.csv` (`last_bar_date` = 2026-05-14 < D — verified leak-free).
Basis used for Category 3 checks: report claims "Spot, T+2", "OTC London spot", "24-hour market" (§2, §3) →
checked primarily against `_full` columns; `_cash` columns checked as a cross-reference and noted where it
would change the verdict.

## 1. Section 7 checklist

| Row | Reviewer notes | Evidence observed | Score (0–5) | Action required |
|---|---|---|---|---|
| 1.1 Variables respected | Asset/LBMA convention, USDX-first counter, D−1 as-of, 5d/25d lookback, USD/oz, 7 sources (≥6) all respected. Tick relationship (100 ticks = USD 1) is used consistently throughout §21b but is never explicitly *stated* as a variable anywhere in §2. Anchor-override narrative (§2, §20) is internally confused: it describes the override as moving "the daily-open anchor... to 15 May 2026" and names "default was 29 April baseline" — but `[DAILY_OPEN_ANCHOR]` is a **time-of-day** (00:00 UK or 07:00 UK), not a date; the report conflates the anchor concept with a run/baseline date. The time actually used, 00:00 UK, is one of the two valid values and is applied consistently on the card (`anchor_broker 02:00`) — so this is a description defect, not a wrong anchor value. | §2 row "As-of date/time-zone"; §20 "Anchor override" row; §21b entry rows | 3 | Restate the anchor-override note correctly against the module's own definition (a time-of-day departure, logged as non-conformance, not a date); state the tick name/size explicitly in §2. |
| 1.2 Coverage & currency consistent | All data dates are D−1 (14 May) or earlier; session date is D (15 May) throughout §2/§6/§13/§21. USD/oz used with no unit drift; tick counts are a consistent derived unit, not a competing currency. | whole report | 5 | none |
| 1.3 Audience & tone | Senior Commodities Analyst / institutional register maintained throughout; no retail tone. | §1, §18 | 5 | none |
| 2.1 Sections present & ordered | All of §1–§21 present, correctly ordered, with §13a–d and §21a–d subsections present. | headings | 5 | none |
| 2.2 Scorecard as a table | §6 is a proper table with the required columns. §11's **weekly and monthly** pivot tables are ordered R3→P→S3 with three levels each side as specified; the **daily** table instead gives five levels each side (R5…P…S5) — more granular than, and structurally different from, the checklist's daily spec. No information lost, but it is a deviation from the specified daily format. | §6, §11 | 4 | Align the daily pivot table to the specified 3-level format, or note the R4/R5·S4/S5 extension as a deliberate addition. |
| 2.3 Method steps visible | §4→§5 show observation → normalisation → consensus with the futures-to-spot statement; §8 is candle-by-candle; §9 gives regime + persistence/overlap/VOLator; charts are captions only (docx→md conversion drop — not scored per brief). | §4–§9 | 5 | none |
| 3.1 Quantitative claims sourced | §1/§12/§14 claims mostly point to a named source or a cross-referenced section. | text | 4 | none |
| 3.2 Citations exist & contain data | Spot-checked three: TradingEconomics (14 May, named, dated, quote used consistently with §13a and §1's inflation narrative); USAGOLD (13 May, named, dated, quote consistent with the "steady buying on dip" physical-demand thread in §12); WGC commentary via VisualCapitalist (named, dated Apr 2026, quote consistent with the §12 structural-floor claim). All three are named, dated, and internally consistent — no fabrication detected on this sample (cannot fetch to confirm existence). | §4, §13a | 4 | none |
| 3.3 Calculations transparent | Pivot formulas are reproducible from the report's own stated H/L/C (verified: P/R1/S1/R2/S2/R3/S3 all recompute exactly from the report's own Thu-14-May O/H/L/C). RSI2 values are asserted, not shown with an RS/gain-loss derivation. **ATR(14) is never stated as an explicit number anywhere in the report**, despite being used pervasively as a stop/target sizing reference (§8, §9, §21b) — it must be back-solved from stop distances (≈USD 60–62 implied, e.g. "0.25×ATR ≈15" ⇒ ATR≈60; "78 USD ≈1.26×ATR" ⇒ ATR≈62). | §6, §11, §21b | 2 | State ATR(14) as an explicit number in §9/§20; show the RSI2 gain/loss derivation, not just the output value. |
| 3.4 Numbers reconcile — internally AND against the level file | **Internally** reconciled: D−1 close 4,652 consistent across §1/§3/§4/§6/§21b; §11 daily-pivot inputs match the §6 table. **Externally, against the level file, this fails badly and repeatedly.** See §2 of this document below for the full numeric breakdown: the daily pivot table is right at P/R1/S1 but wrong beyond ATR-tolerance at R2/R3/S2/S3; the **weekly pivot table is wrong at every level except R1**; the **monthly pivot table is wrong at every level, by USD 100–340**; the report's "25-session swing low" (4,585) is USD 84 away from the level file's `swing_low_25d_full` (4,500.66); the report's "early-April 5,050 high" is USD 161 away from `swing_high_25d_full` (4,889.20); and the implied ATR(14) (~USD 61) is ~39% below `atr14_full` (100.71) and ~23% below `atr14_cash` (79.67). These feed directly into Trade 2's and Trade 3C's entry/stop/TP construction. | cross-section + level file | 0 | See §2 below — regenerate §11 weekly/monthly pivots and the 25-session swing extremes from the actual prior data, and rebuild Trade 2 / Trade 3C off the corrected levels. |
| 4.1 Pillars conclude | §8, §9, §10, §12, §14 each end in a clear, self-consistent direction label. | those sections | 5 | none |
| 4.2 Peer/cross-asset interpreted | §10 gives an explicit mechanism per counter (dollar-denomination/real-yield channel for USDX; risk-appetite channel for equities), not a bare correlation list. | §10 | 5 | none |
| 4.3 Synthesis reconciles tensions | §9 explicitly reconciles the KER-ranging read against the bearish §8 sequence; §15–§18 and §21a explicitly cross-check the SHORT conviction against the §17 range forecast and find no contradiction. | §15–§18, §21a | 5 | none |
| 4.4 Calibrated language | §17 is one sentence; §16 gives explicit scenario probabilities (50/35/15); confidence labelled Medium-High with a stated basis. | §3, §17 | 4 | none |
| (Card construction, scored under C4 per brief) | All three cards (§21b) share the identical M5 rule violation: the Unit-3 break-even trail is computed **on the wrong side of entry for a SHORT** — "entry + 0.2R" placed *above* entry in every card, which is the module's rule for a LONG, not the SHORT direction all three cards trade. Per M5 (reviewer brief §3): "Unit 3 stop → entry ± 0.2R **in the profitable direction** (for a SHORT that is *below* entry)." This is not caught by the static linter (which checks stop/TP side and order, not the BE-trail field), so it is not reflected in Card Integrity — it is a reasoning/construction defect on 3/3 cards, not a linter DUD/WARN. Trade 2's TP3 also sits above TP1/TP2 for a SHORT (linter WARN_TP3_ORDER, consistent with this same directional-confusion pattern). Trade 2's and Trade 3C's stop/entry anchors are additionally built on the mis-derived monthly pivot and 25-session swing low from 3.4 above. | §21b, all three cards | 1 | Recompute the Unit-3 BE-trail on every card as entry − 0.2R for a SHORT (below entry), not entry + 0.2R; rebuild Trade 2 and Trade 3C's structural anchors from the corrected weekly/monthly pivots and swing low. |
| 5.1 Data points dated; staleness flagged | Every OHLC session and article carries a date; the Yahoo 17:52 intraday print is explicitly flagged as pre-close/indicative in §4/§5. | §4, §6, §13, §19 | 5 | none |
| 5.2 Assumptions up front | Futures-to-spot normalisation is *stated* but its size is asserted as "no basis adjustment... within a few dollars" — the brief's own tolerance table treats a USD 10–25 contango as the expected, normal size for this normalisation; the report's claim of near-zero contango is not evidenced and is not obviously consistent with that expectation. The anchor-override note is present (satisfies the letter of "log it") but, per row 1.1 above, misdescribes what was actually overridden. | §21b, §19, §20 | 3 | Justify or correct the "no adjustment" contango claim; correct the anchor-override description per row 1.1. |
| 5.3 Red flags surfaced | §12/§15 surface the relevant risks (India tariffs, real-yield headwind, positioning); the §13d Trump–Xi event collision is carried into all three cards' caveats. | §12, §15, §21b | 5 | none |
| 5.4 Restrictions honoured | No bracketed variable names, module codes (M1..M5), or framework name found anywhere in the report body. GC=F is consistently treated as corroboration-only, not as the priced asset. No evidence of an un-normalised retail dealer premium (none used). | whole report | 5 | none |

## 2. Category 3 external reconciliation — numeric detail (vs `data/levels/XAUUSD_by_date/2026-05-15.csv`)

Tolerances per brief §4 (against `atr14_full` = 100.71, `atr14_cash` = 79.67).

**Daily OHLC (Thu 14 May) — report vs `_full`:** O 4,686 vs 4,692.60 (Δ6.6, consistent) · H 4,702 vs 4,718.75
(Δ16.75, **discrepancy**) · L 4,642 vs 4,644.37 (Δ2.37, consistent) · C 4,652 vs 4,652.26 (Δ0.26, consistent).

**Daily pivots — report vs `_full`:** P 4,665.33 vs 4,671.79 (Δ6.46, discrepancy) · R1 4,688.67 vs 4,699.22
(Δ10.55, discrepancy, near the failure line) · S1 4,628.67 vs 4,624.84 (Δ3.83, consistent) · **R2 4,725.33 vs
4,746.17 (Δ20.84, FAILURE)** · S2 4,605.33 vs 4,597.41 (Δ7.92, discrepancy) · **R3 4,748.67 vs 4,773.60
(Δ24.93, FAILURE)** · **S3 4,568.67 vs 4,550.46 (Δ18.21, FAILURE)**.

**Weekly pivots — report vs `_full`:** **P 4,697.00 vs 4,660.28 (Δ36.72, FAILURE)** · R1 4,809.00 vs 4,819.91
(Δ10.91, discrepancy) · **R2 4,874.00 vs 4,924.37 (Δ50.37, FAILURE)** · **R3 4,986.00 vs 5,084.00 (Δ98,
FAILURE)** · **S1 4,632.00 vs 4,555.82 (Δ76.18, FAILURE)** · **S2 4,520.00 vs 4,396.19 (Δ123.81, FAILURE)** ·
**S3 4,455.00 vs 4,291.73 (Δ163.27, FAILURE)**.

**Monthly pivots — report vs `_full`:** every level fails: **P 4,648.33 vs 4,673.69 (Δ25.36)** · R1 4,946.67 vs
4,837.19 (Δ109.48) · R2 5,253.33 vs 5,052.70 (Δ200.63) · R3 5,551.67 vs 5,216.20 (Δ335.47) · S1 4,341.67 vs
4,458.18 (Δ116.51) · S2 4,043.33 vs 4,294.68 (Δ251.35) · S3 3,736.67 vs 4,079.17 (Δ342.50).

**Swing extremes — report vs `_full`:** 5-day swing high 4,775 vs 4,773.37 (Δ1.63, consistent) · 5-day swing low
(implied 4,642, the window low) vs 4,638.24 (Δ3.76, consistent) · **"25-session swing low" 4,585 vs
`swing_low_25d_full` 4,500.66 (Δ84.34, FAILURE)** · **"early-April 5,050 high" (§7 Chart 3) vs
`swing_high_25d_full` 4,889.20 (Δ160.80, FAILURE)**.

**ATR(14):** report never states it; back-solved from stop-sizing language it is ≈USD 60–62, vs `atr14_full`
100.71 (≈39% low, **FAILURE** threshold is >25%) and `atr14_cash` 79.67 (≈23% low, discrepancy band).

**RSI2:** report's Thu-14-May RSI2 = 0.9 vs `rsi2_full`/`rsi2_cash` = 0.0 (Δ0.9, consistent, within ≤5-point
tolerance either basis).

Using `_cash` instead of `_full` throughout narrows some of these (e.g. daily OHLC fits `_cash` slightly
better) but does not change the weekly/monthly/swing-extreme/ATR verdicts — those fail against both bases.

## 3. Category roll-up

| # | Category | Max | Level | Multiplier | Points | Justification |
|---|---|---|---|---|---|---|
| 1 | Prompt Adherence | 20 | 4 | 0.85 | 17.00 | All Variables present; anchor-override description internally confused (row 1.1); tick unit never explicitly named. |
| 2 | Structural Alignment | 20 | 5 | 1.00 | 20.00 | All sections present/ordered; daily pivot table format deviates from the 3-level spec (no info lost). |
| 3 | Accuracy & Evidence | 25 | 2 | 0.40 | 10.00 | Internally reconciled and no fabricated source on spot-check, but weekly/monthly pivots, both 25-session swing extremes, and the implied ATR(14) diverge materially from the level file (row 3.4); ATR14 never stated explicitly (row 3.3). |
| 4 | Reasoning & Judgment | 20 | 4 | 0.85 | 17.00 | Strong pillar conclusions, mechanism-based cross-asset read, and genuine tension-reconciliation; pulled down by a systemic card-construction defect on 3/3 cards (BE-trail on the wrong side of entry). |
| 5 | Currency & Transparency | 15 | 4 | 0.85 | 12.75 | Data well-dated, red flags surfaced, restrictions honoured; assumption disclosure and anchor-override description each carry a minor gap (row 5.2). |

**Total = 17.00 + 20.00 + 10.00 + 17.00 + 12.75 = 76.75 → 77 / 100**

## 4. Band and override

`band = High Trust (75–89)`
`override = none` — no fabricated source found on the 3-citation spot-check; the anchor-override description
is confused but the anchor value itself (00:00 UK) is one of the two valid values and is applied consistently,
so this does not meet the restriction-breach bar.

## 5. Card Integrity (linter rows, copied verbatim from `qa/gold_regen_qa1/lint_static/2026-05-15.csv`)

| card_id | strategy | flags | dud | Card Integrity |
|---|---|---|---|---|
| 2026-05-15_Trade_1 | Trade 1 — Daily Directional | CLEAN | False | 100 |
| 2026-05-15_Trade_2 | Trade 2 — Pivot (TREND_DOWN) | WARN_TP3_ORDER | False | 90 |
| 2026-05-15_Trade_3C | Trade 3C — Momentum-Breakout (TRANSITION) | CLEAN | False | 100 |

Report-level Card Integrity = mean(100, 90, 100) = **96.67**

## 6. Summary fields

```
c1=4
c2=5
c3=2
c4=4
c5=4
total=77
band=High Trust
override=none
card_integrity=96.67
n_cards=3
n_duds=0
n_warns=1
```
