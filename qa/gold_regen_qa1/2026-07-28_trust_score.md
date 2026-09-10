# Trust Score — Gold_Report_28Jul2026.md (D = 2026-07-28) — run gold_regen_qa1

Basis claimed by report: masthead "Spot XAU/USD (loco London)" and §2 "OTC London spot, immediate
settlement (T+2 loco London)", "Global 24-hour OTC market" → checked against the `_full` columns of
`data/levels/XAUUSD_by_date/2026-07-28.csv` (last_bar_date 2026-07-27 < D, confirmed). `atr14_full` =
85.1286. `_cash` columns cross-checked as a sanity check only.

## 1. Section 7 checklist

| Row | Notes | Evidence | Score |
|---|---|---|---|
| 1.1 Variables respected | Asset correctly spot XAU/USD loco-London, GC=F used corroboration-only and normalised; USDX is the first counter in §10; USD/oz; lookback 5/25 stated; 7 sources used (≥6); tick convention ($0.01, quoted as both $ and ticks) used consistently. But the [AS_OF_DATE] variable — defined in `M1_Variables_v2_1.md` as "the last completed regular session… strictly before the report date… it does not move back a session because that session's close was awkward to source" — is violated for the daily pivot specifically: §11.1 computes the Daily pivot from **24 Jul (Fri)**, not **27 Jul (Mon)**, even though 27 Jul is used correctly everywhere else (§1/§3/§4/§6/§21). One moderate, sub-section-scoped deviation. | §2, §6, §11.1, `M1_Variables_v2_1.md` | 3 |
| 1.2 Coverage & currency consistent | Same 24-Jul-vs-27-Jul date drift is a whole-report coverage-period consistency break: the report's own §6 table states 27 Jul is the latest validated session, then §11.1 silently reverts to 24 Jul three lines later. No USD/oz or tick-unit drift elsewhere. | §6 vs §11.1 | 3 |
| 1.3 Audience & tone | Institutional Senior Commodities Analyst register maintained throughout ("institutional research standards," calibrated confidence labels, no retail tone). | §1, §18 | 5 |
| 2.1 Sections present & ordered | All 21 top-level sections (§1–§21, with 13a–d and 21a–d) present, correctly ordered, appropriately weighted. | headings | 5 |
| 2.2 Scorecard as table | §6 is a genuine table with the specified columns (plus an added Trend column — additive, not missing). §11's daily/weekly/monthly tables are rendered as 5-tier (R5…S5) rather than the specified 3-tier (R3→P→S3) — more information than required, not less, but a template deviation. | §6, §11 | 4 |
| 2.3 Method steps visible | §4–§5 show observation → normalisation → consensus with the futures-to-spot adjustment stated (~$0–5 carry); §8 is candle-by-candle; §9 gives regime/persistence/overlap/VOLator/KER. §7 chart headings are present for all five charts with no image or caption (conversion-only artifact per the brief — not scored). | §4–§9 | 5 |
| 3.1 Quantitative claims sourced | Most §1/§12/§14 claims trace to §4/§6/§13. One exception: §14 "Positioning" cites "COT specs had trimmed longs into the pullback" with no source reference anywhere in §4 or §13. | §1, §12, §14 | 4 |
| 3.2 Citations exist & contain data | Spot-checked TradingEconomics (§4), World Gold Council 244t-Q1/41t-May figure (§12 and §13a, quoted consistently in both places), and OCBC/LiteFinance bearish call (§13a, referenced again in §13b). All three are named, dated, and internally consistent. No fabrication found; no hallucination override triggered. | §4, §12, §13a–b | 5 |
| 3.3 Calculations transparent | RSI2 51.1 for 07-27 **reproduces exactly** from the report's own stated closes (07-23 4,076.00 → 07-24 4,053.17 → 07-27 4,077.00: avg gain 11.915, avg loss 11.415, RS 1.0438, RSI2 = 100−100/2.0438 ≈ 51.1). Daily/weekly/monthly pivot formulas (P=(H+L+C)/3, R1=2P−L, etc.) reproduce exactly from each table's own stated H/L/C. ATR(14) itself is never stated as a plain number in the report body — only backed into via "3×ATR cap $4,292.64" (implies ATR≈71.9) and Trade 3C's "≈5.4×ATR" (implies ATR≈71.9) — both self-consistent with each other but never stated directly. | §6, §11, §21b | 4 |
| 3.4 Numbers reconcile — incl. vs level file | **Internally** the D−1 close (4,077.00) is consistent across §1/§3/§4/§6/§21. **Externally**, against `XAUUSD_by_date/2026-07-28.csv` (_full, atr14_full=85.1286): **Low** 4,009.11 vs 4,065.37 → Δ56.26 = 0.66×ATR (FAIL, >0.20×ATR≈17.03 — this is the single largest OHLC miss found). **Open** 4,053.17 vs 4,089.78 → Δ36.61 = 0.43×ATR (FAIL). High (Δ0.05) and Close (Δ0.34) are both well within tolerance. **Daily pivots** (§11.1, anchored to the wrong 24-Jul session): every level fails — P Δ33.68 (0.40×ATR), R1 Δ23.54, S1 Δ33.62, R2 Δ23.60, S2 Δ43.76, R3 Δ13.46, S3 Δ43.70, all beyond the 0.115×ATR≈9.79 failure line. **Weekly pivots** (§11.2, correct week 20–24 Jul chosen, but H/L/C values off): P Δ7.76 and R1 Δ7.26 sit in the discrepancy band, but S1 Δ15.32, R2 Δ14.82, S2 Δ30.34, R3 Δ29.84, S3 Δ37.90 all fail. **Monthly pivots** (§11.3) are catastrophically wrong: report's June H/L/C (3,720/3,548/3,705) implies P=3,657.67 vs level-file m_full_P=4,165.51 — **Δ507.84 = 5.97×ATR**; R3 Δ1,051.40. **RSI2** 51.1 vs level-file rsi2_full=100.0 → Δ48.9 points (FAIL, >15). This is far beyond "one factual error of moderate consequence" — it is a cluster of large, mutually-reinforcing errors (wrong D−1 low/open, one-session-stale daily pivot, badly wrong monthly OHLC) that propagate into the Executive Snapshot, §8/§15/§16 narrative, and two of three trade cards. | §1,§6,§11 vs level file | 1 |
| 4.1 Pillars conclude | §8 ends "Judgement label: Range —"; §9 ends with an explicit KER-vs-regime reconciliation; §10 ends "Aggregate cross-asset = MIXED"; §12's five sub-factors each carry an upfront direction label; §14 ends with a Watch item tying the section together. | §8–§10, §12, §14 | 4 |
| 4.2 Peer/cross-asset interpreted | §10 gives a genuine mechanism per counter (USDX→bullion price, S&P/DAX→flow competition with gold), not a bare correlation list, and an explicit contradiction flag/aggregate call. | §10 | 5 |
| 4.3 Synthesis reconciles tensions | §9 explicitly reconciles KER vs the choppier short-term tape; §16 explicitly treats the short-term rotation as a consolidation within the medium-term trend; §21a explicitly checks §17 vs the +0.39 score for a conflict and finds none. | §9, §15–§18, §21a | 5 |
| 4.4 Calibrated language | §17 is exactly one conditional sentence ("…provided the 29 July FOMC does not deliver a hawkish surprise"); confidence is stated as Medium with an explicit reason (§3); no hedge-stacking. | §3, §17 | 5 |
| **Card construction (feeds C4, see §3 of the brief)** | Trade 1's inputs (entry=D−1 close, "nearest support $4,053") land close to the *correct* daily S1 (4,055.96) by coincidence, so its static levels are reasonable despite citing the wrong pivot table. Trade 2's entry/TP1/TP2/TP3 are all directly derived from the stale 24-Jul daily pivot (§11.1) and are therefore each off by ≈$23–33 from what the correct 27-Jul-anchored pivot would give (e.g. entry $4,055.47 vs a correct-pivot entry of $4,088.14). Trade 3C's 25-session range ("$3,548–$4,166") reuses the corrupted §11.3 June monthly **low** ($3,548) as its range floor instead of the level file's actual 25-day low (swing_low_25d_full=3,943.08) — this single substitution is the direct cause of the card's WARN_R_HUGE/WARN_TARGET_FAR linter flags (R $388.69 ≈ 4.57×ATR): with the correct range floor the stop would be ≈$4,046.93 and R ≈$136.91 (≈1.6×ATR), inside normal bounds. | §11.1–§11.3, §21b, lint_static | 3 |
| 5.1 Data points dated; staleness flagged | Every price and article in §4/§6/§13 is dated; §6 legend explains MEDIAN-ACCEPTED extremes; §11 flags weekly/monthly as SINGLE-SOURCE INDICATIVE. | §4, §6, §11, §13 | 5 |
| 5.2 Material assumptions stated up front | Futures-to-spot normalisation is stated with its size (§5, "~$0–5 carry"). But the daily-pivot's 24-Jul-vs-27-Jul session substitution is **never disclosed anywhere** — not on the card, not in §19, not in §20's "Anomalies" row (which lists only the Trade 3C stop cap and the weekly/monthly indicative flag). This is a silent anchor departure of exactly the kind the brief's daily-open-anchor guidance says must instead be "logged as a non-conformance." Separately, §20's daily-open-anchor line ("overridden to 00:00 UK; matches the gold default") claims a match to a "gold default" that, per the brief, does not exist for this run (no gold M1 instance) — an internally unverifiable, template-looking claim. | §11.1, §19, §20 | 2 |
| 5.3 Red flags surfaced | FOMC event risk, hawkish-hold headwind and the Trade 1 event-collision caveat are all elevated to §12/§15/§21b, not buried. | §12, §15, §21b | 5 |
| 5.4 Restrictions honoured | No bracketed variable names or module codes (M1..M5) or framework name found in the report body (checked). CFD/retail quotes are flagged directional-only and not used as point anchors; GC=F is corroboration-only. The one soft issue: §11.1's "Source status: … CORROBORATED" label is attached to pivot data computed from the wrong (24-Jul) session without flagging that provenance gap — a mild instance of presenting mis-anchored data with an unqualified corroboration label. | whole report | 4 |

