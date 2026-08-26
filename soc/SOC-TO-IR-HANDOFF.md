# SOC → IR Handoff — Scenario 02 DGA + High NXDOMAIN

## Alert identity
- Scenario: Scenario 02 — DGA + High NXDOMAIN
- Detection: Scenario 02 — Possible DGA / High NXDOMAIN
- MITRE ATT&CK: T1568.002
- SOC Analyst: Sonia
- Resolver-visible client: `10.50.30.20`
- Resolver: `dns-soc-resolver01`

## Latest investigated window
`2026-08-26 06:37:00` to `06:42:00 UTC`

## Metrics
- 418 total DNS replies
- 409 unique qnames
- 408 NXDOMAIN replies
- 97.61% NXDOMAIN ratio
- 5 consecutive Detection v1.0 matching windows
- peak queries/min: 89
- peak unique qnames/min: 87
- peak NXDOMAIN ratio: 1.000

## Baseline
Outside the latest five-minute window, the same client showed:
- avg queries/min: 6.11
- p95 queries/min: ~15.45
- avg unique qnames/min: 4.12
- p95 unique qnames/min: ~10.15
- avg NXDOMAIN ratio: 0.158
- p95 NXDOMAIN ratio: 0.508

## Repetition / scope
Similar matching activity occurred in several earlier clusters in the previous 24 hours.

Latest exact-window scope:
- one resolver-visible client
- five matching one-minute windows

## Raw DNS
The generated-looking names had long/highly variable leftmost labels and overwhelmingly returned NXDOMAIN.

The 10 non-NXDOMAIN replies in the latest window were normal-looking AWS service lookups (for example SSM and GuardDuty). No successful resolution of the generated-looking names was observed in the investigated five-minute window.

## ML
All five corresponding windows were marked `ANOMALY` by `dns_iforest_v1`.

## AI
AI broadly matched the defender evidence and correctly noted that DNS telemetry does not prove the initiating process, endpoint state, or authorization.

## SOC disposition
**INCONCLUSIVE — escalation warranted**

### Confidence
- High: abnormal DGA-like/high-NXDOMAIN behavior occurred
- High: `10.50.30.20` is the resolver-visible client
- High: defensive IR review is justified
- Low: malware/process attribution
- Unknown: authorization/business explanation

## Requested IR action
1. Independently validate the DNS evidence.
2. Preserve relevant telemetry.
3. Review endpoint/process evidence if available.
4. Determine whether an approved explanation exists.
5. Evaluate the planned DNS RPZ/sinkhole containment measure.
6. If approved, apply the defensive policy.
7. Verify in Splunk that post-containment DNS behavior is redirected/controlled.
8. Preserve before/after evidence.

Containment remains a human-approved IR decision.
