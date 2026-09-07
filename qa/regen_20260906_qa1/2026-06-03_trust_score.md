# Trust Score — 2026-06-03 — SP500_Daily_Report_2026-06-03.md

Run: regen_20260906_qa1 · Asset: US500 · D = 2026-06-03 · D-1 slice: `data/slices/US500/US500_upto_2026-06-02.csv` (last bar 2026-06-02 23:45 broker).
Helper: `python3 engine/qa_slice_stats.py --slice data/slices/US500/US500_upto_2026-06-02.csv --date 2026-06-03 --closes 7519.74 7561.22 7580.06 7599.96 7585.50`.

Report as stated: D-1 (2 Jun) O/H/L/C 7,598.20 / 7,602.10 / 7,560.40 / 7,585.50 · RSI2 column 97.4 / 97.0 / 100.0 / 100.0 / 57.9 · ATR(14) never stated as a number (implied 66.43 from "1.3× ATR" = 86.36 and "3×ATR cap" = 199.29) · daily pivots (from 1 Jun H/L/C, not D-1) P 7,601.28 R1 7,619.58 S1 7,581.67 R2 7,639.19 S2 7,563.37 R3 7,657.49 S3 7,543.76 · weekly P 7,557.81 · direction score +0.40 LONG · regime Trending (Bullish), KER +0.349 · cards: Trade 1 LONG MARKET @ 00:00 UK 7,585.50 / SL 7,499.14 / TP 7,671.86 / 7,758.22 / 7,784.79; Trade 2 LONG BUY LIMIT 7,601.28 / SL 7,557.81 / TP 7,619.58 / 7,639.19 / 7,657.49; Trade 3A LONG BUY LIMIT 7,573.68 / SL 7,484.00 / TP 7,620.90 / 7,744.51 / "100%+ ext".

Slice (cash session 16:30–23:00 broker): D-1 O/H/L/C 7,590.8 / 7,624.6 / 7,588.3 / 7,615.8 · ATR14 cash 63.86 (full-day 72.51) · daily pivots from D-1 cash P 7,609.57 R1 7,630.83 S1 7,594.53 R2 7,645.87 S2 7,573.27 R3 7,667.13 S3 7,558.23 · weekly cash P 7,563.63 R1 7,622.97 S1 7,525.47 · 5d swing high 7,624.6 (2 Jun) low 7,504.3 (27 May) · RSI2 on slice closes 3.82 / 100 / 100 / 100 / 100.

## 1. Section 7 checklist

