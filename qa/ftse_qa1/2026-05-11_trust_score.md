# Trust Score v3.7 review — FTSE 100 daily report, D = 2026-05-11

Report: `reports/md/FTSE_EuroStoxx_Daily_Report_2026-05-11.md`
Data: `data/levels/UK100_by_date/2026-05-11.csv` (`last_bar_date` = 2026-05-08 < D, leak check passed); slice `UK100_upto_2026-05-10.csv` (last bar 2026-05-08 22:45 broker); `qa_slice_stats.py --cash-open 10:00 --cash-close 18:30`.
Basis: the report claims the FTSE Russell official cash close, so the `_cash` columns are used. `_full` is quoted where it changes the verdict.

## Score block

```
c1=2
c2=4
c3=1
c4=3
c5=2
total=49
band=Low
override=restriction_breach
card_integrity=80.0
n_cards=3
n_duds=1
n_warns=0
```

`n_cards=3` counts the three linter rows. Two are non-suppressed and scored for Card Integrity (Trade 2 and Trade 3C). The override cap (Moderate, 60–74) is not binding because the raw total is already Low.

## 1. Section 7 checklist

| Row | Notes | Evidence | Score | Action |
|---|---|---|---|---|
| 1.1 Variables respected | FTSE 100 cash is primary and Euro Stoxx 50 is secondary with no cards. Counters are USDX, S&P 500 and DAX, with Brent in §14. The anchor is 07:00 UK and the lookback is 5 sessions. GBP and index points are used. The §4 and §20 claim of "six sources" for FTSE is not met: §4 lists four FTSE rows (FTSE Russell, Yahoo, Trading Economics, BBN Times). Investing.com appears for FTSE only in §20. No exchange or sell-side tier source is named. The lookback table is mis-dated (see 1.2). | §2, §4, §20 | 3 | Make §4 list all six sources actually used. |
| 1.2 Coverage and currency consistent | Date drift points: (a) §6 labels the first session "Fri 2 May 2026", but 2 May 2026 is a Saturday, and the data's session is Fri 1 May (4 May is the bank holiday). (b) "Wed 21 May" is used for UK CPI in §1/§12/§13d/§14/§16/§17/§18, and 21 May 2026 is a Thursday. (c) §13d lists "Wed 20 May" and "Wed 21 May" as both Wednesdays. (d) §12 puts the eurozone HICP final on Wed 21 May but §13d puts it on 20 May. (e) §18 calls 10,228 the "5 May FTSE Russell close" when it is the 8 May close. (f) IAG's profit warning is "Friday" in §12 and "Thu 7 May" in §13d. No currency or unit drift. | §6, §12, §13d, §18 | 2 | Correct weekday and date labels. |
| 1.3 Audience and tone | Senior strategist register, trading-and-risk use, no retail tone. Internal build language leaks (see 5.4). | §1, §18 | 4 | — |
| 2.1 Sections present and ordered | §1–§21 are all present in order, and §21a/b/c/d are present. §13 subsections are numbered differently from the brief: §13c is sentiment/price divergence, and §13d holds both the previous and upcoming calendars. §13a repeats a "Class" column header. §1 is one unbroken paragraph. | headings | 4 | Split §13d. |
| 2.2 Scorecard as a table | §6 is a table, but it lacks the Trend, Source A / Source B, Final and Validation columns (it has Range, Body % and a combined Sources column). The pivot tables are ordered R3→S3 with three levels each side. | §6, §11 | 3 | Add the missing columns. |
| 2.3 Method steps visible | §4–§5 show observations, classification and consensus. §8 is candle-by-candle with a sequence assessment. §9 gives overlap, persistence, VOLator and KER. §7 charts are text captions only (accepted as a placeholder). Several §8 statements do not hold against the report's own table: "three consecutive sessions below 30" (the table shows 20 and 22, two sessions) and "single mid-30s rebound" (none). "Three of five closed in the lower half" (only 5 May and 7 May did). "Inside-days" on 6 May and 8 May (both lows undercut the prior low). | §7–§9 | 4 | Fix the §8 descriptions. |
| 3.1 Quantitative claims sourced | Unsourced figures: ~14% FTSE energy weight, 12.5x vs 21x forward P/E, ~80% non-GBP revenue, Fed funds 4.25–4.50%, gilt 4.55%, GBP/USD 1.27, CFTC commentary, "VIX-Europe". The NFP consensus is given as 62K, but the calendar slice shows consensus 90K (62K is the ADP previous). The VIX close is stated as 17.19 against the VIX slice's 19.22 (Δ −2.0). | §1, §12, §14 | 2 | Source or remove. |
| 3.2 Citations exist and contain data | Three spot-checked: (1) Trading Economics, "−49 pts / −0.48%" with a close of 10,228. This is internally consistent and implies a 7 May close of about 10,277, but the report's own §6 shows 10,262 (−34 pts, −0.33%), so the cited source contradicts the table it is claimed to corroborate. (2) Reuters via TE, "oil tops $100", against Brent $95.42 close in §14 (possible intraday, unreconciled). (3) BoE MPC summary, 30 Apr, 8–1, 3.75%: consistent throughout. Yahoo 10,233.07 against the official 10,228.34 is internally consistent. Fabrication is not proven: the named sources exist and the quoted figures used are mostly self-consistent. The OHLC corroboration labels are the weak point (see 3.5). Hallucinated-source override not triggered; flag for central review. | §4, §13a | 2 | Re-source (1), reconcile (2). |
| 3.3 Calculations transparent | RSI2 is not reproducible from the report's own closes (10,499 / 10,402 / 10,440 / 10,262 / 10,228). 6 May: stated 55, recomputed 28.1. 7 May: stated 20, recomputed 17.6. 8 May: stated 22, recomputed 0.0. The ATR(14) is "estimate = 145" only on the 3C card, and 3×ATR is "≈360" on the Trade 2 card, which implies ATR 120, not 145. Pivot formulas fail from the report's own inputs. Daily (H 10,470 / L 10,255 / C 10,262): R1 should be 10,403 (stated 10,332), R2 10,544 (10,402), R3 10,618 (10,477), S3 9,973 (10,044); P, S1 and S2 are correct. Weekly (10,510 / 10,184 / 10,228): P is correct, and R1 10,431 (10,381), R2 10,633 (10,533), R3 10,757 (10,659), S1 10,105 (10,155), S2 9,981 (10,081), S3 9,779 (9,955) are all wrong. Monthly (10,934 / 9,851 / 10,499): P is correct, and R1 11,005 (10,839), R2 11,511 (11,178), R3 12,088 (11,664), S1 9,922 (10,089), S2 9,345 (9,678), S3 8,839 (9,339) are all wrong. The §13b tilt sum is −3.5, not −4.0, so the tilt is −0.78, not −0.89. The §21a contributions sum to −0.20, not the stated −0.16. | §6, §11, §13b, §21a | 1 | Rebuild all derivations. |
| 3.4 Numbers reconcile | D-1 close 10,228 is consistent across §1, §3, §4, §6. Breaks: §1 sentiment "Mixed (tilt −0.18)" against §13b "Predominantly Bearish (−0.89)". Weekly move −1.5% (§1, §13c) against §6 net −261 pts (−2.49%), where the closes give −271 (−2.58%). §7 puts Friday's close "between weekly S1 and S2", but §11 has it above S1 (10,155) and below P (10,307). §15 calls 10,500 "weekly R1" while §11 R1 is 10,381. The §11 daily pivots are built from Thu 7 May, not D-1 (Fri 8 May). Trade 2 gives 3×ATR "≈360" and 3C gives ATR 145. The §21c/§21d backtest conflicts: Trade 2 "triggered Thu 7 May" against "already triggered Tue"; Trade 1 7 May "+1.33R" against §21d "+0.50R open"; the §21d hit-rates mix open and closed trades. | cross-section | 1 | Reconcile. |
| 3.5 (added) Stated D-1 data against level file | See section 2: 20 OHLC fields checked, 16 outside tolerance; closes off by +127.0 (1 May), +182.1 (5 May), −20.6 (7 May); RSI2 22 against 0.0 (cash) or 15.7 (full); 25-session range 10,934 / 9,851 against 10,697.5 / 10,162.8 (cash); April month inputs not as in the data. | §6, §11, §21b | 1 | Rebuild from the feed. |
| 4.1 Pillars conclude | §8, §9, §10, §12 and §14 each carry a direction label. §9 contradicts itself: the matrix verdict is "favour trend resumption; avoid fade", but the regime is then TRANSITION. | §8–§14 | 4 | — |
| 4.2 Cross-asset interpreted | §10 gives a mechanism per counter (USD translation, US beta, DAX regional read) and flags divergence. The oil / energy-weight channel sits in §12 and is not tied back into §10. USDX and S&P directions are consistent with the slices (USDX 98.21→97.82; S&P +2.5% on the week). | §10 | 4 | — |
| 4.3 Synthesis reconciles tensions | §16 states "no contradiction flag" although §9 says "favour bounce setups at structural support; avoid fresh shorts" while both live cards are SHORT breakdowns. §21a credits the medium-term regime +0.20 although the consolidated label is TRANSITION; with that term at 0 the score would be −0.40, which exceeds the 0.25 threshold in magnitude. §1's tilt of −0.18 conflicts with −0.89. | §9, §16, §21 | 2 | Reconcile. |
| 4.4 Calibrated language | §17 is one sentence. The confidence label (Medium) is stated in §3 and §18. Some overclaiming ("CORROBORATED across all five sessions"). | §3, §17 | 4 | — |
| 4.5 (added) Card construction (protocol) | Trade 1 SUPPRESSED is correctly rendered (the score arithmetic is off but still below 0.25). Trade 2: entry mixes a stop order with a close-confirmed market fill, the stop is not reproducible, the confluence claim fails the report's own 0.15×ATR test, and the levels trace to wrong pivots. Trade 3C: no entry price (linter DUD UNPRICED), range inputs wrong, targets measured from the boundary rather than from an entry. See the feedback file. | §21b | 1 | See feedback. |
| 5.1 Data dated, staleness flagged | Every price and article carries a date, but several are wrong (see 1.2). All tiers are declared CORROBORATED with "no single-source flag", despite OHLC not matching the feed. The UK Finance article is dated only "May 2026". | §4, §6, §13, §19 | 2 | — |
| 5.2 Assumptions up front | The anchor-override caveat appears in §2 and §20, phrased as "per session instructions". The cards show only "next session open" with no clock time and no anchor caveat. | §2, §20, §21b | 3 | Put the anchor on each card. |
| 5.3 Red flags surfaced | §12 and §15 carry risks. The Trade 2 caveat says UK CPI "falls outside the 5-session horizon" but omits the 12 May labour data, 13 May GDP and 14 May Bailey speech, which §16 itself calls key intra-window inputs. | §12, §15, §21b | 3 | — |
| 5.4 Restrictions honoured | Breached. Module codes appear in the report text: "M1", "M2 §9c", "M3", "M5 §5.2a/§5.2c", "X9 audit checklist". A bracketed variable name appears: "[MAX_SIMULTANEOUS_LONG_SHORT]". Framework and baseline vocabulary leaks: "v2.1 baseline", "per session instructions", "20-session weight-lock". Also, 1 May and 5 May OHLC (closes +127 and +182 points from the feed) are presented as "CORROBORATED, FTSE Russell × Yahoo". | §2, §5, §9, §13b, §20, §21 | 1 | Remove. |

