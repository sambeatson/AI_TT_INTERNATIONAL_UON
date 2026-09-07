# Trust Score — 2026-06-24 — SP500_Report_24Jun2026.md

## 1. Section 7 checklist

| Item | Reviewer notes | Evidence observed | Score 0–5 | Action required |
|---|---|---|---|---|
| 1.1 Variables respected | Asset is the S&P 500 cash index (not ES) and counters are USDX·VIX·DAX 40 with USDX first; lookback is 5 sessions; unit is index points/USD. But the Trade 1 daily-open anchor is NOT the 07:00 UK anchor — it is overridden to a "24 Jun cash open proxy" that is simply the last close (card JSON records "MARKET @ cash open 14:30 UK", anchor_broker 16:30). §4 lists six rows but only five distinct providers (CNBC twice), and the tier mix is one index-provider (FRED/S&P DJI) with no exchange or sell-side tier. As-of field reads "24 June 2026 (run/issue date)" rather than the NY close of D-1 (deviation is explained in the note). Tick 0.01 never stated. | §2 (asset, as-of, lookback), §4 (source rows), §10 (counter order), §20 (override log), §21b Trade 1 Entry | 2 | Restore the 07:00 UK anchor or record a SUPPRESSED/deviation row; reach ≥6 distinct providers across the required tiers; set the as-of field to the D-1 NY close. |
| 1.2 Coverage & currency consistent | All data dates are D-1 or earlier and 24 Jun is treated as the forward session; no currency/unit drift. Two consistency failures: (a) the 19 Jun report carries 16 Jun close 7,411 and 18 Jun O/H/L 7,487.36 / 7,511.07 / 7,468.32 marked "CORROBORATED (Δ 0.00)", which this report contradicts with 7,511.35 and 7,430 / 7,506 / 7,421; (b) §21c labels 19 Jun as t−5 although it falls chronologically between t−2 (18 Jun) and t−1 (22 Jun), so the backtest window is mis-indexed. 19 Jun exclusion as Juneteenth is itself documented and defensible. | §2, §6, §21c; reports/md/SP500_Report_19Jun2026.md §6 | 2 | Reconcile the 16 Jun close and 18 Jun O/H/L against the earlier corroborated row; re-index the backtest so t−5 is 15 Jun and the holiday consumes no slot. |
| 1.3 Audience & tone | Consistently senior-strategist register: regime language, invalidation levels, risk framing; no retail tone, no promotional language, no "you should buy" phrasing. | §1, §18, §21d limitations boilerplate | 5 | None. |
| 2.1 Sections present & ordered | §1–§21 all present in the prescribed order, including §13a/b/c/d and §21a/b/c/d, §17 as a single sentence and §19/§20 in place. | Headings throughout | 5 | None. |
| 2.2 Scorecard as a table | §6 carries every required column (Date/O/H/L/C/RSI2/Trend/Src A/Src B/Validation). §11 is malformed against the 3-levels-per-side spec: the daily table publishes R5–S5 (five tiers per side) and the monthly table stops at R2/S2 with no R3/S3. Weekly is correct (R3→P→S3). | §6, §11 | 3 | Publish exactly R3→P→S3 for each of daily/weekly/monthly, or justify extra tiers; add monthly R3/S3. |
| 2.3 Method steps visible | §4 observations → §5 classification/normalisation → consensus is explicit; §8 is candle-by-candle with a stated sequence assessment; §9 states regime, persistence, overlap and VOLator. §7 has no image and no caption/placeholder — only a narrative statement that chart readings are folded into §8–§11. | §4–§9 | 4 | Add a chart caption/placeholder block in §7 so the chart toggles are evidenced. |
| 3.1 Quantitative claims sourced | §1 numbers trace to §4/§6. §12 and §14 carry many unsourced figures: Micron −11%, TSMC −5%, SMH −6.5%, ~68% September-hike odds (from ~29%), PCE projection 3.6%, "9 of 18 members", "~60% of constituents higher", Russell 2000 outperformance. §9/§10 VIX and DAX levels carry no source and the VIX figures do not match the slice. | §12, §14, §9, §10 | 2 | Attach a dated source to every figure in §12/§14 or route it through §4/§6/§13. |
| 3.2 Citations exist & contain data | Three spot-checks are internally consistent: CNBC 23 Jun 7,365.46 "−1.44%" reproduces exactly from 7,472.79 → 7,365.46 (−1.436%); FRED/S&P DJI 22 Jun 7,472.79 matches §6 and the −0.37% quoted in §8 (7,472.79/7,500.58 = −0.371%); IG Markets 23 Jun H 7,478.45 / L 7,349.31 is the exact input that reproduces every §11 daily level. No source is self-contradictory or impossible → no fabrication finding. Weakness: CNBC is counted twice to reach the "six sources cleared the minimum" claim. | §4, §13a, §20 validation log | 3 | Replace the duplicated provider with a distinct index-provider/exchange/sell-side source. |
| 3.3 Calculations transparent | RSI2 reproduces exactly from the report's own close sequence for the three testable rows (helper: 46.9 / 74.3 / 0.0 vs stated 46.9 / 74.3 / ~0.0). But 17 Jun RSI2 = 41.8 is not reproducible: §8 states 16 Jun closed after a 0.57% slide, so both the 16 Jun and 17 Jun periods are losses and RSI2 must be 0.0. The 17 Jun Trend label "Neutral" also violates the stated rule (Close 7,420.10 < Open 7,508 and RSI2 41.8 < 50 → Bearish). All eleven §11 daily levels reproduce exactly from the report's own 23 Jun H/L/C (P 7,397.74; R1 7,446.17; S1 7,317.03; R2 7,526.88; S2 7,268.60; R3 7,575.31; S3 7,187.89). ATR(14) is never stated as a number — it is only implied as 96.0 by the stop (R1 + 24.00 = 0.25×ATR) and the 3×ATR cap (7,365.46 − 288 = 7,077.46). KER ≈ −0.45 is stated. §21a score −0.77 does not reconcile: the listed contributors (−0.25, −0.20, −0.15, −0.05, −0.07) sum to −0.72 and the sixth 0.10-weight term is never named. | §6, §8, §9, §11, §21a, §21b | 2 | State ATR14 numerically; correct the 17 Jun RSI2/Trend; list all six weighted contributors so −0.77 reconciles. |
| 3.4 Numbers reconcile | Cross-section: D-1 close 7,365.46 is identical in §1/§3/§4/§6/§21b, and card pivots equal §11 pivots. Failures: card JSON Trade 1 entry is 7,365.17, not the 7,365.46 D-1 close required of a MARKET entry; §21d hit-rates contradict §21c (Trade 1 "TP1 100%" against a +0.3R row, "TP2 50%" against 1 of 4 rows = 25%; Trade 2 "triggered 3/4" against two triggered rows and no 16 Jun row, though its +1.15 mean is computed on the two). Against the slice, one close is out by more than 10 pts (16 Jun, Δ −11.55) and eleven of fifteen O/H/L fields breach the 8-pt tolerance, including 23 Jun Open Δ +91.6 and 18 Jun Open Δ −84.1. Weekly pivots are labelled 15–19 Jun but their implied H 7,558.99 excludes Mon 15 Jun (slice high 7,583.40). | §6, §11, §21b, §21c/d, cards/baseline/by_date/2026-06-24.json, slice | 1 | Rebuild §6 O/H/L on the corroborated basis; align card entry to the D-1 close; recompute §21d from the §21c rows; rebuild weekly pivots on the full week. |
| 4.1 Pillars conclude | §8 ends "Bearish continuation", §9 "Bias: Bearish", §10 "cross_asset_confirm = CONFIRM", §12 items each carry a price-direction label, §14 ends "equity-negative". But the regime label drifts across the report: §1 "Transitional-to-Bearish", §9 "Transitional-to-Trending Down", §20 "regime_label = TREND_DOWN" — and Trade 2 is titled "trend-follow short below pivot" while its entry sits above P. | §1, §8, §9, §10, §12, §14, §20, §21b | 3 | Use one regime label consistently and make the card titles match the entry geometry. |
| 4.2 Peer/cross-asset interpreted | §10 supplies real mechanisms (USDX → EPS translation and global tightening; VIX → hedging demand/risk-regime; DAX → common global factor) with status and implication, not a correlation list, and the aggregate CONFIRM is reasoned. The evidentiary base is weak: VIX is stated as 16.4 on 16 Jun (slice cash close 17.73), ~17.3 on 22 Jun (17.91), and "toward the low-20s intraday" on 23 Jun (slice high 19.18). USDX ~101.4 matches the slice (101.414). | §10, §9 VOLator paragraph | 3 | Restate the VIX prints from the validated series; drop or evidence "low-20s". |
| 4.3 Synthesis reconciles tensions | §15/§16/§18 do address the two-way PCE risk, the breadth-vs-cap-weight split and a named invalidation (weekly P 7,487), and §17 does not contradict §21a. Card construction, scored here per the brief, fails in three places: Trade 2 is built as a RANGE rally-sell (limit band 7,398–7,415, stop above weekly P) although the declared regime is TREND_DOWN, whose fork requires entry at P − 0.10×(P−S1) = 7,389.66 with stop P + 0.8×(R1−P) = 7,436.48 and TPs at S1/S1.5/S2; Trade 3A enters at the 38.2% retrace (7,453) instead of the mandated 57.5% (7,505.47 on its own swing) and its qualifying swing spans 2 Jun → 23 Jun ≈ 15 sessions, outside the 4–10 session window; Trade 1's confluence note places TP1 7,260.75 "near daily S5" when S5 is 6,929.61 and TP1 lies between S2 7,268.60 and S3 7,187.89. Trade 3A also carries no BE rule (be_rule NONE) although every card requires U3 → entry ± 0.2R on U2 fill. | §15–§18, §21a, §21b all three cards, cards JSON | 2 | Rebuild Trade 2 on the TREND fork, Trade 3A on a 4–10 session swing with a 57.5% entry and the 38.2%/0%/extension TP ladder, add the BE rule, and fix the Trade 1 confluence claim. |
| 4.4 Calibrated language | §17 is exactly one sentence with a single named risk and no hedge stacking. Confidence is explicit in §3 (High) and split appropriately in §18 (High on level, Medium on path). §21d carries the small-sample limitations boilerplate. | §3, §17, §18, §21d | 5 | None. |
| 5.1 Data dated; staleness flagged | Every §6 row, §4 quote and §13a article is dated; single-source/provider-estimated O/H/L are asterisked in §6 and explained in §19; 19 Jun is declared a verified holiday rather than a gap. Counter levels in §9/§10 (VIX, USDX, DAX) are given without dates or timestamps. | §4, §6, §13a, §19 | 4 | Date the counter prints in §9/§10. |
| 5.2 Assumptions up front | The anchor-override caveat appears both on the Trade 1 card and in §20, and the single-source-indicative pivot propagation is carried into the Trade 2 and 3A caveats. The volatility assumption is not declared: the stop buffer and the runner cap both imply ATR14 = 96.0, a number that appears nowhere in the report. | §19, §20, §21b caveats | 4 | Publish ATR14 in §9 and reference it on every card. |
| 5.3 Red flags surfaced | §12 and §15 lay out the downside risks (hot PCE, semi de-rating breadth, dollar drag) and §13d flags the core PCE collision, which is carried into the Trade 1 and Trade 3A caveats. Trade 2's caveats omit the same event collision even though its holding window is identical. | §12, §15, §13d, §21b | 4 | Carry the §13d event collision into the Trade 2 caveat line. |
| 5.4 Restrictions honoured | RESTRICTION BREACH. §20 prints a bracketed variable name — "Override applied: [DAILY_OPEN_ANCHOR] overridden per instruction" — and a module code — "a deliberate deviation from the M1 baseline" — plus an internal process reference ("Step 4 bearish synthesis"). §5.4 forbids bracketed variable names and module codes (M1..M5) in the deliverable. On the positive side, CFD/aggregator quotes are explicitly excluded from the OHLC basis and used for direction only, instrument common names are used, and no framework name appears. | §20, §5 | 1 | Remove the bracketed variable name, the M1 reference and the step reference; describe the override in plain language. |

