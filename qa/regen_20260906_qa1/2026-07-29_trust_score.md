# Trust Score — 2026-07-29 — SP500_Report_29Jul2026.md

Run: `regen_20260906_qa1` · D = 2026-07-29 · Asset = US500 · D-1 = 2026-07-28
Basis for accuracy checks: `data/slices/US500/US500_upto_2026-07-28.csv` via `engine/qa_slice_stats.py`
(cash session 16:30–23:00 broker = 09:30–16:00 ET). Tolerance applied per reviewer brief §4:
|Δ| ≤ 3 pts on a close, ≤ 8 pts on an open/high/low.

## 1. Section 7 checklist

| Item | Reviewer notes | Evidence observed | Score 0–5 | Action required |
|---|---|---|---|---|
| 1.1 All Variables visibly respected | Asset is the S&P 500 cash index, explicitly distinguished from futures and from CFD basis; counters USDX · VIX · DAX 40 with USDX first; as-of = NY close of D-1 (28 Jul), tz America/New_York; lookback 5 sessions (execution) + 25 (regime); unit index points / USD. Six source rows in §4 (one excluded as CFD; FRED appears twice, so 5 distinct usable providers). Daily-open anchor stated as 07:00 UK. Gaps: tick size 0.01 never stated in §2; the 07:00 UK anchor is stated only in §20, not on the cards. | Header; §2 table; §4; §10; §20 "Daily-open anchor confirmed at 07:00 UK" | 4 | Add tick size to §2; restate the anchor on each card. |
| 1.2 Coverage period and currency consistent | Currency/unit consistent throughout (index points / USD, no drift). Coverage drift is material: §11 daily pivots are built from the **27 Jul** session ("prior session 27 Jul") although the report's own as-of session is 28 Jul, and 28 Jul H/L (7452.02/7382.64) are available in §4/§6 and match the slice within 2 pts. §1 calls 7,581 "its early-June record" and §21b 3C calls it the "June record high", while §9 dates the same 7,581 high to **15 Jul**; the slice puts the 25-session high at 7582.80 on 2026-07-15. §12 puts WTI in the "low-$80s" while §13c has oil "to ~$100" on 24 Jul. | §11 header; §1 vs §9 vs §21b confluences; §12 vs §13c | 2 | Rebuild §11 from the 28 Jul session; fix the record-high date; reconcile the oil narrative. |
| 1.3 Audience and tone | Registered as "Senior US Equity Strategist · Trading and risk review (forward-test)". Language is institutional throughout (regime, persistence, overlap, R-multiples); no retail promotion, no advice framing; §18 is a judgement with three numbered reasons. | Header; §1; §18 | 5 | None. |
| 2.1 All sections present and correctly ordered | §1–§21 all present and in order, including §13a per-article table, §13b aggregate with numeric tilt (−0.08), §13c previous-period calendar, §13d upcoming calendar, and §21a/§21b/§21c/§21d. §17 is exactly one sentence. §21d carries the limitations boilerplate. | Headings throughout | 5 | None. |
| 2.2 Scorecard rendered as a table | §6 is a table with the full column set Date/O/H/L/C/RSI2/Trend/Src A/Src B/Final/Validation. §11 daily pivots are a table ordered top-down R5→S5, but carry 5 tiers plus 1.5 tiers per side rather than the specified R3→P→S3; the **weekly and monthly pivots are prose, not tables**, and give only 2 levels per side (weekly) and R1/S1/S2 (monthly) — short of 3 levels each side. | §6; §11 | 3 | Render weekly and monthly pivots as tables, R3→P→S3, three levels each side. |
| 2.3 Method steps visible | §4 lists observation → normalization → classification; §5 explains the consensus build and the exclusion rules; §8 is candle-by-candle for all five sessions with an explicit sequence assessment; §9 states overlap 0.48, persistence 0.54, percentile 47, VOLator slope +0.07 and the Kaufman gate; §7 has five captioned charts (pandoc image placeholders present — accepted as evidence, noted). §5 asserts a "weighted-median method" without showing the weights. | §4–§9 | 5 | Optional: show the weighted-median arithmetic in §5. |
| 3.1 Every quantitative claim sourced | §1, §6, §9, §11 numbers point back to §4/§6/§13 correctly. §12 and §14 carry a block of unsourced figures: "Apple briefly touched a $5tn market cap", "WTI back toward the low-$80s", "Nvidia −5% on $500bn memory deal", "USDX ~101.5", "Gold near ~$4,020–4,077", "VIX ~18", "BofA Bull & Bear ... highest since 2021". None of these is attributed or cross-referenced, and the oil figure contradicts §13c. | §12 bullets 1–4; §14 bullets 3–5 | 2 | Attach a source or an internal cross-reference to every figure in §12/§14, or drop the figure. |
| 3.2 Spot-checked citations exist and contain the data | Three checks, all internally consistent — **no fabrication, override NOT triggered**. (a) §4 "FRED (official) 27 Jul close 7,413.18" matches §6's 27 Jul close exactly. (b) §4 "Investing.com 28 Jul range 7,382.64 / 7,452.02" matches §6's 28 Jul H/L exactly and sits within 2 pts of the slice (7384.6 / 7452.9). (c) §13a "Motley Fool 24 Jul — S&P 500 edged up 0.05%" matches the report's own close-to-close move (7411.98/7408.30 = +0.050%). One citation is used inconsistently with its own stated band: §4 Yahoo 7,429.18 is "within tolerance band" and §20 calls Δ0.40 "within band", but §5 and §19 both define the equity-index tolerance as **±0.10 pt**. | §4 rows 3/5/6; §13a Motley Fool; §5 / §19 / §20 tolerance statements | 4 | Restate the true corroboration pair for 28 Jul, or correct the stated tolerance. |
| 3.3 Calculations transparent | **RSI2 does not reproduce from the report's own closes.** Helper recomputation on the report's stated closes gives 24 Jul 3.9 · 27 Jul 100.0 · 28 Jul 100.0 against the stated 12.9 · 16.4 · 59.2; the slice gives 6.33 · 100.00 · 100.00. Closes 7411.98 → 7413.18 → 7428.78 are two consecutive gains, so mean loss = 0 and RSI2 = 100 is forced; 16.4 and 59.2 are unreachable from the stated series. The 28 Jul report independently prints 3.9 for the same 24 Jul close. Pivots **do** reproduce exactly from the report's own 27 Jul H/L/C (P 7399.393, R1 7438.787, S1 7373.787, R2 7464.393, S2 7334.393, R3 7503.787, S3 7308.787) and satisfy the floor identity R2−P = P−S2 = 65.00; R1.5/S1.5/R4/R5/S4/S5 also reproduce — but from the wrong session. **ATR(14) is never stated numerically** anywhere in the report (only "0.25×ATR" symbolically in the 3C row); the 3C trigger 7598.55 implies ATR = 68.20 against slice ATR14 72.66 (cash) / 81.61 (full-day); the 28 Jul report stated ATR(14) = 77.65. KER value −0.22 given without the (13, EMA 3) parameters or the threshold. §21a components (−0.10, −0.045, −0.033) sum to **−0.178**, not the stated −0.19. §21c R-denominator never disclosed. | §6 RSI2 column vs helper; §11 vs §6; §9; §21a; §21c | 1 | Recompute the RSI2 column; publish ATR(14) and the KER parameters; make §21a components sum to the stated score. |
| 3.4 Numbers reconcile | D-1 close 7428.78 is identical in §1, §3, §4, §6, §13c and §18 (Trade 1 is suppressed, so no MARKET entry to reconcile). §11 pivots are quoted unchanged on the Trade 2 card (7438.79 / 7399.39). §6 RSI2 = §8 narrative values. Breaks: ATR is absent, so §9↔§21 cannot reconcile; Trade 2 says "TP1 zone near 7,465 R2" while its own TP1 is 7478.18 (13.79 out); Trade 2 says entry is "10 points above the pivot band ... a confirmed push through overhead pivots" while 7438.79 is 1.20 **below** the weekly pivot 7439.99 and 18.36 below monthly 7457.15 in the same report's §11; §21a sum ≠ stated score; §1/§21b record date ≠ §9; report 3C trigger 7598.55 vs extracted card entry 7598.01. | §11 vs §21b; §21a; §9 vs §1 | 2 | Fix the confluence and "10 points above" claims; reconcile §21a; publish ATR. |
| 4.1 Each pillar reaches a defended conclusion | §8 ends "Judgement label: Indecision"; §9 "Regime: Transitional / Bias Neutral-to-bearish"; §10 aggregates to MIXED with a contradiction flag; §12 gives a net label per bullet. §14 ends on a watch item with no pillar-level label. The Trade 2 card's stated conclusion is not defended by its own levels (entry sits below the overhead pivots it claims to break through). | §8 close; §9 bullets; §10 flag; §14; §21b Trade 2 | 3 | Add a §14 closing label; re-derive Trade 2 so the rationale matches the level. |
| 4.2 Peer / cross-asset interpreted, not listed | §10 gives a causal mechanism per counter (dollar → tighter global financial conditions and weaker earnings translation; VIX → hedging demand caps follow-through; DAX → common-factor risk beta arguing against a fresh leg lower), an explicit contradiction flag, an aggregate MIXED verdict, and a stated path into §15/§16 and the neutral direction score. Not a correlation list. | §10 table + contradiction flag | 5 | None. |
| 4.3 Synthesis reconciles tensions | §9 explicitly resolves the KER-down vs reversal-up tension and explains why the dual gate lands on Transitional rather than Range; §15/§16 hold the bull/bear balance event-gated; §21a checks the score against §17 and finds no conflict. But the synthesis-to-strategy chain is broken: the Trade 2 entry is built on a stale (27 Jul) pivot set, its thesis invalidation ("daily close back below the daily pivot 7,399") is the **same level as its stop** (7399.39), violating the M5 rule that invalidation be separate from the stop; the 3C TP1 sits 270.27 pts (3.32×ATR14) from entry, beyond the 2.5×ATR14 static cap; the 3C caveats do not propagate the single-source-indicative flag that §19 applies to all prior-period H/L; §9's threshold for the KER gate is asserted without a value. | §9 Kaufman bullet; §15–§18; §21b Trade 2 and 3C | 2 | Separate invalidation from stop; rebuild pivots on D-1; bring 3C TP1 inside the cap or state the exception. |
| 4.4 Calibrated language | §17 is exactly one sentence with a bounded range and a named catalyst; no hedge stacking; §21a states the score and the threshold; §3 states confidence explicitly. Calibration drift: §3 asserts **High** confidence on a close the report itself corroborates only at Δ0.40 against its declared ±0.10 band (and which sits 4.82 pts from the slice cash close); §1 calls the hike probability "unusually elevated" while §14 says "Fed on hold expected" and the only cited figure is 38%. | §3 Confidence; §1 vs §14; §17 | 3 | Downgrade §3 confidence or fix the corroboration claim; align the hike-probability language with the cited 38%. |
| 5.1 Data points dated; staleness flagged | Every §6 row, §4 row and §13a article carries a date. §6 note and §19 flag single-source-indicative O/H/L; §11 and §19 flag all pivot timeframes as SINGLE-SOURCE INDICATIVE. Weaknesses: the §6 Validation column marks only the 28 Jul row "O single-source indic." although the note says all five rows' O/H/L are indicative; §11 is labelled "prior session 27 Jul" with no flag that this is one session stale against the 28 Jul as-of. | §6 Validation column and note; §11 header; §19 | 4 | Flag O/H/L per row; flag or remove the stale pivot session. |
| 5.2 Material assumptions stated up front | Anchor is stated ("Daily-open anchor confirmed at 07:00 UK") and the single-source pivot propagation is stated in §11, §19 and carried into the Trade 2 caveat line. Not stated: the assumption behind the round-number O/H/L; the 3C card does **not** carry the single-source-indicative flag although its 25-session boundary is a prior-period H/L; ATR basis is never declared. | §20 anchor bullet; §11/§19; §21b Trade 2 vs 3C caveats | 3 | Propagate the indicative flag to 3C; declare the ATR basis. |
| 5.3 Red flags surfaced | §12 and §15 carry the risk set (hawkish FOMC, chip/AI-capex selloff, USDX+VIX tightening, loss of 7,360/7,388 exposing 7,294). The §13d FOMC collision is carried explicitly into **both** live card caveat lines ("holding period collides with 30 Jul FOMC"). The KER contradiction and the sentiment/price divergence are both flagged rather than buried. | §12; §15; §13d; §21b caveats | 5 | None. |
| 5.4 All prompt restrictions honoured | Honoured: no module codes (M1–M5), no framework name, no bracketed variable names, instrument common names used, CFD quote listed but explicitly Excluded, ES futures not used as an OHLC basis. **Breached — no-synthesis restriction.** §19 states "No values were synthesised — where corroboration was unavailable, the field is flagged rather than estimated", yet §6 presents round-number O/H/L (7500.00/7515.00/7455.00 · 7490.00/7495.00/7395.00 · 7405.00/7425.00/7360.00) under named Src A / Src B with the row marked CORROBORATED, and these miss the slice by up to 68.80 (27 Jul O), 55.30 (27 Jul H), 45.20 (23 Jul H) and 33.00 (22 Jul L) — an order of magnitude beyond the ≤8-pt CFD-vs-cash tolerance, while the same rows' closes land within 3 pts. The same sessions also disagree with the 28 Jul report's own O/H/L (22 Jul H 7515 vs 7540, L 7455 vs 7470; 23 Jul L 7395 vs 7370). Estimated levels are presented as sourced. | §6 O/H/L vs slice; §19 no-synthesis bullet; cross-check vs `SP500_Daily_Report_28-Jul-2026.md` §6 | 1 | **Restriction override triggered** — cap total at 74, drop C1 one level. Flag every uncorroborated O/H/L as indicative in-row and stop attributing it to Src A/Src B, or source it. |

