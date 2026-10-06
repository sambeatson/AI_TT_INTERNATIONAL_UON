# Trust Score v3.7 — FTSE 100 report dated 2026-07-10 (run ftse_qa1)

Report: `reports/md/FTSE_EuroStoxx_Report_10Jul2026.md` · Level file: `data/levels/UK100_by_date/2026-07-10.csv` (last_bar_date 2026-07-09 < D: leak-free confirmed) · Slice stats run with `--cash-open 10:00 --cash-close 18:30` and `--closes` on the report's five closes.

## Machine-readable result
```
c1=3
c2=4
c3=0
c4=3
c5=3
total=53
band=Low
override=hallucinated_source
card_integrity=100
n_cards=3
n_duds=0
n_warns=0
```

## 1. Section 7 checklist

| Row | Reviewer notes | Evidence observed | Score |
|---|---|---|---|
| 1.1 Variables respected | Asset (FTSE 100 cash), counters (USDX, S&P 500, DAX 40, Euro Stoxx 50), 5-session lookback, GBP/points, Europe/London as-of and 07:00 UK anchor are all present. Not respected: (a) the six sources are not drawn from index-provider / exchange / sell-side tiers (Yahoo tier 3, "Sunday Guardian" tier 4, Sharecast relay with no figure; no FTSE Russell or LSE print); (b) ATR(14) replaced by a 5-session mean true range (103.13) and KER(13) by a 5-session figure (disclosed, but M5 sanity check forbids a proxy); (c) anchor called an "override at user instruction" although 07:00 UK is the standing value; Trade 2 and 3A cards state no anchor time at all; (d) charts not produced. | header, §2, §4, §9, §19, §20, §21b | 2 |
| 1.2 Coverage & currency consistent | All data dated D-1 or earlier; session D for cards; GBP for FTSE, EUR for Euro Stoxx, no unit drift. Slip: "approximately the 8 July close" is given as 10,491.98 but §6 gives 10,489.04 (and 10,691.98 is the 7 Jul close). | §2, §6, §16, §21b | 4 |
| 1.3 Audience & tone | Strategist register, trading and risk-review use, no retail tone. | §1, §18 | 4 |
| 2.1 Sections present & ordered | §1–§21 all present in order; §13a–d and §21a–d all present; §17 is one sentence. | headings | 5 |
| 2.2 Scorecard as a table | §6 is a table but columns deviate from the required Date/O/H/L/C/RSI2/Trend/Source A/Source B/Final/Validation (no Trend, no per-source columns, no Final/Validation; adds Chg % and a free-text Corroboration column). §11 pivots are tables ordered R→P→S but run R5..S5 (five each side) instead of R3..S3. | §6, §11 | 3 |
| 2.3 Method steps visible | §4 observations, §5 normalisation and consensus; §8 candle by candle with sequence; §9 regime with VOLator and KER (persistence/overlap not shown explicitly). §7 contains no chart, caption or placeholder per chart, only a prose statement that charts are not embedded. | §4–§9 | 4 |
| 3.1 Quantitative claims sourced | Only 9 Jul has sourced quotes (§4). The OHLC for 3, 6, 7 and 8 Jul, the 25-session low, the weekly and monthly inputs and all Euro Stoxx figures carry no quote or source anywhere. §12/§14 numbers point to §13a only loosely. | §4, §6, §12 | 3 |
| 3.2 Citations exist & contain data | FAIL. Investing.com row (§4) quotes a 9 Jul day range of 10,430.29–10,458.95, so the report's own consensus close 10,429.22 and its "corroborated" Low 10,419.22 both sit outside that source's own range; no §4 source supplies 10,419.22 at all, yet §6/§19 call High and Low "corroborated (2 src)". The "2 source" close corroboration is also not what §4 shows (TE rounded 10,429 and Yahoo 10,429.22 only). A source whose figure contradicts its own quote counts as fabricated (brief §2 row 3.2). Also: the 10,444.18 intraday and 10,435.73 prints are the only other figures; "Sunday Guardian" 14:36 wrap is an unverifiable tier-4 name. | §4, §6, §19, §20 | 0 |
| 3.3 Calculations transparent | RSI2 reproduces exactly from the report's own closes (`--closes`: 59.6 / 16.5 / 0.0). Daily, weekly, monthly pivot arithmetic is internally exact (implied H/L/C reproduce R2, S2, R3, S3). Mean true range 103.13 reproduces from §6 (TR 3 Jul 95.84, 6 Jul 70.00, 7 Jul 55.00, 8 Jul 224.97, 9 Jul 69.82). KER 0.76 reproduces (249.81 / 330.23) but numerator and denominator are not shown. §21a score (−0.505) shows only four of six signal contributions; the sentiment and medium-term terms must be inferred (−0.35 x 0.15 = −0.0525) and the weight of each signal is not tabulated. | §6, §9, §11, §20, §21a | 3 |
| 3.4 Numbers reconcile | Close 10,429.22 is identical in §1, §3, §4, §6, §21b; pivots in §11 match cards; RSI2 consistent in §6/§8/§21a. Breaks: (i) "closed lower for a third consecutive day" (§1) and "three consecutive lower closes" (§8, §15, §18, §21a) contradict §6 (7 Jul closed +0.38%; only 8 and 9 Jul fell consecutively); (ii) §9 says 8 Jul true range was 199 but §6 gives 224.97 (199.08 is the high-low span); (iii) §3 range 10,395–10,465 is said to be bounded by the session low (10,419.22) and "central pivot plus one resistance step" (10,452.37 / 10,475.53): neither bound matches; (iv) §1 names the monthly pivot 10,379.56 as the single most important watch item, §18 names the daily pivot 10,435.80; (v) §16/§21b invalidation 10,491.98 is not the 8 Jul close in §6 (10,489.04); (vi) §21d states Trade 1 "mean −0.14R" but §21c Trade 1 rows sum to +0.3R (mean +0.06R); "won three of five, lost two, losses larger" is also inconsistent; (vii) §21d says Trade 2 "triggered twice ... did not trigger once" but §21c shows one trigger, two non-triggers, two UNRESOLVABLE; "0 of 8 triggered trades" but §21c shows six triggers; (viii) §21c 08 Jul "stopped out" exits at the close price 10,489.04. Data reconciliation against the level file: see section 2, D-1 close and Low fail. | cross-section | 2 |
| 4.1 Pillars conclude | §9 and §13b conclude with labels (Transitional-Mixed, NEGATIVE −0.35). §8, §10, §12 and §14 end on observations or an explicit "unresolved" rather than a direction label. | §8, §10, §12, §14 | 3 |
| 4.2 Peer/cross-asset interpreted | Mechanisms given for USDX (overseas earnings translation), S&P 500, DAX/Euro Stoxx (sector skew, AstraZeneca weight); contradiction handled well. USDX tagged "Firm / Rising" but slice USDX closes 100.82 (3 Jul) to 100.92 (9 Jul) and fell −0.13% on 9 Jul, so "Rising" is thin; no oil counter row although oil drives §12/§14. | §10 | 4 |
| 4.3 Synthesis reconciles tensions | Short vs medium horizon, KER vs regime, cross-asset vs technical and §17 vs §21a are all addressed in §9, §10, §15, §16, §18, §21a. Weakness: the contradiction is left "unresolved", and the §1 / §18 watch-item mismatch above. | §9–§18 | 4 |
| 4.4 Calibrated language | §17 is exactly one sentence; confidence Medium stated in §3 and §18. Several "unambiguous / unambiguously down" phrasings sit against a stated unresolved contradiction. | §1, §3, §17, §18 | 4 |
| 4.5 Card construction (protocol) | All three cards fail M5. Trade 2 is a pivot-fade sell limit under TRANSITION (only a breakout-side entry is permitted). Trade 3 is built as 3A under TRANSITION (fixed mapping is 3C; 3C is not eligible, so a SUPPRESSED row was required, never substitution). Unit 3 stop "entry + 0.2R" sits on the adverse side for a SHORT on all three cards. Trade 3A: entry at 38.2% not 57.5%, stop at the 50% level not beyond the 0% anchor + 0.25 ATR, TPs at 100%/123.6%/161.8% not 38.2%/0%/extension, runner stop pull widens the stop. Trade 1 and 2 buffers, caps and sanity checks use the 103.13 proxy not atr_14. Trade 2 TP3 "daily P" equals its own entry; its stop at R1 carries no 0.25 ATR buffer. | §21b | 1 |
| 5.1 Data dated; staleness flagged | §4 rows dated and timed; single-source 6 and 7 Jul H/L flagged. §13a articles carry no date column; no dates on the 3, 6, 7, 8 Jul quotes. | §4, §6, §13a, §19 | 3 |
| 5.2 Assumptions up front | Single-source propagation and ATR-proxy caveat are on the cards. Anchor treatment is contradictory (07:00 UK described as an override, proxy-open caveat absent from Trade 1/2/3A cards, Trade 2/3A state no entry time). | header, §19, §20, §21b | 3 |
| 5.3 Red flags surfaced | Geopolitical gap risk, AstraZeneca follow-through, RSI2 trap and weak confluences are surfaced in §12, §13d, §15 and carried into card caveats. §13d lists no dated item for D although the calendar slice has scheduled D items (EUR industrial production 09:00 UK, IEA Oil Market Report 09:00 UK, Euro-area CPI/HICP 07:45 UK, Canada employment 13:30 UK); "UK CPI print" and "BoE commentary" are undated. | §12, §13d, §15, §21b | 4 |
| 5.4 Restrictions honoured | No futures or retail CFD quotes in the OHLC basis; no module codes or bracketed variables. Concerns: 6 and 7 Jul H/L are round figures (10,690.00 / 10,620.00 / 10,700.00 / 10,645.00) and single-source (flagged, so not presented as sourced); an ATR proxy was used where M5 says a proxy may not be substituted; process language ("forward-test session 1 of 20", "weights locked", "sentiment-freeze rule") leaks into the body. | whole report | 3 |

