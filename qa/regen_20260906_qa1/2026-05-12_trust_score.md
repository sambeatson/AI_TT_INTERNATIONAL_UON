# Trust Score — 2026-05-12 — SP500_Report_12May2026.md

Run: regen_20260906_qa1 · D = 2026-05-12 · D-1 slice = `data/slices/US500/US500_upto_2026-05-11.csv` (cash session 16:30–23:00 broker) · helper ATR14 (cash) = 67.24 · slice D-1 cash close 7,419.7 (full-day 7,416.2).

## 1. Section 7 checklist

| Item | Reviewer notes | Evidence observed | Score 0–5 | Action required |
|---|---|---|---|---|
| 1.1 Variables respected | Asset = S&P 500 cash index; counters USDX · VIX · DAX 40 in order; as-of 11 May NY close; 5-session lookback; USD, index points, hundredth-of-a-point tick; Trade 1 anchored 07:00 UK. Source count short: §4 has 7 rows but only 5 distinct sources (Yahoo, TradingEconomics, Investing.com, FRED, CNBC); no exchange-tier or sell-side source. | §2 table; §4; §20 anchor paragraph; §21b Trade 1 entry | 4 | Add at least one exchange-tier and one sell-side source to reach ≥ 6 distinct sources. |
| 1.2 Coverage & currency consistent | All price data dated ≤ 11 May; session dates 12–18 May; articles dated 7–11 May; currency/units consistent (USD, points) throughout. | §2, §6, §13a, §13d, §21c | 5 | None. |
| 1.3 Audience & tone | Senior US Equity Strategist register; trading-and-risk-review framing; no retail tone. | §1, §18, footer | 5 | None. |
| 2.1 Sections present & ordered | §1–§21 all present in order incl. §21a–d and limitations boilerplate. §13 sub-labels deviate: 13c is a "divergence flag" and 13d holds both calendars (spec: 13c previous-period, 13d upcoming); §7 is a placeholder paragraph (pandoc image drop accepted, noted). | Headings; §13c/§13d; §7 | 4 | Relabel §13c = previous-period calendar, §13d = upcoming; keep divergence note inside §13b. |
| 2.2 Scorecard as a table | §6 is a table but lacks the Trend column and the Final/Validation split (has Source A/Source B/Outcome only). §11 tables ordered high→low but extend to R5/S5 with no formula for R4/R5/S4/S5. | §6 header row; §11 three tables | 3 | Add Trend and Final columns to §6; restrict §11 to R3→P→S3 or state the R4/R5 formula. |
| 2.3 Method steps visible | §4→§5 observation → classification → consensus visible; §8 candle-by-candle plus sequence assessment; §9 regime with persistence, overlap, VOLator; §7 charts only as caption placeholder. | §4, §5, §8, §9, §7 | 4 | Render or caption-link the two required charts. |
| 3.1 Quantitative claims sourced | §1 crude $98/bbl, Hormuz "~80% reduced flow", §14 March CPI +0.9%/+3.3%, 2y pricing, "78% beat rate vs 74% 10-yr" carry no source (beat rate traces only to §13a Reuters paraphrase). NFP, DXY 97.84, VIX 18.4 do trace to §13/§19. | §1, §12, §14 | 3 | Source or point each macro figure to §4/§13. |
| 3.2 Citations exist & contain data | (a) Yahoo 11 May 21:48 UK 7,412.84, +13.91 (+0.19%): arithmetic vs 8 May 7,398.93 consistent (Δ 13.91, +0.188%). (b) CNBC 8 May "+0.84% to 7,398.93" implies prior close 7,337.3 — consistent with the §4 derived 7,337.11 within rounding. (c) Investing.com 11 May cited "~20:30 UK" for O/H/L 7,385.31/7,428.97/7,384.20 but used as the full-session range although the cash session closed 21:00 UK — timestamp inconsistent; the figures themselves sit within 6–7 pts of the slice. USDX 97.84 matches slice (97.82–97.85). No fabricated source detected. | §4 rows 1, 3, 6; §19 | 4 | Correct the Investing.com retrieval time or state that the range was re-read after the close. |
| 3.3 Calculations transparent | RSI2 not shown and does not reproduce: report 70/84/76 (07/08/11 May) vs 78.1/68.8/100.0 recomputed from the report's own closes (helper). Trend column absent. Pivots: only P reproduces from stated H/L/C; R1/S1/R2/S2/R3/S3 do not for daily, weekly or monthly (e.g. daily R1 stated 7,415.6, computed 7,422.6; weekly R1 stated 7,429.9, computed 7,456.3; monthly R1 stated 7,101.1, computed 7,140.6). ATR(14) "≈54" appears only on the Trade 1 card, not in §9. KER label given without value. §21a shows three of six weighted contributions (+0.25 +0.20 +0.15 = +0.60) but total +0.42 — the −0.18 balance is not itemised. | §6, §11, §9, §21a, §21b | 1 | Show RSI2 gains/losses; recompute all pivot tiers; state ATR14 and KER numerically in §9; list all six §21a contributions. |
| 3.4 Numbers reconcile | D-1 close 7,412.84/7,412.8 consistent across §1/§3/§4/§6/§18/§21b. Pivots on cards match §11. Failures: §6 07 May Open 7,360.4 > High 7,348.0 (impossible bar); §8 "7,333 (7 May low)" vs §6 07 May low 7,310.5; §1 "seventh straight weekly advance" vs "six" in §3/§4/§9/§15/§18; §21c 11 May Trade 2 "filled at 7,378" though §6 11 May low is 7,384.2; §21d Trade 1 TP1 hit rate 60% vs 40% implied by §21c (only +2.1R and +1.1R ≥ 1R); Trade 3A "38.2% = 7,362 / 61.8% = 7,323" vs 7,353.7 / 7,307.1 from the card's own endpoints. Versus slice: §6 opens/lows for 06, 07, 08 May off by 15–47 pts; 05 May low off 11.1; 11 May close off 6.9; ATR 54 vs 67.2; daily pivots built from 8 May, not D-1. | §6, §8, §1, §21b, §21c, §21d; log §5 | 1 | See §5 log; fix each listed pair. |
| 4.1 Pillars conclude | §8 ends "Bullish continuation"; §9 "Bias: Bullish"; §10 "CONFIRMS". §12 and §14 end without a direction label. | §8, §9, §10 closing lines; §12, §14 | 3 | Add a closing direction label to §12 and §14. |
| 4.2 Peer/cross-asset interpreted | §10 gives mechanisms: dollar translation/financial conditions for USDX; hedge-demand vs stress for VIX; Europe-specific tariff/defence story for DAX; net read stated. | §10 table and note | 5 | None. |
| 4.3 Synthesis reconciles tensions | §16 explicitly reconciles with §9; §20 resolves the VIX dissent; §21a vs §17 no conflict. Card construction (scored here per protocol): Trade 1 stop not derived per M5 §4c (weekly P used instead of tighter of swing/nearest S/R + 0.25×ATR) and no wide-stop flag though R 68.8 > 1×ATR(54); Trade 2 labelled TREND_UP branch but uses limit-at-P, structural stop and 1R/2R targets instead of P+0.10(R1−P) / P−0.8(P−S1) / R1–R1.5–R2, on pivots from 8 May rather than D-1; Trade 3A enters at 38.2% not 57.5%, stop not beyond the swing-low anchor, swing magnitude in ATR and lookback not logged, and levels do not reproduce from the stated endpoints. | §15–§18, §21a, §21b | 2 | Rebuild the three cards to M5 (see feedback). |
| 4.4 Calibrated language | §17 is one sentence with one explicit condition; scenario probabilities 55/25/20 sum to 100; confidence "Medium-High" not on the H/M/L scale. | §3, §16, §17, §18 | 4 | Grade confidence as H/M/L. |
| 5.1 Data dated; staleness flagged | Every price and article dated; 07 May close flagged indicative in §4/§6/§19; monthly pivots flagged; VIX single-primary flagged. 07 May O/H/L carry no source at all. | §4, §6, §13a, §19 | 4 | Source the 07 May O/H/L or flag them indicative. |
| 5.2 Assumptions up front | Anchor override (07:00 UK, 12 May) logged in §20 and on the Trade 1 card; single-source monthly tier propagation stated in §19. Not stated: a 07:00 UK market fill is pre-cash-open, i.e. a proxy (futures/CFD) open, so the entry cannot equal the cash close. | §20, §21b, §19 | 4 | Add the proxy-open caveat to the Trade 1 card. |
| 5.3 Red flags surfaced | §12/§15 risks thorough; §13d flags 12 May CPI as highest impact and §21a notes the binary — but no card carries a CPI event-collision caveat although all three sit across the 08:30 ET print. | §12, §15, §13d, §21b | 3 | Add the CPI collision caveat to each card. |
| 5.4 Restrictions honoured | Bracketed variable name `[PRIMARY_ASSET]` printed in §5 (restriction breach); TradingEconomics US500 CFD used as Source B in the §6 OHLC basis (05 May) and as a corroboration source in §20 — retail CFD quote in the OHLC basis; 07 May O/H/L presented in a "validated" table with no source and an impossible O > H (synthesised bar). "Strategies module" named in §20 (module reference, not a code — noted only). No ES futures, no framework name. | §5 para; §6 row 1; §20; §6 row 3 | 1 | Remove the placeholder; drop CFD from the OHLC basis; source or drop the 07 May bar. |

