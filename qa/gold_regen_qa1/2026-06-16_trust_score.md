# Trust Score — XAUUSD — 2026-06-16

Report: `reports/md/Gold_Report_16Jun2026.md` · Run: `gold_regen_qa1` · Reviewer basis claimed by
report: **spot, loco London, continuous (24h) / OTC London spot, immediate settlement, T+2**
(§2 Market Definition) → checked against `_full` columns of `data/levels/XAUUSD_by_date/2026-06-16.csv`
(`last_bar_date`=2026-06-15 < D=2026-06-16, confirmed leak-free before use). `atr14_full` = 122.755
(the `_full` basis fits materially better than `_cash` on every OHLC field checked — see §1 below).

## 1. Section 7 checklist

| Item | Notes | Evidence | Score | Action |
|---|---|---|---|---|
| 1.1 Variables respected | Asset/units/sources/lookback mostly correct (XAU/USD loco London not COMEX; USDX first counter in §10; 5d/25d lookback stated in §2; ≥6 sources listed in §4, but one — Twelve Data — is explicitly "Excluded (stale/offset)," leaving effectively 5 usable inputs into the consensus build against the ≥6 requirement). More materially: the daily-open-anchor cell in §2 reads "Daily-open anchor set to 07:00 UK for this run (override of the standard 00:00 UK reset)" — this names both values and is logged again in §20 ("overridden to 07:00 UK for this run"), which is better disclosure than a silent switch, but §2 and §21b's Trade 1 Entry field then use 07:00 UK exactly as if it *were* the instance's governing anchor value for pricing, rather than repeating the non-conformance framing at the point of use, which M1_Variables_v2_1 §H.1 explicitly forbids ("never presented as the instance's anchor value"). | §2, §20, §21b | 3 | List the anchor-override wording and the <6-effective-source count as the two Variables not cleanly respected; regeneration must frame 07:00 UK as a logged non-conformance at every point of use (card, §21b, §2), not as the run's anchor, and either source a 6th independent price feed or state explicitly why 5 is sufficient. |
| 1.2 Coverage & currency consistent | Every date used is D-1 (15 Jun) or earlier for data, D (16 Jun) for the session; no USD/oz vs ticks drift (Trade 1: 167.8/16,776=0.0100 USD/tick; Trade 2: 31.9/3,186≈0.0100 USD/tick — consistent tick size). | whole report | 5 | — |
| 1.3 Audience & tone | Senior Commodities Analyst register maintained throughout §1, §18; no retail tone. | §1, §18 | 5 | — |
| **Category 1 avg** | (3+5+5)/3 = 4.33 → **4** | | | |
| 2.1 Sections present & ordered | All §1–§21 present in the specified order, including §13a–d and §21a–d. | headings | 5 | — |
| 2.2 Scorecard as table | §6 is a real table but uses Date/Open/High/Low/Close/RSI2/Trend/Validation — it collapses the spec's Source A/Source B columns into a single "Trend" column, losing the two-source-per-row structure the spec calls for (more than the trivial "Outcome" substitution seen in other runs). §11 pivot tables are correctly ordered R3→P→S3 with exactly 3 levels each side for daily, weekly and monthly — matches the spec exactly. | §6, §11 | 4 | Restore explicit Source A / Source B columns in §6 alongside Trend/Validation. |
| 2.3 Method steps visible | §4→§5 shows observation→normalisation→consensus with the futures-to-spot adjustment stated as an explicit range (~$30–$40 contango, better disclosed than a qualitative-only statement); §8 full candle-by-candle; §9 regime with persistence/overlap/VOLator/KER; charts present as captions only (docx→md image loss, not scored per brief). | §4–§9 | 5 | — |
| **Category 2 avg** | (4+5+5)/3 = 4.67 → **5** | | | |
| 3.1 Quantitative claims sourced | Most §1/§12/§14 claims carry a source or point to §4/§13. But several §12/§14 assertions are unsourced to any named article: "Singapore announced an OTC gold clearing system" (no article in §13a covers this), "Central-bank accumulation (PBoC, RBI and others)" (no dataset/survey named), and §14's "commentary notes short-covering running well ahead of fresh long-buying" (unnamed "commentary"). Combined with the OHLC/pivot sourcing failure at 3.4, this is a material, not trivial, gap. | §12, §14 | 2 | Name a specific source for the Singapore clearing-hub claim, the PBoC/RBI accumulation claim, and the short-covering-positioning claim, or drop them. |
| 3.2 Citations exist & contain data | Spot-checked Reuters (Streible/UBS, 15 Jun 12:42 GMT), UBS (Staunovo), and Investing.com spot close (4,314.33, used consistently in §1/§3/§4/§6/§21b). All three are named, dated, and used consistently; no self-contradiction or impossible date found; no fabrication detected. | §4, §13a | 4 | — |
| 3.3 Calculations transparent | RSI2 reproduces exactly from the report's own five stated closes (last two changes both gains → RS→∞ → RSI=100, matching the report's stated 100.0). Daily pivot P=(H+L+C)/3 reproduces exactly from the report's own (wrong, see 3.4) 12 Jun inputs — the arithmetic is correct, the input session is not. ATR(14) is never stated as an explicit figure anywhere in the body; it must be algebraically inferred from the 3×ATR cap ($4,684.02) and the 0.25×ATR stop buffer (backs out to ≈USD 123.2, close to the file's 122.755, but not disclosed as a number, contrary to the framework's "ATR(14) stated" requirement). §21a's direction score is only partially reconciled: the five contributions it names (+0.25, +0.07, +0.05, −0.10, −0.04) sum to +0.23, not the stated total of +0.27/+0.273 — one of the six weighted signals (weights 0.25/0.20/0.10/0.15/0.15/0.15 per §20) is entirely unaccounted for in the narrative (almost certainly the cross-asset signal, ≈+0.04 missing). | §6, §11, §21a | 2 | State ATR(14) as an explicit USD figure in §9/§21; name and quantify all six signal contributions in §21a so they sum to the stated score. |
| 3.4 Numbers reconcile — internally AND against the level file | **Internally:** the D-1 close (4,314.33) is identical across §1/§3/§4/§6/§21b; §11 pivots match both trade cards exactly (Trade 1 stop-anchor S1=4,177.38, Trade 2 entry/stop built from P=4,211.96/R1=4,253.89/S1=4,177.38) — internally self-consistent, but consistently wrong (see below). **Externally, against `XAUUSD_by_date/2026-06-16.csv` (`_full`):** the 15 Jun Open (4,219.32 vs `prev_open_full` 4,268.73, diff USD 49.41) and Low (4,211.80 vs `prev_low_full` 4,265.62, diff USD 53.82) are both Category-3 failures (>USD 24.55); High (24.11) and Close (5.15) land in the discrepancy band, not failures. **The dominant defect: §11's entire daily pivot table is computed from the wrong prior session.** §11 labels it "Daily (prior session 12 Jun)" and its P (4,211.96) reproduces exactly from the 12 Jun H/L/C already shown in the report's own §6 — but D-1 for session 16 Jun is 15 Jun (Monday), which the report's own §6 table already has validated (H 4,345.40 / L 4,211.80 / C 4,314.33). Checked against the file's correctly-dated `d_full_*` pivots (built from 15 Jun), all seven daily levels fail by USD 55–137 (P diff 102.81, R1 diff 110.03, S1 diff 82.65, R2 diff 130.19, S2 diff 75.43, R3 diff 137.41, S3 diff 55.27 — all vastly exceed the USD 14.12 failure threshold). By contrast, the **weekly** pivot table (correctly labelled "W/E 12 Jun," the last complete week before D) matches the file's `w_full_*` almost exactly (largest diff USD 1.97, all seven levels consistent), and the **monthly** table (May) matches `m_full_*` almost exactly (largest diff USD 0.56) — confirming the staleness is isolated specifically to the daily pivot's input session, not a systemic sourcing failure. The 25-session boundary cited for Trade 3C ($4,804 up / $3,993 down) also fails against the file (`swing_high_25d_full`=4,773.37, diff 30.63; `swing_low_25d_full`=4,023.91, diff 30.91), though this does not change the suppression conclusion. RSI2 (100.0) and ATR14 (≈123.2 inferred) both match the file closely (diff 0 and diff ≈0.5 respectively). | level file cross-check | 1 | See feedback file — rebuild the daily pivot table from the 15 Jun D-1 OHLC (already validated in §6), propagate the corrected P/R1/S1/R2/S2/R3/S3 into §15/§16/§21b, and correct the 25-session boundary citation. |
| **Category 3 avg** | (2+4+2+1)/4 = 2.25 → **2** | | | |
| 4.1 Each pillar reaches a conclusion | §8 "V-reversal / transition... vulnerable to a pause"; §9 "TRANSITION"; §10 "MIXED"; §12 each subsection bold-tagged Supportive/Mixed/Neutral-to-supportive; §14 has a clear narrative implication (rates re-rating, positioning caveat) but ends less crisply labelled than the other pillars. | §8–§10, §12, §14 | 4 | — |
| 4.2 Peer/cross-asset interpreted | §10 gives an explicit mechanism per counter (USDX/SPX/DAX) and explains why the equity/gold co-rise is a shared-driver effect rather than a contradiction, not a bare correlation list. | §10 | 5 | — |
| 4.3 Synthesis reconciles tensions | §9 names the KER-vs-VOLator dual-gate disagreement explicitly; §16 respects the TRANSITION regime rather than asserting a clean trend; §21a explicitly states no conflict with §17. §18's Reasons do not carry the KER-vs-regime tension forward as explicitly as §9 does. | §15–§18, §21a | 4 | — |
| 4.4 Calibrated language | §17 is one sentence, no hedge-stacking; confidence stated (Medium, §3/§18); "likely/provided/capped" language used appropriately. | §3, §17 | 5 | — |
| Card construction (M5, feeds Category 4) | Trade 1: static integrity all reproduces (stop side correct, TP1/TP2 ordered, R=167.76 within [0.3,3.0]×ATR, TP1 within 2.5×ATR, anchor explicit) but a genuine internal inconsistency: the stop-anchor cell cites daily S1 as $4,177 while the thesis-invalidation cell cites "daily S1" as $4,170 — the latter is actually the 12 Jun session low (4,170.02, §6), not the daily S1 figure the report itself states (4,177.38); conflating the two under one label is a card-construction defect. Trade 2's entry (4,216.15) sits USD 98.18 **below** the report's own D-1 close (4,314.33) despite being framed as a forward "breakout side only" TRANSITION order — because it is built on the same stale 12 Jun pivot inputs, the level has already been passed by price and is not a forward-looking breakout trigger at all. This is a direct downstream consequence of the 3.4 pivot-staleness defect, but it is also a card-construction failure in its own right: a breakout entry should sit ahead of, not behind, the current close. | §21b; `cards/baseline/gold/by_date/2026-06-16.json` | 3 | Rebuild Trade 2 entirely once the daily pivots are corrected (it should then sit above the D-1 close, as a genuine breakout order); align the two S1 citations in Trade 1. |
| **Category 4 avg** | (4+5+4+5+3)/5 = 4.2 → **4** | | | |
| 5.1 Data dated; staleness flagged | Every price/article in §4/§6/§13 is dated and 11–15 Jun is explicitly flagged single-source-indicative. But the daily pivot table's use of a 3-sessions-stale prior period (12 Jun, when 15 Jun was already validated in §6) is dated ("prior session 12 Jun") but never flagged as a staleness choice or explained — the report gives no indication it is aware a more recent session was available and skipped. | §4, §6, §11 | 2 | Flag or fix the daily-pivot staleness explicitly. |
| 5.2 Assumptions up front | Futures-to-spot normalisation stated with an explicit size (~$30–$40, §5); anchor-override disclosed with both old and new values (§2, §20); single-source pivot propagation into both live cards' caveats is done correctly. | §21b, §19, §20 | 4 | — |
| 5.3 Red flags surfaced | §12/§15 carry the PPI/ECB hawkish tail, RSI2-overbought risk, and event-binary framing; §13d's 17 Jun FOMC collision is explicitly carried into Trade 1's caveats. | §12, §15, §21b | 5 | — |
| 5.4 Restrictions honoured | No module codes (M1–M5) or bracketed variable names appear in the body; instrument common names used throughout; GC=F correctly kept Directional/corroboration-only, never Core; no retail dealer premium issue found. | whole report | 5 | — |
| **Category 5 avg** | (2+4+5+5)/4 = 4.0 → **4** | | | |

