# Trust Score QA — FTSE 100 report for Mon 13 July 2026 (run ftse_qa1)

Report: `reports/md/FTSE_EuroStoxx_Report_13Jul2026.md` · D = 2026-07-13 · D-1 = Fri 2026-07-10
Level file check: `last_bar_date` = 2026-07-10 < D (leak-free, confirmed). Basis compared: `_cash` (report claims cash index), cash window 10:00–18:30 broker (08:00–16:30 London) via `engine/qa_slice_stats.py`.
Reviewer knowledge cut: nothing on or after D was consulted or is asserted here.

## Result (machine-readable)
```
c1=2
c2=3
c3=2
c4=3
c5=3
total=54
band=Low
override=restriction_breach
card_integrity=100
n_cards=3
n_duds=0
n_warns=0
```
Override note: restriction_breach applied (module codes "M2", "M5" and "weight-lock / v2.1 baseline" inside §20; reconstructed/interpolated H/L presented in the validated OHLC table). C1 was 3 on the raw checklist mean and is reduced one level to 2. The Moderate cap (60–74) does not bind because the arithmetic total (54) is already Low. No hallucinated-source override: no source could be proven fabricated (reviewer cannot fetch), though several figures conflict with the slice (see Category 3).

## 1. Section 7 checklist

| Row | Reviewer notes | Evidence (location) | Score |
|---|---|---|---|
| 1.1 Variables respected | Asset = FTSE 100 cash, Euro Stoxx 50 reference only with no cards ✓; counters USDX / S&P 500 / DAX 40 ✓ (header, §10); as-of D-1 London close ✓; 5-session lookback ✓; GBP/index points ✓. Gaps: the six §4 sources are aggregators/media (Yahoo, Trading Economics, bbntimes, Investing.com, Edge, wallstreetnumbers), with no index-provider / exchange / sell-side tier for prices; the 07:00 UK anchor is described only as a "pre-open frame" and overridden to "reference the 13 Jul session", and no card states an anchor clock time or is a market entry at the anchor; §6 source columns are abbreviations ("SG", "WSN", "Inv", "TE") never defined. | header, §2, §4, §6, §10, §20, cards | 3 |
| 1.2 Coverage & currency consistent | Data dates all ≤ D-1, GBP throughout. Calendar drift: 16 Jul 2026 is a Thursday and 17 Jul a Friday, but the report labels them "Wed 16 Jul" and "Thu 17 Jul" in §1, §12, §13d, §14, §18 and card caveats. §13d is not in date order (Wed 16 listed before Mon 13). | §1, §12, §13d, §14, §18, §21b | 3 |
| 1.3 Audience & tone | Strategist register, risk-review framing, no retail tone. Footer disclaimer acceptable. | §1, §18 | 4 |
| 2.1 Sections present & ordered | §1–§21 all present, in order; §13a–d and §21a–d present; §17 is one sentence. §7 is a placeholder paragraph with no per-chart captions (accepted per brief, noted). §21c labelled "5-Session" but contains four dates (7–10 Jul); no 6 Jul rows. | headings, §7, §21c | 4 |
| 2.2 Scorecard / pivots as tables | §6 is a table, but it collapses Source A / Source B / Final into one "Sources" column. §11 has daily and weekly pivot tables ordered R3→S3, but NO monthly pivot table (level file has June monthly pivots). | §6, §11 | 3 |
| 2.3 Method steps visible | §4→§5 observation → consensus ✓; §8 candle-by-candle + sequence ✓; §9 regime has persistence and KER but VOLator is qualitative only (no value, no ATR14, no overlap measure), and the KER window / smoothing is not stated; charts only as placeholder. | §4–§9 | 3 |
| 3.1 Quantitative claims sourced | §1/§12/§14 carry many unsourced figures: AZN index weight "~7–8%", Brent "<$76", GBP "$1.34", PMI 49.3, VIX "~16", USDX "≈100.5→99.4", S&P "7,537→7,575", Vodafone "+13%", "$5.95bn" — none point to §4/§6/§13. | §1, §10, §12, §14 | 2 |
| 3.2 Citations exist & contain data | Cannot fetch. Three spot checks: (a) Yahoo 10,497.29 / Trading Economics 10,497 — consistent with each other, but the report asserts a ±0.10-pt tolerance and then accepts Δ 0.29 (§5, §20) — self-contradictory; (b) wallstreetnumbers 7 Jul 10,691.98 — used consistently in §6, but conflicts with slice 7 Jul cash close 10,680.1 (Δ +11.9) and full-day 10,650.5; (c) Investing.com Fri O/H/L 10,471.94 / 10,513.90 / 10,462.75 — Δ vs slice cash −18.2 / +9.1 / +11.7. §13a article table has no dates at all (Morningstar, Sunday Guardian, Hilsden etc. undated). Not proven fabricated; not clean. | §4, §5, §6, §13a, §20 | 2 |
| 3.3 Calculations transparent | Pivot arithmetic reproduces exactly from the report's own H/L/C (daily and weekly) ✓. RSI2 does NOT reproduce from the report's own closes (seed 10,679.03 + five closes): Tue 62.7 ✓; Wed reported 41.5 vs 71.1; Thu 3.5 vs 0.0; Fri 20.9 vs 10.7. ATR(14) never stated (only "~60–70-pt norm" vs level file 122.28 cash / 133.35 full). KER −0.62 reproduces from the closes (5-change window incl. seed) but KER(13, EMA3) window is not stated. §21a: listed contributions sum −0.09−0.09−0.04+0.03+0.01 = −0.18, not −0.21; only five of six signals shown; no signal×weight table. | §6, §9, §11, §21a | 2 |
| 3.4 Numbers reconcile | D-1 close 10,497.29 identical in §1/§3/§4/§6/§11 ✓. Breaks: (i) daily H/L called "single-lead" in §5 but "CORROBORATED" in §11/§19; §4 shows O/H/L from Investing.com only; (ii) AZN "~6% over two sessions" (§1, §12) vs "AZN −6.2%" on Thursday alone (§13c); a ~6% fall in a ~7.5% weight cannot produce a −1.94% index day; (iii) S&P "7,537→7,575, +1% wk" is +0.5% on those numbers; (iv) Euro Stoxx Fri −0.23% vs 6,284.27→6,266.83 = −0.28%, and its Fri open 6,266.8 ≈ close 6,266.83; (v) §11 narrative: close "just below" and "fractionally above" daily P in the same sentence; (vi) Trade 1 "TP1 +1R ≈ 50 pts" with R = 84; (vii) §21d "Trade 2 triggered 2/4" but only 3 Trade 2 rows in §21c; (viii) Wed 8 Jul close 10,679.0 ≈ the 3 Jul seed close 10,679.03; opens for Tue and Wed equal the prior close to the penny. | §1, §5, §10, §11, §13c, §19, §21 | 1 |
| 4.1 Pillars conclude | §8 (Exhaustion — reversal risk), §9 (bearish bias, KER Trending Down), §10 (MIXED) end in labels. §12 and §14 are bullet lists with per-bullet tags/none and no closing direction label. | §8–§14 | 3 |
| 4.2 Peer/cross-asset interpreted | §10 gives USD-translation, US-beta and euro-proxy mechanisms, but the DAX mechanism is a restatement; facts under it are wrong vs slice: USDX is flat-to-up (3 Jul 100.82 → 10 Jul 100.98, +0.16%), not "Falling ≈100.5→99.4"; S&P 500 CFD 7,504.6 → 7,579.9 (+1.0%), direction right, levels differ. | §10 | 2 |
| 4.3 Synthesis reconciles tensions | Tensions identified (S&P vs bearish read, sentiment vs price, KER vs regime) but §15/§16 leave the S&P tension "flagged, not resolved"; §9 prescribes a "range/reduced-conviction protocol" while the cards declare TRANSITION; cards run short (T1, T2) and long (T3A) simultaneously. | §9, §15, §16, §21 | 3 |
| 4.4 Calibrated language | §17 is exactly one sentence; confidence "Medium" in §3/§18. "LONG/SHORT-neutral" (§1) is loose. | §1, §3, §17 | 4 |
| 4.5 Card construction (protocol: scored in Cat. 4) | See Section 3 below: Trade 1 issued with |score| 0.21 < 0.25 gate (must be a SUPPRESSED row) and not a market entry at the anchor; Trade 1 TP1/TP2 are 0.6R / 1.6R, not 1R / 2R; Trade 2 R = 29 < 0.3×ATR14 (36.7 cash) and TP2 = 1.7R; Trade 2 is labelled TRANSITION "breakout-side" yet is a counter-trend fade at R1; Trade 3A does not follow 3A or 3C (entry mid-range, TP1 0.4R, TP1 text cites a 38.2% level below the long entry). | §21a, §21b | 1 |
| 5.1 Data dated; staleness flagged | §4 dated; reconstructed 6/8 Jul H/L flagged; STOXX 6–8 Jul flagged directional-only. §13a undated; Tue 7 Jul H/L (10,705.0 / 10,651.0) and Wed (10,712.0 / 10,662.0) are round numbers marked "Corroborated" without flag. | §4, §6, §13a, §19 | 3 |
| 5.2 Assumptions up front | Anchor-override caveat present in §2 and §20 but not on any card (cards state no anchor clock time); weekly-pivot indicative flag carried to Trade 2 caveats ✓; daily pivots wrongly declared corroborated although §5 calls the H/L single-lead. | §2, §5, §11, §19, §20, §21b | 3 |
| 5.3 Red flags surfaced | CPI collision carried onto all three cards ✓; Middle East/oil, AZN overhang, ATR inflation, sub-gate conviction all disclosed ✓. | §12, §15, §21b | 4 |
| 5.4 Restrictions honoured | BREACH: §20 names "M2 §9c formula", "M5 trace", "v2.1 baseline, weight-lock" (module codes / framework internals in the report). Reconstructed (interpolated) H/L/open values sit in the §6 table labelled "Corroborated". Trade 1 issued despite the fixed M5 suppression gate. No retail CFD OHLC basis, futures not used for confirmation, no bracketed variable names found. | §6, §20, §21 | 1 |

