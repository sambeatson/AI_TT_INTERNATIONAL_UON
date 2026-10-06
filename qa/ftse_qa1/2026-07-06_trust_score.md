# Trust Score v3.7 — FTSE_EuroStoxx_Report_06Jul2026.md (D = 2026-07-06)

Run ftse_qa1 · reviewer session for D only · inputs: report, `data/levels/UK100_by_date/2026-07-06.csv` (last_bar_date 2026-07-03 < D, checked), UK100/USDX/US500/VIX/NEWS slices to 2026-07-03, `engine/qa_slice_stats.py --cash-open 10:00 --cash-close 18:30`, transcribed cards, static linter rows.

## Result (machine-readable)
c1=2
c2=4
c3=2
c4=3
c5=3
total=58
band=Low
override=restriction_breach
card_integrity=96.7
n_cards=3
n_duds=0
n_warns=1

Override basis: (a) Trade 2 produced although the report itself states (§11, §19, Trade 2 caveat) that every pivot tier is single-source-indicative and that "per strict rules Trade 2 would normally be SUPPRESSED" — M5 suppression is a fixed rule; (b) §6 bars for 29 Jun–01 Jul carry a synthesis signature (integer-only values, each open exactly equal to the prior close, Thu low = Thu open, whole Mon/Tue bars sitting below the real session lows) while §20 asserts "No prices were synthesised — indicative bars are best-available fetched values". No fabricated *source* was demonstrated on the three-source spot-check, so the hallucinated_source override is not applied. Total (58) already sits below the Moderate cap (74); C1 reduced one level (3 → 2) by the breach.

## 1. Section 7 checklist

