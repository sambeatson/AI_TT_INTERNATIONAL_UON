# Trust Score — XAUUSD Gold_Report_30Jun2026.md (D = 2026-06-30) — run gold_regen_qa1

`last_bar_date` in `data/levels/XAUUSD_by_date/2026-06-30.csv` = 2026-06-29, which is < D. Leak-free, usable.

Report's claimed basis: §2 "Delivery / price basis: OTC London spot, loco London, T+2 settlement;
immediate-settlement spot quote" and "Scope: Global · 24-hour OTC market" — a continuous 24h basis, not a
US-cash-session range. All Category 3 external checks below use the level file's `_full` columns per brief
§4. `_cash` was also checked: every external check fails under `_cash` as well (report O/H/L/C sit
$35–51 from the `_cash` values vs. an `atr14_cash` of $99.41), so the basis choice does not change any
verdict below.

## 1. Section 7 checklist

| Item | Notes | Evidence | Score |
|---|---|---|---|
| 1.1 Variables respected | Asset correctly XAU/USD spot loco-London; GC=F used for "corroboration" only, never blended into the §5 consensus median ✓. USDX is the first row of §10 ✓. As-of = data through 29 Jun close = D−1 ✓. Lookback "5 sessions (execution) · 25 sessions (regime)" stated explicitly in §2 ✓. USD/oz stated in §2 ✓. Tick spec ($0.01/tick) is stated, but only in §20's Agent Log, not the report body proper, and it is **used inconsistently**: all three §21b cards state a tick count exactly 10× too small for their own $ risk (Trade 1 "340 ticks above entry" vs. its own "$34/oz = 3,400 ticks"; Trade 2 "330 ticks" vs. "$33/oz = 3,300 ticks"; Trade 3A "250 ticks" vs. "$25/oz = 2,500 ticks"). §4's price-evidence table only carries 4 "Core" sources into the §5 weighted-median build (2 more are explicitly "Directional"/context-only) — short of the ≥6-source consensus-build bar. | §2, §4, §10, §20, §21b | 3 |
| 1.2 Coverage & currency consistent | Every date in §2/§4/§6/§13/§21 is D−1 or earlier for data, D for the session. USD/oz used throughout; ticks appear only inside cards. No unit drift. | whole report | 5 |
| 1.3 Audience & tone | "Senior Commodities Analyst — Precious Metals"; institutional register throughout (§1, §18), no retail tone. | header, §1, §18 | 5 |
| 2.1 Sections present & ordered | All of §1–§21 present in the correct order, including all four §13 sub-sections and all four §21 sub-sections. | headings | 5 |
| 2.2 Scorecard as a table | §6 is a correctly-columned table (Date/O/H/L/C/RSI2/Trend/Source A/Source B/Valid.). §11 daily pivots: full R3→S3 (7 rows) — compliant. §11 **weekly pivots: R3 is missing** (table runs R2→S3 with no R3 row). §11 **monthly pivots: only R1/P/S1/S2 given — R2, R3 and S3 are all missing**, i.e. 4 of the required 7 levels. | §6, §11 | 2 |
| 2.3 Method steps visible | §4→§5 show observation→normalisation→consensus (futures excluded from the median as directional-only, a valid alternative to a numeric contango adjustment, and stated clearly). §8 is genuinely candle-by-candle for all 5 sessions. §9 gives overlap (0.38), persistence (0.62) and VOLator readings explicitly. §7's five chart headings carry no caption or placeholder text under any of them — the brief allows a caption/placeholder as sufficient evidence and this report supplies none at all; not scoring the conversion itself, but the total absence is a minor gap. | §4–§9 | 4 |
| 3.1 Quantitative claims sourced | PCE 4.1% in §14 traces to §13c's calendar row. Gold/USDX price claims trace to §4. But several other §12/§14 quantitative claims carry no source or cross-reference anywhere in the report: USDX "~101.3, 13-month high" (§1, §10, §12, §14 — never sourced), "bars +20% q/q" investment demand, and the jewellery breakdown "China −32%, India −18%" (§12). | text | 3 |
| 3.2 Citations exist & contain data (3 spot-checked) | TradingEconomics (29 Jun, "fell to $4,040… fourth straight monthly loss") — consistent between §4 and §13a. Vantage (25 Jun, "primarily a real-rates and dollar event") — consistent between §4's sub-$4,000 print and §13a's headline. RoboForex (23 Jun, "sellers have the upper hand," target 4,020) — named, dated, not contradicted elsewhere. All three named, dated, used consistently; none self-contradictory or impossible. No hallucination override triggered. | §4, §13a | 5 |
| 3.3 Calculations transparent | Daily pivots reproduce closely from the report's own stated Mon-29-Jun H/L/C via the standard formulas (P/R1/S1/R2/S2/R3/S3 all match to ~$1 rounding) — internally sound. **RSI2 does not reproduce from the report's own five stated closes** for two of the five rows: using the report's own closes (…4,012 → 4,026.8 → 4,051.3), the last two period-changes into both Fri-26-Jun and Mon-29-Jun are pure gains with zero losses, which the stated formula (RS = mean gain / mean loss over 2 periods) forces to RSI2 = 100 for both sessions — not the reported 35.2 and 62.8. Per brief §4 this is "an arithmetic error, not a basis difference" and is a hard Category 3 failure regardless of level-file proximity. ATR14 is never stated as an explicit number anywhere in §9/§21a; the only ATR figure in the whole report is the informal "ATR ~$89 is large" inside Trade 1's caveat. | §6, §11, §9 | 1 |
| 3.4 Numbers reconcile (internal **and** vs. level file) | **Internal:** D−1 close ($4,051.3) is identical across §1/§3/§4/§6/§21b MARKET-adjacent references — no internal break there. §11 daily pivots reproduce from §11's own stated H/L/C. **External, vs. `XAUUSD_by_date/2026-06-30.csv` `_full`:** Open $4,089 vs. file $4,079.20 (diff $9.80, consistent, ≤$10.78). High $4,089 vs. file $4,086.14 (diff $2.86, consistent). **Low $4,040 vs. file $4,000.66 (diff $39.34, threshold $23.94) → FAIL. Close $4,051.3 vs. file $4,016.68 (diff $34.62, threshold $13.77) → FAIL.** Daily pivots: only R1 (diff $12.27) and R2 (diff $10.17) land in the discrepancy band; **P (diff $25.51), S1 (diff $47.95), S2 (diff $61.19), R3 (diff $23.41) and S3 (diff $83.63) all FAIL** outright. Weekly pivots: only R2 (diff $12.88) is a discrepancy; **P (diff $26.39), R1 (diff $33.65), S1 (diff $47.16) and S3 (diff $60.67) all FAIL**, and R3 is simply missing. Monthly pivots: **all four stated levels (P, R1, S1, S2) FAIL by $90–$173**, and R2/R3/S3 are absent from the report entirely. Implied ATR (~$89, from Trade 1's caveat) vs. `atr14_full` $119.72 is a 25.7% relative gap — just over the 25% failure line. This is comprehensive, majority-of-checkable-figures failure, with no source fabrication detected — recorded as multiple Category 3 failures per brief §4, not the hallucination override. | cross-section + level file | 0 |
| 4.1 Pillars conclude | §8 ends "Range / counter-trend bounce — reversal risk"; §9 ends "Bias: Bearish" with Kaufman confirmation; §10 ends "MIXED → leaning CONFIRM"; §12's every bullet is tagged "(structural)/(cyclical)/(mixed)" with a price-negative/mixed label; §14's bullets each carry an implied directional read in-line. | those sections | 5 |
| 4.2 Peer/cross-asset interpreted | §10 states a mechanism per counter (USDX opportunity-cost channel; S&P/DAX as a hawkish-repricing proxy rather than a haven-rotation signal; Silver as industrial-leverage confirmation) — not a bare correlation list. | §10 | 5 |
| 4.3 Synthesis reconciles tensions | §15 explicitly lays out the bounce-vs-bearish-regime and structural-demand-vs-cyclical-headwind tensions; §16 explicitly states the forward view "respects the §9 bearish regime; it does not contradict it"; §21a's conflict flag notes §17 and the SHORT score align ("no material conflict") rather than reconciling an actual tension. | §15–§18, §21a | 4 |
| 4.4 Calibrated language | §17 is exactly one sentence (a single compound clause with "while"/"unless," no full stop mid-sentence), not hedge-stacked. Confidence stated explicitly as "Medium" in §1 and §3. | §3, §17 | 5 |
| 5.1 Data dated; staleness flagged | §4/§13 date every source. §11's monthly pivots are explicitly flagged "indicative" for provenance reasons. No stale-as-current data found. | §4, §6, §11, §19 | 5 |
| 5.2 Assumptions up front | Consensus-median methodology and the futures-exclusion policy are stated (§5). The corroboration-tolerance assumption is stated (§4: "±$0.50/oz for gold"). The daily-open anchor override (00:00→07:00 UK) is logged compliantly in §2's header/footnote **and** in §20's Agent Log with the reason ("at user request... logged as a configuration deviation") — this is the brief's compliant-handling test, and the report passes it. Gap: the same 07:00 UK anchor time is restated on Trade 1's card but **not** on Trade 2's or Trade 3A's cards. | §21b, §19, §20 | 3 |
| 5.3 Red flags surfaced | §12/§15 carry developed risk lists. §13d's jobs/ISM collision is correctly carried into **two of three** card caveats (Trade 1: "holding period spans §13d jobs/ISM — event risk"; Trade 2: "event collision with §13d jobs report"). Trade 3A's caveat ("pullback entry may not fill; lenient-corroboration data") omits it. | §12, §15, §21b | 4 |
| 5.4 Restrictions honoured | No bracketed variable names, module codes (M1..M5) or internal framework name found anywhere in the report body (checked by search). No retail dealer premium left un-normalised — JM-Bullion-style retail prints are absent from §4 entirely; only spot/CFD sources are used. **However:** §4's own footnote states the four "Core" spot reads span ~$25, "wider than [the stated ±$0.50] tolerance," yet §6 marks every one of the five OHLC rows "CORR" (corroborated) rather than the "single-source — indicative only" label the module's mandatory two-source-within-tolerance rule requires on a tolerance miss. This is disclosed in a footnote and in §19, so it is not hidden — but the §6 table itself, read on its own, presents under-corroborated data as validated. | whole report | 2 |

