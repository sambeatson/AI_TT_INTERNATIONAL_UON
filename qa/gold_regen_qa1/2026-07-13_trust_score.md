# Trust Score — Gold_Report_13Jul2026.md (D = 2026-07-13, run gold_regen_qa1)

## 1. Section 7 Checklist

| Row | Reviewer notes | Evidence observed | Score (0–5) | Action required |
|---|---|---|---|---|
| 1.1 Variables respected | Asset correctly defined as XAU/USD spot, LBMA loco-London, futures corroboration-only (not COMEX GC front-month). USDX is the first counter in §10. As-of = Fri 10 Jul, the last completed session strictly before D — correct. Lookback 5 (6–10 Jul) / 25 (§9) sessions — correct. USD/oz used throughout. §4 lists 7 sources (≥6 minimum met) but §5 text says "Six independent observations" — a minor internal miscount. Tick unit (0.1 USD/oz) is used consistently across all three cards' tick counts but the tick name/size is never explicitly declared anywhere (§2 Market Definition has no tick row). | §2, §4, §5, §21b | 4 | One minor instruction not fully respected: tick name/size never stated (used implicitly only) |
| 1.2 Coverage & currency consistent | Every date in §2/§4/§6/§13/§21 is D−1 (10 Jul) or earlier for data, D (13 Jul) for the session. No USD/oz vs tick unit drift — ticks used only as a secondary, consistently-scaled unit (0.1 USD/oz throughout). | whole report | 5 | None |
| 1.3 Audience & tone | No explicit role/audience statement appears in §1 or §18 (no "Senior Commodities Analyst" title, no named audience). Tone throughout is consistently institutional/dense with no retail language, which is consistent with the intended register even though never stated. | §1, §18 | 4 | Add an explicit role/audience line |
| 2.1 Sections present & ordered | All 21 top-level sections present in the exact order specified (§1–§21, with 13a–d and 21a–d present and correctly nested). | headings | 5 | None |
| 2.2 Scorecard as a table | §6 is a genuine 11-column table (Session/O/H/L/C/RSI2/Src A/Src B/Final/Validation). §11 daily and weekly pivot tables both correctly ordered R3→P→S3 with three levels each side. **§11 has no monthly pivot table at all** — required by M1 (`PIVOT_MONTHLY = YES` default) and cited in the brief's own §11 row, yet absent; the §11 position narrative even references a "daily/weekly/monthly confluence" that cannot exist because no monthly levels were ever computed. | §6, §11 | 3 | Monthly pivot table must be added; the "monthly confluence" narrative line is presently unverifiable |
| 2.3 Method steps visible | §4→§5 show observations → normalization (GC=F basis-adjustment stated) → consensus. §8 is candle-by-candle. §9 gives regime with persistence/overlap/VOLator commentary. Charts present as headers only (docx→md image loss, accepted per brief; overall caption present at §7 note). | §4–§9 | 5 | None |
| 3.1 Quantitative claims sourced | §1 and §12 figures trace back to §4/§13 (e.g. PBoC reserve addition ties to §13a Reuters row). §14 Macro, however, states several bare figures with no source or cross-reference at all: US 10-year yield "~4.49%", USDX "~100.7", WTI "~$69"/Brent "~$72", and the CFTC COT read — none carry a citation or point to another section. | §14 | 3 | Flag the §14 unsourced figures (10Y yield, USDX level, WTI/Brent, COT) for a citation or an explicit cross-reference |
| 3.2 Citations exist & contain data | Spot-checked: (1) Investing.com 10 Jul close 4,121.08 — consistent with §6 Fri close 4,121. (2) Reuters (via TE) 10 Jul PBoC reserves story — consistent with §12. (3) TradingEconomics is cited twice for 10 Jul with two different figures: §4's price row gives 4,121.05, while §13a's TradingEconomics headline (same source, same date) quotes "$4,100 an ounce... down about 1.5%" — the report never reconciles these two same-source, same-date figures (a intraday-vs-close read is plausible but is not stated). Not clearly fabricated (both are named, dated, and independently plausible), so no hallucination override, but it is an unresolved internal inconsistency. | §4, §13a | 4 | Reconcile or timestamp-differentiate the two TradingEconomics 10 Jul figures |
| 3.3 Calculations transparent | RSI2 is shown and reproduces exactly from the report's own stated closes (verified: Thu/Fri RSI2 93.8 reproduces from Wed 4,079 → Thu 4,124 → Fri 4,121 closes; RS=15, RSI2=93.75≈93.8). Daily pivots are internally reproducible from the report's own stated Fri H/L/C. However: ATR(14) is never stated as a number anywhere in the report despite being referenced conceptually (stop cap "3.5×ATR", VOLator). KER is never given a numeric value, only a qualitative label. Most seriously, **§21a's own listed direction-score components do not sum to the stated total**: 0.05 (tech) + 0.02 (cross-asset) − 0.05 (sentiment) − 0.04 (regime) + 0 (Kaufman) + 0.01 (vol) = **−0.01, not the stated +0.14** — a discrepancy of 0.15, large enough to flip the sign of the score and the suppression logic it drives. | §6, §11, §21a | 1 | Recompute §21a so the six weighted components actually sum to the stated net score; state ATR14 and KER numerically |
| 3.4 Numbers reconcile — incl. vs level file | Internal: D−1 close is consistent across §1/§3/§4/§6 (~$4,121). Daily pivots reconcile against `data/levels/XAUUSD_by_date/2026-07-13.csv` (_full basis) within tolerance (P diff 0.92, R1 diff 2.22, S1 diff 0.46, R2 diff 2.68, S2 diff 0.84, R3 diff 3.98, S3 diff 1.30 — all ≤ the 4.08 "consistent" threshold, 0.04×ATR14_full). Fri OHLC/RSI2 also reconcile within tolerance (open diff 2.94, high 1.17, low 0.11, close 1.77, RSI2 diff 2.7 — all inside "consistent" bands). **But the weekly pivots fail badly**: report P=4,156.3 vs file `w_full_P`=4,114.5633 (diff 41.74); R1 diff 47.32; S1 diff 41.28; R2 diff 47.78; S2 diff 35.70; R3 diff 53.36; S3 diff 35.24 — every one of the six weekly levels exceeds the 11.72 (0.115×ATR14_full) Category-3-failure threshold by 3–5×. The report's own implied weekly H/L/C (back-solved from its stated pivots: H≈4,244.9, L≈4,057.9, C≈4,166.1) does not match the actual prior week (6–10 Jul, matching `w_full_period = 2026-W28`) that the level file uses, nor the report's own §6 week (whose own H/L span only 4,058–4,172). This, plus the unreconciled §21a arithmetic from 3.3, are material reconciliation failures. | cross-section + level file | 0 | Weekly pivots must be recomputed from the correct prior-week (6–10 Jul) H/L/C; §21a score must reconcile to its stated components |
| 4.1 Pillars conclude | §8 ends "Indecision"; §9 ends Transitional/Bearish-structural; §12 bullets each carry an inline direction label; §14 bullets are mostly but not uniformly labelled (some descriptive only). | §8, §9, §12, §14 | 4 | None material |
| 4.2 Peer/cross-asset interpreted | §10 gives an explicit mechanism for each counter (USDX real-price effect, S&P/DAX real-yield/opportunity-cost channel, Silver as metals-complex beta) rather than a bare correlation list. | §10 | 5 | None |
| 4.3 Synthesis reconciles tensions | §15/§16/§18/§21a explicitly surface the tension between the +0.14 direction score (mild long) and the §17 forecast (mild downside skew) as a named "Conflict flag" rather than averaging it away, and §16 ties the KER/regime read to the bull/bear balance. This is undermined, however, by the fact that the +0.14 score being reconciled against does not itself arithmetically follow from its stated inputs (see 3.3/3.4) — the synthesis is transparent about the conflict but is built on an unreliable number. | §15–§18, §21a | 3 | Fix the §21a arithmetic; re-check whether the conflict flag still holds once corrected |
| 4.4 Calibrated language | §17 is exactly one sentence. Confidence stated as "Medium" in §3 and §18. Hedge language ("likely", "may", qualifiers) used appropriately without stacking or false certainty. | §3, §17 | 5 | None |
| 5.1 Data dated; staleness flagged | Every price and article in §4/§6/§13 carries a date. Single-source O/H/L fields (Mon–Wed) are explicitly flagged indicative in §6/§19. | §4, §6, §13, §19 | 5 | None |
| 5.2 Assumptions up front | Futures-to-spot normalisation stated with its size (GC=F, ~$2–3 premium subtracted, §4 note). Daily-open-anchor override to 00:00 UK is stated as a logged non-conformance consistently in §2, the report body, and §20 Agent Log (same converted time throughout) — compliant handling per the framework's own non-conformance rule; not scored as a defect since the populated gold instance value cannot be seen. Weekly-level single-source-indicative status is explicitly carried into both live cards' caveats. | §21b, §19, §20 | 5 | None |
| 5.3 Red flags surfaced | §12/§15 carry the CPI event risk, institutional bearish forecasts (HSBC/OCBC), and the equity-strength headwind. §13d's CPI collision is explicitly carried into both live cards' caveats. | §12, §15, §21b | 5 | None |
| 5.4 Restrictions honoured | No bracketed variable names or M1–M5 module codes appear in the report body. Futures (GC=F) used corroboration-only, never as the primary price. §19 explicitly discloses (rather than silently applies) the run-instructed waiver of the corroboration halt on indicative OHLC fields — transparent disclosure, not a silent breach. Instrument common names used throughout. | whole report | 5 | None |

