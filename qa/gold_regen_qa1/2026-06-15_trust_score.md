# Trust Score — Gold_Report_15Jun2026.md (D = 2026-06-15)

Run: `gold_regen_qa1` · Scored against `AI_Output_Trust_Score_Framework_v3.7` §4–7 and
`qa/gold_regen_qa1/REVIEWER_BRIEF.md`. Level file used: `data/levels/XAUUSD_by_date/2026-06-15.csv`
(`last_bar_date=2026-06-12 < 2026-06-15`, confirmed leak-free before use).

## 1. Section 7 checklist

| Row | Score (0–5) | Evidence location | Notes |
|---|---|---|---|
| 1.1 Variables respected | 2 | §2, §20, §21b cards | Asset/spec correct (spot XAU/USD, GC=F corroboration-only), USDX first counter (§10), as-of/lookback logic sound, ≥6 sources (§4). But: daily-open anchor is presented as *becoming* the run's anchor ("set to 07:00 UK for this run") rather than recorded as a logged non-conformance against the module's fixed anchor, in every place it appears (§2 note, §20 log, all three card `entry_mode_text` fields). Also: Trade 1/Trade 2 state a tick count with R; Trade 3A does not — inconsistent tick disclosure. |
| 1.2 Coverage & currency consistent | 4 | §2, whole report | Dates are D-1-or-earlier for data / D for session throughout; no USD/oz–tick–"points" drift found. Minor: §2's "Lookback window" field lists 9–15 Jun (folding the live D-session into a field the checklist expects to be data-only), though the report is careful elsewhere to mark 15-Jun as indicative. |
| 1.3 Audience & tone | 5 | §1, §18, masthead | Consistent institutional Senior-Commodities-Analyst register throughout; no retail tone found. |
| 2.1 Sections present & ordered | 4 | headings | All 21 top-level sections present, correctly ordered, §13a–d and §21a–d all present. §11's monthly pivot table is entirely absent (only daily + weekly given), so one required subcomponent is missing. |
| 2.2 Scorecard as a table | 3 | §6, §11 | §6 is a real table but collapses "Source A / Source B / Validation" into one combined "Source A×B/Outcome" column. §11's daily/weekly tables use R1–R5/S1–S5 (five levels each side) instead of the spec's three-each-side (R3→P→S3), and the monthly table is missing outright. |
| 2.3 Method steps visible | 4 | §4–§9 | Observation→normalisation→consensus shown in §4–§5; §8 is candle-by-candle; §9 gives regime + persistence/overlap/VOLator with numbers. Charts 1, 2, 3 and 5 carry only a bare heading — no caption or placeholder text (brief permits accepting a caption/placeholder for the docx→md image loss, but four of five charts supply neither). |
| 3.1 Quantitative claims sourced | 3 | §12, §14 | Most figures point to §4/§6/§13 (CPI, PPI, PBoC streak). A few are unattributed floating statistics: "China's wholesale demand hit a 16-year low" (§12), "VIX collapsed ~12.5%…to ~19.4" (§14), "India investment demand reportedly up to 40–45%" (§12, "reportedly" only). |
| 3.2 Citations exist & contain data | 5 | §4, §13a | Spot-checked Investing.com, USAGOLD, CNBC (all named, dated, quote a figure used consistently with themselves elsewhere in the report). None self-contradictory or impossible — no fabrication found. |
| 3.3 Calculations transparent | 4 | §6, §11, §9, §21a | RSI2 reproduces exactly from the report's own five closes (verified: RS=72.515/18.84=3.849→RSI2=79.38≈79.4). Daily P/R1/S1 reproduce exactly from the report's own stated H/L/C (P=(4230.57+4170.81+4182.43)/3=4194.60 ✓). §21a's −0.73 sums exactly from its six listed contributors. KER(13) stated. Gap: no raw ATR14 dollar figure is stated anywhere; it must be back-solved from the Trade 1 stop/runner math (≈US$110.8). |
| 3.4 Numbers reconcile (incl. level file) | 1 | §4, §6, §21b + level file | **Internal:** §21b Trade 1's MARKET entry (US$4,176.51) ≠ the report's own stated D-1 (12-Jun) close of US$4,182.43 shown in §4/§6 (Δ US$5.92) — the checklist's "D-1 close identical in §1/§3/§4/§6/§21b" fails on its own terms. **External:** 12-Jun close US$4,182.43 vs `prev_close_full` US$4,216.99, Δ US$34.56 = 0.291×ATR14 (fail threshold 0.115×ATR ≈ US$13.66); High Δ US$15.82 = 0.133×ATR (discrepancy band); daily P Δ US$16.61 (fail), R1 Δ US$33.77 (fail), S1 Δ US$17.39 (fail); weekly S1 Δ US$23.27 (fail), R1 Δ US$22.95 (fail), P Δ US$11.65 (discrepancy band); RSI2 Δ 20.6 pts vs file's 100.0 (fail, >15). Open (Δ3.35) and Low (Δ0.56) are consistent, and the 5-day swing extremes (US$4,363.50/4,023.55 vs file's 4,363.54/4,023.91) match almost exactly — so the failure is concentrated in the 12-Jun close and everything derived from it, not the whole dataset. |
| 4.1 Pillars conclude | 4 | §8,§9,§10,§12,§14 | Each ends in a direction label consistent with its own content. |
| 4.2 Peer/cross-asset interpreted | 4 | §10 | Gives a mechanism per counter (real yields/opportunity cost for USDX and equities, precious-metals beta for silver); DAX's mechanism is the thinnest of the four ("cross-validates the US-led risk bid"). |
| 4.3 Synthesis reconciles tensions | 4 | §15–§18, §21a | §9 explicitly resolves the overlap-ratio-vs-trend tension; §15 flags the Jun-11 demand spike as the key bull risk; §17/§21a agree with no unaddressed conflict. |
| 4.4 Calibrated language | 3 | §3, §17 | §17 is one sentence with a single "unless" condition (not stacked hedging) — compliant, but it is a long compound sentence right at the edge of the "one calibrated sentence" intent. Confidence (Medium) is stated in §3 but not repeated alongside the forecast itself. |
| 4.5 Card construction (folded into Cat. 4 per protocol) | 1 | §21b, cards JSON | Trade 1 and Trade 3A (both SHORT) state the Unit-3 stop moves to "entry +0.2R" on TP2 fill — for a SHORT, entry+0.2R sits *above* entry, locking a small loss, not the "profitable direction" the M5 rule requires. Repeated on 2 of 3 cards. Trade 2's entry is worded "Sell stop/limit," naming both order types at once (ambiguous; required interpretation to transcribe). |
| 5.1 Data dated; staleness flagged | 5 | §4, §6, §13, §19 | Every price/article dated; 15-Jun H/L/C explicitly flagged indicative/single-source; daily/weekly pivots explicitly flagged single-source-indicative. |
| 5.2 Assumptions up front | 1 | §21b, §19, §20 | The anchor override is disclosed (§2, §20) but never framed as the module-required "logged non-conformance" — it is instead presented as the operative anchor for the run ("set to 07:00 UK for this run", "anchor overridden to 07:00 UK" on every card). This is the specific failure pattern the brief flags explicitly. Single-source pivot propagation is, by contrast, correctly carried onto every affected card. |
| 5.3 Red flags surfaced | 5 | §12, §15, §21b | §12/§15 risks are thorough; §13d's FOMC collision is carried into all three card caveats. |
| 5.4 Restrictions honoured | 3 | whole report | No synthesised price presented as sourced; GC=F kept corroboration-only with no numeric futures print used as spot; no module codes/bracketed variable names/framework name found anywhere in the body. But: the pivot trade (Trade 2) would normally be suppressed under the strategy-suppression contract for single-source-indicative pivots, and is produced anyway "per analyst instruction" (§11/§19/§20) — a disclosed but real departure from a stated restriction. |

## 2. Category roll-up

| # | Category | Max | Row mean | Level | Multiplier | Points | Justification |
|---|---|---|---|---|---|---|---|
| 1 | Prompt adherence | 20 | (2+4+5)/3=3.67 | 4 | 0.85 | 17.00 | All Variables respected except the anchor-override framing (1.1) and minor tick-disclosure inconsistency. |
| 2 | Structure | 20 | (4+3+4)/3=3.67 | 4 | 0.85 | 17.00 | All 21 sections present/ordered; monthly pivot table missing, pivot level-count off-spec, §6 columns collapsed, most charts bare. |
| 3 | Accuracy & evidence | 25 | (3+5+4+1)/4=3.25 | 3 | 0.65 | 16.25 | Sourcing and arithmetic transparency are solid; reconciliation against the level file fails materially on the 12-Jun close and its derived daily/weekly pivots and RSI2, plus one internal entry/close mismatch. |
| 4 | Reasoning & judgment | 20 | (4+4+4+3+1)/5=3.20 | 3 | 0.65 | 13.00 | Pillar conclusions, cross-asset mechanism and synthesis are strong; card construction carries a repeated, rule-violating break-even-direction defect on 2 of 3 cards. |
| 5 | Currency & transparency | 15 | (5+1+5+3)/4=3.50 | 3 | 0.65 | 9.75 | Dating and red-flag surfacing are thorough; the anchor override is disclosed but mis-framed (not recorded as a non-conformance), and the suppression-contract departure, though disclosed, is a real restriction gap. |

**Total = 17.00 + 17.00 + 16.25 + 13.00 + 9.75 = 73 → 73/100**

## 3. Total, band, override

```
c1=4
c2=4
c3=3
c4=3
c5=3
total=73
band=Moderate
override=none
card_integrity=96.67
n_cards=3
n_duds=0
n_warns=1
```

Band: **Moderate (60–74)**.
Override check: no fabricated/self-contradictory source found on spot-check (3.2) → no hallucinated-source override. The anchor-override framing and the suppression-contract departure are both explicitly disclosed in the report body (§2/§19/§20/§11) rather than hidden, so they are scored within the normal rubric (rows 1.1, 5.2, 5.4) per the brief's own framing of the anchor issue as "a 5.2 / 1.1 failure," rather than treated as a restriction-breach override.

## 4. Card Integrity (linter rows, copied verbatim — not re-derived)

| card_id | strategy | flags | dud | Card Integrity |
|---|---|---|---|---|
| 2026-06-15_Trade_1 | Trade 1 — Daily Directional (SHORT — TREND_DOWN regime) | CLEAN | False | 100 |
| 2026-06-15_Trade_2 | Trade 2 — Pivot, regime-aware (SHORT — TREND_DOWN pivot breakdown) | WARN_R_TINY(0.19xATR) | False | 90 |
| 2026-06-15_Trade_3A | Trade 3 — Momentum-Pullback 3A (SHORT — TREND_DOWN) | CLEAN | False | 100 |

Report-level Card Integrity = mean(100, 90, 100) = **96.67** (n_cards=3, n_duds=0, n_warns=1). Separate from the 100-point Trust Score.
