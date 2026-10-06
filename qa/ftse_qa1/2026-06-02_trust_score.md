# Trust Score v3.7 - FTSE 100 daily report, D = 2026-06-02 (run ftse_qa1)

Report: `reports/md/FTSE_EuroStoxx_Report_02Jun2026.md`
Data basis: `data/levels/UK100_by_date/2026-06-02.csv` (last_bar_date = 2026-06-01 < D, leak-free confirmed), UK100 M15 slice to 2026-06-01, `engine/qa_slice_stats.py --cash-open 10:00 --cash-close 18:30`. The report claims a cash-index basis, so `_cash` fields are used (`_full` quoted where it changes the verdict).

## Headline lines
c1=1
c2=4
c3=1
c4=3
c5=2
total=45
band=Low
override=restriction_breach
card_integrity=100
n_cards=3
n_duds=0
n_warns=0

(`n_cards=3` linter rows: Trade 1 SUPPRESSED, Trade 2 SUPPRESSED, Trade 3C CLEAN; 1 non-suppressed card is scored. The linter is static and says nothing about the construction defects listed in the feedback, so card_integrity=100 sits beside a Category 4 card-construction score of 2.)

## 1. Category 3 data reconciliation (report vs level file / slice)

The single largest finding: the report's as-of session is Fri 29 May 2026, but the last completed UK100 session before D is **Mon 1 Jun 2026** (cash O 10371.9 / H 10410.4 / L 10286.2 / C 10324.5; full-day C 10329.3). The 1 Jun session is absent from §6 and every derived value. The report itself cites 1 Jun news (§13a) and the 1 Jun USDX read (§10), so the omission is not a data-availability constraint.

### 1a. §6 OHLC (report vs cash-session basis; tolerance 5 pts close, 10 pts O/H/L)
| Session | Field | Report | Cash slice | Delta | Verdict |
|---|---|---|---|---|---|
| Mon 25 May | all | 10470.00 / 10557.16 / 10465.00 / 10545.00 | NO SESSION (UK bank holiday; no UK100 bars) | n/a | Row describes a non-existent session |
| Tue 26 May | O | 10542.00 | 10531.9 | +10.1 | marginal fail |
| | H | 10548.00 | 10560.0 | -12.0 | fail |
| | L | 10450.00 | 10498.0 | -48.0 | fail |
| | C | 10468.00 | 10500.7 | -32.7 | fail (>15) |
| Wed 27 May | O | 10466.00 | 10487.7 | -21.7 | fail |
| | H | 10498.00 | 10523.5 | -25.5 | fail |
| | L | 10440.00 | 10460.6 | -20.6 | fail |
| | C | 10490.00 | 10507.9 | -17.9 | fail (>15) |
| Thu 28 May | O | 10492.00 | 10434.1 | +57.9 | fail |
| | H | 10510.00 | 10446.6 | +63.4 | fail |
| | L | 10470.00 | 10378.8 | +91.2 | fail |
| | C | 10505.00 | 10432.4 | +72.6 | fail (>15) |
| Fri 29 May | O | 10425.85 | 10434.7 | -8.9 | ok |
| | H | 10462.22 | 10462.0 | +0.2 | ok |
| | L | 10409.28 | 10409.2 | +0.1 | ok |
| | C | 10425.96 | 10410.0 (full-day 10368.2) | +16.0 (+57.8) | fail (>15) |
| Mon 1 Jun (D-1) | all | MISSING | 10371.9 / 10410.4 / 10286.2 / 10324.5 | n/a | D-1 session absent; stated "last close" is 101.5 pts above the true D-1 close |

The whole-number, round-figure values for 25-28 May (10470.00, 10465.00, 10545.00, 10542.00 ...) are not tied to any §4 evidence row (§4 evidences only the 29 May close and a May monthly range). They read as synthesised.

### 1b. RSI2
- Arithmetic from the report's own closes reproduces (22.2, 100.0, 16.0 on 27-29 May; qa_slice_stats `--closes` check). Trend labels follow the Close/Open + RSI2 rule on every row. Arithmetic is therefore transparent.
- Against the slice the values are wrong: cash RSI2 for 26 May-1 Jun is 100.00, 100.00, 8.71, 0.00, 0.00 (report 45.8, 22.2, 100.0, 16.0 on 26-29 May). RSI2 at D-1 (1 Jun) = 0.00, and is not reported.

