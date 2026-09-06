import pytest

from automation.rollback import plan


def test_known_good_rollback_is_planned():
    result = plan(
        {
            "current": "v1.3.0",
            "target": "v1.2.4",
            "known_good": ["v1.2.4"],
        }
    )
    assert result["action"] == "rollback"
    assert result["target"] == "v1.2.4"
    assert result["validated"] is True


def test_same_revision_is_noop():
    result = plan(
        {
            "current": "v1.2.4",
            "target": "v1.2.4",
            "known_good": ["v1.2.4"],
        }
    )
    assert result == {"action": "noop", "target": "v1.2.4", "validated": True}


def test_unknown_target_is_rejected():
    with pytest.raises(ValueError, match="not marked known-good"):
        plan(
            {
                "current": "v1.3.0",
                "target": "v1.1.0",
                "known_good": ["v1.2.4"],
            }
        )


def test_invalid_revision_is_rejected():
    with pytest.raises(ValueError, match="semantic version or sha256 digest"):
        plan({"current": "latest", "target": "v1.2.4"})
