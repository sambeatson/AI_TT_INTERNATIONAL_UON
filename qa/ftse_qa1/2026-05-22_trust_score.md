# Trust Score v3.7 — FTSE 100 report dated 2026-05-22 (run ftse_qa1)

Report: `reports/md/FTSE_EuroStoxx_Report_22May2026.md` · D = 2026-05-22 · D-1 = 2026-05-21 (Thursday)
Leak check: level file `last_bar_date` = 2026-05-21 < D; slice last bar 2026-05-21 22:45 broker < D. Both pass.
Data basis: the report states cash-index points, so comparisons use the `_cash` columns (UK window 10:00–18:30 broker = 08:00–16:30 London). `_full` values are given where they matter.

## Result (machine-readable lines)

c1=2
c2=4
c3=0
c4=3
c5=2
total=44
band=Low
override=hallucinated_source
card_integrity=100
n_cards=3
n_duds=0
n_warns=0

Override note. The hallucinated-source test (brief §2 row 3.2) is triggered, so C3 is set to 0 and the total is capped to 40–59. The restriction-breach test is also triggered (§5.4 below). C1 was therefore cut one level, from a row mean of 3.0 to 2. `override=` holds one value, so it carries the heavier cap. The total (44) sits inside the Low band regardless.

## 1. Section 7 checklist

