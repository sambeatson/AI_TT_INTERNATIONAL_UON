# Trust Score v3.7 — FTSE_EuroStoxx_Report_21Jul2026.md (D = 2026-07-21)

Level file check: `last_bar_date` = 2026-07-20 < D (no leak). Slice last bar 2026-07-20 22:45 broker. Basis: report claims cash index closes, so comparisons use the `_cash` columns (UK window 10:00-18:30 broker). Full-day (`_full`) figures are given where they change the reading.

## Result

```
c1=3
c2=4
c3=2
c4=3
c5=3
total=63
band=Moderate
override=restriction_breach
card_integrity=83.3
n_cards=3
n_duds=1
n_warns=1
```

Override basis: the report leaks a module code, "Strategy trace (M5)" in §20 (line 230). Brief §2 row 5.4 lists "no module codes (M1..M5)" as a prompt restriction, so the restriction-breach override applies. The cap is Moderate (60-74). C1 is reduced one level, from 4 to 3. The pre-override total would be 66 (C1 = 4). The score is 63 either way, so the band is Moderate without the cap binding.

## 1. Section 7 checklist

| Row | Reviewer notes | Evidence | Score |
|---|---|---|---|
| 1.1 Variables respected | Asset is the FTSE 100 cash index; CFD is excluded and labelled so (§4, §5). Counters USDX, S&P 500, DAX 40 and Euro Stoxx 50 are present (§10). As-of is D-1 close, Europe/London, 5-session lookback, GBP points. Gaps: (a) none of the cited sources is an index-provider, exchange or sell-side tier. All are media or aggregators (Investing, Yahoo, Alliance, Proactive, Reuters, Trading Economics, "Sunday Guardian"), against a brief requirement of ≥ 6 from those tiers. (b) The daily-open anchor is 00:00 UK, not 07:00 UK. This is disclosed on the card and in §21 as a "run instruction", which I cannot verify. | §2, §4, §20, §21 note | 3 |
| 1.2 Coverage & currency consistent | All data dates are ≤ 20 Jul and the session date is 21 Jul. GBP/points is consistent. Drift is in weekday labels: §13c has "Wed 16 Jul" (GDP) and "Thu 16 Jul" (China GDP) for the same date (16 Jul 2026 is a Thursday). §21c labels 14 Jul as Mon, 15 Jul as Tue, 16 Jul as Wed and 17 Jul as Thu (real: Tue, Wed, Thu, Fri) and lists "Fri 18 Jul" (a Saturday) as a non-session row. | §13c, §21c | 4 |
| 1.3 Audience & tone | Senior strategist tone, risk-review framing, no retail language. | §1, §18 | 4 |
| 2.1 Sections present & ordered | §1-§21 are all present and in order, including §13a-d and §21a-d. §7 holds captions for 5 charts and no images (accepted per brief; pandoc drops images). | headings | 5 |
| 2.2 Scorecard as table | §6 is a table with all required columns. §11 daily/weekly/monthly tables are present. The daily table runs R5→S5 (11 levels), beyond the specified R3→S3. The Euro Stoxx table is condensed to 3 sessions. | §6, §11 | 4 |
| 2.3 Method steps visible | §4 → §5 consensus, §8 candle by candle plus a sequence label, and §9 with overlap/persistence/VOLator/KER are all visible. RSI2 and ATR working are not shown (see 3.3). | §4-§9 | 4 |
| 3.1 Quantitative claims sourced | §4/§6 are sourced per row. In §1, §12 and §14 several figures carry no source or pointer: 10-yr gilt ~4.98%, GBP ~1.34, EUR ~1.14, VIX ~18.8 (+12% Fri), BoE 3.75%, "~£24bn", Nasdaq −2.9%. Slice check: VIX closed 18.17 (+3.2%) on 17 Jul and 18.02 on 20 Jul, not "18.8 (+12% Fri)". §13d lists the consensus as "Unemp. 4.9%; earnings ex-bonus 3.4%". The calendar for D has consensus 4.6 and 3.3, and 4.9 and 3.4 are the previous values. | §1, §12, §13d, §14 | 3 |
| 3.2 Citations exist & contain data | Three spot-checks. (1) Alliance News 20 Jul 16:35, 10,524.76, −75.61 (−0.7%): consistent (−75.61/10,600.37 = −0.71%). (2) Reuters 20 Jul 10:52 GMT 10,543.91, "fell 0.5%": consistent (−0.53% vs 10,600.37). (3) Proactive/Sharecast 20 Jul "16:11", "~10,524", labelled "Cash close · Core, corroborates close": a 16:11 stamp precedes the 16:30 cash close, and its own headline reads "set to end on a low note", so it is a pre-close article used as a close. It is also a rounded figure 0.76 pt from 10,524.76, outside the ±0.10 pt corroboration tolerance the report states (§5, §20). It is a weak corroboration, not impossible. Nothing is demonstrably fabricated, so no hallucination override. Note "Sunday Guardian" as a source for Wed 15 Jul and Fri 17 Jul is odd; I could not verify it. | §4, §5, §6, §13a, §20 | 3 |
| 3.3 Calculations transparent | Pivot arithmetic reproduces from the report's own H/L/C for daily and weekly (checked P, R1-R3, S1-S3, R1.5, S1.5). RSI2 does not reproduce from the report's own closes (10,519.00, 10,515.92, 10,572.24, 10,600.37, 10,524.76): the script gives 16 Jul 94.8, 17 Jul 100.0 and 20 Jul 27.1, against the report's 49.5, 65.4 and 24.3. No RS working is shown. ATR(14) "≈ 96" is stated, but §19 admits it uses "approximated prior-session ranges", against 118.2 (cash) / 134.8 (full) in the level file. KER −0.26 cannot be reproduced. KER(13) on the slice's cash closes is ≈ +0.09 (EMA3 ≈ +0.085), opposite sign and inside the ±0.13 trend gate. §13b tilt arithmetic is wrong: the denominator 1.0+0.5×4+0.7+0.5 = 4.2, not 5.2, so the strict result is −2.5/4.2 = −0.60, not −0.48. The "softened to −0.30" is an ad hoc adjustment that cannot be reproduced. §21a contributions sum correctly (−0.615) but the signal behind Kaufman −0.07 is not stated. | §6, §9, §13b, §20, §21a | 2 |
| 3.4 Numbers reconcile | Internal: D-1 close 10,524.76 is identical in §1, §3, §4, §6, §21b. Pivots in §11 equal the pivots on the cards. ATR 96 is consistent. RSI2 24.3 is consistent across §6, §8, §21a (but wrong, see 3.3). Breaks: §13c says 16 Jul "FTSE −0.5%" and "index still eased", while §6/§8 show 16 Jul +0.54% as a bullish close at the high. §21b Trade 1 says TP1 10,400.76 is "below daily S3 (10,391)" but 10,400.76 > 10,391.01. §21d says "two trend-aligned days (16-17 Jul long, 20 Jul short)", which is three. §21d TP1/2/3 hit rates (40/0/0) are not derivable from §21c. Against data (see §2 below): 3 of 5 closes are > 15 pts from the slice cash close (15 Jul +17.2, 16 Jul +31.8, 17 Jul +27.0). The D-1 close is +9.96 vs 10,534.7. 10 of 15 O/H/L cells exceed the 10 pt tolerance, including opens 38-62 pts off. The 25-session low is 10,180 against 10,328.1 (−148). | §6, §13c, §21 | 2 |
| 4.1 Pillars conclude | §8 ("Indecision → Range/Exhaustion"), §9 ("Neutral-to-Bearish") and §10 ("CONFIRM bearish") end in direction labels. §12 tags each item cyclical/structural with price effects but has no closing direction. §14 has bullets and a watch item but no direction. | §8-§14 | 3 |
| 4.2 Peer/cross-asset interpreted | §10 gives mechanisms for USDX (two-sided: risk headwind vs overseas-earner tailwind), S&P (risk beta) and DAX. The FTSE energy/dollar-earner weight is explained in §10/§12. Oil is a mechanism in §12 only, not in the §10 table. | §10, §12 | 4 |
| 4.3 Synthesis reconciles tensions | The KER vs ranging-regime conflict is addressed (§9), and the STOXX divergence is flagged. Weak points: the §8 label "Indecision / reversal risk" is converted into a full −1 bearish technical signal (−0.25 contribution). Cross-asset takes a full −1 signal (−0.15) although §10 says USDX is neutral and only two of three confirm. SHORT −0.61 is high conviction against "modest bearish bias" (§17) and "reduced-conviction / breakout-watch" (§9). | §8-§10, §17, §21a | 3 |
| 4.4 Calibrated language | §17 is exactly one sentence with no hedge stacking. Confidence "Medium" is stated in §3 and §18. | §3, §17, §18 | 4 |
| 4.5 Card construction (protocol: scored under C4) | Trade 1: stop uses the 5-day swing high where the rule is the tighter of swing/nearest S/R. ATR input 96 is understated. TP1 claim is false. Trade 2: TP3 is not beyond TP2, there is no tranche management, and the stop buffer is ≈ 0.1×ATR where the rule is 0.25×ATR. Trade 3C: entry, TP1, TP2, TP3 and R are unpriced. The boundary is the S1 confluence, not the 25-day low. The stop uses the wrong anchor for a short. The 25-day low (10,180) is wrong. Linter: 1 DUD and 1 WARN. See feedback. | §21b | 2 |
| 5.1 Data dated; staleness flagged | Prices and articles are dated. The 15 Jul H/L widening, the monthly single-source status and the ATR approximation are flagged. Not flagged: the Open column looks like a proxy. 16 Jul open = 15 Jul close (10,515.92). 17 Jul open 10,572.39 ≈ 16 Jul close 10,572.24. 20 Jul open 10,600.00 ≈ 17 Jul close, and the 20 Jul High 10,600.37 equals the 17 Jul close exactly. These opens are 38-62 pts from the slice cash opens yet are marked CORROBORATED (Δ≈0.0). The footnote claims corroboration only for closes. | §6, §19 | 3 |
| 5.2 Assumptions up front | The anchor override is stated on the Trade 1 card and in the §21 note, but not in §20 (Agent Log), as the brief expects. The ATR approximation is disclosed in §19 but not on the cards that depend on it. Monthly single-source tiers are marked not used on Trade 2. | §19, §20, §21b | 3 |
| 5.3 Red flags surfaced | §12/§15 carry the key risks. The CPI collision is carried into the Trade 1 and 3C caveats. Not carried: the UK labour-market release (Tue 21 Jul 09:00 broker = 07:00 UK, per the D calendar) falls inside the Trade 1 window, and the Trade 2 caveat omits the CPI collision. | §13d, §21b | 4 |
| 5.4 Restrictions honoured | CFD excluded from OHLC, no futures, no bracketed variables, no framework name. Breach: "Strategy trace (M5)" in §20 is a module code. Also, the §3 rationale calls "~10,543 mid-session" a CFD print while §4 attributes 10,543.91 to Reuters (cash, intraday), a labelling inconsistency. The Open column looks like a proxy (see 5.1). | §3, §4, §20 | 2 |

