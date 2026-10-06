# Trust Score v3.7 — FTSE 100 daily report, D = 2026-07-28

Report: `reports/md/FTSE_EuroStoxx_Report_28Jul2026.md` · Reviewer run: ftse_qa1 · Data basis: UK100 CFD slice to 2026-07-27 (level file `last_bar_date` = 2026-07-27 < D: leak check passed). Cash window 10:00–18:30 broker (08:00–16:30 London); the report claims a cash-index basis, so `_cash` fields are the reference. `qa_slice_stats.py` run with `--cash-open 10:00 --cash-close 18:30`.

## Machine-readable result
```
c1=2
c2=3
c3=2
c4=3
c5=3
total=54
band=Low
override=restriction_breach
card_integrity=100.0
n_cards=3
n_duds=0
n_warns=0
```
(`override=restriction_breach` is a cap at Moderate 60–74 and C1 down one level. The raw total of 54 is already below the cap, so the cap does not change it; the C1 reduction is applied and is reflected in the total.)

## 1. Section 7 checklist

| Row | Reviewer notes | Evidence (location) | Score |
|---|---|---|---|
| 1.1 Variables respected | FTSE 100 cash index primary, Euro Stoxx 50 reference only, counters USDX / S&P 500 / DAX 40, as-of 27 Jul London close, 5-session lookback, GBP/points, 07:00 UK anchor: all present. Source mix fails: the brief requires ≥6 sources spanning index provider / exchange / sell-side. §4 lists Trading Economics, IG/Proactive, Analytics Insight, Yahoo, Investing.com, BBN Times only (aggregators, media, a retail-CFD broker); no index provider, exchange or sell-side row. IG and BBN/Yahoo are labelled "Exchange-derived" / "Exchange session" without support. | §2, §4, §20 | 3 |
| 1.2 Coverage & currency consistent | Data dates are all ≤ 27 Jul. Drift: §13c "Wed 23 Jul ECB rate decision" (23 Jul 2026 is a Thursday; the next row says "Thu 23 Jul"); §21c rows are labelled Mon 20 … Fri 24 as t−5…t−1, but t−1 for D=28 Jul is Mon 27 Jul — the entry/exit prices on those rows are the 21, 22, 23, 24, 27 Jul open→close figures from §6, i.e. every row is shifted one day; §13d "next 5 sessions" begins "Mon 27". | §13c, §13d, §21c | 3 |
| 1.3 Audience & tone | Strategist tone, no retail language. Draft residue left in a client-facing table: "LONG (score<thr → wk suppressed?)" in §21c. | §1, §18, §21c | 4 |
| 2.1 Sections present & ordered | §1–§21 all present in order; §13a–d and §21a–d present. §7 charts are rendered as captions/descriptions (accepted per brief; noted). | headings | 4 |
| 2.2 Scorecard / pivots as tables | §6 is a table but has a single merged "Sources" column, no Source A / Source B / Final columns. §11 daily and weekly tables show only S2..R2 (two levels each side, ordered S→R), not R3→P→S3 with three levels each side; monthly pivot table absent. | §6, §11 | 2 |
| 2.3 Method steps visible | §4→§5 observation → consensus; §8 candle-by-candle and sequence; §9 regime, KER, VOLator; RSI2 shown. ATR(14) not stated numerically in §9. | §4–§9 | 4 |
| 3.1 Quantitative claims sourced | §12 / §14 figures (Brent −6% below $90, WTI ~85, gilt 10y ~5.05%, GBP/USD ~1.335, EUR/USD ~1.14, DAX +1.32%, Vodafone +5%) carry no source and do not point to §4/§6/§13. §13a has no date column. §19 admits counters are single-source snapshots. | §10, §12, §13a, §14 | 2 |
| 3.2 Citations exist & contain data | Three spot-checks: IG/Proactive "10,781 (+45)" (10,781 − 10,736.23 = +44.77, consistent); Analytics Insight "10,779.27 (+43.04)" (10,779.27 − 43.04 = 10,736.23, consistent with the 24 Jul close); BBN/Yahoo 24 Jul OHLC (consistent with the 24 Jul row). No self-contradictory or impossible source found: no hallucination override. Weakness: the corroboration claim for 21, 22 and 23 Jul closes names sources (Alliance News, BBN, TE) that are not in §4, so it cannot be traced. | §4, §6 | 3 |
| 3.3 Calculations transparent | RSI2 reproduces exactly from the report's own closes (62.8 / 55.5 / 100.0, checked with `--closes`). Pivots reproduce from the stated H/L/C (weekly P computes to 10,671.3, printed 10,672). §21a sum reproduces (0.25+0.20+0.083+0.083+0.045+0 = 0.661) and the §20 signals tie to the locked weights (0.15 × 0.55 = 0.083 KER and sentiment; 0.15 × 0.30 = 0.045). KER 0.56 is consistent with my recomputation (0.54, 13 sessions, cash closes). Gaps: ATR(14) is never stated (only implied by "3.5×ATR ≈ 411" on Trade 1 = 117.4, consistent with 117.5); sentiment tilt +0.55 not reproducible from the stated weights (I get +0.595 with Mixed=0); 21 and 22 Jul Trend shown as Bullish while RSI2 is "n/a" (rule cannot be applied; slice RSI2 for 21 Jul is 48.9 → Neutral); no cross-asset signal derivation (+0.30). | §6, §9, §11, §13b, §20, §21a | 3 |
| 3.4 Numbers reconcile (internal + vs slice) | Internal: D-1 close 10,781 identical in §1/§3/§4/§6/§21b; §11 pivots equal the card levels. Breaks: §7 "three bullish bodies (21, 22, 27 Jul)" vs §6 four bullish rows (21, 22, 24, 27); Trade 1 "TP2 +58 points" vs 10,838 − 10,781 = 57; Trade 2 confluence calls 10,920 "Runner TP2" (it is TP3); §13c UK CPI "Held 2.6%" but calendar previous = 2.8 (fell 2.8→2.6, consensus 2.5); §13c retail sales "vs −0.3% exp" but calendar consensus = −1.0, previous −1.3; §21c implied R per row differs (61, 66, 78, 49, 30 pts) against the card R of 29. Vs slice (cash): see §1A below — only 1 of 5 closes within ±5; 23 Jul close +21.1 (> 15 pts, a Category 3 failure per brief); D-1 O/H/L off by −24.4/−14.3/+22.9; D-1 range 32 pts vs 69.2 actual; daily R1/R2/S1/S2 off by −26.2/−39.3/+11.0/+35.1; weekly low 10,515 vs 10,470.1; monthly pivots missing. | §6, §11, §21 vs level file | 1 |
| 4.1 Pillars conclude | §8 (continuation), §9 (TREND_UP), §10 (MIXED, direction-aligned), §12 per-theme labels, §14 mostly descriptive with a closing "mildly supportive" — §12 and §14 lack one overall direction label. | §8–§14 | 4 |
| 4.2 Cross-asset interpreted | USDX row gives a translation mechanism; DAX ("confirms") and S&P ("no fresh impulse") are descriptive; no oil/Brent row although oil is the headline driver and the FTSE's energy weight is the mechanism (appears in §12 only); VIX unused. | §10 | 3 |
| 4.3 Synthesis reconciles tensions | RSI2=100 overbought vs trend, KER vs flat VOLator, §17 vs §21a all addressed explicitly. Unreconciled: the weekly tier is called "corroborated" while its low (10,515) is an asterisked indicative value. | §8, §9, §15–§18, §21a | 4 |
| 4.4 Calibrated language | §17 is a single sentence; confidence High stated in §3. Mild hedge stack ("only a shallow … likely … barring … or …"). | §3, §17 | 4 |
| 4.5 Card construction (protocol: scored in Cat. 4) | Fixed M5 rules not followed: Trade 2 is a buy-stop "breakout" in TREND_UP (M5 prescribes entry P+0.10×(R1−P), stop P−0.8×(P−S1), TPs R1/R1.5/R2); Trade 3A entry 10,767 is called "38.2%/S1" not the 57.5% retrace, swing endpoints not logged, TP labels conflate fib levels with +1R/+2R, TP3 copies Trade 1's 10,867; Trade 1 stop is bare daily S2 with no 0.25×ATR buffer and the stated anchor "below 27 Jul session floor" is false (stop 10,752 vs cash low 10,747.1); all three cards have R = 29 / 35 / 29 pts = 0.25 / 0.30 / 0.25 ×ATR14 (cash 117.5; floor 35.3). Direction score / Trade 1 trigger itself is correct. See feedback. | §21b | 1 |
| 5.1 Data dated; staleness flagged | §4 and §6 dated; single-source H/L flagged with asterisks. §13a articles undated. Opens for 22 and 23 Jul equal the prior close to the cent (10,585.91; 10,716.97), 23 Jul H = O = 10,716.97, and several H/L are rounded round numbers (10,600*, 10,515*, 10,585*, 10,802*, 10,770*): opens carry no indicative flag. | §4, §6, §13a | 3 |
| 5.2 Assumptions up front | Anchor override (07:00 UK, entry proxied by D-1 close) stated in §2 and §20 but not on any card; single-source pivot flag appears on Trade 2 only, although Trade 1's stop (daily S2) and Trade 3A's entry (daily S1) are also built on the indicative daily tier. §20 states indicative values were "excluded from stop/entry pricing", contradicting the cards. | §2, §20, §21b | 3 |
| 5.3 Red flags surfaced | Oil re-spike and BoE 30 Jul surfaced in §12/§15/§18; BoE carried to Trade 1 caveats only (not Trade 2 / 3A). §13d omits the scheduled high-impact US CB Consumer Confidence on D (17:00 broker = 15:00 UK; consensus 89.5, previous 91.2) and the UK labour-market prints of 21 Jul are absent from §13c. | §12, §13c/d, §15, §21b | 3 |
| 5.4 Restrictions honoured | Breach: §20 contains a module code ("M5 trace — direction score …"); §9 cites "Step-4 … synthesis" (internal method numbering). §5 treats a "wider CFD print of ~10,802" as the 27 Jul high, and §6 uses that figure (10,802*) in the OHLC basis (retail-CFD quote in the OHLC basis); IG is a retail CFD broker. Carried-forward opens presented in a table whose Validation column reads CORROB. | §5, §6, §9, §20 | 2 |

