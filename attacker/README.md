<a id="top"></a>
<img src="https://capsule-render.vercel.app/api?type=soft&color=gradient&customColorList=6,12,19,24,30&height=135&section=header&text=%F0%9F%A7%AC%20Adversary%20Workspace&fontSize=28&fontColor=ffffff&animation=fadeIn&desc=Scenario%2002%20%E2%80%94%20DGA%20%2B%20High%20NXDOMAIN&descSize=14&descAlignY=68&descColor=D966FF" width="100%" alt="🧬 Adversary Workspace" />

<div align="center">

![Scenario](https://img.shields.io/badge/Scenario_02-Execution_Complete-2EA44F?style=flat-square)
![Workspace](https://img.shields.io/badge/Workspace-Adversary_Workspace-A855F7?style=flat-square)

[🏠 Scenario Home](../README.md) · [🏗️ Shared Infrastructure](https://github.com/DNSentinel-Lab/DNS-Lab-Infrastructure) · [🗂️ All Scenario Repositories](https://github.com/orgs/DNSentinel-Lab/repositories)

</div>

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%" alt="section divider" />

**Role owner:** [Musfira](https://github.com/MUSFIRA-ZAFAR)  
**Status:** ✅ Official Scenario 02 adversary/operator execution complete  
**MITRE ATT&CK:** `T1568.002 — Dynamic Resolution: Domain Generation Algorithms`  
**Cyber Kill Chain:** Command & Control

This folder contains the Project Lead / Adversary Operator record for Scenario 02.

Unlike Scenario 01, Scenario 02 does **not** require an external attacker host. The controlled DGA behavior originates from the internal lab victim and follows the normal defender DNS path:

```text
dns-soc-victim01 / 10.50.30.20
        |
        | system DNS
        v
dns-soc-resolver01 / 10.50.30.10
        |
        v
normal upstream resolution
```

The purpose of the adversary role was to generate one fresh, believable DGA-style / high-NXDOMAIN pattern using the already-deployed Python generator while keeping execution timing and ground truth private from the SOC and IR roles until the reveal gate.

## 🗂️ Start here

- [`PROJECT-LEAD-ADVERSARY.md`](PROJECT-LEAD-ADVERSARY.md) — end-to-end adversary/operator story, execution logic and lessons.
- [`SCENARIO-02-ADVERSARY-PLAYBOOK.md`](SCENARIO-02-ADVERSARY-PLAYBOOK.md) — reproducible controlled DGA execution sequence and scope boundary.
- [`ground-truth-template.md`](ground-truth-template.md) — completed private execution record for the official run.

## 🔐 Exercise boundary

The operator used only project-owned AWS infrastructure and the pre-deployed generator on `dns-soc-victim01`.

The official execution rules were:

- use the existing generator unchanged;
- do not tune traffic to Detection v1.0 thresholds;
- do not modify ML;
- do not change RPZ/sinkhole policy during adversary execution;
- do not inspect Splunk, ML, AI or alert state to see whether the defender detected the activity;
- keep exact timing, command, namespace and attacker/operator notes private until the final reveal;
- stop after the one official run.

No malware, credential attack, persistence, denial of service, unrelated Internet targeting or destructive activity was part of this exercise.

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%" alt="section divider" />

<div align="center">

**DNSentinel Scenario 02 · DGA + High NXDOMAIN**

[🏠 Scenario Home](../README.md) · [🏗️ Infrastructure](https://github.com/DNSentinel-Lab/DNS-Lab-Infrastructure) · [⬆ Back to top](#top)

</div>

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=30,24,19,12,6&height=75&

## 🎭 Final reveal complete

SOC and IR decisions are now locked and the response/reset evidence has been preserved. The operator ground truth can therefore be compared safely with defender observations in [`../exercise/final-comparison.md`](../exercise/final-comparison.md).
<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%" alt="section divider" />

<div align="center">

**DNSentinel Scenario 02 · Evidence before verdict · Humans before automation**

[🏠 Scenario Home](../README.md) · [⬆ Back to top](#top)

</div>

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=30,24,19,12,6&height=75&section=footer" width="100%" alt="DNSentinel Scenario 02 footer" />
