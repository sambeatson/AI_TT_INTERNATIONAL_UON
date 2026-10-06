# Trust Score v3.7 — FTSE 100 daily report, D = 2026-06-26

Report: `reports/md/FTSE_EuroStoxx_Report_26-Jun-2026.md` · Reviewer run: ftse_qa1 · Data basis: `data/levels/UK100_by_date/2026-06-26.csv` (last_bar_date 2026-06-25 < D, checked) and the UK100 slice up to 2026-06-25, cash window 10:00–18:30 broker (08:00–16:30 London), `_cash` basis (the report claims the FTSE 100 cash index).

Headline: the report is stated as of the **24 June** close, but D−1 for a 26 June report is **25 June**. Every price, pivot, RSI2, range and card level is therefore one session stale. In addition, four of the five rows in the §6 OHLC table are far outside the CFD-vs-cash tolerance, although the report marks them "Corrob.".

## Machine-readable score lines
```
c1=2
c2=3
c3=2
c4=3
c5=2
total=50
band=Low
override=restriction_breach
card_integrity=100.0
n_cards=3
n_duds=0
n_warns=0
```
`n_cards=3` counts the linter rows (1 SUPPRESSED, 2 scored). `card_integrity` is the mean over the 2 non-suppressed cards. The override is `restriction_breach` and not `hallucinated_source`. The cited sources are named and their quotes are used consistently, so none is demonstrably fabricated. What the report breaches is the no-synthesis restriction: price rows that look constructed are presented as corroborated.

## 1. Section 7 checklist