## 2. Category roll-up

| Cat | Rows averaged | Mean → level | Multiplier | Points (of max) | Justification |
|---|---|---|---|---|---|
| C1 Prompt adherence | 1.1=3, 1.2=3, 1.3=5 → 3.67→4 | **4** | 0.85 | 17.00 / 20 | Asset/counters/sources/units/tick all correct; the one deviation is the sub-section-scoped daily-pivot date drift (not a wholesale variable failure), so it does not force a cap below 4. |
| C2 Structure | 2.1=5, 2.2=4, 2.3=5 → 4.67→4* | **4** | 0.85 | 17.00 / 20 | All 21 sections present and correctly ordered; the only deviation is the 5-tier (not 3-tier) pivot table format — additive, no information lost. Rounded conservatively to 4 given more than one minor deviation accumulates. |
| C3 Accuracy & evidence | 3.1=4, 3.2=5, 3.3=4, 3.4=1 → 3.5→~2 | **2** | 0.40 | 10.00 / 25 | Sourcing, citation integrity and calculation transparency are genuinely strong, but 3.4 fails severely and repeatedly: D−1 low off by 0.66×ATR, D−1 open off by 0.43×ATR, every daily-pivot level fails, most weekly-pivot levels fail, the monthly pivot is off by ~6×ATR, and RSI2 misses the level file by 48.9 points. This is multiple, large, mutually-reinforcing factual errors that materially affect trustworthiness of the technical picture — weighted down from the mechanical row mean to reflect that severity, consistent with "substantial gaps that materially affect trustworthiness" (rubric level 2). |
| C4 Reasoning & judgment (incl. card construction) | 4.1=4, 4.2=5, 4.3=5, 4.4=5 → 4.75→5, card construction=3 pulls it down | **4** | 0.85 | 17.00 / 20 | Pillar conclusions, cross-asset mechanism, synthesis and calibration are all strong (would be 5 on narrative reasoning alone). Pulled to 4 by card-construction defects: Trade 2's full price ladder and Trade 3C's stop/targets are built on corrupted §11 inputs (stale daily pivot; wrong monthly-low-as-range-floor), producing Trade 3C's oversized R and far targets. |
| C5 Currency & transparency | 5.1=5, 5.2=2, 5.3=5, 5.4=4 → 4.0→4 | **4** | 0.85 | 12.75 / 15 | Dating and red-flag surfacing are strong. 5.2 is the weak point: the daily-pivot session substitution is never logged as a non-conformance anywhere in the report, and the §20 anchor-override line references a "gold default" that cannot exist for this run. |

