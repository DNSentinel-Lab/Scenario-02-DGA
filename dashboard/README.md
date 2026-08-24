<a id="top"></a>
<img src="https://capsule-render.vercel.app/api?type=soft&color=gradient&customColorList=6,12,19,24,30&height=135&section=header&text=%F0%9F%93%8A%20Dashboard%20Workspace&fontSize=28&fontColor=ffffff&animation=fadeIn&desc=Scenario%2002%20%E2%80%94%20DGA%20%2B%20High%20NXDOMAIN&descSize=14&descAlignY=68&descColor=D966FF" width="100%" alt="📊 Dashboard Workspace" />

<div align="center">

![Scenario](https://img.shields.io/badge/Scenario_02-Infrastructure_Ready-D29922?style=flat-square)
![Workspace](https://img.shields.io/badge/Workspace-Dashboard_Workspace-0A84FF?style=flat-square)

[🏠 Scenario Home](../README.md) · [🏗️ Shared Infrastructure](https://github.com/DNSentinel-Lab/DNS-Lab-Infrastructure) · [🗂️ All Scenario Repositories](https://github.com/orgs/DNSentinel-Lab/repositories)

</div>

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%" alt="section divider" />

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

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%" alt="section divider" />

<div align="center">

**DNSentinel Scenario 02 · DGA + High NXDOMAIN**

[🏠 Scenario Home](../README.md) · [🏗️ Infrastructure](https://github.com/DNSentinel-Lab/DNS-Lab-Infrastructure) · [⬆ Back to top](#top)

</div>

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,12,19,24,30&height=75&section=footer" width="100%" alt="footer" />