| Row | Reviewer notes | Evidence observed (location) | Score |
|---|---|---|---|
| 1.1 Variables respected | Asset = FTSE 100 cash, Euro Stoxx 50 reference only, counters USDX / S&P 500 / DAX 40, 5-session lookback, GBP/points: all correct. **As-of date wrong**: header, §2 and §5 say "close 24 June"; D−1 is 25 June. The ≥6-source requirement is met in count (§4) but not in tier: no index provider (FTSE Russell / LSE), exchange or sell-side source is cited for the FTSE; all are aggregators or media. Anchor: §20 says only "DAILY_OPEN_ANCHOR overridden to the 26 Jun open", with no 07:00 UK time. The variable name leaks into the report. | Header; §2 "As-of date"; §4; §20 | 2 |
| 1.2 Coverage & currency consistent | Currency consistent. Coverage is shifted a full session: §6 ends 24 Jun, §11 pivots use 24 Jun H/L/C, §21c "t−1" = 24 Jun, §9 range and §21b cards reference the 24 Jun close. The 25 Jun session (cash O 10,427.6 / H 10,577.7 / L 10,413.8 / C 10,538.0) is absent. The 25 Jun US prints (Core PCE, GDP) are listed as "upcoming" in §13. | §1, §6, §11, §13 upcoming, §21c | 2 |
| 1.3 Audience & tone | Strategist tone, trading and risk-review register. No retail language. | §1, §18 | 4 |
| 2.1 Sections present & ordered | §1–§21 all present, incl. §21a–d and the Trade 1 SUPPRESSED row. §7 has a caption only, no chart (pandoc drops images; accepted, noted). §13 is out of order: 13a, 13b, then "13d Divergence", then "13c calendar". Calendar previous and upcoming sit together in 13c, so there is no 13d upcoming calendar. The upcoming table's first row is the literal `[object Object]` ×3 (leaked placeholder). §21a does not itemise all six signals. | headings; §7; §13 | 3 |
| 2.2 Scorecard as a table | §6 is a table but lacks the Source A / Source B / Final columns. §11 daily table is mixed, with a stray "—" / "↑ resist" column. Weekly pivots carry only R2..S2 (R3/S3 missing). **Monthly pivots are absent.** | §6, §11 | 2 |
| 2.3 Method steps visible | §4 → §5 shows observations → consensus. §8 is candle-by-candle with a sequence call, but contains an error (18 Jun described as a "bearish body"; its own O 10,323.7 → C 10,380.0 is bullish). §9 regime is qualitative: persistence, overlap and KER give no numbers beyond "~+0.13", with no window or EMA stated. Charts are a caption only. | §7, §8, §9 | 3 |
| 3.1 Quantitative claims sourced | §1/§12/§14 figures (WTI ~$70, Segro +15%+, Shell/BP −3.6%, miners −1.7–3.6%, "~80% overseas revenue") carry no source, date or pointer to §4/§13. §13a articles are undated. The §10 5-day moves (S&P −0.1%, DAX −0.6%) have no source. | §1, §10, §12, §13a, §14 | 2 |
| 3.2 Citations exist & contain data | The spot-checks are not self-contradictory. Yahoo/Investing 24 Jun 10,461.63 (cash slice 10,455.1, Δ +6.5, near but above the 5-pt close tolerance). Fidelity "~10,461.36 / up 0.3% afternoon" is consistent with §1 +0.31%. CNBC gold "7-month low" is used consistently in §12/§13c/§14. Weaknesses: no URLs; TE close shown as "10,454 / 10,462" (two values); Sigmanomics quotes a 14-day RSI that is used nowhere else. **The "Corrob." status claimed for 18–23 Jun closes is false against the slice (Δ +19.6 to +96.7 pts).** | §4, §6, §13a, §19 | 1 |
| 3.3 Calculations transparent | RSI2 for 22/23/24 Jun reproduces from the report's own closes (100.0 / 42.9 / 28.8; checked with `--closes`). Pivot formulas applied to the 24 Jun H/L/C are arithmetically right (P 10,446, R1 10,485, S1 10,423, R2 10,508, S2 10,384, R3 10,547, S3 10,360). Defects: Trend labels wrong on 18 Jun (C>O, RSI2 20.2 → Neutral, not "Bearish") and 19 Jun (C>O, RSI2 50.5 → Bullish, not "Neutral"). RSI2 for 18/19 Jun cannot be reproduced from the table. §13b weighted mean is (0.7+0.7−0.5)/2.9 = **+0.31**, not +0.10 (five weights for six articles). §9 "≈67th percentile" is wrong against its own numbers: (10,461.63−10,127.6)/(10,570.09−10,127.6) = 75.5%. §21a Σ signal×weight is not reproducible (3 of 6 signals shown). ATR(14) "≈110" vs slice 117.9 cash / 141.1 full. §21d "mean R ≈ +0.80 (closed)" includes the 0.4R trade §21c marks OPEN. | §6, §8, §9, §13b, §21a, §21d | 2 |
| 3.4 Numbers reconcile | Internally good: the close 10,461.63 is identical in §1/§3/§4/§6/§18; §11 pivots = card levels; RSI2 28.8 is the same in §6/§8/§21a. Against the data: **D−1 close wrong basis/date** (report 10,461.63 = 24 Jun; D−1 cash 10,538.0, full-day 10,518.2). The §6 table is badly off the slice (discrepancy table below). Daily pivots are off by up to 223 pts. Weekly pivots are off by 15–77 pts. Monthly pivots are missing. §21b long distances "23 / 43 pts below close" are wrong: 10,461.63−10,423 = 38.6 and −10,403 = 58.6. | whole report | 1 |
| 4.1 Pillars conclude | §8 ends in a Neutral/transition tag, §9 Ranging, §10 "MIXED". §12 has per-factor biases but no aggregate direction label. §14 ends on watch items with no direction. | §8–§14 | 3 |
| 4.2 Peer / cross-asset interpreted | §10 gives mechanisms (USD translation, defensives vs energy/miners, DAX defence being idiosyncratic). Thin, with no oil or Brent row despite the energy discussion. The magnitudes cited conflict with the slice: USDX +1.16% over 5 sessions to 24 Jun (101.591 vs 100.425 on 17 Jun) is called "Flat/firm"; US500 −0.38% is called "−0.1%". | §10 | 3 |
| 4.3 Synthesis reconciles tensions | §9/§16/§21a explicitly reconcile short Transitional vs medium Ranging, and §17 vs §21a. Unreconciled: the 3B card says "current price mid-range" while §9 says mid-to-upper (and the real figure is ~75%). §1 range 10,440–10,485 vs §16 10,400–10,510 are different bands with no explanation. The §13d CPI catalyst does not exist in the calendar. | §1, §9, §16, §21b | 3 |
| 4.4 Calibrated language | §17 is exactly one sentence, with no hedge stacking. Confidence "High" on the consensus and in §18 is over-stated given the report's own admission that most of the OHLC history is single-source indicative. | §3, §17, §18 | 3 |
| 4.5 Card construction (protocol row) | Trade 1: correctly shown SUPPRESSED (|0.04| < 0.25), but the score is not traceable. Trade 2: two-sided card with no single entry; TP2 has no price; the runner target 10,446 is below the long TP1 10,471 (and above the short TP1 10,437); long distances mis-stated; stop buffers below 0.25×ATR; the short sell limit is below the true D−1 close. Trade 3B: stop 10,526 sits inside the entry zone (R = 6 pts = 0.05×ATR14); the short zone is mis-computed (10,535 is 92% of the range); the long leg has no stop; TP3 has no price; the short zone lies below the D−1 close. The linter rows are CLEAN only because the key fields are null (see Card Integrity caveat). | §21b | 1 |
| 5.1 Data dated; staleness flagged | The "indicative" flag on O/H/L is good practice. But the as-of staleness vs D−1 is not flagged, the §13a articles carry no dates, the §13 upcoming events are "This wk" / "Ongoing" / `[object Object]`, and corroboration is asserted where the slice disagrees. | §6, §13, §19 | 2 |
| 5.2 Assumptions up front | The anchor override appears only in §20 and is not on any card. Single-source propagation: present on Trade 2 ("weekly support tiers carry single-source flag"); absent on Trade 3B. §19 states the weekly-low flag. | §19, §20, §21b | 3 |
| 5.3 Red flags surfaced | §12/§15 give two-sided risks. The headline catalyst, "eurozone flash CPI / BoE", is not on the D calendar (D events: Michigan sentiment 17:00 broker = 15:00 UK, US goods trade 15:30 broker, EUR jobseekers 13:00 broker). The HIGH-impact 25 Jun US prints (Core PCE m/m 0.3 vs 0.1 cons., GDP q/q 2.1 vs 1.6) are treated as upcoming. No event collision is carried onto any card. | §1, §13, §21b | 2 |
| 5.4 Restrictions honoured | **Breach.** §6 rows for 18–23 Jun look synthesised and are labelled corroborated: every open equals the prior close (10,380.0 / 10,449.0 / 10,510.0; Euro Stoxx the same: 6,255 / 6,285), with round-number H/L (10,455.0, 10,360.0, 10,520.0, 10,440.0, 10,515.0, 10,410.0, 10,300.0). Rendering artefact `[object Object]` in §13. The process term "locked defaults / first-20 lock" and the variable name DAILY_OPEN_ANCHOR appear in §20. No retail CFD quotes (positive). | §6, §13, §20 | 1 |

