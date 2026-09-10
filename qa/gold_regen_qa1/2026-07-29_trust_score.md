# Trust Score — Gold_Report_29Jul2026.md (D = 2026-07-29, run gold_regen_qa1)

Ground truth used: `data/levels/XAUUSD_by_date/2026-07-29.csv` (`last_bar_date`=2026-07-28 < D=2026-07-29,
confirmed leak-free). Report's declared basis: continuous OTC London spot, 24-hour market (§2 "Global,
24-hour OTC spot market"; "OTC London spot ... immediate settlement (loco London)") — no cash-session
framing anywhere in the report — so checked against the `_full` columns throughout; `_cash` shown where
it materially changes the verdict.

## 1. Section 7 checklist

| Row | Score (0-5) | Notes | Evidence |
|---|---|---|---|
| 1.1 Variables respected | 4 | XAU/USD spot, LBMA loco-London stated; GC=F used corroboration-only (§4 FXLeaders row, not adopted as a row value); USDX is the first counter in §10; 5d/25d lookback stated; USD/oz used throughout; tick size ($0.01) stated and used consistently in §21. Minor gap: of the 6 retained (non-excluded) rows in §4, two ("Trading Economics" close and "TradingEconomics (CFD)") are the same publisher, so true source *independence* is closer to 5 organisations than 6 — the letter of "≥6 sources" is met by row count, not fully by the spirit of independence. | §2, §4, §10 |
| 1.2 Coverage & currency consistent | 5 | All dated figures are D-1 or earlier; §13d upcoming items are correctly D-only forward calendar; no USD/oz-vs-tick drift; §21 states the tick convention once and holds it. | whole report |
| 1.3 Audience & tone | 5 | "Senior Commodities Analyst — Precious Metals" byline; institutional register throughout, no retail tone. | §1, §18, footer |
| 2.1 Sections present & ordered | 5 | All of §1–§21 present in order, including 13a–d and 21a–d. | headings |
| 2.2 Scorecard as a table | 3 | §6 is a real table but uses "Date/Outcome" instead of the spec's "Session/Validation" (functionally equivalent, not a defect on its own). More material: §11's pivot tables are ordered **R5→P→S5** (report's own words: "Order R5→P→S5"), not the spec's three-levels-each-side **R3→P→S3** — a structural deviation from the prescribed depth/order. | §6, §11 |
| 2.3 Method steps visible | 5 | §4→§5 shows observation→normalisation→consensus with the futures-normalisation question explicitly addressed (stated as "not required" here, with reasoning); §8 is candle-by-candle; §9 shows persistence/overlap/VOLator; §7 chart headings present (accepted per brief — conversion drops images). | §4–§9 |
| 3.1 Every quantitative claim sourced | 3 | §4/§6/§13a figures are sourced. Several §14 macro figures are not individually sourced or dated (Fed funds 3.50–3.75%, US 10Y 4.59–4.66%) — asserted without a named source. | §14 |
| 3.2 Citations exist & contain data | 4 | Spot-checked three: Investing.com (28 Jul RT, day range 4,022.23–4,062.05, used consistently in §3/§4) — OK. Trading Economics "Gold Rebounds as Oil Prices Retreat" (27 Jul, "rose 1% toward $4,100") — named, dated; loosely worded ("toward $4,100") against the report's own 27 Jul close of $4,074.56, but not impossible or self-contradictory — not fabricated. FXStreet (28 Jul, RSI-below-50 quote) — named, dated, consistent with the report's own bearish RSI2 read. No fabrication found in the spot-check. | §4, §13a |
| 3.3 Calculations transparent | 2 | Sentiment tilt (§13b) and direction score (§20) both show full weighted-sum arithmetic — good. RSI2 is stated as a number only, no gain/loss derivation shown; reproducing RSI2(28 Jul) from the report's own five closes (mean gain/mean loss over the last 2 changes: +22.66, −44.56 → RS≈0.509 → RSI2≈33.7) lands ~3 points from the reported 36.7 — not egregious, but not shown or exactly reproducible either. ATR14 is never stated as a headline number, only backed out from stop/TP buffers (≈$72, implied consistently across the 0.25×, 3×, 3.5× ATR references — internally self-consistent, but never stated outright). Trade 3C has no stated R at all (card notes confirm no "Risk (R)" row). | §6, §9, §21 |
| 3.4 Numbers reconcile — incl. vs level file | 0 | Internally the D-1 close (~$4,030) is consistent across §1/§3/§4/§6/§21b. Externally, multiple values fail the brief's Category-3 thresholds by wide margins: Tue 28 Jul **Open** $4,047.65 vs `prev_open_full` $4,081.18 (Δ$33.53, threshold for failure >$16.43) and vs `prev_open_cash` $4,029.11 (Δ$18.54, also over the cash failure threshold $13.62) — fails under either basis. **Daily pivots are computed from Mon 27 Jul's H/L/C** ("Daily pivots (from 27 Jul H/L/C)") instead of the correct D-1 session, Tue 28 Jul — an off-by-one-day error; had the report used its own stated Tue 28 Jul H/L/C, P would be ≈$4,044.67, close to the ground-truth `d_full_P` $4,040.67 (Δ≈4), instead of the $4,071.12 actually printed (Δ$30.45 vs ground truth, >2.5x the failure threshold). **Weekly pivots** similarly fail: P $4,036.27 vs `w_full_P` $4,067.44 (Δ$31.17), R1 $4,106.13 vs $4,152.10 (Δ$45.97), S1 $3,982.03 vs $3,968.81 (Δ$13.22) — all exceed the $9.45 failure threshold; S1 is the literal Trade 2 trigger level. **Monthly pivots** fail worse: P $4,111 vs `m_full_P` $4,165.51 (Δ$54.51), R1 $4,279 vs $4,387.95 (Δ$108.95), S1 $3,841 vs `m_full_S1` $3,785.16 (Δ$55.84). The **5-day swing high** used to build the Trade 1 stop ($4,092.6, taken from the report's own Mon 27 Jul high) is Δ$73.47 from `swing_high_5d_full` ($4,166.07). By contrast, the **25-day range** used for Trade 3C ($4,202.67 high / $3,944.23 low) matches ground truth almost exactly (`swing_high_25d_full` 4,202.71, Δ0.04; `swing_low_25d_full` 3,943.08, Δ1.15) — so the error is concentrated in the 5-day/daily-pivot dating, not everywhere. | §6, §11, §21b, level file |
| 4.1 Pillars conclude | 4 | §8 ("Range — reversal risk"), §9 ("TRANSITIONAL — bias bearish"), §10 ("CONFIRM (bearish)"), §12 (each bullet price-negative/watch-item labelled) all end in a direction call. §14 has no single trailing label, only per-bullet framing. | §8–§14 |
| 4.2 Peer/cross-asset interpreted | 5 | §10 gives a mechanism per counter (USD cost-of-carry, risk-on vs. safe-haven bid, ratio widening) rather than a bare correlation list. | §10 |
| 4.3 Synthesis reconciles tensions | 3 | §9 explicitly reconciles the overlap-says-range vs. KER-says-trending-down conflict via the dual-gate rule, and §15–§18 tie §17/§21a together consistently. Docked for a real card-construction defect (scored here per the brief's note that card construction is scored under C4): **Trade 3C's stop is built as boundary + 0.60×width** ($3,944.23 + 0.60×258.44 = $4,099.29, matching the card's stated $4,099) where the M5 rule fixes the 3C stop at **boundary + 0.40×width** (= $3,944.23 + 0.40×258.44 = $4,047.61). TP1/TP2 for the same card are correctly computed (1.0×/1.5× width from the boundary). | §9, §15–18, §21b |
| 4.4 Calibrated language | 4 | §17 is one sentence with conditional framing ("would likely… risks…"); §3 states an explicit Low confidence. Long single sentence borders on hedge-stacking but stays inside "one sentence." | §3, §17 |
| 5.1 Data dated; staleness flagged | 4 | Exceptionally strong: banner notice + §19 + §20 each state the single-source-indicative status explicitly and consistently. Docked one level because several §14 figures (Fed funds range, US 10Y range) carry no explicit date. | §4, §6, §13, §19 |
| 5.2 Assumptions up front | 5 | Futures-to-spot normalisation addressed explicitly (states none was needed and why); the daily-open anchor override is stated in the banner, in §20, **and** the converted 00:00 UK time appears on the Trade 1 card itself — satisfies the module's "recorded as such … same converted time on the card … and in the report body" requirement; single-source-indicative flag is carried into every card's caveats. | §21b, §19, §20 |
| 5.3 Red flags surfaced | 5 | §12/§15 carry the FOMC/dollar/silver risks; §13d's FOMC collision is explicitly carried into both Trade 1 and Trade 2 caveats. | §12, §15, §21b |
| 5.4 Restrictions honoured | 5 | No bracketed variable names or module codes in the body; IFCM excluded explicitly as a retail dealer feed per the stated restriction; GC=F used corroboration-only, never adopted as a row value; instrument common names used throughout. The corroboration-halt relaxation is treated the same way as the anchor override — logged in the banner, §19 and §20 as an explicit, analyst-instructed non-conformance rather than a silent breach, so it does not read as an open restriction violation. | whole report |

## 2. Category roll-up

| Cat | Mean of rows | Level | Multiplier | Max | Points | Justification |
|---|---|---|---|---|---|---|
| C1 Prompt adherence | (4+5+5)/3 = 4.67 | 5 | 1.00 | 20 | 20 | All variables respected; only a source-independence nuance, non-material. |
| C2 Structure | (5+3+5)/3 = 4.33 | 4 | 0.85 | 20 | 17 | All sections present/ordered; pivot-table depth/order deviates from the R3→P→S3 spec. |
| C3 Accuracy & evidence | (3+4+2+0)/4 = 2.25 | 2 | 0.40 | 25 | 10 | Sourced narrative claims and no fabricated citations, but Open, all three pivot tiers, and the 5-day swing high fail the level-file reconciliation by multiples of the failure threshold, and the daily pivot uses the wrong prior session. |
| C4 Reasoning & judgment | (4+5+3+4)/4 = 4.0 | 4 | 0.85 | 20 | 17 | Strong tension-reconciling synthesis and cross-asset mechanism; one concrete card-construction rule violation (Trade 3C stop multiplier). |
| C5 Currency & transparency | (4+5+5+5)/4 = 4.75 | 5 | 1.00 | 15 | 15 | Exemplary, explicit disclosure of the corroboration failure and the anchor override; minor undated macro figures. |

## 3. Total, band, override

```
c1=5
c2=4
c3=2
c4=4
c5=5
total=79
band=High Trust
override=none
```
No fabricated source was found in the 3.2 spot-check (no hallucinated-source override). The two
run-time deviations present (daily-open anchor; corroboration-halt relaxation) are both explicitly
logged in the banner notice, §19 and §20 rather than silently applied, consistent with the module's own
"logged non-conformance, not an anchor" language for the anchor case — so the restriction-breach
override is not triggered either. This is a judgment call the reviewer flags explicitly for anyone
auditing the score: the corroboration relaxation is unusual enough that a stricter reading could treat
it as a restriction breach; it is not applied here because it was disclosed, not hidden.

## 4. Card Integrity (from `qa/gold_regen_qa1/lint_static/2026-07-29.csv`, copied verbatim)

| card_id | strategy | flags | dud | card score |
|---|---|---|---|---|
| 2026-07-29_Trade_1 | Trade 1 - Daily Directional (SHORT) | CLEAN | False | 100 |
| 2026-07-29_Trade_2 | Trade 2 - Pivot, regime-aware (TRANSITION → breakout side only) | CLEAN | False | 100 |
| 2026-07-29_Trade_3C | Trade 3C - Momentum-Breakout (TRANSITION) | WARN_TARGET_FAR(2.92xATR) | False | 90 |

```
card_integrity=96.7
n_cards=3
n_duds=0
n_warns=1
```

## 5. Feedback

See `qa/gold_regen_qa1/2026-07-29_feedback.md`.
