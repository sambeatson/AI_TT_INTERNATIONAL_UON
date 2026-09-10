# Trust Score — Gold_Daily_Report_27May2026.md (D = 2026-05-27, ASSET = XAUUSD)

Run: `gold_regen_qa1`. Scored against `docs/AI_Output_Trust_Score_Framework_v3.7.txt` §4–7 and
`docs/QA_PROTOCOL_TRADE_CARDS.md`, per `qa/gold_regen_qa1/REVIEWER_BRIEF.md`.

Leak-safety check: `data/levels/XAUUSD_by_date/2026-05-27.csv` states `last_bar_date=2026-05-26` < `date=2026-05-27`. OK — file is safe to use.

Basis used for all Category 3 checks: **`_full`** (continuous loco-London), because the report's own
Market Definition states "Global — 24-hour OTC spot market" / "Spot, immediate settlement (loco
London)" throughout, not a US-session range. Tolerances per brief §4, keyed to `atr14_full = 93.0029`:
consistent ≤3.72 (close/pivot) or ≤8.37 (O/H/L); discrepancy above that; failure >10.70 (close/pivot)
or >18.60 (O/H/L); ATR14 failure >25% relative; RSI2 failure >15 or non-reproducing.

## 1. Section 7 checklist

| Row | Notes | Evidence observed | Score | Action required |
|---|---|---|---|---|
| **1.1** Variables respected | Asset correctly scoped to LBMA loco-London spot, GC=F corroboration-only, not numerically used. USDX is first of the three named counters. 5/25-session lookback matches. USD/oz used throughout; ticks (0.01 USD/oz) stated and used consistently. §4 footnote says "Six independent observations meet the minimum source count" but the table lists **seven** rows — a self-contradicted count. §11's daily pivot table is explicitly computed "from 25 May H/L/C" (D−2), not the D−1 session the rest of the report (§1/§3/§4/§6) treats as current — a variable-scope inconsistency (as-of date). | §2, §4, §11 header | **3** | List: source-count mismatch (§4); daily-pivot as-of date uses D−2 not D−1 (§11) |
| **1.2** Coverage & currency consistent | Units (USD/oz, ticks) consistent throughout — no drift. But §11's daily pivots are silently built on 25 May data while §1/§3/§4/§6/§21 all anchor on 26 May as "current" — an undisclosed date inconsistency between sections that is then propagated into Trade 2 and referenced in Trade 3A. | §11 vs §1/§3/§4/§6 | **2** | Flag the daily-pivot date drift explicitly; rebuild §11 daily table from the 26 May (D−1) session |
| **1.3** Audience & tone | Institutional Senior Commodities Analyst register maintained throughout; no retail tone. | §1, §18 | **5** | none |
| **2.1** Sections present & ordered | All 21 top-level sections and all named subsections (13a–d, 21a–d) present, correctly headed and ordered. | headings | **5** | none |
| **2.2** Scorecard as table | §6 is a real table, but uses columns Date/O/H/L/C/RSI2/Trend/Source A/Source B — no explicit "Validation" column (validation is prose below the table instead). §11 weekly/monthly tables are correctly R3→P→S3 (3 levels/side); the **daily** table runs R5→P→S5 (5 levels/side), beyond the specified 3-level format. | §6, §11 | **4** | Add explicit Validation column to §6; trim daily pivot table to R3→P→S3 |
| **2.3** Method steps visible | §4–§5 show observation→normalisation→consensus (no futures data was actually used, so no normalisation step was needed — consistent, not a gap); §8 is candle-by-candle; §9 covers persistence/overlap/VOLator/KER; charts appear as captions only (accepted per brief — docx→md image loss). | §4–§9 | **5** | none |
| **3.1** Quantitative claims sourced | §1/§12/§14 claims are mostly qualified ("reportedly") and point back to §4/§13, but several (PBoC 17-month streak, dealer-inquiry improvement) lack a direct pointer. | §12, §14 | **4** | Add explicit source pointers for the PBoC and dealer-demand claims |
| **3.2** Citations exist & consistent | Spot-checked 3: MyGoldCalc (§4, 26 May, 4,489.65 — matches its own §6/§21 use), Reuters (§13a, 26 May, "Oil rises...US-Iran optimism" — consistent with §13c/§12), World Gold Council (§13a, 26 May, bullish demand quote — consistent with the PBoC structural-floor language in §12). All three named, dated, internally consistent. No fabrication found. | §4, §13a | **5** | none |
| **3.3** Calculations transparent | RSI2 reproduces exactly from the report's own five closes (verified: RS=0.5817 → RSI2=36.78≈36.8). Pivot formula P=(H+L+C)/3 shown with worked numbers. ATR-based stop math is shown but **internally inconsistent**: Trade 1's 0.25×ATR buffer (4,597.00−4,585.00=12.00) implies ATR≈48.0, while Trade 1's own 3.5×ATR cap (184.80) and Trade 3A's 0.25×ATR stop (13.20) both imply ATR≈52.8 — two different ATR values used inside the same report. | §11 (P calc), §21b (stop calcs) | **3** | Reconcile the report's own ATR14 figure to one consistent value across all three cards |
| **3.4** Numbers reconcile — incl. against the level file | Internally, the D−1 close (4,489.65) is consistent across §1/§3/§4/§6/§21 MARKET entry — good. **Externally, against `XAUUSD_by_date/2026-05-27.csv` (_full):** D−1 close fails (\|4,507.58−4,489.65\|=17.93 > 10.70 threshold); D−1 low fails (\|4,482.53−4,453.12\|=29.41 > 18.60); D−1 open/high are consistent (diffs 2.11 / 0.27). §11 daily pivots fail on P (31.38), S1 (57.87), R1 (35.77), S2 (53.48), R3 (13.67), S3 (79.97) — only R2 (9.28) lands in the discrepancy band, not failure. §11 weekly pivots: P/consistent, R1/S1 discrepancy, but R2 (15.75), S2 (17.17), R3 (22.88) fail. Monthly pivots reconcile well (all diffs ≤1.75, consistent). The report's own implied ATR14 (≈48–52.8, see 3.3) fails against both `atr14_full` (93.0029, 43% off) and `atr14_cash` (71.9164, 27% off) — both exceed the 25% failure threshold. RSI2 (36.8 vs `rsi2_full` 50.3332, diff 13.5) lands in the 5–15 discrepancy band — not a failure, since it reproduces from the report's own closes. This is a material, systemic reconciliation break spanning close, low, the entire daily pivot ladder, and the working ATR — it feeds directly into Trade 1, 2 and 3A's stop/entry/target construction. | level file vs §6, §11, §21b | **0** | Rebuild §6 OHLC, §11 daily pivots and the working ATR14 from the correct D−1 (26 May) session before any card is reconstructed |
| **4.1** Pillars conclude | §8 "Exhaustion — reversal risk"; §9 "Bias: Bearish" + KER resolution; §10 "all four counters confirm"; §12 each subsection carries a price-negative/neutral label; §14 macro is directionally toned throughout even without one closing label. Card-level "pillars" (§21b) are weaker: Trade 3A's own TP1 (4,534.62) sits **above** its 4,529.96 short entry — an indefensible target the report does not catch or flag. | §8–§10, §12, §21b | **4** | Flag/fix the Trade 3A TP1 side error |
| **4.2** Peer/cross-asset interpreted | §10 gives explicit mechanism per counter (real-yield channel, risk-on rotation, beta-pair read), not a bare correlation list. | §10 | **5** | none |
| **4.3** Synthesis reconciles tensions | §9 explicitly reconciles the Transitional regime label against the strongly-negative KER reading, resolving to TREND_DOWN; §21a states no conflict between model direction and §17. But the strategy build (§21b) carries an unflagged TP1-side defect and an unflagged wrong-day pivot basis that the synthesis never surfaces or reconciles — a gap between the narrative's polish and the strategy section's own internal quality. | §9, §21a, §21b | **3** | Have the synthesis/agent-log surface the card-construction and pivot-date issues it currently misses |
| **4.4** Calibrated language | §17 is exactly one sentence; confidence stated Medium in §3/§18; hedge language ("likely", "may", "could") used appropriately without hedge-stacking. | §3, §17, §18 | **5** | none |
| **5.1** Data dated; staleness flagged | Every price/article in §4/§6/§13 is dated; 21–22 May intraday H/L and several Silver rows are flagged single-source indicative. The one gap: §11's use of 25 May (not 26 May) data for daily pivots is never flagged as a staleness/date departure from the report's own D−1 convention. | §4, §6, §13, §11 | **4** | Flag the §11 daily-pivot date basis explicitly |
| **5.2** Assumptions up front | Daily-open anchor override is stated in §2 and repeated in §20 (compliant handling — logged, not silently presented as the anchor value). Single-source pivot propagation into the cards is stated in §19 and appears as a caveat on Trade 2 / Trade 3A. No futures normalisation needed (none used). Gap: the 25-May-vs-26-May pivot basis choice is never stated as an assumption or deviation anywhere in the report. | §2, §19, §20, §21b | **3** | State the daily-pivot date-basis choice as an explicit assumption/deviation |
| **5.3** Red flags surfaced | §12/§15 carry the risk case; §13d event collisions (28 May GDP, 29 May PCE) are carried into all three cards' caveats. | §12, §15, §21b | **5** | none |
| **5.4** Restrictions honoured | No synthesised price presented as sourced; futures used corroboration-only (and in fact not numerically used at all); no bracketed `[VARIABLE]` placeholders, no M1–M5 module codes, no framework name found in the report body (checked); instrument common names used throughout. | whole report | **5** | none |