## 2. Category roll-up

| Cat | Rows avg | Level (rounded) | Multiplier | Max | Points | Justification |
|---|---|---|---|---|---|---|
| C1 Prompt adherence | (3+5+5)/3 = 4.33 | 4 | 0.85 | 20 | 17.00 | Asset/USDX/as-of/lookback/unit all correct; held down by a source-count shortfall against the ≥6 consensus-build bar and a systematic tick-count error repeated identically on all three cards. |
| C2 Structure | (5+2+4)/3 = 3.67 | 4 | 0.85 | 20 | 17.00 | All sections present and ordered, §6 is a real table; but §11's weekly pivots are missing R3 and the monthly table is missing R2/R3/S3 (4 of 7 required levels absent). |
| C3 Accuracy & evidence | (3+5+1+0)/4 = 2.25 | 2 | 0.40 | 25 | 10.00 | Citations spot-check clean and several key figures are sourced, but RSI2 fails to reproduce from the report's own stated closes on two of five sessions (a hard arithmetic error), ATR14 is never stated, and the overwhelming majority of externally-checkable D−1 OHLC and pivot figures (daily, weekly, monthly) fail the level-file tolerance by wide margins. |
| C4 Reasoning & judgment | (5+5+4+5)/4 = 4.75 | 5 | 1.00 | 20 | 20.00 | Every pillar concludes with a clear direction; cross-asset mechanism is interpreted, not listed; synthesis explicitly reconciles the bounce-vs-regime tension; §17 is calibrated and exactly one sentence. |
| C5 Currency & transparency | (5+3+4+2)/4 = 3.5 | 3 | 0.65 | 15 | 9.75 | Data is dated and the anchor override is logged compliantly (on the report body and in the Agent Log, though not on two of three cards); held down by §6 labelling every OHLC row "CORR" despite the report's own footnote admitting the tolerance was breached by roughly 50×. |

