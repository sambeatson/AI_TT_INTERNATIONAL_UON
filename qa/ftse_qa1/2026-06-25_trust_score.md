# Trust Score v3.7 — FTSE 100 report for 2026-06-25

Report: `reports/md/FTSE_EuroStoxx_Report_25Jun2026.md` · D = 2026-06-25 · D-1 = 2026-06-24
Level file `data/levels/UK100_by_date/2026-06-25.csv`: `last_bar_date` = 2026-06-24, which is < D, so it is leak-free and used here.
Slice stats were run with `--cash-open 10:00 --cash-close 18:30` and `--closes` set to the report's five stated closes.
The report states a "London cash" basis, so Category 3 is compared on `_cash` (the `_full` figure is shown where it changes the reading).

## Scores (explicit)

```
c1=2
c2=3
c3=1
c4=3
c5=3
total=49
band=Low
override=restriction_breach
card_integrity=96.7
n_cards=3
n_duds=0
n_warns=1
```

The restriction breach is the module codes `[M3]`, `[M5]` and `[UPD]` left in headings, plus `(M5)` in the §20 agent log (brief §2 row 5.4). The restriction cap is Moderate (74). The Category 3 collapse already puts the total at 49, so the cap does not bind. C1 was dropped one level (3 to 2) for the breach.
No fabricated source was established, so `hallucinated_source` does not apply. The Bloomberg and "~10,454" official rows are weak and are recorded under row 3.2.

## 1. Section 7 checklist

### Category 1: Prompt adherence

| Row | Notes | Evidence | Score |
|---|---|---|---|
| 1.1 Variables respected | Asset is the FTSE 100 cash index, with the STOXX as a reference with no cards (§2). Counters are USDX, S&P 500 and DAX 40. Lookback is 5 sessions (18–24 Jun), GBP and index points, Europe/London. Anchor is 07:00 UK, stated in §2, §20 and Trade 1. Six "observations" are listed but only four distinct providers (Investing, Trading Economics twice, Yahoo, Bloomberg). None is a sell-side source, and the "LSE / FTSE Russell" official close is only "~10,454". The ≥6 sources across index-provider, exchange and sell-side tiers is weakly met. Module codes and bracket tags leak into headings (restriction). | §2, §4, §19, §20, headings §6/§7/§8/§9/§10/§11/§12/§13/§14/§20/§21 | 3 |
| 1.2 Coverage and currency consistent | The §4 evidence table contains a 23 Jun Yahoo row (D-2) and a "19–23 Jun" Bloomberg row. The S&P figure in §10 (~7,365, "down ~1.4% on 23 Jun") is a 23 Jun datum presented as the current counter read. On `US500` the 18:30 broker bar was 7,384.4 on 23 Jun and 7,423.3 on 24 Jun, so 24 Jun was a +0.5% rebound that the report omits. The PCE release is dated "this week" and the §13d date cell is `[object Object]`. The calendar has PCE, GDP, durable goods and jobless claims on D itself (15:30 broker = 13:30 London). GBP, points and Europe/London are consistent. | §4, §10, §13d | 3 |
| 1.3 Audience and tone | Institutional strategist register, no retail tone. | §1, §18 | 4 |

Mean = 3.33, which rounds to 3. The restriction-breach override drops it one level, so **C1 = 2**.

### Category 2: Structure

| Row | Notes | Evidence | Score |
|---|---|---|---|
| 2.1 Sections present and ordered | §1–§21 are all present and in order. Content defects: (a) §13b aggregate body is `[object Object]` ×4 and the numeric tilt is not shown (only "+0.30" in §20); (b) §13c is "Divergence" and the previous-period and upcoming calendars are merged into one §13d, where the brief expects 13c = previous calendar and 13d = upcoming; (c) §18 verdict body is `[object Object]` ×2; (d) §21a conviction table is `[object Object]`; (e) §11 gives daily pivots only, with no weekly or monthly tables despite saying they are "enabled". | §11, §13, §18, §21a | 3 |
| 2.2 Scorecard as a table | §6 is a table, but it has no Source A / Source B / Final columns, only a Validation column. §11 is a two-column table with R3 on the same row as P and S1 under R2, so it is not ordered R3→P→S3 per side. No weekly or monthly tables. | §6, §11 | 2 |
| 2.3 Method steps visible | §4–§5 show observations, consensus and the CFD down-weighting. §8 is candle-by-candle plus a sequence assessment. §9 has a regime table but gives no numeric KER, VOLator, persistence or overlap. Charts (§7) are captions only (accepted, pandoc drops images; five captions). | §4–§9 | 3 |

Mean = 2.67, so **C2 = 3**.

### Category 3: Accuracy and evidence

