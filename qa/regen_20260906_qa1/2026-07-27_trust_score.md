# Trust Score — 2026-07-27 — SP500_Report_27Jul2026.md

Run: regen_20260906_qa1 · Asset US500 · D = 2026-07-27 · D-1 slice = 2026-07-26 (Sunday; last completed session Fri 24 Jul 2026).
Basis for Category 3: `data/slices/US500/US500_upto_2026-07-26.csv` via `engine/qa_slice_stats.py`, cash session 16:30–23:00 broker.
Tolerance (brief §4): |Δ| ≤ 3 pts on a close, ≤ 8 pts on an open/high/low.

## 1. Section 7 checklist

| Item | Reviewer notes | Evidence observed | Score 0–5 | Action required |
|---|---|---|---|---|
| 1.1 Variables respected | Asset is the S&P 500 cash index (^GSPC), not ES futures; counters USDX · VIX · DAX 40 with USDX first; as-of NY close of D-1 correctly resolved to Fri 24 Jul (D-1 is a Sunday) with tz America/New_York; lookback 5 sessions (20–24 Jul); index points / USD; 6 distinct named sources in §4. Daily-open anchor is stated as 07:00 UK, but the trailing clause "overridden for the 27 Jul 2026 run per instruction" names no replacement anchor and neither trade card carries an anchor line. Tick size 0.01 never stated (implied by 2-dp quoting). | §2 attribute table; header line; §4 (7 rows / 6 sources); §10; §21b | 4 | State the anchor once, unambiguously (07:00 UK = 09:00 broker) and repeat it on every card; delete or complete the "overridden" clause. |
| 1.2 Coverage & currency consistent | All §2/§6/§13a/§13c dates are D-1 or earlier and §13d is forward-looking as designed; no currency or unit drift. But the weekly pivot block is built on 13–17 Jul, which is two weeks back for a 27 Jul report — the prior completed week is 20–24 Jul — and it is not flagged as stale; the monthly block is labelled "prior month June" but back-solves to H 7,581.51 / L 7,294.19, i.e. the 25-session envelope, not June (slice June cash H 7,624.60 / L 7,243.10). | §11 weekly and monthly tables; §11 position narrative | 2 | Rebuild weekly pivots from 20–24 Jul and monthly pivots from June's actual H/L/C; re-derive every downstream level quoted in §11/§13d/§15/§16/§17. |
| 1.3 Audience & tone | Senior US Equity Strategist register held throughout; §18 is a strategist judgement with confidence split by horizon; closing line scopes the report to trading and risk review (forward-test); no retail tone, no advice framing. | §1, §18, closing italic line | 5 | None. |
| 2.1 Sections present & ordered | §1–§21 all present in the prescribed order, including §13a per-article table, §13b aggregate with a numeric tilt, §13c previous-period and §13d upcoming calendars, and §21a–§21d with the limitations boilerplate. §17 is a single sentence. | Headings throughout | 5 | None. |
| 2.2 Scorecard as a table | §6 is a table but carries only Date/O/H/L/C/RSI2/Trend/Validation Outcome — the Source A, Source B and Final columns are missing; source attribution is demoted to a footnote ("S&P DJI × FRED", "CNBC × AP"). The 24 Jul report in `reports/md/` does carry a "Sources A / B" column, so the omission is a regression. §11 daily table runs R5→S5 (contains R3→P→S3 in order, plus the R1.5/S1.5 tiers the cards need); weekly and monthly tables are R3→P→S3 as required. | §6 table and footnote; §11 three tables; `reports/md/SP500_Report_24Jul2026.md` §6 | 3 | Restore Source A / Source B / Final as columns of §6. |
| 2.3 Method steps visible | §4 observations → §5 classification and consensus build → §6 validated table is a clean chain; §8 is candle-by-candle with an explicit sequence assessment; §9 states persistence, overlap, VOLator slope and the KER dual-gate that resolves the label; §7 carries five captioned chart placeholders (images dropped by pandoc — accepted as evidence, noted here). Weakness: VOLator scaling and KER parameters are never defined and ATR(14) is never given a number, so three of the stated methods cannot be re-walked. | §4–§9; §7 captions | 4 | Print ATR(14), the KER period (13, EMA 3) and the VOLator scaling basis as numbers in §9. |
| 3.1 Quantitative claims sourced | The headline close is sourced and dual-attributed. But a long list of load-bearing numbers carries no source and no pointer to §4/§6/§13: ">78%" September hike odds, "18-month-high" Treasury yields, "~31%" oil premium with Brent >$95 / WTI ~$87, "~88%" early-reporter beat rate, "blended growth near 30%", DAX 25,099 / +1.36%, VIX 18.58, KER −0.385, VOLator slope +0.21. §14 cross-references §10, but §10 itself cites nothing. | §1, §9, §10, §12, §14 | 2 | Add a source or an in-report pointer to every number in §1/§10/§12/§14, or drop the claim. |
| 3.2 Citations exist & contain data | Three spot-checks: (a) CNBC 23 Jul, "worst one-day declines since June 23" — the −1.21% reproduces from the report's own closes (7,408.30/7,498.96) and matches the slice (−1.24%); (b) Trading Economics 24 Jul, ">33% chance of a rate hike" — used identically in §1, §12, §13d, and its §4 price row (7,412 rounded) agrees with 7,411.98; (c) Investing.com 24 Jul day range 7,396.53 / 7,460.98 — reconciles to the slice (7,395.6 / 7,460.2) within 1 pt. No fabricated source: every checked figure is externally corroborated by the slice. Two documentation faults remain: §20 records Investing.com as "fetched; table stale to 14 Jul" while §4 uses it as the Core source for the 24 Jul range, and §6's footnote credits "CNBC × Associated Press" for the 20–23 Jul closes although AP appears in no §4 row. | §4, §13a, §6 footnote, §20 | 3 | Reconcile the §20 staleness note with the §4 Investing.com row (name the page fetched); add the AP row to §4 or drop it from the §6 footnote. |
| 3.3 Calculations transparent | RSI2 does not reproduce from the report's own closes under the specified formula (RS = mean gain / mean loss over 2 periods): 22 Jul stated 65.4 vs 86.6, 23 Jul stated 14.2 vs 0.0 (both prior changes negative), 24 Jul stated 19.3 vs 3.9. It does not match the slice-close series either (86.97 / 0.00 / 6.33). Per brief §4 this is a Category 3 failure, not a note. Daily pivots do reproduce exactly from the report's own 24 Jul H/L/C and satisfy R2−P = P−S2 = 64.45. §21a Σ signal×weight traces exactly to −0.198 ≈ −0.20 on the default 0.25/0.20/0.10/0.15/0.15/0.15 weights. Against that: the §13b tilt of −0.30 does not reproduce from its own stated weights (institutional 1.0 / trade press 0.7 / media 0.5 over the six §13a rows gives −2.0/3.9 = −0.513); ATR(14) is never stated (the 3C levels imply 66.04 vs slice 71.21); KER is quoted without its period. Trend labels do survive: they are unchanged under the corrected RSI2 values. | §6 and helper output; §11; §13b; §20 trace; §21a | 1 | Recompute the RSI2 column and the §13b tilt from the stated formulas; publish ATR(14) and the KER parameters. |
| 3.4 Numbers reconcile | 7,411.98 is identical in §1, §3, §4, §6, §11 and §18; Trade 2 quotes the §11 daily pivots to the cent; RSI2 is consistent across §6/§8/§1/§15 (consistently wrong, but consistent); the §21c R-multiples reconcile to the §21d mean of +0.04. Failures: §16 states a base case of 7,294–7,520 while §17 states 7,335–7,520; ATR(14) exists nowhere in §9/§21 so the card risk cannot be tied back to it; the §11 claim that weekly S1 (7,385.08) and daily S1 (7,385.35) coincide "within ~0.3 pts" survives only because the weekly block uses the wrong week — on 20–24 Jul weekly S1 is 7,347.43, roughly 38 pts away, and that spurious shelf is carried into §15's bull column; §6's Mon 20 Jul Open of 7,457.69 is the 17 Jul close as published in the 24 Jul report, i.e. a close carried into an open field. | §16 vs §17; §11 narrative; §15; §6 vs `SP500_Report_24Jul2026.md` §6 | 2 | Align §16 and §17 on one base-case range; rebuild the S1 confluence claim on the correct week; correct the 20 Jul open. |
| 4.1 Pillars conclude | §8 ends "Judgement label: Indecision"; §9 "Regime: Transitional" plus a preferred protocol; §10 "Aggregate cross-asset read: MIXED"; §12 tags each bullet price-negative/mixed; §14 closes on the FOMC as the primary directional risk. Each label is consistent with the content above it. Deduction: §9's stated protocol ("favour the confirmed break of the 7,294–7,581 envelope") is not what §21b issues, so the pillar's conclusion does not survive into the strategy section. | §8, §9, §10, §12, §14 | 4 | Carry §9's protocol into §21b or explain the departure. |
| 4.2 Peer/cross-asset interpreted | §10 gives a transmission mechanism per counter — USD translation of multinational earnings plus hawkish-Fed repricing, VIX as an implied-vol/risk-regime gauge with the 20 line as the reference, DAX as a common global-risk factor — and each row carries a confirm/contradict verdict and an explicit implication for the S&P. Not a correlation list; the unresolved USDX/VIX-vs-DAX contradiction is passed to §15 and §16 rather than smoothed over. | §10 table and aggregate line | 5 | None. |
| 4.3 Synthesis reconciles tensions | §9 handles the KER-vs-regime conflict properly through the dual-gate rule; §15/§16 carry the oversold-bounce vs hawkish-FOMC tension; §21a addresses §17 against the score. Against that: §16 and §17 publish two different base-case ranges without reconciling them; and the §21b Trade 2 card is LONG while KER, cross-asset, sentiment, §16 and §17 all lean down, with no justification for taking the upside break and no mirror short-side level — while §9's own protocol points at the 7,294–7,581 envelope, the card enters at 7,425.82, inside that envelope and 2.66 pts above the daily pivot, so "breakout-side" is a mislabel. Trade 3C likewise defines both break levels but issues only the upside. Card construction is scored here per the brief. | §15–§18; §21a; §21b both cards | 2 | Reconcile §16/§17; justify the long-side selection or issue the mirror level; stop calling a pivot-momentum entry a breakout. |
| 4.4 Calibrated language | §17 is exactly one sentence with a single directional claim and no hedge stacking; §3 states Confidence High; §18 splits confidence High (close) / Medium (5-day path), which is the right shape given the corroborated close and indicative intraday. Deductions: §3's "High" is applied to a consensus whose intraday basis is single-source, and §21d calls a −0.99R reconstruction one of "three small losers". | §3, §17, §18, §21d | 4 | Downgrade §3 confidence to reflect the indicative intraday basis; fix the §21d characterisation. |
| 5.1 Data dated; staleness flagged | Every §6 row and every §13a article is dated; the 20–23 Jul intraday O/H/L are explicitly marked single-source indicative and §19 records the data gaps and the leniency instruction. Against that: §19 asserts "the 24 Jul full OHLC are live, two-source corroborated" while §4 shows exactly one source for the 24 Jul High/Low (Investing.com) and one for the Open (CNBC quote page); the 13–17 Jul weekly block is stale for a 27 Jul report and is not flagged as such; the monthly block's stated basis is not the basis actually used. | §6, §13a, §19, §4, §11 | 2 | Match the corroboration claims in §19 to the source count actually shown in §4. |
| 5.2 Assumptions up front | The single-source pivot propagation rule is stated and honoured in the narrative — §11 says weekly and monthly levels are not used for level-based entries, and §19 repeats it — and ATR(14) is declared indicative. But the anchor-override caveat is unintelligible in both places it appears ("overridden for the 27 Jul 2026 run", "overridden to the 27 Jul 2026 run") and names no replacement anchor, and neither card states an anchor at all. | §2, §11, §19, §20, §21b | 3 | Rewrite the anchor caveat and put an explicit anchor line on each card. |
| 5.3 Red flags surfaced | §12 lays out five risk channels with direction and horizon tags; §15 balances five bull against five bear items; the §13d FOMC collision is carried into the caveat line of both issued cards ("holding period collides with 29 Jul FOMC (Tier-1 event)" and "FOMC collision flag"), and the highest-impact event is named in §1, §13d, §14, §16 and §18. | §12, §13d, §15, §21b caveats | 5 | None. |
| 5.4 Restrictions honoured | Clean on the explicit prohibitions: no module codes, no bracketed variable names, no framework name, no ES futures reference, instrument common names used, and the one CFD-referenced quote (Trading Economics 7,412) is classified "Direct." and expressly excluded from the core OHLC basis in §5. Breached on "no synthesised/interpolated price presented as sourced": (i) the monthly pivot block is presented as "prior month June" but back-solves to H 7,581.51 / L 7,294.19 — the report's own 25-session envelope — against a slice June cash range of 7,624.60 / 7,243.10, and its S1 of 7,335 is then quoted as a target in §13d, §16 and §17; (ii) §19 upgrades the single-sourced 24 Jul H/L to "two-source corroborated", which is precisely what licenses the "CORROBORATED" daily pivots that §11's own rule would otherwise bar from entries, and those pivots set every Trade 2 level. | §11 monthly table vs slice June; §19 vs §4; §21b Trade 2 | 1 | Rebuild the monthly block from June's real H/L/C or relabel it; restate the 24 Jul H/L as single-source and re-flag the daily pivots accordingly. |

