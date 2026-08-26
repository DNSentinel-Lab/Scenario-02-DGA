<a id="top"></a>

<img src="https://capsule-render.vercel.app/api?type=soft&color=gradient&customColorList=6,12,19,24,30&height=150&section=header&text=%F0%9F%9B%A1%EF%B8%8F%20IR%20Curated%20Evidence&fontSize=30&fontColor=ffffff&animation=fadeIn&fontAlignY=38&desc=Scenario%2002%20%E2%80%94%20Abdul-Rehman%20%7C%20E01%E2%80%93E21%20%7C%20Validate%20%E2%86%92%20Contain%20%E2%86%92%20Verify%20%E2%86%92%20Reset&descSize=14&descAlignY=68&descColor=F59E0B" width="100%" alt="🛡️ IR Curated Evidence" />

<div align="center">

![Evidence](https://img.shields.io/badge/IR_Evidence-E01%E2%80%93E21-F59E0B?style=flat-square)
![Containment](https://img.shields.io/badge/RPZ_Containment-Validated-2EA44F?style=flat-square)
![Reset](https://img.shields.io/badge/Safe_Reset-Complete-14B8A6?style=flat-square)

[🏠 Scenario Home](../../README.md) · [🛡️ IR Workspace](../README.md) · [📖 IR Story](../INCIDENT-RESPONSE.md) · [🧾 Master Evidence](../../evidence/README.md)

</div>

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%" alt="section divider" />

# 🧾 Scenario 02 IR — Curated Evidence

This folder preserves the official E01–E21 Incident Response evidence chain.

## 🖼️ Containment Chain Highlights

<table>
<tr>
<td width="33%"><img src="S02-IR-E10-PreContainment-NXDOMAIN.png" alt="Before containment"><br/><sub><b>E10:</b> pre-containment NXDOMAIN.</sub></td>
<td width="33%"><img src="S02-IR-E14-PostContainment-RPZ-Redirect.png" alt="RPZ redirect"><br/><sub><b>E14:</b> same qname redirected to <code>10.50.30.30</code>.</sub></td>
<td width="33%"><img src="S02-IR-E17-End-to-End-Sinkhole-Reachable.png" alt="Sinkhole HTTP 200"><br/><sub><b>E17:</b> end-to-end sinkhole reachability.</sub></td>
</tr>
<tr>
<td width="33%"><img src="S02-IR-E18-Normal-DNS-Unaffected.png" alt="Normal DNS"><br/><sub><b>E18:</b> unrelated DNS unaffected.</sub></td>
<td width="33%"><img src="S02-IR-E19-Splunk-Before-After-RPZ.png" alt="Splunk before after"><br/><sub><b>E19:</b> Splunk shows NXDOMAIN → NOERROR.</sub></td>
<td width="33%"><img src="S02-IR-E21-PostReset-DNS-Validation.png" alt="Post reset"><br/><sub><b>E21:</b> post-reset qname returned to NXDOMAIN.</sub></td>
</tr>
</table>

## 🔎 Validation

| Evidence | Purpose |
|---|---|
| E01 | raw DNS window presence |
| E02 | independently reproduced core DNS metrics |
| E03 | five one-minute windows |
| E04 | generated-looking qname examples |
| E05 | resolver-visible client scope |
| E06 | non-NXDOMAIN review |
| E07 | endpoint/process telemetry availability |
| E08 | historical recurrence |
| E09 | current-activity check |

## 🛡️ Containment & Verification

| Evidence | Purpose |
|---|---|
| E10 | pre-containment NXDOMAIN |
| E11 | pre-change RPZ safe state |
| E12 | Scenario 02 RPZ rule staged |
| E13 | RPZ runtime activated |
| E14 | same qname redirected to `10.50.30.30` |
| E15 | sinkhole service health |
| E16 | sinkhole local HTTP 200 |
| E17 | victim-to-sinkhole HTTP 200 |
| E18 | unrelated DNS unaffected |
| E19 | Splunk before/after `NXDOMAIN → NOERROR` |
| E20 | RPZ safe state restored |
| E21 | post-reset qname returned to NXDOMAIN |

The source package manifest is retained as [`EVIDENCE-MANIFEST.csv`](EVIDENCE-MANIFEST.csv).

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%" alt="section divider" />

<div align="center">

[🛡️ IR Workspace](../README.md) · [📖 Incident Response](../INCIDENT-RESPONSE.md) · [⬆ Back to top](#top)

</div>

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=30,24,19,12,6&height=75&section=footer" width="100%" alt="DNSentinel Scenario 02 footer" />
