# Trust Score — Gold_Report_20-May-2026.md (D = 2026-05-20, asset = XAUUSD, run = gold_regen_qa1)

Scored against `docs/AI_Output_Trust_Score_Framework_v3.7.txt` §4–§7, adapted per
`docs/QA_PROTOCOL_TRADE_CARDS.md` and `qa/gold_regen_qa1/REVIEWER_BRIEF.md`. Basis used throughout
Category 3: `_full` (the report claims "Spot, immediate settlement (loco London)" / "24-hour OTC
market" — a continuous basis), checked against `data/levels/XAUUSD_by_date/2026-05-20.csv`
(`last_bar_date` = 2026-05-19 < D = 2026-05-20, confirmed leak-free before use).

## 1. Section 7 checklist

| Row | Score | Evidence observed | Notes |
|---|---|---|---|
| 1.1 Variables respected | 3 | §2 table | Asset correctly scoped spot-not-futures (CME named "for corroboration" only, correct); USDX listed first counter; 6 sources in §4; lookback 5/25 correct. Gaps: no Tick Name/Tick Size row anywhere in §2 despite §21 strategy cards requiring it (M1_Variables §B); §2's "As-of date" field is labelled 20 May 2026 (the report/session date) rather than 19 May 2026, the "last completed session strictly before D" that M1_Variables_v2_1 defines `[AS_OF_DATE]` to be — even though §3's Basis field correctly uses 19-May close in practice. |
| 1.2 Coverage & currency consistent | 3 | §21b Trade 1, Trade 3C | Dates throughout are D−1 or earlier for data, D for the session — fine. Unit drift: Trade 1 stop cell states "Distance: 56.03 ticks above entry ... so distance = 5,603 ticks" — the $56.03 figure is dollars, mislabelled as ticks first. Trade 3C TP2 cell: "(+2R) — 4,450 ticks below entry" — 4,450 ticks = $44.50 = 1R, not 2R (the actual $89.00/2R level is correct, the label is wrong). |
| 1.3 Audience & tone | 3 | whole report, §2 | Tone reads institutional throughout (no retail language) but Purpose & Audience is never explicitly stated anywhere in §2 — the brief's "Senior Commodities Analyst — Precious Metals" register can only be inferred from tone, not confirmed against a declared variable. |
| 2.1 Sections present & ordered | 5 | headings §1–§21 | All 21 sections, all required sub-parts (§13a–d, §21a–d), present and correctly ordered. |
| 2.2 Scorecard as a table | 4 | §6, §11 | §6 is a genuine table but uses a single "Corrob." column (Dual/Single*) rather than the prescribed separate Source A / Source B / Validation columns. §11 pivot tables are correctly ordered R3→R2→R1→P→S1→S2→S3 for all three timeframes. |
| 2.3 Method steps visible | 4 | §4–§9 | §4–§5 show observation→normalisation→weighted-median consensus explicitly; §8 gives full candle-by-candle commentary; §9 gives regime + persistence/overlap/VOLator; §7 charts are unavailable but a caption/placeholder is given (accepted per brief, conversion loss not scored). Gap: §2 names CME front-month as available "for corroboration" but no futures-to-spot normalisation amount is ever actually shown applied anywhere in §4/§5/§21. |
| 3.1 Quantitative claims sourced | 4 | §1, §9, §12, §14 | Most figures in §1/§12/§14 are sourced or point to §4/§6/§13 (WGC, CME FedWatch, Yahoo, USAGOLD, etc.). Gap: the "January $5,602 record" figure in §9 carries no source. |
| 3.2 Citations exist & contain data | 4 | §4, §13a | 3-source spot-check (Trading Economics 18-May, USAGOLD 18-May, LiteFinance 19-May): all named, dated, none impossible or self-contradictory in a way that trips the hallucination override. Minor flag: Trading Economics' own §13a headline quotes "$4,550/oz" while §4 quotes the same source at "$4,542.49" for the same date — a $7.51 internal mismatch within one citation. |
| 3.3 Calculations transparent | 3 | §6, §9, §21a | RSI2 is a value-only column, no RS/gain-loss derivation shown. ATR14 ($88.63, used in the Trade 1 runner calc) is never derived or labelled as such anywhere in §9 (§9 gives only VOLator z-scores). §21a shows only the top 3 of presumably 6 weighted signal components (summing to −0.60 of the stated −0.62 total; ~0.02 unaccounted). |
| 3.4 Numbers reconcile (incl. vs level file) | 0 | §6, §11 vs `data/levels/XAUUSD_by_date/2026-05-20.csv` | Internally consistent (same D−1 close used in §1/§3/§4/§6/§21b) but externally fails pervasively: D−1 close $4,504.20 vs level file $4,482.06 (diff $22.14, > $12.18 fail threshold); D−1 low $4,486.86 vs $4,464.95 (diff $21.91, > $21.18 fail threshold); RSI2 0.0 vs 24.78 (diff 24.78, > 15 fail threshold). §11's daily pivot table was built from **18-May H/L/C, not the correct 19-May (D−1) session** — confirmed by reverse-computing P=(4585.20+4525.00+4570.50)/3=$4,560.23 exactly matching the printed value; all 7 daily pivot levels miss the level file by $15.6–$164. Weekly pivots use the correct period label (W/E 15 May = ISO W20, matching the level file's `w_full_period`) but 5 of 7 levels miss by $52–$318. Monthly P is within the discrepancy band ($9.64) but R1/S1/R2/S2/R3/S3 miss by $141–$640. This is a near-total failure of the level-file reconciliation Category 3 exists to test — see feedback items 1–3. |
| 4.1 Pillars conclude | 4 | §8–§10, §12, §14 | §8 ends "BEARISH CONTINUATION"; §9 "Bias: BEARISH"; §12 labels each factor (e.g. "Demand — price-negative"); §14 labels each bullet. §10 gives per-counter Confirm/Contradict labels but no single closing direction label for the section as a whole. |
| 4.2 Peer/cross-asset interpreted | 4 | §10 | Genuine mechanism given (real-yield channel dominating the USDX channel; simultaneous real+nominal sell-off explained for S&P) rather than a bare correlation list. DAX row is comparatively thin. |
| 4.3 Synthesis reconciles tensions | 4 | §15, §16, §18, §21a | USDX-vs-yields decoupling is explicitly flagged and not glossed over; §21a states "Conflict flag with §17: NONE" with reasoning; §16 checks regime consistency explicitly. |
| 4.4 Calibrated language | 4 | §3, §17, §18 | §17 is exactly one sentence; confidence stated H/M/L-style ("Medium" §3, "MEDIUM" §18); conditional framing used throughout for the FOMC scenarios. |
| 5.1 Data dated; staleness flagged | 4 | §4, §6, §13, §19 | All prices/articles dated; 19-May close and monthly H/L/C both explicitly flagged single-source-indicative. |
| 5.2 Assumptions up front | 3 | §2, §19, §20, §21b | Anchor override stated consistently on card, in §20, and in §2 (compliant handling — see §2 below). Single-source pivot propagation caveat correctly carried into the Trade 2 card. Gap: no futures-to-spot normalisation amount is ever shown being applied, only implied as available. |
| 5.3 Red flags surfaced | 4 | §12, §13d, §15, §21b | FOMC/Iran/physical-demand risks surfaced in §12/§15; event collisions carried into the Trade 1 and Trade 3 caveats. Gap: Trade 2's caveat covers only the pivot-corroboration flag, not the FOMC-Minutes collision the other two cards flag. |
| 5.4 Restrictions honoured | 0 | §11, §19, §20, §21b | Openly and repeatedly breached: the bracketed instance variable `[DAILY_OPEN_ANCHOR]` appears verbatim in §20; the internal module code "M5" ("M5 trace…", "M5 §10…") appears five times across §11, §19, §20 and the §21b Trade 2 caveat. The brief's restriction explicitly bars bracketed variable names and module codes (M1..M5) from the report body — this recurs across four sections, not a single slip. **Triggers the restriction-breach override.** |

