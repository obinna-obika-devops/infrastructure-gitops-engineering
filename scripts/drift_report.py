import json, sys
from pathlib import Path

def classify(item):
    kind = item.get("kind", "unknown")
    if kind in {"unexpected_resource", "public_exposure"}:
        return "dangerous"
    if item.get("managed", True) is False:
        return "actionable"
    return "expected"

p = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("examples/drift.json")
data = json.loads(p.read_text())
for item in data.get("changes", []):
    print(f"{classify(item)}: {item.get('resource', 'unknown')} — {item.get('detail', '')}")
