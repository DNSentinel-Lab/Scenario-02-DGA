<a id="top"></a>
<img src="https://capsule-render.vercel.app/api?type=soft&color=gradient&customColorList=6,12,19,24,30&height=135&section=header&text=%F0%9F%A7%BE%20Evidence%20Workspace&fontSize=28&fontColor=ffffff&animation=fadeIn&desc=Scenario%2002%20%E2%80%94%20DGA%20%2B%20High%20NXDOMAIN&descSize=14&descAlignY=68&descColor=D966FF" width="100%" alt="🧾 Evidence Workspace" />

<div align="center">

![Scenario](https://img.shields.io/badge/Scenario_02-ML_Engineering_Complete-2EA44F?style=flat-square)
![Workspace](https://img.shields.io/badge/Workspace-Evidence_Workspace-2EA44F?style=flat-square)

[🏠 Scenario Home](../README.md) · [🧠 ML Engineering](../ml/README.md) · [🏗️ Shared Infrastructure](https://github.com/DNSentinel-Lab/DNS-Lab-Infrastructure)

</div>

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%" alt="section divider" />

**Status:** ✅ ML Engineering evidence complete; official Scenario 02 Detection Engineering / SOC / IR evidence pending.

Infrastructure evidence remains in the shared DNS Lab Infrastructure repository. This scenario repository now preserves the evidence that belongs specifically to Musfira's Machine Learning Engineering phase.

## ML Engineering validation

Primary record:

- [`ml-engineering-validation.md`](ml-engineering-validation.md) — compact acceptance matrix, ground-truth windows, model configuration and small controlled evaluation.

Full narrative:

- [`../ml/ML-ENGINEERING.md`](../ml/ML-ENGINEERING.md) — question → observation → decision → action → validation → lesson.

Curated screenshots:

- [`../screenshots/ml/`](../screenshots/ml/) — core success evidence, supporting setup evidence and selected troubleshooting lessons.

## Evidence already preserved

- real resolver path and private Splunk ML integration;
- least-privilege REST read path;
- dedicated HEC result path;
- exact controlled benign run timestamps;
- 32 one-minute feature windows;
- 24 training / 8 held-out benign rows;
- Isolation Forest v1 training output;
- exact controlled DGA run timestamps;
- six DGA feature windows;
- `6 / 6` DGA anomaly result;
- six successful HEC result writes;
- final `dns_soc_ml` Splunk summary;
- selected reusable troubleshooting evidence;
- complete Python / SPL / Docker source under [`../ml/`](../ml/).

## Still pending for the official Scenario 02 exercise

Do not confuse ML engineering ground truth with the later official case evidence. Future evidence will include:

- Detection Engineering baseline, hunting, positive/benign validation and final rule;
- official adversary ground truth after defender conclusions are locked;
- scheduled alert evidence;
- Scenario 02 AI result and human comparison;
- SOC analyst timeline/disposition;
- IR decision;
- approved RPZ containment;
- before/after sinkhole verification;
- final reset and ground-truth comparison.

Evidence should prove the scenario chain rather than preserve every intermediate command or troubleshooting message.

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%" alt="section divider" />

<div align="center">

**DNSentinel Scenario 02 · DGA + High NXDOMAIN**

[🏠 Scenario Home](../README.md) · [🧠 ML Engineering](../ml/README.md) · [⬆ Back to top](#top)

</div>

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,12,19,24,30&height=75&section=footer" width="100%" alt="footer" />
