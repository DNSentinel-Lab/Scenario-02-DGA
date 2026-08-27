<a id="top"></a>

<img src="https://capsule-render.vercel.app/api?type=soft&color=gradient&customColorList=6,12,19,24,30&height=145&section=header&text=%F0%9F%94%8E%20IR%20SPL%20Validation%20Map&fontSize=30&fontColor=ffffff&animation=fadeIn&fontAlignY=38&desc=Scenario%2002%20%E2%80%94%20Independent%20Reproduction%2C%20Scope%2C%20Recurrence%20and%20Before/After%20Proof&descSize=14&descAlignY=68&descColor=F59E0B" width="100%" alt="🔎 IR SPL Validation Map" />

<div align="center">

![Queries](https://img.shields.io/badge/IR_SPL-01%E2%80%9312-F59E0B?style=flat-square)
![Purpose](https://img.shields.io/badge/Purpose-Independent_Validation-2EA44F?style=flat-square)

[🏠 Scenario Home](../../README.md) · [🛡️ IR Workspace](../README.md) · [📖 Incident Response](../INCIDENT-RESPONSE.md) · [🧾 Evidence](../evidence/README.md)

</div>

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%" alt="section divider" />

# 🔎 IR SPL Validation Map

This folder preserves the exact Splunk searches used by IR to reproduce the SOC handoff independently and to preserve current-state / before-after evidence around containment.

## 🧭 Query Flow

```mermaid
flowchart LR
    A["01–04 · Validate Raw DNS"] --> B["05–07 · Scope / Visibility"]
    B --> C["08–09 · Recurrence / Current State"]
    C --> D["10–12 · Before / After Correlation"]
```

## 📋 Query Index

| Stage | Files | Purpose |
|---|---|---|
| 🔎 Independent validation | [`01_raw_dns_window_presence.spl`](01_raw_dns_window_presence.spl) → [`04_raw_qname_examples.spl`](04_raw_qname_examples.spl) | Reproduce raw events, core metrics, one-minute windows and qname structure |
| 🎯 Scope / attribution boundary | [`05_client_scope.spl`](05_client_scope.spl) → [`07_endpoint_telemetry_availability.spl`](07_endpoint_telemetry_availability.spl) | Confirm resolver-visible client scope and what endpoint telemetry was / was not available |
| 🕒 Recurrence / current state | [`08_historical_recurrence.spl`](08_historical_recurrence.spl), [`09_current_activity_check.spl`](09_current_activity_check.spl) | Establish recurrence and whether activity was still present |
| 🛡️ Before / after | [`10_before_after_exact_qname_attempt.spl`](10_before_after_exact_qname_attempt.spl) → [`12_namespace_broad_fallback.spl`](12_namespace_broad_fallback.spl) | Preserve containment-state comparison in Splunk |

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%" alt="section divider" />

<div align="center">

[🛡️ IR Workspace](../README.md) · [🧰 IR Shell](../shell/README.md) · [⬆ Back to top](#top)

</div>

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=30,24,19,12,6&height=75&section=footer" width="100%" alt="DNSentinel Scenario 02 footer" />
