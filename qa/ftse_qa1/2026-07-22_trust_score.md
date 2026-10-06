# Trust Score QA — FTSE 100 Daily Report, 22 July 2026 (run ftse_qa1)

Report: `reports/md/FTSE_EuroStoxx_Report_22Jul2026.md` · D = 2026-07-22 · D-1 = 2026-07-21
Level file check: `last_bar_date` = 2026-07-21 < D (leak-free, confirmed). Basis used: `_cash` (the report claims the cash index, LSE 08:00–16:30 London). CFD tolerance per brief §4: closes ≤ 5 pts, open/high/low ≤ 10 pts.

## Result lines
```
c1=3
c2=4
c3=2
c4=3
c5=3
total=63
band=Moderate
override=restriction_breach
card_integrity=96.7
n_cards=3
n_duds=0
n_warns=1
```

## 1. Section 7 checklist (every row)

| Row | Reviewer notes | Evidence (location) | Score |
|---|---|---|---|
| 1.1 Variables respected | Asset FTSE 100 cash, Euro Stoxx 50 reference only, no futures; counters USDX / S&P 500 / DAX 40 / STOXX stated; as-of London close 21 Jul; 5-session lookback; GBP points; Trade 1 anchor 07:00 UK. Gaps: the six sources in §4 are all aggregators/media (Alliance, MarketScreener, Investing, Trading Economics, Sharecast, Yahoo); none from index provider / exchange / sell-side tiers (§13b admits "0 institutional"); Trade 2 and Trade 3C state no anchor time. | §2, §4, §13b, §21b | 3 |
| 1.2 Coverage & currency consistent | All data dated 21 Jul or earlier, session 22 Jul; GBP/EUR labelled; no unit drift. | §2, §6, §13, §21 | 4 |
| 1.3 Audience & tone | Professional strategist tone; trading-and-risk-review use. Internal process language leaks ("per the run instruction", "Per M5 rules") — scored under 5.4. | §1, §18, §19, §20 | 4 |
| 2.1 Sections present & ordered | §1–§21 all present in order; §13a–d and §21a–d present. Weaknesses: §21c grid is incomplete (see 3.4); §7 holds chart headings only (pandoc drops images — accepted as placeholders; noted). | headings | 4 |
| 2.2 Scorecard as table | §6 is a table (Outcome column serves as Final/Validation). RSI2 is "—" for 15 and 16 Jul (the slice supports 70.25 / 83.40 on cash closes). §11 daily/weekly/monthly tables present, ordered R5→S5 (covers R3→S3). | §6, §11 | 4 |
| 2.3 Method steps visible | §4 evidence → §5 consensus → §8 candle-by-candle + sequence → §9 regime (overlap 0.60, persistence 0.48, VOLator, KER) all visible. §4 has no rows for 15/16 Jul closes or the 20 Jul Alliance leg that §6 cites as Src B. | §4–§9 | 4 |
| 3.1 Quantitative claims sourced | Gold ~$4,060, Brent ~$85 / +2.5%, UK 10y gilt ~5.03%, BoE 3.75%, energy ~12% weight, ~80% overseas revenue, sterling 1.3375–1.3418, S&P ~7,566, DAX ~25,000 and USDX ~100.9 carry no source and no pointer to §4/§6/§13. Brent is absent from §13a. | §1, §10, §12, §14 | 2 |
| 3.2 Citations exist & contain data | Spot-checks (cannot fetch): (a) Alliance News 21 Jul, 10,585.91, +61.15 — consistent (10,585.91 − 10,524.76 = 61.15). (b) Reuters 21 Jul, headline "easing oil prices lift sentiment" — contradicts the report's own "Brent +2.5% after fresh US strikes" narrative used in §1, §12, §14. (c) nakitte, dated 20 Jul in §13a, "climbs to 10,600.37" — that figure is the 17 Jul close (§6 uses nakitte as the 17 Jul Src B) and the report has 20 Jul falling to 10,524.76; plausible only as a weekend recap, so treated as a date/figure inconsistency, not as proven fabrication. Sunday Guardian dated Tuesday 21 Jul is a weekly title (low weight). Calendar claims fail against the slice (see 3.4). Override not triggered; row scored down. | §4, §13a, §6 | 2 |
| 3.3 Calculations transparent | RSI2 reproduces exactly from the report's own closes (10,600.37→100.0, 10,524.76→27.1, 10,585.91→44.7; STOXX 47.6/64.4/100.0 also reproduce). Daily and weekly pivots reproduce arithmetically from their stated H/L/C. Sentiment tilt +0.44 reproduces (1.5 / 3.4). Gaps: ATR(14) is never stated — it is only implicit in the cards (3.5×ATR = 308 and 3×ATR = 264 give ATR = 88.0); weekly and monthly H/L/C inputs not shown; §21a lists only 3 signals (+0.07, +0.045, +0.05 = +0.165) yet reports +0.14, the technical signal (weight 0.25) is called "highest-weighted" but the signal set does not sum to the stated score and 2 of 6 signals are not shown. | §6, §9, §11, §13b, §21a | 3 |
| 3.4 Numbers reconcile | D-1 close 10,585.91 is identical in §1, §3, §4, §6, §21b and Trade 2 uses §11 P/R1/S1 consistently. Breaks: (i) STOXX "+0.94%" (§3, §10, §6) vs its own table 6,266.40→6,289.00 = +0.36%; (ii) §21d "Trade 2 triggered 4/5" vs §21c 3/5 YES; "TP1 hit rate ≈ 60%" vs two labelled TP1 hits (16, 17 Jul) = 40%; (iii) §21c is missing Trade 3C rows for 17, 20, 21 Jul (12 rows, 15 expected) and the R scale is inconsistent (+0.8R = 56 pts, +1.0R = 71 pts, +0.5R = 62 pts, −1.0R = 47.6 pts) and 16 Jul "TP1 hit" is booked at +0.8R; (iv) Trade 1 TP3 cap 10,849.9 sits below TP2 10,857.8; (v) §1 says medium-term "Ranging–Neutral", §9/§20 resolve to TRANSITION; (vi) §8 "−0.5%" on 20 Jul vs the report's own 10,600.37→10,524.76 = −0.71%. **Slice accuracy (Category 3 main test), cash basis:** D-1 O 10,524.25 vs 10,479.3 (+45.0); H 10,589.00 vs 10,574.2 (+14.8); L 10,483.14 vs 10,470.1 (+13.0); C 10,585.91 vs 10,571.7 (+14.2, ≈ the 15-pt failure line). Prior closes: 15 Jul +17.2, 16 Jul +31.8, 17 Jul +27.0 (all > 15 pts), 20 Jul −9.9. Only 4 of 15 O/H/L cells and 0 of 5 closes are inside tolerance. RSI2 D-1 44.7 vs 48.88 (−4.2), 20 Jul 27.1 vs 46.03 (−18.9). Pivots: daily +11.5 to +16.8 pts on every level; weekly P +27.7, S1 +47.8, S2 +68.7, S3 +88.8 (report range 163.7 vs slice 204.7); monthly P +109.5, S1 +80.8, S2 +155.1, S3 +126.4 (range 437.0 vs 482.6). ATR implied 88.0 vs 119.56 cash / 140.45 full (−26% / −37%). 5-day swing low 10,471.97 vs 10,429.4 (+42.6). 25-day range 10,310/10,747 vs 10,328.1/10,739.6. Counters: USDX said "falling ~100.9", slice closes 100.49→101.20 rising, ends 101.20; S&P 500 said "rising ~7,566", slice closes 7,572.8→7,503.7 falling over the 5 sessions, ends 7,503.7. Calendar: China Q2 GDP in the slice is 15 Jul, actual 4.3 vs consensus 4.2 (beat), report says 16 Jul, 4.3 vs 4.5 (miss) and uses it as the miner-selloff driver; "UK GDP (May) 16 Jul +0.1% m/m" has no row in the calendar (only NIESR 0.4 vs 0.6); UK labour data released 21 Jul 07:00 London (unemployment 4.9 vs 4.6 cons, employment change 147k vs 38k, total pay 4.3 vs 4.6) is absent from §13c. | whole report | 1 |
| 4.1 Pillars conclude | §8 "Range", §9 "Neutral, marginal upside", §10 "CONFIRM-leaning-MIXED" end in direction labels. §12 and §14 have per-bullet tags but no closing direction label; §14 ends on a watch item. | §8–§14 | 3 |
| 4.2 Cross-asset interpreted | §10 and §12 give mechanisms (USD→GBP→translation, S&P beta, oil→Shell/BP weight). But the confirmations rest on counter directions the slice contradicts (USDX rising, S&P 500 down over 5 sessions), so the "Confirms" verdicts and the +0.3 cross-asset input in §21a are not supported. | §10, §12, §21a | 3 |
| 4.3 Synthesis reconciles tensions | §9 reconciles KER Range vs VOLator expansion into TRANSITION; §21a flags the §17 vs score conflict; §15/§16/§18 centre on CPI. Residual: §1 vs §9 regime wording; "High confidence" in §18 despite the close sitting 14 pts off the slice and aggregator-only sourcing. | §1, §9, §15–§18, §21a | 4 |
| 4.4 Calibrated language | §17 is exactly one sentence, single conditional, no hedge stacking; confidence stated in §3 (High). | §3, §17 | 4 |
| 4.5 Card construction (protocol, Category 4) | Trade 1 live although score +0.14 < 0.25 (should be a SUPPRESSED row); stop not the tighter of swing/nearest S/R and no wide-stop flag; runner cap below TP2. Trade 2 built although every daily pivot tier is declared single-source-indicative (suppression rule); entry labelled STOP but sits below the D-1 close; R = 36 is ≈ 0.30×ATR on slice ATR. Trade 3C live although "not yet eligible"; R, TP1 vs ATR band; BE rule deviates from entry ±0.2R; no anchor time on Trades 2 and 3C. Detail in feedback. | §21b | 2 |
| 5.1 Data dated; staleness flagged | Every price and article dated; single-source asterisks present on O/H/L. Brent, gold, gilt, BoE and FX figures undated. | §4, §6, §13, §19 | 4 |
| 5.2 Assumptions up front | Anchor override (07:00 UK) and lenient-corroboration/override assumptions are in §19/§20/§21a, not at the opening; anchor time absent on Trades 2/3C; single-source propagation to Trade 2 caveats is present. | §1, §19–§21b | 3 |
| 5.3 Red flags surfaced | CPI collision carried into all three card caveats; Iran/China/sterling risks in §15; wide stop flagged on 3C. | §12, §15, §21b | 4 |
| 5.4 Restrictions honoured | Breach: module code "M5" appears in the body ("Per M5 rules Trade 1 would suppress", §20); internal variable names leak (`DAILY_OPEN_ANCHOR`, `regime_label`, `swing_low_25d / swing_high_25d`) and "run instruction" language appears in §19, §20, §21a. The report states it applied corroboration "leniently" and produced strategies "rather than suppressed" (§19) against fixed suppression rules. "No value interpolated" (§20) sits next to a Trading Economics range 10,524–10,543 "normalised" to 10,524.76 (§4). CFD prints were kept out of the core (OK) and futures not used (OK). | §4, §19, §20, §21b | 1 |

