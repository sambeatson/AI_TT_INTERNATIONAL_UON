# Trust Score v3.7 QA — FTSE 100 Daily, 16 July 2026 (run ftse_qa1)

Report: `reports/md/FTSE100_Report_16_July_2026.md` · D = 2026-07-16 · D-1 = 2026-07-15
Level file check: `data/levels/UK100_by_date/2026-07-16.csv` has `last_bar_date = 2026-07-15` (< D), so it is leak-free. Basis used for all comparisons is `_cash` (the report claims the cash index). Stats come from `engine/qa_slice_stats.py --cash-open 10:00 --cash-close 18:30`. Pages with images are pandoc-flattened: §7 shows headings and two captions only. I accepted that as chart evidence per the brief.

## Machine-readable result

c1=3
c2=3
c3=2
c4=3
c5=3
total=59
band=Low
override=restriction_breach
card_integrity=100
n_cards=3
n_duds=0
n_warns=0

(Category 1 is 4 before the restriction-breach reduction, then 3 after it. The total of 59 is already inside the Low band, so the Moderate cap at 74 does not bind.)

## 1. Section 7 checklist

| Row | Reviewer notes | Evidence (location) | Score |
|---|---|---|---|
| 1.1 Variables respected | Asset is the FTSE 100 cash index, with Euro Stoxx 50 as a reference that carries no cards. Counters are Dollar Index, S&P 500 and DAX 40. Tz is Europe/London, currency GBP/index points, lookback 5 sessions (9, 10, 13, 14, 15 Jul). **Daily-open anchor is 00:00 UK, not 07:00 UK**, and the card admits it is not executable. Source mix falls short: 6 consulted but only 5 admitted, and none is an index provider, exchange or sell-side source (FTSE Russell and Bloomberg/STOXX were "not retrievable"). Admitted sources are wires, an aggregator and a live blog. | §2, §4, §19, §20, §21b Trade 1 Entry | 3 |
| 1.2 Coverage and currency consistent | All dates are D-1 or earlier, and D for the session. Currency drift on the Euro Stoxx 50: §2 promises a "GBP-equivalent reference" but §19 says no GBP conversion was applied. | §2 vs §19 | 4 |
| 1.3 Audience and tone | Strategist register, risk-review tone, no retail language. | §1, §18 | 5 |
| **Category 1 mean** | (3+4+5)/3 = 4.0, so level 4 before override. **Restriction-breach override reduces it by one level to 3.** | | **3** |
| 2.1 Sections present and ordered | §1–§21 are present in order, including §13a–d and §21a–d. Defects: §21d is a table, not a paragraph. It names no strongest or weakest strategy and omits the per-strategy hit-rate line. Its limitations line is not the mandatory verbatim boilerplate: it drops the third sentence and says "The framework cannot model…". §7 is headings only, which I accept as a placeholder. | §7, §21d | 4 |
| 2.2 Scorecard as a table | §6 is a table, but it lacks the specified Trend, Source A, Source B, Final Value Used and Validation Outcome columns. It adds "True Range" and a merged "Corroboration" column. There is no one-line RSI2 working beneath it. §11 tables lack the required input row (prior-period H/L/C and dates) and the R2−P = P−S2 confirmation. The monthly pivot table is absent. R5→S5 order is correct. | §6, §11 | 2 |
| 2.3 Method steps visible | §4→§5→consensus is clear. §8 is candle by candle but omits close location as a % and the per-session RSI2 read. §9 gives regime, persistence/overlap, VOLator and KER, with the KER-versus-regime clash openly handled. Charts exist only as headings and captions. | §4–§9 | 4 |
| **Category 2 mean** | (4+2+4)/3 = 3.33, so level 3. | | **3** |
| 3.1 Quantitative claims sourced | Most figures carry a source name. Unsourced or unverifiable: DAX "−182 pts to 24,964", Brent/WTI levels, US yields and the EUR/USD figures. Several §6 O/H/L values are round numbers "reconstructed from wire-reported percentage moves", i.e. synthesised, not sourced. The "China GDP missed 4.5% consensus" claim conflicts with the news calendar (see 5.3). | §6, §10, §12, §14 | 3 |
| 3.2 Citations exist and contain the data | Three checked. (a) Reuters 10,515.9 and Alliance News 10,515.92/−13.47 agree with each other and with the arithmetic 10,529.39 − 13.47 = 10,515.92. But both closes sit **+17.2 (15 Jul) and +22.4 (14 Jul) above the feed's cash closes** (10,498.7 and 10,507.0), past the 15-pt failure threshold. (b) Sunday Guardian 10,498.81/−0.29% is excluded as "stale intraday". Its level is within 0.11 pts of the feed cash close 10,498.7, so the exclusion logic is not supported by the data. (c) Investing.com "range 10,442.50–10,526.86" is labelled as the 15 Jul/30-day window, while the same row reports a window high of 10,747.01, and §6 cites Investing.com for a 14 Jul high of 10,552.56. These figures cannot all be right. I could not fetch sources, and no cited item is provably impossible by its own text, so I did **not** invoke the hallucinated-source override. Flagged for a human check. | §4, §5, §6 | 2 |
| 3.3 Calculations transparent | RSI2 fails: no working is shown, and 3 of the 5 printed values do not reproduce from the report's own closes (table below). 13 Jul and 15 Jul both print 55.3. "ATR ≈104" is a 6-session mean of true range, not ATR(14). KER is 0.26 on 6 sessions, not KER(13, EMA3). Pivot arithmetic is correct from the report's own H/L/C. The §21a sum is traceable (+0.30 listed vs +0.29 stated; rounding). | §6, §9, §11, §21a | 1 |
| 3.4 Numbers reconcile | The D-1 close 10,515.92 is identical in §1, §3, §4, §6 and §21b, and card pivots equal §11. Breaks: Trade 1 TP3 is +3R = 365.82 pts from entry but the same cell states a 3×ATR cap of 312.30 pts. §1 says the index "recovered the entire early-July selloff" while §9 says it "rebuilt most of that loss". "Three-day winning streak" conflicts with the §6 closes (13 Jul 10,496.00 is below 10 Jul 10,496.90). The "10,230–10,570 band" for May–June conflicts with the report's own §4 window high 10,747.01. The report also disagrees with the feed on D-1 close, pivots, swing low, ATR and RSI2 (below). | cross-section | 2 |
| **Category 3 mean** | (3+2+1+2)/4 = 2.0, so level **2**. | | **2** |
| 4.1 Pillars conclude | §9 (TRANSITION), §10 (MIXED) and §8 (stall) end in labels. §12 and §14 end on description or a watch item with no direction label. | §8, §9, §10, §12, §14 | 3 |
| 4.2 Cross-asset interpreted | Real mechanisms: sterling and dollar versus overseas earnings, risk beta, DAX industrial/China channel, financials weight. Weakness: "S&P 500 … third consecutive advance" is contradicted by the feed (13 Jul −0.92%), and Brent is discussed only in §12/§14, not as a counter. | §10 | 4 |
| 4.3 Synthesis reconciles tensions | §15, §16 and §18 name the tensions (sentiment −0.15 vs mildly bullish forecast, 2 of 3 counters contradicting). Several are left "stated rather than resolved". KER-versus-regime is resolved by precedence, but on the wrong KER window. | §9, §15, §16 | 3 |
| 4.4 Calibrated language | §17 is one sentence. Confidence is stated (H on price, M on view). §3's "High — corroborated to two decimal places" is overconfident given the feed disagreement and four of five sessions flagged indicative. | §3, §17, §18 | 4 |
| 4.5 Card construction (protocol) | All three cards deviate materially from the fixed rules. Trade 2 should have been suppressed per the report's own §19/§20. Trade 3C is built on the wrong anchor and ineligible. Trade 1 has the wrong stop anchor and an internal TP3 conflict. Details in the feedback file. | §21b | 1 |
| **Category 4 mean** | (3+4+3+4+1)/5 = 3.0, so level **3**. | | **3** |
| 5.1 Data dated, staleness flagged | Prices and articles are dated and times given. Single-source-indicative status is flagged per row and propagated. The flagging is honest, but flagged values were then used for pivots and cards. | §4, §6, §13a, §19 | 4 |
| 5.2 Assumptions up front | The anchor override and relaxed corroboration are disclosed on the cards and in §20, not in §1. | §20, §21b | 4 |
| 5.3 Red flags surfaced | Hormuz and earnings collisions are carried to the cards. The §13d calendar lists none of the scheduled D-day events in the news slice: US Retail Sales m/m, Core Retail Sales m/m, Initial Jobless Claims and Philadelphia Fed Manufacturing (all HIGH, 15:30 broker = 13:30 UK, inside the 08:00–16:30 session). It also omits the 15 Jul US PPI m/m (−0.3 vs +1.6 consensus). The calendar shows China Q2 GDP actual 4.3 against consensus 4.2, so it was not a miss versus that consensus. The report's "4.5% consensus" and the "miss" narrative (§1 driver iii, §12, §13c, §15) are not supported by it. | §1, §12, §13c, §13d | 3 |
| 5.4 Restrictions honoured | **Breached.** (i) O/H/L values reconstructed from narrative percentages or round numbers are used for pivots and cards, which M4 §6 forbids. (ii) Trade 2 is issued although the report states it "would be SUPPRESSED", and credits an analyst instruction. M4 §21b says no run-time instruction may turn a required suppression into a card, and that such an instruction must not appear in the report. (iii) The §21c Trade 2 fill is "≈10,520.00 INDICATIVE FILL", an approximated price. (iv) "Framework" is referenced in §19/§20/§21d. | §6, §11, §19–§21 | 1 |
| **Category 5 mean** | (4+4+3+1)/4 = 3.0, so level 3. | | **3** |

