# Stage 1 summary — `gold_regen_qa1` (XAUUSD, 57 reports)

57 reports, 2026-05-11 → 2026-07-31, each scored in its own isolated session against Trust Score
v3.7. Every session had that date's leak-free level file (`data/levels/XAUUSD_by_date/<D>.csv`,
computed only from bars strictly before D) and its own static lint rows, and nothing else — no
`results/`, no `data/raw/`, no other date, no later report.

Roll-up: `trust_scores.csv`, built and validated by `engine/qa_rollup.py`. Every stated total
reconciles with the recomputation from its category levels, every band matches its total, and every
override is consistent with its C3. **No problems.**

## 1. Distribution

| | |
|---|---|
| total | mean **71.5**, sd 9.1, median 73, range **49–86** |
| bands | Moderate 28 · High 23 · Low 6 · **Very High 0** |
| overrides | none 41 · restriction_breach 14 · hallucinated_source 2 |
| Card Integrity | mean 96.0, min 60.0, at 100 on 27 of 57 |
| linter totals | 10 duds, 118 warns across 171 cards |

Category levels (0–5):

| category | max | mean | distribution |
|---|---:|---:|---|
| C1 Prompt adherence | 20 | 3.68 | 2:4 · 3:17 · 4:29 · 5:7 |
| C2 Structure | 20 | 4.09 | 2:2 · 3:7 · 4:32 · 5:16 |
| **C3 Accuracy & evidence** | 25 | **2.16** | **0:3 · 1:7 · 2:25** · 3:22 · 4:0 · 5:0 |
| C4 Reasoning & judgment | 20 | 3.68 | 2:2 · 3:15 · 4:39 · 5:1 |
| C5 Currency & transparency | 15 | 3.74 | 2:2 · 3:19 · 4:28 · 5:8 |

**No report scored above 3 on Category 3.** Not one of 57. **35 of 57 scored 2 or below.** By
contrast C2 and C4 sit near 4. The gold reports are well-structured and reasoned; their numbers do
not reconcile with the market they are about.

Stability across months (mean total 72.3 / 71.0 / 71.3 and mean C3 2.20 / 2.15 / 2.14 for May / June
/ July) says this is the steady state of the process, not a bad patch.

## 2. What the reviewers found

The counts below come from keyword-matching the 57 feedback files. **They are indicative, not
adjudicated** — a match means the theme is discussed, not that the defect was confirmed on that
date. The override counts in §1 and the category levels are the authoritative numbers; these are
here to show relative weight.

| theme | files mentioning | |
|---|---:|---|
| an M5 card-construction rule violated | 43/57 | |
| bracketed variables / module codes in the body | 42/57 | 14 rose to a scored override |
| a corroboration label unsupported by the report's own evidence | 29/57 | |
| ATR14 understated or never stated | 27/57 | |
| a pivot tier built from the wrong period | 25/57 | |
| RSI2 not reproducing from the report's own closes | 24/57 | |
| OHLC / pivots failing the level file | 22/57 | |
| §21a direction score not summing from its components | 11/57 | |
| break-even trail on the wrong side for a SHORT | 8/57 | |

### 2.1 The pivot tables are not derived from the report's own validated data

The decisive evidence is **2026-07-14**: its §11 daily-pivot inputs (H 4,102 / L 4,068.74 /
C 4,084.41) are a *different price set from its own §6 OHLC table for the same session*, while its
weekly table — built from another source again — matches the broker feed to within $1.30. Each
pivot tier is assembled independently from whatever figures are to hand.

That explains every variant seen: stale daily with clean weekly (2026-07-09, 2026-06-26), clean
daily with catastrophic monthly (2026-06-17: all 14 weekly and monthly levels out by $28–338), or
all three wrong. **2026-06-23** was back-solved by its reviewer: the monthly tier was computed from
the 25-day swing high and a "$4,539 peak" figure taken from narrative prose, not from May's H/L/C.
**2026-07-28**'s monthly P is out by $507.84 — 5.97×ATR.

