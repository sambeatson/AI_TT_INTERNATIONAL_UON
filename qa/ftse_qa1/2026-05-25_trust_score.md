# Trust Score v3.7 — FTSE 100 Daily Report, 25 May 2026 (run ftse_qa1)

Report: `reports/md/FTSE100_Report_25May2026.md` · D = 2026-05-25 · D-1 session = Fri 22 May 2026
Level file check: `data/levels/UK100_by_date/2026-05-25.csv` has `last_bar_date = 2026-05-22` (< D), so it is leak-free. The slice's last bar is 2026-05-22 22:45 broker.
Basis used for Category 3: the report claims a **cash index, regular session** (§2), so the `_cash` fields (10:00–18:30 broker = 08:00–16:30 London) are the primary comparison. `_full` values are shown where they change the conclusion.
Reference values (22 May, cash): O 10,492.6 · H 10,494.5 · L 10,446.0 · C 10,470.4 · RSI2 100.0 · ATR14 143.99 (full-day basis: C 10,436.6 · ATR14 163.72 · RSI2 46.7).
Note: 25 May 2026 is a UK Spring Bank Holiday (calendar row `GBP Spring Bank Holiday`, also `USD Memorial Day`, `EUR/CHF/NOK Whit Monday`). The report never mentions this.

```
c1=2
c2=4
c3=0
c4=3
c5=2
total=44
band=Low
override=hallucinated_source
card_integrity=100
n_cards=3
n_duds=0
n_warns=0
```

Override note: `hallucinated_source` is the binding override (cap Low 40–59, C3 forced to 0). A `restriction_breach` is also present (M5 suppression rules overridden, see 5.4 and 4.5). Its effect is already applied to C1, which falls from 3 to 2. The single `override=` value reports the stricter cap.

---

## 1. Section 7 checklist (every row filled)

### Category 1 — Prompt adherence

| Row | Reviewer notes | Evidence (location) | Score |
|---|---|---|---|
| 1.1 Variables respected | FTSE 100 cash index is the primary asset, with Euro Stoxx 50 as reference only (cards are FTSE only). Counters are USDX, S&P 500 and DAX 40, with VIX mentioned. As-of 22 May close, London, 5-session lookback, GBP and index points all correct. **Misses:** (a) the daily-open anchor is overridden from the instance value 07:00 UK to 00:00 UK, justified only by "per the analytical brief". A deviation from the populated anchor is a logged non-conformance, not a run-time choice. (b) The "≥ 6 sources from index provider / exchange / sell-side tiers" requirement is not met: Yahoo, Trading Economics, Fidelity, IBTimes, BBN Times and Investing.com are aggregators, media or retail brokers, and none is an index provider, exchange or sell-side source. Investing.com has no quote at all in §4 ("Historical series"). | Scope note, §4, §6, §19, §20, Trade 1 card | 2 |
| 1.2 Coverage & currency consistent | Currency is consistent. **Coverage drift:** (a) §11 daily pivots are "computed from the Thursday 21 May session" (D-2), not 22 May (D-1). (b) §11 weekly pivots are "from the prior week (11–15 May)". The completed prior week at D is 18–22 May (level file W21). (c) A Jan 2026 Morningstar item sits in a 5-session sentiment window (§13a). (d) §13d lists "UK PMIs, confidence" as upcoming, but the UK flash PMIs were released 21 May. (e) 25 May is treated as a normal LSE session ("cash-session open", "25 May session close" time-stop) when it is a UK bank holiday. | §11, §13a, §13d, §21b | 2 |
| 1.3 Audience & tone | Strategist register, trading and risk review, no retail tone. | §1, §18 | 4 |

Mean 2.67, which rounds to 3. Restriction-breach override reduces C1 by one level, so **C1 = 2**.

### Category 2 — Structure

| Row | Reviewer notes | Evidence | Score |
|---|---|---|---|
| 2.1 Sections present & ordered | §1–§21 all present and in order. §13a–d, §21a–d all present. §17 is one sentence. §21d carries the limitations boilerplate. §7 is five chart descriptions with no embedded images (accepted per brief, noted). | headings | 5 |
| 2.2 Scorecard / pivots as tables | §6 is a table (FTSE and Euro Stoxx) with the required columns. The validation column is headed "Outcome". Pivot tables run R→S but give **5 levels each side (R5…S5)**, not the 3 each side (R3…S3) the checklist expects. | §6, §11 | 4 |
| 2.3 Method steps visible | Observations → classification → consensus (§4–5), candle-by-candle plus sequence (§8), regime with persistence/overlap/VOLator/KER (§9), five charts described (§7). Present, but several of the visible steps rest on wrong inputs (see C3). ATR(14) is not shown as a number anywhere. | §4–§9 | 4 |

