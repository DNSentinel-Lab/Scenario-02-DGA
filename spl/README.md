<a id="top"></a>
<img src="https://capsule-render.vercel.app/api?type=soft&color=gradient&customColorList=6,12,19,24,30&height=135&section=header&text=%F0%9F%94%8E%20SPL%20Workspace&fontSize=28&fontColor=ffffff&animation=fadeIn&desc=Scenario%2002%20%E2%80%94%20DGA%20%2B%20High%20NXDOMAIN&descSize=14&descAlignY=68&descColor=D966FF" width="100%" alt="SPL Workspace" />

<div align="center">

![Scenario](https://img.shields.io/badge/Scenario_02-Detection_Engineering_Complete-2EA44F?style=flat-square)
![Detection](https://img.shields.io/badge/Detection-v1.0-D966FF?style=flat-square)
![MITRE](https://img.shields.io/badge/MITRE-T1568.002-E34F26?style=flat-square)

[🏠 Scenario Home](../README.md) · [🚦 Detection Engineering](../detection-engineering/README.md) · [📊 Dashboard](../dashboard/README.md) · [🤖 AI Mapping](../ai/README.md)

</div>

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%" alt="section divider" />

**Status:** ✅ Scenario 02 rule-based Detection Engineering SPL complete.

This workspace preserves the four canonical Detection Engineering stages required by the project standard. Supporting test searches are kept separately so the main path stays easy to review.

## 🗂️ Canonical lifecycle

```text
baseline.spl
    ↓
hunting.spl
    ↓
detection.spl
    ↓
validation.spl
```

| File | Purpose |
|---|---|
| [`baseline.spl`](baseline.spl) | Reproduce the known-clean 32-window baseline and median/p95/max metrics used to understand normal resolver behavior. |
| [`hunting.spl`](hunting.spl) | Threshold-free one-minute/client behavior summary plus raw resolver pivot. |
| [`detection.spl`](detection.spl) | Final production Detection v1.0, including the stable analyst/AI evidence contract. |
| [`validation.spl`](validation.spl) | Apply the same frozen v1.0 boundary while keeping both `WOULD DETECT` and `BELOW THRESHOLD` rows visible. |
| [`scheduled-alert.md`](scheduled-alert.md) | Final cadence, lookback, trigger actions, real trigger evidence and webhook result-contract note. |

## 🚨 Final Detection v1.0

```text
Primary source:  dns_soc_dns / Unbound reply events
Entity:          client_ip
Window:          1 minute

query_count >= 20
AND unique_qnames >= 15
AND nxdomain_ratio >= 0.75
```

The threshold is lab-derived, not copied from a generic DGA guide. See the full reasoning in [`../detection-engineering/DETECTION-ENGINEERING.md`](../detection-engineering/DETECTION-ENGINEERING.md).

## 🧾 Engineering validation searches

Folder: [`engineering-validation/`](engineering-validation/)

These are exact supporting searches used to challenge and verify the final rule. They are preserved for reproducibility but do not replace the canonical four SPL artifacts.

The read-only resolver field/timing/contamination/baseline work is preserved as [`resolver-validation-and-baseline-searches.spl`](engineering-validation/resolver-validation-and-baseline-searches.spl). It documents how the Detection Engineer established trusted inputs before hunting or threshold selection.

| Search | Engineering question |
|---|---|
| [`historical-candidate-validation.spl`](engineering-validation/historical-candidate-validation.spl) | Would the candidate separate the known historical DGA run from benign history? |
| [`fresh-positive-validation.spl`](engineering-validation/fresh-positive-validation.spl) | Does a new controlled DGA run cross the same candidate? |
| [`benign-ordinary-dns-validation.spl`](engineering-validation/benign-ordinary-dns-validation.spl) | Does ordinary DNS stay below? |
| [`benign-limited-nxdomain-validation.spl`](engineering-validation/benign-limited-nxdomain-validation.spl) | Does a small benign NXDOMAIN pattern stay below? |
| [`benign-cache-limited-burst-validation.spl`](engineering-validation/benign-cache-limited-burst-validation.spl) | What did the resolver actually observe during a repeated-name burst? |
| [`benign-unique-normal-burst-validation.spl`](engineering-validation/benign-unique-normal-burst-validation.spl) | Does high-volume/high-unique legitimate DNS still stay below without high NXDOMAIN? |
| [`rule-vs-ml-comparison.spl`](engineering-validation/rule-vs-ml-comparison.spl) | How does frozen rule output compare with the existing Isolation Forest on the same historical DGA windows? |
| [`scheduled-alert-raw-drilldown.spl`](engineering-validation/scheduled-alert-raw-drilldown.spl) | Can the analyst recover the raw resolver events behind a triggered minute? |
| [`ai-evidence-contract-test.spl`](engineering-validation/ai-evidence-contract-test.spl) | Does one detection row satisfy the shared webhook evidence contract? |
| [`ai-index-validation.spl`](engineering-validation/ai-index-validation.spl) | Did structured AI triage return to `dns_soc_ai`? |
| [`ai-vs-raw-final-validation.spl`](engineering-validation/ai-vs-raw-final-validation.spl) | Do the AI's core DNS numbers match raw resolver telemetry? |

## 🧠 Separation from ML SPL

[`../ml/spl/`](../ml/spl/) remains Musfira's ML Engineering workspace. Those searches were used for ML data inventory, feature engineering, training/evaluation support and ML result validation.

Root `spl/` belongs to Lubaba's explainable rule-based Detection Engineering lifecycle.

## 🚨 Detection boundary

- `NXDOMAIN` is central to this scenario but **not sufficient by itself**.
- `unique_qname_ratio` and qname length remain useful investigation context even though they are not mandatory v1.0 conditions.
- ML is supporting context, not a dependency of [`detection.spl`](detection.spl).
- No SPL here enables RPZ, sinkholes a domain or authorizes Incident Response.

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%" alt="section divider" />

<div align="center">

[🏠 Scenario Home](../README.md) · [🚦 Detection Story](../detection-engineering/DETECTION-ENGINEERING.md) · [⬆ Back to top](#top)

</div>

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=30,24,19,12,6&height=75&section=footer" width="100%" alt="DNSentinel Scenario 02 footer" />