| Row | Notes | Evidence | Score |
|---|---|---|---|
| 1.1 Variables respected | Asset (FTSE 100 cash), counters (USDX, S&P 500, DAX 40 plus Euro Stoxx 50 as comparator, no Euro Stoxx cards), as-of close 21 May Europe/London, lookback 5/25 sessions, GBP points and 07:00 UK anchor are all respected. Source requirement of ≥ 6 sources from index-provider / exchange / sell-side tiers is NOT met. The six §4 observations are Investing.com, Yahoo Finance, BBN Times, Trading Economics, Fidelity/Sharecast and Analytics Insight (aggregators and media only). No FTSE Russell / LSEG / exchange or sell-side source appears. | §2, §4, header, §21b | 3 |
| 1.2 Coverage & currency consistent | The daily pivots in §11 are struck from the 20 May session (H 10,366 / L 10,142 / C 10,330.84), not from the D-1 (21 May) session. §13a says "all within the lookback window", but "Investing.com · early May" and "Sunday Guardian · 11 May" fall outside the 15–21 May window, and the first has no date. The 25-session series is partly "derived" (§19). Currency is consistent. | §11, §13a, §19 | 2 |
| 1.3 Audience & tone | Strategist register, trading and risk-review framing, no retail tone. | §1, §18 | 4 |
| 2.1 Sections present & ordered | §1–§21 present and in order, including §13a–d and §21a–d. | headings | 5 |
| 2.2 Scorecard as a table | §6 is a table with all required columns. §11 pivots are tables, but with five levels each side (R5–S5, not 3) and a two-column R / P+S layout rather than one R3→P→S3 ladder. | §6, §11 | 4 |
| 2.3 Method steps visible | §4–§5 observations → classification → consensus. §8 candle-by-candle plus sequence. §9 shows overlap, persistence and VOLator slope. §7 has five chart captions (images dropped by pandoc, accepted). Weights in the "weighted median" are not shown. §9 does not state ATR14. | §4–§9 | 4 |
| 3.1 Quantitative claims sourced | Unsourced or wrong figures in §12 / §14: Brent "$104 / $110–111", gilts "≈5%", gold "£3,430–3,460", DAX "24,607", "two hikes priced". "UK CPI around 3.3%" (§12, §14) contradicts the calendar: the 20 May CPI y/y actual was 2.8 (consensus 3.8, prior 3.4). | §12, §14, NEWS slice | 2 |
| 3.2 Citations exist & contain data | Cannot fetch. Three spot-checks, all self-contradictory against the report's own record (brief §2 rows 3.2 / 3.3 treat this as fabricated). (a) Trading Economics, 20 May: §13a quotes "gave up earlier gains to finish broadly flat", yet §6 / §8 / §13c give 20 May as +2.2% (10,112.40 → 10,330.84), "strong bullish continuation", "rallied strongly". §4 gives the TE level as 10,300 and says it "corroborates 20 May path" (−30.8 from the §6 close). (b) Analytics Insight, 21 May 09:59: "FTSE opens lower", 10,393. The report's own prior close is 10,330.84, so 10,393 is +62 above it (§6 open 10,432.54 is +101.7). (c) Fidelity/Sharecast, 20 May 14:03: 10,380.63 is above the report's own 20 May high of 10,366 (impossible by +14.6). In addition, all ten "CORROB. Δ0.03–0.09" §6 rows show only a delta; the Src B values are never displayed, and the deltas cannot hold given the §3.4 findings below. | §4, §6, §13a | 0 |
| 3.3 Calculations transparent | RSI2 for 19 / 20 / 21 May reproduces from the report's own closes (95.5 / 100 / 100). The 15 / 18 May RSI2 (3.1 / 2.0) cannot be reproduced (14 May and earlier closes not shown). Pivot arithmetic is internally correct for the inputs used (P, R1–R3, S1–S3 re-checked). §21a: 0.250 + 0.100 + 0.050 − 0.010 + 0.007 + 0.045 = 0.442 reproduces with the 0.25 / 0.20 / 0.10 / 0.15 / 0.15 / 0.15 weights. §13b tilt: Σw 4.40, Σws +0.20, tilt 0.045 → 0.05 reproduces. Trend rule error: 18 May is labelled Bearish (§6, §8 "second bearish session") but Close 9,999.20 > Open 9,985 with RSI2 2.0 → Neutral by the stated rule. | §6, §8, §11, §13b, §21a | 3 |
| 3.4 Numbers reconcile | D-1 close is the same in §1 / §3 / §4 / §6 / §21b (10,443 / 10,443.47). Breaks: §1 and §13c say 21 May was "+0.11%" / "~0.1%", but §6 gives 20 May close 10,330.84 → 21 May close 10,443.47 = +112.63 pts = +1.09%. The 25-session high is 10,560 (§1, §9) vs 10,623 (§21b 3C) vs "zone above 10,500" (§8). §11 uses a weekly high of 10,510 while §8 says there is "little overhead" above the 21 May high of 10,471.64 until 10,500. §3: Trade 2 stop "below the 21 May low (10,353) with a 0.25×ATR buffer" is 10,360, which is ABOVE 10,353 (a 0.25×ATR buffer gives 10,318, the level Trade 1 uses). **Against the slice (see §3 below) the D-1 close is off by 18.8 pts and the 15–20 May rows are off by 92–330 pts.** | §1, §6, §9, §11, §13c, §21b | 1 |
| 4.1 Pillars conclude | §8 "Bullish continuation", §9 Transitional / Mixed tilting Bullish, §10 aggregate MIXED. §12 and §14 carry factor-level labels but no closing direction label for the section. | §8–§14 | 3 |
| 4.2 Cross-asset interpreted | Mechanisms given (USD → GBP → overseas-earnings translation; S&P as common beta; DAX sector skew). But USDX is called "rising modestly … Confirms": slice closes 15–21 May are 99.303, 98.985, 99.337, 99.150, 99.237 (−0.07% over the window). The premise is wrong. Oil mechanism sits in §12 only. | §10 | 4 |
| 4.3 Synthesis reconciles tensions | §15 / §16 / §18 address short vs medium term, KER vs price, §17 vs §21a. §20 says the KER conflict is "treated as a conviction cap", but the model applies only −0.010 and no cap. TP2 of +250 is described as "ambitious" although 2R = 250 < 3×ATR (≈425), so the flag is not set by the arithmetic. | §9, §16, §20, §21a | 3 |
| 4.4 Calibrated language | §17 is one sentence; confidence Medium stated in §3. | §3, §17 | 4 |
| 4.5 Card construction (protocol) | Trade 2 uses the wrong branch geometry; Trade 3C is shipped against a fired suppression gate; Trade 3C's R and TP1 exceed the ATR bounds; reference close not printed with session date; D-1 pivots and 25-day range mis-stated. See §4 and the feedback file. | §21b | 2 |
| 5.1 Data dated; staleness flagged | Most prices are dated. "early May" article undated; "all within the lookback window" false; §19 discloses a partly derived 25-session series, but its derived highs / lows (10,623 / 9,939) then drive the 3C card despite the claim they are "not used for … trade pricing". | §13a, §19, §21b | 3 |
| 5.2 Assumptions up front | The 07:00 UK anchor caveat is stated at the top, in §20 and in the card. Corroboration status is contradictory: §6 / §11 / §19 say every tier is two-source CORROBORATED, while §19 / §20 / §21b say "corroboration leniency", "single-source-leniency", "directionally indicative". | header, §19–§21 | 3 |
| 5.3 Red flags surfaced | §12 / §15 carry risks. §13d starts at "Wk of 25 May" and omits D (22 May) itself. The NEWS slice schedules for 22 May: EUR GDP q/q (HIGH) at 07:00 UK = the Trade 1 anchor; UK Retail Sales at 08:00 UK; Lagarde speech (HIGH) at 09:30 UK; Ifo at 09:00 UK; US Michigan sentiment 15:00 UK. None reaches a card caveat (only BoE is cited). D-1 events missing from §13c: UK Composite PMI 48.5 vs 52.6 prior (Services 47.9 vs 51.8 consensus); Eurozone CPI y/y 3.0 vs 1.9 consensus. §1 calls BoE a "policy meeting", §13d calls it "commentary / signals"; the calendar through D shows only speeches. | §13c, §13d, §21b | 2 |
| 5.4 Restrictions honoured | Breach. (i) §10 gate "No confirmed break per §4d in TRANSITION → Suppress Trade 3C" has fired (D-1 close below the break level) and 3C was emitted anyway. (ii) §19, §20 and §21b cite a "run instruction" / "corroboration leniency" as authority to produce strategies; the module forbids citing such an instruction in the report. (iii) A "derived" 25-session series feeds a card. (iv) Module internals leak into the text: "SurfaceContractError", "RANGE dual-gate", "v2.1 baseline", "20-session lock window". | §19, §20, §21b | 1 |

