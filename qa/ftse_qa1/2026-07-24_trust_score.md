# Trust Score v3.7 — FTSE 100 Daily Report, 24 July 2026 (run ftse_qa1)

Report: `reports/md/FTSE100_Report_24Jul2026.md` · D = 2026-07-24 · D-1 = 2026-07-23
Reference data: `data/levels/UK100_by_date/2026-07-24.csv` (`last_bar_date` = 2026-07-23 < D, checked) and
`data/slices/UK100/UK100_upto_2026-07-23.csv` (last bar 2026-07-23 22:45 broker). Basis used: `_cash`
(the report states LSE 08:00–16:30 cash-session data). `qa_slice_stats.py --cash-open 10:00 --cash-close 18:30` reproduces the level file.

```
c1=3
c2=4
c3=2
c4=3
c5=3
total=63
band=Moderate
override=restriction_breach
card_integrity=95.0
n_cards=3
n_duds=0
n_warns=1
```
(n_cards counts the three card rows; Trade 1 is SUPPRESSED, so Card Integrity is the mean over the 2 non-suppressed cards.)

## 1. Category 3 data check against the level file (cash basis)

Tolerances (brief §4): close ≤ 5 pts, open/high/low ≤ 10 pts. Delta = report minus level file. PASS marked only where inside tolerance.

### 1a. D-1 and prior sessions, OHLC

| Session | Field | Report | Level/slice (cash) | Delta | Verdict |
|---|---|---|---|---|---|
| Fri 17 Jul | O | 10,620.15 | 10,534.10 | +86.05 | FAIL |
| | H | 10,668.42 | 10,616.20 | +52.22 | FAIL |
| | L | 10,586.30 | 10,514.90 | +71.40 | FAIL |
| | C | 10,598.91 | 10,573.40 | +25.51 | FAIL (>15) |
| Mon 20 Jul | O | 10,596.44 | 10,540.10 | +56.34 | FAIL |
| | H | 10,611.02 | 10,589.40 | +21.62 | FAIL |
| | L | 10,499.18 | 10,503.10 | −3.92 | pass |
| | C | 10,524.76 | 10,534.70 | −9.94 | FAIL (>5) |
| Tue 21 Jul | O | 10,524.25 | 10,479.30 | +44.95 | FAIL |
| | H | 10,592.88 | 10,574.20 | +18.68 | FAIL |
| | L | 10,483.14 | 10,470.10 | +13.04 | FAIL |
| | C | 10,585.91 | 10,571.70 | +14.21 | FAIL (>5) |
| Wed 22 Jul | O | 10,585.87 | 10,587.00 | −1.13 | pass |
| | H | 10,763.44 | 10,758.90 | +4.54 | pass |
| | L | 10,568.72 | 10,557.20 | +11.52 | FAIL (marginal) |
| | C | 10,716.97 | 10,714.60 | +2.37 | pass |
| **Thu 23 Jul (D-1)** | O | 10,716.99 | 10,704.00 | +12.99 | FAIL |
| | H | 10,724.85 | 10,709.80 | +15.05 | FAIL |
| | L | 10,612.40 | 10,597.30 | +15.10 | FAIL |
| | **C** | **10,639.00** | **10,618.10** | **+20.90** | **FAIL (>15)** — appears in §1, §3, §4, §6, §11, §18 and anchors every card |

4 of 20 OHLC fields are inside tolerance. Two closes are off by more than 15 pts (17 Jul +25.51, 23 Jul +20.90). The full-day close is 10,594.90 (delta +44.10), so a full-day basis does not rescue the figure. The report's four stated opens (Mon–Thu) all sit within 2.5 pts of the previous stated close (10,596.44 vs 10,598.91; 10,524.25 vs 10,524.76; 10,585.87 vs 10,585.91; 10,716.99 vs 10,716.97), whereas the slice opens differ from the previous close by −33.3, −55.4, +15.3 and −10.6. The opens look like prior-close proxies but are labelled "Dual-source". This is a concern, not proof.

### 1b. Indicators