### Category 3 discrepancy table (report vs `_cash` slice; tolerance: close ±5, O/H/L ±10)
| Date | Field | Report | Slice (cash) | Δ (report − slice) | Verdict |
|---|---|---|---|---|---|
| 18 Jun | O / H / L / C | 10,323.7 / 10,408.4 / 10,300.0 / 10,380.0 | 10,460.3 / 10,475.8 / 10,372.6 / 10,399.6 | −136.6 / −67.4 / −72.6 / −19.6 | all outside; close >15 |
| 19 Jun | O / H / L / C | 10,380.0 / 10,455.0 / 10,360.0 / 10,449.0 | 10,383.1 / 10,417.4 / 10,347.8 / 10,352.3 | −3.1 / +37.6 / +12.2 / **+96.7** | H, L, C outside; close >15 |
| 22 Jun | O / H / L / C | 10,449.0 / 10,520.0 / 10,440.0 / 10,510.0 | 10,379.2 / 10,441.4 / 10,343.2 / 10,440.9 | +69.8 / +78.6 / +96.8 / +69.1 | all outside; close >15 |
| 23 Jun | O / H / L / C | 10,510.0 / 10,515.0 / 10,410.0 / 10,428.85 | 10,329.6 / 10,461.5 / 10,328.1 / 10,453.0 | **+180.4** / +53.5 / +81.9 / −24.2 | all outside; close >15, and the direction of the day is wrong (the slice shows it up) |
| 24 Jun | O / H / L / C | 10,429.0 / 10,469.3 / 10,407.0 / 10,461.63 | 10,422.2 / 10,468.6 / 10,400.6 / 10,455.1 | +6.8 / +0.7 / +6.4 / +6.5 | O/H/L in tolerance; close 1.5 pts over the 5-pt limit but inside 15 |
| 25 Jun (D−1) | O / H / L / C | **missing** | 10,427.6 / 10,577.7 / 10,413.8 / 10,538.0 | n/a | D−1 session omitted |

RSI2: the report's 24 Jun RSI2 of 28.8 reproduces arithmetically from its own closes. The slice gives cash RSI2 = 100.0 for 24 Jun and 100.0 for 25 Jun (D−1). The report's RSI2 is therefore wrong on the real data, because its closes are wrong. ATR14: report ≈110 vs 117.9 cash / 141.1 full (Δ −7.9 cash).

