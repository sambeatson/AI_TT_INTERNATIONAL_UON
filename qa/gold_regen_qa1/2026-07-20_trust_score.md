# Trust Score — Gold_Report_20Jul2026.md (D = 2026-07-20, run gold_regen_qa1)

## 1. Section 7 Checklist

| Row | Reviewer notes | Evidence observed | Score (0–5) | Action required |
|---|---|---|---|---|
| 1.1 Variables respected | Asset correctly defined as XAU/USD spot, London Good Delivery bar / LBMA loco-London, GC futures named as corroboration-only (and in fact never quoted as a raw price anywhere in §4/§19/§20 — declared but unused). USDX is the first counter in §10. As-of = Fri 17 Jul, the last completed session strictly before D — correctly stated in §2/§20. Lookback 5 / 25 sessions correct. USD/oz used throughout. §4 lists exactly 6 sources (minimum met). Native-unit (tick) reporting is present and consistent on Trade 1 but absent on Trade 3C's stop/TP1/TP2 rows (price only, no tick count) — Presentation Rule 8 applied inconsistently. Most seriously, the §11 daily and weekly pivot tables are built from the wrong prior period (Thu 16 Jul and the week to 10 Jul respectively) even though §2/§20 both correctly state the as-of session is Fri 17 Jul — see 3.4. | §2, §4, §11, §20, §21b | 3 | Add tick counts to the Trade 3C card; fix the §11 pivot input periods (see 3.4) |
| 1.2 Coverage & currency consistent | §2/§20 state D−1 = 17 Jul; §6 five-day block ends 17 Jul; §13 events dated correctly. But §11's own "prior session: Thu 16 Jul" and "prior week to 10 Jul" headers are a full period stale relative to the as-of date stated two sections earlier — a direct within-report currency contradiction, not merely an external mismatch. No USD/tick unit drift found elsewhere. | §2, §11, §20 | 2 | Correct the §11 period headers and every level built from them |
| 1.3 Audience & tone | Institutional, no retail language. No explicit "Senior Commodities Analyst" role line in §1/§18, but tone is consistent with that register throughout (§12, §14, §18). | §1, §18 | 4 | Optional: state the role/audience explicitly |
| 2.1 Sections present & ordered | All 21 sections present in order, including §13a–d and §21a–d. | headings | 5 | None |
| 2.2 Scorecard as a table | §6 is a genuine 11-column table. §11 pivot tables are all R5→P→S5 (five levels each side, per M4 §11), correctly ordered, resistance-on-top. No explicit confirmation that R2−P = P−S2 is printed (M4 §11 asks for this check to be shown). | §6, §11 | 4 | Add the R2−P = P−S2 identity check line under each pivot table |
| 2.3 Method steps visible | §4→§5 show observation → normalization → consensus (weighted median, exclusion rationale for the weekend mid). No futures-to-spot adjustment appears because no futures quote is actually used as a raw source — consistent, not a defect. §8 is candle-by-candle; §9 gives regime + VOLator + KER; charts present as headers only (docx→md image loss, accepted per brief). | §4–§9 | 4 | None material |
| 3.1 Quantitative claims sourced | §1, §12, §14 figures mostly trace to §4/§6/§10/§13 (e.g. DXY level cross-referenced to §10, CFTC positioning to §13a-adjacent context). A few §14 figures ("DXY ≈ 100.5–100.8") are stated without a direct citation row, though they are consistent with the §10 USDX read. | §1, §12, §14 | 4 | Cross-reference the §14 DXY range to a §4/§13 source row |
| 3.2 Citations exist & contain data | Spot-checked three: (1) Reuters 17 Jul "ends down on the week" — consistent with the §10/§14 dollar narrative. (2) FXStreet 18 Jul "reaffirms the near-term bearish outlook" — consistent with the §13b bearish tilt. (3) TradingEconomics is cited twice for 17 Jul with apparently opposed implications: §4 gives "4,016.95 ... +1.03% on day" (implies a close above USD 4,000) while §13a's TradingEconomics headline the same date reads "Gold remained below $4,000 an ounce on Friday ... down more than 3% for the week." Both are individually plausible (intraday quote vs. the eventual close, given the report's own "reversal candle" narrative) but the report never reconciles or timestamps them — an unresolved same-source, same-date inconsistency, not proven fabrication. No hallucination override triggered. | §4, §13a | 3 | Reconcile or timestamp-differentiate the two TradingEconomics 17 Jul figures |
| 3.3 Calculations transparent | §21a's direction score is fully transparent and reproduces exactly: −0.25 −0.20 −0.05 +0.087 −0.051 −0.045 = −0.509 ≈ −0.51 (verified against §20's per-signal trace). Daily/weekly/monthly pivot tables show an input row (H/L/C + period), though the period itself is wrong for two of the three (see 3.4). By contrast, RSI2 has **no working shown** beneath §6 — M4 §6 mandates "the two close-to-close changes, the mean gain, the mean loss, RS, and the resulting value" for the latest session; only a qualitative note is given. ATR(14) is **never stated as a number in §9** — it appears only on the Trade 1 card (60.80), which is itself wrong (see 3.4) — violating M4 §9's requirement that ATR14 "must appear here explicitly and must be the same number that appears on each card." | §6, §9, §20, §21a | 2 | Show the RSI2 working under §6; state ATR14 explicitly and correctly in §9 |
| 3.4 Numbers reconcile — and reconcile against the level file | D−1 close/OHLC reconcile well: report Fri 17 Jul O/H/L/C = 3,972.95 / 4,024.22 / 3,959.69 / 4,017.32 vs. level file (`_full`) 3,977.65 / 4,023.83 / 3,959.65 / 4,016.50 — diffs of 4.70 / 0.39 / 0.04 / 0.82, all inside the "consistent" bands (open/high/low ≤ 8.74, close ≤ 3.88 at ATR14_full = 97.1236). Everything downstream of the pivots and ATR/RSI2 fails badly: (a) **daily pivots** are built from Thu 16 Jul H/L/C, giving P=3,981.13/R1=4,003.95/S1=3,953.75 vs. leak-free (Fri 17 Jul-based) `d_full_P`=3,999.9933/`d_full_R1`=4,040.3367/`d_full_S1`=3,976.1567 — diffs of 18.86 / 36.39 / 22.41, all far past the 11.17 (0.115×ATR14) Category-3 failure ceiling; (b) **weekly pivots** are built from "prior week to 10 Jul" (ISO W28) instead of the correct last-completed week 13–17 Jul (ISO `w_full_period`=2026-W29), giving P=4,113.33 vs. `w_full_P`=4,026.44 (diff 86.89, ~9× the failure threshold), R1=4,186.67 vs. 4,093.23 (diff 93.44), S1=4,016.67 vs. 3,949.71 (diff 66.96); (c) **monthly pivots** use the correct period label (June 2026) but still fail to reconcile: P=4,229.33 vs. `m_full_P`=4,165.5133 (diff 63.82, ~0.66×ATR14); (d) **ATR(14)** on the Trade 1 card = 60.80 vs. `atr14_full`=97.1236 — a 37.4% relative miss, past the 25% failure ceiling (vs. `atr14_cash`=76.1936 it is a 20.2% "discrepancy"-band miss, still not consistent); (e) **RSI2** = 70.2 (Fri) vs. `rsi2_full`=32.3005 / `rsi2_cash`=31.4971 — a 37.9-point gap, far past the >15-point failure threshold, and the value does not visibly reproduce from the report's own stated closes either (no working shown, see 3.3); (f) Trade 3C's `swing_high_25d` = 4,310.00 vs. `swing_high_25d_full`=4,382.22 (diff 72.22, ~0.74×ATR14), which mis-sizes the Trade 3C range width and every level built from it. The daily/weekly pivot error also propagates into Trade 1's stated confluences ("daily R1 4,003.95", "weekly S1 4,016.67") and into §15/§16/§17/§18's repeated "weekly P (4,113.33)" invalidation reference. | cross-section + level file | 0 | Rebuild §11 daily/weekly/monthly pivots from the correct prior periods; restate ATR14 correctly in §9 and on every card; show and correct RSI2; re-source Trade 3C's swing_high_25d |
| 4.1 Pillars conclude | §8 ends "Exhaustion — reversal risk"; §9 ends Trending-Bearish with an explicit KER-vs-VOLator tension note; §10 gives Confirms/Contradicts per counter; §12 factors each carry a direction label; §14 bullets mostly labelled. The Trade 1/Trade 3C "pillars" (cards) reach conclusions but those conclusions rest on the wrong ATR14 and wrong swing_high_25d identified in 3.3/3.4 — a defended-conclusion pillar built on an unreliable number. | §8, §9, §10, §12, §14, §21b | 3 | Rebuild the affected card levels once ATR14 and swing_high_25d are corrected |
| 4.2 Peer/cross-asset interpreted | §10 states a causal mechanism for every counter (USDX price effect, equity risk-off flows, DAX de-risking, silver beta) rather than a bare correlation list, and explicitly bolds the three-counter contradiction against the medium-term regime. | §10 | 5 | None |
| 4.3 Synthesis reconciles tensions | §9 explicitly names the KER-vs-VOLator-slope tension as a TRANSITION signature; §15/§16/§18 explicitly carry the short-term-bounce-vs-medium-term-bearish conflict through to the forecast and judgement without silently resolving it; §21a states the §17-vs-conviction conflict in one sentence per M5 §2b/§9 without editing either output. | §9, §15–§18, §21a | 5 | None |
| 4.4 Calibrated language | §17 is exactly one sentence (single terminal period, compound clauses). Confidence stated as "Medium" in §3/§18. Hedge language ("likely", "credible", "base-case") used without stacking, though §17's own "weekly pivot near 4,113" figure is the erroneous one identified in 3.4. | §3, §17 | 5 | Correct the weekly-pivot figure quoted in §17 once §11 is fixed |
| 5.1 Data dated; staleness flagged | Prices/articles in §4/§6/§13 are dated, and §6/§19 flag the silver secondary-asset data as directional-context-only. But the stale §11 daily/weekly pivot inputs (Thu 16 Jul; week to 10 Jul) are presented as current without any staleness flag anywhere in §11 or §19, despite being a full period older than the as-of date stated in §2/§20 — the exact "data older than the coverage period implies, and not flagged" failure pattern. | §11, §19 | 2 | Flag or (preferably) correct the stale pivot-period inputs |
| 5.2 Assumptions up front | Daily-open-anchor override is logged as an explicit non-conformance in §20, with the same 00:00 UK value stated identically on the Trade 1 card, in §20, and in the report body — compliant handling per the framework's own disclosure rule. Single-source-indicative pivot status is carried into Trade 1's and Trade 3C's caveats and into Trade 2's suppression reasoning. Futures corroboration-only assumption is honoured (no futures price actually used, so nothing to normalise). | §21b, §19, §20 | 4 | None material |
| 5.3 Red flags surfaced | §12/§15 carry the hawkish-Fed/real-yield risk, the Hormuz/oil cross-current, and the FOMC as the bolded highest-impact event; §13d's FOMC and data-run collisions are explicitly carried into both live cards' caveats. | §12, §15, §21b | 5 | None |
| 5.4 Restrictions honoured | Pre-emit naming scan (M4 Presentation Rules 2/3/9) fails: the bracketed token **"[DAILY_OPEN_ANCHOR]"** is printed verbatim as a §20 sub-heading ("**[DAILY_OPEN_ANCHOR] override note:**"); the internal field name **"regime_label"** is printed verbatim three times (§20 ×2, §21 Trade 3 heading "regime_label TRANSITION" ×1); the internal step code **"Step-4"** is printed in §20 ("Step-4 synthesis"). These are explicit, mechanical violations of Rules 2, 3 and 9 — an openly breached restriction. | §20, §21 | 0 | Remove every bracketed token, internal field name, and step code; replace with plain-English equivalents |

