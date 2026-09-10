# Trust Score — Gold_Report_29Jun2026.md (D = 2026-06-29) — run gold_regen_qa1

Framework v3.7, mapped via `docs/QA_PROTOCOL_TRADE_CARDS.md`. Leak-free reference:
`data/levels/XAUUSD_by_date/2026-06-29.csv` (`last_bar_date`=2026-06-26 < D=2026-06-29 — verified leak-free).

## 1. Section 7 checklist

| Row | Notes | Evidence | Score |
|---|---|---|---|
| 1.1 Variables respected | Asset correctly XAU/USD spot, loco-London, futures corroboration-only (§2, §4–5). USDX first counter in §10 ✓. As-of = D-1 (26 Jun) ✓. Lookback 5/25 ✓. USD/oz ✓. 6 rows in §4, but only 5 distinct vendors (Investing.com appears twice) — marginally short of "≥6 independent sources". Tick name/size never stated as its own field in §2 (ticks appear only inside §21 card arithmetic, e.g. "6,200 ticks", implying 1 tick=$0.01, never declared). Daily-open anchor named (07:00 UK) but framed as "has been set… for this run" (§2), which is the exact phrasing `M1_Variables_v2_1.md` forbids for a fixed instance parameter — no non-conformance is logged anywhere for it. | §2, §4, §10, §20 | 3 |
| 1.2 Coverage/currency consistent | No date or unit drift found; USD/oz used throughout; D-1=26 Jun and D=29 Jun consistent everywhere checked. | whole report | 5 |
| 1.3 Audience & tone | Institutional register throughout ("Senior Commodities Analyst" register implied by §18/§1 tone), no retail language. | §1, §18 | 5 |
| 2.1 Sections present/ordered | All 21 sections (§1–§21 incl. 13a–d, 21a–d) present, correctly ordered, headed. | headings | 5 |
| 2.2 Scorecard as table | §6 is a proper OHLC+RSI2 table with Validation column; §11 pivot tables are real tables, but carry 5 levels/side (R5→S5) rather than the brief's specified 3 (R3→S3) — extra content, not missing, but a spec deviation. | §6, §11 | 4 |
| 2.3 Method steps visible | §4→§5 shows observation→normalisation→consensus with the vendor-cluster logic stated; §8 is candle-by-candle; §9 gives regime + persistence/overlap/VOLator + KER; charts present as captions (accepted per brief, docx→md image loss). | §4–§9 | 5 |
| 3.1 Quantitative claims sourced | Most §1/§12/§14 figures point to §4/§6/§13/named releases (Fed dot plot, PCE/BEA, ICE/Investing.com). But the headline D-1 close/high and all pivots, which anchor most of the report, are traceable to a source (Investing.com) that itself proves materially wrong against the leak-free execution series (row 3.4) — a factual-accuracy failure, not just a sourcing-format one. §14's "US 10-year near 4.37%" carries no explicit source. | text | 2 |
| 3.2 Citations exist & consistent | Three-citation spot-check (FXStreet 24 Jun, Forex.com 26 Jun, Phemex/institutional survey): all named, quote a figure used consistently, no self-contradiction found. No fabrication detected. Institutional-survey citation is undated beyond "Jun" (weak but not fabricated). | §4, §13a | 3 |
| 3.3 Calculations transparent | RSI2 for 26 Jun (71.2) **reproduces exactly** from the report's own 5 stated closes (recomputed 71.15≈71.2 — see feedback). Daily P=(H+L+C)/3 also reproduces from the report's own §6 row (4,007.31≈4,007). ATR14/KER given as headline numbers without a shown derivation. | §6, §11, §9, §21a | 4 |
| 3.4 Numbers reconcile (incl. level file) | Internally consistent (D-1 close identical in §1/§3/§4/§6/§21b). **Externally: fails hard against `XAUUSD_by_date/2026-06-29.csv`.** Close off $72.23 (0.589×ATR14_full), High off $66.44 (0.542×ATR), Open off $14.20 (0.116×ATR, discrepancy band), Daily P off $46.48 (0.379×ATR), Daily R1–R3/S1–S3 all off $25–$159, Weekly P off $134.01, RSI2 off 28.8 pts. Only the Low (report $3,983.32 vs file $3,983.14, Δ$0.18) and ATR14 itself (report 112 vs file 122.67/103.40, both within ~10%) reconcile. This is a hard Category-3 failure on the report's primary accuracy test. | cross-section + level file | 0 |
| 4.1 Pillars conclude | §8, §9, §10, §12, §14 each end in a direction label consistent with their own content. | those sections | 5 |
| 4.2 Peer/cross-asset interpreted | §10 gives an explicit mechanism per counter (USDX denominator effect, real-yield override of the equity safe-haven channel, silver sector confirmation) — interpreted, not listed. | §10 | 5 |
| 4.3 Synthesis reconciles tensions | §15/§16/§18 explicitly carry the §10 S&P-gold contradiction forward rather than silently resolving it; KER vs regime agree and are stated as agreeing; §17 vs §21a point the same way. | §15–§18, §21a | 4 |
| 4.4 Calibrated language | §17 is one sentence; confidence stated Medium with reason; "likely/may" language used appropriately elsewhere. | §3, §17 | 4 |
| — Card construction (feeds Category 4 per brief §"Card anchors") | Trade 1/Trade 2 construction is mechanically clean (matches linter CLEAN/no-DUD). **Trade 3A violates the fixed M5 rule**: entry should be the 57.5% retrace of the qualifying swing (M5 spec); the card instead computes and labels a "38.2% retrace" — and even that computation is wrong by its own numbers (see feedback #3). TP2/TP3 are also mislabelled against the fixed 38.2%/0%/100%+ scheme. | §21b, card notes | 2 |
| 5.1 Data dated; staleness flagged | Every §4/§6/§13 row carries a date; monthly pivot tier explicitly flagged indicative (partial-month proxy) and excluded from entries — good practice. | §4, §6, §13, §19 | 4 |
| 5.2 Assumptions up front | Futures-to-spot normalisation and cluster-selection logic stated (§5); cross-vendor divergence stated with size (§19). **Gap:** the daily-open-anchor selection (07:00 UK) is never framed as a fixed, logged instance parameter or non-conformance — it reads as a per-run choice, which `M1_Variables_v2_1.md` explicitly prohibits presenting as the anchor without logging. | §21b, §19, §20 | 3 |
| 5.3 Red flags surfaced | §12/§15 surface exhaustion risk, event collision (30 Jun JOLTS/PMI), and the S&P-gold contradiction; §13d event collisions carried into card caveats (§21b). | §12, §15, §21b | 5 |
| 5.4 Restrictions honoured | No bracketed variable names or module codes (M1..M5) or framework name found in the body; retail FX-broker quotes explicitly excluded (§5); futures used corroboration-only; common instrument names used throughout. | whole report | 5 |

## 2. Category roll-up

| Cat | Rows (mean) | Level (0–5) | Multiplier | Max | Points | Justification |
|---|---|---|---|---|---|---|
| C1 Prompt adherence | (3+5+5)/3=4.33 | **4** | 0.85 | 20 | 17.00 | All variables addressed; source-independence and anchor-framing gaps keep it off 5. |
| C2 Structure | (5+4+5)/3=4.67 | **5** | 1.00 | 20 | 20.00 | All 21 sections present, correctly ordered; scorecard/pivots are real tables. |
| C3 Accuracy & evidence | (2+3+4+0)/4=2.25 | **2** | 0.40 | 25 | 10.00 | Formal sourcing/transparency adequate, but the D-1 OHLC, RSI2, and daily/weekly pivots fail hard against the leak-free level file. |
| C4 Reasoning & judgment | (5+5+4+4+card2)/5=4.0 | **4** | 0.85 | 20 | 17.00 | Pillars/synthesis strong; Trade 3A's fixed-rule (57.5%) violation and internal fib arithmetic error pull this off 5. |
| C5 Currency/transparency | (4+3+5+5)/4=4.25 | **4** | 0.85 | 15 | 12.75 | Dating, red-flag surfacing and restriction handling strong; anchor-logging gap keeps it off 5. |

**Total = 17.00+20.00+10.00+17.00+12.75 = 76.75 → 77 / 100**

## 3. Band and override

- **Band: High Trust (75–89).**
- **Override check:** No fabricated/hallucinated source identified on spot-check (3 citations verified named, dated, internally consistent) → hallucinated_source override does NOT apply. No explicit prompt restriction openly breached (no bracket vars/module codes, futures corroboration-only honoured, retail quotes excluded) → restriction_breach override does NOT apply.
- **override = none**

## 4. Card Integrity (linter rows, copied verbatim from `qa/gold_regen_qa1/lint_static/2026-06-29.csv`)

| card_id | strategy | flags | dud | card score |
|---|---|---|---|---|
| 2026-06-29_Trade_1 | Trade 1 - Daily Directional (SHORT) | CLEAN | False | 100 |
| 2026-06-29_Trade_2 | Trade 2 - Pivot, Trend-Following (SHORT) | CLEAN | False | 100 |
| 2026-06-29_Trade_3A | Trade 3A - Momentum-Pullback (SHORT) | CLEAN | False | 100 |

`card_integrity = 100 − 40·(#DUD) − 10·(#WARN)` per card, floored at 0; report level = mean over non-suppressed cards = **100**.
Note: the linter is a *static integrity* check (stop side, TP ordering, R sizing) and does not check fib-retracement arithmetic — it correctly reports Trade 3A as CLEAN on those static rules even though the card fails the M5 retracement-percentage rule (see checklist "Card construction" row and feedback #3). Card Integrity is copied verbatim and not re-derived.

## 5. Summary line

```
c1=4
c2=5
c3=2
c4=4
c5=4
total=77
band=High Trust
override=none
card_integrity=100
n_cards=3
n_duds=0
n_warns=0
```

See `qa/gold_regen_qa1/2026-06-29_feedback.md` for numbered, actionable feedback.
