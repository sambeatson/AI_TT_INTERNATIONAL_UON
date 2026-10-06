# Trust Score v3.7 — FTSE 100 Daily Report, 21 May 2026

Report: `reports/md/FTSE_100_Report_21_May_2026.md` · D = 2026-05-21 · as-of session D-1 = 2026-05-20 (Wed)
Level file check: `data/levels/UK100_by_date/2026-05-21.csv` has `last_bar_date = 2026-05-20`, which is < D, so it is leak-free and was used.
Basis used for comparison: `_cash` (UK window 08:00–16:30 London = 10:00–18:30 broker), because the report claims the FTSE 100 cash index. Full-day figures are quoted where the gap is basis-sensitive.

## Machine-readable result

```
c1=2
c2=4
c3=0
c4=3
c5=2
total=44
band=Low
override=hallucinated_source
card_integrity=100.0
n_cards=3
n_duds=0
n_warns=0
```

`override` carries one value. Two overrides fire. The hallucinated-source override (cap 40–59, C3 = 0) is recorded as the controlling one. The restriction-breach override (cap 60–74, C1 down at least one level) also fires independently. I applied its C1 reduction (3 → 2) as well. Neither changes the band: the arithmetic total of 44 is already Low.

## 1. Section 7 checklist

| Row | Notes | Evidence (location) | Score |
|---|---|---|---|
| 1.1 Variables respected | Asset is the FTSE 100 cash index, with Euro Stoxx 50 as reference and no cards on it. GBP index points, 5-session lookback and as-of 20 May are right. Counters are USDX / S&P 500 / DAX 40, with no slice available to check DAX. **Daily-open anchor is 00:00 UK, not 07:00 UK**, presented as an analyst override and cited as authority on the cards. The brief and the fixed card rules say the populated value governs. "Sources" are mostly aggregators (Investing, Stooq, Yahoo, TE) with no sell-side tier in §4. | Run note; §2; §4; §20 "Configuration override"; §21b Trade 1 Entry | 2 |
| 1.2 Coverage & currency consistent | Data window is D-1 and the session is D. But the **daily pivots are struck from 19 May (D-2)**, not D-1 (§11 heading). The upcoming calendar is mis-dated: "Thu 22 May" is a Friday; the Eurozone flash PMIs are placed "w/c 25 May" but the calendar puts them on 21 May (D). 25 May bank holiday is not mentioned. No currency drift. | §11 daily heading; §13d; §1; §12; §18 | 3 |
| 1.3 Audience & tone | Strategist register, trading and risk review, no retail tone. Leading "Run note" is administrative but acceptable. | §1, §18 | 4 |
| 2.1 Sections present & ordered | §1–§21 all present and in order, including §13a–d and §21a–d. §7 images are dropped by pandoc; five captions accepted as placeholders. | headings | 5 |
| 2.2 Scorecard as table | §6 is a correct table with all required columns. §11 tables are asymmetric: R1–R5 but only S1–S3, while the caption claims "R5→P→S5". The spec is three levels each side (R3→P→S3). Prior-period H/L/C inputs are not printed above any pivot table. | §6; §11 | 3 |
| 2.3 Method steps visible | Observations → classification → consensus is shown (§4–§5). §8 is candle-by-candle with a sequence call. §9 shows overlap, persistence and VOLator slope. Missing: the RSI2 working line, a numeric ATR(14), and the KER period and smoothing. | §4–§9 | 4 |
| 3.1 Quantitative claims sourced | Many §1/§12/§14 figures carry no source. "3.0% consensus" for UK CPI contradicts the calendar consensus of 3.8 (actual 2.8, prior 3.4). "Unemployment 4.9% prior" is the consensus; the prior was 4.8 (actual 5.0). "DAX near 24,400", "crude near four-year highs" and "VIX high-teens" are unattributed. | §12; §13c; §14; §10 | 2 |
| 3.2 Citations exist & contain data | Three spot-checks. (a) Trading Economics 20 May, "finish broadly flat": the report's own §6/§8 show 20 May as a +62.3 pt (+0.60%) bullish candle with RSI2 100. §13c itself says "flat-to-higher". Contradicted. (b) Analytics Insight 19 May, "opened 51 points higher": the report's §6 gives the 19 May open as 10,303.7, identical to the 18 May close (gap 0.0). Contradicted by the report's own table. (c) CNBC 18 May "European markets rebound": consistent with the +1.05% rebound in §6. Two of three fail on the report's own figures, and the quoted figure is not used consistently. Treated as fabricated per brief §2 row 3.2. Cited URLs are live quote or landing pages (tradingeconomics.com/united-kingdom/stock-market, cnbc.com/quotes/.FTSE) that cannot carry a dated article. | §13a; §6; §8; §13c | 0 |
| 3.3 Calculations transparent | RSI2 reproduces from the report's own closes: 18 May 31.3 (gain 108.3 vs loss 237.6), 19 May 100, 20 May 100. 14 and 15 May cannot be tested without earlier closes. Pivot arithmetic is internally exact (R2−P = P−S2 = H−L on all three tables) and the §21a sum is exact (0.3985 ≈ +0.40). But **ATR(14) is never printed**; it is only implied (3×ATR cap 10,756.9 − 10,393.0 = 363.9, so ATR ≈ 121.3; "~120" in §16). KER is given as −0.14 without period or smoothing. R ÷ ATR is not printed on any card. | §6; §9; §11; §16; §21a/b | 3 |
| 3.4 Numbers reconcile | D-1 close 10,393.0 is identical in §1, §3, §4, §6 and the Trade 1 entry. Weekly pivots on cards match §11. Breaks: (i) the weekly table implies H 10,512.3 / L 10,262.1 / C 10,381.5 for "11–15 May", but §6 shows 15 May closing 10,195.4 with a 10,180.5 low, so the pivot inputs contradict the report's own table; (ii) §13c "FTSE fell 1.7% to 10,195" vs §6 −2.28% (10,433.0 → 10,195.4); (iii) §21a's "three highest-weighted signals" omits VOLator +0.05, which exceeds the cross-asset +0.045 it lists; (iv) §21d "TP1 hit rate 20%" while no §21c outcome reaches +1R; (v) the short-term signal is +1.00 while §8 judgement is "Indecision". | §6, §11, §13c, §21 | 3 |
| 4.1 Pillars conclude | §8 Indecision, §9 Transitional / Neutral, §10 MIXED, §12 each sub-head labelled. §14 sub-heads are only partly labelled (Rates, Energy and Positioning carry no direction label). | §8–§14 | 4 |
| 4.2 Cross-asset interpreted | Mechanisms are given, but the reads are wrong against the slice. USDX closed 98.478 (13 May) → 99.150 (20 May), i.e. rising, not "falling / flat" or "soft". S&P 500 closed 7,461.9 → 7,420.6 over the same window (−0.55%; 14 May close 7,506.5 → −1.1%), not "rising". Both "Confirms" labels, and hence the +0.30 cross-asset input, rest on mis-read counters. The USD mechanism is also muddled: §10/§14 say a softer dollar "lifts the GBP value" of overseas earnings, while §12 says a weaker pound does. | §10; §12; §14 vs USDX/US500 slices | 2 |
| 4.3 Synthesis reconciles tensions | §15/§16/§18 address the KER-vs-VOLator conflict and the DAX non-confirmation. They do not reconcile the +1.00 short-term signal with the "Indecision" label, or the +0.50 medium-term regime signal with the "Neutral" bias in §9. With the short-term signal at 0 the score is 0.149 (< 0.25), which would suppress Trade 1. The §16/§17 thesis rests on a weekly-P / monthly-S1 "confluence" that disappears when the pivots are recomputed (see C3 below). | §9; §16–§18; §21a | 3 |
| 4.4 Calibrated language | §17 is one bold sentence. A second italic meta-sentence sits under it. Confidence "Medium" is stated in §1/§3. No hedge stacking. | §3, §17 | 4 |
| 4.5 Card construction (protocol: scored under C4) | Trade 2 is issued although the report states every pivot tier is single-source-indicative (§11, §19, §20). The fixed rule is "suppress Trade 2", and the report cites a run-time instruction as its reason. Trade 3C is issued with the report itself stating the break is "NOT yet confirmed" (a fixed suppression trigger). Trade 1 entry is 29.9 pts off the D-1 close. ATR, R ÷ ATR and the signed gap to the reference close are absent. Stops and targets are not given in both price and points on Trades 2 and 3C. | §21b | 1 |
| 5.1 Data dated; staleness flagged | Prices and articles are dated. Pivot single-source status is flagged. The one-session-stale daily pivots are not flagged as stale. §19 asserts "no OHLC field was synthesised" while every open in §6 equals the prior close (below). | §4, §6, §11, §13, §19 | 3 |
| 5.2 Assumptions up front | The anchor override and the pivot single-source flag are surfaced up front (Run note) and in §19/§20. But §19 says the April H/L/C was "approximated from the available validated window", an assumption that contradicts the no-synthesis rule, and the basis and ATR are not stated. | Run note; §19; §20 | 3 |
| 5.3 Red flags surfaced | §12/§15 risks and DAX non-confirmation are surfaced. The Tier-1 collision carried onto the cards is the wrong date and weekday ("Thu 22 May MPC"). The calendar rows for D show no MPC decision. D-day Tier-1 events are omitted: BoE Governor Bailey speech 21 May 18:00 broker (HIGH) and the UK / Eurozone flash PMIs. §13c omits the 20 May UK CPI release (HIGH) and the 20 May Bailey speech. | §12; §13c/d; §21b caveats | 2 |
| 5.4 Restrictions honoured | **Breaches.** (i) A run-time instruction is cited as authority to issue cards the fixed rules suppress ("per the run instruction", §11, §19, §20, §21b). (ii) The module code "M5" appears in the §20 heading "Strategy trace (M5)". (iii) Provider ticker codes appear in the body: ^FTSE, ^STOXX50E, ^ftm. (iv) The monthly pivot input is "approximated". (v) §6 opens are chained to the prior close (see C3). | §11, §19, §20, §21b, §2, §4, §6 | 1 |

