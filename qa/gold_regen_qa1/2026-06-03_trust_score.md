# Trust Score — XAUUSD Gold Report, 3 June 2026 (`Gold_Report_03Jun2026.md`)
Run: `gold_regen_qa1` · Reviewer session (Stage 1, QA-only)

`last_bar_date` in `data/levels/XAUUSD_by_date/2026-06-03.csv` = 2026-06-02, which is < D (2026-06-03) — leak-free confirmed before use.

## 1. Section 7 checklist

| Row | Notes | Evidence | Score |
|---|---|---|---|
| 1.1 Variables respected | Asset/LBMA framing, USDX-first counter, 5d/25d lookback, USD/oz, 6 sources all correct. But **as-of is wrong**: §2 declares "Snapshot close 1 June 2026," yet the last completed session strictly before D is 2 June 2026 (level file `last_bar_date`=2026-06-02). §6 never carries a 2 June OHLC/RSI2 row; 2 June appears only as intraday "live" quotes. Tick size (implied $0.01/tick) is never stated explicitly. | §2, §6, §20 | 2 |
| 1.2 Coverage & currency consistent | Dates used (26 May–1 Jun) are technically ≤ D−1, so no literal date-drift, but the true D−1 session is skipped entirely — a coverage gap, not a currency-unit issue (units are consistent throughout). | §2, §6, §11 | 2 |
| 1.3 Audience & tone | Institutional Senior-Commodities-Analyst register held throughout; no retail tone. | §1, §18 | 5 |
| **C1 checklist mean** | (2+2+5)/3 = 3.0 → **3**, then **restriction-breach override drops it ≥1 level → 2** | | **2** |
| 2.1 Sections present & ordered | All of §1–§21 present in order, incl. 13a–d and 21a–d. | headings | 5 |
| 2.2 Scorecard/pivot tables | §6 is a proper table. §11 daily/weekly tables use 5 levels each side (R5→S5) instead of the specified 3 (R3→P→S3); the monthly pivots are given as an inline sentence, not a table at all. | §11 | 2 |
| 2.3 Method steps visible | §4–§5 show observation→consensus; §8 is candle-by-candle; §9 has regime/persistence/overlap/VOLator; chart captions present (accepted per brief — conversion artefact, not scored). | §4–§9 | 5 |
| **C2 checklist mean** | (5+2+5)/3 = 4.0 | | **4** |
| 3.1 Quantitative claims sourced | §1/§12/§14 mostly point to §4/§6/§13; the "58–60%" hike-probability range is only sourced to a "58%" quote in §13a — the 60% upper bound is unsourced. | text | 3 |
| 3.2 Citations exist & contain data | 6 named, dated sources; 3 spot-checked (JM Bullion, TradingEconomics, Reuters/CNBC) are internally consistent, no fabrication. One mischaracterisation: §1 calls the 2 Jun $4,503 print "early... dealing" though JM Bullion (§4) times it 16:46 EDT. | §4, §13a | 4 |
| 3.3 Calculations transparent | RSI2 (53.6, 1 Jun) **does** reproduce from the report's own 5 closes (verified: avg gain 22.17 / avg loss 19.175 → RS 1.156 → RSI 53.6). But ATR14 is never stated as a labelled figure anywhere — only back-solvable from the 3×ATR cap ($4,207.91); §21a's direction score says "three highest-weighted... signals" but lists four terms. | §6, §21a | 2 |
| 3.4 Numbers reconcile incl. vs level file | Internal reconciliation (D−1 close consistent across §1/§3/§4/§6) is fine, but **external reconciliation fails materially**: close diff $12.96 (full) / $12.97 (cash) both exceed the $11.67 / $9.31 fail thresholds; daily pivots P, R3, S1, S2, S3 all exceed the $11.67 fail threshold (only R1 passes by coincidence, R2 is in the discrepancy band); the MARKET entry ($4,500.92) does not equal the true D−1 close; RSI2 for the true D−1 is never computed at all (true rsi2_full=5.45, deeply oversold, vs. the neutral 53.6 the report treats as current). Weekly/monthly pivots do reconcile (diffs ≤$0.6). | §6, §11, §21b, level file | 1 |
| **C3 checklist mean** | (3+4+2+1)/4 = 2.5 → framework §3 intro directs "material methodology gaps... should collapse a score"; 3.4's failure is material (misdated entry, 5 of 7 checkable daily-pivot tiers fail) → rounds to **2**, not 3 | | **2** |
| 4.1 Pillars conclude | §8/§9/§10/§12/§14 each end in a direction label consistent with their own content. | those sections | 5 |
| 4.2 Peer/cross-asset interpreted | §10 gives mechanism (real-rate/USD channel, risk-on reducing safe-haven demand), not a bare correlation list. | §10 | 5 |
| 4.3 Synthesis reconciles tensions | §9 explicitly reconciles KER (trend-down) vs. the Transition regime label; §13b explicitly reconciles structural (+0.13) vs. near-term (−0.27) sentiment; §21a flags conviction as marginal. | §9, §13b, §21a | 5 |
| 4.4 Calibrated language + card construction (also scored here per brief) | §17 is one calibrated sentence; confidence stated Medium (§3/§18). But the card-construction rule for Trade 1's Unit-3 stop is violated: brief §3 fixes "Unit 3 stop → entry ± 0.2R in the profitable direction (for a SHORT that is below entry)"; the report's card and management text both say "entry **+**0.2R" ($4,512.56 — above entry, the *losing* direction for a short), not entry −0.2R ($4,489.28). | §21b | 3 |
| **C4 checklist mean** | (5+5+5+3)/4 = 4.5 → **4** (the card-construction defect is real but isolated to one field on one card, against otherwise excellent reasoning) | | **4** |
| 5.1 Data dated; staleness flagged | Individual prices/articles are dated, but the core staleness — that a more recent completed session (2 Jun) exists and is not used as the OHLC/RSI2 basis — is never flagged; it is instead described as "early... dealing," which obscures rather than surfaces the gap. | §1, §6, §19 | 1 |
| 5.2 Assumptions up front | Futures-to-spot normalisation correctly stated as "none required" (no futures actually used as evidence). But the daily-open-anchor override is never given its converted clock time in the report body (only "session open") — brief requires "the same converted time on the card, in the handoff record and in the report body." | §19, §20, §21b | 2 |
| 5.3 Red flags surfaced | §12/§15 risks reasonably surfaced; §13d jobs-report collision is carried into the Trade 1 caveats. | §12, §15, §21b | 4 |
| 5.4 Restrictions honoured | **Breached.** §20 (report body) writes the reserved module token "DAILY_OPEN_ANCHOR" verbatim, and separately writes "M5 trace:" — both are explicitly barred by checklist 5.4 ("no bracketed variable names, no module codes (M1..M5)... in the report body"). | §20 | 0 |
| **C5 checklist mean** | (1+2+4+0)/4 = 1.75 → **2** | | **2** |

