# Trust Score — Gold_Report_08-Jun-2026.md (XAUUSD, D = 2026-06-08)

Run: `gold_regen_qa1`. Scored against `docs/AI_Output_Trust_Score_Framework_v3.7.txt` §4–7 as
anchored by `docs/QA_PROTOCOL_TRADE_CARDS.md` and amended by `qa/gold_regen_qa1/REVIEWER_BRIEF.md`.

Leak-safety check performed: `data/levels/XAUUSD_by_date/2026-06-08.csv` → `last_bar_date =
2026-06-05` < `date = 2026-06-08`. OK to use.

## 1. Section 7 checklist

| Row | Notes | Evidence | Score |
|---|---|---|---|
| 1.1 Variables respected | Asset/basis/USDX-first/lookback/≥6 sources all correctly observed. Three gaps: (a) §2 "As-of date" is stated as 8 Jun, the report date, not 5 Jun — the last completed session strictly before D that `M1_Variables_v2_1.md` §B defines AS_OF_DATE to be; (b) TICK_SIZE/TICK_NAME (required once §21 strategies are produced) are never declared as a field in §2 — only inferable from the "$0.01" parentheticals inside the cards; (c) the daily-open-anchor override (see below) is logged but never given a distinct converted clock time as the module requires. | §2, §20, §21b | 3 |
| 1.2 Coverage & currency consistent | Every date in §2/§6/§13/§21 is ≤ D−1 (news items dated 6–7 Jun are calendar dates before D, not trading data, so compliant). No USD/oz vs tick vs point drift found. | whole report | 5 |
| 1.3 Audience & tone | Institutional, no retail tone throughout; consistent with a Commodities-desk risk audience. | §1, §18 | 5 |
| 2.1 Sections present & ordered | All of §1–§21 present, correctly numbered, 13a–d and 21a–d present. | headings | 5 |
| 2.2 Scorecard as a table | §6 is a proper table matching the required columns. §11 daily pivots are a proper table (R5→P→S5, a superset of the required R3→P→S3 — not a defect). **Weekly and monthly pivots are not rendered as tables at all** — only a footnote claims they are "enabled in configuration," which the report then fails to deliver. | §6, §11 | 2 |
| 2.3 Method steps visible | §4–§5 observations→consensus shown (no futures-to-spot step needed — no COMEX source was actually used). §8 candle-by-candle present. §9 regime shown with overlap/persistence/VOLator/KER values. §7 chart placeholders present (headings only, no caption text — accepted per brief, conversion artifact). | §4–§9 | 4 |
| 3.1 Quantitative claims sourced | Most figures trace to §4/§6/§13. Two unsourced hanging figures found: 10-year yield 4.54% (§14) and VIX +39.7%/21.51 (§14) carry no source or date. | text | 4 |
| 3.2 Citations exist & contain data | Spot-checked TradingEconomics, TexMetals, forex.com: each is named, dated, and its derivation quote is consistent with the figure used elsewhere. No fabrication found. | §4, §13a | 4 |
| 3.3 Calculations transparent | RSI2 = 0 reproduces exactly from the report's own 5 stated closes (last two changes both losses → RS = 0). Daily pivots (P/R1-3/S1-3) all reproduce exactly from the report's own stated Friday O/H/L/C. KER stated numerically (−0.95). **But ATR14 is never stated as a number anywhere**, and the §21a direction score (−0.62) is asserted with no per-signal weight×score breakdown shown. | §6, §11, §9, §21a | 3 |
| 3.4 Numbers reconcile — internal + level file | Internally consistent (D−1 close ≈$4,339–4,340 throughout §1/§3/§4/§6/§21b; pivots reproduce from the report's own OHLC). **Externally, three separate failures against `data/levels/XAUUSD_by_date/2026-06-08.csv` (`_full` basis, matching the report's own "spot, loco London" claim):** Friday close $4,339.60 vs file $4,327.70 (diff $11.90 > 0.115×ATR14 fail threshold $11.66); RSI2 0 vs file 21.6854 (diff 21.69 > 15-pt fail threshold); ATR14 implied ≈$61 (from "$170 range ≈2.8×ATR" and "3×ATR cap ≈$184") vs file's true atr14_full = 101.4343 (rel. diff ≈40%, fails the 25% threshold) — and this implied ATR is itself internally inconsistent with a THIRD implied ATR ≈$32.5 from Trade 1's stop derivation ("P + 1.3×ATR" = $42.3). Daily pivots R1/S1/R2/S2/R3/S3 are each in the 4–8 discrepancy band (not individual failures) — this is the close error propagating through P=(H+L+C)/3, not a separate defect. | cross-section + level file | 1 |
| 4.1 Pillars conclude | §8, §9, §10, §12 each end in a clear direction label. §14 ends descriptively without a clean directional label. **Card construction (scored here per brief §"Card construction is ALSO scored under Category 4"): Trade 1's stop is derived from an undocumented "P + 1.3×ATR" method rather than M5's specified tighter-of(5-day swing extreme, nearest S/R)+0.25×ATR (capped 3.5×ATR); the level file's true anchor would be the daily R1 (4,435.50, tighter than the 5-day swing high 4,545.87), giving a rule-compliant stop ≈4,460.86, not the report's 4,420.0. Trade 3C's levels (stop 4,372.0; TP1 4,246; TP2 4,183; TP3 4,103.97) do not match M5's 3C transition-breakout formula (stop = 25-day boundary + 0.40×width; TP1/TP2 = +1.0×/1.5×width) — using the file's swing_low_25d_full (4,311.82) and width (461.55), the formula gives stop ≈4,496.44 and TP1 ≈3,847.45, nothing like the card's values.** | those sections, §21b | 3 |
| 4.2 Peer/cross-asset interpreted | §10 gives a stated mechanism for each counter (opportunity cost, haven-flow substitution, high-beta partner), not a bare correlation list. | §10 | 5 |
| 4.3 Synthesis reconciles tensions | §15/§16/§18 explicitly address the equity/gold divergence; §21a explicitly reconciles itself against §17 ("No conflict with §17 — both lean short"). | §15–§18, §21a | 5 |
| 4.4 Calibrated language | §17 is one (long, dense but not hedge-stacked) sentence. Confidence stated (Medium, §3). | §3, §17 | 4 |
| 5.1 Data dated; staleness flagged | All prices/articles dated; monthly pivots explicitly flagged as "carried as directional" (indicative). | §4, §6, §13, §19 | 5 |
| 5.2 Assumptions up front | No futures-to-spot conversion needed this run (none applied, correctly). Anchor override IS logged on the card and in §20 (compliant framing — presented as a non-conformance, not as the instance anchor) **but never states the actual converted UK/broker time**, which `M1_Variables_v2_1.md` §H.1 requires alongside the override log. | §21b, §19, §20 | 3 |
| 5.3 Red flags surfaced | §12/§15 risks present; §13d CPI collision explicitly carried into all three card caveats. | §12, §15, §21b | 5 |
| 5.4 Restrictions honoured | No synthesized price presented as sourced; no bracketed variable names or module codes (M1..M5) leaked into the body (checked by grep); no framework name exposed; instrument common names used throughout. | whole report | 5 |

