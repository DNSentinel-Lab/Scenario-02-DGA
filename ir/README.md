# Incident Response Workspace — Scenario 02 DGA + High NXDOMAIN Activity

**Status:** Reusable RPZ/sinkhole control is infrastructure-ready; Scenario 02 IR exercise not performed.

The shared Infrastructure repository already proved that Unbound can log an RPZ match, redirect one controlled hostname to `10.50.30.30`, produce sinkhole Nginx evidence, and return to disabled enforcement afterward.

That technical validation is **not** the human Scenario 02 response record.

## Future response rule

```text
Finding
→ human SOC investigation
→ approved containment decision
→ enable approved RPZ response
→ expected DNS change
→ sinkhole/network evidence
→ verification
→ reset to safe state
```

Do not treat a detection, ML anomaly score or AI summary as automatic authorization.

## Expected evidence later

- analyst-confirmed finding;
- who approved/performed containment;
- exact RPZ rule/pattern used for the scenario;
- pre-response DNS result;
- post-response `10.50.30.30` result;
- sinkhole access evidence;
- final reset and verification.

No Scenario 02 IR artifact exists here yet.
