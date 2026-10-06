# Trust Score QA - FTSE 100 daily report, D = 2026-06-30

Report: `reports/md/FTSE_EuroStoxx_Report_30Jun2026.md` | Framework: Trust Score v3.7 (Sections 4-7) | Run: ftse_qa1
Data basis: `data/levels/UK100_by_date/2026-06-30.csv` (`last_bar_date` = 2026-06-29 < D, leak-free, checked) and
`qa_slice_stats.py --cash-open 10:00 --cash-close 18:30`. The report claims a cash-index basis, so `_cash` fields are the comparator (`_full` shown where it matters).
D-1 = Mon 2026-06-29 (cash session: O 10,505.9 H 10,524.3 L 10,468.8 C 10,497.8; ATR14 cash 114.81 / full 132.08; RSI2 cash 0.00 / full 45.97).

## Score line

```
c1=2
c2=4
c3=0
c4=3
c5=3
total=48
band=Low
override=hallucinated_source
card_integrity=100
n_cards=3
n_duds=0
n_warns=0
```

## 1. Section 7 checklist

| Row | Score | Notes | Evidence location |
|---|---|---|---|
| 1.1 Variables respected | 2 | Asset, counters (USDX, S&P 500, DAX 40), GBP/points, 5-session lookback are right. Wrong: (a) the as-of is London close of D-1 (29 Jun) but the report is as-of D and its 5-row table runs 24-30 Jun, ending in an in-session D row; (b) the Trade 1 anchor is 00:00 UK, not 07:00 UK, and the deviation is justified "at user instruction" (a waiver the fixed rules forbid citing); (c) §4 lists only five price sources and none is sell-side, against the >= 6 / three-tier requirement. | §2, §4, §6, §20, §21b |
| 1.2 Coverage and currency consistent | 2 | Data rows carry a D (30 Jun) observation, "Investing.com 30 Jun snapshot", "Provisional (in-session)", and §1/§3/§8/§11/§21c all use 10,506.5 as the live level. The US PCE release is dated 26 Jun in §13c; the calendar slice shows it on 25 Jun. §13d omits the D-day US releases in the calendar slice (JOLTS 15:00 UK, CB Consumer Confidence 15:00 UK, MNI Chicago PMI 14:45 UK). §13d dates the Eurozone flash CPI 1 Jul without support in the slice. | §1, §3, §4, §6, §13c, §13d, §21c |
| 1.3 Audience and tone | 4 | Professional strategist register, trading-and-risk-review framing, no retail tone. Minor: "Thursday" without date in §1. | §1, §18 |
| 2.1 Sections present and ordered | 4 | §1-§21 all present and in order, §13a-d and §21a-d present, §21d limitations boilerplate present. Deficiency: no SUPPRESSED row for Trade 1 even though §21a/§20 say the score (+0.16) is below the 0.25 threshold. | headings |
| 2.2 Scorecard as a table | 3 | §6 is a table, but Source A / Source B / Final columns are collapsed into one "Sources" column and there is no "Final" column. §11 tables list five levels each side (R5-S5) instead of R3 -> P -> S3 (three each side). | §6, §11 |
| 2.3 Method steps visible | 4 | §4-§5 show observations -> consensus; §8 is candle-by-candle with a sequence label; §9 has regime, VOLator, KER and the dual-gate. §9 gives no numeric persistence/overlap values, and ATR14 and the KER smoothing are not stated in §9. §7 has five chart captions only (images dropped; accepted as placeholders). | §5, §7, §8, §9 |
| 3.1 Quantitative claims sourced | 2 | §6 O/H/L values for 24, 25 and 29 Jun are round numbers (10,462.0, 10,472.0, 10,460.0, 10,500.0, 10,455.0, 10,545.0) with no §4 row behind them: §4 has no 25 Jun row at all and its 29 Jun row gives only a 10,478-10,500 range. §1/§12/§14 statistics (Brent, GBP/USD, UK CPI, 80% overseas revenue) carry no source. | §4, §6, §12, §14 |
| 3.2 Citations exist and contain data | 1 | Three sources tested, all fail on internal consistency: (1) Trading Economics 26 Jun is quoted "-0.17% on day" in §4 but "edged higher ... outperforming" in §13a. (2) CNBC .FTSE 24 Jun raw quote 10,496.25 is "normalized" to a 10,470 close, with H 10,506.47, which is 37.9 pts above the cash H 10,468.6 for that session and a different figure from its own quote. (3) Investing.com UK100 "30 Jun snapshot" is dated D, after the as-of, and its stated "Open 10,506.50" conflicts with §6's 30 Jun open 10,478.0 (10,506.5 is used as the close). §19 also cites a "known 2025 Yahoo Gold restriction", irrelevant to this asset. Treated as fabricated per brief §2 row 3.2. | §4, §13a, §19 |
| 3.3 Calculations transparent | 2 | RSI2 reproduces from the report's own closes (77.0 / 0.0 / 45.5 for 26, 29, 30 Jun; confirmed by `--closes`), Trend labels follow the stated rule, and daily/weekly/monthly pivots follow the formulas from the report's own H/L/C. But ATR14 appears only on a card (~95; level file 114.81 cash / 132.08 full, -19.8 / -37.1) and is not stated in §9; the sentiment tilt computes to +0.375 and is then reported as +0.30 by an unexplained "conservative" adjustment; the §21a score is not reproducible (five contributions shown, six weights, sum 0.168 vs "+0.16", sentiment contribution 0.015 does not follow from tilt 0.30 x weight 0.10 or 0.15). | §6, §9, §11, §13b, §21a |
| 3.4 Numbers reconcile | 1 | D-1 close differs by section: §1/§3 10,506 (a D value), §6 10,478.5 (29 Jun row), §21b entry 10,486 (pivot). Versus the slice, the 29 Jun close is 10,478.5 vs cash 10,497.8 = -19.3 pts (>15, Category 3 failure; vs full close 10,511.9 = -33.4). Other D-1 fields: O -5.9 (ok), H -0.3 (ok), L -13.8 (>10). See §3 below for all deltas. Stated 25-session range 10,360-10,545 vs data 10,126.2 (10 Jun) - 10,577.7: low off by +233.8, high by -32.7. Stated 5-session band 10,405-10,545 vs data 10,328.1-10,577.7. | §1, §3, §6, §9, §21b |
| 4.1 Pillars conclude | 3 | §8 (Range), §9 (Mildly Bullish), §10 (contradiction flag), §12 (tagged items) conclude; §14 ends in a watch item, not a direction label. | §8-§14 |
| 4.2 Cross-asset interpreted | 4 | Mechanisms given (dollar-earner translation, tech weight, Europe risk-off, energy). Cross-asset reads rest on "falling" S&P/DAX; the S&P slice rebounds +1.3% on D-1 (7,380.0 -> 7,440.3), unmentioned. USDX ~101.2 and VIX ~18 agree with the slice (101.10, 18.03). | §10, §14 |
| 4.3 Synthesis reconciles tensions | 2 | §9 says the dual-gate "defaults to TRANSITION", yet §21b builds a RANGE Trade 2 and a 3B Trade 3 (TRANSITION requires breakout-side Trade 2 and 3C). The KER-vs-regime and §17-vs-§21a conflicts are flagged, but the card geometry contradicts the stated regime. | §9, §16-§18, §21 |
| 4.4 Calibrated language | 4 | §17 is exactly one sentence; confidence "Medium" stated in §3 and §18. Mildly stacked hedges ("most likely ... mild ... contingent"). | §3, §17 |
| 4.x Card construction (protocol) | 0 | A card the fixed rules require to be SUPPRESSED is issued (Trade 1, score +0.16 < 0.25) under "user-directed override"; Trade 2 is issued while §19/§11 flag the daily/weekly tiers indicative and the monthly tier "coarse estimates" (all tiers indicative: Trade 2 must be suppressed); Trade 1 entry is a limit at 10,486 rather than market at the anchor and reference close; the Trade 3 variant does not match the regime; the short legs of Trade 2 and 3B have R < 0.3 x ATR14. Detail in the feedback file. | §20, §21a, §21b |
| 5.1 Data dated; staleness flagged | 3 | Prices and articles are dated and single-source O/H/L is flagged. But the flagged "Corroborated; delta 18" labels contradict the stated +/-0.10 tolerance, and the D in-session row is presented in a D-1 as-of report. | §4, §6, §13, §19 |
| 5.2 Assumptions up front | 3 | The 00:00 UK anchor override is stated in §2, §20 and the card (good) but is attributed to a "user instruction" and "explicit run instruction", which the fixed module forbids citing as authority. Single-source propagation to cards is present as a caveat. | §2, §20, §21b |
| 5.3 Red flags surfaced | 4 | §12/§15 risks and the payrolls collision carried into card caveats. D-day events omitted from §13d. | §12, §15, §21b |
| 5.4 Restrictions honoured | 1 | Breaches: (a) prices that are range end-points or round numbers presented as validated (29 Jun O 10,500 = top of a 10,478-10,500 range; 24/25/29 Jun O/H/L); (b) monthly pivots "coarse estimates" presented in the same format as sourced levels; (c) non-overridable gates relaxed on instruction (Trade 1 suppression; Trade 2 all-indicative suppression); (d) a D-dated provisional row inside a D-1 as-of table. No module codes, bracketed variables or framework name found in the body; no futures; no CFD quotes claimed. | §4, §6, §11, §19-§21 |

