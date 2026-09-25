import pytest
from codeguard.tools.requirement_lookup import get_requirement
from codeguard.tools.types import ToolContext,ToolError
def test_missing_parameter():
 with pytest.raises(ToolError) as e:get_requirement({},ToolContext(),".")
 assert e.value.code=="MISSING_PARAMETER"
def test_unauthorized():
 with pytest.raises(ToolError) as e:get_requirement({"requirement_id":"REQ-OWN-001"},ToolContext(roles={"guest"}),".")
 assert e.value.code=="UNAUTHORIZED"
