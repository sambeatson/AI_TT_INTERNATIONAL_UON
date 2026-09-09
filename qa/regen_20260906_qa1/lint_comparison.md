# Stage 3 — Lint comparison

RUN_ID `regen_20260906_qa1` · asset US500 · data `data/raw/US500_p_M15.csv`
Inputs: `lint_baseline.csv` (159 cards), `lint_draw1.csv` (162 cards, draw K=1).

Both sets were linted post-hoc with full data, as P3 permits. Suppressed cards are emitted as
`SUPPRESSED` and are excluded from every rate below; the denominator is **live (non-suppressed)
cards**, which differs between the arms and is stated explicitly wherever it matters.

## 1. Headline

| | baseline | regen draw1 |
|---|---:|---:|
| cards in registry | 159 | 162 |
| suppressed | 20 (12.6%) | 69 (42.6%) |
| **live cards (denominator)** | **139** | **93** |
| CLEAN | 62 | 51 |
| **clean rate** | **44.6%** | **54.8%** |
| cards carrying ≥1 flag | 77 (55.4%) | 42 (45.2%) |
| cards carrying a DUD flag | 3 (2.2%) | **0 (0.0%)** |

**Regenerated cards still carrying a DUD flag: none.** There are no Stage 2 failures to report
under P3 step 3.

The three baseline duds, for the record — all Trade 2 (pivot pullback) cards:

| card_id | flag |
|---|---|
| `2026-05-18_Trade_2` | DUD_TP2_ORDER (TP2 not beyond TP1) |
| `2026-06-29_Trade_2` | DUD_TP1_SIDE (TP1 on the wrong side of entry) |
| `2026-07-13_Trade_2` | DUD_TP1_SIDE |

## 2. Flag counts per type

Counts are flag instances (a card can carry several). Rates are per live card in that arm.

| flag | class | base n | base % | regen n | regen % |
|---|---|---:|---:|---:|---:|
| STALE_ANCHOR | market-relative | 25 | 18.0 | 24 | 25.8 |
| WARN_R_TINY | static (ATR, D-1) | 17 | 12.2 | 3 | 3.2 |
| MISPLACED_STOP | market-relative | 15 | 10.8 | 3 | 3.2 |
| MISPLACED_LIMIT | market-relative | 11 | 7.9 | 14 | 15.1 |
| WARN_TP3_ORDER | static | 10 | 7.2 | 0 | 0.0 |
| WARN_TARGET_FAR | static (ATR, D-1) | 10 | 7.2 | 0 | 0.0 |
| WARN_R_HUGE | static (ATR, D-1) | 3 | 2.2 | 0 | 0.0 |
| MALFORMED_FILL | market-relative | 3 | 2.2 | 1 | 1.1 |
| WARN_DUPLICATE | static | 2 | 1.4 | 0 | 0.0 |
| DUD_TP1_SIDE | static | 2 | 1.4 | 0 | 0.0 |
| DUD_TP2_ORDER | static | 1 | 0.7 | 0 | 0.0 |

**Every purely static defect class is eliminated.** Ladder inversion, unreachable TP1, over- and
under-sized R, duplicated cards and both dud classes all go to zero; WARN_R_TINY falls 17 → 3.
These are the classes the module edits were aimed at (M5 §9a pre-emit checklist, the risk-floor and
ladder-monotonicity gates), and on those the regeneration does what it was supposed to do.

## 3. The market-relative flags need a different denominator

STALE_ANCHOR, MISPLACED_LIMIT, MISPLACED_STOP and MALFORMED_FILL are not construction checks. The
linter compares each level against `anchor_price(D, anchor_broker)` — the **day-D open at the card's
own anchor time** (`engine/linter.py:69–76`), which is information the card author did not have. A
correctly-sided pullback buy struck at daily S1 is flagged MISPLACED_LIMIT if price gapped through
S1 overnight. So these four measure *how far the market moved between the report and the anchor*,
mixed with genuine mis-siding, and cannot be read as defect rates.

They also only apply to the matching entry mode, so the per-arm live-card denominator is wrong for
them. Per-mode:

| | baseline | regen draw1 |
|---|---|---|
| entry-mode mix (live) | LIMIT 58, MARKET 36, STOP 36, CONDITIONAL 9 | LIMIT 43, MARKET 38, STOP 12 |
| STALE_ANCHOR / MARKET card | 25/36 = 69.4% | 24/38 = 63.2% |
| MALFORMED_FILL / MARKET card | 3/36 = 8.3% | 1/38 = 2.6% |
| MISPLACED_STOP / STOP card | 15/36 = 41.7% | 3/12 = 25.0% |
| **MISPLACED_LIMIT / LIMIT card** | **11/58 = 19.0%** | **14/43 = 32.6%** |

Three of the four improve on the correct denominator. **MISPLACED_LIMIT gets worse, and the
per-mode view makes it worse, not better: 19.0% → 32.6% of limit orders sit on the unfavourable
side of the day-D anchor.** I am not going to explain that away as a gap artefact — the gap
exposure is common to both arms, drawn from the same 54 dates. Magnitudes are unchanged
(median |Δ| 19.5 → 20.8 pts, mean 23.4 → 24.4), so this is more limit orders being through the
anchor by about the same distance, not a few large ones.

The plausible mechanism is that the regenerated Trade 2 / Trade 3B cards are struck on
recomputed floor pivots from the broker feed rather than on the report's quoted (often
aggregator-derived) levels, and a broker-true S1/R1 sits closer to the prior close than the quoted
one did — so a larger share of them is already through by the 09:00 anchor. That is a hypothesis,
not a finding; **Stage 4 settles it**, because MISPLACED_LIMIT and fill behaviour are the same
question asked twice, and the resolver answers it in R rather than in flags.

STALE_ANCHOR barely moves in count (25 → 24) and rises as a share of live cards (18.0% → 25.8%),
purely because the live denominator shrank. On MARKET cards it improves slightly (69.4% → 63.2%),
and the **magnitudes fall materially: median |anchor − entry| 50.9 → 27.0 pts, mean 56.1 → 35.7,
max 121.3 → 98.5**. Regenerated MARKET cards are anchored closer to where the market actually
opened. That is consistent with the M5 rule requiring MARKET entry to be struck at the D-1 close.

## 4. Caveat on the shrinking denominator

The regenerated book suppresses 42.6% of slots against the baseline's 12.6%. A clean rate computed
over 93 cards is not directly comparable to one computed over 139: some of the improvement is
selection — cards that would have been flagged were declined instead of built badly. Under the
protocol that is a legitimate outcome (the suppression gates are part of what the QA feedback
tightened), but it means **the clean-rate improvement in §1 is an upper bound on construction
quality gain**, and the honest read is §2: the static classes go to zero on cards that were
actually emitted.

Whether declining two cards in five is *good* is not a lint question. It is an R question, and
suppressed cards score 0R, so a heavily-suppressed book is pulled mechanically toward zero.
Stage 5 therefore reports total R, mean R conditional on filling, and the fill-rate difference
separately — a total-R comparison alone would confound card quality with card count.

## 5. Reproduce

```
python engine/linter.py --cards cards/baseline/cards_baseline.csv \
    --data data/raw/US500_p_M15.csv --out qa/regen_20260906_qa1/lint_baseline.csv
python engine/linter.py --cards cards/regenerated/regen_20260906_qa1/cards_regen_20260906_qa1_draw1.csv \
    --data data/raw/US500_p_M15.csv --out qa/regen_20260906_qa1/lint_draw1.csv
```