## 2. Category roll-up

| Cat | Level | Multiplier | Points | Justification |
|---|---|---|---|---|
| 1 Prompt adherence (20) | 2 | 0.40 | 8.00 | Rows 1.1/1.2/1.3 = 2/2/4, mean 2.67 -> 3; lowered one level for the restriction breach (non-overridable gates waived by cited instruction; as-of and anchor drift). |
| 2 Structure (20) | 4 | 0.85 | 17.00 | All 21 sections present and ordered; table columns and pivot depth deviate; Trade 1 SUPPRESSED row missing. Rows 4/3/4 -> 3.67 -> 4. |
| 3 Accuracy and evidence (25) | 0 | 0.00 | 0.00 | Rows 2/1/2/1 = mean 1.5 -> 2 before override; zeroed by the fabricated-source rule (three of three sampled citations internally inconsistent or impossible). |
| 4 Reasoning and judgment (20) | 3 | 0.65 | 13.00 | Rows 3/4/2/4 plus card construction 0 = 2.6 -> 3. Reading of the tape and cross-asset logic is sound; the card set contradicts the report's own regime and the fixed gates. |
| 5 Currency, restrictions, transparency (15) | 3 | 0.65 | 9.75 | Rows 3/3/4/1 = 2.75 -> 3. |

