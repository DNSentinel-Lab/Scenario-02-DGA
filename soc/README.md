<a id="top"></a>

<img src="https://capsule-render.vercel.app/api?type=soft&color=gradient&height=185&section=header&text=SOC%20Analyst%20and%20Threat%20Hunting%20Workspace&fontSize=30&fontColor=ffffff&animation=fadeIn&fontAlignY=38&desc=Scenario%2002%20-%20DGA%20plus%20High%20NXDOMAIN%20-%20Sonia%20-%20Defender-Only%20Investigation&descSize=14&descAlignY=68" width="100%" alt="🔎 SOC Analyst & Threat Hunting Workspace" />

<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=700&size=18&duration=2700&pause=850&color=22D3EE&center=true&vCenter=true&repeat=true&width=1080&height=62&lines=Alert+%E2%86%92+Raw+DNS+%E2%86%92+Baseline+%E2%86%92+Scope+%E2%86%92+ML+%2F+AI+Validation+%E2%86%92+5W1H+%E2%86%92+IR+Handoff;Investigate+what+the+telemetry+proves+%E2%80%94+preserve+what+it+cannot+prove" alt="Scenario 02 workflow animation" />

![Scenario](https://img.shields.io/badge/Scenario_02-COMPLETE-2EA44F?style=flat-square)
![Workspace](https://img.shields.io/badge/Workspace-SOC_Investigation-0284C7?style=flat-square)
![Analyst](https://img.shields.io/badge/Analyst-Sonia-22D3EE?style=flat-square)
![Disposition](https://img.shields.io/badge/Disposition-INCONCLUSIVE_%E2%86%92_IR-F59E0B?style=flat-square)
![Evidence](https://img.shields.io/badge/Evidence-E01%E2%80%93E13-A855F7?style=flat-square)

[🏠 Scenario Home](../README.md) · [🚦 Detection](../detection-engineering/README.md) · [📊 Dashboard](../dashboard/README.md) · [🧠 ML](../ml/README.md) · [🤖 AI](../ai/README.md) · [🛡️ IR](../ir/README.md) · [🧾 Evidence](evidence/README.md)

</div>

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%" alt="section divider" />

# 🔎 SOC Analyst Workspace — Scenario 02

**SOC Analyst:** [_Sonia_](https://github.com/sonia11mansha415)  
**Scenario:** DGA + High NXDOMAIN  
**Final disposition:** **INCONCLUSIVE — escalation warranted**

This folder preserves the completed defender-side investigation. Sonia received defender telemetry rather than operator ground truth and worked from the frozen production detection back into raw resolver evidence before using ML or AI.

## 🎯 Case Snapshot

| Field | Defender record |
|---|---|
| **Resolver-visible client** | `10.50.30.20` |
| **Latest cluster** | `2026-08-26 06:37–06:41 UTC` |
| **DNS replies** | `418` |
| **Unique qnames** | `409` |
| **NXDOMAIN replies** | `408` |
| **NXDOMAIN ratio** | `97.61%` |
| **ML context** | Five corresponding `ANOMALY` windows |
| **SOC conclusion** | **INCONCLUSIVE — escalation warranted** |

> [!IMPORTANT]
> The DNS behavior was strongly abnormal, but defender telemetry did **not** prove the initiating process, malware, endpoint compromise, user identity, intent, or authorization.

## 🧭 Investigation Workflow

```mermaid
flowchart LR

    %% =====================================================
    %% PHASE 1 — EVIDENCE COLLECTION
    %% =====================================================
    subgraph EVIDENCE[" "]
        direction TB

        EH["📡 1 · Evidence Collection"]

        A["🚨 Detection<br/>v1.0"]
        B["📡 Raw Unbound<br/>DNS"]
        C["🧬 Qname<br/>Metrics"]

        EH --> A --> B --> C
    end


    %% =====================================================
    %% PHASE 2 — BEHAVIOR ANALYSIS
    %% =====================================================
    subgraph ANALYSIS[" "]
        direction TB

        AH["🔍 2 · Behavior Analysis"]

        D["📊 Same-Client<br/>Baseline"]
        E["🕒 Recurrence<br/>+ Scope"]
        F["🧠 ML<br/>Second Opinion"]

        AH --> D --> E --> F
    end


    %% =====================================================
    %% PHASE 3 — ANALYST DECISION
    %% =====================================================
    subgraph DECISION[" "]
        direction TB

        DH["🧭 3 · Analyst Decision"]

        G["🤖 AI Claim<br/>Validation"]
        H["🧭 5W1H<br/>Assessment"]
        I["📨 IR<br/>Handoff"]

        DH --> G --> H --> I
    end


    %% =====================================================
    %% CONNECT PHASES — GROUP TO GROUP
    %% Keeps each column layout intact
    %% =====================================================
    EVIDENCE --> ANALYSIS
    ANALYSIS --> DECISION


    %% =====================================================
    %% HEADER STYLING
    %% =====================================================
    classDef evidenceHeader fill:#083344,stroke:#22d3ee,stroke-width:2px,color:#ffffff;
    classDef analysisHeader fill:#312e81,stroke:#818cf8,stroke-width:2px,color:#ffffff;
    classDef decisionHeader fill:#052e16,stroke:#4ade80,stroke-width:2px,color:#ffffff;

    class EH evidenceHeader;
    class AH analysisHeader;
    class DH decisionHeader;


    %% =====================================================
    %% NODE STYLING
    %% =====================================================
    classDef detection fill:#450a0a,stroke:#f87171,stroke-width:2px,color:#ffffff;
    classDef telemetry fill:#083344,stroke:#22d3ee,stroke-width:2px,color:#ffffff;
    classDef metrics fill:#172554,stroke:#60a5fa,stroke-width:2px,color:#ffffff;

    classDef baseline fill:#134e4a,stroke:#2dd4bf,stroke-width:2px,color:#ffffff;
    classDef scope fill:#422006,stroke:#fbbf24,stroke-width:2px,color:#ffffff;
    classDef ml fill:#312e81,stroke:#818cf8,stroke-width:2px,color:#ffffff;

    classDef ai fill:#581c87,stroke:#e879f9,stroke-width:2px,color:#ffffff;
    classDef analyst fill:#3b0764,stroke:#c084fc,stroke-width:2px,color:#ffffff;
    classDef handoff fill:#052e16,stroke:#4ade80,stroke-width:3px,color:#ffffff;

    class A detection;
    class B telemetry;
    class C metrics;

    class D baseline;
    class E scope;
    class F ml;

    class G ai;
    class H analyst;
    class I handoff;


    %% =====================================================
    %% GROUP STYLING
    %% =====================================================
    style EVIDENCE fill:#0d1117,stroke:#22d3ee,stroke-width:1px
    style ANALYSIS fill:#0d1117,stroke:#818cf8,stroke-width:1px
    style DECISION fill:#0d1117,stroke:#4ade80,stroke-width:1px

    linkStyle default stroke:#94a3b8,stroke-width:2px
```

## 📚 Start Here

| Artifact | Purpose |
|---|---|
| [`SOC-ANALYST-INVESTIGATION.md`](SOC-ANALYST-INVESTIGATION.md) | Flagship readable investigation story |
| [`SOC-ANALYST-PLAYBOOK.md`](SOC-ANALYST-PLAYBOOK.md) | Detailed investigation workflow |
| [`SOC-TO-IR-HANDOFF.md`](SOC-TO-IR-HANDOFF.md) | Formal evidence handoff to Incident Response |
| [`5W1H.md`](5W1H.md) | Concise evidence-backed case framework |
| [`AI-ML-VALIDATION.md`](AI-ML-VALIDATION.md) | Human validation of ML and AI assistance |
| [`INVESTIGATION-TIMELINE.md`](INVESTIGATION-TIMELINE.md) | Defender-side timeline |
| [`SPL-QUERY-INDEX.md`](SPL-QUERY-INDEX.md) | Investigation query map |
| [`spl/README.md`](spl/README.md) | Exact SOC SPL sequence and workflow |
| [`evidence/README.md`](evidence/README.md) | Curated E01–E13 public evidence |

## 🧾 Evidence Highlights

<table>
<tr>
<td width="33%"><img src="evidence/S02-SOC-E01_Detection-v1-Hit.png" alt="Detection v1.0 hit"><br/><sub><b>E01 · Detection:</b> first live frozen-rule hit.</sub></td>
<td width="33%"><img src="evidence/S02-SOC-E03_Raw-Unbound-Replies.png" alt="Raw Unbound replies"><br/><sub><b>E03 · Raw DNS:</b> exact resolver evidence behind the alert.</sub></td>
<td width="33%"><img src="evidence/S02-SOC-E04_Qname-Pattern-Metrics.png" alt="Qname metrics"><br/><sub><b>E04 · Behavior:</b> qname uniqueness, label and NXDOMAIN measurements.</sub></td>
</tr>
<tr>
<td width="33%"><img src="evidence/S02-SOC-E08_ML-Anomaly-Assessment.png" alt="ML anomaly assessment"><br/><sub><b>E08 · ML:</b> Isolation Forest as a second opinion.</sub></td>
<td width="33%"><img src="evidence/S02-SOC-E10_AI-vs-Human-Validation.png" alt="AI versus human validation"><br/><sub><b>E10 · AI:</b> automation claims checked against human evidence.</sub></td>
<td width="33%"><img src="evidence/S02-SOC-E13_Final-Client-Scope.png" alt="Final client scope"><br/><sub><b>E13 · Scope:</b> final resolver-visible client boundary.</sub></td>
</tr>
</table>

## ⚖️ Analyst Boundary

The conclusion is intentionally narrower than “malware.” Sonia established an abnormal, repeated DGA-like/high-NXDOMAIN pattern and enough evidence to justify independent IR review without upgrading DNS behavior into unsupported endpoint attribution.

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%" alt="section divider" />

<div align="center">

**Alert is a lead. Raw telemetry is evidence. Human judgement owns the disposition.**

[🏠 Scenario Home](../README.md) · [📖 Flagship Investigation](SOC-ANALYST-INVESTIGATION.md) · [🔎 SOC SPL](spl/README.md) · [🛡️ IR Handoff](SOC-TO-IR-HANDOFF.md) · [⬆ Back to top](#top)

</div>

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=30,24,19,12,6&height=75&section=footer" width="100%" alt="DNSentinel Scenario 02 footer" />