## 2. Category 3 data comparison (report vs `_cash` slice; CFD vs cash basis tolerance: close ≤ 5, O/H/L ≤ 10)

| Date | Field | Report | Slice cash | Δ | Within tol.? |
|---|---|---|---|---|---|
| 14 Jul | Open | 10,520.00 | 10,460.4 | +59.6 | no |
| | High | 10,545.00 | 10,545.8 | −0.8 | yes |
| | Low | 10,433.12 | 10,411.5 | +21.6 | no |
| | Close | 10,519.00 | 10,507.0 | +12.0 | no |
| 15 Jul | Open | 10,515.00 | 10,460.7 | +54.3 | no |
| | High | 10,545.00 | 10,536.2 | +8.8 | yes |
| | Low | 10,455.00 | 10,431.0 | +24.0 | no |
| | Close | 10,515.92 | 10,498.7 | +17.2 | no (> 15) |
| 16 Jul | Open | 10,515.92 | 10,453.9 | +62.0 | no |
| | High | 10,572.24 | 10,550.5 | +21.7 | no |
| | Low | 10,471.97 | 10,429.4 | +42.6 | no |
| | Close | 10,572.24 | 10,540.4 | +31.8 | no (> 15) |
| 17 Jul | Open | 10,572.39 | 10,534.1 | +38.3 | no |
| | High | 10,623.69 | 10,616.2 | +7.5 | yes |
| | Low | 10,527.65 | 10,514.9 | +12.8 | no |
| | Close | 10,600.37 | 10,573.4 | +27.0 | no (> 15) |
| 20 Jul (D-1) | Open | 10,600.00 | 10,540.1 | +59.9 | no |
| | High | 10,600.37 | 10,589.4 | +11.0 | no |
| | Low | 10,505.00 | 10,503.1 | +1.9 | yes |
| | Close | 10,524.76 | 10,534.7 | −9.9 | no (> 5, ≤ 15) |