Mean 4.33 → **C2 = 4**.

### Category 3 — Accuracy & evidence (all comparisons are report minus level file)

| Row | Reviewer notes | Evidence | Score |
|---|---|---|---|
| 3.1 Quantitative claims sourced | §1 and §3 point to §4/§6/§13. §12 and §14 carry bare, unsourced figures: Brent "near $100", VIX "~16.7", retail sales "−1.3% vs −0.6% expected", 8–1 vote. **VIX ~16.7 conflicts with the slice** (22 May VIX cash-session close 17.86, last bar 18.16). The "78th percentile" 25-day position is unsupported: from the level file it is 62.7% (cash) / 55.8% (full). | §1, §9, §12, §14 | 2 |
| 3.2 Citations exist & contain the cited data | Three sources checked. **(i) IBTimes**: its own quote is close 10,461.88 and range 10,435.53–10,497.22, yet §6 uses "BBN/IBTimes" as Source B and calls the 22 May row fully "Corrob." at 10,466.26 / H 10,488.05. The close differs by 4.38 and the high by 9.17. The "±0.10 pts on the close" corroboration claim is contradicted by §4's own figures (IBTimes 4.38 away, Trading Economics 10,466/10,474 up to 8 away). The 8-pt gap is described as "provider rounding". **(ii) Bank of England (MPR, Apr)** is dated 29 Apr 2026 in §12, §13a, §13d and §14. The calendar slice shows the decision, vote and Monetary Policy Report on 30 Apr 2026 (3.75, 8 unchanged, 1 hike). The "derivation quote" attributed to this official source ("reduced near-term hike odds are supportive for UK equities") describes the 22 May data, which an April document cannot contain. It is the report's own inference attributed to the BoE. **(iii) Fidelity/Sharecast** 14:53 BST 10,470.09 is consistent with the slice (14:45 UTC bar closes 10,471.8). Two of three spot-checks fail on internal consistency or date, so the brief's "wrong date / figure not matching its own quote" fabrication test is met. | §4, §6, §13a | 0 |
| 3.3 Calculations transparent | **Pass:** RSI2 formula reproduces for 20, 21 and 22 May from the report's own closes (all 100.0); the pivot arithmetic is internally correct for the inputs used (daily P from 21 May H/L/C = 10,417.97; weekly and monthly are formula-consistent). §21a scores sum correctly to +0.40. **Fail:** (a) 18 and 19 May RSI2 (100.0) cannot be reproduced from the table (no prior closes), and 18 May is 39.6 in the slice. (b) ATR(14) is never stated; the cards imply ≈ 92–93 (Trade 3 "400 pts ≈ 4.3×ATR"; Trade 1 3×ATR cap ≈ 276 pts) versus 143.99 (cash) / 163.72 (full): 36% / 43% too low. (c) §13b tilt arithmetic is wrong: weights 1.0 + 0.7 + 3×0.5 + 1.0 = **4.2**, not 4.7, so the tilt is 1.7 / 4.2 = **+0.40**, not +0.36. (d) KER13 EMA3 is stated −0.16. Recomputed from the slice it is **+0.14 (cash) / +0.10 (full)**, so the sign and the class "Trending Down — Moderate" are not reproduced. (e) §21a Kaufman contribution −0.15 treats the signal as −1.0, but the strategy rule is linear in the KER value (−0.16 × 0.15 = −0.024). | §6, §9, §13b, §21a, §21b | 2 |
| 3.4 Numbers reconcile (internally and to the level file) | Internal: the D-1 close 10,466 is identical in §1, §3, §4, §6 and the Trade 1 entry, and §11 pivots match the card quotes. Backtest does not reconcile (see 4.5). **Against the level file (cash basis) the D-1 block fails:** closes are off by −19.5, −26.6, −34.2 and −18.8 pts for 18–21 May, which is over 15 pts on four of five days. See the deltas below. Only 2 of 20 O/H/L/C values fall inside tolerance (22 May H and C). The 22 May open is off by −49.1. Opens for 19–22 May equal the prior close to the cent, while real opens differ by 17.6–68.6 pts. Daily, weekly and monthly pivots are off by up to 96, 339 and 430 pts (table below). | §6, §11 | 1 |

Mean (2, 0, 2, 1) = 1.25 → 1 before override. **Hallucinated-source override sets C3 = 0.**

#### C3 detail A — D-1 OHLC block, report vs level file (cash basis; tolerance close ≤ 5, O/H/L ≤ 10)

