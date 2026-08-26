<a id="top"></a>

<img src="https://capsule-render.vercel.app/api?type=soft&color=gradient&customColorList=6,12,19,24,30&height=140&section=header&text=%F0%9F%A7%A0%20ML%20Live%20Scoring%20Operations&fontSize=26&fontColor=ffffff&animation=fadeIn&fontAlignY=38&desc=Scenario%2002%20%E2%80%94%20Previous-Minute%20Scoring%20%E2%86%92%20Isolation%20Forest%20%E2%86%92%20HEC&descSize=14&descAlignY=68&descColor=2EA44F" width="100%" alt="🧠 ML Live Scoring Operations" />

<div align="center">

![Scenario](https://img.shields.io/badge/Scenario_02-ML_Engineering-2EA44F?style=flat-square) ![Workspace](https://img.shields.io/badge/Workspace-ML-A855F7?style=flat-square)

[🏠 Scenario Home](../../README.md) · [🧠 ML Workspace](../README.md) · [📖 ML Engineering](../ML-ENGINEERING.md)

</div>

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%" alt="section divider" />

# 🧠 ML Live Scoring Operations

The original validated `score_and_hec.py` was a historical/on-demand scorer with a fixed engineering time range. Before the official Scenario 02 run, the model itself was left unchanged and a small operational wrapper was added so fresh DNS windows could be scored automatically.

## 📌 Final operational path

```text
previous completed DNS minute
→ Splunk REST read
→ existing dns_iforest_v1.joblib
→ predict + decision_function
→ HEC
→ index=dns_soc_ml
```

The timer runs at `:45` seconds after each minute to allow normal resolver → Splunk ingestion time before scoring the previous complete minute.

## 🗂️ Files

- [`dns-soc-ml-live-score`](dns-soc-ml-live-score) — live previous-minute scorer wrapper
- [`dns-soc-ml-live-score.service`](dns-soc-ml-live-score.service) — oneshot systemd unit
- [`dns-soc-ml-live-score.timer`](dns-soc-ml-live-score.timer) — per-minute timer
- [`ml.env.example`](ml.env.example) — placeholder-only environment-file format

## 🔐 Security boundary

Real tokens were stored root-only on the host and are **not** committed here. The repository preserves only environment-variable names and placeholder values.

## 📌 Problems isolated during operationalization

The closeout/pre-flight work found and fixed four implementation boundaries without retraining the model:

1. **Persistent credentials** — ML REST/HEC tokens were moved into a root-only runtime environment file so the scorer no longer depended on manual token pasting.
2. **Systemd writable state path** — `ReadWritePaths=/var/lib/dns-soc-ml-live` required the directory to exist before namespace setup; the root-owned mode-700 state directory was created explicitly.
3. **Splunk `_time` format** — REST returned `_time` as a readable string. The live query now preserves a numeric `window_epoch` for the HEC event timestamp while retaining readable `window_time` inside the event.
4. **Variable-name typo** — the event dictionary was corrected from `vent` to `event` before final HEC validation.

The final benign validation produced fresh current-time `dns_soc_ml` records and `HEC_HTTP=200`.

## 🧠 Important model lesson

The benign validation windows were still marked `ANOMALY` by the Isolation Forest. That is not a transport failure; it reinforces the intended architecture:

```text
Detection v1.0 = primary explainable signal
ML             = supporting second opinion
AI             = analyst assistance
Human          = final judgement / response authority
```

No model tuning was performed to make the official exercise look cleaner.

## 💡 Operational note

The wrapper marks a completed minute after the scorer exits successfully. The timer delay was chosen to reduce the chance of scoring a minute before its resolver events are indexed.

---

[📘 ML Engineering](../ML-ENGINEERING.md) · [🏠 Scenario Home](../../README.md) · [⬆ Back to top](#top)
<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%" alt="section divider" />

<div align="center">

**DNSentinel Scenario 02 · Evidence before verdict · Humans before automation**

[🏠 Scenario Home](../../README.md) · [⬆ Back to top](#top)

</div>

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=30,24,19,12,6&height=75&section=footer" width="100%" alt="DNSentinel Scenario 02 footer" />