### 2.2 The prior session is chosen wrongly, in both directions

- **2026-06-24** used the *in-progress* 24 June print as Trade 1's MARKET entry — the report
  reaching into the session it is trading.
- **2026-07-07** excluded a session that had already closed (6 July, confirmed complete by the level
  file) as "still in progress", falling back to 3 July, three sessions stale. Its reviewer noted the
  stale pivots landed numerically near the correct ones and explicitly declined to credit that,
  because the proximity is coincidence.
- **2026-06-03** is anchored a whole session behind D and never carries a true D−1 row at all.

### 2.3 ATR14 is understated by 26–68%, or absent

Stated values of $52–62 against true values of $92–122. On **2026-06-08** two implied values inside
one report disagree with each other by 2×. This is not only a labelling problem: ATR sets the
0.25×ATR stop buffer, the 3.5×ATR cap, and the 2×ATR swing-qualification gate.

**It therefore changes which cards exist.** On **2026-07-10**, Trade 3A was admitted as a "borderline
pass" on the 2×ATR swing gate, short by $2.20 (1.2%); recomputed on the true ATR it is short by
$24.16 (11.7%) — a clear fail. The baseline arm's suppression count is too low for this reason.

### 2.4 The corroboration label is emitted unconditionally

- **2026-07-10** certifies a 9 July low of 4,022.20 as "two-source corroborated" against a true
  4,054.23 — while its **own §4 table lists Kitco at 4,053.60 and Investing.com at 4,054.37**, both
  within a dollar of correct. It passed over the two quotes that agreed with the feed.
- **2026-06-30** labels every OHLC row "CORR" while its own footnote concedes a ~$25 source spread
  against a stated ±$0.50 tolerance — a label contradicted by the same page, 50× over.
- **2026-07-02** prints "Corrob. (Δ<$6)" on a high that is $105.58 out.

A gate that never fails is worse than no gate: it launders unverified figures as verified.

### 2.5 Suppression gates do not bind

Two distinct failures, needing different remedies:

- **Miscalibrated** — the ATR case above (2026-07-10, 2026-07-17), where a wrong input lets a card
  through a gate it should fail.
- **Ignored outright** — **2026-07-24**'s own §20 Agent Log records that Trade 3A's fib swing
  *failed* the 2×ATR gate (1.64×ATR); the card was built on that failed swing anyway, while the
  swing the log records as passing (2.05×ATR) is never used. The gate ran, was written down, and had
  no effect.

Relatedly, the §21a direction score fails to sum from its own printed components on at least three
dates (2026-06-23 stated −0.53 vs −0.64 disclosed; **2026-07-13 stated +0.14 vs −0.01 disclosed —
a sign flip**). Since |score| < 0.25 is the Trade 1 suppression gate, an unreproducible score means
the suppression decision is not auditable.

### 2.6 Card construction drifts from the fixed M5 formulas

Present even where the data is sound, so it needs its own remedy:

- SHORT cards trailing Unit 3 to entry **+** 0.2R — the losing side (8 files, several with 2–3 cards each).
- Trade 1 issued as STOP/LIMIT where market-at-anchor is fixed (2026-06-23, 2026-07-09, 2026-06-02).
- Trade 2 built on the wrong regime branch — fading a level under a TRANSITION call that routes to
  breakout-only (2026-06-02, 2026-07-02, 2026-07-23), or tiered at R3 where RANGE permits only
  R1/R1.5/R2 (2026-07-09, **2026-07-22** — where the wrong pivot pushed the entry outside the
  permitted set entirely).
- Trade 3 on the wrong variant, or the right variant with the wrong retracement (50% or 38.2% where
  57.5% is fixed: 2026-07-10, 2026-06-29, 2026-07-24), or the wrong coefficient
  (**2026-07-29**: boundary + 0.60×width where M5 fixes 0.40).