| Item | Reviewer notes | Evidence observed | Score 0–5 | Action required |
|---|---|---|---|---|
| 1.1 Variables respected | Asset = S&P 500 cash index; counters USDX · VIX · DAX 40 with USDX first; lookback 5/25; USD, index points. Deviations: daily-open anchor is **00:00 UK** on the Trade 1 card and in §20 ("per the run instruction"), not the 07:00 UK variable; as-of in §2 is "3 June 2026" (D) rather than the NY close of D-1; tick 0.01 not stated; §4 has six price rows but no exchange-tier or sell-side-tier price source (only an index provider via FRED plus aggregators/media). | §2 table; §21b Trade 1 "Market at 00:00 UK reference"; §20 "Daily-open anchor set to the 00:00 UK reference"; §4 | 3 | Restore the 07:00 UK anchor; state as-of = NY close of 2 Jun; add exchange/sell-side price tier or say why absent |
| 1.2 Coverage & currency consistent | All price dates are ≤ D-1 and the session is D; no currency/unit drift. But the D-1 session is not covered to its close: the 2 Jun row is an intraday snapshot ("2 Jun intraday −0.19%") presented in §1/§3 as the completed close. §13a dates a CNBC article 31 May (a Sunday) for a 1 Jun closing wrap. | §4 row 5 "2 Jun intraday"; §6 "Close indicative (intraday)"; §1 "closed the prior completed session at 7,585.50"; §13a row 1 | 3 | Re-source the completed 2 Jun close; correct article dates |
| 1.3 Audience & tone | Senior strategist register throughout; risk-review framing (§18 three reasons + single watch item); no retail tone. | §1, §18 | 5 | none |
| 2.1 Sections present & ordered | §1–§21 all present and in order; §13a/b/c/d present (13b has numeric tilt +0.17); §21a/b/c/d present; §17 is one sentence; §21d carries the limitations boilerplate. | headings lines 5–760 | 5 | none |
| 2.2 Scorecard as a table | §6 is a table with Date/O/H/L/C/RSI2/Trend/Source A/Source B/Validation — the **Final** column is absent. §11 daily table is ordered R5→P→S5 (superset of R3→S3, correctly ordered); weekly and monthly R3→P→S3. | §6 header row; §11 | 4 | Add the Final column to §6 |
| 2.3 Method steps visible | §4 observations → §5 classification (Core/Directional, weighted median) → §3 consensus; §8 candle-by-candle with close-in-range % plus sequence assessment; §9 regime with overlap 0.374, persistence 0.522, range-position 93.6%, VOLator and KER. §7 shows five image placeholders (pandoc dropped the images) — accepted as evidence, noted. | §4–§9; §7 `![](media/...)` ×5 | 5 | none (chart images not verifiable in md) |
| 3.1 Quantitative claims sourced | §1 figures trace to §4/§6/§13 (7,585.50, 7,599.96, +5.2% May, Shiller 42.78 → 24/7 Wall St). §12/§14 carry unsourced numbers: WTI ~$90.82, NAAIM ~98, AAII 35.6%, DAX 25,104→25,357, ISM 54 (§13c gives 54 vs 53.2 without a source), Core PCE +3.3%. Counter levels checked against slices: USDX ~99 consistent (99.22 close); VIX "≈16, ticking up on 2 Jun" — slice VIX 2 Jun closed 16.85, down from 17.14 on 1 Jun; the up-tick was 1 Jun, not 2 Jun. | §1, §12, §14, §13c; VIX/USDX slices | 3 | Source §14 positioning and energy figures; correct the VIX 2 Jun direction |
| 3.2 Citations exist & contain data | Three spot-checks. (a) S&P Dow Jones via FRED, 1 Jun close 7,599.96 — dated, figure reused consistently in §1/§6/§8/§20: consistent. (b) Investing.com, 1 Jun, "O 7,595.40 / range 7,582.99–7,620.90", class Core, cash index — but §5 states "Intraday open/high/low for the two most recent sessions were reconstructed from the SPDR S&P 500 ETF series" and §19 states "direct two-source index-level intraday O/H/L for 27–28 May and 1–2 June could not be obtained": the citation is self-contradictory (same fields both directly sourced and ETF-synthesised). (c) CNBC, **31 May**, "S&P 500 closes at a record to kick off June trading", quote "closes at a record … tech rally overpowers oil spike": 31 May 2026 is a Sunday; the record close and the oil spike it describes are dated 1 Jun in §4/§6/§13c — impossible date. Under brief §3.2 a wrong-date/self-contradictory citation counts as fabricated. Documented verbatim: `CNBC | 31 May | S&P 500 closes at a record to kick off June trading | Media | Bullish | "closes at a record ... tech rally overpowers oil spike"`. | §4 rows 1, 4; §5; §19; §13a row 1 | 1 | Hallucinated-source override applied (C3 → 0). Re-date/replace the CNBC citation; make the 1 Jun O/H/L attribution consistent with §5/§19 |
| 3.3 Calculations transparent | RSI2: helper recomputation from the report's own closes gives n/a, n/a, 100.0, 100.0, 57.9 — the last three rows reproduce exactly. Trend labels follow the rule in all five rows. Pivots: daily P/R1–R3/S1–S3 reproduce from the report's 1 Jun H/L/C (7,620.90/7,582.99/7,599.96) to ±0.01; weekly reproduces from H 7,596.09 / L 7,497.29 / C 7,580.06. **ATR(14) is never stated** — only implied via "1.3× ATR" and "3×ATR cap" (≈66.43). KER stated (+0.349). §21a lists weighted contributions (+0.18, +0.12, +0.08, +0.03, +0.03, −0.03 = +0.41 ≈ +0.40) but not the raw signal values or the weights 0.25/0.20/0.10/0.15/0.15/0.15. | §6 note; §11; §9; §21a; helper output | 3 | State ATR(14) numerically in §9; show signal × weight per component in §21a |
| 3.4 Numbers reconcile | Internally: D-1 close 7,585.50 identical in §1/§3/§6/§21b entry; §11 pivots = card levels; RSI2 §6 (57.9) = §8 (~58). Externally (Category 3 failure per brief §4): 2 Jun close 7,585.50 vs slice cash 7,615.80 (Δ −30.30, > 10 pts); 2 Jun H 7,602.10 vs 7,624.6 (Δ −22.5) and L 7,560.40 vs 7,588.3 (Δ −27.9); 28 May close 7,561.22 vs 7,572.5 (Δ −11.28, > 10 pts); 1 Jun O and L off by +20.2 / +14.5. Daily pivots are computed from 1 Jun, not D-1 (slice D-1 P 7,609.57 vs report 7,601.28). Cross-report: the 2026-06-01 report states CNBC-corroborated closes 27 May 7,520.36 and 28 May 7,563.63; this report replaces them with ETF-derived 7,519.74 / 7,561.22. Card text: Trade 1 "TP1 region near daily R1 / 1 Jun ATH 7,620.90" — TP1 is 7,671.86, 51 pts above; Trade 2 "TP1 +1R / TP2 +2R" — with R = 43.47, TP1 is +0.42R and TP2 +0.87R. | §6 vs helper; §11; §21b; prior report §6 | 1 | See §5 reconciliation log |
| 4.1 Pillars conclude | §8 ends "Bullish continuation (with reversal-risk flag)"; §9 "Bias: Bullish"; §10 each counter has a Status/Implication and a closing synthesis; §12 items individually labelled price-supportive/negative but no section-level direction; §14 has no concluding direction label. | §8, §9, §10, §12, §14 | 3 | Add a closing direction label to §12 and §14 |
| 4.2 Peer/cross-asset interpreted | §10 gives mechanisms (dollar → financial conditions/translation; VIX → hedging demand; DAX → common global-risk factor) with status and implication, not a correlation list. One mechanism rests on a VIX 2 Jun up-tick that the VIX slice does not show at the close. | §10 table and note | 4 | Correct the VIX 2 Jun observation |
| 4.3 Synthesis reconciles tensions (incl. card construction) | §15/§16/§18 do reconcile short-term exhaustion vs the Trending-Bullish regime, KER vs regime, and §17 vs §21a (both cautiously long). Card construction against M5 (brief §3): **Trade 1** stop 7,499.14 is described as "below 27 May swing low" but sits 1.85 pts *above* it (7,497.29); no 0.25×ATR buffer; not the "tighter of (swing extreme, nearest S/R)" — nearest support 7,562.12 (§8) would give a far tighter stop; R = 1.3×ATR > 1×ATR without an explicit wide-stop flag; anchor 00:00 UK. **Trade 2** in a TREND regime should be entry P + 0.10×(R1−P) = 7,603.11, stop P − 0.8×(P−S1) = 7,585.59, TPs R1/R1.5/R2 = 7,619.58/7,629.39/7,639.19; the card instead uses entry at P, stop at the weekly pivot, ladder R1/R2/R3, and labels them "+1R/+2R" incorrectly; the buy limit 7,601.28 is *above* the report's own D-1 close 7,585.50 (a "pullback" limit that would fill immediately). **Trade 3A** swing 27 May low → 1 Jun high = 123.61 pts is below the 2×ATR qualification (2×66.43 = 132.86; the report's own §21c suppresses 27 May for exactly this reason); entry at 38.2% instead of 57.5%; ladder shifted (TP1 = 0% level, TP2 = 100% ext); stop buffer 0.20×ATR not 0.25×ATR; non-standard tranche rule replaces the entry+0.2R rule. | §15–§18, §21a, §21b, §21c | 2 | Rebuild all three cards to the M5 templates (see feedback) |
| 4.4 Calibrated language | §17 is exactly one sentence with a single conditional, no hedge stacking; confidence Medium stated in §3/§18; §21a notes "size accordingly". | §3, §17, §18, §21a | 5 | none |
| 5.1 Data dated; staleness flagged | Every price row and article is dated; single-source O/H/L flagged in §6 and §19. The 2 Jun close is flagged "indicative (intraday)" in §6/§19 but presented without that flag in §1 ("closed the prior completed session at 7,585.50"), §3 ("Regular cash-session last close (2 Jun)") and §21b. | §1, §3, §6, §19, §21b | 3 | Carry the indicative flag into §1/§3/§21b or replace with the completed close |
| 5.2 Assumptions up front | §20 states the 00:00 UK anchor but no proxy-open override caveat appears on the Trade 1 card (it says "Market at 00:00 UK reference / on session open" with no caveat). Single-source propagation is contradictory: §11 says "Daily prior-period H/L/C (1 Jun) corroborated — levels actionable" while §5/§19 say 1 Jun O/H/L are ETF-reconstructed and indicative; Trade 2 caveat mentions only the monthly pivots. ETF→index factor ≈10.02 is disclosed. | §5, §11, §19, §20, §21b | 2 | Put the anchor-override caveat on the card; propagate the 1 Jun H/L indicative status to §11 and the cards |
| 5.3 Red flags surfaced | §12/§15 list valuation, oil/inflation, positioning, VIX up-tick; §13d event collision (5 Jun payrolls) is carried into all three card caveats and §18. | §12, §13d, §15, §21b | 5 | none |
| 5.4 Restrictions honoured | No bracketed variable names, module codes or framework name; instrument common names used; futures used as cross-check only; no retail CFD quotes in the basis. Breached: a synthesised/interpolated price presented as sourced — (i) the 2 Jun close ≈7,585.5 is derived from "−0.19% (~−14 pts)" in an intraday article and presented in §1/§3/§21b as the completed cash close and used as the MARKET entry; (ii) ETF-scaled 1 Jun H/L are declared corroborated in §11 and drive the daily pivots and Trade 2/3A levels. | §1, §3, §4 row 5, §5, §11, §19, §21b | 1 | Restriction-breach override applied (C1 −1 level). Never present a derived or ETF-scaled level as a corroborated close/pivot input |

