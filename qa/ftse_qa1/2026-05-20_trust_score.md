# Trust Score v3.7 — FTSE 100 Daily Report, 20 May 2026 (run ftse_qa1)

Report: `reports/md/FTSE100_Report_Daily_20-May-2026.md` · D = 2026-05-20 · D-1 = Tue 19 May 2026
Leak check: level file `last_bar_date` = 2026-05-19 < D (pass). Slice last bar 2026-05-19 22:45 broker (pass).
Basis claimed by the report: LSE regular session (08:00-16:30 London), i.e. the `_cash` fields (cash window 10:00-18:30 broker). All Category 3 comparisons below use `_cash`; `_full` shown where useful.

## Score line (machine-readable)
```
c1=2
c2=3
c3=0
c4=2
c5=2
total=35
band=Very Low
override=hallucinated_source
card_integrity=100
n_cards=3
n_duds=0
n_warns=0
```
Override note: `override=` holds one value. Two override conditions were found. (a) hallucinated_source: self-contradictory / mis-dated citations (see 3.2), so cap at Low and C3 = 0. (b) restriction_breach: module codes, a framework-internal weight naming and a "Strategies Module" reference appear in the report text (see 5.4), so C1 is reduced by one level (3 to 2). Both effects are applied in the numbers above.

## 1. Section 7 checklist

