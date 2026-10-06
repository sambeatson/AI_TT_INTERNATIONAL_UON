# FTSE QA stage 1 — run log

Incidents reported by review sessions. A directory listing exposes later dates' *filenames* (QA
outputs are named by date only — no market information); it is logged because it breaks the
SESSION_TASK rule, not because it leaks prices. Scores were set before any listing unless noted.

| date | incident | effect |
|---|---|---|
| several of 05-11…06-05 | session listed `qa/ftse_qa1/` to check its own output (filenames only, nothing opened) | none on scoring |
| 2026-06-15 | `ls -la qa/ftse_qa1/` after scores were set; hallucinated_source override withheld as a judgement call (TE row self-inconsistent, not proven fabricated) | none on scoring |