### Pivots vs `_cash` level file (D−1 = 25 Jun)
| Level | Report | Level file | Δ |
|---|---|---|---|
| Daily R3 / R2 / R1 | 10,547 / 10,508 / 10,485 | 10,769.8 / 10,673.7 / 10,605.9 | −222.8 / −165.7 / −120.9 |
| Daily P | 10,446 | 10,509.8 | −63.8 |
| Daily S1 / S2 / S3 | 10,423 / 10,384 / 10,360 | 10,442.0 / 10,345.9 / 10,278.1 | −19.0 / +38.1 / +81.9 |
| Weekly (W25) R2 / R1 / P / S1 / S2 | 10,710 / 10,579 / 10,440 / 10,309 / 10,170 | 10,651.7 / 10,502.0 / 10,424.9 / 10,275.2 / 10,198.1 | +58.3 / +77.0 / +15.1 / +33.8 / −28.1 |
| Weekly R3 / S3 | not given | 10,728.8 / 10,048.4 | missing |
| Monthly (May) all levels | **not given** | P 10,370.4, R1 10,599.6, S1 10,180.8, R2 10,789.2, S2 9,951.6, R3 11,018.4, S3 9,762.0 | missing |

The daily pivots are arithmetically correct for the 24 Jun session (cash-session P ≈ 10,441.4 vs the report's 10,446), so they are a session late rather than miscalculated. The report's 25-session range 10,127.6–10,570.09 matches the slice through 24 Jun (10,126.2–10,574.6, Δ ≤ 4.5). Through D−1 the range is 10,126.2–10,577.7.

## 2. Category roll-up

| # | Category | Level | Multiplier | Points | Justification |
|---|---|---|---|---|---|
| 1 | Prompt adherence (20) | 2 | 0.40 | 8.0 | Rows mean 2.67 → 3; restriction-breach override lowers it one level → 2. As-of date one session stale, source tiers not met, anchor time absent. |
| 2 | Structure (20) | 3 | 0.65 | 13.0 | All 21 sections present, but §6 lacks Source A/B/Final columns, monthly pivots are absent, §13 is out of order with a `[object Object]` placeholder, and charts are captions only. |
| 3 | Accuracy & evidence (25) | 2 | 0.40 | 10.0 | Rows mean 1.5 → 2. Four of five §6 rows are far off the slice (closes −19.6 to +96.7) yet labelled corroborated. Pivots are a session stale. Arithmetic errors in §9, §13b, §21d. |
| 4 | Reasoning & judgment (20) | 3 | 0.65 | 13.0 | Rows mean 2.6 → 3. Coherent narrative and a correctly suppressed Trade 1, held down by card construction (row 4.5 = 1). |
| 5 | Currency, restrictions & transparency (15) | 2 | 0.40 | 6.0 | Indicative flags are good, but articles and calendar items are undated, the as-of staleness is not flagged, and synthesised-looking prices are presented as corroborated. |

## 3. Total, band, override
- Total = 8.0 + 13.0 + 10.0 + 13.0 + 6.0 = **50** → band **Low (40–59)**.
- Override check: `restriction_breach` applied. The cap is Moderate (60–74), which does not bind at 50. C1 was reduced one level, 3 → 2. `hallucinated_source` was considered and rejected: no cited source is shown to be non-existent. The failure is false "corroborated" status on constructed OHLC. A reviewer who read the §6 rows as fabricated validation would set C3 = 0 (total 40, still Low).

## 4. Card Integrity (separate from the 100) — linter rows copied verbatim from `lint_static/2026-06-26.csv`

| card_id | strategy | flags | dud | per-card integrity |
|---|---|---|---|---|
| 2026-06-26_Trade_1 | Trade 1 - Daily Directional: SUPPRESSED | SUPPRESSED | False | excluded (suppressed) |
| 2026-06-26_Trade_2 | Trade 2 - Pivot (range-fade), primary card | CLEAN | False | 100 |
| 2026-06-26_Trade_3B | Trade 3B - Mean-Reversion (25-session range) | CLEAN | False | 100 |

Report-level Card Integrity = mean(100, 100) = **100.0** (n_cards=3 rows, 2 scored, n_duds=0, n_warns=0).

Caveat for the roll-up (the score is not altered). The static linter returned CLEAN only because the transcription left `tp2` null on Trade 2 and `card_R_points`, `tp3` null on Trade 3B, so the TP2-order, TP3-order, and R-size tests had nothing to evaluate. The hand review in `2026-06-26_feedback.md` finds substantive defects on both cards. The transcription notes themselves record "long runner target 10,446 is below long TP1 10,471" and "stop 10,526 is only 6 pts above the 10,520 zone edge and BELOW the top of the entry zone (10,535)". Card Integrity=100 should not be read as a clean bill of health for these cards.

## 5. Feedback
See `qa/ftse_qa1/2026-06-26_feedback.md`.
