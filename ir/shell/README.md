<a id="top"></a>

<img src="https://capsule-render.vercel.app/api?type=soft&color=gradient&customColorList=6,12,19,24,30&height=145&section=header&text=%F0%9F%A7%B0%20IR%20Shell%20%26%20RPZ%20Command%20Map&fontSize=30&fontColor=ffffff&animation=fadeIn&fontAlignY=38&desc=Scenario%2002%20%E2%80%94%20Inspect%20%E2%86%92%20Stage%20%E2%86%92%20Reload%20%E2%86%92%20Validate%20%E2%86%92%20Troubleshoot%20%E2%86%92%20Reset&descSize=14&descAlignY=68&descColor=F59E0B" width="100%" alt="🧰 IR Shell & RPZ Command Map" />

<div align="center">

![Commands](https://img.shields.io/badge/IR_Shell-01%E2%80%9308-F59E0B?style=flat-square)
![Control](https://img.shields.io/badge/DNS_Control-Unbound_RPZ-14B8A6?style=flat-square)
![Reset](https://img.shields.io/badge/Safe_State-Restored-2EA44F?style=flat-square)

[🏠 Scenario Home](../../README.md) · [🛡️ IR Workspace](../README.md) · [📖 Incident Response](../INCIDENT-RESPONSE.md) · [🔎 IR SPL](../spl/README.md)

</div>

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%" alt="section divider" />

# 🧰 IR Shell & RPZ Command Map

This folder preserves the exact defensive shell workflow used to inspect resolver state, stage the approved Scenario 02 RPZ control, validate the sinkhole path, troubleshoot one reusable configuration issue, and return the resolver to its safe state.

## 🧭 Command Flow

```mermaid
flowchart LR
    A["🔎 Inspect"] --> B["📸 Preserve Before-State"]
    B --> C["🛡️ Stage RPZ"]
    C --> D["♻️ Reload / Runtime Checks"]
    D --> E["🧯 Troubleshoot"]
    E --> F["✅ Validate Redirect"]
    F --> G["🎯 Verify Sinkhole"]
    G --> H["🌐 Safety Check"]
    H --> I["↩️ Reset"]
```

## 📋 Command Index

| File | Purpose |
|---|---|
| [`01_pre_containment_and_rpz_inspection.sh`](01_pre_containment_and_rpz_inspection.sh) | Inspect resolver / RPZ state and preserve pre-containment conditions |
| [`02_stage_scenario02_rpz.sh`](02_stage_scenario02_rpz.sh) | Stage the narrow Scenario 02 RPZ rule |
| [`03_reload_and_runtime_checks.sh`](03_reload_and_runtime_checks.sh) | Reload and verify runtime state |
| [`04_fix_backup_loaded_as_config.sh`](04_fix_backup_loaded_as_config.sh) | Preserve the reusable backup-file configuration troubleshooting fix |
| [`05_post_containment_validation.sh`](05_post_containment_validation.sh) | Validate post-containment DNS behavior |
| [`06_sinkhole_health_checks.sh`](06_sinkhole_health_checks.sh) | Verify sinkhole service and HTTP path |
| [`07_reset_rpz_to_safe_state.sh`](07_reset_rpz_to_safe_state.sh) | Restore the resolver's safe RPZ state |
| [`08_troubleshooting_commands_used.sh`](08_troubleshooting_commands_used.sh) | Preserve supplementary troubleshooting commands used during IR |

> [!IMPORTANT]
> These files document a **human-approved defensive response** in the project-owned lab. They are preserved for reproducibility; the command ledger and Incident Response narrative remain the authoritative decision record.

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%" alt="section divider" />

<div align="center">

[🛡️ IR Workspace](../README.md) · [📖 Command Ledger](../IR-COMMAND-LEDGER.md) · [⬆ Back to top](#top)

</div>

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=30,24,19,12,6&height=75&section=footer" width="100%" alt="DNSentinel Scenario 02 footer" />