## 3. Total, band, override check

- Total = 8.00 + 17.00 + 0.00 + 13.00 + 9.75 = 47.75, rounded to **48**. Band: **Low** (40-59).
- Override check: `hallucinated_source` applies (sources whose quoted figures contradict their own use or whose date is after the as-of): cap Low, C3 = 0. A restriction breach (non-overridable suppression gates, synthesised range end-points) also applies independently (cap Moderate, C1 down one level); C1 has been lowered accordingly and the stricter label is recorded. The cap does not change the arithmetic result (48 is already inside Low).

### Category 3 evidence: report vs level file (cash basis; points; report minus data)

| Session | Field | Report | Data (cash) | Delta | Verdict |
|---|---|---|---|---|---|
| 24 Jun | O / H / L / C | 10,462.0 / 10,506.5 / 10,415.5 / 10,470.0 | 10,422.2 / 10,468.6 / 10,400.6 / 10,455.1 | +39.8 / +37.9 / +14.9 / +14.9 | O, H, L, C all outside tolerance (C also +19.5 vs full close 10,450.5) |
| 25 Jun | O / H / L / C | 10,472.0 / 10,545.0 / 10,460.0 / 10,529.9 | 10,427.6 / 10,577.7 / 10,413.8 / 10,538.0 | +44.4 / -32.7 / +46.2 / -8.1 | O, H, L, C outside tolerance; high understated by 32.7 |
| 26 Jun | O / H / L / C | 10,530.2 / 10,530.2 / 10,404.7 / 10,512.0 | 10,498.3 / 10,516.4 / 10,401.4 / 10,516.4 | +31.9 / +13.8 / +3.3 / -4.4 | O, H outside; L, C ok |
| 29 Jun (D-1) | O / H / L / C | 10,500.0 / 10,524.0 / 10,455.0 / 10,478.5 | 10,505.9 / 10,524.3 / 10,468.8 / 10,497.8 | -5.9 / -0.3 / -13.8 / -19.3 | L outside; **C off by 19.3 (>15): Category 3 failure** |
| 30 Jun (D) | row | present (O 10,478.0 H 10,521.7 L 10,476.3 C 10,506.5) | not in slice (data ends 29 Jun) | n/a | out of window for a D-1 as-of report; unverifiable and impermissible here |