## 2. Category roll-up

| Cat | Max | Row mean | Level | Multiplier | Points | Justification |
|---|---|---|---|---|---|---|
| C1 Prompt adherence | 20 | (3+2+5)/3=3.33 | **3** | 0.65 | 13.0 | Variables mostly respected but the daily-pivot as-of date silently uses D−2, and the source count in §4's footnote contradicts its own table |
| C2 Structural alignment | 20 | (5+4+5)/3=4.67 | **5** | 1.00 | 20.0 | All 21 sections present and correctly ordered; only minor formatting gaps (no explicit Validation column, 5-level daily pivot table) |
| C3 Accuracy & evidence | 25 | (4+5+3+0)/4=3.00 | **3** | 0.65 | 16.3 | Sourcing and citation integrity are solid and RSI2 is exactly reproducible, but the D−1 close/low, the whole daily-pivot ladder, several weekly levels, and the report's own working ATR14 all fail reconciliation against the level file and, in ATR's case, against each other |
| C4 Reasoning & judgment | 20 | (4+5+3+5)/4=4.25 | **4** | 0.85 | 17.0 | Every analytical pillar reaches a defended, mechanism-based conclusion and the KER/regime tension is explicitly reconciled; card construction (Trade 3A TP1 side, unflagged pivot-date issue) is the one unaddressed weak spot |
| C5 Currency & transparency | 15 | (4+3+5+5)/4=4.25 | **4** | 0.85 | 12.8 | Dating, red-flag surfacing and restriction discipline are strong and the anchor override is handled compliantly; the daily-pivot date basis is the one un-stated assumption |

