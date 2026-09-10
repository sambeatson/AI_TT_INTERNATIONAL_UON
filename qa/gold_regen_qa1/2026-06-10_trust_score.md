# Trust Score — Gold_Report_10-Jun-2026.md (D = 2026-06-10, XAUUSD)

Reviewer basis: `docs/AI_Output_Trust_Score_Framework_v3.7.txt` §4–7, `docs/QA_PROTOCOL_TRADE_CARDS.md`,
`qa/gold_regen_qa1/REVIEWER_BRIEF.md`. Level file used: `data/levels/XAUUSD_by_date/2026-06-10.csv`
(`last_bar_date=2026-06-09 < 2026-06-10`, checked OK). Report claims a spot/loco-London continuous
basis (§2), so `_full` columns are the primary comparator; `_cash` is noted where materially different.

## 1. Section 7 checklist

| Item | Notes | Evidence | Score | Action if below threshold |
|---|---|---|---|---|
| 1.1 Variables respected | Asset/basis, USDX-first, as-of D−1, 5d/25d lookback, USD/oz, ≥6 sources all correct. Tick size/name is never stated anywhere despite §21 being produced (M1 makes it mandatory in that case); ticks used in cards imply 1 tick=$0.01 but this is never declared. §2 also claims "CME front-month (GC) used for corroboration" but no GC/futures row appears anywhere in §4 and §5 explicitly says no futures were blended. | §2, §4, §5, §21b | 3 | List: tick size/name absent; §2/§5 futures-corroboration contradiction |
| 1.2 Coverage & currency consistent | Every date is D−1 or earlier for data, D for the session; no USD/oz–tick unit drift. | whole report | 5 | — |
| 1.3 Audience & tone | Institutional Senior Commodities Analyst register throughout, no retail tone. | §1, §18 | 5 | — |
| 2.1 Sections present & ordered | All 21 sections present, correctly ordered, with 13a–d and 21a–d subsections. | headings | 5 | — |
| 2.2 Scorecard as table | §6 is a proper table; §11 pivot tables follow the brief's R3→P→S3 mapping for daily/weekly/monthly. | §6, §11 | 5 | — |
| 2.3 Method steps visible | §4–5 show observation→normalization→consensus. But §9 never states ATR(14) as an explicit number (M4 §9 requires it to "appear here explicitly... not left to be inferred from a buffer or a cap") — it must be back-solved from the §21b TP3 cap. §6 also omits the required RSI2 "working" line beneath the table. | §6, §9 | 2 | Identify missing pillar content: ATR14 not stated in §9; RSI2 arithmetic not shown under §6 |
| 3.1 Quantitative claims sourced | Most §1/§12/§14 claims trace to §4/§6/§13. A few do not: §12's "70–75% chance of a year-end hike" has no direct citation or cross-reference; §14's "technical screens (Investing.com) read 'Strong Sell'" is a new claim on a source already used only for price in §4; the "~nine-week high" DXY read in §1 is more precise than its §4 source ("multi-month high") supports. | §1, §12, §14 | 3 | Flag unsourced claims: 70–75% hike odds, Investing.com "Strong Sell" screen, "nine-week" DXY framing |
| 3.2 Citations exist & contain data | Spot-check of 3 (TradingKey NFP, FXEmpire, forex.com): first two are internally consistent with figures used elsewhere. The forex.com §4 row is muddled — its raw quote is dated 6 Jun ("close <4,319") but its Normalized column carries a 5 Jun value ($4,375), mixing two sessions in one row. Not fabricated, but not clean. | §4, §13a | 3 | Rebuild the forex.com evidence row so raw quote and normalized value share one date |
| 3.3 Calculations transparent | §21a direction score (−0.25−0.20−0.05−0.15−0.07−0.15=−0.87) and Trade 3A's fib math (57.5%/38.2%/0% of the $4,268→$4,471 swing) all reproduce exactly. But Trade 1's stated stop ($4,368 = 9 Jun high $4,363 + "0.25×ATR buffer") does not reproduce: the buffer actually applied is $5, not 0.25×ATR under either the report's own implied ATR (~$62, which would need a ~$15.50 buffer) or the level file's true ATR14. RSI2 working also not shown (see 2.3). | §21a, §21b, §6 | 2 | Request derivation rebuild for Trade 1 stop buffer |
| 3.4 Numbers reconcile — incl. against level file | Internal reconciliation is clean (the $4,288–4,290 consensus/close/entry figure is identical across §1, §3, §4-implied, §6 and §21b MARKET entry). External reconciliation against `XAUUSD_by_date/2026-06-10.csv` fails broadly and by large margins: D−1 low, D−1 close, ATR14, and almost every daily/weekly/monthly pivot level are outside the framework's Category-3-failure tolerance (see §2 below for figures). This is the primary accuracy test for this run and it fails on the majority of checkable numbers. | level file cross-check | 1 | Identify reconciliation breaks: D−1 low/close, ATR14, daily/weekly/monthly pivots (see feedback file) |
| 4.1 Pillars conclude | §8, §9, §10, §12, §14 each end in a direction label consistent with their content. | those sections | 4 | — |
| 4.2 Peer/cross-asset interpreted | §10 states a transmission mechanism per counter, not a bare correlation list. | §10 | 5 | — |
| 4.3 Synthesis reconciles tensions | §15/§16/§18 address the oversold-bounce-risk vs. bearish-base-case tension and cross-check §17 vs §21a explicitly (§20 "Conflict check"); KER and regime agree so there is little genuine tension to reconcile there. | §15–§18, §21a | 4 | — |
| 4.4 Calibrated language | §17 is one sentence, no hedge stacking; Medium confidence stated in §3/§18. | §3, §17 | 5 | — |
| 5.1 Data dated; staleness flagged | Every price/article dated; the 9 Jun close and all pivot tiers are explicitly flagged indicative. | §4, §6, §11, §19 | 5 | — |
| 5.2 Assumptions up front | Anchor override stated on the card and in §20; single-source pivot propagation into cards stated. The §2 futures-corroboration claim is never substantiated with a stated normalization size (see 1.1). | §19, §20, §21b | 4 | Surface what the claimed GC corroboration actually was, or remove the claim |
| 5.3 Red flags surfaced | §12/§15 carry the risks; the CPI collision is carried into the Trade 1 caveats. | §12, §15, §21b | 5 | — |
| 5.4 Restrictions honoured | No bracketed variable names, module codes or framework name anywhere in the body (confirmed by scan). Common instrument names used throughout. No retail-broker quotes blended. | whole report | 5 | — |

