# Trust Score v3.7 - S&P 500 Daily Report 23 June 2026 (run regen_20260906_qa1, late-added date)

Report: `reports/md/SP500_Report_23Jun2026.md` - D = 2026-06-23 - D-1 = 2026-06-22 - slice `US500_upto_2026-06-22.csv`

c1=3
c2=4
c3=2
c4=2
c5=3
total=58
band=Low
override=restriction breach (applied: C1 4 -> 3; Moderate cap not binding at 58); no fabricated-source override
card_integrity=90
n_cards=3
n_duds=0
n_warns=2

(c1..c5 are rubric levels 0-5; points are in the roll-up table. n_cards counts all three linter rows; Card Integrity 90 is the mean over the two non-suppressed cards.)

## Reference numbers used (engine/qa_slice_stats.py, cash session 16:30-23:00 broker)
- D-1 cash close 7479.30 (full-day 23:45 bar 7481.80); report states 7472.79 (delta -6.5, inside the 10-pt failure line).
- ATR14 111.76 (cash bars) / 126.36 (full-day bars). The report states no ATR(14) anywhere.
- Daily pivots, D-1 cash: P 7495.13 R1 7522.97 S1 7451.47 R2 7566.63 S2 7423.63 R3 7594.47 S3 7379.97.
- Weekly pivots (15-19 Jun cash): P 7495.37 R1 7582.23 S1 7407.33 - the report's weekly tier reconciles within 3 pts.
- Swings: 5d high 7571.40 (16 Jun) low 7408.50 (17 Jun); 25d high 7624.60 (2 Jun) low 7243.10 (9 Jun).
- RSI2 re-run on the report's own five closes (7554.29, 7511.35, 7420.10, 7500.58, 7472.79): 0.0 / 46.9 / 74.3 for 17 Jun / 18 Jun / 22 Jun. Report prints 27.0 / 63.6 / 47.2. All three testable rows fail.

### Report vs slice (cash session), points
| Date | Open (rpt / slice / d) | High | Low | Close |
|---|---|---|---|---|
| 15 Jun | 7516.75 / 7534.1 / -17.4 | 7577.92 / 7583.4 / -5.5 | 7516.75 / 7533.6 / -16.9 | 7554.29 / 7563.4 / -9.1 |
| 16 Jun | 7548.78 / 7562.9 / -14.1 | 7564.96 / 7571.4 / -6.4 | 7508.68 / 7518.2 / -9.5 | 7511.35 / 7522.9 / -11.6 (>10) |
| 17 Jun | 7524.50 / 7531.7 / -7.2 | 7532.17 / 7540.0 / -7.8 | 7402.61 / 7408.5 / -5.9 | 7420.10 / 7427.5 / -7.4 |
| 18 Jun | 7487.36 / 7514.1 / -26.7 | 7511.07 / 7518.3 / -7.2 | 7468.32 / 7472.6 / -4.3 | 7500.58 / 7502.3 / -1.7 |
| 22 Jun | 7487.36 / 7513.1 / -25.7 | 7506.32 / 7538.8 / -32.5 | 7468.32 / 7467.3 / +1.0 | 7472.79 / 7479.3 / -6.5 |

Opens fail the 8-pt tolerance on 4 of 5 days, one close fails the 10-pt line, and 22 Jun high is 32.5 below. The 22 Jun open (7487.36) and low (7468.32) equal the 18 Jun open and low to the cent.
Monthly tier: report P 7547.58 / R1 7631.86 / S1 7495.77 implies May H 7599.4, L 7463.3, C 7580.0 ("approx inputs"). Slice May cash: H 7601.8, L 7177.5, C 7584.8 (low off by about 286 pts; slice monthly P 7454.7, S1 7307.6).
Daily tier: report 22 Jun H-L = 38.0 vs slice cash 71.5 (7538.8-7467.3), so every daily level is mis-struck (report R1 7496.63 vs slice 7522.97; S2 7444.48 vs 7423.63; S3 7420.63 vs 7379.97).