**Total = 13.0 + 20.0 + 16.3 + 17.0 + 12.8 = 79.1 → 79 / 100**

## 3. Band and override check

- **Band: High Trust (75–89).**
- Hallucinated-source override: not triggered — all three spot-checked citations (MyGoldCalc, Reuters, World Gold Council) are named, dated and used consistently; no fabrication found.
- Restriction-breach override: not triggered — no bracketed variable names, no M1–M5 module codes, no framework name in the report body; the daily-open-anchor override is logged as an override in §2 and §20, not silently presented as the instance anchor.
- **override = none**

## 4. Card Integrity (linter rows, copied verbatim from `qa/gold_regen_qa1/lint_static/2026-05-27.csv`)

| card_id | strategy | flags | dud | card score |
|---|---|---|---|---|
| 2026-05-27_Trade_1 | Trade 1 — Daily Directional | CLEAN | False | 100 |
| 2026-05-27_Trade_2 | Trade 2 — Pivot, trend-following short | CLEAN | False | 100 |
| 2026-05-27_Trade_3A | Trade 3 → variant 3A — Momentum-Pullback short | DUD_TP1_SIDE | True | 100 − 40×1 − 10×0 = 60 |

n_cards = 3, n_duds = 1, n_warns = 0. **card_integrity (report level, mean over non-suppressed cards) = (100+100+60)/3 = 86.7**

## Summary line

```
c1=3
c2=5
c3=3
c4=4
c5=4
total=79
band=High Trust
override=none
card_integrity=86.7
n_cards=3
n_duds=1
n_warns=0
```

See `qa/gold_regen_qa1/2026-05-27_feedback.md` for numbered, actionable feedback.
