import argparse
import json
from pathlib import Path

SEVERITY = {
    "public_exposure": "critical",
    "unexpected_resource": "high",
    "configuration_change": "medium",
    "tag_drift": "low",
}

EXIT_CODES = {
    "clean": 0,
    "drift": 2,
    "dangerous": 3,
}


def classify(item):
    kind = item.get("kind", "unknown")
    severity = SEVERITY.get(kind, "medium")
    managed = item.get("managed", True)

    if kind in {"unexpected_resource", "public_exposure"}:
        status = "dangerous"
    elif managed is False:
        status = "actionable"
    else:
        status = "expected"

    return {
        "resource": item.get("resource", "unknown"),
        "kind": kind,
        "status": status,
        "severity": severity,
        "managed": managed,
        "detail": item.get("detail", ""),
    }


def analyze(data):
    findings = [classify(item) for item in data.get("changes", [])]
    summary = {
        "total": len(findings),
        "dangerous": sum(1 for f in findings if f["status"] == "dangerous"),
        "actionable": sum(1 for f in findings if f["status"] == "actionable"),
        "expected": sum(1 for f in findings if f["status"] == "expected"),
    }
    return {"summary": summary, "findings": findings}


def exit_code(report):
    if report["summary"]["dangerous"]:
        return EXIT_CODES["dangerous"]
    if report["summary"]["actionable"]:
        return EXIT_CODES["drift"]
    return EXIT_CODES["clean"]


def main():
    parser = argparse.ArgumentParser(description="Classify infrastructure drift")
    parser.add_argument("path", nargs="?", default="examples/drift.json")
    parser.add_argument("--json", action="store_true", dest="json_output")
    parser.add_argument("--fail-on-drift", action="store_true")
    args = parser.parse_args()

    data = json.loads(Path(args.path).read_text())
    report = analyze(data)

    if args.json_output:
        print(json.dumps(report, indent=2, sort_keys=True))
    else:
        for finding in report["findings"]:
            print(
                f"{finding['severity']} {finding['status']}: "
                f"{finding['resource']} — {finding['detail']}"
            )
        print(json.dumps(report["summary"], sort_keys=True))

    if args.fail_on_drift:
        raise SystemExit(exit_code(report))


if __name__ == "__main__":
    main()