| Item | Report | Level file / recomputation | Delta | Verdict |
|---|---|---|---|---|
| ATR14 (§9, §21) | 118.40 | 116.35 cash (138.57 full) | +2.05 | pass (cash) |
| RSI2 D-1 (§6, §8, §21a) | 45.6 | 59.69 cash (49.95 full) | −14.09 | FAIL |
| RSI2 from the report's own closes, 21 Jul | 45.2 | 45.2 | 0 | reproduces |
| RSI2 from the report's own closes, 22 Jul | 81.3 | 100.0 (two consecutive gains, zero loss) | −18.7 | FAIL: does not reproduce |
| RSI2 from the report's own closes, 23 Jul | 45.6 | 62.7 (gain mean 65.53, loss mean 38.985, RS 1.681) | −17.1 | FAIL: does not reproduce |
| RSI2 17 Jul / 20 Jul | 50.0 / 0.0 | not testable (needs closes before the window); the table holds one down-move before 20 Jul, so 0.0 is not reproducible from the report | n/a | unverifiable |
| 25-session regression slope (§9) | +22.81 pts/session | +5.81 (cash closes 19 Jun–23 Jul) | −17.0 | FAIL (about 3.9×) |
| 25-session net change (§9) | +5.05% from 10,127.60 | +2.57% (10,352.3 to 10,618.1). 10,127.60 is the 10 Jun intraday low (slice 10,126.2), not a close 25 sessions back | n/a | FAIL |
| KER(13, EMA3) (§1, §9) | 0.5051, TRENDING | 0.070 cash (0.077 full): below the 0.09 inner band, below the 0.13 threshold | −0.44 | FAIL |
| 5-day swing low/high | 10,483.14 / 10,763.44 | 10,470.10 / 10,758.90 | +13.04 / +4.54 | marginal fail / pass |

### 1c. Pivots

Daily (report built from its own H 10,724.85 / L 10,612.40 / C 10,639.00; arithmetic reproduces exactly):

| Level | Report | Level file (cash) | Delta |
|---|---|---|---|
| R3 | 10,817.55 | 10,798.67 | +18.88 |
| R2 | 10,771.20 | 10,754.23 | +16.97 |
| R1 | 10,705.10 | 10,686.17 | +18.93 |
| P | 10,658.75 | 10,641.73 | +17.02 |
| S1 | 10,592.65 | 10,573.67 | +18.98 |
| S2 | 10,546.30 | 10,529.23 | +17.07 |
| S3 | 10,480.20 | 10,461.17 | +19.03 |

All seven daily levels are 17–19 pts too high (inherited from the high/low/close offsets). Full-day basis is further away (P 10,632.93, S1 10,542.87).

Weekly (week 13–17 Jul). The report's arithmetic reproduces from its own inputs (H 10,786.20 / L 10,501.55 / C 10,598.91), but the inputs do not match the slice (cash H 10,616.20 / L 10,411.50 / C 10,573.40):

| Level | Report | Level file (cash) | Delta |
|---|---|---|---|
| R3 | 11,040.87 | 10,860.60 | +180.27 |
| R2 | 10,913.54 | 10,738.40 | +175.14 |
| R1 | 10,756.22 | 10,655.90 | +100.32 |
| P | 10,628.89 | 10,533.70 | +95.19 |
| S1 | 10,471.57 | 10,451.20 | +20.37 |
| S2 | 10,344.24 | 10,329.00 | +15.24 |
| S3 | 10,186.92 | 10,246.50 | −59.58 |

The report's weekly high of 10,786.20 is above the highest 25-session cash high in the slice (10,758.90, 22 Jul). It also contradicts the report's own statements that 22 Jul's 10,763.44 was a "three-month high" (§8, §13a).

Monthly (June). Report inputs H 10,570.09 / L 10,127.60 / C 10,447.74 against slice H 10,608.80 / L 10,126.20 / C 10,501.50:

| Level | Report | Level file (cash) | Delta |
|---|---|---|---|
| R3 | 11,078.51 | 11,180.73 | −102.22 |
| R2 | 10,824.30 | 10,894.77 | −70.47 |
| R1 | 10,636.02 | 10,698.13 | −62.11 |
| P | 10,381.81 | 10,412.17 | −30.36 |
| S1 | 10,193.53 | 10,215.53 | −22.00 |
| S2 | 9,939.32 | 9,929.57 | +9.75 |
| S3 | 9,751.04 | 9,732.93 | +18.11 |

Consequence: the "10,628–10,640 multi-timeframe pivot confluence" called "the single most important structural observation in this report" (§11, §16, §17, §18 and the Trade 3A entry) is built from the wrong weekly P (level file 10,533.70), the wrong monthly R1 (level file 10,698.13) and a D-1 close 20.9 pts too high. On the level file no weekly or monthly level lies within 20 pts of the 10,618.10 close.

### 1d. Counters and calendar (slice, all dated before D)