## 2. Category roll-up

| Cat | Level | Multiplier | Points / max | Justification |
|---|---|---|---|---|
| C1 Prompt adherence | 3 | 0.65 | 13.00 / 20 | Mean 4.0, reduced one level for the restriction breach. 00:00 UK anchor, thin source tiers. |
| C2 Structure | 3 | 0.65 | 13.00 / 20 | All sections present. §6 and §11 deviate from the specified columns and input rows. Monthly pivots absent. §21d off-spec. |
| C3 Accuracy and evidence | 2 | 0.40 | 10.00 / 25 | Closes off by 17–22 pts on 14 and 15 Jul, lows off by up to 49 pts, RSI2 irreproducible, wrong ATR and KER basis, pivots 25–150 pts away from the feed. |
| C4 Reasoning and judgment | 3 | 0.65 | 13.00 / 20 | Sound cross-asset mechanisms and tension flags. Card construction is non-compliant on all three cards. |
| C5 Currency, restrictions, transparency | 3 | 0.65 | 9.75 / 15 | Good dating and disclosure. Scheduled D-day events missing. Synthesised prices and a forced Trade 2 breach restrictions. |
| **Total** | | | **58.75, rounded to 59 / 100** | |

## 3. Total, band, override

- Total 59 sits in the Low band (40–59).
- Hallucinated-source override: not triggered. No cited source is provably fabricated from the text alone; see row 3.2.
- Restriction-breach override: **triggered** (row 5.4). C1 was reduced from 4 to 3. The cap at Moderate (74) is not binding.
- `override=restriction_breach`