| Date | Field | Report | Level/slice (cash) | Δ | Verdict |
|---|---|---|---|---|---|
| 18 May | O / H / L / C | 10,204.10 / 10,286.40 / 10,188.55 / 10,271.32 | 10,144.5 / 10,336.3 / 10,141.2 / 10,290.8 | +59.6 / −49.9 / +47.4 / −19.5 | all four fail; close > 15 |
| 19 May | O / H / L / C | 10,271.32 / 10,318.70 / 10,238.90 / 10,298.55 | 10,339.9 / 10,408.9 / 10,313.0 / 10,325.1 | −68.6 / −90.2 / −74.1 / −26.6 | all four fail; close > 15 |
| 20 May | O / H / L / C | 10,298.55 / 10,402.10 / 10,295.20 / 10,388.74 | 10,274.4 / 10,458.8 / 10,272.8 / 10,422.9 | +24.2 / −56.7 / +22.4 / −34.2 | all four fail; close > 15 |
| 21 May | O / H / L / C | 10,388.74 / 10,448.30 / 10,362.15 / 10,443.47 | 10,371.1 / 10,469.1 / 10,344.7 / 10,462.3 | +17.6 / −20.8 / +17.5 / −18.8 | all four fail; close > 15 |
| 22 May (D-1) | O / H / L / C | 10,443.47 / 10,488.05 / 10,435.53 / 10,466.26 | 10,492.6 / 10,494.5 / 10,446.0 / 10,470.4 | −49.1 / −6.5 / −10.5 / −4.1 | H and C pass; O fails; L fails by 0.5 |

Full-day basis does not rescue it: closes are −76.3 / +11.0 / −54.6 / −47.0 / +29.7 for 18–22 May.

Candle and trend facts that the report gets wrong, from the slice (cash):
- 19 May closed below its open (10,339.9 → 10,325.1).
- 22 May closed below its open (10,492.6 → 10,470.4). The day opened at its high.
- §7 says "all five are green" and §6 labels both days "Bullish".
- Under the brief's rule (Close<Open with RSI2>50 = Neutral), 19 and 22 May are Neutral on cash, and 22 May is Bearish on full-day (RSI2 46.7).
- 18 May opened below the 15 May close (10,144.5 vs 10,167.0, a −22.5 gap), not a "weekend gap-up".
- §6 18 May RSI2 is 100.0 versus 39.6 in the slice.
- Ranges quoted in §7–§8 (107 / 86 / 52 pts) compare with 186.0 / 124.4 / 48.5 in the slice for 20 / 21 / 22 May.

#### C3 detail B — pivots and statistics, report vs level file

| Item | Report | Level file (cash / full) | Note |
|---|---|---|---|
| Daily P / R1 / S1 | 10,417.97 / 10,473.80 / 10,387.65 | 10,470.3 / 10,494.6 / 10,446.1 (cash); 10,463.97 / 10,492.33 / 10,408.23 (full) | Built from 21 May, not 22 May. P is off by −52.3 / −46.0. S1 is off by −58.5 / −20.6. |
| Daily R2 / S2 | 10,504.12 / 10,331.82 | 10,518.8 / 10,421.8 (cash); 10,548.07 / 10,379.87 (full) | S2 off by −90.0 / −48.1 |
| Daily R3 / S3 | 10,559.95 / 10,301.50 | 10,543.1 / 10,397.6 (cash); 10,576.43 / 10,324.13 (full) | S3 off by −96.1 / −22.6 |
| Weekly P / R1 / S1 | 10,213.13 / 10,338.27 / 10,066.27 | 10,368.7 / 10,596.2 / 10,242.9 (cash); 10,354.43 / 10,601.87 / 10,189.17 (full) | Report uses 11–15 May. P is off by −155.6 / −141.3, R1 by −257.9 / −263.6. |
| Weekly R2 / S2 / R3 / S3 | 10,485.13 / 9,941.13 / 10,610.27 / 9,794.27 | 10,722.0 / 10,015.4 / 10,949.5 / 9,889.6 (cash) | R2 off by −236.9. The "weekly R2 / daily R1 confluence at 10,474–10,489" disappears on the correct week. |
| Monthly (Apr) P / R1 / S1 | 10,263.78 / 10,609.22 / 9,904.55 | 10,418.8 / 10,650.0 / 10,140.1 (cash); 10,421.17 / 10,671.63 / 10,114.83 (full) | Right month, wrong H/L/C. P is off by −155.0. S1 is off by −235.6 / −210.3. |
| Monthly R2 / S2 / R3 / S3 | 10,968.45 / 9,559.11 / 11,313.89 / 9,199.88 | 10,928.7 / 9,908.9 / 11,159.9 / 9,630.2 (cash) | S2 off by −349.8, S3 off by −430.3 |
| Weekly inputs implied by the report's own levels | H 10,360 / L 10,088 / C ≈ 10,191 | 11–15 May cash H 10,371.1 / L 10,145.9 / C 10,167.0 | L 10,088 matches no bar in the last 10 sessions (lowest cash low 10,141.2, full 10,107.0). It is also the card's swing-low anchor. |
| ATR14 | not stated; implied ≈ 92–93 | 143.99 (cash) / 163.72 (full) | −36% / −43% |
| KER13 EMA3 | −0.16 "Trending Down — Moderate" | +0.14 (cash) / +0.10 (full) | sign not reproduced |
| 25-day range position | ~78th percentile | 62.7% (cash) / 55.8% (full) | |
| VIX | ~16.7 | 17.86 cash-session close, 18.16 last bar | |
| 5-day swing (low → high) | ~10,088 → 10,488 (≈ 400 pts, 4.3×ATR) | 10,141.2 → 10,494.5 = 353.3 pts = 2.45×ATR (cash); 10,107.0 → 10,519.7 = 412.7 pts = 2.52×ATR (full) | Qualifies (≥ 2×ATR) but not at 4.3× |

