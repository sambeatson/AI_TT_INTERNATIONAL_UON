# Trust Score v3.7 — FTSE 100 daily report, 09 Jul 2026 (run ftse_qa1)

Report: `reports/md/FTSE_EuroStoxx_Report_09Jul2026.md` · D = 2026-07-09 (Thursday) · D-1 = 2026-07-08 (Wednesday)
Level file: `data/levels/UK100_by_date/2026-07-09.csv` — `last_bar_date` = 2026-07-08 < D (leak check passed).
Basis the report claims: FTSE 100 cash index, LSE regular session 08:00–16:30 UK, so compared on the `_cash` basis (`--cash-open 10:00 --cash-close 18:30`). `_full` shown where it explains a gap.

## Machine-readable result
```
c1=2
c2=3
c3=1
c4=3
c5=3
total=49
band=Low
override=restriction_breach
card_integrity=100
n_cards=3
n_duds=0
n_warns=0
```
(`n_cards` = 3 card rows, of which 2 are SUPPRESSED and 1 is scored. Card Integrity is separate from the 100.)

## 1. Section 7 checklist

| Row | Notes | Evidence (location) | Score |
|---|---|---|---|
| 1.1 Variables respected | FTSE 100 cash is primary and STOXX carries no card. Counters are DXY, S&P 500, DAX 40 and STOXX. As-of D-1, London tz, 5-session lookback and GBP are all respected. The sources are all aggregators or media: no index provider, exchange or sell-side tier is accepted (LSE/STOXX pages "JS-gated"). The 07:00 UK daily-open anchor is overridden "on instruction". | header note, §2, §4, §20, §21b | 3 |
| 1.2 Coverage and currency consistent | A 04 Jul 2026 session is invented: it was a Saturday, and the US holiday was observed Fri 03 Jul. The real 06 Jul (Mon) session is missing from the 5-day window. "Weekend" geopolitics is cited as the driver of a Thursday open, and "pre-weekend" appears in §3. STOXX 6,360.47 is dated "~03 Jul" in §4 but sits on 07 Jul in §6. Morningstar is dated "Feb/ongoing". | §6, §3, §4, §13a, §13d, §15, §18, §21b | 2 |
| 1.3 Audience and tone | The register suits an equity strategist and a trading/risk review. There is no retail tone. | §1, §18 | 4 |
| 2.1 Sections present and ordered | All 21 headings, §13a–d and §21a–d are present and in order. §7 is only a "charts suppressed" paragraph, with no chart, caption or placeholder. §11 omits the weekly and monthly pivot tables. | headings, §7, §11 | 3 |
| 2.2 Scorecard as table | §6 is a table, but it lacks the Source A / Source B / Final columns. The §11 daily table runs R3→S3, but there are no weekly or monthly tables. | §6, §11 | 2 |
| 2.3 Method steps visible | §4–§5 show observations, classification and consensus. §8 is candle-by-candle with a sequence call. §9 gives regime, overlap and VOLator only qualitatively, with no ATR14, KER or VOLator numbers. The charts are absent. | §4–§9 | 3 |
| 3.1 Quantitative claims sourced | The numbers in §1, §12 and §14 carry no source or cross-reference: BoE 3.75%, UK CPI 2.8% "from 3.3%", EZ CPI 2.8%, Shell+BP "~14%", "~80% overseas revenue", ATH 10,934.90 and 4% below it. | §1, §12, §14 | 2 |
| 3.2 Citations exist, contain the data | The corroboration claim contradicts itself. §19 and §20 call the close "within ±0.10-pt tolerance" of 10,492.51, but the TE source is "≈10,480–10,490" (≈10,485) with the quote "declined over 0.5%". §5 says TE GB100 is a CFD "not a corroborating close", yet §4 classes it "Core" and §20 uses it as the corroborating pair. §3 also treats a ~8-pt gap on 07 Jul as outside tolerance. The Yahoo STOXX 6,360.47 is dated "~03 Jul", but §6 puts 6,360 on 07 Jul and 6,412 on 03 Jul. The Morningstar item has no date. The sources are named and plausible, and I cannot fetch them. I treat this as misrepresented corroboration, not a proven fabricated source, so no hallucinated-source override. | §4, §5, §19, §20, §13a | 1 |
| 3.3 Calculations transparent | The pivot arithmetic reproduces from the report's own H/L/C. RSI2 on the report's own closes gives 89.9 / 56.4 / 10.3 for 04 Jul / 07 Jul / 08 Jul, against 41 / 58 / 9 stated. The 04 Jul RSI2 is wrong by 48.9 points. ATR14 is never stated. KER(13, EMA3) and VOLator are unquantified. §21a lists three contributions summing to 0.00 (−0.06 + 0.06 + 0.00) but states a net of +0.18, and the other three signals and weights are not shown. | §6, §9, §11, §21a | 2 |
| 3.4 Numbers reconcile | The 08 Jul day change is "−1.6%" / "−1.63%" in §1, §4 and §8. The report's own closes give −1.87% from 10,691.98 and −1.79% from 10,684. §3 puts the STOXX consensus at ≈6,360 while §6 has its 08 Jul close at 6,285. §11 says the close is "just above" P 10,542 and then "below" it. The Trend labels contradict the report's rule: 02 Jul (C>O, RSI2 63), 07 Jul (C>O, RSI2 58) and 04 Jul (C<O, RSI2 41) are labelled Neutral. §21b TP2 "broken 04-Jul close" points at a non-session. | §1, §3, §6, §11, §21b | 1 |
| 4.1 Pillars conclude | §8 Exhaustion, §9 Transitional and §10 MIXED each end in a label. §12 has per-bullet tags but no net direction. §14 ends with a positioning bullet and no direction label. | §8–§14 | 3 |
| 4.2 Cross-asset interpreted | The mechanisms are explained (dollar-earner translation, risk beta, regional proxy), and the contradiction flag is good. The premises are partly wrong against the slice: USDX closed at 101.05, not "~100", and is −0.35% over the 5 sessions to 08 Jul. S&P 500 is "Falling", but it is 7,468.5 against 7,478.8 on 01 Jul (−0.14%). | §10, §14 | 4 |
| 4.3 Synthesis reconciles tensions | The §21a conflict flag against §17 is present. But a LONG card is issued from a sub-threshold +0.18 score against a §15 "modestly bearish" balance and an Exhaustion call. The score build is not derivable. | §15–§18, §21a | 3 |
| 4.4 Calibrated language | §17 is one sentence with no hedge stacking. Confidence is stated in §3 and §18. | §3, §17, §18 | 4 |
| 4.5 Card construction (protocol, Category 4) | Trade 3A is issued in a TRANSITION regime, where the rule calls for 3C. Entry is not the 57.5% retrace, and the stop and targets are not the rule levels. A second entry is carried on the same card. The TP2 anchor is a non-session. The weekend gap caveat is wrong, and D's scheduled events are missing from the caveats. See feedback. | §21b | 2 |
| 5.1 Data dated; staleness flagged | Most items are dated, and the indicative OHLC is flagged well. The 04 Jul date is impossible, Morningstar is "Feb/ongoing", the Yahoo STOXX date is approximate, and the stale Morningstar item gets institutional weight 1.0 in the tilt. | §4, §6, §13a, §13b | 3 |
| 5.2 Assumptions up front | The data-sourcing note opens the report, and the anchor override is stated on the card and in §20. | header, §20, §21b | 4 |
| 5.3 Red flags surfaced | The risks in §12, §13d and §15 are surfaced. The real D-day scheduled items are not carried: US Initial Jobless Claims 13:30 UK (HIGH; consensus 210, prior 215), ECB Monetary Policy Meeting Accounts 12:30 UK, US Existing Home Sales 15:00 UK and the US 30-Year Bond Auction. §13d uses undated "mid-Jul" entries. The "weekend gap" caveat is wrong for a Thursday. | §13d, §15, §21b | 3 |
| 5.4 Restrictions honoured | TE GB100 CFD closes are used as a "Core" corroborating source in the OHLC basis (§4, §20) while §5 says retail CFD is excluded. The 04 Jul OHLC are "reconstructions from reported session ranges" (§6 note) presented as "Close corrob.", although §19 says no synthesis was applied. The 02 Jul close is not reproducible from the data. No module codes, bracketed names or framework name were found. Futures are not used. | §4–§6, §19, §20 | 1 |