## 2. Category roll-up

| Category | Level | Multiplier | Points | Justification |
|---|---|---|---|---|
| C1 Prompt adherence (20) | 3 | 0.65 | 13.0 | Rows 3/3/5 → mean 3.67 → 4; restriction-breach override drops one level → 3. Anchor 00:00 UK vs 07:00 UK; D-1 session not covered to its close. |
| C2 Structure (20) | 5 | 1.00 | 20.0 | Rows 5/4/5 → mean 4.67 → 5. All 21 sections with 13a–d and 21a–d present and ordered; §6 lacks only the Final column. |
| C3 Accuracy & evidence (25) | 0 | 0.00 | 0.0 | Rows 3/1/3/1 → mean 2.0 → 2; hallucinated-source override sets C3 = 0. D-1 close wrong by 30.3 pts; CNBC citation impossibly dated; Investing.com attribution contradicted by §5/§19. |
| C4 Reasoning & judgment (20) | 3 | 0.65 | 13.0 | Rows 3/4/2/5 → mean 3.5; framework §9 tiebreak to the lower level → 3. Synthesis sound; all three cards deviate from the M5 templates. |
| C5 Currency, restrictions & transparency (15) | 3 | 0.65 | 9.75 | Rows 3/2/5/1 → mean 2.75 → 3. Dates present and flags exist in §6/§19 but not propagated to §1/§3/§11/§21b; synthesised prices presented as sourced. |
| **Total** | | | **55.75 → 56** | |