- Stop buffers of $1–4 where 0.25×ATR ≈ $20–30 is required — the direct cause of the linter's
  `WARN_R_TINY` flags.

### 2.7 Scaffolding leaks into the report body

`[DAILY_OPEN_ANCHOR]`, `[PRIMARY_ASSET]`, `[BE_TRAIL_R]`, `[CONVICTION_THRESHOLD]`, `regime_label`,
"M5 trace", "M2 §9c", "Step-4". **2026-07-16** carries them 25+ times including in its title and
footer. 14 reports took a scored restriction-breach override for this, capping each at Moderate and
docking C1 a level. It is the cheapest defect in the set to eliminate.

### 2.8 The daily-open anchor

`M1_Variables_v2_1.md` fixes `[DAILY_OPEN_ANCHOR]` to 00:00 UK **or** 07:00 UK, chosen once per
instance, "not re-selected at run time, per session, or to suit when an analysis happened to
finish"; a departure is "a logged non-conformance, not an anchor". 21 of 57 reports reference
07:00 UK and the rest 00:00 UK. No gold M1 instance ships with the package, so the populated value
cannot be read off and no report can be scored against it directly — but several reports present a
mid-run change *as* the instance anchor (2026-07-14 buries the disclosure in §20; 2026-05-26 and
2026-05-21 conflate the anchor time with the run's as-of date), which is the failure mode the rule
names explicitly.

## 3. Two findings about the rubric itself

**The Trust Score dilutes its own most decision-relevant failure.** C3 is one of five categories and
its four rows average together, so a total failure on row 3.4 (external reconciliation) is offset by
sound sourcing and transparent formulas elsewhere. **Nine reports score C3 ≤ 2 and still band
High.** 2026-05-21 sits in High Trust with row 3.4 at 0/5 — its own reviewer flagged that the band
label would materially under-state the report's central risk. 2026-07-01 scores 85 with a monthly
pivot table built on the wrong month, errors to $996.

**Card Integrity measures geometry, not compliance, and is near-uninformative here.** It is 96.0 on
average and exactly 100 on 27 of 57 reports — including **16 reports whose C3 is ≤ 2**. Its
correlation with the total is **0.046**, and with C3 **0.002**. A card can be struck on a pivot that
is $500 wrong, entered by the wrong order type, on the wrong regime branch, and still lint CLEAN,
because the linter only asks whether stop/TP1/TP2 are ordered and sized sanely.

This matters for reading the US500 run: a Card Integrity of 100 there was never evidence of a
well-constructed card either.

## 4. What Stage 2 must change

In priority order, by expected effect:

1. **Compute every level from the execution series.** §6's OHLC, §11's three pivot tiers, ATR14,
   RSI2 and the swing extremes must all come from one validated series for the last completed
   session strictly before D — the series orders actually fill against. This is a wiring change, not
   a tolerance change, and it removes §2.1–2.3 outright and most of §2.6 as a side effect.
2. **State ATR14 explicitly as a number**, from that same series, and derive every buffer, cap and
   qualification gate from it.
3. **Make corroboration conditional on a check that can fail**, and make the failure visible. A tier
   computed from the execution series is corroborated by construction and needs no flag; a tier
   struck from a quote must record the comparison and its outcome.
4. **Make gates bind.** A logged gate failure must suppress the card. The §21a score must reproduce
   from its printed components.
5. **Pre-emit scan for scaffolding** — bracketed tokens, module codes, internal field names.
6. **Per-card construction checklist** for the residue that survives correct inputs: entry mode,
   regime branch, variant letter, retracement percentage, coefficient, buffer, BE-trail direction.

Items 1–3 address the inputs; 4–6 address compliance. Both are needed: §2.6 shows construction
drifts even where data is sound, and §2.3 shows bad data changes which cards exist at all.

**Modules are edited next, from this summary and the 57 feedback files only — no results, no market
data, no report bodies.** The quarantine in `QUARANTINE.md` stays in force until Stage 2 completes.
