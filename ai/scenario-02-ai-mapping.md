<a id="top"></a>

> 🧭 [Scenario 02](../README.md) › [AI Integration](README.md) › **Scenario 02 AI Evidence Mapping — `dga_nxdomain_v1`**

<div align="center">

![Scenario](https://img.shields.io/badge/Scenario_02-COMPLETE-2EA44F?style=flat-square) ![Workspace](https://img.shields.io/badge/Workspace-AI_Integration-7B2CBF?style=flat-square) ![Document](https://img.shields.io/badge/Document-Evidence_Backed-D966FF?style=flat-square)

</div>

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%" alt="section divider" />

# 🤖 Scenario 02 AI Evidence Mapping — `dga_nxdomain_v1`

**Detection Engineer / AI Integrator:** Lubaba  
**Status:** ✅ Validated end-to-end  
**Detection:** `Scenario 02 - Possible DGA / High NXDOMAIN` · `v1.0`  
**MITRE ATT&CK:** `T1568.002`

This document records the Scenario 02-specific evidence contract used with the existing shared AI bridge. It does **not** duplicate or redesign the shared Flask/OpenAI infrastructure.

## 🪪 Identity

```text
scenario_id   = scenario-02-dga
scenario_name = DGA + High NXDOMAIN
ai_profile    = dga_nxdomain_v1
```

## 🏗️ Architecture decision

No new Flask route, AI container, OpenAI integration, AI index, HEC path or public port was created.

Scenario 02 reuses the existing shared bridge:

```text
Splunk scheduled alert
        ↓
internal webhook
        ↓
dns-soc-ai-bridge
        ↓
OpenAI
        ↓
Splunk HEC
        ↓
index=dns_soc_ai
```

The deployed bridge is generic. `dga_nxdomain_v1` is carried inside `evidence_json`; it is not a separate runtime module.

## 📌 Common webhook contract

The bridge normalizes Splunk's first result row and requires:

```text
alert_id
alert_name
scenario
severity
event_time
evidence
```

For Splunk's native webhook envelope, `evidence` is parsed from the result field:

```text
evidence_json
```

Scenario 02 also sends:

```text
source = client_ip
```

## 🧾 Scenario 02 evidence inside `evidence_json`

```text
scenario_id
ai_profile
detection_name
detection_version
first_event
last_event
client_ip
query_count
unique_qnames
unique_qname_ratio
nxdomain_count
nxdomain_ratio
avg_qname_length
max_qname_length
qtypes
response_codes
qname_samples
mitre_technique
rationale
```

The final production search limits the AI copy of qname samples to the first **20** values while keeping the analyst-facing `qname_samples` field intact.

## 💡 Why the result contract changed

The first scheduled AI test reached the bridge but returned HTTP 400. Live schema inspection showed that the detection result did not yet expose the common webhook fields required by the generic bridge.

The fix was deliberately narrow:

```text
keep Detection v1.0 logic unchanged
        ↓
add common result-contract fields
        ↓
retest scheduled alert
```

No DGA threshold, ML model or AI infrastructure component was changed.

![Validated AI evidence contract](../screenshots/detection-engineering/12-ai-alert-evidence-contract.png)

## 🤖 Live AI output schema

Structured fields observed from the shared bridge include:

```text
summary
observed_indicators
network_context
suspicion_reasons
mitre_attack
cyber_kill_chain
missing_evidence
response_considerations
confidence
```

The bridge writes:

```text
index      = dns_soc_ai
sourcetype = dns_soc:ai:triage
source     = dns-soc-ai-bridge
```

and wraps the result with:

```text
human_validation_required = true
```

## 🧾 Final end-to-end validation

The corrected retest proved:

```text
DNS traffic
→ Detection v1.0
→ scheduled Splunk alert
→ webhook
→ dns-soc-ai-bridge
→ OpenAI
→ HEC
→ dns_soc_ai
```

![AI triage indexed](../screenshots/detection-engineering/13-ai-triage-indexed.png)

The returned event carried the expected Scenario 02 context, including:

- `scenario-02-dga`;
- `dga_nxdomain_v1`;
- medium severity;
- source/client `10.50.30.20`;
- MITRE `T1568.002`;
- Command and Control context;
- `human_validation_required=true`.

## 🤖 AI vs raw DNS evidence

The AI summarized:

```text
query_count        = 55
unique_qnames      = 54
unique_qname_ratio = 0.9818
nxdomain_count     = 53
nxdomain_ratio     = 0.9636
```

A separate raw resolver search for the same minute returned the exact same values.

![AI vs raw resolver evidence](../screenshots/detection-engineering/14-detection-engineering-final-readiness.png)

That is the final acceptance condition: the LLM may explain evidence, but its core factual claims must remain defensible from raw Splunk telemetry.

## 📌 Advisory boundaries

AI may:

- summarize observed behavior;
- explain why the pattern is suspicious;
- identify missing evidence;
- suggest investigation pivots;
- add MITRE / Kill Chain context;
- suggest response considerations.

AI must not:

- declare compromise as fact without evidence;
- authorize containment;
- enable RPZ;
- sinkhole domains;
- isolate hosts;
- replace Sonia's later independent SOC judgement;
- replace Abdul-Rehman's later independent IR decision.

## 🗂️ Related artifacts

- [Production detection](../spl/detection.spl)
- [Scheduled alert](../spl/scheduled-alert.md)
- [AI evidence-contract validation SPL](../spl/engineering-validation/ai-evidence-contract-test.spl)
- [AI index validation SPL](../spl/engineering-validation/ai-index-validation.spl)
- [AI-vs-raw validation SPL](../spl/engineering-validation/ai-vs-raw-final-validation.spl)
- [Detection Engineering story](../detection-engineering/DETECTION-ENGINEERING.md)
<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%" alt="section divider" />

<div align="center">

**DNSentinel Scenario 02 · Evidence before verdict · Humans before automation**

[🏠 Scenario Home](../README.md) · [🤖 AI Integration](README.md) · [⬆ Back to top](#top)

</div>

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=30,24,19,12,6&height=75&section=footer" width="100%" alt="DNSentinel Scenario 02 footer" />
