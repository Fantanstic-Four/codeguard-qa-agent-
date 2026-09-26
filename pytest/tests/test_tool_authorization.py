import pytest
from codeguard.tools.publish_ticket import publish_ticket
from codeguard.tools.types import ToolContext,ToolError
def test_requires_role():
 with pytest.raises(ToolError) as e:publish_ticket({"ticket_id":"DRAFT-1"},ToolContext(roles={"reviewer"}));assert e.value.code=="UNAUTHORIZED"
def test_requires_approval():
 with pytest.raises(ToolError) as e:publish_ticket({"ticket_id":"DRAFT-1"},ToolContext(roles={"qa_lead"}));assert e.value.code=="APPROVAL_REQUIRED"
def test_approved():
 r=publish_ticket({"ticket_id":"DRAFT-1"},ToolContext(roles={"qa_lead"},approved_actions={"publish_ticket:DRAFT-1"}));assert r.ok
