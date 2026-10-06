# Trust Score v3.7 — FTSE 100 report dated 24 June 2026 (run ftse_qa1)

Report: `reports/md/FTSE_EuroStoxx_Report_24Jun2026.md` · D = 2026-06-24 · D-1 = 2026-06-23
Level file check: `last_bar_date` = 2026-06-23 < D, so it is leak-free. Basis compared: cash (`_cash`), the basis the report claims (cash index, 08:00–16:30 London).

## Machine-readable result
```
c1=2
c2=4
c3=0
c4=3
c5=2
total=44
band=Low
override=hallucinated_source
card_integrity=75.0
n_cards=3
n_duds=1
n_warns=1
```
`n_cards=3` is the number of card rows transcribed (1 SUPPRESSED, 2 scored). Card Integrity is averaged over the 2 scored cards. Card Integrity is separate and is not in the 100.

## 1. Category 3 data check (report vs level file and slice, D-1 = 23 Jun)

Tolerance (brief §4): |Δ| ≤ 5 pts on a close, ≤ 10 pts on an open/high/low. A close off by more than 15 pts, or an RSI2 that does not reproduce, is a Category 3 failure. Δ = report − cash slice.

| Session | Field | Report | Cash (slice) | Δ | Verdict |
|---|---|---|---|---|---|
| 23 Jun (D-1) | Open | 10439.4 | 10329.6 | +109.8 | FAIL (and equals the 22 Jun close, i.e. chained, not sourced) |
| 23 Jun | High | 10448.6 | 10461.5 | −12.9 | FAIL (>10) |
| 23 Jun | Low | 10345.8 | 10328.1 | +17.7 | FAIL |
| 23 Jun | Close | 10377.5 | 10453.0 (full-day 10429.8) | −75.5 (−52.3) | FAIL (>15) |
| 23 Jun | RSI2 | 55.1 | 100.0 (`rsi2_cash`) | −44.9 | FAIL (report arithmetic is internally reproducible; the closes are wrong) |
| 22 Jun | Open / High / Low / Close | 10363.3 / 10452.8 / 10350.1 / 10439.4 | 10379.2 / 10441.4 / 10343.2 / 10440.9 | −15.9 / +11.4 / +6.9 / −1.5 | Open FAIL, High FAIL, Low pass, Close pass |
| 19 Jun | O / H / L / C | 10388.2 / 10421.0 / 10351.7 / 10363.3 | 10383.1 / 10417.4 / 10347.8 / 10352.3 | +5.1 / +3.6 / +3.9 / +11.0 | Close FAIL (>5), rest pass |
| 18 Jun | O / H / L / C | 10333.5 / 10402.1 / 10309.4 / 10388.2 | 10460.3 / 10475.8 / 10372.6 / 10399.6 | −126.8 / −73.7 / −63.2 / −11.4 | all FAIL |
| 17 Jun | O / H / L / C | 10271.9 / 10349.8 / 10240.6 / 10333.5 | 10494.9 / 10513.3 / 10470.9 / 10513.3 | −223.0 / −163.5 / −230.3 / −179.8 | all FAIL |
| 25-session range | High / Low | 10570.09 / 10127.60 | 10574.6 / 10126.2 | −4.5 / +1.4 | pass |

RSI2 arithmetic: `--closes` on the report's own five closes reproduces 68.7 / 75.3 / 55.1 for 19, 22 and 23 Jun (the first two rows need earlier closes). Trend labels follow the stated rule on every row. The arithmetic is correct. The inputs are not: the slice's cash RSI2 path is 100.0 / 2.7 / 0.0 / 65.2 / 100.0 for 17–23 Jun, so the report's "bullish run into 22 Jun, bearish rollover on 23 Jun" does not match the data. The slice shows 18 and 19 Jun as down closes, then up closes on 22 and 23 Jun (cash close 10453.0 vs 10440.9, +12.1 pts).

Structural signs of synthesis in §6: the Open of every session from 18 Jun onward equals the prior session's Close exactly (10333.5, 10388.2, 10363.3, 10439.4). Real feeds do not produce that.

ATR14: never stated in the report (implied only by the Trade 3C trigger 10098.6 = 10127.6 − 0.25 × ~116). Slice: ATR14 cash 116.26, full-day 141.23.