## 2. Category Roll-up

| Cat | Mean of rows | Level (0–5) | Multiplier | Max | Points | One-line justification |
|---|---|---|---|---|---|---|
| C1 Prompt adherence | (4+5+4)/3 = 4.33 | 4 | 0.85 | 20 | 17 | Correct asset/basis/lookback/counters; tick unit used but never declared; audience implied, not stated |
| C2 Structure | (5+3+5)/3 = 4.33 | 4 | 0.85 | 20 | 17 | Full §1–§21 present and ordered; §11 is missing its monthly pivot table despite a narrative reference to monthly confluence |
| C3 Accuracy & evidence | (3+4+1+0)/4 = 2.00 | 2 | 0.40 | 25 | 10 | Daily OHLC/pivots/RSI2 reconcile to the level file within tolerance, but every weekly pivot level misses by 3–5× the failure threshold, and §21a's direction-score components do not sum to its own stated total |
| C4 Reasoning & judgment | (4+5+3+5)/4 = 4.25 | 4 | 0.85 | 20 | 17 | Pillars conclude, cross-asset mechanisms explained, tensions surfaced explicitly — but the reconciled number (§21a score) they lean on is itself unreliable |
| C5 Currency & transparency | (5+5+5+5)/4 = 5.00 | 5 | 1.00 | 15 | 15 | Dating, assumption disclosure, anchor-override handling, red-flag surfacing and restriction compliance all excellent |

