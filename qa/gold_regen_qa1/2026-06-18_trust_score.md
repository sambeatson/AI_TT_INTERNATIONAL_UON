# Trust Score — Gold_Report_18Jun2026.md (D = 2026-06-18, run gold_regen_qa1)

Reviewer basis for Category 3: report claims "Spot, loco London, T+2" / 24-hour OTC market →
checked primarily against the `_full` columns of `data/levels/XAUUSD_by_date/2026-06-18.csv`
(`_cash` cross-checked; both fail by comparable margins). `last_bar_date` = 2026-06-17 < D — verified
leak-free.

## 1. Section 7 checklist

| Row | Notes | Evidence | Score |
|---|---|---|---|
| 1.1 Variables respected | Asset/basis/counter/as-of/lookback/unit/source-count all correct (7 sources ≥6, USDX first counter, spot loco-London not GC=F, as-of = 17 Jun close). **Gap**: tick size/name never explicitly declared anywhere (only implied by "$X / Y ticks" math in §21b, which is internally consistent at $0.01/tick but never stated as a variable) — required by M1 §B when strategy cards are produced. | §2, §4, §10, §21b | 3 |
| 1.2 Coverage & currency consistent | All data dated D−1 or earlier, session dated D; no USD/oz–tick unit drift. | whole report | 5 |
| 1.3 Audience & tone | Senior Commodities Analyst register maintained throughout; institutional, no retail tone. | §1, §18 | 5 |
| 2.1 Sections present & ordered | All 21 sections present in order incl. 13a–d and 21a–d. §7's five chart sub-headings are rendered with **no caption or placeholder at all** (not even an image-dropped note) — weaker than the brief's minimum bar of "accept a caption or placeholder." | headings, §7 | 4 |
| 2.2 Scorecard as a table | §6 is a proper 10-column table. §11 weekly/monthly tables are correctly R3→P→S3 (3 levels/side), but the **daily** table shows R5→P→S5 (5 levels/side) — inconsistent with weekly/monthly and with M1's `[PIVOT_ABOVE_BELOW_DAILY]=3` default, with no note explaining the deviation. | §6, §11.1 vs §11.2/§11.3 | 3 |
| 2.3 Method steps visible | §4–§5 show observation→normalization→consensus with the futures basis-adjustment stated; §8 is candle-by-candle; §9 states persistence/overlap/VOLator. §7 charts are named but carry zero evidence (see 2.1) — undercuts this row too. | §4–§9 | 3 |
| 3.1 Quantitative claims sourced | §1/§12/§14 figures trace to §4/§6/§13 consistently in form. | text | 4 |
| 3.2 Citations exist & contain data | 3 spot-checked (TradingEconomics 17 Jun, Citi $500 upgrade, Reuters/Mezha 16 Jun): each named, dated, and quotes a figure used consistently elsewhere in the report; none is internally self-contradictory. No fabrication *proven* (no web access), but see 3.4 — the cited spot prices, taken together, describe a session that does not match the leak-free execution feed at all. | §4, §13a | 4 |
| 3.3 Calculations transparent | Pivots are shown derived from stated H/L/C (arithmetic checks out against the report's own — wrong — inputs). RSI2 and the §21a direction score are asserted, not derived inline; ATR(14)≈112 stated but not shown. | §6, §11, §21a | 3 |
| 3.4 Numbers reconcile — internally AND against the level file | **Internally**: D−1 close ($4,352) is identical across §1/§3/§4/§6/§21b MARKET entry — consistent. **Externally: total failure.** Vs. `2026-06-18.csv` (`_full`, ATR14=118.20): Close diff $94.12 (fail >$13.6), Low diff $54.98 (fail >$23.6), RSI2 diff 71.2pts (fail >15 — report shows RSI2 94.3 "extended/overbought", file shows 23.13, i.e. near-oversold). Every daily pivot fails except R2/R3 (which land in the file's tolerance band by arithmetic coincidence given the correct High); every weekly pivot fails (P/R1/S1 diffs $35–47); every monthly pivot fails (P/R1/S1 diffs $40–229). Only Open and High are consistent with the file. Cash-basis comparison fails by comparable or larger margins throughout. | cross-section + level file | 0 |
| 4.1 Pillars conclude | §8/§9/§10/§12 each end in an explicit direction label; §14 is descriptive without its own closing label (relies on §10 cross-reference). | those sections | 4 |
| 4.2 Peer/cross-asset interpreted | §10 gives a mechanism per counter (USDX cost channel, equity risk-off flows, silver co-movement), not a bare correlation list. | §10 | 4 |
| 4.3 Synthesis reconciles tensions | §15/§16/§18 explicitly hold the short-term-bullish/medium-term-Transitional tension open rather than averaging it away; §17 vs §21a flagged "Conflict flag: none" and is genuinely consistent. | §15–§18, §21a | 4 |
| 4.4 Calibrated language | §17 is one (long, comma-joined) sentence; H/M/L confidence stated (§3, §18). | §3, §17 | 4 |
| Card construction (scored under Cat. 4) | Trade 1: TP2 ($4,480) is justified by "daily R2 $4,444 / weekly R2 $4,476" — neither level is at $4,480, an uncorrected mismatch between target and its own cited confluence; stop ($4,288) sits only $2 beyond the report's own daily S1 ($4,290), not the required ~0.25×ATR (~$28) buffer beyond the tighter of swing-extreme/S-R per M5. Trade 3A: TP3 ($4,382) is not beyond TP2 ($4,422) for a LONG — linter WARN_TP3_ORDER confirms. Trade 2: suppression correctly invokes the single-source-indicative pivot flag per §19 — compliant. | §21b, linter | 2 |
| 5.1 Data dated; staleness flagged | All prices/articles dated; §6 rows explicitly flagged "(indicative band)" for single-source dispersion. | §4, §6, §13, §19 | 4 |
| 5.2 Assumptions up front | Futures-to-spot normalization stated with size (~$5–10, §5); anchor override stated identically on the Trade 1 card, in §2, and in §20 Agent Log (see note below) — this is a compliant, well-logged non-conformance, not a silent anchor swap; pivot indicative-flag propagation to Trade 2 is explicit (§19→§21b). | §21b, §19, §20 | 5 |
| 5.3 Red flags surfaced | RSI2 extension and FOMC collision both elevated to §15 and to both live cards' Caveats rows. | §12, §15, §21b | 5 |
| 5.4 Restrictions honoured | JM Bullion dealer-ask correctly down-weighted (no un-normalized retail premium); GC=F used corroboration-only and normalized; no bracketed variable names or module codes found in the body; instrument common names used throughout. No overt breach found, but see 3.4 — the underlying D−1 price series itself cannot be reconciled to the execution feed, which is adjacent to (though not proven to be) a no-synthesis concern. | whole report | 3 |

### Daily-open anchor — explicit check (brief §2)
Compliant. §2 states "07:00 UK (overridden this run — see §20 Agent Log)"; §20 names the deviation as an "OVERRIDE APPLIED" from the "00:00 UK (M1 default)" — which is in fact M1's stated default — states the operator instruction that caused it, and the same 07:00 UK time is carried onto the Trade 1 card. This is the module's specified handling of a non-conformance (recorded as such, same converted time in all three places), not a silent anchor swap. No defect found here.

## 2. Category roll-up

| Cat | Level (0–5) | Multiplier | Max | Points | Justification |
|---|---|---|---|---|---|
| C1 Prompt adherence | 4 | 0.85 | 20 | 17.0 | Variables/scope/audience solid; tick size/name never explicitly stated as a variable |
| C2 Structure | 3 | 0.65 | 20 | 13.0 | All sections present/ordered, but §7 charts carry zero evidence and the daily pivot table's level-count breaks from weekly/monthly/M1 default |
| C3 Accuracy & evidence | 2 | 0.40 | 25 | 10.0 | Sourcing form and internal self-consistency are fine, but external reconciliation against the leak-free level file fails on Close, Low, RSI2, and nearly every daily/weekly/monthly pivot, by many multiples of the failure threshold |
| C4 Reasoning & judgment | 3 | 0.65 | 20 | 13.0 | Pillar conclusions and synthesis are sound, but card construction (scored here) has a real TP2/confluence mismatch, an under-sized Trade 1 stop buffer, and a linter-confirmed TP3-order WARN on Trade 3A |
| C5 Currency & transparency | 4 | 0.85 | 15 | 12.75 | Dating, assumption disclosure and the anchor-override handling are exemplary; red flags are surfaced; restrictions are formally honoured though the unreconciled price base is an adjacent concern |

## 3. Total, band, override

```
c1=4
c2=3
c3=2
c4=3
c5=4
total=66
band=Moderate
override=none
```
Total = 17.0 + 13.0 + 10.0 + 13.0 + 12.75 = 65.75 → rounded to 66. 66 falls naturally in Moderate Trust
(60–74); no band cap needed. No fabricated citation was confirmed (spot-checked sources are named,
dated and internally consistent, so the hallucinated-source override is not invoked, despite the
severe external mismatch scored under 3.4). No openly-violated prompt restriction was found (the
anchor override was correctly logged, not a breach), so the restriction-breach override is not
invoked either.

## 4. Card Integrity (from `qa/gold_regen_qa1/lint_static/2026-06-18.csv`, verbatim)

| card_id | strategy | flags | dud | Card Integrity (100 − 40·DUD − 10·WARN) |
|---|---|---|---|---|
| 2026-06-18_Trade_1 | Trade 1 - Daily Directional | CLEAN | False | 100 |
| 2026-06-18_Trade_2 | Trade 2 - Pivot (TRANSITION) | SUPPRESSED | False | — (suppressed, excluded from mean) |
| 2026-06-18_Trade_3A | Trade 3A - Momentum-Pullback (TRANSITION → fork defaults to 3A) | WARN_TP3_ORDER | False | 90 |

```
card_integrity=95
n_cards=3
n_duds=0
n_warns=1
```
Report-level Card Integrity = mean over the 2 non-suppressed cards = (100 + 90) / 2 = 95.
n_cards is the total number of cards in the linter file (3, including the correctly-suppressed
Trade 2); n_duds/n_warns are totals across all rows.

## 5. Feedback
See `qa/gold_regen_qa1/2026-06-18_feedback.md`.
