# FTSE QA stage 1 — run log

Incidents reported by review sessions. A directory listing exposes later dates' *filenames* (QA
outputs are named by date only — no market information); it is logged because it breaks the
SESSION_TASK rule, not because it leaks prices. Scores were set before any listing unless noted.

| date | incident | effect |
|---|---|---|
| several of 05-11…06-05 | session listed `qa/ftse_qa1/` to check its own output (filenames only, nothing opened) | none on scoring |
| 2026-06-15 | `ls -la qa/ftse_qa1/` after scores were set; hallucinated_source override withheld as a judgement call (TE row self-inconsistent, not proven fabricated) | none on scoring |
| 2026-06-23 | `ls qa/ftse_qa1/` after writing outputs (filenames only) | none on scoring |
| 2026-06-11 | `git status` showed other dates' QA filenames (nothing opened) | none on scoring |
| 2026-06-24 | `git status` showed another session's in-flight filename (nothing opened) | none on scoring |
| 2026-06-19 | report built through D (as-of breach); reviewer did not check D values against data | none on scoring |
| 2026-06-30 | `ls cards/regenerated` (nothing printed) and `ls -la qa/ftse_qa1` (filenames only); both restriction_breach and hallucinated_source applied, CSV records the stricter | none on scoring |
| 2026-06-26 | `ls cards/regenerated` (run-folder names only, nothing opened) | none on scoring |
| 2026-06-29 | `ls qa/ftse_qa1/` after writing outputs (filenames only) | none on scoring |
