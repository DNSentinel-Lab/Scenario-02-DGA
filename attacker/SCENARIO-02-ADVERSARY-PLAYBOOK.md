<a id="top"></a>

> 🧭 [Scenario 02](../README.md) › [Adversary / Operator](README.md) › **Scenario 02 Adversary Playbook — DGA + High NXDOMAIN**

<div align="center">

![Scenario](https://img.shields.io/badge/Scenario_02-COMPLETE-2EA44F?style=flat-square) ![Workspace](https://img.shields.io/badge/Workspace-Adversary_Operator-A855F7?style=flat-square) ![Document](https://img.shields.io/badge/Document-Evidence_Backed-D966FF?style=flat-square)

</div>

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%" alt="section divider" />

# 🧬 Scenario 02 Adversary Playbook — DGA + High NXDOMAIN

**Operator:** [Musfira](https://github.com/MUSFIRA-ZAFAR)  
**Status:** ✅ Used for the completed official Scenario 02 adversary execution  
**Perspective:** Project Lead / Adversary Operator  
**Source endpoint:** `dns-soc-victim01` / `10.50.30.20`  
**Resolver:** `dns-soc-resolver01` / `10.50.30.10`  
**Controlled namespace:** `dga-test.soclab.abdul4rehman215.tech`  
**MITRE ATT&CK:** `T1568.002 — Dynamic Resolution: Domain Generation Algorithms`  
**Cyber Kill Chain:** Command & Control

## 🎯 1. Adversary objective

Generate one fresh, believable DGA-style DNS pattern from the internal victim through its normal resolver path.

The operator is modeling this behavior:

```text
internal endpoint
      |
      | repeatedly generates candidate domain names
      v
system DNS
      |
      v
team-controlled resolver
      |
      v
mostly unsuccessful resolution behavior
```

The operator is **not** trying to satisfy a Splunk threshold. Detection v1.0 is frozen before execution and is not used as feedback during the run.

## 🔐 2. Exercise isolation

Scenario 02 uses:

```text
dns-soc-victim01
    |
    | DNS
    v
dns-soc-resolver01
```

Rules:

- no external Kali attacker is required for this scenario;
- execute only on project-owned lab infrastructure;
- use the existing DGA generator unchanged;
- do not inspect defender results during execution;
- keep exact timing, commands and ground truth private until reveal;
- do not change ML, Detection v1.0 or RPZ;
- run the official generator once and stop.

## 📌 3. Pre-run check

Preflight should validate only operator prerequisites:

```text
victim health
resolver path
system DNS configuration
UTC synchronization
existing generator path/content
RPZ safe state
ground-truth record readiness
```

Prefer opening the SSM session before SOC monitoring begins and leaving it idle until the privately selected execution time.

Do not generate DGA traffic during preflight.

## 🪪 4. Generator identity

Expected deployed generator:

```bash
/opt/dns-soc-ml-generators/dga_dns.py
```

Repository behavior:

```python
RUN_SECONDS = 300
SLEEP = (0.4, 1.0)
```

Each iteration creates a lowercase-alphanumeric label of 14–28 characters beneath:

```text
dga-test.soclab.abdul4rehman215.tech
```

and performs an A-record lookup using the host's normal `resolvectl` path.

Do not change these values for the official run.

## 🎬 5. Official execution wrapper

On `dns-soc-victim01`, use the verified path and preserve timing/hash metadata:

```bash
GEN="/opt/dns-soc-ml-generators/dga_dns.py"

echo "===== SCENARIO 02 OFFICIAL DGA RUN ====="
printf 'HOST: '; hostname
printf 'GENERATOR: %s\n' "$GEN"
printf 'GENERATOR_SHA256: '; sha256sum "$GEN" | awk '{print $1}'

DGA_RUN_START=$(date -u '+%Y-%m-%dT%H:%M:%SZ')
echo "DGA_RUN_START: $DGA_RUN_START"

cd "$(dirname "$GEN")"
python3 "$(basename "$GEN")"

DGA_RC=$?
DGA_RUN_END=$(date -u '+%Y-%m-%dT%H:%M:%SZ')

echo "DGA_RUN_END: $DGA_RUN_END"
echo "GENERATOR_EXIT_CODE: $DGA_RC"
echo "===== OFFICIAL DGA RUN COMPLETE ====="
```

Expected operator-side result:

- script starts and prints its own `DGA_RUN_START`;
- the terminal remains mostly quiet because per-query output is suppressed;
- after about five minutes the script prints `DGA_RUN_END`;
- wrapper prints `GENERATOR_EXIT_CODE: 0`.

![Official DGA execution](../screenshots/attacker/02-official-dga-generator-complete.png)

## 📌 6. Live-run discipline

While the Python process is active:

```text
DO NOT press Ctrl+C
DO NOT change the script
DO NOT increase query rate
DO NOT extend runtime
DO NOT run a second generator
DO NOT open Splunk
DO NOT inspect ML results
DO NOT check scheduled alerts
DO NOT inspect AI output
DO NOT change RPZ
```

Let the existing generator finish naturally.

## 🎬 7. Official run used

The completed official run used:

```text
host: dns-soc-victim01
generator: /opt/dns-soc-ml-generators/dga_dns.py
sha256: 1dc0ce32d964cd2e70981e502e341d6b4ee66934cc79ea188e69bd4e3f8f51c4
generator start: 2026-08-26T06:37:10.787620+00:00
generator end: 2026-08-26T06:42:11.129575+00:00
exit code: 0
```

The two earlier incorrect-path attempts did not execute `dga_dns.py` and are excluded from the official activity window.

## 🎭 8. Ground truth to preserve privately

Record:

- execution date;
- source host/IP;
- resolver path;
- generator path and SHA256;
- exact wrapper command;
- generator configuration as deployed;
- controlled namespace;
- UTC start and end;
- exit code;
- official screenshots;
- operator notes and any failures before the official run.

Use [`ground-truth-template.md`](ground-truth-template.md).

Do not use attacker-side ground truth as input to the SOC disposition.

## 🧾 9. Evidence interpretation

The generator suppresses per-query command output, so the attacker terminal does not contain every generated qname.

Therefore:

- **attacker evidence** proves generator identity, configuration, start/end and successful completion;
- **resolver/Splunk evidence** proves actual DNS qnames, counts, response codes and timing seen by the defender.

Do not fill attacker documentation with defender metrics before the reveal gate.

## 🔐 10. Stop conditions

Stop or abort before execution if:

- the victim or resolver is unhealthy;
- system DNS no longer points through the intended resolver path;
- the generator differs unexpectedly from the verified deployed version;
- RPZ is already enforcing an unapproved containment state;
- the action would leave the controlled namespace/infrastructure;
- platform health is degraded.

Once the correct official run starts, allow it to finish naturally unless safety or infrastructure integrity requires an emergency stop.

## 🎯 11. What success means from the adversary side

The operator succeeds when they can prove:

```text
correct victim
+ correct pre-deployed generator
+ controlled DGA namespace
+ real system DNS path
+ exact UTC start/end
+ clean process exit
+ preserved private evidence
```

Success does **not** require the defender alert to fire. Whether Detection v1.0 detects the run is a defender-side exercise outcome.

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%" alt="section divider" />

<div align="center">

**DNSentinel Scenario 02 · Evidence before verdict · Humans before automation**

[🏠 Scenario Home](../README.md) · [🧬 Adversary / Operator](README.md) · [⬆ Back to top](#top)

</div>

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=30,24,19,12,6&height=75&section=footer" width="100%" alt="DNSentinel Scenario 02 footer" />
