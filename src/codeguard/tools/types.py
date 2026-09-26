from dataclasses import dataclass,field
from typing import Any
@dataclass
class ToolContext:
 user_id:str="local-user"; roles:set[str]=field(default_factory=lambda:{"reviewer"}); approved_actions:set[str]=field(default_factory=set)
@dataclass
class ToolResult:
 ok:bool; tool:str; data:dict[str,Any]=field(default_factory=dict); error_code:str|None=None; message:str=""
class ToolError(Exception):
 def __init__(self,code,message): super().__init__(message); self.code=code; self.message=message