## 4. Category 3 data checks against the level file (cash basis)

Report stated D-1 close 10,515.92 vs feed cash close 10,498.7: Δ +17.2, a failure above 15 pts. Feed full-day close is 10,471.8 (Δ +44.1), so the full basis does not rescue it.

| Session | Field | Report | Cash feed | Δ | Verdict (tolerance close ±5, O/H/L ±10) |
|---|---|---|---|---|---|
| Thu 9 Jul | Open / High / Low / Close | 10,489.04 / 10,520.00 / 10,420.00 / 10,465.00 | 10,439.2 / 10,468.9 / 10,380.4 / 10,457.0 | +49.8 / +51.1 / +39.6 / +8.0 | all four outside |
| Fri 10 Jul | O / H / L / C | 10,465.00 / 10,510.00 / 10,440.00 / 10,496.90 | 10,490.1 / 10,504.8 / 10,451.1 / 10,487.2 | −25.1 / +5.2 / −11.1 / +9.7 | O, L, C outside |
| Mon 13 Jul | O / H / L / C | 10,496.90 / 10,520.00 / 10,470.00 / 10,496.00 | 10,488.1 / 10,526.4 / 10,455.7 / 10,487.4 | +8.8 / −6.4 / +14.3 / +8.6 | L, C outside |
| Tue 14 Jul | O / H / L / C | 10,470.08 / 10,552.56 / 10,422.98 / 10,529.39 | 10,460.4 / 10,545.8 / 10,411.5 / 10,507.0 | +9.7 / +6.8 / +11.5 / **+22.4** | L, C outside (close fails 15) |
| Wed 15 Jul | O / H / L / C | 10,510.00 / 10,545.00 / 10,480.00 / 10,515.92 | 10,460.7 / 10,536.2 / 10,431.0 / 10,498.7 | +49.3 / +8.8 / +49.0 / **+17.2** | O, L, C outside (close fails 15) |

RSI2 (period 2, simple means):

