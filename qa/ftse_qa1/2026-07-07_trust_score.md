# Trust Score v3.7 — FTSE 100 daily report, D = 2026-07-07 (run ftse_qa1)

Report: `reports/md/FTSE100_Report_2026-07-07.md`. Level file `data/levels/UK100_by_date/2026-07-07.csv` checked: `last_bar_date` = 2026-07-06 < D (leak-free). Reference basis for Category 3 = UK100 CFD, cash session 10:00-18:30 broker (08:00-16:30 London), via `engine/qa_slice_stats.py`; full-broker-day values shown where useful.

## Machine-readable result
```
c1=2
c2=4
c3=1
c4=2
c5=2
total=44
band=Low
override=restriction_breach
card_integrity=100
n_cards=3
n_duds=0
n_warns=0
```

## 1. Section 7 checklist

| Row | Score | Notes | Evidence |
|---|---|---|---|
| 1.1 Variables respected | 2 | Asset (FTSE 100 cash, GBP pts) and counters (USDX, S&P 500, DAX; STOXX reference only) correct. NOT respected: (a) as-of London close of D-1 = 6 Jul 2026, but the data window is 29 Jun-3 Jul and the 6 Jul session is absent from §4, §6, §11 and §21c; (b) fewer than 6 usable sources and no index-provider / exchange / sell-side tier (Investing, Yahoo, Trading Economics, Sharecast, TradingView; Stooq blocked; TradingView was only a search snippet per §20); (c) 07:00 UK anchor overridden to "market open" (disclosed). | §2 L18-19; §4; §20 L185, L189; §21b Trade 1 Entry |
| 1.2 Coverage & currency consistent | 2 | Header/§2/§20 say "as of 6 July close", §1 and §18 anchor on "3 July settlement". §1/§3/§5/§18 carry the 3-Jul close as consensus and a 6-Jul "intraday mark" (10,720-10,730 = the session-high area, 6 Jul cash high 10,726.7) in place of the D-1 close (cash 10,641.1 / full-day 10,660.9). Lookback is 29 Jun-3 Jul, not the 5 sessions ending D-1 (30 Jun-6 Jul). Currency/units consistent. | Header L3; §1; §2 L19; §3 |
| 1.3 Audience & tone | 4 | Strategist register, no retail tone. Minor: "per user instruction for this run" and "Stooq (network-blocked in environment)" are process leakage into a desk document. | §19 L182; §20 L185 |
| 2.1 Sections present & ordered | 5 | §1-§21 all present in order incl. §13a-d, §21a-d; §17 is one sentence. | headings |
| 2.2 Scorecard as a table | 3 | §6 is a proper table with all required columns. §11 gives ONLY the daily table; weekly and monthly pivot tables (R3→S3) are absent although §11 says they are "enabled" and §7 refers to a weekly pivot chart. | §6; §11 L95-107 |
| 2.3 Method steps visible | 4 | §4-§5 observation→consensus shown; §8 candle-by-candle + sequence; §9 regime with overlap/persistence/VOLator. §7 charts are text captions only (accepted per brief; noted). The method is applied to the wrong window and, in places, wrong numbers. | §4-§9 |
| 3.1 Quantitative claims sourced | 2 | Unsourced or un-pointed figures: record 10,934.94, BoE 3.75%, UK CPI 2.8% vs 3.3%, "~80% of FTSE revenue overseas", "+1.8% intraday", gold "elevated", ATR "≈90", VOLator readings ("+0.6", "+0.2"). The US-payrolls characterisation is contradicted by the calendar feed (see 3.4). | §1, §12, §14, §9, §21b |
| 3.2 Citations exist & contain data | 2 | Three checked: (i) Investing.com 3 Jul 10,679.03 (range 10,604.25-10,701.32, open 10,652.81) — figures consistent with §6 row 3 Jul and §11, but 3-Jul CFD cash close is 10,660.5 (Δ+18.5); (ii) Sharecast/Fidelity "3 Jul 14:08 UK, 10,658.16, pre-close, intraday" — the same 10,658 is then used in §6 as the 2-Jul CLOSE with Sharecast as Src A: one quote serving two different dates; (iii) TradingView listed as Src A/B for the 29 Jun-1 Jul OHLC rows although §20 says it was "search snippet" only, and those rows are labelled SINGLE-SRC while naming two sources. A source cited as supplying five days of OHLC that it could not supply is a content-claim failure. I cannot prove any URL is non-existent, so no hallucinated_source override is applied (see §3 below). | §4; §6 L47-51; §20 L185 |
| 3.3 Calculations transparent | 2 | RSI2 only shown as "~100" with no gains/losses; first two rows cannot be computed from a 5-close window anyway. Trend rule broken: Tue 30 Jun Close 10,548 > Open 10,537 with RSI2 ~100 ⇒ must be Bullish, report says Neutral. ATR(14) stated only in a card ("≈90"), not in §9; KER(13, EMA3) not stated numerically. Pivot arithmetic reproduces from the report's own 3-Jul H/L/C (P 10,661.5; R1 10,718.8; S1 10,621.7; R2 10,758.6; S2 10,564.5; R3 10,815.9; S3 10,524.7 — all within 1 pt of §11). §21a score reproduces: 0.25+0.20+0.15+0.05+0.045+0.045 = +0.74. | §6, §9, §11, §20 L188, §21a |
| 3.4 Numbers reconcile | 2 | Internally: D-1 "close" 10,679 in §1/§3/§4/§6/§18 but Trade 1 MARKET entry ≈10,720 (§21b) — a 41-pt break; backtest R-multiples inconsistent with card R (2-Jul +58 pts called +1.0R "TP1 hit" while card R = 116; 29-Jun +53 pts = +0.6R implies R≈88); Trade 3A "closed/mean R +0.9" vs §21c "PARTIAL". Pivots on cards = §11 pivots (OK). Vs data: see section 2 below (most numbers wrong). Calendar: report says NFP "weaker than expected"; feed shows 2-Jul NFP actual 57 vs consensus 43 (previous 172) — below prior but ABOVE consensus. | §1, §13c L134, §21b, §21c |
| 4.1 Pillars conclude | 3 | Each of §8, §9, §10, §12, §14 ends in a label (Bullish continuation / Trending Bullish / MIXED / supportive-neutral). Conclusions are reached, but several rest on facts the data contradicts (5 higher closes; near-maximal KER; S&P sell-off). | §8-§14 |
| 4.2 Peer/cross-asset interpreted | 2 | Mechanisms are given, but (a) USDX mechanism is sign-confused: a softer dollar is described as "mildly supportive" via "sterling-translated valuations" while §12/§14 simultaneously argue weaker sterling is the support; (b) the main "contradiction" (tech-led S&P sell-off, S&P VOLator +0.6 "spiking") is contradicted by the counters: US500 closed 7,440→7,546 over 29 Jun-6 Jul at new highs and VIX fell 18.0→16.9 (3 Jul 17.14, 6 Jul 16.89); (c) oil/Brent claimed "steady" with no counter. | §10; §9 L81; §7 L67 |
| 4.3 Synthesis reconciles tensions | 2 | §15/§16 carry the S&P and CPI risks forward, and §17 agrees with §21a. But the report's own tension — "overbought RSI2, don't chase, buy dips toward the pivot" (§9, §16) versus a Trade 1 MARKET long at ≈10,720 (at R1, the 6-Jul high) — is not reconciled; and the +0.045 cross-asset contribution on a MIXED read (one confirm, one contradict, two neutral) is not justified. | §9 L82; §16; §20 L188; §21b |
| 4.4 Calibrated language | 4 | §17 is one sentence; confidence Medium stated in §3/§18. Minor: "well above the conviction threshold", "authentic reflection" are assertive for single-source data. | §3, §17, §21a |
| 4.5 Card construction (protocol add-on) | 1 | Three cards, none constructed to M5: Trade 1 MARKET entry ≠ D-1 close, no wide-stop flag, stop unbuffered, ATR 90 vs 113.9/121.1, TP3 cap wrong; Trade 2 uses RANGE-style S1 limit under a TREND_UP label; Trade 3A uses 38.2% (not 57.5%) retrace, limit on wrong side of D-1 close, TP1/TP2 not the Fib levels, no TP3, swing endpoints not logged. Details in feedback. | §21b |
| 5.1 Data dated; staleness flagged | 2 | Individual quotes carry dates/times. But the staleness that matters is hidden: the report labels itself "as of 6 July close" while the latest session actually used is 3 Jul. §13d upcoming calendar rows are dated only "wk" (no day/time). 6-Jul close absent. SINGLE-SRC flags present in §6. | header; §13d; §6 |
| 5.2 Assumptions up front | 3 | Anchor override stated on the card and in §20; lenient-corroboration instruction disclosed in §19; single-source pivot propagation stated (daily pivots from corroborated H/L/C). Not up front: neither the anchor override nor the 3-Jul-vs-6-Jul window is in §1/§2. | §19-§21b |
| 5.3 Red flags surfaced | 3 | US CPI, US-tech sell-off, UK PMI, miners surfaced and carried into card caveats. Missed: D-day scheduled items in the calendar feed — BoE FPC minutes and Financial Stability Report (12:30 broker = 10:30 London), Fed Governor Bowman speech (14:00 broker = 12:00 London), BoE MPC Mann speech (19:15 broker = 17:15 London), US trade balance (15:30 broker = 13:30 London); a "US CPI" row with no date. | §13d; §12; §21b caveats |
| 5.4 Restrictions honoured | 1 | Breach: price data presented as sourced that show the signature of back-filled values — Open ≈ prior-day Close on all four transitions (10,531→10,537; 10,548→10,548; 10,598→10,600; 10,658→10,653) while the feed gaps on 2 and 3 Jul (1-Jul close 10,472.4 → 2-Jul open 10,433.6; 2-Jul close 10,654.0 → 3-Jul open 10,689.3); errors up to 166 pts on the 2-Jul open/low, 126 pts on the 1-Jul close, against a source (TradingView) that §20 admits was a snippet. Also: corroboration "applied leniently" by instruction so cards are produced despite the gap (§19) — a corroboration rule waived. Minor: "v2.1 baseline" in §20. No module codes, no bracketed variable names, no futures-as-basis. | §6; §19 L182; §20 |

