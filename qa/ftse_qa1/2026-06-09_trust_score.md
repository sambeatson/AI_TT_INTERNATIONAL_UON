# Trust Score v3.7 - FTSE 100 Daily Report, D = 2026-06-09 (run ftse_qa1)

Report: `reports/md/FTSE100_Report_09Jun2026.md` | Level file: `data/levels/UK100_by_date/2026-06-09.csv` (`last_bar_date` = 2026-06-08 < D, leak-free, checked) | Slice: UK100 M15 to 2026-06-08 22:45 broker, cash window 10:00-18:30 broker.
D = Tuesday 9 Jun 2026, so **D-1 = Monday 8 Jun 2026**. The report is "as of close 5 June" (Friday) and omits the 8 Jun session entirely.

## Machine-readable result
```
c1=1
c2=4
c3=0
c4=3
c5=3
total=44
band=Low
override=hallucinated_source
card_integrity=100
n_cards=3
n_duds=0
n_warns=0
```
(n_cards counts all 3 card rows; 2 are non-suppressed and scored. Restriction breach (module codes M1/M5 in the report) also applies and is the reason C1 is lowered one level; the single `override=` field records the more severe cap.)

## 1. Category 3 data checks (report vs level file / slice, basis = cash, as the report claims "Cash GBP")

### 1a. D-1 and the 5-day table (report minus slice cash, points)
| Session | Open | High | Low | Close |
|---|---|---|---|---|
| Mon 1 Jun | +30.6 | +23.5 | +73.9 | **+77.8** (10402.30 vs 10324.5) |
| Tue 2 Jun | +41.6 | +57.1 | +38.9 | **+73.0** (10448.60 vs 10375.6) |
| Wed 3 Jun | **+97.2** | **+86.1** | +17.1 | +9.5 (10351.20 vs 10341.7) |
| Thu 4 Jun | +50.2 | +29.5 | **+82.1** | +17.0 (10360.32 vs 10343.3) |
| Fri 5 Jun | -22.7 | -1.3 | -0.4 | -6.2 (10368.05 vs 10374.2) |
| **Mon 8 Jun (true D-1)** | **absent** | absent | absent | **absent** (slice cash: O 10309.9 / H 10412.8 / L 10307.1 / C 10370.4; full-day C 10354.1) |

- Closes within the 5-pt tolerance: 0 of 5; outside 15 pts: 3 of 5 (1 Jun, 2 Jun, 4 Jun; two by more than 70 pts). O/H/L within 10 pts: 2 of 15 (Fri 5 Jun H and L only).
- Synthesis tell: the report's Open equals the prior close to the cent on 2 Jun (10402.30), 3 Jun (10448.60), 4 Jun (10351.20), i.e. no gap data; §5 admits 1-3 Jun were "reconstructed from the provider news stream and weekly-change reconciliation". Slice opens differ from prior closes by 8-97 pts.
- D-1 identity: stated D-1 close 10,368.05 (Fri) vs true D-1 close 10,370.4 cash / 10,354.1 full-day (Mon). The numerical gap is small but it is a different session; the 8 Jun range (10307.1-10412.8) and bounce are missing from every section.
- RSI2 arithmetic: reproduces from the report's own closes for 3-5 Jun (32.2, 8.6, 100.0 - tool `--closes` check); 1-2 Jun not testable. True D-1 RSI2 (cash) = 89.05, full-day 25.49; report quotes 100.0 for Fri.
- ATR14: not stated in §9 or §21 headline; only "ATR~86" in the Trade 3C caveat. Level file: 99.07 cash / 121.35 full (cash delta -13.1, -13%).
- KER: report "KER -0.19, Trending Down - Strong". Raw KER(13) on slice cash closes is +0.09 (as of 8 Jun) / +0.16 (as of 5 Jun), positive; a magnitude of 0.19 is weak, not "Strong". Not reproducible.
- Range position: report says "lower quartile" (§1), "25%" (§9), "lower third" (§11) - three different statements, and the report's own §6 gives 32.6%. Slice: close at 54.7% of the 25-day range (10141.2-10560.0) and 74.2% of the 5-day range (10236.5-10417.0). The "range-bottom bias" premise is not supported by the data.

### 1b. Pivots (report minus level file, points; report labels all tiers "Indicative")
| Tier | Daily vs cash | Daily vs full | Weekly vs cash | Monthly vs cash |
|---|---|---|---|---|
| P | -7.2 | +4.1 | **+81.8** | **+293.3** |
| R1 | **-26.0** | -21.0 | **+48.0** | **+437.7** |
| R2 | **-41.8** | -48.1 | +37.3 | **+852.5** |
| R3 | **-60.6** | -73.2 | +3.5 | **+996.9** |
| S1 | +8.6 | +31.2 | **+92.5** | **-121.5** |
| S2 | **+27.4** | +56.3 | **+126.3** | **-265.9** |
| S3 | **+43.2** | +83.4 | **+137.0** | **-680.7** |
- Daily: the report's P 10356.21 = (H+L+C)/3 of **Thursday** 4 Jun (10389.7/10318.6/10360.32), not Friday's own table row (Fri H/L/C would give P 10371.78, R1 10412.01, S1 10327.81). So the daily pivots are a session stale even by the report's own numbers, and two sessions stale vs D-1.
- Weekly: P 10424.33 does not match the 1-5 Jun week (cash P 10342.57) nor the report's own §6 week (H 10470.1 / L 10318.6 / C 10368.05 would give P 10385.58).
- Monthly: implied inputs (P 10663.67, R1 11037.33, S1 10059.33) require a May high of ~11,268 and low of ~10,290. May cash high was 10,560.0, low 10,141.2, close 10,410.0 (monthly P 10370.4). The monthly table (R5 13,971.33) is impossible for this index.
- Format: three tiers each side are required; the report prints five (R5-S5) with unsourced extension formulas.

