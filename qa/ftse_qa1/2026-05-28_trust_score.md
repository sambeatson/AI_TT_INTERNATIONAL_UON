# Trust Score v3.7 — FTSE_EuroStoxx_Daily_28May2026.md (D = 2026-05-28)

Reviewer run: ftse_qa1. Level file `data/levels/UK100_by_date/2026-05-28.csv` has `last_bar_date = 2026-05-27` (< D), so it is leak-free. All data comparisons use the cash basis (`_cash`), which is the basis the report claims (official LSE close, 08:00-16:30 London). Full-day (`_full`) values are quoted only where useful.

## Score line (machine-readable)

```
c1=3
c2=3
c3=2
c4=3
c5=3
total=59
band=Low
override=restriction_breach
card_integrity=100
n_cards=3
n_duds=0
n_warns=0
```

`override=restriction_breach`: the Moderate cap (74) is not binding at 59, but C1 is reduced one level (4 to 3). No hallucinated-source override was applied (see 3.2 for the borderline Yahoo row).

## 1. Section 7 checklist

| Row | Reviewer notes | Evidence (location) | Score |
|---|---|---|---|
| 1.1 Variables respected | Asset is FTSE 100 cash index; counters USDX / S&P 500 / DAX 40 plus Euro Stoxx 50 reference; as-of 28 May Europe/London; lookback 5/25; GBP and points; anchor 07:00 UK. Defects: (a) §4 lists 6 rows but only 5 distinct sources (Yahoo counted twice) and no sell-side tier, versus the 6-source requirement; (b) anchor narrative is self-contradictory: §2 says the anchor was "overridden from the M1 default" to 07:00, §20 says it was overridden "from 07:00 ... to the report as-of date" while "anchor time remains 07:00". | §2, §4, §20 | 3 |
| 1.2 Coverage and currency consistent | Data dates are all D-1 or earlier; currency handling is consistent (EUR native for STOXX). Calendar/date drift: "Fri 30 May" is a Saturday, "Mon 2 Jun" is a Tuesday, "Wed 4 Jun" is a Thursday (§12, §13d). §1 says 27 May is "the third consecutive up day since the Spring Bank Holiday" but only 26 and 27 May have traded since it (§8 says four consecutive higher closes, Thu-Wed). | §1, §8, §12, §13d | 4 |
| 1.3 Audience and tone | Institutional tone, no retail language. | §1, §18 | 4 |
| 2.1 Sections present and ordered | §1 to §21 present in order; §13a-d and §21a-d present. Minor: §11 ladders deviate from the 3-each-side R3-to-S3 spec (weekly has R5..S5; daily and weekly carry R1.5/S1.5). | headings, §11 | 4 |
| 2.2 Scorecard as a table | §6 is a table, but it carries only Open/High/Low/Close/Δpts/Δ%/RSI2. The required Trend, Source A, Source B, Final and Validation columns are absent. §11 pivots are tables (weekly, daily, monthly). | §6, §11 | 3 |
| 2.3 Method steps visible | §4-§5 observations to consensus visible; §8 candle-by-candle and sequence present; §9 regime states a label but persistence/overlap evidence is asserted, not shown, and the asserted figures do not reproduce (see 3.4). §7 has no charts: it states the charts "are not embedded" (placeholder/caption only; accepted as a caption per brief, but noted). | §4-§9 | 3 |
| 3.1 Quantitative claims sourced | §1, §3, §4, §6 point to §4 rows. §12 and §14 carry many unsourced figures (sector weights "~16% energy / ~12% banks / ~14% staples", "~80% dollar-exposed", Brent "<$100", GBP/USD ~1.35, EUR/USD ~1.13, VIX 16.87, BoE "50/50" pricing). Several sourced figures also fail the data check (ATR, weekly/monthly pivots, 25-day statistics; see 3.4). | §12, §14, §9 | 2 |
| 3.2 Citations exist and contain data | Three checked: (1) FTSE Russell 27 May close 10,508.88 consistent throughout; (2) Reuters/TE "rose 32 points or 0.31 percent on Tuesday" matches §6 (+32.04, +0.31%); (3) Yahoo ^FTSE "10,508.88 (+0.17%)" contradicts the report's own §6 (+0.10%, i.e. 10.58 / 10,498.30) and the TE row "+0.08%". The Yahoo percentage is a self-contradictory figure. Judgement call: the close figure in the quote is consistent and the contradiction is a percentage field only, so recorded as a defect rather than a fabricated source; no override. §4 also says "Retail CFD quotes excluded" while listing a Trading Economics CFD-proxy row. | §4, §6, §13a | 3 |
| 3.3 Calculations transparent | RSI2 values (62, 78, 92, 94) are not shown and do not reproduce: from the report's own closes (10,443.50, 10,466.26, 10,498.30, 10,508.88; every change positive) the 2-period RS has zero losses, so RSI2 = 100 for 22, 26 and 27 May (`qa_slice_stats --closes`). Data RSI2 (cash) = 100.0. ATR(14) is "estimated as a rough 75 points" (not computed): data ATR14 = 120.51 (cash) / 146.49 (full), so understated by 45.5 pts (-38%) on the cash basis. KER stated as "≈ +0.30" with no window/smoothing parameters (reproduces at 0.30 for raw 13-session KER; 0.375 with EMA3). Sentiment tilt arithmetic is wrong in sign: 0.5+0.5-1.0-1.0+0+0 = -1.00, not +1.00; tilt = -1.00/4.20 = -0.238, not +0.24; then +0.30 is used in the score with no derivation. §21d mean R: (1.0+1.5+0.8+0.5)/4 = 0.95, not 0.83. Pivot formulas do reproduce from the report's own H/L/C inputs (daily P = 10,506.29; weekly P = 10,449.52) but the inputs are wrong. | §6, §8, §9, §13b, §19, §21d | 1 |
| 3.4 Numbers reconcile | D-1 close 10,508.88 is identical in §1, §3, §4, §6, §21b (vs cash close 10,507.9: Δ +1.0, OK). Breaks: Yahoo +0.17% vs §6 +0.10%; Trade 2 invalidation "~9 points above SL" vs "58 points" in the same cell; §1 "third consecutive up day" vs §8 "four"; §8 "10,522 intraday high" on 26 May vs §11 weekly-high 10,522.30 attributed to W/E 22 May while §6 shows week highs of 10,475 / 10,488; Trade 1 "5-day swing low 10,443" is not a low in the report's own §6 (lowest low 10,408); §21c 27 May "TP1 reached intraday" although TP1 is above the stated 27 May high (10,523). Data check below. | cross-section | 2 |
| 4.1 Pillars conclude | §8, §9, §10 end in explicit labels (Trending - Bullish, TREND_UP, CONFIRM). §12 and §14 end descriptively with no direction label. | §8-§14 | 3 |
| 4.2 Cross-asset interpreted | §10 gives a mechanism per counter (earnings translation, cross-Atlantic beta, cyclical read-across). Oil/energy weight handled in §12/§14 rather than §10. S&P is quoted to 26 May though a 27 May close was available (stale by one session). | §10 | 4 |
| 4.3 Synthesis reconciles tensions | RSI2/compression caveats are named. Not reconciled: the numeric sentiment tilt (-0.24 correct arithmetic) vs the +0.30 input; the 25-day regime narrative vs data (below); Trade 2 "pullback-and-re-break" vs Trade 1 market-long in the same direction and day; §13d PCE misdated. | §13b, §15-§18, §21a | 2 |
| 4.4 Calibrated language | §17 is exactly one sentence; confidence Medium stated with reasons in §3 and §18. | §3, §17, §18 | 4 |
| 4.5 Card construction (protocol: scored under C4) | Trade 2 should be a SUPPRESSED row: §19 states weekly, daily and monthly pivots are all single-source-indicative, and the card is produced "per analyst instruction" (a run-time instruction may not override suppression, and may not appear in the report). Trade 2 is a BUY STOP at 10,458.47, below the D-1 close 10,508.88 (wrong side; §5.0). ATR input 75 vs 120.51; no R÷ATR or wide-stop flag printed on any card; reference close and signed gap not printed; Trade 3A swing endpoint (~10,100, mid-April) lies outside the 4-10 session lookback and its high 10,522 is not the data 5-day high (10,560.0, 26 May); Trade 3A Unit 3 override uses the wrong midpoint. Trade 1 stop anchored on a non-existent 10,443 swing. Detail in feedback. Linter rows are CLEAN (static); those are copied verbatim below and are not altered by this row. | §21b | 1 |
| 5.1 Data dated, staleness flagged | Closes and articles are dated; single-source H/L flagged in §6, §11, §19. EBC article dated only "May 2026"; S&P 500 and VIX quoted to 26 May (Tue) rather than 27 May. | §4, §6, §13a, §19 | 4 |
| 5.2 Assumptions up front | Pivot single-source propagation is stated on Trade 2; anchor-override caveat present but contradictory (§2 vs §20). ATR "rough 75" appears only in §19, not in §9's basis, §1, or on any card. | §2, §19, §20, §21b | 3 |
| 5.3 Red flags surfaced | Risks in §12/§15 are sensible and §13d collisions are carried into card caveats, but the calendar is wrong: slice shows US PCE (Core PCE, PCE Price Index), GDP q/q, Durable Goods, Initial/Continuing Claims, New Home Sales scheduled on D itself (28 May, 13:30-15:00 London) and an ECB Schnabel speech 16:45 London, whereas the report puts PCE on "Fri 29 May" and omits these D-day events; "Fri 30 May" is a Saturday. §13c puts UK CPI on Thu 21 May: the calendar shows it on 20 May (also omits the UK PMI prints on 21 May: services 47.9 vs 51.8 consensus). | §12, §13c, §13d, §21b | 3 |
| 5.4 Restrictions honoured | Breached. Bracketed variable name `[DAILY_OPEN_ANCHOR]` (§20); module codes "M1 default" (§2, §20) and "M5 trace" (§20 four times); "per §5.2b", "§5.3a", "Step 4 / Step 5c / Step 7" in the report and §21b; "v2.1 framework deployment" and "session 1 of 20 for this populated instance" (§20); a run-time "analyst instruction" cited as authority to ship a suppressed card (§19, §20, §21b Trade 2). "Beatson-style" in §9 names a methodology/author. | §2, §9, §19, §20, §21b | 1 |

