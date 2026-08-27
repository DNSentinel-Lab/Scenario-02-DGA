<a id="top"></a>

<img src="https://capsule-render.vercel.app/api?type=soft&color=gradient&customColorList=6,12,19,24,30&height=145&section=header&text=%F0%9F%94%8E%20SOC%20SPL%20Investigation%20Map&fontSize=30&fontColor=ffffff&animation=fadeIn&fontAlignY=38&desc=Scenario%2002%20%E2%80%94%20Exact%20Queries%20Used%20from%20Preflight%20to%20Final%20Client%20Scope&descSize=14&descAlignY=68&descColor=22D3EE" width="100%" alt="🔎 SOC SPL Investigation Map" />

<div align="center">

![Queries](https://img.shields.io/badge/SOC_SPL-00%E2%80%9320-22D3EE?style=flat-square)
![Bundle](https://img.shields.io/badge/Bundle-ALL_SOC_ANALYST_QUERIES.spl-A855F7?style=flat-square)

[🏠 Scenario Home](../../README.md) · [🔎 SOC Workspace](../README.md) · [📖 Investigation](../SOC-ANALYST-INVESTIGATION.md) · [🧾 Evidence](../evidence/README.md)

</div>

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%" alt="section divider" />

# 🔎 SOC SPL Investigation Map

This folder preserves the exact searches Sonia used during the completed investigation. The files are ordered by investigation purpose rather than presented as a flat query dump.

## 🧭 Query Flow

```mermaid
flowchart LR
    A["00 · Telemetry Health"] --> B["01–02 · Detection Validation"]
    B --> C["03–05 · Raw DNS / Qname"]
    C --> D["06–10 · Baseline / Recurrence"]
    D --> E["11–13 · ML Review"]
    E --> F["14–17 · AI Validation"]
    F --> G["18–20 · Resolution / Final Scope"]
```

## 📋 Query Index

| Stage | Files | Purpose |
|---|---|---|
| 🩺 Telemetry health | [`00_preflight_live_dns_15m.spl`](00_preflight_live_dns_15m.spl) | Confirm current resolver visibility before case work |
| 🚨 Frozen detection | [`01_detection_v1_live.spl`](01_detection_v1_live.spl), [`02_detection_windows_clean.spl`](02_detection_windows_clean.spl) | Confirm the production detection and clean matching windows |
| 📡 Raw DNS | [`03_raw_unbound_broad_client.spl`](03_raw_unbound_broad_client.spl) → [`05_qname_pattern_metrics.spl`](05_qname_pattern_metrics.spl) | Recover resolver evidence and measure qname behavior |
| 📊 Baseline / recurrence | [`06_baseline_original_failed_test.spl`](06_baseline_original_failed_test.spl) → [`10_detection_activity_clusters.spl`](10_detection_activity_clusters.spl) | Compare the client to historical behavior and separate activity clusters |
| 🧠 ML | [`11_ml_raw_event_format.spl`](11_ml_raw_event_format.spl) → [`13_ml_clean_final.spl`](13_ml_clean_final.spl) | Inspect and clean Isolation Forest result context |
| 🤖 AI | [`14_ai_raw_event_format.spl`](14_ai_raw_event_format.spl) → [`17_ai_vs_human_validation.spl`](17_ai_vs_human_validation.spl) | Inspect AI output and validate claims against evidence |
| 🎯 Resolution / scope | [`18_non_nxdomain_replies.spl`](18_non_nxdomain_replies.spl) → [`20_final_client_scope.spl`](20_final_client_scope.spl) | Review successful DNS and lock final resolver-visible scope |
| 📦 Complete bundle | [`ALL_SOC_ANALYST_QUERIES.spl`](ALL_SOC_ANALYST_QUERIES.spl) | Combined query set for reproducibility |

> [!NOTE]
> [`06_baseline_original_failed_test.spl`](06_baseline_original_failed_test.spl) is intentionally retained as troubleshooting history; the corrected baseline path follows it.

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%" alt="section divider" />

<div align="center">

[🔎 SOC Workspace](../README.md) · [📄 SPL Query Index](../SPL-QUERY-INDEX.md) · [⬆ Back to top](#top)

</div>

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=30,24,19,12,6&height=75&section=footer" width="100%" alt="DNSentinel Scenario 02 footer" />
