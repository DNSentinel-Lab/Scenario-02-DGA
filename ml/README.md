# ML Plan — Scenario 02 DNS Anomaly Detection

**Status:** Approved design — not implemented

Scenario 02 is the selected place to compare normal rule-based DNS detection with a lightweight anomaly detector after real baseline and controlled DGA data exist.

## Purpose

ML is an **additional detection signal**, not a replacement for Splunk detection and not an automatic incident verdict.

```text
Rule-based SPL
      +
Isolation Forest anomaly score
      |
      v
Compare what each catches, misses and falsely flags
```

## First model

**Isolation Forest** using:

- Python;
- pandas;
- numpy;
- scikit-learn.

Deep learning is not required for the planned first implementation.

## Training / analysis unit

Start with mostly normal DNS behavior and evaluate per-client windows such as **1 minute** and **5 minutes**.

Question:

> Does this client DNS window look very different from the normal baseline?

Controlled DGA traffic later gives known ground truth for evaluation.

## Candidate features

The approved plan includes:

```text
query_count
NXDOMAIN_count
NXDOMAIN_ratio
unique_qnames
average_label_length
maximum_label_length
average_entropy
maximum_entropy
digit_ratio
qtype_diversity
cache_hit_ratio
average_interarrival_time
```

These are candidate engineered features, not fields that already exist in Splunk. Each one must be derived and validated from the real resolver data before model training.

Current resolver fields that can support future feature engineering include:

```text
_time
client_ip
qname
qtype
rcode
response_time
cache_flag
response_size
```

The semantics of `cache_flag` must be validated before turning it into a `cache_hit_ratio` feature.

## Where it runs

No additional EC2 is planned.

Future logical layout:

```text
dns-soc-splunk01
    |
    +-- dns-soc-splunk       existing
    +-- dns-soc-ai-bridge    existing shared LLM bridge
    +-- dns-soc-ml           future lightweight Python/scikit-learn component
```

The exact Splunk-to-ML data transport and result-return mechanism were **not** finalized in the approved infrastructure plan. Leave them TBD until implementation rather than inventing an API/HEC design now.

## ML versus LLM

```text
Machine Learning
= detects or scores abnormal DNS behavior

LLM / shared AI bridge
= explains/enriches a stable alert for the human analyst
```

They remain separate components.

## Evaluation plan later

Compare at least:

- rule-based detection true positives;
- Isolation Forest anomaly scores on the same controlled windows;
- benign/false-positive windows;
- cases caught by both;
- cases caught by only one;
- cases where ML adds no useful value.

The project should document where ML helped and where a clear SPL rule was better.

## Implementation gate

Do not start ML until:

1. normal Scenario 02 DNS baseline exists;
2. controlled DGA/high-NXDOMAIN data exists;
3. real feature engineering is validated;
4. the rule-based baseline/detection path is understandable.

No model, training dataset, pickle/joblib artifact, container or ML result is stored in this repository yet.
