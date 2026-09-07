# Trust Score — 2026-06-08 — SP500_Report_08-Jun-2026.md

## 1. Section 7 checklist

| Item | Reviewer notes | Evidence observed | Score 0–5 | Action required |
|---|---|---|---|---|
| 1.1 All Variables visibly respected | Asset = S&P 500 cash index (^GSPC), explicitly "not a futures-derived level"; counters USDX · VIX · DAX 40 in the required order with USDX first; as-of 8 Jun 2026 America/New_York, last corroborated session Fri 5 Jun; 5-session execution / 25-session regime lookback; USD, index points, tick 0.01. **Failure: the daily-open anchor.** M1 specifies 07:00 UK for Trade 1; the run applied a 00:00 UK override and then re-mapped it a second time to the 14:30 UK cash open. Source list is 6 rows but tier coverage is thin — one index-provider tier (S&P DJI/FRED), no exchange tier, and "StreetStats / Polymarket resolution feed" is one row counted as two independent sources in §3. | §2 table; header note; §4; §20 anomaly (1); §21b Trade 1 Entry | 3 | Restore the 07:00 UK anchor (broker 09:00) for Trade 1, or carry the override as an explicit variable deviation without a second re-map; add an exchange-tier or second index-provider source and stop counting a bundled row as two sources |
| 1.2 Coverage window and currency consistent | Currency/units are clean throughout (index points, USD, no drift). Every dated item is D-1 or earlier for data and D for the session. **Period drift:** §11 weekly pivots are built from the week 25–29 May, which was the correct prior week for the 5 Jun report (see `SP500_Report_05Jun2026.md` §11 "Weekly pivots (from W/E 29 May)") but is one week stale for D = Mon 8 Jun, where the prior completed week is 1–5 Jun. §11 monthly block also misses the 4 May low, so its window does not cover all of May. | §11 weekly + monthly blocks; cf. `reports/md/SP500_Report_05Jun2026.md:327` | 2 | Roll the weekly pivot window to 1–5 Jun; rebuild the monthly window to span 1–29 May |
| 1.3 Audience and tone | Senior US Equity Strategist register sustained; framed for trading and risk review (forward-test); no retail tone, no promotional language; "Not investment advice · point-in-time" closing boilerplate present. | §1, §18, closing italics | 5 | None |
| 2.1 All sections present and correctly ordered | §1–§21 all present in order; §13 carries 13a/13b/13c/13d; §21 carries 21a/21b/21c/21d including the limitations boilerplate; §11 carries daily, weekly and monthly blocks. | Headings throughout | 5 | None |
| 2.2 Scorecard rendered as a table | §6 is a table but is missing three of the eleven required columns — **Source A, Source B and Final** are relegated to a footnote rather than rendered as columns. §11 pivot tables are correctly ordered R3→R2→R1→P→S1→S2→S3 with 3 levels each side for daily, weekly and monthly. | §6 table and its footnote; §11 | 3 | Re-render §6 with Date/O/H/L/C/RSI2/Trend/Source A/Source B/Final/Validation as columns |
| 2.3 Method steps visible | §4 observations → §5 classification and consensus build are explicit; §8 is genuinely candle-by-candle with a named sequence assessment; §9 gives regime with persistence, overlap and VOLator. §7 charts are present as five captioned pandoc image placeholders (images dropped in md — accepted as evidence, noted). §9's persistence and overlap are asserted qualitatively ("overlap ... has risen", "median RSI2 ... in the low-30s") with no figure shown. | §4, §5, §7 captions, §8, §9 | 4 | Show the numeric persistence / overlap / median-RSI2 values behind the §9 regime label |
| 3.1 Every quantitative claim sourced | Payrolls 172k, unemployment 4.3%, Nasdaq −4.2%, AVGO −12.6% trace to §13a/§13c. Unsourced: 2026 EPS ≈ $340, Q1 beats ≈ 6%, 10y > 4.5% and 30y > 5%, core CPI ≈ 2.6%, 50-/200-day averages ≈ 7,156 / 6,858, MU −7.7%, AMD −3.6%. **Sourced numbers that do not survive the slice:** ATR(14) ≈ 47 vs 70.34 (cash) / 82.19 (full-day); VIX "+39.7% to 21.51" vs 18.46 and +13.88% — an error that also flips the report's own ">20 elevated" characterisation. | §9, §12, §14; §8/§20 ATR; §10 VIX row | 2 | Attach a source to each §12/§14 figure; recompute ATR(14) and restate the VIX level and one-day change |
| 3.2 Spot-checked citations exist and contain the cited data | (a) **Fortune 5 Jun** — quoted "−200.57"; 7,584.31 − 7,383.74 = 200.57 and 200.57/7,584.31 = 2.645% ≈ the report's −2.64%: internally consistent. (b) **AP / Yahoo 5 Jun 16:18 ET** — headline dates to Friday 6/5/2026; 5 Jun 2026 is indeed a Friday given Mon 1 Jun; quote "worst day since October" is consistent with §1/§8's "largest one-day fall of 2026". (c) **Trading Economics 5 Jun** — raw 7,384; §20 records Δ ≈ 0.26 vs AP, but §3/§5/§19 all assert the six sources agree "within ±0.10 pt". That is the report contradicting its own tolerance claim, not the source contradicting itself. No citation is impossible or self-inconsistent → **no hallucination override**. Weakness: §3 counts the bundled "StreetStats / Polymarket resolution feed" row as two independent sources, and a prediction-market resolution feed is not an independent EOD index source. | §4 rows; §13a rows; §20 corroboration pairs | 3 | Reconcile the ±0.10 pt claim with the recorded Δ 0.26; split or drop the bundled StreetStats/Polymarket row and stop counting it twice |
| 3.3 Calculations transparent | RSI2 reproduces **exactly** from the report's own close sequence — helper returns 14.9 / 35.3 / 13.2 against the report's 14.9 / 35.3 / 13.2. All five Trend labels obey the stated rule (4 Jun correctly Neutral on C>O with RSI2 35.3 < 50). §11 daily pivots reproduce exactly from the report's own Friday H/L/C (P 7,439.58, R1 7,519.16, S1 7,304.16, R2 7,654.58, S2 7,224.58, R3 7,734.16, S3 7,089.16 — all seven check). Weekly and monthly blocks are each internally consistent with a single H/L/C. ATR(14) and KER(13) are stated. **Gap:** §21a's −0.36 is not reproducible — the four components shown (−0.15, −0.11, −0.06, +0.02) sum to −0.30 and the remaining two of the six weighted signals are never shown. | §6 + helper; §11; §20; §21a | 4 | Print all six signal×weight terms in §21a so the score sums to its stated value |
| 3.4 Numbers reconcile across sections | Reconciles: D-1 close 7,383.74 identical in §1/§3/§4/§6/§18 and on the Trade 1 card (7,384); §11 pivot values equal the levels quoted on both cards; ATR ≈ 47 consistent across §8/§20/§21b; RSI2 13.2 consistent across §1/§6/§8/§15. **Breaks:** (i) §5 and §19 state Friday O/H/L "were not used to anchor daily pivots or any entry/stop pricing", but §11 derives the daily pivots from Friday's H/L/C and the Trade 1 stop cites "indicative daily P (7,439.58)" as its structural anchor; (ii) §3/§5/§19 "±0.10 pt across six" vs §4/§20 Trading Economics Δ 0.26; (iii) §8's "true range (~224 points)" does not equal the report's own H−L of 215.00 — it only reconciles against the prior close, a basis never stated; (iv) Trade 3A TP1 is labelled "38.2% retrace of the 7,621→7,384 down-leg ... ≈ 7,384 (~1R)" when 38.2% of that leg is 7,474.34 and 7,460 − 7,384 = 76 pts = 0.72R. | §5, §8, §11, §19, §21b | 2 | Fix the four reconciliation breaks listed; the §5/§19 no-anchor claim and the §11/§21b use of the indicative daily P cannot both stand |
| 4.1 Each pillar reaches a defended conclusion | §8 "Exhaustion — reversal risk"; §9 "TRANSITION, Neutral-to-Bearish"; §10 "CONFIRM (bearish)"; §12 each driver carries a price-supportive/negative + structural/cyclical label; §14 each block concludes. All labels follow from their own content. **The strategy pillar does not:** Trade 3A is declared a 3A Momentum-Pullback but its entry, stop, TP1 and TP2 are all pivot levels rather than the 57.5% / 0%+0.25×ATR / 38.2% / 0% geometry the variant requires, and the qualifying swing endpoints are never logged. | §8–§14 labels; §21b Trade 3A | 3 | Rebuild Trade 3A on the logged swing geometry, or relabel the card as the pivot trade it actually is |
| 4.2 Peer / cross-asset interpreted, not listed | §10 gives a real transmission mechanism for each counter — dollar → financial conditions and earnings translation; VIX → demand for downside protection and de-risking; DAX → common global-risk and tech factor — and states an aggregate CONFIRM with an explicit "no contradiction" check. Undermined by the VIX inputs: 21.51 / +39.7% vs slice 18.46 / +13.88%, and the "'elevated' (>20)" reading is false at 18.46, so the "strongest confirming signal" rests on a wrong number. DAX 24,759 / −0.75% cannot be checked (no DAX slice). | §10 table and aggregate line; §14 | 3 | Restate the VIX level, one-day change and threshold characterisation, then re-derive the cross-asset aggregate |
| 4.3 Synthesis reconciles tensions | §9 resolves KER-ranging vs residual bullish structure by an explicit precedence rule; §8's consistency note names the short-term vs 25-session tension; §15 balances three bull against three bear items; §16 states a base case with an explicit invalidation level; §21a carries a conflict flag against §17 and downgrades conviction to moderate. Genuine reconciliation, not assertion. Weakness: the tensions are resolved onto weekly/monthly levels (7,420.40 / 7,342.66) that come from the wrong window. | §9, §15, §16, §18, §21a | 4 | Re-run the §16/§17 objectives once the weekly and monthly pivot windows are corrected |
| 4.4 Calibrated language | §17 is exactly one sentence with a single conditional, no hedge stacking. §3 states confidence "High (close)". §21a states conviction explicitly as moderate rather than high and says why. §13b gives a numeric tilt alongside the categorical label. | §3, §13b, §17, §21a | 5 | None |
| 5.1 Data points dated; staleness flagged | Every §6 row, §4 row and §13a article is dated; Friday O/H/L are flagged single-source–indicative in §5, §6 footnote, §11, §19 and on both cards; §19 lists the data gaps and the failed source attempts; §13b down-weights the two stale bullish articles and says so. **Not flagged:** the weekly pivot block is a week stale yet is labelled "CORROBORATED", and the monthly block is labelled "CORROBORATED" while its implied low (7,233.62) misses the actual May low of 7,177.50 by 56.12 pts. | §5, §6 footnote, §11, §13b, §19 | 3 | Date-stamp the weekly and monthly pivot windows explicitly and re-verify before labelling either CORROBORATED |
| 5.2 Material assumptions stated up front | Anchor-override caveat appears in the header note, in §20 anomaly (1) with its executability consequence, and on the Trade 1 card itself. Single-source-indicative pivot propagation to §21 is stated in §11, §19, §20 and in both card caveat rows. The corroboration-leniency run instruction is disclosed in §20 anomaly (2). Normalization assumptions stated in §5 and §19. | Header; §5; §11; §19; §20; §21b | 5 | None |
| 5.3 Red flags surfaced | §12 carries four labelled risk drivers; §15 is a two-sided table; the §13d FOMC collision is carried into the caveat row of both cards; oversold-bounce risk (RSI2 13.2) is carried into both cards; the USDX cross-source level discrepancy is surfaced in §14 and §19; §21d states the five-session sample limitation. | §12, §13d, §15, §19, §21b, §21d | 5 | None |
| 5.4 All prompt restrictions honoured | **BREACHED.** (i) §20 opens a paragraph "M5 trace: direction-score weights = DEFAULTS (v2.1 baseline ...)" — a module code in the delivered report, explicitly prohibited. (ii) §20 anomaly (1) prints the raw prompt variable token "DAILY_OPEN_ANCHOR". (iii) The OHLC basis in §4/§6 is sourced from Investing.com "US500" and Trading Economics "US500" — a CFD/spread-bet contract name presented as the cash basis, against the no-retail-CFD-quotes restriction, and consistent with the systematic 6.0–11.5 pt downward offset on all five closes vs the cash slice. (iv) The no-synthesis claim in §5/§19 that Friday's indicative O/H/L did not anchor pivots or entry/stop pricing is contradicted by §11 and by the Trade 1 stop rationale. | §4, §5, §6, §11, §19, §20 (lines 603, 611), §21b | 0 | Strip module codes and variable tokens from §20; state the cash-index source by its own name rather than a CFD contract ticker; make the no-synthesis claim in §5/§19 true or withdraw it → **restriction override triggered** |

