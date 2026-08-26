<a id="top"></a>

> 🧭 [Scenario 02](README.md) › **Runbook**

# Scenario 02 Runbook — DGA + High NXDOMAIN

**Scenario status:** ✅ Complete  
**Detection:** Detection v1.0 frozen before the official run  
**SOC disposition:** `INCONCLUSIVE — escalation warranted`  
**IR status:** `CLOSED — controlled containment validated and safe reset completed`

This runbook is the final operational record for Scenario 02. Engineering validation traffic is kept separate from the official information-separated execution. The official result is based on the fresh run that began at `2026-08-26T06:37:10.787620+00:00`.

---

## 1. Scenario objective

Detect and investigate DNS behavior characterized by:

- unusually high DNS volume;
- many unique qnames;
- rapidly changing/long first labels;
- high NXDOMAIN ratio;
- repeated one-minute anomalies from the same resolver-visible client;
- behavior consistent with DGA-style dynamic resolution.

Then determine whether the evidence justifies a human-approved DNS response and prove that response worked.

The scenario is deliberately scoped to DGA/high-NXDOMAIN DNS behavior. It does not claim malware execution, initial access, exploitation, credential theft, or endpoint compromise.

---

## 2. Roles

| Role | Owner | Responsibility |
|---|---|---|
| Project Lead / Adversary Operator | Musfira | pre-flight, one fresh DGA run, private ground truth |
| ML Engineer | Musfira | Isolation Forest baseline/model and live scoring support |
| Detection Engineer / AI Integrator | Lubaba | baseline, hunts, Detection v1.0, dashboard, alert, AI evidence path |
| SOC Analyst | Sonia | defender-only investigation, ML/AI validation, 5W1H, disposition, IR handoff |
| Incident Responder / Defender | Abdul-Rehman | independent validation, response decision, RPZ containment, verification, reset |

---

## 3. Network and telemetry path

```text
dns-soc-victim01        10.50.30.20
        ↓ system DNS
dns-soc-resolver01      10.50.30.10 / Unbound
        ↓
Splunk index=dns_soc_dns
        ├─ Detection v1.0
        ├─ dns_soc_ml
        └─ dns_soc_ai

Approved response only:
dns-soc-resolver01 / RPZ
        ↓
dns-soc-sinkhole01      10.50.30.30
```

Primary resolver evidence:

```text
index=dns_soc_dns
host=dns-soc-resolver01
sourcetype=unbound:dns
```

ML results:

```text
index=dns_soc_ml
sourcetype=dns_soc:ml:iforest
```

AI results:

```text
index=dns_soc_ai
```

---

## 4. Pre-flight gate — completed

Before operator traffic began, the Project Lead verified:

- victim host health;
- UTC/time readiness;
- victim system DNS path through `10.50.30.10`;
- deployed generator path/content;
- RPZ safe/non-enforcing state;
- private ground-truth record readiness.

The following were frozen before execution:

- Detection v1.0 thresholds;
- ML model/training artifact;
- Dashboard Studio investigation view;
- scheduled alert and AI profile;
- RPZ policy state.

---

## 5. Official adversary/operator execution — completed

Generator:

```text
/opt/dns-soc-ml-generators/dga_dns.py
```

SHA256:

```text
1dc0ce32d964cd2e70981e502e341d6b4ee66934cc79ea188e69bd4e3f8f51c4
```

Controlled namespace:

```text
<generated-label>.dga-test.soclab.abdul4rehman215.tech
```

Official generator timing:

```text
start: 2026-08-26T06:37:10.787620+00:00
end:   2026-08-26T06:42:11.129575+00:00
exit:  0
```

Rules for the official run:

- run once;
- do not change rate/duration based on detection thresholds;
- do not modify Detection v1.0;
- do not retrain ML;
- do not activate RPZ;
- do not inspect Splunk/ML/AI to steer the activity;
- keep ground truth private until defender decisions are locked.

Result: ✅ fresh five-minute DGA-style DNS behavior generated through the normal resolver path.

---

## 6. Detection v1.0 — frozen and triggered

Detection unit:

```text
1 minute × client_ip
```

Thresholds:

```text
query_count >= 20
unique_qnames >= 15
nxdomain_ratio >= 0.75
```

Official live result:

| UTC | Replies | Unique qnames | NXDOMAIN | Ratio | Result |
|---|---:|---:|---:|---:|---|
| 06:37 | 75 | 72 | 71 | 0.947 | MATCH |
| 06:38 | 87 | 86 | 85 | 0.977 | MATCH |
| 06:39 | 82 | 82 | 82 | 1.000 | MATCH |
| 06:40 | 85 | 84 | 83 | 0.976 | MATCH |
| 06:41 | 89 | 87 | 87 | 0.978 | MATCH |

