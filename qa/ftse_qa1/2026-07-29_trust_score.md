# Trust Score v3.7 — FTSE 100 Daily Report, D = 2026-07-29 (run ftse_qa1)

Report: `reports/md/ftse_report_29Jul2026.md`
Level file: `data/levels/UK100_by_date/2026-07-29.csv` (`last_bar_date` = 2026-07-28 < D, leak check passed; n_prior_sessions = 81).
Slice stats: `engine/qa_slice_stats.py --cash-open 10:00 --cash-close 18:30`. The slice's last bar is 2026-07-28 22:45.

## Headline

```
c1=3
c2=4
c3=2
c4=3
c5=3
total=63
band=Moderate
override=none
card_integrity=96.7
n_cards=3
n_duds=0
n_warns=1
```

The single driver of the score: the report treats **Fri 24 Jul as D-1**. The true D-1 is **Tue 28 Jul**. The 27 and 28 Jul sessions are missing from the report entirely, so every number that anchors the cards is two sessions stale. Examples: close 10,736.23 against 10,874.0 on the cash basis, and daily pivots about 150 pts low. The report's own §4 and §13a carry 28 Jul evidence that it excluded.

## 1. Category 3 data check (report vs level file / slice)

Basis claimed by the report: London cash index, so I compare against the `_cash` fields. Tolerances from brief §4: close ≤5, O/H/L ≤10.

### 1a. Stated D-1 (as the report defines it, 24 Jul) against the true D-1 (28 Jul)

| Field | Report (§1/§3/§4/§6/§21b) | True D-1 cash (28 Jul) | Δ | True D-1 full-day | Verdict |
|---|---|---|---|---|---|
| Open | 10,638.86 | 10,795.7 | −156.8 | 10,787.0 | FAIL |
| High | 10,738.83 | 10,878.7 | −139.9 | 10,911.4 | FAIL |
| Low | 10,599.10 | 10,762.8 | −163.7 | 10,752.5 | FAIL |
| Close | 10,736.23 | 10,874.0 | **−137.8** | 10,893.2 | FAIL (>15) |
| RSI2 | 55.5 | 100.0 | −44.5 | 100.0 | FAIL |
| ATR14 | not stated numerically in any section (implied about 106.3 from the 3-ATR cap 11,055 and the 3C trigger) | 109.69 cash / 138.58 full | n/a | | Missing, see 3.3 |

### 1b. The report's five sessions against the slice's cash sessions for the same dates

The first three columns give the report value, the cash-slice value and Δ (report minus slice). A Δ outside tolerance is marked ✗.

