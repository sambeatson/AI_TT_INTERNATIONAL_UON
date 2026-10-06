# Trust Score v3.7 - FTSE 100 Daily Report, 03 Jul 2026 (run ftse_qa1, Stage 1)

Report: `reports/md/FTSE100_EuroStoxx_Report_03Jul2026.md` · D = 2026-07-03 · D-1 = 2026-07-02
Level file `data/levels/UK100_by_date/2026-07-03.csv`: `last_bar_date` = 2026-07-02 < D (leak-free, checked).
Basis: the report claims a cash-index basis, so all comparisons use the `_cash` columns (full-broker-day values in brackets where they change the verdict).
D-1 reference (slice): cash close 10654.0 [full-day 10664.9] · ATR14 115.75 [125.65] · RSI2 86.19 [82.03].

## Machine-readable result
```
c1=2
c2=4
c3=0
c4=3
c5=3
total=48
band=Low
override=hallucinated_source
card_integrity=100.0
n_cards=3
n_duds=0
n_warns=0
```
Override notes: (a) hallucinated_source: CNBC "01 Jul" item (§13a) is an impossible/self-contradictory citation, so C3 is set to 0 and the total is capped at Low (40-59). (b) A restriction breach is ALSO present (see 5.4): C1 was reduced from 3 to 2 for it. The single `override=` field carries the dominant override; the raw (pre-override) C3 would have been 2.

## 1. Section 7 checklist (every row)

