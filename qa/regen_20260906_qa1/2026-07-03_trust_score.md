# Trust Score — 2026-07-03 — SP500_Report_03Jul2026.md

Run: `regen_20260906_qa1` · Asset: US500 (S&P 500 cash index) · D = 2026-07-03 (US market holiday) ·
D-1 = 2026-07-02 · Slice: `data/slices/US500/US500_upto_2026-07-02.csv` (broker CFD M15, cash session
16:30–23:00 broker = 09:30–16:00 ET).

Helper invocation used for every Category 3 arithmetic test:

```
python3 engine/qa_slice_stats.py --slice data/slices/US500/US500_upto_2026-07-02.csv \
  --date 2026-07-03 --closes 7354.02 7440.43 7499.36 7483.23 7482.5
```

As-of session check: the report's last §6 row is **02 Jul 2026**, and §2 states explicitly that the last
completed cash session is Thursday 02 Jul. The as-of session is genuinely D-1, not an earlier session.
(The §2 "As-of date" *field* nevertheless reads 03 July 2026 — D, not the D-1 NY close — flagged under 1.1.)

## 1. Section 7 checklist

| Item | Reviewer notes | Evidence observed | Score 0–5 | Action required |
|---|---|---|---|---|
| 1.1 Variables respected | Asset = S&P 500 cash index (not ES futures) ✓; counters USDX · VIX · DAX 40 with USDX first ✓; tz America/New_York ✓; lookback = 5 completed sessions (26 Jun–02 Jul) ✓; USD, index points, tick 0.01 ✓; 6 sources spanning index provider (S&P DJI via FRED), media desks and a sell-side voice (Goldman via CNBC) ✓ — no exchange-tier source. **Two variable deviations:** the Trade 1 daily-open anchor was moved from the M1 07:00 UK anchor to a 00:00 UK anchor, and the as-of date was set to D rather than the D-1 NY close. Both are disclosed as an operator override, so they are deviations to note, not covert breaches. | §2 table; §3; §4 (6 rows); §10; §13a; §20 bullet 5 ("the daily-open anchor was overridden … to a 00:00 UK anchor, and the as-of date was set to 03 July 2026"); §21b Entry row; §21 unit note | 3 | Restore the 07:00 UK daily-open anchor for Trade 1 unless the operator override is re-issued; set the §2 as-of field to the D-1 NY close. |
| 1.2 Coverage & currency consistent | All price and article dates are D-1 or earlier; the session date is D and the holiday closure is stated ✓. No currency or unit drift (index points/USD throughout) ✓. **Internal date drift:** §4 dates the Investing.com range 7,449.63 / 7,521.81 to the "02 Jul day range", but §6 puts 7,522 on **01 Jul** and gives 02 Jul as 7,450 / 7,508, and §8 calls 7,522 "01 Jul high". The prior-day report (02 Jul) attributes the same pair to the 01 Jul session. | §4 row 5; §6 rows 4–5; §8 S/R paragraph; §3 rationale; `reports/md/SP500_Report_02Jul2026.md` §4 ("Investing.com 01 Jul intraday 7,449.63--7,521.81") | 3 | Re-date the Investing.com range to the session it belongs to and make §1/§3/§4/§6/§8 agree on which day carries 7,522. |
| 1.3 Audience & tone | Written as a Senior US Equity Strategist for a trading-and-risk review; forward-test framing, no retail tone, no advice language, explicit non-advice footer. | Header line; §1; §18; closing disclaimer | 5 | None. |
| 2.1 Sections present & ordered | §1–§21 all present in order; §13a/b/c/d and §21a/b/c/d all present; §17 is a single sentence; §21c backtest and §21d limitations boilerplate both present; Trade 2 appears as a SUPPRESSED row, not an omission. | Headings throughout; §13a–§13d; §21a–§21d | 5 | None. |
| 2.2 Scorecard as a table | §6 is a proper table but collapses **Source A / Source B** into one "Sources" column ("CNBC×Zacks"); Date/O/H/L/C/RSI2/Trend/Final/Validation all present ✓. §11 weekly and monthly tables are correctly R3→P→S3 (3 levels each side); the **daily** table is R5→S5 (5 levels each side), i.e. non-conforming to the specified structure. | §6 header row; §11 daily table (R5 7,685.6 … S5 7,277.0); §11 weekly/monthly tables | 3 | Split §6 sources into Source A and Source B columns; trim the daily pivot table to R3→P→S3. |
| 2.3 Method steps visible | §4 observations → §5 normalisation/weighted-median → §3 consensus is fully traceable; §8 is candle-by-candle then a sequence assessment; §9 states overlap ratio, persistence, VOLator slope, range position and the Kaufman confirmation; §7 carries five chart placeholders (pandoc dropped the images — captions retained, accepted as evidence per protocol). | §4–§5; §8 bullets + "Sequence assessment"; §9 bullets; §7 captions Chart 1–5 | 5 | None (note the pandoc image loss). |
| 3.1 Quantitative claims sourced | Most §1/§12/§14 numbers point back to §4/§6/§13 ✓. Unsourced or unsupported: the payrolls consensus "~115k" (the calendar slice records NFP actual 57.0k against **consensus 43.0k**, previous 172.0k — i.e. a beat, not a miss); VIX "~16.6" and DAX "~25,040" carry no citation and VIX is 0.9–1.0 off the slice; "354 advancers" in §8 is uncited; "Micron −10.6%, Sandisk −10.6%, AMD −6.9%" are uncited. | §12 "Policy / macro"; §13c 02 Jul row; §14; §8 02 Jul bullet; `data/slices/NEWS/news_upto_2026-07-02.csv` (2026-07-02 15:30 Nonfarm Payrolls 57.0 / 43.0 / 172.0; Unemployment Rate 4.2; 2026-07-01 ADP 98.0; 2026-06-25 PCE y/y 4.1) | 2 | Cite or correct the payrolls consensus; attach sources to the VIX/DAX levels and the single-stock moves. |
| 3.2 Citations exist & contain data | **Two citations are internally impossible.** (a) §13a "CNBC · 28 Jun · S&P 500 gained 1.18% to 7,440.43 · 'snapping a five-day losing streak'": 28 Jun 2026 is a **Sunday**, and the report's own §6 and §13c date the +1.18% move to 7,440.43 to **29 Jun**. A source cannot be dated the day before the close it quotes; the equivalent article is dated 29 Jun in the 02 Jul report. (b) §4 "Investing.com · session · 7,449.63 / 7,521.81 · 02 Jul day range" contradicts the same report's §6 (02 Jul H/L = 7,508 / 7,450) and §8 (7,522 = 01 Jul high). Third spot-check passes: §4 S&P DJI-via-FRED 7,483.23 vs CNBC 7,483.24 (Δ0.01) is used consistently in §1/§3/§5/§6; §13a Trading Economics "7478 … losing 0.08%" reconciles to −0.07% off 7,483.23. | §13a row 5 (CNBC 28 Jun); §4 row 5 (Investing.com); §6 rows 2, 4, 5; §8; `reports/md/SP500_Report_02Jul2026.md` §13a (CNBC dated 29 Jun) | 0 | **Hallucinated-source override triggered.** Re-date or drop the CNBC item; re-date the Investing.com range. |
| 3.3 Calculations transparent | RSI2 is exact: the helper recomputes the report's own close sequence to **100.0 / 78.5 / 0.0** against the report's stated 100.0 / 78.5 / 0.0 — zero arithmetic error. Trend labels follow the stated rule (02 Jul C>O but RSI2 0 → Neutral ✓; 01 Jul and 30 Jun Bullish ✓). §11 daily pivots reproduce from the report's own D-1 H/L/C to ≤0.7 pt (exact on H 7,507.9 / L 7,449.5 / C 7,482.6); weekly and monthly tables also reproduce internally (monthly decomposes to H 7,620.9 / L 7,237.8 / C 7,499.4). §21a score reproduces: 0.20(1.0)+0.15(0.84)+0.25(0)+0.10(−0.5)+0.15(−0.15)+0.15(0) = **+0.2535 → +0.25** on the correct weight set. Gaps: ATR is quoted as "ATR≈86" with **no period stated (14)**, and the Kaufman read is "smoothed efficiency ≈ +0.11" with **no KER(13, EMA 3) parameters**. | §6 RSI2 column + helper line "RSI2 recomputed from the REPORT'S OWN closes … 100.0, 78.5, 0.0"; §11 all three tables; §20 strategy trace; §21a; §9 Kaufman bullet; §21b stop/cap rows | 4 | State ATR(14) and KER(13, EMA 3) explicitly with their computed values. |
| 3.4 Numbers reconcile | D-1 close 7,482.5 is identical in §1, §3, §4 (TheStreet normalised), §6 and the §21b entry ✓. §11 pivots are quoted unchanged on the cards (7,480 P / 7,510 R1 / 7,452 S1 / 7,538 R2) ✓. ATR≈86 is used consistently in the 3.5×ATR cap (≈300), the 3×ATR runner (7,740) and the 0.25×ATR break buffer (≈21) ✓. RSI2 in §6 = §8 = §21a input ✓. **Fails:** §1/§3 call 7,449–7,522 "the 02 July session range" while §6 gives 02 Jul as 7,450–7,508; §16 quotes daily R3 as 7,568 ✓ but the base-case range 7,452–7,530 uses a 7,530 "prior-week high" that appears nowhere in §6 or §11. | §1; §3 rationale; §4; §6; §8; §11; §16; §21b | 2 | Reconcile the consensus band with the §6 02 Jul range; source or drop the 7,530 level. |
| 4.1 Pillars conclude | §8 closes on "Judgement label: Indecision" ✓; §9 gives "Transitional" + "Bias: Bullish" ✓; §10 closes on "Aggregate cross-asset read: CONFIRM (mild)" ✓; §12 labels every bucket (price-supportive / neutral-to-negative / mixed / mild support) ✓; §14 carries a direction per bullet but ends with no single macro label. | §8 final line; §9 bullets 1–2; §10 aggregate paragraph; §12 bucket headers; §14 | 4 | Add a closing direction label to §14. |
| 4.2 Peer/cross-asset interpreted | §10 gives a transmission mechanism per counter (dollar → global financial conditions and earnings translation; VIX → implied-vol/risk regime with a complacency caveat; DAX → common cyclical beta), plus an explicit limitation that the counters describe the macro envelope and not the semiconductor rotation actually driving the index. Not a correlation list. | §10 table "Mechanism" column; §10 closing caveat | 5 | None. |
| 4.3 Synthesis reconciles tensions | §9 explicitly reconciles KER ("Ranging – Upward Bias") against the trending read and explains why the composite is TRANSITION; §13b resolves the sentiment-vs-regime divergence; §15/§16/§18 carry the short-vs-medium tension; §21a states an explicit conflict flag against §17 ✓. **Card construction (scored here per protocol):** Trade 1 is compliant end-to-end (MARKET at the anchor = stated D-1 close; R 54.5; TP1 = +1R; TP2 = +2R; U3 → entry+0.2R = 7,493; runner = session-close time-stop or 3×ATR ≈ 7,740; stop = nearest S/R 7,450 − 0.25×ATR ≈ 7,428.5; wide-stop test correctly false). Trade 2 is correctly SUPPRESSED with the stated reason (every pivot tier single-source-indicative). **Trade 3C defects:** the confirmed-break entry is ~7,642 but R is booked off the boundary 7,620.9 (R 229.9 instead of ~251); TP1 8,004 sits 3.89×ATR from entry (linter WARN_TARGET_FAR, cap is 2.5×ATR); the Unit-3 stop moves to the broken boundary 7,621 rather than entry+0.2R. Unexplained: §10 reads CONFIRM (mild) yet §20/§21a score cross-asset at exactly 0.0. | §9 Kaufman bullet; §13b Divergence; §15–§18; §21a conflict flag; §21b all three cards; §20 strategy trace; `qa/regen_20260906_qa1/lint_static/2026-07-03.csv` | 3 | Fix the Trade 3C entry/R basis and TP1 distance; reconcile the cross-asset 0.0 contribution with the CONFIRM (mild) label. |
| 4.4 Calibrated language | §17 is exactly one sentence with a single stated condition — no hedge stacking ✓. Confidence is stated where required: "Medium" in §3 and repeated in §18; conviction is explicitly labelled marginal/at-threshold in §1, §21a and the Trade 1 card. | §17; §3 Confidence column; §18 first line; §21a | 5 | None. |
| 5.1 Data dated; staleness flagged | Every §6 row is dated, every §4 quote carries a date/time, every §13a article is dated. Single-source O/H/L carry an asterisk with a footnote, and §19 explains the cause (cache-lagged/blocked feeds) and the propagation to pivots. Weak point: one article date (28 Jun) is not merely stale but impossible, and the §4 Investing.com row is dated only as "session". | §6 asterisk footnote; §4 Date/Time column; §13a Date column; §19 bullets 1–3 | 4 | Give the Investing.com row an explicit session date. |
| 5.2 Assumptions up front | The anchor-override caveat is on the card ("Market at 00:00 UK (overridden daily-open anchor)") **and** in §20 as a traceability entry; single-source pivot propagation to the cards is stated three times (§11 source-status note, §19 data-gaps bullet, §21b Trade 2 status and Trade 3C caveats); the corroboration-leniency decision is stated explicitly. | §21b Entry row; §20 bullet 5; §11 note; §19 bullet 3; §21b caveats | 5 | None. |
| 5.3 Red flags surfaced | §12 and §15 carry the semiconductor de-rate, PCE at multi-year highs, hawkish Fed and complacent positioning; §13d flags the 06 Jul resumption/earnings collision and it is carried into **both** live card caveat blocks; the backtest anomaly (03 Jul holiday, resolution windows roll to 06 Jul) is logged in §20. | §12; §15 table; §13d; §21b Trade 1 and Trade 3C "Caveats"; §20 backtest bullet | 5 | None. |
| 5.4 Restrictions honoured | No module codes (M1..M5), no framework name, no bracketed variable names, instrument common names used throughout ✓. The CFD-derived 7,478 is explicitly excluded from OHLC and retained confirmation-only (§4 Relevance = "Confirmation only"; §5; §19 Normalization) ✓. No ES/E-mini figures used ✓. Weak point: the indicative §6 O/H/L are not reproducible from the slice (see §5 below — 02 Jul O/H/L off by −23.2/−33.0/+23.0, 26 Jun by +33.2/−27.1/+33.7) and differ from the *same sessions* in the 02 Jul report, and those values then drive the §11 daily pivots that are quoted on the cards. They are asterisked as single-source indicative, so this is a weak-corroboration finding rather than an open restriction breach. | §4 Relevance column; §5; §19 bullet 4; §6 asterisk footnote; §11; slice comparison in §5 below; `reports/md/SP500_Report_02Jul2026.md` §6 | 3 | Rebuild §6 O/H/L from a reproducible basis before deriving pivots. |