## 2. Category roll-up

| # | Category | Max | Level | Multiplier | Points | Justification (one line) |
|---|---|---|---|---|---|---|
| 1 | Prompt adherence | 20 | 4 | 0.85 | 17.00 | Variables mostly respected; the daily-open-anchor is disclosed as an override but then used as if it were the anchor, and only ~5 of the required ≥6 price sources are actually usable. |
| 2 | Structural alignment | 20 | 5 | 1.00 | 20.00 | All §1–§21 sections present, correctly ordered; pivot tables correctly sized; scorecard is a real table with a minor column-naming gap. |
| 3 | Accuracy & evidence | 25 | 2 | 0.40 | 10.00 | The entire daily pivot table is built from the wrong prior session (12 Jun instead of D-1 = 15 Jun), failing all 7 levels by USD 55–137, while weekly and monthly pivots — correctly sourced — match the file almost exactly; 15 Jun Open/Low also fail. |
| 4 | Reasoning & judgment | 20 | 4 | 0.85 | 17.00 | Pillars, cross-asset mechanism and synthesis are strong; Trade 2's breakout entry sits behind the current close (a construction consequence of the stale pivots) and Trade 1 has a small S1-citation inconsistency. |
| 5 | Currency & transparency | 15 | 4 | 0.85 | 12.75 | Dating, red flags and restriction discipline are strong; the daily-pivot staleness is dated but never flagged as such, and ATR14/the §21a score breakdown are not fully disclosed. |

