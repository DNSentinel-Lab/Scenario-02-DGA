<a id="top"></a>

<img src="https://capsule-render.vercel.app/api?type=soft&color=gradient&height=155&section=header&text=Exercise%20Control%20and%20Ground%20Truth&fontSize=30&fontColor=ffffff&animation=fadeIn&fontAlignY=38&desc=Scenario%2002%20-%20Realistic%20Information%20Separation%20to%20Decision%20Lock%20to%20Final%20Reveal&descSize=14&descAlignY=68" width="100%" alt="🎭 Exercise Control & Ground Truth" />

<div align="center">

![Scenario](https://img.shields.io/badge/Scenario_02-Closeout_Complete-2EA44F?style=flat-square)
![Exercise](https://img.shields.io/badge/Exercise-Information_Separated-A855F7?style=flat-square)
![Reveal](https://img.shields.io/badge/Ground_Truth-Revealed_After_Decisions-22D3EE?style=flat-square)

[🏠 Scenario Home](../README.md) · [🧬 Operator](../attacker/README.md) · [🔎 SOC](../soc/README.md) · [🛡️ IR](../ir/README.md) · [🧾 Evidence](../evidence/README.md)

</div>

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%" alt="section divider" />

# 🎭 Scenario 02 Exercise Closeout

This folder explains how the completed Scenario 02 exercise preserved realistic role separation and how private operator ground truth was compared with defender conclusions only after SOC and IR decisions were locked.

## 🧭 Information-Separation Model

```mermaid
flowchart LR
    O["🧬 Operator Ground Truth"] -. "hidden during investigation" .-> X["🔒 Reveal Gate"]
    D["🚨 Frozen Detection"] --> S["🔎 SOC Investigation"]
    S --> I["🛡️ IR Validation / Decision"]
    I --> L["✅ Decisions Locked"]
    O --> X
    L --> X
    X --> C["🎭 Final Comparison"]
```

> [!IMPORTANT]
> The operator did not use defender feedback to tune the official run. SOC and IR worked from defender-visible evidence, and private execution truth was compared only after their conclusions were recorded.

## 📚 Closeout Artifacts

| Artifact | Purpose |
|---|---|
| [`REALISTIC-EXERCISE-PROTOCOL.md`](REALISTIC-EXERCISE-PROTOCOL.md) | Information-separation rules, frozen-control rule and reveal gate |
| [`final-comparison.md`](final-comparison.md) | Operator vs telemetry vs Detection vs ML vs AI vs SOC vs IR comparison |
| [`../attacker/ground-truth-template.md`](../attacker/ground-truth-template.md) | Official private execution record revealed at closeout |
| [`../soc/SOC-TO-IR-HANDOFF.md`](../soc/SOC-TO-IR-HANDOFF.md) | Defender evidence handoff before ground-truth reveal |
| [`../ir/IR-FINAL-REPORT.md`](../ir/IR-FINAL-REPORT.md) | Independent IR closeout record |

## ✅ Why This Matters

The exercise tests more than whether a detection fires. It preserves the difference between **what actually happened**, **what the defender could observe**, **what automation suggested**, and **what humans could responsibly conclude from the evidence available to their role**.

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%" alt="section divider" />

<div align="center">

**Ground truth explains the exercise. Defender evidence earns the decision.**

[🏠 Scenario Home](../README.md) · [🎭 Final Comparison](final-comparison.md) · [⬆ Back to top](#top)

</div>

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=30,24,19,12,6&height=75&section=footer" width="100%" alt="DNSentinel Scenario 02 footer" />