## 1A. Category 3 comparison against the level file (cash basis; report stated − slice)

| Date | Open | High | Low | Close | RSI2 (report / slice) |
|---|---|---|---|---|---|
| 21 Jul | 10,524.76 vs 10,479.3 (+45.5) | 10,600 vs 10,574.2 (+25.8) | 10,515 vs 10,470.1 (+44.9) | 10,585.91 vs 10,571.7 (+14.2) | n/a / 48.9 |
| 22 Jul | 10,585.91 vs 10,587.0 (−1.1) | 10,763.44 vs 10,758.9 (+4.5) | 10,585 vs 10,557.2 (+27.8) | 10,716.97 vs 10,714.6 (+2.4) | n/a / 100.0 |
| 23 Jul | 10,716.97 vs 10,704.0 (+13.0) | 10,716.97 vs 10,709.8 (+7.2) | 10,599 vs 10,597.3 (+1.7) | 10,639.17 vs 10,618.1 (**+21.1**) | 62.8 / 59.7 |
| 24 Jul | 10,638.86 vs 10,582.2 (+56.7) | 10,738.83 vs 10,728.2 (+10.6) | 10,599.10 vs 10,580.9 (+18.2) | 10,736.23 vs 10,728.0 (+8.2) | 55.5 / 53.3 |
| 27 Jul (D−1) | 10,779.27 vs 10,803.7 (−24.4) | 10,802 vs 10,816.3 (−14.3) | 10,770 vs 10,747.1 (+22.9) | 10,781 vs 10,795.0 (−14.0) | 100.0 / 100.0 |

