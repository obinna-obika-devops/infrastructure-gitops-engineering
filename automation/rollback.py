import argparse
import json
import re
from pathlib import Path

VERSION_RE = re.compile(r"^v?\d+\.\d+\.\d+$")
SHA_RE = re.compile(r"^sha256:[a-f0-9]{64}$")


def valid_revision(value):
    return bool(VERSION_RE.fullmatch(value) or SHA_RE.fullmatch(value))


def plan(data):
    current = data.get("current", "").strip()
    target = data.get("target", "").strip()
    known_good = set(data.get("known_good", []))

    if not current or not target:
        raise ValueError("current and target revisions are required")
    if not valid_revision(current):
        raise ValueError("current revision must be semantic version or sha256 digest")
    if not valid_revision(target):
        raise ValueError("target revision must be semantic version or sha256 digest")
    if known_good and target not in known_good:
        raise ValueError("target revision is not marked known-good")
    if current == target:
        return {"action": "noop", "target": target, "validated": True}

    return {
        "action": "rollback",
        "from": current,
        "target": target,
        "validated": True,
        "reason": f"restore known-good revision {target}",
    }


def main():
    parser = argparse.ArgumentParser(description="Create a validated rollback plan")
    parser.add_argument("path", nargs="?", default="examples/promotion.json")
    args = parser.parse_args()

    data = json.loads(Path(args.path).read_text())
    print(json.dumps(plan(data), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