### Category 4 — Reasoning & judgment

| Row | Reviewer notes | Evidence | Score |
|---|---|---|---|
| 4.1 Pillars conclude | §8 "Bullish continuation", §9 "Transitional", §10 "CONFIRM", §12 per-factor labels, §14 closes with a cross-reference check but no single direction label. The conclusions are firmly stated, but §8 relies on candle bodies that are wrong for 19 and 22 May, and §9 on a KER sign that the slice does not reproduce. | §8–§14 | 3 |
| 4.2 Peer/cross-asset interpreted | Mechanisms are given, but they are generic ("risk-appetite proxy", "two-sided" for USD). The FTSE-specific channels (dollar-earner weight, energy/Brent) are not tied to a counter in §10. Brent is discussed only in §12. USDX is labelled "Falling / Flat". In the slice USDX 15 May → 22 May is 99.29 → 99.34 (flat), so "falling" is unsupported. | §10 | 3 |
| 4.3 Synthesis reconciles tensions | §15/§16/§18 and §21a address short-term vs medium-term vs Kaufman and §17 vs §21a explicitly and coherently. The tension itself is built on an unreproduced KER sign and a stale-period pivot set. The TRANSITION regime then drives the Trade 2 and Trade 3 branches. | §9, §15–§18 | 3 |
| 4.4 Calibrated language | §17 is exactly one sentence. Confidence Medium is stated in §3. "Unambiguously Trending Bullish" and "orderly grind" are slightly over-firm given the data issues. | §3, §9, §17 | 4 |
| 4.5 Card construction (protocol row) | Substantive failures: (a) **Trade 2 should be SUPPRESSED.** §19/§20 state every pivot tier is SINGLE-SOURCE-INDICATIVE, yet the card is shipped "per the brief". (b) **Trade 2 wrong-side entry:** BUY STOP 10,424 is 42 pts below the report's own D-1 reference close 10,466 (and 46.4 below the cash close 10,470.4). (c) Trade 2 uses the TREND geometry (P + 0.10×(R1−P), P − 0.8×(P−S1), R1/R1.5/R2) while labelled TRANSITION. (d) **Trade 3A substituted for 3C.** In TRANSITION the fork is 3C; if its eligibility fails the output is a SUPPRESSED row. 3C needs a daily close ≥ 25d high 10,666.5 + 0.25×ATR 36.0 = 10,702.5, which is 232.1 above the D-1 close of 10,470.4 (the boundary itself is 196.1 above). (e) ATR is implied ≈ 92 rather than 143.99, so buffers, the 3×ATR runner cap (10,742 vs 10,902.4 on cash ATR) and the swing qualifier are all mis-scaled. (f) R ÷ ATR and the reference close with session date are not printed on any card; the wide-stop flag is asserted for Trade 1 only. (g) Trade 3 endpoints are "~10,088 (week of 11–15 May)", with no lookback or magnitude logged. 10,088 is not in the data. (h) The Trade 1 anchor 00:00 UK differs from the instance 07:00 UK. (i) §21c backtest does not reconcile: "mean R +1.18 across closed positions" is 1.35 over the four closed rows (1.18 only if the open +0.5R row is included); TP1 "100%" hit rate is inconsistent with the 22 May row open at +0.5R; "5+ days" open on the last session. The linter row for each card is CLEAN. The defects above are rule-text defects, not static-linter flags. | §21a–d, §19, §20 | 1 |