| Row | Reviewer notes | Evidence observed (location) | Score |
|---|---|---|---|
| 1.1 Variables respected | FTSE 100 cash primary; Euro Stoxx as reference; counters USDX / S&P 500 / DAX stated; as-of 02 Jul London close; 5-session lookback; GBP/index points. Weaknesses: source mix is aggregator / retail-broker heavy (Investing, IG, TradingView, Yahoo) with no index-provider/exchange tier actually evidenced for OHLC; the 07:00 UK anchor is stated in the header but Trade 1 is a BUY-STOP at 10,660, not a market entry at the anchor, and Trades 2/3A state no anchor time. | Header; §2; §4; §20; §21b | 3 |
| 1.2 Coverage and currency consistent | Mostly D-1 data, session D. Drift points: CNBC item dated 01 Jul quoting a +1.7% FTSE gain that §6/§8 place on 02 Jul; Morningstar item dated "Jan/ongoing"; §13d treats 03 Jul as a US labour-data day (the slice calendar shows NFP/claims/unemployment released on 02 Jul and a US Independence Day holiday row on 03 Jul). | §13a, §13c, §13d, §14 | 3 |
| 1.3 Audience and tone | Senior strategist register, trading/risk-review tone, no retail language. Minor: process leakage ("per the run instruction", "lenient-corroboration basis", "v2.1 baseline") and a stray bracketed glyph "《denies》" in §13d. | Header, §19, §20, §13d, §21b | 4 |
| 2.1 Sections present and ordered | §1-§21 all present in order incl. §13a-d and §21a-d; §17 is one sentence. Charts: five captions with no image content (pandoc drop accepted; noted). | headings | 4 |
| 2.2 Scorecard as a table | §6 is a table, but has no "Final" column (Close is bolded instead). §11: daily table carries 5 levels each side (R5..S5, brief asks 3), weekly carries R3..S3, and the MONTHLY pivot table is missing entirely. | §6, §11 | 3 |
| 2.3 Method steps visible | §4-§5 observations -> normalisation -> consensus shown; §8 candle-by-candle + sequence; §9 regime with persistence 0.57, range position, KER, VOLator; §21c backtest present. Overlap metric not shown in §9; no inputs shown for KER. | §4-§9, §21c | 4 |
| 3.1 Quantitative claims sourced | Price claims point to §4/§6/§13. Unsourced: UK Bank Rate 3.75% / inflation 2.80% (§12, §14), "~80% of FTSE revenue overseas" (§12), ATR14 "≈88 pts" (§21b; no source or calc), eurozone CPI 2.8%/core 2.4% (§13c, §12) with no article in §13a. | §12, §13c, §14, §21b | 3 |
| 3.2 Citations exist and contain data | Three checked. (1) Trading Economics 02 Jul "+1.7% to 10,653, highest since April 17": consistent with the slice (cash close 10654.0; previous higher cash close 10663.1 on 17 Apr) - PASS on the figure, but its implied prior close (10653/1.017 = 10,475) contradicts the report's own 01 Jul close 10,446.76 (-> §6 01 Jul close is wrong, slice 10472.4). (2) CNBC "01 Jul": quote "FTSE 100 was up 1.7%" cannot be dated 01 Jul - the report's own §6/§13c have FTSE -0.5% on 01 Jul and +1.7% on 02 Jul. Impossible date / figure not matching its own date = counts as fabricated under brief 3.2. (3) IG "30 Jun: near an all-time high" vs the report's own "record-close 10,911 zone" (30 Jun close 10,497.72 is 3.8% below it) - self-inconsistent, unresolved. Also: "Investing.com (derived) 02 Jul RT 10,444" is presented as a CFD divergence; the broker CFD slice closes 02 Jul at 10,654.0 / 10,664.9, so the divergence narrative (§3, §5, §19, header) is not supported by the CFD feed. | §4, §13a, §3, §5, §19 | 0 (override) |
| 3.3 Calculations transparent | RSI2 reproduces from the report's OWN closes (43.8 / 0.0 / 80.2 - engine test passed) but the closes themselves are wrong. Pivots reproduce exactly from the stated 02 Jul H/L/C (P 10596, R1 10722, S1 10527, R2 10791, S2 10401, R3 10917, S3 10332). Fails: ATR14 stated only as "≈88" on one card (slice 115.75 cash / 125.65 full, i.e. 24-30% too low) and never in §9; KER 0.28 given with no inputs (my recompute 13-session, EMA3 ≈ 0.24 unsigned - same classification); sentiment tilt: its own arithmetic gives +0.625 but +0.47 is reported via an unexplained "recency echo" haircut; §21a score +0.42 does not reproduce (listed components sum to 0.25+0.20+0.07+0.15 = 0.67; proper signal×weight with KER 0.28×0.15, cross-asset MIXED 0.3×0.15, VOLator +0.5×0.10 ≈ 0.66). | §6, §11, §13b, §21a, §21b | 2 |
| 3.4 Numbers reconcile | Good: D-1 close 10,653 identical in §1/§3/§4/§6/§18, and within 1.0 pt of the slice cash close (10654.0). Pivots on cards = §11. Breaks: (i) 01 Jul close 10,446.76 vs TE +1.7% (above) and slice 10472.4 (Δ -25.6); (ii) §21d "Trade 1 triggered 3/5" vs §21c table (2 triggers, 1 suppressed, 2 no-trigger); mean R +0.47 is only reproducible by counting a phantom 0; (iii) §21a total; (iv) §13b tilt; (v) §1 "short-term Transitional-to-Bullish" vs §8 "Bullish"; (vi) weekly pivot H/L implied by §11 (H 10560 / L 10380 / C 10500) vs slice week 22-26 Jun (H 10577.7 / L 10328.1 / C 10516.4). See data table below. | whole report | 2 |
| 4.1 Pillars conclude | §8 "Bullish continuation", §9 "Trending - Bullish", §10 "CONFIRM-leaning MIXED", §12 items each tagged supportive/neutral/two-sided but no pillar-level verdict; §14 bullets tagged. | §8-§14 | 4 |
| 4.2 Cross-asset interpreted | Mechanisms given for USDX (earnings translation), S&P (risk beta, low tech weight), DAX (regional appetite). Brent/oil is absent from §10 despite being discussed as a swing factor in §12/§14. USDX slice: -0.54% on 02 Jul (101.411 -> 100.858), "flat/soft" acceptable. | §10 | 4 |
| 4.3 Synthesis reconciles tensions | §16 expects 10,470-10,790 with a close above 10,660-10,722 as the battleground, yet Trade 1 TP2 is 10,926 and the TP3 runner is a 3×ATR cap; §21a states "Conflict flag: none material" while §15 lists crowded-long into resistance and §1 vs §8 disagree on short-term state; the fact that pivots are "would normally be suppressed" is not reconciled with a conviction call. | §15, §16, §18, §21a | 3 |
| 4.4 Calibrated language | §17 is exactly one sentence with a condition; confidence Medium stated in §3/§18 with a reason. (The reason offered - CFD divergence - is not supported by the slice, see 3.2.) | §3, §17 | 4 |
| 4.5 Card construction (protocol row for C4) | All three cards: invalidation set equal to the stop; Trade 2 built with RANGE-style 1R/2R geometry under a declared TREND regime and shipped although the report itself says it "would normally be suppressed"; Trade 3A uses 38.2% as entry (rule: 57.5%) and a sub-threshold swing; Trade 1 not a market entry, no wide-stop flag, ATR understated. Details in feedback. | §21b | 1 |
| 5.1 Data dated, staleness flagged | Prices and most articles dated; single-source O/H/L flagged (26 Jun, 02 Jul H/L). Morningstar "Jan/ongoing" undated; the 02 Jul open (10,478.78, two-decimal) is credited to "TE/TE(alt)" which only quote closes; flagged INDICATIVE but the 29 Jun/01 Jul "CORROBORATED" labels are not borne out by the slice. | §4, §6, §13a | 4 |
| 5.2 Assumptions up front | Lenient-corroboration basis and indicative pivots are stated in the header, §11, §19, §21b. Anchor-override caveat is on Trade 1 only; Trades 2 and 3A carry no anchor/time. | header, §19, §20, §21b | 4 |
| 5.3 Red flags surfaced | Crowded-long, hot-US-data, GBP strength, oil weakness are surfaced. But the headline event of D is wrong: §13d/§14/§18/§21b name "US labour-market data & Fed commentary" on 03 Jul; the slice calendar has US NFP (actual 57 vs 43 consensus), jobless claims and unemployment on 02 Jul (omitted from §13c) and only an Independence Day row for USD on 03 Jul. D's scheduled HIGH items in the calendar are ECB Lagarde speech (11:00 broker = 09:00 UK) and BoE Bailey speech (18:00 broker = 16:00 UK), plus UK/EZ services PMIs; none appear. Card caveats therefore carry the wrong collision. | §13c, §13d, §21b | 2 |
| 5.4 Restrictions honoured | Breaches: (1) M5 pivot-suppression rule: report states every pivot tier is SINGLE-SOURCE-INDICATIVE yet ships Trade 2 (and builds Trades 1/3A on them), citing "would normally be suppressed" - the rule says stating the flag and shipping anyway is the prohibited failure (the tiers could be recomputed from the execution series and flagged CORROBORATED, which the report did not do). (2) Retail-CFD restriction: Investing.com is labelled "CFD-derived ... Demoted" in §4 but is Src A for 26 Jun and 01 Jul in the §6 OHLC table, and IG/TradingView are used as corroborators. (3) Weekly pivots from "reconstructed" prior-week H/L (§19) - synthesised input presented as a level. (4) Process references ("run instruction", "v2.1 baseline", "lenient-corroboration") in the body. | §4, §6, §11, §19, §21b | 1 |

