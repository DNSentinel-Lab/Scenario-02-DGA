<a id="top"></a>
<img src="https://capsule-render.vercel.app/api?type=soft&color=gradient&customColorList=6,12,19,24,30&height=135&section=header&text=%F0%9F%A4%96%20AI%20Integration%20%2F%20Profile&fontSize=28&fontColor=ffffff&animation=fadeIn&desc=Scenario%2002%20%E2%80%94%20DGA%20%2B%20High%20NXDOMAIN&descSize=14&descAlignY=68&descColor=D966FF" width="100%" alt="🤖 AI Integration / Profile" />

<div align="center">

![Scenario](https://img.shields.io/badge/Scenario_02-ML_Engineering_Complete-2EA44F?style=flat-square)
![Workspace](https://img.shields.io/badge/Workspace-AI_Integration_%2F_Profile-7B2CBF?style=flat-square)

[🏠 Scenario Home](../README.md) · [🏗️ Shared Infrastructure](https://github.com/DNSentinel-Lab/DNS-Lab-Infrastructure) · [🗂️ All Scenario Repositories](https://github.com/orgs/DNSentinel-Lab/repositories)

</div>

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%" alt="section divider" />

**Status:** Shared AI infrastructure ready; Scenario 02 ML Engineering complete; Scenario 02 AI profile not created.

The shared Flask/OpenAI bridge already exists in the Infrastructure repository. This folder will contain only the Scenario 02 profile/payload mapping after the final detection fields are stable.

## Future workflow

```text
Stable Scenario 02 alert
      ↓
Structured evidence payload
      ↓
Shared dns-soc-ai-bridge
      ↓
Structured analyst assistance
      ↓
index=dns_soc_ai
      ↓
Human validation against raw resolver evidence
```

Likely evidence includes client identity, first/last time, query/NXDOMAIN counts and ratio, representative qnames/qtypes/results, rule-based detection context, the already-implemented ML prediction/score where useful, and supporting sinkhole/network context.

## Rules

- AI is not the source of truth.
- AI does not authorize RPZ containment.
- ML and LLM are separate: Isolation Forest v1 now scores abnormal behavior in `dns_soc_ml`; the LLM will later explain/enrich stable alert evidence.
- Preserve the real input payload and response after implementation.
- Record where the summary is correct, incomplete or wrong.
- Do not create a fake Scenario 02 profile before alert fields exist.

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%" alt="section divider" />

<div align="center">

**DNSentinel Scenario 02 · DGA + High NXDOMAIN**

[🏠 Scenario Home](../README.md) · [🏗️ Infrastructure](https://github.com/DNSentinel-Lab/DNS-Lab-Infrastructure) · [⬆ Back to top](#top)

</div>

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,12,19,24,30&height=75&section=footer" width="100%" alt="footer" />
