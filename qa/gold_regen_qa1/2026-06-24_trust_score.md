# Trust Score — XAUUSD Gold Report, 24 June 2026 (`Gold_Report_24Jun2026.md`)
Run: `gold_regen_qa1` · Reviewer basis: report claims spot/loco-London/continuous → checked against `_full` columns of `data/levels/XAUUSD_by_date/2026-06-24.csv` (last_bar_date 2026-06-23 < D, confirmed leak-free). Weekly/monthly checks use the same file's `w_full_*`/`m_full_*` rows. Tolerances per brief §4, expressed against `atr14_full` = 122.3607.

## 1. Section 7 checklist

| Row | Notes | Evidence | Score (0–5) |
|---|---|---|---|
| 1.1 Variables respected | Asset/spec/currency/tick correct; USDX first counter. Only 5 distinct sources (Investing.com, TradingEconomics, Goldpedia, LiteFinance, TradingView) feed the §4 price-consensus table against the required ≥6 (CoinCodex is sentiment-only, §13a). Anchor named (00:00 UK) but §20's own "override" note obscures rather than discloses the entry-price problem in row 3.4/4-below. | §2, §4, §20 | 3 |
| 1.2 Coverage & currency consistent | All dated content is D−1 or earlier for data; the 24 Jun print is consistently labelled "live/partial/INDICATIVE" everywhere it appears (§1, §4, §6, §19). No unit drift. | whole report | 4 |
| 1.3 Audience & tone | Consistent Senior Commodities Analyst / institutional register throughout, no retail tone. | §1, §18 | 5 |
| 2.1 Sections present & ordered | All 21 top-level sections present in order. Sub-order slip: §13d (Divergence) is printed *before* §13c (News calendar) — spec order is 13a→13b→13c→13d. | headings, §13 | 4 |
| 2.2 Scorecard as a table | §6 OHLC+RSI2 table is a proper 9-column table, correct rows. §11 pivot tables are **not** to spec: the daily table gives only S3-S2-S1-P-R1-R2 (missing R3, 2 levels not 3 on the R side); the weekly table gives only WS2-WS1-P-WR1-WR2 (missing both WS3 and WR3); **the monthly pivot table required by §11 is entirely absent.** | §11 | 2 |
| 2.3 Method steps visible | §4–§5 show observation→normalisation→consensus; §8 is genuine candle-by-candle; §9 shows regime/KER/VOLator reasoning. §7 Charts is an empty heading with no caption/placeholder at all (conversion-drop is not scored per brief, but zero content is noted). | §4–§9 | 4 |
| 3.1 Quantitative claims sourced | §1/§12/§14 figures mostly point to §4/§6/§13; no widespread unsourced claims. | text | 4 |
| 3.2 Citations exist & contain data | Spot-checked Investing.com (§4), Goldman Sachs via TE (§13a), TradingEconomics 19 Jun (§4): each named, dated, used consistently elsewhere. No fabrication found on this sample. | §4, §13a | 5 |
| 3.3 Calculations transparent | RSI2 independently reproduces from the report's own stated closes for 22, 23 and 24 Jun (verified by hand: 39.5, 33.8, 52.2 all match). Daily-pivot arithmetic (P/R1/R2/S1/S2/S3) is internally self-consistent with the report's own stated 23-Jun OHLC. ATR(14)≈$52.7 stated with no derivation and is later shown (row 3.4) to be badly wrong. | §6, §11 | 3 |
| 3.4 Numbers reconcile — incl. vs level file | Multiple hard failures against `_full` tolerances: **23-Jun Close** 4,129.07 vs level file 4,110.32, diff 18.75 > 14.07 (0.115×ATR) → FAILURE. **ATR(14)** stated ≈$52.7 vs level file 122.3607 (full) / 102.8557 (cash), >55% low either way → FAILURE (>25% relative). **Daily S1/S2/S3** (4,093.65 / 4,058.22 / 4,007.05) vs level file (4,067.9967 / 4,025.6733 / 3,960.4967): diffs 25.65 / 32.55 / 46.55, all > 14.07 → FAILURE on all three, traceable to the bad 23-Jun Low/Close feeding the pivot formula. **5-day swing high** used for the Trade 1 stop (4,330.39, taken from the report's own 18-Jun High) vs level file `swing_high_5d_full` 4,382.22 — diff 51.83, well outside tolerance. Internal break: Trade 1 **MARKET entry (4,198.66) ≠ D−1 close** (report's own 4,129.07, and the level file's 4,110.32/4,111.57) — this breaks the static-integrity rule that a MARKET entry equals the D−1 close (brief §3). Against this, Open (diff 0.02) and High (diff 2.35) reconcile cleanly to `_full`, and **all five weekly pivot levels reconcile within tolerance** (largest diff 3.75, all ≤ 0.04×ATR). | cross-section + level file | 1 |
| 4.1 Pillars conclude | §8/§9/§10/§12/§14 each end in a direction label consistent with their content. | those sections | 4 |
| 4.2 Peer/cross-asset interpreted | §10 states mechanism (opportunity cost via USDX, risk-on rotation via equities), not a bare correlation list. | §10 | 4 |
| 4.3 Synthesis reconciles tensions | §15/§16/§18 address the corrective-bounce-vs-downtrend tension and the KER-choppy-vs-TREND_DOWN tension without averaging them away. | §15–§18 | 4 |
| 4.4 Calibrated language | §17 is one sentence with conditional hedge ("unless a soft PCE..."), not stacked hedges. H/M/L confidence stated (§3 Medium). | §3, §17 | 4 |
| — Card construction (feeds C4 per brief) | Trade 1's stop is built on the wrong ATR and the wrong 5-day swing high (row 3.4); TP2 off by $0.01 vs its own formula (immaterial). Trade 2 follows neither the RANGE nor the TREND_DOWN M5 template (regime is stated TREND_DOWN, but entry sits exactly at the weekly pivot rather than the TREND offset formula P−0.10×(P−S1)); no R, no TP3, no runner rule, no management text stated at all. Trade 3A is built as a breakout-stop at the prior low, not as the required 57.5%-retracement-of-a-qualifying-swing construction — no swing endpoints logged, no 38.2%/0%/100% levels, no TP3. | cards JSON, §21b | 1 |
| 5.1 Data dated; staleness flagged | Every price/article carries a date; the only stale/in-progress datum (24-Jun print) is flagged INDICATIVE consistently. | §4, §6, §13, §19 | 5 |
| 5.2 Assumptions up front | §19/§20 state method (weighted median), tolerance, and the single-source-indicative propagation. No futures-to-spot normalisation needed (report uses only spot-labelled sources). The anchor "override" note in §20 states an anchor *time* (00:00 UK, unchanged) rather than disclosing the real problem — that the MARKET entry price used is not the D−1 close — so the actual non-conformance (row 3.4) is not the thing that gets logged. | §19, §20 | 3 |
| 5.3 Red flags surfaced | ETF outflows, Goldman cut, Fed hawkish path all elevated to §12/§15, not buried. | §12, §15 | 4 |
| 5.4 Restrictions honoured | **Breach**: §20 contains the bracketed module-variable name "[daily-open anchor]" verbatim in the report body, which brief §2 row 5.4 explicitly prohibits ("no bracketed variable names, no module codes"). §19 also references "the framework's no-synthesis discipline" (a softer, generic self-reference). No synthesised/interpolated OHLC found; futures used corroboration-only. | whole report | 0 |

## 2. Category roll-up

| Category | Rows averaged | Raw avg | Rubric level | Multiplier | Points | Justification |
|---|---|---|---|---|---|---|
| C1 Prompt adherence | 1.1, 1.2, 1.3 | (3+4+5)/3 = 4.0 → **override: −1 level (restriction breach)** | **3** | 0.65 | 13.0 | Variables mostly respected; source count short of ≥6; C1 reduced one level for the 5.4 restriction breach. |
| C2 Structure | 2.1, 2.2, 2.3 | (4+2+4)/3 = 3.33 | **3** | 0.65 | 13.0 | All sections present/ordered bar one sub-swap; §11 pivot tables non-conforming and monthly pivots missing entirely. |
| C3 Accuracy & evidence | 3.1–3.4 | (4+5+3+1)/4 = 3.25 | **1** | 0.20 | 5.0 | Citations and RSI2 arithmetic are sound, but Close, ATR(14), three daily pivot levels and the 5-day swing high all breach tolerance against the level file, and the MARKET entry doesn't equal the D−1 close. Card construction (below) reinforces this. |
| C4 Reasoning & judgment | 4.1–4.4 + card construction | narrative (4+4+4+4)/4=4.0, card construction = 1 → weighted down per brief ("card construction ALSO scored under C4") | **2** | 0.40 | 8.0 | Narrative synthesis is genuinely good, but 2 of 3 cards materially depart from their specified M5 construction rules and the third (Trade 1) inherits bad inputs. |
| C5 Currency & transparency | 5.1–5.4 | (5+3+4+0)/4 = 3.0 | **3** | 0.65 | 9.8 | Dating/staleness/red-flags are strong; the open restriction breach (5.4) and the mis-targeted "override" disclosure (5.2) pull the category down. |

## 3. Total, band, override

**Total = 13.0 + 13.0 + 5.0 + 8.0 + 9.8 = 48.8 → 49 / 100**
**Band: Low Trust (40–59).**
**Override check: Restriction breach — TRIGGERED** (bracketed "[daily-open anchor]" in §20 report body). Per framework §6 this caps the band at Moderate Trust (60–74) and requires C1 down ≥1 level — the cap is non-binding here since the computed total (49) already falls below the Moderate range; C1's one-level reduction is applied above. No hallucinated-source override — three-citation spot-check found no fabrication.

## 4. Card Integrity (from `qa/gold_regen_qa1/lint_static/2026-06-24.csv`, copied verbatim — leak-free, static mode)

| card_id | strategy | flags | dud | Card Integrity |
|---|---|---|---|---|
| 2026-06-24_Trade_1 | Trade 1 - Daily Directional (SHORT, TREND_DOWN regime) | CLEAN | False | 100 |
| 2026-06-24_Trade_2 | Trade 2 - Pivot (regime-aware, INDICATIVE) | CLEAN | False | 100 |
| 2026-06-24_Trade_3A | Trade 3A - Momentum-Pullback (SHORT) | CLEAN | False | 100 |

Report-level Card Integrity = mean(100, 100, 100) = **100**. n_cards=3, n_duds=0, n_warns=0.
(Note: the static linter checks stop-side/TP-order/zero-R/etc., not methodology-family conformance or market-derived checks such as "MARKET entry = D−1 close" or ATR-based stop sizing — those failures are captured under C3/C4 above, not in Card Integrity, per the brief's instruction to copy the linter output verbatim.)

## Summary line
c1=3 c2=3 c3=1 c4=2 c5=3 total=49 band=Low_Trust override=restriction_breach card_integrity=100 n_cards=3 n_duds=0 n_warns=0
