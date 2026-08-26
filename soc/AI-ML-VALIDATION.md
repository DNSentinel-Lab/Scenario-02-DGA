<a id="top"></a>

> 🧭 [Scenario 02](../README.md) › [SOC Analyst](README.md) › **AI and ML Validation**

<div align="center">

![Scenario](https://img.shields.io/badge/Scenario_02-COMPLETE-2EA44F?style=flat-square) ![Workspace](https://img.shields.io/badge/Workspace-SOC_Analyst-0284C7?style=flat-square) ![Document](https://img.shields.io/badge/Document-Evidence_Backed-D966FF?style=flat-square)

</div>

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%" alt="section divider" />

# 🧠 AI and ML Validation

## 🧠 ML
Model: `dns_iforest_v1`

All five latest investigated windows returned:
- `prediction = ANOMALY`
- `prediction_value = -1`

ML was used only as a **second opinion** after raw DNS validation.

## 🤖 AI
AI summaries were reviewed only after the SOC understood the raw DNS, baseline, and timeline.

### 🤖 Confirmed AI claims
- client IP
- query volume
- unique qname volume
- NXDOMAIN count/ratio
- long/highly variable qname structure
- possible DGA/high-NXDOMAIN interpretation

### 📌 Attribution correction
Where AI said the client "generated" queries, the SOC interpretation is:

> The resolver observed DNS queries attributed to `client_ip=10.50.30.20`.

### 🧾 Not proven by DNS evidence
- initiating process
- malware family
- endpoint compromise
- user identity
- authorization status
- transport/process attribution beyond the DNS telemetry
<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%" alt="section divider" />

<div align="center">

**DNSentinel Scenario 02 · Evidence before verdict · Humans before automation**

[🏠 Scenario Home](../README.md) · [🔎 SOC Analyst](README.md) · [⬆ Back to top](#top)

</div>

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=30,24,19,12,6&height=75&section=footer" width="100%" alt="DNSentinel Scenario 02 footer" />