## 2. Category roll-up

| Category | Level | Multiplier | Points | Justification |
|---|---|---|---|---|
| C1 Prompt adherence (max 20) | 2 | 0.40 | 8.00 | Rows 1.1/1.2/1.3 = 2/2/5 → mean 3.0 → level 3; the §20 restriction breach drops C1 one level to 2 per the override rule. Anchor variable overridden, source minimum met only by duplicating a provider, and the 16/18 Jun figures contradict the earlier report. |
| C2 Structure (max 20) | 4 | 0.85 | 17.00 | Rows 2.1/2.2/2.3 = 5/3/4 → mean 4.0. All sections present and correctly ordered; §11 pivot tiering is malformed (daily R5–S5, monthly missing R3/S3) and §7 has no chart caption/placeholder. |
| C3 Accuracy & evidence (max 25) | 2 | 0.40 | 10.00 | Rows 3.1/3.2/3.3/3.4 = 2/3/2/1 → mean 2.0. Pivots and three of five RSI2 values reproduce from the report's own inputs, but one close is out by 11.55 pts, eleven O/H/L fields breach tolerance, 17 Jun RSI2/Trend is unreproducible, ATR is unstated and §21a does not reconcile. No fabricated source found. |
| C4 Reasoning & judgment (max 20) | 3 | 0.65 | 13.00 | Rows 4.1/4.2/4.3/4.4 = 3/3/2/5 → mean 3.25 → level 3. Pillars conclude and the forecast is calibrated, but the regime label drifts, the cross-asset mechanism rests on misstated VIX prints, and all three cards deviate from the M5 construction rules. |
| C5 Currency, restrictions & transparency (max 15) | 3 | 0.65 | 9.75 | Rows 5.1/5.2/5.3/5.4 = 4/4/4/1 → mean 3.25 → level 3. Dating and indicative flagging are strong and the override is disclosed, but §20 breaches the no-bracketed-variable / no-module-code restriction. |
| **Total** | — | — | **57.75 → 58** | Sum of category points, rounded to a whole number. |

