# Trust Score v3.7 — FTSE 100 Daily Report, 15 July 2026 (run ftse_qa1)

Report: `reports/md/FTSE_100_Report_15_July_2026.md` · D = 2026-07-15 · D-1 = 2026-07-14
Level file check: `last_bar_date` = 2026-07-14 < D (leak-free, confirmed). Slice last bar 2026-07-14 22:45 broker.
Basis reference (report claims cash index): cash session 10:00–18:30 broker, `_cash` columns. Full-day figures quoted where they change the verdict.
Note: `cards/regenerated/` exists in the tree. It was not opened. `results/`, `data/raw/` and `data/levels/*_levels.csv` are absent, as expected.

## Score line

```
c1=3
c2=4
c3=1
c4=3
c5=2
total=54
band=Low
override=restriction_breach
card_integrity=100
n_cards=2
n_duds=0
n_warns=0
```

(n_cards = non-suppressed cards scored; the report has 3 card rows, one of them the SUPPRESSED Trade 1.)

## 1. Section 7 checklist

### Category 1 — Prompt adherence

| Row | Reviewer notes | Evidence | Score |
|---|---|---|---|
| 1.1 Variables respected | Asset (FTSE 100 cash, Euro Stoxx as reference only), 5-session lookback, GBP/index points, Europe/London as-of, USDX / S&P 500 / DAX 40 counters are all as specified. Deviations: (a) the 07:00 UK daily-open anchor was overridden (§20) and neither card states a clock time or the override; (b) a CFD-derived proxy (Trading Economics GB100) is used in the OHLC validation although the report's own restriction excludes it; (c) STOXX is said to carry a "GBP-equivalent reference" that is never shown; (d) Source set is wide enough (>=6) but includes a retail CFD broker (Capital.com) and a Sunday weekly for weekday closes. | §2, §6, §20, §21b | 3 |
| 1.2 Coverage & currency consistent | Data dates are all <= 14 Jul and the session is 15 Jul throughout. No unit drift beyond the missing STOXX GBP-equivalent. | whole report | 4 |
| 1.3 Audience & tone | Strategist register, trading/risk-review use; no retail tone. | §1, §18 | 4 |

Row mean 3.67 -> 4. Restriction-breach override applied: C1 down one level -> **3**.

### Category 2 — Structure

| Row | Reviewer notes | Evidence | Score |
|---|---|---|---|
| 2.1 Sections present & ordered | §1–§21 all present and in order, including §13a–d and §21a–d; §17 is one sentence; Trade 1 is a SUPPRESSED row, not an omission; §21d carries the limitations boilerplate. §7 shows chart headings/captions only (pandoc drops images — accepted, noted). §7 lists five charts. | headings | 5 |
| 2.2 Scorecard as table | §6 is a table with every required column; §11 daily/weekly/monthly tables are ordered R3→P→S3. | §6, §11 | 5 |
| 2.3 Method steps visible | §4→§5 shows observations→consensus, §8 is candle-by-candle with a sequence read, §9 has regime/persistence/overlap/VOLator. Gaps: ATR(14) is never stated numerically anywhere; KER(13, EMA3) is described ("distorted… inconclusive") but no value is given; overlap ratio is not quantified; weekly/monthly H/L/C inputs to §11 are not shown. | §8, §9, §11 | 3 |

Row mean 4.33 -> **4**.

### Category 3 — Accuracy & evidence