Pivots (report vs `_cash`; Δ = report − slice):

| Table | Report-stated source period | Level | Report | Slice (cash) | Δ |
|---|---|---|---|---|---|
| Daily | "prior session 22 Jun" (D-1 is 23 Jun, so one session stale) | P | 10414.1 | 10414.2 | −0.1 (coincidental; inputs are the wrong session) |
| | | R1 / S1 | 10478.1 / 10375.4 | 10500.3 / 10366.9 | −22.2 / +8.5 |
| | | R2 / S2 | 10516.8 / 10311.4 | 10547.6 / 10280.8 | −30.8 / +30.6 |
| | | R3 / S3 | 10580.8 / 10272.7 | 10633.7 / 10233.5 | −52.9 / +39.2 |
| Weekly | 15–19 Jun | P | 10304.0 | 10424.9 | −120.9 |
| | | R1 / S1 | 10480.3 / 10186.9 | 10502.0 / 10275.2 | −21.7 / −88.3 |
| | | R2 / S2 | 10597.4 / 10010.6 | 10651.7 / 10198.1 | −54.3 / −187.5 |
| | | R3 / S3 | 10773.7 / 9893.5 | 10728.8 / 10048.4 | +44.9 / −154.9 |
| Monthly | May | P | 10417.3 | 10370.4 | +46.9 |
| | | R1 / S1 | 10504.0 / 10264.4 | 10599.6 / 10180.8 | −95.6 / +83.6 |
| | | R2 / S2 | 10656.9 / 10177.7 | 10789.2 / 9951.6 | −132.3 / +226.1 |
| | | R3 / S3 | 10743.6 / 10024.8 | 11018.4 / 9762.0 | −274.8 / +262.8 |

The pivot formulas are applied correctly to the report's own inputs (daily H/L/C 10452.8 / 10350.1 / 10439.4 reproduce every level). The inputs are wrong:
- Weekly: implied H/L/C is 10421.1 / 10127.7 / 10363.2. The low 10127.7 is the 10 Jun month low, outside 15–19 Jun, and below every low in the report's own §6 (min 10240.6). The slice week is H 10574.6 / L 10347.8 / C 10352.3.
- Monthly: implied H/L/C is 10570.2 / 10330.6 / 10351.1. 10570.2 is the 22 May–22 Jun range high, not May. Slice May is H 10560.0 / L 10141.2 / C 10410.0.
- Daily: R4, R5, S4, S5 are extra (brief asks for three levels each side). Labelled "indicative".

Counters (slices to D-1): USDX 101.39 at 23 Jun (report says ≈100.6, i.e. stale by about 4 sessions; direction "rising" is right). S&P 500 −1.3% on 23 Jun to 7386.4, 5-day direction falling (matches). VIX 18.88 ("high-teens" matches). DAX 40 and Euro Stoxx 50 have no slice and could not be tested.

Calendar (news slice): the BoE rate decision (3.75% hold, 2 hike votes) was 18 Jun and UK CPIH was 17 Jun, so both are already past. The report lists "UK CPI / BoE commentary" as the live upcoming catalyst "within 5d" and cites April CPI (2.80%) as latest. Eurozone and UK flash PMIs were released on 23 Jun, yet §12 and §13d list "Eurozone flash PMIs" as upcoming. Scheduled D events absent from §13d: Ifo Business Climate / Expectations / Current Situation, 10y bond auction, BoE MPC member Dhingra speech, US New Home Sales, EIA crude stocks.

## 2. Section 7 checklist

