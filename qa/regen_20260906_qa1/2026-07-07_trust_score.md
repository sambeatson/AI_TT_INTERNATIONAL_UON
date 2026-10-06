# Trust Score v3.7 - S&P 500 report dated 2026-07-07 (SP500_Report_07Jul2026.md)

Reference numbers (slice US500_upto_2026-07-06, cash session 16:30-23:00 broker): D-1 close 7542.60 (full-day 7546.30);
ATR14 84.44 (full-day 91.30); 5d swing 7552.40 / 7427.00; 25d swing 7624.60 / 7243.10; daily pivots (cash) P 7532.47 R1 7562.53 S1 7512.53.

c1=2
c2=3
c3=0
c4=2
c5=3
total=39
band=Very Low
override=HALLUCINATED_SOURCE (cap Low 40-59; C3 set to 0) + RESTRICTION_BREACH (cap Moderate 60-74; C1 lowered 3 -> 2). Caps do not raise the raw total of 39.
card_integrity=96.7
n_cards=3
n_duds=0
n_warns=1

## Section 7 checklist (score 0-5)

| Row | Notes | Evidence | Score |
|---|---|---|---|
| 1.1 Variables | Asset (cash index), counters USDX/VIX/DAX in order, NY as-of, 5/25 lookbacks, USD/points/0.01 tick, 07:00 UK anchor all respected. Sources: only one index-provider (S&P DJI) row; no exchange or sell-side tier in the price table (CNBC/TheStreet/Investing/Yahoo/TradingEconomics are media/aggregator). | Header, §2, §4, §20 | 3 |
| 1.2 Coverage/currency | Header and §2 state as-of 07 Jul while all data is the 06 Jul close (D-1 as-of expected). §1 says "six sources", §5 says "five independent" sources. Sentiment articles dated 27 May / 24 Jun carried without a staleness flag. | Header, §1, §5, §13a | 3 |
| 1.3 Audience/tone | Strategist, risk-review register throughout. | §1, §18 | 4 |
| 2.1 Sections | §1-§21 present and ordered; §13a-d present. §21c reported "Not populated" (no five-session reconstruction). §7 has five chart headings, no caption/placeholder text (pandoc drop accepted). | headings, §21c | 3 |
| 2.2 Tables | §6 is a table with all required columns. §11 daily R3->S3 correct; weekly only R2->S2 (no R3/S3); monthly pivots absent. | §6, §11 | 3 |
| 2.3 Method visible | Observations -> classification -> consensus (§4-5), candle-by-candle plus sequence (§8), regime with overlap/persistence/VOLator (§9) present. | §4-§9 | 4 |
| 3.1 Quantitative claims sourced | §12/§14 figures unsourced or not tied to §13a: Q1 +29% / Q2 +22% profit growth, "richer than ~87% of 40 years", BofA indicator, 50-56% Sept odds, VIX ~15.8, USDX ~100.8 (no value or date in §10). | §12, §14, §10 | 2 |
| 3.2 Citations (3 spot-checks) | (a) Investing.com row "06 Jul session ... day range 7,427.55-7,540.75": that is the 02 Jul low/high; contradicts §6 06 Jul row (L 7,483.20) and the slice (06 Jul cash range 7502.4-7552.4, low >= 7488.1 full-day). Self-contradictory/impossible quote. (b) §6 06 Jul row High 7,540.75 is identical to the 02 Jul High; Open is "single-source-derived, futures-led 07:00 UK" yet Validation says CORROB. (Δ0.00). (c) Goldman 27 May / JPM 24 Jun quotes consistent with §12 usage. Fails on (a),(b). | §4, §6, §13a | 0 |
| 3.3 Calculations | RSI2 reproduces from the report's own closes for 01 Jul 78.5, 02 Jul 0.1, 06 Jul 100.0 (tool: 78.5/0.1/100.0); 30 Jun 100 consistent. Pivots (daily, weekly) reproduce exactly from the report's H/L/C. §21a score 0.096+0.006=0.10 reproduces; tilt +0.64 reproduces (3.5/5.5). Misses: ATR(14) never stated as a number anywhere (cards say "~1x ATR"); KER window/EMA not stated; "RSI2 standard deviation ≈34" is wrong (population sd of 96.1/100/78.5/0.1/100 = 38.3). | §6, §8, §9, §11, §13b, §21a | 3 |
| 3.4 Reconciliation | D-1 close 7,537.43 consistent across §1/§3/§4/§6/§21b (entry "≈7,537"). Slice cash close 7542.60 (Δ5.2, flagged >3 not >10). Breaks: five vs six sources; §4 day range vs §6; 02 Jul close 7,483.24 vs slice 7472.8 (Δ10.4, >10 failure) and 01 Jul close 7,483.23 (Δ0.01 from 02 Jul); 06 Jul Open 7,489.30 vs 7513.9 (Δ24.6), Low 7,483.20 vs 7502.4 (Δ19.2), High 7,540.75 vs 7552.4 (Δ11.7); 29 Jun Open Δ11.1; 25d high 7,602.10 vs 7624.60 (Δ22.5). Pivot tiers inherit the error: P 7520.46 vs 7532.47, S1 7500.17 vs 7512.53, S2 7462.91 vs 7482.47, S3 7442.62 vs 7462.53. Card "≈1x ATR" with R=94 is 1.11x ATR14. | §6, §11, §21b | 1 |
| 4.1 Pillars conclude | §8 Indecision, §9 Neutral/Transitional, §10 NEUTRAL carry labels; §12 and §14 have per-bullet tags but no closing direction label. | §8-§14 | 3 |
| 4.2 Cross-asset | Mechanism given per counter and a contradiction (DAX) carried forward. | §10 | 4 |
| 4.3 Synthesis | §15/§16 reconcile regime vs sentiment. But §9 "Reduced conviction - wait for confirmation" and a NEUTRAL score are followed by §21a "Direction: LONG" and three long cards; the direction label contradicts the NEUTRAL engine output. | §9, §21a | 2 |
| 4.4 Calibrated language | §17 is one sentence; H/M confidence stated in §3/§18. | §3, §17, §18 | 4 |
| Card construction (Cat 4 protocol) | All three cards emitted against fired M5 §10 gates under a "lenient corroboration" instruction cited as authority; Trade 2 geometry borrowed from RANGE under TRANSITION; Trade 3C ineligible; invalidation ≈ stop on Trades 2/3C; wide-stop flag omitted; ATR/R-multiple not printed. Applied as a one-level reduction of C4. | §21b | (-1 on C4) |
| 5.1 Dated | Prices and articles dated; single-source Open flagged. Counter closes (VIX, USDX, DAX) undated; 27 May and 24 Jun articles not flagged stale. | §6, §13a, §10 | 3 |
| 5.2 Assumptions up front | Lenient-corroboration departure disclosed in §1/§20/§21a (disclosure is itself the prohibited citation). Proxy-open caveat in §6/§19/§20 but not on the Trade 1 card. | §1, §20, §21b | 3 |
| 5.3 Red flags | FOMC-minutes collision carried to all three cards; DAX divergence, concentration, valuation in §15. | §12, §15, §21b | 4 |
| 5.4 Restrictions | Breached: cards emitted despite fired gates (score 0.10<0.25; every pivot tier stated SINGLE-SOURCE-INDICATIVE; no confirmed break) with a run instruction cited as authority (M5 rule 8 / §10: such an instruction "must not appear in the report"); Open derived from a "futures-led" anchor (ES confirmation-only); text refers to "the engine" and "the contract §21". | §1, §6, §19-§21 | 1 |