## 2. Category roll-up

| Category | Level | Multiplier | Points | Justification |
|---|---|---|---|---|
| C1 Prompt adherence (max 20) | 4 | 0.85 | 17.00 | Rows 1.1/1.2/1.3 = 3/3/5, mean 3.67 → 4. Asset, counters, tz, lookback, units and source count all respected; two disclosed variable deviations (00:00 UK anchor, as-of set to D) and one internal date-drift on the Investing.com range. |
| C2 Structural alignment (max 20) | 4 | 0.85 | 17.00 | Rows 2.1/2.2/2.3 = 5/3/5, mean 4.33 → 4. All 21 sections and every sub-section present and ordered, method chain fully visible; §6 merges Source A/B and the daily pivot table runs R5→S5 instead of R3→S3. |
| C3 Accuracy & evidence (max 25) | 0 | 0.00 | 0.00 | Raw rows 3.1/3.2/3.3/3.4 = 2/0/4/2, mean 2.0 → 2, but the hallucinated-source override sets C3 = 0. RSI2 and the §21a score are arithmetically exact; two citations are internally impossible; the §6 O/H/L and several closes do not reconcile to the slice. |
| C4 Reasoning & judgment (max 20) | 4 | 0.85 | 17.00 | Rows 4.1/4.2/4.3/4.4 = 4/5/3/5, mean 4.25 → 4. Genuine cross-asset mechanism, explicit KER-vs-regime and sentiment-vs-regime reconciliation, one-sentence calibrated forecast; Trade 3C construction defects and an unexplained 0.0 cross-asset contribution pull 4.3 down. |
| C5 Currency, restrictions & transparency (max 15) | 4 | 0.85 | 12.75 | Rows 5.1/5.2/5.3/5.4 = 4/5/5/3, mean 4.25 → 4. Everything dated, anchor-override and indicative-pivot assumptions stated up front, risks and event collisions carried onto the cards; the non-reproducible indicative O/H/L basis is the weak point. |
| **Total (pre-override)** | — | — | **63.75 → 64** | 17.00 + 17.00 + 0.00 + 17.00 + 12.75. |