| Row | Reviewer notes | Evidence | Score |
|---|---|---|---|
| 3.1 Quantitative claims sourced | §1, §10, §12, §14 carry many bare numbers with no source or pointer: "3 July record high of 10,934.94", USDX ~99.4, VIX ~16, DAX ~24,958, S&P 7,543.59, Brent ~$84–85, WTI ~$79, Shell +1.6%, BP +2.7%, BoE ~50bp. Several are wrong against the slice (see 3.4). | §1, §10, §12, §14 | 2 |
| 3.2 Citations exist & contain data | Three picked. (1) Fidelity/Sharecast 14 Jul 10,532.38: named, dated, but the same figure is used as the 14 Jul High and the report then adopts a different close (10,527) with a stated Δ of ~5; the "close" it is said to corroborate is actually derived from CNBC's percentage (see 3.3). (2) Trading Economics: §4 gives 14 Jul "~10,519 (+0.20%)", §13a gives the TE headline "FTSE edged lower" for the same date; §4/§19/§5 say TE is excluded from level-setting while §6 uses it as Source B (8 Jul) and Source A (13 Jul). (3) Proactive Investors 10 Jul 10,497 (+25) is consistent with the report's 9 Jul close 10,472.45 and passes internally. I cannot fetch, so I do not call any source fabricated, but source (2) is self-inconsistent and the "Corroborated (Δ<0.1)" claims on 8 and 9 Jul are not supported by any figure that matches the data (see 3.4). Sunday Guardian is cited for Mon/Tue closes; flagged as an unusual daily source. Override not triggered, but row scored at the floor. | §4, §6, §13a, §19 | 1 |
| 3.3 Calculations transparent | RSI2 arithmetic reproduces from the report's own closes for the three testable rows (10 Jul 31.0, 13 Jul 96.1, 14 Jul 96.9 — checked with `--closes`); 8 Jul and 9 Jul cannot be tested without prior closes. Trend column errors: 8 Jul (C 10,527 > O 10,465, RSI2 97.0) must be Bullish, shown Neutral; 9 Jul (C < O, RSI2 74.5) must be Neutral, shown Bearish. Daily pivots reproduce exactly from the stated 14 Jul H/L/C (P 10,494.1 etc.). Weekly and monthly pivots do not show their H/L/C and do not reproduce from the actual weeks (see 3.4). §13b tilt: 0.5/3.4 = 0.147, shown "+0.13". §21a: the three shown contributions (+0.06, +0.15, +0.02) sum to +0.23, not the stated +0.19; the other three of six signals are not shown, so the score is not traceable. §8 close-location figures are wrong against §6's own numbers (8 Jul (10,527−10,450)/88 = 88%, shown "~70%"; 9 Jul 44%, shown "~48%"). ATR14 and KER not stated. | §6, §8, §11, §13b, §21a | 2 |
| 3.4 Numbers reconcile | Internal: D-1 close 10,527 is consistent in §1/§3/§6/§18/§21b; §11 pivots equal the pivots quoted on the cards. Breaks: §1 "3 July record high 10,934.94" vs §9 "advance to the 10,747 area" vs slice (see below); the 8 Jul close (10,527.0) is identical to the 14 Jul close; §19 calls the 14 Jul close single-source while §6 lists two sources. Against the slice: three of five closes are wrong by more than 15 pts and the weekly and monthly pivots are materially wrong (table below). Brief §4 makes a close wrong by >15 pts a Category 3 failure. | §1, §6, §9, §11, §19 | 1 |

Row mean 1.5. Brief §4 instructs that closes wrong by >15 pts are a Category 3 failure; the .5 is resolved down -> **1**.

#### Category 3 data check — report vs slice (cash basis, 10:00–18:30 broker)

Tolerance: close ±5, open/high/low ±10. Positive Δ = report above slice.

| Date | Field | Report | Slice cash | Δ | Verdict |
|---|---|---|---|---|---|
| 8 Jul | Open | 10,465.0 | 10,634.1 | −169.1 | FAIL |
| 8 Jul | High | 10,538.0 | 10,636.3 | −98.3 | FAIL |
| 8 Jul | Low | 10,450.0 | 10,454.7 | −4.7 | ok |
| 8 Jul | Close | 10,527.0 | 10,457.0 | +70.0 | FAIL (>15) |
| 9 Jul | Open | 10,500.0 | 10,439.2 | +60.8 | FAIL |
| 9 Jul | High | 10,539.5 | 10,468.9 | +70.6 | FAIL |
| 9 Jul | Low | 10,420.0 | 10,380.4 | +39.6 | FAIL |
| 9 Jul | Close | 10,472.45 | 10,457.0 | +15.45 | FAIL (>15) |
| 10 Jul | Open | 10,475.0 | 10,490.1 | −15.1 | FAIL |
| 10 Jul | High | 10,520.0 | 10,504.8 | +15.2 | FAIL |
| 10 Jul | Low | 10,466.0 | 10,451.1 | +14.9 | FAIL |
| 10 Jul | Close | 10,497.0 | 10,487.2 | +9.8 | FAIL |
| 13 Jul | Open | 10,498.05 | 10,488.1 | +9.95 | ok |
| 13 Jul | High | 10,532.1 | 10,526.4 | +5.7 | ok |
| 13 Jul | Low | 10,478.4 | 10,455.7 | +22.7 | FAIL |
| 13 Jul | Close | 10,496.0 | 10,487.4 | +8.6 | FAIL |
| 14 Jul | Open | 10,441.09 | 10,460.4 | −19.3 | FAIL |
| 14 Jul | High | 10,532.38 | 10,545.8 | −13.4 | FAIL |
| 14 Jul | Low | 10,422.98 | 10,411.5 | +11.5 | FAIL |
| 14 Jul | Close | 10,527.0 | 10,507.0 | +20.0 | FAIL (>15) |

