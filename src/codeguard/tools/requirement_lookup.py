import re
from pathlib import Path
from .types import ToolContext,ToolError,ToolResult
REQ_RE=re.compile(r"^(REQ-[A-Z]+-\\d+):\\s*(.+)$")
def get_requirement(args,ctx,repo_root="."):
 if not(ctx.roles&{"reviewer","qa_lead"}): raise ToolError("UNAUTHORIZED","reviewer or qa_lead required")
 rid=str(args.get("requirement_id","")).strip()
 if not rid: raise ToolError("MISSING_PARAMETER","requirement_id is required")
 corpus=Path(repo_root)/"knowledge/corpus"
 if not corpus.exists(): raise ToolError("SERVICE_UNAVAILABLE","controlled corpus unavailable")
 for p in corpus.glob("*.md"):
  for line in p.read_text(encoding="utf-8").splitlines():
   m=REQ_RE.match(line.strip())
   if m and m.group(1)==rid: return ToolResult(True,"get_requirement",{"requirement_id":rid,"source_id":p.stem,"text":m.group(2)})
 return ToolResult(False,"get_requirement",{}, "NOT_FOUND",f"{rid} not found")
