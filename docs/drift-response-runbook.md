# Drift Response Runbook

1. Confirm whether the drift is intentional.
2. Identify the resource, actor, timestamp, and environment.
3. Classify as expected, actionable, or dangerous.
4. For dangerous drift, contain exposure before reconciliation.
5. Restore the Git-declared state through the normal GitOps path.
6. If the desired state is wrong, fix Git first rather than editing the cluster.
7. Record the incident and add preventive policy where appropriate.

Never silently accept recurring drift.