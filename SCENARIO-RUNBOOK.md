# Scenario 02 Runbook — DGA + High NXDOMAIN Activity

**Status:** Planned — requires Scenario 02 defender-DNS infrastructure before execution  
**Primary MITRE ATT&CK:** T1568.002 — Dynamic Resolution: Domain Generation Algorithms

This is the working checklist for the scenario. Sections remain marked **Planned** until real implementation or evidence exists. Do not fill gaps with invented values.

## 1. Objective

Generate harmless controlled DNS requests that resemble domain-generation behavior and determine whether the SOC can identify the pattern without treating every NXDOMAIN response as malicious.

**Status:** Planned.

## 2. Architecture

Describe only the systems and paths actually used when the scenario is prepared.

```text
Shared infrastructure
      ↓
Scenario-specific infrastructure (if any)
      ↓
Controlled simulation
      ↓
Telemetry
      ↓
Splunk / AI / Human SOC / IR
```

**Scenario infrastructure dependency:** Before execution, deploy `dns-soc-resolver01` (`10.50.30.10`) and `dns-soc-victim01` (`10.50.30.20`) in `SOC-MONITORING-SUBNET`, create the minimum DNS/victim security controls, send resolver telemetry to Splunk, and establish the reusable sinkhole path around `10.50.30.30`.

**Status:** Planned.

## 3. Prerequisites

Before execution, confirm:

- required shared infrastructure is healthy;
- scenario-specific infrastructure, if any, has been built and validated;
- telemetry is arriving with usable timestamps/fields;
- the shared AI bridge is available;
- the Project Lead has the approved simulation plan and ground-truth clock;
- Detection Engineer has captured the normal baseline before attack activity;
- SOC Analyst and IR/Defender know the expected exercise window but do not receive the final detection answer in advance.

**Status:** Planned.

## 4. Attack / Simulation

Record the final controlled commands/tools, safety limits and start/end timestamps only when the exercise is executed.

The simulation must stay inside owned/authorized lab infrastructure and match the scenario objective.

**Status:** Planned.

## 5. Telemetry

List the real sources that capture this scenario. Candidate shared sources include:

- Route 53 public authoritative query logs;
- AWS VPC Resolver Query Logs;
- team-controlled resolver logs from Scenario 02 onward;
- VPC Flow Logs;
- Nginx access telemetry when Web follow-up is relevant;
- CloudTrail when control-plane changes are part of the evidence;
- endpoint/client telemetry only where it is actually collected.

Do not force unused telemetry into the scenario.

**Status:** Planned.

## 6. Detection

Detection focus:

- NXDOMAIN count and NXDOMAIN ratio over time;
- unique generated-name count and repeated client behavior;
- domain/label length and randomness features validated from real events;
- query rate by victim/client;
- process/client context when endpoint telemetry is actually available;
- normal baseline versus controlled generated-domain behavior;

Write the final behavioral hypothesis after observing baseline data.

**Status:** Planned.

## 7. SPL / Detection Logic

Use files under [`spl/`](spl/) after real searches exist:

```text
baseline.spl
hunting.spl
detection.spl
validation.spl
```

Thresholds must be tuned from real baseline and controlled testing rather than copied from an example.

**Status:** Planned.

## 8. Alert

The final alert should contain enough evidence for a human analyst to start investigation without guessing field meanings.

Recommended common fields:

- detection name/version;
- first/last event time;
- observed client/source identity;
- query count / unique-name count / scenario-specific metric;
- relevant query names/types/results;
- supporting Web/network context;
- severity and rationale;
- raw-event or drilldown search.

**Status:** Planned.

## 9. AI Triage

The shared AI bridge is reused. This repository adds only the scenario profile/payload mapping after the detection fields are stable.

Record:

- payload sent;
- AI summary returned;
- useful observations;
- missing/incorrect claims;
- what the SOC Analyst verified independently.

**Status:** Planned.

## 10. SOC Analysis

Build the human investigation timeline from raw evidence. Document pivots, competing explanations, disposition and confidence.

The AI output is supporting context only.

**Status:** Planned.

## 11. Incident Response

After human confirmation, use the team-controlled resolver to apply the approved sinkhole/deny action and prove that subsequent victim DNS behavior changes. Generated public Route 53 records are not created simply to avoid NXDOMAIN.

Record the approved decision and who performed it.

**Status:** Planned.

## 12. Evidence

Store structured evidence notes under [`evidence/`](evidence/) and screenshots under [`screenshots/`](screenshots/).

Evidence should cover:

- pre-scenario health/baseline;
- ground-truth timing;
- telemetry;
- detection/alert;
- AI output;
- SOC analysis;
- containment;
- verification.

**Status:** Planned.

## 13. Containment

Containment is performed only after the human investigation reaches the scenario's approved response condition.

Do not treat detection or AI output as automatic authorization.

**Status:** Planned.

## 14. Verification

Prove what changed after response. Use before/after DNS, network, Web or endpoint evidence appropriate to the scenario.

**Status:** Planned.

## 15. Results

Summarize the final outcome after the exercise:

- detection result;
- SOC disposition;
- response result;
- verification result;
- whether the scenario completion condition passed.

**Status:** Planned.

## 16. MITRE ATT&CK Mapping

Primary mapping: **T1568.002 — Dynamic Resolution: Domain Generation Algorithms**.

Review the mapping against the behavior that was actually generated and detected. Add no extra techniques unless evidence supports them.

If a Cyber Kill Chain view is included, record only the phase that the implemented behavior genuinely demonstrates and cite the scenario evidence for that choice.

**Status:** Planned.

## 17. False Positives

Test plausible benign activity that resembles part of the scenario. Record each threshold or logic change and why it improved separation.

**Status:** Planned.

## 18. Lessons Learned

Capture useful technical, detection, analyst and IR lessons. Write them as reusable engineering knowledge rather than a chat/debugging transcript.

**Status:** Planned.

## 19. Reproduction Instructions

At completion, provide a clean ordered path:

```text
Prerequisites
→ scenario infrastructure
→ baseline
→ controlled simulation
→ validate telemetry
→ run detection
→ investigate
→ AI comparison
→ contain
→ verify
→ cleanup/reset
```

**Status:** Planned.

## 20. Screenshots

Use descriptive filenames and show screenshots next to the sections they prove. Keep a compact screenshot index in [`screenshots/README.md`](screenshots/README.md).

**Status:** Planned.

## Network & protocol view

- Layer 7 DNS: generated names, NXDOMAIN/rcode, query type and label structure;
- Layer 4: client-to-resolver UDP/TCP 53;
- Layer 3: victim/resolver addressing and relevant flow context;
- Endpoint: victim identity/process context where collected;
- Containment: resolver answer/block/sinkhole before vs after;

This section should be updated with the actual fields/ports seen during execution.

## Completion gate

Resolver/victim telemetry is trusted, the detection distinguishes benign NXDOMAIN activity from the controlled DGA pattern, false positives are tested, AI and SOC conclusions are validated, and containment produces measurable before/after evidence.
