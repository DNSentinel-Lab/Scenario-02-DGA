<a id="top"></a>
<img src="https://capsule-render.vercel.app/api?type=soft&color=gradient&customColorList=6,12,19,24,30&height=135&section=header&text=%F0%9F%A4%96%20AI%20Integration%20%2F%20Profile&fontSize=28&fontColor=ffffff&animation=fadeIn&desc=Scenario%2002%20%E2%80%94%20DGA%20%2B%20High%20NXDOMAIN&descSize=14&descAlignY=68&descColor=D966FF" width="100%" alt="AI Integration / Profile" />

<div align="center">

![Scenario](https://img.shields.io/badge/Scenario_02-Detection_Engineering_Complete-2EA44F?style=flat-square)
![AI](https://img.shields.io/badge/Profile-dga__nxdomain__v1-7B2CBF?style=flat-square)
![Human](https://img.shields.io/badge/Human_Validation-Required-D966FF?style=flat-square)

[🏠 Scenario Home](../README.md) · [🚦 Detection Engineering](../detection-engineering/README.md) · [🔎 SPL](../spl/README.md) · [🏗️ Shared Infrastructure](https://github.com/DNSentinel-Lab/DNS-Lab-Infrastructure)

</div>

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%" alt="section divider" />

**Status:** ✅ Scenario 02 AI evidence mapping and end-to-end engineering validation complete.

The shared Flask/OpenAI bridge remains common Infrastructure. Scenario 02 adds only the evidence identity and mapping required by the frozen Detection v1.0 result.

## Scenario identity

```text
scenario_id   = scenario-02-dga
scenario_name = DGA + High NXDOMAIN
ai_profile    = dga_nxdomain_v1
```

Full mapping: [`scenario-02-ai-mapping.md`](scenario-02-ai-mapping.md)

## Reused shared architecture

```text
Scenario 02 scheduled alert
      ↓
internal Splunk webhook
      ↓
dns-soc-ai-bridge
      ↓
OpenAI
      ↓
internal HEC
      ↓
index=dns_soc_ai
      ↓
human validation against raw DNS
```

No new Flask route, AI container, AI index, HEC architecture or public port was created.

## Common alert contract

The final detection emits:

```text
alert_id
alert_name
scenario
severity
event_time
source
evidence_json
```

`evidence_json` carries Scenario 02-specific DNS evidence such as client identity, query/unique/NXDOMAIN metrics, qname length context, qtypes, representative names, MITRE and rationale.

## AI output

The live shared bridge returned structured fields including:

- summary;
- observed indicators;
- network context;
- suspicion reasons;
- MITRE ATT&CK context;
- Cyber Kill Chain context;
- missing evidence;
- response considerations;
- confidence;
- `human_validation_required=true`.

![Scenario 02 AI triage indexed](../screenshots/detection-engineering/13-ai-triage-indexed.png)

## Final evidence check

The final AI result summarized:

```text
55 DNS queries
54 unique qnames
unique_qname_ratio = 0.9818
53 NXDOMAIN
nxdomain_ratio = 0.9636
```

A separate raw `dns_soc_dns` search returned the same core values exactly.

![AI vs raw DNS validation](../screenshots/detection-engineering/14-detection-engineering-final-readiness.png)

This validation is the reason the AI path is documented as **evidence-grounded analyst assistance**, not simply “the API returned HTTP 200.”

## Authority boundary

- Isolation Forest = anomaly signal.
- Detection v1.0 = rule-based security lead.
- LLM = explanation / analyst assistance.
- Raw telemetry = evidence.
- Human SOC / IR = final judgement and response authority.

AI does **not** enable RPZ, sinkhole domains, isolate hosts or authorize Incident Response.

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%" alt="section divider" />

<div align="center">

[🏠 Scenario Home](../README.md) · [📖 AI Mapping](scenario-02-ai-mapping.md) · [⬆ Back to top](#top)

</div>
