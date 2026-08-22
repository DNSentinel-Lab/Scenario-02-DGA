# AI Profile — Scenario 02 DGA + High NXDOMAIN Activity

**Status:** Shared AI infrastructure ready; Scenario 02 profile not created.

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

Likely evidence includes client identity, first/last time, query/NXDOMAIN counts and ratio, representative qnames/qtypes/results, label metrics, optional ML score if later implemented, and supporting sinkhole/network context.

## Rules

- AI is not the source of truth.
- AI does not authorize RPZ containment.
- ML and LLM are separate: ML may score abnormal behavior; LLM explains/enriches stable evidence.
- Preserve the real input payload and response after implementation.
- Record where the summary is correct, incomplete or wrong.
- Do not create a fake Scenario 02 profile before alert fields exist.