## 2. Category 3 data comparison (report minus level-file / slice, cash basis, points)

Tolerance: close ≤5, open/high/low ≤10.

| Session (data date) | Field | Report | Data (cash) | Δ | OK? |
|---|---|---|---|---|---|
| 1 May (report: "Fri 2 May") | O / H / L / C | 10,488 / 10,510 / 10,452 / 10,499 | 10,350.1 / 10,379.8 / 10,284.8 / 10,372.0 | +137.9 / +130.2 / +167.2 / +127.0 | no ×4 |
| 5 May | O / H / L / C | 10,485 / 10,498 / 10,388 / 10,402 | 10,295.4 / 10,309.8 / 10,162.8 / 10,219.9 | +189.6 / +188.2 / +225.2 / +182.1 | no ×4 |
| 6 May | O / H / L / C | 10,398 / 10,455 / 10,360 / 10,440 | 10,336.0 / 10,491.8 / 10,321.9 / 10,442.3 | +62.0 / −36.8 / +38.1 / −2.3 | C only |
| 7 May | O / H / L / C | 10,455 / 10,470 / 10,255 / 10,262 | 10,451.2 / 10,451.2 / 10,277.5 / 10,282.6 | +3.8 / +18.8 / −22.5 / −20.6 | O only |
| 8 May (D-1) | O / H / L / C | 10,196 / 10,261 / 10,184 / 10,228 (official 10,228.34) | 10,189.8 / 10,271.7 / 10,174.8 / 10,222.4 | +6.2 / −10.7 / +9.2 / +5.6 (+5.9 on official) | O, L ok; H marginal; C marginal |

