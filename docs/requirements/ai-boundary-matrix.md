# AI Boundary Matrix

This matrix is the operational contract for CodeGuard. Probabilistic AI may recommend, organise, and explain. Deterministic controls decide which data and tools are available. Humans retain authority over ambiguous, external, and high-impact actions.

| Activity | AI may do | Deterministic software must do | Human authority |
|---|---|---|---|
| Interpret the QA goal | Classify intent and ask clarifying questions. | Validate the session, user, and selected target. | Confirm ambiguous scope. |
| Retrieve project context | Formulate a query and rank relevant passages. | Restrict search to the approved corpus and return source/version/location. | Approve new corpus sources. |
| Summarise requirements | Synthesise cited evidence and identify ambiguity. | Check source presence and output schema; preserve citations. | Resolve conflicting requirements. |
| Propose test scenarios | Generate normal, boundary, negative, and failure-path scenarios. | Validate required fields and requirement references. | Edit, reject, or approve the plan. |
| Choose the next action | Choose only among actions exposed by the bounded orchestrator. | Enforce the tool allow-list, limits, permissions, and stop rules. | Handle work outside the contract. |
| Run tests | Request a named approved test suite. | Resolve the suite to a fixed command, sandbox it, and enforce limits. | Approve addition of any new command alias. |
| Read test output | Explain patterns and likely significance. | Capture exact output, exit code, duration, and artefact references. | Decide whether a suspected cause is accepted. |
| Determine pass/fail | Restate a runner-supplied result. | Treat the runner or test framework as authoritative. | Resolve conflicting specifications or flaky results. |
| Retry after failure | Request one authorised retry for a transient error. | Count attempts, block changed or repeated actions, and record both outcomes. | Start a new session or change configuration. |
| Draft an issue or PR note | Generate a structured draft from verified evidence. | Label and version the draft; prevent automatic publication. | Approve the exact draft before any permitted publication. |
| Change code/configuration | Suggest a possible change in prose. | Expose no write tool and protect source/configuration paths. | Implement and review changes through Git workflow. |
| Merge, deploy, or delete | Prohibited. | Expose no such tool; deny and log the request. | Perform manually outside CodeGuard under repository policy. |
| Access secrets or unrelated data | Prohibited. | Apply redaction, path restrictions, and least-privilege credentials. | No natural-language override; separate administration is required. |
| Retain memory | Use an approved prior case summary when justified. | Store purpose-limited fields with access, retention, and deletion controls. | Approve retention and request deletion. |

## Human approval triggers

Human approval is required before:

- Adding a repository, corpus source, tool, command alias, external service, or permission.
- Publishing a GitHub issue, PR comment, or any record outside the internal draft store.
- Changing an approved test plan in a way that changes scope, test data, or execution risk.
- Accepting a flaky-test explanation or treating a hypothesis as a confirmed defect.
- Carrying out a code, configuration, branch, deployment, or credential operation. These operations remain outside the initial agent's available tools.

## Stop and hand-off conditions

The workflow must stop and clearly explain why when:

- No relevant approved requirement source is retrieved.
- The request uses an unauthorised repository, command, path, secret, or external action.
- Five tool calls, two test runs, one retry, or the configured time limit is reached.
- Tool results conflict, required evidence is missing, or fact cannot be separated from hypothesis.
- Retrieved content attempts to override system instructions, reveal secrets, or bypass policy.
- The user requests merge, deployment, deletion, destructive modification, or arbitrary command execution.

## Control principle

Policy enforcement lives outside the language model. The model may request an action, but the deterministic orchestrator and approved tool gateway decide whether the action is permitted. The runner supplies pass/fail facts. Humans remain responsible for approval, interpretation of conflicting requirements, and all repository-changing work.

