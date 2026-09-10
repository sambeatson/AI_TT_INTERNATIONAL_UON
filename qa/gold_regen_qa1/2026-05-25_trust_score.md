# Trust Score — XAUUSD Gold Report, 25 May 2026 (`gold_regen_qa1`)

Report: `reports/md/Gold_Report_25-May-2026.md` · Level file: `data/levels/XAUUSD_by_date/2026-05-25.csv`
(`last_bar_date`=2026-05-22 < D=2026-05-25 — leak-free, confirmed) · Cards:
`cards/baseline/gold/by_date/2026-05-25.json` · Linter: `qa/gold_regen_qa1/lint_static/2026-05-25.csv`

Basis used for Category 3 checks: **`_full`** (report states "Spot, immediate settlement, loco London" /
"Spot, loco London, continuous" throughout §2–§3, so per brief §4 the `_full` columns apply).
`atr14_full` = 98.6457.

## 1. Section 7 checklist

| Row | What was checked | Evidence location | Notes / evidence observed | Score (0–5) |
|---|---|---|---|---|
| 1.1 Variables respected | Asset=XAU/USD spot, not GC futures (futures corroboration-only, not used) ✓; USDX first counter in §10 ✓; lookback 5/25 stated ✓; USD/oz ✓; 6 independent sources in §4 (exactly the minimum) ✓; tick=0.01 stated in §2 but **used inconsistently**: card states R=$79 as "790 ticks" (should be 7,900 ticks at $0.01) and the 3×ATR runner distance $257 as "2,576 ticks" (should be 25,700) — a systematic 10× error, applied twice. **As-of session also wrong** for the daily/weekly pivot builds (see 1.2/3.4) | §2, §10, §4, §21b | Core variables (asset/unit/lookback/source-count) are respected; tick-unit consistency and the pivot as-of date are not | 3 |
| 1.2 Coverage & currency consistent | §1/§3/§4/§6 all correctly anchor to 22 May (D−1) close. **§11 does not**: daily pivots are computed from 21 May (H 4,548/L 4,488/C 4,535) instead of 22 May, the actual last completed session before D; weekly pivots from 11–15 May instead of the last completed week 18–22 May (`w_full_period`=2026-W21 in the level file). This is an undisclosed date drift within the same report | §11 vs §6/level file | Two of three pivot tables are keyed to the wrong period, with no flag that a different, earlier session/week was substituted | 2 |
| 1.3 Audience & tone | Senior Commodities Analyst — Precious Metals register held throughout; institutional trading-desk language; no retail tone | §1, §18 | Consistent, no issues | 5 |
| 2.1 Sections present & ordered | All 21 sections present in order, incl. 13a–13d and 21a–21d as separate subsections; §17 is one sentence | headings | Full structural compliance | 5 |
| 2.2 Scorecard as table | §6 is a proper table with the required Session/O/H/L/C/RSI2/Source A/Source B/Validation columns ✓. §11 pivot tables are real tables but list **five** levels each side (R5…S5) rather than the three (R3→P→S3) the spec calls for — extra granularity, nothing lost, but a spec deviation | §6, §11 | Format correct; row-count spec not followed | 4 |
| 2.3 Method steps visible | §4→§5 show observation→normalisation→consensus (normalisation correctly stated as not needed this run); §8 is genuine candle-by-candle; §9 gives persistence/overlap/VOLator with numeric readings; charts present as captions only (accepted per brief — .md conversion drops images) | §4–§9 | Strong, transparent method trail | 5 |
| 3.1 Quantitative claims sourced | §1 figures point to §3/§5/§21a; §13-derived figures cite specific dated articles. Minor gap: counter-asset levels quoted in §10/§12 (DXY ~99.3, S&P ~7,473, DAX ~24,500) carry no dated citation of their own (no §4-style evidence row for the counters) | §1, §12, §14 | Mostly sourced, non-material gaps on counter-asset figures | 4 |
| 3.2 Citations exist & contain data | Spot-checked: Investing.com, FXEmpire, Trading Economics (all named, dated 22 May, each quotes a specific figure used elsewhere). One minor internal inconsistency: §4 cites Investing.com's own "prior close" as $4,543.29, but §6 (which also names Investing.com as Source A for 21 May) states the 21 May close as $4,535 — an $8.29 gap between two uses of the same source for what should be the same value. Not severe enough to read as fabrication (same order of magnitude as ordinary feed-snapshot noise), but worth noting | §4, §6, §13a | No fabricated source found; one small same-source internal inconsistency | 4 |
| 3.3 Calculations transparent | RSI2 reproduces exactly from the report's own five stated closes (verified: RS=1.2 → RSI2=54.55≈54.5). Sentiment tilt shown with full numerator/denominator (§13b). Pivot arithmetic (P/R/S) is internally consistent with the H/L/C each table states. Gap: ATR14 and KER are never stated as explicit numbers in the body text (only implied, e.g. "86-tick ATR" in a caveat, itself ambiguous against tick=0.01 convention) | §6, §11, §9, §13b, §21a | Reproducible where shown; ATR14/KER not stated numerically | 4 |
| 3.4 Numbers reconcile — incl. against the level file | **Major failure.** D−1 OHLC itself reconciles cleanly (close diff $3.27, open $0.05, high $6.96, low $0.01 — all within tolerance) and RSI2 reproduces internally, but it diverges sharply from `rsi2_full`=0.0 in the level file (diff 54.5, threshold for failure is >15). Far more seriously: **all three §11 pivot tables fail reconciliation on most levels.** Daily: R1/R2/R3/S1 all exceed the failure threshold (diffs $14.7–$27.5 against a $11.34 cap); only P/S2/S3 land inside tolerance. Weekly: **every level fails**, off by $123–$142 (>10× the $11.34 cap) — a consequence of using the wrong prior week. Monthly: despite naming the *same* calendar month (April 2026) as the level file, R1/R2/R3/S1/S2/S3 all fail (diffs $62–$318), even though the pivot point P itself is close ($6.24 diff) — meaning the report's stated April H $4,773.8 / L $4,585 do not match the executed range behind the level file, independent of any period-selection error. This cascades into the cards: Trade 1's TP1 "confluence" cites weekly S3 = $4,432 (file's true `w_full_S3` = $4,308.52, off by $123) and daily S3 = $4,439 (file's `d_full_S3` = $4,429.78, inside tolerance) | §11, cards §21b, level file | Systemic reconciliation failure across the pivot complex; this is the report's dominant accuracy defect | 0 |
| 4.1 Each pillar reaches a conclusion | §8 "Judgement label: Indecision" ✓; §9 explicit regime label ✓; §10 "CONFIRM" ✓; §12 each subsection ends with a "Direction:" tag ✓. §14 (Macro) has no equivalent single closing direction label. Also scored here (per brief, card construction is scored under Cat. 4): Trade 1's stop-rationale sentence is self-contradictory — it names "5-day swing high $4,580 + 0.25×ATR buffer" and, in the same cell, "the tighter nearest-resistance anchor at $4,568 + buffer," neither of which arithmetically produces the stated $4,589 stop, and $4,568 matches no level in the report's own (wrong-session) §11 daily table — though it is almost exactly the level file's correct `d_full_R2`=4,568.96, suggesting §21's engine used the correct 22 May pivots while §11's displayed table did not | §14; cards §21b | One pillar lacks an explicit closing label; card stop-rationale internally inconsistent | 3 |
| 4.2 Peer/cross-asset interpreted | §10 gives a stated mechanism per counter (real-yield channel, risk-appetite channel, high-beta metal channel), not a bare correlation list | §10 | Clear mechanistic reasoning | 5 |
| 4.3 Synthesis reconciles tensions | §9 explicitly reconciles the Kaufman-vs-overlap/persistence conflict into "Transitional"; §16 addresses both invalidation directions; §21a confirms §17-vs-§21a agreement. Good reconciliation, though it never addresses the tension between its own confident SHORT conviction and the internal pivot-table inconsistencies noted above | §9, §15–§18, §21a | Sound reconciliation of the tensions it recognises | 4 |
| 4.4 Calibrated language | §17 is exactly one sentence; §3 states confidence = Medium explicitly; hedged language used appropriately elsewhere | §3, §17 | Compliant | 5 |
| 5.1 Data dated; staleness flagged | Every price/article carries a date; §11 flags pivot inputs SINGLE-SOURCE INDICATIVE. **But the report never flags that its daily/weekly pivot tables use an older session/week than the true D−1 session/week** — this staleness is presented flatly ("prior session 21 May") with no caveat that a more recent session (22 May) was available and should have been used | §11, §19 | Undisclosed staleness in the pivot inputs | 2 |
| 5.2 Assumptions up front | Futures-to-spot normalisation stated as not needed (with reasoning); anchor override stated on the card, in §2, and in §20 Agent Log — correctly logged as a non-conformance, not silently presented as the instance anchor; single-source pivot propagation into §21 caveats stated. Gap: the wrong-period substitution in §11 is not itself disclosed as an assumption or limitation | §21b, §19, §20 | Anchor-override handling is compliant and well-documented; the pivot-period substitution is not similarly disclosed | 4 |
| 5.3 Red flags surfaced | §12/§15 risks are substantive; §13d's 28 May GDP/claims collision is explicitly carried into the Trade 1 card caveat | §12, §15, §21b | Compliant | 5 |
| 5.4 Restrictions honoured | No bracketed variable names or module codes (M1…M5) or framework name found in the report body; instrument common names used throughout; futures used corroboration-only as stated | whole report | No restriction breach found | 5 |

