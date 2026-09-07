# Trust Score — 2026-07-17 — SP500_Report_17Jul2026.md

## 1. Section 7 checklist

| Item | Reviewer notes | Evidence observed | Score 0–5 | Action required |
|---|---|---|---|---|
| 1.1 Variables respected | Asset is the S&P 500 cash index and the ES/CFD quote is explicitly excluded from the cash basis; counters are USDX · VIX · DAX 40 with USDX first; as-of is the 16 Jul NY close (genuinely D−1); lookback 5 short / 25 medium; USD, index points, tick 0.01; seven source observations, six qualifying. **One configured variable is not respected: the M1 daily-open anchor of 07:00 UK is replaced by 00:00 UK**, an hour at which the cash index does not trade; the report concedes every §21 entry is therefore not executable as configured. | Header; §2 Market Definition table (Asset, Price basis, Tick, Session anchor rows); §4 seven-row evidence table + six-source note; §19 "Normalization assumptions"; §20 "ANCHOR OVERRIDE — instructed" | 3 | Restore the 07:00 UK anchor, or carry the override as a SUPPRESSED/deviation state rather than repricing all three cards off a non-tradeable anchor. |
| 1.2 Coverage & currency consistent | Every dated item in §2/§4/§6/§13/§20 is 16 Jul or earlier; the only D-dated item is the run timestamp and the forward calendar, both correctly framed as forward risk. No currency or unit drift — index points and USD throughout, no per-cent/points confusion. Minor: §13a dates one article "15–16 Jul" where §13c places the same event on 15 Jul. | §6 date column (10/13/14/15/16 Jul); §13a–§13d; §20 run timestamp 17 Jul 04:22 UK | 4 | Give the June PPI article a single publication date consistent with §13c. |
| 1.3 Audience & tone | Written to the Senior US Equity Strategist register throughout — trading-and-risk framing, no retail explainers, no promotional language; §18 is a judgement with an explicit confidence split and a single named watch item. | §1; §18 "Three most important reasons" / "Single watch item"; card caveats ("Size accordingly") | 5 | None. |
| 2.1 Sections present & ordered | §1–§21 all present and in the correct order; §13a/b/c/d and §21a/§21c/§21d all present and labelled. Two gaps: **the §21b heading is absent** (the three cards sit unlabelled between §21a and §21c), and **§7 contains no chart at all** — the report states outright that no placeholder is produced, so there is not even a caption to accept as evidence. | Heading scan §1…§21; §7 body text; §21a → cards → §21c sequence | 3 | Add the "§21b" heading over the card block; produce the candlestick/5-week/VOLator/pivot charts, or at minimum captioned placeholders. |
| 2.2 Scorecard as a table | §6 is a genuine table carrying Date/Open/High/Low/Close/RSI2/Trend/Source A/Source B/Final Used/Validation for all five sessions. All three §11 pivot tables run R3→R2→R1→P→S1→S2→S3, three levels each side, for daily, weekly and monthly. | §6 table; §11 daily/weekly/monthly tables | 5 | None. |
| 2.3 Method steps visible | §4→§5 shows observation → normalization → classification → weighted-median consensus with each exclusion reasoned. §8 is candle-by-candle for all five sessions plus a separate sequence assessment. §9 states regime, persistence, VOLator slope and the Kaufman overlap with an explicit precedence argument. **§7 delivers no chart and no placeholder**, so the graphical step of the method is simply absent. | §4, §5 bullets; §8 "Candle-by-candle" + "Sequence assessment"; §9 measures table + Kaufman confirmation; §7 | 3 | Restore §7 output; note the omission in §20 is disclosure, not remediation. |
| 3.1 Quantitative claims sourced | §1 numbers all resolve to §4/§6/§9/§13. §12 attributes its figures (TSMC capex $60–64bn, Seaport/CNBC on Nvidia, Schwab 62% above 50-DMA, 6.55% mortgage rate). §14 is weaker: the 3M at 3.803%, the 10-2 spread of 31.32bp, the 20Y 5.085% and 30Y 5.086–5.107% carry no named source and no pointer to §4/§13. | §1; §12 bullets; §14 "Rates — front end" / "Rates — long end" rows | 4 | Attribute the §14 yield-curve figures to a named, dated source or point them at §13a. |
| 3.2 Citations exist & contain data | Three spot-checks, all internally consistent: (a) TSMC beat-and-raise (Bloomberg/CNBC, 16 Jul) — 77% gain, capex $60–64bn from $52–56bn, sector −3–4% used identically in §1/§12/§15/§18; (b) June PPI −0.3% (CNBC/TradingEconomics) — the −0.3% and the ~12% hike odds are consistent across §1/§12/§13c/§14; (c) Yahoo Finance §4 row 7,533.77 (−38.63) — reproduces exactly against the 15 Jul close 7,572.40. **No fabricated source found; the hallucination override does not apply.** Two flaws: the Bloomberg row is timestamped "16 Jul 17:47 GMT+3" (≈10:47 ET) yet its basis is given as "Cash close, New York", which its own timestamp cannot support; and §20 states IBM was "excluded from all constituent commentary" after an irreconcilable −25.21%/+3.90% split, while §12 still quotes IBM +3.90% and §13c still quotes −25.21%. | §4 Bloomberg row; §13a rows 1, 3, 6; §12 mega-cap bullet; §13c earnings row; §20 anomaly (5) | 3 | Fix the Bloomberg timestamp/basis pairing; either drop IBM from §12/§13c or withdraw the §20 exclusion claim. |
| 3.3 Calculations transparent | Strong on pivots and scores: all three §11 pivot sets reproduce **exactly** from the report's own H/L/C, and the floor identity R2−P = P−S2 holds at every timeframe (daily 66.72/66.72, weekly 158.11/158.11, monthly 283.74/283.74). §21a reproduces exactly (−0.125+0.080+0.030+0.045−0.023−0.060 = −0.0525) on the mandated weights 0.25/0.20/0.10/0.15/0.15/0.15. The fib ladder reproduces exactly off the stated 10-session swing (50% 7,501.66; 61.8% 7,482.82; 78.6% 7,455.99). ATR(14) 71.74 and KER(13, EMA-3) +0.37 are both stated. **RSI2 fails outright: it does not reproduce from the report's own closes on any testable row** — 14 Jul 58.0 vs 32.0, 15 Jul 75.9 vs 100.0, 16 Jul 35.4 vs 42.7 — and no working or smoothing convention is shown, while §6 asserts "period fixed at 2". | §11 three tables; §21a table; §20 "Fib swing selection"; §9 ATR/KER rows; §6 RSI2 column vs helper recomputation | 2 | Recompute RSI2 as RS = mean gain / mean loss over 2 periods, or state and show the Wilder smoothing actually used. RSI2 drives the §21a short-technical band, so the direction score must be re-derived. |
| 3.4 Numbers reconcile | The D−1 close 7,533.77 is identical in §1, §3, §4, §6 and §19. §11 daily pivots equal the pivots quoted on the cards (S1 7,501.61 = Trade 2 entry; R1 7,568.33 = Trade 3 entry). ATR 71.74 is the same in §9, §15 and all three cards. RSI2 35.4 is the same in §6, §8 and §21a. Four failures: (i) Trade 1 is a MARKET card whose entry 7,542.76 is the 5-session swing midpoint, 8.99 pts above the D−1 close; (ii) the Trade 1 runner stop is 7,551.46 on the card but 7,534.06 in the baseline card record; (iii) §16 gives an expected range of 7,469–7,581 while §17 states a 7,504–7,570 band; (iv) §8 says the 16 Jul low 7,504.02 "sits above the 13 July low of 7,506.41", which its own numbers contradict. | §1/§3/§4/§6/§19 close; §11 vs cards; Trade 1 "Tranche management" vs cards/baseline/by_date/2026-07-17.json; §16 vs §17; §8 "Against this, the lows are constructive" | 2 | Reconcile all four; the Trade 1 entry and the runner-stop mismatch are hard blockers. |
| 4.1 Pillars conclude | §8 closes on a labelled double-top rejection; §9 closes on regime label TRANSITION; §10 closes on aggregate CONTRADICT (−0.4). §12 and §14 end without any direction label — §12 stops on the Kospi bullet, §14 on a breadth row. More seriously, the strategy pillar contradicts the regime pillar it cites: §21 builds a range fade and a counter-side limit while quoting regime label TRANSITION, under which M5 §5.2c/§5.3c mandate breakout-side-only and fork 3C. | §8 sequence assessment; §9 regime row; §10 contradiction flag; §12/§14 endings; §21 "Regime fork: TRANSITION" then 3B | 2 | Add closing direction labels to §12 and §14; rebuild §21 on the fork the regime label actually selects. |
| 4.2 Peer/cross-asset interpreted | §10 is mechanism-driven, not a correlation list: dollar weakness → translation of ~28% foreign revenue, and specifically dovish-repricing weakness rather than risk-aversion weakness; VIX as hedging demand outpacing realised movement; DAX as the same AI-capex shock through a different constituent set. It then argues why a 2:1 contradiction understates the case (two correlated fresh headwinds vs one exhausted tailwind). | §10 mechanism column; §10 "Contradiction flag" paragraph | 5 | None. |
| 4.3 Synthesis reconciles tensions | The narrative reconciliations are genuinely good: §9 resolves Kaufman +0.37 against the short-term read on an explicit stated-window argument; §15 weighs a diffuse bull case against a concentrated bear case; §16 carries an explicit regime-consistency check; §21a flags the conviction/§17 tension. But the synthesis stops at the strategy boundary — the §16/§17 range mismatch is unreconciled, and §21 asserts the 3B fork is chosen "because the regime label is TRANSITION", which inverts the rule it invokes. | §9 "Which signal takes precedence"; §15 balance paragraph; §16 regime consistency check; §21 fork rationale; §16 vs §17 | 2 | Reconcile §16/§17; state the fork rule correctly and follow it. |
| 4.4 Calibrated language | §17 is exactly one sentence with no hedge stacking. Confidence is stated where required: §3 High, §16 Medium, §18 High on price / Medium on direction. The conviction-threshold breach is stated in bold before the cards rather than buried. Deduct only for the Trade 2 header calling it the "highest-quality card" when M5 suppresses that construction outright in this regime. | §17; §3/§16/§18 confidence fields; §21a threshold-breach block; Trade 2 header | 4 | Drop the quality superlative from a card the regime rule does not permit. |
| 5.1 Data dated; staleness flagged | Every §4 row carries a date and time, every §6 row a date, every §13a article a date. The single-source-indicative 15 Jul O/H/L is flagged in §6, again in §19, and again on the two cards whose stop depends on it. §19 carries a per-instrument corroboration table and discloses that the 25-session window holds only 18 validated sessions. | §4 Date/Time column; §6 bullet 2; §19 "Live vs indicative data", corroboration table, "Data gaps" | 5 | None. |
| 5.2 Assumptions up front | The anchor-override caveat appears in §19, in §20 and on all three cards. Single-source propagation is explicit: monthly pivots excluded from entry and stop construction, and the 15 Jul swing-high dependency is repeated on Trade 1 and Trade 3. Normalization assumptions (no FX/grade/location adjustment, the 0.10 Investing.com delta, CFD/ES exclusion) are itemised. | §19 "Normalization assumptions"; §20 ANCHOR OVERRIDE / CORROBORATION LENIENCY; card caveat blocks | 5 | None. |
| 5.3 Red flags surfaced | §12 and §15 are dense with named risks. §13d grades each forward collision (Netflix MODERATE, Asia semis HIGH, US–Iran HIGH) and every one of those is carried onto the cards as a NEWS COLLISION caveat with the mechanism spelled out. §20 logs five anomalies including the IBM discrepancy. | §12; §15 bear column; §13d; three card caveat blocks; §20 Anomalies | 5 | None. |
| 5.4 Restrictions honoured | The textual restrictions are clean: no module codes, no framework name, no bracketed variable names, instrument common names throughout, ES/US500 CFD retained as confirmation only and excluded from the cash OHLC, and no synthesised price presented as sourced (the reconstructed 15 Jul H/L is flagged indicative). **But two fixed M5 rules are violated.** (i) The conviction threshold: |−0.0525| < 0.25 requires Trade 1 to be SUPPRESSED; the card is issued instead, which the report itself calls "a deliberate, logged deviation from the configured suppression rule". (ii) The TRANSITION regime gate: M5 §5.2c suppresses a counter-side limit outright, yet Trade 2 is a buy limit at daily S1, and M5 §5.3c makes 3C the only Trade 3 variant, yet 3B is built. Violation (i) is declared, (ii) is not. | §20 "SUPPRESSION OVERRIDE — Trade 1"; §21a threshold-breach block; §21 Trade 2 entry field; §21 Trade 3B "Fork selected"; §4/§5 CFD exclusion; §2 price basis | 1 | Suppress Trade 1; suppress or rebuild Trade 2 on the breakout side; replace 3B with 3C or log 3C as not eligible. |

