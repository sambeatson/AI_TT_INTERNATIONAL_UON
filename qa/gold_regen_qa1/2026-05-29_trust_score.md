# Trust Score — XAUUSD Gold Daily Report, 29 May 2026

Run: `gold_regen_qa1` · Report: `reports/md/Gold_Daily_Report_29May2026.md` · D = 2026-05-29
Level file: `data/levels/XAUUSD_by_date/2026-05-29.csv` (last_bar_date = 2026-05-28 < D — leak-free, verified)
Basis claimed by report: "Spot, immediate settlement (loco London)" / "Global, 24-hour OTC market" → checked against `_full` columns (weekday cash-session columns given for comparison where relevant).

## 1. Section 7 checklist

| Item | Notes | Evidence | Score | Action |
|---|---|---|---|---|
| 1.1 Variables respected | Asset correctly labelled spot loco-London, not COMEX (GC=F named "for corroboration" only, per rule) — but GC=F is never actually used anywhere in §4/§5/§20, an unused/undelivered declaration. USDX is first counter (§10) ✓. ≥6 sources in §4 ✓. USD/oz ✓. **[TICK_SIZE]/[TICK_NAME] are never stated in §2** even though §21 produces strategy cards (M1_Variables: required whenever strategy recs = YES) — only inferable from the tick math buried in the cards. Most seriously: **AS_OF_DATE was not a completed prior session.** §19/§20 admit the 28-May session "was still in progress at data extraction," yet its snapshot O/H/L/C is used as the validated D−1 basis throughout §1/§3/§4/§6/§11/§21 — this contradicts M1_Variables' AS_OF_DATE definition ("the last completed regular session... strictly before the report date... not the date the run was executed") and is the root cause of the Category-3 failures below. | §2, §6, §19, §20 | 2 | List: (a) add Tick size/Tick name to §2; (b) do not present an in-progress session's data as the validated as-of basis — defer to the last confirmed-complete session or clearly re-derive once the session closes |
| 1.2 Coverage & currency consistent | All dates ≤ 28 May, none after D. USD/oz used throughout; native units (ticks) added on cards, both stated per card rule. No unit drift found. | whole report | 4 | — |
| 1.3 Audience & tone | "Senior Commodities Analyst — Precious Metals" stated in header; institutional tone throughout, no retail language. | §1 header, §18 | 5 | — |
| 2.1 Sections present & ordered | All of §1–§21 present in the required order, including §13a–d and §21a–d. | headings | 5 | — |
| 2.2 Scorecard as a table | §6 is a table but combines "Source A/Source B" into one "Sources" column and adds an unspecified "Trend" column instead. §11 pivot tables are ordered R3→P→S3, three-plus levels each side, for daily/weekly/monthly as required. | §6, §11 | 4 | Split §6's Sources column into Source A / Source B to match spec |
| 2.3 Method steps visible | §4→§5 show observation→normalisation→consensus; consensus method (weighted median) stated. §2 declares a futures-to-spot normalisation source (GC=F) that is never actually exercised — no futures figure appears anywhere to normalise. §8 is candle-by-candle; §9 covers persistence/overlap/VOLator; §7 chart captions present (image drop from docx→md conversion, not scored per brief). | §4–§9 | 4 | Either use GC=F with a stated contango adjustment, or drop the "used for corroboration" claim from §2 |
| 3.1 Every quantitative claim sourced | §1/§12/§14 figures mostly point to §3/§4/§13/§21. §14's "≈50% odds of a Fed hike by December" has no explicit pointer. | text | 4 | Add a source pointer for the Fed-hike-odds figure in §14 |
| 3.2 Citations exist & contain data | Spot-checked Reuters, Investing.com, USAGOLD (all named/dated 28 May, used consistently with their own classification in §13a). Minor tension: USAGOLD is quoted at 4,444.74 (−0.42%) in §4 but classified "Neutral"/dip-buying in §13a for the same date — not impossible or self-contradictory, so no fabrication trigger, but a soft inconsistency. | §4, §13a | 4 | Reconcile USAGOLD's quantitative move with its qualitative "Neutral" tag or explain the divergence |
| 3.3 Calculations transparent | RSI2 method (period 2, Wilder) and ATR(14)/KER method stated in §20. Pivot formula itself (P/R/S from H,L,C) is not restated in the report body, only results are tabled. | §6, §11, §20 | 3 | State the pivot formula once (even a footnote) alongside §11 |
| 3.4 Numbers reconcile — internally AND against the level file | **Internally consistent**: D−1 close (4,404.2) identical across §1/§3/§4/§6/§21b MARKET entry; §11 pivots reproduce exactly from the report's own stated H/L/C (P=(4465.4+4366.8+4404.2)/3=4,412.1 ≈ table's 4,412.2); Trade 2's entry/stop reproduce from the report's own P/S1/R1. **Externally, against the level file, reconciliation fails almost across the board**: D−1 close off by 91.5 (0.90×ATR14_full, fail threshold is 0.115×ATR≈11.75); RSI2 off by 38.4 pts (fail >15); High off by 51.2 (fail, >0.20×ATR≈20.4); daily/weekly/monthly pivots fail on 12 of 17 checkable levels (only Open, Low, ATR14, daily S2, weekly S1 land in/near tolerance — apparently by coincidence, since the underlying H/L/C used to derive them is wrong). See §4 checklist below for the numbers. | cross-section + level file | 1 | See feedback file — re-source the true 28-May O/H/L/C/close and rebuild §6/§11/§21 from it |
| 4.1 Pillars conclude | §8, §9, §10, §12 each end in a direction label. §14 ends on tone but no explicit bolded label like §12's. | those sections | 4 | Add an explicit direction label to close §14 |
| 4.2 Peer/cross-asset interpreted | §10 gives mechanisms (USDX→cost of carry, equity risk-off vs rate channel), not a bare correlation list; the MIXED read is explained, not suppressed. | §10 | 5 | — |
| 4.3 Synthesis reconciles tensions | §15/§16/§18 explicitly address RSI2-oversold vs trend-continuation and the cross-asset MIXED signal; §17 does not conflict with §21a. | §15–§18, §21a | 4 | — |
| 4.4 Calibrated language | §17 is exactly one sentence, no hedge stacking; confidence (Medium) stated in §3/§18. | §3, §17 | 5 | — |
| 5.1 Data dated; staleness flagged | Every price/article carries a date; the in-progress 28-May session is explicitly flagged in §19 ("still in progress at data extraction"). Good disclosure practice — but see 1.1/3.4: the flag does not stop the snapshot being labelled "CORROB." in §6 and used as the validated close everywhere downstream. | §4, §6, §19 | 4 | Do not mark a session-to-date figure "CORROB." for the close field — use "indicative (session in progress)" instead |
| 5.2 Assumptions up front | No futures normalisation was needed (all sources already spot) and this is stated in §5. The daily-open-anchor override IS stated on the Trade 1 card and in §21a, but is **absent from §20 Agent Log**, where the brief/M1_Variables require it to also appear. Monthly single-source pivots are correctly excluded from anchoring any card. | §21b, §19, §20 | 3 | Add one line to §20 recording the 07:00 UK anchor override (vs the 00:00 UK populated default) |
| 5.3 Red flags surfaced | §12/§15 carry the broken-4,500-floor and hawkish-Fed risks. §13d's highest-impact upcoming event (Thu PCE/Q1 GDP) is **not** carried into any card's caveats — Trade 1/2 caveats mention only wide-stop/cross-asset-MIXED, not the scheduled-event collision. | §12, §15, §21b | 3 | Add a PCE/GDP-release caveat to Trade 1 and Trade 2 |
| 5.4 Restrictions honoured | No bracketed variable text found; instrument common names used correctly; no synthesis claimed and no contrary evidence found. **Breach**: the §11 pivot table's Status column names the module code **"M5-derived"** twice (R1.5 and S1.5 rows) — a literal module-code exposure in the report body, forbidden outright by row 5.4. | §11 (Status column, R1.5 and S1.5 rows) | 1 | Replace "M5-derived" with a plain-English label (e.g. "half-level, supplementary") in both cells |

