# Trust Score — Gold_Report_24_July_2026.md (D = 2026-07-24, run gold_regen_qa1)

Framework v3.7, mapped per `docs/QA_PROTOCOL_TRADE_CARDS.md` and `qa/gold_regen_qa1/REVIEWER_BRIEF.md`.
Level file: `data/levels/XAUUSD_by_date/2026-07-24.csv` (`last_bar_date=2026-07-23` < D — leak-free,
verified). Basis used for comparison: `_full` (report describes "Spot, immediate settlement," "OTC
London spot, T+2 settlement (loco London)," "Global — spot gold is a continuous 24-hour market" — a
continuous-market description, not a US-session one, so `_full` columns are the correct basis per
brief §4). `_cash` was checked where noted; the report's own RSI2 fits `_cash` far better than `_full`,
which is itself a finding (see 3.4).

## 1. Section 7 checklist

| Item | Notes | Evidence | Score |
|---|---|---|---|
| 1.1 Variables respected | Asset/spec/basis/unit/currency/tick size all correctly stated (XAU/USD spot, not COMEX GC, with futures declared corroboration-only per §2); USDX is the first counter in §10; as-of = 23 Jul close = D-1; lookback 5/25 stated and used; 8 obs / 6 providers satisfies the ≥6-source minimum; ticks used consistently (82.76 USD = 8,276 ticks etc., all verified exact at $0.01/tick). One real gap: §2 declares "CME front-month futures used for cross-validation" as part of the Asset variable, but no futures price ever appears in §4, §5 or §19 — the declared source is never actually exercised anywhere in the report | §2, §4, §19 | 4 |
| 1.2 Coverage & currency consistent | Every date in §2/§6/§13/§21 is D-1 or earlier for data, D for the session; §13d correctly uses forward dates for the calendar, not data; no USD/oz-vs-tick unit drift anywhere | whole report | 5 |
| 1.3 Audience & tone | Institutional register throughout; footer matches the mandated "[Asset] [Report Type] │ [Date] │ [Role]" format exactly | §1, §18, footer | 5 |
| **C1 mean** | (4+5+5)/3 = 4.67 → **level 5** | | |
| 2.1 Sections present & ordered | All of §1–§21 present, correctly ordered, all sub-sections (§13a–d, §21a–d) present | headings | 5 |
| 2.2 Scorecard as table | §6 is a proper table with the required columns. §11: the daily pivot table correctly prints all 5 levels each side (R5→P→S5, per `modules/M3_Technical_Module_v2_1.md` line 162's mandatory row order). But weekly and monthly pivots are combined into a single table showing only 3 levels each side (R3→P→S3) — both a departure from "one table per active timeframe" (M3 line 160) and from the mandatory R5→S5 row order used correctly for daily | §6, §11 | 3 |
| 2.3 Method steps visible | §4–§5 show observation→normalisation→consensus (no futures-to-spot adjustment needed or claimed, consistent with no futures actually being used, see 1.1); §8 is a clean candle-by-candle read; §9 covers regime, ATR, expanding-range read and KER with an explicit conflict-resolution rule; 4 chart captions present (accepted per brief). Minor gap: KER is named with its period (13) but the EMA-3 smoother parameter is never stated | §4–§9 | 4 |
| **C2 mean** | (5+3+4)/3 = 4.0 → **level 4** | | |
| 3.1 Quantitative claims sourced | Most §1/§12/§14 figures point to §4/§6/§13/§19. But the central-bank reserve figures in §12 (China +7.16t to 2,313.46; India +0.34t to 880.52; Russia −21.77t) carry no named source or date anywhere in the report, unlike every other quantitative claim | §12 | 3 |
| 3.2 Citations exist & contain data | Spot-checked Trading Economics (23 Jul, 4,056.85), FXStreet (23 Jul, 4,050.00), JM Bullion (22:26, 4,063.09): all named, dated, and used consistently between §4 and §13a. No self-contradiction or fabrication found on this check | §4, §13a | 5 |
| 3.3 Calculations transparent | Pivot formulas fully reproduce from the report's own stated H/L/C (R1=2P−L, S1=2P−H, R2=P+(H−L), S2=P−(H−L), R3=H+2(P−L), S3=L−2(H−P) all check exactly, including the R2−P=P−S2=H−L self-check identity). §21a's −0.43 score reproduces exactly from the six listed signal contributions (sum = −0.431). But RSI2 does **not** reproduce from the report's own five stated closes: using RS = mean gain/mean loss over the last 2 periods on the closes in §6, 22 Jul's change sequence (+60.13, +58.55, then −73.74 into 23 Jul) implies RSI2(22 Jul) should be 100 (two straight gains, zero losses) not the stated 88.7, and RSI2(23 Jul) should be ≈44.3 (mean gain 29.28 / mean loss 36.87) not the stated 36.6. ATR(14)=78.50 is explicitly disclosed as a "blended estimate," not derived transparently. KER's EMA-3 smoother is never stated | §6, §9, §21a | 2 |
| 3.4 Numbers reconcile (incl. vs level file) | Internally: D-1 close (4,056.85) identical across §1/§3/§4/§6/§21b MARKET entry. §11 daily pivots match the report's own §6 H/L/C exactly. But §21b Trade 3A is built on the fib swing 4,036.00→4,165.00 (129.00 = 1.64×ATR) — the exact swing §20's own Agent Log records as having **failed** the 2×ATR qualifying gate at the default 4-session lookback; the swing §20 logs as having *passed* at the 5-session lookback is 4,003.72→4,165.00 (161.28 = 2.05×ATR), a different low endpoint the card never uses. Externally, against the level file: D-1 close (diff 7.39), D-1 open (diff 11.75) and daily R1/R2 (diffs 6.37/5.34) sit in the discrepancy band; D-1 high/low and daily P/S1/S2/S3 are consistent; daily **R3 fails** (4,225.12 vs 4,214.47, diff 10.65 > 0.115×atr14_full = 10.11). RSI2 is within tolerance of both level-file bases (diff 2.71 vs `rsi2_full`, diff 0.002 vs `rsi2_cash` — suspiciously exact against the cash figure despite the report claiming a continuous/full basis, worth noting as a basis-consistency flag even though it passes the numeric tolerance). ATR(14)=78.50 vs `atr14_full`=87.9536 is a 10.75% relative gap — discrepancy band, not failure | §6, §11, §20, §21b, level file | 2 |
| **C3 mean** | (3+5+2+2)/4 = 3.0 → **level 3** | | |
| 4.1 Pillars conclude | §8/§9/§10/§14 each reach clear, well-defended direction labels; §12 implies bearish throughout its subsections without one explicit summary sentence. The §21 strategy pillar has two material construction failures: (a) Trade 2 is labelled "trend branch" under the report's own TREND_DOWN regime call, but is built as a sell-limit fade at daily R1 — `modules/M5_Strategies_Module_v2_1.md` §5.2 is explicit that in TREND, "Trade 2 follows the trend across the pivot," not a fade, and names this exact pattern ("a mean-reversion limit under TREND or TRANSITION") as "a construction defect even when the resulting levels are internally consistent"; (b) Trade 3A enters at a 50% retracement when §5.3a fixes entry at "57.5% retracement of the swing," and the fib swing itself is the wrong one (see 3.4) | §9, §21a, §21b | 1 |
| 4.2 Peer/cross-asset interpreted | §10 gives an explicit mechanism per counter (dollar-denomination, real-yield channel resolving the equity contradiction), not a correlation list | §10 | 5 |
| 4.3 Synthesis reconciles tensions | §9 explicitly reconciles KER (trending) vs the choppy 5-session tape with a stated precedence rule; §10/§14/§15/§16/§18 consistently carry forward and resolve the equity-counters-contradict-haven-mechanism tension via the real-yield channel. §17 vs §21a agreement is noted but there was no real tension to resolve there | §9, §10, §14–§18 | 4 |
| 4.4 Calibrated language | §17 is exactly one sentence, no hedge stacking; confidence (Medium) stated and reasoned in §3 and §18 | §3, §17, §18 | 5 |
| **C4 mean** | (1+5+4+5)/4 = 3.75 → **level 4** | | |
| 5.1 Data dated; staleness flagged | Every price/article dated; §19 explicitly flags weekly/monthly pivots and moving averages as single-source, and ATR as a derived/indicative estimate | §4, §6, §13, §19 | 5 |
| 5.2 Assumptions up front | Anchor override handled reasonably: §20 Agent Log names it "Session anchor override" / "an instructed deviation," §2 states 00:00 UK, and all three cards carry the same converted broker time (02:00), satisfying the module's "same converted time on the card, in the handoff record and in the report body" test — though §2's own framing ("has been set to 00:00 UK for this run") reads as a fresh run-time choice rather than a disclosed departure from a named prior value, so the non-conformance is logged but not fully explained. Single-source pivot propagation into card caveats is done correctly (Trade 2 explicitly flags weekly R1 as single-source-indicative and states it is not used as an anchor) | §19, §20, §21b | 4 |
| 5.3 Red flags surfaced | §12/§15 risks well surfaced; §13d's in-session PMI collision is explicitly carried into the Trade 1 and Trade 3A caveats. But the Trade 2 branch-geometry violation (4.1) is a material methodology red flag that is nowhere disclosed as such — the card presents its fade structure as a deliberate, sound design choice | §12, §15, §21b | 3 |
| 5.4 Restrictions honoured | No module codes (M1–M5), bracketed variable names, or framework name found anywhere in the report body (full-text scan); no retail-premium OHLC left un-normalised; futures declared corroboration-only (and, per 1.1, simply unused rather than misused); common instrument names used throughout | whole report | 5 |
| **C5 mean** | (5+4+3+5)/4 = 4.25 → **level 4** | | |

## 2. Category roll-up

| # | Category | Max | Level | Multiplier | Points | Justification |
|---|---|---|---|---|---|---|
| 1 | Prompt adherence | 20 | 5 | 1.00 | 20.0 | All Variables respected; only gap is a declared-but-unused futures cross-validation source |
| 2 | Structural alignment | 20 | 4 | 0.85 | 17.0 | All sections present/ordered; §11 weekly/monthly pivot tables depart from the module's mandatory format used correctly for daily |
| 3 | Accuracy & evidence | 25 | 3 | 0.65 | 16.25 | Pivots and the §21a score reproduce exactly, but RSI2 does not reproduce from the report's own closes, daily R3 fails the level-file tolerance test, and Trade 3A's fib swing contradicts the report's own Agent Log |
| 4 | Reasoning & judgment | 20 | 4 | 0.85 | 17.0 | Strong narrative synthesis and cross-asset mechanism, but the §21 strategy pillar contains a material regime/branch construction defect on Trade 2 and a fixed-parameter miss on Trade 3A |
| 5 | Currency & transparency | 15 | 4 | 0.85 | 12.75 | Good staleness and red-flag disclosure generally; the Trade 2 branch-geometry defect is not itself flagged as a red flag |

Total = 20.0 + 17.0 + 16.25 + 17.0 + 12.75 = **83.0 → 83**

## 3. Total, band, override

c1=5
c2=4
c3=3
c4=4
c5=4
total=83
band=High (75-89)
override=none

card_integrity=100
n_cards=3
n_duds=0
n_warns=0

Override check: no fabricated/hallucinated source found on the 3-citation spot-check (3.2) →
hallucinated-source override does not apply. No module code, bracketed variable, or framework name
found in the report body (5.4) → restriction-breach override does not apply. The Trade 2 branch-geometry
defect (4.1) is a methodology non-conformance within the strategy module, not an open breach of a
prompt-level restriction stated to the reviewer, so it is scored directly in C4/C5 rather than
triggering the override.

## 4. Card Integrity (linter rows, copied verbatim from `qa/gold_regen_qa1/lint_static/2026-07-24.csv`)

| card_id | strategy | flags | dud | card score |
|---|---|---|---|---|
| 2026-07-24_Trade_1 | Trade 1 — Daily Directional | CLEAN | False | 100 |
| 2026-07-24_Trade_2 | Trade 2 — Pivot (regime-aware, trend branch: fade the counter-trend rally into resistance) | CLEAN | False | 100 |
| 2026-07-24_Trade_3A | Trade 3 — Momentum-Pullback (3A) | CLEAN | False | 100 |

Report-level card integrity = mean over non-suppressed cards (all 3 live) = (100+100+100)/3 = 100.
The static linter checks structural inequalities only (stop side, TP order, R size) and cannot detect
the regime-branch or fixed-parameter defects found in Category 4 above — those are real construction
defects not visible to Card Integrity, which is why they are scored separately under C4/C5 rather than
assumed to be covered by a clean linter pass. Card Integrity is separate from the 100-point Trust Score
total above.

Feedback: see `qa/gold_regen_qa1/2026-07-24_feedback.md`.
