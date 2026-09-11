# Week 2 Progress Report



| Field | Entry |
|---|---|
| Group | GROUP D EVENING |
| Project | CodeGuard QA Agent |
| Reporting period | 7–11 September 2026 |
| Group leader | Nakalema Julian |
| Source repository | https://github.com/Fantanstic-Four/codeguard-qa-agent-.git |
| Selected model | Gemini 3.1 Flash-Lite (`gemini-3.1-flash-lite`) |
| Current prompt | v1.1 candidate |

## 1. Work completed against Week 2 objectives

- Selected a small foundation model for the requirement-to-test-plan baseline and documented capability, cost, latency measurement, privacy, access, and portability considerations.
- Implemented a Python command-line interaction that accepts a feature name and approved requirement file, calls the configured foundation model, requests schema-constrained JSON, validates the response, and records model, prompt version, and latency.
- Created Prompt v1.0 and a meaningful v1.1 revision. The second version adds clearer untrusted-context boundaries, insufficient-context behaviour, grounding rules, output limits, and a ban on invented execution claims.
- Created a Prompt Specification covering the role, inputs, context, constraints, output schema, failure behaviour, settings, and acceptance checks.
- Created ten pre-defined evaluation cases covering normal, boundary, negative, missing-context, and adversarial situations.
- Added unit tests and a repeatable evaluation runner that produces CSV evidence.
- TEAM TO VERIFY: Ran the unit tests and retained the genuine result.
- TEAM TO VERIFY: Ran all ten cases with v1.0 and v1.1 using the selected foundation model and committed both CSV files.

## 2. Key engineering decisions

| Decision | Reason |
|---|---|
| Requirement-to-test-plan baseline only | Week 2 must measure the smallest useful model-backed capability before RAG, tools, or agent autonomy are added. |
| Gemini 3.1 Flash-Lite | Its low-latency, cost-conscious positioning and structured JSON support match the bounded task; performance remains subject to measured evidence. |
| Interactions API and Google GenAI SDK | This is the provider's current Python integration path and supports JSON Schema response formatting. |
| Pydantic validation after generation | Provider-side structured output improves format consistency, but application validation remains necessary. |
| Temperature 0.2 | A low value is appropriate for repeatable requirement transformation, while the measured evaluation determines adequacy. |
| Synthetic requirement corpus | Prevents disclosure of confidential or personal data during the baseline experiment. |
| Mock provider limited to smoke tests | Lets the team verify local wiring without falsely presenting deterministic output as model evidence. |



## 3. Failures, challenges, and response

| Challenge or failure | Response and status |
|---|---|
| Model output may be syntactically valid but semantically weak | Added application validation and explicit grounding/coverage checks; inspect genuine failures manually. |
| Requirements may contain instruction-like text | v1.1 delimits evidence as untrusted data and prohibits following embedded instructions. |
| Missing requirements could cause hallucinated tests | v1.1 requires `needs_clarification` with an empty test list. |
| Provider account, key, quota, or service may be unavailable | Fail visibly, use only an approved account, and never replace a genuine model run with mock results. |
| Actual evaluation pending | TEAM TO UPDATE with owner, blocker, resolution, and completion evidence. |



## 4. Individual contributions

| Member | Role | Main work owned | 
|---|---|---|---|
| Nakalema Julian | Requirements and Model Lead | Model decision, selection note, and progress report | 
| Nsubuga Ibrahim | Application and Integration Lead | Model integration, CLI, validation, and fixes |
| Namembwa Sherry  | Prompt and Evaluation Lead | Prompt versions, specification, history, and evaluation cases | 
| Kayiwa Rahim | Quality and DevOps Lead | Unit tests, model evaluation, evidence, and final review | 

## 5. Plan for Week 3

- Assemble and approve a controlled corpus of approximately 10–50 documents or equivalent records.
- Create a source register recording provenance, version, authorisation, and intended use.
- Implement ingestion, segmentation, indexing, and retrieval.
- Supply retrieved evidence as model context and display source references.
- Create at least fifteen RAG questions across answerable, partially answerable, and unanswerable categories.
- Record at least three genuine retrieval or grounding failures and explain their causes.

