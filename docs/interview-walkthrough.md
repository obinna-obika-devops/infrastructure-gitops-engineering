# GitOps Interview Walkthrough

## 60-second explanation

This project demonstrates how infrastructure changes can be governed through Git instead of relying on manual cloud-console changes. Pull requests become the change-control entry point, CI validates Terraform and Kubernetes configuration, policy gates block unsafe changes, environments are promoted in order, and reconciliation keeps the running state aligned with declared state.

## Why GitOps?

GitOps gives infrastructure changes a reviewable and auditable lifecycle. Desired state is versioned, promotion is explicit, and rollback can reference a known-good revision instead of depending on memory or manual reconstruction.

## Drift detection

Drift is not treated as a binary condition. The design separates expected, actionable and dangerous drift so teams can respond according to operational risk rather than blindly overwriting every difference.

## Promotion model

Changes move through dev, staging and production rather than being applied directly to the highest-risk environment. Promotion checks validate order and required controls before a version advances.

## Reliability and security

Policy-as-code catches unsafe infrastructure patterns before deployment. Rollback planning is part of the change process, not something invented after a failed release. Automation should be idempotent and auditable so repeated execution does not create unpredictable state.

## Failure scenarios to discuss

- Manual infrastructure drift outside Git
- A Terraform change that violates policy
- A bad release reaching staging
- Reconciliation detecting divergence
- A failed production promotion
- Need to restore the last known-good revision

## Enterprise additions

For a live enterprise implementation, I would add remote Terraform state and locking, cloud identity federation, environment protection rules, signed commits/artifacts where required, richer drift evidence, change-ticket integration, deployment metrics and tested rollback automation.

## Key takeaway

GitOps is not only a deployment tool. It is an operating model for making infrastructure changes controlled, reviewable, observable and recoverable.