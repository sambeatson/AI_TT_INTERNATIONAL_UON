# Trust Score v3.7 - FTSE 100 Daily, 12 May 2026 (run ftse_qa1)

Report: `reports/md/FTSE_EuroStoxx_Daily_12May2026.md` · D = 2026-05-12 · D-1 = 2026-05-11
Level file `data/levels/UK100_by_date/2026-05-12.csv`: `last_bar_date` = 2026-05-11 < D (checked). Slice last bar 2026-05-11 22:45 broker (checked by `qa_slice_stats.py`, `--cash-open 10:00 --cash-close 18:30`).
Basis used: **cash** (`_cash`), because the report claims the FTSE 100 cash index. Full-day figures are quoted where they change the conclusion.

## Machine-readable result
```
c1=3
c2=4
c3=0
c4=3
c5=2
total=49
band=Low
override=hallucinated_source
card_integrity=100
n_cards=3
n_duds=0
n_warns=0
```
Notes on the override line: the report's 05-08 May OHLC rows are attributed to named, "CORROBORATED" sources (Δ ≤ 0.45 pt) yet differ from the D-1-clean feed by up to 196 pts (far beyond a CFD/cash basis), and the opens of 06 and 07 May equal the prior close to the cent. Those attributions are not credible, so the hallucinated-source rule is applied (cap Low 40-59, C3 = 0). A restriction breach (module codes, bracketed variable name, framework wording, synthesised-looking prices) is ALSO present; its effect (C1 down one level, from 4 to 3) is applied inside c1. Only one value can be written on the `override=` line; the Low cap is the binding one.

## 1. Section 7 checklist (every row)

