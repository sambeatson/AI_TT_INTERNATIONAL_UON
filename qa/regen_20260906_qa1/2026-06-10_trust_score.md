# Trust Score — 2026-06-10 — SP500_Report_10Jun2026.md

Run: `regen_20260906_qa1` · D = 2026-06-10 · asset US500 · data cut D-1 = 2026-06-09
Slice: `data/slices/US500/US500_upto_2026-06-09.csv` (cash session 16:30–23:00 broker = 09:30–16:00 ET)
Framework: `docs/AI_Output_Trust_Score_Framework_v3.7.txt` §4–§7, anchored by `REVIEWER_BRIEF.md`.

## 1. Section 7 checklist

| Item | Reviewer notes | Evidence observed | Score 0–5 | Action required |
|---|---|---|---|---|
| 1.1 Variables respected | Asset correct and explicitly distinguished from ES futures; counters USDX/VIX/DAX 40 in the required order; as-of NY close of D-1 with tz stated; 5-session execution and 25-session regime lookbacks; USD / index points / tick 0.01 all stated. Two failures: (a) the daily-open anchor is overridden to **00:00 UK** where this M1 instance specifies **07:00 UK**, and unlike the 9 Jun report this one never maps 00:00 UK onto a tradable cash-session timestamp; the extracted card records `anchor_broker 09:00` (= 07:00 UK), contradicting the report body. (b) §4 claims "six core exchange/index sources" but the seven rows resolve to only **five distinct** sources (Investing.com ×2, CNBC ×3 counting the Reuters/CNBC row). | §2 definition table and anchor note; §4 evidence table + footnote; §20 as-of override bullet; `cards/baseline/by_date/2026-06-10.json` anchor field | 2 | State the 07:00 UK anchor or justify the override with an executable timestamp; make the card anchor match the body; re-count §4 to six *distinct* sources or drop the claim. |
| 1.2 Coverage & currency consistent | Every data date in §2/§4/§6/§11/§13 is 3–9 Jun (≤ D-1); session date is D; run timestamp 9 Jun evening. Units are index points/USD throughout with no drift. Minor: §13d dates events only as "This week"/"Ongoing"; the 3 Jun close (7,553.68) differs from the 9 Jun report's 7,553.47 by 0.21 pt — outside the ±0.10 pt index tolerance the report itself asserts. | §2 as-of row; §6 date column; §13c/§13d; cross-check vs `reports/md/SP500_Report_09Jun2026.md` §6 | 4 | Date the §13d rows; reconcile the 3 Jun close against the prior report or explain the revision. |
| 1.3 Audience & tone | Senior US Equity Strategist byline; institutional register throughout; §18 is a desk-style judgement with a single watch item; no retail framing, no promotional language, no "you should" constructions. | §1 header block; §18; §21d limitations paragraph | 5 | None. |
| 2.1 Sections present & ordered | All 21 sections present in the mandated order, including the full sub-structure: §13a per-article table, §13b aggregate with a numeric tilt (−0.34), §13c previous-period calendar, §13d upcoming calendar; §21a conviction, §21b cards, §21c 5-session backtest, §21d what-is-working plus the limitations boilerplate. | Headings §1–§21d | 5 | None. |
| 2.2 Scorecard as a table | §6 is a table but **merges Source A and Source B into a single "Source / validation" column and omits the "Final" column**; the 9 Jun report renders Src A / Src B / Validation separately, so this is a regression. §11 gives three pivot tables in correct descending order, but each carries **five levels per side (R5→S5)** where the spec is three (R3→P→S3). | §6 header row; §11 three tables | 3 | Restore discrete Source A / Source B / Final / Validation columns in §6; trim §11 to R3→P→S3 or justify the extension tiers. |
| 2.3 Method steps visible | §4 lists observations with basis and relevance, §5 gives classification and the weighted-median consensus build with an explicit exclusion rationale; §8 is candle-by-candle across all five sessions and closes with a sequence assessment; §9 states regime with overlap 0.448, persistence 0.522, range position 0.395 and the VOLator dual-gate resolution. §7 carries five chart placeholders (pandoc drops the images) — accepted as evidence, noted; only 7.4 has a caption. | §4–§9 | 5 | Optionally add captions to 7.1–7.3 and 7.5 so the placeholders remain self-describing after conversion. |
| 3.1 Quantitative claims sourced | §1 numbers trace to §6/§11. But §10, §12 and §14 carry **six unsourced quantitative claims**: DAX 24,616 (−0.6%), Brent ≈ $91, 10-year yield 4.47–4.56%, gold ≈ $4,286, VIX ≈18–19, USDX ≈99.2. None appears in §4 or §13a. The USDX figure is also **wrong against the slice** (D-1 close 99.972) and its stated *direction* is inverted (see §5 log). | §10 table; §12 bullets 5–6; §14 bullets 1,3,4,5,6 | 2 | Give each §10/§12/§14 figure a named, dated source or a §4/§13a pointer; correct the USDX level and direction. |
| 3.2 Citations exist & contain data | Three spot-checks are internally consistent and none is impossible: CNBC 8 Jun "added 0.3% to close at 7,405.73" reproduces as +0.298% from 7,383.74 and matches §6; CNBC 9 Jun "fell 0.26%" reproduces as −0.258% from 7,405.73 and matches §1; AP/BNN 5 Jun "worst day since October" matches §13c's −2.6% and reproduces as −2.645%. **No fabricated source — the hallucination override does not fire.** Defects: §6 names Source B for 3–4 Jun as "narrative", which is not a named dated citation; §20's corroboration-pair log covers only 9/8/5 Jun while §19 asserts all five closes are two-source corroborated; the Forex.com quote pivots on 7,334 while the report's own §6 puts the 9 Jun low at 7,330, i.e. already through it. | §4; §6 validation column; §13a rows 1,3,4,6; §19; §20 corroboration bullet | 2 | Name the 3–4 Jun Source B; log all five corroboration pairs in §20; reconcile the Forex.com level against the report's own 9 Jun low. |
| 3.3 Calculations transparent | Strong. RSI2 reproduces **exactly** from the report's own close sequence for all three testable rows (13.2 / 9.9 / 53.5, helper `--closes` recomputation). All five Trend labels are correct under the Close-vs-Open + RSI2-50 rule. **All 33 pivot levels across the daily, weekly and monthly tables reproduce exactly** from the H/L/C each table states. §9 range position 0.395 reproduces as 0.394 from the report's own 25-session bounds. ATR(14)=73.5 and smoothed KER +0.02 are both stated. Gaps: ATR 73.5 is 10.9% below the slice cash ATR14 of 82.45; §21a shows only three of six weighted contributions (−0.13/−0.09/−0.05 vs a −0.33 total) and never prints the 0.25/0.20/0.10/0.15/0.15/0.15 weights, so Σ signal×weight is not reproducible. | §6 RSI2 and Trend columns; §11 all three tables; §9; §20 technical trace; §21a | 4 | Print all six §21a signal×weight terms; reconcile the ATR basis. |
| 3.4 Numbers reconcile | D-1 close 7,386.65 is identical in §1, §3, §4 and §6, and §11 pivot levels match those quoted on the cards (7,331 / 7,441 / 7,460 / 7,471 / 7,214 / 7,105); ATR 73.5 is consistent between §20 and §21b; §6 RSI2 equals §8. Four failures: (i) the §21b Trade 1 entry is 7,330, not the D-1 close — the anchor market-entry reconciliation required by 3.4 does not hold; (ii) §6's 9 Jun **Low of 7,330.00 is the Trading Economics CFD figure that §4/§5/§19 all declare excluded** from the OHLC basis; (iii) §8 lists supports as "7,330 (5-day low), then the 19 May swing low at 7,333" — 7,333 is *above* 7,330, so the ordering is impossible; (iv) §21d's hit-rates contradict §21c's own outcomes — Trade 2 TP1 is claimed at 100% although one of four rows closed at +0.7R, and TP2 at 50% although no row reached +2R. | §1/§3/§4/§6 close; §21b entry rows; §4 vs §6 9 Jun low; §8 support sentence; §21c vs §21d | 2 | Fix the §8 support ordering; recompute §21d hit-rates from the §21c rows; remove the CFD low from the OHLC basis; make the Trade 1 entry an anchor market order at the D-1 close. |
| 4.1 Pillars conclude | §8 closes on "Judgement label: Indecision — reversal risk"; §9 on regime TRANSITION plus a preferred-protocol line; §10 on "Aggregate cross-asset: MIXED" with an explicit contradiction flag; §12 and §14 tag every bullet price-negative / neutral / uncertain. Deduction: §9's own conclusion is "reduced conviction — wait for confirmation … favour reactive, level-based trades over directional commitment", yet §21b issues three full-size directional cards, one of which (Trade 2) is a range-edge fade the M5 regime map reserves for RANGE. | §8 judgement label; §9 preferred-trade-protocol bullet; §10 aggregate row; §12/§14 tags; §21b | 4 | Align §21b's aggression with §9's stated protocol, or state why the protocol is overridden. |
| 4.2 Peer/cross-asset interpreted | §10 supplies a genuine transmission mechanism per counter — dollar → global financial conditions and earnings translation; VIX → implied-vol gauge driving de-rating; DAX → shared global risk factor — rather than a correlation list, and carries the USDX contradiction forward to §15/§16 instead of resolving it away. (The mechanism is well argued; the input direction is wrong, scored under 3.1.) | §10 mechanism and implication columns; §10 contradiction flag | 5 | None on structure. |
| 4.3 Synthesis reconciles tensions | §9 resolves the KER-vs-volatility conflict explicitly through the dual gate; §15 sets the softer-USDX upside risk against the downside case; §16 defers to the CPI catalyst and declines to assert a trend; §21a confirms §17 and the direction score agree and names the live tension. Deduction: the synthesis does not carry into the cards. Trade 2 fades a range edge under a TRANSITION regime (M5: transition → breakout side only), and §11's own instruction that daily pivots "cannot anchor level-based limit orders" is contradicted by §21b placing a sell limit and two stop entries on exactly those tiers. | §9 dual-gate bullet; §15; §16; §21a conflict flag; §11 note vs §21b | 3 | Either suppress/re-cast Trade 2 to the breakout side, or lift §11's own prohibition explicitly rather than silently. |
| 4.4 Calibrated language | §17 is exactly one sentence. Confidence is stated as Medium with tone balanced-to-bearish in §3 and repeated in §18. No hedge stacking; the forecast commits to a direction and names its single invalidating condition. | §17; §3 confidence column; §18 | 5 | None. |
| 5.1 Data dated; staleness flagged | Every §6 row is dated, every §13a article is dated, and the single-source O/H/L fields are asterisked in §6 with a footnote, restated in §11 per pivot set and again in §19. Deduction: the §12/§14 macro figures (gold, Brent, 10-year, DAX) carry no date, so their staleness cannot be judged. | §6 asterisks and footnote; §11 notes; §13a date column; §19; §12/§14 | 4 | Date the §12/§14 macro observations. |
| 5.2 Assumptions up front | The anchor override is stated in the §2 note and again in §20; single-source pivot propagation is disclosed in §11, §19 and each card's Caveats row. Deduction: the report never states how a 00:00 UK anchor is executed on an instrument that does not trade then (the 9 Jun report did map it to the cash open), and the extracted card's `anchor_broker 09:00` (07:00 UK) contradicts the body. | §2 anchor note; §19 relaxation paragraph; §20; §21b Caveats rows; card JSON | 3 | Add the execution mapping for the 00:00 UK anchor and reconcile it with the card metadata. |
| 5.3 Red flags surfaced | §12 and §15 both enumerate risks with direction tags; the §13d Tier-1 May CPI collision is carried into all three cards' Caveats; whipsaw risk and two-sided volatility are called out on Trade 3C; §21d closes with the required small-sample / no-slippage limitations boilerplate. | §12; §15 both lists; §21b Caveats ×3; §21d final paragraph | 5 | None. |
| 5.4 Restrictions honoured | **BREACHED.** §6's 9 Jun **Low = 7,330.00** is precisely the Trading Economics **US500 CFD/OTC** intraday figure that §4 marks "excluded from OHLC accept", §5 says was "down-weighted to directional-only", and §19 says is "excluded from OHLC acceptance and retained for directional colour only". It is nonetheless carried in the OHLC table, propagated into the daily pivot set (S1 7,331), and made the entry/break level of all three cards. Compounding it, §19 records a deliberate relaxation of the corroboration rule "so that trading strategies (§21) are produced rather than suppressed", and §11 states daily pivots "cannot anchor level-based limit orders" while §21b places one sell limit and two stop entries against those very tiers. Clean on the other restrictions: no module codes, no framework name, no bracketed variable names (grep-verified); ES futures explicitly excluded; instrument common names used throughout. | §4 last row vs §6 9 Jun row; §5 paragraph; §11 daily-pivot note vs §21b; §19 both paragraphs; §20 deviation flag | 1 | Remove the CFD low from the OHLC basis and rebuild §11 daily pivots from corroborated D-1 H/L/C, or suppress the level-based cards as the standing rule requires. |

