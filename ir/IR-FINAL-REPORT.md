<a id="top"></a>

> 🧭 [Scenario 02](../README.md) › [Incident Response](README.md) › **DNSentinel Scenario 02 — Incident Response / Defender Report**

<div align="center">

![Scenario](https://img.shields.io/badge/Scenario_02-COMPLETE-2EA44F?style=flat-square) ![Workspace](https://img.shields.io/badge/Workspace-Incident_Response-E5534B?style=flat-square) ![Document](https://img.shields.io/badge/Document-Evidence_Backed-D966FF?style=flat-square)

</div>

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%" alt="section divider" />

# 🛡️ DNSentinel Scenario 02 — Incident Response / Defender Report

## 🛡️ Incident identity

- **Scenario:** Scenario 02 — DGA + High NXDOMAIN
- **Incident Responder / Defender:** Abdul-Rehman
- **Resolver-visible client:** `10.50.30.20`
- **Resolver:** `dns-soc-resolver01` / `10.50.30.10`
- **Sinkhole:** `dns-soc-sinkhole01` / `10.50.30.30`
- **Observed namespace used for containment:** `*.dga-test.soclab.abdul4rehman215.tech`
- **MITRE ATT&CK context:** T1568.002 — Dynamic Resolution: Domain Generation Algorithms

## 🛡️ Independent IR validation

IR independently reproduced the core DNS evidence from `index=dns_soc_dns` rather than copying the SOC conclusion:

- 418 DNS replies
- 409 unique qnames
- 408 NXDOMAIN replies
- 97.61% NXDOMAIN ratio
- resolver-visible client `10.50.30.20`
- five consecutive one-minute matching windows in the latest investigated cluster
- repeated matching windows across multiple clusters in the prior 24 hours
- no generated-looking Scenario 02 qname successfully resolved in the investigated five-minute cluster
- no endpoint/process telemetry was available to attribute the DNS to a specific process, malware, or user

## 🛡️ IR classification

**Confirmed recurrent abnormal DGA-like / high-NXDOMAIN DNS behavior.**

The evidence did **not** prove malware identity, endpoint compromise, process identity, user identity, malicious intent, or authorization status.

## 🛡️ Response decision and approval

A human-approved, narrowly scoped DNS RPZ/sinkhole containment test was selected because it was proportionate to the confirmed resolver-visible behavior and the lab objective was to validate the defensive control.

- **Approver:** Abdul-Rehman (explicit human approval recorded before the resolver policy change)
- **Exact approval wall-clock timestamp:** not separately captured in shell/Splunk evidence; do not invent one.
- **Approved policy scope:** only the observed Scenario 02 generated namespace.
- **Sinkhole destination:** `10.50.30.30`

## 🛡️ Containment result

**SUCCESS.**

A defensible qname independently observed in DNS telemetry was used for before/after proof:

`ywvuacnec7gmul193uc.dga-test.soclab.abdul4rehman215.tech`

- **Pre-containment:** `NXDOMAIN` (direct `dig` through `10.50.30.10`)
- **Post-containment:** `NOERROR`, `A 10.50.30.30`
- **Sinkhole HTTP:** `200 OK`, controlled sinkhole page served
- **Unrelated DNS:** normal AWS name continued resolving to a public AWS address
- **Splunk:** same qname changed from `NXDOMAIN` to `NOERROR` after RPZ enforcement

## 🛡️ Reset result

**SUCCESS.** RPZ was restored to the documented safe/non-enforcing state:

- active `rpz-action-override: disabled`
- Scenario 02 wildcard removed
- Unbound configuration valid and service active
- same qname returned to `NXDOMAIN`
- unrelated AWS DNS continued to resolve normally

## 🧾 Key UTC evidence times visible in command/telemetry output

- Latest investigated cluster: approximately `2026-08-26 06:37–06:41 UTC`
- Pre-containment direct `dig`: approximately `2026-08-26 11:52:28 UTC`
- Successful RPZ redirect direct `dig`: approximately `2026-08-26 12:12:26 UTC`
- Sinkhole service HTTP evidence: approximately `2026-08-26 12:16–12:17 UTC`
- Post-reset test qname: approximately `2026-08-26 12:20:04 UTC`
- Post-reset normal AWS DNS: approximately `2026-08-26 12:20:13 UTC`

## 📌 Residual risk / unknowns

- originating process/application: unknown
- malware identity: unproven
- endpoint compromise: unproven
- user identity: unknown
- authorization/business explanation: not established by defender telemetry
- recurrence: historically confirmed, although the Scenario 02 namespace was not active during the latest 60-minute check

## 🚦 Final status

**CLOSED — controlled containment validated and safe reset completed.**
<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%" alt="section divider" />

<div align="center">

**DNSentinel Scenario 02 · Evidence before verdict · Humans before automation**

[🏠 Scenario Home](../README.md) · [🛡️ Incident Response](README.md) · [⬆ Back to top](#top)

</div>

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=30,24,19,12,6&height=75&section=footer" width="100%" alt="DNSentinel Scenario 02 footer" />