## 2. Category 3 data check against the level file (cash basis, tolerance close ±5, O/H/L ±10; fail = close off by more than 15)

| Session | Field | Report | Level file / slice (cash) | Delta | Verdict |
|---|---|---|---|---|---|
| 09 Jul (D-1) | Open | 10,441.09 | 10,439.2 | +1.89 | ok |
| 09 Jul | High | 10,458.95 | 10,468.9 | −9.95 | ok (edge) |
| 09 Jul | Low | 10,419.22 | 10,380.4 | +38.82 | discrepancy |
| 09 Jul | Close | 10,429.22 | 10,457.0 | −27.78 | FAIL (>15) |
| 09 Jul | RSI2 | 0.0 | 0.00 | 0 | ok |
| — | ATR14 | 103.13 (5-session proxy) | 125.46 cash / 133.68 full | −22.33 (−17.8%) | discrepancy |
| 08 Jul | O / H / L / C | 10,666.09 / 10,666.09 / 10,467.01 / 10,489.04 | 10,634.1 / 10,636.3 / 10,454.7 / 10,457.0 | +31.99 / +29.79 / +12.31 / +32.04 | close FAIL; O, H, L discrepancies |
| 07 Jul | O / H / L / C | 10,664.57 / 10,700.00 / 10,645.00 / 10,691.98 | 10,657.8 / 10,739.6 / 10,639.1 / 10,680.1 | +6.77 / −39.60 / +5.90 / +11.88 | H and C discrepancies |
| 06 Jul | O / H / L / C | 10,679.03 / 10,690.00 / 10,620.00 / 10,651.77 | 10,672.4 / 10,726.7 / 10,607.9 / 10,641.1 | +6.63 / −36.70 / +12.10 / +10.67 | H, L, C discrepancies |
| 03 Jul | O / H / L / C | 10,651.30 / 10,747.01 / 10,651.17 / 10,679.03 | 10,689.3 / 10,692.5 / 10,590.6 / 10,660.5 | −38.00 / +54.51 / +60.57 / +18.53 | close FAIL; O, H, L discrepancies |
| 5-day swing | High / Low | 10,747.01 (3 Jul) / 10,419.22 | 10,739.6 (7 Jul) / 10,380.4 | +7.41 / +38.82 | low discrepancy; high date differs |
| 25-day low | | 10,127.60 | 10,126.2 | +1.40 | ok |
| RSI2 arithmetic | 59.6 / 16.5 / 0.0 | from report's own closes: 59.6 / 16.5 / 0.0 | 0 | arithmetic reproduces |

