# Trust Score — 2026-06-29 — SP500_Daily_Report_29Jun2026.md

Run: `regen_20260906_qa1` · Asset US500 · D = 2026-06-29 · D-1 session = Friday 2026-06-26
(last bar in slice `US500_upto_2026-06-28.csv` = 2026-06-26 23:45 broker; the report's as-of session is
genuinely D-1, not an earlier session).
Framework: `docs/AI_Output_Trust_Score_Framework_v3.7.txt` §4–§7, anchored by `qa/regen_20260906_qa1/REVIEWER_BRIEF.md`.

## 1. Section 7 checklist

| Item | Reviewer notes | Evidence observed | Score 0–5 | Action required |
|---|---|---|---|---|
| 1.1 Variables respected | Asset is the S&P 500 cash index (not ES futures); counters are Dollar Index → VIX → DAX 40 in the required order; as-of NY close of D-1; lookback 5 execution / 25 regime; index points, USD, tick 0.01; six sources listed. Fails only on the daily-open anchor: §20 logs an override "from the populated instance value (07:00 UK)" but never names the anchor it was overridden **to**, and the Trade 1 card says only "Market at the overridden daily-open anchor". The card record carries 07:00 UK / 09:00 broker, so the log contradicts the artefact. | §2 attribute table; header line 3; §10 counter order; §4 six-source table; §20 "Override applied"; §21b Trade 1 Entry row | 3 | Name the anchor time explicitly in §20 and on the Trade 1 card. |
| 1.2 Coverage & currency consistent | Every §2/§6/§13a/§13c date is D-1 or earlier; §13d is forward-looking; the session date is D. But §11's weekly block is the week ending **19 Jun**, one week stale, and is used throughout as the live weekly reference (§15, §16, §17, §18, Trade 1 invalidation). Its implied weekly close back-solves to 7,500.59, which equals the 18 Jun close carried in the 26 Jun report (7,500.58) — confirming the stale week. §4 also dates Investing.com at 24 Jun while §5/§6 rely on it for 22–25 Jun. | §11 "Weekly (W/E 19 Jun)"; §16/§17 "7,494 weekly pivot"; §4 Investing.com row; cross-check `reports/md/SP500_Report_26Jun2026.md` §6 | 2 | Rebuild the weekly pivot block from the week 22–26 Jun and re-propagate. |
| 1.3 Audience & tone | Byline "Senior US Equity Strategist · Trading and risk review (forward-test)"; §18 is a strategist judgement with three ranked reasons and a single watch item; no retail framing, no promotional language, no "you should" constructions anywhere. | Header lines 5–6; §18 | 5 | None. |
| 2.1 Sections present & ordered | All of §1–§21 present in order, including the four-part §13 (13a per-article, 13b aggregate with numeric tilt, 13c previous-period, 13d upcoming) and the four-part §21 (21a conviction, 21b cards, 21c 5-session backtest, 21d what-is-working plus the limitations boilerplate). §17 is a single sentence. A "Technical Judgement Summary" table follows §21d as an addition, not a displacement. | Headings throughout | 5 | None. |
| 2.2 Scorecard as a table | §6 is a proper table carrying Date/O/H/L/C/RSI2/Trend/Src A/Src B/Validation — all ten required columns. §11 fails: the **monthly** pivot table is absent entirely, and daily and weekly are crammed into one four-column grid padded with "---" rather than presented as separate ordered tables. Daily runs R5→P→S5 (a superset of R3→P→S3, correctly ordered); weekly runs R3→WP→S3. | §6 table; §11 table | 2 | Add the monthly pivot table; split §11 into per-timeframe tables. |
| 2.3 Method steps visible | §4 observations → §4 Class. column → §5 consensus build with a stated ±0.10 tolerance and a weighted-median rule. §8 is candle-by-candle for all five sessions with close-location percentages and an explicit sequence assessment. §9 states overlap 0.58, persistence 0.59, |directional mean| 0.14, median RSI2 46.9, VOLator +0.19 / slope +0.23, KER −0.09, and shows the dual-gate logic that resolves TRANSITION. §7 carries five captioned chart placeholders — images dropped in the pandoc conversion, accepted as evidence per the brief and noted here. | §4, §5, §8, §9, §7 | 4 | Note the image-conversion loss in-report. |
| 3.1 Quantitative claims sourced | §1's figures resolve to §4/§6/§9/§21a. §14 cross-references §10 and §13d properly. §12 does not: "Dow outperformed (+0.6% on the week)", "Nasdaq fell ~4.6%", "swaps price ~36% odds", and the index's "~28% foreign revenue base" carry no source and appear in no evidence table. The 36% figure is later reused in §13d and §14 as if established. | §12 five bullets; §14 Rates block; §13d FOMC row | 2 | Source or cross-reference every §12 number. |
| 3.2 Citations exist & contain data | Three spot-checks. (a) **S&P DJI via FRED**, 26 Jun, 7,354.02 — named, dated, and used identically in §1, §3, §4, §6, §18, §21b: internally clean. (b) **Investing.com**, dated 24 Jun with raw close 7,358.22 — the row itself is consistent, but §5/§6 use that source as Src A for 22–25 Jun, and §4's note "~4pt offset on some sessions" contradicts §5's "~4–11 points" about the same source. (c) **"Investment digest"**, 25–26 Jun, 7,357.49, Basis "Intraday" yet supplying a *close* — no named publisher, and §6's 25 Jun row lists two sources (Investing × Digest) while its Validation cell reads "SINGLE-SOURCE (indicative)". Contradictory and weakly attributed, but no row is internally impossible, so **no fabrication override is triggered**. | §4 rows 1/4/6; §5; §6 row 25 Jun | 2 | Name the digest publisher; align the offset statement and the source/validation labels. |
| 3.3 Calculations transparent | Pivots reproduce **exactly** from the report's own 26 Jun H/L/C (7,392.95 / 7,294.18 / 7,354.02): P 7,347.05, R1 7,399.92, S1 7,301.15, R2 7,445.82, S2 7,248.28, R3 7,498.69, S3 7,202.38, and R1.5/S1.5/R4/S4/R5/S5 all follow — every one matches to the cent. The weekly block is likewise internally consistent (back-solved H 7,577.91 / L 7,402.60 / C 7,500.59). RSI2 reproduces from the report's own last three closes (helper: 0.0, 0.0, 0.0 — exact). Fails: **ATR(14) is never stated numerically**, only inferable at ≈111.7 from the "3.5×ATR cap of 391 pts" and the 3×ATR level 7,018.6; §21a lists five weighted terms (−0.25, −0.15, −0.10, −0.03, +0.01) that sum to **−0.52**, not the stated **−0.57**, and the sixth weighted term is missing; VOLator +0.19 and slope +0.23 are asserted with no derivation. | §11 (all levels recomputed); §6 note + helper `--closes` output; §21b caps; §21a; §9 | 2 | State ATR(14); show all six weighted terms so Σ signal×weight reproduces the score. |
| 3.4 Numbers reconcile | Holds: D-1 close 7,354.02 identical in §1/§3/§4/§6/§18 and as the Trade 1 entry reference; §11 daily pivots equal the levels quoted on Trade 2 (S1 7,301.2 / S1.5 7,274.7 / S2 7,248.3, P 7,347.05, stop 7,389.4 = P + 0.8×(R1−P) = 7,389.35); RSI2 in §6 matches §8. Fails, five of them: (i) §6 Trend for 22 Jun is "Neutral" but §8 opens "22 Jun (see §6): **bearish**"; (ii) §13b counts "3 Bearish (3 institutional)" while §13a classes CNBC as Media — 2 institutional + 1 media; (iii) §20 says the backtest was "reconstructed at each t−1 close" but every §21c entry is that session's **Open** from §6 (7,500.4 / 7,366.5 / 7,370.9 / 7,360.5 / 7,359.8); (iv) §21a components do not sum to the stated score; (v) Trade 3C states one TP of 6,826.9 while the card record carries TP1 7,050.0 / TP2 6,950.0 / TP3 6,900.0 — three levels that appear nowhere in the report. | §6 vs §8; §13a vs §13b; §20 vs §21c; §21a; §21b Trade 3C vs `cards/baseline/by_date/2026-06-29.json` | 1 | Reconcile all five before regeneration. |
| 4.1 Pillars conclude | §8 → "Bearish continuation — exhaustion / reversal risk into support"; §9 → "Transitional (bearish drift)" with a stated preferred protocol; §10 → "Aggregate cross-asset confirmation: CONFIRM (bearish)"; §12 → each of six bullets ends in a signed label with a cyclical/structural tag; §14 → each block ends price-negative or price-supportive. All five labels are consistent with the content above them. The §21 strategy pillar is the weak one: it concludes in a card set that is not executable as written (see 4.3). | §8, §9, §10, §12, §14, §21b | 4 | Fix the §21 output; prose pillars are sound. |
| 4.2 Peer/cross-asset interpreted | §10 supplies a genuine mechanism per counter, not a correlation list: USD → multinational earnings-translation drag plus tighter global conditions; VIX → implied-vol gauge, sub-20 read as elevated-but-not-stressed; DAX → European equity beta to the same global risk factor. Each has 5-day direction, status and implication, and §14 re-uses the dollar as the named transmission channel. Levels check out against the slices: USDX last 101.41 vs "~101.3"; VIX last 18.78 vs "~18.4–19.7" and §14's "high-18s/19s". | §10 table; §14 Liquidity/FX and Volatility blocks; `USDX_upto_2026-06-28.csv`, `VIX_upto_2026-06-28.csv` final bars | 5 | None. |
| 4.3 Synthesis reconciles tensions | The prose reconciliation is real: §9 explicitly resolves KER (Ranging) against a positive VOLator slope into TRANSITION rather than RANGE; §15 sets the 26 Jun lower-wick and RSI2-pinned-at-0 oversold case against the five-close sequence; §16 gives both an invalidation trigger and a continuation trigger; §21a states the §17 forecast and the conviction score agree. But the synthesis is anchored on the stale weekly pivot — "below weekly pivot and weekly S1" recurs in §11, §15, §16, §17, §18 and as Trade 1's invalidation level — and it terminates in a card set with hard construction faults: Trade 2's TP1 (7,301.2) sits **above** its short entry (7,296.6), its runner is aimed "toward pivot P (7,347.05)", also above entry; Trade 1's TP3 (7,018.6) is not beyond TP2 (6,946.1); Trade 3C's stop is not derived from the 3C rule and it carries no TP2/TP3, no tranche statement and no thesis invalidation. Card construction is scored here per brief §2. | §9, §15, §16, §18; §11/§16/§17 weekly references; §21b all three cards; lint rows | 1 | Rebuild all three cards to the M5 rules; re-anchor on the correct weekly pivot. |
| 4.4 Calibrated language | §17 is exactly one sentence with one conditional, no hedge stacking. §3 states confidence explicitly and split: "High (close); Medium (intraday)". §5 and §19 label indicative data as indicative rather than asserting it. §21d refuses to over-claim from one closed reconstruction ("insufficient closed triggers to rank meaningfully") and carries the five-session limitations boilerplate verbatim. | §17; §3 Confidence cell; §21d | 5 | None. |
| 5.1 Data dated; staleness flagged | Every §6 row, §4 row and §13a article is dated; the single-source-indicative status of the last two sessions' H/L and the 25 Jun close is flagged in §3, §5, §6, §19 and again on the cards — this is done thoroughly and consistently. The gap is the weekly block: it is *labelled* "W/E 19 Jun" but never *flagged as stale*, and §16/§17 then treat 7,494 as the live weekly pivot. | §6 Validation column; §19 "Live vs indicative"; §11 weekly header vs §16/§17 | 3 | Flag or replace the stale week. |
| 5.2 Assumptions up front | The single-source pivot propagation is handled well: §19 states all §11 levels are SINGLE-SOURCE-INDICATIVE and both Trade 2 and Trade 3C repeat it in their caveats. The anchor-override caveat is logged in §20 and referenced on the Trade 1 card, but incompletely — the override's destination is never specified, so the assumption is announced without being stated. | §19; §20 "Override applied"; §21b Trade 1 Caveats; Trade 2/3C Caveats | 3 | Specify the overridden anchor value. |
| 5.3 Red flags surfaced | §12 carries six signed risk bullets and §15 gives a four-by-four bull/bear grid. But the §13d → card link the brief asks for is missing: §13d names quarter-end/mega-cap AI commentary as "highest-impact upcoming item", and no card caveat mentions it — Trade 1's caveats are wide-stop and single-source H/L only. §13d also lists only thematic items and omits every dated calendar entry available in the window (e.g. 29 Jun Dallas Fed Manufacturing Index, ECB Lagarde speech, EUR CPI/HICP). | §12; §15; §13d; §21b caveat rows; `news_upto_2026-06-28.csv` rows dated 2026-06-29 | 2 | Carry §13d collisions into every card caveat; add the dated events. |
| 5.4 Restrictions honoured | Most restrictions hold: no synthesised price is presented as sourced (indicative is labelled indicative); no retail CFD quotes in the OHLC basis; §19 states "no futures blended into OHLC"; instrument common names are used ("Dollar Index", "VIX", "DAX 40"); no bracketed variable placeholders survive. **Breach:** §20 prints the module code "**M5 trace:**" in the report body (line 532), which the brief's 5.4 forbids. | grep of the full report returns exactly one hit: line 532 "**M5 trace:** direction-score weights = defaults" | 1 | Remove the module code. Triggers the restriction-breach override. |