| Row | Reviewer notes | Evidence (location) | Score |
|---|---|---|---|
| 1.1 Variables respected | FTSE 100 cash index is primary, STOXX 50 reference only (§2); GBP/index points; 5-session lookback; Europe/London; 07:00 UK anchor on Trade 1 (§2, §21b). Counters USDX/S&P/DAX appear in §9-§10 but §2 never defines the counter list. S&P 500 value is one session stale (see 5.1). Six FTSE sources named but two are CFD/aggregator quotes (Investing.com "Continuous CFD", Trading Economics "GB100 CFD/cash") on a brief that bars CFD quotes from the OHLC basis. | §2, §4, §10, §21b | 4 |
| 1.2 Coverage and currency consistent | Daily pivots labelled "from 08 May" (§11) - the pivot input session is D-3, not D-1 (11 May). §13c is titled "last 5 sessions" but four of its five rows are 30 Apr (outside the 5-11 May window). S&P 500 7,398.93 is the 08 May close shown as the 11 May close. STOXX GBP-equivalent is flagged, no unit drift. | §11, §13c, §10 | 3 |
| 1.3 Audience and tone | Institutional strategist register throughout, no retail tone. "Round-rounded ticker" typo in §4. | §1, §18 | 4 |
| 2.1 Sections present, ordered | §1-§21 all present in order, including §13a-d, §21a-d; §17 present. §7 holds five chart captions only (images dropped by pandoc; accepted, noted). | headings | 5 |
| 2.2 Scorecard as table | §6 is a table, but has no "Final" column. §11 is ONE merged table (P,R1,R2,R3,S1,S2,S3) not three R3→P→S3 tables, and Daily and Monthly rows have "-" for R3 and S3 (3 levels each side required). | §6, §11 | 3 |
| 2.3 Method steps visible | §4-§5 observations → consensus; §8 candle by candle plus sequence; §9 regime with persistence/overlap/VOLator and KER. ATR(14) not stated in §9 (appears only inside Trade 1). Chart placeholders only. | §4-§9 | 4 |
| 3.1 Quantitative claims sourced | S&P 500 7,398.93 and its +0.84%/+1.46% have no source or date. DAX 24,338.63/−2.43% unsourced and cannot be checked (no DAX slice). Fed Funds 4.00-4.25%, 2y/10y gilt yields, ECB excess liquidity, CFTC positioning, "FTSE energy weight ~12%", "~70% of revenue non-GBP/USD" (both phrasings used) carry no source. §6 sources are named but the figures do not reproduce (3.2). | §10, §12, §14 | 2 |
| 3.2 Citations exist and contain the data | Three checked. (a) §4 "LSE exchange data 10,269 → normalised 10,267.45, agrees to ±0.10 tolerance": 1.55 pt apart, contradicts its own tolerance. (b) §6 "Yahoo / Investing.com / FTSE Russell / TE" CORROBORATED Δ ≤ 0.45 pt for O/H/L/C that differ from the feed by 2-196 pts (table in §3 below); opens of 06 and 07 May equal prior close exactly. (c) §13c NFP "62k, softer than expected": the calendar slice has NFP actual 115k vs consensus 90k (beat); 62k is the ADP prior. §19 says all closes within ±0.10 pt but §6 shows Δ=0.30 and Δ=0.45. Treated as fabricated attribution → override. | §4, §6, §13c, §19 | 0 |
| 3.3 Calculations transparent | RSI2 does not reproduce from the report's own closes (10,398.50 / 10,410.30 / 10,379.51 / 10,233.07 / 10,267.45): engine gives 27.7 / 0.0 / 19.0 vs reported 38.7 / 12.3 / 28.6. Pivot formulas are applied correctly to the report's inputs, but the weekly implied high 10,683.66 and monthly implied high 10,934.94 are not in the report's own table or its stated ATH (10,910.55). KER −0.11 not derivable; recomputed 13-session KER on cash closes is −0.22 raw / −0.27 EMA-3. §21a arithmetic is correct (sum −0.263). | §6, §8, §9, §11, §21a | 1 |
| 3.4 Numbers reconcile | D-1 close 10,267.45 identical in §1/§3/§4/§6/§21b; RSI2 28.6 identical in §6/§8/§21a; card pivots match §11. Breaks: §11 narrative/§15/§18 say close is "below all three timeframe pivots" while the §11 table has Daily P 10,251.21 < 10,267.45; "retraced 4.3% from 10,910.55" vs (10,910.55−10,267.45)/10,910.55 = 5.9%; "25-session mid 10,549" (level file 10,430.2 cash); §1 puts KER "inside −0.09 to 0.09" but §9 says "−0.09 to −0.13 zone"; §13b says 4-2-1 sentiment split but §13a has 5 bearish / 1 mixed / 1 bullish; §21c row 05 May Trade 1 "SL 10,485 hit by 06 May high 10,456" and 08 May "SL 10,357 hit by 11 May high 10,287" are impossible. | §1, §11, §13b, §15, §18, §21c | 2 |
| 4.1 Pillars conclude | §8 (INDECISION), §9 (BEARISH transitional), §10 (SPLIT), §16 reach labels. §12 and §14 end without a direction label. | §8-§16 | 3 |
| 4.2 Cross-asset interpreted | Mechanisms given, but the USDX one is inverted: a weaker dollar lowers the sterling value of USD revenues, so "dollar weakness lifts overseas-revenue constituents on translation" has the sign backwards. Energy-weight mechanism (Brent→Shell/BP) is sound. S&P/DAX reads are generic. | §10, §14, §15 | 2 |
| 4.3 Synthesis reconciles tensions | §8 vs §9 vs §17 vs §21a conflicts addressed ("No conflict"). Cross-asset signal −0.20 is bearish although two of three counters are labelled CONTRADICTS. Trade 1 SHORT and Trade 3B LONG are issued 39 pts apart on the same day and the regime label (TRANSITIONAL) does not match 3B (a RANGE strategy). §1 watch item is UK CPI 21 May, §18 watch item is UK GDP 13 May. | §1, §10, §18, §21 | 3 |
| 4.4 Calibrated language | §17 is one sentence; confidence MEDIUM stated in §3 and §18. Some boilerplate repetition ("No conflict to flag"). | §3, §17 | 4 |
| 4.5 Card construction (protocol Cat 4) | Trade 1 TPs at 0.5R/1.0R/2.0R (rule: 1R/2R), stop not built from swing/S-R + 0.25×ATR, ATR stated ≈80 vs 134.24, runner has no session-close time-stop or 3×ATR cap, native-unit figures ×100. Trade 2 two-sided though regime rule is breakout side only; TPs carry stray ".45". Trade 3B is a RANGE card under a TRANSITIONAL regime, targets are not 3B's (mid / far side −10%), R=36 = 0.27×ATR14 (floor 40.3). See feedback. | §21b | 1 |
| 5.1 Data dated; staleness flagged | Most articles and prints dated. S&P 500 (08 May close, shown as D-1) not flagged stale; GBP/USD, EUR/USD, gilt yields undated; §13c 30 Apr rows inside a "last 5 sessions" table. Report asserts all data CORROBORATED, flags nothing single-source. | §10, §13c, §14 | 3 |
| 5.2 Assumptions up front | Anchor override stated in §2 and §20. Card says "cash anchor - 12 May pre-open" but never states that the cash index does not trade at 07:00 and that entry = D-1 close proxy. Trade 2/3B anchors implicit (resting orders, no expiry). | §2, §20, §21b | 3 |
| 5.3 Red flags surfaced | Iran/Hormuz, BoE, defence/energy divergence surfaced. Missed: US CPI y/y (consensus 3.7% vs prior 3.3%) and Core CPI m/m at 15:30 broker (13:30 London) ON D, plus 10-year note auction 20:00 broker, are absent from §13d and from every card's caveats; §13d starts at 13 May. UK GDP (13 May) inside Trade 2's window not carried to the card. | §13d, §21b | 2 |
| 5.4 Restrictions honoured | Breached: module codes in body ("M2 §9c", "M3 §11 Named Output Surface", "M2 §9a", "M5 strategies trace", "M5 ... DEFAULT (locked...)"); bracketed variable name "[MAX_SIMULTANEOUS_LONG_SHORT]" on Trade 3B; "framework instruction"/"RESTRICTIONS:" wording in §5 and §19; CFD-basis quotes in §4; 06/07 May opens equal the prior close (looks synthesised, presented as sourced). | §4, §5, §13b, §19, §20, §21b | 1 |