| Row | Notes | Evidence | Score |
|---|---|---|---|
| 1.1 Variables respected | Asset (FTSE 100 cash), counters, as-of D-1, tz, 5-session lookback, GBP points respected. Seven named sources, but all are aggregator/media tier (Investing, Yahoo, TE, MarketScreener, Reuters-via-screener) plus a bare "LSE official"; no index-provider (FTSE Russell) quote. The 07:00 UK Trade 1 anchor was overridden to 00:00 UK (declared in §20 only). | §2, §4, §20 | 3 |
| 1.2 Coverage & currency consistent | Daily pivots built from 22 Jun (D-2), not 23 Jun. §3 gives two anchors (23 Jun ≈10,378 consensus, 22 Jun "higher-confidence"). UK CPI (Apr) and "upcoming" CPI/BoE and PMIs are past events. USDX 100.6 vs 101.39. | §3, §11, §12, §13d | 2 |
| 1.3 Audience & tone | Strategist register, trading-and-risk use. Minor informalities ("round-ish level", "generous post-fakeout stop"). | §1, §18, §21b | 4 |
| 2.1 Sections present & ordered | §1–§21 all present and in order, including §13a–d and §21a–d. | headings | 5 |
| 2.2 Scorecard as a table | §6 is a table, but has no "Final" column. §11 tables are ordered high-to-low; daily table runs R5→S5 instead of three levels each side. | §6, §11 | 4 |
| 2.3 Method steps visible | Observations → consensus shown; §8 candle-by-candle; §9 overlap/persistence/VOLator/KER shown. §7 is five chart headings with no caption or placeholder text (accepted as pandoc loss, noted). §5 "weighted-median" is asserted, not shown. | §4–§9 | 4 |
| 3.1 Quantitative claims sourced | The headline numbers (23 Jun close, 17–19 Jun OHLC, pivots) are wrong against the data. Unsourced figures: USDX ≈100.6, UK 10y gilt 4.88%, ≈80% overseas revenue, CPI 2.80% / 3.30%, VIX "high-teens", oil "three-month low", 10,512 resistance (appears nowhere else). | §1, §12, §14, §15 | 1 |
| 3.2 Citations exist & contain data | Spot-checks: (a) Yahoo "22 Jun 16:24 UK, cash close 10,439.40": a close quote stamped before the 16:30 close and the 16:35 auction is impossible. (b) Trading Economics "23 Jun (intra) ≈ −0.6% ≈ 10,377": no price quote, only a percentage on an intraday CFD snapshot. §6 then presents 10,377.5 as "CORROBORATED (close)" with Src A/B Investing/Yahoo, but no such quote exists in §4, and §19 itself says the 23 Jun level is only "directionally corroborated". (c) Goldman / Investing.com item dated only "Jun". 17–19 Jun closes are labelled "Close corrob." with no §4 evidence and miss the data by 180 / 11 / 11 pts. Judged fabricated under the brief's "impossible / figure not matching its own quote" test. | §4, §6, §13a, §19 | 0 (override) |
| 3.3 Calculations transparent | RSI2 reproducible from own closes (68.7 / 75.3 / 55.1); trend rule applied correctly; daily pivot formulas reproduce; §21a trace sums to +0.197 with correct weights (0.25/0.20/0.10/0.15/0.15/0.15). ATR(14) never stated; KER given without its parameters; weekly/monthly inputs not shown and not reproducible from §6. | §6, §11, §9, §20 | 3 |
| 3.4 Numbers reconcile | D-1 close 10,377.5 consistent across §1, §3, §6, §21b. Breaks: §6 "CORROBORATED (close)" vs §19 "directionally corroborated"; weekly low 10127.7 vs §6 lows ≥ 10240.6; §16 range 10,200–10,510 vs §17 10,300–10,500; §8 "nearest support 10,240.6" vs §11 S1 10,375.4; §19 "CFD excluded from the level build" vs the CFD-derived 10,377; §11 narrative garbled ("sits just above daily P (10,414 is above; close is below P…)"). | cross-section | 2 |
| 4.1 Pillars conclude | §8 "Indecision", §9 "Transitional", §10 "MIXED", §12 headings labelled. §14 bullets end without a direction label. | §8–§14 | 4 |
| 4.2 Cross-asset interpreted | Mechanism given per counter (USD translation vs tightening, Wall St beta, continental proxy). Oil/energy weight covered in §12. | §10, §12 | 4 |
| 4.3 Synthesis reconciles tensions | §21a vs §17 conflict is flagged. Not reconciled: §8's "Indecision / early exhaustion" vs the +0.125 short-term bullish contribution; §10 "MIXED" vs +0.045; score +0.20 (long) vs both live cards SHORT; Trade 3C rationale "retests stalled at the upper boundary … bias lower" vs §9 "mild bullish". | §8–§10, §21 | 3 |
| 4.4 Calibrated language | §17 is one sentence; confidence Medium stated. | §3, §17 | 4 |
| 4.5 Card construction (protocol) | Trade 1 correctly SUPPRESSED (|0.20| < 0.25). Trade 2: TP3 above TP2, "entry +0.2R" sign ambiguous for a short, confluences rest on wrong pivots. Trade 3C: no entry price (UNPRICED DUD), stop uses the wrong-side formula, U3 stop is not entry ± 0.2R, TP labels misdescribed. See feedback. | §21b | 1 |
| 5.1 Data dated; staleness flagged | Most items dated; MarketScreener 12 Jun flagged stale. Goldman item dated "Jun"; §13d dates are "Within 5d"; April CPI and 23 Jun TE snapshot not flagged stale/intraday. | §4, §13 | 2 |
| 5.2 Assumptions up front | Anchor override and lenient-corroboration directive are logged in §20 and the indicative-pivot caveat is on the cards. The 00:00 anchor override is not on any card. | §19–§21b | 3 |
| 5.3 Red flags surfaced | §12/§15 risks present. Past events presented as upcoming. D-day scheduled events (Ifo, US New Home Sales, EIA) are not carried into card caveats; no §13d collision caveat on cards. | §12, §13d, §15, §21b | 3 |
| 5.4 Restrictions honoured | An intraday CFD percentage was converted into a "close" and presented as sourced (breach of no-synthesised / no-CFD-in-basis), and §19 says the opposite. Every Open from 18 Jun equals the prior Close (chained, not sourced). No module codes, bracketed variable names or framework name found. | §6, §19 | 1 |

