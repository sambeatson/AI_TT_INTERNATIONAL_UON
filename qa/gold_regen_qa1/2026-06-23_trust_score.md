# Trust Score — Gold_Report_23-Jun-2026.md (D = 2026-06-23)
Run: `gold_regen_qa1` · Asset: XAUUSD · Reviewer: independent QA session (Stage 1)

Leak check: `data/levels/XAUUSD_by_date/2026-06-23.csv` → `last_bar_date=2026-06-22` < `date=2026-06-23`. OK to use.

## 1. Section 7 checklist

| Item | Notes | Evidence | Score |
|---|---|---|---|
| 1.1 Variables respected | Asset framed correctly (XAU/USD spot, LBMA loco-London; GC=F used for corroboration only, excluded from the median). USDX first counter (§10). Lookback 5d/25d stated (§2, §9). USD/oz throughout. Six independent observations in §4/§5/§20. Tick basis stated and used consistently (1 tick=$0.01/oz; 8,900/4,329/4,405 ticks all divide out exactly). Gap: §2's `As-of` field states **23 June 2026 (the report date, D)**, but `M1_Variables_v2_1.md`'s fixed definition of `[AS_OF_DATE]` is "the last completed regular session... strictly before the report date" — i.e. it should read 22 June 2026, matching §6's own last OHLC row. | §2, §4, §6, §10, §20, §21b | 4 |
| 1.2 Coverage & currency consistent | Data dates are D−1 or earlier throughout §6/§13/§21c; forward-looking items correctly dated D or later (§13d, §16, §21c-labelled backtest). No USD/oz–tick drift; tick counts verified self-consistent. Same As-of mislabeling as 1.1 bleeds into this row (§2 vs §6 disagree on what "as-of" means). | whole report | 4 |
| 1.3 Audience & tone | Senior Commodities Analyst — Precious Metals register held throughout; no retail tone. | §1, masthead, §18 | 5 |
| **C1 (mean, rounded)** | (4+4+5)/3 = 4.33 → **4** | | **4** |
| 2.1 Sections present & ordered | All of §1–§21 present in order, including §13a–d and §21a–d. §17 forecast is genuinely one sentence. | headings | 5 |
| 2.2 Scorecard as a table | §6 is a proper O/H/L/C/RSI2/Trend/Src A/Src B/Validation table. §11's three pivot tables are internally inconsistent with each other and with the R3→P→S3 (three-per-side) spec: **daily** shows 5 levels/side (R5–S5); **weekly** shows an irregular 4/3 split that skips R4 entirely (R5,R3,R2,R1 / P / S1,S2,S3); **monthly** shows only 2 resistance vs 3 support levels (R2,R1 / P / S1,S2,S3). No information is lost, but the format is neither the spec nor consistent across timeframes. | §6, §11 | 3 |
| 2.3 Method steps visible | §4→§5 show observation→normalization→consensus with the futures-to-spot contango adjustment stated; §8 is candle-by-candle; §9 covers persistence/overlap/VOLator/KER; §7 chart slots are captioned placeholders (acceptable per brief — conversion drops images). | §4–§9 | 5 |
| **C2 (mean, rounded)** | (5+3+5)/3 = 4.33 → **4** | | **4** |
| 3.1 Quantitative claims sourced | Most §1/§12/§14 figures carry a source (WGC Q1-2026, FOMC dot-plot, PBoC/RBI, §4/§6/§13 pointers). A few are unsourced restatements: §14's VIX (~16.8) and USDX (~100.8–101) are cited without a fresh reference on their second/third appearance. | §12, §14 | 3 |
| 3.2 Citations exist & contain data | Spot-checked three: TradingEconomics (21 Jun, dated, quote "extending its recent decline" consistent with the report's own bearish framing), Morgan Stanley (22 Jun, quote "path to $5,200 hinges on ETF demand" matches headline and is treated as a longer-horizon outlier, not near-term), FOREX.com/Scutt (22 Jun, "Holds Yearly Support—Major Low Forming?" classified Mixed, consistent with its own hedged quote). No self-contradictory or impossible source found. | §4, §13a | 5 |
| 3.3 Calculations transparent | Daily pivot arithmetic reproduces exactly from the report's own stated 22-Jun H/L/C (P=(4220.34+4140.17+4192.83)/3=4184.4467, matching to the cent; R1/S1/R2/S2/R3/S3 all reproduce likewise). RSI2/ATR are stated. **§21a's direction score does not reconcile**: the five "top contributing signals" listed (medium-term regime −0.14, short-term −0.13, cross-asset −0.15, Kaufman −0.15, sentiment −0.07) sum to −0.64, not the stated total of −0.53 — a 0.11 gap consistent with the sixth weighted component (VOLator, `[W_VOLATOR]=0.10`) being silently omitted from the disclosed list. The score is asserted, not shown to derive from all six weighted signals as M5 H.3 requires. | §6, §11, §21a | 2 |
| 3.4 Numbers reconcile — incl. vs level file | Internally: D−1 close ($4,192.83) is consistent across §1/§3/§4/§6/§11/§19. Externally, checked against `data/levels/XAUUSD_by_date/2026-06-23.csv` (`_full` basis, matching the report's own "spot, loco London, continuous" claim — confirmed correct basis since checking against `_cash` produces far larger, inconsistent gaps): §6 OHLC all within tolerance (O diff 8.48 ≤0.09×ATR14_full=10.77; H diff 0.28; L diff 3.69; C diff 1.44 ≤0.04×ATR=4.79). Daily pivots reconcile within tolerance except S2 (diff 5.59, discrepancy band) and S3 (diff 7.48, discrepancy band). Weekly pivots reconcile within tolerance except R3 (diff 5.39, discrepancy band). **Monthly pivots fail catastrophically on every level**: P off 59.57, R1 off 119.21, R2 off 237.69, S1 off 58.91, S2 off 118.55, S3 off 237.03 — all far past the 0.115×ATR14_full=13.76 failure line (`atr14_full=119.7`). Back-solving the report's own monthly R1/S1 (algebra: L=2P−R1, H=2P−S1) reproduces R2/S2 exactly (self-consistent pivot family) from implied H=4595.31, L=4366.41, C=4539.27 — **not May's actual H/L/C**. The implied H (4595.31) sits $0.10 from the level file's `swing_high_25d_full` (4595.21), and the implied C (4539.27) sits $0.27 from the report's own §7.3 caption figure ("$4,539 late-May peak") — strong evidence the monthly pivot table was built from 25-day swing/peak figures rather than the actual prior calendar month's H/L/C. Trade 1's entry ($4,176) and the report's central "confluence" narrative (§11, §15, §16, §18) are anchored to this wrong monthly S3. | §11, level file, `swing_high_25d_full` | 1 |
| **C3 (mean, rounded)** | (3+5+2+1)/4 = 2.75 → **3** | | **3** |
| 4.1 Pillars conclude | §8, §9, §10, §12, §14 each end with an explicit, content-consistent direction label. | those sections | 5 |
| 4.2 Peer/cross-asset interpreted | §10 gives mechanism (USDX opportunity-cost channel, S&P risk-on diversion, DAX confirmation), not a bare correlation list. | §10 | 5 |
| 4.3 Synthesis reconciles tensions | §9 explicitly reconciles the KER-vs-VOLator-slope tension (positive slope kept as the "single dissonance" that still fails the RANGE dual-gate); §15/§16/§18 reconcile short- vs medium-term; §17 vs §21a explicitly checked ("No conflict with the §17 forecast"). | §15–§18, §21a | 5 |
| 4.4 Calibrated language | §17 is exactly one sentence with a stated conditional clause and confidence (Medium) elsewhere; no hedge-stacking. | §3, §17 | 5 |
| Card construction (M5, per QA_PROTOCOL anchor — folded into C4) | Two concrete rule/consistency defects, neither caught by the static linter (which checks arithmetic side/order, not procedural conformance): (a) **Trade 1's entry is not "market at the daily-open anchor"** as the fixed M5 rule requires — it is a conditional sell-stop contingent on "a confirmed daily close below the confluence" (or an alternative market-on-rejection trigger), which could fire hours after the anchor time or not at all; this deviation from the fixed rule is nowhere logged as a non-conformance. (b) **Trade 3A's own caveat cell is self-contradictory**: it computes the fib-leg magnitude check as "range $262 > 2×$121.80? No" — but $262 > $243.60 is true, so the correct answer is Yes (check passes at the default lookback, no adaptive extension needed), yet the report answers "No" to its own arithmetic. Card Integrity itself (separate score) is unaffected — these are procedural/logic defects, not the stop-side/TP-order/R-magnitude checks the linter enforces. | §21b Trade 1, Trade 3A; `cards/.../2026-06-23.json` notes | 2 |
| **C4 (mean incl. card construction, rounded)** | (5+5+5+5+2)/5 = 4.4 → **4** | | **4** |
| 5.1 Data dated; staleness flagged | Every price/article dated; the 19-Jun close delta ($3.66) is explicitly flagged as legitimate spot-vendor dispersion at the Friday handover rather than silently accepted. | §4, §6, §13, §19 | 5 |
| 5.2 Assumptions up front | Futures-to-spot normalization (contango) is stated with its size in §3/§5/§19 — good. But two assumption-disclosure gaps: (i) §1's "(00:00 UK anchor overridden to the 23-Jun session reset)" uses override language with no corresponding non-conformance entry anywhere in §19/§20 explaining what changed or why — the module requires a genuine anchor deviation to be "recorded as such... in the report body" and in "the handoff record," neither of which happens here; (ii) the monthly-pivot data-source error (see 3.4) is undisclosed — the monthly table carries the CORROBORATED flag with no caveat about its H/L/C provenance. | §1, §19, §20, §11 (absence) | 3 |
| 5.3 Red flags surfaced | Demand-side red flags (WGC jewellery declines) and macro red flags (hawkish Fed, USDX highs) are surfaced in §12/§15; the 25-Jun PCE event collision is carried into both Trade 1 and Trade 2's caveat rows. | §12, §15, §21b | 5 |
| 5.4 Restrictions honoured | No bracketed variable names or module codes (M1..M5) found in the report body (checked directly). No un-normalized retail premium (explicitly: "No retail FX-broker spreads were admitted"). GC=F treated as corroboration-only and excluded from the spot median, as required. Instrument common names used throughout. | whole report | 5 |
| **C5 (mean, rounded)** | (5+3+5+5)/4 = 4.5 → **4** (rounded down per reviewer guidance: pick the lower level on a tie) | | **4** |

## 2. Category roll-up

| Category | Max | Level | Multiplier | Points | Justification |
|---|---|---|---|---|---|
| C1 Prompt adherence | 20 | 4 | 0.85 | 17.00 | All Variables substantively respected; the `As-of` field states the report date (D) rather than the last completed session (D−1) that `M1_Variables_v2_1.md` fixes it to. |
| C2 Structure | 20 | 4 | 0.85 | 17.00 | All 21 sections present/ordered; the three §11 pivot tables are internally inconsistent with each other and with the three-levels-per-side spec (5/side daily, an irregular 4/3 weekly that skips R4, 2/3 monthly). |
| C3 Accuracy & evidence | 25 | 3 | 0.65 | 16.25 | D−1 OHLC/RSI2/ATR14 and the daily/weekly pivots reconcile within tolerance against the level file; **the monthly pivot table fails every level by $59–$238 (vs a $13.76 failure threshold)** and is demonstrably built from 25-day swing/peak figures rather than May's actual H/L/C — and this wrong table anchors the report's central "confluence" narrative and Trade 1's entry. §21a's direction score also does not sum to its stated total (VOLator component missing from the disclosed derivation). |
| C4 Reasoning & judgment | 20 | 4 | 0.85 | 17.00 | Pillars, cross-asset mechanism, synthesis and calibration are strong; card construction carries two defects — Trade 1's entry is not the fixed "market at the daily-open anchor" rule, and Trade 3A's own fib-leg caveat contradicts its own arithmetic. |
| C5 Currency & transparency | 15 | 4 | 0.85 | 12.75 | Dating and red-flag surfacing are solid, restrictions honoured; the ambiguous, unlogged anchor-override language and the undisclosed monthly-pivot sourcing error are the main transparency gaps. |
| **Total** | 100 | | | **80.00 → 80** | |

## 3. Total, band, override

```
c1=4
c2=4
c3=3
c4=4
c5=4
total=80
band=High
override=none
card_integrity=100
n_cards=3
n_duds=0
n_warns=0
```

Override check: no fabricated or self-contradictory source found on the 3.2 spot-check (no hallucinated-source override — the monthly-pivot error is a computation/data-sourcing failure, not a fabricated citation). No prompt-level restriction is openly violated (no restriction-breach override). Band from total score: 80 → **High Trust (75–89)**.

## 4. Card Integrity (from `qa/gold_regen_qa1/lint_static/2026-06-23.csv`, copied verbatim)

| card_id | strategy | flags | dud | Card Integrity (100−40·DUD−10·WARN) |
|---|---|---|---|---|
| 2026-06-23_Trade_1 | Trade 1 — Daily Directional | CLEAN | False | 100 |
| 2026-06-23_Trade_2 | Trade 2 — Pivot (regime-aware, TREND_DOWN) | CLEAN | False | 100 |
| 2026-06-23_Trade_3A | Trade 3A — Momentum-Pullback (TREND_DOWN selected) | CLEAN | False | 100 |

Report-level Card Integrity (mean over non-suppressed cards) = **100**. n_cards=3, n_duds=0, n_warns=0. (Static integrity — stop side, TP order, R magnitude — is clean; the card-construction defects noted under C4 above are procedural/sourcing issues the static linter does not check, so they do not change this score, per protocol.)
