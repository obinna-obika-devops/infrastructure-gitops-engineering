import re
from dataclasses import dataclass

ORDER = {"dev": 0, "staging": 1, "prod": 2}
VERSION_PATTERN = re.compile(r"^(?:v?\d+\.\d+\.\d+(?:[-+][A-Za-z0-9.-]+)?|sha256:[a-f0-9]{64})$")


@dataclass(frozen=True)
class Promotion:
    source: str
    target: str
    version: str


def validate(promotion: Promotion) -> list[str]:
    errors: list[str] = []

    if promotion.source not in ORDER or promotion.target not in ORDER:
        errors.append("unknown environment")
    elif ORDER[promotion.target] != ORDER[promotion.source] + 1:
        errors.append("promotion must advance exactly one environment")

    version = promotion.version.strip()
    if not version:
        errors.append("version is required")
    elif version.lower() == "latest":
        errors.append("mutable latest tag is not allowed")
    elif not VERSION_PATTERN.fullmatch(version):
        errors.append("version must be semantic version or sha256 digest")

    return errors