Pivots (report minus level-file cash values; |Δ| > 10 flagged):

| Frame | P | R1 | S1 | R2 | S2 | R3 | S3 |
|---|---|---|---|---|---|---|---|
| Daily | +0.37 | −38.10 | +10.67 | −48.40 | +49.14 | −86.87 | +59.44 |
| Weekly (W27 prior week) | +45.68 | +27.36 | +36.85 | +36.19 | +55.17 | +17.87 | +46.34 |
| Monthly (June) | −32.61 | −66.60 | −26.49 | −72.72 | +7.50 | −106.71 | +13.62 |

The daily P matches only by coincidence of offsetting H/L/C errors; every other daily level is off. The report's pivots are arithmetically correct for its own H/L/C, so the error is in the inputs.

## 3. Category roll-up

| Category | Rows | Mean | Level | Multiplier | Points | Justification |
|---|---|---|---|---|---|---|
| C1 Prompt adherence (20) | 2, 4, 4 | 3.33 | 3 | 0.65 | 13.00 | Core variables present; source tiers, ATR(14) and KER(13) not honoured; anchor wording contradictory. |
| C2 Structure (20) | 5, 3, 4 | 4.00 | 4 | 0.85 | 17.00 | All sections present; §6 columns and §11 depth deviate; §7 has no chart evidence. |
| C3 Accuracy & evidence (25) | 3, 0, 3, 2 | 2.00 | 0 (override) | 0.00 | 0.00 | Hallucinated-source override: Investing.com quote contradicts the report's own close and Low; D-1 close and Low also fail the slice check. |
| C4 Reasoning & judgment (20) | 3, 4, 4, 4, 1 | 3.20 | 3 | 0.65 | 13.00 | Strong cross-asset reasoning and tension handling; every card breaks M5 geometry. |
| C5 Currency & transparency (15) | 3, 3, 4, 3 | 3.25 | 3 | 0.65 | 9.75 | Dated and caveated in §4 and §19; articles undated, anchor caveat contradictory, calendar thin. |

