# FTSE regeneration (ftse_regen1) — run log

| date | draw | incident | effect |
|---|---|---|---|
| 2026-07-03 | 1 | session ran `pip install python-dateutil pytz` (reported pandas would not import in its shell); environment checked afterwards, pandas imports normally | none on cards |
| 07-15, 07-20–07-23, 07-27–07-31 | 1 | session usage limit killed 10 draw-1 sessions mid-run; none had written an output file; re-queued | none |
| 05-11–05-15, 05-18–05-22 | 2 | same usage-limit kill, 10 draw-2 sessions; no outputs written; re-queued. The container was also recycled: scratch folders lost (sessions recreate their own) | none |
