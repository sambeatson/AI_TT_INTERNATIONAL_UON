# P4 — Score every card set under every policy (post-hoc; full data allowed)

For SET in {baseline, <RUN_ID>_draw1, ..., <RUN_ID>_drawK} and POLICY in {card, midnight, usopen, band0845}:
```
python engine/resolver.py --cards <cards csv for SET> --data data/raw/<ASSET>_p_M15.csv \
    --policy $POLICY --open <OPEN> --cutoff <CUTOFF> --out results/${SET}_${POLICY}
python engine/resolver.py ... --policy band0845 --be tp1 --out results/${SET}_band0845_betp1
```
OPEN/CUTOFF: equities/energy/metals/crypto 09:00/23:00; FX 09:00/18:00 (see docs/ENTRY_POLICIES.md).
Baseline band0845 must reproduce −9.49R on the shipped US500 file (regression).

Then for each POLICY produce an equity overlay of baseline vs all draws:
```
python engine/equity.py --runs results/baseline_$POLICY/summary.csv results/<RUN_ID>_draw1_$POLICY/summary.csv ... \
    --labels baseline draw1 ... --risk 2500 --out results/compare/equity_<RUN_ID>_$POLICY.png --title "<ASSET> — $POLICY"
```
Commit `stage4: <RUN_ID> scored`.