## 3. Total, band, override check

- Pre-override total: **64 / 100** (Moderate Trust, 60–74).
- **Hallucinated source override — APPLIES.** Framework §6: *"If any cited source is fabricated, the output
  is capped at the Low Trust band (40–59) regardless of total score, and the Category 3 score is set to 0."*
  Trigger (brief §2, row 3.2: *"A URL/source that is self-contradictory or impossible (wrong date, figure not
  matching its own quote) counts as fabricated"*):
  1. §13a **CNBC dated 28 Jun 2026** — a Sunday, with no US cash session — quoted as reporting
     "S&P 500 gained 1.18% to 7,440.43", a close the report's own §6 and §13c date to **29 Jun**. The same
     article is dated 29 Jun in the earlier 02 Jul report. Impossible date.
  2. §4 **Investing.com** row labelled "02 Jul day range 7,449.63 / 7,521.81", contradicted by the same
     report's §6 (02 Jul H/L = 7,508 / 7,450) and §8 ("7,522 (01 Jul high)"). Figure does not match its own label.
- Effect: C3 forced to 0 (already reflected in the roll-up) and the total capped at the top of the Low band.
- **Restriction breach override — does not apply.** No module codes, framework name or bracketed variables
  appear; the CFD quote is excluded from OHLC and marked confirmation-only; no ES futures figures are used.
  The 00:00 UK anchor is a *variable deviation* disclosed in §20, not one of the 5.4 restrictions, so it is
  scored down in 1.1 rather than treated as a breach.
