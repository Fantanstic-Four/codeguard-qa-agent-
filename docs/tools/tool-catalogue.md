# Week 4 Tool Catalogue

| Tool | Purpose | Impact | Authorization |
|---|---|---|---|
| `get_requirement` | Retrieve approved requirement data | Read-only | reviewer / qa_lead |
| `create_draft_ticket` | Create local draft QA ticket | Low-risk simulated side effect | reviewer / qa_lead |
| `publish_ticket` | Simulate publication | Higher-impact simulated | qa_lead + human approval |

The required demonstrations are `get_requirement` and `create_draft_ticket`. `publish_ticket` demonstrates the human-approval boundary.