Category means before overrides: C1 (3,2,4) = 3.0 → 3, then −1 for the restriction breach → **2**. C2 (5,4,4) = 4.33 → **4**. C3 (2,0,3,1) = 1.5 → 2, then set to **0** by the hallucinated-source override. C4 (3,4,3,4,2) = 3.2 → **3**. C5 (3,3,2,1) = 2.25 → **2**.

## 2. Category roll-up

| Cat | Level | Multiplier | Points | One-line justification |
|---|---|---|---|---|
| C1 Prompt adherence (20) | 2 | 0.40 | 8.0 | Variables mostly respected, but the source tiers are missing, the daily pivots come from the wrong session, and a restriction is breached (−1 level). |
| C2 Structure (20) | 4 | 0.85 | 17.0 | All 21 sections present and ordered; pivot tables over-extended (5 levels) and in a two-column layout. |
| C3 Accuracy & evidence (25) | 0 | 0.00 | 0.0 | Override. D-1 close off by 18.8 pts, 15–20 May rows off by 92–330 pts, pivot inputs wrong, three cited sources self-contradictory. |
| C4 Reasoning & judgment (20) | 3 | 0.65 | 13.0 | Narrative and §21a arithmetic are coherent, but card construction (Trade 2 branch, 3C gate, ATR bounds) fails. |
| C5 Currency & transparency (15) | 2 | 0.40 | 6.0 | D-day events omitted, lookback claim false, corroboration status contradictory, restrictions breached. |

## 3. Category 3 accuracy table (report vs slice)

Tolerance (brief §4): |Δ| ≤ 5 on a close, ≤ 10 on O / H / L. A close off by more than 15 is a Category 3 failure.

| Session | Field | Report | Slice (cash) | Δ (report − slice) | Verdict |
|---|---|---|---|---|---|
| 15 May | O / H / L / C | 10,081 / 10,110 / 9,978 / 10,004.57 | 10,299.0 / 10,309.4 / 10,154.9 / 10,167.0 | −218.0 / −199.4 / −176.9 / −162.4 | FAIL (all four) |
| 18 May | O / H / L / C | 9,985 / 10,058 / 9,905 / 9,999.20 | 10,144.5 / 10,336.3 / 10,141.2 / 10,290.8 | −159.5 / −278.3 / −236.2 / −291.6 | FAIL (all four) |
| 19 May | O / H / L / C | 10,010 / 10,120 / 9,990 / 10,112.40 | 10,339.9 / 10,408.9 / 10,313.0 / 10,325.1 | −329.9 / −288.9 / −323.0 / −212.7 | FAIL (all four) |
| 20 May | O / H / L / C | 10,150 / 10,366 / 10,142 / 10,330.84 | 10,274.4 / 10,458.8 / 10,272.8 / 10,422.9 | −124.4 / −92.8 / −130.8 / −92.1 | FAIL (all four) |
| 21 May (D-1) | O | 10,432.54 | 10,371.1 | +61.4 | FAIL |
| 21 May (D-1) | H | 10,471.64 | 10,469.1 | +2.5 | OK |
| 21 May (D-1) | L | 10,353.47 | 10,344.7 | +8.8 | OK |
| 21 May (D-1) | C | 10,443.47 | 10,462.3 (full-day 10,490.5) | −18.8 (−47.0) | FAIL (> 15) |
| RSI2 | 15 / 18 / 19 / 20 / 21 May | 3.1 / 2.0 / 95.5 / 100 / 100 | 24.8 / 39.6 / 100 / 100 / 100 | −21.7 / −37.6 / −4.5 / 0 / 0 | 15 and 18 May FAIL; D-1 OK |
| ATR14 | D-1 | ≈142 (implied by 3.5×ATR ≈ 496 and 3×ATR ≈ 425) | 147.3 cash / 165.3 full | −5.3 | OK on cash basis |

