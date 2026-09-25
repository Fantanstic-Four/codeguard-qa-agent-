# Authorization and Failure Contract

Expected controlled failures: `MISSING_PARAMETER`, `UNAUTHORIZED`, `SERVICE_UNAVAILABLE`, `UNKNOWN_TOOL`, `UNEXPECTED_TOOL_RESPONSE`, and `APPROVAL_REQUIRED`. `publish_ticket` requires both the `qa_lead` role and an explicit approval key `publish_ticket:<ticket_id>`. The model cannot grant itself approval.
