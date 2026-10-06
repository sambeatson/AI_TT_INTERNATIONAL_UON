# Trust Score v3.7 — FTSE 100 Daily Report, 23 July 2026 (run ftse_qa1)

Report: `reports/md/FTSE100_Report_23Jul2026.md` · Reviewer basis: brief + framework §4–7 · data: level file 2026-07-23 (`last_bar_date` 2026-07-22 < D, leak-free, checked), UK100/USDX/US500/VIX/NEWS slices to 2026-07-22, static linter rows, baseline cards.

```
c1=3
c2=4
c3=2
c4=3
c5=3
total=63
band=Moderate
override=restriction_breach
card_integrity=100.0
n_cards=3
n_duds=0
n_warns=0
```

## 1. Section 7 checklist

| Row | Notes | Evidence | Score |
|---|---|---|---|
| 1.1 Variables respected | FTSE 100 cash primary, Euro Stoxx 50 reference only (no cards), USDX / S&P 500 / DAX 40 counters, GBP/points, 5/25-session lookback all as specified. Daily-open anchor is **08:00 UK**, not the instance's 07:00 UK; §20 says "overridden ... at analyst instruction". Source set is press/aggregator heavy (Share Talk, Sharecast, MarketScreener, Investing.com, Yahoo, Trading Economics); no index-provider or exchange-tier source (§20 admits FTSE Russell feed not accessible), and only two sources actually quote the level 10,716.97. | §2, §4, §20, §21b | 3 |
| 1.2 Coverage and currency consistent | All data dated D-1 or earlier, session D, GBP/points throughout. Drift: §1 says the Healey/defence bid "lifted ... Monday-to-Wednesday" but §13c dates the appointment 21 Jul and shows 20 Jul −0.7%; ECB times 13:45/14:30 "CET" differ from the calendar (see 5.3). | §1, §13c | 4 |
| 1.3 Audience and tone | Senior strategist register, trading/risk-review framing, no retail tone. | §1, §18 | 5 |
| 2.1 Sections present and ordered | §1–§21 all present in order incl. §13a–d, §21a–d. Charts are captions only (accepted per brief; 5 captions). | headings | 5 |
| 2.2 Scorecard as a table | §6 is a table with all required columns (Euro Stoxx block has "—" for O/H/L). §11 pivot tables present and ordered high-to-low, but extended to R5/S5 (brief: three levels a side). | §6, §11 | 4 |
| 2.3 Method steps visible | §4–§5 observation → weighting → consensus; §8 candle-by-candle plus sequence; §9 overlap/persistence/VOLator/KER. RSI2 method (RS, smoothing) and ATR(14) value are not shown anywhere; charts not inspectable. | §6, §8, §9 | 4 |
| 3.1 Quantitative claims sourced and correct | Most §1/§12 figures cite a source, but the figures themselves are contradicted by the slice (section 3 below): two of five closes off by >15 pts, opens/highs off by 18–61 pts, weekly and monthly pivots off by 30–110 pts. The UK CPI "below 2.7% consensus" is contradicted by the calendar (consensus 2.5%, actual 2.6%). §14 gilt 5.03%, GBP 1.3377/1.1717, gold US$4,130 and "thirty-day high 10,747.01" carry no source. | §1, §3, §6, §11, §12, §14 | 2 |
| 3.2 Citations exist and contain data | Cannot fetch. Spot checks: (i) Reuters/MarketScreener 20 Jul "−0.7%": 10,600.37→10,524.76 = −0.71%, consistent; (ii) Share Talk 22 Jul "+131.06 to 10,716.97": 10,585.91+131.06 = 10,716.97, consistent; (iii) MT Newswires 22 Jul "+1.28%" normalised to 10,716.97, but 131.06/10,585.91 = +1.24% (Yahoo row says +1.24%) and 10,585.91×1.0128 = 10,721.4 — inconsistent with its own normalised value. The 20 Jul MarketScreener URL slug ("slips-on-middle-east-tensions-burnham-takes-office") differs from the headline column. None impossible or self-contradictory enough to call fabricated; the "six independent sources agree on the close" claim (§3) is overstated. | §3, §4, §13a | 3 |
| 3.3 Calculations transparent | Pivot arithmetic reproduces exactly from the report's own H/L/C (daily; weekly and monthly via implied H/L/C). RSI2 not shown; the reported 34.0/68.1/90.1 only reproduce under Wilder smoothing with an unstated seed. By the brief definition (mean gain/mean loss over 2 periods) the report's own closes give 27.1 / 44.7 / 100.0 for 20/21/22 Jul (Δ −6.9 / −23.4 / +9.9). KER "307 / 973" not reproducible (slice: 54 / 633 raw; EMA3 0.056). §21a contributions inconsistent with the M5 mapping (below). Sentiment tilt +0.28 derivation shows weights but no arithmetic. ATR(14) value never stated in §9 (only implied by "0.15×ATR = 17.78" on cards). | §6, §9, §11, §13b, §21a | 2 |
| 3.4 Numbers reconcile | D-1 close 10,716.97 identical in §1/§3/§4/§6/§21b; §11 pivots = card levels; RSI2 90.1 same in §6/§8. Breaks: 10,686.89 is called the "17 July" high (§8) and the "prior week's high" (§3, §18) but §6 shows 17 Jul high 10,618.40 and no session above 10,618.40; §11 monthly R2 note says 15.53 pts from daily R2, text says 16.00; §11 says R2 pair "does not qualify as a formal confluence" while the Trade 2 card calls it "strong confluence"; §21a contributions (0.19/0.09/0.05) vs M5 mapping (0.25/0.20/0.15); §6 says 17 Jul O/H/L single-source yet §19 calls weekly pivots "fully CORROBORATED". | §3, §6, §8, §11, §19, §21 | 2 |
| 4.1 Pillars conclude | §8 judgement label; §9 bias; §10 per-counter Confirms; §12 headings carry price-supportive labels; §14 has no closing direction label (only a cross-reference check). | §8–§14 | 4 |
| 4.2 Cross-asset interpreted | Mechanisms given (dollar-earner translation, rotation away from tech, DAX industrial vs FTSE energy mix, oil two-sided). Weakened by data: slice USDX closed lower on 22 Jul (101.200 → 101.102), so "fourth consecutive advance" fails as of D-1; US500 closes 7,572.8 (15 Jul) → 7,506.5 (22 Jul), down 0.9% over the window, yet §10 reads "Rising / Confirms". | §10 | 4 |
| 4.3 Synthesis reconciles tensions | Declares "no conflict anywhere" in §8, §9, §16, §18 while: a 10,747.01 "thirty-day high" sits above the 22 Jul high yet the 22 Jul move is called a clean breakout above an "eight-session shelf" (10,686.89 matches the 2 Jul high of 10,686.8, 14 sessions earlier; 6–7 Jul highs 10,726.7/10,739.6 are above it); §11 vs §21b confluence contradiction. Fragility of unanimity and ECB risk are acknowledged. | §3, §8, §15–§18 | 3 |
| 4.4 Calibrated language | §17 is one sentence; confidence stated (HIGH level / MEDIUM path). Overconfident phrasing ("unusually clean", "no internal contradiction anywhere", "six independent sources") not supported by the reconciliation breaks. | §3, §9, §17, §18 | 3 |
| 4.5 Card construction (protocol, folded into C4) | All three cards deviate from fixed M5 rules (detail in feedback): T1 stop has no 0.25×ATR buffer and invalidation lies between entry and stop; T2 uses limit-at-P / stop-at-S1 / 1R-2R targets instead of the TREND breakout geometry; T3A enters at 38.2% not 57.5% with TP1/TP2 shifted one tier, and uses a swing low (10,483.14) not present in the data. | §21b | 1 |
| 5.1 Data dated; staleness flagged | All prices/articles dated; single-source O/H/L flagged in §6, §19. Flags contradicted for weekly pivots (see 3.4). | §4, §6, §13, §19 | 4 |
| 5.2 Assumptions up front | Anchor override on Trade 1 card and in §20 (not in §1); single-source propagation to Trade 2/3A caveats present. | §20, §21b | 4 |
| 5.3 Red flags surfaced | §12/§15 risks good. The ECB decision/press conference is the "highest-impact event" but is not carried into any card caveat (Trade 1 is a full-day market position). ECB times are stated 13:45 / 14:30 CET; the calendar shows decision 15:15 and press conference 15:45 broker time (= 13:15 / 13:45 UK, 14:15 / 14:45 CEST). | §13d, §21b | 3 |
| 5.4 Restrictions honoured | Breached: (a) 08:00 UK anchor "at analyst instruction" — the anchor is fixed per instance and M5 gate rule 8 forbids citing an instruction as authority; (b) §19 states the 25-session series feeding the §9 regime metrics "blends corroborated closes with reconstructed intermediate sessions" (and Euro Stoxx 21 Jul close is "derived from reported session change") — a synthesised-price breach, which the same paragraph then contradicts ("No value ... was synthesised, interpolated or inferred"). Retail CFD quote correctly excluded; no module codes or bracketed names. | §6, §19, §20 | 1 |

