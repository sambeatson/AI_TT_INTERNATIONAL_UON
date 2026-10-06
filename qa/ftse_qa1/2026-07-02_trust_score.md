# Trust Score v3.7 — FTSE 100 Report 02 Jul 2026 (run ftse_qa1)

Report: `reports/md/FTSE_100_Report_02Jul2026.md` · D = 2026-07-02 · D-1 = 2026-07-01 (Wed) · level file `last_bar_date` = 2026-07-01 (< D, checked)
Basis claimed by the report: cash index, GBP, London close. Comparison basis used: `_cash` (qa_slice_stats `--cash-open 10:00 --cash-close 18:30`); `_full` shown where it changes the verdict.

## Score line

c1=1
c2=4
c3=0
c4=3
c5=2
total=40
band=Low
override=hallucinated_source
card_integrity=100
n_cards=3
n_duds=0
n_warns=0

Notes on the line: c1 is 2 on the checklist mean and is lowered one level for a second breach (the restriction breach in §20, see 5.4). The override field holds the more severe override, which caps the band at Low and sets c3=0 (checklist mean for c3 would have been 2). Total = 0.20×20 + 0.85×20 + 0.00×25 + 0.65×20 + 0.40×15 = 4 + 17 + 0 + 13 + 6 = 40.

## 1. Section 7 checklist