## 2. Category roll-up

| Category | Level | Multiplier | Points | Justification |
|---|---|---|---|---|
| C1 Prompt adherence and instruction compliance (max 20) | **3** | 0.65 | 13.00 | Rows 1.1–1.3 = 4/2/5, mean 3.67 → level 4; the §5.4 restriction breach forces a one-level drop to 3. Variables and audience are respected; the coverage window drifts inside §11 (27 Jul pivots against a 28 Jul as-of) and the record-high date drifts between §1/§21b and §9. |
| C2 Structural and modular framework alignment (max 20) | **4** | 0.85 | 17.00 | Rows 2.1–2.3 = 5/3/5, mean 4.33 → 4. Every section §1–§21 present and ordered, §6 carries the full column set, method steps visible, five captioned charts. Held off 5 by §11: weekly and monthly pivots are prose rather than tables and are short of three levels per side. |
| C3 Accuracy, evidence and factual reliability (max 25) | **2** | 0.40 | 10.00 | Rows 3.1–3.4 = 2/4/1/2, mean 2.25 → 2. Closes are accurate (all five within 3 pts of the slice) and no source is fabricated, but the RSI2 column cannot be reproduced from the report's own closes, ATR(14) is never published, pivots are built off the wrong session, and §12/§14 carry a block of unsourced figures. |
| C4 Reasoning and judgment (max 20) | **3** | 0.65 | 13.00 | Rows 4.1–4.4 = 3/5/3/4 → wait, scored 3/5/2/3, mean 3.25 → 3. Cross-asset mechanism is genuinely interpreted and the KER tension is resolved, but card construction (scored here per the QA protocol) has real defects: stale pivot basis on the live Trade 2 entry, invalidation equal to the stop, 3C TP1 beyond the 2.5×ATR cap, §21a components that do not sum to the stated score. |
| C5 Currency, restrictions and transparency (max 15) | **3** | 0.65 | 9.75 | Rows 5.1–5.4 = 4/3/5/1, mean 3.25 → 3. Dating and red-flag surfacing are strong and the FOMC collision is carried into both cards, but the no-synthesis restriction is breached in §6 and the indicative flag is not propagated to the 3C card. |
| **Total** | — | — | **62.75 → 63** | Sum of category points, rounded to a whole number. |

