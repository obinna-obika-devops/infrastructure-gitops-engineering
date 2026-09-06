from automation.promotion import Promotion, validate

def test_dev_to_staging():
    assert validate(Promotion("dev", "staging", "1.2.3")) == []

def test_cannot_skip_staging():
    assert "promotion must advance exactly one environment" in validate(Promotion("dev", "prod", "1.2.3"))