### Category roll-up from checklist means
| Cat | Rows | Mean | Level |
|---|---|---|---|
| 1 | 3, 3, 4 | 3.33 | 3 → **2 after restriction-breach override** |
| 2 | 4, 3, 3 | 3.33 | 3 |
| 3 | 2, 2, 2, 1 | 1.75 | 2 |
| 4 | 3, 2, 3, 4, 1 | 2.60 | 3 |
| 5 | 3, 3, 4, 1 | 2.75 | 3 |

## 2. Category 3 reconciliation — report vs level file (cash basis, D-1 = Fri 10 Jul)

Tolerance (brief §4): close |Δ| ≤ 5, O/H/L |Δ| ≤ 10. Δ = report − slice cash. "X" = outside tolerance; "XX" = close wrong by > 15 (Category 3 failure).

| Date | Field | Report | Slice cash | Δ | Flag |
|---|---|---|---|---|---|
| Mon 6 Jul (§6) | O | 10,672.9 | 10,672.4 | +0.5 | ok |
| | H | 10,717.8 | 10,726.7 | −8.9 | ok |
| | L | 10,642.0 | 10,607.9 | +34.1 | X |
| | C | 10,660.1 | 10,641.1 | +19.0 | XX |
| Tue 7 Jul | O | 10,660.1 | 10,657.8 | +2.3 | ok |
| | H | 10,705.0 | 10,739.6 | −34.6 | X |
| | L | 10,651.0 | 10,639.1 | +11.9 | X |
| | C | 10,691.98 | 10,680.1 | +11.9 | X |
| | RSI2 | 62.7 | 66.78 | −4.1 | reproduces from report closes |
| Wed 8 Jul | O | 10,691.98 | 10,634.1 | +57.9 | X |
| | H | 10,712.0 | 10,636.3 | +75.7 | X |
| | L | 10,662.0 | 10,454.7 | +207.3 | X |
| | C | 10,679.0 | 10,457.0 | +222.0 | XX |
| | RSI2 | 41.5 | 14.88 (cash); own closes 71.1 | | fails |
| Thu 9 Jul | O | 10,487.9 | 10,439.2 | +48.7 | X |
| | H | 10,539.5 | 10,468.9 | +70.6 | X |
| | L | 10,397.5 | 10,380.4 | +17.1 | X |
| | C | 10,472.45 | 10,457.0 | +15.45 | XX |
| | RSI2 | 3.5 | 0.00 (cash); own closes 0.0 | | fails |
| Fri 10 Jul (D-1) | O | 10,471.9 | 10,490.1 | −18.2 | X |
| | H | 10,513.9 | 10,504.8 | +9.1 | ok |
| | L | 10,462.8 | 10,451.1 | +11.7 | X |
| | C | 10,497.29 | 10,487.2 | +10.1 | X (close > 5, < 15) |
| | RSI2 | 20.9 | 100.0 cash / 64.75 full; own closes 10.7 | | fails |
| ATR(14) | — | not stated (§9 "~60–70-pt norm") | 122.28 cash / 133.35 full | | missing and inconsistent |