## 2. Category roll-up

| Category | Level | Multiplier | Points | Justification |
|---|---|---|---|---|
| C1 Prompt adherence (max 20) | 3 | 0.65 | 13.00 | Rows 1.1–1.3 mean 4.00 → level 4, reduced one level to 3 by the restriction-breach override. Every variable is respected except the daily-open anchor, which is overridden to a non-tradeable 00:00 UK across all three cards. |
| C2 Structure (max 20) | 4 | 0.85 | 17.00 | Rows mean 3.67 → 4. All §1–§21 sections present and ordered, §6 and §11 tables fully formed; §21b heading missing and §7 delivers no chart or placeholder at all. |
| C3 Accuracy & evidence (max 25) | 3 | 0.65 | 16.25 | Rows mean 2.75 → 3. Pivots, fib levels and the §21a score reproduce exactly and no source is fabricated; RSI2 fails to reproduce on every testable row, the 15 Jul open and low are outside slice tolerance, and four cross-section reconciliations fail. |
| C4 Reasoning & judgment (max 20) | 3 | 0.65 | 13.00 | Rows mean 3.25 → 3. §10 mechanism work and §9/§15/§16 contradiction handling are strong, but §12/§14 lack direction labels and all three cards are built against the regime fork the report itself assigns. |
| C5 Currency, restrictions & transparency (max 15) | 4 | 0.85 | 12.75 | Rows mean 4.00 → 4. Dating, indicative flagging, assumption disclosure and red-flag carry-through are exemplary; row 5.4 scores 1 on two openly breached M5 construction rules. |
| **Total** | — | — | **72** | Sum 13.00 + 17.00 + 16.25 + 13.00 + 12.75 = 72.00 → 72. |

