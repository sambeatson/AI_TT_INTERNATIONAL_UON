# Trust Score — 2026-07-15 — SP500_Daily_Report_15Jul2026.md

Run: `regen_20260906_qa1` · Asset: US500 (S&P 500 cash index) · D = 2026-07-15 · D-1 slice = 2026-07-14
Framework: `docs/AI_Output_Trust_Score_Framework_v3.7.txt` §4–§7, anchored by `qa/regen_20260906_qa1/REVIEWER_BRIEF.md`.
Slice basis: `data/slices/US500/US500_upto_2026-07-14.csv` via `engine/qa_slice_stats.py` (cash session 16:30–23:00 broker).

---

## 1. Section 7 checklist

| Item | Reviewer notes | Evidence observed | Score 0–5 | Action required |
|---|---|---|---|---|
| 1.1 Variables respected | Asset is the S&P 500 cash index, not ES futures. Counters are USDX · VIX · DAX 40 with USDX first, in both the header and the §10 table. Timezone America/New_York declared. Lookback 5 sessions (execution) + 25 (regime). Units index points / USD. Daily-open anchor is 07:00 UK, the correct anchor for this instance. Two deviations: the as-of is declared as "15 July 2026", not the NY close of D-1, and §4 lists six evidence rows but only ~5 distinct providers (S&P DJI appears twice, as "S&P Dow Jones" and again as "S&P DJI / FRED"). | Header line 3–6; §2 attribute table; §4 six-row table; §10; §21b Trade 1 "Market at 07:00 UK anchor" | 3 | Restate the as-of as "NY close of 14 Jul 2026 (America/New_York)". Add a sixth genuinely distinct provider to §4 or drop the duplicate S&P DJI row and re-count. |
| 1.2 Coverage & currency consistent | All §6, §13a and §13c dates are D-1 or earlier; §13d is forward-dated as intended; no currency or unit drift (index points/USD throughout). But §11 builds the daily pivots from **13 Jul** H/L/C when 14 Jul (D-1) was available and is used everywhere else in the report — a stale prior period. §2 also books the as-of as D rather than the D-1 close. | §11 heading "Daily pivots (from 13 Jul H/L/C — indicative)"; §6 has a full 14 Jul row; §2 as-of row | 2 | Rebuild §11 daily pivots from the 14 Jul session and re-propagate to §11 narrative, §15, §16 and both cards. |
| 1.3 Audience & tone | Byline "Senior US Equity Strategist · Trading & risk review". Register is institutional throughout — no retail framing, no promotional language, no "you should" constructions. §18 is a structured analyst judgement table with confidence and three reasons. | Header; §12; §18 | 5 | None. |
| 2.1 Sections present & ordered | All of §1–§21 present in order; §13 correctly split into §13a per-article table, §13b aggregate with a numeric tilt, §13c previous-period calendar, §13d upcoming calendar; §21 split a/b/c/d with the §21d limitations boilerplate present. One structural hole: **§21b "Trade 3C — Momentum-Breakout (TRANSITION)" is a bare heading with no body at all** — no fields, no SUPPRESSED row, no suppression reason. §20 states the suppression, the card block does not. | Headings at lines 8–665; §21b line 636 heading followed directly by the §21c heading | 4 | Replace the empty Trade 3C heading with an explicit SUPPRESSED row carrying the reason ("no confirmed close beyond the 25-day boundary by ≥0.25×ATR"). |
| 2.2 Scorecard as a table | §6 is a table but is **missing the Source A and Source B columns and the separate Final column** required by the schema — it carries Date/O/H/L/C/RSI2/Trend/Validation only. The immediately preceding report (14 Jul) does carry a "Source A / B" column, so this is a regression, not a house style. §11 daily table runs R5→S5 (five tiers per side, ordering correct) but the weekly/monthly table stops at R2/S2 — **R3 and S3 are missing on both**. | §6 header row; `reports/md/SP500_Report_14Jul2026.md` §6 for the compliant column set; §11 weekly/monthly table | 2 | Restore Source A / Source B / Final columns in §6. Extend the weekly and monthly pivot tables to R3→P→S3. |
| 2.3 Method steps visible | §4 observations → §5 classification and consensus build is explicit and readable (normalisation to cash points, tolerance stated, exclusion of derived H/L from the consensus number). §8 is genuinely candle-by-candle across all five sessions and closes with a named sequence assessment. §9 states overlap ratio, directional persistence, VOLator slope and the dual-gate resolution. §7 carries five chart placeholders with captions (pandoc dropped the images — accepted as evidence per brief). Not shown: the arithmetic behind the §13b tilt and the §21a score, both of which are asserted rather than derived. | §4–§9; §7 captions; §13b; §21a | 4 | Show the tilt and direction-score arithmetic inline (weight × signal per row) so both reproduce. |
| 3.1 Quantitative claims sourced | §1 numbers all trace to §4/§6/§9. §14's CPI figures are attributable and correct. But **§12 carries no source attribution on any of its figures**: Goldman EPS $20.98 vs ~$14.48 expected, NVDA +4%, SK hynix +12.8%, IBM ~−25%, "first monthly decline since 2020" all appear as bare assertions with no §4/§13a pointer and no named publisher. §14 repeats them the same way. | §12 four paragraphs; §14 | 2 | Attach a §13a row reference or a named dated source to every figure in §12 and §14, or remove the figure. |
| 3.2 Citations exist & contain data | Three sources spot-checked for internal consistency. (a) **S&P Dow Jones, 14 Jul close 7,543.59** — used identically in §1, §3, §4, §6 (7,543.6), §11 narrative and the §21b entry; consistent. (b) **Bloomberg, 14 Jul, "+0.4% on day"** — normalised to ≈7,543.6; against the report's own 13 Jul close of 7,515.34 that is +0.376%, i.e. +0.4% to one decimal, and §13c repeats "+0.4%"; consistent. (c) **Investing.com derived O/H/L 7,547.64 / 7,579.93 / 7,508.16** — matches the §6 10 Jul row and matches the same three numbers in the 14 Jul report; consistent, but §4 date-labels the row "06–10 Jul" (a week) while the values are one session. No source is impossible or self-contradictory, so **no fabrication override**. One real contradiction: §5 and §19 both assert corroboration "inside the ±0.10-point equity tolerance", while §4 and §20 record the 13 Jul pair at 7,515.34 vs 7,515.47, Δ≈0.13 — outside the tolerance the report claims to have met. | §4 rows 1/3/6; §5; §19; §20 "delta ≈0.13 (close, at tolerance edge)" | 3 | Re-date the §4 Investing.com row to "10 Jul". Reword §5/§19 so the 13 Jul pair is described as outside ±0.10 and adopted on the official value, matching §20. |
| 3.3 Calculations transparent | **RSI2 does not reproduce.** Helper recomputation from the report's own §6 closes returns 100.0 / 34.6 / 32.0 for 10, 13 and 14 Jul against the printed 87.2 / 33.8 / **58.0**. The 14 Jul cell is wrong by 26.0 points and the 10 Jul cell by 12.8; on the slice's own closes the column should read 0.00 / 71.41 / 100.00 / 35.93 / 33.49 against the printed 30.0 / 78.0 / 87.2 / 33.8 / 58.0. The 14 Jul report prints 0.0 / 74.2 / 100.0 for the same three closes, confirming the 15 Jul column is the outlier. Per brief §4 this is a Category 3 failure, not a note. **ATR(14) is never stated numerically** anywhere in the report; it is only implied — 78.5 from the §21b "3×ATR cap at 7,779.1 (+236 points)" and ≈70 from the §21c 1R bands, two different values. **Weekly and monthly pivot sets are internally inconsistent**: floor pivots require R2−P = P−S2 = H−L, but weekly gives 136.5 vs 101.3 (R2 overstated by 35.2) and monthly gives 453.6 vs 320.6 (R2 overstated by 133.0). Direction-score contributions in §20 sum to +0.43 against the stated +0.42. The §13b tilt of +0.20 does not reproduce from the stated media 0.5 / trade 0.7 weights, which give +0.147. What does work: the daily pivot ladder R5→S5 reproduces exactly from the report's own 13 Jul H/L/C (P 7,528.1, R1 7,553.2, S1 7,490.2, R2 7,591.1, S2 7,465.1, R3 7,616.2, S3 7,427.2), the Trend labels follow the stated rule given the printed RSI2, and KER(13, EMA-3) is stated. | §6 RSI2 column; helper output; §11 weekly/monthly tables; §20 method and contribution lines; §13b; §21b TP3 line | 1 | Recompute the whole §6 RSI2 column and re-propagate to §8 and the §21a short-term input. State ATR(14) as a number in §9 and use one value in both §21b and §21c. Recompute weekly and monthly R2 as P+(H−L). Reconcile the contribution sum to the printed score. Show the tilt arithmetic. |
| 3.4 Numbers reconcile | Good: the D-1 close is 7,543.59/7,543.6 identically in §1, §3, §4, §6 and the §21b entry; the §11 pivot values are quoted unchanged on both cards; §6 RSI2 matches the §8 narrative sequence (30→87→34→58). Failures: **§21b TP3 is 7,779.1 but the extracted card record `cards/baseline/by_date/2026-07-15.json` holds tp3 = 7,724.0** (= entry + 3R), a 55.1-point mismatch between the report and its own card record. ATR is inconsistent between the card (≈78.5) and the backtest (≈70). §1 says the 25-day range position is "≈85th percentile", §9 says "86th percentile". §8 attributes the 7,481 support level to the "08 Jul low", but §6 puts the 08 Jul low at 7,421.8 — 7,481.7 is the **09 Jul** low. §21a assigns short-term technical a +0.25 contribution on a 0.25 weight, i.e. a maximal +1.0 bullish signal, while §8's own judgement label is "Indecision". | §21b TP3 row vs baseline JSON; §21c note; §1 vs §9; §8 sequence assessment vs §6; §21a vs §20 | 2 | Align TP3 between the card and the card record. Use one ATR. Fix the 85/86 percentile and the 08/09 Jul low attribution. Re-derive the short-term signal so it is consistent with the §8 label. |
| 4.1 Pillars conclude | §8 ends "Judgement label: Indecision". §9 ends "Bias: Neutral with an upward lean" plus a preferred trade protocol. §10 ends "Aggregate cross-asset read: MIXED-to-CONFIRM". §12 tags each driver price-supportive / price-negative and cyclical. §14 is the weak one — it closes on a watch item and never states a direction label. The strategy pillar concludes badly: Trade 3C reaches no conclusion at all (empty heading). | §8 line 191; §9 line 200; §10 line 240; §12; §14 close; §21b Trade 3C | 3 | Add an explicit direction label to the end of §14. Give Trade 3C a stated SUPPRESSED conclusion. |
| 4.2 Peer/cross-asset interpreted | §10 is a mechanism table, not a correlation list — softer dollar → easier financial conditions and multinational earnings translation; easing implied vol → receding hedge demand; DAX as shared global risk beta with an explicit "no independent signal" verdict. That is the right shape. The evidence under it is unreliable: §9 states VIX "eased from the Monday spike (17.2 → ~16.4)" when the slice has 13 Jul 17.65 → 14 Jul 17.37, and §13c states "VIX +14%" on 13 Jul when the slice move is 16.66 → 17.65 = +5.9%. USDX at "~100.7–100.9" does check out (slice 14 Jul 100.905). | §10 table; §9 VOLator paragraph; §13c; VIX and USDX slices | 3 | Correct the VIX levels to 17.65 → 17.37 and the 13 Jul VIX change to ≈+5.9%; the "compressing volatility" claim needs restating against those numbers. |
| 4.3 Synthesis reconciles tensions | Genuine strengths: §9 names the KER-vs-VOLator disagreement and resolves it explicitly through the dual-gate to TRANSITION; §21a raises a conflict flag that the LONG score is more constructive than the §17 forecast and retains both unchanged; §15 is a balanced two-column risk table; §16 gives base case plus invalidation both ways. Against that, the card layer is incoherent. **Trade 2 is a BUY STOP at 7,530.6, which is *below* the D-1 close of 7,543.6** — a stop-entry below market is not a valid stop order and violates the static rule that a STOP level sits on the correct side of the D-1 close. Its stated confirmation trigger is "a daily close above range high 7,580", which sits **above TP1 (7,553.2) and TP2 (7,572.2)**, so the trade cannot be entered on its own trigger without both targets already being passed. And §19 states that *every* pivot tier carries the indicative flag, which under the M5 TRANSITION rule requires Trade 2 to be **suppressed** — it is published instead. The §8 "Indecision" vs §21a maximal-bullish short-term input is never reconciled. | §9 Kaufman paragraph; §21a conflict flag; §21b Trade 2 entry/TP/caveat rows; §19 consequence paragraph | 2 | Re-derive Trade 2 to satisfy the side and confirmation rules, or suppress it explicitly under the all-tiers-indicative rule. Reconcile the §8 label with the §21a short-term input. |
| 4.4 Calibrated language | §17 is exactly one sentence. Confidence is stated as Medium in §3 and again in §18. No hedge stacking — §16 commits to a base case with a named invalidation level in both directions rather than covering every outcome. §21a states a numeric conviction rather than a vague lean. | §17; §3 confidence column; §18 confidence row; §16 | 5 | None. |
| 5.1 Data dated; staleness flagged | Every §6 row, §4 row and §13a article carries a date. Single-source-indicative O/H/L is marked at the cell level with an asterisk, explained in the §6 footnote, and restated per-instrument in §19. That is above-average disclosure. Two defects: the ±0.10 tolerance claim in §5/§19 conflicts with the Δ0.13 recorded in §20 for the 13 Jul pair, and §2 books the as-of as 15 July rather than the D-1 NY close. | §6 asterisks and footnote; §19 "Corroboration status per instrument"; §5 vs §20 | 4 | Reconcile the tolerance statement; restate the as-of convention. |
| 5.2 Assumptions up front | §19 is thorough on the single-source dependency and explicitly traces its propagation into §11 and then into §21. §20 logs sources attempted and refused (Stooq robots-blocked, Yahoo paywalled, Barchart/TradingView not reached), the validation method, the weights basis and the lenient-corroboration standing instruction. Card caveats carry the indicative flag. Gap: the anchor override is noted in §2 and §20, but the Trade 1 card does not caveat that its "≈7,543.6" entry is the D-1 close standing in as a proxy for the unobserved 07:00 UK open. | §19; §20; §21b Trade 1 caveats row; §2 as-of row | 4 | Add the proxy-open caveat to the Trade 1 card itself. |
| 5.3 Red flags surfaced | §12 flags the Hormuz oil channel as the main downside and the IBM warning as a demand-softness signal; §15 carries three downside risks including the PPI/Warsh event risk; the Trade 1 caveat explicitly carries the §13d collision ("holding period collides with 15 Jul PPI + Warsh testimony"). Gap: Trade 2 has a holding period over the same two events and its caveat carries only the indicative-pivot flag, not the event collision. | §12; §15; §21b Trade 1 caveats; §21b Trade 2 caveats | 4 | Carry the §13d PPI/Warsh collision into the Trade 2 caveat as well. |
| 5.4 Restrictions honoured | **BREACHED, on two counts.** (i) Prompt-internal machinery is exposed in the report body: §20 line 542 opens "**M5 trace:** regime_label = TRANSITION …" — a literal module code — and continues "DEFAULTS (0.25/0.20/0.10/0.15/0.15/0.15) — **v2.1 baseline, within the 20-session lock**"; §9 cites "(Transitional regime, **§Step-4 matrix**)"; §2 uses the internal terms "(execution block)" and "(regime block)"; the header carries "(forward-test)". (ii) §4 and §19 both declare the Investing.com derived CFD series excluded from corroborated close and pivot inputs, yet §19 concedes it was "the only accessible full-OHLC feed" and it therefore supplies the **entire §6 O/H/L column**, which via §11 supplies the pivot inputs that set Trade 2's entry, stop and all three targets and Trade 1's stop anchor (13 Jul low 7,503). The indicative flag is applied honestly, but the restriction as written — no retail CFD quotes in the OHLC basis — is not honoured in substance. No positive finding of a synthesised price presented as sourced, though the 13 Jul open printed as 7,566.0, exactly equal to that session's high and 15.2 points off the slice open of 7,550.8, has the shape of a filled-in field. Instrument common names are used correctly throughout; ES futures are not used at all. | §20 line 542 and 539; §9 line 217; §2 lines 50–51; header line 6; §4 footnote vs §19; §11 source-status note; §6 13 Jul row | 1 | Strip every module code, version tag, step reference and internal block name from the report body. Either source the OHLC basis outside the CFD series or state plainly that the restriction was relaxed and why. Re-derive the 13 Jul open. |

