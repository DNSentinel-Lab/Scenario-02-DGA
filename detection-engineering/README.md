<a id="top"></a>

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,12,19,24,30&height=190&section=header&text=Scenario%2002%20Detection%20Engineering&fontSize=34&fontColor=ffffff&animation=fadeIn&fontAlignY=38&desc=DGA%20%2B%20High%20NXDOMAIN%20%7C%20Lubaba%20%7C%20Detection%20v1.0&descSize=15&descAlignY=60&descColor=D966FF" width="100%" alt="Scenario 02 Detection Engineering" />

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=700&size=18&duration=2600&pause=850&color=D966FF&center=true&vCenter=true&repeat=true&width=1000&height=58&lines=Telemetry+%E2%86%92+Baseline+%E2%86%92+Dashboard+%E2%86%92+Hunt+%E2%86%92+Detect;Validate+%E2%86%92+Rule%E2%86%94ML+%E2%86%92+Scheduled+Alert+%E2%86%92+AI+Assist;Build+what+the+analyst+can+verify+from+evidence" alt="Detection Engineering lifecycle" />

![Scenario](https://img.shields.io/badge/Scenario_02-Detection_Engineering_Complete-2EA44F?style=flat-square)
![Workspace](https://img.shields.io/badge/Workspace-Detection_Engineering-AD1457?style=flat-square)
![Detection](https://img.shields.io/badge/Detection-v1.0-D966FF?style=flat-square)
![Validation](https://img.shields.io/badge/Validation-PASS-2EA44F?style=flat-square)
![AI](https://img.shields.io/badge/AI-dga__nxdomain__v1-7B2CBF?style=flat-square)

[🏠 Scenario Home](../README.md) · [📊 Dashboard](../dashboard/README.md) · [🔎 SPL Workspace](../spl/README.md) · [🤖 AI Mapping](../ai/README.md) · [🖼️ Evidence](../screenshots/README.md)

</div>

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%" alt="section divider" />

**Detection Engineer / AI Integrator:** [Lubaba](https://github.com/lubaba1513-pixel)  
**Status:** **✅ Detection Engineering complete**  
**Primary MITRE ATT&CK:** `T1568.002 — Dynamic Resolution: Domain Generation Algorithms`  
**Production rule:** `Scenario 02 - Possible DGA / High NXDOMAIN` · `v1.0`

Lubaba owned the Scenario 02 Detection Engineering lifecycle from trusted Unbound resolver telemetry to SOC-ready alerting. She validated the DNS transaction model, measured ingestion behavior, established the rule baseline, engineered the analyst dashboard, built the hunting and production SPL, challenged the rule with controlled DGA and benign traffic, compared the explainable rule with the existing Isolation Forest model, operationalized Detection v1.0 as a scheduled alert, and integrated the final evidence contract with the shared AI bridge.

> [!IMPORTANT]
> Detection Engineering validation traffic is **not** the official Scenario 02 adversary exercise. The synchronized adversary → SOC → IR exercise remains the next phase, and the frozen v1.0 rule is not tuned during that future live run.

## 🚦 Start here

| Artifact | What it contains |
|---|---|
| [`DETECTION-ENGINEERING.md`](DETECTION-ENGINEERING.md) | **Flagship engineering story** — question → observation → decision → action → validation → lesson, from resolver semantics to AI-vs-raw evidence validation. |
| [`detection-engineering-validation.md`](detection-engineering-validation.md) | **Acceptance record** — compact engineering gates used to declare Scenario 02 Detection Engineering ready. |
| [`../spl/README.md`](../spl/README.md) | Canonical baseline, hunting, production detection, validation and scheduled-alert artifacts. |
| [`../dashboard/README.md`](../dashboard/README.md) | Final Splunk Dashboard Studio investigation surface. |
| [`../ai/scenario-02-ai-mapping.md`](../ai/scenario-02-ai-mapping.md) | `dga_nxdomain_v1` evidence contract and shared-AI validation. |

## 🔁 Engineering path

```mermaid
flowchart TB

    subgraph ROW1[" "]
        direction LR
        A["📡 Unbound<br/>Telemetry"]
        B["🔎 Reply-Side<br/>Semantics"]
        C["⏱️ Ingestion<br/>Timing"]
        D["📊 Clean<br/>Baseline"]
        E["🖥️ Dashboard<br/>+ Hunts"]
        F["🛡️ Detection<br/>v1.0"]

        A --> B --> C --> D --> E --> F
    end

    subgraph ROW2[" "]
        direction RL
        G["✅ Positive + Benign<br/>Validation"]
        H["🧠 Rule ↔ ML<br/>Comparison"]
        I["🚨 Scheduled<br/>Alert"]
        J["📦 Raw Evidence<br/>+ Contract"]
        K["🤖 Shared AI<br/>Bridge"]
        L["🎯 SOC-Ready"]

        G --> H --> I --> J --> K --> L
    end

    F --> G

    style ROW1 fill:none,stroke:none
    style ROW2 fill:none,stroke:none

    classDef engineering fill:#161b22,stroke:#58a6ff,stroke-width:1.5px,color:#f0f6fc,font-size:16px;
    classDef validation fill:#161b22,stroke:#a371f7,stroke-width:1.5px,color:#f0f6fc,font-size:16px;
    classDef final fill:#161b22,stroke:#3fb950,stroke-width:2px,color:#f0f6fc,font-size:16px;

    class A,B,C,D,E,F engineering;
    class G,H,I,J,K validation;
    class L final;
```

The finish line was not simply **"the SPL returned a result."** The rule had to survive both sides of validation, run automatically, preserve a raw-event path, correlate cleanly with ML, and send structured evidence to the existing AI bridge without giving Detection, ML or AI containment authority.

## 🎯 Final detection boundary

```text
1-minute window / client_ip
event_type="reply"

query_count >= 20
AND unique_qnames >= 15
AND nxdomain_ratio >= 0.75
```

<details>
<summary><strong>Why these conditions?</strong></summary>
<br/>

The known-clean 32-window baseline reached maximums of **14 queries**, **10 unique qnames** and **0.50 NXDOMAIN ratio**. A fresh controlled DGA run crossed the candidate rule in all six observed one-minute windows, while ordinary DNS, limited benign NXDOMAIN traffic and a high-volume/high-unique legitimate-name burst stayed below the full combined boundary. The provisional values therefore became Detection v1.0 without threshold chasing.

</details>

## ✅ What was validated

| Engineering gate | Result |
|---|---|
| Unbound field model + reply-side transaction semantics | ✅ Complete |
| DNS ingestion timing | ✅ Complete |
| Clean 32-window rule baseline | ✅ Complete |
| Dashboard Studio investigation surface | ✅ Complete |
| Threshold-free behavior hunt + raw pivot | ✅ Complete |
| Fresh controlled DGA positive validation | ✅ 6/6 windows crossed candidate |
| Benign / false-positive challenges | ✅ PASS |
| Detection `v1.0` | ✅ Frozen |
| Reusable `validation.spl` | ✅ Complete |
| Rule ↔ ML historical comparison | ✅ 6/6 agreement on controlled DGA windows |
| Scheduled alert + real trigger | ✅ Validated |
| Analyst evidence row + raw drilldown | ✅ Validated |
| `dga_nxdomain_v1` AI evidence mapping | ✅ Validated |
| Webhook → OpenAI → HEC → `dns_soc_ai` | ✅ Validated |
| AI numerical claims vs raw DNS | ✅ Exact core-metric match |

## 📊 Analyst-facing result

![Scenario 02 DGA Investigation Dashboard](../screenshots/detection-engineering/04-dga-investigation-dashboard.png)

*The Dashboard Studio view brings NXDOMAIN behavior, unique-name activity, qname-length context, raw resolver evidence and ML supporting context into one investigation surface.*

## 🧩 Connected workspaces

```text
Detection Engineering
├── ../spl/          → baseline, hunts, v1.0 detection, validation, scheduled alert
├── ../dashboard/    → final analyst investigation surface
├── ../ai/           → Scenario 02 alert/AI evidence mapping
├── ../evidence/     → engineering acceptance + validation output
└── ../screenshots/  → curated successful and troubleshooting evidence
```

<details>
<summary><strong>🧰 Troubleshooting that shaped the engineering</strong></summary>
<br/>

Only reusable lessons are preserved publicly:

1. **Caching changed what the sensor saw.** A repeated benign burst looked large at the generator but resolver telemetry was smaller, so a unique legitimate-name burst was used to challenge the rule at the sensor.
2. **ML correlation needed semantic window time.** The first comparison returned no ML rows because Splunk `_time` did not represent the scored DNS minute; the final correlation used the ML `window_time` field.
3. **Webhook reachability did not equal schema compatibility.** The first AI trigger reached the bridge but returned HTTP 400; the fix was to add the common alert/evidence contract to the final detection result without changing Detection v1.0 or the Flask bridge.

See [`../screenshots/detection-engineering/troubleshooting/`](../screenshots/detection-engineering/troubleshooting/).

</details>

## ⏭️ What comes next

Detection Engineering is complete. The next stage is the **official information-separated Scenario 02 exercise**:

```text
Musfira — fresh adversary ground truth
        ↓
frozen Detection v1.0 + scheduled alert
        ↓
shared AI assistance
        ↓
Sonia — independent SOC investigation
        ↓
Abdul-Rehman — independent IR decision
        ↓
human-approved RPZ / sinkhole response if warranted
        ↓
before/after verification + ground-truth comparison
```

No official SOC disposition, IR decision or containment result is claimed in this workspace.

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%" alt="section divider" />

<div align="center">

**DNSentinel Scenario 02 · Evidence before verdict · Humans before automation**

[🏠 Scenario Home](../README.md) · [📖 Full Engineering Story](DETECTION-ENGINEERING.md) · [⬆ Back to top](#top)

</div>