## 2. Category roll-up

| Cat | Level | Multiplier | Max | Points | One-line justification |
|---|---|---|---|---|---|
| C1 Prompt adherence | 2 | 0.40 | 20 | 8.0 | As-of variable wrong by one full session (skips the true D−1 close entirely); checklist mean 3, dropped 1 level by the restriction-breach override |
| C2 Structure | 4 | 0.85 | 20 | 17.0 | All sections present/ordered; pivot tables over-built (5 levels vs. spec'd 3) and monthly pivots not tabulated at all |
| C3 Accuracy & evidence | 2 | 0.40 | 25 | 10.0 | Close and most daily-pivot tiers fail the level-file tolerance; MARKET entry ≠ true D−1 close; true D−1 RSI2 never computed; sourcing/citation mechanics themselves are otherwise sound |
| C4 Reasoning & judgment | 4 | 0.85 | 20 | 17.0 | Pillars, cross-asset mechanism and synthesis are all strong; one concrete card-construction rule violation (Unit-3 stop sign) pulls it down one level |
| C5 Currency & transparency | 2 | 0.40 | 15 | 6.0 | Staleness of the true D−1 session is not flagged; anchor-override clock time omitted; a stated restriction (no module codes in body) is openly breached |

**Total = 8.0 + 17.0 + 10.0 + 17.0 + 6.0 = 58 → rounded 58**

## 3. Total, band, override

- **total = 58**
- **band = Low Trust (40–59)**
- **override = restriction_breach** — §20 names "DAILY_OPEN_ANCHOR" and "M5 trace:" in the report body, breaching checklist 5.4. Per framework §6 this caps the report at Moderate Trust (60–74) and drops C1 ≥1 level; C1 was already dropped to 2 above. The cap is **non-binding** here: the raw weighted total (58) already sits below the 60–74 Moderate band, so the override does not raise the band — it is recorded as the reason C1 was reduced, and because a restriction breach occurred at all.
- No hallucinated source was found (all three spot-checked citations are named, dated, and internally consistent) — override is restriction_breach only, not hallucinated_source.

```
c1=2
c2=4
c3=2
c4=4
c5=2
total=58
band=Low Trust
override=restriction_breach
card_integrity=100
n_cards=3
n_duds=0
n_warns=0
```

## 4. Card Integrity (linter rows, copied verbatim from `qa/gold_regen_qa1/lint_static/2026-06-03.csv`)

| card_id | strategy | flags | dud | card score |
|---|---|---|---|---|
| 2026-06-03_Trade_1 | Trade 1 - Daily Directional (SHORT) | CLEAN | False | 100 |
| 2026-06-03_Trade_2 | Trade 2 - Pivot (TRANSITION) | SUPPRESSED | False | — (suppressed, excluded from mean) |
| 2026-06-03_Trade_3C | Trade 3C - Momentum-Breakout | SUPPRESSED | False | — (suppressed, excluded from mean) |

Card Integrity (report level) = mean over non-suppressed cards = **100** (n_cards=3 total rows, n_duds=0, n_warns=0). This is unchanged from the linter and is copied verbatim per instructions — it does not capture the market-relative defects (Trade 1 entry ≠ true D−1 close; Unit-3 stop sign) found in this review, which are static-integrity-adjacent but outside the linter's leak-free static-mode checks (stop side / TP1 side / TP2 order / zero R / TP3 order / R-size / target-far / duplicate). Those are recorded in `2026-06-03_feedback.md` instead.

## 5. Feedback
See `qa/gold_regen_qa1/2026-06-03_feedback.md`.
