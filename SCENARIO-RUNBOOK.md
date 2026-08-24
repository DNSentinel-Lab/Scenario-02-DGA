<a id="top"></a>

> 🧭 [Scenario 02](README.md) › **Scenario 02 Runbook — DGA + High NXDOMAIN Activity**

![Scenario](https://img.shields.io/badge/Scenario_02-ML_Engineering_Complete-2EA44F?style=flat-square)
![DNSentinel](https://img.shields.io/badge/DNSentinel-Technical_Record-D966FF?style=flat-square)

---

# Scenario 02 Runbook — DGA + High NXDOMAIN Activity

**Status:** Infrastructure + Machine Learning Engineering complete; Detection Engineering is next  
**Primary MITRE ATT&CK:** `T1568.002` — Dynamic Resolution: Domain Generation Algorithms

This runbook separates completed engineering work from the future official Scenario 02 exercise. The controlled benign/DGA traffic used for ML training and evaluation is preserved as **ML engineering ground truth**, not presented as the official information-separated adversary run.

## 1. Objective

Generate harmless controlled DNS requests that resemble domain-generation behavior and determine whether the SOC can identify the pattern without treating every NXDOMAIN response as malicious.

**Status:** Scenario objective locked; official exercise pending.

## 2. Architecture

The defender-DNS platform and the ML path are implemented:

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
                              | private REST :8089
                              v
                         dns-soc-ml
                              |
                              | Isolation Forest v1
                              v
                         private HEC :8088
                              |
                              v
                         dns_soc_ml
        |
        +--> RPZ when human-approved -> 10.50.30.30
                                    -> dns-soc-sinkhole01 / Nginx
                                    -> sinkhole UF -> Splunk / dns_soc_web
```

Final infrastructure RPZ state: policy loaded, logging available, `rpz-action-override: disabled`.

**Status:** Infrastructure + ML path complete.

## 3. Prerequisites

Already satisfied:

- shared AWS/Splunk/AI platform healthy;
- resolver/victim/sinkhole infrastructure built;
- resolver query/reply telemetry searchable;
- core DNS fields validated;
- private sinkhole path and RPZ capability validated;
- RPZ enforcement reset to safe disabled state;
- `dns-soc-ml` container implemented on the existing Splunk host;
- restricted Splunk REST reader validated;
- dedicated `dns_soc_ml` HEC path validated;
- Isolation Forest v1 trained and controlled-DGA scoring completed.

Still required before the **official** Scenario 02 simulation:

- Detection Engineer establishes the official normal baseline used for rule-based detection;
- dashboard/hunting/detection logic is built and frozen before the live exercise;
- Project Lead defines the official controlled DGA generator rate/duration and private ground-truth record;
- SOC Analyst and IR/Defender operate without attacker ground truth until defender conclusions are locked;
- final alert fields are stable before Scenario 02 AI mapping begins.

**Status:** Engineering prerequisites complete; official exercise prerequisites pending.

## 4. Adversary Activity / Simulation

### ML engineering traffic — complete

Two benign generator runs and one five-minute controlled DGA run were used only to train/evaluate the ML layer.

Controlled DGA pattern:

```text
<random-label>.dga-test.soclab.abdul4rehman215.tech
```

No malware was executed and no unrelated external target was used.

### Official Scenario 02 simulation — pending

The Project Lead / Adversary Operator will later perform a fresh information-separated controlled run after Detection Engineering is frozen. Record exact commands/tooling, rate, duration and UTC timestamps privately until defender findings are locked.

**Status:** ML engineering simulation complete; official exercise pending.

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

### ML result source — ready

```text
index=dns_soc_ml
host=dns-soc-ml
source=isolation-forest
sourcetype=dns_soc:ml:iforest
```

Implemented ML result fields include:

```text
event_type
model
scenario
client_ip
window_time
prediction
prediction_value
anomaly_score
query_count
unique_qnames
nxdomain_count
nxdomain_ratio
avg_qname_length
max_qname_length
unique_tlds
a_count
aaaa_count
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

**Status:** Resolver + sinkhole + ML result telemetry validated; official scenario evidence pending.

## 6. Detection

### ML anomaly signal — complete

Isolation Forest v1 uses one-minute DNS behavior windows. It is an additional signal, not the final security detection.

Actual model inputs:

```text
query_count
unique_qnames
nxdomain_count
nxdomain_ratio
avg_qname_length
max_qname_length
unique_tlds
a_count
aaaa_count
```

Controlled evaluation result:

```text
held-out benign: 8 windows -> 2 anomalous
controlled DGA:   6 windows -> 6 anomalous
```

### Rule-based Detection Engineering — next

The future behavioral hypothesis should evaluate the smallest evidence-backed combination of:

- NXDOMAIN count and ratio;
- total query rate;
- unique qnames;
- generated-name/domain length behavior;
- repeated client identity (`client_ip`);
- time-window behavior;
- query-type behavior where useful;
- ML result as a supporting comparison signal.

No rule threshold/window is locked yet.

**Status:** ML signal complete; rule-based detection pending.

## 7. SPL / Detection Logic

ML-specific support searches are implemented under [`ml/spl/`](ml/spl/) for:

- REST validation;
- dataset inventory;
- benign ground-truth review;
- one-minute feature engineering;
- DGA feature validation;
- ML result detail/summary.

The root [`spl/`](spl/) directory remains reserved for Detection Engineering:

```text
baseline.spl
hunting.spl
detection.spl
validation.spl
```

Required Detection Engineering order:

```text
baseline -> hunting -> initial detection -> controlled positive test
-> benign/false-positive test -> tune only if needed
-> final detection -> validation
```

**Status:** ML SPL complete; Detection Engineering SPL pending.

## 8. Alert

After final rule-based detection is stable, create an analyst-ready scheduled alert containing useful DNS evidence and, where appropriate, the ML result for the same client/window.

At minimum the analyst should be able to see:

- detection name/version;
- first/last time;
- client identity;
- query/NXDOMAIN counts and ratio;
- unique-name / length behavior;
- representative qnames/qtypes/results;
- ML prediction/score as supporting context;
- severity/rationale;
- raw-event drilldown.

**Status:** Pending.

## 9. AI Triage

Reuse the shared AI bridge only after stable Detection Engineering fields exist.

Keep the boundary clear:

```text
Isolation Forest = anomaly signal
LLM              = alert explanation / analyst assistance
Human analyst     = final security judgement
```

The ML model does not call OpenAI and neither ML nor the LLM authorizes containment.

**Status:** Scenario 02 AI mapping pending.

## 10. SOC Analysis

Build the official investigation from raw resolver events, rule-based detection, ML context and supporting telemetry.

The SOC Analyst should independently answer:

- which client produced the activity;
- how concentrated the queries were;
- how many names were unique;
- what NXDOMAIN ratio was observed;
- how generated-name characteristics differed from baseline;
- whether the ML signal agrees with raw evidence;
- what benign explanations remain;
- final disposition and confidence.

**Status:** Pending.

## 11. Incident Response

The reusable RPZ/sinkhole control is technically ready, but the official Scenario 02 response has **not** been performed.

Future response chain:

```text
Finding
  ↓
Human investigation
  ↓
Human-approved containment decision
  ↓
Enable approved RPZ response
  ↓
Victim resolves selected name/pattern to 10.50.30.30
  ↓
Sinkhole evidence appears
  ↓
Verify result
  ↓
Reset policy to safe state
```

Do not treat an ML anomaly, SPL result or AI summary as automatic response authorization.

**Status:** Pending.

## 12. Evidence

Already preserved in this repository:

- exact benign ML ground-truth windows;
- model-ready feature windows;
- Isolation Forest training evidence;
- controlled ML DGA ground truth;
- DGA feature shift;
- 6/6 DGA anomaly scoring;
- HEC write-back;
- final `dns_soc_ml` validation;
- selected setup/troubleshooting evidence;
- complete ML source code and supporting SPL.

See:

- [`ml/ML-ENGINEERING.md`](ml/ML-ENGINEERING.md)
- [`evidence/ml-engineering-validation.md`](evidence/ml-engineering-validation.md)
- [`screenshots/ml/`](screenshots/ml/)

Official scenario evidence still required later:

- Detection Engineering baseline/validation;
- official adversary ground truth after reveal;
- alert evidence;
- AI result;
- SOC investigation;
- approved response;
- before/after verification;
- reset and final comparison.

**Status:** ML evidence complete; official exercise evidence pending.

## 13. Containment

Containment is performed only after the human investigation reaches the approved response condition.

The ML component must never edit RPZ, block domains, isolate hosts or stop infrastructure automatically.

**Status:** Pending official exercise.

## 14. Verification

Infrastructure testing has already proven the reusable RPZ/sinkhole path, but official Scenario 02 verification must be repeated as part of the human-approved exercise.

Required official proof:

```text
Before response:
controlled suspicious name -> normal resolver outcome / NXDOMAIN

After approved response:
selected name/pattern -> RPZ -> 10.50.30.30 -> Nginx sinkhole

After reset:
policy returns to agreed safe state
```

**Status:** Infrastructure capability complete; official verification pending.

## 15. Results

### Completed ML Engineering result

```text
32 benign feature windows
24 training
8 held-out benign
2 held-out benign anomalies
6 controlled DGA windows
6/6 DGA anomalies
6 ML result events written to Splunk
```

This proves the ML engineering loop, not the full scenario outcome.

### Official Scenario 02 result

Pending Detection Engineering, live exercise, SOC/IR and verification.

## 16. MITRE ATT&CK Mapping

Primary mapping: **`T1568.002` — Dynamic Resolution: Domain Generation Algorithms**.

The controlled ML generator reproduced DGA-style observable behavior safely inside the owned lab namespace. The final scenario mapping will be confirmed again against the official exercise evidence.

**Status:** Primary mapping retained; official exercise evidence pending.

## 17. False Positives

The ML holdout already demonstrated that anomaly detection can flag benign windows:

```text
2 / 8 held-out benign windows -> ANOMALY
```

That observation must inform later Detection Engineering and analyst interpretation.

The rule-based detection still requires its own deliberate benign/false-positive tests. Record every threshold change and the evidence for it.

**Status:** ML limitation observed; Detection Engineering FP validation pending.

## 18. Lessons Learned

Completed ML lessons include:

- validate real telemetry before training;
- use controlled benign data rather than teaching “NXDOMAIN = attack”;
- keep feature rows inspectable in Splunk;
- use a temporal train/holdout split;
- preserve benign anomalies instead of hiding them;
- separate REST read and HEC write privileges;
- Splunk knowledge-object permissions matter to restricted REST consumers;
- validate Docker Compose before applying changes;
- keep ML separate from the LLM and human response path;
- return ML results to Splunk so analysts can correlate them with raw DNS evidence.

See [`ml/ML-ENGINEERING.md`](ml/ML-ENGINEERING.md) for the full engineering story.

**Status:** ML lessons complete; final scenario lessons pending.

## 19. Reproduction Instructions

### ML Engineering reproduction

Use the completed source under [`ml/`](ml/) in this order:

```text
validate resolver/Splunk path
-> validate restricted REST + HEC
-> generate controlled benign periods
-> validate feature rows
-> train Isolation Forest
-> generate controlled DGA period
-> score DGA windows
-> write results through HEC
-> validate dns_soc_ml
```

### Full Scenario 02 reproduction — future

```text
verify infrastructure + ML
-> Detection Engineering baseline/hunting/detection
-> freeze rule
-> official controlled DGA simulation
-> alert + ML comparison
-> AI triage
-> independent SOC investigation
-> human-approved RPZ containment
-> verify
-> reset
```

**Status:** ML reproduction path documented; full exercise pending.

## 20. Screenshots

ML screenshots are now curated under [`screenshots/ml/`](screenshots/ml/):

```text
core/            -> main successful engineering evidence
setup/           -> supporting setup/data-quality evidence
troubleshooting/ -> selected reusable problem/fix evidence
```

Do not mix the ML engineering screenshots with future official adversary/SOC/IR evidence. Those later stages should receive their own role/case folders when they exist.

**Status:** ML screenshot record complete; official exercise screenshots pending.

## Network & protocol view

- **Layer 7 DNS:** `qname`, `qtype`, `rcode`, generated-name structure, NXDOMAIN ratio and one-minute feature behavior;
- **Layer 4:** victim -> resolver UDP/TCP 53; HTTP 80 to sinkhole after future response;
- **Layer 3:** `10.50.30.20 -> 10.50.30.10`, then `10.50.30.20 -> 10.50.30.30` after approved containment; VPC Flow context where useful;
- **Endpoint:** victim identity is known; process context is added only if later telemetry really provides it;
- **Cloud:** AWS Resolver/Route 53/CloudTrail used only where they support the story;
- **Application follow-up:** sinkhole Nginx access proves redirected HTTP traffic after containment.

## Completion gate

**Infrastructure:** ✅ complete  
**Machine Learning Engineering:** ✅ complete  
**Scenario 02 full exercise:** ⏳ pending

The scenario is complete only after the team can defend:

**Official Simulation → Telemetry → Rule-Based Detection → Alert → ML Comparison → AI Assistance → Human Investigation → Response → Verification → Ground-Truth Comparison → Lessons Learned.**

---

<div align="center">

[🏠 Scenario Home](README.md) · [🧠 ML Engineering](ml/README.md) · [🏗️ Infrastructure](https://github.com/DNSentinel-Lab/DNS-Lab-Infrastructure) · [⬆ Back to top](#top)

<sub>DNSentinel Lab · Evidence-first DNS security engineering</sub>

</div>
