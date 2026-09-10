# Trust Score — Gold (Spot) Daily Report, 22 May 2026
Run: `gold_regen_qa1` · Report: `reports/md/Gold_Spot_Daily_Report_22-May-2026.md` · Asset: XAUUSD · D = 2026-05-22

Basis claimed by the report: "Spot, immediate settlement (loco London)" — continuous/full-day basis.
All Category 3 checks below therefore use the `_full` columns of
`data/levels/XAUUSD_by_date/2026-05-22.csv` (`last_bar_date` = 2026-05-21 < D, confirmed leak-free).
`atr14_full` = 103.9786.

## 1. Section 7 checklist

| Row | Notes | Evidence | Score |
|---|---|---|---|
| 1.1 Variables respected | Asset/basis/futures-corroboration-only/USDX-first/≥6 sources/USD-oz all correctly declared and used. Tick size (0.01) and "ticks" used consistently in §21 cards, but tick name/size is never stated in the §2 Market Definition table itself — a minor omission. **`[AS_OF_DATE]` is mislabeled**: §2 states "As-of date | 22 May 2026", but `M1_Variables_v2_1.md` defines AS_OF_DATE as "the last completed regular session…that closed strictly before the report date" — i.e. it should read 21 May 2026. The report's actual data use (5-day window ending 21 May) is correct; only the labelled field is wrong. | §2, §4, §10 | 3 |
| 1.2 Coverage & currency consistent | Lookback dates (15–21 May) are all D−1 or earlier; the one D-dated reference (Trade 1 entry, 22 May) is the session itself, which is permitted. USD/oz used throughout with no unit drift; ticks always given alongside USD. | whole report | 4 |
| 1.3 Audience & tone | Consistently institutional trading-and-risk register; no retail language; "forward-test…not investment advice" framing matches Purpose & Audience. | §1, §18 | 5 |
| 2.1 Sections present & ordered | All 21 sections present, correctly ordered, with §13a–d and §21a–d subsections present. §7 charts are caption-only placeholders (accepted per brief — docx→md image loss). | headings | 5 |
| 2.2 Scorecard as a table | §6 is a genuine 9-column table (Date/O/H/L/C/RSI2/Trend/Sources A×B/Validation). §11 weekly and monthly pivot tables are correctly R3→P→S3 (3 levels each side); the **daily pivot table uses 5 levels each side (R5…S5)**, inconsistent with the other two tables in the same section and with the checklist's expected format. | §6, §11 | 4 |
| 2.3 Method steps visible | §4–§5 show observation → consensus, §8 is candle-by-candle, §9 shows regime/persistence/overlap/VOLator/KER. §2 declares GC futures as a corroboration source, but **no futures observation ever appears in §4** and no futures-to-spot normalization is shown anywhere — the declared corroboration channel is never actually exercised. | §2, §4–§9 | 4 |
| 3.1 Every quantitative claim sourced | §1/§12/§14 claims are structurally sourced to §4/§6/§13, but a large share of the sourced figures are themselves materially wrong against the leak-free level file (see 3.4) — sourcing format is present, factual grounding is not. | text | 2 |
| 3.2 Citations exist & contain data | Spot-checked TradingEconomics (21 May, 4,517.15, "−0.47% on day"), USAGOLD (20 May, 4,490.73, "recovery print"), FXStreet (21 May, ~4,500, quote consistent with its own headline). All three are named, dated, and used consistently elsewhere in the report; none is self-contradictory or impossible. No fabrication detected — override NOT triggered on this row. | §4, §13a | 4 |
| 3.3 Calculations transparent | RSI2 method stated (period fixed at 2, "computed from the validated close sequence") and reproduces correctly from the report's own 5 closes (recomputed 75.28 ≈ stated 75.3). §13b sentiment tilt arithmetic shown in full. Pivot formula and ATR derivation are not shown inline in the report body (values only). | §6, §9, §13b | 3 |
| 3.4 Numbers reconcile — incl. against the level file | Internally consistent (D−1 close/RSI2/pivots agree across §1/§3/§4/§6/§11/§21b). **Externally, reconciliation against `XAUUSD_by_date/2026-05-22.csv` fails on nearly every checkable field** — see table below. This is the dominant defect in the report. | cross-section + level file | 0 |
| 4.1 Pillars conclude | §8/§9/§10/§12/§14 each close with an explicit direction label. Card construction (also scored here, see brief §3): Trade 2's TP3 ($4,410) sits nearer to entry than TP2 ($4,384) on a short — an internally contradictory runner target, transcribed but not corrected (linter WARN_TP3_ORDER). Trade 3C's stop ($4,684.0) is derived from the wrong range boundary (see Card Integrity feedback) — a genuine M5-formula deviation. | §8–§14, §21b | 3 |
| 4.2 Peer/cross-asset interpreted | §10 gives an explicit mechanism paragraph per counter (USDX real-cost/financial-conditions channel, equity safe-haven channel), not a bare correlation list. | §10 | 5 |
| 4.3 Synthesis reconciles tensions | §9 explicitly reconciles KER (−0.50, trending) vs. persistence/overlap (transitional); §15/§16/§18 carry the equity-counter contradiction forward; §21a's conflict note addresses §17-vs-§21a conditionality explicitly rather than silently aligning them. | §9, §15–§18, §21a | 5 |
| 4.4 Calibrated language | §17 is exactly one sentence, single conditional structure, no hedge-stacking. Confidence stated H/M/L-style ("Low–Medium") in §3. | §3, §17 | 5 |
| 5.1 Data dated; staleness flagged | Every price/article in §4/§6/§13 is dated. Every OHLC and pivot value is explicitly flagged "single-source-indicative" for strict-tolerance purposes (§11, §19, all three cards) — better than the checklist minimum. | §4, §6, §13, §19 | 5 |
| 5.2 Assumptions up front | Daily-open-anchor override is stated up front (§2 run note), logged as a non-conformance in §20 Agent Log, and carried onto every card with the same converted broker time (02:00 = 00:00 UK + 2h) — compliant handling per the brief's anchor rule. Futures-to-spot normalization is declared as policy in §2 but never evidenced (no futures data used). Single-source pivot propagation is explicitly carried into all three cards' caveats. | §21b, §19, §20 | 4 |
| 5.3 Red flags surfaced | §12/§15 carry a full risk set; §13d's 22 May inflation release is explicitly carried into Trade 1's caveats as a holding-period collision. | §12, §15, §21b | 5 |
| 5.4 Restrictions honoured | No bracketed variable names or module codes leak into the body; instrument common names used throughout. **But**: §3/§6/§19/§20 disclose that strict two-source ±0.50 corroboration on intraday H/L was *not* achieved, that fewer than 10 of the 50 approved sources were tried, and that the mandatory `DataCorroborationError` halt was bypassed "per the explicit run instruction, "no DataCorroborationError raised by analyst direction." `Source_Discipline_NoSynthesis_Protocol.md` states this halt rule is "ABSOLUTE… no exceptions… supersedes all prior wording in any patch, module, or protocol document" and contains no provision for an instruction-based override. Disclosing the bypass is better than hiding it, but the bypass itself is a breach of a fixed, non-editable restriction. | §3, §6, §19, §20 | 1 |

