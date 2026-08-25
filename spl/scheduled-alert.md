# Scenario 02 - Scheduled Alert

Alert name: `Scenario 02 - Possible DGA / High NXDOMAIN`

Detection version: `1.0`

MITRE: `T1568.002 - Dynamic Resolution: Domain Generation Algorithms`

Severity: `medium`

## Frozen detection boundary

- Analytical side: `event_type="reply"`
- Entity: `client_ip`
- Window: 1 minute
- `query_count >= 20`
- `unique_qnames >= 15`
- `nxdomain_ratio >= 0.75`

## Schedule

- Alert type: Scheduled
- Cron: `* * * * *`
- Earliest: `-2m@m`
- Latest: `-1m@m`
- Trigger: Number of Results > 0
- Trigger mode: Once
- Throttle during validation: OFF

Rationale: Detection Engineering measured DNS ingestion p95 at about 9.2 seconds. Searching the previous completed minute gives events far more time than that to arrive while avoiding overlap-based duplicate detection.

## Trigger actions

1. Add to Triggered Alerts
   - Severity: Medium
2. Webhook
   - `http://dns-soc-ai-bridge:5000/splunk-webhook`

## Validation

A controlled 45-second DGA validation ran on 2026-08-25 from 09:09:34Z to 09:10:19Z. The scheduled alert produced a real result for the 09:09 minute with:

- client_ip: 10.50.30.20
- query_count: 41
- unique_qnames: 37
- unique_qname_ratio: 0.9024
- nxdomain_count: 36
- nxdomain_ratio: 0.8780

The result preserved Detection v1.0 metadata and a raw-event path back to `index=dns_soc_dns`.

The initial AI webhook test received HTTP 400 because the scheduled result did not yet carry the common alert/evidence contract. The final `detection.spl` was updated only at the result-contract layer; the frozen threshold logic did not change.

The corrected AI retest succeeded end-to-end and indexed structured output into `index=dns_soc_ai`, `sourcetype=dns_soc:ai:triage`.
