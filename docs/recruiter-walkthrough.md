# Recruiter / Interview Walkthrough

Use this page to evaluate the GitOps and infrastructure change-management engineering in a few minutes.

## 5-minute review path

1. Read `README.md` for the operating model.
2. Inspect `terraform/` for environment-aware infrastructure definitions.
3. Inspect `gitops/` for declarative desired state and environment overlays.
4. Inspect `automation/` and `scripts/` for promotion, drift and rollback logic.
5. Inspect `policies/` for policy-as-code controls.
6. Inspect `tests/` and `.github/` for automated validation.
7. Review `docs/` for ADRs and operational procedures.

## What this project proves

This project focuses on the lifecycle of infrastructure change, not just provisioning. The core idea is that infrastructure changes should be reviewable, policy-checked, promoted deliberately, continuously reconciled and recoverable.

Engineering themes demonstrated here include:

- Git as the desired-state source of truth
- Terraform-based environment promotion
- GitOps reconciliation
- drift detection and classification
- policy gates before promotion
- rollback planning
- auditable change records
- Kubernetes overlays and safe workload defaults
- Python automation and testable change-management logic

## Interview discussion points

### How does this reduce operational risk?
Changes flow through pull requests and automated validation before promotion. Production is treated as a controlled destination rather than a place where ad-hoc changes are made directly.

### What is the difference between drift detection and reconciliation?
Drift detection identifies differences between declared and observed state. Reconciliation attempts to restore the declared state. Separating the concepts helps determine when automatic correction is safe and when human review is required.

### How would rollback work?
The workflow identifies the last known-good revision and creates a recovery plan before a risky promotion. In a production environment, rollback would also be constrained by stateful dependencies, schema compatibility and approval policy.

### What would be added in an enterprise environment?
Typical additions would include remote state with locking, federated cloud identity, protected environments, required reviewers, signed artifacts, centralized audit events, production notification routing and integration with change-management systems.

## Local validation

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest -q
terraform -chdir=terraform fmt -check -recursive
terraform -chdir=terraform init -backend=false
terraform -chdir=terraform validate
```

## Scope and integrity

This is a portfolio/reference implementation. It demonstrates production-grade patterns without claiming that the repository currently controls live production infrastructure.
