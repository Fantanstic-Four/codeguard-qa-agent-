# Week 2 Task Allocation for Four Members



| ID | Task | Primary owner | Due date | 
|---|---|---|---|---|
| W2-01 | Compare model options and approve the Week 2 selection | Nakalema Julian, Requirements and Model Lead | 12 Sep 2026 | 
| W2-02 | Finalise the one-page Model Selection Note | Nakalema Julian | 12 Sep 2026 |
| W2-03 | Implement the Gemini client, settings, schema, service, and CLI | Nsubuga Ibrahim, Application and Integration Lead | 12 Sep 2026 |
| W2-04 | Create and review Prompt v1.0 | Namembwa Sherry, Prompt and Evaluation Lead | 12 Sep 2026 |
| W2-05 | Create Prompt v1.1, specification, and version history | Namembwa Sherry | 12 Sep 2026 |
| W2-06 | Finalise the ten controlled evaluation cases | Namembwa Sherry | 12 Sep 2026 | 
| W2-07 | Run unit tests and both genuine model evaluations | Kayiwa Rahim, Quality and DevOps Lead | 12 Sep 2026 |
| W2-08 | Diagnose failures, fix the baseline, and rerun checks | Nsubuga Ibrahim | 12 Sep 2026 | 
| W2-09 | Compile the Week 2 progress report and evidence links | Nakalema Julian | 12 Sep 2026 |
| W2-10 | Final quality, security, and submission review |Kayiwa Rahim| 12 Sep 2026 |

## Role summaries

###Nakalema Julian Requirements and Model Lead

Owns the model decision, checks that it matches the Week 1 boundaries, compiles the weekly report, and coordinates final review. This member does not invent evaluation results; they use the CSV evidence produced by Kayiwa Rahim.

### Nsubuga Ibrahim Application and Integration Lead

Owns the runnable Python baseline, configuration, model-client boundary, schema validation, error handling, and fixes discovered during evaluation.

###Namembwa Sherry Prompt and Evaluation Lead

Owns both prompt versions, the prompt specification, the reasoned version history, and the ten-case controlled dataset. This member ensures expected behaviours are written before observing results.

### Kayiwa Rahim Quality and DevOps Lead

Owns unit-test execution, genuine model runs, evidence capture, secret checks, and final submission review. They verify that mock output is not presented as model evidence.

## Review arrangement

- Nakalema Julian reviews Namembwa Sherry's prompt and evaluation design.
- Nsubuga Ibrahim reviews Kayiwa Rahim's runner or evidence procedure.
- Namembwa Sherry reviews Nsubuga Ibrahim's model integration against the prompt contract.
-Kayiwa Rahim reviews Nakalema Julian's model note and report for unsupported claims.
- All four approve the final Week 2 report through a pull-request comment or documented meeting note.

