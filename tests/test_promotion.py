from automation.promotion import Promotion, validate


def test_dev_to_staging():
    assert validate(Promotion("dev", "staging", "1.2.3")) == []


def test_cannot_skip_staging():
    assert "promotion must advance exactly one environment" in validate(
        Promotion("dev", "prod", "1.2.3")
    )


def test_unknown_environment_is_rejected():
    assert "unknown environment" in validate(Promotion("qa", "prod", "1.2.3"))


def test_latest_tag_is_rejected():
    assert "mutable latest tag is not allowed" in validate(
        Promotion("dev", "staging", "latest")
    )


def test_invalid_version_is_rejected():
    assert "version must be semantic version or sha256 digest" in validate(
        Promotion("dev", "staging", "release-candidate")
    )


def test_digest_version_is_accepted():
    digest = "sha256:" + "a" * 64
    assert validate(Promotion("staging", "prod", digest)) == []
