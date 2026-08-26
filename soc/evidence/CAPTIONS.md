<a id="top"></a>

> 🧭 [Scenario 02](../../README.md) › [SOC Analyst](../README.md) › **GitHub Evidence Captions**

<div align="center">

![Scenario](https://img.shields.io/badge/Scenario_02-COMPLETE-2EA44F?style=flat-square) ![Workspace](https://img.shields.io/badge/Workspace-SOC_Analyst-0284C7?style=flat-square) ![Document](https://img.shields.io/badge/Document-Evidence_Backed-D966FF?style=flat-square)

</div>

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%" alt="section divider" />

# 🧾 GitHub Evidence Captions

## 🚨 E01 — Detection v1.0 hit
Frozen Detection v1.0 identified repeated one-minute high-volume/high-uniqueness/high-NXDOMAIN DNS behavior for resolver-visible client `10.50.30.20`.

## 🚨 E02 — Five detection windows
Five consecutive one-minute windows from 06:37 through 06:41 met the production detection without threshold changes.

## 📌 E03 — Raw Unbound replies
Raw resolver replies confirm the behavior behind the alert: rapidly changing qnames and repeated NXDOMAIN responses from the same client.

## 🔎 E04 — Qname pattern metrics
Qname/label measurements show high uniqueness and long/variable labels in the investigated period. The screenshot displays the first visible rows of the five-minute table.

## 🔎 E05 — Historical baseline
The latest burst is far above the same client's normal per-minute query volume, unique-qname count, and NXDOMAIN ratio.

## 🚨 E06 — 24-hour detection history
Detection v1.0 also matched additional one-minute windows during the previous 24 hours, showing the behavior was not limited to one burst.

## 📌 E07 — Activity clusters
The matching windows group into multiple separated clusters, showing recurrent behavior.

## 🧠 E08 — ML anomaly assessment
The Isolation Forest model `dns_iforest_v1` independently marked all five latest windows as `ANOMALY`. ML is supporting context, not malware proof.

## 🤖 E09 — AI summary review
AI summarized the same defender evidence and preserved key uncertainty around process identity, endpoint state, and authorization.

## 🤖 E10 — AI vs human validation
SOC validated AI claims against Splunk and kept client-IP attribution separate from process/malware attribution.

## 🌐 E11 — Non-NXDOMAIN replies
The successful/non-NXDOMAIN replies visible in the latest window were normal-looking AWS service lookups such as SSM and GuardDuty.

## 📊 E12 — Scenario 02 dashboard
The correctly scoped dashboard summarizes the latest five-minute case: 418 replies, 408 NXDOMAIN, 97.61% NXDOMAIN ratio, 409 unique qnames, one active client, and five ML anomalous windows.

## 🔎 E13 — Final scope
Final scope search shows one resolver-visible client (`10.50.30.20`) with five matching one-minute windows in the latest investigated period.
<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%" alt="section divider" />

<div align="center">

**DNSentinel Scenario 02 · Evidence before verdict · Humans before automation**

[🏠 Scenario Home](../../README.md) · [🔎 SOC Analyst](../README.md) · [⬆ Back to top](#top)

</div>

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=30,24,19,12,6&height=75&section=footer" width="100%" alt="DNSentinel Scenario 02 footer" />