- USDX: §10 says "fourth consecutive advancing session, firm near 101.1". Slice closes: 100.751 (17 Jul), 100.968, 101.200, 101.102 (22 Jul, down 0.097%), 101.435 (23 Jul, up 0.329%). The run of advances ended on 21 Jul and is one session long at D-1; the 101.1 figure is the 22 Jul close and the 23 Jul close is 101.435.
- S&P 500: 7,408 / −1.21% (report) vs 7,418.0 / −1.18% (slice CFD): consistent within basis. VIX +5.9% on 23 Jul consistent with "volatility gauges surged".
- UK June CPI (22 Jul): the report says it "fell by more than expected". Calendar: CPI y/y 2.6 vs consensus 2.5 (above; previous 2.8); CPI m/m 0.1 vs 0.2 (below); CPIH y/y 2.8 vs 2.9 (below); PPI input m/m −2.0 vs +1.9. The headline y/y print was above consensus, so the one-line characterisation is not supported.
- 21 Jul labour data: report cites regular pay 3.4% "in line" (calendar 3.4 vs 3.3 consensus). It omits total pay 4.3 vs 4.6, unemployment 4.9 vs 4.6 and employment change +147k vs +38k.
- 23 Jul US initial claims: report gives "consensus ~211,000 against a prior 208,000" and no outcome. Calendar: actual 187k, consensus 215k.
- 24 Jul scheduled events missing from §13d and the card caveats: UK retail sales 07:00 UK (09:00 broker), UK flash PMIs 09:30 UK, euro-area flash PMIs 08:30–09:00 UK, US new home sales 15:00 UK. The 07:00 UK anchor coincides with UK retail sales.

## 2. Section 7 checklist (every row)

