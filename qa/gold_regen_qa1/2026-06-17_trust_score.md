# Trust Score — XAUUSD Gold Report, 17 June 2026

Run: `gold_regen_qa1` · Report: `reports/md/Gold_Report_17-Jun-2026.md` · Level file:
`data/levels/XAUUSD_by_date/2026-06-17.csv` (last_bar_date 2026-06-16 < 2026-06-17, leak-free — confirmed).
Report's stated basis: "Spot XAU/USD (loco London)" / "OTC London spot" → checked against level file
`_full` columns per REVIEWER_BRIEF §4.

## 1. Section 7 checklist

| Row | Reviewer notes | Evidence observed | Score (0–5) |
|---|---|---|---|
| 1.1 Variables respected | Asset correctly framed as spot XAU/USD (LBMA loco-London), GC=F correctly labelled "corroboration instrument" not the priced asset. USDX is the first cross-asset counter (§10). ≥6 independent sources present (§4, "six independent observations"). Lookback 5/25 stated (§2). Unit USD/oz stated. **Gap:** tick size/name is never declared as a field in §2's Market Definition table even though it is required ("Required when PRODUCE_STRATEGY_RECOMMENDATIONS = YES") and §21 does produce strategy cards; a $0.01 tick is only inferable from the card ticks-math, never stated up front. | §2, §4, §10, §21b | 4 |
| 1.2 Coverage & currency consistent | §2's "As-of date" field is stated as **17 June 2026** (= D), but M1_Variables_v2_1 fixes as-of to "the last completed regular session…that closed strictly before the report date" (= 16 June 2026 here). Every other section (§3, §4, §6, §19) correctly anchors to the 16-Jun close, so this reads as a field-labelling slip rather than an actual same-day data leak, but it is a concrete, locatable inconsistency in a foundational field. No USD/oz-vs-tick unit drift found elsewhere. | §2 vs §3/§4/§6/§19 | 3 |
| 1.3 Audience & tone | "Senior Commodities Analyst — Precious Metals" stated in the masthead; institutional register throughout, no retail tone. | masthead, §1, §18 | 5 |
| 2.1 Sections present & ordered | All 21 sections present, correctly ordered, including §13a–d and §21a–d. §17 is a single (compound) sentence. | headings | 5 |
| 2.2 Scorecard as a table | §6 table has the required columns (plus an extra Trend column). §11's **Weekly and Monthly** pivot tables correctly show 3 levels/side (R3→P→S3) as the checklist specifies, but the **Daily** table shows 5 levels/side (R5…S5) — an internal formatting inconsistency against the checklist's own "three levels each side" spec, applied inconsistently within one report. | §6, §11 | 3 |
| 2.3 Method steps visible | §4–§5 show observation→normalisation→consensus and §8/§9 are fully candle-by-candle / regime-with-persistence. **Gap:** the masthead claims "GC=F corroboration" but no GC=F futures price, and no stated futures-to-spot normalisation size, appears anywhere in §4, §5 or §19 — the claimed corroboration instrument is never actually evidenced. Charts are captions/placeholders only (accepted per brief, not scored). | §4–§9 | 3 |
| 3.1 Quantitative claims sourced | Most §1/§12/§14 figures trace to §4/§6/§13. **Gap:** §12's "Indian investment demand (40–45%)" and PBoC/RBI accumulation claims carry no source/date pointer. | §12 | 4 |
| 3.2 Citations exist & contain data | Spot-checked TradingEconomics, Investing.com, CSFX Research (§4/§13a): all named and dated. TradingEconomics/Investing.com close figures are used consistently elsewhere (§3, §6). CSFX Research is cited twice for 11-Jun with two different implied figures ($4,083.74 in §4 "base-test session reference" vs "Fib base at $4,024" in §13a) — not impossible/self-contradictory enough to be fabricated, but a real internal-consistency weakness. Bloomberg's entry states its own level was "not machine-extracted," i.e. asserted rather than verified. No fabrication found — no override triggered. | §4, §13a | 3 |
| 3.3 Calculations transparent | RSI2 reproduces exactly from the report's own 5-day close sequence (verified: 15–16 Jun both up days ⇒ RSI2=100). Daily pivots reproduce exactly from the report's own stated 16-Jun H/L/C using the standard formulas (verified P/R1/S1/R2/S2/R3/S3 all match to the cent). **Gaps:** ATR14 is never stated as a number anywhere in the report, though it is used operationally (Trade 1's "3×ATR cap", the general 0.25×ATR/3.5×ATR stop rules) — this cannot be checked or reproduced by a reader. KER value is not stated numerically, only classified qualitatively. §21a's score walkthrough shows only 3 of 6 weighted terms explicitly (+0.25, +0.04, +0.00 = 0.29) against a stated total of +0.34; the remaining +0.05 (medium-regime + Kaufman) is left as "near-zero," not itemised — the total does not fully reconcile from the numbers shown. | §6, §11 (pass); §9, §21a (fail) | 2 |
| 3.4 Numbers reconcile — internal + level file | **Internal:** D-1 close ($4,340.00) identical across §1/§3/§4/§6/§21b. §11 daily pivots = pivots quoted on all three cards, exactly. ATR in §9 vs §21 cannot be checked (never stated — see 3.3). **External vs level file (`_full`, since report claims loco-London/continuous):** D-1 close $4,340.00 vs file $4,331.26 → diff $8.74 (discrepancy band, 0.04–0.115×ATR14). D-1 open/high/low all within tolerance (diffs $1.96/$5.38/$0.18). Daily pivots P/R1/R2/R3 within tolerance; daily S1/S2/S3 in the discrepancy band (diffs $7.74/$6.74/$13.30). **Weekly pivots (prior W/E 12-Jun) and Monthly pivots (May) are both severely wrong** — every one of the 7 weekly levels and 7 monthly levels exceeds the Category-3 failure threshold (>0.115×ATR14 ≈ $13.50) by margins of $28–$338 (see feedback doc for full table and compliant values). This is a genuine, systemic Category-3 failure on two of the three pivot timeframes, materially understated by the report's generic "indicative" caveat. | cross-section + level file | 1 |
| 4.1 Pillars conclude | §8, §9, §10, §12, §14 each end in a clear, consistent direction/label. | those sections | 5 |
| 4.2 Peer/cross-asset interpreted | §10 gives a mechanism for each counter (USDX cost-of-carry for non-USD buyers, S&P/DAX risk-on competing-for-flow, Silver sector-beta) — not a bare correlation list. | §10 | 5 |
| 4.3 Synthesis reconciles tensions | §16 explicitly reconciles short- vs medium-term reads; §18 reconciles the equity-strength/haven-thesis tension from §10; §21a explicitly flags and retains-unchanged the §17-vs-§21a tension ("the §17 forecast is two-sided…while the score leans long — both outputs retained unchanged"). | §15–§18, §21a | 5 |
| 4.4 Calibrated language | §17 is one (compound) sentence, no hedge-stacking; confidence (Medium) stated in §1/§3. Minor: the "but" clause folds two conditional scenarios into a single sentence, stylistically borderline. | §3, §17 | 4 |
| 4.5 Card construction (M5 conformance — brief §3, scored under Category 4) | **Trade 1:** stop buffer far tighter than the M5 rule. Nearest structural anchor is the report's own 16-Jun low ($4,306.10); a compliant stop = anchor − 0.25×ATR14 ≈ $4,306.10 − $29.32(full ATR) = $4,276.78 (R ≥ ~$63), not the stated $4,303 (R=$37, only a ~$3.10 buffer). **Trade 2:** entry ("buy-limit at daily P $4,331.90") matches none of the three regime-conditioned M5 formulas — not RANGE (limit at S1/S1.5/S2), not TREND (entry = P+0.10×(R1−P) = $4,334.48), and not TRANSITION (breakout side only, which is the report's own regime call in §9). **Trade 3A:** built as a breakout stop-entry above the 16-Jun high, but M5's 3A is specified as a 57.5%-retracement pullback entry into a qualifying logged swing with stop beyond the 0% anchor by 0.25×ATR — a different methodology entirely. TP2 ($4,425) is mislabelled "≈+2.3R" when it is exactly +2.00R against the card's own $37 R. Card Integrity (linter, static-only) is CLEAN for all three cards, but none of the three fully follows its specified M5 construction formula. | §21b vs modules/M5_Strategies_Module_v2_1.md + level file | 1 |
| 5.1 Data dated; staleness flagged | Every price/article row in §4, §6, §13 is dated. Single-source O/H/L (10-Jun, 12-Jun) explicitly flagged SINGLE-SRC in §6/§19. Weekly/monthly pivots flagged "indicative," but the flag does not quantify how large the resulting error is (see 3.4). | §4, §6, §13, §19 | 4 |
| 5.2 Assumptions up front | Single-source pivot propagation is carried into all three trade-card caveats (good). **Gap:** the futures-to-spot normalisation implied by the masthead's "GC=F corroboration" is never stated with a size anywhere (no GC=F price shown at all) — this is exactly the row-5.2 failure mode the brief calls out ("the defect would be failing to state the normalisation"). No anchor override occurred (00:00 UK applied consistently, §20), so that sub-item is compliant by default. | §21b, §19, §20 | 2 |
| 5.3 Red flags surfaced | FOMC event risk, Iran-deal fragility, and the equity-rotation-competing-for-flow risk are all surfaced in §12/§15; the 17-Jun FOMC collision is carried into all three card caveats. | §12, §15, §21b | 5 |
| 5.4 Restrictions honoured | No bracketed variable names or framework name found in the report body. **Violation:** §20 Agent Log states **"M5 trace: direction-score weights basis = DEFAULT…"** — an explicit internal module code (M5) exposed in the shipped report body, in direct breach of the "no module codes (M1..M5)…in the report body" restriction (M1_Variables_v2_1, Section H footnote; brief row 5.4). This is a restriction-breach override trigger. | §20 line "M5 trace:" | 1 |