| Row | Score | Notes | Evidence location |
|---|---|---|---|
| 1.1 Variables respected | 2 | Asset, GBP/points, cash index, counters (USDX, S&P 500, DAX 40, Euro Stoxx 50 ref) are right. But the as-of is the 30 Jun close, not the London close of D-1 (1 Jul): the lookback window ends one session early. Source list has 6 names but the LSE/FTSE Russell row carries no figure, so only 5 usable. 07:00 UK anchor is used on Trade 1 but is described as an "override of the M1 anchor" (confused: 07:00 is the instance default). | header, §2, §4, §20, §21b |
| 1.2 Coverage & currency consistent | 1 | Whole report is one session stale. 1 Jul was a complete session (34 cash bars, close 10,472.4) yet §3 calls it "two overnight/half-sessions" and §19 says "no post-30-Jun corroborated cash print". Eurozone flash CPI (1 Jul 12:00 broker, already published in the slice with actual) is presented as upcoming in §13d / §1 / §18. Currency/unit consistent otherwise. | §1, §3, §13d, §19 |
| 1.3 Audience & tone | 4 | Institutional tone throughout; one stray "$10,800" in a TradingView derivation quote. | §1, §18, §13a |
| 2.1 Sections present & ordered | 5 | §1–§21 all present, in order; §13a–d and §21a–d present; §17 is one sentence; §21d carries the limitations boilerplate. Extra §3/§7 content fine. Charts are captions only (pandoc drop accepted). | headings |
| 2.2 Scorecard as a table | 2 | §6 is a table but has no "Final" column. §11 has only the daily pivot table, and it runs R5→S5 (five tiers, not three). No weekly or monthly pivot table (R3→P→S3); weekly P ≈10,459 and monthly P ≈10,413 appear only as prose. | §6, §11 |
| 2.3 Method steps visible | 4 | §4→§5 observations → classification → consensus visible; §8 is candle-by-candle with a sequence call; §9 gives regime with overlap/persistence/VOLator but as approximations ("~0.5", ">0.55"), no ATR value, no KER window. | §4–§9 |
| 3.1 Quantitative claims sourced | 2 | WTI ~$70, UK Bank Rate 3.75%, UK CPI 2.8%, VIX ~16.4, USDX ~101, YTD +19–20% have no source or pointer. VIX 16.4 is wrong: slice VIX close 17.61 (30 Jun), 17.81 (1 Jul). | §1, §12, §14 |
| 3.2 Citations exist & contain data | 0 | Three spot-checked. (a) CNBC row dated 28 Jun, headline "Dow ... first close above 52,000": 28 Jun 2026 is a Sunday; a market-close story cannot carry that date. Impossible date, which brief §2 row 3.2 counts as fabricated. (b) Yahoo × Investing "CORROBORATED Δ<0.1" on 26 Jun close 10,412.70 and 25 Jun/24 Jun rows: slice cash closes are 10,516.4 / 10,538.0 / 10,455.1 (−103.7 / −133.0 / +59.9), so the claimed agreement of two feeds cannot be real; 30 Jun Open 10,484.31 is identical to the 29 Jun Open. (c) Trading Economics "29 Jun ~10,508" contradicts the report's own 29 Jun close 10,484.22 (Δ 23.8) cited as the same-day level. | §4, §6, §13a |
| 3.3 Calculations transparent | 3 | RSI2 reproduces from the report's own closes for 26/29/30 Jun (6.5 / 100.0 / 100.0 via `--closes`). Pivots reproduce exactly from the report's 30 Jun H/L/C (P 10,531.39, R1 10,578.92, S1 10,449.60, R2 10,660.71, S2 10,402.07, R3 10,708.24, S3 10,320.28). ATR(14) value never stated (implied ≈111 from the card text); KER "+0.26" has no window/EMA stated and is not reproduced (13-session KER on cash closes to 30 Jun is 0.31 raw / 0.54 EMA3; to 1 Jul 0.03 / 0.35). Direction score arithmetic breaks (see 4.3). | §6, §9, §11, §20, §21 |
| 3.4 Numbers reconcile | 2 | D-1 close reconciles across sections only because every section uses the stale 30 Jun close; none matches the true D-1 close. Internal contradictions: §8 says the 30 Jun close finished "up ~50% of the range" — from §6 it is (10,497.12−10,483.86)/129.32 = 10%, i.e. close near the low, not a "strong bullish rejection" with a green-body close high; §13c says "26 Jun FTSE −1.1% area" while §6 has 26 Jun close 10,412.70 above 25 Jun 10,405 (+0.07%). Trade 1 caveat "ATR wide-stop note (R ≈ 0.5×ATR)" is self-contradictory. Card pivots equal §11 pivots (OK). | §6, §8, §13c, §21b |
| 4.1 Pillars conclude | 4 | §8, §9, §10 end in explicit labels; §12 and §14 end in a net-supportive tone without an explicit single label. | §8–§14 |
| 4.2 Peer/cross-asset interpreted | 4 | §10 gives mechanisms (USD translation, US/EU risk appetite, energy weight in §12). Not a correlation list. Mechanism for USDX "soft" is thin: slice USDX moved 101.59 (24 Jun) → 101.41 (1 Jul), flat, with a +0.24% rise on 1 Jul. | §10, §12 |
| 4.3 Synthesis reconciles tensions | 2 | Short-term label differs across sections: "Transitional–Bullish" (§1, Trade 1), "Bullish continuation" (§8), "Ranging-short" (§9). §20 raw score +0.76, §21a reports +0.30 after an ad-hoc "neutral-transition damping" that is not in the M5 rule set; the −0.46 haircut is unexplained and §21a lists three signals summing to +0.60, not +0.30. §21a says "no conflict" while the card regime labels differ. | §1, §8, §9, §20, §21a |
| 4.4 Calibrated language | 3 | §17 is exactly one sentence. Confidence stated High on the anchor close although the anchor is the wrong session and the same-section range band is ±0.15% around it. | §3, §17, §18 |
| Cards (protocol: card construction under C4) | 2 | Trade 1 stop buffer 8.6 pts (0.08×ATR) instead of 0.25×ATR; Trade 3A swing fails the ≥2×ATR qualifier on the report's own numbers and on the slice; against the true D-1 close Trade 1 MARKET entry is off by 24.6 and Trade 3A LIMIT sits on the wrong side. Details in feedback. Linter is clean (static, uses the report's own close) so the above is by comparison with the level file. | §21b |
| 5.1 Data dated; staleness flagged | 2 | Prices and articles are dated and 24/25 Jun are flagged single-source. But the one-session staleness is never flagged (it is described as "no post-30-Jun print"), and rows labelled CORROBORATED are far from the slice. | §4, §6, §13, §19 |
| 5.2 Assumptions up front | 4 | Anchor-override caveat is on Trade 1 and in §20; single-source flag propagated to cards via "corroboration waiver" caveats. | §19–§21b |
| 5.3 Red flags surfaced | 2 | The D-session calendar's highest-impact scheduled items are absent: US Nonfarm Payrolls / unemployment rate / average hourly earnings (15:30 broker, HIGH, 2 Jul), initial jobless claims (HIGH). §13d instead lists a UK "final GDP" release on 2 Jul that is not in the calendar slice. Calendar collisions are not carried into any card caveat. | §12, §13d, §15, §21b |
| 5.4 Restrictions honoured | 1 | §20 states "run instruction overrode the M1 anchor" (module code M1) and refers to "29-Apr baseline snapshot", §19/§20 to "DataCorroborationError", "per run instruction", "approved 50-source stack" — internal pipeline vocabulary, in breach of "no module codes". Rounded 24–26 Jun O/H/L (10,520 / 10,470 / 10,395 ...) are presented under CORROBORATED labels (26 Jun, 29 Jun). IG is correctly excluded from the consensus. | §19, §20, §6 |

