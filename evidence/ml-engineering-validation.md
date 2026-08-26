<a id="top"></a>

> 🧭 [Scenario 02](../README.md) › [Evidence](README.md) › **ML Engineering Validation Record — Scenario 02**

<div align="center">

![Scenario](https://img.shields.io/badge/Scenario_02-COMPLETE-2EA44F?style=flat-square) ![Workspace](https://img.shields.io/badge/Workspace-Evidence-22D3EE?style=flat-square) ![Document](https://img.shields.io/badge/Document-Evidence_Backed-D966FF?style=flat-square)

</div>

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%" alt="section divider" />

# 🧠 ML Engineering Validation Record — Scenario 02

**Implementation owner:** [Musfira Zafar](https://github.com/MUSFIRA-ZAFAR)  
**Model:** Isolation Forest v1  
**Engineering result:** **PASS**  
**Scenario result:** **ML engineering validated; the later official adversary / SOC / IR / response exercise is now complete**

This record summarizes the evidence used to declare the Scenario 02 Machine Learning Engineering phase complete.

## 🧾 Acceptance matrix

| Gate | Expected | Observed | Result |
|---|---|---|---|
| Resolver source | Real defender DNS evidence available | `dns_soc_dns` / `unbound:dns` searchable | ✅ PASS |
| Victim DNS path | Controlled traffic uses team resolver | `10.50.30.20 -> 10.50.30.10` validated | ✅ PASS |
| Private REST path | ML can read Splunk without public 8089 | internal REST reachable | ✅ PASS |
| Least-privilege read identity | ML reader limited to required DNS data | `dns_soc_ml_reader` scoped to `dns_soc_dns` | ✅ PASS |
| ML result index | Dedicated output dataset exists | `dns_soc_ml` | ✅ PASS |
| HEC write path | Separate ML HEC input works | validation event indexed | ✅ PASS |
| Controlled benign data | Known-normal periods captured | two UTC ground-truth runs | ✅ PASS |
| Feature engineering | One-minute client windows produced | 32 feature rows | ✅ PASS |
| Train/holdout split | Normal rows separated temporally | 24 training / 8 held-out | ✅ PASS |
| Model training | Isolation Forest fits and persists | `dns_iforest_v1.joblib` generated | ✅ PASS |
| Held-out benign check | Model limitation visible | 2 / 8 held-out benign windows anomalous | ✅ OBSERVED |
| Controlled DGA data | Safe DGA-style ground truth exists | five-minute owned-namespace run | ✅ PASS |
| DGA feature rows | DGA behavior reaches Splunk | 6 one-minute windows | ✅ PASS |
| DGA scoring | Controlled DGA appears abnormal | 6 / 6 classified `ANOMALY` | ✅ PASS |
| HEC write-back | Every scored window reaches Splunk | 6 / 6 HTTP 200; `events_sent=6` | ✅ PASS |
| Final Splunk result | Analyst can search ML output | 6 scored windows / 6 anomalies | ✅ PASS |
| Automatic response | ML must not contain/block | no automatic RPZ/sinkhole action | ✅ PASS |
| Secret handling | Tokens absent from repo | source uses environment variables; no token values committed | ✅ PASS |
| Internal TLS | Private Splunk HTTPS uses a self-signed certificate in v1 | working scripts use `verify=False`; production hardening should trust the Splunk CA/certificate | ⚠️ DOCUMENTED |

## 🕒 Ground-truth windows

### 🧠 Controlled benign run 1

```text
UTC:   2026-08-24 07:46:46 -> 08:01:49
epoch: 1787557606 -> 1787558509
```

### 🧠 Controlled benign run 2

```text
UTC:   2026-08-24 08:16:22 -> 08:31:28
epoch: 1787559382 -> 1787560288
```

### 🧠 Controlled DGA run

```text
UTC:   2026-08-24 08:54:28 -> 08:59:28
epoch: 1787561668 -> 1787561968
```

## 🧠 Implemented feature vector

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

The v1 feature record reflects the actual implementation. Earlier planned entropy/digit/interarrival features are not claimed as completed.

## 🧠 Final model configuration

```python
IsolationForest(
    n_estimators=200,
    contamination=0.10,
    random_state=42,
)
```

Observed training output:

```text
feature_rows=32
training_rows=24
holdout_rows=8
train_anomalies=3
holdout_anomalies=2
model_path=/app/dns_iforest_v1.joblib
```

## 📌 Controlled evaluation counts

| Ground truth | Total windows | Predicted anomaly | Predicted normal |
|---|---:|---:|---:|
| Held-out benign | 8 | 2 | 6 |
| Controlled DGA | 6 | 6 | 0 |

For this small controlled set only:

```text
TP = 6
FP = 2
FN = 0
TN = 6

precision = 0.75
recall    = 1.00
F1        ≈ 0.86
FPR       = 0.25
```

These are **lab evaluation metrics**, not production-performance claims.

## 🔎 Final Splunk identity

```text
index      = dns_soc_ml
host       = dns-soc-ml
source     = isolation-forest
sourcetype = dns_soc:ml:iforest
model      = dns_iforest_v1
scenario   = scenario_02_dga
```

Final observed summary:

```text
scored_windows = 6
anomalies      = 6
```

## 🧠 Score-semantics note

The current `anomaly_score` is the value produced by the implemented `decision_function()` call. Controlled anomalous windows had negative values.

Do not interpret the current field as a normalized “higher = more suspicious” score.

## ✅ Engineering completion decision

**Scenario 02 Machine Learning Engineering: COMPLETE.**

The completed ML phase proves:

```text
real DNS evidence
-> controlled benign baseline
-> one-minute feature engineering
-> Isolation Forest training
-> controlled DGA evaluation
-> ML scoring
-> HEC write-back
-> Splunk validation
```

It does **not** mark Scenario 02 Detection Engineering, dashboard/alert work, AI scenario integration, official SOC investigation, IR or containment complete.

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%" alt="section divider" />

<div align="center">

**DNSentinel Scenario 02 · Evidence before verdict · Humans before automation**

[🏠 Scenario Home](../README.md) · [🧾 Evidence](README.md) · [⬆ Back to top](#top)

</div>

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=30,24,19,12,6&height=75&section=footer" width="100%" alt="DNSentinel Scenario 02 footer" />