**Total = 17.00 + 17.00 + 10.00 + 17.00 + 12.75 = 73.75 → 74**

## 3. Total, band, override

- **total = 74**
- **band = Moderate (60–74)**
- **override = none** — Hallucinated-source check: the three spot-checked citations (row 3.2) all exist, are dated, and quote figures used consistently elsewhere; no fabrication found. Restriction-breach check: no bracketed variable name, module code (M1..M5) or framework name appears in the report body (checked by direct search); the daily-pivot date-anchor problem is a Variables/reconciliation failure (scored under C1/C3/C5), not an "openly violated" prompt restriction of the row-5.4 kind, so it is not treated as a restriction-breach override.

## 4. Card Integrity (linter rows, copied verbatim from `qa/gold_regen_qa1/lint_static/2026-07-28.csv`)

| card_id | report_date | strategy | flags | dud | per-card score |
|---|---|---|---|---|---|
| 2026-07-28_Trade_1 | 2026-07-28 | Trade 1 - Daily Directional (LONG) | CLEAN | False | 100 |
| 2026-07-28_Trade_2 | 2026-07-28 | Trade 2 - TRANSITION: breakout-side only (upside), aligned with the 3C long thesis | CLEAN | False | 100 |
| 2026-07-28_Trade_3C | 2026-07-28 | Trade 3C - post-consolidation upside breakout of the 25-session range | WARN_R_HUGE(4.57xATR)\|WARN_TARGET_FAR(7.05xATR) | False | 80 |

`card_integrity = 100 - 40*(#DUD) - 10*(#WARN)`, floored at 0, per card; report level = mean over the
three non-suppressed cards = (100 + 100 + 80) / 3 = **93.3**. Note: static integrity (stop side, TP
ordering, R bounds) passes on all three cards — the linter's WARN flags on Trade 3C are exactly what
the corrupted range-floor input (see C4 card-construction row above) would be expected to produce; the
linter does not know the input is wrong, only that the resulting R/target are outsized.

## Summary line

```
c1=4  c2=4  c3=2  c4=4  c5=4
total=74
band=Moderate
override=none
card_integrity=93.3
n_cards=3
n_duds=0
n_warns=2
```