## 2. Category roll-up

| Cat | Max | Rows (mean) | Level | Multiplier | Points | Justification |
|---|---|---|---|---|---|---|
| 1 Prompt adherence | 20 | 1.1=4, 1.2=3, 1.3=4 → 3.67 → 4; restriction breach → −1 | 3 | 0.65 | 13.0 | Right asset, window, anchor; period drift in §11/§13c/§10; restriction breach (module codes, bracketed variable) lowers it one level. |
| 2 Structure | 20 | 5, 3, 4 → 4.00 | 4 | 0.85 | 17.0 | All sections ordered; §11 not in R3→S3 per-timeframe form and missing R3/S3 on two timeframes. |
| 3 Accuracy | 25 | 2, 0, 1, 2 → 1.25 (would be 1); override sets 0 | 0 | 0.00 | 0.0 | Override applied: fabricated source attribution; 16 of 20 OHLC fields outside tolerance; RSI2 does not reproduce. |
| 4 Reasoning | 20 | 3, 2, 3, 4, 1 → 2.60 | 3 | 0.65 | 13.0 | Score arithmetic traceable and regime labels coherent; USDX mechanism inverted; card construction poor. |
| 5 Currency/transparency | 15 | 3, 3, 2, 1 → 2.25 | 2 | 0.40 | 6.0 | Dated and caveated in places; D-day US CPI missed; restrictions breached. |

## 3. Total, band, override
Total = 13 + 17 + 0 + 13 + 6 = **49** → band **Low** (40-59). Override check: hallucinated-source rule triggered (cap Low, C3 = 0). Restriction-breach rule also triggered (cap Moderate, C1 −1, already included). Without the C3 override the natural C3 would be 1 (0.20×25 = 5) and the total 54, still Low.

### Category 3 evidence: report vs level file / slice (cash basis, report minus feed)