## 2. Category 3 data reconciliation (report vs level file / slice, UK100 cash CFD basis; tolerance close ≤5, O/H/L ≤10)

D-1 (6 Jul) is absent from the report; all comparisons are by calendar date.

| Date | Field | Report | Slice (cash) | Δ | Verdict |
|---|---|---|---|---|---|
| 29 Jun | O / H / L / C | 10,484 / 10,537 / 10,461 / 10,531 | 10,505.9 / 10,524.3 / 10,468.8 / 10,497.8 | -22 / +13 / -8 / **+33** | O, H, C out |
| 30 Jun | O / H / L / C | 10,537 / 10,575 / 10,505 / 10,548 | 10,509.5 / 10,608.8 / 10,490.6 / 10,501.5 | +28 / **-34** / +14 / **+47** | all out |
| 1 Jul | O / H / L / C | 10,548 / 10,612 / 10,520 / 10,598 | 10,481.4 / 10,500.3 / 10,416.0 / 10,472.4 | +67 / **+112** / **+104** / **+126** | all out; day was a down day (close < prior close) |
| 2 Jul | O / H / L / C | 10,600 / 10,701 / 10,585 / 10,658 | 10,433.6 / 10,686.8 / 10,424.8 / 10,654.0 | **+166** / +14 / **+160** / +4 | O, H, L out; C ok |
| 3 Jul | O / H / L / C | 10,653 / 10,701 / 10,604 / 10,679 | 10,689.3 / 10,692.5 / 10,590.6 / 10,660.5 | -36 / +8 / +13 / **+18.5** | O, L, C out (C > 15 pts: failure) |
| 6 Jul (D-1) | C | not stated (consensus 10,679; mark 10,720-10,730) | 10,641.1 (full-day 10,660.9) | +38 to +89 | missing / wrong |