## 4. Total, band, override
- Total = 13.00 + 17.00 + 0.00 + 13.00 + 9.75 = 52.75, rounded to **53**.
- Band: **Low (40–59)**.
- Override check: `hallucinated_source` applied (C3 forced to 0, cap Low 40–59; the total of 53 is inside the cap). Basis: the Investing.com quote in §4 (day range 10,430.29–10,458.95) excludes the report's own consensus close 10,429.22 and its stated "corroborated" Low 10,419.22; no §4 source supports that Low. No separate `restriction_breach` cap was applied because the hallucinated-source cap is the binding one.
- Without the override the C3 rows give level 2 (0.40 x 25 = 10.0), total would be 63 (Moderate). Shown for transparency only.

## 5. Card Integrity (linter rows copied verbatim from `qa/ftse_qa1/lint_static/2026-07-10.csv`; separate from the 100)

| card_id | report_date | strategy | flags | dud | Card Integrity |
|---|---|---|---|---|---|
| 2026-07-10_Trade_1 | 2026-07-10 | Trade 1 — Daily Directional | CLEAN | False | 100 |
| 2026-07-10_Trade_2 | 2026-07-10 | Trade 2 — Pivot, TRANSITION branch | CLEAN | False | 100 |
| 2026-07-10_Trade_3A | 2026-07-10 | Trade 3A — Momentum-Pullback | CLEAN | False | 100 |

Report-level Card Integrity = 100 (3 cards, 0 DUD, 0 WARN, none suppressed). The static linter does not test variant mapping, entry geometry, break-even side or ATR source; those defects are scored in row 4.5 and listed in the feedback file.
