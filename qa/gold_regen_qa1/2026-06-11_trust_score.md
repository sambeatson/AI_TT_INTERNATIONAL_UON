# Trust Score — Gold_Report_11-Jun-2026.md (D = 2026-06-11, run gold_regen_qa1)

Level file used: `data/levels/XAUUSD_by_date/2026-06-11.csv` — `last_bar_date=2026-06-10 < date=2026-06-11` ✓ (leak-free, asserted).
Report's claimed basis: "Spot, loco London" / "Global 24-hour OTC market" (§2, §3) → points to the `_full` columns, but see 1.2/3.4 below — the report's own numbers are internally inconsistent about which basis they track.

## 1. Section 7 checklist

| Row | Notes | Evidence observed | Score (0–5) | Action required |
|---|---|---|---|---|
| 1.1 Variables respected | Asset/LBMA convention correct; GC futures used for corroboration only (§4 "Directional" relevance, §5 down-weighted) — but the "Normalized (USD/oz)" column applies **no** contango adjustment to the futures row (4,293.55→4,294, i.e. unchanged); USDX is the mandatory first counter in §10 ✓; §2's "Lookback window" field states only 5 sessions, the 25-session medium lookback is used (§9, Chart 3) but never declared in §2; tick size/name (required here since §21 produces strategies) is never stated anywhere — cards give "USD (X ticks)" implying 0.01 but never declare it | §2, §4, §5, §10, §21b | 4 | Add tick size/name declaration; state the futures contango size actually applied; add 25-session medium lookback to §2 |
| 1.2 Coverage & currency consistent | Dates are D-1/earlier throughout, no USD/tick unit drift. But basis is internally inconsistent: the report's own stated ATR(14)≈95 (Trade 1 TP3 field) sits close to the level file's `atr14_cash` (91.24, 4% off — consistent tier) while its claimed basis (§2/§3, continuous/loco-London) implies `_full` (atr14_full 108.475, 12.4% off — discrepancy tier). The report never states which basis its own OHLC/pivots are drawn from, and (see 3.4) neither basis reconciles cleanly | §2, §3, whole report | 3 | State explicitly which basis (cash/full) the OHLC and ATR are computed on and use it consistently |
| 1.3 Audience & tone | Senior Commodities Analyst register maintained throughout, no retail tone | §1, §18 | 5 | none |
| 2.1 Sections present & ordered | All top-level §1–§21 present and ordered correctly, §21a–d present. **§11 has no Monthly pivot table at all** — only Daily and Weekly subsections exist; "monthly" does not appear anywhere in the report | §11 | 3 | Add the missing Monthly floor-pivot table |
| 2.2 Scorecard as table | §6 is a proper table. §11's Daily table is 5-a-side (R5→S5) and Weekly is 3-a-side (R3→S3) — inconsistent with the required 3-levels-each-side (R3→P→S3) format across daily/weekly/monthly, and Monthly is absent entirely | §6, §11 | 3 | Standardise §11 to R3→P→S3, three timeframes |
| 2.3 Method steps visible | §4–§5 show observation→normalisation→consensus but the futures-to-spot adjustment size is never stated (only "down-weighted"); §8 is candle-by-candle; §9 has regime/persistence/overlap/VOLator; charts are captions only (accepted per brief, conversion artifact) | §4–§9 | 4 | State the contango figure actually subtracted |
| 3.1 Quantitative claims sourced | §1/§12/§14 claims mostly point to §4/§13; acceptable | text | 4 | none material |
| 3.2 Citations exist & contain data | Spot-checked FXStreet (10 Jun, "~4,100" quote in §13a matches §4's 4,110 entry — consistent), LiteFinance (10 Jun, used consistently in §6 as Source B twice), Investing.com (two distinct dated entries, 9 Jun news 4,293.55 and 5 Jun historical 4,468.69 — both named, dated, and not self-contradictory in isolation). No fabricated source found | §4, §13a | 4 | none — no hallucination override triggered |
| 3.3 Calculations transparent | Pivot formula standard and shown; RSI2 formula referenced. **RSI2 for the as-of row (Thu 11 Jun, ~3 stated) does not reproduce from the report's own five closes** (4,259.5 / 4,192.0 / 4,160.0 / 4,110.0 / 4,118.0): last-2-change gain=8, loss=50 → RS=0.16 → RSI2=13.8, not ~3. This is an arithmetic-reproduction failure per brief §4, independent of the level file | §6 | 2 | Recompute RSI2 for the as-of row from the stated closes; show the working |
| 3.4 Numbers reconcile — internally and against the level file | Internally, D-1 close 4,110.0 is consistent across §1/§3/§4/§6/§21b. **Externally it fails badly on both bases.** vs `_cash`: open 4,160.0 vs 4,150.16 (Δ9.84, discrepancy band ≤18.25); high 4,174.0 vs 4,186.26 (Δ12.26, discrepancy); low 4,090.0 vs 4,081.73 (Δ8.27, borderline); **close 4,110.0 vs 4,082.95 (Δ27.05, > failure threshold 10.49)**. vs `_full`: open Δ95.33, high Δ83.47, low Δ22.9, **close Δ38.54 — all exceed their failure thresholds**. Daily pivots inherit the error: report S1 4,075.3 vs `d_cash_S1` 4,047.70 (Δ27.6, fail) / `d_full_S1` 4,006.55 (Δ68.75, fail); report P 4,124.7 vs `d_cash_P` 4,116.98 (Δ7.72, discrepancy) / `d_full_P` 4,132.01 (Δ7.31, discrepancy). Monthly pivots cannot be checked — absent. The report's whole "4,090–4,098 shelf holding" narrative is contradicted by the level file: the real D-1 close (4,082.95 cash / 4,071.46 full) already sits at or below that shelf | §1, §3, §4, §6, §11, level file | 0 | Every OHLC and pivot value in §6/§11 must be regenerated from the actual D-1 bar; close is off by 2.6–3.7× the failure tolerance on both bases |
| 4.1 Pillars conclude | §8 "Bearish continuation"✓, §9 "Bias: Bearish"✓, §10 "CONFIRM"✓, §12/§14 use per-item directional tags without one final roll-up label — minor | §8–§10, §12, §14 | 4 | none material |
| 4.2 Peer/cross-asset interpreted | §10 states a mechanism per counter (opportunity cost, risk-on rotation), not a bare correlation list | §10 | 5 | none |
| 4.3 Synthesis reconciles tensions | §15 explicitly weighs oversold-bounce risk against the bearish trend; §21a states "no conflict with §17." Card construction folds in here: Trade 1's stop-loss cell is self-contradictory ("anchor: above 10 Jun high 4,174... " but stop given as 4,164, which is *below* 4,174, the level it claims to anchor above) — a reconciliation failure inside a single card; no anchor clock time is stated on any §21b card despite the §20-logged anchor override | §15–§18, §21b | 3 | Fix the Trade 1 stop/anchor-text contradiction; add anchor time to every card |
| 4.4 Calibrated language | §17 is exactly one sentence; confidence (Low–Medium) stated in §3 | §3, §17 | 5 | none |
| 5.1 Data dated; staleness flagged | Every row in §4/§6/§13 dated; single-source OHLC explicitly flagged "SINGLE-SOURCE (indic.)" throughout | §4, §6, §13, §19 | 5 | none |
| 5.2 Assumptions up front | Futures-to-spot normalisation is mentioned but its **size is never stated** (contrast brief: "the futures-to-spot normalisation stated with its size"); anchor override IS logged in §20 as a non-conformance (compliant handling — not silently presented as the anchor) but the **converted 07:00 UK time is not carried onto the individual §21b cards or into the report body outside §20**, contrary to the module's explicit requirement; single-source pivot propagation is carried into card caveats correctly | §21b, §19, §20 | 3 | State the contango size in USD; add the 07:00 UK anchor time to every card and to the report body outside §20 |
| 5.3 Red flags surfaced | §12/§15 risks present; §13d CPI collision explicitly carried into every card's caveats | §12, §15, §21b | 5 | none |
| 5.4 Restrictions honoured | No bracketed variable names, module codes, or framework name found in the body; instrument common names used; futures kept corroboration-only (label); no un-normalised retail premium detected | whole report | 5 | none — no restriction-breach override triggered |

## 2. Category roll-up

| Cat | Level (mean of rows, rounded) | Multiplier | Max | Points | Justification |
|---|---|---|---|---|---|
| C1 Prompt adherence | 4 | 0.85 | 20 | 17.00 | Core variables respected; tick size/name and 25-session lookback never declared, basis (cash/full) never stated |
| C2 Structure | 3 | 0.65 | 20 | 13.00 | All top-level sections present, but §11's Monthly pivot table is entirely missing and the daily/weekly pivot tier-counts don't match spec |
| C3 Accuracy & evidence | 0 | 0.00 | 25 | 0.00 | D-1 close, open, high, and all daily pivots diverge from the leak-free level file by 2–7× the stated failure tolerance on **both** cash and full bases; the as-of RSI2 does not reproduce from the report's own closes. No fabricated source found (override not triggered), but the factual claims here would mislead a decision-maker |
| C4 Reasoning & judgment | 4 | 0.85 | 20 | 17.00 | Pillars conclude, cross-asset mechanism is real, synthesis is coherent, language calibrated; card construction has one internal stop/anchor contradiction (Trade 1) and no anchor time stated on any card |
| C5 Currency & transparency | 5 | 1.00 | 15 | 15.00 | Every data point dated and flagged single-source; CPI collision surfaced into every card; anchor override logged as a non-conformance; contango size and per-card anchor time are the only gaps, folded into 5.2's row score, not enough to drop the category level |

## 3. Total, band, override

```
c1=4
c2=3
c3=0
c4=4
c5=5
total=62
band=Moderate
override=none
card_integrity=100
n_cards=3
n_duds=0
n_warns=0
```

Total = 17.00 + 13.00 + 0.00 + 17.00 + 15.00 = 62.00 → **62**, Moderate Trust (60–74).
Override check: no cited source found fabricated or self-contradictory on inspection (FXStreet, LiteFinance, Investing.com all named/dated/used consistently) → hallucinated-source override **not** triggered. No bracketed variable name, module code, or open restriction breach found in the body → restriction-breach override **not** triggered. `override=none`.

## 4. Card Integrity (linter rows, copied verbatim from `qa/gold_regen_qa1/lint_static/2026-06-11.csv`)

| card_id | strategy | flags | dud | card integrity |
|---|---|---|---|---|
| 2026-06-11_Trade_1 | Trade 1 - Daily Directional | CLEAN | False | 100 |
| 2026-06-11_Trade_2 | Trade 2 - Pivot (regime-aware breakout-side) | CLEAN | False | 100 |
| 2026-06-11_Trade_3A | Trade 3A - Momentum-Pullback (TREND_DOWN fork) | CLEAN | False | 100 |

Report-level Card Integrity = mean over non-suppressed cards = **100** (n_cards=3, n_duds=0, n_warns=0). This is a static, level-construction-only score (correct side/order/R-sizing) and is separate from the Trust Score total above — it does not reflect that the price frame the cards were built from does not match the leak-free D-1 bar (see 3.4).

## 5. Feedback

See `qa/gold_regen_qa1/2026-06-11_feedback.md`.