## 2. Category roll-up

| Category | Level | Multiplier | Points | Justification |
|---|---|---|---|---|
| C1 Prompt adherence (20) | 2 | 0.40 | 8.00 | Rows 1.1/1.2/1.3 = 3/2/5, mean 3.33 → level 3 on merit; the 5.4 restriction breach drops C1 one level to 2 per the override rule. Asset, counters, units and audience are clean; the 07:00 UK anchor variable and the weekly-pivot period are not. |
| C2 Structure (20) | 4 | 0.85 | 17.00 | Rows 2.1/2.2/2.3 = 5/3/4, mean 4.00. All 21 sections and every sub-section present and ordered; the §6 scorecard is missing its Source A / Source B / Final columns. |
| C3 Accuracy & evidence (25) | 3 | 0.65 | 16.25 | Rows 3.1/3.2/3.3/3.4 = 2/3/4/2, mean 2.75 → 3. Internal arithmetic (RSI2, Trend, all three pivot blocks) is exact and reproducible; the inputs it is run on are not — five of five closes outside the 3 pt tolerance, four O/L/H values outside the 8 pt tolerance, ATR 33% low, VIX materially wrong, weekly window one week stale. No fabricated source found. |
| C4 Reasoning & judgment (20) | 4 | 0.85 | 17.00 | Rows 4.1/4.2/4.3/4.4 = 3/3/4/5, mean 3.75 → 4. Pillar logic, tension reconciliation and calibration are strong; Trade 3A is not built to its declared M5 variant and the cross-asset mechanism rests on a wrong VIX print. |
| C5 Currency, restrictions & transparency (15) | 3 | 0.65 | 9.75 | Rows 5.1/5.2/5.3/5.4 = 3/5/5/0, mean 3.25 → 3. Disclosure and caveating are exemplary; the restriction row is a zero on module codes, variable tokens and a CFD-sourced OHLC basis. |
| **Total** | — | — | **68.00** | 8.00 + 17.00 + 16.25 + 17.00 + 9.75 |