### Category 1 — Prompt adherence (M1 Variables)
| Row | Reviewer notes | Evidence (location) | Score |
|---|---|---|---|
| 1.1 Variables respected | FTSE 100 cash index primary, Euro Stoxx 50 reference only (no cards): ok. Counters USDX / S&P 500 / DAX 40 stated in §2 and used in §10 (Brent and VIX added in §10/§14, acceptable). Lookback 5 sessions ok. Anchor 07:00 UK on Trade 1 ok. Source requirement (>= 6 from index-provider / exchange / sell-side tiers) is weak: the OHLC rests on aggregators (Yahoo, Trading Economics, Investing.com) plus Fidelity/Sharecast; no FTSE Russell, LSE or sell-side OHLC source is used for the validated table. S&P 500 "latest" is Mon 18 May, not the D-1 (Tue 19 May) close. | §2, §4, §6, §10, §20 | 3 |
| 1.2 Coverage and currency consistent | Currency/units consistent (GBP index points). As-of drift: (i) daily pivots in §11 are built from Mon 18 May H/L/C, not D-1 (Tue 19 May); (ii) §10 S&P close labelled "Mon close" 7,353.61; (iii) calendar dates wrong: "Mon 26 May UK bank holiday" (the holiday is Mon 25 May; 26 May is a Tuesday), Trade 1 "Wed 26 May 16:30", Trade 2 "Mon 26 May", §12 "23 May (Fri AM)" (23 May is a Saturday; the report's own §13d says Fri 22 May), §12 "21 May (Wed evening US time)" (21 May is Thursday; FOMC minutes are 20 May). | §11, §10, §12, §13d, §21b | 2 |
| 1.3 Audience and tone | Strategist register and risk-review tone broadly maintained. Minor colloquialism ("one swallow doesn't make a summer", §15). | §1, §15, §18 | 4 |
Category 1 mean = 3.00 (level 3). After restriction-breach adjustment (5.4): **level 2**.

### Category 2 — Structural alignment (M4 §1-§21)
| Row | Reviewer notes | Evidence | Score |
|---|---|---|---|
| 2.1 Sections present and ordered | §1-§21 all present and in order, §21a/b/c/d present, §17 present. Deviation: §13 sub-labels do not follow the brief (13c is a "Sentiment / Price Divergence Flag", and the previous-period and upcoming calendars are merged under 13d "Two-Part News Calendar" instead of 13c / 13d). §7 charts: images dropped by conversion; five captions/placeholders (7.1-7.5) accepted as evidence (noted). | headings §7, §13 | 4 |
| 2.2 Scorecard as a table | §6 is a table with all required columns (Date/O/H/L/C/RSI2/Trend/Source A/Source B/Validation; Final column is not present as a separate column). §11 daily and weekly pivots R3 to S3 ordered. Monthly pivot table has **no R3** (R2, R1, P, S1, S2, S3: three levels on the support side, two on the resistance side). | §6, §11 | 3 |
| 2.3 Method steps visible | §4 observations then §5 consensus is shown, but the close is called "synthesised"/"weighted median" with no arithmetic shown; the median of the four listed readings cannot be reproduced to 10,341.05. §8 candle-by-candle and sequence present. §9 regime shows KER, VOLator slope and ATR, but KER window/EMA parameters are not stated, and no persistence/overlap metrics are shown. | §5, §8, §9 | 3 |
Category 2 mean = 3.33 (**level 3**).

### Category 3 — Accuracy and evidence (M2)
**Data comparison vs level file (cash basis; tolerance close <= 5, O/H/L <= 10, pivots judged at <= 10).**

D-1 (Tue 19 May):
| Field | Report (§1/§3/§6/§21b) | Slice cash | Delta | Verdict |
|---|---|---|---|---|
| Open | 10,303.50 | 10,339.9 | -36.4 | discrepancy |
| High | 10,360.51 | 10,408.9 | -48.4 | discrepancy |
| Low | 10,266.14 | 10,313.0 | -46.9 | discrepancy |
| Close | 10,341.05 | 10,325.1 | +15.95 | **fails (> 15)** |
| RSI2 | 93.3 | 100.00 (full-day basis 72.80) | -6.7 | discrepancy |
| ATR(14) | 108.68 (§9) | 148.94 (full-day 163.35) | -40.26 (-27%) | **fails** |

Earlier sessions in §6 (cash basis):
| Session | Report O / H / L / C | Slice cash O / H / L / C | Delta O / H / L / C |
|---|---|---|---|
| Wed 13 May | 10,248.20 / 10,282.40 / 10,160.80 / 10,212.30 | 10,314.9 / 10,357.0 / 10,234.8 / 10,293.6 | -66.7 / -74.6 / -74.0 / -81.3 |
| Thu 14 May | 10,210.50 / 10,245.70 / 10,152.05 / 10,173.40 | 10,319.3 / 10,371.1 / 10,301.1 / 10,355.8 | -108.8 / -125.4 / -149.1 / -182.4 |
| Fri 15 May | 10,180.30 / 10,215.80 / 10,145.60 / 10,195.20 | 10,299.0 / 10,309.4 / 10,154.9 / 10,167.0 | -118.7 / -93.6 / -9.3 (ok) / +28.2 |
| Mon 18 May | 10,198.40 / 10,334.20 / 10,186.30 / 10,299.45 | 10,144.5 / 10,336.3 / 10,141.2 / 10,290.8 | +53.9 / -2.1 (ok) / +45.1 / +8.65 |
Of the 20 report O/H/L/C values for FTSE across the five sessions (the four tabulated sessions plus Tue 19 May above), only 2 are within tolerance (Fri 15 May low -9.3, Mon 18 May high -2.1); 18 are outside (Mon 18 May close +8.65 also fails the 5-pt close tolerance). The full-day basis (`_full`) does not rescue them: e.g. 14 May full close 10,352.0 vs report 10,173.40. Consequences: the report's candle narrative (three-down / two-up, Friday doji, "Wed 13 May sell-off 10,331 to 10,212", "Thu 14 May -39 pts") does not match the slice, in which 13 and 14 May closed above their opens and above the prior close, and 15 May was a -132 pt body (open 10,299.0, close 10,167.0). Report Trend labels for 13 and 14 May (Bearish) would be Bullish under the Trend rule on slice data (Close > Open and RSI2 > 50); 15 May Neutral would be Bearish (Close < Open and RSI2 24.78 < 50).

RSI2 arithmetic from the report's own closes (brief §4 formula, mean gain / mean loss over 2 periods): 15 May 35.9 (report 44.0), 18 May 100.0 (report 89.1), 19 May 100.0 (report 93.3). The report states "Wilder smoothing"; the published figures are reproducible only under Wilder smoothing from an unshown seed, which is not the fixed definition. Slice cash RSI2 for the last five sessions: 75.65, 100.00, 24.78, 39.60, 100.00 versus report 5.2, 1.7, 44.0, 89.1, 93.3.

Pivots (cash basis claimed):
| Level set | Report | Level file (`_cash`) | Delta | Verdict |
|---|---|---|---|---|
| Daily P | 10,273.3 | 10,349.0 | -75.7 | fails; built from Mon 18 May H/L/C instead of D-1 |
| Daily R1 / S1 | 10,360.3 / 10,212.4 | 10,385.0 / 10,289.1 | -24.7 / -76.7 | fails |
| Daily R2 / S2 | 10,421.2 / 10,125.4 | 10,444.9 / 10,253.1 | -23.7 / -127.7 | fails |
| Daily R3 / S3 | 10,508.2 / 10,064.5 | 10,480.9 / 10,193.2 | +27.3 / -128.7 | fails |
| Weekly P | 10,207.7 | 10,228.0 | -20.3 | fails |
| Weekly R1 / S1 | 10,269.9 / 10,133.1 | 10,310.1 / 10,084.9 | -40.2 / +48.2 | fails |
| Weekly R2 / S2 | 10,344.5 / 10,070.9 | 10,453.2 / 10,002.8 | -108.7 / +68.1 | fails |
| Weekly R3 / S3 | 10,406.7 / 9,996.3 | 10,535.3 / 9,859.7 | -128.6 / +136.6 | fails |
| Monthly P | 10,416.6 | 10,418.8 | -2.2 | ok |
| Monthly R1 / S1 | 10,631.0 / 10,149.5 | 10,650.0 / 10,140.1 | -19.0 / +9.4 | R1 fails, S1 ok |
| Monthly R2 / S2 | 10,898.1 / 9,935.0 | 10,928.7 / 9,908.9 | -30.6 / +26.1 | fail |
| Monthly R3 / S3 | missing / 9,667.9 | 11,159.9 / 9,630.2 | n/a / +37.7 | R3 omitted; S3 fails |
The pivot arithmetic is correct given the inputs the report chose (P, R1-R3, S1-S3 reproduce from 10,334.20 / 10,186.30 / 10,299.45 and from 10,282.40 / 10,145.60 / 10,195.20); the failure is input selection (stale session; weekly high 10,282.40 vs slice week high 10,371.1, weekly close 10,195.20 vs 10,167.0). The "strong confluence" weekly R2 / daily R1 pair at 10,344.5 / 10,360.3 does not exist on the level file: cash daily R1 is 10,385.0 and the nearest weekly level is R1 10,310.1 (74.9 pts away); the coincident pair on the level file is daily R2 10,444.9 and weekly R2 10,453.2 (8.3 pts apart).

Other levels: 25-session KER reported -0.25; slice cash 25-session KER = -0.138; KER(13) on EMA(3) of cash closes = +0.021 (sign differs, no parameters stated in the report). 25-day high/low cash 10,666.5 / 10,141.2 (full 10,698.0 / 10,107.0); report §9 gives 10,729.85 / 10,145.60, and the report itself gives the peak three ways (10,683 on "1 May" in §1, 24 April 10,683.65 in §19, 10,729.85 in §9). 5-day swing cash 10,408.9 / 10,141.2 (report cites 10,145.6 low and 10,360 high). Counters: USDX report ~99.06 vs D-1 close 99.337 (-0.28); S&P 500 7,353.61 labelled Mon vs 18 May close 7,405.2 and 19 May close 7,356.3; VIX ~18.6 vs 18.75 (ok).

| Row | Reviewer notes | Evidence | Score |
|---|---|---|---|
| 3.1 Quantitative claims sourced | §12 and §14 give sources in most paragraphs; §1 headline figures, §10 counter values (USDX ~99.06, DAX ~24,450, Brent ~$110.06) and §14 gilt/Brent/VIX figures carry no source or pointer. §6 asserts "CORROBORATED (Δ<0.1%)" for every session with named sources, yet only two of the 20 values match the slice and the "tolerance" is given as both 0.1% and "±0.10 points". | §1, §10, §14, §6 | 3 |
| 3.2 Citations exist and contain data | Three sources spot-checked. (1) ING THINK: URL slug "bank-of-england-cuts-rates-in-heavily-divided-decision" but the report dates it Apr 2026 and summarises it as "BoE hold more hawkish than expected", with a quote about "two cuts in the first half of 2026"; figure/summary contradict the source's own slug and date. (2) CNBC: URL path dated 2026/05/18 but listed as 19 May 2026 and summarising an S&P third straight loss; date does not match. (3) MoneySavingExpert: URL path /2026/04/ but listed as 6 May 2026, an event described as the BoE 30 April decision. In addition the Yahoo 11:55 BST quote 10,398.13 (§4) exceeds the report's own Tue session high 10,360.51 (§4/§6), an impossible reading, and the Yahoo 15:48 quote 10,326.42 is described as "+131.05 / +1.29%" from Friday's close, i.e. a change measured against the wrong reference day. Per brief §2 row 3.2, self-contradictory or mis-dated sources count as fabricated. The 19 May close 10,341.05 is admitted in §5/§19 to be synthesised/reconstructed yet is validated as "CORROBORATED". | §4, §5, §13a, §19 | 0 |
| 3.3 Calculations transparent | Pivot arithmetic transparent and correct. RSI2 not reproducible under the protocol formula (see above). ATR(14) stated but wrong by 40 pts (cash) and R-multiples on the cards are built on it. KER parameters not stated. §21a score cannot be reproduced: stated components sum to +0.103 (+0.088 +0.075 -0.060) plus sentiment +0.015 and VOLator +0.004 = +0.122; the headline +0.28 needs a medium-regime contribution of +0.158, i.e. a +0.79 signal at weight 0.20 on a RANGE_DOWN regime that the text calls only a "small" positive. §21d "mean +0.34R" and "8 of 15 triggered" do not reconcile with the §21c table (7 YES, 3 NO, 5 SUPPRESSED; positive R rows sum to +3.41 over 7 triggered, not +0.34 mean). | §6, §9, §21a, §21c, §21d | 1 |
| 3.4 Numbers reconcile | Breaks: (i) D-1 close 10,341.05 in §1/§3/§6 vs slice 10,325.1; (ii) Tue change given as +0.49% / +50 pts (§13a), +0.4% implied by §6 (+41.6) and "+42" (§13d); (iii) STOXX Tue +0.78% (§1/§13d) vs +0.57% / +0.1% (§4/§13a) vs +1.0% implied by §6 closes; (iv) peak date/value three versions; (v) daily pivots from 18 May while §1/§3 are as-of 19 May; (vi) Trade 1 entry 10,335 vs D-1 close 10,341.05; (vii) Trade 1 stop "102 points (107 pts)"; (viii) ATR quoted 108.68 while cards say R 102 = "1.0 x ATR". | cross-section | 1 |
Category 3 mean (pre-override) = 1.25 (level 1). **Hallucinated-source override: C3 = 0.**

### Category 4 — Reasoning and judgment (M3 + M5)
| Row | Reviewer notes | Evidence | Score |
|---|---|---|---|
| 4.1 Pillars conclude | §9 (Trending Down - Moderate), §10 (CONFIRM), §14 (Cautiously balanced), §15 (Bullish near-term / Balanced 5-day) conclude. §8 ends with a sequence label ("Continuation (reversal-direction)") but no clear direction statement; §12 has no direction label. | §8, §9, §10, §12, §14 | 3 |
| 4.2 Cross-asset interpreted | §10 gives mechanisms (dollar-earner translation, energy weight, US yields channel), not a correlation list. The S&P figure is a D-2 value and the USDX mechanism is stated without the counter-argument; adequate. | §10 | 4 |
| 4.3 Synthesis reconciles tensions | Regime labelled RANGE_DOWN (§1, §9), "transition-to-bullish" (§1), TRANSITION on Trade 2/3 cards; the card variants are chosen from the label that suits them. The report calls 10,344-10,360 a strong-confluence cap (§1, §11, §18) yet Trade 1 is a market LONG into it with TP1 above it, and the Kaufman -0.25 drag is not reconciled with the "+0.28" long score. §17 (range-bound, mild upside bias) vs §21a (LONG, above threshold) are asserted consistent, not reconciled. | §15-§18, §21a | 2 |
| 4.4 Calibrated language | §17 is one sentence. Confidence "High" in §3/§18 contradicts §19 admission that the D-1 OHLC is reconstructed and the monthly pivots are a calendar proxy. | §3, §17, §18, §19 | 2 |
| Card construction (M5) | Trade 1: stop is "daily P - 1/2 ATR, rounded" rather than nearest S/R + 0.25 x ATR; fixed +3R TP3 and a 26 May time-stop instead of the session-close time-stop / 3 x ATR cap; entry is a "reference 10,335 +/- 10", not the D-1 close. Trade 2: stop 10,289 contradicts its own text ("below daily P 10,273"); strong-confluence claims at entry and TP1 rest on stale pivots. Trade 3: labelled 3A under a TRANSITION regime (3C applies) or RANGE_DOWN (3B applies); entry at the 38.2% retrace rather than 57.5%; stop above rather than beyond the 0% anchor; TPs are 1R/2R/3R rather than 38.2% / 0% / 100%+ extension; swing magnitude 215 fails even the report's own 2 x ATR (217.4) test; fib arithmetic "10,277 - 0.618 x 215 = 10,227" is wrong (= 10,144). Trade 1 conviction (+0.28) not reproducible (3.3). Static linter is CLEAN, but static cleanliness does not establish construction compliance. | §21a, §21b | 1 |
Category 4 mean = 2.4 (**level 2**).

### Category 5 — Currency, restrictions and transparency (M2)
| Row | Reviewer notes | Evidence | Score |
|---|---|---|---|
| 5.1 Data dated; staleness flagged | Most rows dated. Staleness not flagged: Morningstar (Feb 2026) and ONS/Commons (Apr 2026) are given weight 1.0 in the tilt; S&P 500 is D-2. The reconstructed 19 May OHLC and calendar-proxy monthly pivots are disclosed only in §19 while §6 and §19's opening state "no single-source-indicative flags". | §4, §10, §13b, §19 | 2 |
| 5.2 Assumptions up front | Anchor-override caveat ("overridden as instructed") appears in §2 and on Trade 1, and the CPI collision is on every card. The calendar-proxy monthly pivot caveat is not propagated to the cards (Trade 2: "Pivot tiers all CORROBORATED - no single-source-indicative flag"); §20 does not record the anchor override. | §2, §20, §21b | 2 |
| 5.3 Red flags surfaced | §12/§15 carry yield, oil and CPI risk; the CPI-at-anchor collision is carried into all three cards. Not surfaced: UK labour-market data on D-1 (19 May: unemployment 5.0% vs 4.9% consensus, regular pay 3.4% vs 5.0%, claimant count 26.5 vs 10.9) is absent from the previous-period calendar; the 20 May BoE Governor Bailey speech (14:15 UK, HIGH), Dhingra/Mann speeches and EIA crude stocks are absent from the upcoming calendar; the UK CPI y/y calendar consensus is 3.8% (previous 3.4%), whereas the report states prior 3.3% and consensus 3.4-3.6%, and Eurozone CPI y/y consensus 1.9% (previous 1.9%) vs report "Flash 2.4%". | §12, §13d | 3 |
| 5.4 Restrictions honoured | Breaches: module codes and framework internals appear in the text: "M2 §9c" (§13b), "M5 §2" (§13c), "M3 regime classification" (§16), "Strategies Module" and the weight identifiers W_SHORT_TECH / W_MEDIUM_REGIME / W_VOLATOR / W_KAUFMAN / W_SENTIMENT / W_CROSS_ASSET (§20). A close described as "synthesised" is presented as a validated, corroborated price (§5, §6, §19). No retail CFD quotes stated; futures used as confirmation only (ok). | §5, §13b, §13c, §16, §20 | 1 |
Category 5 mean = 2.0 (**level 2**).

## 2. Category roll-up
| Cat | Level | Multiplier | Max | Points | Justification |
|---|---|---|---|---|---|
| 1 Prompt adherence | 2 | 0.40 | 20 | 8.0 | Variables mostly honoured (base 3); as-of and calendar-date drift; restriction breach lowers one level. |
| 2 Structure | 3 | 0.65 | 20 | 13.0 | All 21 sections present; monthly pivot table lacks R3; §13 sub-lettering deviates; consensus arithmetic not shown. |
| 3 Accuracy and evidence | 0 | 0.00 | 25 | 0.0 | Pre-override level 1: D-1 close +15.95 pts, ATR -27%, 18 of 20 OHLC values outside tolerance, pivots mostly stale or off. Override: mis-dated / self-contradictory citations set C3 = 0. |
| 4 Reasoning and judgment | 2 | 0.40 | 20 | 8.0 | Cross-asset mechanisms good; regime labels and conviction score not reconciled; card construction non-compliant on all three cards. |
| 5 Currency and transparency | 2 | 0.40 | 15 | 6.0 | CPI collision carried to cards; staleness/proxy caveats not propagated; module-code leakage; omitted 19-20 May events. |

## 3. Total, band, override
Total = 8.0 + 13.0 + 0.0 + 8.0 + 6.0 = **35** → **Very Low** (0-39).
Override check: hallucinated_source TRIGGERED (cap Low 40-59 not binding because the score is already 35; C3 = 0 applied). restriction_breach TRIGGERED (cap Moderate not binding; C1 reduced one level). Reported `override=hallucinated_source`.

## 4. Card Integrity (linter rows, copied verbatim from `lint_static/2026-05-20.csv`; separate from the 100)
| card_id | strategy | flags | dud | per-card score |
|---|---|---|---|---|
| 2026-05-20_Trade_1 | Trade 1 — Daily Directional, LONG | CLEAN | False | 100 |
| 2026-05-20_Trade_2 | Trade 2 — Pivot (regime-aware), TRANSITION regime → breakout-side branch | CLEAN | False | 100 |
| 2026-05-20_Trade_3A | Trade 3 — Momentum-Pullback (3A), TRANSITION regime | CLEAN | False | 100 |

Report-level Card Integrity = mean(100, 100, 100) = **100** · n_cards = 3 · n_duds = 0 · n_warns = 0. (Cards are static-clean; see Category 4 "Card construction" and the feedback file for construction defects the linter does not test.)