## 2. Category roll-up

| Cat | Rows mean | Level | Multiplier | Points | Justification |
|---|---|---|---|---|---|
| C1 Prompt adherence (20) | (3+4+5)/3 = 4.0 | **3** (override: one level down from 4) | 0.65 | 13.00 | Variables mostly respected; anchor deviation (08:00 vs 07:00) and no-synthesis breach trigger the restriction override. |
| C2 Structure (20) | (5+4+4)/3 = 4.33 | **4** | 0.85 | 17.00 | Complete and ordered; RSI2/ATR method and charts not visible. |
| C3 Accuracy and evidence (25) | (2+3+2+2)/4 = 2.25 | **2** | 0.40 | 10.00 | Data checks against the slice fail on closes (16, 17 Jul), opens/highs, RSI2 reproducibility, weekly/monthly pivots and KER; internal reconciliation breaks. No fabricated source established. |
| C4 Reasoning and judgment (20) | (4+4+3+3+1)/5 = 3.0 | **3** | 0.65 | 13.00 | Good mechanism writing; regime and breakout thesis rest on unreconciled levels; card construction poor. |
| C5 Currency and transparency (15) | (4+4+3+1)/4 = 3.0 | **3** | 0.65 | 9.75 | Dating and flags good; restriction breaches and uncarried ECB risk. |

