# Trust Score v3.7 — FTSE 100 daily report, 10 June 2026 (run ftse_qa1)

Report: `reports/md/FTSE_EuroStoxx_Report_10Jun2026.md` · D = 2026-06-10 · D-1 = 2026-06-09
Level file check: `last_bar_date` = 2026-06-09 < D (leak-free, confirmed). Slice last bar 2026-06-09. Basis used for all comparisons: **cash** (`_cash`), the basis the report claims (§2, §4 "Cash close GBP").
Tolerances (brief §4): close |Δ| ≤ 5, open/high/low |Δ| ≤ 10; close wrong by > 15 or an RSI2 that does not reproduce = Category 3 failure.

## Machine-readable result
```
c1=3
c2=4
c3=2
c4=2
c5=4
total=61
band=Moderate
override=none
card_integrity=96.7
n_cards=3
n_duds=0
n_warns=1
```

## 1. Section 7 checklist (every row)

| Row | Item | Notes | Evidence (location) | Score |
|---|---|---|---|---|
| 1.1 | Variables respected | Asset (FTSE cash, Euro Stoxx reference), counters (USDX, S&P 500, DAX 40, Euro Stoxx), as-of 10 Jun Europe/London, 5-session lookback, GBP/points all respected. Deviations: Trade 1 anchor overridden to 00:00 UK (baseline 07:00) — disclosed, "per the run instruction". Source tiers: no index-provider/exchange or sell-side price source actually used (LSE/FTSE Russell row is a 52-week reference only; prices are CNBC/Yahoo/TE/BBNTimes). | §2, §4, §20, §21b | 3 |
| 1.2 | Coverage & currency consistent | All dates ≤ D-1 for data; no unit drift. Drift point: daily pivots are built from the 8 Jun H/L/C (D-2), not 9 Jun (D-1), so the "daily pivot for 10 Jun" is one session stale. Several items undated (T. Rowe Price "early Jun"; Euro Stoxx futures −1.5%; DAX −0.47%). | §11, §10, §13a | 3 |
| 1.3 | Audience & tone | Senior-strategist register throughout, no retail tone. Mild meta-leak in §19 ("per the run instruction, corroboration was treated leniently so that strategy output is not suppressed") — undermines the review-grade tone. | §1, §18, §19 | 4 |
| 2.1 | Sections present & ordered | §1–§21 all present and in order; §13a–d and §21a–d present; §17 is a single sentence block; charts described in §7 (images dropped by pandoc — captions accepted). | headings | 5 |
| 2.2 | Scorecard / pivots as tables | §6 is a table with Date/O/H/L/C/RSI2/Trend/Src A/Src B/Validation (no separate "Final" column — Close serves). §11: daily shows 5 levels each side (R5…S5, beyond the specified 3), weekly and monthly show only 2 each side (R3 and S3 missing); not the required R3→P→S3 grid for all three. | §6, §11 | 3 |
| 2.3 | Method steps visible | §4→§5 observations→consensus visible; §8 candle-by-candle + sequence present; §9 regime with VOLator and KER present but overlap/persistence not quantified and ATR(14) never stated; §7 chart captions present. Several §8 candle descriptions contradict §6 (see 3.4). | §4–§9 | 4 |
| 3.1 | Quantitative claims sourced | Unsourced figures in §12/§14: US CPI "~3.8%", GBP/USD "near 1.34", "Kevin Warsh" as Fed Chair, "~80% of range", FTSE VOLator "+1.0 / slope +0.07", "FOMC 16–17 Jun" (outside the calendar slice). Counter moves (DAX −0.47%, futures −1.5%) carry no source or date. | §10, §12, §14 | 3 |
| 3.2 | Citations exist & contain data | Cannot fetch; three spot-checks. (a) CNBC 9 Jun close 10,227.33 / low 10,227.33: used consistently in §1, §3, §6 — consistent. (b) BBNTimes 5 Jun 10,368.05 (+7.73), prev 10,360.32: arithmetic consistent (10,368.05 − 7.73 = 10,360.32) and used in §6. (c) Yahoo/PA 9 Jun "(−145.87)": implies prior close 10,373.20, but the report's own 8 Jun close is 10,370.20 (down 142.87, not 145.87; Δ3.00); CNBC 8 Jun "FTSE +0.05%" vs report closes 10,368.05→10,370.20 = +0.02%. No impossible date or URL found, so fabricated-source override NOT triggered, but (c) is a self-contradictory figure and is scored. | §1, §4, §13a | 3 |
| 3.3 | Calculations transparent | RSI2 reproduces from the report's own closes: 100.0 / 100.0 / 1.48 (report 100 / 100 / 1.5) — PASS. Trend labels obey the Close/Open + RSI2 rule on 5, 8, 9 Jun. Pivot arithmetic is correct for the inputs used (8 Jun H 10,409.33, L 10,319.17, C 10,370.20 → P 10,366.23, R3 10,503.46, S3 10,232.98) but wrong session; weekly/monthly H/L/C inputs not shown (implied: week H 10,470.1/L 10,300.1; May H 10,698.3/L 10,151.6). RSI2 left blank for 3 and 4 Jun. ATR(14) never stated numerically (implied ≈ 80.7 from the card: 0.25×ATR = 20.17, 3.5×ATR = 283 → 80.9). Level file: ATR14 cash 99.91 (−19%). KER −0.87 not reproducible (13 daily cash closes, EMA3: ≈ −0.11). §21a score not traceable: sentiment −0.31×0.10 = −0.031, not "−0.05"; "three highest-weighted contributors" lists sentiment (weight 0.10, the lowest) instead of the 0.20/0.15 signals; six signal×weight terms never shown. | §6, §9, §11, §21a | 2 |
| 3.4 | Numbers reconcile | See Category 3 discrepancy table below. Internal breaks: "down 145.87" vs 10,370.20−10,227.33 = 142.87; §8 "5 Jun close ~80% of range" (own table: (10,368.05−10,331)/70 = 53%); §8 "8 Jun narrow-range inside-day" while its H 10,409.33 > 5 Jun H 10,401 (not an inside day); 25-session high 10,615 on Trade 3C vs "~10,560 area" in §7; Trade 2 "10,148 already passed" while 10,148 lies between entry 10,189 and TP1 10,082. D-1 close 10,227.33 is identical in §1/§3/§4/§6/§21b entry (good) but 13.4 pts below the cash level file (10,240.7); 3 Jun and 4 Jun closes are > 15 pts off (16.3, 17.0). Daily pivots 83–163 pts off; monthly May high overstated by 138. | whole report | 1 |
| 4.1 | Pillars conclude | §8 "Bearish continuation", §9 "Bias: Bearish", §10 "MIXED" end in labels. §12 and §14 close on watch items, not a direction label for the pillar. | §8, §9, §10, §12, §14 | 3 |
| 4.2 | Cross-asset interpreted | §10 gives mechanisms (USD translation for multinationals, common-factor beta, euro-area proxy), good. But premises are misread against the counter slices: USDX 5-day is rising, not "Falling" (99.553 on 3 Jun → 99.972 on 9 Jun, +0.42%; peak 100.17 on 7 Jun); S&P 500 5-day is falling, not "Rising" (7,536.2 → 7,383.6, −2.0%, −2.86% on 5 Jun, −0.32% on 9 Jun) so the "FTSE fell while S&P rose" divergence is unsupported. | §10, §15 | 3 |
| 4.3 | Synthesis reconciles tensions | §9 reconciles KER vs VOLator to TRANSITION; §16/§18 reconcile bounce vs bearish bias. But §21a states "Conflict flag: none" while §16/§17 forecast an initial counter-bounce against a SHORT entered at the D-1 close, and the regime resolution rests on a KER (−0.87) that does not reproduce; the §21a total is not derivable. | §9, §16, §17, §21a | 2 |
| 4.4 | Calibrated language | §17 is exactly one sentence; confidence "Medium" stated in §1, §3, §18. Sentence nonetheless carries two opposing legs plus a contingency (lower bias, counter-bounce, contingent on CPI). | §3, §17 | 3 |
| 4.5 | Card construction (protocol Category 4) | See Card Integrity and feedback. Trade 1: stop not the tighter of swing/nearest S/R; TP3 between TP1 and TP2 (linter WARN); Unit 3 stop "entry +0.2R (10,267)" on the adverse side of a short; ATR not stated. Trade 2: entry/TP3 keyed to single-source indicative weekly/monthly tiers, daily tiers from the wrong session, no tranche-management row, sell-stop vs "confirmed close" contradiction. Trade 3C: wrong 25-session boundaries (low 10,227 is the D-1 close, true 25-day low 10,141.2; high 10,615 absent from data, true 10,560.0), R not stated, Unit 3 stop at 10,227 above a 10,205 short entry, TP1 366 pts = 3.7×ATR14. | §21b | 1 |
| 5.1 | Data dated; staleness flagged | Single-source O/H/L flagged (3 Jun) and indicative tiers flagged in §19. Undated: T. Rowe Price "early Jun", Euro Stoxx futures −1.5% pre-open, DAX −0.47%. | §4, §6, §13, §19 | 4 |
| 5.2 | Assumptions up front | Anchor-override caveat is on the Trade 1 card and in §20; single-source propagation appears on Trades 2 and 3C. Not in §1/§2; the "corroboration treated leniently so strategy output is not suppressed" assumption is buried in §19. | §19, §20, §21b | 3 |
| 5.3 | Red flags surfaced | CPI collision carried into all three cards; wide-stop flag and RSI2 snap-back flagged on Trade 1; §15 gives both sides. Omitted: BoC decision (14:45 UK), EIA crude stocks (HIGH, 15:30 UK) from the event-collision caveats. | §12, §13d, §15, §21b | 4 |
| 5.4 | Restrictions honoured | No module codes, no bracketed variables, no framework name. Concerns, all disclosed rather than hidden: opens for 4 and 5 Jun equal the prior close (10,358.00; 10,360.32) and 3 Jun O/H/L are round numbers (probable estimates); TE "≈10,370 (+2)" normalised to 10,370.20 (false precision); §7 25-session chart is an "indicative reconstruction". Daily tier labelled CORROBORATED although built from the wrong session. Not an open breach, so no override. | whole report | 3 |

