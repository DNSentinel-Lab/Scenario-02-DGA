<a id="top"></a>

> 🧭 [Scenario 02](../README.md) › [SOC Analyst](README.md) › **SPL Query Index**

<div align="center">

![Scenario](https://img.shields.io/badge/Scenario_02-COMPLETE-2EA44F?style=flat-square) ![Workspace](https://img.shields.io/badge/Workspace-SOC_Analyst-0284C7?style=flat-square) ![Document](https://img.shields.io/badge/Document-Evidence_Backed-D966FF?style=flat-square)

</div>

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%" alt="section divider" />

# 🗂️ SPL Query Index

The `spl/` folder preserves **all SPL used in the SOC Analyst chat**, including failed/troubleshooting variants so the GitHub history shows what was tried and how it was fixed.

| File | Purpose |
|---|---|
| `00_preflight_live_dns_15m.spl` | Telemetry health / pre-flight |
| `01_detection_v1_live.spl` | Frozen production detection with qname samples |
| `02_detection_windows_clean.spl` | Clean one-minute detection rows |
| `03_raw_unbound_broad_client.spl` | Broad raw client view before exact scoping |
| `04_raw_unbound_exact_window.spl` | Raw Unbound evidence for 06:37–06:42 |
| `05_qname_pattern_metrics.spl` | Label length, uniqueness, qtypes, NXDOMAIN metrics |
| `06_baseline_original_failed_test.spl` | Original failed baseline test; troubleshooting history |
| `07_baseline_corrected.spl` | Correct 24-hour baseline search |
| `08_top_dns_minutes_24h.spl` | Top busiest one-minute windows |
| `09_all_detection_windows_24h.spl` | All frozen-detection matches in 24h |
| `10_detection_activity_clusters.spl` | Groups repeated detection minutes into clusters |
| `11_ml_raw_event_format.spl` | Inspect raw ML event format |
| `12_ml_spath_duplicate_test.spl` | ML duplicate-extraction troubleshooting test |
| `13_ml_clean_final.spl` | Final clean ML evidence table |
| `14_ai_raw_event_format.spl` | Inspect raw AI event format |
| `15_ai_spath_duplicate_test.spl` | AI duplicate-extraction troubleshooting test |
| `16_ai_summary_clean_final.spl` | Final clean AI summary table |
| `17_ai_vs_human_validation.spl` | AI reasoning/network-context validation |
| `18_non_nxdomain_replies.spl` | Successful/non-NXDOMAIN DNS replies |
| `19_exact_window_base_search.spl` | Exact five-minute raw-event base search |
| `20_final_client_scope.spl` | Final exact-window affected-client scope |
<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%" alt="section divider" />

<div align="center">

**DNSentinel Scenario 02 · Evidence before verdict · Humans before automation**

[🏠 Scenario Home](../README.md) · [🔎 SOC Analyst](README.md) · [⬆ Back to top](#top)

</div>

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=30,24,19,12,6&height=75&section=footer" width="100%" alt="DNSentinel Scenario 02 footer" />