---

## 2. Category roll-up

| Category | Level | Multiplier | Points | Justification |
|---|---|---|---|---|
| C1 Prompt adherence (max 20) | 2 | 0.40 | 8.00 | Rows 1.1–1.3 = 3, 2, 5 → mean 3.33 → level 3. The §5.4 restriction breach forces C1 down one level under framework §6, giving level 2. Variables are largely right (asset, counters and order, anchor, units) but the as-of convention is wrong and §11 works off a stale D-2 prior period. |
| C2 Structure (max 20) | 3 | 0.65 | 13.00 | Rows 2.1–2.3 = 4, 2, 4 → mean 3.33 → level 3. Full §1–§21 skeleton in the right order with all §13 and §21 sub-blocks, but §6 is missing its Source A/B/Final columns, the weekly and monthly pivot tables stop at R2/S2, and the Trade 3C card is an empty heading. |
| C3 Accuracy & evidence (max 25) | 2 | 0.40 | 10.00 | Rows 3.1–3.4 = 2, 3, 1, 2 → mean 2.00 → level 2. Driven by 3.3: the §6 RSI2 column does not reproduce from the report's own closes (14 Jul 58.0 vs 32.0; 10 Jul 87.2 vs 100.0), ATR(14) is never stated and is implied at two different values, and the weekly and monthly pivot sets fail their own R2−P = P−S2 identity. Three cited sources check out internally, so no fabrication override applies. |
| C4 Reasoning & judgment (max 20) | 3 | 0.65 | 13.00 | Rows 4.1–4.4 = 3, 3, 2, 5 → mean 3.25 → level 3. The analytical narrative is good — real mechanisms in §10, an explicit dual-gate resolution in §9, an honest conflict flag in §21a, a one-sentence §17. The card layer drags it down: Trade 2's buy stop sits below the D-1 close, its confirmation trigger sits above two of its own targets, and it should have been suppressed under the all-tiers-indicative rule. |
| C5 Currency, restrictions & transparency (max 15) | 3 | 0.65 | 9.75 | Rows 5.1–5.4 = 4, 4, 4, 1 → mean 3.25 → level 3. Dating and assumption disclosure are genuinely strong (§19/§20 are the best part of the report), but 5.4 fails hard: module codes and internal step/version references are exposed in §20, §9 and §2, and the CFD series that §4/§19 exclude is in fact the sole basis for the §6 O/H/L column and the §11 pivots that price both cards. |
| **Total** | — | — | **53.75 → 54** | Σ(multiplier × max) = 8.00 + 13.00 + 10.00 + 13.00 + 9.75 = 53.75, rounded to 54. |

