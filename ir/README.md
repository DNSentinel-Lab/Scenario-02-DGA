# Incident Response Workspace — Scenario 02 DGA + High NXDOMAIN Activity

**Status:** Planned.

This folder records the human response decision, approved containment, verification and cleanup/reset actions for the scenario.

## Response rule

After human confirmation, use the team-controlled resolver to apply the approved sinkhole/deny action and prove that subsequent victim DNS behavior changes. Generated public Route 53 records are not created simply to avoid NXDOMAIN.

A complete response record should show:

```text
Finding
→ human decision
→ approved action
→ expected technical change
→ observed post-response evidence
→ final verification
```

Do not treat a Splunk alert or AI summary as automatic response authorization.

## Final artifacts later

The exact files depend on the exercise. A completed scenario may include an incident-response note/playbook, containment commands/configuration and a before/after verification record.
