# Trust Score — Gold_Report_21Jul2026.md (D = 2026-07-21, run gold_regen_qa1)

Basis claimed by the report: "XAU/USD spot (loco London)" / "Spot, immediate settlement (loco London)"
→ checked against `_full` columns of `data/levels/XAUUSD_by_date/2026-07-21.csv`
(`last_bar_date` = 2026-07-20 < 2026-07-21 — leak-free, confirmed). Cross-checked against `_cash` where noted.

## 1. Section 7 checklist

| Row | Notes | Evidence | Score |
|---|---|---|---|
| 1.1 Variables respected | Asset/basis/unit correct (§2); USDX first counter (§10); as-of = 20 Jul close (correct, D−1); 5d/25d lookback correct; 6 independent sources used (§4, meets ≥6 minimum). Gaps: §2 declares CME GC=F "for corroboration" but no futures quote appears anywhere in the report — the variable is declared but never exercised. Tick size/name is never stated explicitly (only inferred as $0.01/tick from the card figures). The one place ticks are cross-referenced is internally wrong: Trade 1 stop cell says "4,201 ticks above entry" while the Risk cell says "$42.10 (4,210 ticks)" for the same distance — a 9-tick self-contradiction. | §2, §4, §10, §21b | 3 |
| 1.2 Coverage & currency consistent | All dated items in §2/§6/§13/§21 are D−1 or earlier for data, D for the session; §13d (upcoming calendar) is correctly forward-dated as a calendar, not evidence. No USD/oz vs "points" drift. | whole report | 5 |
| 1.3 Audience & tone | Consistent institutional register throughout, no retail tone. | §1, §18 | 5 |
| 2.1 Sections present & ordered | All of §1–§21 present in the specified order, including 13a–13d and 21a–21d. | headings | 5 |
| 2.2 Scorecard as a table | §6 is a proper table (adds a Trend column, harmless). §11 weekly table matches the R3→P→S3 spec exactly. Daily table is R5→S5 (5 levels/side, superset of spec — not a defect). Monthly table shows only R2→P→S2 (2 levels/side) — **misses the required R3/S3 outer band**. | §6, §11 | 4 |
| 2.3 Method steps visible | §4→§5 show observation→normalisation→consensus with method stated; §8 is candle-by-candle; §9 states overlap/persistence/VOLator/KER; §7 gives captions only (docx→md image drop) — accepted per brief, not scored. | §4–§9 | 5 |
| 3.1 Quantitative claims sourced | Most §1/§12/§14 figures trace to §4/§6/§13. Central-bank buying figures in §12 ("PBoC +7t, India +0.3t") carry no source at all; US 10Y ~4.60% is repeated several times without a source tag. | §12 | 3 |
| 3.2 Citations exist & contain data | Spot-checked 3: Investing.com (20 Jul, 4,003.79; its own note "prev close 4,017.60" matches §6's Fri close exactly — consistent). TradingView (20 Jul, 4,020.93 — used only as one of six reads, consistent). Trading Economics: §4 gives its 20 Jul quote as 4,007.72 (CFD ref) while §13a quotes the *same outlet, same date* as "Gold hovered around $4,030 an ounce on Monday" — a ~$22 unreconciled gap between two uses of one source on one day. Not clearly impossible/fabricated (could be different times of day), so no override triggered, but it is a real internal-consistency gap in a spot-checked source. | §4, §13a | 3 |
| 3.3 Calculations transparent | RSI2 reproduces from the report's own 5 stated closes: using 3988.40→4017.60→4008.30, avg gain 14.60 / avg loss 4.65, RS=3.140, RSI2=75.85 ≈ the stated 75.8 — passes. Daily pivots reproduce exactly from the report's own stated H/L/C (P=4009.60, R1=4029.20, S1=3988.70, R2=4050.10, S2=3969.10, R3=4069.70, S3=3948.20 all recompute exactly via standard floor-pivot formulas) — passes. ATR14 is never stated as a number; it is only inferable from "3×ATR(14)≈$164" ⇒ ATR≈$54.67, and (see 3.4) that figure is far from the true ATR14 on either basis. KER is stated as a value (−0.77) and classification but its parameters (period 13, EMA 3) are never stated. | §6, §11, §9, §21 | 3 |
| 3.4 Numbers reconcile — internally and against the level file | Internal: D−1 close 4008.30 consistent across §1/§3/§4/§6; §11 pivots match the cards (Trade 1 stop = daily R2 4050.10 ✓; Trade 2 entry = daily R1 4029.20 ✓); Trade 2's TP2 cell ($3,987.40) doesn't match its own cited confluence (daily S1 $3,988.7, a $1.3 gap). External, against the level file (`_full`, ATR14=92.6614): **Close 4008.30 vs 4007.64 → diff 0.66, consistent. Low 3990.00 vs 3982.78 → diff 7.22, consistent. Open 4017.60 vs 4001.21 → diff 16.39, discrepancy. High 4030.50 vs 4040.67 → diff 10.17, discrepancy. RSI2 75.8 vs 81.8777 → diff 6.08, discrepancy.** Daily pivots: P (diff 0.76) and R1/S1 (diff 8.75 / 8.64) are consistent/discrepancy, but **R2 (diff 18.15), S2 (diff 16.63), R3 (diff 26.14) and S3 (diff 26.03) are all FAILURE-tier** (>0.115×ATR14=10.66) — the small H/L error compounds through the (H−L)-scaled outer pivots. Weekly pivots (from week of 13–17 Jul) are excellent: P/R1/S1/R2/S2/R3/S3 all within 0.12–2.60 of the file, all consistent. **Monthly pivots are largely FAILURE-tier**: P diff 13.09, R1 diff 24.95, S1 diff 35.44, S2 diff 23.58 (all >10.66); only R2 (diff 2.60) matches. **ATR14**: report's implied $54.67 vs file's $92.66 (full, 41.0% relative diff) or $74.14 (cash, 26.3% relative diff) — **fails the 25% relative tolerance under either basis**. **5-day swing high** used to justify the Trade 1 stop ("$4,078 swing high"): report's own 5-day-table max (4078.50) vs file's `swing_high_5d_full` 4103.17 → diff 24.67, **FAILURE-tier** (>0.20×ATR14=18.53). These are material, quantifiable misses, not just wording issues, and the ATR error directly produces a mischaracterised card (see 4.x, Feedback). | cross-section + level file | 1 |
| 4.1 Pillars conclude | §8 → "Range — with downside bias"; §9 → "Bias: Bearish"; §10 → aggregate "MIXED"; §12 subsections each end in a directional label. §14 ends on a conditional "watch item" framing rather than a crisp label, though the content is unambiguous. | those sections | 4 |
| 4.2 Peer/cross-asset interpreted | §10 states a mechanism per counter (USDX→FX cost/real yields; S&P→risk-off mechanism, flagged as contradicting; DAX→neutral; Silver→industrial-demand/ratio mechanism) — not a correlation list. | §10 | 5 |
| 4.3 Synthesis reconciles tensions | §16 explicitly resolves S&P/silver vs bearish synthesis ("the reason conviction is moderate rather than high"); §9 explicitly states KER takes precedence over the nested short-term range; §21a explicitly flags "Conflict flag: none" between §17 and the SHORT conviction. | §15–§18, §21a | 5 |
| 4.4 Calibrated language | §17 is exactly one sentence; §3 states Confidence: Medium; hedging is proportionate, not stacked. | §3, §17 | 5 |
| — Card construction (folds into C4 per brief §2) | Trade 1: SL-vs-Risk tick count self-contradicts (4,201 vs 4,210 ticks for the same distance); the U3 0.2R trail is given as *above* entry for a SHORT ($4,016.4 > $4,008 entry) — sign-inverted; the "Wide ATR-relative stop" caveat is not supported once the true ATR14 (92.66 full / 74.14 cash) is used — R=$42.10 is 0.45×ATR (full) / 0.57×ATR (cash), not wide; it only looks wide against the report's own erroneous ~$55 ATR. Trade 2: same U3 0.2R sign inversion ($4,033.4 above entry on a SHORT); TP2 vs its own cited confluence disagree by $1.3. Trade 3A: entry cell names three different candidate prices ($4,003.3 / $4,024.20 / "≈$4,020") without clearly resolving which is the entry; the validity caveat inverts its own question and answer (asks "magnitude ≈$74 > 2×ATR?" then answers with a conclusion that only follows if magnitude < 2×ATR); TP1 confluence ($3,991) vs the confluence row's own S1 figure ($3,988.7) disagree by $2.3. | cards/baseline/gold/by_date/2026-07-21.json, §21b | (feeds C4) |
| 5.1 Data dated; staleness flagged | All prices/articles dated. Daily H/L/C is flagged "CORROBORATED (two-source)". Monthly H/L/C is also flagged "CORROBORATED" with no caveat, yet (3.4) 4 of its 5 shown levels are FAILURE-tier against the leak-free file — the report is overconfident about a data point that does not, in fact, reconcile. | §4, §6, §11, §19 | 3 |
| 5.2 Assumptions up front | The daily-open anchor override is correctly flagged as a non-conformance (not silently presented as the anchor) in §2, on the Trade 1 card, and in §20's Agent Log/Anomalies — this is the compliant pattern the module asks for. But the module also requires "the same converted time" to appear in all three places, and **no clock time for the overridden anchor is given anywhere in the report** (only "the 21 Jul session open (overridden open anchor)"). GC=F normalisation: never used, so nothing to disclose (consistent, not a violation). | §21b, §19, §20 | 3 |
| 5.3 Red flags surfaced | §12/§15 carry the FOMC, Iran/Hormuz, and cross-asset-contradiction risks; §13d's FOMC collision is explicitly carried into the Trade 1 caveat ("holding period collides with 29 Jul FOMC"). | §12, §15, §21b | 5 |
| 5.4 Restrictions honoured | No bracketed variable names, module codes (M1–M5), or the framework name appear anywhere in the report body (checked). Retail FX-broker quotes explicitly excluded per source restrictions (§4 footnote). Futures corroboration-only is honoured by not using it at all. The one soft gap: the "3×ATR(14)≈$164" cap is presented as a rule output with no shown derivation, and (3.4) does not reconcile with any OHLC-derived ATR in the report — borderline unstated synthesis rather than an openly-breached restriction. | whole report | 4 |

## 2. Category roll-up

| Cat | Rows averaged | Level (0–5) | Multiplier | Points (/max) | Justification |
|---|---|---|---|---|---|
| C1 Prompt adherence | 1.1=3, 1.2=5, 1.3=5 → mean 4.33 | **4** | 0.85 | 17.00 / 20 | Correct asset/coverage/sources/units, but tick size never stated and the one tick cross-check self-contradicts; a declared corroboration variable (GC=F) is never used. |
| C2 Structure | 2.1=5, 2.2=4, 2.3=5 → mean 4.67 | **5** | 1.00 | 20.00 / 20 | All sections present and ordered; only gap is the monthly pivot table showing 2 levels/side instead of 3. |
| C3 Accuracy & evidence | 3.1=3, 3.2=3, 3.3=3, 3.4=1 → mean 2.5 | **3** | 0.65 | 16.25 / 25 | RSI2 and daily pivots are internally reproducible and daily P/R1/S1 and all weekly pivots reconcile well, but ATR14, the 5-day swing high, daily R2/S2/R3/S3, and 4 of 5 shown monthly pivots are all FAILURE-tier against the leak-free level file. |
| C4 Reasoning & judgment | 4.1=4, 4.2=5, 4.3=5, 4.4=5 → mean 4.75, pulled down for card construction | **4** | 0.85 | 17.00 / 20 | Strong synthesis and cross-asset mechanism, but card construction carries a sign-inverted 0.2R trail rule on two of three cards, an unresolved multi-price entry on Trade 3A, and a "wide stop" caveat that the true ATR does not support. |
| C5 Currency & transparency | 5.1=3, 5.2=3, 5.3=5, 5.4=4 → mean 3.75 | **4** | 0.85 | 12.75 / 15 | Red flags and event-collision caveats are well surfaced; the anchor override is correctly logged as a non-conformance but never given a clock time, and "CORROBORATED" is applied to monthly pivots that don't externally reconcile. |

## 3. Total, band, override

- **Total = 17.00 + 20.00 + 16.25 + 17.00 + 12.75 = 83** (rounded to whole number)
- **Band = High Trust (75–89)**
- **Override check:** No source spot-checked was impossible/fabricated (the Trading Economics internal gap is a discrepancy, not a fabrication) → hallucinated-source override does not apply. No prompt restriction is openly breached (no module/bracket leakage; anchor override is logged, not hidden) → restriction-breach override does not apply.
- **override = none**

```
c1=4
c2=5
c3=3
c4=4
c5=4
total=83
band=High
override=none
card_integrity=96.67
n_cards=3
n_duds=0
n_warns=1
```

## 4. Card Integrity (linter rows, copied verbatim from `qa/gold_regen_qa1/lint_static/2026-07-21.csv`)

| card_id | strategy | flags | dud | Card Integrity |
|---|---|---|---|---|
| 2026-07-21_Trade_1 | Trade 1 — Daily Directional (SHORT — bearish regime, conviction −0.71) | CLEAN | False | 100 |
| 2026-07-21_Trade_2 | Trade 2 — Pivot (regime-aware, TREND branch: sell rallies to resistance) | WARN_R_TINY(0.23xATR) | False | 100 − 10 = 90 |
| 2026-07-21_Trade_3A | Trade 3A — Momentum-Pullback (regime = TREND_DOWN → 3A active) | CLEAN | False | 100 |

Report-level Card Integrity = mean(100, 90, 100) = **96.67**. n_cards = 3, n_duds = 0, n_warns = 1.
(The WARN_R_TINY(0.23×ATR) on Trade 2 is consistent with the level file: R=$20.90 / ATR14_full $92.6614 = 0.226×ATR, under the 0.3×ATR WARN threshold.)