## 2. Category roll-up

| Cat | Rows (mean) | Level (rounded) | Multiplier | Max | Points | Justification |
|---|---|---|---|---|---|---|
| C1 Prompt adherence | (4+3+5)/3 = 4.00 → **override applied: −1 level** | **3** | 0.65 | 20 | 13.00 | Mean level was 4; restriction-breach override (M5 code exposure, row 5.4) mandates Category 1 reduced ≥1 level. |
| C2 Structural alignment | (5+3+3)/3 = 3.67 | **4** | 0.85 | 20 | 17.00 | All sections present/ordered (5); daily-pivot level-count inconsistency and unevidenced futures-corroboration claim pull 2.2/2.3 down. |
| C3 Accuracy & evidence | (4+3+2+1)/4 = 2.50 | **2** | 0.40 | 25 | 10.00 | Rounded down from 2.5 given the severity of the 3.4 finding (7 weekly + 7 monthly pivot levels all exceed the failure threshold, by up to 25× tolerance) and the material 3.3 gap (ATR14 never stated, though used to size stops/caps). |
| C4 Reasoning & judgment | (5+5+5+4+1)/5 = 4.00 | **4** | 0.85 | 20 | 17.00 | Narrative reasoning (pillars, cross-asset mechanism, synthesis) is strong; pulled down by card-construction non-conformance across all three cards (4.5). |
| C5 Currency & transparency | (4+2+5+1)/4 = 3.00 | **3** | 0.65 | 15 | 9.75 | Red flags and single-source propagation are well handled; pulled down by the unstated futures normalisation (5.2) and the module-code restriction breach (5.4). |

