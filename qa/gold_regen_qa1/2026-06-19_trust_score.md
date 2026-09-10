# Trust Score — Gold_Report_19-Jun-2026.md (XAUUSD, D = 2026-06-19)

Run: gold_regen_qa1 · Reviewer basis: `data/levels/XAUUSD_by_date/2026-06-19.csv` (`last_bar_date` =
2026-06-18 < D, confirmed leak-free) · `qa/gold_regen_qa1/lint_static/2026-06-19.csv` ·
`cards/baseline/gold/by_date/2026-06-19.json`

## 1. Section 7 checklist

| Row | Notes | Evidence | Score (0-5) |
|---|---|---|---|
| 1.1 Variables respected | Asset correct (XAU/USD spot, not COMEX-primary); USDX first counter present (§10). **AS_OF_DATE wrong**: §2 states as-of = 19 Jun (= D itself), but M1_Variables fixes as-of to "the last completed session strictly before the report date" = 18 Jun (D−1). Consensus build (§5) explicitly uses only 2 "core" spot sources for the weighted median, not the ≥6 independent sources the spec requires "for the consensus price build" (4 more sources are listed but downweighted to directional-only, never blended). Tick size/name never stated in §2's Market Definition table (only backed into later as "ticks at 0.01"). | §2, §5, §10 | 2 |
| 1.2 Coverage & currency consistent | Follows from 1.1: because as-of is mis-set to D, §6 carries a full "CORROBORATED" OHLC row for 19 Jun (D) itself, presented as settled fact (close $4,137.80) in the Exec Snapshot and Consensus Call — data for D presented as already known. This directly collides with §21c, which lists Fri 19 Jun as a **resolved t−1 backtest trade** (entry 4188.3 / exit 4137.8, "+1.0 TP1", "Days to res.: 1") on the very day Trade 1's live card also says it enters "Market at 07:00 UK... Reference 4,188.30 (19 Jun open)" — the "forward" trade and a "already-resolved" trade are the same entry on the same day. Internally self-contradictory. | §2, §6, §21b, §21c | 2 |
| 1.3 Audience & tone | Senior Commodities Analyst register maintained throughout; institutional tone; no retail framing. | §1, §18 | 5 |
| 2.1 Sections present & ordered | All 21 top-level sections present, correctly ordered, headings match spec. But §7 (Charts), §9 (Medium-Term Regime & VOLator) and §20 (Agent Log) are **headings with no body content at all** — §9 in particular is a required Deep-Dive pillar (asserted in §1 as "Transitional — Bearish", KER ≈ −0.35) that is never substantiated anywhere in the report body. | §7, §9, §20 | 2 |
| 2.2 Scorecard as a table | §6 is a correct table. §11's daily pivot table shows R5→S5 (5 levels/side) rather than the specified R3→S3 (3 levels/side); weekly/monthly tables show only R3..S1/S2, omitting S3. Format deviates from the fixed spec on all three pivot tables. | §6, §11 | 3 |
| 2.3 Method steps visible | §4–§5 show the futures-to-spot normalisation with its size (~+14 basis) ✓. §8 gives a summary judgement, not a true candle-by-candle walk of the 5 days. §9 (regime/persistence/overlap/VOLator) is completely empty despite being asserted elsewhere. §7 Charts has no per-chart caption or placeholder for any of the 5 toggled chart types — just one generic note. | §4-§9 | 1 |
| 3.1 Quantitative claims sourced | §1/§12/§14 figures mostly carry a source (Fed, Trading Economics, WGC) or point to §4/§13. | §1, §12, §14 | 4 |
| 3.2 Citations exist & contain data | Spot-checked 3 (Reuters/TE dollar headline, Goldman forecast cut, Fed hike-signal quote): each named, dated, quote consistent with its own row. No fabrication detected. | §4, §13a | 4 |
| 3.3 Calculations transparent | RSI2 reproduces exactly from the report's own stated closes for both 18 Jun and 19 Jun (two consecutive loss periods ⇒ RS=0 ⇒ RSI2=0, matches). Daily pivots reproduce exactly from the report's own stated H/L/C via the standard formulas. But KER (−0.35) and ATR14 are asserted/implied only, never shown as a derivation, and §9 (where KER method would live) is empty. | §6, §11, §9 | 3 |
| 3.4 Numbers reconcile — incl. level file | Internally self-consistent (pivots correctly derive from the report's own stated D−1 H/L/C). **Externally: FAILS.** Report's D−1 (18 Jun) close = 4,188.45 vs level file `prev_close_full` = 4,209.16 → diff $20.71 ≈ 0.173×ATR14(119.78), exceeding the 0.115×ATR14 (≈$11.5) Category-3 failure threshold (and worse against `_cash`, diff $28.53). Low is in the discrepancy band (diff $14.42 vs `prev_low_full`, ≈0.12×ATR). Because pivots are computed from this wrong close, daily S1 (diff $23.61), S2 (diff $26.51) and S3 (diff $38.60) all also exceed the failure threshold vs `d_full`. Weekly pivots, by contrast, reconcile tightly against `w_full` (all diffs <$2, well inside tolerance) — so the weekly build is sound; the daily build is not. Monthly is explicitly flagged SINGLE-SOURCE-INDICATIVE and not used for entry/stop pricing, so its large gap vs `m_full` is handled correctly per protocol (flagged, not silently wrong). | level file cross-check | 1 |
| 4.1 Pillars conclude | §8 concludes "Bearish continuation" ✓; §10 concludes "CONFIRM (bearish)" ✓; §12 items each carry a directional tag ✓. §9 reaches no conclusion in-body (it is empty) despite being cited in §1/§16/§18; §14 is a single placeholder line. | §8-§14 | 3 |
| 4.2 Peer/cross-asset interpreted | §10 gives a mechanism per counter (USDX real-cost channel, S&P risk-on rotation, DAX cross-validation, silver complex read), not a bare correlation list. | §10 | 5 |
| 4.3 Synthesis reconciles tensions | §15/§16/§18 address the bull/bear tension and state an explicit invalidation level; §21a matches §17. But the §8 "Trending" vs §1's "Transitional" medium-term regime label is never reconciled anywhere in the body, because §9 (where that reconciliation would happen) is empty. | §15-§18 | 3 |
| 4.4 Calibrated language | §17 is exactly one sentence, no hedge-stacking. Confidence (High) stated explicitly in §3 and §18. | §3, §17 | 5 |
| 5.1 Data dated; staleness flagged | Most sources/articles dated. As-of itself is mis-set to D rather than D−1 (see 1.1/1.2) with no staleness/leakage flag anywhere acknowledging that D's own session is being treated as settled ahead of Trade 1's stated anchor entry. | §2, §6 | 3 |
| 5.2 Assumptions up front | Futures-to-spot normalisation stated with size ✓; monthly single-source propagation carried into card caveats ✓. But the daily-open-anchor override ("07:00 UK anchor override," Trade 1) is stated on the card and in the report body, yet **§20 Agent Log — the handoff record the anchor rule specifically requires — is completely empty**, so the override is not recorded there as the module mandates. | §21b, §20 | 3 |
| 5.3 Red flags surfaced | PMI event collision, wide-stop flag and geopolitical two-way risk are surfaced in §12/§15 and carried into Trade 1's caveats. The Trade-1/backtest same-day self-contradiction (1.2) is itself an unflagged limitation, never surfaced anywhere. | §12, §15, §21b | 4 |
| 5.4 Restrictions honoured | No bracketed variable names or module codes (M1..M5) anywhere in the body (checked). Futures kept corroboration-only, not blended. Instrument common names used throughout. No enumerated 5.4 restriction is openly breached. | whole report | 4 |

## 2. Category roll-up

| Cat | Rows averaged | Mean | Level | Multiplier | Max | Points | Justification |
|---|---|---|---|---|---|---|---|
| C1 Prompt adherence | 1.1,1.2,1.3 | (2+2+5)/3=3.0 | 3 | 0.65 | 20 | 13.0 | Asset/tone right; as-of date wrong, consensus built off 2 sources not ≥6. |
| C2 Structure | 2.1,2.2,2.3 | (2+3+1)/3=2.0 | 2 | 0.40 | 20 | 8.0 | §9 and most of §7 effectively empty; pivot tables wrong level-count. |
| C3 Accuracy & evidence | 3.1,3.2,3.3,3.4 | (4+4+3+1)/4=3.0 | 3 | 0.65 | 25 | 16.25 | D−1 close and 3 of 6 daily pivots fail the level-file tolerance; weekly build sound; no fabrication. |
| C4 Reasoning & judgment | 4.1,4.2,4.3,4.4 | (3+5+3+5)/4=4.0 | 4 | 0.85 | 20 | 17.0 | Strong cross-asset mechanism and calibration; medium-term regime pillar unreconciled because §9 is empty. |
| C5 Currency & transparency | 5.1,5.2,5.3,5.4 | (3+3+4+4)/4=3.5→4 | 4 | 0.85 | 15 | 12.75 | Assumptions mostly stated; anchor override not logged in the (empty) Agent Log. |

## 3. Total, band, override

```
total = 13.0 + 8.0 + 16.25 + 17.0 + 12.75 = 67.0 → 67
band  = Moderate Trust (60-74)
override = none  (no fabricated source found on spot-check; no enumerated 5.4 restriction openly breached)
```

c1=3
c2=2
c3=3
c4=4
c5=4
total=67
band=Moderate
override=none
card_integrity=86.67
n_cards=3
n_duds=1
n_warns=0

## 4. Card Integrity (from `qa/gold_regen_qa1/lint_static/2026-06-19.csv`, verbatim)

| card_id | strategy | flags | dud | score |
|---|---|---|---|---|
| 2026-06-19_Trade_1 | Trade 1 — Daily Directional | CLEAN | False | 100 |
| 2026-06-19_Trade_2 | Trade 2 — Pivot (TREND_DOWN, trend-following) | CLEAN | False | 100 |
| 2026-06-19_Trade_3A | Trade 3 — Momentum-Pullback (variant 3A) | DUD_TP1_SIDE | True | 60 |

Report-level Card Integrity = mean(100, 100, 60) = **86.67** (n_cards=3, n_duds=1, n_warns=0; no suppressed cards).
