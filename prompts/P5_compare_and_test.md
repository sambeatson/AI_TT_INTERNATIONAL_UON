# P5 — Compare and test

For each POLICY (and the `band0845_betp1` variant):
```
python engine/stats.py --a results/baseline_$POLICY/summary.csv \
    --b results/<RUN_ID>_draw1_$POLICY/summary.csv [... drawK] \
    --labels baseline regenerated --out results/compare/stats_<RUN_ID>_$POLICY.md
```
Then write `results/compare/REPORT_<RUN_ID>.md` following `docs/STATS_PLAN.md`:
1. Headline table: per policy — baseline total R, regenerated mean total R across draws (sd), block-bootstrap
   CI of the difference, P(diff ≤ 0), fraction of draws beating baseline, fill rate, dud rate.
2. Family and month breakdowns.
3. Trust Score / Card Integrity vs outcome: per-report scatter and OLS of total R on the two scores, both arms.
4. Equity overlays (embed the PNGs).
5. A plain statement of what is and is not supported by the "what counts as a result" rule, and the
   limitations (single instrument, single regime, residual model prior knowledge).
Commit `stage5: <RUN_ID> report`.
