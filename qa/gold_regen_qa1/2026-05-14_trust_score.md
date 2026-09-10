# Trust Score — Gold_Report_14_May_2026.md (D = 2026-05-14, RUN_ID = gold_regen_qa1)

Framework: `docs/AI_Output_Trust_Score_Framework_v3.7.txt` §4–§7, anchors per `docs/QA_PROTOCOL_TRADE_CARDS.md`
and `qa/gold_regen_qa1/REVIEWER_BRIEF.md`. Basis used for Category 3: `_full` (report states "Spot, immediate
settlement (loco London)", a 24-hour continuous basis), checked against `data/levels/XAUUSD_by_date/2026-05-14.csv`
(`last_bar_date` = 2026-05-13 < D, confirmed leak-free).

## 1. Section 7 checklist

| Row | Notes | Evidence observed | Score (0–5) |
|---|---|---|---|
| 1.1 Variables respected | Asset correctly XAU/USD spot loco London, not COMEX (§2); CME GC=F used as corroboration only, normalised (§4/§5/§19); USDX is the first counter in §10; ≥6 sources satisfied (§4, 6 core + 1 excluded); ticks stated and used consistently in §21b. Deviation: lookback window is stated as "5 trading days (08 May – 14 May 2026)" — includes D itself as the 5th session, whereas the fixed as-of rule (brief §2 row 1.1) requires the window to end strictly before D. | §2, §4, §10, §21b | 4 |
| 1.2 Coverage & currency consistent | USD/oz used throughout, no unit drift. Same D-day inclusion issue as 1.1: §1/§6/§8 treat 14 May's intraday print as the current session inside the 5-session table rather than as supplementary context outside the as-of window. Mitigated by explicit "provisional pending settlement" flagging (§6 note, §19). | §1, §6, §8, §19 | 4 |
| 1.3 Audience & tone | Senior Commodities Analyst — Precious Metals register maintained throughout; no retail tone. | §1, §18 | 5 |
| 2.1 Sections present & ordered | All of §1–§21 present, correctly ordered, with §13a–d and §21a–d sub-sections present. | headings | 5 |
| 2.2 Scorecard as a table | §6 matches the spec exactly (Session/O/H/L/C/RSI2/Source A/Source B/Validation). §11: brief specifies pivot tables "ordered R3→P→S3 (three levels each side)"; the report instead gives R5→P→S5 (five levels each side) for all three of daily, weekly and monthly — a consistent structural deviation from the specified table shape. | §6, §11 | 3 |
| 2.3 Method steps visible | §4–§5 show observations → normalisation → consensus with the futures-to-spot contango stated; §8 is candle-by-candle; §9 states overlap ratio, persistence, VOLator slope and KER. §7 charts suppressed with an explicit note per the allowed docx→md conversion exception — not scored down. | §4–§9 | 5 |
| 3.1 Quantitative claims sourced | §4/§13 well sourced. §12 mixed: several rows (Supply "mine output stable QoQ", Substitution/spread ratio math) carry no dated source, only "(per WGC commentary)" on one row; §14 mostly sourced (CFTC positioning cited). | §12, §14 | 3 |
| 3.2 Citations exist & contain data | Spot-checked 3: USAGOLD (§4 + §13a #3) — named, dated, consistent figures across both uses. CME GC=F (§4 + §6 + §19) — named, dated, consistent contango treatment. CNBC/Wells Fargo recap (§13a #7) — named, dated "12 May 2026 (cited Apr 16 note)"; the compound date is unusual but not self-contradictory or impossible. No fabrication found; no override triggered. | §4, §13a | 4 |
| 3.3 Calculations transparent | Fails on reproducibility, self-contained (report's own inputs) and externally: (a) RSI2 for 12/13/14 May does not reproduce from the report's own 5-session closes (correct value is 0 in all three cases — see feedback #4); (b) daily pivots R1/S1/R3/S3 do not reproduce from the report's own stated 13-May H/L/C via the fixed pivot formula (P and R2/S2 do); (c) weekly and monthly pivot tables fail to reproduce from their own stated H/L/C on nearly every tier, by up to $375 (monthly R3) — see feedback #1–3; (d) ATR(14) stated as $52/oz in the Trade 1 card is unsupported and far off both level-file bases. | §6, §8, §11, §21b | 1 |
| 3.4 Numbers reconcile — incl. vs level file | Internal: §16 mislabels the monthly Pivot ($4,608, per the report's own §11 table) as "monthly R1" (actual monthly R1 per §11 = $4,718) — a direct self-contradiction. D−1 close is reasonably consistent across §3/§4/§6/§21b (4,688–4,690, within tolerance). External vs `XAUUSD_by_date/2026-05-14.csv`: daily pivots mostly within tolerance (P/R2/S2 consistent; R1/S1/R3/S3 in the "discrepancy" band, $4.08–$8.86 off); RSI2 fails (>15pt gap vs rsi2_full=0.0 on 3 sessions); ATR14 fails (48.7% relative error vs atr14_full); weekly pivots fail on every tier (e.g. P off $77.72, S3 off $289.27, all > the $11.65 failure threshold); monthly pivots fail on every tier (P off $65.69, R3 off $252.20). | §11, §16, §21b + level file | 1 |
| 4.1 Pillars conclude | §8 ends "Indecision — with a downside skew"; §9 ends "Bias: Bullish"; §10 has a per-row Implication column plus an overall contradiction-flag paragraph; §12 has a Direction column per row; §14 ends each subsection with "Net effect on Gold: …". All conclude. | §8, §9, §10, §12, §14 | 5 |
| 4.2 Peer/cross-asset interpreted | §10 gives a stated mechanism per counter (real-yield/liquidity channel for USDX, safe-haven channel for DAX, rotation read for Silver) rather than a bare correlation list. | §10 | 5 |
| 4.3 Synthesis reconciles tensions | §15/§16/§18 and §21a explicitly reconcile short- vs medium-term reads and flag (and resolve) the KER-vs-conviction tension. Weakened by the §16 monthly-pivot mislabel (defect above) feeding directly into the synthesis language, and by the runner-stop rule violation on 2 of 3 cards (see 4-row below / feedback #6), which is scored under Category 4 per the brief's card-construction note. | §15–§18, §21a, §21b | 3 |
| 4.4 Calibrated language | §17 is exactly one sentence, not hedge-stacked. Confidence stated as Medium in §3 and §18. | §3, §17 | 5 |
| 5.1 Data dated; staleness flagged | Every price/article in §4/§6/§13 is dated; 14 May intraday figures explicitly flagged "provisional pending session settlement". | §4, §6, §13, §19 | 5 |
| 5.2 Assumptions up front | Futures-to-spot normalisation stated with its size (~$11 contango, §5/§19). Single-source pivot propagation is carried into Trade 2's card (explicit SINGLE-SOURCE-INDICATIVE flag, §21b). The daily-open anchor override is logged in §20 as a non-conformance against the original 29-Apr instance date, with the anchor TIME itself (00:00 UK) stated as unchanged — compliant handling per the brief's explicit test. Minor gap: the override is not restated on the Trade 1 card itself, only in §20. | §19, §20, §21b | 4 |
| 5.3 Red flags surfaced | §12/§15 carry explicit risk rows (India duty shock, USDX headwind, Iran de-escalation risk); §13d upcoming-calendar collisions (Michigan print, PBoC data) are carried into card invalidation/caveats. | §12, §15, §21b | 5 |
| 5.4 Restrictions honoured | §19 explicitly states "No price was synthesised". No bracketed variable names or module codes (M1..M5) found in the report body; no framework name leaked; instrument common names used throughout; futures used corroboration-only and normalised. | whole report | 5 |

## 2. Category roll-up

| # | Category | Max | Mean of rows | Level (0–5) | Multiplier | Points | Justification |
|---|---|---|---|---|---|---|---|
| 1 | Prompt adherence | 20 | (4+4+5)/3 = 4.33 | 4 | 0.85 | 17.0 | Asset/sources/counters/ticks all correct; the D-day-inside-lookback deviation is disclosed, not silent. |
| 2 | Structure | 20 | (5+3+5)/3 = 4.33 | 4 | 0.85 | 17.0 | Section set/order perfect and §6 table correct; §11 pivot tables consistently over-extended (5 tiers/side vs the specified 3). |
| 3 | Accuracy & evidence | 25 | (3+4+1+1)/4 = 2.25 | 2 | 0.40 | 10.0 | Daily-close/daily-P/R2/S2 and sourcing are sound and no fabrication found, but RSI2 never reproduces, weekly/monthly pivots fail internal *and* external reconciliation on almost every tier, and the stated ATR14 is ~49% off. |
| 4 | Reasoning & judgment | 20 | (5+5+3+5)/4 = 4.5 → 4 | 4 | 0.85 | 17.0 | Pillars conclude, cross-asset mechanism is real, language calibrated; synthesis and card-construction quality docked for the §16 pivot mislabel and the wrong-side runner stop on 2 of 3 cards (rounded down per "pick the lower level when in doubt"). |
| 5 | Currency & transparency | 15 | (5+4+5+5)/4 = 4.75 | 5 | 1.00 | 15.0 | Dating, assumption disclosure, red-flag surfacing and restriction discipline are all strong; only a minor gap on restating the anchor override at card level. |

## 3. Total, band, override

```
c1=4
c2=4
c3=2
c4=4
c5=5
total=76
band=High
override=none
card_integrity=100
n_cards=3
n_duds=0
n_warns=0
```

Total = 17.0 + 17.0 + 10.0 + 17.0 + 15.0 = 76 → **High Trust (75–89)**.
Override check: no fabricated source found on the 3-source spot-check (3.2); no explicit prompt restriction openly
violated (the pivot/RSI2/ATR errors are calculation failures, not fabricated sourcing or a stated restriction being
broken) → **override = none**.

## 4. Card Integrity (linter rows, copied verbatim from `qa/gold_regen_qa1/lint_static/2026-05-14.csv`)

| card_id | strategy | flags | dud | integrity (100 − 40·DUD − 10·WARN) |
|---|---|---|---|---|
| 2026-05-14_Trade_1 | Trade 1 — Daily Directional (00:00 UK anchor, 14 May 2026) | CLEAN | False | 100 |
| 2026-05-14_Trade_2 | Trade 2 — Regime-aware Pivot (indicative) | CLEAN | False | 100 |
| 2026-05-14_Trade_3C | Trade 3 — Complex (3C transition breakout) | CLEAN | False | 100 |

Report-level Card Integrity (mean over non-suppressed cards) = **100**. This is a static, leak-free, mechanical
score (stop side / TP order / R-size checks only) and is separate from the 100-point Trust Score above; it does
not capture the runner-stop direction defect noted under Category 4 (see feedback #6), since that rule is not
among the fields the static linter checks.

## 5. Feedback

See `qa/gold_regen_qa1/2026-05-14_feedback.md`.
