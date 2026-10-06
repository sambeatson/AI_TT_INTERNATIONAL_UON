# Trust Score v3.7 — FTSE 100 Daily Report, 04 June 2026 (run ftse_qa1)

Report: `reports/md/FTSE_EuroStoxx_Report_04Jun2026.md` · D = 2026-06-04 · D-1 = 2026-06-03
Level file check: `last_bar_date` = 2026-06-03 < D (leak-free, confirmed). Slice last bar 2026-06-03 22:45 broker.
Basis claimed by the report: FTSE 100 **cash index** (so compared to the `_cash` columns; `_full` shown for reference). Tolerances per brief §4 (close ≤5 pts, O/H/L ≤10 pts; close >15 pts or RSI2 not reproducing = Category 3 failure).

## Score line
```
c1=3
c2=4
c3=0
c4=3
c5=3
total=53
band=Low
override=hallucinated_source
card_integrity=100
n_cards=3
n_duds=0
n_warns=0
```
(Override note: the fabricated/self-contradictory-source test fires (C3 forced to 0, cap Low 40–59). A restriction breach (no synthesised price presented as sourced; Trade 1 produced against the suppression rule) is also indicated, so C1 is reduced one level 4→3. The `override=` field carries the stricter cap.)

## 1. Section 7 checklist

