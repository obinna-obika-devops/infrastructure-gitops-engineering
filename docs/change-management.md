# Change Management Model

Every change follows: proposal → CI validation → policy evaluation → review → merge → environment promotion → reconciliation → verification.

Production changes should have an owner, risk classification, rollback target, and observable success criteria. Emergency changes are exceptional and must be documented after the fact.

## Promotion gates

- Dev: automated validation
- Staging: tests plus change review
- Production: staging verification plus explicit approval

Git history provides the audit trail for desired state.