# Trust Score — Gold_Daily_Report_13May2026.md (D = 2026-05-13, run `gold_regen_qa1`)

Basis claimed by the report: "Spot, loco London, T+2 settlement" (§3) / "OTC London spot, T+2 settlement
(LBMA convention)" (§2) → checked against the level file's `_full` columns (continuous 24h spot), with
`_cash` shown as a secondary reference where it changes the read. `last_bar_date` in the level file =
2026-05-12 < D = 2026-05-13, confirmed leak-free before use.

## 1. Section 7 checklist

| Row | Notes | Evidence | Score (0–5) |
|---|---|---|---|
| 1.1 Variables respected | Asset framed as XAU/USD spot loco London throughout, not COMEX GC front-month; GC=F used only as flagged "Directional" corroboration (§4, §5) with contango stated. USDX is the first/primary counter (§2, §10). As-of = 12 May (D−1), consistent everywhere. 6 sources in §4 (meets the ≥6 minimum exactly). Tick = $0.01 used consistently and correctly in every card's R/TP tick conversion (verified: Trade 1 $55→5,500 ticks, $110→11,000, $195→19,500; Trade 2 $30→3,000 — all correct). Daily-open anchor stated as 00:00 UK (the M1 default) with no undisclosed re-selection. | §2, §4, §21b | 5 |
| 1.2 Coverage & currency consistent | Every date in §2/§4/§6/§13/§21 is D−1 (12 May) or earlier for data, D (13 May) for the session. USD/oz used throughout with no unit drift; tick/price dual-quoting in §21 is internally consistent. | whole report | 5 |
| 1.3 Audience & tone | Institutional, Senior-Commodities-Analyst register throughout; no retail framing. | §1, §18 | 5 |
| 2.1 Sections present & ordered | §1–§21 all present in the specified order, including §13a–d and §21a–d. | headings | 5 |
| 2.2 Scorecard as a table | §6 is a proper table (Session/O/H/L/C/RSI2/Trend/Validation Outcome — close enough to the specified columns, Source A/B folded into the Validation Outcome text). §11 daily/weekly/monthly pivot tables are each ordered R3→R2→R1→P→S1→S2→S3. | §6, §11 | 5 |
| 2.3 Method steps visible | §4→§5 show observation→normalization→consensus with the futures-to-spot contango stated; §8 is candle-by-candle; §9 gives regime + persistence/overlap + VOLator + KER; §7 charts are schematic placeholders with an explicit note that the .docx→.md conversion drops images — accepted per brief, not scored down. | §4–§9 | 5 |
| 3.1 Quantitative claims sourced | §1, §12, §14 figures generally point to §4/§6/§13 or a named source (WGC, CME FedWatch, USAGOLD). | text | 4 |
| 3.2 Citations exist & contain data | Spot-checked three: Investing.com 12 May 16:00 (§4), USAGOLD 11 May +0.52% (§4), Reuters/CNBC 11 May sentiment quote (§13a). None self-contradictory or impossible; no fabrication found. | §4, §13a | 4 |
| 3.3 Calculations transparent | RSI2 does **not** reproduce from the report's own stated 5-day closes on 2 of 3 checkable rows (11 May: report 75, recomputed 56.3, diff 18.7; 12 May: report 32, recomputed 45.8, diff 13.8 — both fail the brief's "must reproduce" rule regardless of file-closeness). Daily pivots: R1/S1/R3/S3 do **not** follow from the report's own stated H/L/C=4,773.4/4,676.4/4,704.3 using the stated formula (recomputed R1=4,759.67 vs stated 4,750.4; S1=4,662.67 vs 4,653.0; R3=4,856.67 vs 4,847.4; S3=4,565.67 vs 4,556.0 — each off by ~$9.3–9.7), while P/R2/S2 do reproduce correctly. §21a shows only 3 of the 6 weighted signals that are supposed to sum to the +0.06 composite score, so it is not independently reconstructable. | §6, §11, §9, §21a | 1 |
| 3.4 Numbers reconcile — and vs level file | Internally: D−1 close is consistent across §1/§3/§4/§6/§21b (all ≈$4,695–4,715 band). Externally, against `data/levels/XAUUSD_by_date/2026-05-13.csv` (`_full`): Low $4,676.4 vs $4,638.24 → diff $38.16, **exceeds** the $20.72 (0.20×ATR) failure line. ATR(14) $52 vs $103.61 → **49.8% relative error, exceeds 25% failure line** (also fails vs `_cash` $82.10 at 36.6%). Daily pivots: R1 diff $29.26, R2 diff $28.38, S2 diff $47.48, R3 diff $67.39, S3 diff $46.6 — 5 of 7 daily levels **exceed** the $11.92 (0.115×ATR) failure line; only High and R2/S2-adjacent DP sit inside tolerance. Weekly pivot P: report $4,678.6 vs file $4,660.28(full)/$4,663.11(cash) → diff $18.3–15.5, **exceeds** failure line. Monthly pivot P: report $4,786 vs file $4,673.69(full)/$4,670.91(cash) → diff **$112–115, the largest single miss found**, driven by a monthly High input (≈$5,090) that does not match the leak-free April data. | cross-section + level file | 0 |
| 4.1 Pillars conclude | §8, §9, §10, §12, §14 each end in an explicit direction label (Signal / Net sequence label / Direction / Status). | those sections | 4 |
| 4.2 Peer/cross-asset interpreted | §10 gives a mechanism for each counter (USD-cost-of-carry, risk-appetite absorption, three-channel vs single-channel safe-haven flow), not a bare correlation list. | §10 | 4 |
| 4.3 Synthesis reconciles tensions | §15/§16/§18 explicitly reconcile the short-term bearish tilt against the medium-term range-bullish read; §16 states it "runs alongside" §9 rather than against it. §17 vs §21a: report itself flags "Conflict flag: none," and the two are indeed consistent. | §15–§18, §21a | 4 |
| 4.4 Calibrated language | §17 is one long, grammatically single sentence but stacks several qualifying clauses ("slight downside skew," "most likely," a specific band, plus the structural-floor claim) — borderline hedge-stacking. Confidence stated as Medium in §3/§18. | §3, §17 | 3 |
| 4.5 Card construction (M5, fixed rule — folded into C4 per brief) | §21a states composite score +0.06, explicitly below the fixed 0.25 conviction threshold. M5's fixed rule (brief §3) requires this to produce an **explicit SUPPRESSED row**, not an alternate card. The report instead produces Trade 1 as a live "reduced conviction" LONG card. The operator instruction cited in §19/§20 licenses *not suppressing for incomplete corroboration* — a different axis — and does not license overriding the conviction-threshold rule. This deviation from a fixed M5 rule is also **not logged as a non-conformance in §20 Agent Log** (only mentioned inline in §21a), unlike the anchor-override handling the module requires by analogy. | §21a, §21b, §20 | 1 |
| 5.1 Data dated; staleness flagged | Every price/article in §4/§6/§13 is dated; single-source O/H/L fields in §6 are explicitly flagged "single-source — indicative." | §4, §6, §13, §19 | 5 |
| 5.2 Assumptions up front | Futures-to-spot contango normalization stated with its size (§5, "$5–$10"). Anchor is the default (00:00 UK) with no override to log. However, the conviction-threshold deviation above (row 4.5) is a fixed-rule departure that is **not** surfaced in §20 the way the module's own anchor-override precedent requires. | §21b, §19, §20 | 3 |
| 5.3 Red flags surfaced | §12 (Indian demand drag) and §15 both carry real downside risks; §13d's PPI event collision is carried into the §21b card caveats for Trade 1 ("PPI catalyst within session"). | §12, §15, §21b | 4 |
| 5.4 Restrictions honoured | No bracketed variable names or module codes (M1..M5) or framework name found in the report body; GC=F is corroboration-only and flagged Directional, not Core; no retail dealer premium is folded into the OHLC basis. | whole report | 5 |