Eight of twelve O/H/L fields (24-29 Jun) exceed the 10-pt tolerance; three of four closes exceed 5 pts.
RSI2: 26 Jun 77.0, 29 Jun 0.0, 30 Jun 45.5 reproduce from the report's own closes (arithmetic correct). The D-1 RSI2 of 0.0 coincides with the cash value (0.00); the full-day value is 45.97.
ATR14: report ~95 (one card) vs 114.81 cash / 132.08 full.

Daily pivots (report built from its own 29 Jun H 10,524 / L 10,455 / C 10,478.5; arithmetic correct) vs cash level file:

| Level | Report | Data | Delta |
|---|---|---|---|
| R3 | 10,585.7 | 10,580.63 | +5.1 |
| R2 | 10,554.8 | 10,552.47 | +2.3 |
| R1 | 10,516.7 | 10,525.13 | -8.4 |
| P | 10,485.8 | 10,496.97 | -11.2 |
| S1 | 10,447.7 | 10,469.63 | -21.9 |
| S2 | 10,416.8 | 10,441.47 | -24.7 |
| S3 | 10,378.7 | 10,414.13 | -35.4 |

Weekly pivots (report implies W/E 26 Jun H 10,545 / L 10,404.7 / C 10,512; data week 22-26 Jun H 10,577.7, L 10,328.1 on 23 Jun, C 10,516.4):

| Level | Report | Data | Delta |
|---|---|---|---|
| R3 | 10,710.0 | 10,869.63 | -159.6 |
| R2 | 10,627.5 | 10,723.67 | -96.2 |
| R1 | 10,569.8 | 10,620.03 | -50.2 |
| P | 10,487.2 | 10,474.07 | +13.1 |
| S1 | 10,429.5 | 10,370.43 | +59.1 |
| S2 | 10,347.0 | 10,224.47 | +122.5 |
| S3 | 10,289.2 | 10,120.83 | +168.4 |

The report's weekly range uses only the 26 Jun low (10,404.7) and the 25 Jun high 10,545, missing the week's actual low (23 Jun) and high.

Monthly pivots (May 2026; the report calls them "coarse estimates"; implied May H 10,700.1 / L 10,250.1 / C 10,360.0 vs data H 10,560.0 / L 10,141.2 / C 10,410.0):

| Level | Report | Data | Delta |
|---|---|---|---|
| R3 | 11,073.3 | 11,018.4 | +54.9 |
| R2 | 10,886.7 | 10,789.2 | +97.5 |
| R1 | 10,623.3 | 10,599.6 | +23.7 |
| P | 10,436.7 | 10,370.4 | +66.3 |
| S1 | 10,173.3 | 10,180.8 | -7.5 |
| S2 | 9,986.7 | 9,951.6 | +35.1 |
| S3 | 9,723.3 | 9,762.0 | -38.7 |

Swings: report 5-session band 10,405-10,545 vs data 10,328.1-10,577.7; report 25-session band 10,360-10,545 vs data 10,126.2-10,577.7.

## 4. Card Integrity (linter rows copied verbatim from `qa/ftse_qa1/lint_static/2026-06-30.csv`; separate from the 100)

| card_id | strategy | flags | dud | card score |
|---|---|---|---|---|
| 2026-06-30_Trade_1 | Trade 1 - Daily Directional | CLEAN | False | 100 |
| 2026-06-30_Trade_2 | Trade 2 - Pivot (range-aware) | CLEAN | False | 100 |
| 2026-06-30_Trade_3B | Trade 3B - Mean-Reversion (Transitional/Range regime) | CLEAN | False | 100 |

Report-level Card Integrity = 100 (n_cards 3, n_duds 0, n_warns 0). The static linter checks geometry only; the construction defects above (gates, regime fork, anchor, leg R) are scored in Category 4 and are not visible to it.

## 5. Feedback

See `qa/ftse_qa1/2026-06-30_feedback.md`.