| Row | Reviewer notes | Evidence (location) | Score |
|---|---|---|---|
| 1.1 Variables respected | Asset = FTSE 100 cash (correct; STOXX 50 reference only, no cards). Counters USDX / S&P 500 / DAX 40 / STOXX 50 (+VIX in §14). As-of 03 Jun close, Europe/London, 5-day lookback, GBP/pts all respected. **Daily-open anchor overridden to 00:00 UK** instead of 07:00 UK (disclosed, attributed to a "run instruction"). Sources are mostly aggregators/media (Yahoo, TE, Investing, CNBC, T. Rowe); only LSE/FTSE Russell is index-provider tier; "corroboration leniency" relaxes the validation standard. | §2 italic note, §4, §20 last bullet, §21b Trade 1 | 3 |
| 1.2 Coverage & currency consistent | Data dates are ≤ D-1 throughout; GBP/index points consistent. Drift: D is itself a Thursday yet §1/§12/§13d speak of "Thursday's … communications" / "Thu (wk)" as if a future date; §21c lists the 04 Jun (D) session as a "t−1" backtest row (off-by-one labelling: 03 Jun is D-1 yet labelled t−2). | §1, §13d, §21c | 4 |
| 1.3 Audience & tone | Professional strategist register, no retail tone. Minor leakage of engine jargon ("per the run instruction", "weight-lock counter", "v2.1 baseline") into the body. | §19–§21 | 4 |
| 2.1 Sections present & ordered | §1–§21 all present, in order; §13a/b/c/d; §21a/b/c/d present; §17 is one sentence. §7 has five caption-only chart placeholders (images dropped by pandoc — accepted). | headings | 5 |
| 2.2 Scorecard table; pivot tables | §6 is a proper table with all required columns (FTSE and STOXX). §11 has daily (R5→S5, five levels each side rather than three) and weekly (R3→S3) tables; **monthly pivot table is missing entirely**. | §6, §11 | 3 |
| 2.3 Method steps visible | §4→§5 observation→classification→consensus is shown, but the "weighted-median" has no weights/numbers. §8 is candle-by-candle with a sequence call; §9 gives overlap/persistence/VOLator (approximate, "~"). Charts: captions only. | §4–§9 | 4 |
| 3.1 Quantitative claims sourced | Oil "<$100", tariff "up to 12.5% on ~60 partners", "PCE highest in ~3 yrs", S&P "~7,554 from 7,610", VIX "~16", DAX 24,901 carry no named, dated source; ATR "≈285 pts" has no ATR value. | §1, §10, §12, §14, §21b | 3 |
| 3.2 Spot-checked citations exist and contain the data | **Fail** — see "Citation spot-check" below (3 of 3 inspected sources self-contradictory or impossible). Triggers hallucination override. | §4, §13a | 0 |
| 3.3 Calculations transparent | RSI2 is reproducible from the report's own closes (100.0 / 72.4 / 0.0 confirmed with `--closes`). Daily pivot arithmetic is internally correct for the stated 03 Jun H/L/C. Sentiment tilt shown and correct (Σw·s = −1.0, Σw = 3.9, −0.26). **ATR(14) is never stated as a number** (only implied by "3×ATR ≈285" → ATR ≈95). KER value not given in §9 (only "weakly positive"; +0.49 appears first in §21a). §21a score: sixth (VOLator, w=0.10) signal omitted; signal values do not follow the M5 §2a mapping (technical −0.50 instead of −1/0/+1; Transition regime +0.30 instead of ±0.5; MIXED cross-asset −0.20 instead of ±0.3); "three highest contributors" lists five. Weekly pivots described as "from 25–29 May H/L/C" but back-solve exactly to 28–29 May only (H 10,362, L 10,250, C 10,339) — and L 10,250 is the very 28 May low the report says was "excluded from pivot inputs". | §6, §9, §11, §13b, §21a | 3 |
| 3.4 Numbers reconcile | D-1 close 10,354.43 consistent across §1/§3/§4/§6 (internally). Breaks: Daily S2 is 10,283 on Trade 2 TP3 and 10,282 on Trade 3A TP2 (table 10,282.6); Investing quote range low 10,409 vs §6 03 Jun low 10,354.43 (close outside the quoted range); TE "+0.37% to 10,378" and Yahoo "−0.18%" do not match the §6 closes (01 Jun 10,402 → 02 Jun 10,378 = −0.23%; 02 Jun → 03 Jun = −0.23%); Trade 1 "weekly S1 10,272 sits ~46 pts below TP-path" (it is 46 pts below *entry*; TP1 is 10,168); §21d Trade 1 "3/5 triggered, mean +0.43R" counts the open 04 Jun row as a trigger (closed triggers +0.6, +0.7 → mean +0.65) while Trade 2/3A exclude it; Trade 1 "TP1 hit ≈67%" with realised outcomes of +0.6R/+0.7R (both below +1R). **Against the slice: D-1 OHLC and four prior sessions fail by large margins (below).** | §4/§6/§13/§21 | 1 |
| 4.1 Pillars conclude | §8 "Exhaustion — reversal risk", §9 bias "Neutral-to-mildly-bullish", §10 aggregate "MIXED", §12 items each net-labelled but no overall §12 label, §14 items labelled with a closing watch item. Largely concluded. | §8–§14 | 4 |
| 4.2 Cross-asset mechanism | USD→GBP→FTSE overseas-earner translation, oil→Shell/BP weight, S&P beta, Continental peers all given with mechanism. "Firm dollar weakens GBP" is asserted, not evidenced. | §10, §12 | 4 |
| 4.3 Synthesis reconciles tensions | §8 vs §9, KER vs VOLator and §17 vs §21a are explicitly reconciled. But the strategy layer contradicts the synthesis: regime stated as Transitional (§9) yet Trade 2 is built as a RANGE fade and Trade 3 as 3A (trend); all three cards SHORT while conviction is NEUTRAL (−0.05) and cross-asset is MIXED; Trade 1 produced despite NEUTRAL. | §9, §21a, §21b | 3 |
| 4.4 Calibrated language | §17 exactly one sentence; confidence "Medium" stated in §3; low-conviction caveats carried. | §3, §17 | 4 |
| 4.5 Card construction (protocol: scored under C4) | Severe M5 non-compliance on all three cards (see §3 below and feedback): Trade 1 not suppressed under NEUTRAL, built as sell-stop not MARKET, 00:00 anchor, stop wider than the tighter-of rule, no wide-stop flag, no R/ATR print, invalidation inside the stop; Trade 2 wrong regime branch, TP ladder not ±1R/±2R, buffer wrong, invalidation 2 pts from stop; Trade 3A wrong variant (Transition→3C), non-qualifying swing (round-trip 10,354→10,462→10,354), entry at 38.2% not 57.5%, TP2 not at swing origin, stop buffer short; D-1 reference close and signed gap not printed on any card. | §21b | 1 |
| 5.1 Data dated; staleness flagged | Prices and most articles dated, 28 May open/low flagged indicative. Undated: "late May" (CNBC Europe), "Ongoing"/"Rolling" calendar rows, "Thu (wk)", "to 30 Apr / 03 Jun chart". The indicative flag is contradicted by "Corroborated (Δ≈0)" on rows that fail against the slice. | §4, §6, §13 | 3 |
| 5.2 Assumptions up front | Anchor override stated in §2, §20 and Trade 1; ATR/KER short-path caveat stated; weekly single-source flag propagated to cards. Anchor not stated on Trade 2 / 3A cards; the "run instruction" overrides (leniency, Trade 1 production) are not reproduced where the reader needs them. | §2, §19, §20, §21b | 4 |
| 5.3 Red flags surfaced | ECB/BoE collision carried into all three card caveats and §12/§15. But the event is mischaracterised (see Calendar below); US Initial Jobless Claims (HIGH, 13:30 UK on D) not mentioned; the data-quality red flag (opens equal prior closes) is not disclosed. | §12, §13d, §15 | 3 |
| 5.4 Restrictions honoured | **Breach.** (i) Opens of 29 May, 01 Jun and 02 Jun equal the prior close exactly (and the STOXX table repeats the pattern: 6,035 / 6,062 / 6,108) while labelled "Corroborated (Δ≈0)" — interpolated values presented as sourced, contradicting §19 "No price … was synthesised". (ii) Trade 1 issued with |score| 0.05 < 0.25 (M5 §2b / CONVICTION_THRESHOLD = 0.25 require a SUPPRESSED row). (iii) corroboration tolerance relaxed. No bracketed variable names, no M1–M5 codes in the body. | §6, §19, §20, §21b | 1 |