## 2. Category roll-up

| # | Category | Level | Multiplier | Points / max | Justification |
|---|---|---|---|---|---|
| 1 | Prompt adherence | 1 | 0.20 | 4 / 20 | Checklist mean 2.33 → 2; lowered to 1 for the restriction breach (module code / pipeline vocabulary in §20). As-of window is one session stale. |
| 2 | Structural alignment | 4 | 0.85 | 17 / 20 | All 21 sections and sub-sections present; weak on §11 (no weekly/monthly tables, five tiers) and §6 (no Final column). |
| 3 | Accuracy & evidence | 0 | 0.00 | 0 / 25 | Hallucinated-source override (impossible-dated CNBC citation; "corroborated" closes 104–133 pts from the slice). Checklist mean without override would be 2. |
| 4 | Reasoning & judgment | 3 | 0.65 | 13 / 20 | Pillars and cross-asset mechanism sound; score derivation, short-term label and card construction have visible faults. |
| 5 | Currency & transparency | 2 | 0.40 | 6 / 15 | Dates and anchor caveats present; staleness unflagged, D-session calendar wrong/missing, restriction breach. |

## 3. Total, band, override check

- Total = 40 → band Low (40–59).
- Hallucinated-source override: triggered. Cap Low (40–59, not binding at 40), C3 forced to 0.
- Restriction-breach override: also triggered (module code M1 and pipeline terms in §20). Cap Moderate (60–74) is superseded by the Low cap; C1 reduced one level (2 → 1). Recorded in the single `override=` field as the more severe, `hallucinated_source`.
- Human spot-check recommended on the CNBC row (date 28 Jun is a Sunday); if the date is shown to be a transcription slip rather than a non-existent article, c3 would revert to 2 and the total to 50 (still Low) with override=restriction_breach.

## 4. Category 3 data reconciliation (report vs `data/levels/UK100_by_date/2026-07-02.csv` and slice, cash basis)

Tolerance (brief §4): |Δ| ≤ 5 close, ≤ 10 open/high/low. Report − slice.

| Date | Field | Report | Slice cash | Δ | Verdict |
|---|---|---|---|---|---|
| 24 Jun | O / H / L / C | 10,455 / 10,520 / 10,440 / 10,515 | 10,422.2 / 10,468.6 / 10,400.6 / 10,455.1 | +32.8 / +51.4 / +39.4 / +59.9 | all four outside; close >15 = failure |
| 25 Jun | O / H / L / C | 10,515 / 10,535 / 10,395 / 10,405 | 10,427.6 / 10,577.7 / 10,413.8 / 10,538.0 | +87.4 / −42.7 / −18.8 / −133.0 | all four outside; close >15 = failure |
| 26 Jun | O / H / L / C | 10,405 / 10,470 / 10,395 / 10,412.70 | 10,498.3 / 10,516.4 / 10,401.4 / 10,516.4 | −93.3 / −46.4 / −6.4 / −103.7 | O, H, C outside; close >15 = failure; L ok |
| 29 Jun | O / H / L / C | 10,484.31 / 10,520 / 10,470 / 10,484.22 | 10,505.9 / 10,524.3 / 10,468.8 / 10,497.8 | −21.6 / −4.3 / +1.2 / −13.6 | O outside; C outside (≤15); H, L ok |
| 30 Jun | O / H / L / C | 10,484.31 / 10,613.18 / 10,483.86 / 10,497.12 | 10,509.5 / 10,608.8 / 10,490.6 / 10,501.5 | −25.2 / +4.4 / −6.7 / −4.4 | O outside; H, L, C ok |
| 1 Jul (D-1) | all | not in report | 10,481.4 / 10,500.3 / 10,416.0 / 10,472.4 | n/a | missing session |

