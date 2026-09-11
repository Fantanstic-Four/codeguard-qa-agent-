# Project Charter

## Project identity

**Project:** CodeGuard QA Agent  
**Course:** BSE4104 Emerging Trends in Software Engineering  
**Week:** Week 1 — Problem Framing and AI-Native Requirements  
**Group:** FANTASTIC FOUR  
**Group leader:** NAKALEMA JULIAN  
**Team members and student numbers:**
NAKALEMA JULIAN 23/U/13388/EVE
KAYIWA RAHIM 23/U/09499/EVE
NAMEMBWA SHERRY 23/U/14586/EVE
NSUBUGA IBRAHIM 23/U/24436/EVE
**Submission date:** 4 September 2026

## 1. Problem statement

Small software teams and student development groups often move from requirements to implementation without a disciplined and traceable quality-assurance process. Requirements may be distributed across user stories, README files, issue descriptions, API notes, and architecture documents. A tester must locate the relevant acceptance criteria, decide what to test, choose an appropriate command, interpret test logs, and rewrite the observed facts into an issue or pull-request note. Under deadline pressure, this process produces inconsistent coverage, duplicated effort, undocumented assumptions, and failures that are difficult to reproduce.

General-purpose AI assistants can suggest tests, but an ordinary chat response is insufficient. A model may rely on unstated assumptions, invent repository details, suggest an unsafe or unavailable command, or confidently describe a failure that is not supported by actual test output. The engineering problem is therefore not merely generating test text. It is building a controlled workflow that connects approved project evidence to approved testing tools, records the execution trace, and keeps consequential actions under human control.

## 2. Target users and current pain point

The primary user is a QA engineer or developer responsible for validating a feature in a small, authorised repository. In the capstone prototype, the primary persona is a student team member acting as the QA lead.

Secondary users are developers who need reproducible failure reports, project leads who need requirement-coverage evidence, and reviewers who must inspect what the AI and software tools actually did.

The current pain point is that the user spends significant time searching fragmented documents, translating requirements into test cases, remembering safe commands, interpreting noisy output, and copying the same facts into reports. Important edge cases, source references, and uncertainties may be missed.

## 3. Proposed AI-native solution

CodeGuard will be a small web or API-based application that supports one traceable QA workflow. It will combine a foundation model, retrieval from a controlled project corpus, typed software tools, and a bounded orchestration loop. The model will not have direct access to the operating system, repository credentials, or a general-purpose shell. Every exposed tool will have a documented purpose, input schema, output schema, permission check, and failure response.

The system will start with a model-backed requirement-to-test-plan baseline in Week 2. Week 3 will add retrieval and source grounding. Week 4 will add explicit tools. Week 5 will add a bounded sense-decide-act-observe workflow. Later weeks will make state and justified memory explicit, add evaluation and guardrails, and produce a reproducible final release. This progression keeps the project small enough to test and explain while demonstrating engineering beyond a chatbot wrapper.

## 4. Primary end-to-end workflow

1. A QA engineer selects an approved repository, branch, and feature or user story.
2. The application validates access and creates a bounded QA session with a trace ID.
3. The agent retrieves relevant requirements and repository documentation from the controlled knowledge index.
4. The agent proposes a structured test plan mapped to cited acceptance criteria and identifies missing information.
5. The user reviews, edits, approves, or rejects the proposed plan.
6. The deterministic test runner resolves an approved suite identifier to a fixed command and executes it in a sandbox.
7. The runner returns the exact command, exit code, duration, structured results, standard output, and artefact references.
8. The agent explains the outcome using the retrieved requirements and observed execution evidence, separating facts from hypotheses.
9. The system saves a QA summary and may prepare a draft issue or pull-request note.
10. A human must approve any permitted external publication. Code changes, merging, deployment, and destructive operations remain prohibited.

## 5. Why AI adds value

AI is useful where the work involves ambiguous natural-language requirements, dispersed context, scenario generation, and explanation. It can retrieve and synthesise relevant evidence, propose normal and edge cases, identify missing information, and summarise test output for a developer.

AI is not trusted to authenticate users, grant repository access, decide which system command is safe, create authoritative pass/fail facts, or approve repository-changing actions. Authentication, allow-lists, schema validation, exact test execution, trace recording, and approval enforcement remain deterministic. Humans resolve conflicting requirements and retain authority over external or high-impact actions.

## 6. Objectives