---

## 3. Total, band, override check

- **Raw total: 53.75 → 54 / 100.**
- **Band: Low (40–59).**
- **Override applied: `restriction_breach`.**
  - Trigger: row 5.4. `M5 trace:` (§20), `v2.1 baseline, within the 20-session lock` (§20), `§Step-4 matrix` (§9), `(execution block)` / `(regime block)` (§2) and `(forward-test)` (header) are module codes and prompt-internal references appearing verbatim in the delivered report, which the instance restrictions forbid. Compounded by the CFD-derived series supplying the whole §6 O/H/L column and, through §11, the pivot inputs for both trade cards, contrary to the exclusion stated in §4 and §19.
  - Effects per framework §6: total capped at Moderate (≤ 74) and C1 dropped at least one level. C1 was dropped from level 3 to level 2 (−7.00 points at the 20-point maximum). The 74 cap does **not** bind — the post-drop total of 54 already sits below it.
- **Fabrication override: not applied.** Three cited sources were spot-checked (S&P Dow Jones 14 Jul close 7,543.59; Bloomberg "+0.4% on day"; Investing.com derived 7,547.64 / 7,579.93 / 7,508.16). Each is named, dated, and quotes a figure used consistently elsewhere in the report; the Bloomberg percentage reconciles to the report's own 13 Jul close, and the Investing.com triplet reproduces exactly in the §6 10 Jul row and in the preceding 14 Jul report. No source is self-contradictory or impossible. C3 therefore stands at its checklist level of 2, not 0.
- **As-of session check: PASSED.** The report's D-1 is genuinely 2026-07-14, not an earlier session — §6 carries a full 14 Jul row, §1/§3/§4 quote the 14 Jul close, and that close (7,543.59) sits 2.81 points from the slice's 14 Jul cash close of 7,546.40, inside the ≤3-point close tolerance. The one stale element is §11, which reaches back to 13 Jul for its daily pivot inputs; that is scored under rows 1.2 and 3.3 rather than as a wholesale wrong-session finding.

