# Scenario 02 — DGA + High NXDOMAIN Activity

**Status:** Planned — requires Scenario 02 defender-DNS infrastructure before execution  
**Primary MITRE ATT&CK:** T1568.002 — Dynamic Resolution: Domain Generation Algorithms

## Objective

Generate harmless controlled DNS requests that resemble domain-generation behavior and determine whether the SOC can identify the pattern without treating every NXDOMAIN response as malicious.

## Infrastructure dependency

Before execution, deploy `dns-soc-resolver01` (`10.50.30.10`) and `dns-soc-victim01` (`10.50.30.20`) in `SOC-MONITORING-SUBNET`, create the minimum DNS/victim security controls, send resolver telemetry to Splunk, and establish the reusable sinkhole path around `10.50.30.30`.

The shared AWS/Splunk platform is not rebuilt inside this repository. Any new AWS resource is designed in the infrastructure project and documented there after it exists.

## Detection focus

- NXDOMAIN count and NXDOMAIN ratio over time;
- unique generated-name count and repeated client behavior;
- domain/label length and randomness features validated from real events;
- query rate by victim/client;
- process/client context when endpoint telemetry is actually available;
- normal baseline versus controlled generated-domain behavior;

## Network & protocol view

- Layer 7 DNS: generated names, NXDOMAIN/rcode, query type and label structure;
- Layer 4: client-to-resolver UDP/TCP 53;
- Layer 3: victim/resolver addressing and relevant flow context;
- Endpoint: victim identity/process context where collected;
- Containment: resolver answer/block/sinkhole before vs after;

DNS is Layer 7 evidence, but the scenario should correlate it with the Layer 3/4, endpoint, cloud or application evidence that actually helps prove the behavior.

## Planned dashboard

The dashboard should follow one shared time range and lead the analyst from summary → behavior → correlation → raw evidence.

- Shared time range plus victim/client, query-type and response filters;
- KPIs: total queries, NXDOMAIN count, NXDOMAIN ratio, unique names, active clients;
- Queries/NXDOMAIN ratio over time;
- Top generated names/parent patterns plus label-length/randomness views;
- Client behavior and resolver context;
- Before/after sinkhole or deny verification table;

See [`dashboard/README.md`](dashboard/README.md) for the planned layout.

## Team

| Role | Member |
|---|---|
| Project Lead / Attack Simulation | Musfira |
| SOC Analyst | Sonia |
| Detection Engineer | Lubaba |
| IR / Defender | Abdul-Rehman |

## Scenario workflow

This repository follows the common 20-part standard:

**Objective → Architecture → Prerequisites → Simulation → Telemetry → Detection → SPL → Alert → AI Triage → SOC Analysis → IR → Evidence → Containment → Verification → Results → MITRE → False Positives → Lessons → Reproduction → Screenshots.**

The working checklist is [`SCENARIO-RUNBOOK.md`](SCENARIO-RUNBOOK.md).

## Repository map

```text
.
├── README.md                 # scenario overview and locked design
├── SCENARIO-RUNBOOK.md       # 20-part execution/documentation checklist
├── dashboard/                # dashboard plan, later final XML/export
├── spl/                      # baseline, hunting, detection and validation SPL
├── ai/                       # scenario profile/payload mapping for shared AI bridge
├── ir/                       # response/containment/verification record
├── evidence/                 # structured ground truth and evidence notes
└── screenshots/              # curated visual evidence
```

The folders are prepared now, but fake implementation artifacts are not. Real `.spl`, dashboard XML, AI profiles and evidence are added only when they have been built and tested.

## Shared project references

- [DNS Lab Infrastructure](https://github.com/DNSentinel-Lab/DNS-Lab-Infrastructure) — shared AWS, DNS, Splunk and AI foundation
- [Scenario infrastructure roadmap](https://github.com/DNSentinel-Lab/DNS-Lab-Infrastructure/blob/main/00-project-design/scenario-infrastructure-roadmap.md) — future EC2/DNS/network changes owned by the infrastructure repository
- [Scenario documentation standard](https://github.com/DNSentinel-Lab/DNS-Lab-Infrastructure/blob/main/00-project-design/scenario-documentation-standard.md) — common 20-part SOC workflow, dashboard and evidence rules

## Completion condition

Resolver/victim telemetry is trusted, the detection distinguishes benign NXDOMAIN activity from the controlled DGA pattern, false positives are tested, AI and SOC conclusions are validated, and containment produces measurable before/after evidence.
