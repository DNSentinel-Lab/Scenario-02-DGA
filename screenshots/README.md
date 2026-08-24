<a id="top"></a>
<img src="https://capsule-render.vercel.app/api?type=soft&color=gradient&customColorList=6,12,19,24,30&height=135&section=header&text=%F0%9F%96%BC%EF%B8%8F%20Screenshot%20Evidence&fontSize=28&fontColor=ffffff&animation=fadeIn&desc=Scenario%2002%20%E2%80%94%20DGA%20%2B%20High%20NXDOMAIN&descSize=14&descAlignY=68&descColor=D966FF" width="100%" alt="🖼️ Screenshot Evidence" />

<div align="center">

![Scenario](https://img.shields.io/badge/Scenario_02-ML_Engineering_Complete-2EA44F?style=flat-square)
![Workspace](https://img.shields.io/badge/Workspace-Screenshot_Evidence-6F42C1?style=flat-square)

[🏠 Scenario Home](../README.md) · [🧠 ML Engineering](../ml/README.md) · [🏗️ Shared Infrastructure](https://github.com/DNSentinel-Lab/DNS-Lab-Infrastructure)

</div>

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%" alt="section divider" />

**Status:** ✅ Scenario 02 ML Engineering screenshots curated. Official Detection Engineering / SOC / IR screenshot sets remain pending.

The repository keeps detailed evidence available while the flagship ML story displays only the images that move the engineering explanation forward.

## Machine Learning

Folder: [`ml/`](ml/)

### Core success evidence

Folder: [`ml/core/`](ml/core/)

The 16-image core set proves the clean ML chain:

```text
private Splunk paths
→ victim DNS preflight
→ restricted ML read scope
→ HEC result path
→ controlled benign ground truth
→ feature engineering
→ Python dependency validation
→ Isolation Forest training
→ controlled DGA ground truth
→ DGA feature shift
→ 6/6 scoring
→ HEC write-back
→ final Splunk result
```

### Supporting setup evidence

Folder: [`ml/setup/`](ml/setup/)

Contains only the supporting technical screens useful for explaining:

- Compose validation / pre-ML backup;
- KV Store recovery confirmation;
- DNS field extractions;
- shared Splunk props required by the restricted REST consumer.

### Troubleshooting evidence

Folder: [`ml/troubleshooting/`](ml/troubleshooting/)

Only six reusable problem/fix screenshots were kept publicly:

| Evidence | Lesson |
|---|---|
| `T01` + `T02` | token creation failure was a shared KV Store dependency problem, not an ML-model bug |
| `T05` + `T09` | validate Compose syntax before touching the working stack |
| `T06` + `T07` | REST service accounts depend on Splunk knowledge-object visibility as well as index permissions |

Repeated failures, command-only screens and low-value debugging captures were intentionally excluded.

## Screenshot rule

One screenshot should prove one important fact, decision or reusable lesson.

For every important image:

1. explain what was being tested;
2. show the evidence;
3. add one short caption explaining what it proves.

Do not publish tokens, credentials, secret environment values or irrelevant account details.

The full source mapping is preserved in [`ml/screenshot-manifest.csv`](ml/screenshot-manifest.csv).

## Future Scenario 02 evidence

The official exercise should later use separate role/case folders rather than mixing new evidence into the ML set.

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%" alt="section divider" />

<div align="center">

**DNSentinel Scenario 02 · DGA + High NXDOMAIN**

[🏠 Scenario Home](../README.md) · [🧠 ML Engineering](../ml/README.md) · [⬆ Back to top](#top)

</div>

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,12,19,24,30&height=75&section=footer" width="100%" alt="footer" />