## 2. Category roll-up

| Cat | Level | Multiplier | Max | Points | One-line justification |
|---|---|---|---|---|---|
| C1 Prompt adherence | 5 | 1.00 | 20 | 20.00 | Variables, sources, tick math, anchor and audience all cleanly observed. |
| C2 Structure | 5 | 1.00 | 20 | 20.00 | All 21 sections present, correctly ordered; tables well-formed; chart placeholders excused per brief. |
| C3 Accuracy & evidence | 1 | 0.20 | 25 | 5.00 | Citation hygiene is fine, but RSI2 does not reproduce from the report's own closes, daily-pivot R1/S1/R3/S3 do not follow from the report's own stated H/L/C, and ATR14, D−1 Low, most daily pivots, the weekly pivot and (worst) the monthly pivot all fail external reconciliation against the level file — numbers do not reconcile, the defining C3 failure mode. |
| C4 Reasoning & judgment | 3 | 0.65 | 20 | 13.00 | Pillar conclusions, cross-asset mechanism and synthesis are genuinely good (would be level 4), but capped at Adequate by the fixed-rule conviction-threshold breach on Trade 1 card construction, which Category 4 is explicitly charged with catching. |
| C5 Currency & transparency | 4 | 0.85 | 15 | 12.75 | Dating, red-flag surfacing and restriction discipline are strong; docked for not logging the conviction-threshold deviation in §20 the way the module's anchor-override precedent requires. |

**Total = 20.00 + 20.00 + 5.00 + 13.00 + 12.75 = 70.75 → 71**

**Band = Moderate Trust (60–74).** Output is partially reliable; the C3 accuracy gap is large enough that
the report must not be used as-is and is suitable only as an input to human-led review / targeted
regeneration of §6/§11/§21a's numeric layer.

**Override = none.** No fabricated source found in the 3-citation spot-check (no C3-zero trigger beyond
the checklist-driven 0 on row 3.4). The conviction-threshold breach is a fixed-methodology (M5) violation
captured via the C4 card-construction deduction, not a prompt-stated Variables-block restriction, so the
restriction-breach override is not invoked.

## 3. Card Integrity (separate from the 100 — linter rows copied verbatim)

| card_id | strategy | flags | dud | integrity = 100 − 40·dud − 10·warn |
|---|---|---|---|---|
| 2026-05-13_Trade_1 | Trade 1 - Daily Directional (reduced conviction) | CLEAN | False | 100 |
| 2026-05-13_Trade_2 | RANGE FADE: short the upper rail / long the lower rail | WARN_R_TINY(0.29xATR) | False | 90 |
| 2026-05-13_Trade_3B | Trade 3 - Complex (variant 3B - Mean-Reversion, range regime) | CLEAN | False | 100 |

`card_integrity = mean(100, 90, 100) = 96.67`
`n_cards = 3` · `n_duds = 0` · `n_warns = 1`

Note (context only, not a re-derivation): Trade 2's WARN_R_TINY(0.29×ATR) is consistent with the true
leak-free ATR14_full = 103.6121 (30/103.6121 = 0.29), not with the report's own stated ATR of $52
(30/52 = 0.58, which would not have triggered the warn) — one more symptom of the §9/§21 ATR error
recorded under C3 above.

## 4. Summary line

`c1=5 c2=5 c3=1 c4=3 c5=4 total=71 band=Moderate override=none card_integrity=96.67 n_cards=3 n_duds=0 n_warns=1`

See `qa/gold_regen_qa1/2026-05-13_feedback.md` for the numbered, actionable defect list.
