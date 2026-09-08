# Week 1 Progress Report



| Field | Entry |
|---|---|
| Group | Group D Evening |
| Project | CodeGuard QA Agent |
| Reporting period | 31 August–4 September 2026 |
| Group leader | Nakalema Julian |
| CodeGuard source repository | https://github.com/Fantanstic-Four/codeguard-qa-agent-.git |
| Approved target fork |https://github.com/Fantanstic-Four/spring-petclinic |
| ClickUp project | https://app.clickup.com/1200430000003208/v/f/1200430000006068/1200430000005131|

## 1. Work completed against Week 1 objectives

- Selected the software-engineering QA agent use case and reduced it to one primary workflow: requirement retrieval → test-plan generation → human review → approved sandbox test → evidence-based explanation → draft report → approval gate.
- Produced a Project Charter defining the problem, target users, pain point, AI value, objectives, scope, corpus, assumptions, constraints, success measures, and risks.
- Defined ten testable user stories with acceptance criteria and eight non-functional requirements.
- Created an AI Boundary Matrix separating probabilistic AI work from deterministic policy and execution controls and human authority.
- Created the initial context architecture containing the application layer, bounded orchestrator, foundation model, approved knowledge index, tool gateway, sandbox runner, target fork, and trace store.
- TEAM TO VERIFY: Created `codeguard-qa-agent`, pushed the Week 1 artefacts, and retained the commit or pull-request link.
- TEAM TO VERIFY: Forked `spring-projects/spring-petclinic`, renamed or identified the fork as `codeguard-target-petclinic`, recorded its exact commit, and captured a truthful baseline-test result.
- TEAM TO VERIFY: Created the ClickUp project, assigned Week 1 tasks to real members, set deadlines and statuses, and linked tasks to repository evidence.

## 2. Key engineering decisions

| Decision | Reason |
|---|---|
| One bounded workflow | A narrow workflow is feasible in eight weeks and can be evaluated more credibly than a general assistant. |
| Direct orchestration first | Explicit state and policy checks make agent behaviour easier to understand, test, and explain. |
| Separate target fork | The team can develop CodeGuard independently while testing against a stable, pinned, public application revision. |
| Controlled corpus | Authorised requirements and technical documents provide traceable grounding without confidential data. |
| Typed tool contracts | The model requests named operations; deterministic software validates their schemas and permissions. |
| Draft-only external output | Issue and PR content remains a draft until an authenticated human approves the exact version. |

## 3. Failures, challenges, and responses

| Challenge | Response or status |
|---|---|
| Risk of building a generic chatbot | Reframed the system around a traceable QA workflow with tools, evidence, limits, and stop conditions. |
| Risk of unsafe shell execution | Decided that the model will never provide executable free-form commands; the runner accepts configured suite IDs only. |
| Risk of using sensitive or unavailable data | Limited the prototype to the approved public target fork, team-created documents, and synthetic records. |
| Prompting alone cannot guarantee grounding | Planned a source register, retrieval citations, and explicit unsupported-answer behaviour for Week 3. |
| Actual repository or ClickUp evidence incomplete | TEAM TO COMPLETE: state the owner, deadline, and current response for unfinished work. |

## 4. Repository and ClickUp evidence

| Evidence | Link or reference | What it demonstrates |
|---|---|---|
| CodeGuard source repository |https://github.com/Fantanstic-Four/codeguard-qa-agent-.git | The team's original agent project and Week 1 structure. |
| Target fork and revision |https://github.com/Fantanstic-Four/spring-petclinic | The authorised read-only application and reproducible revision. |
| ClickUp board |https://app.clickup.com/1200430000003208/v/l/6-1200430000006242-1 | Tasks, real owners, dates, statuses, and linked evidence. |



## 5. Plan for Week 2

- Select an accessible foundation model and document capability, cost, latency, privacy, and access constraints.
- Implement the smallest useful model-backed capability: structured requirement-to-test-plan generation.
- Create Prompt Specification v1.0 with role, task, context, constraints, output schema, and failure behaviour.
- Build at least ten baseline cases and record expected versus actual behaviour.
- Version at least two meaningful prompt iterations.
- Update the AI Engineering Log with the model decision, prompt changes, checks, and responsible reviewers.