## 2. Category roll-up

| Category | Level | Multiplier | Points | Justification |
|---|---|---|---|---|
| C1 Prompt adherence (max 20) | 3 | 0.65 | 13.00 | Rows 1.1/1.2/1.3 = 4/2/5, mean 3.67 → level 4; the restriction breach recorded at 5.4 drops C1 one level to 3 per framework §6. Variables, asset, counters, window and audience are right; the weekly and monthly period selections are not. |
| C2 Structure (max 20) | 4 | 0.85 | 17.00 | Rows 2.1/2.2/2.3 = 5/3/4, mean 4.00. Every section and sub-section present and ordered, method chain visible; §6 is missing its Source A / Source B / Final columns. |
| C3 Accuracy & evidence (max 25) | 2 | 0.40 | 10.00 | Rows 3.1/3.2/3.3/3.4 = 2/3/1/2, mean 2.00. The RSI2 column fails to reproduce from the report's own closes on all three testable rows, the §13b tilt fails to reproduce from its own weights, ATR(14) is absent, weekly and monthly pivots sit on the wrong periods, and many §12/§14 numbers are unsourced. Offsetting: the D-1 row, the daily pivots and the §21a score all reconcile exactly. |
| C4 Reasoning & judgment (max 20) | 4 | 0.85 | 17.00 | Rows 4.1/4.2/4.3/4.4 = 4/5/2/4, mean 3.75 → level 4. Cross-asset mechanism and the KER/regime reconciliation are strong; the synthesis fails where §16 and §17 diverge and where the long "breakout" card contradicts the report's own downside skew and its own envelope. |
| C5 Currency, restrictions & transparency (max 15) | 3 | 0.65 | 9.75 | Rows 5.1/5.2/5.3/5.4 = 2/3/5/1, mean 2.75 → level 3. Risk surfacing and event-collision propagation are exemplary; corroboration claims overstate the evidence table and the monthly basis is misattributed. |
| **Total** | — | — | **66.75 → 67** | Sum of category points, rounded to a whole number. |