## 2. Category roll-up

| # | Category | Max | Row mean | Level | Multiplier | Points | Justification |
|---|---|---|---|---|---|---|---|
| 1 | Prompt adherence | 20 | (3+5+5)/3=4.33 | 4 | 0.85 | 17 | All Variables respected but tick size/name never stated; §2/§5 futures-corroboration contradiction |
| 2 | Structural alignment | 20 | (5+5+2)/3=4.0 | 4 | 0.85 | 17 | Full section set, correctly ordered, real tables — but §9 omits the mandatory explicit ATR14 figure and §6 omits the mandatory RSI2 working line |
| 3 | Accuracy & evidence | 25 | (3+3+2+1)/4=2.25 | 2 | 0.40 | 10 | Internally consistent, but D−1 low/close, ATR14 and almost all daily/weekly/monthly pivots fail external reconciliation against the level file by wide margins; one card's stop arithmetic does not reproduce |
| 4 | Reasoning & judgment | 20 | (4+5+4+5)/4=4.5→4 | 4 | 0.85 | 17 | Pillars conclude, cross-asset is interpreted, synthesis reconciles the main tension — but Trade 1's stop-buffer arithmetic error and the resulting mis-applied "wide stop" flag are a concrete card-construction defect |
| 5 | Currency & transparency | 15 | (5+4+5+5)/4=4.75→5 | 5 | 1.00 | 15 | Dating, staleness flags, red flags and restrictions are all clean; only the unsubstantiated futures-corroboration claim is a minor gap |

## 3. Total, band, override

- **Total = 17+17+10+17+15 = 76**
- **Band = High Trust (75–89)**
- **Override check:** No fabricated/hallucinated source found on spot-check (§3.2) → no hallucination override. No bracketed variable, module code or framework name found anywhere in the body (grep-confirmed) and no other prompt restriction is openly breached → no restriction-breach override.

```
c1=4
c2=4
c3=2
c4=4
c5=5
total=76
band=High Trust
override=none
card_integrity=100
n_cards=3
n_duds=0
n_warns=0
```

## 4. Card Integrity (linter rows, copied verbatim from `qa/gold_regen_qa1/lint_static/2026-06-10.csv`)

| card_id | strategy | flags | dud | per-card score |
|---|---|---|---|---|
| 2026-06-10_Trade_1 | Trade 1 - Daily Directional (SHORT) | CLEAN | False | 100 |
| 2026-06-10_Trade_2 | Trade 2 - Pivot (TREND_DOWN) | SUPPRESSED | False | excluded from mean |
| 2026-06-10_Trade_3A | Trade 3A - Momentum-Pullback (SHORT) | CLEAN | False | 100 |

Report-level Card Integrity = mean over non-suppressed cards = mean(100, 100) = **100**. n_cards=3, n_duds=0, n_warns=0. (Card Integrity is a static-linter score and does not capture the Trade 1 stop-buffer arithmetic error noted under 3.3/4 above, which the static linter's DUD/WARN rules do not test.)
