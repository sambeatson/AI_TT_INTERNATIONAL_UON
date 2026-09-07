# Trust Score — 2026-06-26 — SP500_Report_26Jun2026.md

Run: regen_20260906_qa1 · Asset US500 · D = 2026-06-26 · D-1 = 2026-06-25
Slice: `data/slices/US500/US500_upto_2026-06-25.csv` (broker CFD M15, cash session 16:30–23:00 broker)
Framework: `docs/AI_Output_Trust_Score_Framework_v3.7.txt` §4–§7, anchored by `qa/regen_20260906_qa1/REVIEWER_BRIEF.md`

## 1. Section 7 checklist

| Item | Reviewer notes | Evidence observed | Score 0–5 | Action required |
|---|---|---|---|---|
| 1.1 Variables respected | Asset is the S&P 500 cash index (^GSPC), not ES futures — correct. Counters are USDX, VIX, DAX 40 with USDX listed first — correct. Unit/currency index points/USD — correct. Six sources in §4 — meets the ≥6 minimum. **Two hard variable violations:** (a) the as-of session is 24 Jun, but D-1 is 25 Jun — the slice carries a complete 25 Jun cash session (O 7427.90 H 7432.60 L 7332.90 C 7365.90); (b) the daily-open anchor is overridden to 00:00 UK against the mandated 07:00 UK for this M1 instance. The 5-session lookback is nominally 5 rows but is the wrong five (17, 18, 22, 23, 24 Jun instead of 18, 22, 23, 24, 25 Jun; 19 Jun Juneteenth is correctly excluded). | §2 "As-of date 24 June 2026 last validated session"; §2 anchor-override note; §6 date column; §20 "Overrides applied" | 2 | Re-anchor the whole report to the 25 Jun cash close (7,365.90 ± basis) and restore the 07:00 UK daily-open anchor. |
| 1.2 Coverage & currency consistent | No currency or unit drift; everything is index points/USD throughout. No data value is dated on or after D. **But the currency of coverage is internally contradictory:** §3 and §5 assert the 25 Jun session was "in progress at preparation", while §20 timestamps preparation at ~21:30 UK — 30 minutes *after* the 21:00 UK / 16:00 ET cash close. §13c is headed "5 sessions to 24 Jun" (should run to D-1) and omits the 25 Jun HIGH-impact US data cluster present in the news slice. §13d lists "Fri 26 Jun PCE follow-through" as upcoming, but Core PCE printed on 25 Jun. | §3, §5, §13c, §13d, §20 timestamp | 2 | Extend coverage to D-1; move the 25 Jun PCE/GDP/durables cluster from §13d to §13c; reconcile the "in progress" claim with the 21:30 UK timestamp. |
| 1.3 Audience & tone | Senior US Equity Strategist byline; institutional register sustained end-to-end; §18 is framed as a trading-and-risk-review judgement with a single named watch item. No retail tone, no promotional framing, no execution exhortation. | §1, §18, §21 caveats | 5 | None. |
| 2.1 Sections present & ordered | All of §1–§21 present in the prescribed order. §13 carries a, b, c, d; §21 carries a, b, c, d. §17 is exactly one sentence. §21d includes the limitations boilerplate. No missing or transposed headings. | Heading scan of the full file | 5 | None. |
| 2.2 Scorecard as a table | §6 is a proper table with Date/O/H/L/C/RSI2/Trend/Source/Validation (Source A and B merged into one column — cosmetic). **§11 pivot tables are malformed:** the daily table stops at S2 (no S3) and crams "S1 / S2" into one cell with a trailing empty column; the weekly table starts at R2 (no R3); monthly pivots have no table at all, only a suppression paragraph. The brief requires 3 levels each side, R3→S3, for daily, weekly and monthly. | §6 table; §11 daily and weekly tables | 2 | Rebuild §11 as three tables, each R3 R2 R1 P S1 S2 S3; render the monthly table with cells marked INDICATIVE rather than omitting it. |
| 2.3 Method steps visible | §4 lists raw observations, §5 classifies and weights them into a consensus with an explicit weighted-median rationale. §8 is candle-by-candle across all five rows and closes with a sequence assessment. §9 states overlap ratio 0.415, persistence 0.55, VOLator slope, median RSI2 and range position. §7 carries five captioned chart placeholders (pandoc image references — accepted as evidence per the brief, noted). | §4–§9 | 5 | None (note that chart images are not renderable in the .md conversion). |
| 3.1 Quantitative claims sourced | §1 numbers trace to §4/§6/§9. **§12 and §14 carry unsourced quantitative claims** with no citation and no pointer to §4/§6/§13: Q1 EPS "+28.9% YoY", Q2 "+22%", forward P/E "~20.7×", Brent "−4.3% to ~$73.7", WTI "~$70.3", 10Y "below 4.5%", JPMorgan 2026 EPS "$350 (2027 $390)", "Gold fell sharply this week". None of these appear in §4 or §13a. | §12 all five bullets; §14 bullets 2 and 3 | 2 | Attach a named, dated source to every figure in §12 and §14, or route it through §4/§13a. |
| 3.2 Citations exist & contain data | Three spot-checks. (a) S&P DJI via FRED, 23 Jun close 7,365.46 — consistent with the §6 23 Jun close and with the 25 Jun report's §4. PASS. (b) Investing.com, 24 Jun close 7,358.22 — used identically in §1, §3, §4, §6, §11 and §21. Internally consistent. PASS. (c) **Yahoo Finance ^GSPC, "24 Jun", 7,475.34, basis "Real-time derived" — impossible.** It exceeds the report's own 24 Jun high (7,428.06, §6) by 47.28 pts; it exceeds the slice's 24 Jun full-day high (7,438.00) and the 25 Jun full-day high (7,438.00) by 37.34; §3 re-dates the same 7,430–7,475 zone to the 25 June session; and the prior day's report cites Yahoo for 24 Jun 16:00 ET at 7,358.22, not 7,475.34. A real-time quote of an index cannot sit 47 pts above that index's own session high. Per brief row 3.2 this is a fabricated citation. | §4 Yahoo row vs §6 24 Jun row; §3 rationale; slice 24/25 Jun highs | 0 | Remove or correctly re-date the Yahoo row and re-derive §4/§5 without it. **Triggers the hallucinated-source override.** |
| 3.3 Calculations transparent | RSI2 is fully reproducible: the helper recomputes 74.3 / 0.0 / 0.0 for 22, 23 and 24 Jun from the report's own closes — exact. 18 Jun's 46.9 reproduces to 46.86 using the 16 Jun close 7,511.35 carried by the 24 Jun report, so all five rows are arithmetically sound on the report's own basis. §11 pivots reproduce to 0.01 on all six levels from the report's own 24 Jun H/L/C. ATR(14)=122.5 and KER(13, EMA-3)=−0.19 are both stated. **Two defects:** ATR 122.5 matches the slice's *full-day* ATR14 (121.04) but not the *cash-session* ATR14 (109.31) that the report's own §2 basis requires — a Δ13.19 basis mismatch; and the §21a direction score does not reconcile — the four contributions shown (−0.25, −0.15, −0.12, +0.09) sum to −0.43, not the stated −0.56, and only 4 of the 6 weighted signals are disclosed. | §6 footnote; helper RSI2 line; §11 arithmetic; §20 ATR/KER; §21a | 3 | Show all six weighted signals so −0.56 sums; recompute ATR14 on the declared cash-session basis. |
| 3.4 Numbers reconcile | The anchor close 7,358.22 is identical in §1, §3, §4, §6 and §18 — internally consistent, though it is the D-2 close. All six §11 pivot levels reproduce exactly on the §21b/§21c cards (7,374.37 / 7,411.91 / 7,465.61 / 7,320.67 / 7,283.13 / 7,234.18). RSI2 in §6 matches §8 row for row. **Failures:** Trade 1's TP3 is labelled "+3R cap; runner exit = session close + 3×ATR cap (≈367 pts)" but is placed at 7,111.20, which is 225.6 pts (3R) from entry, not 367.5 — the card contradicts its own rule text; and §6 claims "CORROB. (Δ0.00)" for whole rows including O/H/L on Investing × FRED, while §20 concedes FRED corroborates *closes* only. | §21b Trade 1 TP3 row; §6 validation column vs §20 bullet 1 | 3 | Fix the Trade 1 runner arithmetic; restrict the Δ0.00 corroboration claim to the close column. |
| 4.1 Pillars conclude | §8 ends "Bearish continuation"; §9 ends "Transitional (bearish lean)" with a Kaufman confirmation; §10 ends with an explicit contradiction flag; §12 labels each bullet with a directional tag. **§14 ends with no direction label at all** — five bullets, no synthesis. More seriously, the §21 pillar's conclusions violate M5 across all three cards: Trade 1 is a stop-entry at the 24 Jun low rather than market at the daily-open anchor, and its stop sits *on* daily R1 with no 0.25×ATR buffer; Trade 2 is a limit fade although §9 declares TRANSITION (breakout side only), is placed at P rather than R1/R1.5/R2, and its TPs are 0.6R/1.0R instead of 1R/2R; Trade 3A uses a 38.2% entry instead of 57.5% on a swing (7,532.17→7,336.82 = 195.35 pts) that fails the ≥2×ATR14 gate on every ATR basis available (218.62 cash, 242.08 full-day, 245.0 on the report's own 122.5), so 3A should not have been produced at all. | §14; §21b all three cards vs brief §3 | 1 | Give §14 a direction label; rebuild all three cards to the M5 geometry set out in the feedback file. |
| 4.2 Peer/cross-asset interpreted | §10 is structurally strong — a per-counter Mechanism column, a Status column, and a contradiction flag that is explicitly carried into §15, §16 and every card caveat rather than resolved silently. **But two of the three counter directions are inverted against the slice.** USDX is stated "Falling (~101.2)"; the slice shows it rising over the window (100.878 on 18 Jun → 101.646 on 24 Jun → 101.433 on 25 Jun) and the D-1 close is 101.433, not ~101.2. VIX is stated "Falling (19.5→18.6)"; the slice shows it rising over the same window (17.90 on 18 Jun → 18.61 on 25 Jun), and 19.5 appears nowhere — the window's highest close is 18.98 and highest high 19.25. The 18.6 endpoint is right; the direction and the start point are not. Since the mechanism is built on "softer dollar / fading hedging demand", the inversion propagates into §1, §14, §16 and the §21a +0.09 cross-asset offset. | §10 table rows 1–2 vs `VIX_upto_2026-06-25.csv`, `USDX_upto_2026-06-25.csv` | 2 | Restate USDX and VIX 5-day direction from the slice and re-derive the §10 Status/Implication columns and the §21a cross-asset term. |
| 4.3 Synthesis reconciles tensions | Genuinely well handled. §15 sets the bullish sell-side reset against crowding/flash-crash risk with named levels on both sides. §16 states plainly that the bearish §9 read is "deliberately moderated by the §10 cross-asset contradiction" and gives two-sided invalidation (close above 7,494 constructive, below 7,234 deeper risk-off). §18 names all three tensions. §21a flags the SHORT score against the §17 consolidation forecast and the bullish institutional case and explicitly declines to edit either output to align. | §15, §16, §18, §21a conflict flag | 5 | None. |
| 4.4 Calibrated language | §17 is exactly one sentence with a single conditional and no hedge stacking. Confidence is stated as Medium in §3 and repeated in §18. §1 gives a bounded consensus (7,358 ± 35) rather than a point claim. Conviction is expressed as a signed score with a stated threshold. | §3, §17, §18, §21a | 5 | None. |
| 5.1 Data dated; staleness flagged | Every §6 row, §4 row and §13a article carries a date; §19 correctly flags the 25 Jun session and all CFD/derived quotes as single-source indicative and excludes them from validated data. **But the single-source-indicative O/H/L flagging required by the brief is absent and actively contradicted:** §6 marks all five rows "CORROB. (Δ0.00)" on Investing × FRED across every column, while §20 states FRED corroborates closes only, and both the 24 Jun and 25 Jun reports marked their O/H/L indicative. The measured O/H/L deltas against the slice (up to −26.74 on the 18 Jun open) are inconsistent with a Δ0.00 two-source corroboration. Separately, the report is a full session stale and does not flag that as a limitation. | §6 validation column; §19; §20 bullet 1; §5 of the 25 Jun report | 2 | Mark O/H/L indicative where only the close is dual-sourced; add a staleness note if D-1 cannot be validated. |
| 5.2 Assumptions up front | The anchor-override caveat is stated twice and early — a dedicated note under §2 naming the substituted anchor and scoping its effect, and again in §20 under Overrides applied. Single-source pivot propagation is handled properly: §11 marks monthly pivots INDICATIVE and excludes them from level placement, §19 restates it per surface, and the Trade 2 card carries the same exclusion in its Caveats row. The assumption chain is traceable from §2 to the card. | §2 note; §11 monthly paragraph; §19 bullet 2; §20; §21b Trade 2 Caveats | 5 | None. |
| 5.3 Red flags surfaced | §12 carries a dedicated price-negative bullet (crowding, flash-crash) and §15 lists six downside risks with levels. §13d collisions are carried into card caveats — Trade 1 explicitly notes "holding period spans §13d month-end rebalance", and the §10 contradiction is repeated on all three cards. **But the collision set is misstated:** the highest-impact item in reach was the 25 Jun US data cluster (Core PCE m/m 0.3 vs 0.1 consensus, GDP q/q 2.1 vs 1.6, Durable Goods −4.5 vs 0.6 — all HIGH/MODERATE in the news slice), which appears in neither §13c nor §13d, and §14 describes PCE as "within expectations" when the slice shows Core PCE m/m and y/y both above consensus. | §12, §15, §13c/§13d vs `news_upto_2026-06-25.csv`; §14 bullet 2 | 3 | Add the 25 Jun US data cluster to §13c and correct the §14 PCE characterisation. |
| 5.4 Restrictions honoured | Clean on most restrictions: no ES futures use, CFD/retail quotes explicitly excluded from the OHLC basis (§5, §19), instrument common names used throughout, no framework name, no M1–M5 module codes. **Hard breach:** §20 prints a bracketed variable name — "Overrides applied: [DAILY_OPEN_ANCHOR] overridden to 00:00 UK" — which the brief's 5.4 restriction list prohibits outright. Compounding: the anchor value itself deviates from the mandated 07:00 UK, and §6 presents O/H/L as sourced-and-corroborated when they are not two-source (a synthesised/unverified field presented as sourced). "v2.1 baseline" in §20 is a weights version tag rather than a module code — noted, not counted. | §20 Overrides bullet (bracketed token); §2 anchor note; §6 validation column | 1 | Delete the bracketed token and name the parameter in prose; restore the 07:00 UK anchor. **Triggers the restriction-breach override.** |