Of 20 O/H/L/C fields, 2 are within tolerance. RSI2 reproduces from the report's own closes (`--closes`) for 19–21 May, so the arithmetic is sound and the failure is in the closes themselves.

Pivots (cash basis, Δ = report − level file):

| Daily (report: 20 May H/L/C; should be 21 May) | P | R1 | R2 | R3 | S1 | S2 | S3 |
|---|---|---|---|---|---|---|---|
| Report | 10,279.6 | 10,417.2 | 10,503.6 | 10,641.2 | 10,193.2 | 10,055.6 | 9,969.2 |
| Level file `d_cash` | 10,425.4 | 10,506.0 | 10,549.8 | 10,630.4 | 10,381.6 | 10,301.0 | 10,257.2 |
| Δ | −145.8 | −88.8 | −46.2 | +10.8 | −188.4 | −245.4 | −288.0 |

| Weekly (W20, 11–15 May) | P | R1 | R2 | R3 | S1 | S2 | S3 |
|---|---|---|---|---|---|---|---|
| Report | 10,164.2 | 10,350.4 | 10,696.2 | 10,882.4 | 9,818.4 | 9,632.2 | 9,286.4 |
| Level file `w_cash` | 10,228.0 | 10,310.1 | 10,453.2 | 10,535.3 | 10,084.9 | 10,002.8 | 9,859.7 |
| Δ | −63.8 | +40.3 | +243.0 | +347.1 | −266.5 | −370.6 | −573.3 |

| Monthly (April) | P | R1 | R2 | R3 | S1 | S2 | S3 |
|---|---|---|---|---|---|---|---|
| Report | 10,414.7 | 10,649.3 | 10,854.7 | 11,089.3 | 10,209.3 | 9,974.7 | 9,769.3 |
| Level file `m_cash` | 10,418.8 | 10,650.0 | 10,928.7 | 11,159.9 | 10,140.1 | 9,908.9 | 9,630.2 |
| Δ | −4.1 | −0.7 | −74.0 | −70.6 | +69.2 | +65.8 | +139.1 |

Pivot inputs implied by the level file (cash): weekly H 10,371.1 / L 10,145.9 / C 10,167.0 (report: 10,510 / 9,978 / 10,004.57); April H 10,697.5 / L 10,187.6 / C 10,371.3 (report: 10,620 / 10,180 / 10,444). Weekly and monthly periods are correctly identified; the daily period is not.

Swings: report 25-session range 9,939–10,623 (width 684) vs cash 10,141.2–10,666.5 (width 525.3). Report 5-day low 9,905 vs cash 10,141.2.

Counters (slice, 21 May close): S&P 500 7,452.3 (15 May 7,400.8 → +0.70%), consistent with "rising, near 7,400". VIX 17.91 (report "around 17", Δ +0.9, acceptable). USDX 99.237, flat over the window, contradicting "rising modestly".

## 4. Card Integrity (linter rows, copied verbatim from `lint_static/2026-05-22.csv`)

| card_id | strategy | flags | dud | per-card score |
|---|---|---|---|---|
| 2026-05-22_Trade_1 | Trade 1 — Daily Directional | CLEAN | False | 100 |
| 2026-05-22_Trade_2 | Trade 2 — Pivot (TRANSITION, breakout side) | CLEAN | False | 100 |
| 2026-05-22_Trade_3C | Trade 3C — Momentum-Breakout | CLEAN | False | 100 |

Report-level Card Integrity = mean(100, 100, 100) = **100**. n_cards = 3, n_duds = 0, n_warns = 0.

The static linter has no ATR and no market data, so it cannot see the rule failures listed in the feedback file (wrong Trade 2 branch, 3C gate, R and TP1 bounds against ATR). Card Integrity stays 100 as computed; those defects are scored in C4 row 4.5 and C1 / C5 via the breach.

## 5. Total, band, override

- Total = 8.0 + 17.0 + 0.0 + 13.0 + 6.0 = **44** → band **Low** (40–59).
- Override: **hallucinated_source** (C3 → 0, cap 40–59), based on the three self-contradictory source checks in row 3.2. Restriction breach also applies (row 5.4; C1 −1) and is already reflected in C1 = 2.

Feedback for the regeneration agent: `qa/ftse_qa1/2026-05-22_feedback.md`.