## 3. Category roll-up

| Cat | Max | Row mean | Level | Multiplier | Points | Justification |
|---|---|---|---|---|---|---|
| C1 Prompt adherence | 20 | 3.0 | 2 | 0.40 | 8.0 | Row mean 3 → 3, then reduced one level for the restriction breach (§5.4). 07:00 anchor overridden, stale/mis-dated coverage. |
| C2 Structure | 20 | 4.33 | 4 | 0.85 | 17.0 | All sections present and ordered. No "Final" column, extra pivot levels, chart headings without captions. |
| C3 Accuracy & evidence | 25 | 1.5 | 0 | 0.00 | 0.0 | Override: an impossible source timestamp and a derived percentage presented as corroborated closes. Without the override it would be 1: D-1 close −75.5 pts, RSI2 55.1 vs 100.0, 4 of 5 sessions out of tolerance, all weekly/monthly pivots out by 20–275 pts. |
| C4 Reasoning & judgment | 20 | 3.2 | 3 | 0.65 | 13.0 | Sound pillar structure and cross-asset mechanism, offset by card defects and unreconciled direction conflicts. |
| C5 Currency & transparency | 15 | 2.25 | 2 | 0.40 | 6.0 | Past events listed as upcoming, undated items, a synthesised price presented as sourced. |

## 4. Total, band, override
- Total = 8.0 + 17.0 + 0.0 + 13.0 + 6.0 = **44** → **Low Trust (40–59)**.
- Override check: `hallucinated_source` applies (cap 40–59, C3 = 0), on the Yahoo 16:24 "close", the TE-derived 23 Jun close attributed to Investing/Yahoo, and uncorroborated "Close corrob." labels on 17–19 Jun. A restriction breach (synthesised/CFD-derived price presented as sourced) also holds independently, so C1 was reduced one level. The 59 cap is not binding at 44. Without the C3 override the total would be 49 (still Low).

## 5. Card Integrity (linter rows copied verbatim from `lint_static/2026-06-24.csv`)

| card_id | strategy | flags | dud | Card score |
|---|---|---|---|---|
| 2026-06-24_Trade_1 | Trade 1 - Daily Directional | SUPPRESSED | False | suppressed, excluded |
| 2026-06-24_Trade_2 | Trade 2 - Pivot (TRANSITION, breakout side only) | WARN_TP3_ORDER | False | 100 − 10 = 90 |
| 2026-06-24_Trade_3C | Trade 3 - Momentum-Breakout (3C, TRANSITION) | UNPRICED | True | 100 − 40 = 60 |

Report-level Card Integrity = mean(90, 60) = **75.0** · n_cards = 3 (2 scored) · n_duds = 1 · n_warns = 1.