### 1c. ATR14
- Never stated as a number anywhere in the report. It can only be inferred from "0.25xATR (~18 pts)" in the card, i.e. ~72 pts. Level file: ATR14 cash = 117.82 (full-day 138.69). Implied value is ~39% too low.

### 1d. Pivots (D = 2 Jun, `_cash` fields)
Daily - report derives from "prior session 28 May" (wrong session even by the report's own as-of 29 May; correct session is 1 Jun):
| Level | Report | Cash | Delta |
|---|---|---|---|
| R3 | 10560.00 | 10518.73 | +41.3 |
| R2 | 10535.00 | 10464.57 | +70.4 |
| R1 | 10520.00 | 10394.53 | +125.5 |
| P | 10495.00 | 10340.37 | +154.6 |
| S1 | 10480.00 | 10270.33 | +209.7 |
| S2 | 10455.00 | 10216.17 | +238.8 |
| S3 | 10440.00 | 10146.13 | +293.9 |

Weekly - report uses "prior week W/E 22 May"; the prior completed week for D is 25-29 May (2026-W22):
| Level | Report | Cash W22 | Delta |
|---|---|---|---|
| R3 | 11100.00 | 10701.60 | +398.4 |
| R2 | 10860.00 | 10630.80 | +229.2 |
| R1 | 10660.00 | 10520.40 | +139.6 |
| P | 10420.00 | 10449.60 | -29.6 |
| S1 | 10220.00 | 10339.20 | -119.2 |
| S2 | 9980.00 | 10268.40 | -288.4 |
| S3 | 9780.00 | 10158.00 | -378.0 |

Monthly - report uses "prior month April 2026"; the prior month for D is May 2026:
| Level | Report | Cash May | Delta |
|---|---|---|---|
| R3 | 11648.93 | 11018.40 | +630.5 |
| R2 | 11291.93 | 10789.20 | +502.7 |
| R1 | 10795.97 | 10599.60 | +196.4 |
| P | 10438.97 | 10370.40 | +68.6 |
| S1 | 9943.01 | 10180.80 | -237.8 |
| S2 | 9586.01 | 9951.60 | -365.6 |
| S3 | 9090.05 | 9762.00 | -672.0 |

The daily table is arithmetically self-consistent with its own stated 28 May inputs (P=(H+L+C)/3, R1=2P-L etc. reproduce), so the failure is the derivation session, not the formula. R4/R5/S4/S5 rows are extra to the R3-P-S3 requirement. All three tables are far outside the 10-pt tolerance on every level except weekly P (-29.6, still outside).

### 1e. Swings / range / counters
- 5-day swing: report 10,557 (Mon 25 May, a non-session) / 10,409; data high 10560.0 (26 May) / low 10286.2 (1 Jun).
- 25-session range: card states 10,082-10,935; data (cash) 10141.2-10560.0 (width 418.8). The 10,935 high is not in the data and also contradicts §9 ("toward the mid-10,500s") and §4 (May high 10,557).
- VIX "~15.7" (§14): slice closes 16.53 (29 May), 17.14 (1 Jun). USDX "~99.2 on 1 Jun" matches (99.193). S&P 500 "7,564 -> 7,580+" is consistent (29 May close 7581.1; 1 Jun 7600.2, not mentioned).
- Calendar: §13d omits scheduled-for-D events HIGH BoE Governor Bailey speech (17:00 broker = 15:00 UK), HIGH US JOLTS (17:00 broker = 15:00 UK), HIGH Eurozone CPI flash y/y (12:00 broker = 10:00 UK, consensus 2.6, prev 3.0), Eurozone unemployment change (10:00 broker = 08:00 UK). It lists "US ISM / payrolls run-in" as upcoming whereas ISM Manufacturing was scheduled 1 Jun. §13c omits the whole 1 Jun day (Powell speech HIGH, ISM Manufacturing, S&P Global PMIs).

## 2. Section 7 checklist
| Row | Item | Score | Notes and evidence |
|---|---|---|---|
| 1.1 | Variables respected | 2 | FTSE 100 cash primary, GBP, index points, counters USDX/S&P/DAX/EURO STOXX named (§2, §10). Fails: as-of is 29 May not D-1 = 1 Jun (§2, header); daily-open anchor "overridden to the 2 June session per instruction" with no converted time and not the 07:00 UK anchor (header, §20, card); source tiers (index provider / exchange / sell-side) not evidenced - only retail aggregators in §4. |
| 1.2 | Coverage and currency consistent | 1 | Data dated 29 May as "last close" while §10/§13a use 1 Jun items; weekly pivots from W/E 22 May, monthly from April, daily from 28 May - three different derivation sessions (§11); Mon 25 May shown as a session. |
| 1.3 | Audience and tone | 4 | Strategist tone, risk-aware; minor lapses ("cross-curric", "do not trade them" hedging). |
| 2.1 | Sections present and ordered | 4 | §1-§21 present in order incl. §13a-d, §21a, §21c, §21d. §21b has no heading (cards sit under bare "Trade 1/2/3" headings). §7 holds five caption placeholders (pandoc drops images - accepted, noted). |
| 2.2 | Scorecard as a table | 3 | §6 is a table but has no Source A / Source B / Final columns (only a Validation column). §11 tables run R5->S5 (five levels per side, R3->S3 required) - ordering otherwise correct. |
| 2.3 | Method steps visible | 4 | §4-§5 observation -> consensus; §8 candle-by-candle + sequence; §9 regime with overlap/persistence/VOLator/KER. Content rests on mis-stated bars. |
| 3.1 | Quantitative claims sourced | 2 | §1/§12/§14 carry Brent $91-95, WTI, gold $4,400-4,560, 2y UST 4.02%, ~46% Dec-hike odds, VIX 15.7 with no per-figure source or pointer to §4/§13; VIX is wrong vs slice. |
| 3.2 | Citations exist and consistent | 1 | (a) Yahoo 29 May is given as "10,425.96 delayed close" and "10,409.28 delayed close" for the same source/date - the second equals the report's own 29 May Low (10409.28), i.e. a Low labelled as a Close. (b) Trading Economics 29 May headline "FTSE edges up" is classed Bullish while §1 says the index closed down 0.75% that day. (c) §6 25 May row has no source and the session did not exist. Source existence cannot be fetched; the consistency failures are recorded here. |
| 3.3 | Calculations transparent | 3 | RSI2 reproducible from own closes; trend labels and §21a score (-0.06 = -0.25+0.10+0+0.06-0.015+0.045) reproduce; pivot formulas reproducible from stated inputs; KER 0.39 stated. ATR(14) never stated as a number (only ~18 pts = 0.25xATR implied, i.e. ~72 vs 117.82). |
| 3.4 | Numbers reconcile | 1 | Close 10,425.96 consistent in §1/§6/§8, but §3/§5 use 10,420; true D-1 close is 10324.5 (1 Jun). §9 "mid-10,500s" vs card 25-session high 10,935; card carries no D-1 reference close, no ATR; card range 10,082-10,935 vs data 10141.2-10560.0; report's own pivots (§11) are not the levels used on the card. Section 1 of this file: close wrong by >15 pts on 26, 27, 28, 29 May and by 101.5 pts vs the true D-1 close - a Category 3 failure to score. |
| 4.1 | Pillars conclude | 3 | §8 "Indecision - reversal risk", §9 "Neutral with a soft tilt", §10 "MIXED", §14 bullet-wise Neutral/Neutral-to-supportive. §12 sub-sections give only a one-line net for Energy; Monetary, Geopolitics and FX end without a direction label. |
| 4.2 | Cross-asset interpreted | 4 | §10 gives a mechanism per counter (dollar-earner translation, energy weight, US beta, euro-area industrial read). USDX mechanism is internally awkward (GBP strength framed as headwind while USDX "firming" is labelled neutral/mild contradict). |
| 4.3 | Synthesis reconciles tensions | 3 | §9 resolves KER (+0.39) vs short-term corrective into TRANSITION; §21a flags §17 vs KER. But §16 says range-bound, §17 says "resolving lower", §21 builds the only card on the upside; the long-biased card is not reconciled with a bearish short-term score (-0.25) and neutral composite. |
| 4.4 | Calibrated language | 3 | §17 is exactly one sentence but stacks "most likely ... resolving lower ... unless"; confidence (Low) stated in §3, not at §17. |
| 4.x | Card construction (protocol) | 2 | Trade 1 and Trade 2 SUPPRESSED rows correct in form (trigger and value stated, no ladder). Trade 3C fails several pre-emit checks (feedback items 3-10): range taken from the 5-day band not the 25-day boundary; no D-1 reference close printed; ATR not stated on the card and implied ATR wrong; R/ATR ratio absent; invalidation identical to the stop price; no anchor time; no point conversion; confirmed-break gate not met so the card should be a SUPPRESSED row. |
| 5.1 | Data dated, staleness flagged | 3 | Prices dated and single-source flagged; but staleness of the 29 May as-of vs 1 Jun D-1 not flagged, and unsourced 25-28 May O/H/L/C not individually flagged. |
| 5.2 | Assumptions up front | 2 | Indicative banner at top is good; anchor override named in header and §20 but no time, and the card does not restate the anchor; single-source propagation to the card is present in caveats. |
| 5.3 | Red flags surfaced | 3 | §12/§15 risks and the US-Iran event collision are carried into the card caveat; the scheduled HIGH events for D (EUR CPI flash 10:00 UK, BoE Bailey 15:00 UK, US JOLTS 15:00 UK) are missing from §13d and from card caveats. |
| 5.4 | Restrictions honoured | 1 | (i) A price row (25 May) is shown for a non-session and O/H/L/C for 25-28 May have no evidence row - synthesised prices presented as indicative-sourced. (ii) A user instruction is cited as authority for relaxing the corroboration gate and the anchor (header, §20: "user explicitly authorised an indicative report with leniency on price corroboration"; anchor "overridden ... per user instruction") - prohibited by the no-override rule. (iii) Module code "M5 strategy trace" and "v2.1 baseline; locked" appear in §20 (module code / framework identifier). (iv) A card (3C) is emitted although the suppression trigger "no confirmed break" fires. |

Category means: C1 = (2+1+4)/3 = 2.33 -> 2, then reduced one level for the restriction breach = **1**. C2 = (4+3+4)/3 = 3.67 -> **4**. C3 = (2+1+3+1)/4 = 1.75 -> 2, but the brief's rule that a close wrong by >15 pts (here four sessions plus the missing D-1 close) is a Category 3 failure to score gives **1**. C4 = (3+4+3+3+2)/5 = 3.0 -> **3**. C5 = (3+2+3+1)/4 = 2.25 -> **2**.

## 3. Category roll-up
| # | Category | Max | Level | Multiplier | Points | Justification |
|---|---|---|---|---|---|---|
| 1 | Prompt adherence | 20 | 1 | 0.20 | 4.0 | Wrong as-of session; no 07:00 UK anchor; restriction breach drops one level |
| 2 | Structural alignment | 20 | 4 | 0.85 | 17.0 | All sections present; §6 lacks Source A/B/Final columns; §21b heading absent |
| 3 | Accuracy and evidence | 25 | 1 | 0.20 | 5.0 | D-1 session absent; closes off 16-73 pts on four sessions; pivots from wrong sessions off by up to 672 pts; non-session row |
| 4 | Reasoning and judgment | 20 | 3 | 0.65 | 13.0 | Reasoning coherent on its own inputs; card construction non-compliant |
| 5 | Currency and transparency | 15 | 2 | 0.40 | 6.0 | Indicative flagging good; staleness, anchor, restrictions fail |
| | Total | 100 | | | 45.0 | |

## 4. Total, band, override
- total = 4.0 + 17.0 + 5.0 + 13.0 + 6.0 = 45 -> band **Low** (40-59).
- Override check: **restriction_breach** (see row 5.4: user-instruction authority cited for gate relaxation, module code in body, synthesised price row, card emitted against a fired suppression trigger). Effect: cap Moderate (74) - not binding at 45; C1 reduced one level (already applied above).
- hallucinated_source considered and not applied: no cited source was shown to be non-existent (the review cannot fetch). The Yahoo/10,409.28 and 25 May row inconsistencies are scored under 3.2 and 5.4. If a downstream reviewer treats them as fabricated, C3 = 0 and the total would be 40 (still Low).

## 5. Card Integrity (linter rows copied verbatim from `qa/ftse_qa1/lint_static/2026-06-02.csv`)
| card_id | strategy | flags | dud |
|---|---|---|---|
| 2026-06-02_Trade_1 | Trade 1 - Daily Directional | SUPPRESSED | False |
| 2026-06-02_Trade_2 | Trade 2 - Pivot (regime-aware) | SUPPRESSED | False |
| 2026-06-02_Trade_3C | Trade 3C - Momentum-Breakout (regime = TRANSITION) | CLEAN | False |

Per card: Trade 3C = 100 - 40x0 - 10x0 = 100; suppressed cards not scored. Report level (mean over 1 non-suppressed card) = 100. n_duds = 0, n_warns = 0. The static linter does not test pre-emit rows 1, 4, 5, 6, 10, 11 or the suppression trigger; those are in the feedback.

## 6. Feedback
See `qa/ftse_qa1/2026-06-02_feedback.md`.