| Row | Notes | Evidence | Score |
|---|---|---|---|
| 3.1 Quantitative claims sourced | §4 and §6 are sourced at feed level. Several §1, §12 and §14 figures carry no source: "~80% overseas earnings", "70% Sept hike odds (up from ~29%)", "Segro +15%", "Shell/BP −3.6%", "gilt 10y 4.95%", "USDX 13-month high". The "~7,365" S&P level is wrong or stale (see 1.2). | §1, §10, §12, §14 | 3 |
| 3.2 Citations exist and contain data | Spot checks: (i) Trading Economics 24 Jun 10,454 (+0.24%): consistent with the 23 Jun close 10,428.85 (+0.241%). OK. (ii) Investing.com 24 Jun 16:35 10,454.0: plausible and consistent. OK. (iii) Bloomberg "19–23 Jun" 10,428.85: a date range quoting one value that equals only the 23 Jun close, while §6 has a different 19 Jun close (10,363.27). It is non-independent of the Yahoo 23 Jun row (identical to 2 d.p.) yet counted as "Corrob.". Also the "official" LSE/FTSE Russell row is "~10,454", an approximation and not an observed print. §3 and §6 claim three-feed corroboration of the D-1 close, but the Yahoo datum shown is 23 Jun. The §13a quotes are dated and consistent (23 Jun was a Tuesday). Trading Economics is tiered "Media" in two rows and "Inst./Official, wt 1.0" in another. No source is shown to be fabricated, but evidence quality is weak. | §3, §4, §6, §13a, §19, §20 | 3 |
| 3.3 Calculations transparent | RSI2 for 22/23/24 Jun reproduces from the report's own closes (100.0 / 89.2 / 73.6, `--closes` test), and the 19 Jun value cannot be tested. Daily pivots P/R1/S1/R2/S2/R3/S3 and R1.5/S1.5 reproduce exactly from the report's H/L/C 10,462.20 / 10,406.95 / 10,454.00. Failures: ATR(14) is never stated numerically (the cards imply ≈94, the level file has 112.29 cash / 136.42 full); the claim that ATR has "fewer than 14 true ranges" is false (57 prior sessions exist); KER is never stated numerically; the §21a score table is blank; Trade 2 entry 10,448 does not equal its own formula (P + 10%×(R1−P) = 10,444.46); the §13b tilt is not shown (13a recomputes to +0.32 vs the stated +0.30). | §6, §9, §11, §13, §21 | 2 |
| 3.4 Numbers reconcile / OHLC vs slice | See the tables below. D-1 close is identical in §1/§3/§4/§6/§21b (10,454) and within 1.1 pts of the cash close. Reconciliation failures: 18 Jun close is 61.6 pts off and 23 Jun close 24.2 pts off (both > 15 pts, a Category 3 failure per brief §4); only 9 of 20 OHLC fields are within tolerance; the 23 Jun and 24 Jun opens are identical (10,438.24); RSI2 differs from the slice-based RSI2 on four of five days; the 5-day swing low is 10,240 in the report vs 10,328.1 in the data; the entry/stop pivots on the cards reconcile to §11 but Trade 2 R, swing lows and backtest R-units do not reconcile. | §6, §8, §21 | 1 |

Section 7 mean = (3 + 3 + 2 + 1) / 4 = 2.25. Brief §4 makes a close more than 15 pts wrong (18 Jun and 23 Jun) and an RSI2 that does not match the data a Category 3 failure to score, and the 18 Jun row is wrong on all four fields by 60–190 pts. **C3 = 1.**

#### Report D-1 (24 Jun) vs level file (cash basis)

| Field | Report | `_cash` | Δ | `_full` | Δ | Within tol.? |
|---|---|---|---|---|---|---|
| Open | 10,438.24 | 10,422.2 | +16.0 | 10,426.3 | +11.9 | No (cash) |
| High | 10,462.2 | 10,468.6 | −6.4 | 10,468.6 | −6.4 | Yes |
| Low | 10,406.95 | 10,400.6 | +6.4 | 10,373.6 | +33.4 | Yes (cash) |
| Close | 10,454 | 10,455.1 | −1.1 | 10,450.5 | +3.5 | Yes |
| RSI2 | 73.6 (reproduces from own closes) | 100.0 | −26.4 | 100.0 | −26.4 | No |
| ATR14 | not stated (cards imply ≈94) | 112.29 | ≈ −18 | 136.42 | ≈ −42 | No |

#### Five-session OHLC vs slice (cash basis; tolerance 5 pts close, 10 pts O/H/L)

