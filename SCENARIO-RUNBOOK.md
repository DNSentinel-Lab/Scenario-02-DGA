<a id="top"></a>

> 🧭 [Scenario 02](README.md) › **Scenario 02 Runbook — DGA + High NXDOMAIN Activity**

![Scenario](https://img.shields.io/badge/Scenario_02-Infrastructure_Ready-D29922?style=flat-square)
![DNSentinel](https://img.shields.io/badge/DNSentinel-Technical_Record-D966FF?style=flat-square)

---

# Scenario 02 Runbook — DGA + High NXDOMAIN Activity

**Status:** Infrastructure ready — scenario execution, Detection Engineering and ML not started  
**Primary MITRE ATT&CK:** `T1568.002` — Dynamic Resolution: Domain Generation Algorithms

This is the working checklist for the scenario. Infrastructure prerequisites are now real; scenario sections stay **Planned** until the corresponding exercise evidence exists. Do not fill gaps with invented values.

## 1. Objective

Generate harmless controlled DNS requests that resemble domain-generation behavior and determine whether the SOC can identify the pattern without treating every NXDOMAIN response as malicious.

**Status:** Planned — exercise not run.

## 2. Architecture

The Scenario 02 infrastructure dependency is complete:

```text
dns-soc-victim01 / 10.50.30.20
        |
        | DNS
        v
dns-soc-resolver01 / 10.50.30.10 / Unbound
        |
        +--> normal forward -> AWS VPC Resolver 10.50.0.2
        |
        +--> resolver UF -> Splunk / dns_soc_dns
        |
        +--> RPZ when human-approved -> 10.50.30.30
                                    -> dns-soc-sinkhole01 / Nginx
                                    -> sinkhole UF -> Splunk / dns_soc_web
```

Final infrastructure RPZ state: policy loaded, logging available, `rpz-action-override: disabled`.

**Status:** Infrastructure complete.

## 3. Prerequisites

Already satisfied:

- shared AWS/Splunk/AI platform healthy;
- resolver/victim/sinkhole infrastructure built;
- resolver query/reply telemetry searchable;
- core DNS fields validated;
- private sinkhole path and RPZ capability validated;
- RPZ enforcement reset to safe disabled state.

Still required before the scenario simulation:

- Detection Engineer captures a normal DNS baseline;
- Project Lead defines the controlled DGA generator, rate and safety limit;
- exercise start/end ground-truth method is agreed;
- SOC Analyst and IR/Defender know the exercise window but are not handed a pre-written conclusion;
- optional ML implementation remains deferred until baseline/rule-based work exists.

**Status:** Infrastructure prerequisites complete; execution prerequisites pending.

## 4. Attack / Simulation

Generate harmless nonexistent labels under an owned/authorized lab namespace. Do not create thousands of public Route 53 records just to avoid NXDOMAIN.

Conceptual pattern:

```text
<generated-label>.dga.soclab.abdul4rehman215.tech
```

Record final commands/tool, generation rate, maximum duration/count and exact ground-truth timestamps only when executed.

**Status:** Planned.

## 5. Telemetry

### Primary Scenario 02 resolver source — ready

```text
index=dns_soc_dns
host=dns-soc-resolver01
source=/var/log/dns-soc/unbound.log
sourcetype=unbound:dns
```

Validated fields:

```text
event_type
client_ip
qname
qtype
rcode
response_time
cache_flag
response_size
```

### Sinkhole application source — ready

```text
index=dns_soc_web
host=dns-soc-sinkhole01
source=/var/log/nginx/access.log
sourcetype=nginx:access
```

### Supporting shared sources

Use only where they contribute real evidence:

- AWS VPC Resolver Query Logs;
- VPC Flow Logs;
- Route 53 public query logs;
- CloudTrail when control-plane changes are relevant;
- shared AI result index after alert integration;
- endpoint/client telemetry only if actually onboarded later.

**Status:** Infrastructure telemetry validated; scenario DGA telemetry not generated yet.

## 6. Detection

Future behavioral hypothesis should evaluate:

- NXDOMAIN count and ratio;
- total query rate;
- unique qnames;
- label length/randomness/entropy features derived from `qname`;
- repeated client identity (`client_ip`);
- time-window behavior;
- query-type diversity where it adds value.

The final threshold/window is set only after normal baseline and controlled simulation results exist.

**Status:** Planned.

## 7. SPL / Detection Logic

Create real files under [`spl/`](spl/) only after the searches exist:

```text
baseline.spl
hunting.spl
detection.spl
validation.spl
```

Required order:

```text
baseline -> hunting -> initial detection -> controlled positive test
-> benign/false-positive test -> tune only if needed
-> final detection -> validation
```

**Status:** Planned.

## 8. Alert

After final detection is stable, create an analyst-ready scheduled alert containing at least:

- detection name/version;
- first/last time;
- client identity;
- query/NXDOMAIN counts and ratio;
- unique-name and relevant label metrics;
- representative qnames/qtypes/results;
- severity/rationale;
- drilldown/raw search;
- supporting sinkhole/network context only when available.

**Status:** Planned.

## 9. AI Triage

Reuse the shared AI bridge. Add a Scenario 02 profile only after stable alert fields exist.

ML and LLM remain different components:

- ML may later contribute an anomaly score;
- the LLM explains/enriches structured alert evidence;
- neither authorizes containment.

Record the input payload, AI response and human validation against raw Splunk evidence.

**Status:** Planned.

## 10. SOC Analysis

Build the investigation from raw resolver events and supporting telemetry. Document pivots, timeline, competing explanations, disposition and confidence.

**Status:** Planned.

## 11. Incident Response

The reusable RPZ/sinkhole control is technically ready, but the Scenario 02 response has **not** been performed.

Future response chain:

```text
Finding
  ↓
Human investigation
  ↓
Human-approved containment decision
  ↓
Enable the approved RPZ response
  ↓
Victim resolves selected name/pattern to 10.50.30.30
  ↓
Sinkhole evidence appears
  ↓
Verify result
  ↓
Reset policy to safe state
```

Do not treat a Splunk result, ML score or AI summary as automatic response authorization.

**Status:** Planned.

## 12. Evidence

Infrastructure proof stays in the shared Infrastructure repository. Scenario evidence stored here later should cover:

- baseline;
- ground-truth simulation timing;
- DGA/high-NXDOMAIN telemetry;
- detection/alert;
- false-positive validation;
- optional ML comparison;
- AI result;
- human SOC analysis;
- approved response;
- before/after containment verification;
- reset and lessons.

**Status:** Planned.

## 13. Containment

Containment is performed only after the human investigation reaches the approved response condition.

**Status:** Planned.

## 14. Verification

Prove both states with evidence:

```text
Before response:
generated/suspicious controlled name -> normal resolver outcome / NXDOMAIN

After approved response:
selected name/pattern -> RPZ -> 10.50.30.30 -> Nginx sinkhole
```

Then prove the final reset state again.

**Status:** Planned.

## 15. Results

Summarize the final detection result, optional ML comparison, SOC disposition, response, verification and overall scenario completion condition.

**Status:** Planned.

## 16. MITRE ATT&CK Mapping

Primary mapping: **`T1568.002` — Dynamic Resolution: Domain Generation Algorithms**.

Map only behavior actually generated, observed and detected. Do not add extra techniques because they sound related.

**Status:** Planned.

## 17. False Positives

Deliberately test plausible benign NXDOMAIN behavior and other normal activity that may resemble part of the detection. Record every threshold/feature change and the evidence for it.

**Status:** Planned.

## 18. Lessons Learned

Capture technical, detection, ML, analyst and IR lessons as reusable engineering knowledge rather than a chat/debug transcript.

**Status:** Planned.

## 19. Reproduction Instructions

At scenario completion, provide one clean order:

```text
verify completed infrastructure
-> baseline
-> controlled DGA simulation
-> validate telemetry
-> dashboard/hunting
-> rule-based detection
-> optional ML comparison
-> benign/positive validation
-> alert
-> AI triage
-> human investigation
-> approved RPZ containment
-> verify
-> reset
```

**Status:** Planned.

## 20. Screenshots

Scenario execution screenshots start in [`screenshots/`](screenshots/) only when the real exercise begins. Infrastructure evidence remains in the shared Infrastructure repository and is not duplicated here.

**Status:** Planned.

## Network & protocol view

- **Layer 7 DNS:** `qname`, `qtype`, `rcode`, generated-label structure, NXDOMAIN ratio;
- **Layer 4:** victim -> resolver UDP/TCP 53; HTTP 80 to sinkhole after response;
- **Layer 3:** `10.50.30.20 -> 10.50.30.10`, then `10.50.30.20 -> 10.50.30.30` after approved containment; VPC Flow context where useful;
- **Endpoint:** victim identity is known; process context is added only if later telemetry really provides it;
- **Cloud:** AWS Resolver/Route 53/CloudTrail used only where they support the story;
- **Application follow-up:** sinkhole Nginx access proves the redirected HTTP request.

## Completion gate

Infrastructure is ready, but the scenario is not complete until the team can reproduce:

**Simulation → Telemetry → Detection → Alert → AI Assistance → Human Investigation → Response → Verification → Lessons Learned.**

---

<div align="center">

[🏠 Scenario Home](README.md) · [🏗️ Infrastructure](https://github.com/DNSentinel-Lab/DNS-Lab-Infrastructure) · [⬆ Back to top](#top)

<sub>DNSentinel Lab · Evidence-first DNS security engineering</sub>

</div>