- The 7 May high matches the full-day bar (10,470.1). The 7 May low and close do not match either basis: full-day L 10,195.7, C 10,202.0.
- A close error above 15 pts on three sessions (1 May, 5 May, 7 May) is a Category 3 failure under brief §4.
- The 1 May close (10,499) equals the figure the report gives as the April month close (10,499).
- **RSI2 (D-1):** report 22. Data: cash 0.0, full 15.7. From the report's own closes: 0.0. Does not reproduce. The 6 May value (55 against 28.1 recomputed) also fails.
- **ATR14:** the report gives 145 (estimate, on the 3C card only). Data: cash 135.4, full 150.2. Consistent in size, but not stated in §9/§21a and inconsistent with the "≈360" figure for 3×ATR.
- **5-day swing:** report H 10,510 (mis-dated to 1 May) / L 10,184. Data: 10,491.8 (6 May) / 10,162.8 (5 May). Δ +18.2 / +21.2.
- **25-session range:** report 10,934 / 9,851 (width 1,083). Data: cash 10,697.5 / 10,162.8 (width 534.7); full 10,727.5 / 10,162.8. The report's high is +236.5 above the cash figure and its low is −311.8 below.

Daily pivots. The report builds them from Thu 7 May rather than D-1 (Fri 8 May).

