
# Week 4 Tool Test Plan and Evaluation

## 1. Purpose

This document records the Week 4 testing and evaluation of the CodeGuard QA Agent tool/function-calling implementation.

The Week 4 evaluation focuses on:

- Successful execution of explicit tools.
- Retrieval of approved requirement data.
- Execution of a low-risk simulated side effect.
- Input validation and missing parameters.
- Role-based authorization.
- Human approval before higher-impact actions.
- Controlled handling of unknown tools and failures.
- Regression testing of the existing CodeGuard functionality.

The tools evaluated are:

1. `get_requirement` — retrieves an approved requirement from the local controlled requirements corpus.
2. `create_draft_ticket` — creates a local draft ticket as a low-risk simulated side effect.
3. `publish_ticket` — demonstrates the authorization and human-approval boundary for a higher-impact simulated action.

---

## 2. Test Environment

The Week 4 evaluation was performed using the CodeGuard QA Agent repository.

Environment used during the final evaluation:

- Operating System: Windows
- Shell: PowerShell
- Python: 3.14.6
- Test Framework: pytest 8.4.2
- Tool Interface: `codeguard.tool_cli`
- Requirement Corpus: `knowledge/corpus/`
- Draft Ticket Storage: `evidence/tool-data/draft-tickets/`

---

## 3. Automated Regression Test

The complete automated test suite was executed using:

```powershell
python -m pytest -v
```

The recorded test run produced:

```text
21 passed, 2 warnings
```

All 21 collected automated tests passed.

The two warnings were Pytest collection warnings associated with production classes whose names begin with `Test`. They did not cause test failures.

The automated suite covered existing prompting, schema validation, service/orchestration functionality, Week 3 RAG functionality, and the Week 4 tool implementation.

---

## 4. Tool Test Cases

| ID    | Test Scenario                                                   | Expected Result                                      | Actual Result                                                                    | Status           |
| ----- | --------------------------------------------------------------- | ---------------------------------------------------- | -------------------------------------------------------------------------------- | ---------------- |
| W4-01 | Retrieve an existing requirement using`get_requirement`       | Requirement is returned with its ID, source and text | `REQ-OWN-001` was successfully returned from `12-petclinic-owner-management` | PASS             |
| W4-02 | Call`get_requirement` without the required requirement ID     | Controlled missing-parameter failure                 | Automated test passed                                                            | PASS             |
| W4-03 | Attempt requirement lookup without an authorized role           | Request is rejected                                  | Automated authorization test passed                                              | PASS             |
| W4-04 | Requirement corpus/service unavailable                          | Controlled`SERVICE_UNAVAILABLE` response           | Not yet recorded in manual evaluation evidence                                   | NOT YET VERIFIED |
| W4-05 | Create a draft ticket using`create_draft_ticket`              | A local draft ticket is created                      | `DRAFT-13307568` was successfully created                                      | PASS             |
| W4-06 | Call draft-ticket tool with a required parameter missing        | Controlled missing-parameter failure                 | Automated test passed                                                            | PASS             |
| W4-07 | Attempt draft creation using an unauthorized role               | Request should be rejected                           | Not separately recorded in manual evaluation evidence                            | NOT YET VERIFIED |
| W4-08 | Request an unknown tool through the registry                    | Controlled`UNKNOWN_TOOL` result                    | Automated registry test passed                                                   | PASS             |
| W4-09 | Reviewer attempts`publish_ticket`                             | Request is rejected with`UNAUTHORIZED`             | `UNAUTHORIZED` returned with message `qa_lead required`                      | PASS             |
| W4-10 | QA lead attempts`publish_ticket` without human approval       | Request is blocked with`APPROVAL_REQUIRED`         | `APPROVAL_REQUIRED` was returned                                               | PASS             |
| W4-11 | QA lead executes`publish_ticket` with explicit human approval | Simulated higher-impact action succeeds              | `simulated_published` returned successfully                                    | PASS             |
| W4-12 | Tool handler produces an unexpected response/error              | Application should return a controlled failure       | Not yet recorded in evaluation evidence                                          | NOT YET VERIFIED |

---

## 5. Tool 1: Requirement Retrieval

### Test Objective

Verify that `get_requirement` can retrieve an approved requirement from the controlled CodeGuard requirement corpus.

### Command

```powershell
python -m codeguard.tool_cli get_requirement --args '{\"requirement_id\":\"REQ-OWN-001\"}'
```

### Actual Result

```json
{
  "ok": true,
  "tool": "get_requirement",
  "data": {
    "requirement_id": "REQ-OWN-001",
    "source_id": "12-petclinic-owner-management",
    "text": "A user can search for owners by last name."
  },
  "error_code": null,
  "message": ""
}
```

### Evaluation

**PASS**

The tool successfully retrieved the requested requirement and returned traceable information containing the requirement ID, source ID and requirement text.

---

## 6. Tool 2: Draft Ticket Creation

### Test Objective

Verify that CodeGuard can execute a low-risk simulated side effect by creating a local draft ticket.

### Command

```powershell
python --% -m codeguard.tool_cli create_draft_ticket --args "{\"title\":\"Review owner search\",\"description\":\"Check negative owner-search behavior\",\"requirement_id\":\"REQ-OWN-001\"}"
```

### Actual Result

```json
{
  "ok": true,
  "tool": "create_draft_ticket",
  "data": {
    "ticket_id": "DRAFT-13307568",
    "status": "draft",
    "path": "evidence\\tool-data\\draft-tickets\\DRAFT-13307568.json"
  },
  "error_code": null,
  "message": ""
}
```

### Side-Effect Verification

The generated file was verified using:

```powershell
Get-ChildItem evidence\tool-data\draft-tickets
```

The following draft was present:

```text
DRAFT-13307568.json
```

The contents were inspected using:

```powershell
Get-Content evidence\tool-data\draft-tickets\*.json
```

Recorded draft:

```json
{
  "ticket_id": "DRAFT-13307568",
  "status": "draft",
  "title": "Review owner search",
  "description": "Check negative owner-search behavior",
  "requirement_id": "REQ-OWN-001",
  "created_by": "local-user",
  "created_at": "2026-09-26T11:12:57.145491+00:00"
}
```

### Evaluation

**PASS**

The tool performed the intended low-risk side effect and persisted the draft ticket locally. No external ticketing service was contacted.

---

## 7. Authorization Test

### Test Objective

Verify that a normal reviewer cannot perform the higher-impact `publish_ticket` action.

The tool was invoked without the required `qa_lead` role.

### Actual Result

```json
{
  "ok": false,
  "tool": "publish_ticket",
  "data": {},
  "error_code": "UNAUTHORIZED",
  "message": "qa_lead required"
}
```

### Evaluation

**PASS**

The authorization boundary correctly prevented a reviewer from performing the simulated publication action.

---

## 8. Human Approval Test

### Test Objective

Verify that possessing the `qa_lead` role alone is insufficient to perform the higher-impact action.

### Command

```powershell
python --% -m codeguard.tool_cli publish_ticket --role qa_lead --args "{\"ticket_id\":\"DRAFT-13307568\"}"
```

### Actual Result

```json
{
  "ok": false,
  "tool": "publish_ticket",
  "data": {},
  "error_code": "APPROVAL_REQUIRED",
  "message": "human approval required for publish_ticket:DRAFT-13307568"
}
```

### Evaluation

**PASS**

The higher-impact action was blocked even though the caller possessed the required role. Explicit human approval was still required.

---

## 9. Approved Higher-Impact Action

### Test Objective

Verify that the simulated publication action can proceed after both authorization and explicit human approval have been supplied.

### Command

```powershell
python --% -m codeguard.tool_cli publish_ticket --role qa_lead --approve publish_ticket:DRAFT-13307568 --args "{\"ticket_id\":\"DRAFT-13307568\"}"
```

### Actual Result

```json
{
  "ok": true,
  "tool": "publish_ticket",
  "data": {
    "ticket_id": "DRAFT-13307568",
    "status": "simulated_published"
  },
  "error_code": null,
  "message": ""
}
```

### Evaluation

**PASS**

The action succeeded only after the required role and explicit approval were supplied.

The publication is simulated and does not contact or modify an external ticketing system.

---

## 10. Authorization and Approval Flow

The evaluation demonstrated the following control flow:

```text
Reviewer
   |
   v
publish_ticket
   |
   +----> UNAUTHORIZED


QA Lead
   |
   v
publish_ticket
   |
   +----> APPROVAL_REQUIRED


QA Lead + Explicit Human Approval
   |
   v
publish_ticket
   |
   +----> simulated_published
```

This demonstrates that authorization and human approval are separate controls.

Having the correct role does not automatically authorize a higher-impact action.

---

## 11. Issues Found During Evaluation

### 11.1 Requirement Lookup Regex

During the first manual demonstration, a valid requirement such as `REQ-OWN-001` returned `NOT_FOUND`.

The requirement-matching regular expression had been over-escaped.

It was corrected from an expression that treated `\d` and `\s` incorrectly to:

```python
REQ_RE = re.compile(r"^(REQ-[A-Z]+-\d+):\s*(.+)$")
```

After the correction, `REQ-OWN-001` was successfully retrieved from the controlled corpus.

### 11.2 PowerShell JSON Argument Parsing

PowerShell argument handling caused JSON containing spaces to be split before it reached the Python CLI.

For example, the initial draft-ticket invocation failed because parts of the title and description were interpreted as separate command-line arguments.

The PowerShell stop-parsing operator `--%` was used for the demonstration:

```powershell
python --% -m codeguard.tool_cli create_draft_ticket --args "{\"title\":\"Review owner search\",\"description\":\"Check negative owner-search behavior\",\"requirement_id\":\"REQ-OWN-001\"}"
```

This allowed the complete JSON object to reach the CodeGuard CLI correctly.

---

## 12. Evidence

Week 4 evaluation evidence is stored under:

```text
evidence/
├── traces/
│   └── week4/
│       ├── 01-full-pytest.txt
│       ├── 02-requirement-lookup.txt
│       ├── 03-draft-ticket.txt
│       ├── 04-unauthorized.txt
│       ├── 05-approval-required.txt
│       └── 06-approved-action.txt
│
└── tool-data/
    └── draft-tickets/
        └── DRAFT-13307568.json
```

Only evidence files that have actually been captured should be committed.

---

## 13. Evaluation Summary

The Week 4 evaluation successfully demonstrated the main CodeGuard tool-calling safety controls.

The `get_requirement` tool successfully retrieved traceable requirement information from the controlled corpus.

The `create_draft_ticket` tool successfully performed a low-risk simulated side effect by creating and persisting a local draft record.

The `publish_ticket` tests demonstrated two separate safety boundaries:

1. Role-based authorization.
2. Explicit human approval.

A normal reviewer was denied access to the action. A QA lead without explicit approval was also blocked. The simulated action succeeded only when both the appropriate role and explicit approval were supplied.

The automated regression suite also completed successfully with 21 passing tests and no test failures.

Additional failure scenarios marked **NOT YET VERIFIED** in this document must not be reported as passing until their corresponding tests or execution evidence have been completed.