The full-day D-1 close is 10,453.0 (23:45 bar), 71.8 below the report. The report's basis is cash, so this is context only.

Other D-1 fields (level file):

| Item | Report | Level file (cash / full) | Δ |
|---|---|---|---|
| RSI2 (20 Jul) | 24.3 | 46.03 / 7.74 | −21.7 vs cash. The report's own closes give 27.1 (the report's number is also wrong against its own data). |
| ATR14 | ≈ 96 | 118.2 / 134.8 | −22.2 / −38.8 |
| 5d swing high / low | 10,623.69 / 10,433.12 | 10,616.2 / 10,411.5 | +7.5 / +21.6 |
| 25d high / low | 10,747.01 / 10,180.00 | 10,739.6 / 10,328.1 (full 10,318.1) | +7.4 / −148.1. Width 567 vs 411.5. |
| 20 Jul day move | −75.61 (−0.7%) | −38.7 (−0.37%) cash | the report's drop is about twice the cash CFD drop. |

Daily pivots (report from 20 Jul H 10,600.37 / L 10,505 / C 10,524.76; level file `d_cash_*`):

| Level | Report | Level file | Δ |
|---|---|---|---|
| R3 | 10,677.12 | 10,668.0 | +9.1 |
| R2 | 10,638.75 | 10,628.7 | +10.05 |
| R1 | 10,581.75 | 10,581.7 | +0.05 |
| P | 10,543.38 | 10,542.4 | +1.0 |
| S1 | 10,486.38 | 10,495.4 | −9.0 |
| S2 | 10,448.01 | 10,456.1 | −8.1 |
| S3 | 10,391.01 | 10,409.1 | −18.1 |

