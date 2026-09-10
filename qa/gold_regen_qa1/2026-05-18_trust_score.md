# Trust Score — Gold_Daily_Report_18-May-2026.md (run `gold_regen_qa1`)

Reviewer basis: `docs/AI_Output_Trust_Score_Framework_v3.7.txt` §4–7, `docs/QA_PROTOCOL_TRADE_CARDS.md`,
`qa/gold_regen_qa1/REVIEWER_BRIEF.md`. Level file: `data/levels/XAUUSD_by_date/2026-05-18.csv`
(`last_bar_date`=2026-05-15 < D=2026-05-18 — leak-free, confirmed). Report claims a continuous
23-hour OTC spot basis ("Delivery basis: OTC London spot"), so all Category-3 checks below use the
`_full` columns unless stated otherwise. `atr14_full` = 107.195.

## 1. Section 7 checklist

| Row | Notes | Evidence | Score |
|---|---|---|---|
| 1.1 Variables respected | Asset correctly XAU/USD spot, not COMEX front-month (GC=F used for corroboration only) — correct. USDX is the first counter in §10 — correct. **As-of date mislabelled**: §2 states "As-of date: 18 May 2026", but M1_Variables defines AS_OF_DATE as the last completed session strictly before D, i.e. 15-May — the report uses the report date, not the as-of session, in that field, even though every actual calculation is anchored to 15-May. **Tick size/name never declared**: §2 has no TICK_SIZE/TICK_NAME row, though ticks are used pervasively in §21 (implied $0.01/tick, applied consistently) and the module requires this be stated when strategy cards are produced. **Two bracketed variable placeholders leak into body text** — `[PRIMARY_ASSET]` (§5) and `[BE_TRAIL_R]` (§21b Trade 3C) — a direct restriction breach (see override below). | §2, §5, §21b | 2 |
| 1.2 Coverage & currency consistent | Data dates are D−1 (15-May) or earlier throughout; session date is D (18-May) throughout. No USD/oz vs tick unit drift — tick conversions are internally consistent (100 ticks = $1 in all three cards). | §1–§21 | 4 |
| 1.3 Audience & tone | Institutional Senior-Commodities-Analyst register maintained throughout; no retail tone. | §1, §18 | 5 |

Mean = 3.67 → **4**, reduced to **3** by the restriction-breach override (Category 1 down ≥1 level).

| Row | Notes | Evidence | Score |
|---|---|---|---|
| 2.1 Sections present & ordered | All of §1–§21 (incl. §13a–d, §21a–d) present, correctly ordered, correctly headed. | headings | 5 |
| 2.2 Scorecard as a table | §6 table has Date/O/H/L/C/Δ%/RSI2/Validation — the required **Source A / Source B columns are missing** (Source A/B are stated in prose above the table instead of as columns). §11 weekly and monthly pivot tables are correctly 3-levels-each-side, R3→P→S3; the **daily table shows 5 levels each side** (R5–R1…S1–S5) rather than the specified 3. | §6, §11 | 3 |
| 2.3 Method steps visible | §4–§5 show observation → normalisation → consensus with the futures/CFD basis discussed; §8 is full candle-by-candle; §9 gives regime + KER + VOLator; §7 charts are text placeholders (acceptable per brief — conversion drops images). | §4–§9 | 5 |

Mean = 4.33 → **4**.

