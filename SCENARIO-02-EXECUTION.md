<a id="top"></a>

<img src="https://capsule-render.vercel.app/api?type=soft&color=gradient&customColorList=6,12,19,24,30&height=155&section=header&text=%F0%9F%8E%AC%20End-to-End%20Execution%20Record&fontSize=30&fontColor=ffffff&animation=fadeIn&fontAlignY=38&desc=Scenario%2002%20%7C%20Official%20Run%20%E2%86%92%20Detection%20%E2%86%92%20SOC%20%E2%86%92%20IR%20%E2%86%92%20Containment%20%E2%86%92%20Reset&descSize=14&descAlignY=68&descColor=D966FF" width="100%" alt="🎬 End-to-End Execution Record" />

<div align="center">

![Scenario](https://img.shields.io/badge/Scenario_02-COMPLETE-2EA44F?style=flat-square) ![MITRE](https://img.shields.io/badge/MITRE-T1568.002-E34F26?style=flat-square) ![Closeout](https://img.shields.io/badge/Closeout-Evidence_Backed-A855F7?style=flat-square)

[🏠 Scenario Home](README.md) · [🔎 SOC](soc/README.md) · [🛡️ IR](ir/README.md) · [🧾 Evidence](evidence/README.md)

</div>

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%" alt="section divider" />

# 🎬 Scenario 02 — End-to-End Execution

This is the short operational record of the completed **DGA + High NXDOMAIN** exercise. It connects the engineering work, official operator activity, defender telemetry, SOC investigation, Incident Response, sinkhole containment, safe reset, and final reveal without reproducing every command or screenshot.

## 🎬 1. Ready before execution

Before the official run, the environment was already engineered and validated:

- `dns-soc-victim01` used `dns-soc-resolver01` as its DNS path;
- Unbound telemetry was indexed in `dns_soc_dns`;
- the Isolation Forest model and live scorer were available in `dns_soc_ml`;
- Detection v1.0 and the Dashboard Studio investigation view were frozen;
- the `dga_nxdomain_v1` AI evidence path was ready;
- RPZ existed in a safe/non-enforcing state;
- `dns-soc-sinkhole01` was reserved as `10.50.30.30` for approved response.

Musfira completed the final pre-flight without changing the detection, ML model, or RPZ policy.

## 🎬 2. Official operator run

The operator executed the existing generator once, unchanged, from `dns-soc-victim01`.

| Field | Ground truth |
|---|---|
| Generator | `/opt/dns-soc-ml-generators/dga_dns.py` |
| SHA256 | `1dc0ce32d964cd2e70981e502e341d6b4ee66934cc79ea188e69bd4e3f8f51c4` |
| Start | `2026-08-26T06:37:10.787620+00:00` |
| End | `2026-08-26T06:42:11.129575+00:00` |
| Namespace | `*.dga-test.soclab.abdul4rehman215.tech` |
| Exit code | `0` |

![Official DGA run complete](screenshots/attacker/02-official-dga-generator-complete.png)

The operator stopped there. Splunk, ML, AI, and defender alerts were not inspected to decide whether the run should be repeated or accelerated.

## 📌 3. Defender-visible result

Detection v1.0 independently matched five consecutive one-minute windows from `06:37` through `06:41 UTC`.

| UTC minute | Replies | Unique qnames | NXDOMAIN | Ratio |
|---|---:|---:|---:|---:|
| 06:37 | 75 | 72 | 71 | 0.947 |
| 06:38 | 87 | 86 | 85 | 0.977 |
| 06:39 | 82 | 82 | 82 | 1.000 |
| 06:40 | 85 | 84 | 83 | 0.976 |
| 06:41 | 89 | 87 | 87 | 0.978 |

Across the exact five-minute window, Sonia measured **418 replies, 409 unique qnames, 408 NXDOMAIN replies, and a 97.61% NXDOMAIN ratio** from resolver-visible client `10.50.30.20`.

![Five detection windows](soc/evidence/S02-SOC-E02_Detection-Windows.png)

## 🔎 4. SOC investigation

Sonia worked from defender telemetry only. The investigation progressed from alert → raw replies → qname structure → baseline → recurrence → scope → ML → AI → 5W1H.

The strongest observations were:

- generated-looking first labels changed rapidly under the same Scenario 02 parent namespace;
- the five live windows were far above the client's historical baseline;
- similar matching behavior had recurred in earlier clusters;
- all five matching ML windows were `ANOMALY`;
- non-NXDOMAIN replies in the investigated window were ordinary AWS service names;
- DNS evidence did not identify a process, malware family, user, or intent.

![SOC dashboard exact-window view](soc/evidence/S02-SOC-E12_Scenario02-Dashboard.png)

Sonia locked:

> **INCONCLUSIVE — escalation warranted**

and handed the evidence to IR rather than converting strong DNS evidence into unsupported malware attribution.

## 🛡️ 5. IR independent validation

Abdul-Rehman independently reproduced the SOC findings from raw resolver telemetry:

```text
418 replies
409 unique qnames
408 NXDOMAIN
97.61% NXDOMAIN
one resolver-visible client: 10.50.30.20
five consecutive matching one-minute windows
```

IR also confirmed historical recurrence and found no endpoint/process telemetry that could responsibly attribute the DNS to a process or malware.

The response decision therefore targeted the **observed namespace**, not the whole endpoint.

## 🛡️ 6. Human-approved containment

IR selected one observed qname as the before/after control:

```text
ywvuacnec7gmul193uc.dga-test.soclab.abdul4rehman215.tech
```

### 📌 Before

![Pre-containment NXDOMAIN](ir/evidence/S02-IR-E10-PreContainment-NXDOMAIN.png)

The qname returned `NXDOMAIN` through `10.50.30.10`.

### 🛡️ After approved RPZ enforcement

![Post-containment redirect](ir/evidence/S02-IR-E14-PostContainment-RPZ-Redirect.png)

The same qname returned `NOERROR` with `A 10.50.30.30`.

The sinkhole served HTTP `200`, unrelated AWS DNS continued to resolve, and Splunk preserved the before/after response-code change.

## 🛡️ 7. Safe reset

After evidence was captured, RPZ was returned to its documented safe/non-enforcing state. The selected qname returned to `NXDOMAIN` and normal DNS remained healthy.

The response was therefore not merely applied; it was **verified and reversed cleanly**.

## 🎭 8. Final reveal

Only after SOC and IR decisions were locked was operator ground truth compared with defender evidence.

The timelines aligned:

```text
06:37:10.787620  generator begins
06:37–06:41       Detection v1.0 matches five windows
06:42:11.129575  generator completes
```

The defender stack observed the fresh authorized DGA execution without receiving operator timing or intended outcome during the decision process.

## ✅ Final outcome

> **Scenario 02 completed successfully as an information-separated DGA/high-NXDOMAIN defense exercise.** Detection v1.0 surfaced the fresh behavior without live tuning; SOC independently confirmed a recurrent DNS anomaly while preserving attribution limits; IR independently reproduced the evidence and validated a narrowly scoped RPZ sinkhole response; the resolver was then restored safely.

For the deeper role stories, continue to:

- [Project Lead / Adversary](attacker/PROJECT-LEAD-ADVERSARY.md)
- [ML Engineering](ml/ML-ENGINEERING.md)
- [Detection Engineering](detection-engineering/DETECTION-ENGINEERING.md)
- [SOC Analyst Investigation](soc/SOC-ANALYST-INVESTIGATION.md)
- [Incident Response](ir/INCIDENT-RESPONSE.md)
- [Final Comparison](exercise/final-comparison.md)

---

[⬆ Back to top](#top)
<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%" alt="section divider" />

<div align="center">

**DNSentinel Scenario 02 · Evidence before verdict · Humans before automation**

[🏠 Scenario Home](README.md) · [⬆ Back to top](#top)

</div>

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=30,24,19,12,6&height=75&section=footer" width="100%" alt="DNSentinel Scenario 02 footer" />
