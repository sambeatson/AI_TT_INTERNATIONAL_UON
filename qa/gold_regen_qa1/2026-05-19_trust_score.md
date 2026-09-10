# Trust Score v3.7 — Gold_Report_19_May_2026.md (D = 2026-05-19)

Reviewer: gold_regen_qa1 session · ASSET = XAUUSD
Level file used: `data/levels/XAUUSD_by_date/2026-05-19.csv` (`last_bar_date` = 2026-05-18 < D — verified leak-free).
Basis used for Category 3 checks: report claims "OTC London spot", "loco London", "Global 24-hour OTC market"
(§2, §3, §5) → checked primarily against `_full` columns; `_cash` checked as cross-reference.

## 1. Section 7 checklist

| Row | Reviewer notes | Evidence observed | Score (0–5) | Action required |
|---|---|---|---|---|
| 1.1 Variables respected | Asset/LBMA convention, USDX-first counter (§10 order), 5d/25d lookback, USD/oz, 7 sources (≥6) all respected. Two defects: (a) §2's "As-of date/timezone" row states **19 May 2026** — but M1 defines AS_OF_DATE as the last completed session strictly before D (18 May), and the report's own §1/§20 correctly treat 18 May as the as-of session. The formal §2 field conflates run-date with as-of-date. (b) Tick size/name is never populated as a §2 Variable row (only appears ad hoc inside §21b cards as "tick = 0.01 USD/oz"), though M1 requires it stated when strategies are produced. | §2 "As-of date/timezone" row; §21b tick references | 3 | Correct §2's As-of date to 18 May 2026 (the as-of *session*, distinct from the 19 May run/report date); add an explicit Tick size / Tick name row to §2. |
| 1.2 Coverage & currency consistent | Same As-of-date conflation as 1.1 is a coverage-consistency defect. No USD/oz vs tick unit drift otherwise. | whole report | 3 | Same fix as 1.1(a). |
| 1.3 Audience & tone | Senior Commodities Analyst / institutional register maintained throughout; no retail tone. | §1, §18 | 5 | none |
| 2.1 Sections present & ordered | §1–§21 all present. One lettering deviation: the spec's §13c "prior calendar" / §13d "upcoming calendar" are instead at §13d/§13e in this report, because an unlabelled extra subsection ("Divergence flag") was inserted as §13c. No information lost, but the sub-heading scheme drifts from the fixed M4 structure. | headings, §13 | 4 | Relabel §13 subsections to match the fixed M4 order (13a per-article, 13b aggregate, 13c prior calendar, 13d upcoming calendar) or fold the divergence flag into 13b. |
| 2.2 Scorecard as a table | §6 is a proper 11-column table (Date/O/H/L/C/RSI2/Trend/Source A/Source B/Final/Validation). §11's daily, weekly and monthly pivot tables are all correctly ordered R3→R2→R1→P→S1→S2→S3, three levels each side, matching the checklist spec exactly. | §6, §11 | 5 | none |
| 2.3 Method steps visible | §4→§5 show observation → normalisation → consensus with the futures-to-spot adjustment stated (−$5); §8 is candle-by-candle; §9 gives regime + overlap/persistence/VOLator/KER; charts are captions only (docx→md conversion drop — not scored per brief). | §4–§9 | 5 | none |
| 3.1 Quantitative claims sourced | Most §1/§12/§14 claims point to a named source or cross-reference a section. Two claims use generic "per market commentary" with no specific outlet named (§12 Demand: "ETF outflows accelerated... per market commentary"; §14 Positioning: "ETF outflows in gold over the prior week per market commentary"). | text | 3 | Name the specific commentary source for both "per market commentary" claims, or drop them. |
| 3.2 Citations exist & contain data | Spot-checked three: Reuters/TD Securities (15 May, named, dated, "-2.6%" figure used consistently in §8's 15-May commentary); USAGOLD (18 May, named, dated, correctly flagged as indicative mid-session); CME GC=F front-month (18 May settle, named, dated) — this one is internally inconsistent: §4 states the settle range as "$4,558.40 high / 4,483.97 low" normalized to "≈4,520", but applying the stated −$5 adjustment (§5) to either the high or the low does not produce 4,520 (4,558.40−5=4,553.40; 4,483.97−5=4,478.97) — the normalized figure does not reconcile to the raw quote plus the report's own stated adjustment. Not treated as fabrication (no fake URL/ticker; CME GC=F is a real, correctly-named instrument), but a genuine internal-consistency gap on one of the three spot-checked sources. | §4, §13a | 3 | Show the arithmetic that turns the CME $4,558.40/$4,483.97 settle range into the "≈4,520" normalized figure, or correct one of the two numbers. |
| 3.3 Calculations transparent | RSI2 shown with the RS = mean gain/mean loss formula and reproduces exactly from the report's own five closes (verified: RSI2(18 May) = 1.6 recomputes from 4685.00→4540.07→4542.49). Pivot formulas stated and reproduce from the report's own (misanchored, see 3.4) H/L/C. Direction score (§21a) shows every weighted contribution explicitly. ATR(14) is used pervasively (§21b) but its ≈70.2 value is never derived from a stated TR series — only asserted. | §6, §11, §9, §21a | 4 | State the ATR(14) derivation (or at minimum the 14-session TR values feeding it), not just the output. |
| 3.4 Numbers reconcile — internally AND against the level file | **Internally** consistent: the 18-May close (4,542.49) is used identically across §1/§3/§4/§6/§21a. **Externally, against the level file, this fails severely and pervasively** — see §2 of this document for the full numeric breakdown. Highlights: the 18-May close is off by $23.66 (basis-adjusted failure threshold $11.98); RSI2 is off by 17.97 points (failure >15); the report's own implied ATR14 (~70.2) is 32.6% below `atr14_full` (failure >25%); and — the largest single defect — **the §11 daily pivot table is anchored on 15 May's H/L/C instead of the D−1 (18 May) session**, so every one of its seven levels fails the ≤0.115×ATR tolerance, by $33 (P) up to $192 (R3). The weekly pivot table (correctly anchored on W/E 15 May) still fails at 5 of 7 levels against the level file (P off $16.33, S1–S3 all fail). The monthly pivot table fails at 6 of 7 levels (correctly flagged single-source-indicative, which is the one thing done right here). | cross-section + level file | 0 | See §2 below. Rebuild §11's daily pivot table from the actual 18 May H/L/C (the correct D−1 session), not 15 May's; rebuild the OHLC and RSI2 rows for 18 May from the leak-free tape; recompute every downstream reference (Trade cards, §15/§16/§18 support/resistance levels) from the corrected figures. |
| 4.1 Pillars conclude | §8, §9, §10, §12, §14 each end in a clear, self-consistent direction label (Exhaustion/reversal-risk; Trending-Down/Bearish; Confirms; per-factor net status; cross-referenced confirmation). | those sections | 5 | none |
| 4.2 Peer/cross-asset interpreted | §10 gives an explicit real-yield/dollar-channel mechanism per counter, distinguishing a yield-led from a growth-fear-led regime — genuinely interpretive, not a correlation list. | §10 | 5 | none |
| 4.3 Synthesis reconciles tensions | §8/§9/§16/§18 explicitly reconcile the short-term Exhaustion read against the medium-term Trending-Down regime; §21a explicitly checks the SHORT conviction against §17 and states no conflict. | §15–§18, §21a | 5 | none |
| 4.4 Calibrated language | §17 is technically one sentence but stacks three hedged clauses ("with a downward bias, with the FOMC April minutes the binary determinant of whether... becomes a tradable low or merely a pause..."); Confidence is explicitly labelled Medium (§3, §18). | §3, §17 | 4 | Tighten §17 to a single unhedged clause per the framework's "no hedge stacking" requirement. |
| (Card construction, scored under C4 per brief) | Trade 1's entry method ("sell on first 30-min close back below the 18 May close... or market on session open if already below") is a conditional/confirmation entry, not the M5-fixed "market at the daily-open anchor" rule. **Trade 3A violates the fixed M5 §5.3a formula on three separate elements**: (i) Entry should be the midpoint of the 50% and 61.8% retracements (= 4,633.23) but the card uses the raw 50% level (4,617) — off by $16.23; (ii) TP1 should be the 38.2% retracement (= 4,584.97, a level between entry and the swing extreme) but the card sets TP1 to the swing low itself (4,480.79 — the full 100%/extreme point, not a 38.2% level); (iii) the stop should be beyond the swing extreme (swing high, 4,753.50) by 0.25×ATR (≈4,771.05) but the card uses the 78.6% retracement + buffer (4,712.75) instead — a materially different, and non-compliant, stop formula. None of this is caught by the static linter (it checks level ordering, not which formula produced the level), so it is not reflected in Card Integrity. | §21b Trade 1, Trade 3A | 2 | See feedback items 8–10 for the exact corrected numbers and rules. |
| 5.1 Data points dated; staleness flagged | Every OHLC session and article carries a date; three of five §6 sessions are explicitly flagged commentary-corroborated-only (not dual-source). | §4, §6, §13, §19 | 5 | none |
| 5.2 Assumptions up front | Futures-to-spot normalisation is stated (−$5, §5) but is internally inconsistent with the report's own §4 footnote ("basis vs spot typical +5/+15 USD") and does not reconcile to the CME row's own numbers (see row 3.2). The daily-open-anchor note is present in both §2 and §20 but is self-contradictory: it says "user override applied" and, in the same clause, "confirms M1 default for this instance" — a value cannot simultaneously be an override and the default. | §21b, §19, §20 | 3 | Correct the futures-basis figure to be internally consistent with the report's own stated typical range; rewrite the anchor note to state plainly whether 00:00 UK is this instance's populated default or a logged departure from it — not both. |
| 5.3 Red flags surfaced | §12/§15 surface the relevant risks (ETF outflows, Hormuz escalation, hawkish Fed repricing); the §13d/e FOMC-minutes collision is carried into the Trade 1 and Trade 3A caveats. | §12, §15, §21b | 5 | none |
| 5.4 Restrictions honoured | **Module codes appear in the report body, in violation of the fixed restriction** ("no module codes (M1..M5)... in the report body"): "confirms M1 default for this instance" (§2, line 17) and "confirms M1 default value for this Gold instance" (§20, line 263) both name M1; "Tilt not consumed by M5 (primary asset only)" (§13b, line 200) names M5. Three occurrences across two sections — this is an explicit, repeated restriction breach, not a one-off slip. Futures (GC=F) otherwise correctly treated as corroboration-only; no un-normalised retail dealer premium found. | whole report — lines 17, 200, 263 | 0 | Remove all three module-code references; restate the anchor note and the tilt-scope note in plain language with no M1–M5 naming. **Triggers the restriction-breach override.** |

## 2. Category 3 external reconciliation — numeric detail (vs `data/levels/XAUUSD_by_date/2026-05-19.csv`)

Tolerances per brief §4 (against `atr14_full` = 104.1686, `atr14_cash` = 81.1886).

**D−1 (18 May) OHLC — report vs `_full`:** O 4,540.07 vs 4,531.52 (Δ8.55, consistent) · H 4,580.00 vs 4,584.27
(Δ4.27, consistent) · L 4,480.79 vs 4,480.30 (Δ0.49, consistent) · **C 4,542.49 vs 4,566.15 (Δ23.66,
FAILURE — threshold 11.98)**. O/H/L are all consistent on the full basis; the close alone fails, by roughly
double the failure threshold.

**RSI2 (18 May):** report 1.6 vs `rsi2_full` 19.57 (Δ17.97, **FAILURE**, threshold >15) · vs `rsi2_cash` 10.44
(Δ8.84, discrepancy band). The value does reproduce exactly from the report's own five stated closes (verified
by hand: RS = mean gain/mean loss over the last two changes = 1.21/72.47 → RSI2 ≈ 1.6) — this is not an
arithmetic error, it is a consequence of the close-price divergence documented above.

