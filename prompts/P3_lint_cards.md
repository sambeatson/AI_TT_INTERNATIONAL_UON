# P3 — Lint both card sets (post-hoc; full data allowed)

1. `python engine/linter.py --cards cards/baseline/cards_baseline.csv --data data/raw/<ASSET>_p_M15.csv --out qa/<RUN_ID>/lint_baseline.csv`
2. For each draw: `python engine/linter.py --cards cards/regenerated/<RUN_ID>/cards_<RUN_ID>_draw<K>.csv --data data/raw/<ASSET>_p_M15.csv --out qa/<RUN_ID>/lint_draw<K>.csv`
3. Produce `qa/<RUN_ID>/lint_comparison.md`: flag counts per type per set, dud rate, clean rate, and a
   list of any regenerated card that still carries a DUD flag (these are Stage 2 failures — report them,
   do not fix them here).
4. Commit `stage3: <RUN_ID> lint`.