## 2. Category roll-up

| Cat | Rows (mean) | Level | Multiplier | Max | Points | Justification |
|---|---|---|---|---|---|---|
| C1 Prompt adherence | (3+4+5)/3 = 4.0 → **4**, then **override: −1 level** (restriction breach) | **3** | 0.65 | 20 | 13.0 | AS_OF_DATE mislabelled; forced down one level by the restriction-breach override (row 5.4). |
| C2 Structure | (5+4+4)/3 = 4.33 → **4** | 4 | 0.85 | 20 | 17.0 | All sections present/ordered; daily pivot table format inconsistent with weekly/monthly; declared futures corroboration never exercised. |
| C3 Accuracy & evidence | (2+4+3+0)/4 = 2.25 → **2** | 2 | 0.40 | 25 | 10.0 | Sourcing format adequate and no fabricated citation, but external reconciliation against the level file fails on close, high, ATR14, RSI2, daily P/R1, weekly P, and all three monthly pivot levels. |
| C4 Reasoning & judgment | (3+5+5+5)/4 = 4.5 → **4** (rounded down; card-construction defects weigh against a 5) | 4 | 0.85 | 20 | 17.0 | Strong pillar conclusions, mechanism-level cross-asset read, and tension reconciliation, offset by Trade 2's internally contradictory TP3 and Trade 3C's wrong-boundary stop. |
| C5 Currency & transparency | (5+4+5+1)/4 = 3.75 → **4** | 4 | 0.85 | 15 | 12.75 | Excellent staleness-flagging and anchor-override handling; dragged down by the source-discipline halt bypass (row 5.4), which does not by itself force this row's category below 4 on the row-mean but is the trigger for the report-level override below. |

## 3. Total, band, override

```
c1=3
c2=4
c3=2
c4=4
c5=4
total=70
band=Moderate Trust (60-74)
override=restriction_breach
card_integrity=93.3
n_cards=3
n_duds=0
n_warns=2
```

Raw total = 13.0 + 17.0 + 10.0 + 17.0 + 12.75 = 69.75 → **70**.