**Implied ATR(14) (report's own ≈70.2, from the Trade 1 card's "3×ATR(14) = 210.6" and Trade 3A's "0.25×ATR
buffer" arithmetic):** vs `atr14_full` 104.17 → 32.6% low (**FAILURE**, threshold >25%) · vs `atr14_cash` 81.19
→ 13.5% low (discrepancy band).

**Daily pivots — report vs `_full` (report is anchored on 15 May H/L/C, NOT the D−1 18 May session):** **every
level fails**: R3 4,902.05 vs 4,710.82 (Δ191.23) · R2 4,806.02 vs 4,647.54 (Δ158.48) · R1 4,673.05 vs 4,606.85
(Δ66.20) · P 4,577.02 vs 4,543.57 (Δ33.45) · S1 4,444.05 vs 4,502.88 (Δ58.83) · S2 4,348.02 vs 4,439.60
(Δ91.58) · S3 4,215.05 vs 4,398.91 (Δ183.86). This is a wrong-anchor error, not just noise: recomputing P from
the report's *own* 18-May H/L/C (4,580/4,480.79/4,542.49) gives 4,534.43 — much closer to the level file's
4,543.57 (Δ9.14, discrepancy band, not failure) — confirming the defect is which session was used, not the
formula.

**Weekly pivots — report vs `_full` (correctly anchored on W/E 15 May, the last completed week before D):** R3
4,974.55 vs 4,965.60 (Δ8.95, discrepancy) · R2 4,864.02 vs 4,869.48 (Δ5.46, discrepancy) · R1 4,702.05 vs
4,703.97 (Δ1.92, consistent) · **P 4,591.52 vs 4,607.85 (Δ16.33, FAILURE)** · **S1 4,429.55 vs 4,442.34
(Δ12.79, FAILURE)** · **S2 4,319.02 vs 4,346.22 (Δ27.20, FAILURE)** · **S3 4,157.05 vs 4,180.71 (Δ23.66,
FAILURE)**. The anchor week is right; the underlying weekly H/L/C the report assembled from its own sourced
data (H 4,753.50, L 4,481, C 4,540.07) diverges from the level file's implied weekly H/L/C (H 4,773.37, L
4,511.74, C 4,538.45).