## 3. Category 3 data comparison (report vs level file, cash basis claimed; tolerance close ±5, O/H/L ±10, brief §4)

Closes and RSI2 (report § 6 vs slice cash session 10:00–18:30 broker):

| Date | Close report / slice / Δ | Open Δ | High Δ | Low Δ | RSI2 report / slice / report-own-closes (simple) |
|---|---|---|---|---|---|
| 16 Jul | 10,572.24 / 10,540.4 / **+31.8** | 10,514.96 vs 10,453.9 **+61.1** | 10,572.24 vs 10,550.5 **+21.7** | 10,447.55 vs 10,429.4 **+18.2** | 99.9 / 83.4 / n/a |
| 17 Jul | 10,600.37 / 10,573.4 / **+27.0** | 10,575.10 vs 10,534.1 **+41.0** | 10,618.40 vs 10,616.2 +2.2 | 10,552.30 vs 10,514.9 **+37.4** | 99.9 / 100.0 / n/a |
| 20 Jul | 10,524.76 / 10,534.7 / **−10.0** | 10,600.27 vs 10,540.1 **+60.2** | 10,600.27 vs 10,589.4 **+10.9** | 10,483.14 vs 10,503.1 **−20.0** | 34.0 / 46.0 / 27.1 |
| 21 Jul | 10,585.91 / 10,571.7 / **+14.2** | 10,524.25 vs 10,479.3 **+45.0** | 10,592.50 vs 10,574.2 **+18.3** | 10,483.14 vs 10,470.1 **+13.0** | 68.1 / 48.9 / 44.7 |
| 22 Jul | 10,716.97 / 10,714.6 / +2.4 | 10,608.97 vs 10,587.0 **+22.0** | 10,733.96 vs 10,758.9 **−24.9** | 10,565.96 vs 10,557.2 +8.8 | 90.1 / 100.0 / 100.0 |

Two closes exceed the 15-pt failure threshold (16 and 17 Jul); the RSI2 sequence does not reproduce from the report's own closes under the brief definition (21 Jul Δ −23.4). The report's weekly/monthly highs and the 10,686.89 "prior week high" are not found in the slice for the stated week (prior-week cash high 10,616.2; 10,686.8 is the 2 Jul high).

Daily pivots (report from 22 Jul H/L/C vs level file `d_cash_*`):