Structural finding from the slice: the large down session sits on **Wed 8 Jul** (cash 10,680.1 → 10,457.0, range 10,636.3–10,454.7), after which Thu 9 and Fri 10 are comparatively narrow (cash ranges 88.5 and 53.7 pts). The report places the shelf through Wed (close 10,679.0) and the "~281-pt gap-down candle" on Thu 9 Jul. The §7/§8/§9/§13c narrative (shelf → gap → stabilisation, "Shell lifted index above 10,670 on Wed") is built on this mis-dated row.

Seed close: report uses 3 Jul close 10,679.03; slice cash close 3 Jul = 10,660.5 (Δ +18.5).

### Pivots
Daily (report from H 10,513.9 / L 10,462.8 / C 10,497.29; arithmetic verified exact) vs `d_cash_*`:

| Level | Report | Level file | Δ |
|---|---|---|---|
| R3 | 10,571.0 | 10,564.67 | +6.3 |
| R2 | 10,542.5 | 10,534.73 | +7.8 |
| R1 | 10,519.9 | 10,510.97 | +8.9 |
| P | 10,491.3 | 10,481.03 | +10.3 |
| S1 | 10,468.7 | 10,457.27 | +11.4 |
| S2 | 10,440.2 | 10,427.33 | +12.9 |
| S3 | 10,417.6 | 10,403.57 | +14.0 |

