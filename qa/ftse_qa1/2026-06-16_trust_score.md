# Trust Score v3.7 — FTSE 100 report dated 2026-06-16 (run ftse_qa1)

Report: `reports/md/FTSE_EuroStoxx_Report_16Jun2026.md` · D = 2026-06-16 · D-1 = 2026-06-15 (Mon)
Level file check: `last_bar_date` = 2026-06-15 < D, so it is leak-free. Basis used: **cash** (`_cash`), because the report claims the cash index. Full-day figures are shown where relevant.

## Machine-readable result
```
c1=3
c2=3
c3=2
c4=3
c5=3
total=59
band=Low
override=none
card_integrity=100
n_cards=3
n_duds=0
n_warns=0
```

## Headline finding
The report anchors on **Friday 12 June** (D-2) as "the as-of close" and deliberately sets Monday 15 June (D-1) aside as "developing context" (§1, §2, §3, §6, §19). The brief requires the as-of to be the London close of D-1. Every downstream level (consensus close, five-session table, pivots, RSI2, cross-asset counters, all three card entries) is therefore one session stale. The data-derived D-1 (15 Jun) cash close is 10,441.2 (full-day 10,415.6); the report states 10,471.72 in §1, §3, §4, §6, §18 and on the Trade 1 entry — off by 30.5 pts (cash) / 56.1 pts (full-day), over the 15-pt "failure to score" threshold in brief §4.

## 1. Section 7 checklist