### 1c. Sources (3.2)
1. LSE (FTSE Russell), 29 May-5 Jun, "range to 10,910.55": impossible. Highest slice high since 29 May = 10,462.0 (and the report's own §6 maximum = 10,470.1). The figure is used nowhere else. Counted as fabricated per brief 3.2.
2. Trading Economics: §4 says official close 10,368.05 (+7.7 pts, +0.07%); §13a TE headlines say "gained 15 points or 0.14 percent" and §4 prints "close ~10,375". The cited source contradicts its own quoted figure (slice cash close 10,374.2 is consistent with the +15 / ~10,375 version).
3. Kalkine, 8 Jun 08:52, labelled "next-session pre-open colour"; 8 Jun is the D-1 session, not the next session; the same report uses 8 Jun STOXX closes (§6, §13a) and an 8 Jun "FTSE drops 0.28%" article yet carries no FTSE 8 Jun bar. Date handling is internally inconsistent.
Also: §19/§20 state Investing.com returned a stale window, yet it is listed as Src B for all five rows of §6 and as the origin of the 5 Jun O/H/L.

### 1d. Counters (slice, D-1 = 8 Jun)
USDX 5-day rising, ~100.03-100.09: consistent. S&P 500 Fri -2.9% (report -2.6%, close enough on a CFD basis); VIX +15.9% Fri: "spiked" consistent. Not reflected: Mon 8 Jun S&P +0.61%, VIX -4.4%, USDX -0.06% (the D-1 counter state). DAX/Euro Stoxx not in slices: unchecked. §13d omits the dated D-day events present in the calendar (EUR Industrial Production and Trade Balance 07:00 UK; USD Trade Balance 13:30 UK; USD Existing Home Sales 15:00 UK, HIGH; ECB Lagarde speech 17:30 UK, HIGH); it lists only undated "wk of 9 Jun" items.

## 2. Section 7 checklist
| Row | Evidence / notes | Score |
|---|---|---|
| 1.1 Variables respected | FTSE cash primary, USDX/S&P/DAX/STOXX counters, GBP points, 5-session lookback present. But as-of is 5 Jun (D-1 is 8 Jun); lookback window 1-5 Jun not 2-8 Jun; source tiers: only one index-provider row, no exchange/sell-side; anchor overridden to 00:00 UK (07:00 required), logged in §20 only. | 2 |
| 1.2 Coverage & currency consistent | §2, §6, §10, §21c all stop at Fri 5 Jun; 8 Jun data is used for STOXX and news but not for the FTSE; run timestamp 8 Jun 21:48 UK proves D-1 data existed. | 1 |
| 1.3 Audience & tone | Strategist tone, risk-review framing, no retail language. | 4 |
| 2.1 Sections present & ordered | §1-§21 present in order incl. §13a-d and §21a-d; Trade 1 SUPPRESSED row present. | 5 |
| 2.2 Scorecard as table | §6 table has all columns; §11 three pivot tables but five tiers each side (brief: three), monthly table implausible. | 4 |
| 2.3 Method steps visible | §4/§5 observations-to-consensus shown; §8 candle-by-candle + sequence; §9 regime with overlap/persistence/VOLator. §7 Charts heading is empty: no image, caption or placeholder. | 3 |
| 3.1 Quantitative claims sourced | §12/§14 figures (WTI 90.5, Brent 93, gold 4,331, 10Y gilt 4.88%, CPI 2.80%, GBP/USD 1.334, mining stock % moves, S&P -2.6%, DAX -0.75%) carry no source or cross-reference. | 2 |
| 3.2 Citations exist & contain data | See 1c: LSE 10,910.55 impossible; TE self-contradictory; Kalkine mis-dated role. Counts as fabricated. | 0 |
| 3.3 Calculations transparent | RSI2 reproduces (3-5 Jun); pivot arithmetic internally correct but fed with Thursday H/L/C; ATR not stated in §9; KER -0.19 not reproducible and mislabelled "Strong"; §21a components (+0.25 -0.10 -0.045 -0.015 +0.029) sum to +0.119, not the stated +0.17, only five of six signals shown, and Kaufman contributes +0.029 despite a "Trending Down" read. | 2 |
| 3.4 Numbers reconcile | 10,368.05 consistent across §1/§3/§4/§6; but TE +15 vs +7.7 pts, ~10,375 vs 10,368.05; pivots in §11 vs §6 Friday row do not reconcile; ATR only on card (86 vs 99.07); range position stated three ways; closes off slice by 78/73/17 pts. | 1 |
| 4.1 Pillars conclude | §8 Indecision, §9 Transitional, §10 MIXED, §11 narrative, §15; §12 and §14 close with item labels but no single direction label. | 3 |
| 4.2 Cross-asset interpreted | §10 gives mechanisms (USD tightening vs GBP translation for overseas earners; US beta; DAX; STOXX divergence); oil/energy weight handled in §12 not §10. Counter state is stale (no 8 Jun). | 4 |
| 4.3 Synthesis reconciles tensions | KER-vs-range tension addressed. Unreconciled: §21a gives short-term technicals the full +0.25 while §1/§8 call the state "Transitional/Mixed"/"Indecision"; §21a "no directional conflict" while Trade 2 is long and Trade 3C short; "range-bottom" thesis contradicted by slice (54.7% of 25-day range). | 2 |
| 4.4 Calibrated language | §17 is one sentence; §3 gives confidence. "High" confidence on a close the report's own TE source contradicts. | 3 |
| 4.5 Card construction (protocol) | See section 4 below: Trade 2 fade under TRANSITION, TP1/TP2 0.68R/1.21R instead of 1R/2R, stop lacks buffer and sits above the 5-day low, all-indicative tiers not suppressed; Trade 3C keyed to a 5-day swing not the 25-day boundary, targets/stop off-rule, BE level on the wrong side, ATR wrong. | 1 |
| 5.1 Data dated; staleness flagged | Items are dated; single-source O/H/L flagged; the one-session staleness of the whole analysis is not flagged; 8 Jun mis-labelled "next-session". | 3 |
| 5.2 Assumptions up front | §19 states the lenient-corroboration instruction and single-source pivot propagation; caveats on both cards; anchor override in §20 (no live card carries it, Trade 1 suppressed). | 4 |
| 5.3 Red flags surfaced | §12/§15 risks, Tier-1 oil catalyst carried into card caveats; but D-day scheduled HIGH events (US Existing Home Sales, Lagarde) absent from §13d. | 3 |
| 5.4 Restrictions honoured | Module codes "M1" and "M5" appear in §20 (breach); opens synthesised as prior close and presented in the OHLC table with an Investing.com source column the report elsewhere says returned stale data; Trade 2 issued although every pivot tier is single-source-indicative. | 1 |

## 3. Category roll-up
| Cat | Rows mean | Level | Mult | Points | Justification |
|---|---|---|---|---|---|
| C1 Prompt adherence (20) | 2.33 -> 2, minus 1 for restriction breach | **1** | 0.20 | 4.0 | Wrong as-of session (stale by one trading day), anchor overridden, module codes in output. |
| C2 Structure (20) | 4.00 | **4** | 0.85 | 17.0 | Complete and ordered; chart section empty, five-tier pivots. |
| C3 Accuracy & evidence (25) | 1.25 -> 1; override | **0** | 0.00 | 0.0 | Fabricated/impossible source figure (LSE 10,910.55); closes off by up to 78 pts; monthly pivots impossible; D-1 session missing. |
| C4 Reasoning & judgment (20) | 2.60 -> 3 | **3** | 0.65 | 13.0 | Sound structure and mechanisms, but regime premise contradicted by data and card construction off-rule. |
| C5 Currency & transparency (15) | 2.75 -> 3 | **3** | 0.65 | 9.75 | Good disclosure of single-source status; stale as-of, restriction breach, missing D-day events. |

Sum = 43.75, rounded **total = 44**.

## 4. Total, band, override
- Total 44 -> band **Low** (40-59).
- Override check: **hallucinated_source** applied (LSE figure 10,910.55 impossible against slice and the report's own table; TE self-contradiction): cap Low, C3 = 0. Restriction breach (module codes M1/M5 in §20; synthesised opens/prior-close reconstruction presented in the scorecard) also applies: cap Moderate (not binding) and C1 lowered one level (2 -> 1).

## 5. Card Integrity (linter rows copied verbatim from `qa/ftse_qa1/lint_static/2026-06-09.csv`)
| card_id | strategy | flags | dud | per-card score |
|---|---|---|---|---|
| 2026-06-09_Trade_1 | Trade 1 - Daily Directional | SUPPRESSED | False | suppressed (excluded) |
| 2026-06-09_Trade_2 | Trade 2 - Pivot, regime-aware (TRANSITION -> fade toward the corroborated floor) | CLEAN | False | 100 |
| 2026-06-09_Trade_3C | Trade 3C - Momentum-Breakout; TRANSITION regime, anchor = 25-session range boundary | CLEAN | False | 100 |

Report-level Card Integrity = mean(100, 100) = **100**; n_cards=3, n_duds=0, n_warns=0. The static linter does not test M5 construction; those defects are scored under C4 row 4.5 and itemised in the feedback file.