## 2. Category roll-up

| Cat | Rows averaged | Mean → level | Multiplier | Max | Points | Justification |
|---|---|---|---|---|---|---|
| C1 Prompt adherence | 2, 4, 5 | 3.67 → 4, **forced to 3 by restriction-breach override** | 0.65 | 20 | 13.00 | AS_OF_DATE / tick-spec gaps already pulled this down; override drops it one further level |
| C2 Structure | 5, 4, 4 | 4.33 → 4 | 0.85 | 20 | 17.00 | All sections present/ordered; minor table-column and unused-source-declaration gaps |
| C3 Accuracy & evidence | 4, 4, 3, 1 | 3.0 → 3 | 0.65 | 25 | 16.25 | Internally coherent, but the level-file reconciliation (the new, decisive test) fails on close, RSI2 and most pivots |
| C4 Reasoning & judgment | 4, 5, 4, 5 (pillars) | 4.5 → pulled to **4** for card construction | 0.85 | 20 | 17.00 | Pillar reasoning strong, but the Unit-3 runner-stop direction is inverted for SHORTs on 2 of 3 cards (see feedback) — scored under C4 per protocol |
| C5 Currency & transparency | 4, 3, 3, 1 | 2.75 → 3 | 0.65 | 15 | 9.75 | Good dating discipline undercut by the missing §20 anchor-override line, the uncaptioned PCE collision, and the module-code breach |

**Total = 13.00 + 17.00 + 16.25 + 17.00 + 9.75 = 73.00 → 73**

## 3. Total, band, override

