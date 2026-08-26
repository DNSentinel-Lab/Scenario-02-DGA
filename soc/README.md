<a id="top"></a>

> 🧭 [Scenario 02](../README.md) › **SOC Analyst**

# SOC Analyst Workspace — Scenario 02

**SOC Analyst:** Sonia  
**Scenario:** DGA + High NXDOMAIN  
**Final disposition:** **INCONCLUSIVE — escalation warranted**

This folder preserves the completed defender-side investigation. Sonia received defender telemetry rather than operator ground truth and worked from the frozen production detection back into raw resolver evidence before using ML or AI.

## Start here

- [`SOC-ANALYST-INVESTIGATION.md`](SOC-ANALYST-INVESTIGATION.md) — readable flagship investigation story
- [`SOC-ANALYST-PLAYBOOK.md`](SOC-ANALYST-PLAYBOOK.md) — detailed investigation workflow
- [`SOC-TO-IR-HANDOFF.md`](SOC-TO-IR-HANDOFF.md) — formal evidence handoff
- [`5W1H.md`](5W1H.md) — concise investigation framework
- [`AI-ML-VALIDATION.md`](AI-ML-VALIDATION.md) — human validation of automation
- [`INVESTIGATION-TIMELINE.md`](INVESTIGATION-TIMELINE.md) — defender timeline
- [`SPL-QUERY-INDEX.md`](SPL-QUERY-INDEX.md) — query map
- [`spl/`](spl/) — exact SPL used during the investigation
- [`evidence/`](evidence/) — curated official evidence

## Investigation at a glance

```text
Detection v1.0 hit
→ five consecutive one-minute windows
→ raw Unbound validation
→ qname-pattern measurement
→ same-client baseline
→ historical recurrence
→ ML second opinion
→ AI claim validation
→ 5W1H
→ INCONCLUSIVE — escalation warranted
→ IR handoff
```

### Exact latest cluster

```text
client:          10.50.30.20
window:          2026-08-26 06:37–06:41 UTC
DNS replies:     418
unique qnames:   409
NXDOMAIN:        408
NXDOMAIN ratio:  97.61%
ML:              five corresponding ANOMALY windows
```

The conclusion is intentionally narrower than “malware”: the DNS behavior was strongly abnormal, but the available telemetry did not prove the initiating process, malware, endpoint compromise, user identity, intent, or authorization.

---

[🏠 Scenario Home](../README.md) · [⬆ Back to top](#top)
