# Scenario 02 — Detection Engineering Validation Record

**Detection Engineer / AI Integrator:** Lubaba  
**Scenario:** DGA + High NXDOMAIN  
**Production detection:** `Scenario 02 - Possible DGA / High NXDOMAIN`  
**Version:** `1.0`  
**MITRE ATT&CK:** `T1568.002 — Dynamic Resolution: Domain Generation Algorithms`  
**Status:** **✅ Detection Engineering ready for the official Scenario 02 exercise**

This record summarizes the acceptance evidence used to close the engineering phase. It does not represent the later official adversary/SOC/IR exercise.

## Final detection boundary

```text
Primary source:  index=dns_soc_dns
Event side:      event_type="reply"
Entity:          client_ip
Window:          1 minute

query_count >= 20
AND unique_qnames >= 15
AND nxdomain_ratio >= 0.75
```

## Acceptance matrix

| Gate | Expected | Observed | Result |
|---|---|---|---|
| Live resolver fields | Stable DNS fields available | `event_type`, `client_ip`, `qname`, `qtype`, `rcode`, timing/context fields available | ✅ PASS |
| Transaction semantics | Avoid query/reply double count | Reply side selected as one completed DNS transaction | ✅ PASS |
| Ingestion timing | Delivery fast enough to schedule safely | Median `2.389 s`; p95 `9.195 s`; max sample `9.196 s` | ✅ PASS |
| Clean DE baseline | Known-clean one-minute/client distribution | 32 windows measured independently from raw `dns_soc_dns` | ✅ PASS |
| Baseline query maximum | Establish normal upper range | `14` | ✅ PASS |
| Baseline unique-qname maximum | Establish normal upper range | `10` | ✅ PASS |
| Baseline NXDOMAIN-ratio maximum | Establish normal failure range | `0.50` | ✅ PASS |
| Dashboard Studio | Analyst investigation surface | 5 inputs, 13 visualizations, 16 data sources; filters/raw path validated | ✅ PASS |
| Hunting | Threshold-free behavior + raw pivot | Two reusable hunts preserved | ✅ PASS |
| Fresh positive DGA | Candidate should recognize target behavior | 6/6 fresh controlled DGA one-minute windows crossed candidate | ✅ PASS |
| Ordinary DNS benign test | Should not detect basic DNS use | Below candidate | ✅ PASS |
| Limited benign NXDOMAIN | Should not detect a few failed lookups | Below candidate | ✅ PASS |
| Repeated normal burst | Understand sensor-visible behavior | Cache-limited visibility identified; test not overstated | ✅ PASS |
| Unique legitimate-name burst | Challenge volume + uniqueness without NXDOMAIN | `23` queries, `23` unique names, `0.0` NXDOMAIN ratio → below full rule | ✅ PASS |
| Threshold freeze | Avoid tuning to desired outcome | Candidate retained unchanged as Detection v1.0 | ✅ PASS |
| `validation.spl` | Show positive and below-threshold rows | `WOULD DETECT` + `BELOW THRESHOLD` visible using same v1.0 logic | ✅ PASS |
| Rule ↔ ML comparison | Compare without forcing agreement | Historical controlled DGA: 6/6 `DETECT` + `ANOMALY` | ✅ PASS |
| ML integrity | Do not retrain/redesign model | Existing Isolation Forest preserved; raw score semantics retained | ✅ PASS |
| Scheduled alert | Real automatic execution | Cron `* * * * *`, range `-2m@m` → `-1m@m`, real trigger confirmed | ✅ PASS |
| Triggered result | Alert row contains real DGA evidence | Example 09:09 minute: 41 queries, 37 unique, NXDOMAIN ratio `0.8780` | ✅ PASS |
| Raw drilldown | Analyst can recover original events | Exact `dns_soc_dns` resolver replies searchable for detected minute/client | ✅ PASS |
| Analyst evidence contract | Human/AI result row stable | `alert_id`, `alert_name`, `scenario`, `severity`, `event_time`, `source`, `evidence_json` | ✅ PASS |
| Scenario 02 AI identity | Stable scenario mapping | `scenario-02-dga` / `dga_nxdomain_v1` | ✅ PASS |
| Shared AI architecture | Reuse existing foundation | No new Flask route/container/index/public port required | ✅ PASS |
| AI E2E | Alert → bridge → OpenAI → HEC | Structured event indexed in `dns_soc_ai` | ✅ PASS |
| AI advisory boundary | No automatic verdict/containment | `human_validation_required=true`; uncertainty preserved | ✅ PASS |
| AI vs raw evidence | Core AI facts must be defensible | `55 / 54 / 0.9818 / 53 / 0.9636` matched raw DNS exactly | ✅ PASS |
| Automatic response | Must remain disabled | No RPZ, isolation or IR action authorized by rule/ML/AI | ✅ PASS |
| Official scenario execution | Must remain separate from engineering validation | Later completed with five live rule matches, SOC investigation, IR containment verification and safe reset | ✅ COMPLETE |