| Level | Report | Data cash | Δ | Data full |
|---|---|---|---|---|
| R3 | 10,477 | 10,368.0 | +109.0 | 10,385.6 |
| R2 | 10,402 | 10,319.9 | +82.1 | 10,328.6 |
| R1 | 10,332 | 10,271.1 | +60.9 | 10,288.7 |
| P | 10,329 | 10,223.0 | +106.0 | 10,231.7 |
| S1 | 10,189 | 10,174.2 | +14.8 | 10,191.8 |
| S2 | 10,114 | 10,126.1 | −12.1 | 10,134.8 |
| S3 | 10,044 | 10,077.3 | −33.3 | 10,094.9 |

Weekly pivots (2026-W19). The report's inputs take H from a day outside the week.

| Level | Report | Data cash | Δ | Data full |
|---|---|---|---|---|
| R3 | 10,659 | 10,750.9 | −91.9 | 10,768.4 |
| R2 | 10,533 | 10,621.3 | −88.3 | 10,630.1 |
| R1 | 10,381 | 10,421.9 | −40.9 | 10,439.4 |
| P | 10,307 | 10,292.3 | +14.7 | 10,301.1 |
| S1 | 10,155 | 10,092.9 | +62.1 | 10,110.4 |
| S2 | 10,081 | 9,963.3 | +117.7 | 9,972.1 |
| S3 | 9,955 | 9,763.9 | +191.1 | 9,781.4 |

Monthly pivots (April). The data imply April inputs of roughly H 10,727.5 / L 10,170.7 / C 10,363 (full basis), against the report's 10,934 / 9,851 / 10,499.