| Session | Report | From the report's own closes | Feed cash closes |
|---|---|---|---|
| 9 Jul | 0.0 | not testable (needs 7 Jul close) | 0.00 |
| 10 Jul | 57.0 | reproduces if the 8 Jul close is 10,489.04 | 100.00 |
| 13 Jul | 55.3 | **97.3** | 100.00 |
| 14 Jul | 86.5 | **97.4** | 100.00 |
| 15 Jul | 55.3 | **71.3** | 70.25 |

Three of the five printed values fail to reproduce from the report's own closes, so this is a data failure per the brief. The 55.3 in §1 and §8 and the +0.13 short-term bias input inherit it. §8's reading "RSI2 mid-range, neither overbought nor oversold" is not supported: the correct value is about 71.

| Item | Report | Level file | Δ |
|---|---|---|---|
| ATR(14) | ≈104 (6-session mean TR; used on cards as 104.1) | 118.34 cash / 126.74 full | −14.2 / −22.6 |
| 5-day swing high / low | 10,552.56 / 10,420.00 | 10,545.8 / 10,380.4 | +6.8 / **+39.6** |
| 25-day swing high / low | not stated | 10,739.6 / 10,235.8 | n/a |
| KER (13 sessions) | 0.26 on 6 sessions | cash closes: 0.031 raw, 0.014 on EMA3 (my own computation from the slice), both below the 0.13 threshold | window and value wrong |

Daily pivots (report is arithmetically correct from H 10,545 / L 10,480 / C 10,515.92, so every delta comes from the inputs):

| Level | Report | Cash | Δ |
|---|---|---|---|
| R3 | 10,612.28 | 10,651.47 | −39.2 |
| R2 | 10,578.64 | 10,593.83 | −15.2 |
| R1 | 10,547.28 | 10,546.27 | +1.0 |
| P | 10,513.64 | 10,488.63 | +25.0 |
| S1 | 10,482.28 | 10,441.07 | +41.2 |
| S2 | 10,448.64 | 10,383.43 | +65.2 |
| S3 | 10,417.28 | 10,335.87 | +81.4 |

Weekly pivots (week 6–10 Jul). The report's implied inputs are H 10,680 / L 10,420 / C 10,496.9; the cash week is H 10,739.6 / L 10,380.4 / C 10,487.2.

| Level | Report | Cash | Δ |
|---|---|---|---|
| R3 | 10,904.60 | 11,050.27 | −145.7 |
| R2 | 10,792.30 | 10,894.93 | −102.6 |
| R1 | 10,644.60 | 10,691.07 | −46.5 |
| P | 10,532.30 | 10,535.73 | −3.4 |
| S1 | 10,384.60 | 10,331.87 | +52.7 |
| S2 | 10,272.30 | 10,176.53 | +95.8 |
| S3 | 10,124.60 | 9,972.67 | +151.9 |

Monthly: not produced by the report. The level file carries June cash P 10,412.17 (R1 10,698.13, S1 10,215.53, R2 10,894.77, S2 9,929.57, R3 11,180.73, S3 9,732.93).

Narrative checks against the slices:
- The 8 Jul cash close was 10,457.0 against 7 Jul 10,680.1 (−223.1). The 15 Jul close of 10,498.7 recovers 41.7 of that (about 19%). "Recovered the entire early-July selloff" (§1) is contradicted.
- US500 13 Jul −0.92% (close 7,510.2 vs 7,579.9), so "a third consecutive advance" (§10) is contradicted. The USDX 5-day fall is confirmed (100.924 on 9 Jul to 100.492 on 15 Jul, with −0.39% and −0.41% on the last two days).

## 5. Card Integrity (linter rows, copied verbatim from `qa/ftse_qa1/lint_static/2026-07-16.csv`)

| card_id | report_date | strategy | flags | dud | Card Integrity |
|---|---|---|---|---|---|
| 2026-07-16_Trade_1 | 2026-07-16 | Trade 1 - Daily Directional | CLEAN | False | 100 |
| 2026-07-16_Trade_2 | 2026-07-16 | Trade 2 - Pivot (regime-aware) | CLEAN | False | 100 |
| 2026-07-16_Trade_3C | 2026-07-16 | Trade 3 - Momentum-Breakout (variant 3C) | CLEAN | False | 100 |

Report-level Card Integrity = mean(100, 100, 100) = 100. n_cards = 3, n_duds = 0, n_warns = 0. The static linter checks only geometry (sides, ordering, R and TP distance bounds). It cannot see the rule-level construction defects scored under row 4.5 and itemised in the feedback file. This number is separate from the 100-point total.
