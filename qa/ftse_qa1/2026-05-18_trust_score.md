# Trust Score v3.7 — FTSE 100 Daily Report, 18 May 2026 (run ftse_qa1)

Report: `FTSE100_Daily_Report_18-May-2026.md` · D = 2026-05-18 · D-1 data session = Fri 2026-05-15
Level file check: `last_bar_date` = 2026-05-15 < D (leak-free, OK). Slice last bar 2026-05-15 22:45 broker.
Basis claimed by the report: LSE cash close (cash). Compared against `_cash` fields (and `_full` where noted).

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
Override note: the hallucinated-source override (Low cap, C3 = 0) is the binding one. A restriction breach
(brief §2 row 5.4) ALSO applies independently and is why C1 is reduced from 3 to 2. The `override=` field can hold only
one value; `hallucinated_source` is entered because it is the stricter cap.

## 1. Section 7 checklist (every row)

| Row | Reviewer notes | Evidence (location) | Score |
|---|---|---|---|
| 1.1 Variables respected | FTSE 100 cash primary, Euro Stoxx 50 reference only (no cards); counters USDX / S&P 500 / DAX 40 (+VIX, Brent); as-of Fri 15 May close Europe/London; 5-session lookback; GBP/points. Deviations: (a) daily-open anchor for Trade 1 is 08:00 UK "user override", not the 07:00 UK anchor required by the Variables (stated in §20 and the §21d note, so disclosed but still a deviation); (b) the >=6-source test is met only by arithmetic sleight: §5 says "Five independent confirmations clear the [MINIMUM_SOURCE_COUNT] = 6 threshold once EURO STOXX 50 is included as the corroborating secondary" — a second index is not a corroborating source for FTSE; the five FTSE close sources are quoted at an identical 10,195.37 to 0.05 pts, which the slice does not support (see 3.4); (c) bracketed variable names leaked (see 5.4). | §2, §5, §20, §21b/d note | 3 |
| 1.2 Coverage and currency consistent | Data dates are D-1 or earlier; session D forward. Drift points: §13d dates the US CPI release "Tue 13 May" and US PPI "Wed 14 May" — NEWS slice schedules CPI on 12 May 15:30 broker and PPI on 13 May 15:30 broker; the report's own §6 labels 13 May a Wednesday, so weekday/date pairs in §13d are internally inconsistent. §1 "down 1.7% on the week" vs §7 "net 1.35% drop across the week" (slice cash Mon open 10,254.8 to Fri close 10,167.0 = −0.86%). §1 "five-day high-to-low excursion of ~530 points" vs §6 own range 10,378.40−10,163.56 = 214.8. §12 UK CPI "09:00 BST" vs §13e/§20 "07:00 UK". STOXX 50 labelled a "Zurich" close. | §1, §7, §12, §13d, §13e | 3 |
| 1.3 Audience and tone | Institutional strategist register, trading-and-risk use, no retail tone. Minor slip: "per typical sequence" used as a source for a Eurozone HICP number (§12). | §1, §18 | 4 |
| 2.1 Sections present and ordered | §1–§21 all present in order; §21a/b/c/d present; §17 is one sentence. §13 is lettered §13a, §13b, §13c = Divergence Flag, §13d = previous calendar, §13e = upcoming calendar, whereas the structure is §13c previous / §13d upcoming (extra sub-section shifts the lettering). §7 has no embedded chart; a caption/placeholder says five charts "configured" but "not embedded in this text-only deliverable" (accepted as placeholder per brief, noted). §14 is a table with no direction label. | headings | 4 |
| 2.2 Scorecard as a table | §6 is a table with Date/O/H/L/C/RSI2/Trend/Src A/Src B/Final/Validation (FTSE and STOXX). §11 daily, weekly and monthly pivot tables ordered R3→P→S3, three levels each side. Table form is correct (content errors are scored in C3). | §6, §11 | 5 |
| 2.3 Method steps visible | §4 observations → §5 consensus build (visible, though §5 logic is muddled); §8 candle-by-candle plus sequence assessment; §9 regime with overlap ratio, persistence, VOLator, KER; charts: placeholder only. | §4–§9 | 4 |
| 3.1 Quantitative claims sourced | Prices and counters in §4/§10 carry sources; §12 sector moves (Fresnillo −10.09%, Antofagasta −10.71%, etc.) and §14 rates/credit numbers (10y gilt 4.55%, iTraxx +15bp, HY +12bp) carry no source and do not point to §4/§6/§13. §1 Brent $109.26 / WTI $105.42 cited only in §10/§12 without a source row. VIX 18.43 (+6.78%) is single-source (§19) yet used as a bearish contributor in §10/§18. Weekly S1 "10,055" quoted in §1/§3/§16 has no source and contradicts §11 (weekly S1 = 10,113.15). | §1, §10, §12, §14 | 3 |
| 3.2 Citations exist and contain the data | Three sources checked. (1) Bloomberg, §13a row 2: URL path `/news/2026-03-18-boe-assumptions` but article dated 14 May 2026 — the URL embeds a date two months before the stated publication date, impossible/self-contradictory → counted as fabricated per brief. (2) City AM, §13a row 5: URL slug "ftse-100-hits-10000-mark-after-rolls-royce" vs headline "closes whisker away from 10,000" and the item is dated "Jan 2026 / hist context" (outside the 5-day lookback, used with a Bullish weight) — weak/inconsistent. (3) Investing.com, §4 row 3: quotes prior-day range 10,266.14–10,360.51, which matches neither the report's own Thu 14 May range (10,232.50–10,378.40, §6) nor the slice. One clear failure triggers the hallucinated-source override. | §4, §13a | 0 |
| 3.3 Calculations transparent | RSI2 values do not reproduce from the report's own closes (see table below): Thu 84.3 vs 100.0, Fri 15.2 vs 40.1. Pivot arithmetic fails on R3 in all three tables and on weekly S3 (own inputs). ATR(14) appears only inside a card cell ("≈145") and not in §6/§9. KER (|0.115| smoothed) stated. §21a: Σ = −0.1625−0.08−0.02−0.045−0.0825−0.0825 = −0.4725, reported −0.48. §13b tilt arithmetic miscounts (7 Bearish not 6; 4 media/trade bearish not 3; max weight sum 10.0 not 12.5). | §6, §9, §11, §13b, §21a | 1 |
| 3.4 Numbers reconcile | D-1 close 10,195.37 is identical across §1/§3/§4/§6/§21b (internally consistent) but is 28.4 pts above slice cash close 10,167.0 and 8.4 above full-day close 10,187.0. Pivots on cards match §11 (P 10,244.89, R1 10,326.22, S1 10,114.05). Breaks: weekly S1 10,055 (§1, §3, §16) vs 10,113.15 (§11); Friday close-location 22% (§8, §18) vs (10,195.37−10,163.56)/212.17 = 15%; §9 25-day range 783 / midpoint 10,543 vs slice 520.6 / 10,406.2 (cash 25d high 10,666.5 on 2026-04-17, not 10,934.94); "break of prior 30-day low at 10,164" is not borne out by slice (12 May cash low 10,145.9 is below Friday's 10,154.9); ATR(14) 145 vs 140.23 cash / 151.20 full; monthly pivot inputs far from the level file. | cross-section | 1 |
| 4.1 Pillars conclude | §8 "Bearish continuation", §9 "Bias: Bearish", §10 per-counter reads plus −0.55 score, §12 each sub-block has a Status. §14 Macro is a bare table with no direction label. §12 as a whole has no section-level label. | §8–§14 | 3 |
| 4.2 Cross-asset interpreted | §10 gives mechanisms specific to the FTSE (dollar-earner translation via BP/SHEL/GSK/Unilever, energy weight ~11–12%, rate channel). Weaknesses: USDX row is labelled "Bearish" though its own mechanism text says "Mixed for FTSE"; −0.55 score has no derivation; VIX counted among "four bearish" while §19 declares VIX informational / not in the primary counter set; VIX 18.43 (+6.78%) vs slice 19.06 (+0.42%) and "first sustained move above 18 in three weeks" is contradicted by the slice (VIX closes 18.98–19.52 all week). | §10, §19 | 3 |
| 4.3 Synthesis reconciles tensions | §8, §9, §16 each say "No conflict to flag" although tensions exist and are unaddressed: KER "ranging-bias-down" (|0.115| < 0.13 trend threshold) vs a "trend-following short bias" in §9 and a "TREND-DOWN" Trade 2; §9 says expanding VOLator argues stops ≥1.5 ATR while all three stops are 0.45–0.92 ATR; §17 says price "grinds lower through" the 10,244 pivot while Trades 2 and 3A only fill if price rallies to 10,242/10,245; §21a regime "TRANSITION-BEAR" vs §21b Trade 2 "TREND-DOWN". | §9, §16, §17, §21 | 2 |
| 4.4 Calibrated language | §17 is exactly one sentence (long, one trailing "risk skewed" clause; acceptable). Confidence stated Medium in §1/§3/§18 ("M-confidence" in §1). Language "confirmed bearish" sits uneasily with Medium confidence and a Transitional regime. | §1, §3, §17, §18 | 4 |
| 4.5 Card construction (protocol row) | See Card Integrity and feedback. Linter is CLEAN on all three cards but the cards carry semantic defects the static linter cannot see: Trade 1 stop has no 0.25×ATR buffer, skips the nearer daily P, Unit-3 stop moved to entry+0.2R (adverse for a short), entry price absent from the Entry cell, TP1 narrative incoherent, 5-day time-stop on a daily trade; Trade 2 labelled TREND-DOWN under a Transitional/KER-ranging regime, stop and TPs not per the TREND rule, TP3 cell contradictory (runner exit above a short entry); Trade 3A entry at 38.2% not 57.5%, swing = a single 212-pt day (< 2×ATR), stop text contradicts price, override stop equals original stop. §21a score arithmetic off by 0.01. | §21a, §21b | 1 |
| 5.1 Data dated, staleness flagged | Every price and article is dated; City AM flagged historical; reconstruction of Mon–Thu OHLC disclosed in the §6 footnote and §19. But §6 still labels those rows "Corroborated" with Src A/Src B filled, and §19 asserts "within ±0.10 point" which the slice contradicts by tens of points. | §6, §13a, §19 | 3 |
| 5.2 Assumptions up front | Anchor override disclosed on the card, §20 and §21 footnote. Not up front: the reconstruction/synthesis of Mon–Thu OHLC (buried in §19, absent from §1); single-source monthly pivots are declared "advisory" in §19 yet Trade 1 TP2 and Trade 3A TP3/TP confluence cite monthly S1 as a confluence ("strong three-way") — not propagated as indicative onto the cards. | §1, §19, §20, §21b | 2 |
| 5.3 Red flags surfaced | §12/§15 surface CPI 20 May, Hormuz, BoE hawk dissent, banking weight. Event collisions not carried into card caveats: Trade 1 runner time-stop is Fri 22 May (spans UK CPI Wed 20 May, FOMC minutes, PMI); no card mentions the D-day MPC speaker (Mann, 11:30 broker = 09:30 UK) or ECB Elderson (10:30 broker = 08:30 UK) in the slice calendar; §13e lists "BoE Bailey speech 15:00 UK" which is not in the slice's scheduled rows for D. | §12, §13e, §15, §21b | 3 |
| 5.4 Restrictions honoured | BREACHES: (a) bracketed variable names in the report body — [RESTRICTIONS] §4, [MINIMUM_SOURCE_COUNT] §5/§13b/§20, [LOOKBACK_WINDOW] §13b, [CONVICTION_THRESHOLD] §21a, [ATR_STOP_CAP] §21d note; (b) module code "M5 §21" in §19; (c) reconstructed/interpolated Mon–Thu O/H/L presented as "Corroborated" with two named sources in §6 (note Opens equal the prior close on Mon–Thu: 10,335.20 start, then 10,266.14, 10,210.95, 10,254.10 — a synthesis signature; real deltas to the slice are 28–104 pts). Honoured: CFD quote excluded (Trading Economics 10,165); FTSE futures not used; instrument common names. | §4–§6, §13b, §19, §21 | 1 |

## 2. Category-3 evidence — report vs level file (basis claimed: cash)

### 2a. D-1 (Fri 15 May) OHLC / RSI2 / ATR
| Field | Report | Level `_cash` | Δ (rpt−cash) | Level `_full` | Δ (rpt−full) | Tolerance verdict |
|---|---|---|---|---|---|---|
| Open | 10,318.66 | 10,299.0 | +19.7 | 10,352.9 | −34.2 | cash FAIL (>10) |
| High | 10,375.73 | 10,309.4 | +66.3 | 10,362.3 | +13.4 | FAIL both |
| Low | 10,163.56 | 10,154.9 | +8.7 | 10,152.3 | +11.3 | cash OK |
| Close | 10,195.37 | 10,167.0 | +28.4 | 10,187.0 | +8.4 | cash FAIL (>15 = Cat-3 failure); full also >5 |
| RSI2 | 15.2 | 24.78 | −9.6 | 0.0 (n/a, full-day) | | recompute from own closes = 40.1 (Δ 24.9) FAIL |
| ATR14 | ≈145 (§21b only) | 140.23 | +4.8 | 151.20 | −6.2 | consistent within 5%, but not stated in §6/§9 |

### 2b. Mon–Thu OHLC (report vs slice cash session; opens = prior close in the report)
| Date | Open (Δ) | High (Δ) | Low (Δ) | Close (Δ) |
|---|---|---|---|---|
| Mon 11 May | 10,335.20 vs 10,254.8 (+80.4) | 10,360.40 vs 10,284.2 (+76.2) | 10,250.10 vs 10,221.9 (+28.2) | 10,266.14 vs 10,264.1 (+2.0) OK |
| Tue 12 May | 10,266.14 vs 10,190.5 (+75.6) | 10,330.80 vs 10,250.3 (+80.5) | 10,180.30 vs 10,145.9 (+34.4) | 10,210.95 vs 10,250.1 (−39.2) |
| Wed 13 May | 10,210.95 vs 10,314.9 (−103.9) | 10,290.50 vs 10,357.0 (−66.5) | 10,165.20 vs 10,234.8 (−69.6) | 10,254.10 vs 10,293.6 (−39.5) |
| Thu 14 May | 10,254.10 vs 10,319.3 (−65.2) | 10,378.40 vs 10,371.1 (+7.3) OK | 10,232.50 vs 10,301.1 (−68.6) | 10,372.93 vs 10,355.8 (+17.1) FAIL (>15) |

Candle direction in the slice (close vs open) is Mon up, Tue up, Wed down, Thu up, Fri down; the report shows Mon down, Tue down, Wed up, Thu up, Fri down. Mon, Tue and Wed body directions are reversed.

### 2c. RSI2 arithmetic from the report's own closes (`--closes 10266.14 10210.95 10254.10 10372.93 10195.37`)
| Date | Report RSI2 | Recomputed from own closes | Δ |
|---|---|---|---|
| Wed 13 May | 45.6 | 43.9 | +1.7 (acceptable) |
| Thu 14 May | 84.3 | 100.0 (two consecutive gains, zero loss) | −15.7 FAIL |
| Fri 15 May | 15.2 | 40.1 | −24.9 FAIL |
Mon/Tue cannot be tested (need closes before the window). Slice cash RSI2 for reference: Mon 40.92, Tue 74.87, Wed 75.65, Thu 100.0, Fri 24.78.

### 2d. Pivots — report vs level file, plus arithmetic from the report's own H/L/C
| Level | Daily rpt | `d_cash` | Δ | `d_full` | Δ | Weekly rpt | `w_cash` | Δ | `w_full` | Δ |
|---|---|---|---|---|---|---|---|---|---|---|
| R3 | 10,599.45 | 10,420.47 | +179.0 | 10,525.43 | +74.0 | 10,675.05 | 10,535.3 | +139.8 | 10,592.3 | +82.8 |
| R2 | 10,457.06 | 10,364.93 | +92.1 | 10,443.87 | +13.2 | 10,460.62 | 10,453.2 | +7.4 | 10,494.8 | −34.2 |
| R1 | 10,326.22 | 10,265.97 | +60.3 | 10,315.43 | +10.8 | 10,327.99 | 10,310.1 | +17.9 | 10,340.9 | −12.9 |
| P | 10,244.89 | 10,210.43 | +34.5 | 10,233.87 | +11.0 | 10,245.78 | 10,228.0 | +17.8 | 10,243.4 | +2.4 |
| S1 | 10,114.05 | 10,111.47 | +2.6 | 10,105.43 | +8.6 | 10,113.15 | 10,084.9 | +28.3 | 10,089.5 | +23.7 |
| S2 | 10,032.72 | 10,055.93 | −23.2 | 10,023.87 | +8.9 | 10,030.94 | 10,002.8 | +28.1 | 9,992.0 | +38.9 |
| S3 | 9,902.16 | 9,956.97 | −54.8 | 9,895.43 | +6.7 | 9,816.51 | 9,859.7 | −43.2 | 9,838.1 | −21.6 |

Arithmetic from the report's own inputs (P=(H+L+C)/3, R3=H+2(P−L), S3=L−2(H−P)):
- Daily (H 10,375.73 / L 10,163.56 / C 10,195.37): P, R1, S1, R2, S2 reproduce; R3 should be 10,538.38 (report 10,599.45, off 61.1); S3 should be 9,901.87 (report 9,902.16, ok).
- Weekly (H 10,378.40 / L 10,163.56 / C 10,195.37): P, R1, S1, R2, S2 reproduce; R3 should be 10,542.83 (report 10,675.05, off 132.2); S3 should be 9,898.31 (report 9,816.51, off 81.8).
- Monthly (H 10,934.94 / L 9,950.00 / C 10,580): P, R1, S1, R2, S2, S3 reproduce; R3 should be 12,011.56 (report 11,964.94, off 46.6).

Monthly, report vs `m_cash`: P 10,488.31 vs 10,418.8 (+69.5); R1 11,026.62 vs 10,650.0 (+376.6); S1 10,041.68 vs 10,140.1 (−98.4); R2 11,473.25 vs 10,928.7 (+544.6); S2 9,503.37 vs 9,908.9 (−405.5); R3 11,964.94 vs 11,159.9 (+805.0); S3 9,056.74 vs 9,630.2 (−573.5). Inverting the level file's monthly P/R1/S1 (cash) gives implied April H ≈ 10,697.5, L ≈ 10,187.6, C ≈ 10,371.3 versus the report's H 10,934.94, L 9,950.00, C ≈ 10,580 (+237 / −238 / +209). The report labels these inputs single-source-indicative, so the staleness is flagged, but the size of the error is material and the monthly levels are then reused on cards.

### 2e. Counters and calendar
- USDX 99.21 (+0.49%) vs slice 99.303 (+0.43%): consistent.
- S&P 500 7,408.50 (−1.24%) vs slice US500 7,400.8 (−1.38%): consistent (cash vs CFD).
- VIX 18.43 (+6.78%) vs slice 19.06 (+0.42%): level Δ 0.63, percentage change off by 6.4 pts; "first sustained move above 18 in three weeks" contradicted (week range 18.98–19.52 closes).
- US CPI actuals (0.6% m/m, 3.8% y/y) and PPI m/m 1.4% match the slice; dates are wrong (12 May and 13 May) and consensus/prior differ (slice CPI m/m cons 0.7 not 0.4; PPI m/m cons 0.4, prev 0.5, not 0.3/1.0).
- Omitted from §13d: UK GDP q/q 0.6 (cons 0.0 in feed, prev 0.1), m/m 0.3, y/y 1.1 on 14 May 09:00 broker (HIGH); US Retail Sales m/m 0.5 vs 1.2 consensus (14 May, HIGH).

## 3. Category roll-up

| Cat | Max | Row mean | Level | Multiplier | Points | Justification |
|---|---|---|---|---|---|---|
| C1 Prompt adherence | 20 | (3+3+4)/3 = 3.33 → 3, minus 1 for restriction breach | 2 | 0.40 | 8.0 | Anchor deviates from 07:00 UK, source-count claim relies on a non-corroborating index, bracketed variable names and a module code leaked. |
| C2 Structure | 20 | (4+5+4)/3 = 4.33 | 4 | 0.85 | 17.0 | All 21 sections present and ordered; tables correct; minor sub-lettering drift, charts placeholder only. |
| C3 Accuracy and evidence | 25 | (3+0+1+1)/4 = 1.25 → 1, then override | 0 | 0.00 | 0.0 | Hallucinated-source override (Bloomberg URL dated 2026-03-18 for a 14 May article) sets C3 = 0. Independently, D-1 close off by 28.4, Mon–Thu OHLC reconstructed, RSI2 and R3/S3 do not reproduce. |
| C4 Reasoning and judgment | 20 | (3+3+2+4+1)/5 = 2.6 → 3 | 3 | 0.65 | 13.0 | Good FTSE-specific mechanisms; tensions asserted away; card construction weak. |
| C5 Currency and transparency | 15 | (3+2+3+1)/4 = 2.25 → 2 | 2 | 0.40 | 6.0 | Dated data and disclosed anchor override, but reconstruction buried, monthly levels leaked onto cards, restrictions breached. |

## 4. Total, band, override check
- Total = 8.0 + 17.0 + 0.0 + 13.0 + 6.0 = **44** → **Low Trust (40–59)**.
- Hallucinated-source override: TRIGGERED (row 3.2). Cap Low 40–59 (total 44 already inside the cap); C3 = 0.
- Restriction-breach override: ALSO TRIGGERED (row 5.4). Cap Moderate 60–74 (superseded by the Low cap); C1 lowered one level (3 → 2). Both are reflected above.

## 5. Card Integrity (static linter rows, copied verbatim from `lint_static/2026-05-18.csv`)

| card_id | report_date | strategy | flags | dud |
|---|---|---|---|---|
| 2026-05-18_Trade_1 | 2026-05-18 | Trade 1 - Daily Directional | CLEAN | False |
| 2026-05-18_Trade_2 | 2026-05-18 | Trade 2 - Pivot (regime-aware) - TREND-DOWN configuration | CLEAN | False |
| 2026-05-18_Trade_3A | 2026-05-18 | Trade 3A - Momentum-Pullback | CLEAN | False |

Per card: 100 − 40×0 − 10×0 = 100, 100, 100. Report-level Card Integrity = mean(100, 100, 100) = **100.0**.
n_cards = 3 (none suppressed) · n_duds = 0 · n_warns = 0.
Caution: a clean linter does not mean the cards are rule-compliant; the semantic defects are in `2026-05-18_feedback.md` and are scored in C4 row 4.5 (the Card Integrity score itself is separate and not folded into the 100).

## 6. Feedback
See `qa/ftse_qa1/2026-05-18_feedback.md`.