## 2. Category roll-up

| Cat | Max | Level | Multiplier | Points | Justification |
|---|---|---|---|---|---|
| C1 Prompt adherence | 20 | 2 | 0.40 | 8.0 | Row average (3,3,3)→3, reduced by the mandatory ≥1-level cut for the restriction-breach override (§6 of framework). |
| C2 Structural alignment | 20 | 4 | 0.85 | 17.0 | Row average (5,4,4)→4.33→4. All sections present/ordered; minor table-column and method-transparency gaps. |
| C3 Accuracy & evidence | 25 | 1 | 0.20 | 5.0 | Row average (4,4,3,0)→2.75, deliberately taken to the lower level (framework §9: "pick the lower rubric level when in doubt") given 3.4's severity — the D−1 OHLC, RSI2 and every pivot tier fail level-file reconciliation, several by 5–15× the failure threshold, and the daily pivot table is demonstrably built from the wrong prior session. |
| C4 Reasoning & judgment | 20 | 3 | 0.65 | 13.0 | Pillar rows average 4.0 (strong synthesis, calibrated language), pulled down to 3 by card-construction defects on all three cards (see below) — card construction is scored under this category per the brief. |
| C5 Currency & transparency | 15 | 2 | 0.40 | 6.0 | Row average (4,3,4,0)→2.75, taken to the lower level given 5.4 is the row that triggers the override — same rationale as C3. |