## 2. Category roll-up

| # | Category | Rows (mean) | Level | Multiplier | Points | Justification |
|---|---|---|---|---|---|---|
| 1 | Prompt adherence (20) | 3,4,4 = 3.67 → 4; restriction breach -1 | 3 | 0.65 | 13.00 | Variables mostly respected; source count and anchor narrative defective; override drops one level. |
| 2 | Structure (20) | 4,3,3 = 3.33 → 3 | 3 | 0.65 | 13.00 | All sections present; §6 table lacks five required columns; no charts. |
| 3 | Accuracy and evidence (25) | 2,3,1,2 = 2.00 | 2 | 0.40 | 10.00 | RSI2 and ATR not reproducible; OHLC/pivots off the data; tilt arithmetic sign error. |
| 4 | Reasoning and judgment (20) | 3,4,2,4,1 = 2.80 → 3 | 3 | 0.65 | 13.00 | Good section-level labels and mechanisms; card construction and synthesis weak. |
| 5 | Currency, restrictions, transparency (15) | 4,3,3,1 = 2.75 → 3 | 3 | 0.65 | 9.75 | Dated data; calendar errors; restriction breaches. |

## 3. Total, band, override

- Total = 13.00 + 13.00 + 10.00 + 13.00 + 9.75 = 58.75, rounded to **59**.
- Band: **Low** (40-59).
- Override: **restriction_breach** (module codes, bracketed variable name, framework version, and a run-time instruction used to override a required suppression). Moderate cap (74) not binding; C1 reduced one level.
- Hallucinated-source override: not applied (Yahoo percentage mismatch recorded as a 3.2 defect; no impossible or undated source found).

