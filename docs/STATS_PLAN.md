# Statistical plan

**Unit of analysis.** Blended R per card (mean of three units; non-filled = 0). Cards are three per
day on one instrument, usually same direction: they are not independent. **Effective N = report dates
(54)**, not cards (159). Every headline test respects this.

**Primary comparison** — baseline cards vs regenerated cards, same policy, same data:
1. Paired by `card_id`: Wilcoxon signed-rank on non-zero differences; sign test; mean/median difference.
2. **Daily-block bootstrap** of the total-R difference (resample dates with replacement, 5,000 draws) →
   95% CI and P(diff ≤ 0). This is the headline number.
3. Fill-rate difference (two-proportion z); dud-rate and defect-rate difference (same).
4. Mann–Whitney on filled-card R distributions; win-rate change.
5. By family (Trade 1 / 2 / 3A / 3C) and by month, same tests where n allows.

**Multiple draws.** Regenerate k = 3–5 card sets per date (different seeds / fresh sessions). Report the
distribution of total R across draws and the fraction beating baseline. Compare distributions, not one draw.

**Across policies** — repeat 1–5 for each of `card`, `usopen`, `midnight`, `band0845`, and the `--be tp1`
variant. A result that holds under one policy only is a policy artefact, not a card-quality effect.

**Trust Score as a covariate.** Regress per-report total R (baseline and regenerated) on the report's
Trust Score and Card Integrity score. If QA score predicts outcome in the baseline, the QA rubric has
validity; if regeneration raises the score but not the outcome, the rubric is measuring the wrong thing.

**What counts as a result.** Block-bootstrap CI excluding zero AND consistent sign across ≥3 of 4 policies
AND ≥ 60% of draws beating baseline. Anything less is reported as "suggestive".

**Outputs.** `results/compare/<name>.md` (tables), `results/compare/<name>.png` (equity overlays),
`results/compare/<name>_stats.csv`. `engine/stats.py` and `engine/equity.py` produce them.
