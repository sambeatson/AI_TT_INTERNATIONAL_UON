# Trust Score — 2026-06-15 — SP500_Report_15Jun2026.md

Run: `regen_20260906_qa1` · Asset: US500 · D = 2026-06-15 · D-1 slice = `data/slices/US500/US500_upto_2026-06-14.csv`
Basis note: slice is the broker CFD M15 feed; cash-session (16:30–23:00 broker) figures used throughout.
Reference values from `engine/qa_slice_stats.py`: D-1 cash close **7431.90**, ATR14 (cash) **94.04**,
daily pivots P 7418.17 / R1 7472.43 / S1 7377.63 / R2 7512.97 / S2 7323.37 / R3 7567.23 / S3 7282.83,
5-day swing 7243.10–7486.40, 25-day swing 7243.10–7624.60 (width 381.50).

## 1. Section 7 checklist

| Item | Reviewer notes | Evidence observed | Score 0–5 | Action required |
|---|---|---|---|---|
| 1.1 Variables respected | Asset is the S&P 500 **cash** index (not ES); counters USDX · VIX · DAX 40 with USDX first; as-of NY close of D-1 (12 Jun) in America/New_York; 5-session execution block + 25-session regime block; USD / index points / tick 0.01; six sources in §4 plus institutional tier in §13a. Deductions: the Trade 1 entry line reads "07:00 UK anchor / **NY open**", two mutually exclusive anchors, and §20 states the anchor was "overridden to the 12 Jun close as the t-anchor", a third. Separately, M5 requires Trade 2 SUPPRESSED when every pivot tier is single-source-indicative — §19 states all daily/weekly/monthly pivot inputs carry that flag, yet Trade 2 is produced under a "lenient-corroboration override". | Header line 3; §2 table; §4 (6 rows); §21b Trade 1 "Entry"; §20 "Daily-open anchor overridden…"; §19 "lenient-corroboration override" | 3 | Pick one anchor and state it identically on the card and in §20. Either emit Trade 2 as a SUPPRESSED row or remove the blanket single-source flag with a second intraday source. |
| 1.2 Coverage & currency consistent | Every priced observation is dated 12 Jun or earlier; §13d correctly carries only forward-dated events; §20 timestamp 14 Jun (UK) precedes D. No currency or unit drift — everything is index points/USD, SPY explicitly scaled ×10 and quarantined to directional use. Minor: StreetStats stamped "12 Jun 16:57 ET" against a §2 definition that excludes after-market, unexplained as a publication time. | §2, §4, §6, §13, §20 | 4 | Label the 16:57 ET stamp as a publication time or replace with the 16:00 ET settle. |
| 1.3 Audience & tone | Consistent senior-strategist register throughout; §1 and §18 are written for a trading-and-risk review; no retail framing, no promotional language, risks stated plainly. | §1, §12, §15, §18 | 5 | None. |
| 2.1 Sections present & ordered | All of §1–§21 present in order, including §13a/b/c/d and §21a/b/c/d, and §21d carries the limitations boilerplate. §17 is a single sentence. Deduction: §15's table contains exactly one bullet per side (a 1×2 stub); the substance is in the prose beneath it rather than the required balance table. | Headings throughout; §15 lines 374–393; §21d limitations note | 4 | Populate the §15 table with the risks already argued in the prose beneath it. |
| 2.2 Scorecard as a table | §6 is a table but its columns are Date/O/H/L/C/RSI2/Trend/**Validation** — the required **Source A**, **Source B** and **Final** columns are absent, so per-row provenance is asserted only in a footnote. §11 daily and weekly tables run R3→S2 only: **S3 is missing on both** (report's own inputs give daily S3 = 7284.12, weekly S3 = 7039.86); the monthly table carries only P/R1/S1, i.e. one level per side against the required three. `grep -i "S3"` on the report returns nothing. | §6 header row; §11 all three tables | 2 | Add Source A/Source B/Final columns to §6; extend all three §11 tables to R3→P→S3. |
| 2.3 Method steps visible | §4 lists raw observations → normalization → basis → relevance; §5 states the classification and the weighted-median consensus rule and names what was down-weighted and why. §8 is genuinely candle-by-candle with an explicit sequence assessment. §9 shows the regime with overlap 0.49, persistence 0.62, percentile ~51, VOLator slope and KER. §7 charts are pandoc image refs with a caption (accepted per brief; images not renderable here). Deduction: §5 names the weighted-median method but shows none of its arithmetic. | §4–§9 | 4 | Show the weighted-median computation in §5. |
| 3.1 Quantitative claims sourced | §1 numbers all trace to §6/§9/§13/§21. §12 largely sourced (FactSet named for 21.9%/23.2%, BofA named, CPI/PPI resolve to §13c). Unsourced: WTI "≈ $86" and the "first ~100%-probability hike out to early 2027" in §12; **Fed funds 3.50–3.75% and 10Y 4.47% in §14 carry no source and no cross-reference**. §10's VIX figures are also unsourced and do not survive the slice check (below). | §12, §14, §10 | 3 | Source or cross-reference the §14 rates block, the WTI level and the rate-path claim. |
| 3.2 Citations exist & contain data | Three spot-checks. (a) StockAnalysis/Tiingo SPY 741.75 → "≈7,417 (×10)": arithmetic correct (7417.5) and correctly excluded from the definitive level — consistent. (b) **Trading Economics "7,431 (+0.50%)"**: the +0.50% is internally consistent (7394.30→7431.46 = +0.503%), but §5 and §20 use this source as one of two that corroborate 7,431.46 "within the ±0.10-pt equity-index tolerance" while its own normalized figure is 7,431.0 — a 0.46-pt delta. §20 states "delta < 0.5 pt, tolerance ±0.10 pt" in one sentence, which cannot both hold. (c) Reuters poll / GS / UBS "median year-end target 7,620; GS 8,000; UBS 7,900": the quoted median sits below both named constituents and coincides to the point with the report's own record-high level, unverifiable but not impossible. All sources are named; none is impossible on its face, so **no fabrication override is triggered** — the defect is the corroboration claim, not the source. | §4, §5, §13a, §20 | 3 | Restate the corroboration on a tolerance the quoted figures actually satisfy, or drop Trading Economics from the corroborating pair. |
| 3.3 Calculations transparent | Strong where shown: RSI2 rows 3–5 reproduce **exactly** from the report's own closes (helper returns 0.0 / 51.5 / 100.0 against stated 0.0 / 51.5 / 100.0); all five Trend labels are correct under the stated rule; §11 daily and weekly pivots reproduce to 0.01 from the report's own H/L/C on all six printed levels; §21a score reproduces exactly (0.250+0.100+0.000−0.019+0.083+0.150 = **+0.564**) on the mandated weights; §13b tilt reproduces exactly as Σ(weight×polarity)/6 = **+0.55**; §8's five close-location percentages all reproduce from §6 (14.8 / 60.7 / 0.8 / 88.2 / 73.3); KER stated with its parameters (13-session, 3-EMA). **Failure: ATR(14) is never stated numerically anywhere in the report** — `grep` finds only "ATR-based", "0.25×ATR", "3.5×ATR cap", "3×ATR cap". Every stop buffer, the wide-stop test and both runner caps are therefore unverifiable (the Trade 1 offset of 24.10 pts implies ATR ≈ 96.4; the slice gives 94.04). S3 is nowhere computed. | §6, §8, §9, §11, §13b, §21a | 3 | State ATR14 numerically in §9 and reuse that one number in every ×ATR expression in §21b. |
| 3.4 Numbers reconcile | D-1 close 7,431.46 is identical in §1, §3, §4, §6 and the §21b Trade 1 entry reference. §11 pivots match the levels quoted on the cards (Trade 2 entry 7470.90 = daily R1; Trade 3C stop 7416.96 = daily P). RSI2 in §6 matches every value repeated in §8. Failures: (i) ATR cannot be reconciled between §9 and §21 because it is absent; (ii) the extracted card carries **entry 7431.51 against a stated close of 7431.46**; (iii) the extracted Trade 2 card carries **tp3 = 7620.0, a level that appears nowhere in the §21b Trade 2 table**; (iv) the §5/§20 ±0.10-pt tolerance contradiction; (v) §16's base-case range 7,360–7,530 and §17's 7,510–7,530 band are both breached by Trade 1's own TP2 7,616.6 and TP3 7,709.1; (vi) §21c implies R ≈ 48 pts (7,410.85→7,431.46 = 20.61 pts = +0.43R) against the live card's R = 92.6. | cross-section; `cards/baseline/by_date/2026-06-15.json` | 2 | Set card entry to the D-1 close exactly; delete or derive Trade 2's tp3; reconcile the backtest R model with the live card. |
| 4.1 Pillars conclude | §8 closes "transitional-bullish signature"; §9 closes "Ranging — Downward Bias" within a Transitional block; §10 closes with an explicit "Aggregate cross-asset read: CONFIRM". §12 labels each block (price-negative to neutral / price-supportive / caution) but never resolves them into one direction. §14 ends on watch items with no direction label at all. | §8–§10, §12, §14 | 4 | Add a closing direction label to §12 and §14. |
| 4.2 Peer/cross-asset interpreted | §10 supplies real transmission mechanisms rather than a correlation list — dollar → multinational earnings translation, VIX → implied-vol collapse as a risk-on signal, DAX → common global-risk factor — and names the dollar as the swing variable. USDX checks out against the slice (stated ≈99.8 vs 99.809; "spiked >100 mid-week" matches 10 Jun 100.059). Deduction: **the VIX row's levels are wrong** — stated 5-day path 19.4 → 17.7 against a slice path of 18.12 → 18.72 (the slice peak is 20.43 on 10 Jun), and §13c's "VIX −9%" on 12 Jun is −4.05% on the slice. The direction of the last two sessions is right; the magnitudes are not. DAX unverifiable (no slice). | §10, §13c | 4 | Restate the VIX levels and the 12 Jun VIX percentage from source. |
| 4.3 Synthesis reconciles tensions | Prose synthesis is competent: §16 explicitly states it respects rather than contradicts the Transitional regime and gives a base-case invalidation; §21a asserts consistency with §17. But the central tension is never addressed — §9 reads the medium term as "Ranging — Downward Bias" with a negative VOLator slope, while §20 assigns the medium-term signal **+0.5** (contribution +0.100) with no explanation. **The card layer, scored here, departs from M5 in five places**: Trade 3C's entry is the 5-day swing high 7,483.15 rather than a confirmed close beyond the 25-day boundary by ≥0.25×ATR (≥ 7,648 on slice), its stop is the daily pivot rather than low + 0.40×width (7,395.70), and its TPs are ±1R/±2R rather than 1.0×/1.5× width; Trade 3C's thesis invalidation (7,416.96) is **identical to its stop** (7,416.96) against the explicit "separate from the stop" rule, and its be_rule is NONE against the mandatory U3 → entry+0.2R on U2 fill; Trade 2's structural stop is placed 0.10 pt below the pivot rather than pivot − 0.25×ATR. | §9 vs §20; §21b all three cards; card JSON `be_rule`/`tp3` | 2 | Rebuild Trade 3C on the 3C rule; add the 0.25×ATR buffer to Trade 2's stop; give 3C a distinct invalidation and the BE rule; justify the medium-term signal sign. |
| 4.4 Calibrated language | §17 is **exactly one sentence**, carries an explicit condition ("contingent on a non-hawkish FOMC") and does not stack hedges. Confidence "High" is stated in §1, §3 and §18. Deduction: the calibration does not hold across sections — §17 projects 7,510–7,530 "over the coming week" while the same report's Trade 1 targets 7,616.6 and 7,709.1, and no confidence is attached to any card. | §1, §3, §17, §18, §21b | 4 | Bring the card targets inside the forecast band or widen/justify the band; state a confidence per card. |
| 5.1 Data dated; staleness flagged | Every §6 row and every §4 observation is dated; the single-source-indicative status of intraday H/L is flagged in the §6 footnote and again in §19, and its propagation into pivots is stated. **Failure: §13a has no date column** — six articles carry source, class, sentiment and quote but no date, so their currency cannot be assessed, and this is the table that feeds the +0.55 tilt into the direction score. | §6 footnote, §19, §13a | 3 | Add a date column to §13a. |
| 5.2 Assumptions up front | §19 states the single-source-indicative flag, its propagation to all pivot tiers, the May-proxy monthly basis, the SPY ×10 normalization and the lenient-corroboration override; §20 states the anchor override and the blocked endpoints. All three cards carry the single-source-indicative caveat. **Failure: the anchor-override caveat is absent from the Trade 1 card**, which instead asserts a clean "07:00 UK anchor / NY open" — the brief requires it on the card *and* in §20. | §19, §20, §21b Caveats rows | 3 | Add the anchor-override caveat to the Trade 1 card. |
| 5.3 Red flags surfaced | §12 surfaces the BofA sell-side contrarian signal and elevated valuations; §15 gives the hawkish-FOMC and Iran-re-escalation downside; §13d identifies the FOMC as the highest-impact event and that collision is carried explicitly into the caveats of **all three** cards; §16 states a base-case invalidation level. | §12, §15, §13d, §21b | 5 | None. |
| 5.4 Restrictions honoured | Clean on most: no module codes (`grep` for M1–M5 returns nothing), no framework name, no bracketed variable names, no ES futures price used anywhere (futures appear only as a scope descriptor in §2), instrument common names throughout, and no synthesised price presented as sourced — the May monthly proxy is flagged indicative in both §11 and §19. **Concern: CFD material sits inside the close/OHLC basis.** §4 lists Trading Economics with basis "Cash/**CFD** ref" at relevance **Core**, and §5 promotes exactly that source to one of the two independent sources that make the close CORROBORATED; and Investing.com, which §5 itself describes as CFD-derived for its live header, is the sole source of every intraday H/L in §6. §5 does deliberately exclude the Investing.com live header, showing the restriction was understood — so this is scored as an unresolved basis ambiguity rather than an unambiguous breach, and **no restriction_breach override is fired**. | §4 basis column, §5, §6 footnote, §19; grep results | 2 | Re-label the Trading Economics basis unambiguously and replace it in the corroborating pair with a cash-only source. |

## 2. Category roll-up

Rounding: category level = mean of its rows, rounded half-up to the nearest whole level.

| Category | Level | Multiplier | Points | Justification |
|---|---|---|---|---|
| C1 Prompt adherence (max 20) | 4 | 0.85 | 17.00 | Rows 3, 4, 5 → mean 4.00. Variables, counters, timezone, lookback, units and source count are all respected; the deductions are the three-way anchor contradiction and the M5 Trade 2 suppression rule being overridden rather than applied. |
| C2 Structure (max 20) | 3 | 0.65 | 13.00 | Rows 4, 2, 4 → mean 3.33 → 3. Every section and subsection is present and correctly ordered, but the two mandated tables are malformed: §6 is missing Source A/Source B/Final, and all three §11 tables are short of the R3→P→S3 requirement (S3 absent entirely from the report). |
| C3 Accuracy & evidence (max 25) | 3 | 0.65 | 16.25 | Rows 3, 3, 3, 2 → mean 2.75 → 3. Internal arithmetic is genuinely strong — RSI2, both pivot sets, §21a, §13b and §8 all reproduce exactly — but ATR14 is never stated, the ±0.10-pt corroboration claim contradicts its own quoted figures, §14's rates are unsourced, the VIX figures fail the slice check, and four of five §6 opens sit outside the open/low tolerance. |
| C4 Reasoning & judgment (max 20) | 4 | 0.85 | 17.00 | Rows 4, 4, 2, 4 → mean 3.50 → 4. Pillar conclusions, cross-asset mechanism and forecast discipline are solid; the card layer is the weak point — Trade 3C is not built on the 3C rule at all, Trade 2's stop misses its 0.25×ATR buffer, 3C's invalidation duplicates its stop, and the medium-term signal sign is never reconciled with the §9 read. |
| C5 Currency, restrictions & transparency (max 15) | 3 | 0.65 | 9.75 | Rows 3, 3, 5, 2 → mean 3.25 → 3. Disclosure is a genuine strength (§19/§20 are candid about every override and limitation) and red flags are carried into the cards, but §13a is undated, the anchor-override caveat never reaches the card, and CFD-referenced material sits at Core relevance inside the close basis. |
| **Total** | — | — | **73.00** | Σ points = 17.00 + 13.00 + 16.25 + 17.00 + 9.75 |

## 3. Total, band, override check

- **Raw total: 73.00 → 73 (integer).**
- **Band: Moderate** (60–74).
- **Override check — fabricated source:** NOT triggered. Three sources were spot-checked (Tiingo/SPY, Trading Economics, Reuters/GS/UBS). Each is named; the SPY ×10 normalization is arithmetically exact; the Trading Economics +0.50% change is internally consistent with §6. The defect found is that §5/§20 claim a ±0.10-pt corroboration that the source's own 0.46-pt delta cannot satisfy — a false corroboration claim about a real, self-consistent quote, not a source that contradicts itself or is impossible. Scored under 3.2/3.4; **C3 is not zeroed**.
- **Override check — restriction breach:** NOT triggered. Module codes, framework name, bracketed variable names and ES-futures pricing are all absent (verified by grep). No synthesised price is presented as sourced — the May monthly proxy is flagged indicative in §11 and §19. The one live concern is CFD material inside the close/OHLC basis (Trading Economics at "Cash/CFD ref", Core, used in the corroborating pair; Investing.com the sole intraday H/L source). Because §5 explicitly identifies and down-weights the CFD-derived feed, the restriction was understood and partly applied; the residue is an ambiguous basis label rather than an unambiguous breach. Scored hard at row 5.4 (level 2) instead of firing the cap.
- **Override applied: none.** Final Trust Score **73 / 100 — Moderate**.
- Note: the score sits one point under the Moderate/High boundary. Fixing either malformed table set (§6 columns, §11 S3 levels) or stating ATR14 would move C2 or C3 up a level and carry the report into the High band.

## 4. Card Integrity

Linter rows, verbatim from `qa/regen_20260906_qa1/lint_static/2026-06-15.csv`:

| card_id | report_date | strategy | flags | dud |
|---|---|---|---|---|
| 2026-06-15_Trade_1 | 2026-06-15 | Trade 1 - Daily Directional | CLEAN | False |
| 2026-06-15_Trade_2 | 2026-06-15 | Trade 2 - Pivot (buy stop daily R1) | CLEAN | False |
| 2026-06-15_Trade_3C | 2026-06-15 | Trade 3C - Breakout (buy stop 5-day swing high) | CLEAN | False |

Per-card integrity (100 − 40·#DUD − 10·#WARN, floored at 0):

| Card | #DUD | #WARN | Integrity |
|---|---|---|---|
| 2026-06-15_Trade_1 | 0 | 0 | 100 |
| 2026-06-15_Trade_2 | 0 | 0 | 100 |
| 2026-06-15_Trade_3C | 0 | 0 | 100 |

**Report mean over non-suppressed cards (3 of 3): 100.0**

All three cards clear every static check the engine enforces — stop on the correct side, TP1 beyond entry, TP2 beyond TP1, TP3 beyond TP2, R inside the 0.3–3.0×ATR14 window (92.6 / 54.04 / 66.19 against ATR14 94.04 → 0.98× / 0.57× / 0.70×), TP1 inside 2.5×ATR14, both buy-stop levels above the D-1 close, anchor explicit. Integrity is therefore 100.0 and **this number says nothing about M5 conformance** — the construction defects found against the M5 rules (Trade 3C built on the wrong rule entirely, Trade 2's missing 0.25×ATR stop buffer, 3C's invalidation duplicating its stop, 3C's missing BE rule, Trade 2 produced where M5 requires suppression, and the card entry 7431.51 against a 7431.46 close) are scored at checklist row 4.3 and listed in the feedback file.

## 5. Data reconciliation log

Tolerances per brief §4: |Δ| ≤ 3 pts on a close, ≤ 8 pts on an open/high/low = consistent. A close wrong by > 10 pts, or an RSI2 that does not reproduce from the report's own closes, is a Category 3 failure.

### §6 — five-row OHLC against the D-1 slice (cash session)

| Section | Field | Report value | Slice value | Delta | Verdict |
|---|---|---|---|---|---|
| §6 Mon 8 Jun | Open | 7,440.57 | 7,451.8 | −11.23 | **DISCREPANCY** (> 8 pt open tolerance) |
| §6 Mon 8 Jun | High | 7,466.81 | 7,471.3 | −4.49 | Consistent |
| §6 Mon 8 Jun | Low | 7,395.13 | 7,398.8 | −3.67 | Consistent |
| §6 Mon 8 Jun | Close | 7,405.73 | 7,411.0 | −5.27 | **DISCREPANCY** (> 3 pt close tolerance; < 10, not a C3 failure) |
| §6 Tue 9 Jun | Open | 7,438.66 | 7,454.4 | −15.74 | **DISCREPANCY** (> 8) |
| §6 Tue 9 Jun | High | 7,483.15 | 7,486.4 | −3.25 | Consistent |
| §6 Tue 9 Jun | Low | 7,237.85 | 7,243.1 | −5.25 | Consistent |
| §6 Tue 9 Jun | Close | 7,386.65 | 7,387.3 | −0.65 | Consistent |
| §6 Wed 10 Jun | Open | 7,350.54 | 7,351.1 | −0.56 | Consistent |
| §6 Wed 10 Jun | High | 7,396.56 | 7,400.7 | −4.14 | Consistent |
| §6 Wed 10 Jun | Low | 7,265.93 | 7,271.5 | −5.57 | Consistent |
| §6 Wed 10 Jun | Close | 7,266.99 | 7,271.7 | −4.71 | **DISCREPANCY** (> 3; < 10, not a C3 failure) |
| §6 Thu 11 Jun | Open | 7,287.67 | 7,305.0 | −17.33 | **DISCREPANCY** (> 8; largest single deviation) |
| §6 Thu 11 Jun | High | 7,412.68 | 7,416.6 | −3.92 | Consistent |
| §6 Thu 11 Jun | Low | 7,257.33 | 7,260.0 | −2.67 | Consistent |
| §6 Thu 11 Jun | Close | 7,394.30 | 7,391.9 | +2.40 | Consistent |
| §6 Fri 12 Jun | Open | 7,410.85 | 7,420.9 | −10.05 | **DISCREPANCY** (> 8) |
| §6 Fri 12 Jun | High | 7,456.40 | 7,458.7 | −2.30 | Consistent |
| §6 Fri 12 Jun | Low | 7,363.01 | 7,363.9 | −0.89 | Consistent |
| §6 Fri 12 Jun | Close | 7,431.46 | 7,431.90 | −0.44 | Consistent — the headline close is sound |

Pattern: highs, lows and closes sit inside tolerance on 13 of 15 fields, but **four of five opens are 10–17 pts below the slice, all in the same direction**. This is not a symmetric CFD-vs-cash basis; it is a systematic bias in the open column only, and those same opens are the entries used in the §21c backtest.

### §6 — RSI2, two independent tests

| Section | Field | Report value | (a) Slice RSI2 | Δ vs slice | (b) Recomputed from the report's own closes | Verdict |
|---|---|---|---|---|---|---|
| §6 Mon 8 Jun | RSI2 | 9.9 | 8.46 | +1.44 | n/a (needs pre-window closes) | Consistent with slice |
| §6 Tue 9 Jun | RSI2 | 53.5 | 43.84 | +9.66 | n/a (needs pre-window closes) | Note — large gap, but untestable from the report's own closes and traceable to the differing pre-window closes |
| §6 Wed 10 Jun | RSI2 | 0.0 | 0.00 | 0.00 | **0.0** | Exact — reproduces |
| §6 Thu 11 Jun | RSI2 | 51.5 | 50.98 | +0.52 | **51.5** | Exact — reproduces |
| §6 Fri 12 Jun | RSI2 | 100.0 | 100.00 | 0.00 | **100.0** | Exact — reproduces |

Every RSI2 value that can be tested against the report's own close sequence reproduces to the digit. **No Category 3 RSI2 failure.** All five Trend labels are also correct under the stated rule (8 Jun Bearish, 9 Jun Neutral — C<O but RSI2 53.5 > 50, 10 Jun Bearish, 11 Jun Bullish, 12 Jun Bullish).

### §11 — pivots reproduced from the report's own D-1 H/L/C (7,456.40 / 7,363.01 / 7,431.46)

| Section | Level | Report value | Recomputed from report's own H/L/C | Delta | Slice (cash) | Δ vs slice | Verdict |
|---|---|---|---|---|---|---|---|
| §11 daily | P | 7,416.96 | 7,416.96 | 0.00 | 7,418.17 | −1.21 | Exact |
| §11 daily | R1 | 7,470.90 | 7,470.90 | 0.00 | 7,472.43 | −1.53 | Exact |
| §11 daily | S1 | 7,377.51 | 7,377.51 | 0.00 | 7,377.63 | −0.12 | Exact |
| §11 daily | R2 | 7,510.35 | 7,510.35 | 0.00 | 7,512.97 | −2.62 | Exact |
| §11 daily | S2 | 7,323.57 | 7,323.57 | 0.00 | 7,323.37 | +0.20 | Exact |
| §11 daily | R3 | 7,564.29 | 7,564.29 | 0.00 | 7,567.23 | −2.94 | Exact |
| §11 daily | S3 | **absent** | 7,284.12 | — | 7,282.83 | — | **MISSING — malformed table** |
| §11 weekly | P | 7,384.15 | 7,384.15 | 0.00 | 7,387.13 | −2.98 | Exact |
| §11 weekly | R1 | 7,530.46 | 7,530.46 | 0.00 | 7,531.17 | −0.71 | Exact |
| §11 weekly | S1 | 7,285.16 | 7,285.16 | 0.00 | 7,287.87 | −2.71 | Exact |
| §11 weekly | R2 | 7,629.45 | 7,629.45 | 0.00 | 7,630.43 | −0.98 | Exact |
| §11 weekly | S2 | 7,138.85 | 7,138.85 | 0.00 | 7,143.83 | −4.98 | Exact |
| §11 weekly | R3 | 7,775.76 | 7,775.76 | 0.00 | 7,774.47 | +1.29 | Exact |
| §11 weekly | S3 | **absent** | 7,039.86 | — | — | — | **MISSING — malformed table** |
| §11 monthly | P/R1/S1 | 7,504.37 / 7,675.07 / 7,409.37 | internally consistent (implies H 7,599.37, L 7,333.67, C 7,580.07) | — | May proxy, not in slice | — | Internally consistent; R2/R3/S2/S3 **MISSING** |

Every printed pivot reproduces to the cent from the report's own inputs, and every one sits inside basis tolerance against the slice. The defect is completeness, not arithmetic.

### Other cross-checks

| Section | Report value | Slice / recomputed value | Delta | Verdict |
|---|---|---|---|---|
| §9 / §21b | ATR(14) — **never stated numerically** | 94.04 (cash) · 109.68 (full-day) | — | **FAILURE** — every 0.25×ATR, 3×ATR and 3.5×ATR expression is unverifiable; Trade 1's 24.10-pt buffer implies ATR ≈ 96.4 |
| §10 VIX | 5-day path 19.4 → 17.7, "Falling" | 18.12 → 18.72 (peak 20.43 on 10 Jun) | start −1.28 / end +1.02 | **DISCREPANCY** — both endpoints wrong; the 5-day net move is slightly *up*, not down |
| §13c VIX | "VIX −9%" on 12 Jun | 19.51 → 18.72 = −4.05% | −4.95 pp | **DISCREPANCY** — overstated by ~2× |
| §10 USDX | ≈ 99.8, "spiked >100 mid-week then reversed" | 12 Jun 99.809; 10 Jun 100.059; 8 Jun 100.029 | +0.01 | Consistent |
| §10 DAX 40 | 24,210 → 24,635 | no slice available | — | Unverifiable |
| §9 25-day range | 7,237.85 – 7,620.90 (width 383.05) | 7,243.10 – 7,624.60 (width 381.50) | low −5.25 / high −3.70 / width +1.55 | Consistent |
| §8 5-day swing high | 7,483.15 | 7,486.40 | −3.25 | Consistent |
| §8 5-day swing low | 7,237.85 | 7,243.10 | −5.25 | Consistent |
| §1/§3/§4/§6/§21b | D-1 close 7,431.46 (identical in all five) | 7,431.90 | −0.44 | Consistent and internally reconciled |
| Card JSON Trade 1 | entry 7,431.51 | report's own close 7,431.46 | +0.05 | **DISCREPANCY** — a MARKET entry must equal the D-1 close exactly |
| Card JSON Trade 2 | tp3 7,620.0 | not present anywhere in the §21b Trade 2 table | — | **DISCREPANCY** — unsourced card field |
| §9 percentile | "~51st percentile" | 50.5% from the report's own range | −0.5 pp | Consistent |
| §13c | "S&P +0.50% to 7,431.46" | +0.503% from §6 closes | 0.00 | Exact |
| §13b | tilt +0.55 | Σ(weight×polarity)/6 = 0.550 | 0.00 | Exact |
| §21a / §20 | score +0.56 (+0.564) | Σ of stated contributions = +0.564 | 0.00 | Exact |
| §21d | mean R +0.03 | mean of §21c column = +0.03 | 0.00 | Exact |
| §8 close locations | 15% / 61% / 1% / 88% / 73% | 14.8 / 60.7 / 0.8 / 88.2 / 73.3 from §6 | ≤ 0.8 pp | Exact |
| §5 / §20 | TE corroborates 7,431.46 "within ±0.10 pt" | TE normalized 7,431.0 → 0.46 pt delta | +0.36 pt over tolerance | **DISCREPANCY** — claim contradicts its own quoted figure |
| §21c vs §21b | backtest implies R ≈ 48 pts (7,410.85→7,431.46 = 20.61 = +0.43R) | live Trade 1 R = 92.6 | ~44.6 pts | **DISCREPANCY** — two different risk models in one report |