## 2. Category 3 detail — report vs level file (cash basis; |Δ| tolerance: close 5 / O,H,L 10)

| Session | Field | Report | Slice cash | Δ | Verdict |
|---|---|---|---|---|---|
| 02 Jul | O / H / L / C | 10,486 / 10,540 / 10,460 / 10,528 | 10,433.6 / 10,686.8 / 10,424.8 / 10,654.0 | +52.4 / −146.8 / +35.2 / **−126.0** | all fail (close >15) |
| 02 Jul | RSI2 | 63 | 86.19 | −23 | fail |
| 03 Jul | O / H / L / C | 10,530 / 10,690 / 10,525 / 10,679 | 10,689.3 / 10,692.5 / 10,590.6 / 10,660.5 | −159.3 / −2.5 / −65.6 / **+18.5** | O, L, C fail (close >15) |
| 03 Jul | RSI2 | 88 | 100.00 | −12 | fail |
| "04 Jul" | whole bar | 10,680 / 10,712 / 10,655 / 10,662, RSI2 41 | none: Saturday, no UK100 bars | n/a | **non-existent session** |
| 06 Jul | whole bar | omitted | 10,672.4 / 10,726.7 / 10,607.9 / 10,641.1, RSI2 25.10 | n/a | **real session missing** |
| 07 Jul | O / H / L / C | 10,651 / 10,747 / 10,651 / 10,684 | 10,657.8 / 10,739.6 / 10,639.1 / 10,680.1 | −6.8 / +7.4 / +11.9 / +3.9 | O, H, C pass; L marginal fail (+11.9 vs 10) |
| 07 Jul | RSI2 | 58 | 66.78 | −9 | fail (basis) |
| 08 Jul | O / H / L / C | 10,666 / 10,666 / 10,467 / 10,492.51 | 10,634.1 / 10,636.3 / 10,454.7 / 10,457.0 | +31.9 / +29.7 / +12.3 / **+35.5** | all fail (close >15) |
| 08 Jul | vs full-day | same | 10,638.9 / 10,674.1 / 10,454.7 / 10,492.6 | +27.1 / −8.1 / +12.3 / −0.1 | the close equals the 23:45 broker bar, not the cash close |
| 08 Jul | RSI2 | 9 | 14.88 (cash) | −6 | marginal; arithmetic on own closes gives 10.3 (OK) |

