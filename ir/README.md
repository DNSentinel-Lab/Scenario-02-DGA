<a id="top"></a>

> 🧭 [Scenario 02](../README.md) › **Incident Response**

# Incident Response / Defender Workspace — Scenario 02

**Incident Responder / Defender:** Abdul-Rehman  
**Final IR status:** **CLOSED — controlled containment validated and safe reset completed**

This folder preserves the completed Incident Response phase that began from Sonia's formal SOC handoff. IR independently reproduced the critical DNS evidence before deciding whether the prepared RPZ/sinkhole response was justified.

## Start here

- [`INCIDENT-RESPONSE.md`](INCIDENT-RESPONSE.md) — flagship IR story
- [`IR-FINAL-REPORT.md`](IR-FINAL-REPORT.md) — concise final incident report
- [`IR-COMMAND-LEDGER.md`](IR-COMMAND-LEDGER.md) — exact investigation/response command ledger
- [`LESSONS-LEARNED.md`](LESSONS-LEARNED.md) — reusable operational lessons
- [`AI-AND-AUTOMATION-NOTE.md`](AI-AND-AUTOMATION-NOTE.md) — automation boundary
- [`spl/`](spl/) — exact IR Splunk searches
- [`shell/`](shell/) — resolver, victim, sinkhole, and reset commands
- [`evidence/`](evidence/) — curated E01–E21 response evidence

## IR at a glance

```text
SOC handoff
→ independently reproduce DNS metrics
→ verify qname structure and client scope
→ check endpoint/process visibility
→ confirm recurrence
→ classify what is / is not proven
→ explicit human approval
→ preserve pre-containment NXDOMAIN
→ enforce narrow RPZ
→ same qname → 10.50.30.30
→ verify sinkhole HTTP 200
→ prove unrelated DNS still works
→ prove Splunk before/after
→ restore safe RPZ state
→ same qname → NXDOMAIN
```

IR confirmed recurrent abnormal DGA-like/high-NXDOMAIN behavior. It did **not** claim malware, process identity, endpoint compromise, user identity, intent, or authorization when those facts were not present in defender telemetry.

---

[🏠 Scenario Home](../README.md) · [⬆ Back to top](#top)
