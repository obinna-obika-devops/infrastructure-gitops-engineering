from dataclasses import dataclass
ORDER = {"dev": 0, "staging": 1, "prod": 2}
@dataclass(frozen=True)
class Promotion:
    source: str
    target: str
    version: str
def validate(p: Promotion) -> list[str]:
    errors=[]
    if p.source not in ORDER or p.target not in ORDER: errors.append("unknown environment")
    elif ORDER[p.target] != ORDER[p.source] + 1: errors.append("promotion must advance exactly one environment")
    if not p.version.strip(): errors.append("version is required")
    return errors
