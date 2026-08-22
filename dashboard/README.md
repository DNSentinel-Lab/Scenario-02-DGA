# Dashboard Plan — Scenario 02 DGA + High NXDOMAIN Activity

**Status:** Planned — infrastructure telemetry and core resolver fields are ready; dashboard engineering has not started.

## Real data available

Primary resolver source:

```text
index=dns_soc_dns
host=dns-soc-resolver01
sourcetype=unbound:dns
```

Validated fields available now:

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

Private sinkhole evidence is also available through:

```text
index=dns_soc_web
host=dns-soc-sinkhole01
sourcetype=nginx:access
```

## Design goal

The dashboard is an investigation surface, not decoration. Every panel must answer a SOC question and use real project fields.

## Planned layout

- one shared **Time Range** input;
- filters for `client_ip`, `qtype`, `rcode` and domain/name where useful;
- KPIs: total queries, NXDOMAIN count, NXDOMAIN ratio, unique qnames, active clients;
- query/NXDOMAIN behavior over time;
- generated-name and label-length/randomness views after those derived features are validated;
- client/resolver behavior;
- sinkhole before/after response verification;
- analyst-ready investigation table with raw-event pivots.

## Quality rules

- Build the normal baseline before finalizing detection-oriented panels.
- Use actual fields, not a pre-labelled `classification="Suspicious"` shortcut.
- Do not invent entropy/randomness fields until the SPL that derives them has been tested.
- Prefer useful drilldowns to raw resolver evidence.
- Keep visual language consistent with the other scenario dashboards.
- Save final dashboard XML/export here only after it has been built and validated.

No dashboard artifact exists yet.
