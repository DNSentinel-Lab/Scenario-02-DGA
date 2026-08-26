<a id="top"></a>

<img src="https://capsule-render.vercel.app/api?type=soft&color=gradient&customColorList=6,12,19,24,30&height=150&section=header&text=%F0%9F%94%8E%20SOC%20Curated%20Evidence&fontSize=30&fontColor=ffffff&animation=fadeIn&fontAlignY=38&desc=Scenario%2002%20%E2%80%94%20Sonia%20%7C%20E01%E2%80%93E13%20%7C%20Detection%20%E2%86%92%20Scope%20%E2%86%92%20Handoff&descSize=14&descAlignY=68&descColor=22D3EE" width="100%" alt="🔎 SOC Curated Evidence" />

<div align="center">

![Evidence](https://img.shields.io/badge/SOC_Evidence-E01%E2%80%93E13-22D3EE?style=flat-square)
![Status](https://img.shields.io/badge/Investigation-Complete-2EA44F?style=flat-square)
![Disposition](https://img.shields.io/badge/Disposition-INCONCLUSIVE_%E2%86%92_IR-F59E0B?style=flat-square)

[🏠 Scenario Home](../../README.md) · [🔎 SOC Workspace](../README.md) · [📖 Investigation](../SOC-ANALYST-INVESTIGATION.md) · [🧾 Master Evidence](../../evidence/README.md)

</div>

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%" alt="section divider" />

# 🧾 Scenario 02 SOC — Curated Evidence

These images are the public evidence set for Sonia's completed SOC investigation. The full troubleshooting/progress screenshot archive remains outside the flagship story; only screenshots that answer an investigation question are promoted here.

## 🖼️ Evidence Highlights

<table>
<tr>
<td width="33%"><img src="S02-SOC-E01_Detection-v1-Hit.png" alt="Detection hit"><br/><sub><b>E01:</b> first live Detection v1.0 hit.</sub></td>
<td width="33%"><img src="S02-SOC-E03_Raw-Unbound-Replies.png" alt="Raw Unbound"><br/><sub><b>E03:</b> raw resolver evidence.</sub></td>
<td width="33%"><img src="S02-SOC-E05_Client-Historical-Baseline.png" alt="Client baseline"><br/><sub><b>E05:</b> same-client historical baseline.</sub></td>
</tr>
<tr>
<td width="33%"><img src="S02-SOC-E08_ML-Anomaly-Assessment.png" alt="ML assessment"><br/><sub><b>E08:</b> ML second opinion.</sub></td>
<td width="33%"><img src="S02-SOC-E10_AI-vs-Human-Validation.png" alt="AI human validation"><br/><sub><b>E10:</b> AI claims checked by a human analyst.</sub></td>
<td width="33%"><img src="S02-SOC-E13_Final-Client-Scope.png" alt="Final client scope"><br/><sub><b>E13:</b> final resolver-visible scope.</sub></td>
</tr>
</table>

## 📋 Full Evidence Set

| Evidence | Purpose |
|---|---|
| `S02-SOC-E01_Detection-v1-Hit.png` | first live Detection v1.0 hit |
| `S02-SOC-E02_Detection-Windows.png` | five consecutive frozen-detection windows |
| `S02-SOC-E03_Raw-Unbound-Replies.png` | raw resolver evidence for the exact cluster |
| `S02-SOC-E04_Qname-Pattern-Metrics.png` | qname uniqueness/label/NXDOMAIN measurements |
| `S02-SOC-E05_Client-Historical-Baseline.png` | same-client historical baseline |
| `S02-SOC-E06_All-Detection-Windows-24h.png` | wider frozen-rule recurrence |
| `S02-SOC-E07_Detection-Activity-Clusters.png` | separate historical activity clusters |
| `S02-SOC-E08_ML-Anomaly-Assessment.png` | Isolation Forest second opinion |
| `S02-SOC-E09_AI-Summary-Review.png` | AI summary after raw-evidence investigation |
| `S02-SOC-E10_AI-vs-Human-Validation.png` | AI claims checked against human evidence |
| `S02-SOC-E11_Non-NXDOMAIN-Replies.png` | successful DNS response review |
| `S02-SOC-E12_Scenario02-Dashboard.png` | exact-window analyst dashboard |
| `S02-SOC-E13_Final-Client-Scope.png` | final resolver-visible scope |

> [!IMPORTANT]
> Evidence captions state exactly what each image proves and avoid upgrading DNS observations into process or malware attribution.

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%" alt="section divider" />

<div align="center">

[🔎 SOC Workspace](../README.md) · [📖 Investigation](../SOC-ANALYST-INVESTIGATION.md) · [⬆ Back to top](#top)

</div>

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=30,24,19,12,6&height=75&section=footer" width="100%" alt="DNSentinel Scenario 02 footer" />
