<a id="top"></a>
<img src="https://capsule-render.vercel.app/api?type=soft&color=gradient&customColorList=6,12,19,24,30&height=135&section=header&text=%F0%9F%93%8A%20Dashboard%20Studio&fontSize=28&fontColor=ffffff&animation=fadeIn&desc=Scenario%2002%20%E2%80%94%20DGA%20%2B%20High%20NXDOMAIN&descSize=14&descAlignY=68&descColor=D966FF" width="100%" alt="Dashboard Studio" />

<div align="center">

![Scenario](https://img.shields.io/badge/Scenario_02-Detection_Engineering_Complete-2EA44F?style=flat-square)
![Dashboard](https://img.shields.io/badge/Splunk-Dashboard_Studio-000000?style=flat-square&logo=splunk&logoColor=white)
![Artifact](https://img.shields.io/badge/Artifact-Validated_JSON-D966FF?style=flat-square)

[🏠 Scenario Home](../README.md) · [🚦 Detection Engineering](../detection-engineering/README.md) · [🔎 SPL](../spl/README.md) · [🖼️ Evidence](../screenshots/README.md)

</div>

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%" alt="section divider" />

# 🔎 Scenario 02 — DGA + High NXDOMAIN Investigation

**Status:** ✅ Complete and validated  
**Platform:** Splunk Enterprise 10.4.2 / Dashboard Studio  
**Artifact:** [`scenario-02-dga-investigation-dashboard.json`](scenario-02-dga-investigation-dashboard.json)

The dashboard was engineered as an **investigation surface**. Its job is to help a SOC analyst move from high-level DNS behavior to the exact resolver evidence behind a suspicious client/minute.

![Final Scenario 02 dashboard](../screenshots/detection-engineering/04-dga-investigation-dashboard.png)

## 🗂️ Final implementation

```text
5 global inputs
13 visualizations
16 data sources / searches
```

The exported JSON is the actual validated Dashboard Studio definition. It is preserved here rather than recreated from screenshots.

## 🗂️ Global controls

- Global Time Range
- Client IP
- Response Code
- Query Type
- Qname / Domain

Raw-DNS filters are applied to raw resolver searches. Response-code/query-type/qname filters are not blindly forced onto the already-aggregated ML result dataset.

## 🔎 SOC summary row

| KPI | Analyst question |
|---|---|
| Total DNS Replies | How much resolver activity is in scope? |
| NXDOMAIN Count | How many failed resolutions occurred? |
| NXDOMAIN Ratio | Is failure dominant, not merely present? |
| Unique Qnames | How broad is the requested-name set? |
| Active Clients | Which clients generated the visible activity? |
| ML Anomalous Windows | Does the independent Isolation Forest also consider any window unusual? |

## 📊 Behavior over time

- **DNS Volume + NXDOMAIN Over Time** — is there a concentrated burst and did failure rise with it?
- **Unique Qnames + NXDOMAIN Ratio Over Time** — did name breadth and failed resolution rise together?
- **Average + Maximum Qname Length Over Time** — are requested names structurally longer than the clean baseline?
- **Query-Type Distribution** — what DNS record types were involved?

## 🔎 Investigation views

- **Top NXDOMAIN Names** — which failed names dominate the selected context?
- **Raw DNS Investigation** — exact resolver replies with client, qname, qtype, rcode and response time.
- **ML Window Context — Supporting Signal** — existing Isolation Forest prediction and raw anomaly score beside one-minute behavior metrics.

> [!NOTE]
> The dashboard was already complete before the final rule/alert/AI integration work. Later engineering did not justify redesigning a working analyst surface simply to add more panels. Rule ↔ ML validation is preserved separately in the SPL/evidence workspace.

## 🧾 Evidence path

```text
Dashboard summary
      ↓
behavior window
      ↓
client / time pivot
      ↓
Raw DNS Investigation
      ↓
index=dns_soc_dns
```

The dashboard supports investigation; it does not make the final SOC disposition.

## ✅ Official exercise closeout

The same analyst surface was later used during Sonia's completed Scenario 02 investigation. It supported the exact 06:37–06:41 UTC window after Detection v1.0 surfaced five consecutive matches. The final SOC narrative and exact-window dashboard evidence are preserved in [`../soc/SOC-ANALYST-INVESTIGATION.md`](../soc/SOC-ANALYST-INVESTIGATION.md).

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%" alt="section divider" />

<div align="center">

**DNSentinel Scenario 02 · Evidence before verdict · Humans before automation**

[🏠 Scenario Home](../README.md) · [📖 Detection Story](../detection-engineering/DETECTION-ENGINEERING.md) · [⬆ Back to top](#top)

</div>

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=30,24,19,12,6&height=75&section=footer" width="100%" alt="DNSentinel Scenario 02 footer" />
