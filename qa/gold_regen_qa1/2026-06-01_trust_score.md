# Trust Score — XAUUSD Gold Report, 1 June 2026
Run: gold_regen_qa1 · Report: `reports/md/Gold_Report_01Jun2026.md` · Level file: `data/levels/XAUUSD_by_date/2026-06-01.csv` (last_bar_date 2026-05-29 < 2026-06-01, leak-free, verified)

## 1. Section 7 checklist

| Row | Notes | Evidence | Score |
|---|---|---|---|
| 1.1 Variables respected | Asset = XAU/USD spot, GC=F used corroboration-only (§2, §5) — correct. USDX listed first in §10 cross-asset table — correct. As-of = 29 May close (D-1), lookback 5d short / 25d medium stated and used (§2, §9) — correct. USD/oz throughout; tick $0.01 stated and used consistently on all cards. 6 distinct named sources in §4 (Investing.com, Bloomberg, Trading Economics, LiteFinance, CME GC=F, Yahoo) — meets the ≥6 floor exactly, no margin. | §2, §4, §9, §10, §21b | 4 |
| 1.2 Coverage & currency consistent | §11/§19 monthly pivots are computed from "April H 4,889.70 / L 4,500.85 / C 4,614.95" and labelled §19 "CORROBORATED" — but the prior completed month relative to D=1 Jun is **May**, not April (level file `m_full_period`=2026-05). This is a coverage-period drift that also drives a large external accuracy failure (see 3.4) and propagates into Card 3B's TP2. | §11, §19, level file | 2 |
| 1.3 Audience & tone | Institutional Commodities-desk register throughout; no retail tone; closing forward-test/no-advice disclaimer appropriate. | §1, §18, closing line | 5 |
| 2.1 Sections present & ordered | All 21 numbered sections present in order incl. 21a–d. §13c and §13d are merged into one "13c/d" block instead of two labelled subsections — minor, no information lost. | headings | 4 |
| 2.2 Scorecard as table | §6 is a real table but uses Date/O/H/L/C/RSI2/Validation columns — the required Source A / Source B columns are missing (sourcing is prose above the table, not columns). §11 pivot tables are correctly ordered R3→P→S3, 3-a-side, for daily/weekly/monthly. | §6, §11 | 3 |
| 2.3 Method steps visible | §4–§5 show observation→normalisation→consensus with the futures-to-spot adjustment stated ("de-based," ~$50 vs spot); §8 is genuine candle-by-candle; §9 states persistence (50d/200d) and VOLator/Kaufman; §7 gives narrative captions in place of dropped images (per brief, not penalised). | §4–§9 | 4 |
| 3.1 Quantitative claims sourced | Most §1/§12/§14 figures point to §4/§6/§13. Several unsourced: "CME FedWatch ~50% by some reads" (§12), "speculative length was flushed" (§14), CNBC central-bank-selling claim dated only "April" in §12 vs no date at all in §13a. | §12, §14 | 3 |
| 3.2 Citations exist & contain data | Spot-checked 3: Investing.com (29 May 16:00 ET, 4,539.27 — reused identically in §6/§21b), Bloomberg XAU (29 May, 4,540.26 — reused in §5), Trading Economics (29 May, 4,541.41 — reused in §5). All named, dated, internally consistent. No fabrication found on this sample. | §4, §5 | 5 |
| 3.3 Calculations transparent | RSI2 reproduces exactly from the report's own stated closes for 27 May (19.6) and 28 May (66.4); daily pivot arithmetic P=(H+L+C)/3 etc. reproduces exactly from the stated 29-May H/L/C; §21a score (+0.36) reproduces exactly as Σ(signal×weight). But ATR14 itself is never printed as a number anywhere in the report body (only invoked conceptually, e.g. "3×ATR(14) price cap"), and KER is given a value but not its EMA-3 smoothing detail. | §6, §11, §9, §21a | 3 |
| 3.4 Numbers reconcile (incl. level file) | Internally: D-1 close ($4,539/4,539.27) identical across §1/§3/§4/§6/§21b. Externally vs level file (`_full`, matching the report's "loco London, continuous spot" basis): 29-May O/H/L/C all within tolerance (Δopen $4.16, Δhigh $0.10, Δlow $0.42, Δclose $0.72 — all ≤ consistent thresholds); daily pivots all within ≤$1.3 of `d_full_*` (consistent). **Weekly pivots fail badly**: report's assumed prior-week H/L ($4,760/$4,400) vs the level-file-implied actual weekly H/L ($4,595.21/$4,366.35, back-solved from `w_full_S1`/`w_full_R1`) — every weekly R/S level in §11 is off by $33–230, all past the 0.115×ATR (~$11.8) failure line. This is correctly flagged single-source-indicative in §19, so not penalised as fabrication, but it is a large recorded discrepancy. **Monthly pivots fail badly and are mislabelled reliable**: report's April H/L/C (4,889.70/4,500.85/4,614.95) vs the level-file-implied actual May H/L/C (4,773.37/4,366.35/4,539.99, back-solved from `m_full_*`) — every monthly R/S/P level in §11 is off by $65–130 (P alone off by $108.60), all past the 0.115×ATR failure line, and §19 asserts these are "CORROBORATED" with no caveat. | §11, §19, level file | 1 |
| 4.1 Pillars conclude | §8, §9, §10, §12 each end in an explicit direction/status label. §14 (Macro) lists rates/inflation/liquidity/positioning/geopolitics each with an implicit lean but no single wrap-up label. | §8–§14 | 4 |
| 4.2 Peer/cross-asset interpreted | §10 gives a stated mechanism per counter (USDX cost-of-holding, S&P risk-on/haven substitution, DAX confirmation, Silver beta) — not a bare correlation list. | §10 | 5 |
| 4.3 Synthesis reconciles tensions | §9 explicitly states Kaufman/medium-term takes precedence over the short-term reclaim; §15/16/18 and §21a all explicitly flag the LONG-conviction-vs-bearish-medium-term-structure conflict rather than averaging it away. | §9, §15–§18, §21a | 5 |
| 4.4 Calibrated language | §17 is exactly one sentence, no hedge stacking. Confidence stated (Medium-High) in §3/§18; conditional language used appropriately in §13d/§16. | §3, §17 | 5 |
| **Card construction (feeds C4 per protocol)** | Trade 1: stop ($4,486) sits essentially *at* S1 ($4,486.86/§11) with no 0.25×ATR buffer applied — rule requires stop = nearest S/R − 0.25×ATR (≈ $4,462 using the level file's S1). Trade 2 (RANGE-type, "buy pullback to pivot"): TP1 is stated $4,565 but the fixed rule (TP1 = entry ± 1R for Trade 1 and RANGE Trade 2) requires TP1 = $4,505 + $45 = $4,550 — a $15 rule violation. Trade 3 labelled "fork 3B" but built as an ad-hoc stop-entry breakout above R1; it matches neither 3B's defined limit-in-range-tier logic (11.4–21.4%/78.6–88.6% of the 25-day range, which — using `swing_low_25d_full`/`swing_high_25d_full` — would sit near $4,686–$4,727, not $4,596) nor 3C's 25-day-boundary-break-plus-buffer logic; its TP2 is additionally anchored to the mis-sourced monthly pivot from row 3.4 ($4,668 vs the correct $4,559.90). | §21b, level file | 2 |
| 5.1 Data points dated; staleness flagged | Most data dated; single-source intraday H/L explicitly flagged indicative in §6/§19. Some macro claims (CNBC, CME FedWatch) lack a precise date. | §6, §13, §19 | 4 |
| 5.2 Assumptions up front | Futures-to-spot normalisation stated with its size (§5). Anchor override is stated in the report body (§2 "override of standard reset") and in §20 — but per the M1 module rule the override must also carry "the same converted time on the card"; none of the three cards states a clock time at all (confirmed against the card-transcription notes, which had to *assume* 02:00 because no time is printed on any card). | §21b, §19, §20 | 3 |
| 5.3 Red flags surfaced | §12/§15 carry the standing risks. §13d's event collisions (Powell/PMI, JOLTS, ADP/Beige Book, NFP) are discussed at report level (§13d, §18) but are not carried into any of the three cards' confluence/invalidation text as caveats. | §12, §15, §21b | 3 |
| 5.4 Restrictions honoured | No bracketed variable names, module codes, or framework name found in the body. Futures kept corroboration-only and de-based consistently. **But** the monthly H/L/C figures used in §11 carry no citation anywhere in §4/§13 and are nonetheless declared "CORROBORATED" in §19 — an uncited, in fact incorrect, figure presented as sourced/corroborated. This trips the 5.4 restriction "no synthesised or interpolated price presented as sourced." | §11, §19, whole report | 2 |

## 2. Category roll-up

| Cat | Mean of rows | Level (rounded) | Multiplier | Max | Points | Justification |
|---|---|---|---|---|---|---|
| 1 Prompt adherence | (4+2+5)/3=3.67→4, **override drops 1 level** | **3** | 0.65 | 20 | 13.00 | Variables and tone strong; monthly-period drift (1.2) and the restriction-breach override both apply. |
| 2 Structure | (4+3+4)/3=3.67 | **4** | 0.85 | 20 | 17.00 | All sections present; scorecard table missing two required columns. |
| 3 Accuracy & evidence | (3+5+3+1)/4=3.0 | **3** | 0.65 | 25 | 16.25 | Daily OHLC/pivots and RSI2 reconcile against the level file; weekly and (unflagged) monthly pivots both fail the tolerance badly. |
| 4 Reasoning & judgment | (4+5+5+5+2)/5=4.2→4, weighed down by systematic card-construction defects across all 3 cards | **3** | 0.65 | 20 | 13.00 | Pillar synthesis and cross-asset reasoning are strong; all three trade cards carry a real M5 construction-rule violation. |
| 5 Currency & transparency | (4+3+3+2)/4=3.0 | **3** | 0.65 | 15 | 9.75 | Dating and assumption disclosure mostly present; anchor time missing from the cards; monthly-pivot mislabelling breaches the no-synthesis-presented-as-sourced restriction. |

**Total = 13.00 + 17.00 + 16.25 + 13.00 + 9.75 = 69** (rounded to nearest whole number)

## 3. Total, band, override

```
c1=3
c2=4
c3=3
c4=3
c5=3
total=69
band=Moderate Trust (60-74)
override=restriction_breach
card_integrity=100
n_cards=3
n_duds=0
n_warns=0
```

**Override detail:** §11/§19 present the monthly floor pivots as "CORROBORATED" although the underlying H/L/C are uncited anywhere in the report and are in fact drawn from the wrong calendar month (April instead of the completed-May period the level file uses as `m_full_period`). Presenting an unsourced, materially wrong figure as corroborated breaches the 5.4 restriction "no synthesised or interpolated price presented as sourced." Per framework §6, this caps the band at Moderate Trust and drops Category 1 by at least one rubric level (applied above: 3.67→4 dropped to 3). The natural weighted total (69) already falls inside the Moderate Trust band, so the override does not further compress the score — it is recorded because the breach condition is independently met.

No hallucinated-source override: the three spot-checked citations (3.2) are named, dated, and internally consistent; no fabricated source, URL, or dataset name was found.

## 4. Card Integrity (linter rows, copied verbatim from `qa/gold_regen_qa1/lint_static/2026-06-01.csv`)

| card_id | strategy | flags | dud | Card Integrity |
|---|---|---|---|---|
| 2026-06-01_Trade_1 | Trade 1 — Directional (tactical long) | CLEAN | False | 100 |
| 2026-06-01_Trade_2 | Trade 2 — Regime-aware pivot | CLEAN | False | 100 |
| 2026-06-01_Trade_3B | Trade 3 — Regime-driven complex (fork 3B: range/breakout) | CLEAN | False | 100 |

Report-level Card Integrity = mean over non-suppressed cards = **100** (n_cards=3, n_duds=0, n_warns=0). Card Integrity is a purely static, leak-free score and does not reflect the level-construction rule violations noted under "Card construction" in §1 above — those are M5-rule breaches the static linter does not check (buffer-off-S/R, exact-R TP formula, wrong sub-strategy template), and are scored instead under Category 4 and detailed in the feedback file.
