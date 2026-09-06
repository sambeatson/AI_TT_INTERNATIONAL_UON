# modules/ — the prompt stack (plain-text copies of the project's .docx modules)

M1_Variables_v2_1        variables contract (what changes per run)
M1_SP500_v2_1            the S&P 500 M1 instance used for the baseline reports
M2_Research_Standard_v2_1  sourcing / OHLC triangulation rules   -> Trust Score Cat. 3 & 5 anchor
M3_Technical_Module_v2_1   indicator and pivot arithmetic          -> Cat. 4 anchor
M4_Output_Structure_v2_1   §1–§21 report layout                    -> Cat. 2 anchor
M5_Strategies_Module_v2_1  card construction rules (3 units, BE, runner, suppression)
Source_Discipline_NoSynthesis_Protocol, Agentic_Safe_Source_Module — restriction texts (Cat. 5 overrides)

These are the files you edit between Stage 1 (QA) and Stage 2 (regeneration). Commit each edit on its
own so an R delta in Stage 5 can be attributed to a specific change. Regenerated cards must cite the
module version (git short-SHA) they were produced under in their `rationale` field.