### Citation spot-check (row 3.2) — one from §4/Scorecard, one from §13a, one from §10/§13c
1. **Investing.com (UK100), 03 Jun** (§4): raw quote "Open 10,425.85; range 10,409–10,462" but the normalised column gives low 10,354 and §5 says it "corroborated the session envelope (10,354–10,462)"; the §6 close 10,354.43 lies *outside* the quoted range. Figure does not match its own quote.
2. **Trading Economics, 02 Jun** (§4, §13a): "10,378 (+0.37%)" implies a prior close of ≈10,339.7, which is the **29 May** close in §6; the §6 01 Jun close is 10,402 (so 02 Jun is −0.23%). The quote cannot be reconciled with the report's own table. Yahoo "10,354.43 (−0.18%)" has the same defect (−0.23% from 10,378).
3. **CNBC US, "31 May — S&P 500 closes at record to kick off June"** (§13a): 31 May 2026 is a Sunday (no US cash close); date impossible.
Per brief §2 row 3.2 a source that is self-contradictory/impossible counts as fabricated → hallucinated-source override.

## 2. Category 3 data checks against the level file (cash basis; `_full` in brackets)

**D-1 = 03 Jun 2026**

| Field | Report | Level file cash [full] | Δ (report − cash) | Verdict |
|---|---|---|---|---|
| Open | 10,425.85 | 10,351.4 [10,390.8] | +74.5 | FAIL (>10) |
| High | 10,462.22 | 10,384.0 [10,392.6] | +78.2 | FAIL (>10) |
| Low | 10,354.43 | 10,320.7 [10,305.8] | +33.7 | FAIL (>10) |
| Close | 10,354.43 | 10,341.7 [10,305.8] | +12.7 | Outside ±5; within 15 (note only). Does not match the full-day basis either (+48.6) |
| RSI2 | 0.0 | 60.12 | −60.1 | FAIL (follows from the wrong closes; arithmetic itself reproduces) |
| ATR14 | not stated; implied ≈95 (3×ATR≈285) | 110.43 [132.83] | ≈−15 (−14%) | Not stated; implied value low |

Note: the report's 03 Jun high 10,462.22 matches the **29 May** cash high (10,462.0), not 03 Jun.

**Earlier rows in the §6 five-day table** (report − cash)

| Date | Open Δ | High Δ | Low Δ | Close Δ | RSI2 report / slice |
|---|---|---|---|---|---|
| 28 May | −104.1 (10,330 vs 10,434.1) | −84.6 | −128.8 | **−170.4** (10,262 vs 10,432.4) | — / 8.71 |
| 29 May | −172.7 | −102.0 | −154.2 | **−71.0** (10,339 vs 10,410.0) | — / 0.00 |
| 01 Jun | −32.9 | −0.4 (ok) | +33.8 | **+77.5** (10,402 vs 10,324.5) | 100.0 / 0.00 |
| 02 Jun | +41.3 | +37.9 | +17.5 | +2.4 (ok) | 72.4 / 37.41 |