## 2. Category roll-up

| Category | Level | Multiplier | Points | Justification |
|---|---|---|---|---|
| C1 Prompt adherence (20) | 3 | 0.65 | 13.00 | Rows 1.1–1.3 mean 4.67 → 5; restriction-breach override drops C1 by at least one level; two distinct breaches (placeholder variable, CFD in OHLC basis) → taken down to 3. |
| C2 Structure (20) | 4 | 0.85 | 17.00 | Rows 4/3/4, mean 3.67 → 4: all 21 sections present; §6 missing Trend/Final columns; §13 sub-labels off. |
| C3 Accuracy & evidence (25) | 2 | 0.40 | 10.00 | Rows 3/4/1/1, mean 2.25 → 2: RSI2 and pivot arithmetic do not reproduce; impossible 07 May bar; multiple internal contradictions; several unsourced macro figures. |
| C4 Reasoning & judgment (20) | 3 | 0.65 | 13.00 | Rows 3/5/2/4, mean 3.5; tie resolved to the lower level per framework §9 guidance, driven by non-compliant card construction. |
| C5 Currency, restrictions & transparency (15) | 3 | 0.65 | 9.75 | Rows 4/4/3/1, mean 3.0: dating and caveats good; restriction breaches and missing CPI-collision caveat. |
| **Total** | | | **62.75 → 63** | |