RSI2 arithmetic on the report's own closes: the 04 Jul value fails (stated 41, reproduced 89.9) and the 07 Jul and 08 Jul values pass. The 02 Jul and 03 Jul values cannot be tested, because the window lacks earlier closes.

Daily pivots, report vs cash level file (report P/R/S from indicative 08 Jul H/L/C, which are themselves off the slice):

| Level | Report | Cash | Δ |
|---|---|---|---|
| P | 10,542 | 10,516.0 | +26.0 |
| R1 | 10,617 | 10,577.3 | +39.7 |
| R2 | 10,741 | 10,697.6 | +43.4 |
| R3 | 10,816 | 10,758.9 | +57.1 |
| S1 | 10,418 | 10,395.7 | +22.3 |
| S2 | 10,343 | 10,334.4 | +8.6 |
| S3 | 10,219 | 10,214.1 | +4.9 |

Against the full-day file, P is within 1.4, but R2 is −19, S2 +22, R3 −30 and S3 +31. The report states the cash basis. Weekly and monthly pivots are not given. The cash weekly P is 10,589.67 and the cash monthly P is 10,412.17, so they are computable.

Other slice checks:
- ATR14 (cash) is 124.11, and the report does not state it.
- The 25-session swing is 10,126.2 to 10,739.6. The report's "10,127" June low matches. Its "10,747" high is +7.4 off, which is within the open/high/low tolerance.
- USDX closes were 101.41 (01 Jul), 100.86 (02 Jul), 101.06 (07 Jul) and 101.05 (08 Jul).
- The calendar shows Eurozone CPI y/y at 3.0 actual against 3.2 prior on 01 Jul. The report says 2.8%.
- The 02 Jul US NFP print was 57 against a consensus of 43 and a prior of 172, and USDX fell 0.55% that day. The report says "strong US jobs firmed USD".