| Row | Level | Notes and evidence location |
|---|---|---|
| 1.1 Variables respected | 2 | Asset (FTSE 100 cash, Euro Stoxx 50 as reference) and counters (USDX, S&P 500, DAX 40) are right; GBP/points right; lookback is 5 sessions in count (§2). But as-of is Fri 12 Jun, not D-1 Mon 15 Jun (§1, §2 "As-of reference", §3). Window is 8-12 Jun, should be 9-15 Jun. Anchor is overridden to 00:00 UK (§20, Trade 1 entry) instead of 07:00 UK; disclosed, so a noted deviation not a breach. Source tiers: the five "Core" sources (FT/BBN Times, Yahoo, TradingView, AJ Bell, Fidelity) are retail/media aggregators of one LSE feed, not index-provider / exchange / sell-side tiers; "5 independent sources" (§4, §5) overstates independence. |
| 1.2 Coverage and currency consistent | 2 | Data dates stop at 12 Jun while the narrative uses 15 Jun facts: Brent ~$83 on 15 Jun and Shell/BP "fell 3-4.6% on Monday" (§12), oil "~5% into the new week" (§1), Share Talk Monday futures (§13a). A report that cites Monday evidence but excludes Monday's bar is internally inconsistent. Currency/units consistent (GBP points; STOXX in EUR labelled). |
| 1.3 Audience and tone | 4 | Professional strategist register, trading-and-risk-review use, no retail tone (§1, §18). Minor: "not investment advice" footer is boilerplate. |
| 2.1 Sections present and ordered | 5 | §1-§21 all present and in order; §13a-d and §21a-d present; §17 is one sentence. |
| 2.2 Scorecard as table | 2 | §6 is a table but lacks the required Source A / Source B / Final columns (only Date, O, H, L, C, RSI2, Trend, Validation). RSI2 blank ("—") for two of five FTSE rows and Mon/Tue STOXX. §11 daily table has no R3 (R3 10,697 appears only on the Trade 1 card), merges "R1.5 / R2" in one cell, and gives no S1.5-to-S3 symmetry in a three-each-side R3→P→S3 layout; weekly table has only WS2..WR2; **monthly pivots are absent entirely**. |
| 2.3 Method steps visible | 3 | §4-§5 show observations, classification and consensus; §8 is candle-by-candle with a sequence read; §9 gives regime with KER and VOLator. §7 renders no charts, only a caption table (accepted as placeholder per brief, but the report says charts "will populate on a run with full OHLC corroboration"). §9 does not state KER parameters (13, EMA 3) or show the overlap/persistence figures. |
| 3.1 Quantitative claims sourced | 3 | §4 and §6 carry source labels. Unsourced in §1/§9/§12/§14: record high 10,934.94, "$120 conflict peak", Brent ~$83 / WTI ~$80, HICP 3.2%, "three-week closing high above the 50-day average" (no 50-day figure shown), VIX "~17.7, -9%". |
| 3.2 Citations exist and contain data | 2 | Spot checks. (a) FT/BBN Times "+1.63% / +168.84 pts": 10,471.72 - 168.84 = 10,302.88 = the report's own Thu close, so internally consistent. (b) Investing.com "O 10,302.68 / H 10,471.72" (§4, §5): §19 says Investing.com was "unreachable" and §20 says "stale cache"; the quoted Friday open 10,302.68 equals the report's Thu close (10,302.88) minus 0.20 and also equals the Friday low, whereas the UK100 cash session for 12 Jun opened 10,368.9 with low 10,368.3 (66 pts higher). Self-contradictory and not matching the feed; not treated as an outright fabricated source because the report itself flags it as a stale-cache "Directional" quote, but it carries weight in §5 and §8. (c) AJ Bell "15 Jun prev close 10,471.72": consistent with a Friday settle. Fidelity "12 Jun 16:35 BST, 15-min delayed" implies the quote is not the closing print. |
| 3.3 Calculations transparent | 3 | Daily pivot reproduces exactly from the report's own Fri H/L/C (P 10,415.37; R1 10,528.06; S1 10,359.02; S2 10,246.33; S3 10,189.98). RSI2 reproduces from the report's own closes (16.1 / 100.0 / 100.0 confirmed by `qa_slice_stats --closes`) but RS gains/losses are not shown. ATR(14) "≈118" has no derivation. §21a score does not add up: listed contributors 0.25 + 0.15 + 0.09 + 0.15 = 0.64, stated +0.68; the sixth weighted signal (0.15) is never named. §21d "TP2 hit rate ≈33%" is not supported by the §21c rows (no row reaches +2R). Sentiment tilt 3.00/4.90 = 0.61 is arithmetically right but the per-article weights are not shown. |
| 3.4 Numbers reconcile | 2 | Close 10,471.72 is identical across §1/§3/§4/§6/§18/§21b, and §11 pivots match the cards (but the R3 10,697 on Trade 1 is not in §11). Breaks: (i) §8 says Wed 10 Jun "opened 37 points lower at 10,336" but §6 gives Tue close 10,226.80, so 10,336 is a +109.2 gap up (37 below Mon's 10,373.10, not Tue's close); (ii) §8 says Thu "turned up ~1.0%", §6 gives 10,254.81 to 10,302.88 = +0.47%; (iii) Trade 3A states stop 10,330 "~170 pts" from entry 10,500 but R "~80 pts"; (iv) Trade 1 confluence "S1 10,359 and open 10,303 within 0.15×ATR" but they are 56 pts apart (0.47×ATR 118); (v) §21c Trade 2 row "limit 10,300 → 10,254" labelled "+1R" (10,254 is below the entry); (vi) §14 VIX "~17.7, collapsed ~9% on Friday". |
| 3.5 Data check vs level file (brief §4) | 1 | See table below. D-1 close wrong by 30.5 pts; five-day table is the wrong window with open/high/low errors up to 90.5 pts; every daily pivot tier is struck from D-2; weekly pivots wrong by 11-77 pts; monthly absent; ATR14 118 vs 111.04. |
| 4.1 Pillars conclude | 4 | §9 label (TREND_UP, transitional lean), §10 (CONFIRM), §14 ("net-supportive"), §12 ("price-supportive on balance") conclude. §8 ends on levels with no explicit direction label. |
| 4.2 Peer/cross-asset interpreted | 3 | USDX mechanism given (earnings translation, FOMC) and oil/energy weight discussed in §10/§12. S&P and DAX rows are correlation statements ("aligns", "in lockstep"), not mechanisms. Counters are D-2 values (VIX, S&P, USDX) not D-1. |
| 4.3 Synthesis reconciles tensions | 3 | §15/§16/§18 tie short-term (RSI2 100, stretched) to medium-term "transitional" lean and the FOMC; §21a asserts no conflict with §17. The reconciliation is built on the stale close and omits the D-1 session entirely. |
| 4.4 Calibrated language | 4 | §17 is exactly one sentence with a single conditional; H/M confidence stated in §3, §18, §21a. "High" confidence in §21a sits oddly with the report's own "indicative intraday H/L" caveat. |
| 4.5 Card construction (protocol) | 1 | All three cards depart from the fixed M5 rules (detail in the feedback file). Trade 1: market entry not at D-1 close, stop has no 0.25×ATR buffer, no wide-stop flag at R ≈ 1.02×ATR14. Trade 2: regime is TREND_UP but entry/stop use range-style construction (entry P, stop S1.5) not P+0.10×(R1−P) / P−0.8×(P−S1). Trade 3A: entry is not the 57.5% retrace, offers two alternative entries, swing endpoints not logged, stop is not 0.25×ATR beyond the swing-low anchor, and stated R (80) contradicts its own stop distance (170). |
| 4.6 Direction-score derivation traceable | 2 | §21a +0.68 does not reconcile to its listed components (0.64) and the sixth signal is missing (see 3.3). |
| 5.1 Data dated; staleness flagged | 3 | Prices dated in §4/§6; indicative O/H/L flagged. Staleness of the anchor (Fri vs Mon) is flagged in §3 and §19 but is a self-chosen defect, not mitigated. The seven §13a articles carry no publication dates. |
| 5.2 Assumptions up front | 4 | Anchor override stated in §20 and on the Trade 1 card; "lenient-corroboration" instruction stated in §21a; indicative-swing caveat on Trade 3A. Trade 1/Trade 2 do not state that D-1 (Mon 15 Jun) is excluded. |
| 5.3 Red flags surfaced | 3 | FOMC 17 Jun carried to Trade 1 and 3A caveats (not Trade 2). §13d lists "UK CPI (May)" on 16 Jun, which is not in the slice calendar for D (the only GBP row on 16 Jun is a 10-year gilt auction). §13d omits HIGH-impact scheduled rows for D: BoJ rate decision (06:19 broker), RBA rate decision (07:30 broker), BoJ press conference. §13c omits the HIGH US CPI of 10 Jun (y/y 4.2 vs 4.0 consensus) and US PPI of 11 Jun (1.1 vs 1.0). |
| 5.4 Restrictions honoured | 3 | CFD GB100 quote excluded from the build (good); no module codes or bracketed variables seen; FTSE futures used only in a sentiment quote. Weaknesses: Thu close labelled "derived/corrob. via Fri Δ" (a back-derived price counted as corroborated); round indicative O/H/L for 8-11 Jun are presented in a table that feeds the weekly pivots; "Core" label given to non-independent aggregators. No hallucinated-source or restriction-breach override triggered. |