Full-day basis for D−1 (O 10,734.9 · H 10,826.5 · L 10,710.6 · C 10,787.0) is no closer on O/H/L (−44.4 / −24.5 / +59.4); close −6.0. Tolerances (brief §4): close ±5, O/H/L ±10. Pass: 22 Jul O/H/C, 23 Jul L/H, 21 Jul none. RSI2 arithmetic reproduces from the report's own closes (not an arithmetic failure).

Pivots, report vs level file (cash):

| Level | Report | Level file | Δ |
|---|---|---|---|
| Daily P | 10,784 | 10,786.13 | −2.1 |
| Daily R1 / S1 | 10,799 / 10,767 | 10,825.17 / 10,755.97 | −26.2 / +11.0 |
| Daily R2 / S2 | 10,816 / 10,752 | 10,855.33 / 10,716.93 | −39.3 / +35.1 |
| Daily R3 / S3 | absent | 10,894.37 / 10,686.77 | missing |
| Weekly P (week of 20–24 Jul; level file H 10,758.9 / L 10,470.1 / C 10,728.0) | 10,672 (H 10,763 / L 10,515 / C 10,736) | 10,652.33 | +19.7 |
| Weekly R1 / S1 | 10,828 / 10,580 | 10,834.57 / 10,545.77 | −6.6 / +34.2 |
| Weekly R2 / S2 | 10,920 / 10,423 | 10,941.13 / 10,363.53 | −21.1 / +59.5 |
| Weekly R3 / S3 | absent | 11,123.37 / 10,256.97 | missing |
| Monthly (2026-06) P / R1 / S1 / R2 / S2 / R3 / S3 | absent | 10,412.17 / 10,698.13 / 10,215.53 / 10,894.77 / 9,929.57 / 11,180.73 / 9,732.93 | missing |