| Session | O (rep / feed / Δ) | H | L | C | RSI2 (rep / feed cash / engine on report's closes) |
|---|---|---|---|---|---|
| 05 May | 10,405.20 / 10,295.4 / +109.8 | 10,428.70 / 10,309.8 / +118.9 | 10,358.40 / 10,162.8 / +195.6 | 10,398.50 / 10,219.9 / +178.6 | 56.4 / 0.46 / n.a. |
| 06 May | 10,398.50 / 10,336.0 / +62.5 | 10,456.40 / 10,491.8 / −35.4 | 10,372.10 / 10,321.9 / +50.2 | 10,410.30 / 10,442.3 / −32.0 | 64.1 / 59.39 / n.a. |
| 07 May | 10,410.30 / 10,451.2 / −40.9 | 10,448.90 / 10,451.2 / −2.3 | 10,358.50 / 10,277.5 / +81.0 | 10,379.51 / 10,282.6 / +96.9 | 38.7 / 58.20 / 27.7 |
| 08 May | 10,277.00 / 10,189.8 / +87.2 | 10,298.45 / 10,271.7 / +26.8 | 10,222.10 / 10,174.8 / +47.3 | 10,233.07 / 10,222.4 / +10.7 | 12.3 / 0.00 / 0.0 |
| 11 May (D-1) | 10,233.56 / 10,254.8 / −21.2 | 10,286.57 / 10,284.2 / +2.4 | 10,226.50 / 10,221.9 / +4.6 | 10,267.45 / 10,264.1 / +3.4 | 28.6 / 40.92 / 19.0 |

Within tolerance (close ≤5, O/H/L ≤10): 4 of 20 fields (07 May H; 11 May H, L, C). D-1 open is out by 21.2. Closes wrong by >15 pts: 05 May (+178.6), 06 May (−32.0), 07 May (+96.9). Full-day basis does not rescue them (e.g. 05 May full-day L 10,162.8, C 10,267.6).

| Metric (D-1) | Report | Level file (cash / full) | Δ |
|---|---|---|---|
| ATR14 | ≈80 (card only) | 134.24 / 147.39 | −54 (−40%) |
| RSI2 | 28.6 | 40.92 / 75.44 | −12.3 vs cash; reproduces as 19.0 from the report's own closes |
| 5d swing high / low | 10,456 / 10,222 (implied by table) | 10,491.8 / 10,162.8 | 8 May low 10,174.8 (cash), not 10,222 |
| 25d high / low | ATH 10,910.55 (27 Feb) cited | 10,697.5 / 10,162.8 (cash) | 25-session window excludes 27 Feb |

| Pivot | Report | Level file (cash) | Δ |
|---|---|---|---|
| Daily P / R1 / R2 / S1 / S2 | 10,251.21 / 10,280.31 / 10,327.56 / 10,203.96 / 10,174.86 | 10,256.73 / 10,291.57 / 10,319.03 / 10,229.27 / 10,194.43 | −5.5 / −11.3 / +8.5 / −25.3 / −19.6 |
| Daily R3 / S3 | missing ("-") | 10,353.87 / 10,166.97 | missing |
| Weekly P / R1 / R2 / R3 | 10,379.61 / 10,537.11 / 10,841.16 / 10,998.66 | 10,292.33 / 10,421.87 / 10,621.33 / 10,750.87 | +87.3 / +115.2 / +219.8 / +247.8 |
| Weekly S1 / S2 / S3 | 10,075.56 / 9,918.06 / 9,614.01 | 10,092.87 / 9,963.33 / 9,763.87 | −17.3 / −45.3 / −149.9 |
| Monthly P / R1 / R2 | 10,591.40 / 11,018.54 / 11,362.08 | 10,418.8 / 10,650.0 / 10,928.7 | +172.6 / +368.5 / +433.4 |
| Monthly S1 / S2 | 10,247.86 / 9,820.72 | 10,140.1 / 9,908.9 | +107.8 / −88.2 |
| Monthly R3 / S3 | missing ("-") | 11,159.9 / 9,630.2 | missing |

Daily pivots reproduce from the 08 May bar (H 10,298.45, L 10,222.10, C 10,233.07), i.e. the wrong session; from the report's own 11 May bar they would be P 10,260.17, R1 10,293.84, S1 10,233.77. Weekly pivots imply a week high of 10,683.66 and low of 10,222.11 (feed: 10,491.8 / 10,162.8). Monthly pivots imply a April high of 10,934.94, above the report's own ATH of 10,910.55 (feed: 10,697.5).

Other data checks against the slices: USDX 97.84 vs 97.92 (CFD close 11 May): acceptable. S&P 500 7,398.93 = 08 May close (cash CFD 7,400.6), the 11 May cash CFD close is 7,419.7: stale by one session. VIX not used. NFP (08 May) actual 115k vs consensus 90k (report: 62k, "softer"). CFTC (slice, 08 May): GBP non-commercial net −63.9 (net short), EUR +32.2 (net long); report states speculators net-short EUR and net-long GBP (both reversed). US CPI (12 May 13:30 London) consensus 3.7% y/y vs 3.3% prior: not in the report.

## 4. Card Integrity (linter rows copied verbatim from `qa/ftse_qa1/lint_static/2026-05-12.csv`)

| card_id | report_date | strategy | flags | dud |
|---|---|---|---|---|
| 2026-05-12_Trade_1 | 2026-05-12 | Trade 1 - Daily Directional (SHORT, mild conviction) | CLEAN | False |
| 2026-05-12_Trade_2 | 2026-05-12 | Trade 2 - Regime-Aware Pivot (TRANSITIONAL breakout-side, two-sided) | CLEAN | False |
| 2026-05-12_Trade_3B | 2026-05-12 | Trade 3 - Regime-driven Complex: 3B Mean-Reversion (RANGE-aware long) | CLEAN | False |

Per card: 100 / 100 / 100. Report-level Card Integrity = 100 (3 non-suppressed cards, 0 DUD, 0 WARN). The score is separate from the 100-point total. The static linter does not use the level-file ATR; construction defects against M5 and the level file's ATR14 are listed in the feedback and scored in C4 row 4.5.

## 5. Feedback
See `qa/ftse_qa1/2026-05-12_feedback.md`.