## 2. Category roll-up

| Cat | Rows (raw) | Mean | Level | Multiplier | Max | Points | Justification |
|---|---|---|---|---|---|---|---|
| C1 Prompt adherence | 3, 5, 5 | 4.33 | 4 | 0.85 | 20 | 17.00 | Solid but for the as-of-date mislabel, undeclared tick spec, and under-specified anchor override |
| C2 Structure | 5, 2, 4 | 3.67 | 4 | 0.85 | 20 | 17.00 | All sections present and ordered, but weekly/monthly pivot tables are claimed-but-missing |
| C3 Accuracy & evidence | 4, 4, 3, 1 | 3.00 | 3 | 0.65 | 25 | 16.25 | OHL match the level file closely; Close, RSI2 and (implied) ATR14 all fail their tolerance bands against the leak-free file |
| C4 Reasoning & judgment | 3, 5, 5, 4 | 4.25 | 4 | 0.85 | 20 | 17.00 | Strong synthesis and cross-asset mechanism; card-construction derivations for Trade 1 and Trade 3C deviate materially from the fixed M5 formulas |
| C5 Currency & transparency | 5, 3, 5, 5 | 4.50 | 5 | 1.00 | 15 | 15.00 | Dating, red-flag surfacing and restriction discipline are clean; anchor-override time-statement is the one recorded gap |

c1=4
c2=4
c3=3
c4=4
c5=5

## 3. Total, band, override

total=82
band=High
override=none

No fabricated source found among spot-checked citations (3.2). No prompt restriction openly breached — no bracketed variable, module code, or framework name found in the body; no retail-dealer premium or synthesized price presented as sourced (5.4).

## 4. Card Integrity (linter rows, copied verbatim from `qa/gold_regen_qa1/lint_static/2026-06-08.csv`)

| card_id | flags | dud | #DUD | #WARN | score = 100 − 40·DUD − 10·WARN |
|---|---|---|---|---|---|
| 2026-06-08_Trade_1 | UNPRICED | True | 1 | 0 | 60 |
| 2026-06-08_Trade_2 | CLEAN | False | 0 | 0 | 100 |
| 2026-06-08_Trade_3C | CLEAN | False | 0 | 0 | 100 |

card_integrity=86.7
n_cards=3
n_duds=1
n_warns=0

(Card Integrity is separate from the 100-point total per protocol.)