ATR14 (cash) = 117.51 (full 142.90): not stated in the report; the Trade 1 caveat implies 117.4 (consistent).

## 2. Category roll-up

| Category | Rows | Mean | Level | Multiplier | Points | Justification |
|---|---|---|---|---|---|---|
| C1 Prompt adherence (20) | 3,3,4 | 3.33 → 3, **−1 for restriction override** | 2 | 0.40 | 8.00 | Variables mostly respected, source-tier mix and date labelling drift; module code "M5" in §20 and retail-CFD high in the OHLC basis breach stated restrictions. |
| C2 Structure (20) | 4,2,4 | 3.33 | 3 | 0.65 | 13.00 | All sections present; §6 lacks Source A/B/Final columns; §11 has two levels per side and no monthly table. |
| C3 Accuracy & evidence (25) | 2,3,3,1 | 2.25 | 2 | 0.40 | 10.00 | Arithmetic reproduces, no fabricated source, but 4 of 5 closes outside ±5, 23 Jul close +21.1, D-1 O/H/L 14–24 pts off, range understated by half, daily and weekly outer pivots 20–60 pts off, §12/§14 unsourced. |
| C4 Reasoning & judgment (20) | 4,3,4,4,1 | 3.2 | 3 | 0.65 | 13.00 | Narrative reasoning is coherent and tensions are reconciled; card construction departs from the fixed M5 rules on all three cards. |
| C5 Currency & transparency (15) | 3,3,3,2 | 2.75 | 3 | 0.65 | 9.75 | Dating and flags mostly present; proxy-open and single-source caveats not propagated to cards; restriction breaches as above. |

## 3. Total, band, override

- Total = 8.00 + 13.00 + 10.00 + 13.00 + 9.75 = 53.75 → **54**
- Band: **Low** (40–59)
- Override check: hallucinated source — none found (three spot-checks consistent; no impossible or self-contradictory citation). Restriction breach — **yes** (module code "M5" printed in §20; a retail-CFD print used as the 27 Jul high in the OHLC basis; carried-forward opens in a CORROB table). Cap Moderate (60–74) not binding at 54; C1 reduced one level (3 → 2).

## 4. Card Integrity (linter rows, copied verbatim from `qa/ftse_qa1/lint_static/2026-07-28.csv`)

| card_id | strategy | flags | dud | Card score |
|---|---|---|---|---|
| 2026-07-28_Trade_1 | Trade 1 - Daily Directional (LONG) | CLEAN | False | 100 |
| 2026-07-28_Trade_2 | Trade 2 - Pivot (regime-aware, TREND_UP breakout) | CLEAN | False | 100 |
| 2026-07-28_Trade_3A | Trade 3A - Momentum-Pullback (LONG, TREND_UP fork) | CLEAN | False | 100 |

Report-level Card Integrity = 100.0 (n_cards=3, n_duds=0, n_warns=0). This is the static linter, which has no market data. Against the level file's ATR14 (cash 117.51; 0.3×ATR = 35.25) all three cards have R below the 0.3×ATR floor (29.0 / 35.0 / 29.0); this is not counted in Card Integrity and is dealt with in feedback.