## 2. Category roll-up

| # | Category (max) | Row mean | Level | Multiplier | Points | Justification |
|---|---|---|---|---|---|---|
| 1 | Prompt adherence (20) | 3.0 → 3, **−1 for restriction breach** | 2 | 0.40 | 8.0 | Anchor overridden to 00:00 UK and defended by a run-time instruction. Suppression gates overridden. Wrong-day daily pivots. |
| 2 | Structure (20) | 4.0 | 4 | 0.85 | 17.0 | All 21 sections present and ordered. The pivot tables are asymmetric and carry no inputs. |
| 3 | Accuracy & evidence (25) | 2.0 → 2, **set to 0 by hallucinated-source override** | 0 | 0.00 | 0.0 | See §3 below. Citations fail on the report's own figures; D-1 OHLC and all three pivot sets are far outside tolerance. |
| 4 | Reasoning & judgment (20) | 2.8 → 3 | 3 | 0.65 | 13.0 | The directional narrative is internally coherent. The counters are mis-read, the signal inputs are inconsistent with the stated labels, and two cards are issued against fired suppression gates. |
| 5 | Currency & transparency (15) | 2.25 → 2 | 2 | 0.40 | 6.0 | Stale daily pivots, a mis-dated dominant catalyst, omitted D-day events, and several restriction hits. |
| | **Total** | | | | **44** | |