## 3. Total, band, override check

- Raw weighted total: **72.00 → 72**.
- **Hallucinated-source override: does not apply.** Three cited sources were spot-checked for internal consistency (TSMC beat-and-raise via Bloomberg/CNBC; June PPI −0.3% via CNBC/TradingEconomics; the Yahoo Finance §4 close row) and each is named, dated, and quotes a figure used consistently elsewhere in the report. The Yahoo row's −38.63 reproduces exactly against the 15 Jul close. No source is impossible or self-contradictory in its figures. The Bloomberg row's "17:47 GMT+3" timestamp against a "Cash close, New York" basis is an internal labelling error, not a fabricated source, and is penalised in row 3.2 rather than by override. C3 is therefore **not** set to 0.
- **Restriction-breach override: APPLIES.** Two fixed rules of the strategy module are openly violated by the output. First, the conviction threshold — the report's own direction score is −0.0525 against a threshold of 0.25, which mandates a SUPPRESSED Trade 1 row; the report issues a full Trade 1 card and states on the card that it is "a deliberate, logged deviation from the configured suppression rule". Second, the TRANSITION regime gate — a counter-side limit is expressly suppressed in TRANSITION, yet Trade 2 is a buy limit at daily S1, and Trade 3 is built as the RANGE variant 3B when the assigned regime label admits only 3C. Consequence: total capped at Moderate (74) and C1 reduced by one level (4 → 3), both applied above.
- Cap check: 72 ≤ 74, so the Moderate cap does not bind further.
- **Final Trust Score: 72 — Band: Moderate (60–74).** Override recorded: `restriction_breach`.
- Usage decision: not fit for release as-is; regenerate against the feedback file. The report's evidence discipline and disclosure are strong enough that a rebuild of §6 RSI2 and §21 should recover most of the loss.

