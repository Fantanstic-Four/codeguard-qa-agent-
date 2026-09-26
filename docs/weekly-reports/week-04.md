
Week 4: Tools and Function Calling

Work completed

- Defined explicit CodeGuard tools.
- Implemented requirement retrieval.
- Implemented local draft-ticket creation.
- Integrated tool execution with application orchestration.
- Added deterministic authorization.
- Added human approval for higher-impact action.
- Evaluated successful and failure scenarios.

Actual evaluation

- Full pytest suite: [FINAL result after Member 3 integration]
- get_requirement: successful
- create_draft_ticket: successful
- draft record: DRAFT-13307568
- unauthorized publication: correctly denied
- qa_lead without approval: correctly denied
- qa_lead with explicit approval: simulated publication successful

Challenges

- Successful requirement lookup initially returned NOT_FOUND because the
  requirement regex was over-escaped.
- Regex was corrected and REQ-OWN-001 was successfully retrieved.
- PowerShell argument parsing interfered with JSON containing spaces.
- PowerShell stop-parsing (--%) was used for reliable CLI demonstration.

Evidence

- PR links
- commit links
- ClickUp links
- evidence/traces/week4/*
- evidence/tool-data/draft-tickets/DRAFT-13307568.json