## 3. Category 3 data comparison (report vs `UK100_by_date/2026-05-21.csv`, cash basis)

Tolerance (brief §4): |Δ| ≤ 5 pts on a close, ≤ 10 pts on O/H/L. Δ = report − data.

### 3a. D-1 OHLC block (§6) vs `qa_slice_stats.py --cash-open 10:00 --cash-close 18:30`

| Date | Open (rep / data / Δ) | High | Low | Close |
|---|---|---|---|---|
| 14 May | 10,381.5 / 10,319.3 / **+62.2** | 10,449.3 / 10,371.1 / **+78.2** | 10,358.2 / 10,301.1 / **+57.1** | 10,433.0 / 10,355.8 / **+77.2** |
| 15 May | 10,433.0 / 10,299.0 / **+134.0** | 10,446.8 / 10,309.4 / **+137.4** | 10,180.5 / 10,154.9 / **+25.6** | 10,195.4 / 10,167.0 / **+28.4** |
| 18 May | 10,195.4 / 10,144.5 / **+50.9** | 10,328.6 / 10,336.3 / −7.7 (ok) | 10,188.9 / 10,141.2 / **+47.7** | 10,303.7 / 10,290.8 / **+12.9** |
| 19 May | 10,303.7 / 10,339.9 / **−36.2** | 10,366.5 / 10,408.9 / **−42.4** | 10,279.1 / 10,313.0 / **−33.9** | 10,330.6 / 10,325.1 / +5.5 (marginal) |
| 20 May (D-1) | 10,330.7 / 10,274.4 / **+56.3** | 10,458.3 / 10,458.8 / −0.5 (ok) | 10,279.1 / 10,272.8 / +6.3 (ok) | **10,393.0 / 10,422.9 / −29.9** |