## 2. Category roll-up

| # | Category (max) | Row mean | Level | Multiplier | Points | Justification |
|---|---|---|---|---|---|---|
| 1 | Prompt adherence (20) | (3+3+4)/3 = 3.33 -> 3; restriction breach -1 | 2 | 0.40 | 8.0 | Asset/window/currency right; anchor not honoured on cards; source tiers thin; restriction breach (5.4) lowers C1 one level. |
| 2 | Structure (20) | (4+3+4)/3 = 3.67 | 4 | 0.85 | 17.0 | All 21 sections present and ordered; monthly pivots missing; pivot table depth/columns off. |
| 3 | Accuracy & evidence (25) | (3+0+2+2)/4 = 1.75 -> 2; override | 0 | 0.00 | 0.0 | Fabricated-source override (CNBC 01 Jul). Even raw: 13 of 15 O/H/L fields outside tolerance, two closes >15 pts off, ATR and pivots off. |
| 4 | Reasoning & judgment (20) | (4+4+3+4+1)/5 = 3.2 | 3 | 0.65 | 13.0 | Narrative coherent and regime read consistent with the slice (persistence 0.56 vs 0.57 stated); card construction and §21a derivation are poor. |
| 5 | Currency, restrictions, transparency (15) | (4+4+2+1)/4 = 2.75 | 3 | 0.65 | 9.75 | Dating/assumptions good; D calendar wrong; restrictions breached. |