Consequences: three of five closes miss by >15 pts. Slice-based Trend labels: 01 Jun is a close<open, RSI2 0.0 session (Bearish), the report calls it the "Bullish impulse"; 03 Jun cash is close<open with RSI2 60.1 (Neutral), the report says Bearish; the narrative "01 Jun strong bullish impulse then two distribution sessions off 10,462 on 03 Jun" is not what the slice shows (cash closes 10,432.4 → 10,410.0 → 10,324.5 → 10,375.6 → 10,341.7; the 10,462 high was printed 29 May). 5-day cash swing is 10,462.0 / 10,286.2; the report's "10,250 window floor" and "25-session ceiling 10,935" are not in the 25-day data (25d cash 10,560.0 [26 May] / 10,141.2 [18 May]).

**Daily pivots** (report derived from its own wrong H/L/C; cash from D-1 cash H/L/C)

| Level | Report | Cash | Δ | Verdict |
|---|---|---|---|---|
| R3 | 10,534.1 | 10,440.2 | +93.9 | FAIL |
| R2 | 10,498.1 | 10,412.1 | +86.0 | FAIL |
| R1 | 10,426.3 | 10,376.9 | +49.4 | FAIL |
| P | 10,390.4 | 10,348.8 | +41.6 | FAIL |
| S1 | 10,318.5 | 10,313.6 | +4.9 | ok |
| S2 | 10,282.6 | 10,285.5 | −2.9 | ok |
| S3 | 10,210.7 | 10,250.3 | −39.6 | FAIL |

(R4/R5/S4/S5 shown by the report are beyond the three-level-each-side layout.)

**Weekly pivots** (report "25–29 May"; cash week 26–29 May, W22)

| Level | Report | Cash | Δ |
|---|---|---|---|
| R3 | 10,496.0 | 10,701.6 | −205.6 |
| R2 | 10,429.0 | 10,630.8 | −201.8 |
| R1 | 10,384.0 | 10,520.4 | −136.4 |
| P | 10,317.0 | 10,449.6 | −132.6 |
| S1 | 10,272.0 | 10,339.2 | −67.2 |
| S2 | 10,205.0 | 10,268.4 | −63.4 |
| S3 | 10,160.0 | 10,158.0 | +2.0 |

Consequence: the report's "above the weekly pivot, below weekly R1" positioning is reversed against the data (D-1 cash close 10,341.7 is below weekly P 10,449.6 and 2.5 pts above weekly S1 10,339.2).

**Monthly pivots**: absent from §11. Level file (May 2026, cash): P 10,370.4 · R1 10,599.6 · R2 10,789.2 · R3 11,018.4 · S1 10,180.8 · S2 9,951.6 · S3 9,762.0.

**Counters (slice, broker CFDs; basis differences expected):** USDX D-1 close 99.553, 5-day up (99.226 on 27 May → 99.553) — consistent with "firm ~99". US500 close 7,538.7 vs report ≈7,554 (−1.0% on the day, 7,614.7 → 7,538.7) — within CFD basis. VIX 17.00 vs report "~16" (1 pt, minor). DAX/STOXX not in slices (unverifiable here).

**Calendar for D (news slice, scheduled-only rows):** no ECB or BoE policy-rate decision is scheduled for 04 Jun. Rows are EUR "ECB President Lagarde Speech" HIGH 11:00 broker (09:00 UK); GBP "BoE Governor Bailey Speech" HIGH 18:40 broker (16:40 UK, after the 16:30 cash close); GBP S&P Global/CIPS Construction PMI MODERATE 11:30 broker (09:30 UK); USD Initial Jobless Claims HIGH 15:30 broker (13:30 UK). The report's "coincident ECB and BoE policy communications … both expected on hold" is not supported by the calendar, is undated ("Thu (wk)"), and the card caveat "holding period collides with §13d ECB/BoE event" misses the actual timings (Lagarde 09:00 UK; Bailey after the cash close; jobless claims 13:30 UK).