Mean (3, 3, 3, 4, 1) = 2.8 → **C4 = 3**.

### Category 5 — Currency, restrictions, transparency

| Row | Reviewer notes | Evidence | Score |
|---|---|---|---|
| 5.1 Data dated; staleness flagged | Most items are dated. Brent, VIX and the retail-sales consensus are undated and unsourced. The Jan 2026 Morningstar item is included in the "5-day" tilt without a staleness flag. The BoE source carries a wrong date (29 vs 30 Apr). The 22 May row is said to be fully corroborated while the report's own sources disagree. The indicative flag is applied to H/L but not to opens, which are chained to the prior close. | §4, §6, §12–§14 | 3 |
| 5.2 Assumptions up front | The anchor-override caveat is in the scope note, §20 and the Trade 1 card. Indicative-pivot propagation is stated in §19, §20 and each card. The up-front omission is the bank holiday. | scope note, §19–§21b | 4 |
| 5.3 Red flags surfaced | Missing: UK Spring Bank Holiday / US Memorial Day / Whit Monday collision on D (none in §13d, §15 or the card caveats). UK CPI y/y printed 2.8 vs 3.8 consensus (prev 3.4) on 20 May and UK composite PMI 48.5 (prev 52.6) on 21 May. §13c/§14 describe CPI only as "above the 2% target / looked through" and attribute 21 May to "political turmoil", with the PMI miss unmentioned. | §13c, §13d, §14, §15 | 2 |
| 5.4 Restrictions honoured | Open breaches of fixed M5 rules, each justified in the report by "per the brief": Trade 2 shipped with every pivot tier flagged indicative; Trade 3A built in place of the SUPPRESSED 3C row; wrong-side BUY STOP shipped with a note; anchor re-selected for this run. §6 opens equal to the prior close to the cent on four days, presented as Source A/B corroborated (cannot be matched to any feed in the slice; suspected synthesised values). A module-version token ("v2.1 baseline") appears in §20. No retail CFD quotes or futures used. | §6, §19–§21b | 0 |

Mean (3, 4, 2, 0) = 2.25 → **C5 = 2**.

---

## 2. Category roll-up

| # | Category (max) | Level | Multiplier | Points | One-line justification |
|---|---|---|---|---|---|
| 1 | Prompt adherence (20) | 2 | 0.40 | 8.0 | Anchor re-selected, source tiers not met, pivot periods stale; breach override lowers 3 → 2. |
| 2 | Structure (20) | 4 | 0.85 | 17.0 | All 21 sections in order; pivot tables carry 5 levels per side instead of 3; charts are text only. |
| 3 | Accuracy & evidence (25) | 0 | 0.00 | 0.0 | Four of five closes off by 19–34 pts, pivots off by 50–430 pts, a source whose date and quote are inconsistent; hallucinated-source override. |
| 4 | Reasoning & judgment (20) | 3 | 0.65 | 13.0 | Coherent narrative, but the premises are wrong (KER, candles) and card construction breaks fixed rules. |
| 5 | Currency & transparency (15) | 2 | 0.40 | 6.0 | Bank holiday and CPI/PMI misses omitted; M5 suppression rules overridden. |

## 3. Total, band, override

- Total = 8.0 + 17.0 + 0.0 + 13.0 + 6.0 = **44** → band **Low** (40–59).
- Override check: the hallucinated-source override applies (cap Low, C3 = 0, consistent with the 44 above). The restriction-breach override also applies (cap Moderate, C1 reduced one level, already applied). No further cap changes the result.

## 4. Card Integrity (separate from the 100) — linter rows copied verbatim from `qa/ftse_qa1/lint_static/2026-05-25.csv`

| card_id | report_date | strategy | flags | dud |
|---|---|---|---|---|
| 2026-05-25_Trade_1 | 2026-05-25 | Trade 1 — Daily Directional | CLEAN | False |
| 2026-05-25_Trade_2 | 2026-05-25 | Trade 2 — Pivot (regime-aware). Regime TRANSITION → breakout-side limit only. | CLEAN | False |
| 2026-05-25_Trade_3A | 2026-05-25 | Trade 3 — Momentum-Pullback (3A). Built against the most recent qualifying up-swing; see Caveats for the regime note. | CLEAN | False |

Per card: 100 − 40×0 − 10×0 = 100 for each of the 3 non-suppressed cards. The report-level mean is 100.
The linter is static and leak-free, so it does not test the market-relative or rule-text defects recorded under 4.5. Those defects are in the feedback file.

## 5. Feedback

See `qa/ftse_qa1/2026-05-25_feedback.md`.
