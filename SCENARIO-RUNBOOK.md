<a id="top"></a>

> 🧭 [Scenario 02](README.md) › **Scenario 02 Runbook — DGA + High NXDOMAIN Activity**

![Scenario](https://img.shields.io/badge/Scenario_02-Engineering_Ready-2EA44F?style=flat-square)
![Detection](https://img.shields.io/badge/Detection-v1.0-D966FF?style=flat-square)
![DNSentinel](https://img.shields.io/badge/DNSentinel-Technical_Record-7B2CBF?style=flat-square)

---

# Scenario 02 Runbook — DGA + High NXDOMAIN Activity

**Engineering status:** ✅ Infrastructure + ML Engineering + Detection Engineering + Dashboard + Scheduled Alert + Scenario AI integration complete  
**Official exercise status:** ⏳ Fresh adversary execution → independent SOC → IR → human-approved containment/verification pending  
**Primary MITRE ATT&CK:** `T1568.002` — Dynamic Resolution: Domain Generation Algorithms

This runbook separates **completed engineering validation** from the future information-separated Scenario 02 exercise. Controlled benign/DGA traffic used to train ML or validate Detection v1.0 is preserved as engineering evidence; it is **not** presented as the official adversary ground truth.

## 1. Objective

Generate harmless controlled DNS behavior that resembles domain-generation activity and determine whether the SOC can distinguish the pattern from ordinary DNS failure noise without reducing the logic to `NXDOMAIN = malicious`.

Engineering now proves that the lab can:

- observe real resolver behavior;
- establish a clean rule baseline;
- compare explainable Detection v1.0 with an independent Isolation Forest signal;
- operationalize the rule as a scheduled alert;
- preserve raw DNS drilldown;
- pass stable Scenario 02 evidence through the shared AI bridge;
- require human validation before any response.

**Status:** ✅ Engineering objective complete; official information-separated exercise pending.

## 2. Architecture

The implemented defender, ML, detection and AI paths are:

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
                              +--> Detection v1.0
                              |       |
                              |       +--> Scheduled Alert
                              |       |       |
                              |       |       +--> Triggered Alerts
                              |       |       +--> Shared AI Bridge
                              |       |               |
                              |       |               +--> OpenAI
                              |       |               +--> HEC -> dns_soc_ai
                              |       |
                              |       +--> Raw resolver-event drilldown
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
        +--> RPZ only when human-approved -> 10.50.30.30
                                           -> dns-soc-sinkhole01 / Nginx
                                           -> sinkhole UF -> dns_soc_web
```

Final infrastructure RPZ state remains safe: policy loaded, logging available, enforcement disabled until a human-approved response step.

**Status:** ✅ Engineering architecture complete.

## 3. Prerequisites

Already satisfied:

- shared AWS/Splunk/AI platform healthy;
- resolver/victim/sinkhole infrastructure built;
- Unbound query/reply telemetry searchable in `dns_soc_dns`;
- reply-side transaction semantics validated;
- core resolver fields validated;
- resolver ingestion latency measured;
- clean Detection Engineering baseline established from 32 known-benign one-minute/client windows;
- Scenario 02 Dashboard Studio investigation surface validated;
- Detection v1.0 frozen after controlled positive + benign testing;
- scheduled alert created and proven with a real trigger;
- raw-event drilldown validated;
- Isolation Forest v1 trained and written back to `dns_soc_ml`;
- Rule ↔ ML historical comparison validated;
- Scenario AI evidence contract validated;
- end-to-end alert → webhook → OpenAI → HEC → `dns_soc_ai` path validated;
- AI core DNS metrics independently checked against raw resolver evidence.

Still required immediately before the **official** exercise:

- reconfirm the resolver, Splunk, ML, alert and AI services are healthy;
- confirm Detection v1.0 remains frozen;
- Project Lead prepares fresh official adversary ground truth privately;
- SOC Analyst receives defender evidence only, not attacker timing/commands;
- Incident Responder remains independent until an IR handoff is justified;
- confirm RPZ remains disabled until human approval.

**Status:** ✅ Engineering prerequisites complete; ⏳ live exercise preflight pending.

## 4. Adversary Activity / Simulation

### Engineering traffic — complete

Scenario 02 used several controlled traffic sets for engineering purposes:

- two known-benign DNS periods for ML and rule-baseline work;
- one historical controlled DGA period for ML evaluation;
- fresh controlled DGA traffic for Detection Engineering positive validation;
- ordinary DNS, limited NXDOMAIN and burst-style benign traffic for false-positive testing;
- small final DGA runs to validate scheduled alert and AI integration.

Controlled DGA names remained inside the project-owned lab namespace. No malware was executed and no unrelated external target was attacked.

### Official Scenario 02 adversary execution — pending

The Project Lead / Adversary Operator will perform a **fresh** information-separated run after preflight. Exact commands/tooling, UTC start/end, generated pattern and ground truth remain private until the defender record is locked.

The official adversary is not instructed to cross the detection thresholds. A miss is a valid exercise result and must not be repaired by live tuning.

**Status:** ✅ Engineering simulation complete; ⏳ official adversary execution pending.

## 5. Telemetry

### Primary resolver source — validated

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

Primary Detection Engineering analytical side:

```text
event_type="reply"
1 minute / client_ip
```

This avoids counting one request twice and preserves the final DNS result.

### ML result source — validated

```text
index=dns_soc_ml
host=dns-soc-ml
source=isolation-forest
sourcetype=dns_soc:ml:iforest
```

Implemented result fields include:

```text
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

`anomaly_score` preserves the model's raw decision-function semantics; controlled anomalies were negative. It is not documented as a normalized threat score.

### AI result source — validated

```text
index=dns_soc_ai
source=dns-soc-ai-bridge
sourcetype=dns_soc:ai:triage
```

### Sinkhole application source — ready for future approved response

```text
index=dns_soc_web
host=dns-soc-sinkhole01
source=/var/log/nginx/access.log
sourcetype=nginx:access
```

Supporting AWS/cloud/network sources are used only where they contribute real evidence.

**Status:** ✅ Engineering telemetry paths validated; official run evidence pending.

## 6. Detection

### Clean rule baseline

Detection Engineering deliberately did not call mixed lab history “normal.” Two known-clean periods produced **32 one-minute/client windows**.

Observed benign maximums:

| Metric | Maximum |
|---|---:|
| `query_count` | 14 |
| `unique_qnames` | 10 |
| `unique_qname_ratio` | 1.00 |
| `nxdomain_count` | 5 |
| `nxdomain_ratio` | 0.50 |
| `max_qname_length` | 45 |

This invalidated weak ideas such as:

```text
NXDOMAIN alone = DGA
high uniqueness alone = DGA
long qname alone = DGA
```

### Detection v1.0 — frozen

```text
Scenario 02 - Possible DGA / High NXDOMAIN
version: 1.0
severity: medium
MITRE: T1568.002

1 minute / client_ip / event_type="reply"

query_count >= 20
AND unique_qnames >= 15
AND nxdomain_ratio >= 0.75
```

The final rule combines **volume + name breadth + failed-resolution behavior**. Qname length, qtypes and response context remain analyst evidence rather than mandatory conditions.

### Positive validation

A fresh controlled Detection Engineering DGA run produced six one-minute windows. All six crossed the candidate rule; observed windows were approximately:

```text
query_count        = 30–94
unique_qnames      = 30–91
unique_qname_ratio = 0.9681–1.0000
nxdomain_ratio     = 0.9574–1.0000
avg_qname_length   ≈ 56.97–59.80
max_qname_length   = 65
```

### Benign / false-positive validation

The **same unchanged rule** was challenged with:

- ordinary DNS lookups;
- limited benign NXDOMAIN activity;
- a repeated-name burst where caching reduced sensor-visible traffic;
- a unique legitimate-name burst that produced `23 queries / 23 unique names / 0.0 NXDOMAIN ratio` and stayed below the full rule.

### Isolation Forest — supporting second opinion

ML v1 results:

```text
held-out benign: 8 windows -> 2 anomalous
controlled DGA:   6 windows -> 6 anomalous
```

The model remains an anomaly signal, not the detection rule or incident verdict.

**Status:** ✅ Detection Engineering complete / v1.0 frozen for official exercise.

## 7. SPL / Detection Logic

Canonical Detection Engineering SPL is implemented at the repository root:

- [`spl/baseline.spl`](spl/baseline.spl) — known-clean one-minute/client baseline and summary;
- [`spl/hunting.spl`](spl/hunting.spl) — threshold-free behavior summary + raw resolver pivot;
- [`spl/detection.spl`](spl/detection.spl) — production Detection v1.0 and stable evidence contract;
- [`spl/validation.spl`](spl/validation.spl) — same frozen conditions with `WOULD DETECT` / `BELOW THRESHOLD` labels.

Exact supporting engineering searches are preserved under [`spl/engineering-validation/`](spl/engineering-validation/) for positive/benign tests, Rule ↔ ML correlation, scheduled-alert drilldown and AI validation.

ML-specific feature/training support SPL remains separately under [`ml/spl/`](ml/spl/).

**Status:** ✅ Complete.

## 8. Alert

Final scheduled alert:

```text
Name:          Scenario 02 - Possible DGA / High NXDOMAIN
Schedule:      * * * * *
Earliest:      -2m@m
Latest:        -1m@m
Trigger:       Number of Results > 0
Trigger mode:  Once
Severity:      Medium
Throttle:      Off during engineering validation
Actions:       Triggered Alerts + Webhook
Webhook:       internal dns-soc-ai-bridge path
```

Why the previous complete minute is searched:

```text
Unbound -> Universal Forwarder -> Splunk
median ≈ 2.389 s
p95    ≈ 9.195 s
max sample ≈ 9.196 s
```

This gives current resolver events time to arrive while keeping the one-minute behavioral unit clean.

A real scheduled trigger was validated. One detected minute contained approximately:

```text
client_ip          = 10.50.30.20
query_count        = 41
unique_qnames      = 37
unique_qname_ratio = 0.9024
nxdomain_count     = 36
nxdomain_ratio     = 0.8780
```

The alert is a **lead**, not a final incident verdict.

See [`spl/scheduled-alert.md`](spl/scheduled-alert.md).

**Status:** ✅ Complete and validated.

## 9. AI Triage

Scenario 02 reuses the existing shared AI bridge. No second Flask service, OpenAI integration, index or public port was created.

Scenario identity:

```text
scenario_id   = scenario-02-dga
scenario_name = DGA + High NXDOMAIN
ai_profile    = dga_nxdomain_v1
```

The final alert result provides the common bridge contract:

```text
alert_id
alert_name
scenario
severity
event_time
source
evidence_json
```

`evidence_json` carries stable Scenario 02 DNS evidence such as client, counts/ratios, qname-length context, qtypes, samples, Detection v1.0 metadata, MITRE and rationale.

### Integration troubleshooting that mattered

The first end-to-end webhook test returned HTTP 400. Transport was working; the result row did not yet satisfy the bridge schema. Lubaba fixed only the **result-contract layer**. Detection thresholds, Flask, Docker networking and ML stayed unchanged.

### Final validated path

```text
Detection v1.0
→ scheduled Splunk alert
→ internal webhook
→ dns-soc-ai-bridge
→ OpenAI
→ internal HEC
→ index=dns_soc_ai
```

The final AI event preserved `human_validation_required=true` and used cautious language rather than declaring malware/compromise as fact.

Most importantly, a separate raw DNS aggregation independently confirmed the AI's core metrics exactly:

```text
AI:  55 queries / 54 unique / 53 NXDOMAIN / ratio 0.9636
RAW: 55 queries / 54 unique / 53 NXDOMAIN / ratio 0.9636
```

See [`ai/scenario-02-ai-mapping.md`](ai/scenario-02-ai-mapping.md).

**Status:** ✅ Scenario 02 AI engineering path complete; official analyst comparison pending.

## 10. SOC Analysis

The official SOC investigation has **not** been performed.

Sonia will work from defender-visible evidence only:

```text
Alert
→ Scenario 02 Dashboard
→ Raw Unbound replies
→ Rule/ML context
→ AI triage validation
→ historical/context pivots as needed
→ independent disposition + confidence
→ IR handoff only if warranted
```

She is not given official attacker start time, generator details or intended outcome before her disposition is locked.

**Status:** ⏳ Pending official exercise.

## 11. Incident Response

The reusable RPZ/sinkhole control is technically ready, but the official Scenario 02 response has **not** been performed.

Future chain:

```text
Finding
  ↓
Independent SOC investigation
  ↓
IR validation
  ↓
Human-approved containment decision
  ↓
Enable approved RPZ response if warranted
  ↓
Selected name/pattern -> 10.50.30.30
  ↓
Sinkhole evidence
  ↓
Verify change
  ↓
Reset policy to safe state
```

Detection, ML and AI cannot authorize this step.

**Status:** ⏳ Pending official exercise.

## 12. Evidence

### Completed ML evidence

- controlled benign ground-truth windows;
- feature engineering;
- model training/holdout validation;
- controlled DGA ground truth;
- 6/6 DGA anomaly scoring;
- HEC write-back and `dns_soc_ml` validation.

See [`ml/ML-ENGINEERING.md`](ml/ML-ENGINEERING.md), [`evidence/ml-engineering-validation.md`](evidence/ml-engineering-validation.md) and [`screenshots/ml/`](screenshots/ml/).

### Completed Detection Engineering evidence

- resolver field/transaction validation;
- ingestion latency;
- clean baseline;
- final Dashboard Studio view;
- threshold-free hunt;
- fresh controlled positive detection;
- benign no-detection challenge;
- frozen Detection v1.0;
- reusable validation view;
- Rule ↔ ML comparison;
- real scheduled-alert trigger;
- raw resolver drilldown;
- AI evidence contract;
- `dns_soc_ai` result;
- final AI-vs-raw readiness check.

See [`detection-engineering/DETECTION-ENGINEERING.md`](detection-engineering/DETECTION-ENGINEERING.md), [`detection-engineering/detection-engineering-validation.md`](detection-engineering/detection-engineering-validation.md) and [`screenshots/detection-engineering/`](screenshots/detection-engineering/).

### Official exercise evidence still required

- fresh adversary ground truth after reveal;
- official alert/detection record;
- Sonia's independent SOC record;
- AI-vs-human comparison;
- IR decision;
- approved containment if warranted;
- before/after verification;
- reset proof;
- final ground-truth comparison and scenario lessons.

**Status:** ✅ Engineering evidence complete; ⏳ official exercise evidence pending.

## 13. Containment

Containment is performed only after the human investigation reaches the approved response condition.

The reusable RPZ/sinkhole path is already engineered and safe-state tested, but neither Detection v1.0, ML nor the LLM may edit RPZ, block domains, isolate hosts or stop infrastructure automatically.

**Status:** ⏳ Pending official exercise / human approval.

## 14. Verification

Infrastructure testing has proven the mechanism; official verification must still be repeated as part of the human-approved exercise.

Required official proof:

```text
Before response:
controlled suspicious behavior -> normal resolver outcome / NXDOMAIN

After approved response:
selected name/pattern -> RPZ -> 10.50.30.30 -> Nginx sinkhole

After reset:
policy returns to safe state
```

**Status:** ✅ reusable capability ready; ⏳ official before/after proof pending.

## 15. Results

### Machine Learning Engineering

```text
32 benign feature windows
24 training
8 held-out benign
2 held-out benign anomalies
6 controlled DGA windows
6/6 DGA anomalies
6 ML result events written to Splunk
```

### Detection Engineering

```text
32 clean rule-baseline windows
Detection v1.0 = query_count>=20 + unique_qnames>=15 + nxdomain_ratio>=0.75
6/6 fresh controlled DGA minutes detected
ordinary / limited-NXDOMAIN / legitimate-name benign challenges below full rule
6/6 historical controlled DGA windows = Rule DETECT + ML ANOMALY
scheduled alert = real trigger validated
Scenario AI contract = validated
AI -> dns_soc_ai = validated
AI core DNS metrics = exact raw-evidence match in final readiness test
```

These prove **engineering readiness**, not the final incident outcome.

### Official Scenario 02 result

Pending fresh adversary execution, independent SOC/IR, response/verification and ground-truth comparison.

## 16. MITRE ATT&CK Mapping

Primary mapping: **`T1568.002` — Dynamic Resolution: Domain Generation Algorithms**.

The controlled engineering generators reproduced DGA-style DNS behavior safely inside the owned lab namespace, and Detection v1.0 was designed specifically for the generated-name/high-NXDOMAIN pattern.

Do not over-map the final scenario. The official exercise will confirm that this remains the appropriate primary mapping for the behavior actually executed and observed.

**Status:** ✅ Engineering mapping validated; ⏳ official exercise confirmation pending.

## 17. False Positives

### ML limitation preserved

```text
2 / 8 held-out benign windows -> ANOMALY
```

This is why ML remains a second opinion.

### Rule-based validation complete

Detection v1.0 was challenged with the exact same conditions against:

- ordinary DNS;
- limited benign NXDOMAIN;
- burst activity affected by caching;
- unique legitimate-name burst (`23 queries / 23 unique / NXDOMAIN ratio 0.0`).

The last test is especially useful: high volume + high uniqueness alone did **not** satisfy the DGA rule because the failed-resolution dimension was absent.

**Status:** ✅ Detection Engineering false-positive validation complete; official live behavior may still reveal new edge cases.

## 18. Lessons Learned

### ML lessons

- validate real telemetry before training;
- train on controlled benign data;
- keep feature rows explainable;
- preserve benign anomalies rather than hiding model limits;
- separate Splunk read and HEC write privileges;
- return ML results to the analyst platform.

### Detection Engineering lessons

- count completed DNS transactions, not both query + reply events;
- contaminated lab history cannot be called a normal baseline;
- baseline can invalidate weak detection ideas before they reach production;
- DGA detection needs combined behavior rather than one indicator;
- validate what the **sensor observed**, not only what a generator attempted—caching matters;
- derived analytics must be correlated by the behavior-window time they describe;
- a saved alert is not complete until a real scheduled trigger is proven;
- successful network transport does not prove webhook payload compatibility;
- AI output is useful only when its claims can be checked against raw telemetry;
- protect known-good layers and change only the demonstrated failing boundary.

**Status:** ✅ Engineering lessons documented; final exercise lessons pending.

## 19. Reproduction Instructions

### ML Engineering

```text
validate resolver/Splunk path
-> validate restricted REST + HEC
-> generate controlled benign periods
-> build feature rows
-> train Isolation Forest
-> generate controlled DGA period
-> score DGA windows
-> write results through HEC
-> validate dns_soc_ml
```

### Detection Engineering

```text
validate resolver fields / reply semantics
-> measure ingestion latency
-> select known-clean baseline
-> build analyst dashboard
-> hunt without thresholds
-> derive candidate rule from evidence
-> fresh controlled DGA positive test
-> benign / false-positive challenges
-> freeze Detection v1.0
-> validation.spl
-> Rule ↔ ML comparison
-> scheduled alert + real trigger
-> raw-event drilldown
-> stable evidence contract
-> Scenario 02 shared-AI E2E validation
-> AI-vs-raw final check
```

### Official Scenario 02 exercise — next

```text
preflight + freeze engineering
-> fresh private adversary ground truth
-> detection/alert runs unchanged
-> AI assistance
-> independent SOC investigation
-> IR decision
-> human-approved RPZ/sinkhole if warranted
-> before/after verification
-> reset
-> ground-truth reveal + comparison
-> final scenario lessons
```

**Status:** ✅ engineering reproduction paths documented; ⏳ official exercise pending.

## 20. Screenshots

Curated engineering evidence is split by workstream:

```text
screenshots/
├── ml/
│   ├── core/
│   ├── setup/
│   └── troubleshooting/
└── detection-engineering/
    ├── 01-resolver-field-validation.png
    ├── ...
    ├── 14-detection-engineering-final-readiness.png
    ├── supporting/
    └── troubleshooting/
```

Detection Engineering screenshots tell one continuous engineering story from telemetry validation to final AI-vs-raw readiness.

Official adversary/SOC/IR screenshots must remain separate and will be added only after those stages actually occur.

**Status:** ✅ engineering screenshot record complete; ⏳ official exercise screenshots pending.

## Network & protocol view

- **Layer 7 — DNS:** `qname`, `qtype`, `rcode`, unique-name behavior, NXDOMAIN ratio, qname length and one-minute client behavior;
- **Layer 4:** victim → resolver UDP/TCP 53; HTTP 80 to sinkhole only after future approved response;
- **Layer 3:** `10.50.30.20 -> 10.50.30.10`; future approved containment may produce `10.50.30.20 -> 10.50.30.30`; VPC Flow context only where useful;
- **Endpoint/client:** `client_ip` identifies the resolver-visible client; process claims are added only if endpoint telemetry actually proves them;
- **Cloud:** AWS Resolver/Route 53/CloudTrail used only where they support a concrete investigation question;
- **Application follow-up:** Nginx sinkhole access becomes response-verification evidence after human-approved containment.

## Completion gate

**Infrastructure:** ✅ complete  
**Machine Learning Engineering:** ✅ complete — Musfira  
**Detection Engineering / Dashboard / Alert / Scenario AI:** ✅ complete — Lubaba  
**Official adversary execution:** ⏳ pending — Musfira  
**Independent SOC investigation:** ⏳ pending — Sonia  
**Independent IR / approved containment:** ⏳ pending — Abdul-Rehman  
**Final response verification / ground-truth comparison:** ⏳ pending

Scenario 02 is fully complete only after the team can defend:

**Official Simulation → Telemetry → Frozen Detection → Alert → ML Comparison → AI Assistance → Independent Human Investigation → Human-Approved Response → Verification → Ground-Truth Comparison → Lessons Learned.**

---

<div align="center">

[🏠 Scenario Home](README.md) · [🚦 Detection Engineering](detection-engineering/README.md) · [🧠 ML Engineering](ml/README.md) · [🤖 AI Mapping](ai/README.md) · [🏗️ Infrastructure](https://github.com/DNSentinel-Lab/DNS-Lab-Infrastructure) · [⬆ Back to top](#top)

<sub>DNSentinel Lab · Evidence-first DNS security engineering</sub>

</div>