## 2. Category roll-up

| Category | Level | Multiplier | Points | Justification |
|---|---|---|---|---|
| C1 Prompt adherence (max 20) | 2 | 0.40 | 8.0 | Rows 1.1/1.2/1.3 = 3/2/5, mean 3.33 → level 3; the restriction breach at 5.4 drops C1 one level to **2** per framework §4. Variables, counters, basis and lookback are respected; the anchor override is under-specified and the weekly reference is a week stale. |
| C2 Structure (max 20) | 4 | 0.85 | 17.0 | Rows 2.1/2.2/2.3 = 5/2/4, mean 3.67 → level 4. Section inventory and ordering are complete and the method chain is visible end to end; the monthly pivot table is missing and §11 is malformed as a single padded grid. |
| C3 Accuracy & evidence (max 25) | 2 | 0.40 | 10.0 | Rows 3.1/3.2/3.3/3.4 = 2/2/2/1, mean 1.75 → level 2. Internal arithmetic (pivots, RSI2) reproduces exactly, but 12 of 20 §6 OHLC fields breach the brief's basis tolerance, the D-1 close is out by 18.22 pts and the 25 Jun open by 67.40 pts, the weekly pivot is off by 101.13 pts, ATR(14) is unstated, the conviction score does not sum, and five cross-section reconciliations fail. No source is provably fabricated, so C3 is not zeroed. |
| C4 Reasoning & judgment (max 20) | 4 | 0.85 | 17.0 | Rows 4.1/4.2/4.3/4.4 = 4/5/1/5, mean 3.75 → level 4. The analytical pillars, the cross-asset mechanism and the calibration are genuinely strong; the deduction is concentrated in 4.3, where card construction (scored here per brief §2) fails on all three cards and the synthesis rests on the stale weekly pivot. Card mechanics are additionally captured outside the 100 in §4 below. |
| C5 Currency, restrictions & transparency (max 15) | 2 | 0.40 | 6.0 | Rows 5.1/5.2/5.3/5.4 = 3/3/2/1, mean 2.25 → level 2. Indicative-data discipline is a strength; the stale week is unflagged, the anchor assumption is incomplete, §13d never reaches the card caveats, and a module code appears in the body. |
| **Total** | — | — | **58** | Σ(multiplier × max) = 8.0 + 17.0 + 10.0 + 17.0 + 6.0 = 58.0 → **58**. |

