# Trust Score — Gold_Report_Daily_12May2026.md (D = 2026-05-12, run gold_regen_qa1)

## 1. Section 7 checklist

| Row | Check | Level (0-5) | Notes | Evidence location |
|---|---|---|---|---|
| 1.1 | Variables respected | 1 | Asset definition, USDX-first counter, ≥6 sources, and tick discipline (1 tick = 0.01 USD/oz, used consistently in all tick counts) are all compliant. But the as-of/lookback window is anchored to Friday 8 May 2026 — **not** the last completed session strictly before D. The level file's `last_bar_date` (2026-05-11, Monday) proves the true D-1 session is Monday 11 May, which the report's §6/§9/§11 backbone never rolls forward to. | §2, §6, §11 vs level file `last_bar_date` |
| 1.2 | Coverage & currency consistent | 1 | §3/§4 cite Monday 11-May live prints ("Monday cash open USD 4,686.82", "11 May Asia print") as current, while §6 OHLC+RSI2, §9 regime/ATR and §11 pivots are all still built from Friday 8-May data — two different data vintages coexist and are never reconciled or flagged. | §3 vs §6/§9/§11 |
| 1.3 | Audience & tone | 5 | Institutional register throughout; no retail tone. | whole report |
| 2.1 | Sections present & ordered | 5 | §1–§21(a-d) all present, in order, including §13a-d. | headings |
| 2.2 | Scorecard as table | 5 | §6 is a table with all required columns (plus Trend/Final extras); §11 daily/weekly/monthly pivot tables ordered R3→P→S3, ≥3 levels each side. | §6, §11 |
| 2.3 | Method steps visible | 4 | §4→§5 show observation→normalisation→consensus; §8 candle-by-candle; §9 regime with persistence/overlap/VOLator; charts are descriptive placeholders (acceptable per brief). Futures-to-spot adjustment is described as an observed ~USD 30 market gap rather than a stated normalisation figure. | §4–§9 |
| 3.1 | Quantitative claims sourced | 4 | Most §1/§12/§14 figures point to §4/§6/§10/§13. | text |
| 3.2 | Citations exist & contain data | 4 | Spot-checked 3 sources (WGC Q1 2026 release, FinanceMagnates/UBP, TradingEconomics weekly framing): each named, dated, and used consistently with its own quote. No fabrication found. | §4, §13a |
| 3.3 | Calculations transparent | 3 | Daily pivot arithmetic verified correct from the report's own stated H/L/C (P/R1/R2/R3/S1/S2/S3 all reproduce exactly). §21a score Σsignal×weight verified (+0.5215 → rounds to +0.52, consistent with §1). RSI2 seed/method described but not shown numerically. **ATR(14)'s absolute value is never stated anywhere** despite being the multiplier basis for every card's R (only ratios like "1.04×ATR(14)" appear). | §6, §11, §9, §21a |
| 3.4 | Numbers reconcile (incl. vs level file) | 0 | Severe failure, internal and external. Trade 1's MARKET entry (4699.00, "anchored to 11-May settle USD 4,699.07") matches **neither** the report's own §6/§11 D-1 close (Friday, 4730.70) **nor** the true D-1 close from `data/levels/XAUUSD_by_date/2026-05-12.csv` (4734.78 full / 4733.67 cash) — off by USD 35.78/34.67, both exceeding the close-failure tolerance (>0.115×ATR14≈11.27). §11's daily pivots (correctly computed from the stale Fri H/L/C) miss the level file's true D-1 daily pivots by USD 9–45 on R1/S1/R2/S2/R3/S3, all exceeding the 0.115×ATR14 failure tolerance. Report's RSI2 82.4 vs level file `rsi2_full`=100.0: diff 17.6 > 15 → failure. Implied ATR (~64.0-64.4 from card R/ATR ratios) vs level `atr14_full`=98.0079: ~34.5% relative diff → failure (>25%). Trade 1's SL confluence text cites "weekly S2 (USD 4,609.92)" — a figure that matches neither §11's own weekly pivot table (S2 = 4,474.80) nor the level file's true weekly S2 (4,396.19 full / 4,399.02 cash). | §6, §9, §11, §21b vs level file |
| 4.1 | Pillars conclude | 4 | §9/§10 end in clear labels (Transitional-leaning-Bullish; CONFIRM); §8/§12/§14 give consistent directional colour without always naming a crisp single label. | §8–§10, §12, §14 |
| 4.2 | Peer/cross-asset interpreted | 5 | §10 gives mechanisms (dollar inverse-correlation, risk-appetite vs dollar-linked transmission for SPX), not a bare correlation list. | §10 |
| 4.3 | Synthesis reconciles tensions | 5 | §16 carries an explicit "Conflict flag" reconciling the 5-day Trending-Bullish vs 25-day Transitional read; §18/§21a consistent with §17. | §15–§18, §21a |
| 4.4 | Calibrated language | 5 | §17 is exactly one sentence; confidence (Medium) stated in §3/§18. | §3, §17 |
| 4.5 | Card construction (scored under C4 per §3 of the protocol) | 2 | All three cards inherit the wrong-session pivot/ATR base (see 3.4). Trade 1's own stated 3×ATR(14) runner cap (USD 4,891.60) sits **below** its own printed TP3 (USD 4,898.80) — TP3 is unreachable under the card's own rule. Trade 1's R = 66.60 = 1.04×(implied ATR) exceeds the card rule's 1×ATR wide-stop threshold but no wide-stop flag is printed. Minor arithmetic slips: Trade 2's "entry + 0.2R" stated as 4,715.89 (correct: 4,715.87); Trade 3A's stated as 4,678.12 (correct: 4,678.38); Trade 2/3A "Confluences at TPs" prose figures ($0.02-0.05) don't match the cards' own TP fields. | §21b (all three cards) |
| 5.1 | Data dated; staleness flagged | 1 | Every price/article carries a date, but the fact that the formal OHLC/RSI2/ATR/pivot backbone is a full session stale (Friday, not the true D-1 Monday) is never disclosed in §19 or §20; §19's "Data gaps" paragraph lists LBMA-fix and COT gaps but omits this one. | §19, §20 |
| 5.2 | Assumptions up front | 3 | Futures-to-spot gap discussed (§5); single-source monthly-pivot propagation correctly flagged into all three cards' caveats; the stale-session assumption is not disclosed anywhere. | §21b, §19, §20 |
| 5.3 | Red flags surfaced | 5 | RSI2-overbought, CPI Tier-1 collision, and Hormuz risk are all surfaced in §12/§15 and correctly carried into every card's caveats row. | §12, §15, §21b |
| 5.4 | Restrictions honoured | 4 | No bracketed variable names, module codes, or framework name in the body; retail JM Bullion quote correctly excluded from the median; CME futures kept corroboration-only. Minor: the entry anchor "anchored to 11-May settle USD 4,699.07" mislabels a Monday-Asia intraday print as a settlement/close price. | whole report |

