<a id="top"></a>

> 🧭 [Scenario 02](../README.md) › [SOC Analyst](README.md) › **Scenario 02 SOC Investigation Playbook**

<div align="center">

![Scenario](https://img.shields.io/badge/Scenario_02-COMPLETE-2EA44F?style=flat-square) ![Workspace](https://img.shields.io/badge/Workspace-SOC_Analyst-0284C7?style=flat-square) ![Document](https://img.shields.io/badge/Document-Evidence_Backed-D966FF?style=flat-square)

</div>

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%" alt="section divider" />

# 🔎 Scenario 02 SOC Investigation Playbook

## 🎯 Purpose
Guide the SOC Analyst through Scenario 02 using only defender-side evidence, without attacker/operator ground truth.

## 🚨 Rules
- Keep Detection v1.0 frozen.
- Use defender evidence only.
- Treat `10.50.30.20` as a resolver-visible client, not process attribution.
- Validate raw DNS before ML or AI.
- ML is a second opinion.
- AI is advisory and must be checked against Splunk.

## 🗂️ Workflow

### 📌 1. Telemetry health
Run [`00_preflight_live_dns_15m.spl`](spl/00_preflight_live_dns_15m.spl) with a live monitoring window.

Goal: confirm Unbound reply telemetry is arriving.

### 🚨 2. Frozen production detection
Run [`01_detection_v1_live.spl`](spl/01_detection_v1_live.spl).

Frozen conditions:
- query_count >= 20
- unique_qnames >= 15
- nxdomain_ratio >= 0.75

If no result appears, continue monitoring. Do not lower thresholds.

### 🚨 3. Detection triage
Run [`02_detection_windows_clean.spl`](spl/02_detection_windows_clean.spl).

Goal: identify exact client/minute metrics.

### 🧾 4. Raw Unbound validation
Run [`04_raw_unbound_exact_window.spl`](spl/04_raw_unbound_exact_window.spl) for the detected window.

Goal: prove the aggregate alert is backed by raw DNS reply events.

### 🔎 5. Qname structure
Run [`05_qname_pattern_metrics.spl`](spl/05_qname_pattern_metrics.spl).

Goal: measure uniqueness, first-label lengths, qtypes, and NXDOMAIN ratio.

### 🔎 6. Client baseline
Run [`07_baseline_corrected.spl`](spl/07_baseline_corrected.spl).

Goal: compare current behavior with the same client's previous 24-hour one-minute behavior, excluding the latest detection period.

### 🕒 7. Historical timeline and recurrence
Run:
- [`08_top_dns_minutes_24h.spl`](spl/08_top_dns_minutes_24h.spl)
- [`09_all_detection_windows_24h.spl`](spl/09_all_detection_windows_24h.spl)
- [`10_detection_activity_clusters.spl`](spl/10_detection_activity_clusters.spl)

Goal: determine whether the behavior is isolated or recurrent.

### 🧠 8. ML second opinion
First inspect event shape with [`11_ml_raw_event_format.spl`](spl/11_ml_raw_event_format.spl), then use [`13_ml_clean_final.spl`](spl/13_ml_clean_final.spl).

Do not interpret `ANOMALY` as malware proof.

### 🤖 9. AI review
First inspect event shape with [`14_ai_raw_event_format.spl`](spl/14_ai_raw_event_format.spl), then use:
- [`16_ai_summary_clean_final.spl`](spl/16_ai_summary_clean_final.spl)
- [`17_ai_vs_human_validation.spl`](spl/17_ai_vs_human_validation.spl)

Validate each AI claim against raw DNS evidence.

### 🌐 10. Non-NXDOMAIN review
Run [`18_non_nxdomain_replies.spl`](spl/18_non_nxdomain_replies.spl).

Goal: determine whether suspicious/generated-looking qnames successfully resolved in the latest window.

### 🧾 11. Dashboard validation
Scope the Scenario 02 dashboard to:
- 2026-08-26 06:37:00 → 06:42:00
- Client IP: `10.50.30.20`

Observed dashboard summary:
- 418 replies
- 408 NXDOMAIN
- 97.61% NXDOMAIN
- 409 unique qnames
- 1 active client
- 5 ML anomalous windows

### 🔎 12. Final scope
Run [`20_final_client_scope.spl`](spl/20_final_client_scope.spl).

Goal: establish affected resolver-visible client count and peak metrics.

### 📨 13. Documentation and handoff
Complete:
- 5W1H
- AI/ML validation notes
- SOC disposition/confidence
- SOC → IR handoff

## 🔎 Final SOC disposition used in this case
**INCONCLUSIVE — escalation warranted**

The SOC confirmed anomalous DGA-like/high-NXDOMAIN behavior with high confidence, but DNS telemetry alone did not prove process/malware attribution or authorization.
<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%" alt="section divider" />

<div align="center">

**DNSentinel Scenario 02 · Evidence before verdict · Humans before automation**

[🏠 Scenario Home](../README.md) · [🔎 SOC Analyst](README.md) · [⬆ Back to top](#top)

</div>

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=30,24,19,12,6&height=75&section=footer" width="100%" alt="DNSentinel Scenario 02 footer" />