Weekly (report from H 10,717.8 / L 10,397.5 / C 10,497.29; arithmetic exact) vs `w_cash_*` (week 2026-W28: H 10,739.6 on 7 Jul, L 10,380.4 on 9 Jul, C 10,487.2):

| Level | Report | Level file | Δ |
|---|---|---|---|
| R3 | 10,997.9 | 11,050.27 | −52.4 |
| R2 | 10,857.8 | 10,894.93 | −37.1 |
| R1 | 10,677.6 | 10,691.07 | −13.5 |
| P | 10,537.5 | 10,535.73 | +1.8 |
| S1 | 10,357.3 | 10,331.87 | +25.4 |
| S2 | 10,217.2 | 10,176.53 | +40.7 |
| S3 | 10,036.9 | 9,972.67 | +64.2 |

Monthly: **absent** from §11. Level file (`m_cash_*`, 2026-06): P 10,412.17 · R1 10,698.13 · R2 10,894.77 · R3 11,180.73 · S1 10,215.53 · S2 9,929.57 · S3 9,732.93.

### Counters and calendar (slice)
- USDX 3 Jul close 100.82 → 10 Jul close 100.98 (flat/slightly up); report says falling ≈100.5→99.4. Wrong direction and level.
- S&P 500 CFD 7,504.6 → 7,579.9 (+1.0%); report 7,537→7,575 (+0.5% on its own figures, stated +1%).
- VIX close 16.66 (report "~16").
- Calendar for D: no Eurozone/Germany final CPI on 13 Jul (EUR rows are Current Account, BTF auctions, Schnabel speech 19:45 broker); Fed Bowman, Waller speeches and US budget balance on 13 Jul are omitted from §13d. Final EUR CPI/HICP printed 10 Jul (−0.3 m/m, in line) and is omitted from §13c; 6 Jul UK Construction PMI actual 38.4 (cons. 35.3) is described only as "mild-contraction data" against a Composite PMI 49.3.

