<a id="top"></a>
<img src="https://capsule-render.vercel.app/api?type=soft&color=gradient&customColorList=6,12,19,24,30&height=135&section=header&text=%F0%9F%A7%BE%20Evidence%20Workspace&fontSize=28&fontColor=ffffff&animation=fadeIn&desc=Scenario%2002%20%E2%80%94%20DGA%20%2B%20High%20NXDOMAIN&descSize=14&descAlignY=68&descColor=D966FF" width="100%" alt="Evidence Workspace" />

<div align="center">

![ML](https://img.shields.io/badge/ML_Evidence-Complete-2EA44F?style=flat-square)
![Detection](https://img.shields.io/badge/Detection_Evidence-Complete-2EA44F?style=flat-square)
![Official Exercise](https://img.shields.io/badge/Official_SOC%2FIR_Exercise-Pending-D966FF?style=flat-square)

[🏠 Scenario Home](../README.md) · [🧠 ML Engineering](../ml/README.md) · [🚦 Detection Engineering](../detection-engineering/README.md) · [🖼️ Screenshots](../screenshots/README.md)

</div>

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%" alt="section divider" />

**Status:** ML Engineering evidence ✅ complete · Detection Engineering evidence ✅ complete · official adversary/SOC/IR evidence ⏳ pending.

This workspace separates engineering evidence from the later official information-separated exercise.

## Machine Learning Engineering

- [`ml-engineering-validation.md`](ml-engineering-validation.md) — Musfira's ML acceptance record.
- [`../ml/ML-ENGINEERING.md`](../ml/ML-ENGINEERING.md) — full ML engineering story.
- [`../screenshots/ml/`](../screenshots/ml/) — curated ML screenshots.

## Detection Engineering

- [`../detection-engineering/detection-engineering-validation.md`](../detection-engineering/detection-engineering-validation.md) — Lubaba's Detection Engineering acceptance record.
- [`../detection-engineering/DETECTION-ENGINEERING.md`](../detection-engineering/DETECTION-ENGINEERING.md) — complete engineering story.
- [`detection-v1-validation-output.csv`](detection-v1-validation-output.csv) — preserved final Detection v1 output rows from controlled validation.
- [`../screenshots/detection-engineering/`](../screenshots/detection-engineering/) — curated Detection Engineering evidence.

## Engineering evidence now preserved

### ML

- controlled benign ground-truth windows;
- 32 ML feature windows;
- 24 training / 8 held-out benign rows;
- Isolation Forest v1 implementation;
- controlled DGA ground truth;
- 6/6 DGA anomaly result;
- HEC write-back to `dns_soc_ml`.

### Detection Engineering

- resolver field and reply-side semantic validation;
- measured Unbound → UF → Splunk ingestion timing;
- independent 32-window rule baseline;
- final Dashboard Studio artifact;
- threshold-free hunts;
- fresh positive DGA validation;
- multiple benign / false-positive challenges;
- Detection v1.0 freeze;
- reusable validation SPL;
- rule ↔ ML comparison;
- real scheduled alert trigger;
- analyst evidence contract;
- raw-event drilldown;
- `dga_nxdomain_v1` AI mapping;
- webhook → OpenAI → HEC result in `dns_soc_ai`;
- final AI-vs-raw DNS exact core-metric validation.

## Still pending for the official Scenario 02 exercise

The following must remain separate from engineering validation:

- fresh adversary ground truth from Musfira;
- official live alert outcome with Detection v1.0 frozen;
- Sonia's independent SOC investigation and disposition;
- AI-vs-human comparison;
- Abdul-Rehman's independent IR decision;
- human-approved RPZ/sinkhole containment where warranted;
- before/after response verification;
- safe reset;
- ground-truth reveal and final scenario comparison.

> [!IMPORTANT]
> A controlled engineering DGA run is not the official attacker run. Evidence is labelled by purpose so future reviewers cannot confuse validation traffic with the blind exercise.

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%" alt="section divider" />

<div align="center">

[🏠 Scenario Home](../README.md) · [🚦 Detection Validation](../detection-engineering/detection-engineering-validation.md) · [⬆ Back to top](#top)

</div>