## 3. Total, band, override check

- Raw total: 8.00 + 17.00 + 10.00 + 13.00 + 9.75 = **57.75 → 58**.
- Band for 58: **Low** (40–59).
- Fabricated-source override: **not triggered**. Three cited sources were spot-checked (CNBC 23 Jun −1.44%, FRED/S&P DJI 22 Jun 7,472.79 with §8's −0.37%, IG Markets 23 Jun H/L feeding §11) and each is internally consistent, correctly dated and used consistently elsewhere in the report. C3 therefore stands at level 2 rather than 0.
- Restriction override: **triggered**. §20 contains the bracketed variable name `[DAILY_OPEN_ANCHOR]` and the module code `M1`, both forbidden by §5.4. Effect: C1 dropped one level (3 → 2, already applied above) and the total capped at 74. The computed total of 58 sits below the cap, so the cap is not binding; the recorded override is `restriction_breach`.
- Final: **58 / Low / restriction_breach**.

## 4. Card Integrity

Linter rows for 2026-06-24, verbatim:

| card_id | report_date | strategy | flags | dud |
|---|---|---|---|---|
| 2026-06-24_Trade_1 | 2026-06-24 | Trade 1 - Daily Directional | CLEAN | False |
| 2026-06-24_Trade_2 | 2026-06-24 | Trade 2 - Pivot (sell limit daily P shelf) | CLEAN | False |
| 2026-06-24_Trade_3A | 2026-06-24 | Trade 3A - Momentum-Pullback (38.2% rally-sell) | CLEAN | False |

Per-card integrity (100 − 40×#DUD − 10×#WARN, floored at 0):

| Card | #DUD | #WARN | Integrity |
|---|---|---|---|
| 2026-06-24_Trade_1 | 0 | 0 | 100 |
| 2026-06-24_Trade_2 | 0 | 0 | 100 |
| 2026-06-24_Trade_3A | 0 | 0 | 100 |

Report mean over non-suppressed cards (3 of 3): **100.0**. No card is suppressed; the direction score |−0.77| ≥ 0.25, so Trade 1 is correctly not suppressed.

Note: the static linter is clean — stops sit on the correct side, TP ladders are monotonic, both LIMIT levels sit above the D-1 close for shorts, and every R sits inside the 0.3–3.0×ATR14 band (Trade 1 R 105 = 0.90×ATR14, Trade 2 R 85 = 0.73×, Trade 3A R 92 = 0.79×, on the slice ATR14 of 116.28). The M5 construction defects assessed in row 4.3 are not visible to the static checks and do not change this number.

## 5. Data reconciliation log

Slice basis: `data/slices/US500/US500_upto_2026-06-23.csv`, cash session 16:30–23:00 broker. Tolerance: |Δ| ≤ 3 pts on a close, ≤ 8 pts on an open/high/low.

| Section | Report value | Slice value | Delta | Verdict |
|---|---|---|---|---|
| §6 16 Jun Open | 7,541 | 7,562.90 | −21.90 | FAIL (>8) |
| §6 16 Jun High | 7,556 | 7,571.40 | −15.40 | FAIL (>8) |
| §6 16 Jun Low | 7,503 | 7,518.20 | −15.20 | FAIL (>8) |
| §6 16 Jun Close | 7,511.35 | 7,522.90 | −11.55 | FAIL (>10 — Category 3 failure) |
| §6 17 Jun Open | 7,508 | 7,531.70 | −23.70 | FAIL (>8) |
| §6 17 Jun High | 7,559 | 7,540.00 | +19.00 | FAIL (>8) |
| §6 17 Jun Low | 7,402 | 7,408.50 | −6.50 | OK |
| §6 17 Jun Close | 7,420.10 | 7,427.50 | −7.40 | FAIL (>3) |
| §6 18 Jun Open | 7,430 | 7,514.10 | −84.10 | FAIL (>8) |
| §6 18 Jun High | 7,506 | 7,518.30 | −12.30 | FAIL (>8) |
| §6 18 Jun Low | 7,421 | 7,472.60 | −51.60 | FAIL (>8) |
| §6 18 Jun Close | 7,500.58 | 7,502.30 | −1.72 | OK |
| §6 22 Jun Open | 7,500.6 | 7,513.10 | −12.50 | FAIL (>8) |
| §6 22 Jun High | 7,530 | 7,538.80 | −8.80 | FAIL (>8) |
| §6 22 Jun Low | 7,460 | 7,467.30 | −7.30 | OK |
| §6 22 Jun Close | 7,472.79 | 7,479.30 | −6.51 | FAIL (>3) |
| §6 23 Jun Open | 7,462 | 7,370.40 | +91.60 | FAIL (>8, largest single error) |
| §6 23 Jun High | 7,478.45 | 7,431.80 | +46.65 | FAIL (>8) |
| §6 23 Jun Low | 7,349.31 | 7,356.20 | −6.89 | OK |
| §6 23 Jun Close | 7,365.46 | 7,374.40 | −8.94 | FAIL (>3) |
| §6 RSI2 16 Jun | 29.8 | 76.45 (slice closes) | −46.65 | Discrepancy; not testable from the report's own closes (needs pre-window closes) |
| §6 RSI2 17 Jun | 41.8 | 0.00 (slice closes) | +41.80 | FAIL — also unreproducible from the report's own data: §8 states 16 Jun fell 0.57%, so two consecutive losses force RSI2 = 0.0 |
| §6 RSI2 18 Jun | 46.9 | 46.9 (helper, report's own closes) | 0.00 | PASS — arithmetic exact |
| §6 RSI2 22 Jun | 74.3 | 74.3 (helper, report's own closes) | 0.00 | PASS — arithmetic exact |
| §6 RSI2 23 Jun | ~0.0 | 0.0 (helper, report's own closes) | 0.00 | PASS — arithmetic exact |
| §6 Trend 17 Jun | Neutral | Rule → Bearish (C 7,420.10 < O 7,508; RSI2 < 50) | — | FAIL — label violates the stated trend rule |
| §11 daily P/R1/S1/R2/S2/R3/S3 from report's own 23 Jun H/L/C | 7,397.74 / 7,446.17 / 7,317.03 / 7,526.88 / 7,268.60 / 7,575.31 / 7,187.89 | Recomputation from H 7,478.45 L 7,349.31 C 7,365.46 gives the same seven values (R4/R5/S4/S5 also extend correctly by H−L) | 0.00 | PASS — reproduces exactly from its own inputs |
| §11 daily P vs slice | 7,397.74 | 7,387.47 | +10.27 | Discrepancy (inherited from the §6 23 Jun H/L/C errors) |
| §11 daily R1 vs slice | 7,446.17 | 7,418.73 | +27.44 | Discrepancy |
| §11 daily S1 vs slice | 7,317.03 | 7,343.13 | −26.10 | Discrepancy |
| §11 weekly P | 7,487.19 | 7,495.37 | −8.18 | Discrepancy |
| §11 weekly implied High (from R1/S1 algebra) | 7,558.99 | 7,583.40 (week 15–19 Jun) | −24.41 | FAIL — the table is labelled 15–19 Jun but excludes Mon 15 Jun |
| §11 monthly implied May High | 7,600.00 | 7,601.80 | −1.80 | OK |
| §11 monthly implied May Low | 7,237.85 | 7,177.50 | +60.35 | FAIL (flagged single-source-indicative, but still out) |
| §11 monthly implied May Close | 7,560.00 | 7,584.80 | −24.80 | FAIL |
| §11 monthly P | 7,465.95 | 7,454.70 | +11.25 | Discrepancy |
| §1/§9 record high 2 Jun | 7,620.90 | 7,624.60 (2026-06-02 cash high) | −3.70 | OK |
| §21b implied ATR14 (stop buffer 24.00 = 0.25×ATR; runner cap 7,077.46 = entry − 3×ATR) | 96.00 | 116.28 (cash) / 129.63 (full-day) | −20.28 | FAIL — and the value is never stated in the report |
| §9 VIX 16 Jun | 16.4 | 17.73 | −1.33 | Discrepancy |
| §9 VIX 22 Jun | ~17.3 | 17.91 | −0.61 | Discrepancy |
| §9/§10 VIX 23 Jun "low-20s intraday" | low-20s | 19.18 session high | ≈ −1 to −2 | FAIL — overstated |
| §10/§12 USDX 23 Jun | ~101.4 | 101.414 | +0.01 | PASS |
| §10 DAX 40 ~25,140 | ~25,140 | no slice available | — | Not verifiable from permitted inputs |
| Card JSON Trade 1 entry vs D-1 close | 7,365.17 | Report D-1 close 7,365.46 (slice cash close 7,374.40) | −0.29 (−9.23 vs slice) | FAIL — a MARKET entry must equal the D-1 close |
| §13c FOMC 17 Jun hold at 3.50–3.75% | 3.50–3.75% | News slice 2026-06-17 Fed Interest Rate Decision actual 3.750 | 0.00 | PASS |
| §13d 24 Jun New Home Sales impact | Medium | News slice rates New Home Sales HIGH on 2026-06-24 | — | Minor discrepancy in impact grading |