Result: ✅ five consecutive production-rule matches without live tuning.

Canonical SPL is preserved in [`spl/detection.spl`](spl/detection.spl).

---

## 7. ML second opinion — completed

The Isolation Forest was trained from normal DNS behavior before the official exercise. It was not retrained against the official DGA run.

During closeout/pre-flight, live scoring was operationalized so the previous completed minute could be scored automatically and written to `dns_soc_ml` without manually pasting tokens each time. See [`ml/operations/README.md`](ml/operations/README.md).

Official SOC result:

```text
06:37  ANOMALY
06:38  ANOMALY
06:39  ANOMALY
06:40  ANOMALY
06:41  ANOMALY
```

Boundary:

> ML says the window differs from the learned baseline. It does not prove maliciousness or authorize response.

---

## 8. AI assistance — completed

The `dga_nxdomain_v1` path received structured defender evidence after the detection pipeline was built.

SOC used AI only after understanding raw DNS evidence. Important AI claims were checked against Splunk rather than accepted as ground truth.

Boundary:

> AI summarizes and prioritizes evidence; human analysts retain the final judgement and response authority.

See [`ai/scenario-02-ai-mapping.md`](ai/scenario-02-ai-mapping.md) and [`soc/AI-ML-VALIDATION.md`](soc/AI-ML-VALIDATION.md).

---

## 9. SOC investigation — completed

Sonia's investigation sequence:

1. confirm live resolver telemetry;
2. verify the frozen detection hit;
3. view all five one-minute windows;
4. inspect raw Unbound replies;
5. measure qname structure;
6. compare `10.50.30.20` with its historical baseline;
7. inspect 24-hour detection recurrence/clusters;
8. use ML as a second opinion;
9. inspect AI only after raw evidence;
10. challenge AI statements against Splunk;
11. review successful/non-NXDOMAIN names;
12. use Dashboard Studio for exact-window investigation;
13. confirm final resolver-visible client scope;
14. complete 5W1H and disposition;
15. hand off to IR.

Exact five-minute SOC metrics:

```text
418 replies
409 unique qnames
408 NXDOMAIN
97.61% NXDOMAIN
client_ip=10.50.30.20
```

Historical comparison showed the official windows were far above normal behavior for the same client, and matching behavior had recurred across earlier clusters.

SOC disposition:

> **INCONCLUSIVE — escalation warranted**

Confidence was high that abnormal DGA-like/high-NXDOMAIN behavior occurred, but process identity, malware identity, endpoint compromise, user identity, intent, and authorization remained unproven.

See [`soc/SOC-ANALYST-INVESTIGATION.md`](soc/SOC-ANALYST-INVESTIGATION.md).

---

## 10. SOC → IR handoff — completed

The handoff preserved:

- alert identity;
- exact investigated UTC window;
- resolver-visible client;
- raw DNS metrics;
- qname examples and generated-looking structure;
- baseline and recurrence findings;
- ML assessment;
- AI validation;
- MITRE context;
- 5W1H;
- SOC disposition/confidence;
- explicit unknowns.

Operator ground truth was not required for the defender handoff.

See [`soc/SOC-TO-IR-HANDOFF.md`](soc/SOC-TO-IR-HANDOFF.md).

---

## 11. IR independent validation — completed

Abdul-Rehman independently reproduced the critical SOC evidence rather than copying the handoff conclusion.

IR confirmed:

- 418 DNS reply events;
- 409 unique qnames;
- 408 NXDOMAIN responses;
- 97.61% NXDOMAIN;
- five consecutive matching one-minute windows;
- generated-looking first-label structure under the Scenario 02 namespace;
- one resolver-visible client in the exact cluster;
- historical recurrence;
- no successful resolution of generated-looking Scenario 02 qnames in the investigated cluster;
- no endpoint/process telemetry suitable for responsible process attribution.

IR classification:

> **Confirmed recurrent abnormal DGA-like / high-NXDOMAIN DNS behavior.**

Attribution remained limited to resolver-visible behavior.

---

## 12. Response decision and approval — completed

Containment was not automatic.

After independent validation, a human-approved narrow response was selected:

```text
*.dga-test.soclab.abdul4rehman215.tech
        →
10.50.30.30
```

Approver: Abdul-Rehman, explicit approval before policy change.

The exact separate wall-clock approval timestamp was not preserved and must not be invented.