## 3. Card construction review (Category 4.5)
Level-file facts used: D-1 cash close 10,487.2 (report 10,497.29) · ATR14 cash 122.28 (0.25×ATR = 30.57; 0.3×ATR = 36.7; 3×ATR = 366.8; 3.5×ATR = 428.0) · 5d swing 10,739.6 / 10,380.4 · 25d range 10,739.6 / 10,126.2 (width 613.4).

| Card | Defects |
|---|---|
| Trade 1 | Score −0.21 (and sum of listed contributions is −0.18) is below the 0.25 gate → must be a SUPPRESSED row; report issues it live "per run instruction" while its own §21c shows Fri 10 Jul Trade 1 as SUPPRESSED on the same gate. Entry is a conditional stop-entry at 10,491, not a market entry at the 07:00 UK anchor at the D-1 close. TP1 10,441 is 50 pts = 0.6R (text says +1R); TP2 10,357 = 1.6R (rule 2R); TP3 10,300 is a third-party chart target instead of the session-close/3×ATR runner (cap = 366.8 pts). Stop 10,575 is "above R3 10,571" and not built from tighter-of(swing, S/R)+0.25×ATR. |
| Trade 2 | R = 29 pts = 0.24×ATR14 (< 0.3×ATR14 = 36.7 cash, 40.0 full-day). TP2 10,469 = 1.7R (rule 2R). Labelled "TRANSITION → breakout-side fade" — contradictory: TRANSITION permits breakout side only, a sell-limit at R1 is a RANGE fade; §9 itself says "range protocol". TP3 text "runner exit at pivot P" equals TP1 (P = TP1 = 10,491). Pivot inputs called corroborated although §5 says H/L single-lead. |
| Trade 3A | Labelled 3A (trend) and "TRANSITION breakout-side long" simultaneously; matches neither 3A (57.5% retrace of a ≥2×ATR swing) nor 3C (confirmed close beyond 25-day boundary by ≥0.25×ATR). Entry 10,540 sits 67% up the 25-day range. Entry is "stop-entry on a confirmed daily-close reclaim" — not executable within one session. TP1 10,570 = 0.42R; TP1 text cites a 38.2% level ≈10,520 which is below a long entry of 10,540. Stop 10,468 described as "below Fri low band" but sits above the 10,462.8 low. TP3 text gives two levels (10,712 / 10,678). |

Card Integrity (linter, static mode; copied verbatim, not re-derived):

| card_id | strategy | flags | dud |
|---|---|---|---|
| 2026-07-13_Trade_1 | Trade 1 - Daily Directional (conditional; conviction below gate) | CLEAN | False |
| 2026-07-13_Trade_2 | Trade 2 - Pivot (regime-aware: TRANSITION -> breakout-side fade) | CLEAN | False |
| 2026-07-13_Trade_3A | Trade 3 - Momentum-Pullback (3A): long the reclaim (regime fork = TRANSITION -> breakout-side long) | CLEAN | False |

Per card: 100 / 100 / 100. Report-level Card Integrity = **100** over 3 non-suppressed cards (0 DUD, 0 WARN). The linter has no market data, so the R-vs-ATR and gate findings above are Category 4 findings, not Card Integrity deductions.

## 4. Total
| Cat | Level | Multiplier | Max | Points | Justification |
|---|---|---|---|---|---|
| 1 | 2 | 0.40 | 20 | 8.00 | Variables mostly respected, but anchor and source-tier gaps; restriction breach drops 3→2 |
| 2 | 3 | 0.65 | 20 | 13.00 | Full section skeleton; monthly pivots missing, §6 column set reduced, backtest table short |
| 3 | 2 | 0.40 | 25 | 10.00 | Wed 8 Jul close off by 222 pts, Mon and Thu closes off by > 15; RSI2 fails on 3 of 4 values; no ATR; USDX wrong; weekly H/L inputs wrong |
| 4 | 3 | 0.65 | 20 | 13.00 | Reasoning structure sound, but card construction fails several fixed M5 rules |
| 5 | 3 | 0.65 | 15 | 9.75 | Good red-flag and caveat discipline; module codes and reconstructed prices breach restrictions |
| | | | 100 | **53.75 → 54** | **Low (40–59)**; override restriction_breach (cap Moderate not binding) |