**Total = 8.0 + 17.0 + 5.0 + 13.0 + 6.0 = 49 → 49/100.**

## 3. Total, band, override

```
c1=2
c2=4
c3=1
c4=3
c5=2
total=49
band=Low
override=restriction_breach
card_integrity=96.67
n_cards=3
n_duds=0
n_warns=1
```

Band: **Low Trust (40–59)**.

Override check: the restriction-breach override (bracketed `[DAILY_OPEN_ANCHOR]` + repeated "M5" module
codes in the report body) is triggered and applies: Category 1 was reduced by one rubric level
(3→2, already reflected above) and the band is capped at Moderate (60–74). Since the raw computed
total (49) already sits below the Moderate floor, the cap does not move the band upward — the band
remains Low Trust as computed. The hallucinated-source override was **not** triggered: the 3-source
spot-check (Trading Economics, USAGOLD, LiteFinance) found no source that was fabricated,
self-contradictory or impossible — Category 3's very low score reflects factual/reconciliation
failure against the level file, not sourcing fabrication.

Anchor note (positive finding, not a defect): the report explicitly names its daily-open anchor
(00:00 UK), labels it "(override)" in §2, and logs it in §20 with the same converted time carried
onto every card's `anchor_broker` field — this is the compliant handling the brief asks reviewers to
check for, independent of the bracket/module-code leak noted in row 5.4.

## 4. Card Integrity (linter rows, copied verbatim from `qa/gold_regen_qa1/lint_static/2026-05-20.csv`)

| card_id | strategy | flags | dud | integrity score |
|---|---|---|---|---|
| 2026-05-20_Trade_1 | Trade 1 — Daily Directional | CLEAN | False | 100 |
| 2026-05-20_Trade_2 | Trade 2 — Pivot (regime-aware), TREND-DOWN variant | CLEAN | False | 100 |
| 2026-05-20_Trade_3C | Trade 3 — Momentum-Breakout (3C variant) | WARN_TP3_ORDER | False | 90 |

Card Integrity (report level) = mean(100, 100, 90) = **96.67** (n_cards=3, n_duds=0, n_warns=1). This is
separate from the 100-point Trust Score above. Note that "CLEAN"/low WARN counts here reflect only
the linter's static, leak-free structural checks (stop side, TP order, R sizing) — they do **not**
capture the card-construction rule violations found in Category 4 below (missing ATR stop buffer on
Trade 1, TREND-DOWN formula not applied on Trade 2, undefined hybrid variant on Trade 3C), which are
methodology mismatches against M5, not static-integrity breaks.