**Override check**: A prompt/module restriction was breached — the Source Discipline "ABSOLUTE NO-SYNTHESIS RULE" mandatory halt (`DataCorroborationError`) was bypassed without exhausting the approved source list and without any verifiable authorization, per the report's own §20 Agent Log entry ("no DataCorroborationError raised by analyst direction"). Per framework §6, this caps the band at Moderate Trust (60–74) and requires C1 down at least one level — both already applied above. The raw total (70) already sits inside the Moderate band, so the override is binding on C1 but does not change the band from what the raw score would already produce. No fabricated/impossible source was found on the 3-source spot check, so the hallucinated-source override (C3 = 0, cap at Low) is **not** triggered independently — C3's row-mean score of 2 stands on its own reconciliation failures, not on a fabrication finding.

## 4. Category 3 — external reconciliation detail (vs. `XAUUSD_by_date/2026-05-22.csv`, `_full` basis)

| Check | Report value | Level file value | Diff | Diff ×ATR14 | Verdict (brief §4 tolerance) |
|---|---|---|---|---|---|
| D−1 Close | 4,517.2 | 4,543.25 | 26.05 | 0.251 | **FAIL** (>0.115) |
| D−1 Open | 4,530.5 | 4,546.66 | 16.16 | 0.155 | discrepancy (0.09–0.20) |
| D−1 High | 4,540.0 | 4,570.76 | 30.76 | 0.296 | **FAIL** (>0.20) |
| D−1 Low | 4,490.0 | 4,488.75 | 1.25 | 0.012 | consistent |
| RSI2 (D−1) | 75.3 | 99.1644 | 23.86 pts | — | **FAIL** (>15; note: RSI2 *does* reproduce correctly from the report's own stated closes — this is a data-accuracy failure, not an arithmetic one) |
| ATR14 | ≈72 (implied, Trade 1 caveat) | 103.9786 | — | 30.8% relative | **FAIL** (>25%) |
| Daily pivot P | 4,515.7 | 4,534.2533 | 18.55 | 0.178 | **FAIL** (>0.115) |
| Daily R1 | 4,541.5 | 4,579.7567 | 38.26 | 0.368 | **FAIL** |
| Daily S1 | 4,491.5 | 4,497.7467 | 6.25 | 0.060 | discrepancy |
| Weekly pivot P | 4,640.0 | 4,607.8533 | 32.15 | 0.309 | **FAIL** (period label "week ending 15 May" is correct — matches file's `2026-W20`, Mon 11–Fri 15 May — the value itself is what fails) |
| Monthly pivot P | 4,611.3 | 4,673.69 | 62.39 | 0.600 | **FAIL** (period "April 2026" correctly matches file's `m_full_period`) |
| Monthly R1 | 4,922.7 | 4,837.19 | 85.51 | 0.822 | **FAIL** |
| Monthly S1 | 4,382.7 | 4,458.18 | 75.48 | 0.726 | **FAIL** |
| 5d swing low (used as Trade 1 TP1 confluence) | 4,474 | 4,453.63 | 20.37 | 0.196 | discrepancy, near-FAIL boundary |
| 25d swing high (Trade 3C range top) | 4,840 | 4,889.2 | 49.2 | 0.473 | **FAIL** |
| 25d swing low (Trade 3C range bottom) | 4,450 | 4,453.63 | 3.63 | 0.035 | consistent |

Every externally-checkable OHLC, ATR, RSI2 and pivot value in the report — with the sole exceptions of D−1 Low, daily S1, and the 25-day swing low — fails or sits at the edge of the brief's Category 3 tolerance bands. The report's underlying D−1 session read is not reconcilable with the leak-free broker feed, and every pivot table in §11 (all built from that same D−1 read) inherits the error.

## 5. Card Integrity (from `qa/gold_regen_qa1/lint_static/2026-05-22.csv`, copied verbatim)

| card_id | strategy | flags | dud | Card Integrity (100 − 40·DUD − 10·WARN) |
|---|---|---|---|---|
| 2026-05-22_Trade_1 | Trade 1 — Daily Directional | CLEAN | False | 100 |
| 2026-05-22_Trade_2 | Trade 2 — Pivot (TRANSITION, breakout side only) | WARN_TP3_ORDER | False | 90 |
| 2026-05-22_Trade_3C | Trade 3 — Momentum-Breakout (variant 3C) | WARN_TARGET_FAR(3.58xATR) | False | 90 |

Report-level Card Integrity = mean(100, 90, 90) = **93.3** (separate from the 100-point Trust Score).
n_cards = 3, n_duds = 0, n_warns = 2.
