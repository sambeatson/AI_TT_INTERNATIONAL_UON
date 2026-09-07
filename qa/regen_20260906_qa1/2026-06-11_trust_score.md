# Trust Score — 2026-06-11 — SP500_Report_11Jun2026.md

## 1. Section 7 checklist

| Item | Reviewer notes | Evidence observed | Score 0–5 | Action required |
|---|---|---|---|---|
| 1.1 Variables respected | Asset is the S&P 500 cash index (not ES); counters listed USDX · VIX · DAX 40 with USDX first; as-of the 10-Jun NY cash close, America/New_York; 5-session execution / 25-session regime lookback; USD index points; daily-open anchor stated as 07:00 UK and the card carries broker 09:00 (= UK+2). Source stack is thin for the ">= 6 sources across index-provider / exchange / sell-side tiers" variable: §4 has six rows but only five distinct outlets (TheStreet twice), and §5 leans on "StreetStats", which appears in no source table and in no §20 attempt log. | §2, §4, §5, §10, §13, §20, §21b | 3 | Rebuild §4 to six distinct, named outlets with tier labels; delete or properly cite "StreetStats". |
| 1.2 Coverage & currency consistent | Every price and event date is 10-Jun or earlier; the session is D = 11-Jun; units are index points / USD throughout with no FX or basis drift. Only lapse: the Reuters survey in §13a is dated "Jun" with no day. | §2, §4, §6, §13, §21 | 4 | Date the Reuters survey row to a specific day <= 10-Jun. |
| 1.3 Audience & tone | Senior US Equity Strategist register held throughout; framed for trading and risk review; no retail phrasing, no promotional language, no advice framing. | §1, §12, §16, §18 | 5 | None. |
| 2.1 Sections present & ordered | All of §1–§21 present in the prescribed order, including §13a/b/c/d and §21a/b/c/d. §17 is a single sentence; §19 and §20 both present. | Headings, whole report | 5 | None. |
| 2.2 Scorecard as a table | §6 is a table but omits the Source A / Source B / Final columns — corroborating sources are pushed into a footnote. §11 daily table carries six levels per side (R5–R1.5 / S1–S5) rather than the required three (R3→P→S3), and R1.5 is printed below R1 so the resistance column is not monotonic. Monthly pivots absent with no toggle note. Weekly table is correctly three-per-side. | §6, §11 | 2 | Restore Source A/Source B/Final columns in §6; re-cut §11 daily to R3→P→S3 in order; add the monthly table or state the toggle is NO. |
| 2.3 Method steps visible | §4→§5 runs observations → classification → weighted-median consensus; §8 is candle-by-candle plus an explicit sequence assessment; §9 names persistence, overlap and VOLator, though only qualitatively (the 10-Jun report gave overlap 0.448 / persistence 0.522 as numbers); §7 charts are pandoc image placeholders, accepted as evidence and noted. | §4–§9 | 4 | State persistence / overlap numerically in §9 as prior reports do. |
| 3.1 Quantitative claims sourced | CPI figures carry (BLS); §14 points back to §10/§13d; §1 numbers trace to §4/§6. Unsourced and unreconciled: VIX "close 22.22" / "22.2" repeated in §9, §10 and §14 (counter slice D-1 cash close 20.28, last M15 bar 20.43); "PPI ran 3.9% y/y"; "index ex-AI roughly flat year-to-date" attributed only to "strategists"; "Russell 2000 relative resilience" with no reference. | §9, §10, §12, §13d, §14 | 2 | Source or drop the VIX level, the PPI figure, the ex-AI breadth claim and the Russell 2000 claim. |
| 3.2 Citations exist & contain data | Three spot-checks. (a) S&P DJI via FRED, 08-Jun, 7,405.73 — used consistently in §5, §6 and §21c: PASS. (b) Investing.com, 09-Jun, 7,385.48 — the report itself states twice that the Investing.com cached table terminates at 04-Jun (§19 "the cached aggregator table terminated at 04 June"; §20 "cached table 05-May→04-Jun"), yet §4 quotes it for a precise 09-Jun close and the §6 footnote names it as the 05-Jun and 09-Jun corroborator: self-contradictory citation, counts as fabricated. (c) "StreetStats" (§5) is used to claim two-source corroboration of the 08-Jun close and appears nowhere in §4 or §20: unverifiable source name. | §4, §5, §6 footnote, §19, §20 | 0 | Remove the Investing.com attributions for 05/09-Jun and the "StreetStats" claim; re-derive the corroboration pairs from sources actually held. |
| 3.3 Calculations transparent | Daily pivots reproduce exactly from the report's own 10-Jun H 7,345 / L 7,250 / C 7,266.99 (P 7,287.33, R1 7,324.66, S1 7,229.66, R2 7,382.33, S2 7,192.33, R3 7,419.66, S3 7,134.66, R1.5 7,353.49, S1.5 7,210.99): PASS. §21a contributions sum to −0.61 as stated. Failures: RSI2 does not reproduce from the report's own close column (helper: 08-Jun 9.9 vs stated 22.8; 09-Jun 52.1 vs stated 17.6; 10-Jun 0.0 vs stated 4.8); weekly R3 is 7,776.66 against 7,810.66 from its own H/L/C; the §13b tilt −0.55 is not derivable from its own stated method (5 bearish + 1 mixed in §13a → −0.83); the Kaufman contribution is +0.02 although §9 classes KER −0.139 as Trending Down — Strong, i.e. the sign is inverted against its own weight mapping. ATR(14)=81.56 and KER stated. | §6, §9, §11, §13b, §20, §21a | 1 | Recompute the RSI2 column and the weekly R3; restate the §13b tilt so it reproduces from the article table; correct the sign of the Kaufman contribution. |
| 3.4 Numbers reconcile | D-1 close 7,266.99 is consistent across §1, §3, §4, §6 and the §11 inputs. Breaks: card entry is 7,267.45, equal to neither the validated close (7,266.99) nor the slice cash close (7,271.70), although the entry is MARKET; §6 RSI2 disagrees with the 10-Jun report for the same sessions (08-Jun 22.8 vs 9.9; 09-Jun 17.6 vs 53.5; 04-Jun 57.8 vs 35.3) and the 09-Jun close itself moved 7,386.65 → 7,385.48, outside the ±0.10-pt tolerance both reports claim; §13a lists six articles, §13b counts five; §11 narrative says the close sits "just below daily S1" when 7,266.99 is above S1 7,229.66; §15 cites "VIX expansion (§11/§10)" where §11 is the pivot section. | §1–§6, §11, §13, §15, §21b, cards JSON | 1 | Reconcile the RSI2 column against the prior report and the close series; fix the §13a/§13b count; fix the §11 position sentence and the §15 cross-reference; set the MARKET entry to the validated D-1 close. |
| 4.1 Pillars conclude | §8 ends "Bearish continuation"; §9 "Bias: Bearish"; §10 "Aggregate cross-asset confirmation: CONFIRM"; §14 blocks carry direction labels. Two defects: the §12 "Substitution / breadth" block is the only one with no price-direction label, and §9's regime conclusion (Transitional) is contradicted by §21b Trade 3A, which asserts "TREND_DOWN regime". | §8, §9, §10, §12, §14, §21b | 3 | Label the §12 breadth block; make the regime label in §21b identical to §9. |
| 4.2 Peer/cross-asset interpreted | §10 gives transmission mechanisms rather than a correlation list — dollar → financial conditions and earnings translation; VIX → de-grossing; DAX → shared global risk factor — each with a status and an implication. Weakened only by the misstated VIX level. | §10 | 4 | Correct the VIX level; mechanisms may stand. |
| 4.3 Synthesis reconciles tensions | §15/§16/§18 balance bull and bear and give an explicit invalidation zone, and §21a states no conflict with §17. But the central tension is left unresolved and propagates into the cards: §9 calls the regime Transitional (and §21a's regime contribution −0.10 = −0.5 × 0.20 is precisely the M5 Transition mapping), while §21b builds Trade 3A, which M5 §3/§5.3a reserve for TREND_UP/TREND_DOWN — under TRANSITION the fork is Trade 3C. Trade 2 is then suppressed on the ground that "regime is Transitional/Trend-down, not RANGE", which is not an M5 suppression trigger (M5 §5.2c gives TRANSITION a breakout-side Trade 2; §6 lists only all-tiers-indicative or a missing surface value as suppression grounds), and its SUPPRESSED row is missing from the card set entirely. Trade 1's stop takes only the 5-day swing-high branch of M5 §4c and declares the 3.5×ATR cap binding, ignoring the nearest-resistance branch (§8's own 7,431 shelf), which is far tighter. | §9, §15–§18, §21a, §21b, M5 §3/§4c/§5.2c/§5.3a | 1 | Resolve the regime label once and rebuild the §21b fork from it; apply M5 §4c both-branch stop selection; emit the Trade 2 SUPPRESSED row with an M5-valid reason. |
| 4.4 Calibrated language | §17 is exactly one sentence and does not hedge-stack; confidence High is stated in §3 and repeated in §18; §21d carries the small-sample limitation boilerplate. | §3, §17, §18, §21d | 5 | None. |
| 5.1 Data dated; staleness flagged | Every §4/§6/§13 row carries a date and §19 flags the 05/09/10-Jun intraday extremes as single-vendor indicative. Undercut by §6 itself, whose Validation column reads "Corroborated" on all five rows including the three the footnote and §19 call indicative, and by the undated Reuters survey. | §4, §6, §13, §19 | 3 | Make the §6 Validation column say "Close corroborated · O/H/L indicative" on those three rows. |
| 5.2 Assumptions up front | §20 records the operator anchor override and the 10-Jun t−1 anchor; §11 and §21b both propagate the single-source-indicative pivot flag; the Trade 1 card discloses the ATR-cap size reduction and the wide stop. | §11, §19, §20, §21b | 4 | None material; keep the propagation wording once §21b is rebuilt. |
| 5.3 Red flags surfaced | §12 and §15 both carry live risks with the highest-impact event named; §13d Fedspeak collision is carried into the caveat line of both produced cards; wide-stop and "TP2 ambitious" flags are present as M5 §5.1 requires. | §12, §15, §13d, §21b | 5 | None. |
| 5.4 Restrictions honoured | ES futures are confirmation-only (§5); no retail CFD quote enters the OHLC basis; no bracketed variable names, module codes or framework name appear; instruments use common names. BREACH: §19 states "No value in this report was synthesised" in the same paragraph that admits the last three sessions' extremes "were reconstructed from market-wrap closes plus directional intraday colour", and those reconstructed values are presented in the "Validated OHLC" table under Validation = "Corroborated". Synthesised prices presented as sourced is an explicit prompt restriction. | §5, §6, §19 | 1 | Either drop the reconstructed O/H/L or present them as estimates outside the validated table; remove the blanket no-synthesis assertion. |

## 2. Category roll-up

| Category | Level | Multiplier | Points | Justification |
|---|---|---|---|---|
| C1 Prompt adherence (max 20) | 3 | 0.65 | 13.00 | Rows 1.1–1.3 mean 4.0; reduced one level by the restriction-breach override (synthesised O/H/L presented as corroborated, §6/§19). |
| C2 Structural alignment (max 20) | 4 | 0.85 | 17.00 | Rows 2.1–2.3 mean 3.67 → 4. All sections present and ordered; §6 column set and §11 daily pivot layout are malformed. |
| C3 Accuracy & evidence (max 25) | 0 | 0.00 | 0.00 | Rows 3.1–3.4 mean 1.0; set to 0 by the hallucinated-source override (Investing.com quoted for 09-Jun against its own stated 04-Jun cutoff; "StreetStats" uncitable). RSI2 also fails to reproduce from the report's own closes. |
| C4 Reasoning & judgment (max 20) | 3 | 0.65 | 13.00 | Rows 4.1–4.4 mean 3.25 → 3. Mechanisms and calibration are strong; the regime label contradiction drives a non-compliant §21b fork and an M5-invalid Trade 2 suppression. |
| C5 Currency, restrictions & transparency (max 15) | 3 | 0.65 | 9.75 | Rows 5.1–5.4 mean 3.25 → 3. Dating and red-flag disclosure are good; the no-synthesis restriction is openly breached. |
| **Total** | — | — | **52.75 → 53** | Sum of category points, rounded. |

## 3. Total, band, override check

- Pre-override total (C1 4, C2 4, C3 1, C4 3, C5 3): 17.00 + 17.00 + 5.00 + 13.00 + 9.75 = 61.75 → 62.
- Overrides applied, both triggered:
  - **Hallucinated source** — §4 attributes a precise 09-Jun close (7,385.48) to Investing.com and the §6 footnote names it as the 05-Jun and 09-Jun corroborator, while §19 and §20 both state that source's cached table ends at 04-Jun; §5 additionally claims 08-Jun corroboration from "StreetStats", a name absent from §4 and from the §20 attempt log. Effect: C3 = 0 and total capped at the Low band (40–59).
  - **Restriction breach** — reconstructed (synthesised) 05/09/10-Jun O/H/L are carried in the "Validated OHLC" table with Validation = "Corroborated" while §19 asserts nothing was synthesised. Effect: total capped at 60–74 and C1 dropped one level (4 → 3).
- Post-override total: **53**. The Low-band cap (<= 59) is not binding at 53; the Moderate cap is superseded by the stricter override.
- **Band: Low (40–59).**
- **Override recorded: hallucinated_source** (restriction_breach also present and applied to C1).

## 4. Card Integrity

Linter rows, verbatim from `qa/regen_20260906_qa1/lint_static/2026-06-11.csv`:

| card_id | report_date | strategy | flags | dud |
|---|---|---|---|---|
| 2026-06-11_Trade_1 | 2026-06-11 | Trade 1 - Daily Directional | WARN_TP3_ORDER\|WARN_TARGET_FAR(2.87xATR) | False |
| 2026-06-11_Trade_3A | 2026-06-11 | Trade 3A - Momentum-Pullback (57.5% rally-sell) | CLEAN | False |

Per-card integrity:

| Card | #DUD | #WARN | Integrity |
|---|---|---|---|
| 2026-06-11_Trade_1 | 0 | 2 | 100 − 0 − 20 = 80 |
| 2026-06-11_Trade_3A | 0 | 0 | 100 |
| **Report mean (non-suppressed)** | 0 | 2 | **90.0** |

This date emits **fewer than three cards**: the lint file carries two rows. Trade 2 is discussed as suppressed in §21b prose but produces no card row, so M5 §6 / §21b ("suppressed trades produce a SUPPRESSED row, not an omission") is not satisfied at the card-set level. Suppressed rows are excluded from the integrity mean by definition, so the mean stands at 90.0 over the two produced cards.

M5 assessment of each card (feeds row 4.3, not the integrity number):

- **Trade 1 (SHORT, MARKET @ 07:00 UK)** — anchor explicit and correct; three equal units, BE+0.2R on TP2 fill and a session-close/3×ATR runner all present; wide-stop and TP2-ambitious flags present per M5 §5.1. Defects: stop selection used only the 5-day swing-high branch of M5 §4c and declared the 3.5×ATR cap binding, ignoring the nearest-resistance branch; R = 285 pts exceeds the static bound R <= 3.0×ATR14 (258.4 on the slice, 244.7 on the report's own 81.56) and TP1 sits 2.87×ATR away against a 2.5×ATR limit; tp3 = 6,900.0 lies between TP2 (6,696.1) and TP1 (6,981.5) instead of beyond TP2; entry 7,267.45 does not equal the validated D-1 close; the U3 trail is labelled "entry +0.2R" while the quoted 7,210 is entry − 0.2R; thesis invalidation (7,455) sits inside the stop, whereas M5 §5.1 asks for the next structural level beyond it.
- **Trade 2 (Pivot, regime-aware)** — suppressed on a ground M5 does not recognise ("regime is not RANGE"); under TRANSITION, M5 §5.2c specifies a breakout-side-only Trade 2 aligned with 3C. No card row emitted.
- **Trade 3A (SHORT, SELL LIMIT)** — internally arithmetic-clean (57.5% of its own swing = 7,463; stop = 7,620.90 + 0.25×81.56 = 7,641; 38.2% = 7,392; R = 178 pts = 2.18×ATR, inside every static bound) and the limit sits on the correct side of the D-1 close, hence CLEAN. But it is the wrong variant for the regime the report itself declares (M5 §3 sends TRANSITION to 3C), its 100% anchor is the 10-Jun 7,250 rather than the actual 09-Jun fractal low, its TP3 is an "≈7,000 area" rather than the computed 100% extension, and the lookback actually used is not logged as M5 §4b requires.

## 5. Data reconciliation log

Slice basis: `data/slices/US500/US500_upto_2026-06-10.csv`, cash session 16:30–23:00 broker. Tolerance per brief §4: |Δ| <= 3 pts on a close, <= 8 pts on an open/high/low.

| Section | Report value | Slice value | Delta | Verdict |
|---|---|---|---|---|
| §6 04-Jun Open | 7,516.54 | 7,541.30 | −24.76 | FAIL (>8) |
| §6 04-Jun High | 7,598.19 | 7,604.30 | −6.11 | OK |
| §6 04-Jun Low | 7,516.54 | 7,535.00 | −18.46 | FAIL (>8) |
| §6 04-Jun Close | 7,584.31 | 7,592.70 | −8.39 | FAIL (>3) |
| §6 05-Jun Open | 7,561.00 | 7,540.50 | +20.50 | FAIL (>8) |
| §6 05-Jun High | 7,561.00 | 7,545.30 | +15.70 | FAIL (>8) |
| §6 05-Jun Low | 7,360.00 | 7,372.80 | −12.80 | FAIL (>8) |
| §6 05-Jun Close | 7,383.74 | 7,392.50 | −8.76 | FAIL (>3) |
| §6 08-Jun Open | 7,388.00 | 7,451.80 | −63.80 | FAIL (>8) |
| §6 08-Jun High | 7,431.00 | 7,471.30 | −40.30 | FAIL (>8) |
| §6 08-Jun Low | 7,372.00 | 7,398.80 | −26.80 | FAIL (>8) |
| §6 08-Jun Close | 7,405.73 | 7,411.00 | −5.27 | FAIL (>3) |
| §6 09-Jun Open | 7,402.00 | 7,454.40 | −52.40 | FAIL (>8) |
| §6 09-Jun High | 7,430.00 | 7,486.40 | −56.40 | FAIL (>8) |
| §6 09-Jun Low | 7,320.00 | 7,243.10 | +76.90 | FAIL (>8) — largest single break; the session the report calls a "deep intraday plummet" is stated 77 pts above the actual low |
| §6 09-Jun Close | 7,385.48 | 7,387.30 | −1.82 | OK |
| §6 10-Jun Open | 7,340.00 | 7,351.10 | −11.10 | FAIL (>8) |
| §6 10-Jun High | 7,345.00 | 7,400.70 | −55.70 | FAIL (>8) |
| §6 10-Jun Low | 7,250.00 | 7,271.50 | −21.50 | FAIL (>8) |
| §6 10-Jun Close (anchor) | 7,266.99 | 7,271.70 | −4.71 | FAIL (>3), inside the 10-pt hard-failure threshold |
| §6 RSI2 04-Jun | 57.8 | 35.21 (slice closes) | +22.59 | FAIL — label flips Neutral→Bullish |
| §6 RSI2 05-Jun | 8.2 | 12.08 (slice closes) | −3.88 | Note |
| §6 RSI2 08-Jun | 22.8 | 8.46 (slice) / 9.9 (report's own closes) | +14.34 / +12.90 | FAIL — does not reproduce from the report's own closes |
| §6 RSI2 09-Jun | 17.6 | 43.84 (slice) / 52.1 (report's own closes) | −26.24 / −34.50 | FAIL — from its own closes RSI2 > 50, so Trend must be Neutral, not Bearish |
| §6 RSI2 10-Jun | 4.8 | 0.00 (slice) / 0.0 (report's own closes) | +4.80 | FAIL — does not reproduce from the report's own closes |
| §9 / §20 ATR(14) | 81.56 | 86.13 (cash) / 99.77 (full day) | −4.57 / −18.21 | Note — plausible on the cash basis; the linter's 2.87×ATR warn implies an engine ATR near 99.3 |
| §11 daily pivots (from own H/L/C) | P 7,287.33 · R1 7,324.66 · S1 7,229.66 · R2 7,382.33 · S2 7,192.33 · R3 7,419.66 · S3 7,134.66 · R1.5 7,353.49 · S1.5 7,210.99 | Recomputed from the same H 7,345 / L 7,250 / C 7,266.99 | 0.00 on every level | PASS — reproduces exactly |
| §11 daily pivots vs slice | P 7,287.33 · R1 7,324.66 · S1 7,229.66 | P 7,314.63 · R1 7,357.77 · S1 7,228.57 | −27.30 · −33.11 · +1.09 | FAIL — inherited from the wrong 10-Jun H/L |
| §11 weekly R3 | 7,776.66 | 7,810.66 from the report's own H 7,620.90 / L 7,360.00 / C 7,383.74 | −34.00 | FAIL — does not reproduce from its own inputs |
| §11 weekly P / R1 / S1 / R2 / S2 / S3 | 7,454.88 / 7,549.76 / 7,288.86 / 7,715.78 / 7,194.00 / 7,027.98 | 7,454.88 / 7,549.76 / 7,288.86 / 7,715.78 / 7,193.98 / 7,027.96 | 0.00 except ±0.02 rounding | PASS |
| §11 weekly pivots vs slice week 01–05 Jun | P 7,454.88 · S1 7,288.86 | P 7,463.30 · S1 7,302.00 | −8.42 · −13.14 | Note — basis plus the 7,620.90 vs 7,624.60 high |
| §8 / §21b 5-day swing low | 7,250 (attributed to 10-Jun) | 7,243.10 (09-Jun) | +6.90, wrong session | Value within tolerance, date attribution FAIL |
| §8 5-day swing high | 7,598 (04-Jun) | 7,604.30 (04-Jun) | −6.30 | OK |
| §9 / §21b 25-day high | 7,620.90 (02-Jun) | 7,624.60 (02-Jun) | −3.70 | OK |
| §9 / §14 VIX close | 22.22 / 22.2 | 20.28 (cash close) / 20.43 (last M15 bar) | +1.94 / +1.79 | FAIL — direction (rising) is right, level is not |
| §10 / §14 USDX direction | "firm and rising" | 99.445 (04-Jun) → 100.019 (10-Jun) | — | PASS |
| §21b Trade 1 entry (MARKET) | 7,267.45 (card) / "reference 7,267" | 7,266.99 validated close / 7,271.70 slice close | +0.46 / −4.25 | FAIL — a MARKET entry must equal the D-1 close |
| §13a vs §13b article count | §13b: 4 Bearish + 1 Mixed = 5 | §13a lists 6 articles (5 Bearish + 1 Mixed) | −1 article | FAIL — and the stated tilt −0.55 reproduces from neither count |
| §6 RSI2 vs prior report (10-Jun) | 04-Jun 57.8 · 08-Jun 22.8 · 09-Jun 17.6 | 35.3 · 9.9 · 53.5 in SP500_Report_10Jun2026.md | +22.5 · +12.9 · −35.9 | FAIL — same sessions, three different values |
| §6 09-Jun close vs prior report | 7,385.48 | 7,386.65 in SP500_Report_10Jun2026.md | −1.17 | FAIL — outside the ±0.10-pt tolerance both reports claim |
