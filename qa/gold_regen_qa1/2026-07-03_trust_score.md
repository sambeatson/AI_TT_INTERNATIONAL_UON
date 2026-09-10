# Trust Score — XAUUSD Gold Report, 03 Jul 2026 (`Gold_Report_03-Jul-2026.md`)
Run: gold_regen_qa1 · Reviewer basis: report claims spot/loco-London continuous quoting → checked against `_full` columns of `data/levels/XAUUSD_by_date/2026-07-03.csv` (`last_bar_date=2026-07-02 < 2026-07-03`, confirmed leak-free).

## 1. Section 7 checklist

| Row | Reviewer notes | Evidence observed | Score (0–5) |
|---|---|---|---|
| 1.1 Variables respected | Asset = XAU/USD spot loco London, GC futures corroboration-only ✓; USDX first counter in §10 ✓; as-of = last completed session (02 Jul) ✓; lookback 5/25 ✓; USD/oz ✓; 7 named sources ✓; tick 0.01 used consistently. Daily-open anchor is named and its override is logged in §20 but never carried onto the cards or into §21b as the module requires — a real gap, not fatal. | §2, §10, §20, §21b | 4 |
| 1.2 Coverage & currency consistent | D-1 close (4,108.07) used identically wherever quoted in-report (§6, §11); no USD/oz unit drift anywhere. | whole report | 4 |
| 1.3 Audience & tone | Consistently institutional register ("Senior Commodities Analyst — Precious Metals"); no retail tone. | §1, header | 5 |
| 2.1 Sections present & ordered | All of §1–§21 present, correctly ordered, with §13a–d and §21a–d all present. | headings | 5 |
| 2.2 Scorecard as table | §6 is a proper 10-column table ✓. §11's three pivot tables, however, print 5 levels/side (R5…S5, 11 rows) instead of the specified 3-levels/side R3→P→S3 format — a systematic format deviation across all three (daily/weekly/monthly). | §11 | 2 |
| 2.3 Method steps visible | §4–§8 candle-by-candle and futures-to-spot normalisation stated. §9's Kaufman line is an **unrendered template artifact** — `KER = {S['ker_value']:.2f} → Trending Down — Moderate` — printed verbatim instead of the number, breaking the one calculation §9 is supposed to show (the value -0.22 is only recoverable from §1/§21a). | §9 | 3 |
| 3.1 Quantitative claims sourced | Most §1/§12/§14 figures point to §4/§6/§10/§13. | text | 3 |
| 3.2 Citations exist & contain data | Spot-checked Investing.com, Capital.com, FXStreet (one from Scorecard-adjacent, one Deep-Dive, one Risk-adjacent use). Investing.com and Capital.com are internally consistent. **FXStreet fails**: §4 quotes FXStreet (02 Jul) giving "20-SMA ≈ $4,034"; the same "20-day SMA" figure is then used **five more times** (§8, §11 narrative, §16, Trade 3A entry rationale, Trade 3A TP3/confluence) as **$4,183** — a $149 self-contradiction on the same named, dated source's own figure. Per brief §1/framework 3.2, a source whose quoted figure does not match how it is used elsewhere counts as fabricated → **triggers the hallucinated-source override.** | §4 vs §8/§11/§16/§21b | 0 |
| 3.3 Calculations transparent | RSI2 reproduces from the report's own 5 closes (two consecutive gains → RS→∞ → RSI2=100, matches §6). But: ATR14 is never stated anywhere in the report body (cards' stops/TPs cannot be checked against it in-text); Trade 2's entry cell claims "$4,145.00 ... ~3,700 ticks above daily P" — actual distance to the stated P ($4,009.32) at the card's own 0.01 tick is 13,568 ticks, not 3,700 (R/TP tick counts elsewhere on the same card are correct); Trade 3A's entry is labelled "38.2% retrace" and TP1 is separately labelled "38.2% target" for the same leg — two different price levels cannot both be the 38.2% level. | §21b (Trade 2, Trade 3A) | 1 |
| 3.4 Numbers reconcile — incl. level file | **Daily pivots (§11) are computed from 01 Jul H/L/C, not 02 Jul (D-1)** — P=(4045.00+3951.68+4031.29)/3=4,009.32 reproduces exactly from 01 Jul, confirming the wrong session was used; vs the leak-free `d_full_P`=4,099.4833, a 90.16-pt (0.79×ATR14) miss — Category 3 failure, and a full session's staleness undisclosed as such. §6's own 02 Jul close (4,108.07) vs level file `prev_close_full` 4,123.79: 15.72 (0.1375×ATR14) — exceeds the 0.115×ATR14 failure threshold. Weekly P (4,037.44 vs `w_full_P` 4,086.99, 0.43×ATR14) and monthly P (4,238.39 vs `m_full_P` 4,165.5133, 0.64×ATR14) both exceed the failure threshold too (period selection for both is correct, only the level is off). O/H/L for 02 Jul are within tolerance. | §6, §11 vs level file | 1 |
| 4.1 Each pillar concludes | §8/§9/§10/§12/§14 each end with an explicit direction label. | those sections | 4 |
| 4.2 Peer/cross-asset interpreted | §10 states mechanism for each counter (USDX opportunity-cost, equity-risk rotation, silver beta), not a bare correlation list. | §10 | 4 |
| 4.3 Synthesis reconciles tensions | §15/§16/§18 explicitly hold the short-term-bull/medium-term-bear tension open rather than averaging it away; §21a states the score/forecast alignment without editing either to match. | §15–18, §21a | 4 |
| 4.4 Calibrated language / card construction | Narrative language is calibrated. Card construction (folded into C4 per protocol) is materially non-compliant on **Trade 3A**: (a) the 01Jul-low→02Jul-high leg is only ~1–2 sessions old, short of the required 4–10 session lookback; (b) its magnitude is 192.43 pts vs the required ≥2×ATR14 = 228.64 pts — **the swing does not qualify** under the M5 rule at all; (c) the entry ($4,072.00) reproduces the **38.2%** retracement (calc: 4,144.11−0.382×192.43=4,070.60), not the required **57.5%** entry (calc: 4,033.46) — a ~$39 misplacement; (d) the stop ($4,030.00, "below the 02 Jul low") is anchored to an unrelated data point instead of "beyond the 0% anchor by 0.25×ATR" (compliant ≈ 3,951.68−0.25×114.3221 = 3,923.10) — a ~$107 misplacement. This is not a cosmetic slip; a user re-deriving the card from the stated methodology gets different numbers than the ones printed. | §21b (Trade 3A) | 0 |
| 5.1 Data dated; staleness flagged | Every price/article dated; §20 proactively flags the TradingEconomics snapshot as partially stale (19 Jun) rather than presenting it as current. | §4, §13, §20 | 4 |
| 5.2 Assumptions up front | Futures-to-spot normalisation ($20–40) stated in §5 with size. The daily-open-anchor override (00:00 UK → 23:00 UK) is logged **only** in §20 — never converted onto either live card, and never appears in §21b — contrary to the module's explicit requirement that an anchor departure be carried "on the card, in the handoff record and in the report body." Nothing in the card text states any clock time at all. | §20 vs §21b | 2 |
| 5.3 Red flags surfaced | §12/§15 risks are substantive; §13d's CPI collision is explicitly carried into both live cards' caveat rows. | §12, §15, §21b | 4 |
| 5.4 Restrictions honoured | No module codes, bracketed variable names, or framework name appear in the body — **except** §9's leaked `{S['ker_value']:.2f}` template fragment, which is exactly the kind of raw internal-variable exposure the restriction is meant to prevent. | §9 | 3 |

