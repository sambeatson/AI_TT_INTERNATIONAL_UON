# Trust Score — Gold_Report_14Jul2026.md (D = 2026-07-14, run gold_regen_qa1)

Scored against `docs/AI_Output_Trust_Score_Framework_v3.7.txt` §4–7, mapped to trade-card reports
per `docs/QA_PROTOCOL_TRADE_CARDS.md` and `qa/gold_regen_qa1/REVIEWER_BRIEF.md`. Category 3 checked
against `data/levels/XAUUSD_by_date/2026-07-14.csv` (`last_bar_date=2026-07-13 < 2026-07-14`, confirmed
leak-free). Report claims basis "Spot, immediate settlement (loco London)" throughout (§2/§3) →
checked primarily against the `_full` columns, with `_cash` shown alongside for completeness.

## 1. Section 7 checklist

| Row | Notes | Evidence | Score |
|---|---|---|---|
| 1.1 Variables respected | Asset defined correctly (XAU/USD spot, GC=F corroboration-only); USDX first counter (§10); 6/6 sources (§4, meets minimum exactly); lookback 5/25 stated (§2); USD/oz, tick 0.01 used consistently. But the daily-open anchor is presented as a plain fixed anchor ("session anchor 00:00 UK" §2; "Market at 00:00 UK" §21b Trade1) with no override/non-conformance marking anywhere except a buried §20 Agent Log line — violates M1 §H's explicit requirement that a deviation be marked on the card, in the body, and in the handoff record, never presented as the anchor. | §2, §4, §10, §20, §21b | 3 |
| 1.2 Coverage/currency consistent | All data dated D−1 or earlier, session dated D; USD/oz used throughout with no unit drift. | whole report | 5 |
| 1.3 Audience & tone | Institutional Senior-Commodities-Analyst register maintained throughout; no retail tone. | §1, §18 | 5 |
| **C1 mean** | (3+5+5)/3 = 4.33 | | **level 4** |
| 2.1 Sections present & ordered | All 21 sections + required subsections (13a–d, 21a–d) present, correctly ordered, correctly headed. | headings | 5 |
| 2.2 Scorecard as table | §6 is a real table but combines Source A/B into one "Sources" column rather than the two named columns the spec implies; §11 pivot tables show 5 levels each side (R5…S5) rather than the specified 3 (R3…S3) — extra, not missing, but non-conforming to the fixed table shape. | §6, §11 | 3 |
| 2.3 Method steps visible | §4–§5 show observation→normalization→consensus (futures-to-spot basis mentioned qualitatively, no explicit numeric contango stated); §8 is candle-by-candle; §9 gives overlap/persistence/VOLator with values; §7 chart placeholders are empty but per brief this is a conversion artifact and not scored. | §4–§9 | 4 |
| **C2 mean** | (5+3+4)/3 = 4.0 | | **level 4** |
| 3.1 Quantitative claims sourced | §1/§12/§14 assert USDX ~100.9, 10Y ~4.59%, Fed-hike odds 60–70%, oil +4–5%, VIX ~15 with no pointer to any source anywhere in the report — §4's evidence table covers gold price only, §13 covers gold-specific news/sentiment only; no macro/rates/FX source is named at all. | §1, §12, §14 | 1 |
| 3.2 Citations exist & consistent | Spot-checked OCBC (institutional, dated only "Jul" — imprecise), RoboForex (13 Jul), LiteFinance (13 Jul): all named, mostly dated, and each is reused consistently across §4 (price) and §13a (sentiment) without contradiction. No fabricated source detected. | §4, §13a | 4 |
| 3.3 Calculations transparent | Jul 13 RSI2 (9.5) does **not** reproduce from the report's own 5 stated closes (recomputes to 0.0 — see feedback #3); pivot arithmetic is internally correct given its own (wrong) H/L/C inputs; §21a direction score shows only 3 of 6 weighted terms, not the full Σsignal×weight. | §6, §11, §21a | 1 |
| 3.4 Numbers reconcile (internal + level file) | **Internal:** §11.1's stated prior-session H/L/C (4,102.00/4,068.74/4,084.41) contradicts §6's Jul 13 OHLC (4,091.14/4,050.39/4,059.39) used everywhere else (§1,§3,§4,§21b MARKET entry) — two different "D−1" price sets in one report. **External:** D−1 close/low fail against both bases; daily and monthly pivots fail against both bases by 27–272 USD (all »0.115×ATR14); only the weekly pivots reconcile (within 0.56–1.30 USD of `_full`, well inside tolerance). See feedback for the full table. | cross-section + level file | 0 |
| **C3 mean** | (1+4+1+0)/4 = 1.5 → tie, resolved down per framework §9 "pick the lower rubric level when in doubt" | | **level 1** |
| 4.1 Pillars/cards reach a defended conclusion | §8/§10 end in explicit judgement labels; §12 labels each factor; §9 states a bias. But Trade 3A (§21b) substitutes a breakout/stop-entry for the M5-specified 57.5%-retracement construction with no swing endpoints or magnitude check logged — a real card-construction failure, and §21a shows only a partial score derivation. | §8, §9, §10, §12, §21b | 2 |
| 4.2 Peer/cross-asset interpreted | §10 gives an explicit mechanism for each counter (USDX real-yield/opportunity-cost channel, silver complex-liquidation tell, equities haven-demand channel) — not a bare correlation list. | §10 | 5 |
| 4.3 Synthesis reconciles tensions | §9 explicitly reconciles the KER-vs-price-bias tension; §15/16/18 handle bull/bear tensions; §17 vs §21a explicitly notes "no conflict." But the Trade 3A methodology substitution is never acknowledged as a departure from the M5 rule it violates. | §9, §15–§18, §21a | 3 |
| 4.4 Calibrated language | §17 is one (compound) sentence; §3 states confidence = Medium explicitly; conditional language ("likely," "would," "unless") used appropriately throughout. | §3, §17 | 4 |
| **C4 mean** | (2+5+3+4)/4 = 3.5 → tie, resolved down | | **level 3** |
| 5.1 Data dated; staleness flagged | Price/news data dated to the day in almost all cases; OCBC dated only "Jul" (imprecise). | §4, §6, §13, §19 | 4 |
| 5.2 Assumptions up front; anchor override on card + §20 | Futures-to-spot normalization is stated up front (§5, §19). But the anchor override (see 1.1) is **not** stated up front or on the card — it surfaces only in §20's Agent Log, the second-to-last section — a direct, explicitly-checked failure of the module's disclosure requirement. | §21b, §19, §20 | 1 |
| 5.3 Red flags surfaced | June-CPI (§13d Tier-1) collision is explicitly carried into all three live cards' Caveats rows; geopolitical two-sided risk and Fed-hike risk are surfaced in §12/§15. | §12, §15, §21b | 5 |
| 5.4 Restrictions honoured | No bracketed variable names or module codes (M1…M5) found in the body; GC=F is explicitly corroboration-only throughout. But §11 labels the daily/monthly pivot inputs "CORROBORATED, not indicative" when they diverge from the level file by 50–270 USD — an unsupported certainty claim on data that does not hold up; Trade 3A's stop cell also carries a literal unresolved "R?" placeholder. | whole report | 2 |
| **C5 mean** | (4+1+5+2)/4 = 3.0 | | **level 3** |