## 4. Category 3 data check (report vs `data/levels/UK100_by_date/2026-05-28.csv`, cash basis)

Tolerances (brief §4): |Δ| ≤ 5 on close, ≤ 10 on open/high/low. Δ = report minus data.

| Session | Field | Report | Data (cash) | Δ | Verdict |
|---|---|---|---|---|---|
| Thu 21 May | Open | 10,420 | 10,371.1 | +48.9 | FAIL |
| | High | 10,475 | 10,469.1 | +5.9 | ok |
| | Low | 10,408 | 10,344.7 | +63.3 | FAIL |
| | Close | 10,443.50 | 10,462.3 | -18.8 | FAIL (>15) |
| Fri 22 May | Open | 10,443 | 10,492.6 | -49.6 | FAIL |
| | High | 10,488 | 10,494.5 | -6.5 | ok |
| | Low | 10,462 | 10,446.0 | +16.0 | FAIL |
| | Close | 10,466.26 | 10,470.4 | -4.1 | ok |
| Tue 26 May | Open | 10,478 | 10,531.9 | -53.9 | FAIL |
| | High | 10,522 | 10,560.0 | -38.0 | FAIL |
| | Low | 10,475 | 10,498.0 | -23.0 | FAIL |
| | Close | 10,498.30 | 10,500.7 | -2.4 | ok |
| Wed 27 May (D-1) | Open | 10,498 | 10,487.7 | +10.3 | marginal fail |
| | High | 10,523 | 10,523.5 | -0.5 | ok |
| | Low | 10,487 | 10,460.6 | +26.4 | FAIL |
| | Close | 10,508.88 | 10,507.9 | +1.0 | ok |

Closes: 2 of 4 within tolerance and one (21 May) off by more than 15 pts. D-1 close and D-1 high agree; D-1 low is 26.4 too high (and so compresses the daily ladder).