## Section 7 checklist
| Row | Notes / evidence | Score |
|---|---|---|
| 1.1 Variables respected | Asset, counters (USDX first), NY as-of, 5-session lookback, USD/points/0.01 all correct. Anchor: §2 and §20 replace the 07:00 UK anchor with 09:30 ET "per instruction" - not the instance value. "Min 6 sources met" is nominal: Bloomberg gives no figure, Trading Economics is excluded, no sell-side source supplies a price. | 3 |
| 1.2 Coverage and currency consistent | All price dates D-1 or earlier; holiday handled. Drift: §3 "daily S2 to R1 band" 7,444-7,520 but 7,520.48 is R2 (§11); §13a articles dated only "Jun 2026" / "2026". | 4 |
| 1.3 Audience and tone | Strategist register, risk-review framing throughout. | 4 |
| 2.1 Sections present and ordered | §1-§21 all present in order incl. §13a-d, §21a-d; §7 shows five chart captions only (placeholder accepted). §21c table incomplete (see 3.4). | 4 |
| 2.2 Scorecard as table | §6 is a table with all required columns; daily/weekly/monthly pivot tables ordered R5 to S5 (superset of R3-S3). | 4 |
| 2.3 Method steps visible | §4-§5 observations to consensus; §8 candle-by-candle plus sequence; §9 regime stated but persistence/overlap/VOLator slope are adjectives, no ATR(14), KER parameters not given. | 3 |
| 3.1 Quantitative claims sourced | §10 counter ranges (USDX 99.8-100.7, VIX 16.8-17.2, DAX 24,990-25,140) undated and unsourced; §1 items (Russell 3,000, Alphabet -5%, 299/503) uncited; §12/§14 cite only "FOMC statement / SEP". | 2 |
| 3.2 Citations exist and contain data | Spot checks: FRED 18 Jun 7,500.58 (consistent with §6); CNBC 22 Jun 7,472.79 -0.37% (7472.79/7500.58-1 = -0.37%, consistent); Yahoo 7,475.34 -0.34% (consistent). None impossible, so no fabricated-source override. Concerns: Investing.com 22 Jun value is "CNBC-aligned" (not independent); 22 Jun open and low duplicate 18 Jun and have no named source. | 2 |
| 3.3 Calculations transparent | Pivot arithmetic reproduces from the report's own H/L/C (daily, weekly). RSI2 fails 3 of 3 testable rows (27.0/63.6/47.2 vs 0.0/46.9/74.3); Trend labels for 18 and 22 Jun therefore wrong (should be Neutral). ATR(14) never stated; KER(13, EMA 3) parameters absent; §21a components (-0.12, -0.06, +0.04, +0.005 = -0.135) do not sum to the stated -0.22 and omit two of six signals. | 1 |
| 3.4 Numbers reconcile | D-1 close 7,472.79 identical in §1/§3/§4/§6/§11/§18; card levels match §11. Breaks: Trade 2 "124 points / 12,400 ticks" vs actual 23.2 pts; Trade 3B TP1 7,481 "range mid / daily P" matches neither (P 7,482.48); §21c missing rows (Trade 2 on 17 Jun, Trade 3B on 22 Jun, Trade 1 on 3 of 5 days) while §21d quotes "4/5" and "2/4"; accuracy vs slice per table above. | 3 |
| 4.1 Pillars conclude | §8, §9, §10 end in labels; §12 and §14 list drivers with price-direction tags but no closing direction label. | 3 |
| 4.2 Cross-asset interpreted | Mechanism given for USDX (translation); VIX and DAX mechanisms are one-phrase labels; USDX "confirms mild risk-on" not tied to the regime call. | 3 |
| 4.3 Synthesis reconciles tensions | KER-on-boundary vs regime handled. Unreconciled: §9/§1 say Transitional while §21 builds RANGE Trade 2 and 3B; simultaneous short (Trade 2) and long (Trade 3B) cards under a "mild downside" §17; RSI2 errors feed the §8 "momentum re-fading" story. | 2 |
| 4.4 Calibrated language | §17 is one sentence but stacks hedges and contradicts itself ("most likely ... mild downside lean ... biased lower only on a hot print"); confidence Medium stated in §3/§18; §21a label "SHORT (mild) / NEUTRAL" is not a permitted state below threshold. | 3 |
| 4.5 Card construction and score derivation (protocol table) | Regime/fork mismatch; Trade 2 shipped with every tier flagged indicative; 3B entry outside its band; invalidation defects; ATR/R-ratio/reference close absent; score not traceable. See feedback. | 1 |
| 5.1 Data dated, staleness flagged | Prices dated; 22 Jun O/H/L flagged indicative. §13a sources undated; Oppenheimer "outlook for 2026" is a year-ahead view used as June sentiment; counter figures undated. | 3 |
| 5.2 Assumptions up front | Anchor deviation and indicative pivots disclosed in §2/§19/§20 and caveats, but the anchor is not on the cards and is attributed to an instruction. | 3 |
| 5.3 Red flags surfaced | §12/§15 carry PCE, FOMC, tech-concentration risks; PCE collision on both cards. Micron (24 Jun) collision not carried into card caveats. | 4 |
| 5.4 Restrictions honoured | Breaches: (a) "daily-open anchor" and "v2.1 baseline, locked" survive the naming scan (§2, §20); (b) run-time instruction cited as authority twice - anchor override (§2, §20) and "Per instruction ... leniency on corroboration" (§19); (c) Trade 2 emitted although §19/§11 state the daily tier is indicative and the weekly/monthly tiers are single-source or "approx" with no second source shown; (d) 22 Jun open/low copied from 18 Jun and presented in the table; (e) §7 VOLator series described as "illustrative". | 1 |