## 3. Category roll-up

| Cat | Rows | Mean | Level | Multiplier | Points | Justification |
|---|---|---|---|---|---|---|
| 1 Prompt adherence (20) | 3, 2, 4 | 3.0 → 3, **minus 1 for the restriction-breach override** | 2 | 0.40 | 8.00 | The anchor is overridden, the window has an invented session and a missing one, and the weekend framing is wrong. |
| 2 Structure (20) | 3, 2, 3 | 2.67 → 3 | 3 | 0.65 | 13.00 | All sections are present, but there are no charts, no weekly or monthly pivot tables, and the §6 columns are incomplete. |
| 3 Accuracy (25) | 2, 1, 2, 1 | 1.5; lower level taken in doubt per §9 | 1 | 0.20 | 5.00 | Four of five 5-day bars fail (02 Jul close −126, a Saturday bar, a missing 06 Jul, 08 Jul close +35.5). The corroboration claim is self-contradictory, RSI2 and Trend labels are wrong, and ATR14/KER are not stated. |
| 4 Reasoning (20) | 3, 4, 3, 4, 2 | 3.2 → 3 | 3 | 0.65 | 13.00 | Mechanisms and the conflict flag are sound. The card is built off-rule and the §21a derivation is not traceable. |
| 5 Currency, restrictions, transparency (15) | 3, 4, 3, 1 | 2.75 → 3 | 3 | 0.65 | 9.75 | Caveats are up front and indicative data is flagged. The CFD basis is used and dates are wrong. |
| **Total** | | | | | **48.75 → 49** | |

## 4. Total, band and override

- Total: 49 / 100. Band: **Low Trust (40–59)**, with no regeneration use as-is.
- Hallucinated-source override: not triggered. The sources are named and dated and I cannot fetch them. The self-contradictions are recorded under 3.2 instead.
- Restriction-breach override: **triggered** on row 5.4.
  - The CFD series (TE GB100) is used as a "Core" corroborating close in the OHLC basis, against the report's own §5 exclusion and the retail-CFD restriction.
  - OHLC "reconstructions" are shown for a date with no session and tagged "Close corrob.", against the no-synthesis restriction.
  - The effect is a cap at Moderate (60–74), which is not binding at 49, and C1 down one level (3 → 2).

## 5. Card Integrity (linter rows, verbatim from `lint_static/2026-07-09.csv`)

| card_id | strategy | flags | dud |
|---|---|---|---|
| 2026-07-09_Trade_1 | Trade 1 — Daily Directional | SUPPRESSED | False |
| 2026-07-09_Trade_2 | Trade 2 — Pivot (regime-aware) | SUPPRESSED | False |
| 2026-07-09_Trade_3A | Trade 3A — Momentum-Pullback (long), TRANSITION regime with oversold short-term hook | CLEAN | False |

- Trade 3A: 100 − 40·0 − 10·0 = 100.
- Report level is the mean over non-suppressed cards, so card_integrity = 100 (n_cards = 3, n_duds = 0, n_warns = 0).
- CLEAN is a static check only. The rule-construction defects on Trade 3A are scored under row 4.5 and listed in the feedback.
- Scoring-engine requirement flagged: a buy limit at 10,470 is above the D-1 cash close of 10,457.0, though it is below the report's own 10,492.51. On the report's own close it is not an integrity failure.

## 6. Reviewer scope note

My first shell command listed `README.md`, `docs/ENTRY_POLICIES.md` and `cards/regenerated/` by name. I read none of them and did not open their contents. No file other than those named in `SESSION_TASK.md` was read. `results/` and `data/raw/` are absent from the tree, as expected. Nothing here depends on price on or after D.