## 2. Category roll-up

| Cat | Rows averaged | Mean | Level | Multiplier | Max | Points | One-line justification |
|---|---|---|---|---|---|---|---|
| C1 Prompt adherence | 1.1,1.2,1.3 = 3,2,5 | 3.33 | **3** | 0.65 | 20 | 13.00 | Core variables respected; tick-unit math and pivot as-of date are not |
| C2 Structure | 2.1,2.2,2.3 = 5,4,5 | 4.67 | **5** | 1.00 | 20 | 20.00 | All 21 sections present/ordered; scorecard tables correct; pivot tables carry extra (not missing) rows |
| C3 Accuracy & evidence | 3.1,3.2,3.3,3.4 = 4,4,4,0 | 3.00 | **3** | 0.65 | 25 | 16.25 | Sourcing/citations/RSI2 arithmetic are sound; the §11 pivot complex fails reconciliation against the level file almost everywhere |
| C4 Reasoning & judgment | 4.1,4.2,4.3,4.4 = 3,5,4,5 | 4.25 | **4** | 0.85 | 20 | 17.00 | Pillars mostly conclude and reconcile tensions well; card stop-rationale is internally inconsistent |
| C5 Currency & transparency | 5.1,5.2,5.3,5.4 = 2,4,5,5 | 4.00 | **4** | 0.85 | 15 | 12.75 | Dating/assumptions/red-flags/restrictions mostly strong; pivot-input staleness is undisclosed |

