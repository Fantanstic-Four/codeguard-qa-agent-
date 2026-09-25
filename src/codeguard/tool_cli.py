import argparse,json
from dataclasses import asdict
from .tools import ToolContext,build_default_registry
def main():
 p=argparse.ArgumentParser();p.add_argument("tool");p.add_argument("--args",default="{}");p.add_argument("--role",action="append",default=[]);p.add_argument("--approve",action="append",default=[]);n=p.parse_args()
 roles=set(n.role) if n.role else {"reviewer"};r=build_default_registry().execute(n.tool,json.loads(n.args),ToolContext(roles=roles,approved_actions=set(n.approve)));print(json.dumps(asdict(r),indent=2))
if __name__=="__main__":main()