| Date | Field | Report | `_cash` | Δ | Verdict |
|---|---|---|---|---|---|
| 18 Jun | O / H / L / C | 10,268.4 / 10,341 / 10,240.1 / 10,338 | 10,460.3 / 10,475.8 / 10,372.6 / 10,399.6 | −191.9 / −134.8 / −132.5 / −61.6 | All four fail. The report's 18 Jun bullish body is a bearish body (C<O) in the data. |
| 19 Jun | O / H / L / C | 10,400.46 / 10,418.58 / 10,352.9 / 10,363.27 | 10,383.1 / 10,417.4 / 10,347.8 / 10,352.3 | +17.4 / +1.2 / +5.1 / +11.0 | O and C fail, H and L pass. The data shows a gap down, not "gapped up". |
| 22 Jun | O / H / L / C | 10,372.2 / 10,470 / 10,360 / 10,437.85 | 10,379.2 / 10,441.4 / 10,343.2 / 10,440.9 | −7.0 / +28.6 / +16.8 / −3.1 | H and L fail, O and C pass. |
| 23 Jun | O / H / L / C | 10,438.24 / 10,462.19 / 10,332.4 / 10,428.85 | 10,329.6 / 10,461.5 / 10,328.1 / 10,453.0 | +108.6 / +0.7 / +4.3 / −24.2 | O and C fail (C is −1.0 vs the full-day close 10,429.8, so it looks like a full-day basis mixed into a "cash" table), H and L pass. |
| 24 Jun | see table above | | | | O fails. |

Fields in tolerance: 9 of 20. Closes wrong by more than 15 pts: 18 Jun (−61.6) and 23 Jun (−24.2).

RSI2 on the cash closes versus the report's RSI2:

| Date | Report | Slice (cash) |
|---|---|---|
| 19 Jun | 100.0 | 0.00 |
| 22 Jun | 100.0 | 65.19 |
| 23 Jun | 89.2 | 100.00 |
| 24 Jun | 73.6 | 100.00 |

#### Pivots, report §11 (daily) vs level file `_cash`

| Level | Report | `_cash` | Δ |
|---|---|---|---|
| R3 | 10,530.4 | 10,550.27 | −19.9 |
| R2 | 10,496.3 | 10,509.43 | −13.1 |
| R1 | 10,475.15 | 10,482.27 | −7.1 |
| P | 10,441.05 | 10,441.43 | −0.4 |
| S1 | 10,419.9 | 10,414.27 | +5.6 |
| S2 | 10,385.8 | 10,373.43 | +12.4 |
| S3 | 10,364.65 | 10,346.27 | +18.4 |

P, R1 and S1 are within 10 pts, and R2, S2, R3 and S3 are 12–20 pts out (driven by the H/L input errors).
Weekly and monthly pivots are absent from the report, so nothing can be compared. Level-file references: weekly (2026-W25, cash) P 10,424.9 / R1 10,502.0 / S1 10,275.2 / R2 10,651.7 / S2 10,198.1 / R3 10,728.8 / S3 10,048.4. Monthly (2026-05, cash) P 10,370.4 / R1 10,599.6 / S1 10,180.8 / R2 10,789.2 / S2 9,951.6 / R3 11,018.4 / S3 9,762.0.

#### Other reconciliations recorded

- §7 caption "net positive on 4 of 5 sessions" does not match §6 (3 of 5: 18, 22 and 24 Jun) or the data (3 of 5).
- §1 "a fourth advance in five sessions" does not match the §6 closes (3 advances in 4 steps).
- 5-day swing: the report has 10,470 high / 10,240 low, while the data has 10,475.8 (18 Jun) / 10,328.1 (23 Jun).
- 25-day range, never used in the cards: cash 10,126.2–10,574.6.

### Category 4: Reasoning and judgment

| Row | Notes | Evidence | Score |
|---|---|---|---|
| 4.1 Pillars conclude | §8 ends in a constructive-but-unconfirmed read, §9 in TRANSITION, §10 in MIXED. §12 gives per-row stances but no aggregate label, and §14 ends on watch items with no direction label. | §8–§14 | 3 |
| 4.2 Cross-asset interpreted | The USDX translation mechanism is explicit. The S&P and DAX "contradicts" reads give only a risk-off mechanism. Oil and energy weighting is handled in §12, not §10. The counter levels used are stale or unverified (S&P). | §10 | 4 |
| 4.3 Synthesis reconciles tensions | §15 and §16 reconcile TRANSITION with the long bias, and §21a notes the regime. §18's verdict body is `[object Object]` and §21a's table is blank, so the §17 vs §21a reconciliation cannot be traced. | §15–§18, §21a | 3 |
| 4.4 Calibrated language | §17 is exactly one sentence with one condition. Confidence appears in §3 only. | §3, §17 | 4 |
| Card construction (protocol) | All three cards have construction defects: Trade 1 stop logic contradicts itself and TP3 sits below TP1 (linter WARN); Trade 2 is a buy-stop below the D-1 close with an arithmetic error and R below 0.3×ATR; Trade 3C uses a 5-day range built from a wrong low, not the 25-day boundary. See `2026-06-25_feedback.md`. | §21b | 1 |