## 3. Total, band, override
Total = 8.0 + 17.0 + 0.0 + 13.0 + 9.75 = 47.75 -> **48**. Band **Low (40-59)**. Override: **hallucinated_source** (cap Low; C3 = 0). Secondary: restriction breach (C1 3 -> 2); the cap Moderate (74) is non-binding because the Low cap is lower.

## 4. Category 3 data checks against the level file (cash basis; |Δ| tolerance: close 5, O/H/L 10)

Report minus slice (cash session 10:00-18:30 broker). `X` = outside tolerance.

| Session | Field | Report | Slice cash | Δ | Slice full-day | Verdict |
|---|---|---|---|---|---|---|
| 26 Jun | Open | 10498.00 | 10498.3 | -0.3 | 10512.9 | ok |
| 26 Jun | High | 10537.00 | 10516.4 | +20.6 | 10526.8 | X |
| 26 Jun | Low | 10460.00 | 10401.4 | +58.6 | 10401.4 | X |
| 26 Jun | Close | 10500.00 | 10516.4 | -16.4 | 10476.0 | X (>15) |
| 29 Jun | Open | 10530.18 | 10505.9 | +24.3 | 10506.0 | X |
| 29 Jun | High | 10545.00 | 10524.3 | +20.7 | 10532.7 | X |
| 29 Jun | Low | 10485.00 | 10468.8 | +16.2 | 10468.8 | X |
| 29 Jun | Close | 10508.00 | 10497.8 | +10.2 | 10511.9 | X cash (ok on full-day, -3.9) |
| 30 Jun | Open | 10490.00 | 10509.5 | -19.5 | 10510.3 | X |
| 30 Jun | High | 10530.00 | 10608.8 | -78.8 | 10608.8 | X (large) |
| 30 Jun | Low | 10460.00 | 10490.6 | -30.6 | 10485.0 | X |
| 30 Jun | Close | 10497.72 | 10501.5 | -3.8 | 10506.2 | ok |
| 01 Jul | Open | 10484.31 | 10481.4 | +2.9 | 10499.1 | ok |
| 01 Jul | High | 10527.00 | 10500.3 | +26.7 | 10504.2 | X |
| 01 Jul | Low | 10439.96 | 10416.0 | +24.0 | 10416.0 | X |
| 01 Jul | Close | 10446.76 | 10472.4 | -25.6 | 10461.7 | X (>15; -15.0 even on full-day) |
| 02 Jul | Open | 10478.78 | 10433.6 | +45.2 | 10451.7 | X |
| 02 Jul | High | 10665.00 | 10686.8 | -21.8 | 10686.8 | X |
| 02 Jul | Low | 10470.00 | 10424.8 | +45.2 | 10424.8 | X |
| 02 Jul | Close | 10653.00 | 10654.0 | -1.0 | 10664.9 | ok (D-1 close correct) |

Summary: D-1 close correct; 13 of 15 O/H/L fields outside tolerance; closes for 26 Jun, 29 Jun (cash) and 01 Jul wrong by 16.4 / 10.2 / 25.6 pts.

