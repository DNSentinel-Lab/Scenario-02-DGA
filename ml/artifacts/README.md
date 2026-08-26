<a id="top"></a>

<img src="https://capsule-render.vercel.app/api?type=soft&color=gradient&customColorList=6,12,19,24,30&height=140&section=header&text=%F0%9F%A7%A0%20ML%20Runtime%20Artifacts&fontSize=26&fontColor=ffffff&animation=fadeIn&fontAlignY=38&desc=Scenario%2002%20%E2%80%94%20Reproducible%20Model%20Artifact%20Boundary&descSize=14&descAlignY=68&descColor=2EA44F" width="100%" alt="🧠 ML Runtime Artifacts" />

<div align="center">

![Scenario](https://img.shields.io/badge/Scenario_02-ML_Engineering-2EA44F?style=flat-square) ![Workspace](https://img.shields.io/badge/Workspace-ML-A855F7?style=flat-square)

[🏠 Scenario Home](../../README.md) · [🧠 ML Workspace](../README.md) · [📖 ML Engineering](../ML-ENGINEERING.md)

</div>

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%" alt="section divider" />

# 🧠 ML Runtime Artifacts

**Status:** Runtime artifact generated successfully; binary model intentionally not committed.

The Scenario 02 trainer created this file inside the running ML container:

```text
/app/dns_iforest_v1.joblib
```

It contains:

- the fitted `IsolationForest` model;
- the fixed feature order;
- training-row count;
- held-out-row count.

## 💡 Why the binary is not in GitHub

`joblib` is a Python serialization format. Loading an untrusted serialized object can be unsafe, and the file is also tied to the exact Python/scikit-learn runtime that created it.

This repository therefore preserves the reproducible source instead:

```text
../model/train_iforest.py
../docker/requirements.txt
../spl/09_ml_feature_engineering_benign.spl
```

The model can be recreated from the same trusted lab data by following [`../ML-ENGINEERING.md`](../ML-ENGINEERING.md).

## 🧠 Observed v1 model record

```text
model result name: dns_iforest_v1
training windows:  24
held-out windows:  8
features:          9
runtime path:      /app/dns_iforest_v1.joblib
```

Do not commit locally regenerated `*.joblib`, `*.pkl`, tokens or secret environment files.
<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%" alt="section divider" />

<div align="center">

**DNSentinel Scenario 02 · Evidence before verdict · Humans before automation**

[🏠 Scenario Home](../../README.md) · [⬆ Back to top](#top)

</div>

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=30,24,19,12,6&height=75&section=footer" width="100%" alt="DNSentinel Scenario 02 footer" />