| Row | Check | Notes / evidence location | Score |
|---|---|---|---|
| 1.1 Variables respected | FTSE 100 cash index primary (§2 ✓); counters USDX, S&P 500, DAX 40, Euro Stoxx 50 (§10 ✓); as-of Fri 03 Jul close, Europe/London, 5-session lookback, GBP/index points ✓. Misses: daily-open anchor set to **00:00 UK** instead of 07:00 UK (§2 note, §20, Trade 1 entry) — disclosed but a deviation; "minimum source count (6) met" (§4) rests on anonymised rows ("Aggregator quote", "Economic-data provider"), one of which is "Excluded" and one gives only a day high — effectively 4 usable sources, no sell-side/exchange tier evidenced | 2 |
| 1.2 Coverage & currency consistent | Data dates all ≤ D-1, session = D ✓; GBP/points ✓. §13d is "Wk of 07 Jul" — omits D itself (06 Jul) and gives no dates; §2 promises GBP-equivalent for Euro Stoxx "where used" but none shown | 3 |
| 1.3 Audience & tone | Strategist register, trading/risk-review framing throughout §1, §18 | 5 |
| **C1 mean 3.33 → 3; restriction breach −1 level** | | **2** |
| 2.1 Sections present & ordered | §1–§21 all present in order; §13a–d, §21a–d present; §17 is one sentence | 5 |
| 2.2 Scorecard as table | §6 is a table but lacks Source A / Source B / Final columns (only a single "Validation" column). §11: daily shown R5→S5 in a side-by-side two-column grid (not an R3→P→S3 ladder); weekly has only R2/R1/P/S1/S2 (no R3/S3); monthly only R1/P/S1 (no R2,R3,S2,S3). Brief requires 3 levels each side for all three | 2 |
| 2.3 Method steps visible | §4–§5 observation→consensus present but thin; §8 candle-by-candle + sequence ✓; §9 regime, persistence 1.0, VOLator readings ✓; Kaufman efficiency never given a number (KER(13,EMA3) value absent), ATR(14) absent from §9; §7 charts are a caption only (accepted, pandoc drops images) | 4 |
| **C2 mean 3.67 → 4** | | **4** |
| 3.1 Quantitative claims sourced | §12/§14 figures carry no source and do not point to §4/§6/§13: Brent ~93.7, WTI ~90.6, gilt 10Y ~4.95%, EUR/GBP ~0.857, gold ~4,118 (−3.4%), VIX ~15.8 (−2.1%), "~one-third" ECB July hike, "~80% multinational revenue". VIX ~15.8 vs slice VIX last 17.14 (−2.5% on the day) — Δ1.3 pts. §1/§13c "softer-than-expected" payrolls: calendar shows NFP actual 57 vs consensus 43 (prior 172), unemployment 4.2 vs 4.2 cons (prior 4.3) → actual **beat** consensus; §13c "Below consensus" is contradicted | 2 |
| 3.2 Citations exist & contain data (3 spot-checks) | (i) Trading Economics FTSE, 03 Jul: quote "highest since March 2" vs report text "two-month high" (§1, §8, §13a) — 2 Mar to 3 Jul is four months; internally inconsistent. (ii) Sharecast/Fidelity 02 Jul "FTSE up 1.8%": consistent with §6 (10,466→10,658 = +1.83%) and slice (+1.73% cash). (iii) STOXX: close 6,417 "corroborated" by the index provider's same-date 52-week-high print of 6,412.68 — a print *below* the stated close and below the report's own session high 6,420.44 cannot corroborate it; and 4.3 pts is not within the ±0.10 tolerance claimed. Also the FTSE "economic-data provider ≈10,679" gives no figure to ±0.10, so "Δ≈0, tolerance ±0.10" (§20) is not demonstrable. Prices cite generic labels, no named/dated publisher. No impossible URL found; no override triggered | 2 |
| 3.3 Calculations transparent | RSI2 reproducible from the report's own closes (Wed/Thu/Fri = 100.0 ✓ via `--closes`); Trend labels follow the O/C/RSI2 rule from the report's own table ✓; §11 pivot arithmetic reproduces from the stated inputs (P=(10688+10466+10658)/3=10,604 ✓, R1=2P−L=10,742 ✓ …); sentiment tilt 5/6=+0.83 ✓. Gaps: ATR(14) given only on Trade 1 ("≈113"); KER value not stated; §21a lists three signals but not the six signal×weight terms, so +0.72 is not reproducible; §21d "mean R ≈ +1.26 (closed positions)" actually includes the OPEN +0.3R row (closed-only mean = 1.50) and "TP2 ≈ 60%" matches no count (2/5=40%, 2/4=50%); §21c rows give no R in points | 3 |
| 3.4 Numbers reconcile (internal + slice) | D-1 close 10,679.03 consistent across §1/§3/§4/§6/§21b ✓. Breaks: §11 daily pivots are "from Thu 02 Jul H/L/C" although D-1 is Fri 03 Jul (own Fri row would give P=10,661.5); Trade 3A TP2 10,880 labelled "5-day swing high" vs §8 swing high 10,701.32; Trade 2 runner 10,826 < TP1 10,890 < TP2 11,035; §8 support "10,337 (5-day swing low)" vs slice 10,416.0 (Δ−79). **Slice reconciliation fails materially — see §2 below** (D-1 close Δ+18.5 > 15; Mon–Wed bars off by up to 179 pts; RSI2 Wed/Thu 100 vs 11.28/86.19; weekly pivots from the wrong week, Δ≈−327; monthly P Δ−29) | 1 |
| **C3 mean 2.0 → 2** | no hallucinated-source override applied | **2** |
| 4.1 Pillars conclude | §8 "Bullish continuation", §9 "Bias: Bullish", §10 "CONFIRM", §12 sub-sections labelled price-supportive/mixed, §15 balanced; §14 is bullet list without a closing direction label | 4 |
| 4.2 Cross-asset mechanism | §10 gives mechanisms, but the USDX one has the wrong sign: a falling USD (rising GBP) is stated to "lift GBP-translated multinational earnings" (§10, §12 FX), while §13d/§164 says a stronger pound hurts FTSE multinationals — self-contradictory. Brent/energy is argued in §12 but is not a §10 counter; S&P and DAX rows are correlation-style ("risk beta", "proxy") | 2 |
| 4.3 Synthesis reconciles tensions | §15/§16/§18 assert "no conflict" throughout; USD-translation contradiction, RSI2-pinned-at-100 vs trend-pullback entry (Trade 3A requires a pullback to P while §21a says LONG market), and the Trade 2 suppression conflict are noted but not resolved. §17 vs §21a consistent | 3 |
| 4.4 Calibrated language | §17 is one sentence, "likely … unless"; §3 confidence Medium; KER "near-maximal" on an unseasoned window flagged; "strongly positive" signals unsupported by itemisation | 4 |
| 4.5 Card construction (protocol) | All three cards deviate from fixed M5 rules (detail in feedback file): Trade 1 no 0.25×ATR buffer, no wide-stop flag at R=1.42×ATR, entry cell states no price, stale-day pivots; Trade 2 must be SUPPRESSED, entry/stop/TP not the TREND formula, TP3 below TP1; Trade 3A entry is daily P not a 57.5% retrace, TP1/TP2 mis-defined, no swing endpoints logged | 1 |
| **C4 mean 2.8 → 3** | | **3** |
| 5.1 Data dated; staleness flagged | Prices/articles dated ✓; single-source-indicative O/H/L flagged ✓ (but the flagged values are materially wrong); §13d undated ("Wk of 07 Jul") | 3 |
| 5.2 Assumptions up front | Anchor override stated in §2, §20 and Trade 1 entry cell ✓ (Trade 2/3A state no anchor time; Trade 1 caveats row does not name it); pivot-indicative flag propagated to all three cards ✓ | 4 |
| 5.3 Red flags surfaced | UK CPI/BoE in §12/§15/§18/cards, but (i) the "UK CPI / US CPI / Eurozone CPI final / BoE minutes — week of 07 Jul" rows have no support in the calendar slice and no dates; (ii) the actual D-day calendar is omitted: US S&P Global Services PMI (HIGH, 14:45 UK), ISM Non-Mfg PMI & Prices Paid (HIGH, 15:00 UK), ECB Lagarde speech (HIGH, 17:00 UK), BoE MPC Mann speech (17:45 UK), UK Construction PMI (09:30 UK); (iii) §13c omits EZ CPI y/y 1 Jul (3.0 vs cons 2.1, prior 3.2) and Bailey/Lagarde speeches, and misstates NFP vs consensus. Card caveats therefore carry the wrong collision | 3 |
| 5.4 Restrictions honoured | Breach: Trade 2 issued against the fixed suppression rule "under corroboration-leniency instruction"; §6 early bars show a synthesis signature while §20 denies synthesis. No retail CFD in OHLC basis ✓; no module codes / bracketed variable names / framework name ✓; futures not used ✓ | 1 |
| **C5 mean 2.75 → 3** | | **3** |

