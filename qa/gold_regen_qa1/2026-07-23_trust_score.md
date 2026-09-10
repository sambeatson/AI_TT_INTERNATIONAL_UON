# Trust Score — Gold_Report_23_Jul_2026.md (D = 2026-07-23, run gold_regen_qa1)

Framework v3.7, mapped per `docs/QA_PROTOCOL_TRADE_CARDS.md` and `qa/gold_regen_qa1/REVIEWER_BRIEF.md`.
Level file: `data/levels/XAUUSD_by_date/2026-07-23.csv` (`last_bar_date=2026-07-22` < D — leak-free, verified).
Basis used for comparison: `_full` (report describes "Spot, immediate settlement, loco London,"
"OTC London spot, T+2 settlement," "Global — 24-hour market" — a continuous-market description, not a
US-session one, so `_full` columns are the correct basis per brief §4). `_cash` was also checked where
noted; it fits no better.

## 1. Section 7 checklist

| Item | Notes | Evidence | Score |
|---|---|---|---|
| 1.1 Variables respected | Asset/spec/basis/unit/currency/tick all correctly stated; USDX first counter in §10; as-of = D-1; lookback 5/25; 6 independent sources claimed. But the daily-open anchor is handled inconsistently: §2 states "Session anchor: 00:00 UK" as a plain fact with no override flag; §20 separately claims "the instruction to override the standing anchor value was applied" without ever naming the standing value it replaced, and without logging it as the "non-conformance" the anchor rule requires. | §2, §20, Trade 1 card | 3 |
| 1.2 Coverage & currency consistent | All dated D-1 or earlier / D for session; USD/oz and ticks used consistently throughout (e.g. 8,503 ticks = $85.03 at $0.01/tick) | whole report | 5 |
| 1.3 Audience & tone | Consistent institutional register throughout, no retail tone | §1, §18 | 5 |
| **C1 mean** | (3+5+5)/3 = 4.33 → **level 4** | | |
| 2.1 Sections present & ordered | All of §1–§21 present, correctly ordered, all sub-sections (13a–d, 21a–d) present | headings | 5 |
| 2.2 Scorecard as table | §6 is a proper table with the required columns. §11: daily and weekly pivot tables print 5 levels each side (R5→S5) but the monthly table prints only 3 (R3→S3) per the brief's spec — inconsistent format across the three pivot tables in the same report | §6, §11 | 4 |
| 2.3 Method steps visible | §4–§5 show observation→normalisation→consensus with the futures-to-spot adjustment stated; §8 is a clean candle-by-candle read; §9 covers persistence/overlap/VOLator/KER; 5 chart captions present (accepted per brief) | §4–§9 | 5 |
| **C2 mean** | (5+4+5)/3 = 4.67 → **level 5** | | |
| 3.1 Quantitative claims sourced | Most figures point to §4/§6/§13, but some macro claims in §12/§14 are soft ("widely held," "roughly 68–70% probability") without a named source at point of use | §12, §14 | 3 |
| 3.2 Citations exist & contain data | Spot-checked Trading Economics (22 Jul, 4,151.55), USAGOLD (22 Jul, 4,135.20), TradingView (22 Jul, 4,144.83): all named, dated, and used consistently elsewhere in the report. No self-contradiction or fabrication found on this check | §4, §5 | 4 |
| 3.3 Calculations transparent | Pivot arithmetic reproduces exactly from the report's own stated H/L/C. But RSI2 for 22 Jul (94.93) does **not** reproduce from the report's own quoted closes: its own Net column shows both prior two session changes as gains (21 Jul +60.13, 22 Jul +79.51); with zero losses in a 2-period window RS is undefined and RSI2 must equal 100 — which is also exactly what the level file's `rsi2_full`/`rsi2_cash` show (100.0). This is an arithmetic failure per brief §4, independent of any basis question | §6, §21a | 1 |
| 3.4 Numbers reconcile (incl. vs level file) | Internally consistent (close identical across §1/§3/§4/§6/§21b; §11 pivots match §6's stated H/L/C exactly). Externally, against the leak-free level file: D-1 close, D-1 low, most daily and weekly pivot levels, and the 25-session swing extremes all fail the brief §4 tolerance table (see feedback file for the full list — 10 of the 17 checkable daily/weekly pivot+OHLC fields exceed the failure threshold) | §6, §11, level file | 0 |
| **C3 mean** | (3+4+1+0)/4 = 2.0 → **level 2** | | |
| 4.1 Pillars conclude | §8/§9/§10/§12/§14 all reach well-defended conclusions. The §21 strategy pillar does not: Trade 2 and Trade 3A are each built on a regime branch the report's own M5 methodology forbids for a TRANSITION regime (see 4.3 and feedback file) | §21a/b | 1 |
| 4.2 Peer/cross-asset interpreted | §10 gives an explicit mechanism per counter (why USDX/yields/silver/equities matter), not a correlation list | §10 | 5 |
| 4.3 Synthesis reconciles tensions | §15/§16/§18 reconcile short- vs medium-term, KER vs regime, §17 vs §21a thoughtfully at the narrative level. But the synthesis never flags that Trade 2 (pivot pullback limit) and Trade 3A (momentum-pullback) directly contradict the TRANSITION regime the report itself established in §9 — a direct self-contradiction the synthesis should have caught | §9, §21a, §21b | 3 |
| 4.4 Calibrated language | §17 is one calibrated sentence; confidence (Medium) stated in §3/§18; scenario confidence H/M/L in §16 | §3, §16, §17 | 5 |
| **C4 mean** | (1+5+3+5)/4 = 3.5 → **level 3** (rounded down per reviewer guidance: pick the lower level when the mean sits on a boundary and a material methodology gap is in play) | | |
| 5.1 Data dated; staleness flagged | Every price/article dated; 22 Jul session explicitly flagged "captured in progress"; monthly pivot explicitly flagged SINGLE-SOURCE-INDICATIVE throughout | §4, §6, §13, §19 | 5 |
| 5.2 Assumptions up front | Futures-to-spot normalisation stated with its size (3–5 USD) — good. Anchor override handling fails the brief's explicit test (see 1.1): stated in §20 as an "override... applied as instructed," not logged as the required non-conformance, original value never named, and not flagged on the Trade 1 card itself | §19, §20, Trade 1 card | 2 |
| 5.3 Red flags surfaced | Market/macro red flags well surfaced (RSI2 exhaustion, cross-asset contradiction, wide-stop flag, jobless-claims collision carried into §21b). But the Trade 2 / Trade 3A regime-branch non-compliance is a material methodology red flag that is nowhere disclosed | §12, §15, §21b | 3 |
| 5.4 Restrictions honoured | No module codes/bracketed variables/framework name in the body; §19 states no synthesised/interpolated price; futures used corroboration-only | whole report | 4 |
| **C5 mean** | (5+2+3+4)/4 = 3.5 → **level 3** (same rounding rationale as C4) | | |

## 2. Category roll-up

| # | Category | Max | Level | Multiplier | Points | Justification |
|---|---|---|---|---|---|---|
| 1 | Prompt adherence | 20 | 4 | 0.85 | 17.0 | Variables observed; anchor-override disclosure is the one real gap |
| 2 | Structural alignment | 20 | 5 | 1.00 | 20.0 | All sections present/ordered; only a minor pivot-table level-count inconsistency |
| 3 | Accuracy & evidence | 25 | 2 | 0.40 | 10.0 | RSI2 arithmetic does not reproduce; D-1 close/low and most pivots fail external reconciliation against the level file |
| 4 | Reasoning & judgment | 20 | 3 | 0.65 | 13.0 | Strong narrative synthesis; Trade 2 and Trade 3A built on a regime branch the report's own methodology forbids |
| 5 | Currency & transparency | 15 | 3 | 0.65 | 9.75 | Good staleness/red-flag handling generally; anchor-override and card-methodology gaps undisclosed |

Total = 17.0 + 20.0 + 10.0 + 13.0 + 9.75 = **69.75 → 70**

## 3. Total, band, override

c1=4
c2=5
c3=2
c4=3
c5=3
total=70
band=Moderate (60-74)
override=none
card_integrity=96.67
n_cards=3
n_duds=0
n_warns=1

Override check: no fabricated/hallucinated source found on the 3-citation spot-check (3.2) →
hallucinated-source override does not apply. The anchor-override handling (1.1/5.2) is a disclosure
failure, not an open, unambiguous breach of a stated restriction (the report does attempt, incompletely,
to disclose it in §20) → restriction-breach override not applied; this is instead penalised directly in
C1 and C5 above.

## 4. Card Integrity (linter rows, copied verbatim from `qa/gold_regen_qa1/lint_static/2026-07-23.csv`)

| card_id | strategy | flags | dud | card score |
|---|---|---|---|---|
| 2026-07-23_Trade_1 | Trade 1 — Daily Directional | CLEAN | False | 100 |
| 2026-07-23_Trade_2 | Trade 2 — Pivot, TRANSITION regime branch | WARN_TP3_ORDER | False | 90 |
| 2026-07-23_Trade_3A | Trade 3A — Momentum-Pullback | CLEAN | False | 100 |

Report-level card integrity = mean over non-suppressed cards (all 3 live) = (100+90+100)/3 = 96.67.
Card Integrity is separate from the 100-point Trust Score total above.

Feedback: see `qa/gold_regen_qa1/2026-07-23_feedback.md`.