Full-day D-1 close is 10,478.3 (Δ +48.7); the cash basis the report claims is the fairer test. Of 20 fields, 17 are outside tolerance.
Session character: the report's 8 Jul is a +62 pt bullish body; the slice's 8 Jul cash session is open 10,634.1 → close 10,457.0 (−177.1 pts, a large down session) and its 9 Jul close equals its 8 Jul close.

RSI2 (cash closes from the slice): 8 Jul 14.88, 9 Jul 0.00, 10 Jul 100.00, 13 Jul 100.00, 14 Jul 100.00. Report: 97.0, 74.5, 31.0, 96.1, 96.9. The report's own arithmetic reproduces where testable; the inputs are wrong.
ATR14: slice cash 122.54 / full 131.24 — not stated in the report.

Counters and context vs slices (CFD feeds, broker time):

| Item | Report | Slice | Note |
|---|---|---|---|
| USDX | ~99.4 | 100.91 (14 Jul close), 101.05→100.91 over 8–14 Jul | level off by ~1.5; "flat" direction fine |
| VIX | ~16 | 17.37 (14 Jul close); 16.66–17.92 over the window | off by ~1.4 |
| S&P 500 | 7,543.59 (+0.38%) | 7,547.6 close, +0.50% vs 13 Jul close | CFD vs cash, acceptable |
| Record high 3 Jul | 10,934.94 | 25-session cash max 10,739.6 (7 Jul); 3 Jul cash high 10,692.5 | not supported; also contradicts §9 (10,747) |
| Resistance shelf "10,532–10,539, repeated highs 8–14 Jul" | as stated | highs 10,636.3 / 10,468.9 / 10,504.8 / 10,526.4 / 10,545.8 | shelf does not exist |
| Invalidation "9-Jul close 10,472" | 10,472 | 9 Jul cash close 10,457.0 | |

Pivot check (cash) — the report's daily pivots are from 14 Jul H/L/C; tolerance for pivots taken as ±10:

| Level | Daily report | Daily cash | Δ | Weekly report | Weekly cash | Δ | Monthly report | Monthly cash (June) | Δ |
|---|---|---|---|---|---|---|---|---|---|
| R3 | 10,674.7 | 10,699.0 | −24.3 | 10,670.5 | 11,050.27 | −379.8 | 11,508.2 | 11,180.73 | +327.5 |
| R2 | 10,603.5 | 10,622.4 | −18.9 | 10,605.0 | 10,894.93 | −289.9 | 11,127.6 | 10,894.77 | +232.8 |
| R1 | 10,565.3 | 10,564.7 | +0.6 | 10,551.0 | 10,691.07 | −140.1 | 10,888.8 | 10,698.13 | +190.7 |
| P | 10,494.1 | 10,488.1 | +6.0 | 10,485.5 | 10,535.73 | −50.2 | 10,508.2 | 10,412.17 | +96.0 |
| S1 | 10,455.9 | 10,430.4 | +25.5 | 10,431.5 | 10,331.87 | +99.6 | 10,269.4 | 10,215.53 | +53.9 |
| S2 | 10,384.7 | 10,353.8 | +30.9 | 10,366.0 | 10,176.53 | +189.5 | 9,888.8 | 9,929.57 | −40.8 |
| S3 | 10,346.5 | 10,296.1 | +50.4 | 10,312.0 | 9,972.67 | +339.3 | 9,650.0 | 9,732.93 | −82.9 |

