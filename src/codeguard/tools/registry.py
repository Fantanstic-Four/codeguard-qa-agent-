from pathlib import Path
from .catalog import TOOL_CATALOGUE
from .types import ToolResult,ToolError
from .requirement_lookup import get_requirement
from .draft_ticket import create_draft_ticket
from .publish_ticket import publish_ticket
class ToolRegistry:
 def __init__(self,repo_root="."): self.repo_root=Path(repo_root);self.handlers={"get_requirement":get_requirement,"create_draft_ticket":create_draft_ticket,"publish_ticket":publish_ticket}
 def catalogue(self): return TOOL_CATALOGUE
 def execute(self,name,args,ctx):
  if name not in self.handlers:return ToolResult(False,name,{},"UNKNOWN_TOOL",f"Unknown tool: {name}")
  try:return self.handlers[name](args,ctx,self.repo_root)
  except ToolError as e:return ToolResult(False,name,{},e.code,e.message)
  except Exception as e:return ToolResult(False,name,{},"UNEXPECTED_TOOL_RESPONSE",str(e))
def build_default_registry(repo_root="."):return ToolRegistry(repo_root)
