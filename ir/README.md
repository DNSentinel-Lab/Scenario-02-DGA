<a id="top"></a>

<img src="https://capsule-render.vercel.app/api?type=soft&color=gradient&height=185&section=header&text=Incident%20Response%20and%20Defender%20Workspace&fontSize=30&fontColor=ffffff&animation=fadeIn&fontAlignY=38&desc=Scenario%2002%20-%20DGA%20plus%20High%20NXDOMAIN%20-%20Abdul-Rehman%20-%20Human-Approved%20Containment&descSize=14&descAlignY=68" width="100%" alt="🛡️ Incident Response & Defender Workspace" />

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

    %% =====================================================
    %% COLUMN 1 — VALIDATE & DECIDE
    %% =====================================================
    subgraph VALIDATE[" "]
        direction TB

        VH["🔎 1 · Validate & Decide"]

        A["📨 SOC<br/>Handoff"]
        B["🔎 Independent<br/>Validation"]
        C["🧭 Classification"]
        D["👤 Human<br/>Approval"]

        VH --> A --> B --> C --> D
    end


    %% =====================================================
    %% COLUMN 2 — PRESERVE & CONTAIN
    %% =====================================================
    subgraph CONTAIN[" "]
        direction TB

        CH["🛡️ 2 · Preserve & Contain"]

        E["📸 Preserve<br/>Before-State"]
        F["🛡️ RPZ<br/>Enforcement"]
        G["🎯 Sinkhole<br/>Redirect"]

        CH --> E --> F --> G
    end


    %% =====================================================
    %% COLUMN 3 — VERIFY & RECOVER
    %% =====================================================
    subgraph VERIFY[" "]
        direction TB

        RH["✅ 3 · Verify & Recover"]

        H["✅ DNS + HTTP + Splunk<br/>Verification"]
        I["🌐 Normal DNS<br/>Safety"]
        J["♻️ Safe<br/>Reset"]

        RH --> H --> I --> J
    end


    %% =====================================================
    %% COLUMN-TO-COLUMN FLOW
    %% =====================================================
    VALIDATE --> CONTAIN
    CONTAIN --> VERIFY


    %% =====================================================
    %% HEADER STYLING
    %% =====================================================
    classDef validateHeader fill:#0b2239,stroke:#60a5fa,stroke-width:2px,color:#ffffff;
    classDef containHeader fill:#2a1111,stroke:#f87171,stroke-width:2px,color:#ffffff;
    classDef verifyHeader fill:#0f2a1d,stroke:#4ade80,stroke-width:2px,color:#ffffff;

    class VH validateHeader;
    class CH containHeader;
    class RH verifyHeader;


    %% =====================================================
    %% NODE STYLING
    %% =====================================================
    classDef handoff fill:#172554,stroke:#60a5fa,stroke-width:2px,color:#ffffff;
    classDef validate fill:#083344,stroke:#22d3ee,stroke-width:2px,color:#ffffff;
    classDef decision fill:#3b0764,stroke:#c084fc,stroke-width:2px,color:#ffffff;
    classDef approval fill:#422006,stroke:#fbbf24,stroke-width:2px,color:#ffffff;

    classDef preserve fill:#312e81,stroke:#818cf8,stroke-width:2px,color:#ffffff;
    classDef enforce fill:#450a0a,stroke:#f87171,stroke-width:2px,color:#ffffff;
    classDef sinkhole fill:#7c2d12,stroke:#fb923c,stroke-width:2px,color:#ffffff;

    classDef verifyok fill:#052e16,stroke:#4ade80,stroke-width:2px,color:#ffffff;
    classDef safety fill:#134e4a,stroke:#2dd4bf,stroke-width:2px,color:#ffffff;
    classDef reset fill:#1f2937,stroke:#94a3b8,stroke-width:2px,color:#ffffff;

    class A handoff;
    class B validate;
    class C decision;
    class D approval;

    class E preserve;
    class F enforce;
    class G sinkhole;

    class H verifyok;
    class I safety;
    class J reset;


    %% =====================================================
    %% CONTAINER STYLING
    %% =====================================================
    style VALIDATE fill:#0d1117,stroke:#60a5fa,stroke-width:1px
    style CONTAIN fill:#0d1117,stroke:#f87171,stroke-width:1px
    style VERIFY fill:#0d1117,stroke:#4ade80,stroke-width:1px

    linkStyle default stroke:#94a3b8,stroke-width:2px
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