## 3. Total, band, override

**Total = 13.00 + 20.00 + 16.25 + 17.00 + 12.75 = 79 (rounded)**
**Band = High Trust (75–89)**
**Override check:** No fabricated/hallucinated source identified (three spot-checked citations are named, dated, and — with one minor exception noted at 3.2 — internally consistent) → hallucinated_source override does NOT apply. No explicit prompt-stated restriction is openly violated; the daily-open anchor override is logged as a non-conformance exactly as the module requires → restriction_breach override does NOT apply.
**Override = none.**

## 4. Card Integrity (from `lint_static/2026-05-25.csv`, copied verbatim)

| card_id | strategy | flags | dud | Card Integrity (100−40·DUD−10·WARN) |
|---|---|---|---|---|
| 2026-05-25_Trade_1 | Trade 1 — Daily Directional | CLEAN | False | 100 |
| 2026-05-25_Trade_2 | Trade 2 — Pivot (TRANSITION regime) | SUPPRESSED | False | — (suppressed, excluded from mean) |
| 2026-05-25_Trade_3C | Trade 3C — Momentum-Breakout | SUPPRESSED | False | — (suppressed, excluded from mean) |

Report-level Card Integrity = mean over non-suppressed cards = mean(100) = **100**.

## Score line

```
c1=3
c2=5
c3=3
c4=4
c5=4
total=79
band=High Trust
override=none
card_integrity=100
n_cards=3
n_duds=0
n_warns=0
```