## 2. Category Roll-up

| Cat | Mean of rows | Level (0–5) | Multiplier | Max | Points | One-line justification |
|---|---|---|---|---|---|---|
| C1 Prompt adherence | (3+2+4)/3 = 3.00 → **restriction-breach override applies: −1 level** | 2 | 0.40 | 20 | 8.0 | Asset/sources/anchor handling correct, but §11's period drift and the restriction breach (5.4) force the override floor |
| C2 Structure | (5+4+4)/3 = 4.33 | 4 | 0.85 | 20 | 17.0 | All 21 sections present and ordered; pivot tables correctly shaped but missing the R2−P=P−S2 identity check |
| C3 Accuracy & evidence | (4+3+2+0)/4 = 2.25 | 2 | 0.40 | 25 | 10.0 | D−1 OHLC reconciles well, but daily/weekly/monthly pivots, ATR14, RSI2 and Trade 3C's swing_high_25d all fail the level-file reconciliation, several by multiples of the failure threshold |
| C4 Reasoning & judgment | (3+5+5+5)/4 = 4.50 → rounds down to lower level per "pick the lower level when in doubt" | 4 | 0.85 | 20 | 17.0 | Excellent narrative synthesis and cross-asset interpretation; card-construction pillar (4.1) weakened by the wrong ATR14/swing inputs feeding Trade 1 and Trade 3C |
| C5 Currency & transparency | (2+4+5+0)/4 = 2.75 | 3 | 0.65 | 15 | 9.75 | Anchor-override and red-flag handling are exemplary, but the stale pivot inputs go unflagged (5.1) and the naming-scan restriction breach (5.4) scores 0 |

