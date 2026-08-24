<a id="top"></a>
<img src="https://capsule-render.vercel.app/api?type=soft&color=gradient&customColorList=6,12,19,24,30&height=135&section=header&text=%F0%9F%94%8E%20SPL%20Workspace&fontSize=28&fontColor=ffffff&animation=fadeIn&desc=Scenario%2002%20%E2%80%94%20DGA%20%2B%20High%20NXDOMAIN&descSize=14&descAlignY=68&descColor=D966FF" width="100%" alt="🔎 SPL Workspace" />

<div align="center">

![Scenario](https://img.shields.io/badge/Scenario_02-Infrastructure_Ready-D29922?style=flat-square)
![Workspace](https://img.shields.io/badge/Workspace-SPL_Workspace-00B8D9?style=flat-square)

[🏠 Scenario Home](../README.md) · [🏗️ Shared Infrastructure](https://github.com/DNSentinel-Lab/DNS-Lab-Infrastructure) · [🗂️ All Scenario Repositories](https://github.com/orgs/DNSentinel-Lab/repositories)

</div>

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%" alt="section divider" />

**Status:** Planned — resolver fields are validated, but baseline/hunting/detection/validation searches have not been created for the scenario yet.

## Real input fields

Primary source:

```text
index=dns_soc_dns sourcetype=unbound:dns
```

Available persistent fields:

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

## Final file pattern

Create these only after real searches exist:

```text
spl/
├── baseline.spl
├── hunting.spl
├── detection.spl
└── validation.spl
```

## Required development order

```text
baseline
-> hunting
-> initial rule-based DGA detection
-> controlled positive test
-> minimal benign/false-positive test
-> tune only if evidence requires it
-> final detection
-> validation
```

Potential future features derived from `qname` can include label length, entropy/randomness and digit ratio, but they are not claimed as existing fields yet.

## Rules

- Final thresholds come from the lab baseline + controlled DGA/high-NXDOMAIN behavior.
- NXDOMAIN **ratio** matters in addition to raw count.
- Keep `client_ip` as a primary pivot.
- Test benign NXDOMAIN patterns deliberately.
- Keep rule-based detection independently useful even if ML is later added.
- Do not create placeholder `.spl` files just to make the repository look complete.

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%" alt="section divider" />

<div align="center">

**DNSentinel Scenario 02 · DGA + High NXDOMAIN**

[🏠 Scenario Home](../README.md) · [🏗️ Infrastructure](https://github.com/DNSentinel-Lab/DNS-Lab-Infrastructure) · [⬆ Back to top](#top)

</div>

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,12,19,24,30&height=75&section=footer" width="100%" alt="footer" />