**Total = 13.00 + 17.00 + 10.00 + 17.00 + 9.75 = 66.75 → rounds to 67**

## 3. Total, band, override

```
total = 67
band = Moderate Trust (60–74)
override = restriction_breach   (M5 module code exposed in §20 report body — see row 5.4)
```
Override effect: caps the band at Moderate Trust (60–74) and reduces Category 1 by ≥1 level — both already
reflected above (the unmodified total of 67 already falls inside the Moderate cap; C1 was reduced from
mean-level 4 to 3). No hallucinated-source override triggered — the three spot-checked citations (3.2) are
named, dated, and not self-contradictory to the point of fabrication.

## 4. Card Integrity (linter rows, copied verbatim from `qa/gold_regen_qa1/lint_static/2026-06-17.csv`)

| card_id | strategy | flags | dud | Card Integrity (100 − 40·DUD − 10·WARN) |
|---|---|---|---|---|
| 2026-06-17_Trade_1 | Trade 1 - Daily Directional | CLEAN | False | 100 |
| 2026-06-17_Trade_2 | Trade 2 - Pivot (regime-aware) | CLEAN | False | 100 |
| 2026-06-17_Trade_3A | Trade 3 - Regime-driven (fork: 3A Momentum-Pullback) | CLEAN | False | 100 |

Report-level Card Integrity = mean over non-suppressed cards = (100+100+100)/3 = **100**.

Note: Card Integrity (static linter) is separate from, and does not capture, the M5 construction-methodology
non-conformance documented under row 4.5 above — the linter checks stop-side/TP-order/R-bounds only, not
adherence to the specific regime-conditioned entry/stop formulas.

## 5. Explicit score lines

```
c1=3
c2=4
c3=2
c4=4
c5=3
total=67
band=Moderate Trust
override=restriction_breach
card_integrity=100
n_cards=3
n_duds=0
n_warns=0
```