| Row | Reviewer notes | Evidence location | Score |
|---|---|---|---|
| 1.1 Variables respected | Asset FTSE 100 cash index (UKX), EURO STOXX 50 secondary, no cards on it; counters USDX / S&P 500 / DAX 40; tz Europe/London; lookback 5 sessions; GBP, index points; 07:00 UK anchor stated. Seven sources listed but the tier mix is exchange, provider and aggregators with no sell-side. Brent is treated as dominant yet absent from the §10 counter table. | §2, §4, §10, header | 4 |
| 1.2 Coverage and currency consistent | Dates and as-of consistently D-1 for data, D for session. No unit drift. The stale USDX reading is scored in Cat 3. | whole report | 4 |
| 1.3 Audience and tone | Institutional strategist register throughout. | §1, §18 | 5 |
| 2.1 Sections present and ordered | §1–§21 all present, §13a–d and §21a–d present, order correct. §7 contains a table of five described charts, with the statement "Chart rendering is not available"; the protocol expects two charts (placeholder accepted per brief). | headings, §7 | 4 |
| 2.2 Scorecard as a table | §6 is a table but carries Change/Chg%/Range/TR/Corroboration instead of the required Trend, Source A, Source B, Final, Validation columns. The Trend label (Close>Open and RSI2>50) is missing. §11 pivot tables are present, R3 to S3, three each side, for daily, weekly and monthly. | §6, §11 | 3 |
| 2.3 Method steps visible | §4–§5 observations to consensus; §8 candle-by-candle with sequence assessment; §9 regime, VOLator and KER shown. No persistence/overlap read. Minor description slips: Tue 21 Jul is called an "inside day" while its low breaks Monday's low; Fri 17 "upper shadow roughly 70" is 48 above the open; "two upper, two lower, one neutral" closes is three lower-third closes on the report's own table. | §7–§9 | 4 |
| 3.1 Quantitative claims sourced | §1, §12 and §14 carry many uncited figures: Brent $94.13 / $100, gilt 5.03%, Fed funds 3.50–3.75%, EURUSD 1.1375, GBPUSD 1.3377, Shell +2% / BP +1.5%, 92% hike pricing, 52-week high and low. Several point to §13 only loosely. | §1, §12, §14 | 3 |
| 3.2 Citations exist and contain data | Cannot fetch. Three spot-checks: (a) Proactive Investors "down 77 points at 10,639": the report's own prior close implies 77.97, so "77" is truncation, not contradiction; (b) MarketScreener "-0.73%" reproduces (77.97 / 10,716.97 = 0.7275%); (c) Trading Economics "10,701 to 10,639": plausible. No source is self-contradictory, so no hallucinated-source override. Weaknesses: the 22 Jul close is said to be corroborated by "four independent sources" and only one appears in §4; §3 says six sources, §5 says seven observations, §20 says seven retained plus one excluded; §3 range is "10,639.00 – 10,640.00" while every normalised value is 10,639.00. | §3, §4, §5, §20 | 3 |
| 3.3 Calculations transparent | Pivot arithmetic reproducible and correct from the report's own inputs. ATR stated. RSI2 not shown, and 2 of 3 testable values fail to reproduce from the report's own closes (81.3 vs 100.0; 45.6 vs 62.7). KER 0.5051 and slope +22.81 are stated without derivation and do not reproduce (0.07 and +5.81). Sentiment tilt −0.20 is "weighted mean of the nine contributions" but those nine contributions average +0.00 (unweighted) and about +0.005 with high=2, medium=1.5, low=1 weights; the 39/54/7 shares do not reproduce. §21a lists contributions, not the signal and weight behind each. | §6, §9, §13b, §21a | 2 |
| 3.4 Numbers reconcile | The D-1 close 10,639.00 is identical in §1, §3, §4, §6, §11, §18 and the cards, and card pivots match §11. Breaks: weekly high 10,786.20 vs "three-month high" 10,763.44; "touched $100" (§12, §13a) vs "toward $100" (§1, §14); source counts (see 3.2); §1 "5.05% above its late-June base" vs §9 base 10,127.60 (a 10 Jun low); §19 says single-source fields are "not used for entry or stop pricing in §21" yet Trade 2 enters at daily S1 and stops off daily S2, and Trade 3A TP2 is pinned to the single-source 23 Jul high. | cross-section | 3 |
| 3.5 External data vs level file (added; per SESSION_TASK step 1) | D-1 close +20.90 (>15); 17 Jul close +25.51 (>15); 4 of 20 OHLC fields in tolerance; RSI2 off by 14.1; weekly pivots off by 15–180; monthly off by up to 102; KER and slope off by factors of about 7 and 4; USDX run mis-stated. See section 1. | §6, §9, §10, §11 | 1 |
| 4.1 Pillars conclude | §8 REJECTION WITHIN UPTREND; §9 TRANSITION; §10 negative −0.35 with relative-strength qualification; §12 per-factor directions plus horizon weighting paragraph; §14 ends in a watch item with a stated directional risk. All present. §9's conclusion contradicts itself (see 4.3). | §8–§14 | 4 |
| 4.2 Cross-asset interpreted | Strong mechanisms: overseas earnings translation for the dollar, energy weighting for Brent, rate-sensitive composition of continental indices, and a regional-vs-index-specific distinction. Not a correlation list. | §10, §12 | 4 |
| 4.3 Synthesis reconciles tensions | Tensions are named (KER vs short-term; regional vs index-specific), but the resolution is incoherent. §9 says the efficiency ratio "takes precedence for regime classification" while the regime label is TRANSITION. The forks then follow the efficiency reading rather than the label (§20 "Regime fork"). | §9, §15, §16, §20 | 3 |
| 4.4 Calibrated language | §17 is exactly one sentence; confidence H on price and M on direction; "mild upward bias" is consistent with a NEUTRAL +0.06. The one sentence is long and carries four clauses. | §3, §17, §18 | 4 |
| 4.5 Card construction (protocol: scored under Cat 4) | Both cards are built against the fixed card rules: Trade 2 is a counter-side limit under TRANSITION (a "re-labelled" rotation limit), and Trade 3A is built under TRANSITION whose fork is 3C. Also: entry at 50% not 57.5% (3A); 3A stop anchored to the 61.8% level rather than the 0% anchor; buffer 0.15×ATR instead of 0.25×ATR on both; Unit 3 stop moved to entry less 0.2R instead of entry plus 0.2R; invalidation exactly 0.15×ATR from the stop on both (must be more than); D-1 reference close and signed gap not printed; R as a multiple of ATR not printed; 3A has no anchor time; Trade 2 TP3 below TP2. Full list in the feedback file. | §21b | 1 |
| 4.6 Direction score traceable (protocol anchor) | Sum of contributions reproduces (+0.055, printed +0.06) and weights match defaults (short-tech 0.25 → −0.30 gives −0.075, etc.), and the Trade 1 suppression (|0.06| < 0.25) is correctly shown as a SUPPRESSED row. But the signal values do not follow the fixed value mapping (short-term bias must be +1 / −1 / 0; TRANSITION regime must be ±0.5; CONTRADICT must be ×−0.5) and the inputs (KER, tilt) are wrong. | §20, §21a | 2 |
| 5.1 Data dated, staleness flagged | Every price and article dated; single-source highs and lows flagged in §6, §11, §19; USDX shown as a band with a stated reason. USDX band is one session stale. | §4, §6, §13, §19 | 4 |
| 5.2 Assumptions up front | Anchor 07:00 UK stated in the header and Trade 2; Trade 3A has no anchor. The single-source caveat reaches the cards but §19/§20 describe the cards incorrectly (see 3.4). §1 does not surface the INDICATIVE daily pivot flag. | header, §19–§21 | 3 |
| 5.3 Red flags surfaced | News collision carried to both cards' caveats; geopolitical and rate risks in §12/§15. Missing from §13d and card caveats: UK retail sales at the 07:00 UK anchor, UK/euro flash PMIs, US new home sales; the 21 Jul labour miss and the CPI y/y beat are not surfaced. | §12, §13, §15, §21b | 3 |
| 5.4 Restrictions honoured | No retail CFD used in consensus; no bracketed names, module codes or framework names. Breaches: (i) the fixed regime fork and the TRANSITION Trade 2 rule are overridden and §20 says so openly ("resolved to the momentum-pullback branch on the trending efficiency reading"); (ii) single-source highs and lows are used to compute daily pivots although §6 states they "may not be used for pivot prior-period calculation". Concern, not scored as breach: opens look like prior-close proxies labelled dual-source. | §6, §11, §20, §21b | 2 |