- Produce a source-grounded test plan for one selected feature.
- Map proposed scenarios to explicit acceptance criteria.
- Execute only approved test suites in an isolated environment.
- Capture reproducible command, result, timing, and log evidence.
- Explain failures without fabricating results and distinguish observations from possible causes.
- Draft a clear issue or pull-request note while requiring human approval before publication.
- Evaluate completion, groundedness, tool selection, safety, latency, and failure recovery using controlled scenarios.

## 7. Project scope

### In scope

- One approved target repository and one primary QA workflow.
- Approximately 10–50 approved project documents or equivalent records.
- Retrieval of requirements, acceptance criteria, architecture notes, and testing instructions.
- Structured generation of normal, boundary, negative, and failure-path test scenarios.
- Human review of the plan before execution.
- Execution of named, allow-listed test suites in a sandbox.
- Evidence-based explanation of passing, failing, unavailable, or uncertain outcomes.
- Trace capture and preparation of an internal draft issue or pull-request note.
- One justified persistent-memory use case, such as an approved prior case summary, in a later week.

### Out of scope

- Automatic source-code modification, commit, push, or branch creation by the agent.
- Automatic merge, deployment, release, or branch deletion.
- General or arbitrary shell access.
- Secret discovery or access to unrelated or unauthorised repositories.
- Autonomous publication of issues, comments, or pull requests.
- Security exploitation or penetration testing.
- Production access or use of confidential institutional data.
- Claims that CodeGuard replaces professional testing or human engineering judgement.

## 8. Data and controlled corpus

The initial corpus will contain approximately 10–20 public, team-owned, or team-created items: the project charter, user stories, acceptance criteria, README, architecture notes, API contracts, testing guidance, selected source-code documentation, synthetic issue records, and test-output examples. Each item will have a source name, owner, version, date, authorisation status, and intended use.

The approved test target will be a team fork of the public Spring PetClinic repository, recorded in `config/targets/petclinic.yaml`. CodeGuard will treat the fork as read-only during the MVP. Real secrets, private third-party source code, personal data, and restricted institutional data will not be processed.

## 9. Assumptions and constraints

- The team can create and maintain the CodeGuard source repository and a public PetClinic fork.
- The chosen target revision contains runnable tests and non-sensitive documentation.
- An accessible foundation model and embedding service are available within the team's budget or free-tier limits.
- The test runner can be isolated locally or in a container and configured with a strict command allow-list.
- The eight-week schedule favours one demonstrable workflow over broad support for many languages and repository types.
- AI-generated suggestions will be reviewed, tested, and understood by the team before acceptance.
- GitHub and ClickUp evidence must represent work that was actually performed.

## 10. Success measures

| Measure               |                                                                                     Week 8 target |
| --------------------- | ------------------------------------------------------------------------------------------------: |
| Requirement grounding |                         At least 90% of produced test-plan items cite a relevant approved source. |
| Acceptance coverage   |                         At least 85% of testable acceptance criteria receive a relevant scenario. |
| Execution fidelity    |                   100% of reported commands, exit codes, and pass/fail facts match runner output. |
| Tool safety           |                 Zero successful prohibited actions; unauthorised requests are refused and logged. |
| Workflow completion   |               At least 80% of normal scenarios reach a useful QA report within configured limits. |
| Traceability          | 100% of evaluated sessions record inputs, sources, tool calls, results, stop reason, and outcome. |
| Human control         |    100% of external publication attempts require approval; merge and deployment stay unavailable. |

## 11. Key risks and responses

| Risk                                  | Planned response                                                                                  |
| ------------------------------------- | ------------------------------------------------------------------------------------------------- |
| Hallucinated repository facts         | Require source references, mark unsupported claims, and compare factual results with tool output. |
| Unsafe command suggestion             | Expose typed suite identifiers only; deterministic code resolves them to fixed commands.          |
| Prompt injection in repository text   | Treat retrieved text as untrusted data and enforce tool policy outside the model.                 |
| Scope expansion                       | Limit the MVP to one target type, one workflow, and a small controlled corpus.                    |
| Weak team ownership                   | Assign identifiable tasks, use reviewed pull requests, keep an AI log, and rehearse explanations. |
| Unavailable model or external service | Keep provider configuration replaceable and return structured failure rather than false results.  |

## 12. Approval and Week 1 completion criteria

Week 1 is complete when the team has reviewed and approved this charter, validated the ten user stories and acceptance criteria, accepted the AI Boundary Matrix, stored the initial architecture diagram, created the CodeGuard source repository, recorded the approved target fork and exact revision, created the ClickUp project, assigned identifiable tasks, linked genuine evidence, and recorded material AI assistance in the engineering log.

Approval of this charter authorises prototype development only. It does not authorise production access, deployment, autonomous repository changes, or processing of restricted data.
