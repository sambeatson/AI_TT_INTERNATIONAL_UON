# Trust Score — Gold_Report_11_May_2026.md (D = 2026-05-11)
Run: `gold_regen_qa1` · Asset: XAUUSD · Reviewer: independent QA session (Stage 1)

Leak check: `data/levels/XAUUSD_by_date/2026-05-11.csv` → `last_bar_date=2026-05-08` < `date=2026-05-11`. OK to use.

## 1. Section 7 checklist

| Item | Notes | Evidence | Score |
|---|---|---|---|
| 1.1 Variables respected | Asset framed correctly (XAU/USD spot, LBMA loco-London; CME futures used for corroboration only in the labelling, though see 5.4 note on weighting). USDX first counter (§10). As-of = last completed session before D (Fri 8 May, correctly skipping non-trading Sun 10). Lookback 5d/25d stated. USD/oz. Six independent sources in §4/§20. Gap: tick size/tick name (required by `M1_Variables_v2_1.md` §[TICK_SIZE]/[TICK_NAME] when strategies are produced) is never explicitly stated — ticks are used consistently (implied $0.01/tick, verified: 90/9000=38/3800=82/8200=0.01) but never declared as a value. | §2, §4, §10, §20, §21b | 4 |
| 1.2 Coverage & currency consistent | Every date in §2/§6/§13/§21 is D−1 or earlier for data, D or later only in the forward-looking §13d/§16/§21c-labelled-as-backtest sections as expected. No USD/oz–tick–point unit drift; tick counts verified self-consistent throughout. | whole report | 5 |
| 1.3 Audience & tone | Senior Commodities Analyst — Precious Metals register held throughout; no retail tone. | §1, masthead, §18 | 5 |
| **C1 (mean, rounded)** | (4+5+5)/3 = 4.67 → **5** | | **5** |
| 2.1 Sections present & ordered | All of §1–§21 present in order, including §13a–d and §21a–d. §17 forecast is genuinely one sentence. | headings | 5 |
| 2.2 Scorecard as a table | §6 is a proper O/H/L/C/RSI2/Source A/Source B/Validation table. §11 weekly and monthly tables are correctly R3→P→S3 (three levels/side) per spec, but the **daily** table runs R5→P→S5 (five levels/side) — extra rows beyond the specified three-per-side format; ordering is still correctly high-to-low and no information is lost. | §6, §11 | 4 |
| 2.3 Method steps visible | §4→§5 show observation→normalization→consensus with the futures-to-spot contango adjustment stated; §8 is candle-by-candle; §9 covers persistence/overlap/VOLator/KER; §7 chart slots are captioned placeholders (acceptable per brief — conversion drops images). | §4–§9 | 5 |
| **C2 (mean, rounded)** | (5+4+5)/3 = 4.67 → **5** | | **5** |
| 3.1 Quantitative claims sourced | Most §1/§12/§14 figures carry a source (WGC, Deloitte, CME FedWatch, §4/§6/§13 pointers). Two claims are weakly/un-sourced: §14 VIX 17.19 has no citation, and "retail trader positioning per available aggregators ~68% long" cites no specific aggregator — this is the kind of vague "industry estimate" phrasing the framework flags under 3.1/3.2. | §12, §14 | 3 |
| 3.2 Citations exist & contain data | Spot-checked three: CME Group front-month (8 May, 5pm ET, 4,730.70 — corroborated by the separate Yahoo Finance row at the same 4,730.70), TradingEconomics §13a article (dated, named, quote consistent with the report's own ~3.5% Mon→Fri close move), Dukascopy §13a article (dated, named, Mixed classification matches its own hedged quote). No self-contradictory or impossible source found on this sample. | §4, §13a | 5 |
| 3.3 Calculations transparent | Pivot arithmetic is reproducible from the stated H/L/C (see 3.4 for which H/L/C). KER and §21a's Σ(signal×weight) (0.20+0.11+0.11=0.42) are shown. **ATR(14) is never stated anywhere in the report as an explicit figure** — it only appears implicitly via "R ≈ N×ATR" sanity-flag ratios in §21b, which back out to ATR≈USD 79.5–79.65/oz across all three cards (internally consistent with each other, but ~10–22% off both level-file ATR14 bases — see 3.4). **RSI(2) does not reproduce from the report's own five stated closes** using the framework's specified 2-period mean-gain/mean-loss formula: Wed/Thu/Fri all have two consecutive up-closes in the report's own §6 table (Mon→Tue +38, Tue→Wed +65, Wed→Thu +27, Thu→Fri +28 — no losses in any 2-day window from Tue onward), so mean loss = 0 and the formula gives RSI=100 for Wed, Thu and Fri, not the stated 82.7 / 78.9 / 85.2. Per the brief, this is a Category 3 failure regardless of the fact that the Friday value (85.2) happens to sit within tolerance of the level file's `rsi2_full` (88.32). | §6, §9, §11, §21a, §21b | 2 |
| 3.4 Numbers reconcile — incl. vs level file | Internally: D−1 close = 4,715 identical across §1/§3/§4/§6/§21b MARKET entry — consistent. Externally, checked against `data/levels/XAUUSD_by_date/2026-05-11.csv` (`_full` basis, matching the report's own "spot, loco London, T+2" claim): §6 OHLC all consistent (O diff 0.07, H diff 1.64, L diff 3.71, C diff 0.44 — all ≤0.09×ATR14_full=9.2, well inside tolerance). **§11's daily pivots are built from Thursday 7 May's H/L/C, not Friday 8 May's** (reproduced exactly: P=(4720+4630+4687)/3=4679.00, matching the report's stated daily P to the cent) — i.e. the whole daily pivot table is one session stale. Against `d_full_*`: P off by 36.50 (0.356×ATR), R1 off 21.30 (0.208×ATR), S1 off 43.65 (0.425×ATR), R2 off 14.15 (0.138×ATR), S2 off 58.85 (0.574×ATR), S3 off 66.00 (0.643×ATR) — all past the 0.115×ATR failure line (only R3 lands close, at 1.05, by numerical coincidence). **§11's weekly pivots are one full week stale** — the report uses "week ending 2 May" instead of the correct prior completed week (Mon 4–Fri 8 May, which is `w_full_period=2026-W19` in the level file, the week that actually precedes D). Weekly P off by 74.28 (0.724×ATR); every other weekly level is off by 30–183 points — a severe, uniformly-directioned failure. Monthly pivots (flagged SINGLE-SOURCE-INDICATIVE by the report itself) are close: P off 6.69 (0.065×ATR, discrepancy band, not a failure, and already caveated). Swing extremes used for Trade 3A (Mon low 4,490; Fri high 4,751) vs `swing_low_5d_full`=4,500.66 / `swing_high_5d_full`=4,764.75: diffs 10.66 and 13.75 — discrepancy band, not failures. None of this triggers the hallucination override (it is a wrong-period sourcing error, not an invented source), but it is a material, decision-relevant reconciliation failure — Trade 2's entire entry/stop/TP ladder is anchored to the wrong daily P (see feedback + C4). | §11, level file | 1 |
| **C3 (mean, rounded)** | (3+5+2+1)/4 = 2.75 → **3** | | **3** |
| 4.1 Pillars conclude | §8, §9, §10, §12, §14 each end with an explicit, content-consistent direction label. | those sections | 5 |
| 4.2 Peer/cross-asset interpreted | §10 gives mechanism (USDX inverse relationship, DAX risk-off safe-haven read, S&P dissent explained), not a bare correlation list. | §10 | 5 |
| 4.3 Synthesis reconciles tensions | §15/§16/§18 reconcile short- vs medium-term and §17 vs §21a explicitly ("No conflict with the §17 forecast — both lean bullish"); KER-vs-medium-regime tension is present but only lightly addressed (KER is only compared to the short-term read, not reconciled against the "Transitional, Mixed-to-Bullish" medium-term call). | §15–§18, §21a | 4 |
| 4.4 Calibrated language | §17 is exactly one sentence with a stated confidence (Medium) elsewhere; no hedge-stacking. | §3, §17 | 5 |
| Card construction (M5, per QA_PROTOCOL anchor — folded into C4) | Two concrete rule/consistency defects, neither caught by the static linter (which checks arithmetic side/order, not sourcing or procedural conformance): (a) **Trade 1's confluence row misstates its own numbers** — it claims TP1 (USD 4,805) sits "between daily R1 (4,728) and daily R2 (4,769)", but 4,805 > 4,769, i.e. TP1 is actually above daily R2, not between R1 and R2 (true under either the report's own wrong-period pivots or the corrected level-file pivots). (b) **Trade 3A's Unit 3 (runner) stop management deviates from the fixed M5 rule** — M5 requires the Unit 3 stop to move to entry ± 0.2R in the profitable direction on the Unit 2 fill; Trade 3A instead only adjusts its stop on a 100%-extension price break (a different trigger than "Unit 2 fill"), and even then only to USD 4,570.5 — essentially at the original stop (4,569), not to entry+0.2R (which would be ≈USD 4,667.4). Card Integrity itself (separate score) is unaffected since these are not among the linter's checked flags. | §21b Trade 1, Trade 3A; `cards/.../2026-05-11.json` notes | 3 |
| **C4 (mean incl. card construction, rounded)** | (5+5+4+5+3)/5 = 4.4 → **4** | | **4** |
| 5.1 Data dated; staleness flagged | Every price/article dated; Wed 6 May flagged 'indicative'; silver and monthly pivots flagged SINGLE-SOURCE-INDICATIVE. | §4, §6, §13, §19 | 5 |
| 5.2 Assumptions up front | Futures-to-spot normalization ($10–25 contango) is stated with its size in §4/§5/§19 — good. The as-of-date override IS logged in §20, but only at the very end of the report, not "up front" as the criterion asks. More materially: **the daily/weekly pivot period error (see 3.4) is nowhere disclosed as an assumption, override, or limitation** — the tables are labelled CORROBORATED with no caveat about which prior period was used. | §19, §20, §11 (absence) | 2 |
| 5.3 Red flags surfaced | Friday's upper-wick exhaustion is surfaced (§8→§15); retail positioning contrarian flag surfaced (§14→implicitly §15); CPI event-collision carried into all three cards' caveat rows. The pivot-period sourcing problem (a genuine red flag) is not surfaced anywhere. | §12, §15, §21b | 4 |
| 5.4 Restrictions honoured | No bracketed variable names or module codes found in the report body (checked directly). No un-normalized retail premium (JM Bullion explicitly reduced). Instrument common names used throughout. Minor note: CME front-month futures are given full Tier-1 weight *inside* the weighted-median that produces the primary consensus number, which sits close to (rather than clearly subordinate to) "corroboration only" — normalized first, and disclosed, so treated as a soft note rather than a breach. | whole report | 4 |
| **C5 (mean, rounded)** | (5+2+4+4)/4 = 3.75 → **4** | | **4** |

## 2. Category roll-up

| Category | Max | Level | Multiplier | Points | Justification |
|---|---|---|---|---|---|
| C1 Prompt adherence | 20 | 5 | 1.00 | 20.00 | All variables respected; only gap is tick size/name never explicitly declared (used consistently). |
| C2 Structure | 20 | 5 | 1.00 | 20.00 | All 21 sections present/ordered; daily pivot table carries two extra tiers beyond the R3→S3 spec, no info lost. |
| C3 Accuracy & evidence | 25 | 3 | 0.65 | 16.25 | OHLC/close reconcile tightly with the level file, but daily pivots are built from the wrong (Thursday, not Friday) prior session and weekly pivots from the wrong (one-week-stale) prior week — both fail tolerance badly and are undisclosed; ATR14 never stated explicitly; RSI(2) does not reproduce from the report's own stated closes. |
| C4 Reasoning & judgment | 20 | 4 | 0.85 | 17.00 | Pillars, cross-asset mechanism, synthesis and calibration are strong; card construction carries a self-contradictory confluence claim (Trade 1) and a Unit-3 stop-management rule deviation (Trade 3A). |
| C5 Currency & transparency | 15 | 4 | 0.85 | 12.75 | Dating and most red-flag surfacing are solid; the undisclosed pivot-period error and the buried as-of override are the main transparency gaps. |
| **Total** | 100 | | | **86.00 → 86** | |

## 3. Total, band, override

```
c1=5
c2=5
c3=3
c4=4
c5=4
total=86
band=High
override=none
card_integrity=100
n_cards=3
n_duds=0
n_warns=0
```

Override check: no fabricated/self-contradictory source found on the 3.2 spot-check (no hallucinated-source override). No prompt-level restriction is openly violated — the pivot-period error is a data-sourcing/reconciliation failure, already penalized through C3/C5, not a restriction breach — so no restriction-breach override applies. Band from total score: 86 → **High Trust (75–89)**.

## 4. Card Integrity (from `qa/gold_regen_qa1/lint_static/2026-05-11.csv`, copied verbatim)

| card_id | strategy | flags | dud | Card Integrity (100−40·DUD−10·WARN) |
|---|---|---|---|---|
| 2026-05-11_Trade_1 | Trade 1 — Daily Directional (direction-of-the-day expression) | CLEAN | False | 100 |
| 2026-05-11_Trade_2 | Trade 2 — Pivot (TREND_UP breakout, daily timeframe) | CLEAN | False | 100 |
| 2026-05-11_Trade_3A | Trade 3A — Momentum-Pullback | CLEAN | False | 100 |

Report-level Card Integrity (mean over non-suppressed cards) = **100**. n_cards=3, n_duds=0, n_warns=0. (Static integrity is clean; the two card-construction defects noted under C4 above are not linter-checked flags — sourcing/procedural issues, not stop-side/TP-order/R-magnitude arithmetic — so they do not change this score, per protocol.)
