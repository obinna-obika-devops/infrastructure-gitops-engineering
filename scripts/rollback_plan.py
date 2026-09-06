import json, sys
from pathlib import Path

def plan(data):
    current = data["current"]
    target = data["target"]
    if current == target:
        return {"action": "noop", "target": target}
    return {"action": "rollback", "target": target, "reason": f"restore known-good revision {target}"}

p = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("examples/promotion.json")
print(json.dumps(plan(json.loads(p.read_text())), indent=2))