Weekly pivots (W/E 17 Jul; level file `w_cash_*`):

| Level | Report | Level file | Δ |
|---|---|---|---|
| R3 | 10,862.24 | 10,860.6 | +1.6 |
| R2 | 10,742.96 | 10,738.4 | +4.6 |
| R1 | 10,671.67 | 10,655.9 | +15.8 |
| P | 10,552.39 | 10,533.7 | +18.7 |
| S1 | 10,481.10 | 10,451.2 | +29.9 |
| S2 | 10,361.82 | 10,329.0 | +32.8 |
| S3 | 10,290.53 | 10,246.5 | +44.0 |

Monthly pivots (June; level file `m_cash_*`):

| Level | Report | Level file | Δ |
|---|---|---|---|
| R3 | 11,229.67 | 11,180.73 | +48.9 |
| R2 | 10,959.33 | 10,894.77 | +64.6 |
| R1 | 10,722.67 | 10,698.13 | +24.5 |
| P | 10,452.33 | 10,412.17 | +40.2 |
| S1 | 10,215.67 | 10,215.53 | +0.1 |
| S2 | 9,945.33 | 9,929.57 | +15.8 |
| S3 | 9,708.67 | 9,732.93 | −24.3 |

The monthly set is honestly flagged single-source and not used on cards.

