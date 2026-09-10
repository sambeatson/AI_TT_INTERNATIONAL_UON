# Trust Score — Gold_Daily_Report_21-May-2026.md (run `gold_regen_qa1`)

Reviewer basis: `docs/AI_Output_Trust_Score_Framework_v3.7.txt` §4–7, `docs/QA_PROTOCOL_TRADE_CARDS.md`,
`qa/gold_regen_qa1/REVIEWER_BRIEF.md`. Level file: `data/levels/XAUUSD_by_date/2026-05-21.csv`
(`last_bar_date`=2026-05-20 < D=2026-05-21 — leak-free, confirmed). Report claims a continuous
loco-London spot basis ("Price basis: Spot, immediate settlement (loco London)"; "Market scope:
Global — 24-hour OTC market"), so all Category-3 checks below use the `_full` columns unless stated
otherwise. `atr14_full` = 105.2621, `rsi2_full` = 42.3251.

## 1. Section 7 checklist

| Row | Notes | Evidence | Score |
|---|---|---|---|
| 1.1 Variables respected | Asset correctly XAU/USD spot, not COMEX front-month (GC=F named for cross-validation only, and never actually cited as a price input in §4). USDX is the first counter in §10 — correct. Lookback (5 short / 25 medium), USD/oz unit, ≥6 sources (exactly 6 Core+Directional in §4), and a single consistent tick size (USD 0.01/tick, applied identically across all three cards: 105.94→10,594 ticks; 27.24→2,724 ticks; 126.63→12,663 ticks) are all respected. **The daily-open anchor note is genuinely ambiguous**: §2 states "Daily-open anchor: 00:00 UK — overridden to 21 May 2026 per instruction," and the body repeats "the run instruction overrides the daily-open anchor to value the report for the 21 May 2026 session." Grammatically this reads as if the *anchor itself* (a time-of-day, per M1_Variables) were overridden *to a date* — a category error. The anchor **time** (00:00 UK) is in fact used consistently throughout (Trade 1 entry text, all three cards' `anchor_broker`=02:00 = 00:00 UK+2h broker offset), so there is no evidence of an actual anchor-time departure — but the module's requirement to log any departure unambiguously as a non-conformance is not clearly met by this wording, which instead reads as presenting a date-selection as if it were the anchor. | §2, §20, §21b | 3 |
| 1.2 Coverage & currency consistent | Every data date in §2/§4/§6/§13 is 20-May-2026 or earlier; the session itself is dated 21-May throughout. §13d's upcoming calendar correctly spans 21–28 May. No USD/oz vs. tick unit drift. | §1–§21 | 5 |
| 1.3 Audience & tone | Institutional Senior-Commodities-Analyst register maintained throughout ("forward-test," "conviction score," "tick-priority") with no retail tone. | §1, §18 | 5 |

Mean = 4.33 → **4**.

| Row | Notes | Evidence | Score |
|---|---|---|---|
| 2.1 Sections present & ordered | All of §1–§21 present in order, including §13a–d and §21a–d. | headings | 5 |
| 2.2 Scorecard as a table | §6 is a proper table with Date/O/H/L/C/RSI2/Trend/Source A/Source B/Validation. §11's three pivot tables are each ordered R3→R2→R1→P (left column) / S1→S2→S3 (right column), matching the required 3-levels-each-side layout. | §6, §11 | 5 |
| 2.3 Method steps visible | §4–§5 show observation→normalisation→consensus (correctly noting no futures-to-spot adjustment was needed since no futures price was actually used as an input); §8 is full candle-by-candle; §9 gives regime, overlap ratio, persistence, KER and VOLator together with an explicit tension-resolution (overlap 0.66 "would suggest a range" vs. 3rd-percentile close resolving to TREND_DOWN); §7 charts are captions/placeholders only (acceptable per brief — the .docx→.md conversion drops images). | §4–§9 | 5 |

Mean = 5.00 → **5**.

| Row | Notes | Evidence | Score |
|---|---|---|---|
| 3.1 Quantitative claims sourced | Most §1/§12/§14 figures point to §4/§6/§13 (CPI, PPI, WGC 244t, USDX, 10Y yield). A few are asserted without a specific pointer: §12.3's "USDX... around 99.4" has no dated citation of its own (§10 only says "Rising"); §14's retail-positioning claim ("roughly two-thirds of accounts long... one broker read") names no broker and no date. | text | 3 |
| 3.2 Citations exist & contain data | Spot-checked FXStreet (20-May), World Gold Council (Q1 ref), and Business Standard/Reuters (20-May): each is named, dated, and its quote is used consistently elsewhere in the report (no internal self-contradiction). However, confidence in this row is undermined by 3.4 below: the report claims tight dual-source "CORROBORATED" deltas (Δ0.04–Δ0.47) for the very 20-May OHLC values that diverge from the leak-free level file by up to 0.69×ATR — two independently-named sources agreeing closely with each other on a figure that is that far from the verified execution series is not proven fabrication, but it is not the untroubled pass the delta values imply either. | §4, §6, §13a | 2 |
| 3.3 Calculations transparent | RSI2 formula is stated and reproduces exactly from the report's own five stated closes (verified: last two changes are both losses → RS=0 → RSI2=0.0, matching the report's claimed 0.0 for 20-May). Daily pivots reproduce exactly from the report's own stated H/L/C via the stated formulas (P, R1–R3, S1–S3 all recompute to the cent). Direction-score trace in §20 sums correctly (−0.250−0.200+0.000−0.022−0.083−0.150 = −0.705). One gap: KER (−0.15, "Trending Down — Strong") is asserted as an output with no KER(13, EMA3) derivation shown. | §6, §11, §20, §21a | 4 |
| 3.4 Numbers reconcile — internally AND against the level file | **Internally**: the D−1 close (4,489.40) is identical across §1/§3/§4/§6/§21b's MARKET entry — consistent. One small internal miss: §1 states the conviction score as **−0.70** while §21a and the trade card state **−0.71** (both rounding the same §20 raw score of −0.705, inconsistently). **Externally, this is the report's dominant failure.** Against `data/levels/XAUUSD_by_date/2026-05-21.csv` (`_full`): D−1 close diff = 54.37 (0.517×ATR14, **FAIL**, threshold 0.115×ATR); D−1 open diff = 59.12 (0.562×ATR, **FAIL**, threshold 0.20×ATR); D−1 low diff = 22.17 (0.211×ATR, **FAIL**); only D−1 high is consistent (diff 4.67 = 0.044×ATR). RSI2: report states 0.0 vs. `rsi2_full` = 42.3251 — diff 42.3 points, **FAIL** (threshold >15; also fails against `rsi2_cash` = 45.3351). Daily pivots: 6 of 7 levels **FAIL** tolerance (P diff 0.117×ATR, R1 diff 0.444×ATR, S1 diff 0.189×ATR, R2 diff 0.372×ATR, S2 diff 0.138×ATR, R3 diff 0.699×ATR); only S3 is a discrepancy (0.066×ATR), none are fully consistent. Weekly pivots: S1/S2/S3 **FAIL** (0.204/0.251/0.351×ATR); P/R1/R2/R3 sit in the discrepancy band (0.042–0.104×ATR), none consistent. Notably, the monthly pivot tier — the one tier the report itself flags SINGLE-SOURCE INDICATIVE and excludes from strategy pricing — is the *only* one that reconciles cleanly: all seven monthly levels are within 0.017×ATR of the level file, i.e. effectively exact. ATR14 itself is within tolerance on the full basis (report implies ≈96.16 vs. `atr14_full`=105.2621, 8.6% relative, <10% consistent) but fails on the cash basis (17.8%, discrepancy band). | cross-section + level file | 0 |

Mean = 2.25 → rounds toward the lower level per framework §9 reviewer guidance ("pick the lower rubric level when in doubt") → **2**.

| Row | Notes | Evidence | Score |
|---|---|---|---|
| 4.1 Pillars conclude — incl. card construction | §8 ("Bearish continuation"), §9 ("Bias: Bearish"), §10 ("CONFIRM"), each §12 sub-item (Price-Supportive/Price-Negative/Neutral/Two-Sided), all close with an explicit label. Card construction (scored here per the brief): Trade 1 and Trade 3A are clean (linter CLEAN both). **Trade 2 has a real construction defect**: its TP3 field reads "Runner toward the daily pivot region on a continuation leg" — but Trade 2 is a SHORT below the daily pivot (entry 4,500.04 vs. pivot 4,504.40, which sits *above* entry); a downside continuation leg moves *away* from the pivot, not toward it, so the stated runner direction is backwards. Trade 2 also carries the linter's `WARN_R_TINY(0.26×ATR)` — its 27.24-USD stop is below the module's 0.3×ATR14 minimum. | §8–§10, §12, §21b, linter | 4 |
| 4.2 Peer/cross-asset interpreted | §10 gives an explicit transmission mechanism for every counter (USDX opportunity-cost channel, equity risk-appetite channel, gold-silver de-rating), not a bare correlation list. | §10 | 5 |
| 4.3 Synthesis reconciles tensions | §9 explicitly reconciles the elevated overlap ratio (0.66, range-like) against the 3rd-percentile range-bottom close (trend-like), resolving to TREND_DOWN with reasoning shown; §15–§18/§21a are mutually consistent (no conflict flagged, and none found). One gap: the report treats RSI2 "pinned at zero" purely as bearish-momentum confirmation and never addresses the more conventional reading that an RSI2 floor print also raises oversold/bounce risk — a tension a synthesis section would normally at least acknowledge before dismissing. | §9, §15–§18 | 4 |
| 4.4 Calibrated language | §17 is one sentence with an appropriately calibrated conditional ("contingent on the FOMC minutes not delivering a dovish surprise"); confidence (Medium) is stated in §3 with an explicit reason. | §3, §17 | 5 |

Mean = 4.50 → rounds toward the lower level per framework §9 reviewer guidance → **4**.

| Row | Notes | Evidence | Score |
|---|---|---|---|
| 5.1 Data dated; staleness flagged | Every price/article is dated; the two 19-May intraday reads (Trading Economics, Univest) are explicitly reclassified from Core to Directional/stale because they pre-date the 20-May leg lower — correct staleness handling. | §4, §5, §13a | 5 |
| 5.2 Assumptions up front | Futures-to-spot normalisation correctly stated as not required (no futures price was actually used as a §4 input). Monthly-tier single-source propagation is explicitly carried into §19 and the Trade 2 caveat. The daily-open anchor note (see 1.1) is the material gap here too: it is the report's one "override" disclosure, and its wording conflates the anchor time with the as-of date rather than clearly logging what — if anything — departed from the fixed instance value. | §19, §20, §21b | 3 |
| 5.3 Red flags surfaced | §12/§15 cover retail-positioning contrarian risk, the FOMC binary, and the geopolitical two-sided risk; §13d's FOMC-minutes collision is explicitly carried into both Trade 1's and Trade 2's caveats. | §12, §15, §21b | 5 |
| 5.4 Restrictions honoured | No bracketed variable placeholders, no module codes (M1–M5), and no framework name found anywhere in the report body; instrument common names used throughout; futures corroboration-only claim is honoured (GC=F is named but never cited as a price input). | whole report | 5 |

Mean = 4.50 → rounds toward the lower level per framework §9 reviewer guidance → **4**.

## 2. Category roll-up

| Cat | Level | Multiplier | Max | Points | Justification |
|---|---|---|---|---|---|
| C1 Prompt adherence | 4 | 0.85 | 20 | 17.00 | Variables, coverage, tone and tick usage all respected; the daily-open anchor disclosure conflates anchor-time with as-of-date in ambiguous wording. |
| C2 Structure | 5 | 1.00 | 20 | 20.00 | All 21 sections present, correctly ordered; both scorecard and pivot tables meet the specified formats; method steps visible with genuine tension-resolution shown. |
| C3 Accuracy & evidence | 2 | 0.40 | 25 | 10.00 | RSI2 and pivot arithmetic are internally reproducible and correct, but the D−1 OHLC, RSI2 and 9 of 14 checked pivot levels diverge from the leak-free level file well past the failure threshold (up to 0.70×ATR / 42+ RSI2 points) — the report's core reference dataset does not match the verified execution series. |
| C4 Reasoning & judgment | 4 | 0.85 | 20 | 17.00 | Every pillar concludes with a defended, mechanism-based direction label and a real overlap-vs-range-bottom tension is explicitly reconciled; Trade 2's runner direction is internally backwards and its stop fails the 0.3×ATR minimum (linter WARN). |
| C5 Currency & transparency | 4 | 0.85 | 15 | 12.75 | Staleness, red flags and restrictions are all well handled; the anchor-override disclosure is the one recurring transparency gap, and it is central enough (flagged explicitly for review in this run) to hold this row below Excellent. |

**total = 76.75 → 77**
**band = High Trust (75–89)**
**override = none** — no fabricated/hallucinated source was found among the three spot-checked citations (FXStreet, World Gold Council, Business Standard/Reuters — each named, dated, and used consistently), and no bracketed variable, module code or framework name was found in the body, so neither override rule triggers.

**Reviewer note on the band:** this total sits only 2 points inside the High Trust floor, driven almost entirely by Category 3's row 3.4 (scored 0/5) — the report's D−1 OHLC and RSI2 diverge from the leak-free level file by margins several multiples over the framework's own failure thresholds, and this is the single most decision-relevant defect in the report because every downstream pivot, stop and target in §11 and §21b inherits it. The mechanical roll-up keeps the report in High Trust only because C1/C2/C4/C5 are each independently strong and Category 3's other three rows (sourcing, citation spot-check, calculation transparency) are genuinely sound on their own terms. A reviewer relying on the band label alone, without reading the Category 3 detail above, would materially under-estimate this report's central risk — the data-anchoring failure identified in row 3.4 should be treated as the priority for regeneration regardless of the overall band.

## 3. Card Integrity (separate from the 100 — copied verbatim from `qa/gold_regen_qa1/lint_static/2026-05-21.csv`)

| card_id | strategy | flags | dud | card score |
|---|---|---|---|---|
| 2026-05-21_Trade_1 | Trade 1 — Daily Directional | CLEAN | False | 100 |
| 2026-05-21_Trade_2 | Trade 2 — Pivot (regime-aware, TREND_DOWN branch) | WARN_R_TINY(0.26xATR) | False | 90 |
| 2026-05-21_Trade_3A | Trade 3 — Momentum-Pullback (variant 3A; TREND_DOWN) | CLEAN | False | 100 |

`card_integrity = 96.67`  ·  `n_cards = 3`  ·  `n_duds = 0`  ·  `n_warns = 1`

## 4. Feedback

See `qa/gold_regen_qa1/2026-05-21_feedback.md`.
