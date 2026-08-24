# ML Runtime Artifacts

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

## Why the binary is not in GitHub

`joblib` is a Python serialization format. Loading an untrusted serialized object can be unsafe, and the file is also tied to the exact Python/scikit-learn runtime that created it.

This repository therefore preserves the reproducible source instead:

```text
../model/train_iforest.py
../docker/requirements.txt
../spl/09_ml_feature_engineering_benign.spl
```

The model can be recreated from the same trusted lab data by following [`../ML-ENGINEERING.md`](../ML-ENGINEERING.md).

## Observed v1 model record

```text
model result name: dns_iforest_v1
training windows:  24
held-out windows:  8
features:          9
runtime path:      /app/dns_iforest_v1.joblib
```

Do not commit locally regenerated `*.joblib`, `*.pkl`, tokens or secret environment files.
