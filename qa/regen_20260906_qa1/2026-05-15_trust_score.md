# Trust Score — 2026-05-15 — SP500_Daily_Report_15_May_2026.md

Run: regen_20260906_qa1 · Asset US500 · D-1 slice 2026-05-14 (cash session 16:30–23:00 broker) · Reviewer basis: brief §1–§5, framework v3.7 §4–§7.
Helper run: `qa_slice_stats.py --closes 7398.93 7412.84 7400.96 7444.25 7501.59` → slice D-1 cash close 7,509.10; ATR14 (cash) 67.01; daily pivots (cash) P 7,498.30 / R1 7,533.70 / S1 7,473.70 / R2 7,558.30 / S2 7,438.30 / R3 7,593.70 / S3 7,413.70; 5d swing 7,522.90 / 7,345.30; 25d swing 7,522.90 / 6,790.60; RSI2 from report's own closes: n/a, n/a, 53.9, 78.5, 100.0.

## 1. Section 7 checklist

| Item | Reviewer notes | Evidence observed | Score 0–5 | Action required |
|---|---|---|---|---|
| 1.1 Variables respected | Asset, counters (USDX first), lookback, USD/points all correct. Trade 1 anchor is 13:30 UK, not the fixed 07:00 UK; report attributes this to a "user directive" (§20 OVERRIDE 1) that is not part of the fixed stack. As-of stated as "15 May (issued early-session)" rather than NY close of D-1. Tick 0.01 not stated. Six distinct outlets cited (CNBC, TheStreet, Yahoo, FRED, Reuters/Detroit News, Crestwood). | §2 table; §12 "anchor 13:30 UK, override"; §20 OVERRIDE 1; §21b Trade 1 Entry | 3 | Restore 07:00 UK anchor; state as-of = 14 May NY close; add tick size |
| 1.2 Coverage & currency consistent | All price data dated 8–14 May (≤ D-1); session-day references (Powell 15 May) are calendar items, acceptable. No currency/unit drift. §13c has 15 May as first row, consistent with D. | §2, §6, §13c, §21c | 4 | none |
| 1.3 Audience & tone | Strategist register throughout. Slight meta-commentary in body ("the user has explicitly directed…", §6 note, §19, §21d) belongs in §20 only. | §6 note, §19 footnote, §21d | 4 | Move directive commentary to §20 |
| 2.1 Sections present & ordered | §1–§21 all present and ordered; §21a–d present. §13c is labelled "week ahead" (it is the upcoming calendar) and §13d is "collision risk" — the previous-period calendar required for §13c is absent, and the upcoming calendar sits under the wrong letter. | §13 headings | 4 | Add §13c previous-period calendar; move upcoming calendar to §13d; keep collision note inside §13d |
| 2.2 Scorecard as a table | §6 is a table but lacks Trend, Final and Validation columns and merges Source A/Source B into one column. §11 tables are ordered P, R1, R2, R3, S1, S2, S3 — not R3→P→S3. | §6 table header; §11 three tables | 2 | Rebuild §6 with Date/O/H/L/C/RSI2/Trend/Source A/Source B/Final/Validation; reorder §11 R3,R2,R1,P,S1,S2,S3 |
| 2.3 Method steps visible | §4 observations → §5 normalisation/weighting → §3 consensus visible. §8 candle-by-candle plus sequence read. §9 gives persistence, overlap, VOLator slope. §7: five image placeholders with captions (pandoc-dropped images; accepted). | §4, §5, §8, §9, §7 | 5 | none |
| 3.1 Quantitative claims sourced | Most §1/§12/§14 figures trace to §4/§13a (84%/12.3%/13.4% → Crestwood; CPI 3.8% → 24/7 WS/Reuters; Dow 50,000 → TheStreet). Unsourced: "three deviations of momentum above the monthly pivot" (§12), PHLX +65% YTD (§14/§15), WTI $101.45 / $102.18 (§14), ISM prices 84.6 (§12/§14), "early-April lows near 7,180" (§9 — slice 25d low is 6,790.6). USDX "falling/flat" (§10/§14) is contradicted by the slice (97.87 → 98.87 over the 5 sessions). | §9, §10, §12, §14 | 2 | Source or drop the unsourced figures; correct USDX direction; correct the 25-session low |
| 3.2 Citations exist & contain data | Three spot-checks: (a) CNBC 14 May "+0.77%" × Yahoo prior close 7,444.25 → 7,501.57 ≈ 7,501.59 used consistently in §1/§3/§4/§6/§18/§21b; (b) FRED 12 May 7,400.96 × Reuters "−11.88 pts to 7,400.96" → implies 7,412.84 = §6 11 May close, consistent; (c) Yahoo 13 May "7,444.25 +0.58%" → 7,400.96 × 1.0058 = 7,443.9, consistent to rounding. No self-contradictory or impossible citation found. Weakness: §20 uses a Yahoo intraday quote at 11:10 ET (7,499.72) as "confirmation" of a 16:00 close — cannot corroborate a close. 11 May close is a back-calculation, not a quote (§20 "FRED (back-calc)"). | §4, §13a, §20 | 4 | Do not cite intraday quotes as close corroboration; label back-calculated values as derived |
| 3.3 Calculations transparent | Pivots: all three tables reproduce exactly from the stated inputs (verified). RSI2: 12 May shown as 0 but the report's own closes give 53.9 (11 May +13.91, 12 May −11.88 → RS 1.17); slice gives 65.86 — FAIL per brief §4. 13/14 May reproduce (78.5/100). ATR(14) is not computed — a "conservative 60-pt baseline" (§19); slice ATR14 = 67.01. KER is a "4-period proxy ≈ 0.81", not KER(13, EMA 3). Direction score components sum to 0.798 (0.25+0.20−0.01+0.15+0.048+0.15) but are reported as "+0.79 … rounded to +0.78". Trade 2 stop arithmetic: 7,481.23 − 19.26 = 7,461.97, card says 7,461.74. Trade 3C TP1 labelled "1 × width (325) applied to entry" but 7,595 − 7,510 = 85. | §6, §9, §19, §20 Strategies trace, §21b | 1 | Recompute RSI2 for 12 May; compute ATR(14) and KER(13, EMA3) from a ≥14-session series; fix score rounding; fix Trade 2/3C arithmetic |
| 3.4 Numbers reconcile | Internal: D-1 close 7,501.59 identical in §1/§3/§4/§6/§18/§21b; §11 pivots = card pivots; ATR 60 consistent across §19/§21b; RSI2 100 in §6 = §15. Inconsistencies: score +0.79 (§20) vs +0.78 (§1/§21a); resistance zone 7,525–7,550 (§11/§16/§20) vs 7,525–7,575 (§17); Trade 1 caveat "holding-period extends through 20 May" vs Trade 1 TP3 time-stop 16:00 ET 15 May. Against the slice: three closes off 6.9–8.8 pts; 8 of 15 O/H/L values off 10–39 pts; §6 opens are exactly the prior closes (synthesised); weekly low 7,260 vs 7,177.5; April low ≈6,750 vs 6,471.7; 25d low ≈7,180 vs 6,790.6 (see §5 log). Cross-report: the 14 May report stated 11 May H/L 7,424.7/7,392.0 RSI2 57.1 and 12 May H/L 7,422.9/7,378.5 RSI2 36.0; this report restates them as 7,438.40/7,395.60 RSI2 100 and 7,423.10/7,370.20 RSI2 0. | cross-section; slice; reports/md/SP500_Report_14May2026.md | 2 | Reconcile score, zone, holding period; source real opens; carry prior-report O/H/L forward unchanged |
| 4.1 Pillars conclude | §8 "decisively bullish"; §9 TREND_UP; §10 CONFIRM (3/3); §12 sub-labels (supportive / supportive-with-reservations / negative-modest / mixed); §14 "consistent — no contradictions". Labels present and match section content, but §10/§14's USDX label rests on a direction that the slice contradicts. | §8–§14 | 4 | Re-run §10/§14 with correct USDX direction |
| 4.2 Peer/cross-asset interpreted | Mechanisms given for each counter (translation effect, vol compression signature, global risk premium). But USDX "falling/flat, easing" is wrong on the slice (rising every session 11–14 May, +1.00 over the block); VIX 17.87 vs slice 18.98 (basis-plausible; direction falling agrees). The "3 of 3 confirm" conclusion is therefore not supported for USDX. | §10 table; USDX slice | 3 | Correct USDX read; re-evaluate whether USDX confirms or contradicts |
| 4.3 Synthesis reconciles tensions | §15/§16 address RSI2-100/KER exhaustion vs trend ("one pullback"); §21a notes no conflict with §17. Not reconciled: (i) 3C is framed as a "confirmed breakout above 25-session range top" while the stated D-1 close 7,501.59 is below the stated top 7,505.30 — no break has occurred; (ii) Trade 2 is a BUY STOP below the D-1 close; (iii) §9 says all three pivot tiers are single-source yet Trade 2 is produced against the M5 suppression rule; (iv) "above weekly R2" thesis (§1/§11/§15) depends on a weekly low 82 pts above the slice's. Card construction deviates from M5 on all three cards (see §4 of this file). | §9, §11, §15–§18, §21a–b | 2 | Rebuild cards per M5; reconcile 3C trigger with the D-1 close; drop weekly-R2 claim or re-source the weekly low |
| 4.4 Calibrated language | §17 is one sentence (long, with an either/or branch but not hedge-stacked). Confidence stated in §3 (High) and §18 (High on level / Medium on path). §16 gives range, base case and invalidation. | §3, §16, §17, §18 | 4 | Tighten §17 to a single directional clause |
| 5.1 Data dated; staleness flagged | Every §4/§6/§13a item dated; single-source O/H/L flagged in §4, §6, §11, §19 and on cards; ATR flagged as estimate. Monthly H/L flagged as "estimated". | §4, §6, §11, §19 | 4 | none beyond replacing estimates with sourced values |
| 5.2 Assumptions up front | Anchor override is logged in §20 but the Trade 1 card states "Market at 13:30 UK" without an explicit override/proxy caveat on the card. Single-source pivot propagation to cards is done. The "user directive" basis for both overrides is asserted, not evidenced, and is not in the fixed stack. | §20 OVERRIDE 1/2; §21b caveats | 3 | Put the anchor deviation on the card caveat; remove unevidenced directive claims |
| 5.3 Red flags surfaced | §12/§15 list CPI, Nvidia 20 May, Iran/oil, complacent VIX. §13d collision carried into all three card caveats (Trade 1's collision flag conflicts with its own 15 May time-stop). | §12, §13d, §15, §21b | 4 | Align Trade 1 collision caveat with its holding period |
| 5.4 Restrictions honoured | Breaches: (a) §6 opens for 11–14 May equal the prior close to the cent and are presented as "Yahoo intraday tape" — synthesised prices presented as sourced; (b) 14 May close is computed (+0.77% × 7,444.25) and 11 May close is back-calculated, both labelled CORROBORATED closes; (c) M5 Trade 2 suppression rule (all pivot tiers single-source) overridden; (d) fixed 07:00 UK anchor overridden. No module codes, bracketed variables or framework name found; ES futures mentioned as excluded/confirmation-only (acceptable); no retail CFD quotes in the OHLC basis. | §6 Open column; §3/§5/§20; §19 footnote; §20 OVERRIDE 1/2 | 1 | Source actual opens or mark them "not available"; label derived closes as derived; apply the suppression rule; use 07:00 UK |

## 2. Category roll-up

| Category | Level | Multiplier | Points | Justification |
|---|---|---|---|---|
| C1 Prompt adherence (max 20) | 3 | 0.65 | 13.00 | Rows 3/4/4 → mean 3.67 → 4; restriction-breach override lowers C1 one level → 3 |
| C2 Structure (max 20) | 4 | 0.85 | 17.00 | Rows 4/2/5 → mean 3.67 → 4; §6 columns and §11 ordering are the defects |
| C3 Accuracy & evidence (max 25) | 2 | 0.40 | 10.00 | Rows 2/4/1/2 → mean 2.25 → 2; RSI2 12 May fails to reproduce; synthesised opens; USDX direction wrong; large weekly/monthly/25d low errors |
| C4 Reasoning & judgment (max 20) | 3 | 0.65 | 13.00 | Rows 4/3/2/4 → mean 3.25 → 3; card construction off-M5 on all three cards; 3C "confirmed" break not confirmed |
| C5 Currency, restrictions & transparency (max 15) | 3 | 0.65 | 9.75 | Rows 4/3/4/1 → mean 3.00 → 3; restriction breaches in 5.4 |
| **Total** | | | **62.75 → 63** | |

## 3. Total, band, override check

- Total: **63/100**
- Band: **Moderate** (60–74)
- Overrides: **restriction_breach** — synthesised opens presented as sourced Yahoo tape, derived closes labelled corroborated, the M5 Trade 2 suppression rule and the fixed 07:00 UK anchor both overridden on an unevidenced "user directive". Cap at Moderate (60–74): total 63 is within the cap, no further reduction; C1 reduced one level (4 → 3), already applied above. No fabricated source found (hallucinated_source override not triggered).

## 4. Card Integrity

Lint rows (verbatim from `qa/regen_20260906_qa1/lint_static/2026-05-15.csv`):

| card_id | report_date | strategy | flags | dud |
|---|---|---|---|---|
| 2026-05-15_Trade_1 | 2026-05-15 | Trade 1 - Daily Directional | CLEAN | False |
| 2026-05-15_Trade_2 | 2026-05-15 | Trade 2 - Pivot (TREND breakout, buy stop) | CLEAN | False |
| 2026-05-15_Trade_3C | 2026-05-15 | Trade 3C - Momentum-Breakout (buy stop) | CLEAN | False |

Per-card integrity (100 − 40·#DUD − 10·#WARN, floor 0):

| Card | #DUD | #WARN | Integrity | Suppressed |
|---|---|---|---|---|
| Trade 1 | 0 | 0 | 100 | no |
| Trade 2 | 0 | 0 | 100 | no |
| Trade 3C | 0 | 0 | 100 | no |

**Report-level Card Integrity (mean over non-suppressed cards): 100.0.** n_cards 3 · n_duds 0 · n_warns 0.

M5 construction assessment (feeds row 4.3, not the integrity number; slice ATR14 = 67.01, so R band [0.3, 3.0]×ATR = [20.10, 201.03] pts, TP1 ≤ 2.5×ATR = 167.5 pts from entry):

- Trade 1 (MARKET, LONG): entry 7,501.59 = report D-1 close (slice cash close 7,509.10, Δ 7.51). Anchor 13:30 UK ≠ fixed 07:00 UK. Stop 7,453.59 (R 48 = 0.72×ATR, in band, no wide-stop flag needed) is derived as "halfway between S1 and weekly R1 as 0.8×ATR" — not the M5 §4c rule (tighter of 5d swing low / nearest support, + 0.25×ATR buffer). TP1/TP2 = ±1R/±2R ✓; TP3 runner 3×ATR cap and session time-stop ✓; BE 0.2R ✓; invalidation separate ✓. Caveat says the hold extends through 20 May while TP3 time-stops on 15 May — contradiction. TP1 "strong confluence with monthly R2 7,549.67" is an artefact of an April low that is ~278 pts above the slice's.
- Trade 2 (STOP, LONG, TREND branch): entry formula P + 0.10×(R1−P) ✓ on the report's pivots. Defects: (i) a BUY STOP at 7,485.68 sits below the D-1 close (7,501.59 stated / 7,509.10 slice) — a stop order there is not executable as a stop; (ii) stop arithmetic 7,461.74 should be 7,461.97 (R 23.71 not 23.94); (iii) TP ladder is R1/R2 + runner instead of M5's R1/R1.5/R2; (iv) the report states all pivot tiers are SINGLE-SOURCE INDICATIVE, which under M5 §5.2 suppresses Trade 2 entirely — the card should be a SUPPRESSED row.
- Trade 3C (STOP, LONG): M5 §4d requires a confirmed close beyond the 25-day boundary by ≥ 0.25×ATR (16.75 pts). Stated D-1 close 7,501.59 is below the stated boundary 7,505.30 (slice: 7,509.10 vs 7,522.90) — no confirmed break; a conditional buy stop 4.7 pts above the top does not meet the margin. Stop "halfway between entry and range mid" and TP1 "1×width" are not the M5 formulas (stop = low + 0.40×width, TP1 = +1.0×width, TP2 = +1.5×width) and the stated arithmetic does not match the levels (7,595 − 7,510 = 85, not 325). The 25-session range itself is wrong vs the slice (≈7,180–7,505, width 325 vs 6,790.6–7,522.9, width 732.3). R 85 and TP1 +85 are inside the static bands, which is why the linter passes it.

## 5. Data reconciliation log

Tolerances (brief §4): close |Δ| ≤ 3 consistent; open/high/low |Δ| ≤ 8 consistent; larger = discrepancy; close > 10 or non-reproducing RSI2 = Category 3 failure. Slice = cash session 16:30–23:00 broker.

| Section | Field | Report value | Slice value | Δ (report − slice) | Verdict |
|---|---|---|---|---|---|
| §6 | 8 May Open | 7,338.50 | 7,375.60 | −37.10 | Discrepancy |
| §6 | 8 May High | 7,402.10 | 7,407.50 | −5.40 | Consistent |
| §6 | 8 May Low | 7,332.80 | 7,371.80 | −39.00 | Discrepancy |
| §6 / §4 | 8 May Close | 7,398.93 | 7,400.60 | −1.67 | Consistent |
| §6 | 11 May Open | 7,398.93 | 7,391.30 | +7.63 | Consistent (but = prior close, synthesised) |
| §6 | 11 May High | 7,438.40 | 7,435.00 | +3.40 | Consistent |
| §6 | 11 May Low | 7,395.60 | 7,391.30 | +4.30 | Consistent |
| §6 / §4 | 11 May Close | 7,412.84 | 7,419.70 | −6.86 | Discrepancy (< 10, not a failure) |
| §6 | 12 May Open | 7,412.84 | 7,396.30 | +16.54 | Discrepancy (= prior close, synthesised) |
| §6 | 12 May High | 7,423.10 | 7,415.50 | +7.60 | Consistent |
| §6 / §8 | 12 May Low | 7,370.20 | 7,345.30 | +24.90 | Discrepancy |
| §6 / §4 | 12 May Close | 7,400.96 | 7,409.80 | −8.84 | Discrepancy (< 10, not a failure) |
| §6 | 13 May Open | 7,400.96 | 7,412.00 | −11.04 | Discrepancy (= prior close, synthesised) |
| §6 / §8 | 13 May High | 7,448.90 | 7,466.00 | −17.10 | Discrepancy |
| §6 | 13 May Low | 7,392.10 | 7,381.50 | +10.60 | Discrepancy |
| §6 / §4 | 13 May Close | 7,444.25 | 7,451.50 | −7.25 | Discrepancy (< 10, not a failure) |
| §6 | 14 May Open | 7,444.25 | 7,463.90 | −19.65 | Discrepancy (= prior close, synthesised) |
| §6 / §11 / §8 | 14 May High | 7,505.30 | 7,522.90 | −17.60 | Discrepancy |
| §6 / §11 | 14 May Low | 7,436.80 | 7,462.90 | −26.10 | Discrepancy |
| §1/§3/§4/§6/§18/§21b | 14 May Close (D-1) | 7,501.59 | 7,509.10 | −7.51 | Discrepancy (< 10, not a failure; derived value, see 5.4) |
| §6 | RSI2 11 May | 100 | 100.00 (own closes n/a) | 0 | Consistent |
| §6 | RSI2 12 May | 0 | 65.86 slice / 53.9 from report's own closes | −65.9 / −53.9 | **FAIL — does not reproduce from own closes** |
| §6 | RSI2 13 May | 78 | 80.81 slice / 78.5 own closes | −2.8 / −0.5 | Consistent |
| §6 | RSI2 14 May | 100 | 100.00 / 100.0 | 0 | Consistent |
| §11 daily | P/R1/R2/R3/S1/S2/S3 from report H/L/C | 7,481.23 / 7,525.66 / 7,549.73 / 7,594.16 / 7,457.16 / 7,412.73 / 7,388.66 | Recomputed from report inputs: identical | 0.00 | Reproduces ✓ |
| §11 daily | P vs slice cash pivot | 7,481.23 | 7,498.30 | −17.07 | Discrepancy (inherits H/L error) |
| §11 daily | S1 vs slice | 7,457.16 | 7,473.70 | −16.54 | Discrepancy |
| §11 weekly | inputs H / L / C (4–8 May) | 7,402.10 / 7,260.00 / 7,398.93 | 7,407.50 / 7,177.50 / 7,400.60 | −5.4 / +82.5 / −1.7 | Low is a discrepancy; pivots reproduce from own inputs ✓ |
| §11 weekly | P / R1 / R2 vs slice | 7,353.68 / 7,447.35 / 7,495.78 | 7,328.53 / 7,479.57 / 7,558.53 | +25.2 / −32.2 / −62.8 | Discrepancy — "close above weekly R2" not true on slice (7,509.10 < 7,558.53) |
| §11 monthly | inputs H / L / C (April) | ≈7,235 / ≈6,750 / 7,209.00 | 7,226.70 / 6,471.70 / 7,213.70 | +8.3 / +278.3 / −4.7 | Low is a discrepancy; pivots reproduce from own inputs ✓; slice-based P 6,970.70, R2 7,725.70 — the 7,549.67 "monthly R2 confluence" is an artefact |
| §9 / §21b 3C | 25-session low / range | ≈7,180 (width ≈325, mid ≈7,340) | 6,790.60 on 13 Apr (width 732.3, mid 7,156.75) | ≈ +390 | Discrepancy |
| §8 / §21b | 5-day swing low | 7,370.20 | 7,345.30 | +24.90 | Discrepancy |
| §9 / §19 / §21b | ATR(14) | 60 (baseline, not computed) | 67.01 cash / 75.39 full-day | −7.0 | Discrepancy — not computed |
| §9 / §10 / §14 | VIX level 14 May | 17.87 | 18.98 (cash close) | −1.11 | Basis-plausible; direction (falling) consistent (19.32 → 18.98) |
| §10 / §14 | USDX 5-day direction | "Falling / flat", "easing" | 97.87 (8 May) → 97.93 → 98.28 → 98.49 → 98.87 (14 May), +1.00 | direction reversed | **Discrepancy — direction contradicted** |
| §20 / §1 / §21a | Direction score | +0.79 → "+0.78" | components sum 0.798 | −0.02 | Inconsistent rounding |
| §21b Trade 2 | Stop | 7,461.74 | 7,481.23 − 0.8×24.07 = 7,461.97 | −0.23 | Arithmetic error |
| §21b Trade 3C | TP1 vs its stated derivation | 7,595 ("1×width 325 applied to entry") | 7,510 + 325 = 7,835 | −240 | Label does not match level |
| §6 vs prior report | 11 May H/L, RSI2 | 7,438.40 / 7,395.60, 100 | 14 May report: 7,424.7 / 7,392.0, 57.1 | +13.7 / +3.6 | Cross-report inconsistency |
| §6 vs prior report | 12 May H/L, RSI2 | 7,423.10 / 7,370.20, 0 | 14 May report: 7,422.9 / 7,378.5, 36.0 | +0.2 / −8.3 | Cross-report inconsistency (RSI2) |