| Level | Report | Data cash | Δ | Data full |
|---|---|---|---|---|
| R3 | 11,664 | 11,159.9 | +504.1 | 11,228.4 |
| R2 | 11,178 | 10,928.7 | +249.3 | 10,978.0 |
| R1 | 10,839 | 10,650.0 | +189.0 | 10,671.6 |
| P | 10,428 | 10,418.8 | +9.2 | 10,421.2 |
| S1 | 10,089 | 10,140.1 | −51.1 | 10,114.8 |
| S2 | 9,678 | 9,908.9 | −230.9 | 9,864.4 |
| S3 | 9,339 | 9,630.2 | −291.2 | 9,558.0 |

Other counters:
- The USDX Friday close is 97.82 in the slice against 97.95 in the report (acceptable).
- The S&P 500 weekly change is +2.5% against the report's +2.3% (acceptable).
- The VIX close is 19.22 in the slice against 17.19 in the report (Δ −2.0, flagged).
- Calendar checks: Halifax HPI (−0.1% m/m, 0.4% y/y) and NFP 115K match. The NFP consensus is 90K, not 62K. The D-day calendar rows for D are BoE Woods speech (15:40 UK) and Bbk Mauderer speech; neither is in the report's "Mon 11 May" row, which lists the BRC retail data and a Bundesbank report instead.

## 3. Category roll-up

| Category | Level | Multiplier | Points | Justification |
|---|---|---|---|---|
| C1 Prompt adherence (20) | 2 | 0.40 | 8.0 | Row mean of 1.1/1.2/1.3 is 3.0. The restriction breach (5.4) lowers it one level. Source count is short and the date labels are wrong. |
| C2 Structure (20) | 4 | 0.85 | 17.0 | All sections are present and ordered. The §6 table is missing columns and the §13 numbering differs from the brief. |
| C3 Accuracy and evidence (25) | 1 | 0.20 | 5.0 | Three closes are off by 127 to 182 points and one by 21 points. RSI2 does not reproduce. 16 of the 18 pivot levels are off by more than 5 points and 10 by more than 40. Row mean (2, 2, 1, 1, 1) = 1.4, which rounds to 1. |
| C4 Reasoning and judgment (20) | 3 | 0.65 | 13.0 | The pillar reasoning is decent. Row mean (4, 4, 2, 4, 1) = 3.0. The cards drag the score down, and the shorts conflict with the §9 "avoid fresh shorts" protocol. |
| C5 Currency and transparency (15) | 2 | 0.40 | 6.0 | The caveats are present but data are declared "CORROBORATED" when they are not. Row mean (2, 3, 3, 1) = 2.25, which rounds to 2. |

## 4. Total, band, override

- Total = 8 + 17 + 5 + 13 + 6 = **49** → band **Low** (40–59).
- Override check:
  - Restriction breach: yes (module codes M1/M2/M3/M5/X9, bracketed variable `[MAX_SIMULTANEOUS_LONG_SHORT]`, framework/baseline vocabulary, and unsupported prices presented as sourced). C1 was reduced by one level and the Moderate cap is non-binding.
  - Hallucinated source: not triggered. Flagged (3.2) for central review: the TE quote conflicts with the report's own 7 May close, and the "FTSE Russell × Yahoo" corroboration labels sit on rows that do not match the feed.
- `override=restriction_breach`.

## 5. Card Integrity (linter rows, copied verbatim from `qa/ftse_qa1/lint_static/2026-05-11.csv`)

| card_id | report_date | strategy | flags | dud |
|---|---|---|---|---|
| 2026-05-11_Trade_1 | 2026-05-11 | Trade 1 - Daily Directional | SUPPRESSED | False |
| 2026-05-11_Trade_2 | 2026-05-11 | Trade 2 - Pivot, TRANSITION regime, breakout-side only (per §5.2c) | CLEAN | False |
| 2026-05-11_Trade_3C | 2026-05-11 | Trade 3C - Momentum-Breakout (TRANSITION fork) | UNPRICED | True |

| Card | #DUD | #WARN | Card score |
|---|---|---|---|
| Trade 1 | — | — | suppressed (excluded) |
| Trade 2 | 0 | 0 | 100 |
| Trade 3C | 1 | 0 | 60 |

Report-level Card Integrity = mean(100, 60) = **80.0** over 2 non-suppressed cards. n_cards=3, n_duds=1, n_warns=0.