## 2. Category roll-up

| Cat | Max | Rows (mean) | Level | Multiplier | Points | Justification |
|---|---|---|---|---|---|---|
| 1 Prompt adherence | 20 | 3, 4, 4 → 3.67 → 4; **override: −1 level** | **3** | 0.65 | 13.00 | Variables mostly respected, but no index-provider/exchange/sell-side sources and a restriction breach (module code "M5" in the body) drops the level one step. |
| 2 Structural alignment | 20 | 4, 4, 4 → 4.00 | **4** | 0.85 | 17.00 | All sections present and ordered, tables correct; chart sections are headings only, §21c incomplete, RSI2 blank for two rows. |
| 3 Accuracy & evidence | 25 | 2, 2, 3, 1 → 2.00 | **2** | 0.40 | 10.00 | Closes 14–32 pts off the slice on four of five sessions, weekly and monthly pivots off by 28–155 pts, ATR 26% low, two counters directionally wrong, calendar claims not in the slice; arithmetic of RSI2 and pivots is internally sound. |
| 4 Reasoning & judgment | 20 | 3, 3, 4, 4, 2 → 3.20 | **3** | 0.65 | 13.00 | Regime logic and synthesis are coherent, but the cross-asset read rests on wrong directions and card construction has several rule violations. |
| 5 Currency, restrictions & transparency | 15 | 4, 3, 4, 1 → 3.00 | **3** | 0.65 | 9.75 | Data dated and flags present; restrictions breached (module code, variable names, lenient-corroboration/suppression overrides). |

