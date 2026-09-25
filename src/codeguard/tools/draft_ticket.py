import json,uuid
from datetime import datetime,timezone
from pathlib import Path
from .types import ToolContext,ToolError,ToolResult
def create_draft_ticket(args,ctx,repo_root="."):
 if not(ctx.roles&{"reviewer","qa_lead"}): raise ToolError("UNAUTHORIZED","reviewer or qa_lead required")
 title=str(args.get("title","")).strip(); desc=str(args.get("description","")).strip()
 if not title or not desc: raise ToolError("MISSING_PARAMETER","title and description are required")
 tid=f"DRAFT-{uuid.uuid4().hex[:8].upper()}"; out=Path(repo_root)/"evidence/tool-data/draft-tickets";out.mkdir(parents=True,exist_ok=True)
 rec={"ticket_id":tid,"status":"draft","title":title,"description":desc,"requirement_id":args.get("requirement_id"),"created_by":ctx.user_id,"created_at":datetime.now(timezone.utc).isoformat()}
 path=out/f"{tid}.json";path.write_text(json.dumps(rec,indent=2),encoding="utf-8")
 return ToolResult(True,"create_draft_ticket",{"ticket_id":tid,"status":"draft","path":str(path)})