## 3. Total, band, override check

- Raw total: **58** (8.0 + 17.0 + 10.0 + 17.0 + 6.0).
- **Restriction breach: YES.** §20 line 532 carries the module code "**M5 trace:**" in the report body, which brief row 5.4 forbids ("no module codes (M1..M5)"). Framework §4 caps the total at Moderate (74) and drops C1 at least one level. The C1 drop is applied (level 3 → level 2, −4.0 points, already reflected above). The 74 cap is **not binding**, since the post-drop total of 58 is already below it.
- **Fabricated source: NO.** Three cited sources were spot-checked for internal consistency. The FRED/S&P DJI row is clean and consistent across six sections. The Investing.com and "Investment digest" rows are weakly attributed and contradicted *elsewhere* in the report (date-of-use, offset magnitude, source count vs validation label), but no row states a figure that contradicts its own quote or is impossible on its face. The Low cap and C3 = 0 are therefore **not** applied.
- Final Trust Score: **58** · Band: **Low** (40–59) · Override recorded: **restriction_breach**.
- Note: the report sits 2 points below the Moderate boundary on its own merits, not because of the cap. The restriction breach still costs it 4 points via the mandatory C1 drop.

## 4. Card Integrity

Linter rows from `qa/regen_20260906_qa1/lint_static/2026-06-29.csv`, verbatim:

| card_id | report_date | strategy | flags | dud |
|---|---|---|---|---|
| 2026-06-29_Trade_1 | 2026-06-29 | Trade 1 - Daily Directional | WARN_TP3_ORDER | False |
| 2026-06-29_Trade_2 | 2026-06-29 | Trade 2 - Pivot (sell stop below daily S1) | DUD_TP1_SIDE | True |
| 2026-06-29_Trade_3C | 2026-06-29 | Trade 3C - Momentum-Breakout (sell stop, conditional) | CLEAN | False |

Per-card integrity, 100 − 40·(#DUD) − 10·(#WARN), floored at 0:

| Card | #DUD | #WARN | Integrity |
|---|---|---|---|
| 2026-06-29_Trade_1 | 0 | 1 | 100 − 10 = **90** |
| 2026-06-29_Trade_2 | 1 | 0 | 100 − 40 = **60** |
| 2026-06-29_Trade_3C | 0 | 0 | **100** |

Non-suppressed cards: 3 of 3 (no card is marked suppressed, and the direction score −0.57 is past the ±0.25 threshold, so Trade 1 is correctly not suppressed).

**Report Card Integrity = (90 + 60 + 100) / 3 = 83.3**

M5 rule assessment behind row 4.3 (this does **not** change the integrity number above):
- **Trade 1** — TP3 7,018.6 is the 3×ATR price cap, which for a short is *nearer* to entry than TP2 6,946.1; recorded as TP3 it violates the TP3-beyond-TP2 rule (the WARN). The runner is a time-stop-or-cap construct and should be recorded as such with TP3 null. Entry, stop derivation (5-day swing high + 0.25×ATR), R within the 3.5×ATR cap, 1R/2R targets, the BE+0.2R rule and the wide-stop flag are all internally correct; the anchor is not explicit.
- **Trade 2** — the DUD. TP1 is set at daily S1 7,301.2 while the entry is a sell-stop at 7,296.6, i.e. *below* S1. For a short, TP1 must be below entry; here it is 4.6 pts above, so Unit 1 would be an instant adverse fill. Compounding it, the runner is aimed "toward pivot P (7,347.05)", 50 pts above the entry. The stop arithmetic (P + 0.8×(R1−P) = 7,389.35) is correct but is the TREND rule mirrored, applied under a TRANSITION regime. No three-unit tranche statement on the card.
- **Trade 3C** — lints CLEAN only because the card record carries TP1 7,050.0 / TP2 6,950.0 / TP3 6,900.0, which are strictly descending and inside the 2.5×ATR TP1 cap. The report itself states a single TP of 6,826.9 (= 1× range width) that appears nowhere in the record and would sit 383 pts from entry, beyond the 2.5×ATR cap of 276.9. The stop ≈7,349.7 is described as "generous" rather than derived; the 3C rule (low + 0.40×width) gives 7,395.7 on slice numbers. No TP2/TP3 in the report, no tranche statement, no thesis invalidation separate from the stop.

## 5. Data reconciliation log

Basis: slice cash session 16:30–23:00 broker = 09:30–16:00 ET. Brief tolerance: |Δ| ≤ 3 pts on a close, ≤ 8 pts on O/H/L. Δ = report − slice.

**§6 Validated OHLC table (all twenty fields):**

| Section | Field | Report value | Slice value | Delta | Verdict |
|---|---|---|---|---|---|
| §6 | 22 Jun Open | 7,500.44 | 7,513.10 | −12.66 | Discrepancy (>8) |
| §6 | 22 Jun High | 7,530.01 | 7,538.80 | −8.79 | Discrepancy (>8) |
| §6 | 22 Jun Low | 7,460.01 | 7,467.30 | −7.29 | Within tolerance |
| §6 | 22 Jun Close | 7,472.79 | 7,479.30 | −6.51 | Discrepancy (>3) |
| §6 | 23 Jun Open | 7,366.51 | 7,370.40 | −3.89 | Within tolerance |
| §6 | 23 Jun High | 7,424.17 | 7,431.80 | −7.63 | Within tolerance |
| §6 | 23 Jun Low | 7,347.60 | 7,356.20 | −8.60 | Discrepancy (>8) |
| §6 | 23 Jun Close | 7,365.46 | 7,374.40 | −8.94 | Discrepancy (>3) |
| §6 | 24 Jun Open | 7,370.88 | 7,389.00 | −18.12 | Discrepancy (>8) |
| §6 | 24 Jun High | 7,428.06 | 7,438.00 | −9.94 | Discrepancy (>8) |
| §6 | 24 Jun Low | 7,336.82 | 7,346.00 | −9.18 | Discrepancy (>8) |
| §6 | 24 Jun Close | 7,358.22 | 7,372.30 | −14.08 | **FAIL** (close wrong by >10) |
| §6 | 25 Jun Open | 7,360.50 | 7,427.90 | −67.40 | **FAIL** (8× tolerance) |
| §6 | 25 Jun High | 7,389.40 | 7,432.60 | −43.20 | **FAIL** (5× tolerance) |
| §6 | 25 Jun Low | 7,340.20 | 7,332.90 | +7.30 | Within tolerance |
| §6 | 25 Jun Close | 7,357.49 | 7,365.90 | −8.41 | Discrepancy (>3) |
| §6 | 26 Jun Open (D-1) | 7,359.80 | 7,323.80 | +36.00 | **FAIL** (4× tolerance) |
| §6 | 26 Jun High (D-1) | 7,392.95 | 7,402.10 | −9.15 | Discrepancy (>8) |
| §6 | 26 Jun Low (D-1) | 7,294.18 | 7,303.10 | −8.92 | Discrepancy (>8) |
| §6 | 26 Jun Close (D-1) | 7,354.02 | 7,335.80 | +18.22 | **FAIL** (close wrong by >10) |

Twelve of twenty fields breach tolerance; five are outright Category 3 failures. Direction of error is not uniform (25 Jun O/H are far too low, 26 Jun O and C are too high), so this is not a constant CFD-vs-cash basis offset. For reference the D-1 full-broker-day close is 7,345.60 (Δ +8.42), so the report's close does not match the full-day basis either.

**RSI2:**

| Section | Field | Report value | Slice / recomputed | Delta | Verdict |
|---|---|---|---|---|---|
| §6 | 22 Jun RSI2 | 74.3 | 0.0 (helper, RSI2 on slice cash closes) | −74.3 | **FAIL** vs slice; not testable from the report's own closes (needs pre-window closes) |
| §6 | 23 Jun RSI2 | 0.0 | 0.0 (slice) | 0.00 | Reconciles |
| §6 | 24 Jun RSI2 | 0.0 | 0.0 (slice) / 0.0 (from report's own closes) | 0.00 | Reconciles — exact test of report arithmetic |
| §6 | 25 Jun RSI2 | 0.0 | 0.0 (slice) / 0.0 (from report's own closes) | 0.00 | Reconciles — exact test |
| §6 | 26 Jun RSI2 | 0.0 | 0.0 (slice) / 0.0 (from report's own closes) | 0.00 | Reconciles — exact test |

The RSI2 arithmetic on the report's own close column is correct where testable. The 22 Jun print of 74.3 is the one RSI2 value that does not reproduce on the slice sequence.

**§11 daily pivots — reproduction from the report's own 26 Jun H 7,392.95 / L 7,294.18 / C 7,354.02:**

| Level | Report | Recomputed from report's own H/L/C | Delta | Verdict | Slice cash D-1 pivot | Delta vs slice |
|---|---|---|---|---|---|---|
| P | 7,347.05 | 7,347.05 | 0.00 | Reproduces exactly | 7,347.00 | +0.05 |
| R1 | 7,399.92 | 7,399.92 | 0.00 | Reproduces exactly | 7,390.90 | +9.02 |
| S1 | 7,301.15 | 7,301.15 | 0.00 | Reproduces exactly | 7,291.90 | +9.25 |
| R2 | 7,445.82 | 7,445.82 | 0.00 | Reproduces exactly | 7,446.00 | −0.18 |
| S2 | 7,248.28 | 7,248.28 | 0.00 | Reproduces exactly | 7,248.00 | +0.28 |
| R3 | 7,498.69 | 7,498.69 | 0.00 | Reproduces exactly | 7,489.90 | +8.79 |
| S3 | 7,202.38 | 7,202.38 | 0.00 | Reproduces exactly | 7,192.90 | +9.48 |
| R1.5 / S1.5 | 7,422.87 / 7,274.72 | 7,422.87 / 7,274.72 | 0.00 | Reproduce exactly | 7,418.45 / 7,269.95 | +4.42 / +4.77 |
| R4 / S4 / R5 / S5 | 7,597.46 / 7,103.61 / 7,696.23 / 7,004.84 | same | 0.00 | Reproduce exactly | — | — |

All thirteen daily levels reproduce to the cent from the report's own inputs (row 3.3 satisfied). The residual gap to the slice is inherited from the §6 H/L errors, not from the pivot arithmetic; P, R2 and S2 land within a third of a point because the H and L errors offset.

**§11 weekly pivots — wrong week:**

| Section | Field | Report value | Slice value (prior week 22–26 Jun, cash) | Delta | Verdict |
|---|---|---|---|---|---|
| §11 | Weekly P | 7,493.70 | 7,392.57 | +101.13 | **FAIL** — stale week (W/E 19 Jun) |
| §11 | Weekly R1 | 7,584.80 | 7,482.03 | +102.77 | **FAIL** |
| §11 | Weekly S1 | 7,409.49 | 7,246.33 | +163.16 | **FAIL** |
| §11 | Weekly R2 | 7,669.01 | 7,628.27 | +40.74 | **FAIL** |
| §11 | Weekly S2 | 7,318.39 | 7,156.87 | +161.52 | **FAIL** |
| §11 | Weekly R3 | 7,760.11 | 7,717.73 | +42.38 | **FAIL** |
| §11 | Weekly S3 | 7,234.18 | 7,010.63 | +223.55 | **FAIL** |
| §11 | Monthly pivots | absent | — | — | **FAIL** — required table missing |

The weekly block is internally self-consistent (back-solving gives H 7,577.91 / L 7,402.60 / C 7,500.59) but is built from the week ending 19 Jun. The 26 Jun report carries an 18 Jun close of 7,500.58, confirming the source week. Consequence: the report's repeated claim that price sits "below weekly S1" is false on the correct week — 7,335.80 is above the corrected weekly S1 of 7,246.33 — and §11's claimed weekly-S3/25-day-low confluence at 7,234–7,238 does not exist on the corrected week (weekly S3 = 7,010.63).

**Other quantities:**

| Section | Field | Report value | Slice value | Delta | Verdict |
|---|---|---|---|---|---|
| §21b | ATR(14), implied from "3.5×ATR cap of 391 pts" | ≈111.7 | 110.76 (cash) | +0.94 | Consistent, but never stated explicitly |
| §21b | ATR(14), implied from 3×ATR level 7,018.6 | ≈111.8 | 110.76 (cash) | +1.04 | Consistent |
| §8, §21b | 5-day swing high | 7,530.01 | 7,538.80 (22 Jun) | −8.79 | Discrepancy — feeds the Trade 1 stop |
| §8, §11 | 5-day swing low | 7,294 | 7,303.10 (26 Jun) | −9.10 | Discrepancy |
| §8, §16, §21b | 25-day low | 7,238 | 7,243.10 (9 Jun) | −5.10 | Minor discrepancy — feeds the 3C trigger |
| §21b | 25-day range width | 383 | 381.50 | +1.50 | Within tolerance |
| §1, §9 | Range percentile of D-1 close | ~30th | 29.1% (report close on slice 25-day range) | −0.9pp | Reconciles |
| §10, §14 | Dollar Index | ~101.3 | 101.41 (last bar) | −0.11 | Reconciles |
| §10, §14 | VIX | ~18.4–19.7 / "high-18s/19s" | 18.78 (last bar) | in range | Reconciles |
| §21a | Direction score | −0.57 | Σ of the five stated components = −0.52 | −0.05 | **FAIL** — components do not sum to the score |
| §21b/card | Trade 3C TP set | single TP 6,826.9 | card record TP1 7,050.0 / TP2 6,950.0 / TP3 6,900.0 | — | **FAIL** — report and card record disagree entirely |
| §20 vs §21c | Backtest entry basis | "reconstructed at each t−1 close" | §21c entries equal the §6 Open column | — | **FAIL** — stated method contradicts the table |

**Cross-report consistency (reports dated before D only):** `SP500_Report_26Jun2026.md` §6 carries 22, 23 and 24 Jun with OHLC and RSI2 identical to the 29 Jun report to the cent, including the 22 Jun RSI2 of 74.3 — the data lineage is internally consistent across reports even though it diverges from the slice. One conflict: the 26 Jun report validates 22/23/24 Jun as "CORROB. (Δ0.00)" via Investing × FRED, while the 29 Jun report downgrades the 24 Jun row to "Close single-src offset — indicative". The same row cannot be both.

**As-of session check:** PASS. The last bar in the slice is 2026-06-26 23:45 broker; 2026-06-29 is a Monday; the report names "Last completed session Friday 26 June 2026" in §2 and dates §6's final row 26 Jun. The report is anchored on D-1 and not on an earlier session.