## 2. Category 3 data comparison (report vs level file / slice, cash basis)

Report column O/H/L/C vs `UK100_by_date/2026-06-10.csv` / slice cash session. Δ = report − slice. Flags: * beyond tolerance (close > 5, O/H/L > 10); ** close > 15 (Category 3 failure per brief §4).

| Session | Field | Report | Slice (cash) | Δ | Flag |
|---|---|---|---|---|---|
| Wed 3 Jun | O / H / L / C | 10,342.0 / 10,402.0 / 10,300.0 / 10,358.0 | 10,351.4 / 10,384.0 / 10,320.7 / 10,341.7 | −9.4 / +18.0 / −20.7 / +16.3 | H*, L*, C** |
| Thu 4 Jun | O / H / L / C | 10,358.0 / 10,402.0 / 10,318.0 / 10,360.32 | 10,301.0 / 10,360.2 / 10,236.5 / 10,343.3 | +57.0 / +41.8 / +81.5 / +17.0 | O*, H*, L*, C** |
| Fri 5 Jun | O / H / L / C | 10,360.32 / 10,401.0 / 10,331.0 / 10,368.05 | 10,383.0 / 10,417.0 / 10,331.9 / 10,374.2 | −22.7 / −16.0 / −0.9 / −6.2 | O*, H*, C* |
| Mon 8 Jun | O / H / L / C | 10,369.05 / 10,409.33 / 10,319.17 / 10,370.20 | 10,309.9 / 10,412.8 / 10,307.1 / 10,370.4 | +59.2 / −3.5 / +12.1 / −0.2 | O*, L* |
| Tue 9 Jun (D-1) | O / H / L / C | 10,372.0 / 10,372.77 / 10,227.33 / 10,227.33 | 10,353.9 / 10,368.7 / 10,240.5 / 10,240.7 | +18.1 / +4.1 / −13.2 / −13.4 | O*, L*, C* |