## 3. Category roll-up

| # | Category (max) | Row mean | Level | Multiplier | Points | Justification |
|---|---|---|---|---|---|---|
| 1 | Prompt adherence (20) | 4.33 → 4; override lowers by one | **3** | 0.65 | 13.00 | Variables respected; restriction-breach override applied (fixed regime fork and card-gate rules overridden, single-source inputs used in pivots). |
| 2 | Structure (20) | 3.67 → 4 | **4** | 0.85 | 17.00 | All sections present and ordered; §6 lacks the required Trend/Source A/Source B/Final/Validation columns; charts are described, not rendered. |
| 3 | Accuracy and evidence (25) | 2.40 → 2 | **2** | 0.40 | 10.00 | D-1 close +20.9 and 17 Jul close +25.5 off; weekly and monthly pivot inputs wrong; RSI2, KER, slope and sentiment tilt do not reproduce. |
| 4 | Reasoning and judgment (20) | 3.00 → 3 | **3** | 0.65 | 13.00 | Good mechanism work and a calibrated forecast; contradictory regime handling and non-compliant card construction. |
| 5 | Currency and transparency (15) | 3.00 → 3 | **3** | 0.65 | 9.75 | Dated and flagged; assumptions contradicted by the cards; calendar gaps. |

Total = 13.00 + 17.00 + 10.00 + 13.00 + 9.75 = 62.75 → **63 / 100 — Moderate (60–74)**.

## 4. Override check

- Hallucinated source: not triggered. The three spot-checked citations are dated, named and numerically consistent with the report; C3 is not forced to 0. (Residual doubt: the "four independent sources" for 22 Jul is not shown in §4.)
- Restriction breach: **triggered** (`restriction_breach`). Cap at 74 (not binding at 63); C1 reduced from 4 to 3. Basis: the report's own Agent Log states the Trade 3 variant was chosen "on the trending efficiency reading" against its TRANSITION label, and Trade 2 is a counter-side limit under TRANSITION. Both are fixed gates the card rules declare non-overridable. Secondary basis: single-source highs and lows used for daily pivot computation against the report's stated protocol.

## 5. Card Integrity (linter rows copied verbatim from `qa/ftse_qa1/lint_static/2026-07-24.csv`)

| card_id | strategy | flags | dud | per-card score |
|---|---|---|---|---|
| 2026-07-24_Trade_1 | Trade 1 - Daily Directional | SUPPRESSED | False | excluded |
| 2026-07-24_Trade_2 | Trade 2 - Pivot, TRANSITION-regime branch (rotation from support toward the pivot) | WARN_TP3_ORDER | False | 100 − 10 = 90 |
| 2026-07-24_Trade_3A | Trade 3A - Momentum-Pullback | CLEAN | False | 100 |

Report-level Card Integrity = mean(90, 100) = **95.0**. n_duds=0, n_warns=1. The static linter cannot see the defects listed under row 4.5 (wrong branch, wrong stop anchor, wrong BE side, invalidation distance); those are scored in Category 4 and detailed in the feedback.

## 6. Band and recommended action

Moderate Trust (63): must not be used as-is. Regeneration should target Category 3 (re-ingest D-1 and weekly/monthly H/L/C on the cash basis), the regime-to-card mapping and the card construction.