## 2. Category roll-up

| Category | Level | Multiplier | Points | Justification |
|---|---|---|---|---|
| C1 Prompt adherence (max 20) | **3** | 0.65 | 13.00 | Rows 1.1/1.2/1.3 = 2/4/5, mean 3.67 → level 4. The restriction breach at 5.4 forces the mandatory one-level drop: **4 → 3**. |
| C2 Structure (max 20) | **4** | 0.85 | 17.00 | Rows 2.1/2.2/2.3 = 5/3/5, mean 4.33 → 4. All 21 sections and every sub-section present and ordered; the loss is confined to §6's merged source columns and §11's five-tier pivot tables. |
| C3 Accuracy & evidence (max 25) | **3** | 0.65 | 16.25 | Rows 3.1/3.2/3.3/3.4 = 2/2/4/2, mean 2.50 → 3 (round half up). Arithmetic is genuinely strong — RSI2 and all 33 pivot levels reproduce exactly from the report's own inputs — but the inputs themselves are wrong (9 Jun low off by 86.9 pts, 3 Jun close off by 11.5 pts) and six macro figures are unsourced. Sensitivity: rounding 2.50 down to level 2 gives a total of 67, still band Moderate. |
| C4 Reasoning & judgment (max 20) | **4** | 0.85 | 17.00 | Rows 4.1/4.2/4.3/4.4 = 4/5/3/5, mean 4.25 → 4. Prose reasoning is the strongest part of the report: real cross-asset mechanisms, an explicit dual-gate resolution, a carried-forward contradiction, a one-sentence forecast. Card construction — scored here per brief §2 — is where it loses ground (Trade 2 fading under TRANSITION; §11's own prohibition contradicted). |
| C5 Currency, restrictions & transparency (max 15) | **3** | 0.65 | 9.75 | Rows 5.1/5.2/5.3/5.4 = 4/3/5/1, mean 3.25 → 3. Disclosure discipline is otherwise good — the report flags its own deviations in §19 and §20 — but flagging a breach is not honouring the restriction, and 5.4 scores 1. |
| **Total** | — | — | **73.00 → 73** | Σ(multiplier × max) = 13.00 + 17.00 + 16.25 + 17.00 + 9.75 = 73.00. |

## 3. Total, band, override check

- **Raw total: 73** (13.00 + 17.00 + 16.25 + 17.00 + 9.75 = 73.00, rounded to a whole number).
- **Hallucinated-source override: NOT triggered.** Three cited sources were spot-checked for internal consistency (CNBC 8 Jun, CNBC 9 Jun, AP/BNN 5 Jun). Each is named, dated, and quotes a figure that reproduces from the report's own close sequence to within 0.01 pp. No cited source carries an impossible date or a figure contradicting its own quote. C3 is therefore scored on the merits, not zeroed.
- **Restriction-breach override: TRIGGERED.** A retail CFD quote (Trading Economics US500, 9 Jun intraday ≈7,330) is used in the OHLC basis at §6 after being declared excluded in §4, §5 and §19, and is then propagated into the §11 daily pivots and into the entry or break level of all three §21b cards. Effects applied: (a) total capped at **74**; (b) C1 dropped one level, 4 → 3. The cap is **not binding** here — 73 ≤ 74 — because the C1 drop has already removed 3.00 points (a level-4 C1 would have scored 17.00 and totalled 77).
- **Final Trust Score: 73 / 100.**
- **Band: Moderate (60–74).**
- **Override recorded: `restriction_breach`.**

## 4. Card Integrity

Linter rows, verbatim from `qa/regen_20260906_qa1/lint_static/2026-06-10.csv`:

| card_id | report_date | strategy | flags | dud |
|---|---|---|---|---|
| 2026-06-10_Trade_1 | 2026-06-10 | Trade 1 - Daily Directional (sell stop) | CLEAN | False |
| 2026-06-10_Trade_2 | 2026-06-10 | Trade 2 - Pivot (sell limit weekly P) | CLEAN | False |
| 2026-06-10_Trade_3C | 2026-06-10 | Trade 3C - Momentum-Breakout (sell stop) | CLEAN | False |

Per-card integrity (100 − 40·#DUD − 10·#WARN, floored at 0):

| Card | #DUD | #WARN | Integrity |
|---|---|---|---|
| 2026-06-10_Trade_1 | 0 | 0 | 100 |
| 2026-06-10_Trade_2 | 0 | 0 | 100 |
| 2026-06-10_Trade_3C | 0 | 0 | 100 |

**Report Card Integrity = 100.0** (mean over 3 non-suppressed cards; 0 suppressed).

*All three cards pass the static engine: stop on the correct side, TP1 beyond entry, TP2 beyond TP1, TP3 beyond TP2, R between 0.3× and 3.0× ATR14, TP1 within 2.5× ATR14, entry on the correct side of the D-1 close. Integrity 100.0 measures only that static geometry. The M5 construction assessment below is scored under checklist rows 4.1/4.3 and does not alter this number.*

M5 construction assessment (feeds rows 4.1/4.3, not the integrity figure):

| Card | M5 conformance | Defects |
|---|---|---|
| Trade 1 | Fails | Not a market order at the daily-open anchor (sell stop at 7,330, plus a second mutually exclusive "market on a failed retest of 7,460–7,471" on the same card); TP ladder is 0.5R/1R/2R where M5 requires TP1 = 1R and TP2 = 2R; R = 146 pts > 1×ATR (1.99×ATR reported, 1.77×ATR on the slice) with **no wide-stop flag**; stop 7,476 is the pivot cluster + 5 pts, not the tighter of (5-day swing extreme, nearest S/R) + 0.25×ATR; TP3 7,038 lies beyond the card's own 3×ATR runner cap (7,109.5). Correct: three equal units, Unit-3 → entry − 0.2R on Unit-2 fill (≈29 pts in profit, arithmetic checks), session-close time-stop, invalidation separate from the stop. |
| Trade 2 | Fails | Range-edge fade issued under a **TRANSITION** regime, where M5 permits the breakout side only; entry 7,460 sits between daily R1 (7,441) and R1.5 (≈7,468.5) rather than on a defined tier; stop 7,518 = shelf 7,517 + 1 pt, not structural + 0.25×ATR (7,535.4 reported / 7,537.6 slice) nor 3.5×ATR; TP3 stated in prose as "Daily P (7,386) → trail to 7,330" — 7,386 is *above* TP2 7,344 and therefore the wrong side for a short, with the card JSON resolving to 7,330; management text says "runner exit at pivot P" while TP3 is 7,330 ≠ P. M5 also requires suppression when the pivot tiers are single-source-indicative, which §19 states they are. Correct: TP1/TP2 exactly 1R/2R, three equal units, BE rule. |
| Trade 3C | Fails | Correct variant for the regime, but the breakout boundary is wrong: 3C requires a confirmed close beyond the **25-day** boundary by ≥ 0.25×ATR — the 25-day low is 7,243.10 (slice; 7,234 by the report's own §9), so the trigger must be ≤ 7,222.5 (slice) or ≤ 7,215.6 (report's own numbers), whereas the card triggers at 7,330/7,322, roughly 90–107 pts *inside* the range; stop 7,396 = entry + 1×ATR, not high − 0.40×width (width 381.5 → 152.6 pts); TP1 7,248 is 1R, not +1.0×width (6,940.5), and TP2 7,214 is 1.46R rather than 1.5×width; confirmation basis is a 5-minute close, not the specified confirmed close; **the stated invalidation (daily close above 7,386) sits inside the stop (7,396)**, so the two are not separable as the brief requires. |

## 5. Data reconciliation log

Tolerances per brief §4: |Δ| ≤ 3 pts on a close and ≤ 8 pts on an open/high/low is consistent (CFD-vs-cash basis); larger is a recorded discrepancy; a close wrong by > 10 pts, or an RSI2 that will not reproduce from the report's own closes, is a scored Category 3 failure. Slice values are cash-session (16:30–23:00 broker).

| Section | Report value | Slice value | Delta | Verdict |
|---|---|---|---|---|
| §6 Wed 3 Jun Open | 7,605.31 | 7,602.00 | +3.31 | Consistent |
| §6 Wed 3 Jun High | 7,605.35 | 7,608.00 | −2.65 | Consistent |
| §6 Wed 3 Jun Low | 7,551.22 | 7,556.00 | −4.78 | Consistent |
| §6 Wed 3 Jun Close | 7,553.68 | 7,565.20 | −11.52 | **FAIL — close error > 10 pts (Category 3)** |
| §6 Thu 4 Jun Open | 7,516.54 | 7,541.30 | −24.76 | Discrepancy (> 8 pts) |
| §6 Thu 4 Jun High | 7,598.19 | 7,604.30 | −6.11 | Consistent |
| §6 Thu 4 Jun Low | 7,516.54 | 7,535.00 | −18.46 | Discrepancy (> 8 pts); also identical to the stated Open to the cent |
| §6 Thu 4 Jun Close | 7,584.31 | 7,592.70 | −8.39 | Discrepancy (> 3 pts) |
| §6 Fri 5 Jun Open | 7,565.00 | 7,540.50 | +24.50 | Discrepancy (> 8 pts) |
| §6 Fri 5 Jun High | 7,565.00 | 7,545.30 | +19.70 | Discrepancy (> 8 pts); also identical to the stated Open to the cent |
| §6 Fri 5 Jun Low | 7,375.00 | 7,372.80 | +2.20 | Consistent |
| §6 Fri 5 Jun Close | 7,383.74 | 7,392.50 | −8.76 | Discrepancy (> 3 pts) |
| §6 Mon 8 Jun Open | 7,400.00 | 7,451.80 | −51.80 | Discrepancy (> 8 pts) |
| §6 Mon 8 Jun High | 7,448.00 | 7,471.30 | −23.30 | Discrepancy (> 8 pts) |
| §6 Mon 8 Jun Low | 7,388.00 | 7,398.80 | −10.80 | Discrepancy (> 8 pts) |
| §6 Mon 8 Jun Close | 7,405.73 | 7,411.00 | −5.27 | Discrepancy (> 3 pts) |
| §6 Tue 9 Jun Open | 7,409.00 | 7,454.40 | −45.40 | Discrepancy (> 8 pts); equals the full-broker-day open (7,409.0) exactly — wrong session basis |
| §6 Tue 9 Jun High | 7,440.00 | 7,486.40 | −46.40 | Discrepancy (> 8 pts) |
| §6 Tue 9 Jun Low | **7,330.00** | **7,243.10** | **+86.90** | **FAIL — load-bearing; this is the excluded CFD figure, and it sets daily S1, the §8 support, and all three card levels** |
| §6 Tue 9 Jun Close | 7,386.65 | 7,387.30 | −0.65 | Consistent |
| §6 RSI2 3 Jun | 14.9 | 16.23 (slice closes) | −1.33 | Basis difference; not testable from report closes (needs pre-window seed) |
| §6 RSI2 4 Jun | 35.3 | 35.21 (slice closes) | +0.09 | Consistent |
| §6 RSI2 5 Jun | 13.2 | 12.08 (slice) / **13.2 (report's own closes)** | 0.00 vs own closes | **Reproduces exactly** |
| §6 RSI2 8 Jun | 9.9 | 8.46 (slice) / **9.9 (report's own closes)** | 0.00 vs own closes | **Reproduces exactly** |
| §6 RSI2 9 Jun | 53.5 | 43.84 (slice) / **53.5 (report's own closes)** | 0.00 vs own closes | **Reproduces exactly** (the 9.7-pt gap to the slice is inherited from the wrong close inputs, not from the RSI2 arithmetic) |
| §6 Trend column, all 5 rows | Bearish/Neutral/Bearish/Neutral/Neutral | Rule: C>O & RSI2>50 Bullish; C<O & RSI2<50 Bearish; else Neutral | — | Consistent — all five labels correct on the report's own O/C/RSI2 |
| §11 Daily P / R1 / S1 / R2 / S2 / R3 / S3 | 7386 / 7441 / 7331 / 7496 / 7276 / 7551 / 7221 | Recomputed from the report's own H 7,440 / L 7,330 / C 7,386.65 | 0 on every level | **Reproduces exactly** (inputs are wrong; the arithmetic is not) |
| §11 Daily P / R1 / S1 | 7386 / 7441 / 7331 | 7372.27 / 7501.43 / 7258.13 (slice D-1 cash) | +13.7 / −60.4 / **+72.9** | **FAIL — the entire daily pivot set is displaced by the bad 9 Jun H/L** |
| §11 Weekly P / R1 / S1 / S2 | 7460 / 7545 / 7299 / 7214 | Recomputed from the report's own H 7,620.90 / L 7,375.00 / C 7,383.74 | 0 on every level | Reproduces exactly |
| §11 Weekly P / R1 / S1 / S2 | 7460 / 7545 / 7299 / 7214 | 7463.30 / 7553.80 / 7302.00 / 7211.50 (slice, 1–5 Jun cash) | −3.30 / −8.80 / −3.00 / +2.50 | Consistent (weekly set survives; only R1 marginally outside) |
| §11 Monthly P / R1 / S1 / R2 / S2 / R3 / S3 | 7471 / 7708 / 7343 / 7837 / 7105 / 8074 / 6977 | Recomputed from the report's own H 7,599.38 / L 7,233.62 / C 7,580.06 | 0 on every level | Reproduces exactly (May inputs not verifiable from a D-1 slice) |
| §11 R4/R5/S4/S5, all three tables | 12 extension levels | Recomputed as R3±(H−L) etc. from the report's own inputs | 0 on every level | Reproduces exactly; the tier count itself exceeds the R3→P→S3 spec (row 2.2) |
| §8 nearest support (5-day low) | 7,330 | 7,243.10 | +86.90 | **FAIL** — and §8 then lists 7,333 as the *next* support below 7,330, which is arithmetically impossible |
| §8 nearest resistance (5-day high) | 7,605 | 7,608.00 | −3.00 | Consistent |
| §9 25-session range | 7,234 – 7,621 | 7,243.10 – 7,624.60 | −9.10 / −3.60 | Low marginally outside tolerance; high consistent |
| §9 range position | 0.395 | 0.394 (from the report's own bounds and close) | +0.001 | Reproduces |
| §9 record high (1–2 Jun) | 7,620.90 | 7,624.60 (2026-06-02) | −3.70 | Consistent |
| §20 / §21b ATR(14) | 73.5 | 82.45 cash (94.81 full-day) | −8.95 (−10.9%) | Discrepancy — understates R-multiples on every card |
| §1/§3/§4/§6 D-1 close | 7,386.65 | 7,387.30 | −0.65 | Consistent |
| §10 / §14 VIX | "Rising / elevated (~18–19)" | D-1 close 18.52; 5-session 16.85 → 18.52 | ≈0 | Consistent in level and direction |
| §10 / §14 USDX | "**Falling** (~99.2)" | D-1 close **99.972**; 5-session 99.205 → 99.972 (**rising**) | −0.77 and **direction inverted** | **FAIL — the sole cross-asset contradiction in §10 rests on an inverted input; it propagates to §14, §15, §16 and the §21a conflict flag** |
| §10 DAX 40 | 24,616 (−0.6%) | No DAX slice supplied | n/a | Not checkable; also unsourced (row 3.1) |
| §4 vs §6, 9 Jun low | §4: CFD 7,330 "excluded from OHLC accept" | §6 uses 7,330.00 as the 9 Jun Low | — | **Internal contradiction — the restriction breach of row 5.4** |
| §21c vs §21d, Trade 2 | TP1 100%, TP2 50% | §21c rows: +1.0R, +1.4R, +0.7R, +0.9R | — | **FAIL** — TP1 (1R) reached on 3 of 4, not 4 of 4; TP2 (2R) reached on 0 of 4, not 2 of 4 |
| Cross-report, 3 Jun close | 7,553.68 | 7,553.47 (`SP500_Report_09Jun2026.md` §6) | +0.21 | Outside the ±0.10 pt tolerance the report itself asserts |
| Cross-report, 5 Jun O/H/L | 7,565.00 / 7,565.00 / 7,375.00 | 7,580 / 7,585 / 7,380 (`SP500_Report_09Jun2026.md` §6) | −15 / −20 / −5 | Same session's "indicative" O/H/L revised without note |