## 3. Total, Band, Override

```
total = 17 + 17 + 10 + 17 + 15 = 76
band = High Trust (75–89)
override = none
```
No fabricated source was found (all three spot-checked citations are named, dated, and at worst show an unreconciled intraday-vs-close discrepancy, not invention) — no hallucination override. No prompt restriction was openly violated — the two run-level deviations found (daily-open anchor, corroboration-halt waiver) are both explicitly logged as non-conformances per the framework's own disclosure rule, not silently applied — no restriction-breach override.

## 4. Card Integrity (from `qa/gold_regen_qa1/lint_static/2026-07-13.csv`, copied verbatim)

| card_id | strategy | flags | dud | per-card score |
|---|---|---|---|---|
| 2026-07-13_Trade_1 | Trade 1 - Daily Directional | SUPPRESSED | False | n/a — suppressed, excluded from the mean |
| 2026-07-13_Trade_2 | Trade 2 - Pivot (regime-aware); RANGE regime -> fade toward pivot | WARN_R_TINY(0.26xATR) | False | 100 − 10×1 = 90 |
| 2026-07-13_Trade_3B | Trade 3B - Mean-Reversion (RANGE + KER below trend threshold + flat VOLator slope) | WARN_R_TINY(0.27xATR) | False | 100 − 10×1 = 90 |

```
card_integrity = mean(90, 90) = 90
n_cards = 3
n_duds = 0
n_warns = 2
```

## Score lines

c1=4
c2=4
c3=2
c4=4
c5=5
total=76
band=High
override=none
card_integrity=90
n_cards=3
n_duds=0
n_warns=2