Counters (slices): USDX 20 Jul close 100.97, consistent with "~100.7-100.9 flat-to-firmer". S&P 500 15→20 Jul −1.7%, consistent with "−1.6% wk". VIX does not match (18.02, not ~18.8; Fri +3.2%, not +12%).

RSI2 trend labels: with the report's own closes, 16 Jul (RSI2 94.8, close > open) should be Bullish, not Neutral, and 17 Jul stays Bullish at 100.0.

## 3. Category roll-up

| Cat | Level | Multiplier | Points | Justification |
|---|---|---|---|---|
| C1 Prompt adherence (20) | 3 | 0.65 | 13.0 | Rows 3/4/4 give 4 before override. Restriction-breach override (module code "M5" in §20) reduces it to 3. Source tiers and the 00:00 anchor deviation also weigh. |
| C2 Structure (20) | 4 | 0.85 | 17.0 | All sections are present and ordered, and the tables are tables. Minor: charts are captions only, the daily pivot table is over-extended, and the STOXX table is condensed. |
| C3 Accuracy & evidence (25) | 2 | 0.40 | 10.0 | RSI2 does not reproduce from the report's own closes. 3 of 5 closes are > 15 pts from the slice. Opens are 38-62 pts off. ATR, 25d low and KER sign are wrong. The sentiment tilt arithmetic is wrong. Weekday and 16 Jul direction contradictions. Not fabricated. |
| C4 Reasoning & judgment (20) | 3 | 0.65 | 13.0 | Cross-asset mechanisms are good and the §17 sentence is calibrated. Signal derivation is over-stated relative to the narrative, and card construction is weak (2). |
| C5 Currency & transparency (15) | 3 | 0.65 | 9.75 | Data is dated and the main single-source flags are present. The Open proxy pattern is unflagged, the anchor override is missing from §20, and the module code leaks. |

Sum = 62.75 → total = 63.

## 4. Total, band, override

- Total: 63 / 100. Band: Moderate Trust (60-74).
- Hallucinated source: none established (three-source spot check; Proactive "16:11 close" is a weak corroboration, not a fabrication).
- Restriction breach: yes (module code "M5" in §20). Cap Moderate, C1 reduced one level. `override=restriction_breach`.

## 5. Card Integrity (linter rows copied verbatim from `lint_static/2026-07-21.csv`)

| card_id | strategy | flags | dud | card score |
|---|---|---|---|---|
| 2026-07-21_Trade_1 | Trade 1 — Daily Directional (SHORT — TRANSITION/bearish score) | CLEAN | False | 100 |
| 2026-07-21_Trade_2 | Trade 2 — Pivot (TRANSITION: breakout-side limit only, aligned with 3C short) | WARN_TP3_ORDER | False | 90 |
| 2026-07-21_Trade_3C | Trade 3C — Momentum-Breakout (post-consolidation) | UNPRICED | True | 60 |

Report-level card_integrity = (100 + 90 + 60) / 3 = 83.3. n_cards=3, n_duds=1 (UNPRICED, `dud=True`), n_warns=1. No card is suppressed. Card Integrity is separate from the 100.

## 6. Feedback

See `qa/ftse_qa1/2026-07-21_feedback.md`.