- 3 of the five closes miss by more than 15 pts (14, 15 and 20 May); 18 May misses by 12.9 and 19 May by 5.5, both outside the 5-pt close tolerance. On the full-day basis the D-1 close is 10,443.3, so the report misses by −50.3.
- 12 of 15 open / high / low cells miss by more than 10 pts. Only 3 pass: 18 May high, 20 May high, and 20 May low.
- **Opens are chained.** The 15, 18, 19 and 20 May opens equal the prior close (to 0.1). The slice's actual open-vs-prior-close gaps are −56.8, −22.5, +49.1 and −50.7. Observed opens do not behave this way, which points to synthesised opens. §19 claims no field was synthesised.
- The §6 "corroborated within ±0.10" claim, and four sources all at exactly 10,393.0 in §4, cannot be reconciled with a cash close 29.9 pts higher. §3's own range, 10,360–10,410, and Yahoo's 10,408, already show tens of points of dispersion.
- RSI2 recomputed from the report's own closes (`--closes`): 18 May 31.3, 19 May 100.0, 20 May 100.0. These match. The 14 and 15 May rows are untestable. The RSI2 arithmetic is not a failure; the closes it is built on are wrong by more than 15 pts on D-1.
- Data RSI2 on cash closes is 100.0 / 24.78 / 39.60 / 100.0 / 100.0 for 14–20 May, against the report's 100.0 / 17.8 / 31.3 / 100.0 / 100.0. The 15 and 18 May values differ by 7–8 points because the closes differ.

### 3b. ATR(14)

| | Value |
|---|---|
| Report (implied, never printed) | ≈ 121.3 (3×ATR runner cap 363.9) and "~120" in §16 |
| Data, cash bars | 151.76 (Δ ≈ −30.5, −20%) |
| Data, full-day bars | 167.91 |

With the data ATR, Trade 1's R of 144 is 0.95×ATR, so the "wide stop" flag the report sets is an artefact of the understated ATR.

### 3c. Pivots (§11) vs level file

| Table | Report P / R1 / S1 | Data (cash) P / R1 / S1 | Δ P |
|---|---|---|---|
| Daily (report: from 19 May; data: from D-1 = 20 May) | 10,325.4 / 10,371.7 / 10,284.3 | 10,384.83 / 10,496.87 / 10,310.87 | **−59.4** (stale session) |
| Weekly (11–15 May, 2026-W20) | 10,385.3 / 10,508.5 / 10,258.3 | 10,228.0 / 10,310.1 / 10,084.9 | **+157.3** (R1 +198.4, S1 +173.4) |
| Monthly (April 2026) | 10,528.0 / 10,652.7 / 10,388.0 | 10,418.8 / 10,650.0 / 10,140.1 | **+109.2** (S1 +247.9) |

