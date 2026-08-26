<a id="top"></a>

> 🧭 [Scenario 02](../../README.md) › [SOC Analyst](../README.md) › **Curated Evidence Set**

<div align="center">

![Scenario](https://img.shields.io/badge/Scenario_02-COMPLETE-2EA44F?style=flat-square) ![Workspace](https://img.shields.io/badge/Workspace-SOC_Analyst-0284C7?style=flat-square) ![Document](https://img.shields.io/badge/Document-Evidence_Backed-D966FF?style=flat-square)

</div>

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%" alt="section divider" />

# 🧾 Curated Evidence Set

Use these for the public GitHub investigation story. They are renamed and lightly cropped to remove low-value outer margins while retaining Splunk evidence.

| Evidence | What it proves |
|---|---|
| `E01_Detection-v1-Hit.png` | Detection v1.0 returned matching windows; visible row shows 89 queries, 87 unique qnames, 97.8% NXDOMAIN. |
| `E02_Detection-Windows.png` | Clean five consecutive detection windows for client 10.50.30.20. |
| `E03_Raw-Unbound-Replies.png` | Raw Unbound replies in exact 06:37–06:42 window; changing qnames and NXDOMAIN visible. |
| `E04_Qname-Pattern-Metrics.png` | Measured qname/label metrics; screenshot shows the first visible rows from the five-minute window. |
| `E05_Client-Historical-Baseline.png` | 24-hour baseline excluding the latest five-minute detection period. |
| `E06_All-Detection-Windows-24h.png` | All frozen-detection matches in the previous 24 hours. |
| `E07_Detection-Activity-Clusters.png` | Fifteen matching minutes grouped into five repeated activity clusters. |
| `E08_ML-Anomaly-Assessment.png` | Clean ML table; all five windows marked ANOMALY by dns_iforest_v1. |
| `E09_AI-Summary-Review.png` | Clean AI summary table with alert metrics and cautious attribution wording. |
| `E10_AI-vs-Human-Validation.png` | AI reasoning/network-context view used to validate claims and attribution limits. |
| `E11_Non-NXDOMAIN-Replies.png` | The 10 non-NXDOMAIN replies were normal-looking AWS service lookups. |
| `E12_Scenario02-Dashboard.png` | Final dashboard scoped to 06:37–06:42 and client 10.50.30.20. |
| `E13_Final-Client-Scope.png` | Final scope: one resolver-visible client, five matching windows, peak 89 queries and 87 unique qnames. |

## 💡 Publishing notes
- Use `E12_Scenario02-Dashboard.png` as the main visual summary.
- Use `E03_Raw-Unbound-Replies.png` to prove the alert is backed by raw resolver telemetry.
- Use `E05_Client-Historical-Baseline.png` to show why the behavior is unusual for the same client.
- Place ML and AI evidence after raw DNS/baseline evidence in the README narrative.
- Keep broad-range, incorrect-time, duplicate-`spath`, and error screenshots out of the public evidence folder; those stay in `screenshots_all/`.
- `E04_Qname-Pattern-Metrics.png` shows only the first visible rows of the five-minute table; do not caption it as visually showing all five rows.
<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%" alt="section divider" />

<div align="center">

**DNSentinel Scenario 02 · Evidence before verdict · Humans before automation**

[🏠 Scenario Home](../../README.md) · [🔎 SOC Analyst](../README.md) · [⬆ Back to top](#top)

</div>

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=30,24,19,12,6&height=75&section=footer" width="100%" alt="DNSentinel Scenario 02 footer" />