**Daily-open anchor check:** compliant. §2 and every §21b card state "00:00 UK" consistently; the card field `anchor_broker` = "02:00" broker time is the correct UTC+3 conversion of 00:00 UK (BST, UTC+1) with no undisclosed override.

## 2. Category roll-up

| Cat | Level (mean of rows, rounded) | Multiplier | Max | Points | Justification |
|---|---|---|---|---|---|
| C1 Prompt adherence | 2 | 0.40 | 20 | 8.00 | As-of/lookback window anchored one session stale (rows 1.1/1.2); tone/source-count/tick discipline compliant. |
| C2 Structure | 5 | 1.00 | 20 | 20.00 | All 21 sections present, ordered, tabular where required; method steps visible with a minor futures-normalisation gap. |
| C3 Accuracy & evidence | 3 | 0.65 | 25 | 16.25 | Sourcing and citations sound; pivot/RSI2/ATR arithmetic internally correct but built on the wrong session and fails every level-file tolerance check; ATR(14) never stated numerically; a card confluence figure (weekly S2) matches nothing else in the report. |
| C4 Reasoning & judgment | 4 | 0.85 | 20 | 17.00 | Regime synthesis, cross-asset mechanism, and calibrated language are strong; card construction (also scored here) carries an unreachable TP3, a missed wide-stop flag, and several small arithmetic slips. |
| C5 Currency & transparency | 3 | 0.65 | 15 | 9.75 | Red flags and single-source propagation handled well; the session-staleness of the core dataset is never flagged, and one price is mislabelled as a settlement. |

## 3. Total, band, override

```
c1=2
c2=5
c3=3
c4=4
c5=3
total=71
band=Moderate
override=none
```

Override check: no cited source is fabricated (three spot-checked sources are named, dated, and self-consistent) → no hallucinated-source override. No explicit prompt restriction is openly breached (the daily-open anchor is handled compliantly; the stale-session issue is a currency/accuracy failure, already reflected in low C3/C5, not a breach of a stated restriction) → no restriction-breach override.

## 4. Card Integrity (from `qa/gold_regen_qa1/lint_static/2026-05-12.csv`, copied verbatim)

| card_id | flags | dud | integrity = 100 − 40·#DUD − 10·#WARN |
|---|---|---|---|
| 2026-05-12_Trade_1 | CLEAN | False | 100 |
| 2026-05-12_Trade_2 | CLEAN | False | 100 |
| 2026-05-12_Trade_3A | WARN_R_TINY(0.24xATR) | False | 90 |

```
card_integrity=96.67
n_cards=3
n_duds=0
n_warns=1
```

## 5. Feedback

See `qa/gold_regen_qa1/2026-05-12_feedback.md`.