Back-solved inputs: the weekly pivots imply H 10,539.5 / L 10,420.0 / C 10,497.0, which is 9 Jul's (report) H/L, not the 6–10 Jul week; the true week is H 10,739.6 (7 Jul), L 10,380.4 (9 Jul), C 10,487.2. The monthly pivots imply H 10,747.0 / L 10,127.6 / C 10,650.0; the true June is H 10,608.8, L 10,126.2, C 10,501.5. Both are marked "CORROBORATED" in §11 and §19. The "three-timeframe confluence at 10,486–10,527" does not exist on the true levels (monthly P 10,412.2; weekly P 10,535.7; daily P 10,488.1).

### Category 4 — Reasoning & judgment

| Row | Reviewer notes | Evidence | Score |
|---|---|---|---|
| 4.1 Pillars conclude | §8 (Range, nascent bullish tilt), §9 (Neutral-to-mildly-bullish, TRANSITION), §10 (CONFIRM), §12 items each carry a cyclical/structural and price-supportive/negative label, §15 net balance. §14 ends in a watch item, not a direction label. Conclusions are internally consistent but built on wrong inputs (8 Jul read as a bullish session; shelf and support levels not in the data). | §8–§15 | 3 |
| 4.2 Peer / cross-asset | §10 gives mechanisms (USD translation of ~80% overseas revenue, global risk beta, eurozone read) and §12 ties energy weight to Brent. Good. The USDX level is wrong (~99.4 vs 100.9) and the oil linkage is not carried into §10 as a counter. | §10, §12 | 4 |
| 4.3 Synthesis reconciles tensions | §16 reconciles short vs medium term explicitly; §17 and §21a agree. But the regime is labelled TRANSITION while Trade 2 is built as a range fade ("buy support") and Trade 3 as 3A (trend pullback), contrary to the M5 rule (TRANSITION → breakout side only; 3A is a trend card). §9's "range-fade protocol" is not the TRANSITION protocol. | §9, §16, §21 | 3 |
| 4.4 Calibrated language | §17 is exactly one sentence with a single conditional; confidence Medium stated in §3 and §18; "low conviction" in §21a. Medium confidence sits awkwardly with a flagged single-source close. | §3, §17 | 4 |
| 4.5 Card construction (protocol row) | Linter CLEAN, but construction rules are broken: Trade 2 is not a TRANSITION breakout and is not at an S1/S1.5/S2 tier; its entry and confluence use a weekly P (10,486) that is 50 pts off the true weekly P (10,535.7, which is above the D-1 close, so a buy limit there is on the wrong side); stop has no 0.25×ATR buffer; "STRONG confluence" relies on the wrong monthly P. Trade 3A is a breakout buy-stop, not a 57.5% retracement; no swing endpoints logged; stop is a pivot, not the 0% anchor − 0.25×ATR; TP1 is 29 pts (0.62R). Details in feedback. | §21b | 1 |

Row mean 3.0 -> **3**.

### Category 5 — Currency, restrictions & transparency