## 3. Total, band, override check

- Raw weighted total: **68.00 → 68**
- Override check — hallucinated source: **not triggered.** All three spot-checked citations (Fortune, AP/Yahoo, Trading Economics) are internally consistent — Fortune's −200.57 and AP's date/day-of-week both reconcile, and Trading Economics' 7,384 is a genuine rounding of 7,383.74. The ±0.10 pt inconsistency is the report misdescribing its own tolerance, not a source that cannot exist. C3 is **not** zeroed.
- Override check — breached prompt restriction: **TRIGGERED** (row 5.4). Module code "M5 trace" and the raw variable token "DAILY_OPEN_ANCHOR" appear in §20; the §4/§6 OHLC basis is a US500 CFD feed. Consequences applied: total capped at 74, C1 dropped one level (3 → 2).
- Cap effect: 68 is already below the 74 cap, so the cap does not bind; the C1 demotion cost 3.00 points (11.00 → 8.00).
- **Final Trust Score: 68 — Band: Moderate (60–74) — Override: restriction_breach**

## 4. Card Integrity

Linter rows, verbatim from `qa/regen_20260906_qa1/lint_static/2026-06-08.csv`:

| card_id | report_date | strategy | flags | dud |
|---|---|---|---|---|
| 2026-06-08_Trade_1 | 2026-06-08 | Trade 1 - Daily Directional | CLEAN | False |
| 2026-06-08_Trade_3A | 2026-06-08 | Trade 3A - Momentum-Pullback (sell limit weekly S2) | CLEAN | False |

