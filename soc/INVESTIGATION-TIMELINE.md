# Investigation Timeline

| Stage | Defender action | Result |
|---|---|---|
| Pre-flight | Confirmed Unbound reply telemetry in `dns_soc_dns` | Telemetry healthy |
| Live monitoring | Ran frozen Detection v1.0 | Initially no result; later alert condition matched |
| Alert triage | Summarized one-minute client windows | Five consecutive matches at 06:37–06:41 |
| Raw DNS validation | Opened exact-window Unbound replies | 418 replies in the five-minute window |
| Qname analysis | Measured uniqueness and first-label lengths | Long/highly variable labels and very high uniqueness |
| Baseline | Compared same client outside latest window | Latest activity far above average and p95 |
| Historical scope | Searched previous 24 hours | Multiple earlier matching clusters |
| ML | Reviewed `dns_soc_ml` | All five latest windows = `ANOMALY` |
| AI | Reviewed `dns_soc_ai` only after raw evidence | AI broadly matched the evidence and preserved attribution limits |
| Successful replies | Checked `rcode!="NXDOMAIN"` | Normal-looking AWS service names in visible successful set |
| Dashboard | Scoped Scenario 02 dashboard to exact client/window | 418 replies, 408 NXDOMAIN, 97.61%, 409 unique qnames, 5 ML anomalous windows |
| Final scope | Checked all matching clients in exact window | One resolver-visible client: `10.50.30.20` |
| SOC decision | Evidence-backed disposition | INCONCLUSIVE — escalation warranted |