## 2. Category roll-up

| Cat | Level (mean of rows, rounded) | Multiplier | Max | Points | Justification |
|---|---|---|---|---|---|
| C1 Prompt adherence | 4 | 0.85 | 20 | 17.00 | Variables all respected; anchor-override propagation is the one real gap |
| C2 Structure | 3 | 0.65 | 20 | 13.00 | All sections present/ordered, but pivot-table format wrong in all 3 sets and §9 contains unrendered code |
| C3 Accuracy & evidence | **0** | 0.00 | 25 | 0.00 | Hallucinated-source override (FXStreet 20-SMA self-contradiction) applies; independently supported by wrong-session daily pivots, close/weekly/monthly pivot misses beyond tolerance, and two calculation errors |
| C4 Reasoning & judgment | 3 | 0.65 | 20 | 13.00 | Pillar reasoning and synthesis are strong (rows 4.1–4.3 ≈4); card construction (4.4) is a severe outlier — Trade 3A fails its own swing-qualification, retracement, and stop rules |
| C5 Currency & transparency | 3 | 0.65 | 15 | 9.75 | Dating and red-flag surfacing are good; anchor-override disclosure and the leaked variable fragment pull this down |

## 3. Total, band, override

```
total = round(17.00+13.00+0.00+13.00+9.75) = 53
band  = Low Trust (40–59)
override = hallucinated_source   (FXStreet's own 20-day-SMA figure: $4,034 in §4 vs $4,183 used five times elsewhere in §8/§11/§16/§21b — a self-contradictory citation per brief §1 / framework 3.2, which caps the band at Low Trust and sets C3 = 0)
```
Note: the natural point total (53) already falls inside the override's Low-Trust cap (40–59), so the override and the arithmetic total agree here — the override is still the binding reason for the band, not a coincidence of the score.

## 4. Card Integrity (from `qa/gold_regen_qa1/lint_static/2026-07-03.csv`, copied verbatim)

| card_id | strategy | flags | dud | integrity (100−40·#DUD−10·#WARN) |
|---|---|---|---|---|
| 2026-07-03_Trade_1 | Trade 1 — Daily Directional | SUPPRESSED | False | excluded (suppressed) |
| 2026-07-03_Trade_2 | Trade 2 — Pivot, range-fade (TRANSITION) | CLEAN | False | 100 |
| 2026-07-03_Trade_3A | Trade 3A — Momentum-Pullback | CLEAN | False | 100 |

Report-level Card Integrity = mean over non-suppressed cards = mean(100, 100) = **100**.

Note for the regeneration agent: the static linter only checks stop/TP side and ordering, so it correctly shows Trade 3A as CLEAN. The Trade 3A defects in row 4.4 above (wrong retracement %, non-qualifying swing, misplaced stop) are semantic M5-rule violations the linter cannot see — they do not show up in Card Integrity and must be fixed independently of it.

## 5. Explicit score lines

c1=4
c2=3
c3=0
c4=3
c5=3
total=53
band=Low Trust (40-59)
override=hallucinated_source
card_integrity=100
n_cards=3
n_duds=0
n_warns=0