Other fields:
- RSI2: report "~100" on every row. Slice cash RSI2: 30 Jun 16.6, 1 Jul 11.3, 2 Jul 86.2, 3 Jul 100.0, 6 Jul (D-1) **25.10** (level file: cash 25.10, full-day 47.00). The report's own five closes do reproduce RSI2 = 100 for the last three rows (`--closes` test) but the closes themselves are wrong; "five higher closes / monotonic" is false (actual cash closes 10,497.8, 10,501.5, 10,472.4, 10,654.0, 10,660.5, 10,641.1). The "overbought RSI2 ~100" caution and positioning text are therefore unsupported; D-1 RSI2 is 25.1.
- ATR14: report ≈90 (§21b only); level file 113.91 (cash) / 121.13 (full): Δ -24 to -31 (-21% to -26%).
- Kaufman efficiency: report "near-maximal / strongly trending up"; raw 13-session close-to-close efficiency from the slice = 0.20 (13 cash closes 10,513.3 … 10,641.1; net 127.8 over path 627). Low efficiency, not trending-up. (EMA-3 smoothing not applied; the gap to "near-maximal" is far larger than any smoothing effect.)
- 25-day position: D-1 cash close 10,641.1 sits at 86% of the 25-day range (10,126.2-10,726.7), 5-day swing 10,416.0-10,726.7.
- Daily pivots (report from 3 Jul; level file from 6 Jul), cash / full-day:

| Level | Report | Cash | Δ | Full-day | Δ |
|---|---|---|---|---|---|
| R3 | 10,816 | 10,828.0 | -12 | 10,841.2 | -25 |
| R2 | 10,759 | 10,777.4 | -18 | 10,784.0 | -25 |
| R1 | 10,719 | 10,709.2 | +10 | 10,722.4 | -3 |
| P | 10,662 | 10,658.6 | +3 | 10,665.2 | -3 |
| S1 | 10,622 | 10,590.4 | +32 | 10,603.6 | +18 |
| S2 | 10,564 | 10,539.8 | +24 | 10,546.4 | +18 |
| S3 | 10,525 | 10,471.6 | **+53** | 10,484.8 | +40 |

  Wrong session (3 Jul, not D-1 = 6 Jul); S1/S2/S3 and R2/R3 outside 10 pts on either basis.
- Weekly / monthly pivots: not presented. Level file (cash): W P 10,589.7, R1 10,763.3, S1 10,486.8, R2 10,866.2, S2 10,313.2, R3 11,039.8, S3 10,210.3; Monthly P 10,412.2, R1 10,698.1, S1 10,215.5, R2 10,894.8, S2 9,929.6, R3 11,180.7, S3 9,732.9.
- Cross-asset counters (slice, 29 Jun→6 Jul): US500 7,440.3→7,546.3 (up, 6 Jul at the window high, 3 Jul +0.4%); USDX 101.10→100.85 (down ~0.25%); VIX 18.03→16.89 (down). Report: "S&P 500 falling (tech-led)", "S&P VOLator spiking" — contradicted.
- Not testable from the slice (flagged, not penalised as errors): the 10,934.94 "late-February record" (slice starts April; 25-day high is 10,726.7), DAX and Euro Stoxx figures, article quotes.

## 3. Override check
- Hallucinated source: NOT triggered. Evidence of misattribution exists (Sharecast quote reused across two dates; TradingView cited for OHLC it could not supply) but nothing proves a cited source or URL to be non-existent; handled inside 3.2 and 5.4.
- Restriction breach: TRIGGERED (5.4). Prices presented as sourced that carry the Open≈prior-Close back-fill signature with errors up to 166 pts, plus corroboration standard waived "per user instruction" (§19). Effect: cap Moderate (74) — not binding at 44; C1 lowered one level: row mean 1.1-1.3 = (2+2+4)/3 = 2.67 → 3, minus one = **2**.

## 4. Category roll-up

| Cat | Level | Multiplier | Max | Points | Justification |
|---|---|---|---|---|---|
| 1 Prompt adherence | 2 | 0.40 | 20 | 8.0 | Mean 3 (rows 2/2/4) reduced one level for restriction breach; wrong as-of window, thin/untiered sources, anchor overridden. |
| 2 Structure | 4 | 0.85 | 20 | 17.0 | All 21 sections and sub-sections present and ordered; weekly/monthly pivot tables missing; charts text-only. Mean (5+3+4)/3 = 4. |
| 3 Accuracy & evidence | 1 | 0.20 | 25 | 5.0 | Row mean 2.0, but brief §4 failure triggers: close wrong by >15 pts on 4 of 5 days (up to 126), D-1 absent, RSI2 25.1 vs "~100", ATR ≈90 vs 114-121, cross-asset facts contradicted. |
| 4 Reasoning & judgment | 2 | 0.40 | 20 | 8.0 | Rows 3/2/2/4/1 → mean 2.4. Directional case rests on false inputs; cards fail construction. |
| 5 Currency & transparency | 2 | 0.40 | 15 | 6.0 | Rows 2/3/3/1 → mean 2.25. Hidden staleness, undated calendar, restriction breach. |
| **Total** | | | 100 | **44** | **Low (40-59)** |

## 5. Card Integrity (linter rows copied verbatim from `qa/ftse_qa1/lint_static/2026-07-07.csv`; separate from the 100)

| card_id | strategy | flags | dud |
|---|---|---|---|
| 2026-07-07_Trade_1 | Trade 1 — Daily Directional (LONG — TREND_UP regime) | CLEAN | False |
| 2026-07-07_Trade_2 | Trade 2 — Pivot (regime-aware, TREND_UP → buy-the-dip to support pivots) | CLEAN | False |
| 2026-07-07_Trade_3A | Trade 3A — Momentum-Pullback (TREND_UP variant) | CLEAN | False |

Per card 100 − 40·0 − 10·0 = 100 each; report-level mean = **100** (n_cards=3, n_duds=0, n_warns=0).
Caution: the linter runs in static mode with no market data and cannot see the construction defects scored under 4.5 (market entry ≠ D-1 close, limit on the wrong side of the D-1 close, wrong regime template, wrong Fib retrace). A clean linter row is not evidence of a compliant card.