| Row | Notes | Evidence | Score |
|---|---|---|---|
| 3.1 Quantitative claims sourced | Most §1/§12/§14 figures carry an attribution (WGC, CME FedWatch, Barchart, §4/§6/§13); a few macro figures (e.g. ten-year yield 4.60%) are asserted without a clean pointer. | text | 3 |
| 3.2 Citations exist & contain data | Spot-checked CNBC, Yahoo Finance, USAGOLD (§4): each is named, dated 15-May, and its figure is used consistently in the §5 build. No fabrication found in the three checked. | §4 | 3 |
| 3.3 Calculations transparent | **RSI2 does not reproduce**: report states 5.9 for 15-May; recomputed from the report's own stated closes (4,649→4,562, an unbroken loss run) the correct value is exactly 0 (avg gain 0, avg loss 62.5, RS=0) — which is also `rsi2_full` in the level file. **Daily pivots do not reproduce from the report's own stated H/L/C** (4,684/4,483/4,562) via the stated formula: only P and S2 match; R1 (recomputed 4,669.67 vs stated 4,636), S1 (4,468.67 vs 4,442), R2 (4,777.33 vs 4,710) and R3 (4,870.67 vs 4,797) do not. **§5's own weighted-median arithmetic is wrong**: the four close-equivalent prints (4,538/4,562/4,564/4,540) median to 4,551 as the report itself states, then the text "rounds" this to a consensus of 4,562 — an unexplained 11-dollar jump that is not a rounding operation. **ATR(14) is materially wrong**: report assumes ATR(14) ≈ 57–58 USD (§8, §21b) vs. the leak-free `atr14_full` = 107.195 (−46.4% relative) and `atr14_cash` = 86.27 (−33.3% relative even on the more forgiving basis) — both exceed the >25%-relative failure threshold, and this wrong ATR is the basis for every card's stop-cap and 0.25×ATR buffer. | §5, §6, §8, §11, §21 | 0 |
| 3.4 Numbers reconcile — incl. vs. level file | Internally the D−1 close (4,562) is consistent across §1/§3/§4/§6/§21b. Externally, against the level file (full basis): close diff 23.55 (0.22×ATR, **fail**, threshold 0.115×ATR); low diff 28.74 (0.27×ATR, **fail**, threshold 0.20×ATR); open diff 0.18 (consistent); high diff 18.6 (0.17×ATR, discrepancy band, not failure). Daily pivots: S1 diff 0.34×ATR (**fail**), R2 diff 0.14×ATR (**fail**), S2 diff 0.40×ATR (**fail**), S3 diff 0.16×ATR (**fail**); only P/R1 consistent, R3 a discrepancy. Weekly pivots: only P is consistent (0.008×ATR); S1/R2/S2/R3/S3 all **fail** (0.31–0.73×ATR), R1 a discrepancy. Monthly pivots (stated basis "April H/L/C ≈ 4,810/4,260/4,650"): only R3 consistent; P/S1/R2/S2/S3 all **fail** (0.49–1.37×ATR) against the level file's actual April pivots — the stated April H/L/C itself is far off the true month range. The report's own §19 explicitly claims only "~1-2 dollars" basis risk on the 4,483 CFD low it uses, against an actual 28.74 gap to the true full-basis low. | cross-section + level file | 0 |

Mean = 1.5 → **2** (rounds to 2, half rounds up per convention with the sum 3+3+0+0=6/4=1.5→2).

| Row | Notes | Evidence | Score |
|---|---|---|---|
| 4.1 Pillars conclude | §8, §9, §10 each end with a clear direction label. §12 and §14 imply a bearish tilt through content but neither closes with an explicit direction-label sentence the way §8–10 do. | those sections | 4 |
| 4.2 Peer/cross-asset interpreted | §10 gives real mechanisms (real-yield channel, dollar-gold inverse, gold-silver ratio widening) for every counter, not a bare correlation list. | §10 | 5 |
| 4.3 Synthesis reconciles tensions — incl. card construction | §15–§18/§21a are internally coherent (no conflict flag, forecast matches direction score). But: (a) each of the three cards contains an internal confluence-number mismatch in its own text (Trade 1's Confluences cell cites "daily S1 (4,442)" while its own TP1 cell states 4,476 — 34 USD apart; Trade 2's Confluences cell cites monthly S1 4,398 / weekly S2 4,390 while its own TP1 cell states 4,376 — 14–22 USD apart); (b) §20's Agent Log states "Trade 2 RANGE-pivot built; Trade 3B RANGE mean-reversion built," directly contradicting §21b, which builds a TRANSITION breakout Trade 2 and a Trade 3C card — a genuine handoff-record vs. output contradiction; (c) Trade 3C's stop rationale computes a midpoint (4,636) and an inside-range stop (4,606) and then substitutes an unexplained 4,565 without reconciling the two computed numbers. | §21b, §20 | 2 |
| 4.4 Calibrated language | §17 is one sentence; confidence (Medium) stated in §3. | §3, §17 | 4 |

Mean = 3.75 → **4**.

