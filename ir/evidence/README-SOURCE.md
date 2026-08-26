<a id="top"></a>

> 🧭 [Scenario 02](../../README.md) › [Incident Response](../README.md) › **DNSentinel Scenario 02 — Curated IR/Defender Evidence**

<div align="center">

![Scenario](https://img.shields.io/badge/Scenario_02-COMPLETE-2EA44F?style=flat-square) ![Workspace](https://img.shields.io/badge/Workspace-Incident_Response-E5534B?style=flat-square) ![Document](https://img.shields.io/badge/Document-Evidence_Backed-D966FF?style=flat-square)

</div>

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%" alt="section divider" />

# 🛡️ DNSentinel Scenario 02 — Curated IR/Defender Evidence

This is the **recommended GitHub evidence set** for Scenario 02 Incident Response. The screenshots were renamed consistently and trimmed only to remove empty black margins; no event values, commands, or results were altered.

## 📌 Recommended usage

- Put the images under a scenario path such as `incident-response/evidence/`.
- Keep **E01–E09** for independent validation and scope.
- Keep **E10–E19** for containment and verification.
- Keep **E20–E21** for reset/recovery proof.
- Keep troubleshooting screenshots out of the main README unless you want a dedicated lessons-learned section. They remain available in the complete raw screenshot archive.

## 🧾 Evidence table

| ID | File | Category | What it proves |
|---|---|---|---|
| E01 | `S02-IR-E01-Raw-DNS-Window-Presence.png` | Primary validation | Shows 836 raw Unbound events in the exact 06:37–06:42 UTC window; supports 418 query/reply pairs. |
| E02 | `S02-IR-E02-Core-DNS-Metrics.png` | Primary validation | IR independently reproduced 418 replies, 409 unique qnames, 408 NXDOMAIN, 97.61%, client 10.50.30.20. |
| E03 | `S02-IR-E03-One-Minute-Validation.png` | Primary validation | Five consecutive 1-minute windows all meet the detection-like thresholds. |
| E04 | `S02-IR-E04-Raw-Qname-Examples.png` | Primary validation | Shows highly variable alphanumeric first labels under the observed dga-test namespace and NXDOMAIN responses. |
| E05 | `S02-IR-E05-Client-Scope.png` | Primary validation | Shows only resolver-visible client 10.50.30.20 in the investigated window. |
| E06 | `S02-IR-E06-Non-NXDOMAIN-Review.png` | Primary validation | Shows the 10 successful replies were normal AWS service names and not the generated-looking namespace. |
| E07 | `S02-IR-E07-Endpoint-Telemetry-Availability.png` | Attribution limits | Shows available DNS/ML/AWS telemetry but no endpoint/process telemetry proving process identity. |
| E08 | `S02-IR-E08-Historical-Recurrence.png` | Risk assessment | Shows 15 matching 1-minute windows across multiple separate clusters in the previous 24 hours. |
| E09 | `S02-IR-E09-Current-Activity-Check.png` | Risk assessment | Latest 60-minute check shows zero Scenario 02 namespace replies; activity was not active at that moment. |
| E10 | `S02-IR-E10-PreContainment-NXDOMAIN.png` | Containment before | Same defensible observed qname returns NXDOMAIN before containment. |
| E11 | `S02-IR-E11-PreChange-RPZ-Safe-State.png` | Change control | Shows RPZ loaded with enforcement disabled, reusable test record only, and valid Unbound configuration. |
| E12 | `S02-IR-E12-RPZ-Scenario02-Rule-Staged.png` | Change control | Shows narrow wildcard for dga-test namespace added and configuration check passes. |
| E13 | `S02-IR-E13-RPZ-Runtime-Activated.png` | Change control | Shows backup moved out of Unbound include directory, clean config, service active, and cache flush. |
| E14 | `S02-IR-E14-PostContainment-RPZ-Redirect.png` | Containment after | Exact same qname now returns NOERROR with A 10.50.30.30. |
| E15 | `S02-IR-E15-Sinkhole-Service-Health.png` | Sinkhole validation | Shows dns-soc-sinkhole01 at 10.50.30.30 with nginx active and TCP/80 listening. |
| E16 | `S02-IR-E16-Sinkhole-Local-HTTP200.png` | Sinkhole validation | Shows local HTTP 200 and the controlled sinkhole page. |
| E17 | `S02-IR-E17-End-to-End-Sinkhole-Reachable.png` | Sinkhole validation | Victim reaches 10.50.30.30 and receives the controlled sinkhole page. |
| E18 | `S02-IR-E18-Normal-DNS-Unaffected.png` | Safety validation | Normal AWS DNS still returns a normal public A record instead of 10.50.30.30. |
| E19 | `S02-IR-E19-Splunk-Before-After-RPZ.png` | Containment telemetry | Same qname appears as NXDOMAIN before containment and NOERROR after RPZ activation. |
| E20 | `S02-IR-E20-RPZ-Safe-State-Restored.png` | Reset | Shows original safe/non-enforcing RPZ state restored, config valid, Unbound active. |
| E21 | `S02-IR-E21-PostReset-DNS-Validation.png` | Reset | After reset the test qname is NXDOMAIN again and unrelated AWS DNS resolves normally. |

## 🛡️ Core containment chain

`E10 NXDOMAIN before` → `E11/E12/E13 controlled RPZ change` → `E14 10.50.30.30 redirect` → `E15/E16/E17 sinkhole healthy/reachable` → `E18 normal DNS unaffected` → `E19 Splunk behavior changed` → `E20/E21 safe reset and recovery`.

## 🔐 Attribution boundary

These screenshots prove abnormal and recurrent resolver-visible DNS behavior and a successful defensive control. They **do not prove malware identity, endpoint compromise, process identity, user identity, malicious intent, or authorization status**.
<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%" alt="section divider" />

<div align="center">

**DNSentinel Scenario 02 · Evidence before verdict · Humans before automation**

[🏠 Scenario Home](../../README.md) · [🛡️ Incident Response](../README.md) · [⬆ Back to top](#top)

</div>

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=30,24,19,12,6&height=75&section=footer" width="100%" alt="DNSentinel Scenario 02 footer" />
