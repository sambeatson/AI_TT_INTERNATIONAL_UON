# Trust Score — Gold_Report_25Jun2026.md (D = 2026-06-25) — run `gold_regen_qa1`

Level file used: `data/levels/XAUUSD_by_date/2026-06-25.csv` (`last_bar_date=2026-06-24` < D — leak-free,
verified). Report states its basis as "Spot, immediate settlement (loco London), USD/oz" (§3/§5) —
continuous/24h — so all Category-3 checks below use the file's `_full` columns per brief §4.

## 1. Section 7 checklist

| Row | Check | Notes | Evidence | Score |
|---|---|---|---|---|
| 1.1 | Variables respected | Asset correctly defined as XAU/USD spot, GC=F corroboration-only (§2) ✓. USDX mandatory first counter, present (§10) ✓. As-of = 25 Jun, session data to 24 Jun ✓. Lookback 5/25 ✓. USD/oz ✓. 7 sources in §4 (≥6) ✓. **Gap:** tick size/name is never stated in §2 Market Definition, though used consistently as $0.01/tick across both Trade 1 and Trade 2 cards (124/12,400 and 49/4,900) — a declared-variable omission, not an inconsistency. | §2, §4, §21b | 4 |
| 1.2 | Coverage & currency consistent | All dated data ≤ 24 Jun, session = 25 Jun throughout §1–§21; no USD/oz–tick–"points" drift found. | whole report | 5 |
| 1.3 | Audience & tone | "Senior Commodities Analyst — Precious Metals" stated (title block, §1); institutional tone maintained, no retail phrasing. | title, §18 | 5 |
| 2.1 | Sections present & ordered | All of §1–§21 (incl. 13a–d, 21a–d) present in the specified order. | headings | 5 |
| 2.2 | Scorecard as a table | §6 is a fully compliant 9(10)-column OHLC+RSI2 table. §11 Daily is compliant (R5→P→S5, exceeds the 3-level minimum). **§11 Weekly and Monthly both collapse R2 and R3 into a single "R3/R2" row** — neither table shows three distinct levels above pivot as the checklist requires; 2 of 3 pivot tables fail this row. | §11 | 2 |
| 2.3 | Method steps visible | §4→§5 show observation→consensus (futures-to-spot step stated as "not required" since all accepted sources are native spot — acceptable, not contradicted). §8 is full candle-by-candle. §9 states overlap ratio, persistence, VOLator qualitatively. §7 chart headers (7.1–7.5) are present but carry no caption/placeholder noting the image drop — a minor formatting gap under the brief's leniency. | §4–§9 | 4 |
| 3.1 | Quantitative claims sourced | Most §1/§12/§14 figures trace to §4/§10/§13 (USDX 101.4, PCE 3.6%, VIX +13.8%). One vaguely-sourced figure: §12 "Q1 2026 jewellery demand... China −32%, India −18% YoY **per World Gold Council-style reads**" — a hedge-worded, non-specific attribution rather than a named/dated source. | §12 | 3 |
| 3.2 | Citations exist & contain data | Spot-checked 3: Investing.com (live) — named, dated 24 Jun, quotes prev close 4,110.11 (matches §6 24-Jun open) — consistent. TradingEconomics — named, dated, "~4,016... −3% on day"; against its own implied prior close (~4,110) that is closer to −2.3%, a minor internal rounding looseness, not fabrication. LBMA/GC=F align. — a blended attribution (two source types in one row) but dated and used consistently with §6/§11. No fabricated source found. | §4, §13a | 4 |
| 3.3 | Calculations transparent | Pivot **formulas** reproduce exactly from the report's own stated 24-Jun H/L/C (P=(H+L+C)/3=4,039.64 ✓ etc. — see 3.4 for whether those inputs are right). RSI2 is **not** shown as arithmetic anywhere, and the stated 24-Jun RSI2 = 5.8 does **not** reproduce: from the report's own 22-Jun (4,192.83) → 23-Jun (4,110.11) → 24-Jun (4,016.00) closes, both period changes are losses, so RS = 0 and RSI2 must be 0, not 5.8. ATR(14) is **never stated as a number** anywhere in the report — it is only back-inferable from Trade 1's "capped at 3.5×ATR(14)=406" (implying ATR≈116). KER is stated qualitatively (≈−0.35) but its own inputs aren't shown. | §6, §9, §21b | 1 |
| 3.4 | Numbers reconcile (incl. vs level file) | **Internally:** D-1 close (4,016) is identical across §1/§3/§4/§6/Trade-1 MARKET entry ✓; §11 daily pivots equal the levels quoted on the cards (Trade 2 entry 4,032 ≈ P−10%(P−S1) using §11's own P/S1) ✓. **Externally, against the level file:** D-1 low (3,988.00 vs true 3,959.13, diff 28.87 > 0.20×ATR) and close (4,016.00 vs true 3,999.13, diff 16.87 > 0.115×ATR) both fail; open/high pass. Daily pivots P, S1, S2, R3, S3 all fail the >0.115×ATR14 threshold (diffs of 15–60 USD); only R1 is consistent and R2 is a mid-band discrepancy. Weekly P/R1 are consistent, but S1/S2/S3 are all in the discrepancy band. **Monthly pivots fail across the board and badly** — diffs of 78–201 USD (0.6×–1.6×ATR14), an order of magnitude beyond the failure threshold. | cross-section + level file | 0 |
| 4.1 | Pillars conclude | §8 "Bearish continuation", §9 "Bias: Bearish", §10 "CONFIRM (bearish)", §12 each bullet tagged price-negative/-positive, §14 closes on a directional watch item. All consistent with their own content. | those sections | 5 |
| 4.2 | Peer/cross-asset interpreted | §10 states mechanisms (USD price effect, real-yield/opportunity-cost, broken safe-haven transmission), not a bare correlation list. | §10 | 5 |
| 4.3 | Synthesis reconciles tensions | §15/§16/§18 explicitly weigh the soft-PCE bull case against the hot-PCE bear case; §21a states "No conflict with the §17 forecast — both point lower." | §15–§18, §21a | 5 |
| 4.4 | Calibrated language | §17 is exactly one sentence; confidence (Medium) stated in §3/§18. | §3, §17 | 5 |
| 4.x | Card construction (per brief §3, scored under Category 4) | Static linter is CLEAN on all 3 cards (see §4 below), so side/order/R-multiple integrity is fine. But two substantive construction defects survive the linter: **(a)** Trade 1's Confluences row cites "TP1 near daily S1 3,964" while the TP1 row itself states 3,892 — a ~72-point (0.57×ATR) internal contradiction between the stated TP1 and its own justification. **(b)** Trade 1's stop is anchored to "22 Jun swing-area" (§21b), but the card-construction rule requires the 5-day swing extreme; the report's own §6 table shows the 5-day high is 18 Jun's 4,330.39 (matching the level file's `swing_high_5d_full` 4,329.82), not 22 Jun's 4,220.34 — the stop derivation does not use the swing level the rule specifies. | §21b, §6, level file | 2 |
| 5.1 | Data dated; staleness flagged | All prices/articles dated; 24-Jun O/H/L/C flagged SINGLE-SOURCE INDICATIVE in §6/§19. | §4, §6, §19 | 5 |
| 5.2 | Assumptions up front | Futures-to-spot step stated (§5, "not required"); anchor override stated on the card **and** in §20 (compliant handling — see anchor note below); single-source pivot propagation explicitly carried into Trade 2's caveat. | §21b, §19, §20 | 5 |
| 5.3 | Red flags surfaced | §12/§15 risks present; §13d PCE collision explicitly carried into Trade 1's caveat row. | §12, §15, §21b | 5 |
| 5.4 | Restrictions honoured | **Breach.** §20 Agent Log contains the literal module codes "M1 default 00:00 UK" (line 1) and "M5 trace" (line 4) inside the report body — exactly what M5's own instructions ("Section H variables must never appear by name in the report body") and the brief's row 5.4 ("no module codes M1..M5... in the report body") prohibit. This is an open, unambiguous restriction breach → **Restriction-breach override applies** (Section 6). | §20 | 0 |

### Daily-open-anchor handling (checked per brief §2)
Compliant. §20 explicitly logs the anchor as "OVERRIDDEN per run instruction (M1 default 00:00 UK)," the
same override is carried onto the Trade 1 card ("anchor overridden to 25 Jun session open per
instruction"), and it is never presented as if it were the instance's native anchor value — this is the
logged-non-conformance pattern the module requires, done correctly. (The module-name leak noted at 5.4 is
a separate defect from the anchor-handling substance, which is sound.)

## 2. Category roll-up

| Cat | Checklist rows (mean) | Raw level | Override adj. | Final level | Multiplier | Points (of max) | Justification |
|---|---|---|---|---|---|---|---|
| C1 Prompt adherence | 1.1=4, 1.2=5, 1.3=5 → 4.67 | 5 | −1 (restriction-breach override, §6) | **4** | 0.85 | 17.00 / 20 | Strong variable adherence; tick size never declared is the only intrinsic gap; one level removed for the restriction breach found at 5.4. |
| C2 Structure | 2.1=5, 2.2=2, 2.3=4 → 3.67 | **4** | — | **4** | 0.85 | 17.00 / 20 | All sections present/ordered; the weekly/monthly pivot tables collapsing R2/R3 into one row is the material gap. |
| C3 Accuracy & evidence | 3.1=3, 3.2=4, 3.3=1, 3.4=0 → 2.00 | **2** | — | **2** | 0.40 | 10.00 / 25 | D-1 low and close both breach tolerance; RSI2 does not reproduce from the report's own closes; most daily and effectively all monthly pivots fail against the level file. |
| C4 Reasoning & judgment | 4.1=5, 4.2=5, 4.3=5, 4.4=5, cards=2 → 4.40 | **4** | — | **4** | 0.85 | 17.00 / 20 | Direction logic, cross-asset mechanism and synthesis are strong; card construction carries a real confluence/TP mismatch and a mis-cited swing anchor on Trade 1. |
| C5 Currency & transparency | 5.1=5, 5.2=5, 5.3=5, 5.4=0 → 3.75 | **4** | — | **4** | 0.85 | 12.75 / 15 | Staleness flags, assumptions and red-flag surfacing are all sound; the module-code leak at 5.4 is the one clear restriction breach. |

## 3. Total, band, override

```
c1=4
c2=4
c3=2
c4=4
c5=4
total=74
band=Moderate Trust (60-74)
override=restriction_breach
```

Total = 17.00 + 17.00 + 10.00 + 17.00 + 12.75 = 73.75 → **74**.
Natural band from the total (60–74) is already Moderate Trust, which also satisfies the
restriction-breach override's cap of "Moderate Trust (60–74) regardless of total score" — so the override
does not further move the band here, but it is the reason C1 sits at 4 rather than the 5 its own checklist
rows would otherwise average to. No fabricated source was found on the 3-source spot-check (3.2), so the
hallucinated-source override does **not** apply.

## 4. Card Integrity (linter rows, copied verbatim from `qa/gold_regen_qa1/lint_static/2026-06-25.csv`)

| card_id | strategy | flags | dud | per-card integrity |
|---|---|---|---|---|
| 2026-06-25_Trade_1 | Trade 1 - Daily Directional (SHORT) | CLEAN | False | 100 |
| 2026-06-25_Trade_2 | Trade 2 - Pivot, regime-aware (TREND_DOWN → trend-follow short across pivot) | CLEAN | False | 100 |
| 2026-06-25_Trade_3A | Trade 3A - Momentum-Pullback (TREND_DOWN, SHORT) | CLEAN | False | 100 |

```
card_integrity=100
n_cards=3
n_duds=0
n_warns=0
```

All three cards are linter-CLEAN (no DUD, no WARN flags) — this is a separate, deterministic score from
the 100-point Trust Score above and does not offset the C3/C4 findings, which concern construction-logic
and data-accuracy defects the static linter does not check (e.g. the confluence/TP1 mismatch, the
mis-cited swing anchor, and the pivot input errors).

## 5. Feedback
See `qa/gold_regen_qa1/2026-06-25_feedback.md`.