## 3. Total, band, override check

- Raw total: 13.00 + 17.00 + 10.00 + 17.00 + 9.75 = **66.75 → 67**.
- Band: **Moderate** (60–74).
- Fabricated-source override: **not triggered**. All three spot-checked citations (CNBC 23 Jul, Trading Economics 24 Jul, Investing.com 24 Jul) are named, dated, quote a figure used consistently elsewhere, and the Investing.com 24 Jul range reconciles to the slice within 1 pt. The §20 "stale to 14 Jul" note is an internal documentation contradiction, not evidence of an impossible source, since the figure it attributes is externally correct.
- Restriction-breach override: **triggered**. Synthesised levels presented under a sourced basis — the "prior month June" monthly pivots are the 25-session envelope, and the single-sourced 24 Jul H/L are asserted as two-source corroborated in order to release the daily pivots for card entries. Effect: cap at Moderate (≤ 74) and C1 down one level. The cap is not binding at 67; the C1 reduction from 4 to 3 is applied and is already reflected in §2 above (it costs 4.00 points).
- Final Trust Score: **67 / 100 — Moderate**. Override recorded: `restriction_breach`.

## 4. Card Integrity

Linter rows, verbatim from `qa/regen_20260906_qa1/lint_static/2026-07-27.csv`:

| card_id | report_date | strategy | flags | dud |
|---|---|---|---|---|
| 2026-07-27_Trade_1 | 2026-07-27 | Trade 1 - Daily Directional | SUPPRESSED | False |
| 2026-07-27_Trade_2 | 2026-07-27 | Trade 2 - Pivot (TRANSITION breakout side) | CLEAN | False |
| 2026-07-27_Trade_3C | 2026-07-27 | Trade 3C - Momentum-Breakout (conditional upside) | WARN_TARGET_FAR(3.35xATR) | False |

Per-card integrity, 100 − 40·(#DUD) − 10·(#WARN), floored at 0:

| Card | #DUD | #WARN | Integrity | In report mean? |
|---|---|---|---|---|
| 2026-07-27_Trade_1 | 0 | 0 | 100 | No — SUPPRESSED |
| 2026-07-27_Trade_2 | 0 | 0 | 100 | Yes |
| 2026-07-27_Trade_3C | 0 | 1 | 90 | Yes |

**Report Card Integrity = (100 + 90) / 2 = 95.0** over the 2 non-suppressed cards. Cards in lint file: 3 · DUD flags: 0 · WARN flags: 1.

M5 assessment feeding row 4.3 (separate from the integrity number above):
- **Trade 1** — correctly issued as a SUPPRESSED row rather than omitted, with the threshold test shown (|−0.20| < 0.25). The input is soft: the sentiment component rests on the §13b tilt of −0.30, which recomputes to −0.513, moving the score to −0.230 — suppression still holds. No anchor stated on the card.
- **Trade 2** — arithmetically clean and internally traceable: entry 7,425.82 = P + 0.10×(R1−P), stop 7,392.91 = P − 0.8×(P−S1), R = 32.91 = 0.46×ATR14 (no wide-stop flag needed), stop on the correct side, TP1 < TP2 < TP3, buy stop above the D-1 close, thesis invalidation (daily close below P) separate from the stop, confluences listed, FOMC collision flagged. Defects: it applies the TREND recipe in a TRANSITION regime without stating the substitution; "breakout-side" describes an entry 2.66 pts above the daily pivot and well inside the 7,294–7,581 envelope §9 nominates as the breakout reference; TP1 is 23.98 pts = 0.73R, inside 1R; TP2 and TP3 are given in price only, not points; no anchor line; no mirror short-side level despite the report's stated downside skew.
- **Trade 3C** — the 3C geometry is applied correctly on the report's own range: entry 7,598.01 = high + 0.25×ATR, stop 7,409.11 = low + 0.40×width, TP1 = high + 1.0×width, TP2 = 1.5×, midpoint invalidation 7,437.84 correct, TP3 null (permitted), FOMC flagged. Defects: the 25-session low is 7,294.18 against a slice 7,303.10 (Δ 8.92, outside tolerance), so width and every derived level drift; the implied ATR of 66.04 is never stated and is below the slice ATR14 of 71.21; TP1 sits 270.81 pts from entry = 3.35×ATR on the linter's basis, breaching the 2.5×ATR14 rule (the WARN); levels are quoted in price only; the card is not flagged for the corroboration status of the 25-session boundaries; the down-break level 7,277.67 is defined but no card is issued for it.

## 5. Data reconciliation log

Slice values are cash-session (16:30–23:00 broker) unless stated. Verdict per brief §4 tolerance: close ≤ 3 pts, O/H/L ≤ 8 pts.

| Section | Report value | Slice value | Delta | Verdict |
|---|---|---|---|---|
| §6 Mon 20 Jul Open | 7457.69 | 7495.30 | −37.61 | Discrepancy — and 7,457.69 is the 17 Jul close published in the 24 Jul report, i.e. a close in an open field |
| §6 Mon 20 Jul High | 7469.00 | 7512.80 | −43.80 | Discrepancy (flagged indicative) |
| §6 Mon 20 Jul Low | 7421.00 | 7439.30 | −18.30 | Discrepancy (flagged indicative) |
| §6 Mon 20 Jul Close | 7443.28 | 7446.60 | −3.32 | Marginal fail (>3), well inside the 10-pt failure threshold |
| §6 Tue 21 Jul Open | 7451.00 | 7487.70 | −36.70 | Discrepancy (flagged indicative) |
| §6 Tue 21 Jul High | 7520.00 | 7515.70 | +4.30 | Consistent |
| §6 Tue 21 Jul Low | 7448.00 | 7466.50 | −18.50 | Discrepancy (flagged indicative) |
| §6 Tue 21 Jul Close | 7509.20 | 7508.00 | +1.20 | Consistent |
| §6 Wed 22 Jul Open | 7510.00 | 7490.30 | +19.70 | Discrepancy (flagged indicative) |
| §6 Wed 22 Jul High | 7524.00 | 7525.50 | −1.50 | Consistent |
| §6 Wed 22 Jul Low | 7480.00 | 7488.00 | −8.00 | Consistent (at tolerance) |
| §6 Wed 22 Jul Close | 7498.96 | 7498.80 | +0.16 | Consistent |
| §6 Thu 23 Jul Open | 7492.00 | 7416.70 | +75.30 | Major discrepancy (flagged indicative) |
| §6 Thu 23 Jul High | 7495.00 | 7449.80 | +45.20 | Major discrepancy (flagged indicative) |
| §6 Thu 23 Jul Low | 7402.00 | 7375.30 | +26.70 | Discrepancy (flagged indicative) |
| §6 Thu 23 Jul Close | 7408.30 | 7405.50 | +2.80 | Consistent |
| §6 Fri 24 Jul Open | 7406.30 | 7407.60 | −1.30 | Consistent |
| §6 Fri 24 Jul High | 7460.98 | 7460.20 | +0.78 | Consistent |
| §6 Fri 24 Jul Low | 7396.53 | 7395.60 | +0.93 | Consistent |
| §6 Fri 24 Jul Close | 7411.98 | 7411.80 | +0.18 | Consistent — the D-1 anchor is sound |
| §6 RSI2 Tue 21 Jul | 82.1 | 85.99 (slice closes) | −3.89 | Not testable from the report's own closes (needs pre-window data); differs from slice |
| §6 RSI2 Wed 22 Jul | 65.4 | 86.6 (from the report's own closes) / 86.97 (slice) | −21.2 | **FAIL** — does not reproduce from the report's own close column |
| §6 RSI2 Thu 23 Jul | 14.2 | 0.0 (report's own closes) / 0.00 (slice) | +14.2 | **FAIL** — both prior changes negative, RSI2 must be 0 |
| §6 RSI2 Fri 24 Jul | 19.3 | 3.9 (report's own closes) / 6.33 (slice) | +15.4 | **FAIL** — propagated into §1, §8 and §15 |
| §6 Trend labels (all 5) | Neutral/Bullish/Neutral/Bearish/Neutral | Same under corrected RSI2 | 0 | Consistent — labels survive the RSI2 correction |
| §11 Daily P | 7423.16 | 7422.53 | +0.63 | Consistent; reproduces exactly from the report's own 24 Jul H/L/C |
| §11 Daily R1 / S1 | 7449.80 / 7385.35 | 7449.47 / 7384.87 | +0.33 / +0.48 | Consistent; R1 = 2P−L and S1 = 2P−H both check |
| §11 Daily R2 / S2 | 7487.61 / 7358.71 | 7487.13 / 7357.93 | +0.48 / +0.78 | Consistent; identity R2−P = P−S2 = 64.45 holds exactly |
| §11 Daily R3 / S3 | 7514.25 / 7320.90 | 7514.07 / 7320.27 | +0.18 / +0.63 | Consistent |
| §11 Weekly P (stated 13–17 Jul) | 7475.22 | 7487.17 | −11.95 | Discrepancy — implied H/L 7,565.36 / 7,402.60 vs slice 7,582.80 / 7,431.60 |
| §11 Weekly S1 (stated 13–17 Jul) | 7385.08 | 7391.53 | −6.45 | Does not reconcile on the stated week |
| §11 Weekly P vs correct prior week (20–24 Jul) | 7475.22 | 7436.47 | +38.75 | **Wrong period** — prior completed week for a 27 Jul report is 20–24 Jul |
| §11 Weekly S1 vs correct prior week | 7385.08 | 7347.43 | +37.65 | **Wrong period** — voids the "weekly/daily S1 confluence within 0.3 pts" claim used in §11 and §15 |
| §11 Monthly P (stated prior month June) | 7458.35 | 7452.97 | +5.38 | Pivot near, but the block's width is not June's |
| §11 Monthly R1 / S1 | 7622.51 / 7335.19 | 7662.83 / 7281.33 | −40.32 / +53.86 | **Wrong basis** — back-solved H 7,581.51 / L 7,294.19 equals the 25-session envelope, not June (7,624.60 / 7,243.10) |
| §11 Monthly R2 / S2 | 7745.67 / 7171.03 | 7834.47 / 7071.47 | −88.80 / +99.56 | **Wrong basis**; S1 of 7,335 is nonetheless quoted as a target in §13d, §16, §17 |
| §11 Monthly R3 / S3 | 7909.83 / 7047.87 | 8044.33 / 6899.83 | −134.50 / +148.04 | **Wrong basis** |
| §9 25-session high | 7581.50 | 7582.80 | −1.30 | Consistent |
| §9 25-session low | 7294.18 | 7303.10 | −8.92 | Discrepancy (>8) — propagates to 3C width, stop and both break levels |
| §9 / §21 ATR(14) | Not stated (66.04 implied by the 3C levels) | 71.21 cash (80.84 full-day) | −5.17 vs cash | **Missing** — required by row 3.3; the 24 Jul report implied ~72.5, consistent with the slice |
| §9 / §10 VIX Tue | 17.05 | 17.43 (21 Jul); 17.04 is the 15 Jul close | −0.38 | Discrepancy — value looks anchored to the wrong session |
| §9 / §10 / §14 VIX Fri | 18.58 | 18.36 | +0.22 | Minor discrepancy; direction (rising) correct |
| §10 / §12 USDX level | 101.46 | 101.47 | −0.01 | Consistent |
| §10 / §12 USDX weekly change | +0.7% | +0.72% (100.74 → 101.47) | −0.02pp | Consistent |
| §10 DAX 40 (25,099, Fri +1.36%) | 25,099 / +1.36% | No in-scope slice | n/a | Unverified — outside the permitted inputs |
| §13b sentiment tilt | −0.30 | −0.513 (weighted mean of the six §13a rows at the stated 1.0/0.7/0.5 weights) | +0.213 | **FAIL** — does not reproduce from its own stated method |
| §21a / §20 direction score | −0.20 | −0.198 from the §20 contributions on the default weights | +0.002 | Consistent as published; recomputes to −0.230 with the corrected tilt — still below the 0.25 threshold, so Trade 1 stays suppressed |
| §21c/§21d backtest mean R | +0.04 | (−0.99 −0.16 +1.37 −0.06)/4 = +0.04 | 0.00 | Consistent — though the R denominator (~61–67 pts per row) is never stated |
| §16 vs §17 base-case range | 7,294–7,520 (§16) vs 7,335–7,520 (§17) | n/a | 41 pts on the lower bound | **Internal conflict** between adjacent sections |