- **Final Trust Score: 59 / 100 · Band: Low Trust (40–59) · Override: hallucinated_source.**

## 4. Card Integrity

Linter rows copied verbatim from `qa/regen_20260906_qa1/lint_static/2026-07-03.csv`:

| card_id | report_date | strategy | flags | dud |
|---|---|---|---|---|
| 2026-07-03_Trade_1 | 2026-07-03 | Trade 1 - Daily Directional | CLEAN | False |
| 2026-07-03_Trade_2 | 2026-07-03 | Trade 2 - Pivot (TRANSITION breakout side) | SUPPRESSED | False |
| 2026-07-03_Trade_3C | 2026-07-03 | Trade 3C - Momentum-Breakout (conditional) | WARN_TARGET_FAR(3.89xATR) | False |

Per-card integrity (100 − 40·#DUD − 10·#WARN, floored at 0):

| Card | #DUD | #WARN | Integrity | Note |
|---|---|---|---|---|
| 2026-07-03_Trade_1 | 0 | 0 | 100 | CLEAN. |
| 2026-07-03_Trade_2 | — | — | n/a (suppressed) | Excluded from the mean per protocol (non-suppressed cards only). |
| 2026-07-03_Trade_3C | 0 | 1 | 90 | WARN_TARGET_FAR: TP1 8,004 sits 3.89×ATR from entry against a 2.5×ATR cap. |

- Cards in file: **3** · DUD flags: **0** · WARN flags: **1** · suppressed: 1.
- **Report Card Integrity (mean over non-suppressed cards) = (100 + 90) / 2 = 95.0**

M5 rule assessment behind row 4.3 (does **not** change the number above):
- Trade 1 — compliant. |score| = 0.25 ≥ 0.25 so not suppressed; MARKET entry = stated D-1 close; three equal
  units; TP1 = +1R, TP2 = +2R; U3 → entry+0.2R on U2 fill; runner = session-close time-stop or 3×ATR;
  stop = nearest S/R − 0.25×ATR, inside the 3.5×ATR cap; wide-stop test correctly evaluated false; thesis
  invalidation (7,452) separate from and above the stop (7,428); confluences listed; indicative flag propagated.
  Deviation: the entry anchor is 00:00 UK, not the M1 07:00 UK anchor.
- Trade 2 — compliant suppression. TRANSITION → breakout side only, and every pivot tier is
  single-source-indicative, which is the stated suppression condition; shown as a SUPPRESSED row with the
  contextual construction noted as non-actionable.
- Trade 3C — three construction defects: entry/R basis mismatch (R booked off the boundary 7,620.9 rather
  than the ~7,642 confirmed-break entry), TP1 beyond the 2.5×ATR cap, and the Unit-3 stop moved to the broken
  boundary instead of entry ± 0.2R. Range definition, break buffer (0.25×ATR), stop (low + 0.40×width),
  TP1 (+1.0×width) and TP2 (1.5×width) are all correct.

## 5. Data reconciliation log

Tolerance per brief §4: |Δ| ≤ 3 pts on a close, ≤ 8 pts on an open/high/low = consistent (CFD-vs-cash basis).
Slice values are cash-session (16:30–23:00 broker) unless stated. Δ = report − slice.

### 5.1 §6 OHLC vs slice cash session

| Section | Report value | Slice value | Delta | Verdict |
|---|---|---|---|---|
| §6 26 Jun Open | 7,357 | 7,323.8 | +33.2 | FAIL (>8) |
| §6 26 Jun High | 7,375 | 7,402.1 | −27.1 | FAIL (>8) |
| §6 26 Jun Low | 7,336.82 | 7,303.1 | +33.7 | FAIL (>8) |
| §6 26 Jun Close | 7,354.02 | 7,335.8 | +18.2 | **FAIL (>10 pts — Category 3 failure)** |
| §6 29 Jun Open | 7,366 | 7,403.0 | −37.0 | FAIL (>8) |
| §6 29 Jun High | 7,445 | 7,450.6 | −5.6 | OK |
| §6 29 Jun Low | 7,360 | 7,355.1 | +4.9 | OK |
| §6 29 Jun Close | 7,440.43 | 7,443.0 | −2.57 | OK |
| §6 30 Jun Open | 7,452 | 7,446.2 | +5.8 | OK |
| §6 30 Jun High | 7,512 | 7,513.4 | −1.4 | OK |
| §6 30 Jun Low | 7,448 | 7,441.7 | +6.3 | OK |
| §6 30 Jun Close | 7,499.36 | 7,493.3 | +6.06 | FAIL (>3) |
| §6 01 Jul Open | 7,479 | 7,478.6 | +0.4 | OK |
| §6 01 Jul High | 7,522 | 7,525.4 | −3.4 | OK |
| §6 01 Jul Low | 7,450 | 7,452.6 | −2.6 | OK |
| §6 01 Jul Close | 7,483.23 | 7,489.1 | −5.87 | FAIL (>3) |
| §6 02 Jul Open (D-1) | 7,479 | 7,502.2 | −23.2 | FAIL (>8) |
| §6 02 Jul High (D-1) | 7,508 | 7,541.0 | −33.0 | FAIL (>8) |
| §6 02 Jul Low (D-1) | 7,450 | 7,427.0 | +23.0 | FAIL (>8) |
| §6 02 Jul Close (D-1) | 7,482.5 | 7,472.8 | +9.7 | FAIL (>3) |

D-1 stated range width 58.0 pts vs slice 114.0 pts — the report's 02 Jul session is under half the observed
cash range, which is what propagates into every daily pivot tier below.

### 5.2 RSI2

| Section | Report value | Check value | Delta | Verdict |
|---|---|---|---|---|
| §6 RSI2 30 Jun | 100.0 | 100.0 (helper, report's own closes) | 0.0 | PASS — arithmetic exact |
| §6 RSI2 01 Jul | 78.5 | 78.5 (helper, report's own closes) | 0.0 | PASS — arithmetic exact |
| §6 RSI2 02 Jul | 0.0 | 0.0 (helper, report's own closes) | 0.0 | PASS — arithmetic exact |
| §6 RSI2 30 Jun | 100.0 | 100.00 (helper, slice closes) | 0.0 | OK |
| §6 RSI2 01 Jul | 78.5 | 92.29 (helper, slice closes) | −13.79 | Basis-driven (close series), not an arithmetic error |
| §6 RSI2 02 Jul | 0.0 | 0.00 (helper, slice closes) | 0.0 | OK |
| §6 RSI2 26 Jun / 29 Jun | "---" | 0.00 / 78.08 (slice) | n/a | Blank where the slice yields values; 29 Jun was 96.1 in the 02 Jul report |

### 5.3 §11 pivots — reproduction from the report's own D-1 H/L/C, then vs slice

Reproduction test using the report's stated 02 Jul H 7,508 / L 7,450 / C 7,482.5 (P=(H+L+C)/3 etc.):

| Section | Report value | Recomputed from report's own H/L/C | Delta | Verdict |
|---|---|---|---|---|
| §11 daily P | 7,480.0 | 7,480.17 | −0.17 | REPRODUCES |
| §11 daily R1 | 7,510.5 | 7,510.33 | +0.17 | REPRODUCES |
| §11 daily S1 | 7,452.1 | 7,452.33 | −0.23 | REPRODUCES |
| §11 daily R2 | 7,538.4 | 7,538.17 | +0.23 | REPRODUCES |
| §11 daily S2 | 7,421.7 | 7,422.17 | −0.47 | REPRODUCES |
| §11 daily R3 | 7,568.8 | 7,568.33 | +0.47 | REPRODUCES |
| §11 daily S3 | 7,393.7 | 7,394.33 | −0.63 | REPRODUCES |

(The residual ≤0.63 pt is rounding: the tiers are exact on unrounded H 7,507.9 / L 7,449.5 / C 7,482.6.
Weekly tiers likewise decompose exactly to H 7,530.1 / L 7,336.9 / C 7,354.02; monthly to H 7,620.9 /
L 7,237.8 / C 7,499.4. R4/R5/S4/S5 are consistent ±(H−L) extensions but are outside the specified R3→S3 set.)

Same tiers against the slice-derived D-1 cash pivots:

| Section | Report value | Slice value | Delta | Verdict |
|---|---|---|---|---|
| §11 daily P | 7,480.0 | 7,480.27 | −0.27 | OK |
| §11 daily R1 | 7,510.5 | 7,533.53 | −23.03 | FAIL |
| §11 daily S1 | 7,452.1 | 7,419.53 | +32.57 | FAIL |
| §11 daily R2 | 7,538.4 | 7,594.27 | −55.87 | FAIL |
| §11 daily S2 | 7,421.7 | 7,366.27 | +55.43 | FAIL |
| §11 daily R3 | 7,568.8 | 7,647.53 | −78.73 | FAIL |
| §11 daily S3 | 7,393.7 | 7,305.53 | +88.17 | FAIL |
| §11 weekly P | 7,407.0 | 7,392.57 | +14.43 | FAIL |
| §11 weekly R1 | 7,477.1 | 7,482.03 | −4.93 | Borderline OK |
| §11 weekly S1 | 7,283.9 | 7,246.33 | +37.57 | FAIL |

### 5.4 Volatility, structure and counters

| Section | Report value | Slice value | Delta | Verdict |
|---|---|---|---|---|
| §21b ATR (period unstated) | ≈86 | 92.86 (cash ATR14) / 98.53 (full-day ATR14) | −6.86 / −12.53 | Understated ~7–13%; period label missing |
| §21b Trade 1 entry (MARKET = D-1 close) | 7,482.5 | 7,472.8 | +9.70 | FAIL (>3 pts on a close) |
| §8 / §21b 5-day swing low | 7,336.82 | 7,303.10 | +33.72 | FAIL |
| §8 5-day swing high | 7,522 | 7,541.00 | −19.00 | FAIL |
| §21b Trade 3C 25-session high | 7,620.9 | 7,624.60 | −3.70 | OK |
| §21b Trade 3C 25-session low | 7,237.85 | 7,243.10 | −5.25 | OK |
| §21b Trade 3C range width | 383.05 | 381.50 | +1.55 | OK |
| §9 range position | ≈64% | 60.2% (slice basis) | +3.8pp | OK — exact on the report's own numbers |
| §10/§12/§14 VIX level | ≈16.6–16.8 | 17.58 (D-1 close, VIX slice) | ≈−0.90 | FAIL — ~5–6% understated |
| §10/§12/§14 USDX level | ≈101.1 | 100.858 (D-1 close, USDX slice) | +0.24 | OK |
| §10 DAX 40 level | ≈25,040 | no slice supplied | n/a | Unverifiable |

### 5.5 Calendar and cross-report checks

| Section | Report value | Reference value | Delta | Verdict |
|---|---|---|---|---|
| §12/§13c June payrolls consensus | "57k vs ~115k consensus" | NEWS slice 2026-07-02 15:30 Nonfarm Payrolls: actual 57.0, consensus 43.0, previous 172.0 | consensus −72k | FAIL — the print beat the recorded consensus; "soft/below consensus" is unsupported |
| §12/§13c unemployment rate | 4.2% | 4.2 (NEWS slice, 2026-07-02) | 0.0 | OK |
| §13c 01 Jul ADP | +98k | 98.0 (NEWS slice, 2026-07-01) | 0.0 | OK |
| §12/§14 PCE | ~4.1% | PCE Price Index y/y 4.1 (NEWS slice, 2026-06-25) | 0.0 | OK |
| §13d holiday claim | 03 Jul US cash market closed | 03 Jul 2026 is a Friday; slice ends 2026-07-02 23:45 with no 03 Jul bars | — | Consistent |
| §6 26 Jun O/H/L | 7,357 / 7,375 / 7,336.82 | 7,351.00 / 7,369.20 / 7,300.85 (02 Jul report §6) | +6.0 / +5.8 / +35.97 | Cross-report inconsistency on the low |
| §6 29 Jun O/H/L | 7,366 / 7,445 / 7,360 | 7,372.50 / 7,445.90 / 7,360.20 (02 Jul report §6) | −6.5 / −0.9 / −0.2 | Consistent |
| §6 30 Jun O/H/L | 7,452 / 7,512 / 7,448 | 7,441.10 / 7,521.81 / 7,439.10 (02 Jul report §6) | +10.9 / −9.8 / +8.9 | Cross-report inconsistency |
| §6 closes 26/29/30 Jun | 7,354.02 / 7,440.43 / 7,499.36 | identical in the 02 Jul report | 0.0 | Consistent |
| §4 Investing.com range session | "02 Jul day range" | 01 Jul intraday (02 Jul report §4) | 1 session | FAIL — see 3.2 |
| §13a CNBC article date | 28 Jun (Sunday) for the +1.18% / 7,440.43 close | 29 Jun (02 Jul report §13a; report's own §6/§13c) | 1 day, non-trading | **FAIL — fabricated-source trigger** |