RSI2: report 100.0 (5 Jun), 100.0 (8 Jun), 1.5 (9 Jun) vs slice cash 100.00 / 89.05 / 0.00 (different closes; the report's own arithmetic reproduces: 100 / 100 / 1.48). 3 Jun and 4 Jun left blank (slice 60.12 / 4.51). ATR14: not stated; implied ≈ 80.7 vs level file cash 99.91 (full 126.28). 5-day swing high used 10,409.33 vs 10,417.00 (cash, 5 Jun).

Daily pivots (report: derived from 8 Jun H/L/C; level file: derived from D-1 9 Jun cash session):

| Level | Report | Level file `d_cash` | Δ |
|---|---|---|---|
| R3 | 10,503.5 | 10,454.3 | +49.2 |
| R2 | 10,456.4 | 10,411.5 | +44.9 |
| R1 | 10,413.3 | 10,326.1 | +87.2 |
| P | 10,366.2 | 10,283.3 | +82.9 |
| S1 | 10,323.1 | 10,197.9 | +125.2 |
| S2 | 10,276.1 | 10,155.1 | +121.0 |
| S3 | 10,233.0 | 10,069.7 | +163.3 |

(Even the report's own 9 Jun H/L/C would give P = 10,275.8, so the stale-session error is internal as well.)

Weekly (W/E 5 Jun) vs `w_cash`: P 10,379.4 vs 10,342.6 (+36.8); R1 10,458.7 vs 10,448.6 (+10.1); R2 10,549.4 vs 10,523.1 (+26.3); S1 10,288.7 vs 10,268.1 (+20.6); S2 10,209.4 vs 10,162.1 (+47.3); R3/S3 (10,629.1 / 10,087.6) not given.

Monthly (May) vs `m_cash`: P 10,423.3 vs 10,370.4 (+52.9); R1 10,695.0 vs 10,599.6 (+95.4); R2 10,970.0 vs 10,789.2 (+180.8); S1 10,148.3 vs 10,180.8 (−32.5); S2 9,873.3 vs 9,951.6 (−78.3); R3/S3 (11,018.4 / 9,762.0) not given. Implied May high 10,698.3 vs 10,560.0 (+138.3).

25-session range used on Trade 3C: 10,227 – 10,615 (width 388) vs level file cash 10,141.2 – 10,560.0 (width 418.8); full-day 10,107.0 – 10,560.0.

Counter checks: USDX 5-day rising (+0.42% 3→9 Jun), S&P 500 5-day falling (−2.0%) — both opposite to §10 directions.

Calendar check (news slice): US CPI 15:30 broker = 13:30 UK on 10 Jun, HIGH — present. BoC decision (14:45 UK, HIGH) and China CPI present. "UK monthly GDP 10–12 Jun": no GBP event on 10 Jun in the calendar slice. Omitted from §13c/§13d: ECB Lagarde speech 9 Jun (HIGH), US EIA crude stocks 10 Jun 15:30 UK (HIGH), US 10-Year Note Auction 10 Jun 18:00 UK (HIGH).

## 3. Category roll-up

| Cat | Max | Rows | Mean | Level | Multiplier | Points | Justification |
|---|---|---|---|---|---|---|---|
| 1 Prompt adherence | 20 | 3, 3, 4 | 3.33 | 3 | 0.65 | 13.00 | Asset, counters, window and currency respected; anchor overridden, source tiers thin, pivots one session stale. |
| 2 Structure | 20 | 5, 3, 4 | 4.00 | 4 | 0.85 | 17.00 | All 21 sections and sub-sections in order; pivot grids deviate (daily 5 levels, weekly/monthly 2). |
| 3 Accuracy & evidence | 25 | 3, 3, 2, 1 | 2.25 | 2 | 0.40 | 10.00 | Two closes > 15 pts off, opens/lows off by up to 82, daily pivots stale (83–163 pts), May high +138, ATR/KER not reproducible, own-table breaks; RSI2 arithmetic is correct. |
| 4 Reasoning & judgment | 20 | 3, 3, 2, 3, 1 | 2.40 | 2 | 0.40 | 8.00 | Mechanisms present but counter directions inverted; §21a not traceable; all three cards carry construction defects. |
| 5 Currency & transparency | 15 | 4, 3, 4, 3 | 3.50 (rounded up) | 4 | 0.85 | 12.75 | Overrides and indicative tiers disclosed, CPI collision carried to cards; some undated items and buried assumption. |

## 4. Total, band, override

Total = 13.00 + 17.00 + 10.00 + 8.00 + 12.75 = 60.75 → **61**. Band: **Moderate Trust (60–74)**.

Override check: fabricated source — not triggered (no impossible URL/date found; the −145.87 and +0.05% mismatches are reconciliation failures, scored under 3.2/3.4). Restriction breach — not triggered (anchor override and indicative inputs are disclosed). `override=none`.

## 5. Card Integrity (linter rows copied verbatim from `qa/ftse_qa1/lint_static/2026-06-10.csv`; separate from the 100)

| card_id | strategy | flags | dud | Card Integrity |
|---|---|---|---|---|
| 2026-06-10_Trade_1 | Trade 1 - Daily Directional (SHORT) | WARN_TP3_ORDER | False | 90 |
| 2026-06-10_Trade_2 | Trade 2 - Pivot (TRANSITION, breakout side only) - SHORT | CLEAN | False | 100 |
| 2026-06-10_Trade_3C | Trade 3C - Momentum-Breakout (TRANSITION) - SHORT | CLEAN | False | 100 |

n_cards = 3 (none suppressed) · n_duds = 0 · n_warns = 1 · report-level Card Integrity = (90 + 100 + 100)/3 = **96.7**.

Reviewer note (not part of the linter number, not re-derived): the static linter cannot see the Unit 3 stop sign on Trades 1 and 3C or the missing R on Trade 3C; those and the other card defects are in `2026-06-10_feedback.md` and were scored under row 4.5.