| Item | Report | Data (cash) | Δ | Note |
|---|---|---|---|---|
| RSI2 27 May | 94 | 100.0 | -6.0 | Report's own closes also give 100.0; 78/92/94 do not reproduce. |
| ATR(14) | ~75 ("rough") | 120.51 (full 146.49) | -45.5 | Understated 38%; drives stop buffer, caps, TP3. |
| Daily P | 10,506.29 | 10,497.33 | +8.96 | |
| Daily R1 / S1 | 10,525.59 / 10,489.59 | 10,534.07 / 10,471.17 | -8.5 / +18.4 | |
| Daily R2 / S2 | 10,542.29 / 10,470.29 | 10,560.23 / 10,434.43 | -17.9 / +35.9 | |
| Daily R3 / S3 | 10,561.59 / 10,453.59 | 10,596.97 / 10,408.27 | -35.4 / +45.3 | |
| Weekly H / L / C | 10,522.30 / 10,360.00 / 10,466.26 | 10,494.5 / 10,141.2 / 10,470.4 (implied by data pivots) | +27.8 / +218.8 / -4.1 | Weekly low is wrong by 219 pts. |
| Weekly P | 10,449.52 | 10,368.70 | +80.8 | Key level for Trade 2 and the invalidation. |
| Weekly R1 / S1 | 10,539.04 / 10,376.74 | 10,596.20 / 10,242.90 | -57.2 / +133.8 | |
| Weekly R2 / S2 | 10,611.82 / 10,287.22 | 10,722.00 / 10,015.40 | -110.2 / +271.8 | |
| Weekly R3 / S3 | 10,701.34 / 10,214.44 | 10,949.50 / 9,889.60 | -248.2 / +324.8 | |
| Monthly P (Apr) | 10,270 | 10,418.80 | -148.8 | Report values are round tens and described as "reconstructed". |
| Monthly R1 / S1 | 10,460 / 10,080 | 10,650.0 / 10,140.1 | -190 / -60.1 | |
| Monthly R2 / S2 | 10,650 / 9,890 | 10,928.7 / 9,908.9 | -278.7 / -18.9 | |
| 5-day swing (cash) | low 10,443 (Trade 1 stop anchor) | low 10,272.8 (20 May), high 10,560.0 (26 May) | +170.2 | |
| 25-day range (cash) | "late-April low near 10,025" | low 10,141.2 (18 May), high 10,638.9 (21 Apr) | n/a | No close in the window is as low as 10,025; the window high is above the D-1 close. |
| 25-day mean | "near 10,310" | 10,357.5 | -47.5 | |
| Negative sessions in 25 | "only six" | 11 | | |
| Mean daily change over 25 | "+0.18%" | +0.006% | | Window opens at 10,504.4 (21 Apr) and ends at 10,507.9: net ≈ +0.03%, not "+4.8%". |
| §1 "fresh multi-week high" / §9 "fresh swing high" | | D-1 close 10,507.9 is 131.0 below the 25-day high 10,638.9 and 52.1 below the 5-day high 10,560.0 | | Regime narrative not supported by the slice; the TREND_UP label itself rests mainly on the KER (0.30). |
| USDX / S&P 500 / VIX (27 May) | 99.19 / 7,519.12 (26 May) / 16.87 | 99.226 / 7,522.5 (26 May), 7,543.0 (27 May) / 17.13 (CFD 27 May) | small | VIX source basis differs; S&P stale by one session. |

## 5. Card Integrity (linter rows copied verbatim from `qa/ftse_qa1/lint_static/2026-05-28.csv`)

| card_id | report_date | strategy | flags | dud | #DUD | #WARN | Card Integrity |
|---|---|---|---|---|---|---|---|
| 2026-05-28_Trade_1 | 2026-05-28 | Trade 1 - Daily Directional | CLEAN | False | 0 | 0 | 100 |
| 2026-05-28_Trade_2 | 2026-05-28 | Trade 2 - Pivot (regime-aware, TREND_UP branch - pivot breakout LONG) | CLEAN | False | 0 | 0 | 100 |
| 2026-05-28_Trade_3A | 2026-05-28 | Trade 3A - Momentum-Pullback (TREND_UP regime fork; LONG) | CLEAN | False | 0 | 0 | 100 |

Report-level Card Integrity = mean(100, 100, 100) = **100** (n_cards=3, n_duds=0, n_warns=0). The static linter does not test the §5.0 order-side rule against the D-1 close for Trade 2, nor suppression gates; those defects are scored under 4.5 and listed in the feedback, not folded into this number.

## 6. Feedback

See `qa/ftse_qa1/2026-05-28_feedback.md`.
