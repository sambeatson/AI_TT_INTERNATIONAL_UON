# Leakage protocol (binding)

The experiment compares cards written with hindsight-free information to cards that were actually
issued. Any information from the report date or later that reaches the QA or regeneration agent
invalidates the comparison. These rules are enforced mechanically, not by instruction.

## Rule 1 — the data cut
For a report dated **D** (the session the report is FOR), the agent may see only bars whose
**broker date < D**. That is up to and including the 23:45 broker bar of D-1. Not one bar from
broker date D. `engine/slices.py` produces these files and a MANIFEST recording the last bar included.
The agent is pointed at `data/slices/<asset>/<asset>_upto_<D-1>.csv` and nothing else.

## Rule 2 — no results in context
The QA and regeneration sessions must not have access to: `results/`, `qa/baseline/lint_baseline.csv`
(market-relative flags reveal day-D prices), the prior chat transcript, or memory of it. Run them in a
fresh Claude Code session per stage. The static linter (`linter.py --cards` without `--data`) IS allowed;
it needs no market data.

## Rule 3 — reports are read as-of
The report for D contains only D-1 information by construction (its own §21c backtest is prior-session).
The agent reads the report for D and reports for dates < D. It never opens a report dated > D.

## Rule 4 — news
`data/news/` is sliced on `timestamp_broker < D 00:00 broker`. A scheduled event calendar for D
(time, event name, impact tier, consensus) is ex-ante information and MAY be provided.
Actual prints, headlines, and unscheduled events dated D MAY NOT.

## Rule 5 — no new research
Regeneration uses only: the report text for D, the QA feedback for D, the data slice, and the news slice.
No web search. No additional sources. The test is whether QA feedback alone improves the cards.

## Rule 6 — separation of arms
Baseline cards (`cards/baseline`) and regenerated cards (`cards/regenerated/<run_id>`) are scored by
the SAME engine, SAME policy flags, SAME data file, in the same command. The scoring stage runs with the
full data file — that is fine, scoring is post-hoc by definition.

## Rule 7 — audit trail
Every regenerated card JSON carries `source: regen_<run_id>_draw<k>`, the slice filename it was built
from, and the `last_bar_broker` from the manifest. A card whose provenance fields are missing is discarded.

## What still cannot be fully controlled
The model that regenerates cards was trained on data that may include this period. This is a limitation
to state in the write-up, not something the protocol can remove. The mitigations above remove the
*explicit* leakage channels; residual prior knowledge is acknowledged.