**Monthly pivots — report vs `_full` (flagged single-source-indicative in §11/§19, correctly):** P 4,750.00 vs
4,673.69 (Δ76.31, FAILURE) · R1 5,050.00 vs 4,837.19 (Δ212.81, FAILURE) · R2 5,300.00 vs 5,052.70 (Δ247.30,
FAILURE) · R3 5,650.00 vs 5,216.20 (Δ433.80, FAILURE) · S1 4,450.00 vs 4,458.18 (Δ8.18, discrepancy) · S2
3,900.00 vs 4,294.68 (Δ394.68, FAILURE) · S3 3,600.00 vs 4,079.17 (Δ479.17, FAILURE). The report's own
single-source-indicative flag on this table is fully justified by these deltas — correctly applied
transparency, credited under row 5.1/5.2, even though the values themselves fail Category 3.

## 3. Category roll-up

| # | Category | Max | Level | Multiplier | Points | Justification |
|---|---|---|---|---|---|---|
| 1 | Prompt Adherence | 20 | 3 | 0.65 | 13.00 | As-of date field conflates run-date with as-of-session date; tick unit never formally stated as a Variable. Computed mean rounds to 4, but the restriction-breach override (row 5.4) forces this category down at least one level per the framework's override rule. |
| 2 | Structural Alignment | 20 | 5 | 1.00 | 20.00 | All sections present; §6/§11 tables fully compliant; only a minor §13 sub-lettering drift, no information lost. |
| 3 | Accuracy & Evidence | 25 | 2 | 0.40 | 10.00 | Sourced and internally self-consistent, but external reconciliation against the level file fails pervasively: D−1 close, RSI2, implied ATR14, and — most seriously — every level of the daily pivot table (wrong prior-session anchor) and most of the weekly and monthly pivot tables. |
| 4 | Reasoning & Judgment | 20 | 4 | 0.85 | 17.00 | Strong, mechanism-based pillar conclusions and genuine tension-reconciliation; pulled down by Trade 1's non-compliant conditional entry and Trade 3A's three-way departure from the fixed M5 retracement/stop formula. |
| 5 | Currency & Transparency | 15 | 3 | 0.65 | 9.75 | Data well-dated, red flags surfaced, single-source-indicative flag correctly applied to the monthly pivots — but module codes (M1, M5) appear three times in the report body, an explicit restriction breach, and the futures-basis and anchor-override notes are each internally inconsistent. |