RSI2: report's own closes reproduce the report's RSI2 for 26/29/30 Jun (6.5/100.0/100.0), so the arithmetic is internally consistent; the inputs are wrong. Slice cash RSI2: 25 Jun 100.00, 26 Jun 79.33, 29 Jun 0.00, 30 Jun 16.59, 1 Jul 11.28 (full basis 0.00). Report values 37.9 / 6.5 / 100.0 / 100.0 are 62 / 73 / 100 / 83 points from these. D-1 RSI2 absent from the report.

ATR14: never stated; implied ≈111 (cards) vs level file cash 109.44 / full 115.33 — consistent.

Pivots (report daily pivots are for the 30 Jun session; D-1 pivots must come from 1 Jul):

| Level | Report | Level file cash | Δ | Level file full | Δ |
|---|---|---|---|---|---|
| Daily P | 10,531.4 | 10,462.9 | +68.5 | 10,460.63 | +70.8 |
| R1 | 10,578.9 | 10,509.8 | +69.1 | 10,505.27 | +73.6 |
| S1 | 10,449.6 | 10,425.5 | +24.1 | 10,417.07 | +32.5 |
| R2 | 10,660.7 | 10,547.2 | +113.5 | 10,548.83 | +111.9 |
| S2 | 10,402.1 | 10,378.6 | +23.5 | 10,372.43 | +29.7 |
| R3 | 10,708.2 | 10,594.1 | +114.1 | 10,593.47 | +114.7 |
| S3 | 10,320.3 | 10,341.2 | −20.9 | 10,328.87 | −8.6 |
| Weekly P (W26) | ≈10,459 | 10,474.07 | −15.1 | 10,457.27 | +1.7 |
| Monthly P (Jun) | ≈10,413 | 10,412.17 | +0.8 | 10,413.73 | −0.7 |

Weekly P matches the full-day basis, not the cash basis the report claims. Weekly/monthly R/S tiers not given. Report's own pivot arithmetic is correct for its 30 Jun H/L/C.

Other data checks: VIX ~16.4 vs slice 17.61 (30 Jun) / 17.81 (1 Jul); S&P 500 +0.79% on 30 Jun vs slice +0.66% (CFD, UTC day); USDX ~101 vs 101.17 (30 Jun) / 101.41 (1 Jul) consistent; DAX / Euro Stoxx not in slices (not checked). Report's "5-day swing low 10,395" vs slice 10,401.4 (26 Jun) (Δ 6.4, ok); 25-session low in slice 10,126.2 (10 Jun) vs report "~10,320" start of the leg.

## 5. Card Integrity (linter rows `qa/ftse_qa1/lint_static/2026-07-02.csv`, copied verbatim)

| card_id | report_date | strategy | flags | dud |
|---|---|---|---|---|
| 2026-07-02_Trade_1 | 2026-07-02 | Trade 1 - Daily Directional (LONG · Transitional–Bullish) | CLEAN | False |
| 2026-07-02_Trade_2 | 2026-07-02 | Trade 2 - Pivot, regime-aware (TREND_UP → pivot breakout LONG) | CLEAN | False |
| 2026-07-02_Trade_3A | 2026-07-02 | Trade 3A - Momentum-Pullback (TREND_UP → LONG) | CLEAN | False |

Per card: 100 / 100 / 100 (0 DUD, 0 WARN). Report-level Card Integrity = 100 (3 non-suppressed cards). Not part of the 100-point total. The linter is static and uses the report's own D-1 close; the construction defects in the feedback file come from comparing the cards with the level file and the M5 rules, not from re-running the linter.

## 6. Feedback

See `qa/ftse_qa1/2026-07-02_feedback.md`.