| Row | Notes | Evidence | Score |
|---|---|---|---|
| 5.1 Data dated; staleness flagged | Every price/article carries a date. But the report labels every pivot tier "CORROBORATED" and claims strong dual-source agreement, while the external check above shows most pivots and the close/low diverge well past the discrepancy band from the leak-free feed — the confidence implied by "CORROBORATED" is not supported to the degree claimed. | §4, §6, §13, §19 | 3 |
| 5.2 Assumptions up front | Futures-to-spot normalisation is stated with its size (~24 dollars, §5). Anchor override is stated on the header, in §20, and on every card. The ATR(14) assumption (~57-58) is stated but not sourced/derived, and is materially wrong (see 3.3) without being flagged as an estimate needing validation. | §21b, §19, §20 | 3 |
| 5.3 Red flags surfaced | §12/§15 risks are well covered (FOMC binary, Bloomberg-not-fetched flag, gold-equity co-decline anomaly). §13d event risk is carried into card caveats (weekend gap, FOMC-conditional cancellation on Trade 3C). | §12, §15, §21b | 4 |
| 5.4 Restrictions honoured | **Two bracketed variable names appear verbatim in the report body**: `[PRIMARY_ASSET]` (§5, "per [PRIMARY_ASSET] definition") and `[BE_TRAIL_R]` (§21b Trade 3C, "tighter than [BE_TRAIL_R] dictates"). **Internal module section codes are also exposed**: Trade 2's direction line reads "mirrors §5.2c configuration" and Trade 3C's tranche-management cell reads "explicit per §5.3c TP2 rule" — these are M5's own internal subsection numbers, not report-facing content. Futures corroboration-only is otherwise respected; no obvious un-normalised retail premium found. | whole report | 1 |

Mean = 2.75 → **3**.

## 2. Category roll-up

| Cat | Level | Multiplier | Max | Points | Justification |
|---|---|---|---|---|---|
| C1 Prompt adherence | 3 | 0.65 | 20 | 13.00 | As-of-date field mislabelled, tick size/name never declared, and reduced ≥1 level by the restriction-breach override (bracketed variables in body). |
| C2 Structure | 4 | 0.85 | 20 | 17.00 | All 21 sections present/ordered; §6 scorecard missing its Source A/B columns and the daily pivot table shows 5 levels/side instead of 3. |
| C3 Accuracy & evidence | 2 | 0.40 | 25 | 10.00 | RSI2, the §5 weighted-median arithmetic, the daily-pivot formula, and ATR(14) all fail to reproduce from the report's own stated inputs; close/low and most daily/weekly/monthly pivots fail the level-file tolerance. |
| C4 Reasoning & judgment | 4 | 0.85 | 20 | 17.00 | Strong cross-asset mechanism and calibrated forecast, but card-level confluence numbers are internally inconsistent and §20 contradicts §21b on which strategies were built. |
| C5 Currency & transparency | 3 | 0.65 | 15 | 9.75 | Anchor override and futures-normalisation properly disclosed, but "CORROBORATED" is overstated given the external divergence, and two restriction breaches (bracket leaks, module-code leaks) sit here too. |

**total = 67**
**band = Moderate Trust (60–74)**
**override = restriction_breach** — `[PRIMARY_ASSET]` and `[BE_TRAIL_R]` appear as literal bracketed variable names in the report body (§5, §21b Trade 3C), and internal module subsection codes (§5.2c, §5.3c) are exposed in §21b — a breach of the "no bracketed variable names / no module codes" restriction (checklist 5.4). Per framework §6 this caps the band at Moderate (60–74) and requires Category 1 reduced by at least one rubric level; both are already reflected above (raw C1 mean 3.67→4, dropped to 3; raw total 67 already sits inside the Moderate cap, so the override does not further change the banding). No hallucinated-source override: the three spot-checked citations (CNBC, Yahoo Finance, USAGOLD) are named, dated, and used consistently — not fabricated, even though the resulting numbers diverge from the leak-free feed.

## 3. Card Integrity (separate from the 100 — copied verbatim from `lint_static/2026-05-18.csv`)

| card_id | strategy | flags | dud | card score |
|---|---|---|---|---|
| 2026-05-18_Trade_1 | Trade 1 — Daily Directional (score-driven) | CLEAN | False | 100 |
| 2026-05-18_Trade_2 | Trade 2 — Pivot (regime-aware) — TRANSITION, breakout-side only | CLEAN | False | 100 |
| 2026-05-18_Trade_3C | Trade 3C — Momentum-Breakout (TRANSITION) | WARN_TARGET_FAR(2.86xATR) | False | 90 |

`card_integrity = 96.67`  ·  `n_cards = 3`  ·  `n_duds = 0`  ·  `n_warns = 1`

## 4. Feedback

See `qa/gold_regen_qa1/2026-05-18_feedback.md`.
