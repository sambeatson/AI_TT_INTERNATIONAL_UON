# Reviewer brief — Trust Score v3.7 applied to the S&P 500 daily reports (run regen_20260906_qa1)

This brief is distilled from `modules/` (the prompt stack the reports were produced under) and
`docs/QA_PROTOCOL_TRADE_CARDS.md`. It contains no market information. It exists so that 54 independent
review sessions apply the same anchors. Where the brief and the framework text disagree, the framework
(`docs/AI_Output_Trust_Score_Framework_v3.7.txt`, Sections 4–7) wins.

## 1. Scoring mechanics (framework §4, §6, §7)
- Five categories, each scored 0–5, converted by multiplier: 5→1.00, 4→0.85, 3→0.65, 2→0.40, 1→0.20, 0→0.00.
- Maxima: C1 Prompt adherence 20 · C2 Structure 20 · C3 Accuracy & evidence 25 · C4 Reasoning & judgment 20 ·
  C5 Currency, restrictions & transparency 15. Total = Σ(multiplier × max), rounded to a whole number.
- Category level = mean of its Section 7 checklist rows, rounded to the nearest whole level.
- Bands: Very High 90–100 · High 75–89 · Moderate 60–74 · Low 40–59 · Very Low 0–39.
- Overrides: a fabricated source → cap at Low (40–59) and C3 = 0. A breached prompt restriction →
  cap at Moderate (60–74) and C1 down one level at least.