## 3. Total, band, override check

- Total: **56/100** (13.0 + 20.0 + 0.0 + 13.0 + 9.75 = 55.75 → 56).
- Band: **Low** (40–59).
- Overrides: **hallucinated_source** — §13a `CNBC | 31 May | "S&P 500 closes at a record to kick off June trading"` is dated a Sunday two sessions before the close and oil spike it quotes (both 1 Jun per §4/§6/§13c), and the §4 `Investing.com | 1 Jun | O 7,595.40 / range 7,582.99–7,620.90 | Core` citation is contradicted by §5/§19, which state those fields were ETF-reconstructed. Per brief §3.2 these count as fabricated: C3 = 0, total capped at 59 (56 is already inside the cap). A **restriction breach** also applies (interpolated 2 Jun close and ETF-scaled 1 Jun H/L presented as sourced/corroborated and used for entries and pivots): C1 reduced from 4 to 3; the Moderate cap (74) is not binding. The CSV override field records the binding override, `hallucinated_source`.

## 4. Card Integrity

Linter rows (`qa/regen_20260906_qa1/lint_static/2026-06-03.csv`, verbatim):

| card_id | report_date | strategy | flags | dud |
|---|---|---|---|---|
| 2026-06-03_Trade_1 | 2026-06-03 | Trade 1 - Daily Directional | CLEAN | False |
| 2026-06-03_Trade_2 | 2026-06-03 | Trade 2 - Pivot (buy limit daily P) | CLEAN | False |
| 2026-06-03_Trade_3A | 2026-06-03 | Trade 3A - Momentum-Pullback (38.2% fib) | CLEAN | False |

