# Trust Score — Gold_Report_09Jul2026.md (XAUUSD, D = 2026-07-09)

Run: gold_regen_qa1 · Reviewer basis: `data/levels/XAUUSD_by_date/2026-07-09.csv` (`last_bar_date` =
2026-07-08 < D, confirmed leak-free) · `qa/gold_regen_qa1/lint_static/2026-07-09.csv` ·
`cards/baseline/gold/by_date/2026-07-09.json`

## 1. Section 7 checklist

| Row | Notes | Evidence | Score (0-5) |
|---|---|---|---|
| 1.1 Variables respected | Asset correct (XAU/USD spot loco London, GC=F kept corroboration-only, never blended — §5). USDX correctly the first row of §10. Lookback 5/25 stated (§2). **AS_OF_DATE wrong**: §2 states "09 July 2026" but `M1_Variables` fixes AS_OF_DATE to "the last completed session strictly before the report date" = 08 Jul 2026 — the report names D itself, not D−1. **Consensus build uses far fewer than the required ≥6 sources**: §4 lists 6 rows, but only Investing.com and GC=F are class "Core"; §5 explicitly states the other four (TradingEconomics, TradingView, MQL5, LiteFinance/OCBC) are "genuine ticks but represent the session trough, not the settled close" and are not blended — the $4,125/oz consensus is effectively a 1–2-source build, not the fixed 6. Tick size/name never stated as a value in §2's table (backed into cards only as "USD/ticks" at an implied 10-ticks-per-$1). | §2, §4, §5, §10 | 2 |
| 1.2 Coverage & currency consistent | Unlike the mis-labelled as-of date, the report does **not** leak D's own session as settled: §6's last OHLC row is 08 Jul (D−1), and §21c's backtest window ends at 08 Jul (t−1) — D itself never appears as a resolved bar or trade. Currency/units consistent throughout (USD/oz; every card's "USD (n ticks)" pair uses the same ~10-ticks-per-$1 conversion). So 1.1's as-of-date defect is a labelling error, not a data leak. | §2, §6, §21b, §21c | 3 |
| 1.3 Audience & tone | Senior Commodities Analyst, Precious Metals register held throughout; institutional tone; no retail framing. | §1, §18 | 5 |
| 2.1 Sections present & ordered | All 21 top-level sections present, correctly ordered, headings match spec, and — unlike weaker runs in this series — §7, §9 and §20 all carry real content (§9 in particular is fully populated: overlap ratio, persistence, VOLator, KER). | headings | 5 |
| 2.2 Scorecard as a table | §6 is a correct table with all required columns. §11's daily, weekly **and** monthly pivot tables all show **R5→S5 (5 levels/side, 11 rows)**, not the specified R3→P→S3 (3 levels/side) — deviates from the fixed 2.2 format on all three tables. | §6, §11 | 3 |
| 2.3 Method steps visible | §4–§5 show observations → normalisation → consensus with the futures-to-spot adjustment stated (qualitatively). §8 is a genuine candle-by-candle walk of all 5 sessions. §9 is fully populated (regime, persistence 0.59, overlap 0.62, VOLator −1.0/slope −0.28, KER −0.11). §7 "Charts" is 5 bare headings with **no caption or placeholder text under any of them** — the brief accepts a caption/placeholder as evidence for the dropped images, but this report supplies neither for any of the 5 toggles. | §4-§9 | 4 |
| 3.1 Quantitative claims sourced | §1/§12/§14 figures mostly carry a source (FOMC minutes, PBoC, dollar index >101, hike-odds range) or point to §4/§13. | §1, §12, §14 | 4 |
| 3.2 Citations exist & contain data | Spot-checked 3: Investing.com 08 Jul close (named, dated, used consistently in §1/§3/§4/§6 — internally consistent even though wrong vs the level file, see 3.4); CME GC=F settle/high/low (named, dated, high/low figures reused consistently in §5); TradingEconomics/PBoC reserve-build headline (named, dated, quote consistent in §12/§13a). None is self-contradictory or impossible on its own terms — no fabrication trigger. | §4, §13a | 4 |
| 3.3 Calculations transparent | RSI2 (28.7) reproduces closely (≈28.6) from the report's own stated 5 closes via RS = mean-gain/mean-loss over 2 periods — transparent, even though built on a wrong close (see 3.4). Daily/weekly/monthly pivots are correctly derived by the standard formulas from the report's own stated H/L/C. But ATR14 (only ever given as "≈109", never derived) and KER (−0.11, no derivation shown) are asserted, not shown; and Trade 1's runner "3×ATR cap → ~4,006 floor" does not reconcile to entry(4,103)−3×ATR(109)=3,776, nor to any other reference price in the card — an uncorroborated, non-reproducible number. | §6, §9, §11, §21b | 3 |
| 3.4 Numbers reconcile — **and reconcile against the level file** | Internally consistent (same wrong 08 Jul close/low reused everywhere). **Externally: fails badly.** Report's D−1 close 4,125.28 vs `prev_close_full` 4,077.47 → diff $47.81 = **0.46×ATR14** (fail threshold is >0.115×ATR ≈ $12). Report's D−1 low 4,096.55 vs `prev_low_full`/`prev_low_cash` 4,021.75 → diff $74.80 = **0.72×ATR** (fail, threshold ≈$9 abs / 0.20×ATR). RSI2 28.7 vs `rsi2_full`/`rsi2_cash` 0.0 → diff **28.7 pts**, exceeding the >15-pt failure line. Because the daily pivots are computed from the wrong close, **every daily pivot fails or sits in the discrepancy band** (P diff $40.89=0.39×ATR; S1 $81.72=0.79×ATR; S2 $115.65=1.11×ATR; S3 $156.48=1.50×ATR — all >>0.115×ATR). By contrast, **High** (diff $0.04) and **Open** (diff $3.97=0.04×ATR) both reconcile tightly, and the **weekly pivot table matches the level file almost exactly** (all 6 weekly levels within 0.02×ATR) — so only the 08 Jul close/low and everything downstream of them (RSI2, daily pivots, Trade 1/2's confluence claims) is broken; the weekly build and the open/high are sound. Monthly pivots also fail (diff up to 2.6×ATR) but are explicitly flagged single-source/indicative. | level file cross-check | 0 |
| 4.1 Pillars conclude | §8 → "Indecision"; §9 → "Ranging — Downward Bias"; §10 → "MIXED"; §12/§14 subsections each carry an explicit directional tag. All five conclude cleanly and consistently with their own content. | §8-§14 | 5 |
| 4.2 Peer/cross-asset interpreted | §10 gives a mechanism per counter (USDX real cost-of-holding, S&P/DAX haven-flow rotation) and an explicit, reasoned contradiction flag on which channel dominates the current tape — not a bare correlation list. | §10 | 5 |
| 4.3 Synthesis reconciles tensions | §15/§16/§18 lay out upside vs downside risk explicitly with stated invalidation levels; §9 explicitly states the KER read "agrees with the §9 regime... no contradiction to resolve"; §21a explicitly flags "no material conflict" between the SHORT score and the §17 range-with-bearish-lean forecast. | §15-§18, §21a | 5 |
| 4.4 Calibrated language | §17 is exactly one sentence, no hedge-stacking. Confidence (Medium) stated explicitly in §3 and §18. | §3, §17 | 5 |
| 5.1 Data dated; staleness flagged | Every price/article in §4/§6/§13 is dated; §19 explicitly characterises the OHLC as "accepted-close/directionally-corroborated" rather than tick-identical. The as-of-date mislabelling (1.1/1.2) is itself an unflagged dating inconsistency. | §2, §4, §6, §19 | 4 |
| 5.2 Assumptions up front | Single-source pivot propagation is carried into every card's caveats ("Indicative (single-source) pivots") ✓. But the futures-to-spot normalisation is only ever described qualitatively ("contango premium") — no stated $ size, unlike the brief's expected "roughly USD 10–25" disclosure. And the daily-open-anchor departure is called an "override... per run instruction" (§20) without ever stating the populated instance value it was overridden from, or logging it as the module's required "non-conformance" — it is instead presented plainly as "Daily-open anchor: 00:00 UK" in §2's Market Definition table, i.e. as the anchor value itself. | §21b, §19, §20 | 3 |
| 5.3 Red flags surfaced | Geopolitical two-way risk, dollar/real-yield headwind and the CPI event are surfaced in §12/§15 and correctly carried into card-specific caveats (Trade 1: 09 Jul jobless claims; Trade 2/3B: 14 Jul CPI collision). | §12, §15, §21b | 5 |
| 5.4 Restrictions honoured | No bracketed variable names or module codes (M1..M5) anywhere in the body (checked by search). Futures kept corroboration-only throughout. Instrument common names used. No enumerated 5.4 restriction openly breached. | whole report | 5 |

## 2. Category roll-up

| Cat | Rows averaged | Mean | Level | Multiplier | Max | Points | Justification |
|---|---|---|---|---|---|---|---|
| C1 Prompt adherence | 1.1,1.2,1.3 | (2+3+5)/3=3.33 | 3 | 0.65 | 20 | 13.0 | Asset/tone/lookback right; AS_OF_DATE mis-set to D; consensus effectively built off 1-2 of the required ≥6 sources. |
| C2 Structure | 2.1,2.2,2.3 | (5+3+4)/3=4.0 | 4 | 0.85 | 20 | 17.0 | All 21 sections present and well-populated (a real improvement over weaker runs in this series); pivot tables wrong level-count (R5→S5, not R3→S3); §7 has headings but zero caption/placeholder text. |
| C3 Accuracy & evidence | 3.1,3.2,3.3,3.4 | (4+4+3+0)/4=2.75 | 3 | 0.65 | 25 | 16.25 | No fabrication on spot-check, formulas shown and reproducible — but the stated D−1 close/low/RSI2 fail the level-file tolerance by a wide margin (0.46×ATR, 0.72×ATR, 28.7 pts respectively) and every daily pivot built from them fails too; High/Open and the entire weekly pivot table reconcile cleanly, so the fault is isolated to the close/low and its downstream daily pivots, not the whole report. |
| C4 Reasoning & judgment | 4.1,4.2,4.3,4.4 | (5+5+5+5)/4=5.0 → adjusted | 4 | 0.85 | 20 | 17.0 | The four analytical rows are excellent (defended conclusions, real cross-asset mechanism, explicit tension reconciliation, calibrated language). Per protocol, card construction is ALSO scored here: Trade 1 is built as a STOP order on a confirmed break, not the M5-fixed "market at the daily-open anchor"; Trade 2 (RANGE regime) is tiered at daily R3 instead of the required R1/R1.5/R2, and its TP2 is only ≈1.59R, not the fixed 2R; Trade 3B's entry/TP1 use 5-day swing levels (4,195-4,202 / "range mid" ≈4,118) instead of the required 25-day-range percentile zones (78.6-88.6% ≈ $4,393-4,450 full-basis; true range-mid ≈ $4,229) — a fundamentally different, non-compliant construction on all three cards. This pulls the category down one level from what the pillar rows alone would earn. |
| C5 Currency & transparency | 5.1,5.2,5.3,5.4 | (4+3+5+5)/4=4.25 | 4 | 0.85 | 15 | 12.75 | Dating and red-flag surfacing strong; normalisation size and the anchor-override non-conformance are stated only partially/implicitly. |

## 3. Total, band, override

```
total = 13.0 + 17.0 + 16.25 + 17.0 + 12.75 = 76.0 → 76
band  = High Trust (75-89)
override = none  (no fabricated source on 3-citation spot-check; no enumerated 5.4 restriction openly breached —
           the anchor and source-count gaps are scored as 1.1/5.2 deductions, not restriction-breach overrides)
```

c1=3
c2=4
c3=3
c4=4
c5=4
total=76
band=High
override=none
card_integrity=96.67
n_cards=3
n_duds=0
n_warns=1

## 4. Card Integrity (from `qa/gold_regen_qa1/lint_static/2026-07-09.csv`, verbatim)

| card_id | strategy | flags | dud | score |
|---|---|---|---|---|
| 2026-07-09_Trade_1 | Trade 1 — Daily Directional (SHORT) | CLEAN | False | 100 |
| 2026-07-09_Trade_2 | Trade 2 — Pivot, Range-Aware (SHORT fade of resistance) | CLEAN | False | 100 |
| 2026-07-09_Trade_3B | Trade 3B — Mean-Reversion (range fade, regime-driven) | WARN_R_TINY(0.29xATR) | False | 90 |

Report-level Card Integrity = mean(100, 100, 90) = **96.67** (n_cards=3, n_duds=0, n_warns=1; no suppressed
cards). Note: Card Integrity is a static/structural score and does not catch the M5 construction-rule
violations described under C4 above (wrong entry mode on Trade 1, wrong regime tier and TP2 multiple on
Trade 2, wrong percentile zone on Trade 3B) — those are not among the linter's DUD/WARN checks (stop
side, TP1 side, TP2 order, zero R, TP3 order, R-tiny/huge, target-far, duplicate) and are recorded
separately in the feedback file.