| Level | Report | Level file | Δ |
|---|---|---|---|
| P | 10,672.30 | 10,676.9 | −4.6 |
| R1 | 10,778.63 | 10,796.6 | −18.0 |
| S1 | 10,610.63 | 10,594.9 | +15.7 |
| R2 | 10,840.30 | 10,878.6 | −38.3 |
| S2 | 10,504.30 | 10,475.2 | +29.1 |
| R3 | 10,946.63 | 10,998.3 | −51.7 |
| S3 | 10,442.63 | 10,393.2 | +49.4 |

Weekly pivots (week 13–17 Jul; report implied H 10,686.89 / L 10,429.22 / C 10,600.37 vs level file H 10,616.2 / L 10,411.5 / C 10,573.4):

| Level | Report | Level file `w_cash_*` | Δ |
|---|---|---|---|
| P | 10,572.16 | 10,533.7 | +38.5 |
| R1 | 10,715.10 | 10,655.9 | +59.2 |
| S1 | 10,457.43 | 10,451.2 | +6.2 |
| R2 | 10,829.83 | 10,738.4 | +91.4 |
| S2 | 10,314.49 | 10,329.0 | −14.5 |
| R3 | 10,972.77 | 10,860.6 | +112.2 |
| S3 | 10,199.76 | 10,246.5 | −46.7 |

Monthly pivots (June; report implied H 10,570.09 / L 10,127.60 / C 10,447.74 vs level file H 10,608.8 / L 10,126.2 / C 10,501.5):

| Level | Report | Level file `m_cash_*` | Δ |
|---|---|---|---|
| P | 10,381.81 | 10,412.17 | −30.4 |
| R1 | 10,636.02 | 10,698.13 | −62.1 |
| S1 | 10,193.53 | 10,215.53 | −22.0 |
| R2 | 10,824.30 | 10,894.77 | −70.5 |
| S2 | 9,939.32 | 9,929.57 | +9.8 |
| R3 | 11,078.51 | 11,180.73 | −102.2 |
| S3 | 9,751.04 | 9,732.93 | +18.1 |

Other numeric checks: ATR14 implied by cards 118.53 vs level file cash 115.25 (Δ +3.3, consistent). KER(13, EMA3) stated +0.32 (net 307 / path 973) vs slice cash-closes 0.056 (raw 0.085; net 54 / path 633) — below the 0.13 trending threshold. 25-session range position 0.86 stated vs 0.90 slice (consistent). 5-session directional persistence 0.62 stated vs 0.40 from slice closes. UK CPI June: calendar actual 2.6% y/y, consensus 2.5%, previous 2.8% (report: consensus 2.7%). §21a: reported signal contributions 0.19 / 0.09 / 0.05 (short tech / regime / cross-asset) vs M5 mapping 0.25×1 / 0.20×1 / 0.15×1; the rest reproduce (0.05, 0.048, 0.042). Direction (LONG) and the ≥0.25 threshold are unaffected, but the stated +0.46 is not the sum of correctly mapped signals.

## 4. Total, band, override

Total = 13.00 + 17.00 + 10.00 + 13.00 + 9.75 = 62.75 → **63**. Band: **Moderate Trust (60–74)**. Override: **restriction_breach** (anchor deviation cited to analyst instruction; reconstructed/derived prices admitted in §19 and §6). Cap 60–74 applied (not binding at 63); C1 reduced from 4 to 3. Hallucinated-source override: not established (sources unverifiable offline, none self-contradictory to the standard in brief row 3.2).

## 5. Card Integrity (linter static rows, copied verbatim)

| card_id | report_date | strategy | flags | dud | score |
|---|---|---|---|---|---|
| 2026-07-23_Trade_1 | 2026-07-23 | Trade 1 — Daily Directional | CLEAN | False | 100 |
| 2026-07-23_Trade_2 | 2026-07-23 | Trade 2 — Pivot, regime-aware | CLEAN | False | 100 |
| 2026-07-23_Trade_3A | 2026-07-23 | Trade 3A — Momentum-Pullback (trending-up regime fork) | CLEAN | False | 100 |

Report-level Card Integrity = 100.0 (n_cards 3, n_duds 0, n_warns 0). The linter is static (side/order/R/target-distance only); the rule-construction defects in the feedback are scored in C4 row 4.5, not here.

## 6. Feedback

See `qa/ftse_qa1/2026-07-23_feedback.md`.