- Card Integrity is SEPARATE (not in the 100): per card 100 − 40·(#DUD) − 10·(#WARN), floored at 0;
  report level = mean over non-suppressed cards. Copy the linter rows verbatim; do not re-derive.

## 2. Section 7 checklist mapped to these reports
| Row | What to check here | Where |
|---|---|---|
| 1.1 Variables respected | Asset = S&P 500 cash index (not ES futures) · counters USDX, VIX, DAX 40 (USDX first) · as-of NY close of D-1, tz America/New_York · lookback 5 sessions · USD, index points, tick 0.01 · ≥ 6 sources from index provider / exchange / sell-side tiers · daily-open anchor **07:00 UK** for Trade 1 | §2, §4, §10, §13, §21b |
| 1.2 Coverage & currency consistent | Every date in §2/§6/§13/§21 is D-1 or earlier for data and D for the session; no currency/unit drift | whole report |
| 1.3 Audience & tone | Senior US Equity Strategist; trading-and-risk-review use; no retail tone | §1, §18 |
| 2.1 Sections present & ordered | §1 Executive Snapshot · §2 Market Definition · §3 Consensus Price Call · §4 Price Evidence Table · §5 Consensus Build · §6 Validated OHLC+RSI2 Table · §7 Charts · §8 Short-Term Technical · §9 Medium-Term Regime & VOLator · §10 Cross-Asset · §11 Floor Pivots · §12 Key Market Considerations · §13 Sentiment/News/Calendar (§13a per-article table, §13b aggregate with numeric tilt, §13c previous-period calendar, §13d upcoming calendar) · §14 Macro · §15 Bull/Bear · §16 Forward View · §17 Forecast (ONE sentence) · §18 Final Judgement · §19 Source Discipline Note · §20 Agent Log · §21 Strategy (§21a conviction, §21b cards, §21c 5-session backtest, §21d what-is-working + limitations boilerplate) | headings |
| 2.2 Scorecard as a table | §6 is a table with Date/O/H/L/C/RSI2/Trend/Source A/Source B/Final/Validation; §11 pivot tables ordered R3→P→S3 (3 levels each side) for daily, weekly, monthly | §6, §11 |
| 2.3 Method steps visible | §4–§5 show observations → classification → consensus; §8 candle-by-candle + sequence; §9 regime with persistence/overlap/VOLator; §7 charts present (pandoc drops images: accept a caption/placeholder as evidence, note it) | §4–§9 |
| 3.1 Quantitative claims sourced | Every number in §1, §12, §14 carries a source or points to §4/§6/§13 | text |
| 3.2 Citations exist & contain data | You cannot fetch. Pick three cited sources: named, dated, quote a figure that is used consistently elsewhere in the report. A URL/source that is self-contradictory or impossible (wrong date, figure not matching its own quote) counts as fabricated | §4, §13a |
| 3.3 Calculations transparent | RSI2 shown or reproducible: RS = mean gain / mean loss over 2 periods, RSI2 = 100 − 100/(1+RS); Trend: Close>Open & RSI2>50 Bullish, Close<Open & RSI2<50 Bearish, else Neutral · pivots P=(H+L+C)/3, R1=2P−L, S1=2P−H, R2=P+(H−L), S2=P−(H−L), R3=H+2(P−L), S3=L−2(H−P) · ATR(14) stated · KER(13, EMA 3) stated · §21a score = Σ signal×weight with weights 0.25/0.20/0.10/0.15/0.15/0.15 | §6, §11, §9, §21a |
| 3.4 Numbers reconcile | D-1 close identical in §1, §3, §4, §6, §21b entry; pivots in §11 = pivots quoted on cards; ATR in §9/§21; RSI2 in §6 = §8 = §21a input | cross-section |
| 4.1 Pillars conclude | §8, §9, §10, §12, §14 each end in a direction label consistent with their content | those sections |
| 4.2 Peer/cross-asset interpreted | §10 gives a mechanism (why USDX/VIX/DAX matter for the call), not a correlation list | §10 |
| 4.3 Synthesis reconciles tensions | §15/§16/§18 address conflicts between short- and medium-term reads, KER vs regime, §17 vs §21a | §15–§18, §21a |
| 4.4 Calibrated language | §17 exactly one sentence, no hedge stacking; confidence H/M/L stated where the framework asks | §3, §17 |
| 5.1 Data dated; staleness flagged | Every price and article dated; single-source-indicative O/H/L flagged | §4, §6, §13, §19 |
| 5.2 Assumptions up front | Anchor-override caveat (proxy open) stated on the card and in §20; single-source pivot propagation to cards | §21b, §19, §20 |
| 5.3 Red flags surfaced | §12/§15 risks; §13d event collisions carried into card caveats | §12, §15, §21b |
| 5.4 Restrictions honoured | No synthesised/interpolated price presented as sourced; no retail CFD quotes in the OHLC basis; ES futures confirmation-only; no bracketed variable names, no module codes (M1..M5), no framework name in the report; instrument common names | whole report |

Card construction is ALSO scored under Category 4 (protocol table): see §3 below.

## 3. Card construction rules (M5, fixed) — what a compliant card must satisfy
- Direction score = Σ signal×weight; |score| < 0.25 → Trade 1 SUPPRESSED (a SUPPRESSED row, not omission).
- Three equal units on every card. TP1 = entry ± 1R, TP2 = entry ± 2R for Trade 1 and RANGE Trade 2; on Unit 2
  fill, Unit 3 stop → entry ± 0.2R. Runner: session-close time-stop OR 3×ATR(14) price cap (Trade 1).
- Trade 1: market at the daily-open anchor (07:00 UK in this M1 instance; a 00:00 UK anchor is a deviation to note).
  Stop = tighter of (5-day swing extreme, nearest S/R) + 0.25×ATR buffer, capped at 3.5×ATR. Wide-stop flag if R > 1×ATR.
- Trade 2 by regime: RANGE → limit at S1/S1.5/S2 (long) or R1/R1.5/R2 (short), tier by distance in ATR, stop 3.5×ATR
  or structural+0.25×ATR. TREND → entry at P + 0.10×(R1−P) (long), stop P − 0.8×(P−S1), TPs R1/R1.5/R2.
  TRANSITION → breakout side only. Suppressed if every pivot tier is single-source-indicative.
- Trade 3A (trend): entry 57.5% retrace of the qualifying swing (magnitude ≥ 2×ATR, 4–10 session lookback,
  endpoints logged), stop beyond the 0% anchor by 0.25×ATR, TP1 38.2%, TP2 0%, TP3 100%+ extension.
  3B (range): limits at 11.4–21.4% / 78.6–88.6% of the 25-day range, stops 10% of width inside, TP1 mid, TP2 far side −10%.
  3C (transition): confirmed close beyond the 25-day boundary by ≥ 0.25×ATR, stop at low + 0.40×width, TP1 = +1.0×width, TP2 = 1.5×.
- Every card: thesis invalidation separate from the stop; confluences listed; single-source-indicative flag
  propagated; stops/targets in both price and points.
- Static integrity the scoring engine enforces (regeneration must satisfy): stop on the correct side; TP1 beyond
  entry; TP2 beyond TP1; TP3 beyond TP2 or null; 0.3×ATR14 ≤ R ≤ 3.0×ATR14; TP1 within 2.5×ATR14 of entry;
  a MARKET entry equals the D-1 close; a LIMIT/STOP level sits on the correct side of the D-1 close; anchor explicit.

## 4. Data basis for Category 3 checks
- The slice is the broker CFD M15 feed (broker time = UTC+3 = UK+2). Cash session = 16:30–23:00 broker
  (09:30–16:00 ET). `engine/qa_slice_stats.py` prints cash-session and full-day OHLC, RSI2, ATR14, pivots, swings.
- Expect a CFD-vs-cash basis of a few points on every field. Treat |Δ| ≤ 3 pts on a close or ≤ 8 pts on an
  open/high/low as consistent; larger deltas are discrepancies to record with location. A close that is
  wrong by more than 10 pts, or an RSI2 that does not reproduce from the report's own closes, is a Category 3
  failure to score, not just a note.
- Use `--closes` with the report's five stated closes to test the RSI2 arithmetic independently of basis.

## 5. What feedback may and may not contain
- May: the defect, the rule it violates, and the numeric condition a compliant level must satisfy, with the
  numbers from the slice (D-1 close, ATR14, pivots, swings). May: which reconciliation failed, which section
  is missing or malformed, which restriction was breached.
- May not: anything about what price did on or after D, or whether a trade would have worked. You do not know.