## 3. Total, band, override check

- **Raw total: 13.00 + 17.00 + 10.00 + 13.00 + 9.75 = 62.75 → 63**
- **Override — fabricated source: NOT triggered.** Three spot-checked citations (§4 FRED 27 Jul close 7,413.18; §4 Investing.com 28 Jul range 7,382.64/7,452.02; §13a Motley Fool 24 Jul "+0.05%") are each named, dated, and quote a figure used consistently elsewhere in the report; none is self-contradictory or impossible. C3 is therefore scored on its merits (2), not zeroed.
- **Override — restriction breach: TRIGGERED.** §19's explicit no-synthesis restriction is breached by the §6 O/H/L set (see row 5.4). Effects applied: total capped at 74 and C1 dropped one level (4 → 3). The C1 drop is already reflected in the roll-up above; the cap is **not binding** because 63 < 74.
- **Final Trust Score: 63 · Band: Moderate (60–74).**
- Consistency note: the band the cap would have imposed (Moderate) is the same band the arithmetic produces, so the score stands as computed.

## 4. Card Integrity

Linter rows, copied verbatim from `qa/regen_20260906_qa1/lint_static/2026-07-29.csv`:

| card_id | report_date | strategy | flags | dud |
|---|---|---|---|---|
| 2026-07-29_Trade_1 | 2026-07-29 | Trade 1 - Daily Directional | SUPPRESSED | False |
| 2026-07-29_Trade_2 | 2026-07-29 | Trade 2 - Pivot (TRANSITION breakout side) | CLEAN | False |
| 2026-07-29_Trade_3C | 2026-07-29 | Trade 3C - Momentum-Breakout (conditional upside) | WARN_TARGET_FAR(3.32xATR) | False |