**Total = 17.00 + 20.00 + 10.00 + 17.00 + 12.75 = 76.75 → 77 / 100**
**Band: High Trust (75–89)**

## 3. Override check

- Hallucinated-source override: **not triggered.** Three-citation spot-check (Reuters/Streible, UBS/Staunovo, Investing.com) found each named, dated, and used consistently; no source is impossible or self-contradictory.
- Restriction-breach override: **not triggered.** No explicit prompt restriction (no synthesis, no module names, futures corroboration-only, instrument common names) is openly violated; the daily-pivot staleness is a data-sourcing/accuracy defect, not a stated-restriction breach.
- `override = none`

## 4. Card Integrity (separate score — linter rows copied verbatim, not re-derived)

| card_id | strategy | flags | dud |
|---|---|---|---|
| 2026-06-16_Trade_1 | Trade 1 - Daily Directional (LONG) | CLEAN | False |
| 2026-06-16_Trade_2 | Trade 2 - Pivot, TRANSITION breakout-side (LONG, indicative) | WARN_R_TINY(0.26xATR) | False |
| 2026-06-16_Trade_3C | Trade 3C - Momentum-Breakout (TRANSITION) | SUPPRESSED | False |

Per-card score = 100 − 40·(#DUD) − 10·(#WARN), floored at 0: Trade 1 = 100, Trade 2 = 90 (1 WARN;
Trade 3C suppressed, excluded from the mean per protocol).

**card_integrity = 95** (mean of the 2 non-suppressed cards) · **n_cards = 3** · **n_duds = 0** · **n_warns = 1**

---

## Score summary
```
c1=4
c2=5
c3=2
c4=4
c5=4
total=77
band=High Trust
override=none
card_integrity=95
n_cards=3
n_duds=0
n_warns=1
```
