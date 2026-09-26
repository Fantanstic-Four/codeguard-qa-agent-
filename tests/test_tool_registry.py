from codeguard.tools import ToolContext,build_default_registry
def test_unknown_tool():
 r=build_default_registry().execute("missing",{},ToolContext());assert not r.ok and r.error_code=="UNKNOWN_TOOL"