RSI2: arithmetic reproduces from the report's own closes (43.8, 0.0, 80.2). Versus slice cash RSI2: 29 Jun 0.00 (report "—"), 30 Jun 16.59 (report 43.8, Δ +27.2), 01 Jul 11.28 (report 0.0, Δ -11.3), 02 Jul 86.19 [full 82.03] (report 80.2, Δ -6.0 [-1.8]). Trend labels from slice (Close vs Open and RSI2): 26 Jun Bullish, 29 Jun Bearish, 30 Jun Bearish, 01 Jul Bearish, 02 Jul Bullish; report: Neutral, Neutral, Neutral, Bearish, Bullish.

ATR14: report ≈88 (one card only) vs 115.75 cash / 125.65 full: Δ -27.8 / -37.7 (-24% / -30%).

Daily pivots (report from 02 Jul H 10665 / L 10470 / C 10653 vs level file `d_cash_*`, [`d_full_*`]):

| Level | Report | Level file cash [full] | Δ cash |
|---|---|---|---|
| R3 | 10917 | 11014.27 [11021.53] | -97.3 X |
| R2 | 10791 | 10850.53 [10854.17] | -59.5 X |
| R1 | 10722 | 10752.27 [10759.53] | -30.3 X |
| P | 10596 | 10588.53 [10592.17] | +7.5 ok |
| S1 | 10527 | 10490.27 [10497.53] | +36.7 X |
| S2 | 10401 | 10326.53 [10330.17] | +74.5 X |
| S3 | 10332 | 10228.27 [10235.53] | +103.7 X |

Weekly pivots (report "22-26 Jun" vs `w_cash_*`):

| Level | Report | Level file cash | Δ |
|---|---|---|---|
| R3 | 10760 | 10869.63 | -109.6 X |
| R2 | 10660 | 10723.67 | -63.7 X |
| R1 | 10580 | 10620.03 | -40.0 X |
| P | 10480 | 10474.07 | +5.9 ok |
| S1 | 10400 | 10370.43 | +29.6 X |
| S2 | 10300 | 10224.47 | +75.5 X |
| S3 | 10220 | 10120.83 | +99.2 X |

Monthly pivots (June, `m_cash_*`): MISSING from the report (level file: P 10412.17, R1 10698.13, S1 10215.53, R2 10894.77, S2 9929.57, R3 11180.73, S3 9732.93).
Root cause of the pivot spread: the report's range 02 Jul L 10470 is 45.2 pts above the slice low 10424.8 and H is 21.8 below; weekly range implied H 10560 / L 10380 vs slice 10577.7 / 10328.1.

Other checks: KER 13/EMA3 ≈ 0.24 (stated +0.28, class unchanged); 25-session directional persistence 0.56 (stated 0.57) - regime read is supported by the slice. USDX 02 Jul -0.54%, S&P 500 +1.7% over the five sessions - counter directions in §10 acceptable. News calendar: see 5.3.

## 5. Card Integrity (linter rows copied verbatim from `qa/ftse_qa1/lint_static/2026-07-03.csv`)

| card_id | report_date | strategy | flags | dud | score |
|---|---|---|---|---|---|
| 2026-07-03_Trade_1 | 2026-07-03 | Trade 1 - Daily Directional (LONG) | CLEAN | False | 100 |
| 2026-07-03_Trade_2 | 2026-07-03 | Trade 2 - Pivot, regime-aware (LONG pullback-buy) | CLEAN | False | 100 |
| 2026-07-03_Trade_3A | 2026-07-03 | Trade 3 - Momentum-Pullback (3A) (LONG) | CLEAN | False | 100 |

Report-level Card Integrity = mean(100, 100, 100) = **100.0** (n_cards=3, n_duds=0, n_warns=0, none suppressed). The static linter is blind to the construction defects listed in feedback (invalidation = stop, wrong regime geometry, wrong fib levels, missing flags); those are scored under C4 row 4.5, not here.