Per-card integrity (100 − 40·#DUD − 10·#WARN, floored at 0):

| Card | #DUD | #WARN | Integrity |
|---|---|---|---|
| 2026-06-08_Trade_1 | 0 | 0 | 100 |
| 2026-06-08_Trade_3A | 0 | 0 | 100 |

- Non-suppressed cards: 2. **Report-level Card Integrity = 100.0**
- **This date carries fewer than three cards.** The lint file and `cards/baseline/by_date/2026-06-08.json` contain two rows only. §21b of the report does render a Trade 2 SUPPRESSED block in prose, but no Trade 2 record with `suppressed: true` was emitted into the card layer, so the linter sees an omission rather than a suppression. M5 requires a SUPPRESSED row, not an omission.
- Card Integrity is the static, leak-free geometry score only. Both cards pass it while still breaching M5 construction rules that the static linter does not test (wide-stop flag, runner ATR cap, 3A retrace geometry, anchor time). Those are scored in row 4.1 and itemised in the feedback file.

## 5. Data reconciliation log

Tolerances per the reviewer brief: |Δ| ≤ 3.0 pts on a close, ≤ 8.0 pts on an open/high/low. Slice values are cash-session (16:30–23:00 broker) from `data/slices/US500/US500_upto_2026-06-07.csv`.

| Section | Report value | Slice value | Delta | Verdict |
|---|---|---|---|---|
| §6 Mon 1 Jun Open | 7,582.29 | 7,575.20 | +7.09 | PASS |
| §6 Mon 1 Jun High | 7,617.66 | 7,623.60 | −5.94 | PASS |
| §6 Mon 1 Jun Low | 7,562.61 | 7,568.50 | −5.89 | PASS |
| §6 Mon 1 Jun Close | 7,599.96 | 7,606.00 | −6.04 | **FAIL** (>3 pt) |
| §6 Tue 2 Jun Open | 7,595.40 | 7,590.80 | +4.60 | PASS |
| §6 Tue 2 Jun High | 7,620.90 | 7,624.60 | −3.70 | PASS |
| §6 Tue 2 Jun Low | 7,582.99 | 7,588.30 | −5.31 | PASS |
| §6 Tue 2 Jun Close | 7,609.78 | 7,615.80 | −6.02 | **FAIL** (>3 pt) |
| §6 Wed 3 Jun Open | 7,605.31 | 7,602.00 | +3.31 | PASS |
| §6 Wed 3 Jun High | 7,605.35 | 7,608.00 | −2.65 | PASS |
| §6 Wed 3 Jun Low | 7,551.22 | 7,556.00 | −4.78 | PASS |
| §6 Wed 3 Jun Close | 7,553.68 | 7,565.20 | −11.52 | **FAIL — Category 3 failure** (>10 pt) |
| §6 Thu 4 Jun Open | 7,516.54 | 7,541.30 | −24.76 | **FAIL** (>8 pt); report prints Open = Low = 7,516.54, a synthesised-looking pair |
| §6 Thu 4 Jun High | 7,598.19 | 7,604.30 | −6.11 | PASS |
| §6 Thu 4 Jun Low | 7,516.54 | 7,535.00 | −18.46 | **FAIL** (>8 pt) |
| §6 Thu 4 Jun Close | 7,584.31 | 7,592.70 | −8.39 | **FAIL** (>3 pt) |
| §6 Fri 5 Jun Open | 7,560.00 | 7,540.50 | +19.50 | **FAIL** (>8 pt); flagged indicative in the report |
| §6 Fri 5 Jun High | 7,575.00 | 7,545.30 | +29.70 | **FAIL** (>8 pt); flagged indicative |
| §6 Fri 5 Jun Low | 7,360.00 | 7,372.80 | −12.80 | **FAIL** (>8 pt); flagged indicative |
| §6 Fri 5 Jun Close | 7,383.74 | 7,392.50 | −8.76 | **FAIL** (>3 pt) |
| §6 RSI2 1 Jun / 2 Jun | 100.0 / 100.0 | 100.00 / 100.00 | 0.00 / 0.00 | PASS |
| §6 RSI2 3 Jun | 14.9 | 16.23 | −1.33 | PASS (basis-explained) |
| §6 RSI2 4 Jun | 35.3 | 35.21 | +0.09 | PASS |
| §6 RSI2 5 Jun | 13.2 | 12.08 | +1.12 | PASS (basis-explained) |
| §6 RSI2 recomputed from the report's OWN closes | 14.9 / 35.3 / 13.2 | helper: 14.9 / 35.3 / 13.2 | 0.00 | **PASS — RSI2 arithmetic is exact** |
| §6 Trend labels (all 5 rows) | Bullish/Bullish/Bearish/Neutral/Bearish | rule applied to the report's own O/C/RSI2 | — | PASS — all five correct |
| §11 Daily pivots, reproduction from the report's own Fri H/L/C (7,575.00 / 7,360.00 / 7,383.74) | P 7,439.58 · R1 7,519.16 · R2 7,654.58 · R3 7,734.16 · S1 7,304.16 · S2 7,224.58 · S3 7,089.16 | all seven recomputed identically | 0.00 | **PASS — internally exact** |
| §11 Daily P | 7,439.58 | 7,436.87 | +2.71 | PASS |
| §11 Daily R1 | 7,519.16 | 7,500.93 | +18.23 | **FAIL** |
| §11 Daily S1 | 7,304.16 | 7,328.43 | −24.27 | **FAIL** |
| §11 Daily R2 / S2 | 7,654.58 / 7,224.58 | 7,609.37 / 7,264.37 | +45.21 / −39.79 | **FAIL** — range inflated (215.00 stated vs 172.50 actual) |
| §11 Daily R3 / S3 | 7,734.16 / 7,089.16 | 7,673.43 / 7,155.93 | +60.73 / −66.77 | **FAIL** |
| §11 Weekly window | "prior week 25–29 May" | prior completed week for D = Mon 8 Jun is **1–5 Jun** | one week stale | **FAIL — wrong window** (the 5 Jun report legitimately used W/E 29 May; it was not rolled forward) |
| §11 Weekly P | 7,559.72 | 7,463.30 (1–5 Jun) | +96.42 | **FAIL** |
| §11 Weekly R1 | 7,619.72 | 7,553.80 | +65.92 | **FAIL** |
| §11 Weekly S1 | 7,520.06 | 7,302.00 | +218.06 | **FAIL** |
| §11 Weekly S2 | 7,460.06 | 7,211.50 | +248.56 | **FAIL** — this level is Trade 3A's entry |
| §11 Weekly S3 | 7,420.40 | 7,050.20 | +370.20 | **FAIL** — this level is the §16/§17 primary objective |
| §11 Weekly block vs the 25–29 May week it actually used | P 7,559.72 (implied H 7,599.38 / L 7,499.72 / C 7,580.06) | P 7,563.63 (H 7,601.80 / L 7,504.30 / C 7,584.80) | −3.91 (P) | PASS against the wrong week — the arithmetic is right, the window is not |
| §11 Monthly implied High | 7,599.38 | 7,601.80 (29 May) | −2.42 | PASS |
| §11 Monthly implied Low | 7,233.62 | 7,177.50 (4 May) | +56.12 | **FAIL** — the early-May low is outside the window used |
| §11 Monthly P | 7,471.02 | 7,454.70 | +16.32 | **FAIL** |
| §11 Monthly R1 | 7,708.42 | 7,731.90 | −23.48 | **FAIL** |
| §11 Monthly S1 | 7,342.66 | 7,307.60 | +35.06 | **FAIL** — Trade 3A TP2 and a §17 objective |
| §11 Monthly S2 | 7,105.26 | 7,030.40 | +74.86 | **FAIL** — Trade 1 TP3 / runner target |
| §11 Monthly S3 | 6,976.90 | 6,883.30 | +93.60 | **FAIL** |
| §8 / §20 ATR(14) | ≈ 47 pts | 70.34 (cash) · 82.19 (full-day) | −23.34 (cash) | **FAIL** — 33% low; drives the "≈2.0× ATR" stop claim (true 1.29×) and the "4.7× ATR" range claim (true 3.1×) |
| §8 Friday true range | ≈ 224 pts | 219.90 (cash TR incl. prior close) | −4.10 | PASS, but does not equal the report's own H−L of 215.00; the prior-close basis is unstated |
| §1 / §10 / §14 VIX level | 21.51 | 18.46 | +3.05 | **FAIL** — and the ">20 elevated" characterisation is false at 18.46 |
| §1 / §10 VIX one-day change | +39.7% | +13.88% | +25.8 pp | **FAIL** |
| §10 / §14 USDX | "rising to ~99.5–100" | 100.072, +0.63% on the day, up four of five sessions | ≈ 0 | PASS |
| §10 DAX 40 | 24,759, −0.75% | no DAX slice available | — | UNVERIFIED |
| §12 / §13c May Non-Farm Payrolls | 172k actual | 172.0 (NEWS calendar, 2026-06-05, HIGH) | 0.0 | PASS |
| §12 payrolls consensus | "~85k expected" | 77.0 | +8.0 | MINOR — restate to the calendar consensus |
| §13c payrolls prior | "Apr ~120k" | 115.0 | +5.0 | MINOR |
| §12 unemployment rate | 4.3% | 4.3 | 0.0 | PASS |
| §21a direction score | −0.36 | shown components sum to −0.30 | −0.06 unexplained | **FAIL** — two of the six weighted terms are never shown |
| §21b Trade 1 entry (card) | 7,384.0 MARKET | report D-1 close 7,383.74 · slice D-1 cash close 7,392.50 | +0.26 vs report · −8.50 vs slice | PASS vs the report's own basis; FAIL vs the slice |