| Date | Open | High | Low | Close | RSI2 (report / slice cash) |
|---|---|---|---|---|---|
| Mon 20 Jul | 10,600.27 / 10,540.1 / **+60.2 ✗** | 10,600.27 / 10,589.4 / +10.9 ✗ | 10,523.89 / 10,503.1 / +20.8 ✗ | 10,544.60 / 10,534.7 / +9.9 ✗ | 20.5 / 46.0 (not testable from the report's own closes) |
| Tue 21 Jul | 10,544.60 / 10,479.3 / **+65.3 ✗** | 10,612.40* / 10,574.2 / +38.2 ✗ | 10,510.20* / 10,470.1 / +40.1 ✗ | 10,585.30 / 10,571.7 / +13.6 ✗ | 42.2 / 48.9 (not testable) |
| Wed 22 Jul | 10,585.30 / 10,587.0 / −1.7 ✓ | 10,730.10* / 10,758.9 / −28.8 ✗ | 10,580.00* / 10,557.2 / +22.8 ✗ | 10,716.97 / 10,714.6 / +2.4 ✓ | 100.0 / 100.0 |
| Thu 23 Jul | 10,716.97 / 10,704.0 / +13.0 ✗ | 10,740.50 / 10,709.8 / +30.7 ✗ | 10,611.30 / 10,597.3 / +14.0 ✗ | 10,639.17 / 10,618.1 / **+21.1 ✗ (>15)** | 62.9 / 59.7 |
| Fri 24 Jul | 10,638.86 / 10,582.2 / **+56.7 ✗** | 10,738.83 / 10,728.2 / +10.6 ✗ | 10,599.10 / 10,580.9 / +18.2 ✗ | 10,736.23 / 10,728.0 / +8.2 ✗ | 55.5 / 53.2 |

- Only 2 of 20 O/H/L/C fields are inside tolerance.
- One close (Thu 23 Jul) is off by more than 15 pts, which is a Category 3 failure under brief §4.
- Report values sit systematically +10 to +20 above the cash slice on closes, more than a "few points" basis gap.
- **Open = previous close.** On 21, 22 and 23 Jul the Open equals the prior day's Close to the cent: 10,544.60, 10,585.30 and 10,716.97. Src B is "—" on 21 and 22 Jul, yet only H/L are asterisked. This looks like a synthesised open presented as a sourced field. I record it as a concern (5.4, 5.1) and do not treat it as proven fabrication.
- **RSI2 arithmetic.** Recomputed from the report's own closes (`--closes`), the last three rows reproduce exactly: 100.0 / 62.9 / 55.5. The first two cannot be tested because the report gives no earlier closes. The arithmetic itself is sound but never shown.
- **Trend labels** (Close vs Open and RSI2 vs 50) are applied correctly on all five rows.

### 1c. Pivots

| Set | Report | Level file (cash) | Level file (full) | Δ / note |
|---|---|---|---|---|
| Daily P | 10,691.39 | 10,838.5 | 10,852.37 | −147.1 / −161.0. Internally correct arithmetic from 24 Jul H/L/C, but the wrong session. |
| Daily R1 / S1 | 10,783.67 / 10,643.94 | 10,914.2 / 10,798.3 | 10,952.23 / 10,793.33 | −130.5 / −154.4 (cash) |
| Daily R2 / S2 | 10,831.12 / 10,551.66 | 10,954.4 / 10,722.6 | 11,011.27 / 10,693.47 | −123.3 / −171.0 (cash) |
| Daily R3 / S3 | 10,923.40 / 10,504.21 | 11,030.1 / 10,682.4 | 11,111.13 / 10,634.43 | −106.7 / −178.2 (cash) |
| Weekly P (W30 = 20–24 Jul, correct period) | 10,632.38 | 10,652.33 | 10,635.67 | −19.95 cash / −3.3 full |
| Weekly R1 / S1 | 10,867.29 / 10,501.33 | 10,834.57 / 10,545.77 | 10,837.53 / 10,512.43 | +32.7 / −44.4 (cash); +29.8 / −11.1 (full) |
| Weekly R2 / S2 | 10,998.34 / 10,266.42 | 10,941.13 / 10,363.53 | 10,960.77 / 10,310.57 | +57.2 / −97.1 (cash); +37.6 / −44.2 (full) |
| Weekly R3 / S3 | 11,233.25 / 10,135.37 | 11,123.37 / 10,256.97 | 11,162.63 / 10,187.33 | +109.9 / −121.6 (cash); +70.6 / −52.0 (full) |
| Monthly P (June) | 10,345.90 | 10,412.17 | 10,413.73 | −66.3 / −67.8 |
| Monthly R1 / S1 | 10,564.19 / 10,121.70 | 10,698.13 / 10,215.53 | 10,701.27 / 10,218.67 | −133.9 / −93.8 (cash) |
| Monthly R2 / S2 | 10,788.39 / 9,903.41 | 10,894.77 / 9,929.57 | 10,896.33 / 9,931.13 | −106.4 / −26.2 (cash) |
| Monthly R3 / S3 | 11,006.68 / **absent** | 11,180.73 / 9,732.93 | 11,183.87 / 9,736.07 | −174.1; S3 missing from the report |

- **Weekly construction error.** Back-solving the report's weekly table from P and R1 gives H = 10,763.44 and L = 10,397.47. That is the 25-session range, not the prior week's H/L. From the report's own §6 table the week's H/L/C is 10,740.50 / 10,510.20 / 10,736.23, giving P = 10,662.31, R1 = 10,814.42 and S1 = 10,584.12. So the weekly table does not reconcile with the report's own §6.
- **Monthly construction error.** Back-solving the report's June table gives L about 10,127.6 (level file about 10,126.2, which agrees), H about 10,570.1 (level file about 10,608.8, so 38.7 low) and C about 10,340.0 (level file about 10,506.2, so about 166 low).
- **Layout.** §11 breaches the brief's three-levels-per-side layout, carries daily R4/R5/S4/S5 and weekly R5, and the monthly table lacks S3.

### 1d. Other level-file comparisons

- **25-session range.** The report gives 10,397.48 – 10,763.44. It was acceptable for its own date: the cash high through 24 Jul was 10,758.9 (Δ +4.5) and the low 10,380.4 (Δ +17.1, outside the ±10 tolerance). At D-1 the cash 25-day range is **10,380.4 – 10,878.7** (full: 10,373.6 – 10,911.4). The report's "range top 10,763.44" is 115.3 below the true D-1 range top.
- **5-day swing low.** The report uses 10,510.20 (an asterisked, single-source, "not for stop pricing" value from 21 Jul). The level-file value is 10,557.2 cash (22 Jul).
- **ATR cross-check inside the cards.**
  - T1's 0.25-ATR buffer is 62.3 pts (10,572.50 − 10,510.20), which implies ATR about 249.
  - The same card's 3-ATR cap (11,055 − 10,736.23 = 318.8) implies about 106.3.
  - T3C's 0.25-ATR trigger offset (10,790.04 − 10,763.44 = 26.6) also implies about 106.4.
  - Level file: 109.69 cash.
  - T1's stop therefore cannot be reproduced from its own stated formula (0.25 × 106.3 = 26.6 → 10,536.8, not 10,572.50).
- **Counters** (broker feeds in the slices, 20→24 Jul, which is the report's own window):

| Counter | Report | Slice, 20→24 Jul | Slice, 22→28 Jul |
|---|---|---|---|
| US500 | "Rising / Confirms" | 7,444.3 → 7,408.8 (−0.5%) | 7,506.5 → 7,435.6 (−0.9%) |
| USDX | "Flat / mixed, unresolved ~99.4 vs 101.5" | 100.968 → 101.467 (+0.5%) | 101.102 → 101.421 (+0.3%) |

  - The USDX level in the slice (101.42 at 28 Jul) supports the report's "101.5" figure and not "99.4".
  - VIX closed 18.20 on 28 Jul (18.31 on 24 Jul). The report does not use VIX, so this is not a defect.
- **Calendar for D** (news slice, broker time = UK + 2h):
  - Fed rate decision, 21:00 broker = **19:00 UK on D** (HIGH).
  - FOMC press conference, 21:30 broker = 19:30 UK on D (HIGH).
  - EIA crude stocks, 17:30 broker = 15:30 UK on D (HIGH).
  - The only BoE rows on D are LOW-impact credit/mortgage data at 09:30 UK.
  - The report's "Bank of England policy signals… Wk of 28 Jul, High" and "BoE meeting in the coming week" have no support in D's calendar rows, and the Fed event is undated ("coming week") although it falls on D.
  - Items the report states that do check out against the slice: UK CPI 2.6% y/y (22 Jul), retail sales +1.0% m/m (24 Jul), composite PMI 52.1 (24 Jul).

## 2. Section 7 checklist

| # | Item | Reviewer notes | Evidence (location) | Score |
|---|---|---|---|---|
| 1.1 | Variables respected | Respected: asset = FTSE 100 cash (futures not used, CFD excluded), counters USDX / S&P 500 / DAX 40 (+ Euro Stoxx 50 reference), GBP / index points, Europe/London, 5-session and 25-session lookbacks (in form). Not respected: (i) as-of London close of **D-1** is wrong (24 Jul, not 28 Jul); (ii) the ≥6 sources from index provider / exchange / sell-side tiers are not met, since the sources are Investing.com, Yahoo, BBN, AJ Bell, Trading Economics, aggregators and media, with no index provider or exchange; (iii) the Trade 1 anchor clock time (07:00 UK) is never stated ("European pre-open reference"). Three Variables not respected caps the row at 3. | §1, §2, §3, §4, §20, §21b | 3 |
| 1.2 | Coverage & currency consistent | Currency is consistently GBP / pts. The coverage window is wrong: the data window ends 24 Jul although 27 and 28 Jul are completed sessions before D. §12/§13a nonetheless use 28 Jul news (Unilever, Barclays, TE "closes 0.93% higher") against a 24 Jul price anchor, so the window is internally mixed. §1 "net +136" is Mon open → Fri close; close-to-close Mon→Fri is +191.6. | §1, §6, §12, §13a, §19 | 2 |
| 1.3 | Audience & tone | Professional equity-strategist register throughout; no retail tone. The DATA-INTEGRITY NOTICE exposes prompt-instruction meta ("explicit instruction to proceed leniently"), a minor register slip. | §1, §18, header | 4 |
| 2.1 | Sections present & ordered | §1–§21 all present and in order, including §13a–d and §21a–d. Charts appear as captions only (accepted per brief; pandoc drops images). §17 is one sentence. | headings | 5 |
| 2.2 | Scorecard as a table | §6 is a table, but there is no "Final" column (brief requires Date/O/H/L/C/RSI2/Trend/Src A/Src B/Final/Validation). §11 pivot tables are side-by-side two-column layouts, not an ordered R3→P→S3 ladder. Daily has R4/R5/S4/S5 and R1.5 (beyond 3 levels per side); weekly has R5 but no R4/S4; **monthly has no S3**. | §6, §11 | 3 |
| 2.3 | Method steps visible | §8 candle-by-candle plus a sequence call is good. §9 gives overlap 0.70 and VOLator slope +0.06, but persistence is only "positive but not decisive" and the Kaufman efficiency ratio has no number. §5 claims a "weighted-median" with no weights or arithmetic shown, and the consensus is a single carried-forward close rather than a build across observations. | §5, §8, §9 | 3 |
| 3.1 | Quantitative claims sourced | Price and news items carry sources in §4/§13a. Unsourced inline: DAX +1.36%, Euro Stoxx +1.14%, Brent ">$100" and "low-$90s", gold ~4,070 / ~4,350, BoE 3.75%, UK CPI 2.6%, Barclays "5–6%", £1bn buyback, "five-month high", "February record near 10,935". Unilever is given as "+5–8%" in §12 against "5.5%" in the §13a quote. | §1, §10, §12, §14 | 3 |
| 3.2 | Spot-checked citations exist / contain data | Spot-checks: (a) Investing × Yahoo 24-Jul close 10,736.23 is used consistently in §1/3/4/6/21b, and the −0.73% / +0.91% / −77.8 / +97 arithmetic all reconcile. (b) **Trading Economics (CFD)** is shown with raw quote 10,736.23, identical to the "cash" providers, yet excluded as a CFD feed that "diverges by ~290 points"; self-contradictory. The slice's CFD closes for 24 Jul are 10,714–10,728, nowhere near a 290-pt gap. (c) TE 28-Jul article "gained 99 points or 0.93%": the 99 pts / 0.93% pair implies a base of about 10,645, inconsistent with a roughly 10,775 prior close (99/10,775 = 0.92%). In addition, the AJ Bell row is undated ("intraday ref") and eToro is classed "Institutional" (weight 1.0) though it is a retail broker. I found no source that is impossible or fabricated on its face, so the override is not triggered, but the evidence is soft. | §4, §13a, §13b | 3 |
| 3.3 | Calculations transparent | Reproducible: RSI2 from the report's own closes (last three rows exact); daily pivots from 24 Jul H/L/C; the §21a contributions sum to +0.709. Not transparent: RSI2 workings not shown; **ATR(14) and the Kaufman value are never stated numerically** (brief requires both) and the implied ATRs are inconsistent (249 vs 106); the weekly pivots use the wrong H/L (the 25-session range); the sentiment tilt computes to +0.595 (2.2/3.7) and is then "tempered to +0.46" by an unexplained haircut; the consensus weighted-median shows no weights. | §6, §9, §11, §13b, §21b | 2 |
| 3.4 | Numbers reconcile | Internally the close 10,736.23 is identical in §1/3/4/6/21b, and the card pivots equal the §11 pivots. But (i) against the data the D-1 is wrong, with closes off by 137.8 (D-1) and 21.1 (23 Jul), see §1; (ii) the weekly pivots do not reconcile with the report's own §6 H/L; (iii) the ATR is not reconcilable; (iv) the T1 TP3 cap (11,055) sits below TP2 (11,063.69); (v) §21d "mean R +0.02 on closed positions" is wrong: the closed trades (20, 22, 23 Jul) average −0.27R and +0.02 only appears if the open marks are included; (vi) §21c per-session R values are inconsistent (implied R ≈ 69.6 on 20 Jul, 131.7 on 22 Jul, 77.8 on 23 Jul vs the live card R 163.7). | §6, §11, §21b–d | 1 |
| 4.1 | Pillars conclude | §8 ("Indecision — resolving bullish"), §9 (Transitional, upward lean), §10 (aggregate CONFIRM), §12 (per-driver net labels) and §14 (per-bullet labels) conclude coherently. §14 lacks an overall direction label. The §10 "S&P 500 Rising / Confirms" conclusion is contradicted by the slice (see 1d). | §8–§10, §12, §14 | 4 |
| 4.2 | Cross-asset interpreted | Mechanisms are given: USD translation of FTSE earnings, Wall Street beta, DAX / Euro Stoxx regional beta, oil's energy weight vs inflation relief. Weakened because the S&P direction is mislabelled and USDX is parked as "neutral" on a feed conflict that the slice resolves (about 101.4). | §10, §12 | 3 |
| 4.3 | Synthesis reconciles tensions | Kaufman-vs-regime and short- vs medium-term tensions are explicitly handled. But the larger tension is ignored: §4 lists 28 Jul prices of 10,791 / 10,801 / 10,876 and §13a cites a 28 Jul close, all above the 3C trigger (10,790.04) and range top (10,763.44) that §21b says are "not yet met". The synthesis (§15/§16/§18) never reconciles its own 28 Jul evidence with a 24 Jul anchor. | §4, §13a, §15–§18, §21b | 2 |
| 4.4 | Calibrated language | §17 is one sentence with a single risk clause; confidence is "Medium" in §3 / §18 with a stated reason; no hedge stacking. The Medium confidence rests on a two-session-stale anchor, and §21d states a mean R on "closed positions" that is not what was computed. | §3, §17, §21d | 4 |
| 4.5 | Card construction (protocol: scored under Category 4) | Linter: 1 WARN, 0 DUD, so the static score is high. Beyond static checks: T1 market entry ≠ D-1 close and its stop rests on an asterisked "not for stop pricing" low; T2 is live although the report itself says every pivot tier is single-source-indicative (M5 requires suppression), and its buy-stop is below the D-1 close 10,874.0; T3C uses a stale 25-session range and mislabels its trigger "not yet met". The cards carry TP points inconsistently and omit the FOMC and EIA collisions. See feedback. | §21b | 2 |
| 5.1 | Data dated; staleness flagged | Most prices and articles are dated, and the stale anchor is openly disclosed. Problems: the AJ Bell row is undated; §13d uses "Wk of 28 Jul" / "Ongoing" instead of dates; Open fields on single-source rows are not flagged; the report never recognises that 27–28 Jul data exists in its own evidence table. | §4, §6, §13d, §19 | 3 |
| 5.2 | Assumptions up front | The header DATA-INTEGRITY NOTICE and the T1 caveat ("anchored to last corroborated close, not a reconciled 29-Jul open") state the stale-anchor and indicative-pivot assumptions up front; the override is in §20. The 07:00 UK anchor time is not stated; the notice also invokes an unspecified "lenient" instruction. | header, §19, §20, §21b | 4 |
| 5.3 | Red flags surfaced | Cross-feed conflict and indicative pivots are surfaced well (§12, §15, §19). Under-surfaced: the D-day Fed decision (19:00 UK) is undated and not carried into any card caveat; EIA stocks (15:30 UK) are absent; the invalid "BoE meeting" item is flagged High; the 28 Jul evidence that contradicts the "not yet met" status is not elevated. | §12, §13d, §15, §21b | 3 |
| 5.4 | Restrictions honoured | CFD/retail quotes are explicitly excluded from the OHLC basis; no module codes (M1–M5), no framework name, no bracketed variable names; futures not used. Concerns: the Open = prior Close pattern on three rows (possible synthesised values presented as sourced; single-source Opens unflagged); TE "CFD" and eToro retail used in evidence and weighting; Trade 2 produced despite the M5 suppression condition the report itself triggers. None openly violates a prompt-stated restriction, so no override. | whole report | 3 |

## 3. Category roll-up

| Category | Max | Row mean | Level | Multiplier | Points | Justification |
|---|---|---|---|---|---|---|
| 1 Prompt adherence | 20 | (3+2+4)/3 = 3.00 | **3** | 0.65 | 13.00 | Asset / counters / currency respected; D-1 as-of date wrong, source tiers unmet, anchor time unstated. |
| 2 Structure | 20 | (5+3+3)/3 = 3.67 | **4** | 0.85 | 17.00 | All 21 sections present and ordered; scorecard and pivot tables defective; method not fully numeric. |
| 3 Accuracy & evidence | 25 | (3+3+2+1)/4 = 2.25 | **2** | 0.40 | 10.00 | Wrong D-1 (close −137.8 pts), 18 of 20 OHLC fields outside tolerance, weekly / monthly pivots mis-built, ATR / KER absent, internal inconsistencies. |
| 4 Reasoning & judgment | 20 | (4+3+2+4+2)/5 = 3.00 | **3** | 0.65 | 13.00 | Mechanisms and regime logic are coherent, but the synthesis ignores its own 28 Jul evidence and the card construction is weak. |
| 5 Currency & transparency | 15 | (3+4+3+3)/4 = 3.25 | **3** | 0.65 | 9.75 | Stale anchor honestly disclosed; undated items, buried collisions, possible synthesised opens. |

## 4. Total, band, override

- Total = 13.00 + 17.00 + 10.00 + 13.00 + 9.75 = 62.75, rounded to **63**. Band: **Moderate Trust (60–74)**.
- Override check: `none`.
  - Hallucinated source: no source is impossible on its face, so there was no basis to set C3 = 0. The soft points are logged under 3.2 (TE "CFD" listing with the identical cash quote, undated AJ Bell, eToro classed as Institutional).
  - Restriction breach: no prompt-stated restriction was openly violated. The synthesised-open and M5-suppression concerns are logged under 5.4 and 4.5.

## 5. Card Integrity (linter rows copied verbatim from `qa/ftse_qa1/lint_static/2026-07-29.csv`; SEPARATE from the 100)

| card_id | report_date | strategy | flags | dud | Card score (100 − 40·DUD − 10·WARN) |
|---|---|---|---|---|---|
| 2026-07-29_Trade_1 | 2026-07-29 | Trade 1 — Daily Directional (LONG · TRANSITION-with-upward-lean) | WARN_TP3_ORDER | False | 90 |
| 2026-07-29_Trade_2 | 2026-07-29 | Trade 2 — Pivot, breakout-side (upside), regime = TRANSITION | CLEAN | False | 100 |
| 2026-07-29_Trade_3C | 2026-07-29 | Trade 3 — Momentum-Breakout (variant 3C), post-indecision at the 25-session range top | CLEAN | False | 100 |

- No cards are suppressed, so n_cards = 3.
- Report-level Card Integrity = (90 + 100 + 100)/3 = **96.7**.
- n_duds = 0, n_warns = 1.
- The linter runs in static mode on the report's own numbers, so CLEAN does not mean the levels are right against D-1 (see feedback).

## Process note

My first shell call included `ls` on `cards/regenerated`, which printed three subfolder names. I did not open any of them. All other reads were limited to the paths named in `SESSION_TASK.md`. The forbidden `results/`, `data/raw/` and `data/levels/*_levels.csv` were absent as expected. I do not know what price did on or after D, and nothing above speculates about it.
