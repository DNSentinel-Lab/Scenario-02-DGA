<a id="top"></a>

<img src="https://capsule-render.vercel.app/api?type=soft&color=gradient&customColorList=6,12,19,24,30&height=185&section=header&text=%F0%9F%9B%A1%EF%B8%8F%20Incident%20Response%20%26%20Defender%20Workspace&fontSize=30&fontColor=ffffff&animation=fadeIn&fontAlignY=38&desc=Scenario%2002%20%E2%80%94%20DGA%20%2B%20High%20NXDOMAIN%20%7C%20Abdul-Rehman%20%7C%20Human-Approved%20Containment&descSize=14&descAlignY=68&descColor=F59E0B" width="100%" alt="🛡️ Incident Response & Defender Workspace" />

<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=700&size=18&duration=2700&pause=850&color=F59E0B&center=true&vCenter=true&repeat=true&width=1080&height=62&lines=SOC+Handoff+%E2%86%92+Independent+Validation+%E2%86%92+Human+Approval+%E2%86%92+RPZ+%E2%86%92+Sinkhole+%E2%86%92+Verify+%E2%86%92+Reset;Containment+is+incomplete+until+telemetry+proves+the+outcome+changed" alt="Scenario 02 workflow animation" />

![Scenario](https://img.shields.io/badge/Scenario_02-COMPLETE-2EA44F?style=flat-square)
![Workspace](https://img.shields.io/badge/Workspace-Incident_Response-E5534B?style=flat-square)
![Responder](https://img.shields.io/badge/Responder-Abdul--Rehman-F59E0B?style=flat-square)
![Control](https://img.shields.io/badge/Control-Unbound_RPZ-14B8A6?style=flat-square)
![Evidence](https://img.shields.io/badge/Evidence-E01%E2%80%93E21-2EA44F?style=flat-square)
![Status](https://img.shields.io/badge/Status-CLOSED-2EA44F?style=flat-square)

[🏠 Scenario Home](../README.md) · [🔎 SOC](../soc/README.md) · [🚦 Detection](../detection-engineering/README.md) · [📊 Dashboard](../dashboard/README.md) · [🤖 AI](../ai/README.md) · [🧾 Evidence](evidence/README.md)

</div>

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%" alt="section divider" />

# 🛡️ Incident Response / Defender Workspace — Scenario 02

**Incident Responder / Defender:** [_Abdul-Rehman_](https://github.com/abdul4rehman215)  
**Final IR status:** **CLOSED — controlled containment validated and safe reset completed**

This folder preserves the completed Incident Response phase that began from Sonia's formal SOC handoff. IR independently reproduced the critical DNS evidence before deciding whether the prepared RPZ/sinkhole response was justified.

## 🎯 Response Snapshot

| Field | IR record |
|---|---|
| **Input** | Sonia's evidence-backed SOC handoff |
| **Independent metrics** | `418` replies · `409` unique qnames · `408` NXDOMAIN · `97.61%` |
| **Resolver-visible client** | `10.50.30.20` |
| **Containment scope** | Narrow Scenario 02 namespace control |
| **Control** | Unbound RPZ |
| **Sinkhole** | `10.50.30.30` |
| **Verification** | DNS redirect + HTTP 200 + unrelated DNS safety + Splunk before/after |
| **Reset** | Safe RPZ state restored; same qname returned to NXDOMAIN |
| **Final status** | **CLOSED** |

## 🧭 Response Lifecycle

```mermaid
flowchart LR
    A["📨 SOC Handoff"] --> B["🔎 Independent Validation"]
    B --> C["🧭 Classification"]
    C --> D["👤 Human Approval"]
    D --> E["📸 Preserve Before-State"]
    E --> F["🛡 RPZ Enforcement"]
    F --> G["🎯 Sinkhole Redirect"]
    G --> H["✅ DNS / HTTP / Splunk Verification"]
    H --> I["🌐 Normal DNS Safety"]
    I --> J["♻️ Safe Reset"]
```

## 📚 Start Here

| Artifact | Purpose |
|---|---|
| [`INCIDENT-RESPONSE.md`](INCIDENT-RESPONSE.md) | Flagship end-to-end IR story |
| [`IR-FINAL-REPORT.md`](IR-FINAL-REPORT.md) | Concise final incident report |
| [`IR-COMMAND-LEDGER.md`](IR-COMMAND-LEDGER.md) | Exact investigation and response command ledger |
| [`LESSONS-LEARNED.md`](LESSONS-LEARNED.md) | Reusable operational lessons |
| [`AI-AND-AUTOMATION-NOTE.md`](AI-AND-AUTOMATION-NOTE.md) | Automation and authority boundary |
| [`spl/README.md`](spl/README.md) | IR Splunk validation sequence |
| [`shell/README.md`](shell/README.md) | Resolver / RPZ / sinkhole / reset command sequence |
| [`evidence/README.md`](evidence/README.md) | Curated E01–E21 response evidence |

## 🧾 Evidence Highlights

<table>
<tr>
<td width="33%"><img src="evidence/S02-IR-E10-PreContainment-NXDOMAIN.png" alt="Pre-containment NXDOMAIN"><br/><sub><b>E10 · Before:</b> same qname returned NXDOMAIN before containment.</sub></td>
<td width="33%"><img src="evidence/S02-IR-E14-PostContainment-RPZ-Redirect.png" alt="RPZ redirect"><br/><sub><b>E14 · Redirect:</b> approved RPZ changed the answer to <code>10.50.30.30</code>.</sub></td>
<td width="33%"><img src="evidence/S02-IR-E17-End-to-End-Sinkhole-Reachable.png" alt="Sinkhole reachable"><br/><sub><b>E17 · Reachability:</b> victim-to-sinkhole HTTP path returned 200.</sub></td>
</tr>
<tr>
<td width="33%"><img src="evidence/S02-IR-E18-Normal-DNS-Unaffected.png" alt="Normal DNS unaffected"><br/><sub><b>E18 · Safety:</b> unrelated DNS continued to work.</sub></td>
<td width="33%"><img src="evidence/S02-IR-E19-Splunk-Before-After-RPZ.png" alt="Splunk before after"><br/><sub><b>E19 · Telemetry:</b> Splunk preserved the NXDOMAIN → NOERROR transition.</sub></td>
<td width="33%"><img src="evidence/S02-IR-E21-PostReset-DNS-Validation.png" alt="Post reset DNS"><br/><sub><b>E21 · Reset:</b> safe-state restoration returned the qname to NXDOMAIN.</sub></td>
</tr>
</table>

## ⚖️ Response Boundary

IR confirmed recurrent abnormal DGA-like/high-NXDOMAIN behavior and a defensible narrow containment target. It did **not** claim malware, process identity, endpoint compromise, user identity, intent, or authorization when those facts were absent from defender telemetry.

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%" alt="section divider" />

<div align="center">

**Validate independently. Contain narrowly. Verify technically. Reset safely.**

[🏠 Scenario Home](../README.md) · [📖 Flagship IR Story](INCIDENT-RESPONSE.md) · [🔎 IR SPL](spl/README.md) · [🧰 IR Shell](shell/README.md) · [⬆ Back to top](#top)

</div>

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=30,24,19,12,6&height=75&section=footer" width="100%" alt="DNSentinel Scenario 02 footer" />