**Total = 17.00 + 17.00 + 10.00 + 20.00 + 9.75 = 73.75 → 74/100**

## 3. Band & override

- **Band: Moderate Trust (60–74).**
- Hallucinated-source override: not triggered — all three spot-checked citations are named, dated, and internally consistent; the D−1 data discrepancies are a reconciliation failure, not fabrication.
- Restriction-breach override: not triggered as a hard band cap — the CORR-mislabelling issue (§5.4 above) is disclosed in the report's own footnote/§19 rather than hidden, and no bracketed variable/module-code leakage was found; it is scored as a C5 deduction rather than an override. Reviewers should weigh this judgement call: it is close to a breach of M3's "mandatory" two-source corroboration rule.
- `override = none`

## 4. Card Integrity (linter rows, copied verbatim from `qa/gold_regen_qa1/lint_static/2026-06-30.csv`)

| card_id | strategy | flags | dud |
|---|---|---|---|
| 2026-06-30_Trade_1 | Trade 1 - Daily Directional | WARN_R_TINY(0.28xATR) | False |
| 2026-06-30_Trade_2 | Trade 2 - Pivot (regime-aware, TREND) | WARN_R_TINY(0.28xATR) | False |
| 2026-06-30_Trade_3A | Trade 3 - Complex (fork → 3A Momentum-Pullback) | WARN_R_TINY(0.21xATR) | False |

Card Integrity per card = 100 − 40×0 − 10×1 = 90 (all three; no DUD, one WARN each).
**Report-level Card Integrity = 90** (mean over 3 non-suppressed cards).

## Summary line

```
c1=4  c2=4  c3=2  c4=5  c5=3
total=74  band=Moderate Trust  override=none
card_integrity=90  n_cards=3  n_duds=0  n_warns=3
```

See `qa/gold_regen_qa1/2026-06-30_feedback.md` for the numbered, actionable defect list.