Per-card integrity — `100 − 40·(#DUD) − 10·(#WARN)`, floored at 0:

| Card | #DUD | #WARN | Integrity |
|---|---|---|---|
| 2026-07-29_Trade_1 | 0 | 0 | n/a — SUPPRESSED, excluded from the mean |
| 2026-07-29_Trade_2 | 0 | 0 | 100 |
| 2026-07-29_Trade_3C | 0 | 1 (WARN_TARGET_FAR) | 90 |

**Report-level Card Integrity (mean over non-suppressed cards) = (100 + 90) / 2 = 95.0**

Counts for the roll-up CSV: n_cards = 3 (all lint rows) · n_duds = 0 · n_warns = 1.

M5 rule assessment (feeds checklist rows 4.1/4.3, **not** the integrity number):

- **Trade 1** — compliant. Direction score |−0.19| < 0.25 → suppressed, and it is rendered as a SUPPRESSED row rather than omitted, as the rule requires.
- **Trade 2** — TRANSITION breakout-side-only is the correct fork. Static integrity passes (stop below entry; TP1 7478.18 > entry; TP2 7517.57 > TP1; R = 39.40 pts sits inside 0.3×ATR14 = 21.80 and 3.0×ATR14 = 217.98; TP1 distance 39.39 < 2.5×ATR14 = 181.65; buy-stop 7438.79 is above the D-1 close on both the report's basis 7428.78 and the slice cash 7433.60). Rule defects: pivot basis is the 27 Jul session, not D-1; invalidation level equals the stop level; the "10 points above the pivot band" and "TP1 zone near 7,465 R2" claims contradict the report's own §11 and TP1; TP3 is narrative only, with no price/points (the extracted card carries 7560.0, a number the report never states); no anchor on the card.
- **Trade 3C** — the 3C arithmetic reproduces from the stated range (width 287.32; stop 7294.18 + 0.40×width = 7409.11; TP1 7581.50 + 1.0×width = 7868.82; TP2 7581.50 + 1.5×width = 8012.48; midpoint invalidation 7437.84 ≈ "~7,438"; mirror-short trigger 7277.13). Rule defects: TP1 sits 270.27 pts = 3.32×ATR14 from entry, breaching the 2.5×ATR14 cap (the linter WARN); ATR is undisclosed and the implied 68.20 disagrees with the slice ATR14; the 25-session low 7294.18 is 8.92 pts off the slice low 7303.10; no single-source-indicative flag; levels in price only, no points; report trigger 7598.55 vs extracted entry 7598.01.

## 5. Data reconciliation log

Slice = US500 cash session (09:30–16:00 ET). Tolerance: close ≤ 3 pts, O/H/L ≤ 8 pts. "full-day" = broker-day OHLC, shown where it is the nearer basis.

| Section | Report value | Slice value | Delta | Verdict |
|---|---|---|---|---|
| §6 22 Jul Open | 7500.00 | 7490.30 (cash) / 7506.70 (full) | +9.70 / −6.70 | OK on full-day basis |
| §6 22 Jul High | 7515.00 | 7525.50 (both bases) | −10.50 | **Discrepancy** |
| §6 22 Jul Low | 7455.00 | 7488.00 (cash) / 7467.80 (full) | −33.00 / −12.80 | **Discrepancy** |
| §6 22 Jul Close | 7498.96 | 7498.80 | +0.16 | OK |
| §6 23 Jul Open | 7490.00 | 7416.70 (cash) / 7496.20 (full) | +73.30 / −6.20 | OK on full-day basis only |
| §6 23 Jul High | 7495.00 | 7449.80 (cash) / 7513.00 (full) | +45.20 / −18.00 | **Discrepancy** |
| §6 23 Jul Low | 7395.00 | 7375.30 (both bases) | +19.70 | **Discrepancy** |
| §6 23 Jul Close | 7408.30 | 7405.50 | +2.80 | OK |
| §6 24 Jul Open | 7410.00 | 7407.60 | +2.40 | OK |
| §6 24 Jul High | 7440.00 | 7460.20 (both bases) | −20.20 | **Discrepancy** |
| §6 24 Jul Low | 7388.00 | 7395.60 | −7.60 | OK |
| §6 24 Jul Close | 7411.98 | 7411.80 | +0.18 | OK |
| §6 27 Jul Open | 7405.00 | 7473.80 (cash) / 7471.00 (full) | −68.80 / −66.00 | **Discrepancy — largest in the report** |
| §6 27 Jul High | 7425.00 | 7480.30 (cash) / 7491.00 (full) | −55.30 / −66.00 | **Discrepancy** |
| §6 27 Jul Low | 7360.00 | 7382.90 (both bases) | −22.90 | **Discrepancy** |
| §6 27 Jul Close | 7413.18 | 7415.50 | −2.32 | OK |
| §6 28 Jul Open | 7415.00 | 7417.40 | −2.40 | OK |
| §6 28 Jul High | 7452.02 | 7452.90 | −0.88 | OK |
| §6 28 Jul Low | 7382.64 | 7384.60 | −1.96 | OK |
| §6 28 Jul Close (D-1) | 7428.78 | 7433.60 (cash) / 7435.60 (full) | −4.82 / −6.82 | **Discrepancy** (>3 pts, but ≤10 — recorded, not a Cat-3 close failure) |
| §6 RSI2 22 Jul | 46.0 | 86.97 (slice closes); n/a from report closes (window) | −40.97 vs slice | **Fail** — 28 Jul report prints 86.6 for the same session |
| §6 RSI2 23 Jul | 6.9 | 0.00 (slice closes); n/a from report closes (window) | +6.90 vs slice | **Fail** — 28 Jul report prints 0.0 |
| §6 RSI2 24 Jul | 12.9 | 6.33 (slice) / **3.9 (report's own closes)** | +9.00 vs report's own | **Fail** — does not reproduce |
| §6 RSI2 27 Jul | 16.4 | 100.00 (slice) / **100.0 (report's own closes)** | −83.60 | **Fail** — two consecutive up-closes force RSI2 = 100 |
| §6 RSI2 28 Jul | 59.2 | 100.00 (slice) / **100.0 (report's own closes)** | −40.80 | **Fail** — does not reproduce |
| §6 Trend 22 Jul | Neutral | Rule-implied Bearish (C 7498.96 < O 7500.00 and RSI2 46.0 < 50) | — | **Mislabel** against the stated trend rule |
| §11 pivot session | "prior session 27 Jul" | D-1 for D = 29 Jul is **28 Jul** | 1 session stale | **Discrepancy** — wrong input session |
| §11 P | 7399.39 | Reproduces exactly from report's 27 Jul H/L/C (7399.393); D-1-correct value from report's own 28 Jul H/L/C = 7421.15; slice cash D-1 P = 7423.70 | −21.76 vs report-correct / −24.31 vs slice | Arithmetic OK, input wrong |
| §11 R1 | 7438.79 | Report-correct D-1 R1 = 7459.65; slice cash R1 = 7462.80 | −20.86 / −24.01 | Arithmetic OK, input wrong |
| §11 identity R2−P vs P−S2 | 65.00 vs 65.00 | Floor-pivot identity | 0.00 | **Pass** |
| §11 R1.5 / S1.5 / R3 / S3 / R4 / R5 / S4 / S5 | 7451.59 / 7354.09 / 7503.79 / 7308.79 / 7568.79 / 7633.79 / 7243.79 / 7178.79 | All reproduce from the report's own 27 Jul H/L/C | 0.00 | Arithmetic OK, input wrong |
| §9 25-session range | 7,294 – 7,581 | 7303.10 (2026-06-26) – 7582.80 (2026-07-15) | +8.92 low / −1.30 high | Minor discrepancy |
| §9 / §1 range percentile | 47th | (7428.78 − 7294.18) / 287.32 = 46.8% | −0.2 | OK (self-consistent) |
| §1 / §21b "record" date | "early-June record" / "June record high" | Slice 25-session high is 2026-07-15; §9 of the same report says 15 Jul; the 24 Jul report cites a June record of 7,620.90 | — | **Internal + cross-report inconsistency** |
| §9 / §21 ATR(14) | Not stated; implied 68.20 from the 3C trigger | 72.66 (cash) / 81.61 (full-day); 28 Jul report stated 77.65 | −4.46 / −13.41 | **Fail** — ATR(14) required to be stated |
| §21a direction score | −0.19 | Stated components −0.10 + (−0.045) + (−0.033), others "net to zero" = −0.178 | 0.012 | **Discrepancy** — components do not sum to the score |
| §21b T2 entry 7438.79 | Buy stop, "10 points above the pivot band" | Weekly P 7439.99 and monthly P 7457.15 in the same report's §11 | −1.20 / −18.36 | **Fail** — entry is below the band it claims to clear |
| §21b T2 TP1 "zone near 7,465 R2" | TP1 = 7478.18 | R2 = 7464.39 | 13.79 | **Fail** — confluence claim wrong |
| §21b T2 R | 39.40 pts | 0.3×ATR14 = 21.80 · 3.0×ATR14 = 217.98 · 1×ATR14 = 72.66 | — | **Pass**, no wide-stop flag needed |
| §21b 3C trigger | 7598.55 (boundary + 0.25×ATR) | 7581.50 + 0.25×72.66 = 7599.67 (cash) / +0.25×81.61 = 7601.90 (full) | −1.12 / −3.35 | Discrepancy from undisclosed ATR; extracted card says 7598.01 |
| §21b 3C TP1 distance | 7868.82 − 7598.55 = 270.27 | Cap 2.5×ATR14 = 181.65 (cash) / 204.03 (full) | +88.62 / +66.24 | **Fail** — 3.32×ATR, the linter WARN |
| §21c backtest entries | 7500 / 7410 / 7405 / 7415 | These are the §6 opens for 22 / 24 / 27 / 28 Jul; 27 Jul open is 68.80 off the slice | — | Inherits the §6 open errors |
| §21d mean R | ≈ −0.08 | (0.02 − 0.03 − 0.12 − 0.20) / 4 = −0.0825 | 0.0025 | OK (self-consistent) |
| §4 / §20 corroboration Δ | Yahoo Δ0.40 "within band" | §5 and §19 state the tolerance is ±0.10 pt | 0.30 over | **Internal inconsistency** |
| Cross-report §6 O/H/L (22–24 Jul) | 22 Jul H 7515 / L 7455; 23 Jul L 7395; 24 Jul O 7410 / H 7440 | `SP500_Daily_Report_28-Jul-2026.md` §6: 22 Jul H 7540 / L 7470; 23 Jul L 7370; 24 Jul O 7409 / H 7434 | up to 25 pts | **Cross-report inconsistency** on identical historical sessions |
| Cross-report §6 RSI2 (22–24 Jul) | 46.0 / 6.9 / 12.9 | 28 Jul report: 86.6 / 0.0 / 3.9 (matches the slice and the report's own closes) | up to 40.6 | **Cross-report inconsistency** — the prior report's values are the correct ones |
| Header / §2 as-of session | "As-of session close 28 July 2026 (America/New_York)"; "last completed session 28 July 2026" | D-1 = 2026-07-28; slice last bar 2026-07-28 23:45 | 0 | **Pass** — as-of is genuinely D-1 (but §11 does not use it) |
