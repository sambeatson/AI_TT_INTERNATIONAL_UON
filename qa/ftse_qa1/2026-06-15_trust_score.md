# Trust Score v3.7 QA — FTSE 100 daily report, D = 2026-06-15

Report: `reports/md/FTSE_EuroStoxx_Report_15Jun2026.md` · run ftse_qa1 · D-1 = Fri 2026-06-12
Level file check: `last_bar_date` = 2026-06-12 < D (2026-06-15). Slice last bar 2026-06-12 22:45 broker. No leak. `qa_slice_stats.py` run with `--cash-open 10:00 --cash-close 18:30` and `--closes 10373.20 10227.33 10254.81 10303.88 10471.72`.

## Machine-readable result
```
c1=4
c2=4
c3=2
c4=3
c5=4
total=70
band=Moderate
override=none
card_integrity=83.3
n_cards=3
n_duds=1
n_warns=1
```

## 1. Section 7 checklist

| Row | Reviewer notes | Evidence observed | Score |
|---|---|---|---|
| 1.1 Variables respected | FTSE 100 cash is the primary asset; Euro Stoxx 50 is secondary with no cards; counters USDX / S&P 500 / DAX 40 (VIX in §14); as-of 12 Jun London close; 5/25-session lookbacks; GBP/points. Anchor overridden to 00:00 UK (baseline 07:00): disclosed in header, §2, §20 but not as a caveat on any card. Source set is index-provider / exchange-aggregator / portal heavy; no sell-side tier in §4. | Header, §2, §4, §20, §21b | 4 |
| 1.2 Coverage & currency consistent | Data dates are D-1 or earlier, run date D. Calendar drift: §21c labels 5 Jun as "Thu" (it is a Friday) and labels Thu 11 Jun as t−1 (D-1 is Fri 12 Jun, absent from the table); §13d labels UK CPI "Wed 18 Jun" and labour data "Thu 19 Jun" (18 Jun is a Thursday, 19 Jun a Friday). | §13d, §21c | 3 |
| 1.3 Audience & tone | Strategist register, risk-review framing, no retail tone. | §1, §18 | 5 |
| 2.1 Sections present & ordered | §1–§21 all present and in order; §13a–d and §21a–d present; §17 is one sentence; §7 holds five caption-only chart placeholders (pandoc dropped images; accepted as evidence). | headings | 5 |
| 2.2 Scorecard as a table | §6 is a table but has no Source A / Source B / Final columns (sources are in a footnote only). §11 daily table is split R5→P→S5 (5 levels each side, brief expects 3) and weekly and monthly pivot tables are absent entirely ("not computed"), although both are derivable (see feedback #5). | §6, §11 | 2 |
| 2.3 Method steps visible | §4→§5 observation to consensus is shown; §8 is candle by candle with a sequence call; §9 gives overlap 0.20, persistence 0.50, range position, VOLator readings, KER +0.25. ATR(14) never printed and KER derivation not shown. | §4–§9 | 4 |
| 3.1 Quantitative claims sourced | §1 and §11 trace to §4/§6; §12 and §14 carry many figures (stock moves, WTI ~$85, "CPI at 3-yr high", "Dec hike fully priced", USDX 99.8, VIX 17.68) with no source tag or pointer. §13a gives domain-only URLs and no article dates. | §12, §13a, §14 | 3 |
| 3.2 Citations exist & contain data | Three checks. (a) Trading Economics: raw "10,462 (rounded)" normalised to "≈10,472"; a 10-pt gap is not rounding and the quote does not match its own normalisation (the raw figure is in fact close to the feed: 10,460.9 full-day close). (b) Investing.com "12 Jun range 10,302.68–10,471.72": the low contradicts the feed's 12 Jun low of 10,368.3 (Δ −66). (c) T. Rowe Price "+1.00% on week": feed gives +0.82% (10,374.2 → 10,459.5), a plausible basis gap, so not contradicted. I cannot fetch; (a) and (b) are inconsistencies, not proven fabrication, so the override is NOT applied. Judgement call, flagged for the central review. | §4, §13a | 2 |
| 3.3 Calculations transparent | Daily pivots reproduce exactly from the report's own H/L/C (P 10,415.37, R1 10,528.07, R2 10,584.41, R3 10,697.11, S1 10,359.03, S2 10,246.33, S3 10,189.99). RSI2 does NOT reproduce: from the report's own closes the tool gives 15.9 / 100 / 100 for 10, 11, 12 Jun versus 63.7 / 91.6 / 91.6 stated; identical 91.6 on two consecutive days after a +167.8 pt up-day is not possible under any seed; "Wilder" claimed where the M3 definition is a 2-period simple mean. 08 Jun RSI2 2.8 is explained as "post down-leg" but the feed shows 3 / 4 / 5 Jun closes of 10,341.7 / 10,343.3 / 10,374.2 (rising to flat): the feed value is 89.05. ATR(14) not stated (the stop arithmetic implies ≈131.8, close to the feed's 132.06 full-day ATR). §21a lists only three of six signal contributions (0.25+0.10+0.06 = 0.41 of 0.54). The "5-DMA reconciles exactly to the independently published 5-DMA" check in §5/§20 is circular (it is the mean of the same five closes, 10,326.19). | §5, §6, §9, §20, §21a | 2 |
| 3.4 Numbers reconcile | D-1 close 10,471.72 identical in §1, §3, §4, §6, §21b, and §11 pivots equal the pivots quoted on cards. Breaks: Trade 1 confluence says "TP1 sits beyond daily R3" but TP1 10,673.72 < report R3 10,697.11; Trade 1 stop is described as "SL near S1/S2" and "5-day swing-low shelf 10,302.68" but §6's own 5-day low is 10,127.60; Trade 2 TP1 is labelled "+1R-equivalent" but is +112.7 vs R 175.4; §21d says Trade 1 "5/6" and Trade 2 "2/3" triggers while §21c lists 5 Trade 1 and 2 Trade 2 rows; §21c Tue 9 Jun short entered 10,227 and marked 10,255 is shown as +0.4R (sign wrong); "prior-week shelf ~10,557" is the 25-session high (10,560.0 on 26 May), three weeks back. | §8, §11, §21 | 2 |
| 4.1 Pillars conclude | §8 Bullish continuation; §9 Bias Bullish; §10 MIXED; §12 each item tagged; §14 items tagged but no overall direction line. | §8–§14 | 4 |
| 4.2 Cross-asset interpreted | USDX, S&P and DAX each get a mechanism and a status; the FTSE's dollar-earner/energy weight is only touched ("two-sided"); S&P read is mostly common-factor beta. | §10, §12 | 4 |
| 4.3 Synthesis reconciles | DAX divergence, KER vs regime, FOMC and CPI collisions carried through §15–§18 and §21a/§17 consistency stated. Does not reconcile the Transitional regime label with TREND-style pullback cards, nor the "grinds higher" call with RSI2 ~92 as a stated mean-reversion risk. | §9, §15–§18 | 4 |
| 4.4 Calibrated language | §17 is exactly one sentence with one conditional; confidence H stated in §3 despite a 10-pt TE spread and RSI2 irreproducibility. | §3, §17 | 4 |
| 4.5 Card construction (protocol, Cat 4) | Trade 3A: TP1 10,471.72 is below the 10,500 long entry (DUD) and the entry is a breakout stop, not the 57.5% retrace; no BE rule on Unit 2 fill. Trade 1: TP3 10,867.22 < TP2 10,875.72; TP2 (+404) is beyond the 3×ATR cap (396.2); stop anchored to a mis-stated 12 Jun low. Trade 2: regime is "Transitional" (breakout side only) but card is a pullback limit at P; TP1/TP2 are 0.64R / 0.96R, not 1R / 2R; two entries on one card. | §21b, linter | 1 |
| 5.1 Data dated; staleness | All prices dated 12 Jun; STOXX 10–11 Jun and RSI2 seed flagged indicative. §13a articles carry no date and domain-level URLs only; "approx" STOXX closes for 10/11 Jun. | §4, §6, §13a, §19 | 3 |
| 5.2 Assumptions up front | Anchor override in header/§2/§20; ATR/KER window-proxy caveat in §19; single-source pivot propagation stated. Anchor-override and proxy-ATR caveats are not on the cards. | header, §19, §20, §21b | 4 |
| 5.3 Red flags surfaced | §12/§15 risks good; FOMC collision on all three cards; CPI date wrongly weekday-labelled; 12 Jun open/low gap issue not flagged. | §12, §13d, §15, §21b | 4 |
| 5.4 Restrictions honoured | No futures quotes, no retail CFD in the OHLC basis (TE directional only), no module codes or framework name, no bracketed variables. Tickers `^FTSE`/`^STOXX50E` in §2/§6 headings are minor. No clear breach found. | whole report | 4 |

## 2. Category roll-up

| Cat | Max | Rows | Mean | Level | Multiplier | Points | Justification |
|---|---|---|---|---|---|---|---|
| 1 Prompt adherence | 20 | 4,3,5 | 4.00 | 4 | 0.85 | 17.00 | Variables respected; anchor deviation disclosed; calendar weekday drift. |
| 2 Structure | 20 | 5,2,4 | 3.67 | 4 | 0.85 | 17.00 | Complete §1–§21; §6 lacks source columns; weekly/monthly pivots absent. |
| 3 Accuracy & evidence | 25 | 3,2,2,2 | 2.25 | 2 | 0.40 | 10.00 | 12 Jun open/low off by 66 pts, closes off 12–13 pts on two days, RSI2 irreproducible, numbers break across §11/§21. |
| 4 Reasoning & judgment | 20 | 4,4,4,4,1 | 3.40 | 3 | 0.65 | 13.00 | Prose reasoning sound; card construction poor (one DUD, one WARN, regime mismatch). |
| 5 Currency & transparency | 15 | 3,4,4,4 | 3.75 | 4 | 0.85 | 12.75 | Dating and caveats mostly present; articles undated. |

## 3. Total, band, override
- Total = 17.00 + 17.00 + 10.00 + 13.00 + 12.75 = 69.75, rounded to **70**.
- Band: **Moderate** (60–74).
- Override check: hallucinated source: not applied (see 3.2: inconsistencies found but no source proven impossible; flagged for central review). Restriction breach: none found. `override=none`.

## 4. Category 3 data comparison (report vs slice, CFD cash basis 08:00–16:30 London)

| Date | Field | Report | Feed (cash) | Δ | Tolerance | Verdict |
|---|---|---|---|---|---|---|
| 08 Jun | Open | 10,369.05 | 10,309.9 | +59.2 | 10 | FAIL |
| 08 Jun | High | 10,409.33 | 10,412.8 | −3.5 | 10 | ok |
| 08 Jun | Low | 10,319.17 | 10,307.1 | +12.1 | 10 | FAIL (marginal) |
| 08 Jun | Close | 10,373.20 | 10,370.4 | +2.8 | 5 | ok |
| 09 Jun | Open | 10,372.77 | 10,353.9 | +18.9 | 10 | FAIL |
| 09 Jun | High | 10,372.77 | 10,368.7 | +4.1 | 10 | ok |
| 09 Jun | Low | 10,227.33 | 10,240.5 | −13.2 | 10 | FAIL |
| 09 Jun | Close | 10,227.33 | 10,240.7 | −13.4 | 5 | FAIL (<15) |
| 10 Jun | Open | 10,227.38 | 10,251.2 | −23.8 | 10 | FAIL |
| 10 Jun | High | 10,263.81 | 10,267.5 | −3.7 | 10 | ok |
| 10 Jun | Low | 10,127.60 | 10,126.2 | +1.4 | 10 | ok |
| 10 Jun | Close | 10,254.81 | 10,256.3 | −1.5 | 5 | ok |
| 11 Jun | Open | 10,255.16 | 10,238.9 | +16.3 | 10 | FAIL |
| 11 Jun | High | 10,370.15 | 10,373.4 | −3.3 | 10 | ok |
| 11 Jun | Low | 10,252.27 | 10,235.8 | +16.5 | 10 | FAIL |
| 11 Jun | Close | 10,303.88 | 10,299.9 | +4.0 | 5 | ok |
| 12 Jun | Open | 10,302.68 | 10,368.9 | −66.2 | 10 | FAIL (large) |
| 12 Jun | High | 10,471.72 | 10,473.5 | −1.8 | 10 | ok |
| 12 Jun | Low | 10,302.68 | 10,368.3 | −65.6 | 10 | FAIL (large) |
| 12 Jun | Close | 10,471.72 | 10,459.5 (full 10,460.9) | +12.2 (+10.8) | 5 / fail >15 | FAIL (<15) |

- No close is off by more than 15 pts. The 12 Jun open/low errors (≈66 pts) are far outside basis and propagate to §11 and the cards.
- 5-day mean close: report 10,326.19 vs feed 10,325.36 (consistent).
- RSI2 (feed, cash, simple mean): 89.05 / 0.00 / 10.74 / 100 / 100. RSI2 from the report's own closes: n/a / n/a / 15.9 / 100 / 100. Report: 2.8 / 28.9 / 63.7 / 91.6 / 91.6.
- Trend labels vs the stated rule: 10 Jun is Close>Open with RSI2 63.7>50, so the label should be Bullish; the report says Neutral. Other four rows are consistent with the report's own RSI2.
- ATR14: not stated in the report. Feed: 132.06 (full), 106.6 (cash). Implied by the Trade 1 stop arithmetic ≈131.8.
- Daily pivots (report vs level file, cash / full):

| Level | Report | Cash | Δ cash | Full | Δ full |
|---|---|---|---|---|---|
| R3 | 10,697.11 | 10,604.43 | +92.7 | 10,625.73 | +71.4 |
| R2 | 10,584.41 | 10,538.97 | +45.4 | 10,555.57 | +28.8 |
| R1 | 10,528.07 | 10,499.23 | +28.8 | 10,508.23 | +19.8 |
| P | 10,415.37 | 10,433.77 | −18.4 | 10,438.07 | −22.7 |
| S1 | 10,359.03 | 10,394.03 | −35.0 | 10,390.73 | −31.7 |
| S2 | 10,246.33 | 10,328.57 | −82.2 | 10,320.57 | −74.2 |
| S3 | 10,189.99 | 10,288.83 | −98.8 | 10,273.23 | −83.2 |

- Weekly and monthly pivots: not stated in the report (declared "single-source indicative"); the level file provides both.
- Counters: USDX ~99.8 (feed 99.809) ok; S&P 7,431 (feed 7,433.9) ok; VIX 17.68, −9% (feed 18.72, −4.1% from 19.51) mismatch of 1.04 pts (the slice may be a futures proxy; noted, not scored separately).
- 5-day swing (cash): high 10,473.5, low 10,126.2; 25-day high 10,560.0 (26 May), low 10,126.2.

## 5. Card Integrity (linter rows, verbatim from `qa/ftse_qa1/lint_static/2026-06-15.csv`)

| card_id | report_date | strategy | flags | dud | card score |
|---|---|---|---|---|---|
| 2026-06-15_Trade_1 | 2026-06-15 | Trade 1 — Daily Directional (LONG) | WARN_TP3_ORDER | False | 90 |
| 2026-06-15_Trade_2 | 2026-06-15 | Trade 2 — Pivot (regime-aware, LONG-from-support) | CLEAN | False | 100 |
| 2026-06-15_Trade_3A | 2026-06-15 | Trade 3 — Momentum-Pullback (3A, LONG) | DUD_TP1_SIDE | True | 60 |

card_integrity = (90 + 100 + 60) / 3 = 83.3 · n_cards = 3 · n_duds = 1 · n_warns = 1 (none suppressed). Separate from the 100.

Feedback: `qa/ftse_qa1/2026-06-15_feedback.md`.
