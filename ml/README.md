<a id="top"></a>
<img src="https://capsule-render.vercel.app/api?type=soft&color=gradient&customColorList=6,12,19,24,30&height=135&section=header&text=%F0%9F%A7%A0%20Machine%20Learning%20Engineering&fontSize=28&fontColor=ffffff&animation=fadeIn&desc=Scenario%2002%20%E2%80%94%20Isolation%20Forest%20v1&descSize=14&descAlignY=68&descColor=D966FF" width="100%" alt="🧠 Machine Learning Engineering" />

<div align="center">

![Scenario](https://img.shields.io/badge/Scenario_02-ML_Engineering_Complete-2EA44F?style=flat-square)
![Model](https://img.shields.io/badge/Model-Isolation_Forest_v1-F7931E?style=flat-square&logo=scikitlearn&logoColor=white)
![Owner](https://img.shields.io/badge/Implementation-Musfira_Zafar-D966FF?style=flat-square)

[🏠 Scenario Home](../README.md) · [📖 ML Engineering Story](ML-ENGINEERING.md) · [🧾 Validation Record](../evidence/ml-engineering-validation.md) · [🏗️ Shared Infrastructure](https://github.com/DNSentinel-Lab/DNS-Lab-Infrastructure)

</div>

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%" alt="section divider" />

**Status:** ✅ Machine Learning Engineering complete  
**Implementation owner:** [Musfira Zafar](https://github.com/MUSFIRA-ZAFAR) — Scenario 02 Project Lead / Adversary Operator + ML implementation  
**Scenario boundary:** ML Engineering, Detection Engineering, Dashboard Studio, alerting, AI integration, the information-separated SOC/IR exercise, RPZ containment, verification, and safe reset are now complete. ML remains documented as a supporting second opinion rather than the incident verdict.

Scenario 02 now has a working anomaly-detection layer built from real defender DNS telemetry. The implementation teaches an Isolation Forest model the shape of controlled normal DNS behavior, scores controlled DGA-style windows, and returns the model result to Splunk as a separate analyst signal.

> [!IMPORTANT]
> ML is **not** the final Scenario 02 detection and it is **not** an automatic incident verdict. The completed Detection Engineering phase now compares explainable SPL behavior with this independent ML signal; the official human analyst still makes the security decision.

## 🎯 What was built

```text
dns-soc-victim01
        |
        | DNS
        v
dns-soc-resolver01 / Unbound
        |
        | resolver telemetry
        v
Splunk / index=dns_soc_dns
        |
        | private REST :8089
        v
dns-soc-ml
        |
        | 1-minute DNS behavior features
        v
Isolation Forest v1
        |
        | prediction + decision score
        v
private HEC :8088
        |
        v
Splunk / index=dns_soc_ml
```

The ML component runs as `dns-soc-ml` on the existing Splunk EC2/Docker platform. No new EC2, public ML API or host-published ML port was required.

## 🎯 Result at a glance

| Item | Observed implementation |
|---|---|
| Model | `IsolationForest` |
| Model name in result events | `dns_iforest_v1` |
| Analysis window | 1 minute / client |
| Controlled benign feature windows | 32 |
| Training windows | 24 |
| Held-out benign windows | 8 |
| Training anomalies | 3 |
| Held-out benign anomalies | 2 |
| Controlled DGA feature windows | 6 |
| DGA windows classified anomalous | **6 / 6** |
| ML result index | `dns_soc_ml` |
| ML sourcetype | `dns_soc:ml:iforest` |
| Model runtime artifact | `/app/dns_iforest_v1.joblib` — generated, not committed |

This small controlled result proves the end-to-end engineering path. It does **not** claim production accuracy or that every anomaly is malicious.

## 🧠 Actual v1 feature set

The implemented model uses nine directly explainable DNS behavior features:

```text
query_count
unique_qnames
nxdomain_count
nxdomain_ratio
avg_qname_length
max_qname_length
unique_tlds
a_count
aaaa_count
```

`unique_tlds` is the implementation's count of the final DNS label extracted by the SPL. The repository preserves the real implementation rather than replacing it with a different planned feature definition.

Earlier planning considered entropy, digit-ratio and interarrival features. Those were **not** part of the final v1 model and are not presented as implemented.

## 🧠 Training design

The model was trained only on controlled benign DNS periods.

```text
Benign run 1
2026-08-24 07:46:46 UTC -> 08:01:49 UTC

Benign run 2
2026-08-24 08:16:22 UTC -> 08:31:28 UTC

32 total 1-minute windows
        |
        +--> first 24 -> model training
        |
        +--> last 8  -> held-out benign check
```

The implementation then generated a separate controlled DGA period:

```text
2026-08-24 08:54:28 UTC -> 08:59:28 UTC
```

Those six DGA windows were used for evaluation, not for teaching the model what normal looks like.

## 🧠 Actual model parameters

```python
IsolationForest(
    n_estimators=200,
    contamination=0.10,
    random_state=42,
)
```

The stored artifact contains the fitted model, the fixed feature order and the train/holdout row counts.

## 🔐 Security boundary

Read and write access are intentionally separate:

```text
ML READ
restricted Splunk identity / token
        -> private REST :8089
        -> dns_soc_dns

ML WRITE
separate HEC token
        -> private HEC :8088
        -> dns_soc_ml
```

The real token values are not stored in this repository. The helper scripts expect them from environment variables:

```text
SPLUNK_ML_TOKEN
SPLUNK_ML_HEC_TOKEN
```

The current v1 scripts use HTTPS with `verify=False` only on the private `dns-soc-internal` path because the lab Splunk service presents a self-signed internal certificate. This is preserved as an implementation fact and a hardening item; production-style deployment should trust the Splunk certificate/CA and restore certificate verification.

## 🗂️ Repository map

| Area | Purpose |
|---|---|
| [`ML-ENGINEERING.md`](ML-ENGINEERING.md) | Flagship technical story: data → features → model → evaluation → Splunk |
| [`model/`](model/) | Training, scoring and HEC write-back Python |
| [`generators/`](generators/) | Controlled benign and DGA DNS generators |
| [`docker/`](docker/) | ML Dockerfile, pinned dependencies and Compose service snippet |
| [`scripts/`](scripts/) | Small execution helpers that pass tokens through environment variables |
| [`spl/`](spl/) | ML-specific REST, data inventory, feature engineering and result validation searches |
| [`artifacts/README.md`](artifacts/README.md) | Runtime model-artifact policy and reproduction note |
| [`../evidence/ml-engineering-validation.md`](../evidence/ml-engineering-validation.md) | Compact acceptance/evaluation record |
| [`../screenshots/ml/`](../screenshots/ml/) | Curated success, setup and troubleshooting evidence |

## 🧠 Why the ML SPL is kept here

The searches under `ml/spl/` support the ML engineering workflow: data inventory, feature construction, DGA evaluation and ML-result validation.

The root [`../spl/`](../spl/) directory now contains the completed Scenario 02 Detection Engineering lifecycle:

```text
baseline.spl
hunting.spl
detection.spl
validation.spl
```

Keeping those areas separate prevents ML feature-building SPL from being mistaken for the final security detection.

## 🧠 What this model means to the SOC

The model answers one narrow question:

> **Does this client's one-minute DNS behavior look different from the normal behavior used to train the model?**

It does **not** answer:

> Is this host definitely infected?

The official analyst will compare:

```text
raw resolver evidence
        +
rule-based DGA detection
        +
ML prediction / score
        |
        v
human SOC judgement
```

## 🧠 Score interpretation

The field named `anomaly_score` currently preserves scikit-learn's `decision_function()` output from the implemented code.

For the controlled DGA windows, anomalous values were negative. Therefore the current field must **not** be documented as “higher = more suspicious.” The completed Detection Engineering/dashboard work preserved the raw score semantics instead of silently normalizing it.

## 📌 What the small evaluation showed

Held-out benign data was not perfect:

```text
8 held-out benign windows
2 flagged anomalous
6 treated as normal
```

Controlled DGA data showed clear separation in this lab run:

```text
6 controlled DGA windows
6 flagged anomalous
0 missed
```

That is exactly why the model remains a second opinion. Anomaly means **unusual**, not automatically malicious.

## 🧠 What this ML phase did not complete by itself

ML Engineering stopped at the anomaly-signal boundary. It did not own the explainable detection, the SOC disposition, the response decision, or containment. Those later phases are now complete and are documented in their dedicated workspaces.

During the official information-separated exercise, the frozen Detection v1.0 rule produced five consecutive live windows and the ML service produced five corresponding `ANOMALY` windows. Sonia used those ML results only as supporting context beside raw DNS evidence, and Abdul-Rehman made the later response decision independently.

This closes the operational loop without changing the original ML responsibility boundary.

**DNSentinel Scenario 02 · Machine Learning Engineering**

## ✅ Live scoring closeout

Before the official exercise, the existing Isolation Forest model was operationalized for fresh DNS windows without retraining it. The final runtime uses a root-only token file, a previous-completed-minute scorer, HEC write-back to `dns_soc_ml`, and a systemd timer at `:45` seconds after each minute.

The implementation and safe placeholder configuration are preserved in [`operations/`](operations/).

During the official latest cluster, all five corresponding ML windows were available to Sonia as `ANOMALY` second-opinion evidence. The model did not determine Sonia's disposition or Abdul-Rehman's response decision.
<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%" alt="section divider" />

<div align="center">

**DNSentinel Scenario 02 · Evidence before verdict · Humans before automation**

[🏠 Scenario Home](../README.md) · [⬆ Back to top](#top)

</div>

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=30,24,19,12,6&height=75&section=footer" width="100%" alt="DNSentinel Scenario 02 footer" />