**Total = 13.00 + 20.00 + 10.00 + 17.00 + 9.75 = 69.75 → 70 / 100**

## 4. Band and override

`band = Moderate Trust (60–74)`
`override = restriction_breach` — "M1" appears twice (§2 line 17, §20 line 263) and "M5" once (§13b line 200)
directly in the report body, violating the fixed restriction that module codes (M1..M5) must never be named
in the report body. Per the framework's override rule this caps the band at Moderate Trust (60–74) and
requires Category 1 down at least one rubric level; both are applied above (the natural total of 70 already
falls inside the Moderate band, so the cap does not change the numeric total, only confirms the band and the
Category 1 reduction). No hallucinated-source override: all three spot-checked citations (row 3.2) name real,
dated sources: the CME GC=F normalization arithmetic gap is a computational inconsistency, not a fabricated
source.

## 5. Card Integrity (linter rows, copied verbatim from `qa/gold_regen_qa1/lint_static/2026-05-19.csv`)

| card_id | strategy | flags | dud | Card Integrity |
|---|---|---|---|---|
| 2026-05-19_Trade_1 | Trade 1 — Daily Directional (SHORT, conviction-based) | CLEAN | False | 100 |
| 2026-05-19_Trade_2 | Trade 2 — Pivot, Regime-Aware (TREND_DOWN, SHORT) | CLEAN | False | 100 |
| 2026-05-19_Trade_3A | Trade 3A — Momentum-Pullback SHORT (TREND_DOWN) | CLEAN | False | 100 |

Report-level Card Integrity = mean(100, 100, 100) = **100.00**

(Static level-ordering integrity is clean on all three cards; the defects found in this review — the wrong
pivot anchor feeding Trade 2, and Trade 3A's non-compliant retracement/stop formula — are construction-rule
violations the static linter does not check, so they are captured under Category 3/4 above, not here.)

## 6. Summary fields

```
c1=3
c2=5
c3=2
c4=4
c5=3
total=70
band=Moderate Trust
override=restriction_breach
card_integrity=100.00
n_cards=3
n_duds=0
n_warns=0
```