- **total = 73**
- **band = Moderate (60–74)**
- **override = restriction_breach** — "M5-derived" (a module code, M1..M5) appears twice in the §11 table body, breaching row 5.4. Per protocol this caps the total at Moderate and drops C1 at least one level; both are already satisfied by the raw computation (73 ≤ 74; C1 forced from 4→3), so no further adjustment was needed.
- No hallucinated-source override triggered: the three spot-checked citations (Reuters, Investing.com, USAGOLD) are each named, dated and used consistently with their own quoted content — the close-value problem traces to using an in-progress session as the as-of basis, not to a fabricated or self-contradictory source.

```
c1=3
c2=4
c3=3
c4=4
c5=3
total=73
band=Moderate
override=restriction_breach
card_integrity=100
n_cards=3
n_duds=0
n_warns=0
```

## 4. Card Integrity (linter rows, copied verbatim from `qa/gold_regen_qa1/lint_static/2026-05-29.csv`)

| card_id | strategy | flags | dud | integrity (100−40·DUD−10·WARN) |
|---|---|---|---|---|
| 2026-05-29_Trade_1 | Trade 1 - Daily Directional (SHORT) | CLEAN | False | 100 |
| 2026-05-29_Trade_2 | Trade 2 - Pivot, regime-aware (TREND_DOWN breakout, SHORT) | CLEAN | False | 100 |
| 2026-05-29_Trade_3A | Trade 3A - Momentum-Pullback (TREND_DOWN, SHORT) | CLEAN | False | 100 |

Report-level Card Integrity = mean(100, 100, 100) = **100** (n_cards=3, n_duds=0, n_warns=0). This is a static, leak-free, internal-consistency score only — it does not (and per protocol cannot) detect the Unit-3 runner-stop direction error or the level-file reconciliation failures found above; those are captured under C3/C4 instead.

## 5. Data basis for the Category-3 checks (level file `data/levels/XAUUSD_by_date/2026-05-29.csv`, `_full` columns — matches the report's claimed "spot, loco London, continuous" basis; ATR14_full = 102.1993)

| Check | Report states | Level file (`_full`) | Diff | Tolerance zone | Verdict |
|---|---|---|---|---|---|
| D−1 Open | 4,456.5 | 4,463.13 | 6.63 | ≤9.20 consistent | Consistent |
| D−1 High | 4,465.4 | 4,516.58 | 51.18 | >20.44 fail | **Fail** |
| D−1 Low | 4,366.8 | 4,366.35 | 0.45 | ≤9.20 consistent | Consistent |
| D−1 Close | 4,404.2 | 4,495.71 | 91.51 | >11.75 fail | **Fail** |
| RSI2 | 5.1 | 43.4572 | 38.36 | >15 fail | **Fail** |
| ATR14 | ≈102.2 (§20) | 102.1993 | ~0.001% | ≤10% consistent | Consistent |
| Daily P | 4,412.2 | 4,459.5467 | 47.35 | >11.75 fail | **Fail** |
| Daily R1 | 4,457.5 | 4,552.7433 | 95.24 | >11.75 fail | **Fail** |
| Daily R2 | 4,510.8 | 4,609.7767 | 98.98 | >11.75 fail | **Fail** |
| Daily R3 | 4,556.1 | 4,702.9733 | 146.87 | >11.75 fail | **Fail** |
| Daily S1 | 4,358.9 | 4,402.5133 | 43.61 | >11.75 fail | **Fail** |
| Daily S2 | 4,313.6 | 4,309.3167 | 4.28 | ≤4.09 borderline consistent | Consistent (borderline) |
| Daily S3 | 4,260.3 | 4,252.2833 | 8.02 | 4.09–11.75 discrepancy | Discrepancy |
| Weekly P | 4,574.0 | 4,516.4567 | 57.54 | >11.75 fail | **Fail** |
| Weekly R1 | 4,649.2 | 4,579.2833 | 69.92 | >11.75 fail | **Fail** |
| Weekly R2 | 4,775.3 | 4,651.8367 | 123.46 | >11.75 fail | **Fail** |
| Weekly R3 | 4,850.5 | 4,714.6633 | 135.84 | >11.75 fail | **Fail** |
| Weekly S1 | 4,447.9 | 4,443.9033 | 4.00 | ≤4.09 consistent | Consistent |
| Weekly S2 | 4,372.7 | 4,381.0767 | 8.38 | 4.09–11.75 discrepancy | Discrepancy |
| Weekly S3 | 4,246.6 | 4,308.5233 | 61.92 | >11.75 fail | **Fail** |
| Monthly P | 5,006.3 | 4,673.69 | 332.6 | >11.75 fail | **Fail** (flagged indicative/non-anchoring in report, so not used on cards — but see feedback) |

Pattern: the report's own Low and (mostly) Open match the level file closely, but High and Close are far off, and every pivot derived from that Close is consequently far off. This is consistent with a genuine mid-session snapshot (the low had printed; the eventual high and the recovery to the real close had not) being carried through the report as the finalised D−1 session.
