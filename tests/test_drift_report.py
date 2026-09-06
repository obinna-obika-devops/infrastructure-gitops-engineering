from automation.drift_report import analyze, classify, exit_code


def test_public_exposure_is_critical_and_dangerous():
    finding = classify({"resource": "sg", "kind": "public_exposure"})
    assert finding["severity"] == "critical"
    assert finding["status"] == "dangerous"


def test_unmanaged_change_is_actionable():
    report = analyze(
        {
            "changes": [
                {
                    "resource": "bucket",
                    "kind": "configuration_change",
                    "managed": False,
                }
            ]
        }
    )
    assert report["summary"]["actionable"] == 1
    assert exit_code(report) == 2


def test_dangerous_drift_uses_distinct_exit_code():
    report = analyze(
        {"changes": [{"resource": "sg", "kind": "public_exposure"}]}
    )
    assert report["summary"]["dangerous"] == 1
    assert exit_code(report) == 3


def test_clean_report_exits_zero():
    report = analyze({"changes": []})
    assert report["summary"]["total"] == 0
    assert exit_code(report) == 0
