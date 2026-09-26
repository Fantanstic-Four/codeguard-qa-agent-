import pytest
from codeguard.tools.draft_ticket import create_draft_ticket
from codeguard.tools.types import ToolContext,ToolError
def test_missing_parameter(tmp_path):
 with pytest.raises(ToolError) as e:create_draft_ticket({"title":"x"},ToolContext(),tmp_path)
 assert e.value.code=="MISSING_PARAMETER"
def test_local_draft(tmp_path):
 r=create_draft_ticket({"title":"Review","description":"Check owner search"},ToolContext(),tmp_path);assert r.ok and r.data["status"]=="draft"