- Daily other levels. Report R2 10,412.8 / R3 10,459.1 / S2 10,238.0 / S3 10,196.9. Data R2 10,570.83 / R3 10,682.87 / S2 10,198.83 / S3 10,124.87. Deltas are −158.0, −223.8, +39.2 and +72.0.
- Weekly. The report's table implies H 10,512.3, L 10,262.1, C 10,381.5. The data (cash) give H 10,371.1, L 10,145.9, C 10,167.0. The implied C equals the report's *14 May open* and does not match §6's 15 May close of 10,195.4.
- Monthly. The report's table implies H 10,668.0, L 10,403.3, C 10,512.7. The data give H 10,697.5, L 10,187.6, C 10,371.3. §19 admits the April H/L/C was "approximated".
- Consequence: the "weekly-P / monthly-S1 confluence at 10,385–10,388" is the central support claim in §1, §11, §15, §16, §17, §18 and Trade 1/Trade 2 confluences. In the level file weekly P is 10,228.0 and monthly S1 is 10,140.1, 87.9 pts apart. There is no confluence.
- "Daily R1 (10,372) now broken": in the data, daily R1 is 10,496.87 and the cash D-1 close 10,422.9 is below it.

### 3d. Other checks against the slices

- 25-session range (Trade 3C). The report uses high 10,668.0 / low 10,180.5 (width 487.5). Cash data give high 10,666.5 (17 Apr) / low 10,141.2 (18 May), width 525.3. The high is within tolerance; the low is +39.3 off. The report's low is the 15 May low, not the 18 May low.
- KER(13, EMA 3). Recomputed from cash daily closes it is about +0.03. The report's −0.14 "Trending Down — Moderate" is not reproduced, and the headline "KER contradicts price" tension in §1/§9 is not supported on this basis.
- Counters. USDX 13 May close 98.478 → 20 May 99.150 (up). S&P 500 7,461.9 → 7,420.6 (down). VIX closed at 18.45 on 20 May (the "high teens" claim holds). DAX has no slice.
- Calendar. UK CPI y/y on 20 May: actual 2.8, consensus 3.8, previous 3.4 (HIGH). Unemployment on 19 May: actual 5.0, consensus 4.9, previous 4.8. Calendar rows for D: UK and Eurozone flash PMIs, BoE Governor Bailey speech (HIGH), and others. No MPC decision row appears in the slice through D, and 22 May 2026 is a Friday.

## 4. Override check

- **Hallucinated source: fires.** Two of three spot-checked citations are contradicted by the report's own figures (3.2 above). The "four independent core feeds at exactly 10,393.0" cluster is also unreconcilable with the slice or with the report's own §3 dispersion. Cap Low (40–59); C3 = 0.
- **Restriction breach: also fires.** A run-time instruction is cited as authority for issuing suppressed cards. The module code "M5" appears. Provider tickers appear. A synthesised or approximated input is presented as sourced. The anchor is not the populated value. Cap Moderate (60–74); C1 reduced one level, applied above.
- Binding cap is Low. Arithmetic total 44, band Low. Not capped further.

## 5. Card Integrity (from `qa/ftse_qa1/lint_static/2026-05-21.csv`, copied verbatim; not re-derived)

| card_id | strategy | flags | dud | Card Integrity |
|---|---|---|---|---|
| 2026-05-21_Trade_1 | Trade 1 — Daily Directional (LONG) | CLEAN | False | 100 |
| 2026-05-21_Trade_2 | Trade 2 — Pivot | CLEAN | False | 100 |
| 2026-05-21_Trade_3C | Trade 3C — Momentum-Breakout | CLEAN | False | 100 |

Report-level Card Integrity = mean of 3 non-suppressed cards = **100.0** (n_cards = 3, n_duds = 0, n_warns = 0).

Note. The static linter checks geometry from each card's own numbers only. It does not test the suppression gates, the order-side rule against the true D-1 close, or the ATR basis. Card Integrity is therefore separate from, and not a statement about, the card-construction findings under row 4.5 and in the feedback file.

## 6. Feedback
See `qa/ftse_qa1/2026-05-21_feedback.md`.