## 3. Card construction findings (feeds C4 row 4.5; detail in feedback)
Reference close: D-1 cash close 10,341.7; ATR14 cash 110.43 (3.5×ATR = 386.5; 0.3×ATR = 33.1; 3.0×ATR = 331.3; 2.5×ATR = 276.1).
- Trade 1: |score| 0.05 < 0.25 → must be a SUPPRESSED row. Built as SELL STOP 10,318 at 00:00 UK instead of MARKET at the D-1 close at 07:00 UK. R = 150 = 1.36×ATR → wide-stop flag required, omitted, R/ATR not printed. Invalidation 10,436 sits inside the stop 10,468 (must be beyond SL).
- Trade 2: regime Transitional → breakout-side only; a counter-side R1 sell limit is a suppressed construct. TP1 10,390 = 0.49R (must be ±1R), TP2 10,318 = 1.46R (must be ±2R). Invalidation 10,498 is 2 pts from the stop 10,500.
- Trade 3A: Transitional → 3C (not 3A). Swing 10,354→10,462→10,354 is not a swing (net 0, up-leg 108 = 0.98×ATR, <2×ATR = 220.9). Entry 10,400 labelled 38.2% (really ≈42.6% of the 10,354–10,462 leg); rule is 57.5%. Stop beyond 0% anchor must be +0.25×ATR = +27.6 (report +8).

## 4. Category roll-up

| Cat | Rows | Mean | Level | Multiplier | Points | Justification |
|---|---|---|---|---|---|---|
| C1 Prompt adherence (20) | 3, 4, 4 | 3.67 → 4; −1 for restriction breach | **3** | 0.65 | 13.00 | Structure of Variables respected; anchor overridden to 00:00 UK; Trade 1 produced against the suppression rule; synthesised opens presented as sourced. |
| C2 Structure (20) | 5, 3, 4 | 4.00 | **4** | 0.85 | 17.00 | All 21 sections in order; §6 a real table; monthly pivots missing and daily table over-extended. |
| C3 Accuracy & evidence (25) | 3, 0, 3, 1 (mean 1.75) | override | **0** | 0.00 | 0.00 | Self-contradictory/impossible citations; D-1 O/H/L off 34–78 pts; three closes off by 71–170 pts; weekly pivots off 63–206 pts; monthly absent. Hallucinated-source override sets C3 = 0. |
| C4 Reasoning & judgment (20) | 4, 4, 3, 4, 1 | 3.20 | **3** | 0.65 | 13.00 | Sound narrative and mechanisms, but strategy layer contradicts regime/synthesis and card construction fails M5 on all three cards. |
| C5 Currency & transparency (15) | 3, 4, 3, 1 | 2.75 | **3** | 0.65 | 9.75 | Dated and assumption-aware in form; undated rows; event mischaracterised; restriction breach. |

## 5. Total, band, override
- Total = 13.00 + 17.00 + 0.00 + 13.00 + 9.75 = 52.75 → **53**
- Band: **Low Trust (40–59)**
- Override check: hallucinated-source override **applied** (cap Low 40–59, C3 = 0). Restriction-breach override also indicated (cap Moderate 60–74, C1 −1): the stricter Low cap governs; C1 already reduced 4→3. `override=hallucinated_source`.

## 6. Card Integrity (static linter rows copied verbatim from `qa/ftse_qa1/lint_static/2026-06-04.csv`; separate from the 100)

| card_id | report_date | strategy | flags | dud | Card Integrity |
|---|---|---|---|---|---|
| 2026-06-04_Trade_1 | 2026-06-04 | Trade 1 - Daily Directional | CLEAN | False | 100 |
| 2026-06-04_Trade_2 | 2026-06-04 | Trade 2 - Pivot (regime-aware) | CLEAN | False | 100 |
| 2026-06-04_Trade_3A | 2026-06-04 | Trade 3A - Momentum-Pullback (regime fork: Transitional → 3A) | CLEAN | False | 100 |

`n_cards=3` · `n_duds=0` · `n_warns=0` · report-level Card Integrity = mean(100, 100, 100) = **100**.
Caution: the static linter checks only geometry (sides, ordering, R-size bounds). It does not test regime branch, suppression, anchor/entry mode, TP ratios or invalidation placement, which is why a 100 here coexists with the construction defects above (scored in C4 row 4.5, not in Card Integrity).

## 7. Feedback
See `qa/ftse_qa1/2026-06-04_feedback.md`.