## Category roll-up

| Cat | Rows (mean) | Level | Multiplier | Points | Justification |
|---|---|---|---|---|---|
| C1 (20) | 3,3,4 = 3.33 -> 3; restriction override -1 | 2 | 0.40 | 8.00 | Variables mostly honoured; source tiers thin; prompt restrictions openly breached. |
| C2 (20) | 3,3,4 = 3.33 -> 3 | 3 | 0.65 | 13.00 | Complete skeleton; §21c empty, weekly R3/S3 and monthly pivots missing. |
| C3 (25) | 2,0,3,1 = 1.5 -> 2; hallucinated-source override | 0 | 0.00 | 0.00 | Self-contradictory Investing range and a 06 Jul O/H/L not supported by the slice. |
| C4 (20) | 3,4,2,4 = 3.25 -> 3; card construction -1 | 2 | 0.40 | 8.00 | Technical read coherent; strategy section contradicts its own gates. |
| C5 (15) | 3,3,4,1 = 2.75 -> 3 | 3 | 0.65 | 9.75 | Dating adequate; restrictions row fails. |

Total = 8.00 + 13.00 + 0.00 + 8.00 + 9.75 = 38.75 -> **39** -> Very Low (0-39). Override check: both overrides trigger; the binding cap (Low 40-59) is above the raw total, so the band is set by the raw total.

## Card Integrity (linter static rows, verbatim)

| card_id | strategy | flags | dud |
|---|---|---|---|
| 2026-07-07_Trade_1 | Trade 1 - Daily Directional (LONG) | CLEAN | False |
| 2026-07-07_Trade_2 | Trade 2 - Pivot, regime-aware (LONG pullback) | WARN_TP3_ORDER | False |
| 2026-07-07_Trade_3C | Trade 3C - Momentum-Breakout (LONG) | CLEAN | False |

Per card: 100, 90, 100 -> report-level 96.7. n_cards=3, n_duds=0, n_warns=1. (The linter does not test the M5 §10 gates; those are scored under Category 4 and 5.4.)