Mean = (3 + 4 + 3 + 4 + 1) / 5 = 3.0, so **C4 = 3**.

### Category 5: Currency, restrictions and transparency

| Row | Notes | Evidence | Score |
|---|---|---|---|
| 5.1 Data dated, staleness flagged | The §13a article table has no dates. Counter levels (S&P ~7,365, DAX ~24,200, USDX ~101.6) are undated. Pivots are flagged single-source indicative where relevant. The D-1 evidence rows are mostly dated. | §4, §10, §13a | 3 |
| 5.2 Assumptions up front | The anchor-override caveat is in §2 and §20 but not in the Trade 1 caveats row. Trade 2's caveat covers the pivots. | §2, §20, §21b | 4 |
| 5.3 Red flags surfaced | §12 and §15 carry risks. The PCE collision is carried to Trade 1 and Trade 3C but not to Trade 2. PCE is not placed on D (13:30 London), and GDP, durable goods and jobless claims on D are not mentioned. The previous-period calendar omits the 18 Jun BoE decision (hold, 2 hike votes, HIGH impact) and the 23 Jun UK flash PMIs. The 23 Jun "resilient US PMI" is not in the supplied calendar, so it is unverified. | §13d, §21b | 3 |
| 5.4 Restrictions honoured | Breaches: bracketed module codes `[M3]`/`[M5]`/`[UPD]` in 11 headings and "(M5)" in §20. Concerns: a CFD print (10,462) sits in the §3 "corroborated band" and the §20 corroboration pair (Δ≈8 pt), and the 24 Jun high (10,462.2) tracks that CFD print. The STOXX "consensus" 6,012 is taken from a derived/CFD feed while §6 labels the same row CORROBORATED despite the 200–300 pt dispersion flagged in §3. `[object Object]` placeholder text appears 8 times (§13b ×4, §13d date cell, §18 ×2, §21a). Credit: the report states that no value was synthesised and flags single-source pivots. | headings, §3, §6, §19, §20 | 2 |

Mean = 3.0, so **C5 = 3**.

## 2. Category roll-up

| Category | Max | Level | Multiplier | Points | Justification |
|---|---|---|---|---|---|
| C1 Prompt adherence | 20 | 2 | 0.40 | 8.00 | Variables mostly respected (3.33 → 3), but module codes in headings breach a restriction, so −1. |
| C2 Structure | 20 | 3 | 0.65 | 13.00 | All 21 sections present, but §13b/§18/§21a bodies are blank and §13c/§13d mis-split; §6 lacks Source columns; no weekly or monthly pivots. |
| C3 Accuracy | 25 | 1 | 0.20 | 5.00 | 18 Jun row wrong on all fields (close −61.6); 23 Jun close −24.2; 9 of 20 OHLC fields within tolerance; RSI2 off the slice on 4 of 5 days; ATR and KER unstated. |
| C4 Reasoning | 20 | 3 | 0.65 | 13.00 | Pillar reasoning and the one-sentence forecast are sound; card construction defective in all three cards. |
| C5 Currency and transparency | 15 | 3 | 0.65 | 9.75 | Dated evidence and caveats mostly present; articles undated, calendar gaps, and restriction concerns. |

Total = 8.00 + 13.00 + 5.00 + 13.00 + 9.75 = 48.75, which rounds to **49**.

## 3. Total, band, override

- total = 49, band = Low (40–59).
- Override check: no fabricated source established, so no C3 = 0 override. A prompt restriction (no module codes or bracketed tags) is breached, so the cap is Moderate (74) and C1 is down one level. The cap is non-binding because the raw total is already 49.

## 4. Card Integrity (linter rows copied verbatim from `qa/ftse_qa1/lint_static/2026-06-25.csv`)

| card_id | strategy | flags | dud | card score |
|---|---|---|---|---|
| 2026-06-25_Trade_1 | Trade 1 - Daily Directional (LONG) | WARN_TP3_ORDER | False | 90 |
| 2026-06-25_Trade_2 | Trade 2 - Pivot, regime-aware (TRANSITION -> breakout side only, LONG) | CLEAN | False | 100 |
| 2026-06-25_Trade_3C | Trade 3C - Momentum-Breakout (TRANSITION regime) | CLEAN | False | 100 |

Report-level Card Integrity = mean(90, 100, 100) = **96.7** (3 cards, 0 DUD, 1 WARN). This is separate from the 100-point Trust Score.

Reviewer note, not a re-derivation: the Trade 2 and Trade 3C rows are CLEAN in static mode, yet a buy-stop of 10,448 sits below the D-1 close 10,454/10,455.1, and R = 24 pts is below 0.3×ATR14 (33.7 at the level file's cash ATR 112.29). Both are detailed in the feedback file. Card Integrity numbers above are the linter's, unmodified.