## 4. Card Integrity

Linter rows, copied verbatim from `qa/regen_20260906_qa1/lint_static/2026-07-17.csv`:

| card_id | report_date | strategy | flags | dud |
|---|---|---|---|---|
| 2026-07-17_Trade_1 | 2026-07-17 | Trade 1 - Daily Directional | CLEAN | False |
| 2026-07-17_Trade_2 | 2026-07-17 | Trade 2 - Pivot (buy limit daily S1) | CLEAN | False |
| 2026-07-17_Trade_3 | 2026-07-17 | Trade 3 - Pivot fade (sell limit daily R1) | CLEAN | False |

Per-card integrity (100 − 40·#DUD − 10·#WARN, floored at 0):

| Card | #DUD | #WARN | Integrity |
|---|---|---|---|
| 2026-07-17_Trade_1 | 0 | 0 | 100 |
| 2026-07-17_Trade_2 | 0 | 0 | 100 |
| 2026-07-17_Trade_3 | 0 | 0 | 100 |
| **Report mean (3 non-suppressed cards)** | 0 | 0 | **100.0** |

All three cards pass every static-integrity test: stops on the correct side, TP1 beyond entry, TP2 beyond TP1, TP3 beyond TP2, R inside 0.3–3.0×ATR14 (0.61 / 0.67 / 0.43) and TP1 inside 2.5×ATR14 of entry on each card. The M5 rule assessment below is scored under row 4.x and row 5.4 and does **not** alter this number.

M5 assessment feeding rows 4.1 / 4.3 / 5.4 (not the integrity score):

| Card | M5 rule | Assessment |
|---|---|---|
| Trade 1 | §2 conviction threshold; §5.1 entry at the daily-open anchor; static rule "MARKET entry equals the D−1 close"; §5.1 stop derivation | Must be SUPPRESSED at \|−0.0525\| < 0.25. Entry 7,542.76 is the 5-session swing midpoint, 8.99 pts above the D−1 close, on a card the baseline records as entry_mode MARKET. The stop value 7,586.27 is correct per rule (daily R1 7,568.33 + 0.25×ATR 17.94) but the card describes it as "the 15 July swing high 7,581.50 plus a 0.25 × ATR buffer", which would be 7,599.44. Runner stop 7,551.46 on the card vs 7,534.06 in the baseline record. |
| Trade 2 | §5.2c TRANSITION — breakout side only; §5.2a TP3 rule | A buy limit at daily S1 is exactly the counter-side limit §5.2c suppresses under a TRANSITION label. Entry 7,501.61 = daily S1 and stop 7,453.57 = weekly S1 7,471.50 − 0.25×ATR are both correctly derived, and TP1/TP2 are correct at ±1R/±2R; but TP3 7,716.82 uses the Trade 1 3×ATR runner cap, where §5.2a specifies a runner toward P. |
| Trade 3 | §3 regime gate; §5.3b/§5.3c | Fork 3B requires regime_label = RANGE; the report's label is TRANSITION, which selects 3C. Even as a 3B, the construction is wrong — it uses daily R1 with ±1R/±2R targets instead of 78.6–88.6% of the 25-day range, a stop 10% of width inside the boundary, TP1 at the midpoint and TP2 at low + 0.10×width. Internal arithmetic is otherwise exact (stop 7,581.50 + 0.25×ATR = 7,599.44 ≈ 7,599.43; R 31.10; TP1/TP2/TP3 all correct off that R). |

## 5. Data reconciliation log

Slice: `data/slices/US500/US500_upto_2026-07-16.csv`, cash session 16:30–23:00 broker. Tolerance per the brief: |Δ| ≤ 3 pts on a close, ≤ 8 pts on an open/high/low.

| Section | Report value | Slice value | Delta | Verdict |
|---|---|---|---|---|
| §6 10 Jul Open | 7,547.64 | 7,544.70 | +2.94 | Consistent (CFD basis) |
| §6 10 Jul High | 7,579.93 | 7,579.50 | +0.43 | Consistent |
| §6 10 Jul Low | 7,508.16 | 7,505.60 | +2.56 | Consistent |
| §6 10 Jul Close | 7,575.39 | 7,574.20 | +1.19 | Consistent |
| §6 13 Jul Open | 7,547.53 | 7,550.80 | −3.27 | Consistent |
| §6 13 Jul High | 7,565.37 | 7,565.80 | −0.43 | Consistent |
| §6 13 Jul Low | 7,506.41 | 7,507.00 | −0.59 | Consistent |
| §6 13 Jul Close | 7,515.34 | 7,518.20 | −2.86 | Consistent (inside 3.00) |
| §6 14 Jul Open | 7,536.70 | 7,535.70 | +1.00 | Consistent |
| §6 14 Jul High | 7,557.44 | 7,559.70 | −2.26 | Consistent |
| §6 14 Jul Low | 7,513.23 | 7,512.90 | +0.33 | Consistent |
| §6 14 Jul Close | 7,543.59 | 7,546.40 | −2.81 | Consistent |
| §6 15 Jul Open | 7,549.10 | 7,569.10 | **−20.00** | **DISCREPANCY** — 2.5× the 8-pt open tolerance; the row is flagged single-source-indicative in §6/§19, which explains but does not repair it |
| §6 15 Jul High | 7,581.50 | 7,582.80 | −1.30 | Consistent (this is the swing high anchoring the Trade 1 and Trade 3 stops) |
| §6 15 Jul Low | 7,540.20 | 7,528.60 | **+11.60** | **DISCREPANCY** — exceeds the 8-pt low tolerance; same single-source row |
| §6 15 Jul Close | 7,572.40 | 7,573.90 | −1.50 | Consistent |
| §6 16 Jul Open | 7,558.80 | 7,554.00 | +4.80 | Consistent |
| §6 16 Jul High | 7,570.74 | 7,572.20 | −1.46 | Consistent |
| §6 16 Jul Low | 7,504.02 | 7,506.00 | −1.98 | Consistent |
| §6 16 Jul Close (D−1) | 7,533.77 | 7,536.20 | −2.43 | Consistent (inside 3.00) |
| §6 RSI2 10 Jul | 87.1 | 100.00 (slice closes) / n/a (own closes) | −12.9 vs slice | Not independently testable from the report's own closes; slice value differs materially |
| §6 RSI2 13 Jul | 33.8 | 35.93 (slice closes) / n/a (own closes) | −2.13 vs slice | Plausible; not testable from the report's own closes |
| §6 RSI2 14 Jul | 58.0 | 33.49 (slice) / **32.0 (report's own closes)** | **+26.0 vs own closes** | **FAIL** — does not reproduce from the report's own close sequence |
| §6 RSI2 15 Jul | 75.9 | 100.00 (slice) / **100.0 (report's own closes)** | **−24.1 vs own closes** | **FAIL** — two consecutive up closes give RS undefined → 100 under the stated 2-period formula |
| §6 RSI2 16 Jul | 35.4 | 42.18 (slice) / **42.7 (report's own closes)** | **−7.3 vs own closes** | **FAIL** — and it changes the §21a short-technical band from 40–60 to 20–40 |
| §6 14 Jul Trend | Neutral, stated as "by rule" | Close 7,543.59 > Open 7,536.70 with the report's own RSI2 58.0 > 50 | — | Internal contradiction: the report's own rule yields Bullish on the RSI2 it prints (Neutral is correct only on the recomputed 32.0) |
| §9 ATR(14) | 71.74 | 70.30 (cash) / 78.47 (full day) | +1.44 vs cash | Consistent |
| §11 daily P | 7,536.18 | 7,538.13 | −1.95 | Consistent; reproduces exactly from the report's own H/L/C (22,608.53 / 3) |
| §11 daily R1 / S1 | 7,568.33 / 7,501.61 | 7,570.27 / 7,504.07 | −1.94 / −2.46 | Consistent; both reproduce exactly as 2P−L and 2P−H |
| §11 daily R2 / S2 | 7,602.90 / 7,469.46 | 7,604.33 / 7,471.93 | −1.43 / −2.47 | Consistent; identity R2−P = P−S2 = 66.72 holds exactly |
| §11 daily R3 / S3 | 7,635.05 / 7,434.89 | 7,636.47 / 7,437.87 | −1.42 / −2.98 | Consistent; both reproduce from H+2(P−L) and L−2(H−P) |
| §11 weekly P / R1 / S1 | 7,525.71 / 7,629.61 / 7,471.50 | 7,524.93 / 7,628.77 / 7,470.37 | +0.78 / +0.84 / +1.13 | Consistent; identity R2−P = P−S2 = 158.11 holds exactly |
| §11 weekly R2 / S2 / R3 / S3 | 7,683.82 / 7,367.60 / 7,787.72 / 7,313.39 | 7,683.33 / 7,366.53 / 7,787.17 / 7,311.97 | +0.49 / +1.07 / +0.55 / +1.42 | Consistent |
| §11 monthly (June basis) | P 7,457.15, R1 7,620.13, S1 7,336.39, R2 7,740.89, S2 7,173.41, R3 7,903.87, S3 7,052.65 | Not derivable from the D−1 slice | — | All seven reproduce exactly from the stated June H/L/C 7,577.92 / 7,294.18 / 7,499.36; identity R2−P = P−S2 = 283.74 holds. Correctly flagged single-source-indicative and excluded from card construction |
| §8/§20 5-day swing high | 7,581.50 (15 Jul) | 7,582.80 (15 Jul) | −1.30 | Consistent, same session |
| §8 5-day swing low | 7,504.02 (16 Jul) | 7,505.60 (10 Jul) | −1.58 | Level consistent; the slice puts the 5-session low on 10 Jul, not 16 Jul |
| §9/§11 June low (monthly S-side basis) | 7,294.18 (26 Jun) | 7,303.10 (26 Jun, 25d cash low) | −8.92 | Marginal — just outside the 8-pt low tolerance; same session, and already flagged indicative |
| §9 25-session high (implied) | 7,581.50 | 7,583.40 (15 Jun) | −1.90 | Consistent in level; the slice's 25-day high sits on 15 Jun, outside the report's 18-session window |
| §9 "Net change, 5 sessions −9.87" | −9.87 | Sum of the report's own five session deltas (+31.75 −60.05 +28.25 +28.81 −38.63) | 0.00 | Internally exact; the +31.75 requires a 9 Jul close of 7,543.64, corroborated by `SP500_M1_Report_16Jul2026.md` |
| §6 10/13/14 Jul OHLC | as printed | Identical rows in `SP500_M1_Report_16Jul2026.md` | 0.00 | Cross-report consistent |
| §11 weekly pivots | P 7,525.71 / S1 7,471.50 | Identical in `SP500_M1_Report_16Jul2026.md` | 0.00 | Cross-report consistent |
| §21a direction score | −0.0525 | Recomputed on the stated weights and signals | 0.0000 | Exact |
| §13b numeric tilt | −0.15 | Mean of the nine §13a tilts = −1.10 / 9 = −0.122 | −0.028 | Adjustment is disclosed in §13b and §20 as a salience weighting; traceable |
| §20 fib swing | 7,421.82–7,581.50 = 159.68 = 2.23×ATR | 159.68 / 71.74 = 2.226 | 0.00 | Exact; 50%/61.8%/78.6% levels (7,501.66 / 7,482.82 / 7,455.99) all reproduce |
| §21d net points | +95.18 | 60.05 + 28.25 + 38.63 − 31.75 | 0.00 | Exact |
| §21b Trade 1 entry vs D−1 close | 7,542.76 (MARKET) | 7,533.77 report close / 7,536.20 slice cash close | +8.99 / +6.56 | **FAIL** — a MARKET Trade 1 entry must equal the D−1 close |
| §21b Trade 1 runner stop | 7,551.46 | 7,534.06 in `cards/baseline/by_date/2026-07-17.json` | 17.40 | **FAIL** — report and card record disagree on the same field |
| §21b anchor | 00:00 UK on all three cards | baseline `anchor_broker` 16:30 (Trade 1), 09:00 (Trades 2 and 3) | — | **FAIL** — the card record still carries the 14:30 UK and 07:00 UK anchors the report says were overridden |
| §16 vs §17 expected range | §16 7,469–7,581; §17 7,504–7,570 | — | 35 / 11 pts | Unreconciled internal inconsistency |
| §8 low comparison | "16 July low of 7,504.02 sits above the 13 July low of 7,506.41" | Report's own §6 values | 2.39 | False on the report's own numbers — 7,504.02 is below 7,506.41 |
| Report as-of session | 16 July 2026 close, America/New_York | Last slice bar 2026-07-16 23:45 | 0 | Genuinely D−1; no value dated on or after 17 July appears anywhere in the data sections |
