# AI and ML Validation

## ML
Model: `dns_iforest_v1`

All five latest investigated windows returned:
- `prediction = ANOMALY`
- `prediction_value = -1`

ML was used only as a **second opinion** after raw DNS validation.

## AI
AI summaries were reviewed only after the SOC understood the raw DNS, baseline, and timeline.

### Confirmed AI claims
- client IP
- query volume
- unique qname volume
- NXDOMAIN count/ratio
- long/highly variable qname structure
- possible DGA/high-NXDOMAIN interpretation

### Attribution correction
Where AI said the client "generated" queries, the SOC interpretation is:

> The resolver observed DNS queries attributed to `client_ip=10.50.30.20`.

### Not proven by DNS evidence
- initiating process
- malware family
- endpoint compromise
- user identity
- authorization status
- transport/process attribution beyond the DNS telemetry