C4 mean over 4.1-4.5 = 2.4 -> 2. C1 mean 3.67 -> 4, reduced one level by the restriction override -> 3.

## Category roll-up
| Cat | Level | Multiplier | Points / max | Justification |
|---|---|---|---|---|
| C1 Prompt adherence | 3 (4 before override) | 0.65 | 13.00 / 20 | Variables mostly right; anchor replaced, source tiers nominal; restriction override lowers one level. |
| C2 Structure | 4 | 0.85 | 17.00 / 20 | All 21 sections and sub-sections present; §7 images not verifiable; §21c incomplete; §9 qualitative. |
| C3 Accuracy and evidence | 2 | 0.40 | 10.00 / 25 | RSI2 not reproducible, opens/high off by 14-33 pts, monthly tier built on a May low about 286 pts too high, ATR absent, claims unsourced. |
| C4 Reasoning and judgment | 2 | 0.40 | 8.00 / 20 | Cross-asset and synthesis adequate; card construction and score derivation fail. |
| C5 Currency and transparency | 3 | 0.65 | 9.75 / 15 | Dating and flags mostly present; restrictions row at 1. |

## Total, band, override
Total = 13.00 + 17.00 + 10.00 + 8.00 + 9.75 = 57.75 -> **58**. Band: Low (40-59).
Override: restriction breach applies (C1 down one level; Moderate cap of 74 not binding). No fabricated-source override: the three spot-checked citations are internally consistent and none is impossible; the 22 Jun O/L duplication is scored as a no-synthesis breach under 5.4, not as a fabricated source.

## Card Integrity (copied verbatim from lint_static/2026-06-23.csv; not re-derived)
| card_id | strategy | flags | dud | Integrity |
|---|---|---|---|---|
| 2026-06-23_Trade_1 | Trade 1 - Daily Directional | SUPPRESSED | False | excluded (suppressed) |
| 2026-06-23_Trade_2 | Trade 2 - Pivot (regime-aware), RANGE protocol | WARN_TP3_ORDER | False | 90 |
| 2026-06-23_Trade_3B | Trade 3B - Mean-Reversion (Transitional/Range regime fork) | WARN_R_TINY(0.28xATR) | False | 90 |

Report-level Card Integrity = mean(90, 90) = 90. n_cards=3, n_duds=0, n_warns=2.