## 2. Category 3 — slice vs report (cash basis claimed; UK100 CFD cash window 08:00–16:30 London)

Tolerances (brief §4): close ≤5, O/H/L ≤10; >15 on a close = Category 3 failure. Δ = report − slice (cash).

| Session | Field | Report | Slice (cash) | Δ | Verdict |
|---|---|---|---|---|---|
| Mon 29 Jun | O / H / L / C | 10,353 / 10,402 / 10,337 / 10,388 | 10,505.9 / 10,524.3 / 10,468.8 / 10,497.8 | −152.9 / −122.3 / −131.8 / −109.8 | Fail (entire bar below the real low) |
| Tue 30 Jun | O / H / L / C | 10,388 / 10,430 / 10,362 / 10,419 | 10,509.5 / 10,608.8 / 10,490.6 / 10,501.5 | −121.5 / −178.8 / −128.6 / −82.5 | Fail |
| Wed 01 Jul | O / H / L / C | 10,419 / 10,470 / 10,405 / 10,466 | 10,481.4 / 10,500.3 / 10,416.0 / 10,472.4 | −62.4 / −30.3 / −11.0 / −6.4 | Fail O, H; L and C just outside tolerance |
| Thu 02 Jul | O / H / L / C | 10,466 / 10,688 / 10,466 / 10,658 | 10,433.6 / 10,686.8 / 10,424.8 / 10,654.0 | +32.4 / +1.2 / +41.2 / +4.0 | Fail O, L; H, C ok |
| Fri 03 Jul (D-1) | O | 10,653.00 | 10,689.3 | −36.3 | Fail |
| Fri 03 Jul | H | 10,701.32 | 10,692.5 | +8.8 | ok |
| Fri 03 Jul | L | 10,604.25 | 10,590.6 | +13.65 | Fail (>10) |
| Fri 03 Jul | **C** | **10,679.03** | **10,660.5** (full-day 23:45 bar: 10,629.6) | **+18.5** (full-day +49.4) | **Fail (>15)** — the "CORROBORATED" tag is not supported against the slice |