| Row | Reviewer notes | Evidence | Score |
|---|---|---|---|
| 5.1 Data dated; staleness flagged | Prices and articles are dated; single-source flag is raised for 14 Jul. But 8–13 Jul are labelled "Corroborated" when the closes do not match the data, STOXX rows use "≈" with no source time, and the §3 Basis line calls a percentage-derived close a "weighted median of validated sources". | §3, §4, §6 | 3 |
| 5.2 Assumptions up front | The derivation of the 14 Jul close (+0.3% applied to the 13 Jul close) is disclosed in §5 but not in §1/§3. The anchor-override caveat is in §20 only; the brief requires it on the card as well; neither card carries a clock time or the override. Single-source propagation: daily pivots are barred from entries (good) yet TP2/TP3 are tied to daily R2/R3. | §5, §20, §21b | 2 |
| 5.3 Red flags surfaced | §12/§15 surface the rates and Hormuz risks and §13d collisions are carried into card caveats. But the report gives no UK CPI date or time (the calendar slice has no UK CPI row for 6–15 Jul), and calendar items for D are missing from §13d: US PPI m/m (HIGH, 15:30 broker; consensus 1.6), BoC rate decision (HIGH, 16:45), EIA crude stocks (HIGH, 17:30), BoE MPC Pill speech. §13c omits the two BoE Governor Bailey speeches and two ECB Lagarde speeches on 14 Jul (all HIGH). | §12, §13c, §13d | 3 |
| 5.4 Restrictions honoured | Breaches: (1) a price synthesised from a percentage change (13 Jul close × 1.003) is adopted as the consensus close and presented in §6 with CNBC as Source A; CNBC supplied no level. (2) A CFD-derived proxy (Trading Economics GB100, labelled "CFD proxy — downweighted per restrictions" in §4) is used as Source B (8 Jul) and Source A (13 Jul) in the OHLC validation, while §5 and §19 state it is excluded from level-setting. No bracketed variable names or module codes found; "v2.1 baseline / weight-lock" in §20 is internal jargon. | §3, §5, §6, §19 | 1 |

Row mean 2.25 -> **2**.

## 2. Category roll-up

| # | Category | Level | Multiplier | Points | Max | Justification |
|---|---|---|---|---|---|---|
| 1 | Prompt adherence | 3 (4 before override) | 0.65 | 13.0 | 20 | Variables largely respected; CFD proxy and derived price used against the report's own restriction, anchor override only in §20. |
| 2 | Structure | 4 | 0.85 | 17.0 | 20 | All 21 sections and sub-sections present and ordered; tables correct; ATR and KER values missing. |
| 3 | Accuracy & evidence | 1 | 0.20 | 5.0 | 25 | 17/20 OHLC fields outside tolerance, three closes >15 pts out, weekly/monthly pivots built on wrong H/L/C and marked corroborated, an unsupported record high. |
| 4 | Reasoning & judgment | 3 | 0.65 | 13.0 | 20 | Reasoning and mechanisms are sound; card construction contradicts the regime and the M5 rules. |
| 5 | Currency & transparency | 2 | 0.40 | 6.0 | 15 | Dates present; anchor and derivation caveats thin; calendar items missed; restriction breached. |

## 3. Total, band, override

- Total = 13.0 + 17.0 + 5.0 + 13.0 + 6.0 = **54**.
- Band: **Low Trust (40–59)**.
- Override check: `hallucinated_source` — not triggered (cannot fetch; no cited source is provably non-existent, though the Trading Economics entries are self-inconsistent). `restriction_breach` — **triggered** (synthesised close presented as sourced; CFD proxy used in the OHLC basis against the report's own stated restriction). Cap at Moderate (60–74) is not binding at 54; C1 reduced from 4 to 3.
- **override=restriction_breach**

## 4. Card Integrity (static linter rows, copied verbatim from `qa/ftse_qa1/lint_static/2026-07-15.csv`)

| card_id | report_date | strategy | flags | dud |
|---|---|---|---|---|
| 2026-07-15_Trade_1 | 2026-07-15 | Trade 1 - Daily Directional | SUPPRESSED | False |
| 2026-07-15_Trade_2 | 2026-07-15 | Trade 2 - Pivot (regime-aware). Transitional regime -> buy support at corroborated weekly pivot confluence | CLEAN | False |
| 2026-07-15_Trade_3A | 2026-07-15 | Trade 3A - Momentum-Pullback. 14-Jul range-top close + CONFIRM cross-asset -> buy a shallow pullback in the resolution attempt | CLEAN | False |

| card | #DUD | #WARN | Card Integrity |
|---|---|---|---|
| Trade 1 | — | — | suppressed (excluded) |
| Trade 2 | 0 | 0 | 100 |
| Trade 3A | 0 | 0 | 100 |

Report-level Card Integrity (mean over non-suppressed cards) = **100**. n_cards=2, n_duds=0, n_warns=0.
The linter is static and clean; the construction defects in Category 4 row 4.5 are rule violations the static pass does not test.