## 3. Total, band, override check
- Total = 13.00 + 17.00 + 10.00 + 13.00 + 9.75 = 62.75 → **63**
- Band: **Moderate (60–74)**
- Override check: `restriction_breach` applies (module code "M5" in §20 body text; internal variable names; fixed M5 suppression rules overridden by "run instruction"). Cap at Moderate (63 is inside the cap) and C1 reduced one level (4 → 3), as applied above. `hallucinated_source` not triggered: the nakitte (20 Jul / 10,600.37) and Reuters ("easing oil prices") items are inconsistent but not shown to be impossible; they are scored in row 3.2.

## 4. Card Integrity (linter rows, copied verbatim from `qa/ftse_qa1/lint_static/2026-07-22.csv`; not re-derived)

| card_id | report_date | strategy | flags | dud | per-card score |
|---|---|---|---|---|---|
| 2026-07-22_Trade_1 | 2026-07-22 | Trade 1 — Daily Directional (LONG, low-conviction override) | WARN_TP3_ORDER | False | 90 |
| 2026-07-22_Trade_2 | 2026-07-22 | Trade 2 — Pivot, TRANSITION (breakout side only — upside) | CLEAN | False | 100 |
| 2026-07-22_Trade_3C | 2026-07-22 | Trade 3C — Momentum-Breakout (TRANSITION variant, upside) | CLEAN | False | 100 |

Report-level Card Integrity = mean(90, 100, 100) = **96.7** · n_cards = 3 · n_duds = 0 · n_warns = 1. (Separate from the 100. The construction issues scored in row 4.5 are hand observations and are not folded into this number.)