| Card | #DUD | #WARN | Integrity = 100 − 40·DUD − 10·WARN | Suppressed |
|---|---|---|---|---|
| 2026-06-03_Trade_1 | 0 | 0 | 100 | no |
| 2026-06-03_Trade_2 | 0 | 0 | 100 | no |
| 2026-06-03_Trade_3A | 0 | 0 | 100 | no |

Report-level Card Integrity (mean over non-suppressed cards): **100.0**. n_cards = 3, n_duds = 0, n_warns = 0.

Note: the static linter validates each card against the report's own stated D-1 close (7,585.50) and its own R; it does not see that the stated close is 30.3 pts from the slice, that Trade 2's buy limit sits above the report's own close, or the M5 template deviations recorded in row 4.3. Those are scored in Category 4 and listed in the feedback file, not in the integrity number.

## 5. Data reconciliation log

Tolerances (brief §4): close |Δ| ≤ 3 consistent; open/high/low |Δ| ≤ 8 consistent; close |Δ| > 10 = Category 3 failure. Slice values are cash-session (16:30–23:00 broker) CFD bars; delta = report − slice.

| Section | Field | Report value | Slice value | Delta | Verdict |
|---|---|---|---|---|---|
| §6 | 27 May Open | 7,523.95 | 7,531.0 | −7.05 | consistent (basis) |
| §6 | 27 May High | 7,528.96 | 7,536.0 | −7.04 | consistent (basis) |
| §6 | 27 May Low | 7,497.29 | 7,504.3 | −7.01 | consistent (basis) |
| §6 / §8 | 27 May Close | 7,519.74 | 7,528.5 | −8.76 | discrepancy (> 3); prior report (2026-06-01) had 7,520.36 CNBC-corroborated |
| §6 | 28 May Open | 7,517.63 | 7,525.0 | −7.37 | consistent (basis) |
| §6 | 28 May High | 7,566.73 | 7,576.2 | −9.47 | discrepancy (> 8) |
| §6 | 28 May Low | 7,507.41 | 7,515.5 | −8.09 | discrepancy (marginal, > 8) |
| §6 | 28 May Close | 7,561.22 | 7,572.5 | −11.28 | **failure (> 10)**; prior report had 7,563.63 CNBC-corroborated |
| §6 | 29 May Open | 7,574.25 | 7,581.1 | −6.85 | consistent (basis) |
| §6 / §8 / §11 (weekly H) | 29 May High | 7,596.09 | 7,601.8 | −5.71 | consistent (basis) |
| §6 / §8 (support) | 29 May Low | 7,562.12 | 7,567.9 | −5.78 | consistent (basis) |
| §6 / §5 / §19 | 29 May Close | 7,580.06 | 7,584.8 | −4.74 | discrepancy (> 3, basis-sized); agrees with prior report |
| §6 / §4 | 1 Jun Open | 7,595.40 | 7,575.2 | +20.20 | discrepancy |
| §6 / §4 / §8 / §11 (pivot H) / §21b | 1 Jun High | 7,620.90 | 7,623.6 | −2.70 | consistent |
| §6 / §4 / §11 (pivot L) | 1 Jun Low | 7,582.99 | 7,568.5 | +14.49 | discrepancy |
| §1 / §4 / §6 / §11 (pivot C) | 1 Jun Close | 7,599.96 | 7,606.0 | −6.04 | discrepancy (> 3, basis-sized) |
| §6 | 2 Jun Open (D-1) | 7,598.20 | 7,590.8 | +7.40 | consistent |
| §6 | 2 Jun High (D-1) | 7,602.10 | 7,624.6 | −22.50 | discrepancy |
| §6 | 2 Jun Low (D-1) | 7,560.40 | 7,588.3 | −27.90 | discrepancy |
| §1 / §3 / §6 / §11 narrative / §21b Trade 1 entry | 2 Jun Close (D-1) | 7,585.50 | 7,615.8 (full-day 23:45 close 7,621.3) | −30.30 | **failure (> 10)** — intraday snapshot presented as the completed close; direction of the day inverted (slice: +9.8 on the day, report: −14.5) |
| §6 | RSI2 2 Jun | 57.9 | 100.0 (slice closes) / 57.9 (report's own closes) | — | arithmetic reproduces from the report's closes; value wrong only because the close is wrong |
| §6 | RSI2 29 May, 1 Jun | 100.0, 100.0 | 100.0, 100.0 (both bases) | 0 | consistent |
| §6 | RSI2 27 May, 28 May | 97.4, 97.0 | 3.82, 100.0 (slice); n/a from report closes | — | not reproducible from data in the report (needs 22/26 May closes); with the prior report's 26 May close 7,519.12 both rows would compute to 100 |
| §9 / §21b | ATR(14) | not stated (implied 66.43) | 63.86 cash / 72.51 full-day | +2.57 vs cash | consistent in magnitude; stated value missing (row 3.3) |
| §11 | Daily P | 7,601.28 (from 1 Jun) | 7,609.57 (from D-1 cash) | −8.29 | deviation: wrong prior period (1 Jun instead of D-1 = 2 Jun); reproduces exactly from the report's own 1 Jun H/L/C |
| §11 | Daily R1 / S1 | 7,619.58 / 7,581.67 | 7,630.83 / 7,594.53 | −11.25 / −12.86 | as above |
| §11 | Weekly P / R1 / S1 | 7,557.81 / 7,618.34 / 7,519.54 | 7,563.63 / 7,622.97 / 7,525.47 | −5.82 / −4.63 / −5.93 | consistent (basis); reproduces from report H 7,596.09 L 7,497.29 C 7,580.06 |
| §11 | Monthly P | 7,457.72 | 7,454.7 (May cash) | +3.02 | consistent; flagged indicative in report |
| §9 / §10 | VIX 2 Jun | "≈16, ticking up on 2 Jun" | 1 Jun 17.14 → 2 Jun 16.85 (down); level 16.5–17.4 | — | direction of the 2 Jun move not supported at the close |
| §10 / §14 | USDX | "~99, flat" | 99.19 → 99.22 | — | consistent |
| §21b Trade 1 | MARKET entry | 7,585.50 | D-1 cash close 7,615.8 | −30.30 | entry does not equal the D-1 close on the slice basis |
| §21b Trade 2 | BUY LIMIT vs D-1 close | 7,601.28 vs report close 7,585.50 | vs slice close 7,615.8 | — | above the report's own D-1 close (wrong side for a long limit on the report's basis); below the slice close |
| §21b Trade 3A | swing 27 May L → 1 Jun H | 123.61 pts | 120.3 pts (7,504.3 → 7,624.6) | — | below 2×ATR on both bases (132.86 report basis; 127.7 slice basis) |