## 2. Category roll-up

| Category | Max | Level | Multiplier | Points | Justification |
|---|---|---|---|---|---|
| 1 Prompt Adherence | 20 | 4 | 0.85 | 17.00 | Variables solid; anchor-override handling is the one real, moderate deviation. |
| 2 Structural Alignment | 20 | 4 | 0.85 | 17.00 | All sections present/ordered; scorecard/pivot table shapes deviate from spec but lose no information. |
| 3 Accuracy & Evidence | 25 | 1 | 0.20 | 5.00 | Internal price-set contradiction, D−1 OHLC and daily/monthly pivots fail against the level file on both bases, RSI2 does not reproduce, macro claims largely unsourced. |
| 4 Reasoning & Judgment | 20 | 3 | 0.65 | 13.00 | Narrative pillars are well-reasoned and cross-asset mechanisms are explained; Trade 3A methodology substitution and partial §21a transparency pull this down. |
| 5 Currency & Transparency | 15 | 3 | 0.65 | 9.75 | CPI-collision flagging is strong; anchor-override non-disclosure and an unsupported "CORROBORATED" claim on bad pivot data are the material gaps. |

**Total = 17.00 + 17.00 + 5.00 + 13.00 + 9.75 = 61.75 → 62 / 100**

**Band: Moderate Trust (60–74).** Meaningful C3 gaps (the framework's highest-weighted, most
consequential category) sit alongside otherwise solid structure and reasoning — a textbook Moderate
Trust profile: not usable as-is, but not a wholesale structural/reasoning failure either.

**Override check:**
- Hallucinated source override: **not triggered.** No spot-checked citation was found to be
  fabricated, self-contradictory, or impossible; the numeric failures are data-reconciliation errors,
  not invented sources.
- Restriction breach override: **not triggered.** The anchor-override disclosure failure (1.1/5.2) is
  real and scored down in both categories, but the override *is* disclosed somewhere in the report
  (§20) rather than being an open, undisclosed violation — the defect is placement/completeness of the
  disclosure, not its total absence.

## 3. Card Integrity (SEPARATE — not part of the 100; linter rows copied verbatim from
`qa/gold_regen_qa1/lint_static/2026-07-14.csv`)

| card_id | strategy | flags | dud | card score (100 − 40·dud − 10·warn) |
|---|---|---|---|---|
| 2026-07-14_Trade_1 | Trade 1 — Daily Directional (SHORT) | CLEAN | False | 100 |
| 2026-07-14_Trade_2 | Trade 2 — Pivot (RANGE-edge fade) | UNPRICED | True | 60 |
| 2026-07-14_Trade_3A | Trade 3A — Momentum-Pullback (SHORT) | CLEAN | False | 100 |

`card_integrity = mean(100, 60, 100) = 86.7` (Trade 3B was correctly SUPPRESSED by the report's own
dual-gate check and is excluded from the linter/this mean, consistent with "report level = mean over
non-suppressed cards.")

## 4. Summary line

```
c1=4  c2=4  c3=1  c4=3  c5=3
total=62  band=Moderate Trust  override=none
card_integrity=86.7  n_cards=3  n_duds=1  n_warns=0
```

Full defect list, per card and per report section, with the level-file numbers a compliant level
must satisfy: see `qa/gold_regen_qa1/2026-07-14_feedback.md`.