## 3. Total, Band, Override

```
total = 8.0 + 17.0 + 10.0 + 17.0 + 9.75 = 61.75 → 62
band = Moderate Trust (60–74)
override = restriction_breach
```
Restriction-breach override fires: the report body prints the bracketed variable token
`[DAILY_OPEN_ANCHOR]` and the internal field name `regime_label` (×3) and the internal step code
`Step-4` verbatim — explicit violations of M4 Presentation Rules 2, 3 and 9 (No Variable Exposure /
No Module References / Pre-Emit Naming Scan). Per the framework's override rule this caps the band at
Moderate Trust (60–74) and reduces C1 by at least one rubric level; both are already reflected above,
and the naturally-computed total (62) independently lands inside the capped band, so no further
adjustment is needed. No cited source was found to be clearly fabricated (the TradingEconomics
same-date inconsistency in 3.2 is an unreconciled discrepancy, not proven invention), so the
hallucinated-source override is not applied.

## 4. Card Integrity (from `qa/gold_regen_qa1/lint_static/2026-07-20.csv`, copied verbatim)

| card_id | strategy | flags | dud | per-card score |
|---|---|---|---|---|
| 2026-07-20_Trade_1 | Trade 1 — Daily Directional (SHORT — regime bias bearish, conviction −0.51) | WARN_R_TINY(0.19xATR) | False | 100 − 10×1 = 90 |
| 2026-07-20_Trade_2 | Trade 2 — Pivot (regime-aware) | SUPPRESSED | False | n/a — suppressed, excluded from the mean |
| 2026-07-20_Trade_3C | Trade 3C — Momentum-Breakout. TRANSITION regime | UNPRICED | True | 100 − 40×1 = 60 |

```
card_integrity = mean(90, 60) = 75
n_cards = 3
n_duds = 1
n_warns = 1
```

## Score lines

c1=2
c2=4
c3=2
c4=4
c5=3
total=62
band=Moderate
override=restriction_breach
card_integrity=75
n_cards=3
n_duds=1
n_warns=1