## 3. Total, band, override check

Total 63/100. Band: **Moderate** (60–74).
Overrides: **restriction_breach** — `[PRIMARY_ASSET]` bracketed variable name printed in §5 ("cash is the [PRIMARY_ASSET] basis"), plus a retail CFD quote (TradingEconomics US500) inside the §6 OHLC basis. Cap at Moderate applies (total already ≤ 74); C1 reduced from 5 to 3. No fabricated source found on the three-source spot-check, so the hallucinated-source override does not apply.

## 4. Card Integrity

Linter rows (`qa/regen_20260906_qa1/lint_static/2026-05-12.csv`, verbatim):

| card_id | report_date | strategy | flags | dud |
|---|---|---|---|---|
| 2026-05-12_Trade_1 | 2026-05-12 | Trade 1 - Daily Directional | CLEAN | False |
| 2026-05-12_Trade_2 | 2026-05-12 | Trade 2 - Pivot (TREND_UP pullback, buy daily P) | CLEAN | False |
| 2026-05-12_Trade_3A | 2026-05-12 | Trade 3A - Momentum-Pullback (38.2% fib) | CLEAN | False |

Per-card integrity (100 − 40·#DUD − 10·#WARN): Trade 1 = 100 · Trade 2 = 100 · Trade 3A = 100. Suppressed cards: none. Report-level mean = **100.0** (n_cards 3, n_duds 0, n_warns 0).

M5-rule assessment (feeds row 4.3, not the integrity number): all three cards pass the static checks (stop side, TP ordering, R = 68.8/34.0/52.0 within [20.2, 201.7] = [0.3, 3.0]×67.24, TP1 within 168.1 of entry, market entry = report D-1 close, limits below the close, anchor explicit). They fail the construction rules: Trade 1 stop anchor and missing wide-stop flag; Trade 2 wrong branch formula and stale (8 May) pivots; Trade 3A wrong retrace level, wrong stop anchor, unlogged swing metrics.

## 5. Data reconciliation log

Slice values are cash-session (16:30–23:00 broker) unless stated. Tolerance: close ≤ 3 pts, O/H/L ≤ 8 pts.

| Section | Field | Report value | Slice / recomputed value | Delta | Verdict |
|---|---|---|---|---|---|
| §6 05 May | Open | 7,242.5 | 7,245.4 | −2.9 | consistent |
| §6 05 May | High | 7,278.4 | 7,278.1 | +0.3 | consistent |
| §6 05 May | Low | 7,231.8 | 7,242.9 | −11.1 | discrepancy |
| §6 05 May | Close | 7,265.1 | 7,265.8 | −0.7 | consistent |
| §6 06 May | Open | 7,265.0 | 7,310.4 | −45.4 | discrepancy (equals prior close — looks synthesised) |
| §6 06 May | High | 7,371.2 | 7,374.9 | −3.7 | consistent |
| §6 06 May | Low | 7,259.6 | 7,306.9 | −47.3 | discrepancy |
| §6 06 May | Close | 7,365.1 | 7,366.4 | −1.3 | consistent |
| §6 07 May | Open | 7,360.4 | 7,379.6 | −19.2 | discrepancy; also O > stated H (impossible bar) |
| §6 07 May | High | 7,348.0 | 7,389.6 | −41.6 | discrepancy |
| §6 07 May | Low | 7,310.5 | 7,325.6 | −15.1 | discrepancy |
| §6 07 May | Close | 7,337.1 | 7,344.6 | −7.5 | discrepancy (< 10, not a failure on its own) |
| §6 08 May | Open | 7,340.2 | 7,375.6 | −35.4 | discrepancy |
| §6 08 May | High | 7,401.5 | 7,407.5 | −6.0 | consistent |
| §6 08 May | Low | 7,332.9 | 7,371.8 | −38.9 | discrepancy |
| §6 08 May | Close | 7,398.9 | 7,400.6 | −1.7 | consistent |
| §6 11 May (D-1) | Open | 7,385.3 | 7,391.3 | −6.0 | consistent |
| §6 11 May (D-1) | High | 7,429.0 | 7,435.0 | −6.0 | consistent |
| §6 11 May (D-1) | Low | 7,384.2 | 7,391.3 | −7.1 | consistent |
| §6 11 May (D-1) | Close | 7,412.8 | 7,419.7 cash (7,416.2 full-day) | −6.9 (−3.4) | discrepancy vs cash; within basis vs full-day |
| §6 RSI2 05–11 May | RSI2 | 78 / 92 / 70 / 84 / 76 | slice closes: 70.1 / 100.0 / 82.2 / 72.0 / 100.0 | — | discrepancy |
| §6 RSI2 07/08/11 May | RSI2 from report's own closes | 70 / 84 / 76 | 78.1 / 68.8 / 100.0 | −8.1 / +15.2 / −24.0 | **failure** — arithmetic does not reproduce |
| §21b / §9 | ATR(14) | ≈54 | 67.24 cash (74.39 full-day) | −13.2 | discrepancy; not stated in §9 |
| §11 daily | Basis session | 8 May H/L/C | D-1 = 11 May (cash P 7,415.33, R1 7,439.37, S1 7,395.67, R2 7,459.03, S2 7,371.63, R3 7,483.07, S3 7,351.97) | — | **failure** — wrong session for daily pivots |
| §11 daily | R1 / S1 / R2 / S2 / R3 / S3 from report's own 8 May H/L/C | 7,415.6 / 7,360.9 / 7,432.3 / 7,323.1 / 7,470.5 / 7,285.4 | 7,422.6 / 7,354.0 / 7,446.4 / 7,309.2 / 7,491.2 / 7,285.4 | −7.0 / +6.9 / −14.1 / +13.9 / −20.7 / 0.0 | failure — only P (7,377.8) and S3 reproduce |
| §11 weekly | R1 / S1 / R2 / S2 / R3 / S3 from report's own W/E 9 May H/L/C | 7,429.9 / 7,313.1 / 7,460.9 / 7,259.1 / 7,514.9 / 7,229.1 | 7,456.3 / 7,286.6 / 7,513.8 / 7,174.4 / 7,626.0 / 7,116.9 | −26.4 / +26.5 / −52.9 / +84.7 / −111.1 / +112.2 | failure — only P (7,344.1) reproduces; slice weekly (cash) P 7,328.5 / R1 7,479.6 / S1 7,249.6 |
| §11 monthly | R1 / S1 / R2 / S2 / R3 / S3 from April H/L/C | 7,101.1 / 6,892.9 / 7,179.3 / 6,763.1 / 7,250.6 / 6,684.7 | 7,140.6 / 6,853.6 / 7,258.3 / 6,684.3 / 7,427.6 / 6,566.6 | −39.5 / +39.3 / −79.0 / +78.8 / −177.0 / +118.1 | failure — only P (6,971.3) reproduces |
| §21b Trade 3A | 5-day swing low → high | 7,231.8 → 7,429.0 | 7,242.9 (05 May) → 7,435.0 (11 May) | −11.1 / −6.0 | low is a discrepancy |
| §21b Trade 3A | 38.2% / 61.8% retrace from the card's own endpoints | 7,362.0 / 7,323 | 7,353.7 / 7,307.1 | +8.3 / +15.9 | failure — does not reproduce |
| §4 / §20 | TradingEconomics US500 ~21:00 UK | 7,423.0 | slice 23:00-broker bar close 7,416.0 | +7.0 | consistent (CFD basis) |
| §10 / §19 | USDX 8 May | 97.84 | 97.82–97.85 (slice 8 May 23:00–23:45) | ≈0 | consistent |
| §10 / §19 | VIX 8 May / 11 May | 17.19 / 18.38 | 19.22 / 19.52 (VIX slice closes) | −2.0 / −1.1 | basis difference (VIX slice is a derivative feed); not counted as a discrepancy |
| §8 vs §6 | 7 May low | 7,333 (§8) | 7,310.5 (§6) | +22.5 | internal inconsistency |
| §21c vs §6 | 11 May Trade 2 fill at 7,378 | "Yes (pivot pullback touch)" | §6 11 May low 7,384.2 (slice 7,391.3) — limit never touched | — | internal inconsistency |
| §21d vs §21c | Trade 1 TP1 hit rate | 60% | 2 of 5 = 40% | +20 pp | internal inconsistency |
| §1 vs §3/§4/§9/§15/§18 | Weekly streak | seventh | sixth | — | internal inconsistency |
