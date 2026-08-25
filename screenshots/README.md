<a id="top"></a>
<img src="https://capsule-render.vercel.app/api?type=soft&color=gradient&customColorList=6,12,19,24,30&height=135&section=header&text=%F0%9F%96%BC%EF%B8%8F%20Screenshot%20Evidence&fontSize=28&fontColor=ffffff&animation=fadeIn&desc=Scenario%2002%20%E2%80%94%20DGA%20%2B%20High%20NXDOMAIN&descSize=14&descAlignY=68&descColor=D966FF" width="100%" alt="Screenshot Evidence" />

<div align="center">

![ML](https://img.shields.io/badge/ML_Screenshots-Curated-2EA44F?style=flat-square)
![Detection](https://img.shields.io/badge/Detection_Screenshots-Curated-2EA44F?style=flat-square)

[🏠 Scenario Home](../README.md) · [🧠 ML Engineering](../ml/README.md) · [🚦 Detection Engineering](../detection-engineering/README.md) · [🧾 Evidence](../evidence/README.md)

</div>

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%" alt="section divider" />

**Status:** ✅ ML Engineering screenshots curated · ✅ Detection Engineering screenshots curated · official adversary/SOC/IR screenshots pending.

The repository keeps evidence that proves an engineering fact, decision or reusable lesson. Repeated construction screens and low-value troubleshooting are intentionally excluded from the reader-facing story.

## Machine Learning

Folder: [`ml/`](ml/)

The existing ML set remains unchanged and documents Musfira's complete Isolation Forest implementation.

## Detection Engineering

Folder: [`detection-engineering/`](detection-engineering/)

### Core evidence chain

| Evidence | What it proves |
|---|---|
| `01-resolver-field-validation.png` | Live Unbound fields and resolver evidence are usable for Detection Engineering. |
| `02-dns-ingestion-latency.png` | Alert timing is based on measured Unbound → UF → Splunk delivery. |
| `03-rule-baseline-validation.png` | Normal one-minute/client behavior was measured before thresholds. |
| `04-dga-investigation-dashboard.png` | Final analyst investigation surface is complete. |
| `05-dga-hunting-behavior.png` | Threshold-free DGA behavior hunt works. |
| `06-controlled-positive-detection.png` | Fresh controlled DGA traffic crosses the candidate rule. |
| `06a-controlled-positive-test-traffic.png` | Ground-truth generation for the Detection Engineering positive test. |
| `07-benign-no-detection.png` | Benign challenge stays below the full rule. |
| `08-final-detection-v1-validation.png` | Detection v1.0 is frozen with final metadata/evidence. |
| `08a-validation-spl-detect-vs-below.png` | Reusable validation view shows both sides of the rule boundary. |
| `09-rule-vs-ml-comparison.png` | Frozen rule and Isolation Forest agree on six historical controlled DGA windows. |
| `10-scheduled-alert-triggered.png` | Detection v1.0 operates as a real scheduled Splunk alert. |
| `11-raw-event-drilldown.png` | Analyst can recover the raw resolver events behind the alert. |
| `12-ai-alert-evidence-contract.png` | Final alert row satisfies the human/AI evidence contract. |
| `13-ai-triage-indexed.png` | Shared AI bridge returns structured Scenario 02 triage to `dns_soc_ai`. |
| `14-detection-engineering-final-readiness.png` | AI core metrics match a separate raw DNS aggregation exactly. |

### Supporting evidence

Folder: [`detection-engineering/supporting/`](detection-engineering/supporting/)

Supporting screens preserve detail that is useful for technical review but does not need to appear in the flagship story: final contract columns, trigger history/result detail and expanded AI triage fields.

### Troubleshooting evidence

Folder: [`detection-engineering/troubleshooting/`](detection-engineering/troubleshooting/)

Only three reusable problem/fix stories are kept publicly:

| Evidence | Lesson |
|---|---|
| `t01-cache-limited-sensor-visibility.png` | Measure what the sensor actually observed; caching can change traffic-generator visibility. |
| `t02-ml-window-time-correlation.png` | Correlate derived analytics by semantic behavior time, not blindly by Splunk index time. |
| `t03-ai-webhook-contract-failure.png` | A reachable webhook can still fail schema validation; isolate transport from payload compatibility. |

The original Detection Engineering build screenshot manifest is preserved as [`detection-engineering/source-screenshot-manifest.csv`](detection-engineering/source-screenshot-manifest.csv) for traceability.

## Screenshot rule

For each important image:

1. explain what was being tested;
2. show the image;
3. state what the evidence proves.

Do not use screenshots as a substitute for reasoning. Do not publish credentials, tokens, secret environment values or irrelevant account details.

> [!IMPORTANT]
> Detection Engineering validation traffic is not the official Scenario 02 adversary execution. Official attacker/SOC/IR evidence will be stored separately when that exercise is performed.

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%" alt="section divider" />

<div align="center">

[🏠 Scenario Home](../README.md) · [📖 Detection Story](../detection-engineering/DETECTION-ENGINEERING.md) · [⬆ Back to top](#top)

</div>