## 2. Category roll-up

| Category | Level | Multiplier | Points | Justification |
|---|---|---|---|---|
| C1 Prompt adherence (max 20) | 2 | 0.40 | 8.00 | Rows 1.1/1.2/1.3 = 2/2/5, mean 3.00 → level 3. Restriction-breach override drops C1 one level → **2**. Driven by the D-2 as-of session, the 00:00 UK anchor substitution and the §13c/§13d coverage slip. |
| C2 Structure (max 20) | 4 | 0.85 | 17.00 | Rows 2.1/2.2/2.3 = 5/2/5, mean 4.00 → level 4. Section inventory and method visibility are complete; the only structural failure is §11, where the daily table omits S3, the weekly omits R3 and the monthly has no table. |
| C3 Accuracy & evidence (max 25) | 0 | 0.00 | 0.00 | Rows 3.1/3.2/3.3/3.4 = 2/0/3/3, mean 2.00 → level 2 on the raw checklist. **Hallucinated-source override forces C3 = 0** (Yahoo Finance ^GSPC 24 Jun 7,475.34, impossible against the report's own 24 Jun high of 7,428.06 and against the slice). |
| C4 Reasoning & judgment (max 20) | 3 | 0.65 | 13.00 | Rows 4.1/4.2/4.3/4.4 = 1/2/5/5, mean 3.25 → level 3. Narrative synthesis and calibration are the report's strongest work; the M5 card geometry fails on all three cards and two of three cross-asset directions are inverted against the slice. |
| C5 Currency, restrictions & transparency (max 15) | 3 | 0.65 | 9.75 | Rows 5.1/5.2/5.3/5.4 = 2/5/3/1, mean 2.75 → level 3. Assumption disclosure is exemplary; the bracketed variable name in §20 is a hard restriction breach and the O/H/L corroboration claim overstates the evidence. |
| **Total** | — | — | **47.75 → 48** | Σ(multiplier × max). |

## 3. Total, band, override check

- Raw total: 8.00 + 17.00 + 0.00 + 13.00 + 9.75 = **47.75 → 48**
- **Override 1 — fabricated source (fires).** §4 cites "Yahoo Finance ^GSPC · 24 Jun · 7,475.34 (derived) · Real-time derived". This figure is impossible on four independent tests: it sits 47.28 pts above the report's own §6 24 Jun high (7,428.06); it sits 37.34 pts above the slice's 24 Jun full-day high (7,438.00) and above the 25 Jun full-day high (7,438.00), so it is unreachable on either candidate session; §3 attributes the same 7,430–7,475 zone to the 25 June session, contradicting the §4 date label; and the 25 Jun report cites Yahoo for 24 Jun 16:00 ET at 7,358.22. Per brief row 3.2, a citation whose figure is self-contradictory or impossible counts as fabricated. Effect: **cap at Low (40–59) and C3 = 0.** C3 was set to 0 above; 48 already falls inside the band, so no numeric cap is applied.
- **Override 2 — restriction breach (fires).** §20 prints the bracketed variable name `[DAILY_OPEN_ANCHOR]`, prohibited by restriction 5.4; the anchor is additionally set to 00:00 UK against the mandated 07:00 UK. Effect: **cap at Moderate (60–74) and C1 down at least one level.** C1 was dropped 3 → 2 above; 48 already satisfies the 74 cap.
- Binding constraint: the fabricated-source cap (59) is the stricter of the two. Final total 48 is below both caps, so the score stands unmodified after the level adjustments.
- **Final Trust Score: 48 / 100 — Band: Low (40–59) — Override recorded: hallucinated_source** (restriction_breach also fired and is applied through C1).

## 4. Card Integrity

Linter rows copied verbatim from `qa/regen_20260906_qa1/lint_static/2026-06-26.csv`:

| card_id | report_date | strategy | flags | dud |
|---|---|---|---|---|
| 2026-06-26_Trade_1 | 2026-06-26 | Trade 1 - Daily Directional (sell stop) | CLEAN | False |
| 2026-06-26_Trade_2 | 2026-06-26 | Trade 2 - Pivot (sell limit daily P) | CLEAN | False |
| 2026-06-26_Trade_3A | 2026-06-26 | Trade 3A - Momentum-Pullback (sell limit daily R1 / 38.2%) | CLEAN | False |

Per-card integrity, 100 − 40·(#DUD) − 10·(#WARN), floored at 0:

| Card | #DUD | #WARN | Integrity |
|---|---|---|---|
| 2026-06-26_Trade_1 | 0 | 0 | 100 |
| 2026-06-26_Trade_2 | 0 | 0 | 100 |
| 2026-06-26_Trade_3A | 0 | 0 | 100 |

Non-suppressed cards: 3 of 3. **Report Card Integrity = 100.0**

The three cards pass every static rule the scoring engine enforces — stop on the correct side of entry, TP1 beyond entry, TP2 beyond TP1, TP3 beyond TP2, R inside 0.3–3.0×ATR14, TP1 inside 2.5×ATR14, LIMIT/STOP levels on the correct side of the D-1 close (Trade 1 sell stop 7,336.80 below, Trade 2 sell limit 7,374.37 and Trade 3A sell limit 7,411.91 above the 7,365.90 D-1 close), anchor explicit. Integrity is therefore 100.0 and is not reduced here.

The M5 *construction* assessment is a separate matter and is scored at row 4.1, not in this number. Against the brief §3 rules: Trade 1 uses a stop-entry at the 24 Jun low instead of market at the daily-open anchor and takes its stop on daily R1 with no 0.25×ATR buffer, and its TP3 is placed at 3R (225.6 pts) while the card text calls it a 3×ATR cap (367.5 pts). Trade 2 is a limit fade at P although §9 declares a TRANSITION regime (breakout side only), and even under RANGE rules the short limits belong at R1/R1.5/R2 with TP1/TP2 at 1R/2R, not the 0.6R/1.0R used. Trade 3A is produced on a 195.35-pt swing that fails the ≥2×ATR14 qualifying gate on every available ATR basis, uses a 38.2% entry instead of the required 57.5% retrace, and places its stop at daily R2 rather than beyond the 0% anchor by 0.25×ATR. Numeric replacements are in the feedback file.

Note on the card record: `cards/baseline/by_date/2026-06-26.json` stores `anchor_broker` "09:00" for all three cards — 09:00 broker (UTC+3) is 07:00 UK, i.e. the standard anchor — while the report text declares a 00:00 UK anchor override. The card record and the report narrative disagree about which anchor was used.

## 5. Data reconciliation log

Basis: slice cash session 16:30–23:00 broker (09:30–16:00 ET). Tolerance per brief §4 — close |Δ| ≤ 3 pts, open/high/low |Δ| ≤ 8 pts is consistent; a close wrong by more than 10 pts is a Category 3 failure.

### 5.1 §6 OHLC — every stated value against the slice

| Section | Field | Report value | Slice value | Delta | Verdict |
|---|---|---|---|---|---|
| §6 | 17 Jun Open | 7,524.50 | 7,531.70 | −7.20 | Within tolerance |
| §6 | 17 Jun High | 7,532.17 | 7,540.00 | −7.83 | Within tolerance |
| §6 | 17 Jun Low | 7,402.61 | 7,408.50 | −5.89 | Within tolerance |
| §6 | 17 Jun Close | 7,420.10 | 7,427.50 | −7.40 | **Discrepancy** (close tolerance 3 pts) |
| §6 | 18 Jun Open | 7,487.36 | 7,514.10 | −26.74 | **Discrepancy** (O/H/L tolerance 8 pts) |
| §6 | 18 Jun High | 7,511.07 | 7,518.30 | −7.23 | Within tolerance |
| §6 | 18 Jun Low | 7,468.32 | 7,472.60 | −4.28 | Within tolerance |
| §6 | 18 Jun Close | 7,500.58 | 7,502.30 | −1.72 | Within tolerance |
| §6 | 22 Jun Open | 7,500.44 | 7,513.10 | −12.66 | **Discrepancy** |
| §6 | 22 Jun High | 7,530.01 | 7,538.80 | −8.79 | **Discrepancy** (marginal) |
| §6 | 22 Jun Low | 7,460.01 | 7,467.30 | −7.29 | Within tolerance |
| §6 | 22 Jun Close | 7,472.79 | 7,479.30 | −6.51 | **Discrepancy** |
| §6 | 23 Jun Open | 7,366.51 | 7,370.40 | −3.89 | Within tolerance |
| §6 | 23 Jun High | 7,424.17 | 7,431.80 | −7.63 | Within tolerance |
| §6 | 23 Jun Low | 7,347.60 | 7,356.20 | −8.60 | **Discrepancy** (marginal) |
| §6 | 23 Jun Close | 7,365.46 | 7,374.40 | −8.94 | **Discrepancy** |
| §6 | 24 Jun Open | 7,370.88 | 7,389.00 | −18.12 | **Discrepancy** |
| §6 | 24 Jun High | 7,428.06 | 7,438.00 | −9.94 | **Discrepancy** |
| §6 | 24 Jun Low | 7,336.82 | 7,346.00 | −9.18 | **Discrepancy** |
| §6 | 24 Jun Close | 7,358.22 | 7,372.30 | −14.08 | **CATEGORY 3 FAILURE** (>10 pts on the anchor close) |

The deltas are one-signed (the report is below the slice on 19 of 20 fields) and grow toward the recent sessions, which is not the behaviour of a symmetric CFD-vs-cash basis. The 24 Jun close — the value the entire report is anchored on — is the worst of them.

### 5.2 As-of session

| Section | Report value | Slice value | Delta | Verdict |
|---|---|---|---|---|
| §2 As-of date | "24 June 2026 last validated session" | D-1 is 2026-06-25; the slice carries a complete 25 Jun cash session (O 7,427.90 H 7,432.60 L 7,332.90 C 7,365.90, ~100 pt range, full bar coverage to 22:45 broker) | one session | **FAIL — as-of is D-2, not D-1** |
| §1/§3/§4/§6/§18 anchor close | 7,358.22 (24 Jun) | 7,365.90 (25 Jun D-1 cash close) | −7.68 | **FAIL — wrong session used as the anchor** |
| §6 window | 17, 18, 22, 23, 24 Jun | 18, 22, 23, 24, 25 Jun (19 Jun Juneteenth correctly excluded, confirmed by the 24 Jun report's own footnote) | shifted one session back | **FAIL** |
| §3/§5 "25 Jun in progress at preparation" | 25 Jun in progress | §20 timestamps preparation at ~21:30 UK, after the 21:00 UK cash close | — | **Internal contradiction** |

### 5.3 RSI2

| Section | Report value | Recomputed | Delta | Verdict |
|---|---|---|---|---|
| §6 22 Jun RSI2 | 74.3 | 74.3 from the report's own closes (helper) | 0.0 | PASS — arithmetic exact |
| §6 23 Jun RSI2 | 0.0 | 0.0 from the report's own closes (helper) | 0.0 | PASS |
| §6 24 Jun RSI2 | 0.0 | 0.0 from the report's own closes (helper) | 0.0 | PASS |
| §6 18 Jun RSI2 | 46.9 | 46.86 using the 16 Jun close 7,511.35 from the 24 Jun report | 0.04 | PASS |
| §6 17 Jun RSI2 | 0.0 | Not valuable from the five stated closes alone; consistent with the 18 Jun figure reproducing | — | Consistent |
| §6 RSI2 column vs slice | 0.0 / 46.9 / 74.3 / 0.0 / 0.0 | Slice cash closes over the true D-1 window (19, 22, 23, 24, 25 Jun): 90.23 / 0.00 / 0.00 / 0.00 / 0.00 | — | Diverges because the session set is wrong, not because the RSI2 formula is wrong |
| Cross-report | 17 Jun RSI2 = 0.0 | 24 Jun report states 41.8 for 17 Jun on the same close series | 41.8 | Cross-report inconsistency; the 26 Jun value is the self-consistent one |

The RSI2 formula itself is applied correctly. The column is wrong only because it is computed over the wrong five sessions.

### 5.4 §11 pivots

Reproduction from the report's own 24 Jun H/L/C (7,428.06 / 7,336.82 / 7,358.22):

| Level | Report value | Recomputed from the report's own H/L/C | Delta | Verdict |
|---|---|---|---|---|
| P | 7,374.37 | 7,374.37 | 0.00 | PASS |
| R1 | 7,411.91 | 7,411.91 | 0.00 | PASS |
| R2 | 7,465.61 | 7,465.61 | 0.00 | PASS |
| R3 | 7,503.15 | 7,503.15 | 0.00 | PASS |
| S1 | 7,320.67 | 7,320.67 | 0.00 | PASS |
| S2 | 7,283.13 | 7,283.13 | 0.00 | PASS |
| S3 | not stated | 7,229.43 | — | **Missing from the table** |

Against the correct D-1 (25 Jun) cash session:

| Level | Report value | Slice D-1 value | Delta | Verdict |
|---|---|---|---|---|
| P | 7,374.37 | 7,377.13 | −2.76 | Wrong prior session |
| R1 | 7,411.91 | 7,421.37 | −9.46 | Wrong prior session |
| R2 | 7,465.61 | 7,476.83 | −11.22 | Wrong prior session |
| R3 | 7,503.15 | 7,521.07 | −17.92 | Wrong prior session |
| S1 | 7,320.67 | 7,321.67 | −1.00 | Wrong prior session |
| S2 | 7,283.13 | 7,277.43 | +5.70 | Wrong prior session |
| S3 | — | 7,221.97 | — | Missing |

Weekly pivots reverse-engineer cleanly from H 7,577.91 / L 7,402.60 / C 7,500.59 and all six stated levels are internally exact. Against the slice's prior-week (15–19 Jun) cash pivots: P 7,493.70 vs 7,495.37 (−1.67), R1 7,584.80 vs 7,582.23 (+2.57), R2 7,669.01 vs 7,670.27 (−1.26), S1 7,409.49 vs 7,407.33 (+2.16), S2 7,318.39 vs 7,320.47 (−2.08), S3 7,234.18 vs 7,232.43 (+1.75). All within basis tolerance — **weekly pivots PASS**; R3 (7,757.13) is the only omission.

### 5.5 Derived statistics and cross-asset

| Section | Report value | Slice value | Delta | Verdict |
|---|---|---|---|---|
| §20 ATR(14) | 122.5 | 121.04 full-day / 109.31 cash session | +1.46 / +13.19 | Matches the full-day basis, not the cash basis §2 declares — **basis mismatch** |
| §10 USDX 5-day direction | Falling | Rising: 100.878 (18 Jun) → 101.646 (24 Jun) → 101.433 (25 Jun) | direction inverted | **FAIL** |
| §10 USDX level | ~101.2 | 101.433 (D-1 close) | −0.23 | Discrepancy |
| §10 VIX 5-day direction | Falling | Rising: 17.90 (18 Jun) → 18.61 (25 Jun) | direction inverted | **FAIL** |
| §10 VIX path | 19.5 → 18.6 | Window max close 18.98, max high 19.25; D-1 close 18.61 | start point −0.52 vs max high | Endpoint PASS; start point not present in the window |
| §10 DAX 40 | Rising/firm ~25,000 | No DAX slice supplied | — | Not verifiable |
| §14 PCE | "within expectations on 25 Jun" | Core PCE m/m actual 0.3 vs consensus 0.1 (HIGH); Core PCE y/y 3.4 vs 3.3 (HIGH) | above consensus | **FAIL** |
| §13d | "Fri 26 Jun PCE follow-through" listed as upcoming | Core PCE released 25 Jun 15:30 broker | — | **Calendar error** |
| §21a direction score | −0.56 | Stated contributions −0.25 −0.15 −0.12 +0.09 = −0.43 | 0.13 | **Does not reconcile** |
| §21b Trade 1 TP3 | 7,111.20, described as a 3×ATR cap "≈367 pts" | 7,336.80 − 225.6 = 3R, not 3×ATR (367.5 pts → 6,969.30) | 141.9 | **Self-contradictory** |
| §4 Yahoo ^GSPC | 7,475.34 (24 Jun, real-time derived) | 24 Jun full-day high 7,438.00; 25 Jun full-day high 7,438.00; report's own 24 Jun high 7,428.06 | +37.34 / +47.28 | **FABRICATED — override trigger** |