## 3.5 Data comparison (report vs `UK100_by_date/2026-06-16.csv` and slice, cash basis, broker 10:00-18:30)

| Field | Report | Level file / slice (cash) | Δ | Verdict |
|---|---|---|---|---|
| D-1 (15 Jun) close | not stated (anchor 12 Jun 10,471.72 used as "current") | 10,441.2 (full-day 10,415.6) | 30.5 (56.1 full) | FAIL (>15) |
| D-1 session in §6 | absent (rows 8-12 Jun) | 15 Jun: O 10,557.6 H 10,574.6 L 10,422.8 C 10,441.2 | — | missing row |
| Fri 12 Jun C | 10,471.72 | 10,459.5 (full 10,460.9) | 12.2 (10.8) | outside 5 |
| Fri 12 Jun O / H / L | 10,302.68 / 10,471.72 / 10,302.68 | 10,368.9 / 10,473.5 / 10,368.3 | 66.2 / 1.8 / 65.6 | O, L fail |
| Thu 11 Jun O / H / L / C | 10,260 / 10,330 / 10,245 / 10,302.88 | 10,238.9 / 10,373.4 / 10,235.8 / 10,299.9 | 21.1 / 43.4 / 9.2 / 3.0 | O, H fail |
| Wed 10 Jun O / H / L / C | 10,336 / 10,358 / 10,200.21 / 10,254.81 | 10,251.2 / 10,267.5 / 10,126.2 / 10,256.3 | 84.8 / 90.5 / 74.0 / 1.5 | O, H, L fail |
| Tue 9 Jun O / H / L / C | 10,360 / 10,372 / 10,180 / 10,226.80 | 10,353.9 / 10,368.7 / 10,240.5 / 10,240.7 | 6.1 / 3.3 / 60.5 / 13.9 | L fail, C outside 5 |
| Mon 8 Jun O / H / L / C | 10,368.05 / 10,402 / 10,330 / 10,373.10 | 10,309.9 / 10,412.8 / 10,307.1 / 10,370.4 | 58.2 / 10.8 / 22.9 / 2.7 | O, H, L fail |
| RSI2 (Wed / Thu / Fri) | 16.1 / 100 / 100 | 10.74 / 100 / 100 (D-1 15 Jun: 89.71 cash, 52.57 full) | 5.4 / 0 / 0 | arithmetic reproduces from the report's own closes; D-1 value absent |
| ATR14 | ≈118 | 111.04 cash (135.39 full) | 7.0 (17.4) | mild |
| Daily P | 10,415.4 | 10,479.53 (full 10,464.93) | 64.1 (49.5) | FAIL |
| Daily R1 / S1 | 10,528.1 / 10,359.0 | 10,536.27 / 10,384.47 | 8.2 / 25.5 | S1 fail (R1 and full-day S1 match by coincidence of D-2 structure; not credited) |
| Daily R2 / S2 | 10,584.4 / 10,246.3 | 10,631.33 / 10,327.73 | 46.9 / 81.4 | FAIL |
| Daily R3 / S3 | 10,697 (card only) / 10,190.0 | 10,688.07 / 10,232.67 | 8.9 / 42.7 | S3 fail |
| Weekly P / R1 / S1 / R2 / S2 | 10,374.5 / 10,569.0 / 10,277.2 / 10,666.2 / 10,082.8 | W24 10,353.07 / 10,579.93 / 10,232.63 / 10,700.37 / 10,005.77 | 21.4 / 10.9 / 44.6 / 34.2 / 77.0 | FAIL (built from wrong week L 10,180 and H 10,471.72; true week L 10,126.2, H 10,473.5) |
| Monthly pivots | absent | May: P 10,370.4, R1 10,599.6, S1 10,180.8, R2 10,789.2, S2 9,951.6, R3 11,018.4, S3 9,762.0 | — | missing |
| VIX "Friday" | ~17.7 (-9%) | 12 Jun 18.72 (-4.0%); 15 Jun 17.68 | 1.0 | attributed to the wrong session |
| S&P 500 Fri | 7,431.46 (+0.50%) | 7,433.9 (+0.53%) | 2.4 | ok (D-2); D-1 is 7,559.4 (+1.69%) |
| USDX | ~99.3-100.1 | 12 Jun 99.81; 15 Jun 99.68 | — | ok range |