## Threshold rationale

The clean baseline reached:

```text
query_count max       = 14
unique_qnames max     = 10
nxdomain_ratio max    = 0.50
```

The fresh controlled DGA run produced approximately:

```text
query_count        ≈ 30–94
unique_qnames      ≈ 30–91
unique_qname_ratio ≈ 0.9681–1.0000
nxdomain_ratio     ≈ 0.9574–1.0000
```

The high-volume/high-unique legitimate-name challenge reached:

```text
query_count       = 23
unique_qnames     = 23
nxdomain_ratio    = 0.0
```

and remained below the full detection. No test demonstrated a need to change the candidate threshold, so it was frozen as v1.0.

## Scheduled-alert validation

```text
Name:         Scenario 02 - Possible DGA / High NXDOMAIN
Schedule:     * * * * *
Earliest:     -2m@m
Latest:       -1m@m
Trigger:      Number of Results > 0
Trigger mode: Once
Severity:     Medium
Actions:      Triggered Alerts + Webhook
```

A fresh validation run beginning at `2026-08-25T09:09:34Z` produced a real scheduled result for the 09:09 minute with:

```text
client_ip          = 10.50.30.20
query_count        = 41
unique_qnames      = 37
unique_qname_ratio = 0.9024
nxdomain_count     = 36
nxdomain_ratio     = 0.8780
```

## AI final validation

The corrected end-to-end AI path returned structured Scenario 02 triage into:

```text
index=dns_soc_ai
sourcetype=dns_soc:ai:triage
```

The AI reported the following core DNS facts for the final validation minute:

```text
query_count        = 55
unique_qnames      = 54
unique_qname_ratio = 0.9818
nxdomain_count     = 53
nxdomain_ratio     = 0.9636
```

A separate raw resolver aggregation returned the exact same values.

## Evidence links

- [Flagship engineering story](DETECTION-ENGINEERING.md)
- [Baseline SPL](../spl/baseline.spl)
- [Hunting SPL](../spl/hunting.spl)
- [Detection v1.0](../spl/detection.spl)
- [Validation SPL](../spl/validation.spl)
- [Scheduled alert](../spl/scheduled-alert.md)
- [Engineering validation searches](../spl/engineering-validation/)
- [Dashboard Studio JSON](../dashboard/scenario-02-dga-investigation-dashboard.json)
- [Scenario 02 AI mapping](../ai/scenario-02-ai-mapping.md)
- [Full Detection v1 validation output](../evidence/detection-v1-validation-output.csv)
- [Curated Detection Engineering screenshots](../screenshots/detection-engineering/)

## Completion boundary

**Detection Engineering:** ✅ complete  
**Official Scenario 02 adversary/SOC/IR exercise:** ✅ completed after the engineering validation recorded here

The later official exercise followed that boundary: Detection v1.0 remained frozen and information separation was preserved. The fresh run produced five consecutive matching windows without live threshold changes; any disagreement or miss would have been treated as an exercise result rather than a reason to tune the rule during execution.