The response targeted the observed namespace, not all DNS from `10.50.30.20`.

---

## 13. Pre-containment proof — completed

Observed qname used as the control:

```text
ywvuacnec7gmul193uc.dga-test.soclab.abdul4rehman215.tech
```

Before RPZ enforcement:

```text
resolver: 10.50.30.10
result:   NXDOMAIN
```

Evidence: [`ir/evidence/S02-IR-E10-PreContainment-NXDOMAIN.png`](ir/evidence/S02-IR-E10-PreContainment-NXDOMAIN.png)

---

## 14. RPZ containment — completed

The Scenario 02 wildcard was staged in the existing Unbound RPZ zone and the safe override was changed only after approval.

A useful operational issue was discovered during enforcement: a `.ir-backup` file had been left inside `/etc/unbound/unbound.conf.d/`. Because the directory is actively included by Unbound, the backup still carried `rpz-action-override: disabled`. Runtime logs showed `rpz-disabled` even though the primary file looked correct.

The backup was moved outside the active include directory, Unbound was restarted, and enforcement was re-tested.

After enforcement, the **same qname** returned:

```text
NOERROR
A 10.50.30.30
```

Evidence: [`ir/evidence/S02-IR-E14-PostContainment-RPZ-Redirect.png`](ir/evidence/S02-IR-E14-PostContainment-RPZ-Redirect.png)

---

## 15. Response verification — completed

IR verified all three required layers:

### Redirect

The selected Scenario 02 qname returned `10.50.30.30` through the normal resolver.

### Sinkhole service

`dns-soc-sinkhole01` was brought online and Nginx served the controlled sinkhole page. The victim received HTTP `200`.

### Unrelated DNS safety

Normal AWS DNS, including `ssm.us-east-1.amazonaws.com`, continued to resolve to its normal public AWS address.

### Splunk before/after

Resolver telemetry preserved the same qname changing from:

```text
NXDOMAIN
→
NOERROR
```

This proved the response changed observable DNS behavior rather than merely changing a configuration file.

---

## 16. Safe reset — completed

After response evidence was captured:

- RPZ was restored to the documented safe/non-enforcing state;
- the Scenario 02 wildcard was removed from active enforcement;
- Unbound configuration validated successfully;
- Unbound remained active;
- the selected qname returned to `NXDOMAIN`;
- unrelated AWS DNS remained healthy.

Reset is part of the response lifecycle, not an optional cleanup step.

---

## 17. Final ground-truth comparison — completed

After SOC and IR decisions were locked, operator ground truth was compared with defender evidence.

The official generator began at `06:37:10.787620 UTC`; raw resolver events and the first detection window begin in the same period. The generator ended at `06:42:11.129575 UTC`, after five consecutive detection windows had been observed.

The comparison confirms that the defender pipeline observed the fresh authorized DGA execution without using private operator timing or intended outcome during SOC/IR decision-making.

See [`exercise/final-comparison.md`](exercise/final-comparison.md).

---

## 18. Final result

```text
Official DGA execution        ✅
Resolver telemetry            ✅
Detection v1.0                ✅ five consecutive live matches
Isolation Forest              ✅ five corresponding anomalies
AI assistance                 ✅ reviewed and human-validated
SOC investigation             ✅ completed
SOC disposition               INCONCLUSIVE — escalation warranted
IR independent validation     ✅ completed
Human approval                ✅ before RPZ change
RPZ redirect                  ✅ same qname → 10.50.30.30
Sinkhole HTTP                 ✅ 200
Normal DNS                    ✅ unaffected
Splunk before/after           ✅ NXDOMAIN → NOERROR
Safe reset                    ✅ selected qname → NXDOMAIN again
Scenario closeout             ✅ complete
```

---

## 19. Evidence and reproducibility

- Detection Engineering SPL: [`spl/`](spl/)
- ML source/artifacts: [`ml/`](ml/)
- SOC queries and evidence: [`soc/`](soc/)
- IR SPL, shell ledger, and evidence: [`ir/`](ir/)
- Operator record: [`attacker/`](attacker/)
- Master evidence index: [`evidence/README.md`](evidence/README.md)

---

## 20. Final documentation boundary

This repository claims only what the evidence supports.

It does **not** claim:

- confirmed malware execution;
- a proven endpoint process;
- a proven user;
- endpoint compromise;
- malicious intent established by DNS alone;
- an invented human-approval timestamp.

It does document a complete, realistic defensive workflow from fresh DNS behavior through verified containment and reset.

---

[⬆ Back to top](#top)