---

## 4. Card Integrity

Linter rows copied verbatim from `qa/regen_20260906_qa1/lint_static/2026-07-15.csv`:

| card_id | report_date | strategy | flags | dud |
|---|---|---|---|---|
| 2026-07-15_Trade_1 | 2026-07-15 | Trade 1 - Daily Directional | CLEAN | False |
| 2026-07-15_Trade_2 | 2026-07-15 | Trade 2 - Pivot (TRANSITION breakout side) | CLEAN | False |
| 2026-07-15_Trade_3C | 2026-07-15 | Trade 3C - Momentum-Breakout | SUPPRESSED | False |

Per-card integrity, 100 − 40·(#DUD) − 10·(#WARN), floored at 0:

| card_id | #DUD | #WARN | Integrity |
|---|---|---|---|
| 2026-07-15_Trade_1 | 0 | 0 | 100 |
| 2026-07-15_Trade_2 | 0 | 0 | 100 |
| 2026-07-15_Trade_3C | — | — | suppressed — excluded from the mean |

**Report Card Integrity = 100.0** (mean over the two non-suppressed cards). Totals across the file: 3 card rows, 0 DUD_* flags, 0 WARN_* flags.

### M5 construction assessment (feeds row 4.x, not the integrity number)

**Trade 1 — Daily Directional (LONG).** Largely compliant. Direction score +0.42 clears the 0.25 conviction threshold, so publishing rather than suppressing is correct. Three equal units are specified; TP1 = entry + 1R (7,603.8) and TP2 = entry + 2R (7,664.0) are exact; the Unit 3 break-even move to entry + 0.2R = 7,555.6 is correct; the runner is a session-close time-stop or 3×ATR cap, as the rule requires. The stop derivation reproduces: the tighter of the 5-day swing low (7,421.8) and the nearest S/R (13 Jul low 7,503) is 7,503, less a 0.25×ATR buffer of 19.6, giving 7,483.4 and R = 60.2. R is inside the 3.5×ATR cap and inside the 0.3–3.0×ATR14 band (22.7 to 227.3 on the slice ATR14 of 75.77), TP1 is well inside 2.5×ATR14 of entry, the anchor is explicit, thesis invalidation (daily close below 7,490) is separate from the stop and sits above it, confluences are listed, and the indicative flag is propagated. R = 60.2 < 1×ATR, so no wide-stop flag is due. Defects: the stop anchor 7,503 is a CFD-derived indicative low (slice cash low 7,507.0); ATR(14) is never stated, only implied at 78.5; TP3 disagrees with the card record (7,779.1 vs 7,724.0); the "TP1 near daily R2 (7,591) region" confluence is 12.7 points loose; and the entry does not caveat that 7,543.6 is a D-1-close proxy for the 07:00 UK open.

**Trade 2 — Pivot (TRANSITION, breakout side).** Three rule breaches. (1) It should not exist: §19 states every pivot tier carries the single-source-indicative flag, and the M5 TRANSITION rule suppresses Trade 2 when every pivot tier is single-source-indicative. (2) The entry is a BUY STOP at 7,530.6, 13.0 points **below** the D-1 close of 7,543.6 — a stop-entry must sit above the reference price on a long, and this violates the static rule that a LIMIT/STOP level sits on the correct side of the D-1 close. (3) The entry formula used, P + 0.10×(R1−P), and the stop formula, P − 0.8×(P−S1), are the **TREND** construction, not a breakout construction; the arithmetic is internally correct (7,528.1 + 2.51 = 7,530.6; 7,528.1 − 30.32 = 7,497.8; R = 32.8) but the wrong rule was applied to a TRANSITION regime. Compounding these: the stated confirmation ("daily close above range high 7,580") sits above TP1 7,553.2 and TP2 7,572.2, so the trade cannot trigger without both targets already exceeded; there is no three-unit tranche block and no break-even rule on the card (the card record supplies BE_0.2R_ON_TP2 at 7,537.16, which the report never states); no confluences row; and the caveat omits the §13d PPI/Warsh collision that Trade 1 does carry. R = 32.8 does clear the 0.3×ATR14 floor of 22.7.

**Trade 3C — Momentum-Breakout (TRANSITION).** Present as a heading only, with no body. The M5 rule requires a suppression to appear as an explicit SUPPRESSED row, not as an omission; §20 records the reason ("no confirmed break above 7,580") but §21b does not. The underlying suppression judgement is defensible — 3C requires a confirmed close beyond the 25-day boundary by ≥ 0.25×ATR, and on the slice the 25-day high is 7,583.40 against a D-1 close of 7,546.40 — but it must be stated on the card.

---

## 5. Data reconciliation log

Slice values are cash-session (16:30–23:00 broker) unless marked full-day. Tolerances per brief §4: |Δ| ≤ 3 pts on a close, ≤ 8 pts on an open/high/low.

### §6 OHLC, all five rows

| Section | Field | Report value | Slice value | Delta | Verdict |
|---|---|---|---|---|---|
| §6 | 08 Jul Open | 7,476.5 | 7,459.6 | +16.9 | **DISCREPANCY** (>8) |
| §6 | 08 Jul High | 7,488.5 | 7,488.1 | +0.4 | OK |
| §6 | 08 Jul Low | 7,421.8 | 7,421.1 | +0.7 | OK |
| §6 | 08 Jul Close | 7,482.7 | 7,478.6 | +4.1 | **DISCREPANCY** (>3) |
| §6 | 09 Jul Open | 7,491.6 | 7,498.8 | −7.2 | OK (near limit) |
| §6 | 09 Jul High | 7,546.9 | 7,547.4 | −0.5 | OK |
| §6 | 09 Jul Low | 7,481.7 | 7,482.3 | −0.6 | OK |
| §6 | 09 Jul Close | 7,543.6 | 7,542.8 | +0.8 | OK |
| §6 | 10 Jul Open | 7,547.6 | 7,544.7 | +2.9 | OK |
| §6 | 10 Jul High | 7,579.9 | 7,579.5 | +0.4 | OK (matches full-day high 7,579.9 exactly) |
| §6 | 10 Jul Low | 7,508.2 | 7,505.6 | +2.6 | OK |
| §6 | 10 Jul Close | 7,575.4 | 7,574.2 | +1.2 | OK |
| §6 | 13 Jul Open | 7,566.0 | 7,550.8 | +15.2 | **DISCREPANCY** (>8; printed equal to that session's own high) |
| §6 | 13 Jul High | 7,566.0 | 7,565.8 | +0.2 | OK |
| §6 | 13 Jul Low | 7,503.0 | 7,507.0 | −4.0 | OK |
| §6 | 13 Jul Close | 7,515.3 | 7,518.2 | −2.9 | OK (at limit) |
| §6 | 14 Jul Open | 7,536.7 | 7,535.7 | +1.0 | OK |
| §6 | 14 Jul High | 7,557.4 | 7,559.7 | −2.3 | OK |
| §6 | 14 Jul Low | 7,513.2 | 7,512.9 | +0.3 | OK |
| §6 | 14 Jul Close | 7,543.6 | 7,546.4 | −2.8 | OK (at limit) |

### §6 RSI2 column

| Section | Field | Report value | Slice / recomputed | Delta | Verdict |
|---|---|---|---|---|---|
| §6 | 08 Jul RSI2 | 30.0 | 0.00 (slice closes); 14 Jul report prints 0.0 for the same close | +30.0 | **FAIL** |
| §6 | 09 Jul RSI2 | 78.0 | 71.41 (slice closes); 14 Jul report prints 74.2 | +6.6 | **FAIL** |
| §6 | 10 Jul RSI2 | 87.2 | 100.00 (slice); **100.0 recomputed from the report's own closes** | −12.8 | **FAIL** — two consecutive gains give zero mean loss, so RSI2 must be 100 |
| §6 | 13 Jul RSI2 | 33.8 | 35.93 (slice); 34.6 from the report's own closes | −0.8 vs own | OK |
| §6 | 14 Jul RSI2 | 58.0 | 33.49 (slice); **32.0 recomputed from the report's own closes** | +26.0 vs own | **FAIL** — also flips the Trend label: at RSI2 32.0 with Close 7,543.6 > Open 7,536.7 the rule gives Neutral, not the printed Bullish |

### §11 pivots

| Section | Field | Report value | Slice / derived value | Delta | Verdict |
|---|---|---|---|---|---|
| §11 | Daily pivot source session | 13 Jul (D-2) | 14 Jul (D-1) required | one session stale | **FAIL** |
| §11 | Daily P (from report's own 13 Jul H/L/C) | 7,528.1 | 7,528.1 recomputed from 7,566.0 / 7,503.0 / 7,515.3 | 0.0 | OK — reproduces exactly |
| §11 | Daily R1 / S1 / R2 / S2 / R3 / S3 | 7,553.2 / 7,490.2 / 7,591.1 / 7,465.1 / 7,616.2 / 7,427.2 | identical on recomputation from the report's own H/L/C | 0.0 | OK — all reproduce; R4/R5/S4/S5 also reproduce as ±(H−L) extensions |
| §11 | Daily P (correct D-1 basis) | 7,528.1 | 7,539.67 (helper, 14 Jul cash) | −11.6 | **FAIL** — wrong prior period |
| §11 | Daily R1 / S1 (correct D-1 basis) | 7,553.2 / 7,490.2 | 7,566.43 / 7,519.63 | −13.2 / −29.4 | **FAIL** |
| §11 | Weekly P (W/E 10 Jul) | 7,544.7 | 7,524.93 (helper, 06–10 Jul cash) | +19.8 | **FAIL** |
| §11 | Weekly R1 / S1 | 7,610.7 / 7,509.4 | 7,628.77 / 7,470.37 | −18.1 / +39.0 | **FAIL** |
| §11 | Weekly R2 internal identity | 7,681.2 | P + (H−L) = 7,646.0, since P − S2 = 101.3 | +35.2 | **FAIL** — R2−P (136.5) ≠ P−S2 (101.3) |
| §11 | Monthly R2 internal identity | 7,898.5 | P + (H−L) = 7,765.5, since P − S2 = 320.6 | +133.0 | **FAIL** — R2−P (453.6) ≠ P−S2 (320.6) |

### Cross-section and cross-asset

| Section | Field | Report value | Slice / derived value | Delta | Verdict |
|---|---|---|---|---|---|
| §1 / §3 / §4 / §6 / §21b | D-1 close | 7,543.59 (7,543.6) | 7,546.40 | −2.81 | OK — identical across all five sections |
| §21b | 5-day swing low | 7,421.8 | 7,421.10 | +0.7 | OK |
| §8 / §11 | 5-day swing high | 7,579.9 | 7,579.50 | +0.4 | OK |
| §9 / §21b / §21c | ATR(14) | not stated; implied 78.5 (3×ATR cap 7,779.1 = +236) and ≈70 (§21c 1R bands) | 75.77 cash / 83.42 full-day | two implied values, 8.5 apart | **FAIL** — value never stated and not internally single-valued |
| §9 | VIX 13 Jul → 14 Jul | 17.2 → ~16.4 | 17.65 → 17.37 | −0.45 / −0.97 | **FAIL** |
| §13c | VIX change 13 Jul | +14% | +5.9% (16.66 → 17.65) | −8.1 pp | **FAIL** |
| §13c | Index change 13 Jul | −0.8% | −0.74% slice; −0.79% on the report's own closes | ≤0.06 pp | OK |
| §14 | USDX level | ~100.7–100.9 | 100.905 (14 Jul close) | within band | OK |
| §1 / §12 / §13c | June CPI y/y | 3.5% vs 3.8% consensus | 3.5 actual vs 3.8 consensus (news slice, 14 Jul 15:30) | 0.0 | OK |
| §14 | June core CPI y/y | 2.6% | 2.6 actual (news slice) | 0.0 | OK |
| §1 vs §9 | 25-day range position | ≈85th (§1) / 86th (§9) | 88.6th on slice 25-day range 7,260.00–7,583.40 | internal 1 pp; 2.6–3.6 pp vs slice | Minor — internal inconsistency |
| §21b vs card record | Trade 1 TP3 | 7,779.1 (3×ATR cap) | 7,724.0 in `cards/baseline/by_date/2026-07-15.json` | −55.1 | **FAIL** — report and card record disagree |
| §21a vs §20 | Direction score | +0.42 | contributions sum to +0.43 (0.25 + 0.10 − 0.05 + 0.05 + 0.03 + 0.05) | +0.01 | **FAIL** (minor) |
| §13b | Sentiment tilt | +0.20 "source-class weighted" | +0.147 from the stated media 0.5 / trade 0.7 weights | −0.053 | **FAIL** — stated derivation does not reproduce |
| §8 vs §6 | "7,481 … (08 Jul low)" | 7,481 attributed to 08 Jul | §6 08 Jul low is 7,421.8; 7,481.7 is the 09 Jul low | mislabelled session | **FAIL** (minor) |
| §5 / §19 vs §4 / §20 | 13 Jul corroboration delta | "inside the ±0.10-point equity tolerance" | 7,515.34 vs 7,515.47 = 0.13, recorded in §20 | +0.03 over tolerance | **FAIL** — self-contradictory claim |
| §21c vs §21d | Mean mark-to-market R | +0.12 | (0.09 + 0.74 + 0.39 − 0.72 + 0.10) / 5 = +0.12 | 0.00 | OK |
| Cross-report | 08–10 Jul O/H/L/C | identical to `reports/md/SP500_Report_14Jul2026.md` §6 | same three sessions, same values | 0.00 | OK — the 08 Jul open and close deltas above are a persistent source-basis issue, not a fresh invention |
| Cross-report | 08 / 09 / 10 Jul RSI2 | 30.0 / 78.0 / 87.2 | 0.0 / 74.2 / 100.0 in the 14 Jul report for the same closes | +30.0 / +3.8 / −12.8 | **FAIL** — the 15 Jul column is the outlier against both the slice and the preceding report |
