# User Stories and Acceptance Criteria

These ten user stories define the Week 1 functional baseline. Each criterion is observable and can later become an evaluation scenario. Terms such as **approved repository**, **approved command**, **source reference**, and **human approval** must be implemented as deterministic controls rather than left to model judgement.

## US-01: Start an authorised QA session

**User story:** As a QA engineer, I want to select an approved repository, branch, and feature so that the agent works only within an authorised target.

**Acceptance criteria**

- **AC-01.1:** Given an authenticated user and allow-listed repository, when the user selects the repository and branch, the system creates a session with a unique trace ID.
- **AC-01.2:** Given a repository outside the allow-list, when it is requested, access is denied before any model or tool call and the denial is logged.
- **AC-01.3:** The session stores the repository identifier, branch, feature or story identifier, user identifier, start time, and configured limits without storing secrets.

## US-02: Retrieve grounded feature context

**User story:** As a QA engineer, I want the agent to retrieve relevant requirements and architecture notes so that test planning is based on approved evidence.

**Acceptance criteria**

- **AC-02.1:** For an answerable feature query, the system returns relevant acceptance criteria with the source name, version, and location.
- **AC-02.2:** If no sufficiently relevant source is found, the system reports insufficient context and asks for clarification instead of inventing requirements.
- **AC-02.3:** Only documents marked approved and authorised for the selected repository are eligible for retrieval.

## US-03: Generate a requirement-mapped test plan

**User story:** As a QA engineer, I want a proposed test plan mapped to acceptance criteria so that I can review coverage before tests run.

**Acceptance criteria**

- **AC-03.1:** Each proposed test contains a test ID, scenario, preconditions, input, expected result, requirement reference, and priority.
- **AC-03.2:** The plan distinguishes normal, boundary, negative, and failure-path scenarios where applicable.
- **AC-03.3:** Every factual statement about the feature is cited or labelled as an assumption requiring review.

## US-04: Review and amend the test plan

**User story:** As a QA engineer, I want to approve, edit, or reject the proposed plan so that human judgement remains in control of what is tested.

**Acceptance criteria**

- **AC-04.1:** Before execution, the user can accept the plan, remove a scenario, edit a scenario, or add an instruction.
- **AC-04.2:** The system records the original plan, approved plan, approving user's identity, and approval time.
- **AC-04.3:** Rejected scenarios are not executed; their rejection reason may be stored without changing the source requirement.

## US-05: Run an approved test

**User story:** As a QA engineer, I want the system to run approved tests in a sandbox so that results are reproducible without risking the host or production environment.

**Acceptance criteria**

- **AC-05.1:** The tool accepts only a typed test-suite identifier or allow-listed command alias; free-form shell commands are rejected.
- **AC-05.2:** Each run records the resolved command, working directory, environment profile, start and end times, exit code, and output-artefact references.
- **AC-05.3:** The runner enforces configured time, resource, and network limits and returns a structured failure when a limit is reached.

## US-06: Explain an observed result

**User story:** As a developer, I want the agent to explain passing and failing results using exact evidence so that I can act efficiently.

**Acceptance criteria**

- **AC-06.1:** The explanation clearly separates observed facts, requirement interpretation, and possible causes.
- **AC-06.2:** A test is reported as passed or failed only when the deterministic runner supplies that result; missing or conflicting evidence is reported as unknown.
- **AC-06.3:** Quoted or referenced log content includes the test name and location in the stored result artefact.

## US-07: Recover safely from failure

**User story:** As a QA engineer, I want the agent to stop or recover safely when a source, model, or tool fails so that it does not loop or hide uncertainty.

**Acceptance criteria**

- **AC-07.1:** The workflow stops after a maximum of five tool calls or two test executions unless the user starts a new session.
- **AC-07.2:** For a transient tool error, the system may retry once only when the action remains authorised, and it records both attempts.
- **AC-07.3:** For repeated failure, missing authorisation, or ambiguous requirements, the system stops with a clear reason and recommended human action.

## US-08: Draft an issue or pull-request note

**User story:** As a developer, I want a draft issue or pull-request note created from verified QA evidence so that reporting is faster and consistent.

**Acceptance criteria**

- **AC-08.1:** The draft contains a concise summary, requirement reference, reproduction steps, expected result, actual result, and evidence links where available.
- **AC-08.2:** The output is labelled as a draft and is not published automatically.
- **AC-08.3:** Any unsupported suspected cause is labelled as a hypothesis rather than a confirmed defect.

## US-09: Approve or reject external publication

**User story:** As a project lead, I want publication to require explicit approval so that the agent cannot create external repository records without accountability.

**Acceptance criteria**

- **AC-09.1:** Creating a permitted GitHub issue or PR comment requires an authenticated approval event tied to the exact draft version.
- **AC-09.2:** Editing a draft after approval invalidates the approval and requires a new approval.
- **AC-09.3:** Merge, deployment, branch deletion, secret access, and arbitrary code modification remain prohibited even when requested in natural language.

## US-10: Inspect the execution trace

**User story:** As a reviewer, I want to inspect the agent trace so that I can verify sources, decisions, tool use, and the stop reason.

**Acceptance criteria**

- **AC-10.1:** The trace displays the user request, retrieved source references, approved plan, tool name and inputs, tool-result summary, decisions, and final outcome.
- **AC-10.2:** Sensitive values are redacted before storage or display, and trace access follows project permissions.
- **AC-10.3:** The reviewer can correlate every final pass/fail claim and report section with source or tool evidence.

## Non-functional requirements

| ID | Requirement | Testable definition |
|---|---|---|
| NFR-01 | Security | No tool call bypasses user, repository, path, or command allow-lists; secrets never enter prompts or traces. |
| NFR-02 | Traceability | Every evaluated session has a unique trace ID and records sources, tools, results, approvals, and stop reason. |
| NFR-03 | Reliability | Failures use structured states; an unavailable result is never converted into a fabricated success. |
| NFR-04 | Performance | In the controlled prototype, test-plan generation normally completes within 30 seconds, excluding test execution. |
| NFR-05 | Reproducibility | The repository contains versioned prompts, configuration examples, dependency instructions, and repeatable test-suite aliases. |
| NFR-06 | Maintainability | Model, retrieval, orchestration, and tools use explicit interfaces and can be tested independently. |
| NFR-07 | Privacy | Only public, team-owned, synthetic, or authorised data is processed; retained memory has a purpose and deletion route. |
| NFR-08 | Usability | Results clearly separate requirements, plan, observed evidence, interpretation, uncertainty, and approval actions. |

## Week 1 definition of done

- The charter has been reviewed and approved by the team.
- All ten user stories have testable acceptance criteria.
- The AI Boundary Matrix separates AI suggestions, deterministic controls, and human authority.
- The architecture diagram includes the model, controlled context, orchestrator, tool gateway, sandbox, and trace store.
- The CodeGuard repository and ClickUp project exist and have genuine evidence links.
- If the PetClinic fork is used, its exact URL, branch, and pinned commit have been recorded.
- The progress report contains real contribution and repository evidence.
- AI assistance has been declared and every member can explain the submitted work.

