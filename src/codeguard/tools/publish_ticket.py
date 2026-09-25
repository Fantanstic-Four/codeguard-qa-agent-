from .types import ToolError,ToolResult
def publish_ticket(args,ctx,repo_root="."):
 if "qa_lead" not in ctx.roles: raise ToolError("UNAUTHORIZED","qa_lead required")
 tid=str(args.get("ticket_id","")).strip()
 if not tid: raise ToolError("MISSING_PARAMETER","ticket_id is required")
 key=f"publish_ticket:{tid}"
 if key not in ctx.approved_actions: raise ToolError("APPROVAL_REQUIRED",f"human approval required for {key}")
 return ToolResult(True,"publish_ticket",{"ticket_id":tid,"status":"simulated_published"})