Tolerances per brief §4: close ≤ 5, O/H/L ≤ 10 pts.

## 2. Category roll-up

| Cat | Level | Multiplier | Points (of max) | Justification |
|---|---|---|---|---|
| 1 Prompt adherence | 3 | 0.65 | 13.00 / 20 | Right asset, counters, currency and register; wrong as-of session (D-2 not D-1), wrong window, anchor overridden to 00:00 (disclosed), weak source tiers. Rows 2, 2, 4 = 2.67. |
| 2 Structure | 3 | 0.65 | 13.00 / 20 | All 21 sections present and ordered; scorecard missing source columns, pivots missing R3/S3 symmetry and monthly set, charts not rendered. Rows 5, 2, 3 = 3.33. |
| 3 Accuracy and evidence | 2 | 0.40 | 10.00 / 25 | Internally reproducible pivots/RSI2 but the D-1 close is wrong by 30.5 pts, every pivot tier is stale, O/H/L errors up to 90 pts, several internal contradictions. Rows 3, 2, 3, 2, 1 = 2.2. |
| 4 Reasoning and judgment | 3 | 0.65 | 13.00 / 20 | Pillars conclude and §17 is calibrated, but card construction fails M5 on all three cards and the +0.68 score does not reconcile. Rows 4, 3, 3, 4, 1, 2 = 2.83. |
| 5 Currency, restrictions, transparency | 3 | 0.65 | 9.75 / 15 | Deviations disclosed (anchor, lenient corroboration, indicative flags); articles undated, calendar gaps, derived Thu close counted as corroborated. Rows 3, 4, 3, 3 = 3.25. |

## 3. Total, band, override
- Total = 13.00 + 13.00 + 10.00 + 13.00 + 9.75 = 58.75, rounded **59**.
- Band: **Low** (40-59).
- Override check: no fabricated source established (Investing.com quote is flagged stale-cache and its figures are internally consistent, but see 3.2); no explicit prompt restriction breached (00:00 anchor and lenient-corroboration instruction are logged as instance overrides). `override=none`.

## 4. Card Integrity (linter rows copied verbatim from `qa/ftse_qa1/lint_static/2026-06-16.csv`; separate from the 100)

| card_id | report_date | strategy | flags | dud |
|---|---|---|---|---|
| 2026-06-16_Trade_1 | 2026-06-16 | Trade 1 — Daily Directional (LONG · TREND_UP regime) | CLEAN | False |
| 2026-06-16_Trade_2 | 2026-06-16 | Trade 2 — Pivot (regime-aware, TREND_UP → buy-the-dip to support) | CLEAN | False |
| 2026-06-16_Trade_3A | 2026-06-16 | Trade 3A — Momentum-Pullback (complex, TREND_UP fork) | CLEAN | False |

Per card: 100 / 100 / 100. Report-level Card Integrity = mean = **100**; n_cards = 3, n_duds = 0, n_warns = 0.

Note: the static linter uses no market data, so CLEAN means only that stop side, TP order and R size are internally coherent. It does not test entry-versus-D-1-close, pivot provenance or M5 construction; those defects are scored under C4 row 4.5 and listed in the feedback file.

## 5. Feedback
See `qa/ftse_qa1/2026-06-16_feedback.md`.
