<a id="top"></a>

> 🧭 [Scenario 02](../README.md) › [Detection SPL](README.md) › **Scenario 02 - Scheduled Alert**

<div align="center">

![Scenario](https://img.shields.io/badge/Scenario_02-COMPLETE-2EA44F?style=flat-square) ![Workspace](https://img.shields.io/badge/Workspace-Detection_SPL-D966FF?style=flat-square) ![Document](https://img.shields.io/badge/Document-Evidence_Backed-D966FF?style=flat-square)

</div>

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%" alt="section divider" />

# 🚨 Scenario 02 - Scheduled Alert

Alert name: `Scenario 02 - Possible DGA / High NXDOMAIN`

Detection version: `1.0`

MITRE: `T1568.002 - Dynamic Resolution: Domain Generation Algorithms`

Severity: `medium`

## 🚨 Frozen detection boundary

- Analytical side: `event_type="reply"`
- Entity: `client_ip`
- Window: 1 minute
- `query_count >= 20`
- `unique_qnames >= 15`
- `nxdomain_ratio >= 0.75`

## ⏱️ Schedule

- Alert type: Scheduled
- Cron: `* * * * *`
- Earliest: `-2m@m`
- Latest: `-1m@m`
- Trigger: Number of Results > 0
- Trigger mode: Once
- Throttle during validation: OFF

Rationale: Detection Engineering measured DNS ingestion p95 at about 9.2 seconds. Searching the previous completed minute gives events far more time than that to arrive while avoiding overlap-based duplicate detection.

## 🚨 Trigger actions

1. Add to Triggered Alerts
   - Severity: Medium
2. Webhook
   - `http://dns-soc-ai-bridge:5000/splunk-webhook`

## 🧾 Validation

A controlled 45-second DGA validation ran on 2026-08-25 from 09:09:34Z to 09:10:19Z. The scheduled alert produced a real result for the 09:09 minute with:

- client_ip: 10.50.30.20
- query_count: 41
- unique_qnames: 37
- unique_qname_ratio: 0.9024
- nxdomain_count: 36
- nxdomain_ratio: 0.8780

The result preserved Detection v1.0 metadata and a raw-event path back to `index=dns_soc_dns`.

The initial AI webhook test received HTTP 400 because the scheduled result did not yet carry the common alert/evidence contract. The final [`detection.spl`](detection.spl) was updated only at the result-contract layer; the frozen threshold logic did not change.

The corrected AI retest succeeded end-to-end and indexed structured output into `index=dns_soc_ai`, `sourcetype=dns_soc:ai:triage`.
<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%" alt="section divider" />

<div align="center">

**DNSentinel Scenario 02 · Evidence before verdict · Humans before automation**

[🏠 Scenario Home](../README.md) · [🔎 Detection SPL](README.md) · [⬆ Back to top](#top)

</div>

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=30,24,19,12,6&height=75&section=footer" width="100%" alt="DNSentinel Scenario 02 footer" />