RSI2 (cash closes) vs report: Mon 0.00 / Tue 16.59 (report "—"); Wed 11.28 vs 100.0; Thu 86.19 vs 100.0; Fri 100.0 vs 100.0 (ok). Report RSI2 is arithmetically consistent with its own (wrong) closes. Trend labels from the slice: Mon, Tue, Wed Bearish (close<open, RSI2<50) vs report Neutral/Neutral/Bullish. The "five consecutive higher closes" / "five higher closes" claim (§1, §8, §9, §15, §21d) is not true of the slice: Wed 01 Jul closed lower (10,472.4 vs 10,501.5).

ATR14: report "≈113" (Trade 1 only) vs 112.19 cash / 121.23 full → ok.

| Pivot | Report | Slice (cash) | Δ |
|---|---|---|---|
| Daily R3 / R2 / R1 | 10,964 / 10,826 / 10,742 | 10,807.03 / 10,749.77 / 10,705.13 | +157.0 / +76.2 / +36.9 |
| Daily P | 10,604 | 10,647.87 | −43.9 |
| Daily S1 / S2 / S3 | 10,520 / 10,382 / 10,298 | 10,603.23 / 10,545.97 / 10,501.33 | −83.2 / −164.0 / −203.3 |
| Weekly R2 / R1 / P / S1 / S2 | 10,549 / 10,399 / 10,263 / 10,113 / 9,976 | 10,866.17 / 10,763.33 / 10,589.67 / 10,486.83 / 10,313.17 | −317.2 / −364.3 / −326.7 / −373.8 / −337.2 |
| Monthly R1 / P / S1 | 10,640 / 10,383 / 10,209 | 10,698.13 / 10,412.17 / 10,215.53 | −58.1 / −29.2 / −6.5 |

Diagnosis: daily set is the Thu 02 Jul inputs (stated), not D-1 (Fri 03 Jul); weekly set back-solves to H≈10,413 / L≈10,127, i.e. an earlier week, and does not even match the report's own §6 week (which would give P≈10,572); monthly set back-solves to H≈10,557 (June high 10,608.8) and a 10,466 close. Swing: report 5-day low 10,337 vs slice 10,416.0; report swing high 10,701.32 vs 10,692.5 (ok).

## 3. Roll-up

| Category | Level | Multiplier | Points | Justification |
|---|---|---|---|---|
| 1 Prompt adherence (20) | 2 | 0.40 | 8.0 | Variables mostly honoured; 00:00 UK anchor override; thin source tiers; restriction breach (Trade 2 against suppression rule, synthesis signature) takes one level |
| 2 Structure (20) | 4 | 0.85 | 17.0 | Full §1–§21 sequence; §6 missing Source A/B/Final columns and §11 missing 3-per-side ladders |
| 3 Accuracy & evidence (25) | 2 | 0.40 | 10.0 | D-1 close +18.5 off, four sessions of OHLC and RSI2 materially wrong, pivots from wrong day/week, unsourced §12/§14 figures, STOXX corroboration contradiction |
| 4 Reasoning & judgment (20) | 3 | 0.65 | 13.0 | Pillars conclude, one-sentence forecast; USD translation mechanism self-contradictory; all three cards depart from M5 rules |
| 5 Currency & transparency (15) | 3 | 0.65 | 9.75 | Dated and flagged, anchor caveat present; calendar misses D-day events and mis-states NFP; restriction breach |
| **Total** | | | **57.75 → 58** | |

Total 58 → band **Low** (40–59). Override check: hallucinated_source — not triggered (no impossible/fabricated URL or source demonstrated; contradictions logged under 3.2 and 3.4); restriction_breach — **triggered** (cap 74 not binding; C1 lowered 3→2).

## 4. Card Integrity (linter rows copied verbatim from `qa/ftse_qa1/lint_static/2026-07-06.csv`; separate from the 100)

| card_id | strategy | flags | dud | card score |
|---|---|---|---|---|
| 2026-07-06_Trade_1 | Trade 1 - Daily Directional (LONG — TREND_UP regime) | CLEAN | False | 100 |
| 2026-07-06_Trade_2 | Trade 2 - Pivot (regime-aware, TREND breakout side) | WARN_TP3_ORDER | False | 90 |
| 2026-07-06_Trade_3A | Trade 3 - Momentum-Pullback (3A) | CLEAN | False | 100 |

Report-level Card Integrity = mean(100, 90, 100) = **96.7** · n_cards=3 · n_duds=0 · n_warns=1. (Static linter is clean on two cards; the construction defects against M5 rules are scored in 4.5 and listed in the feedback file.)
