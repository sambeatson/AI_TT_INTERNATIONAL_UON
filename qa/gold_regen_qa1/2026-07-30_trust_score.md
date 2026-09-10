# Trust Score — XAUUSD Gold Report, 30 Jul 2026 (`Gold_Report_30-Jul-2026.md`)
Run: gold_regen_qa1 · Reviewer basis: report claims spot/loco-London continuous quoting (§2, §3: "Spot, loco London") → checked primarily against the `_full` columns of `data/levels/XAUUSD_by_date/2026-07-30.csv` (`last_bar_date=2026-07-29 < 2026-07-30`, confirmed leak-free); `_cash` shown alongside where it materially changes the read. `atr14_full`=84.77, `atr14_cash`=72.5864.

## 1. Section 7 checklist

| Row | Reviewer notes | Evidence observed | Score (0–5) |
|---|---|---|---|
| 1.1 Variables respected | Asset = XAU/USD spot loco London, GC=F corroboration-only ✓; USDX first counter row in §10 ✓; as-of session named as 29 Jul, lookback 5/25 ✓; USD/oz throughout ✓; 6 named sources ✓. Two gaps: (a) tick size/name is never stated in §2 (only recoverable by back-solving the cards' "X ticks" notes, which imply $0.01 used consistently but unstated); (b) the anchor override is disclosed (§2, §20, on the Trade 1 card) but §2's footnote cross-references "(see §19)" — §19 contains no anchor content at all, it is in §20 — and the language ("requested for the 30-Jul session") reads as an authorised per-session choice rather than the module's required "logged non-conformance" framing. | §2, §19 vs §20, §21b | 3 |
| 1.2 Coverage & currency consistent | No USD/oz unit drift anywhere. Dates are D−1-or-earlier throughout, but see 3.4/3.2: the daily-pivot header is labelled "28 Jul" (D−2) rather than 29 Jul (D−1, the report's own as-of session), and Investing.com's own quoted "prev close" in §4 (4,076.80) does not match the same source's 29-Jul close as printed in §6 (4,045.17). | §6 vs §11 header, §4 vs §6 | 4 |
| 1.3 Audience & tone | Consistently institutional register ("Senior Commodities Analyst — Precious Metals"); no retail tone anywhere. | header, §1, §18 | 5 |
| 2.1 Sections present & ordered | All of §1–§21 present in order, including §13a–d and §21a–d. §7's five chart subsections (7.1–7.5) carry only headings — no caption, placeholder text, or even a one-line description under any of them (more than the "image dropped in .md conversion" case the brief excuses; there is no textual evidence at all that a chart existed). | headings, §7 | 4 |
| 2.2 Scorecard as table | §6 is a proper 10-column table ✓. §11's three pivot tables (daily/weekly/monthly) each print 5 levels/side (R5…P…S5, 11 rows) instead of the specified 3-levels/side R3→P→S3 format — a systematic deviation across all three tables. | §11 | 2 |
| 2.3 Method steps visible | §4→§5 show observation → recency-weighting/down-weighting → weighted-median consensus, with the no-blending futures policy stated. §8 is candle-by-candle. §9 states overlap/persistence/VOLator/KER numerically. §7 chart evidence is empty (see 2.1). | §4–§9 | 4 |
| 3.1 Quantitative claims sourced | Most §1/§12/§14 figures point to §4/§6/§10/§13; §12's "Source: Fed statement; TradingEconomics rates" is generic (no date/page) but not fabricated. | text | 3 |
| 3.2 Citations exist & contain data | Spot-checked Investing.com, Capital.com, TradingEconomics (Scorecard-adjacent, Deep-Dive, Risk-adjacent uses). **Investing.com fails**: §4's Price Evidence row for Investing.com (30 Jul intraday) states "Prev close 4,076.80" — Investing.com's own quoted previous (29 Jul) close. §6 attributes the 29 Jul close as **4,045.17**, sourced jointly to Investing.com (Source A) and TradingEconomics (Source B), "Validation: CORROBORATED." The same source, same data point (29-Jul close), is given two figures $31.63 apart in two sections of the same report. Per brief §1/framework 3.2 this is a self-contradictory citation → **triggers the hallucinated-source override.** Capital.com and TradingEconomics citations elsewhere are internally consistent. | §4 vs §6 | 0 |
| 3.3 Calculations transparent | RSI2 reproduces exactly from the report's own five stated closes for 27/28/29 Jul (verified: two consecutive gains → RS→∞ → RSI2=100 on 29 Jul; RS=1.65/8.70→RSI2=15.9 on 28 Jul; both losses→RSI2=0 on 27 Jul). **But ATR(14) is never stated anywhere in the report** despite being invoked repeatedly in the cards ("0.25×ATR buffer", "3×ATR", "ATR-stop within cap") — a reviewer cannot check any stop/target derivation against a number the report itself never prints. | §6 (RSI2 OK); whole report (ATR never shown) | 1 |
| 3.4 Numbers reconcile — incl. level file | Internally: the Investing.com self-contradiction above (3.2); §11's daily-pivot header reads "(prior session 28 Jul)" though the report's own as-of session is 29 Jul (§2) — reproducing the floor-pivot formula on the report's own 28-Jul H/L/C (4,107.25/4,041.98/4,028.40, §6) gives P=4,059.21, exactly the printed value, confirming the wrong (stale) session was used and labelled as such, openly but incorrectly. **Externally, against the leak-free level file (claimed `_full` basis): D-1 Open 4,047.65 vs 4,027.87 (Δ19.78=0.233×ATR, FAIL); High 4,082.45 vs 4,116.60 (Δ-34.15=-0.403×ATR, FAIL); Low 4,021.56 vs 3,995.94 (Δ25.62=0.302×ATR, FAIL); Close 4,045.17 vs 4,066.26 (Δ-21.09=-0.249×ATR, FAIL — though it lands within tolerance of `_cash` 4,044.85, Δ0.32, despite the report claiming a loco-London/`_full` basis).** Daily pivot P happens to land within tolerance of `d_full_P` (Δ-0.39) despite the wrong-session label, but R1/S1/R2/S2/R3/S3 all FAIL against both bases (Δ 0.10–1.21×ATR). Weekly P/R1 FAIL both bases (Δ0.16–0.28×ATR); weekly S1 is within tolerance of `_full` only. Monthly P FAILS by 1.10×ATR (full) / 1.12×ATR (cash); monthly R1 FAILS; **monthly S1 (4,135.30) misses `m_full_S1` (3,785.16) by $350.14 = 4.13×ATR — the largest single miss found.** This is a comprehensive, not isolated, reconciliation failure. | §6, §11 vs level file | 0 |
| 4.1 Each pillar concludes | §8 "Judgement label: Indecision — reversal risk" ✓; §9 "Preferred protocol: Reduced conviction..." ✓; §10 "Aggregate cross-asset: MIXED" ✓. §12 and §14 are considerations lists that do not close with an explicit direction label the way §8–§10 do. | §8–§10 strong, §12/§14 weaker | 3 |
| 4.2 Peer/cross-asset interpreted | §10 states a mechanism per counter (USDX opportunity-cost/real-yield channel, equity risk-off vs. real-yield dominance, silver's PM-pair read) rather than a bare correlation list. | §10 | 4 |
| 4.3 Synthesis reconciles tensions | §9 explicitly resolves KER vs. regime ("KER takes precedence... hence TRANSITION not TREND_DOWN"); §15/§16/§18 hold the bearish-macro-vs-haven/silver tension open rather than averaging it; §21a states the §17-vs-conviction alignment explicitly. | §9, §15–§18, §21a | 4 |
| 4.4 Calibrated language / card construction | Narrative language is calibrated (Medium confidence stated, "likely"/"tilted... not one-way"). Card construction (folded into C4 per protocol) shows real M5-rule breaks on all three live cards: **Trade 1** — stop ($4,077.45) implies a buffer of only ~$1.01 beyond the nearest S/R (daily R1, $4,076.44), not the required 0.25×ATR (≈$21.19 on `atr14_full`, ≈$18.15 on `atr14_cash` — the stop should sit ≈$4,094.6–4,097.6, not $4,077.45); the card's own Confluences row cites "SL near 5-day swing high $4,133.00" which is $55.55 from the actual stop used — the stated anchor and the computed stop don't match each other. **Trade 2** — TP3/runner is "toward weekly P $4,054.17," which sits *above* both entry ($3,943.55) and stop ($3,995.80) on a SHORT — a directionally invalid runner target (confirmed WARN_TP3_ORDER in the linter). **Trade 3C** — the "3,960–4,318" range used for the measured-move width ($358) has no support at either basis: `swing_high_25d_full`=4,202.71 (Δ115.29) and `swing_high_25d_cash`=4,180.52 (Δ137.48), both 5.7–6.8× the OHL discrepancy tolerance — the true full-basis width is $259.63 and cash-basis $216.62, so both TP1 and TP2 are inflated by roughly $100+ from an unsupported boundary. | §21b (all three cards) | 1 |
| 5.1 Data dated; staleness flagged | Every price/article carries a date; §19 flags 23–27 Jul intraday H/L as indicative. But the daily-pivot's actual staleness (computed from D−2, not D−1 as the report's own as-of rule requires) is never flagged as stale anywhere — it is presented as a plain, undisputed label. | §4, §6, §13, §19; gap at §11 | 3 |
| 5.2 Assumptions up front | Anchor override stated with baseline (00:00 UK) and converted time on the Trade 1 card; no-blending futures policy stated; pivot single-source-indicative flag stated in §19/§20/cards. | §2, §19, §20, §21b | 4 |
| 5.3 Red flags surfaced | §12/§15 risks substantive (Fed dissents, Hormuz, GDP collision); §13d's GDP event is carried into card caveats (Trade 3C "size down accordingly"; Trade 1 pivots-indicative caveat). | §12, §15, §21b | 4 |
| 5.4 Restrictions honoured | No bracketed variable names, module codes (M1–M5), or framework name found anywhere in the body; instrument common names used throughout. | whole report | 5 |

## 2. Category roll-up

| Cat | Level (mean of rows, rounded) | Multiplier | Max | Points | Justification |
|---|---|---|---|---|---|
| C1 Prompt adherence | 4 | 0.85 | 20 | 17.00 | Variables respected; tick size unstated and the anchor-override disclosure has a broken cross-reference (§19 vs §20) and soft "requested" framing rather than explicit non-conformance language |
| C2 Structure | 3 | 0.65 | 20 | 13.00 | All 21 sections present/ordered; pivot tables print 5 levels/side in all three tables instead of the specified 3; §7 charts carry no evidence at all (headings only) |
| C3 Accuracy & evidence | **0** | 0.00 | 25 | 0.00 | Hallucinated-source override (Investing.com's own "prev close" 4,076.80 vs its own §6 close 4,045.17); independently supported by comprehensive external reconciliation failure — D-1 O/H/L all FAIL, most daily/weekly/monthly pivots FAIL (up to 4.13×ATR on monthly S1), ATR never stated |
| C4 Reasoning & judgment | 3 | 0.65 | 20 | 13.00 | Pillar reasoning and cross-asset/synthesis rows are strong (≈4); card construction is a severe outlier across all three live cards (Trade 1 stop-buffer mismatch, Trade 2 inverted runner target, Trade 3C unsupported range width) |
| C5 Currency & transparency | 4 | 0.85 | 15 | 12.75 | Dating, assumption disclosure and red-flag surfacing are solid; the one gap is the unflagged staleness of the wrong-session daily pivot |

## 3. Total, band, override

```
total = round(17.00+13.00+0.00+13.00+12.75) = 56
band  = Low Trust (40-59)
override = hallucinated_source   (Investing.com's own quoted "prev close" 4,076.80 in §4 contradicts the same
           source's 29-Jul close of 4,045.17 as printed in §6 — a self-contradictory citation per brief §1 /
           framework 3.2, which caps the band at Low Trust and sets C3 = 0)
```
Note: the natural point total (56) already falls inside the override's Low-Trust cap (40–59) — the two agree,
and the override is still the binding reason for the band, not a coincidence of the arithmetic. Even setting
the override aside, the external reconciliation failures documented under 3.4 (systematic, multi-timeframe,
up to 4.13×ATR) are severe enough on their own to keep C3 at or near 0.

## 4. Card Integrity (from `qa/gold_regen_qa1/lint_static/2026-07-30.csv`, copied verbatim)

| card_id | strategy | flags | dud | integrity (100−40·#DUD−10·#WARN) |
|---|---|---|---|---|
| 2026-07-30_Trade_1 | Trade 1 — Daily Directional (SHORT) | CLEAN | False | 100 |
| 2026-07-30_Trade_2 | Trade 2 — Pivot, TRANSITION (breakout-side only) | WARN_TP3_ORDER | False | 90 |
| 2026-07-30_Trade_3C | Trade 3C — Momentum-Breakout (TRANSITION, downside) | UNPRICED | True | 60 |

Report-level Card Integrity = mean over non-suppressed cards (all 3; none suppressed) = mean(100, 90, 60) = **83.33**.

Note for the regeneration agent: the static linter only checks stop/TP side, order and pricing completeness,
so Trade 1 shows CLEAN despite the semantic stop-buffer/anchor mismatch documented under row 4.4 above, and
Trade 3C's UNPRICED/DUD flag is a direct, unavoidable consequence of correctly leaving `entry=null` under the
no-inference rule while the card awaits its breakout confirmation — not a pricing error. Trade 2's
WARN_TP3_ORDER is genuine: the runner target is on the wrong side of both entry and stop. None of the four
Category-3/4 semantic defects (Investing.com self-contradiction, wrong-session daily pivot, Trade 1 buffer
mismatch, Trade 3C's unsupported range width) are visible to the static linter and must be fixed independently
of Card Integrity.

## 5. Explicit score lines

c1=4
c2=3
c3=0
c4=3
c5=4
total=56
band=Low Trust (40-59)
override=hallucinated_source
card_integrity=83.33
n_cards=3
n_duds=1
n_warns=1
