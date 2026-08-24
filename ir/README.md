<a id="top"></a>
<img src="https://capsule-render.vercel.app/api?type=soft&color=gradient&customColorList=6,12,19,24,30&height=135&section=header&text=%F0%9F%9B%A1%EF%B8%8F%20Incident%20Response%20Workspace&fontSize=28&fontColor=ffffff&animation=fadeIn&desc=Scenario%2002%20%E2%80%94%20DGA%20%2B%20High%20NXDOMAIN&descSize=14&descAlignY=68&descColor=D966FF" width="100%" alt="🛡️ Incident Response Workspace" />

<div align="center">

![Scenario](https://img.shields.io/badge/Scenario_02-ML_Engineering_Complete-2EA44F?style=flat-square)
![Workspace](https://img.shields.io/badge/Workspace-Incident_Response_Workspace-E5534B?style=flat-square)

[🏠 Scenario Home](../README.md) · [🏗️ Shared Infrastructure](https://github.com/DNSentinel-Lab/DNS-Lab-Infrastructure) · [🗂️ All Scenario Repositories](https://github.com/orgs/DNSentinel-Lab/repositories)

</div>

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%" alt="section divider" />

**Status:** Reusable RPZ/sinkhole control is infrastructure-ready and ML Engineering is complete; the Scenario 02 IR exercise has not been performed.

The shared Infrastructure repository already proved that Unbound can log an RPZ match, redirect one controlled hostname to `10.50.30.30`, produce sinkhole Nginx evidence, and return to disabled enforcement afterward.

That technical validation is **not** the human Scenario 02 response record.

## Future response rule

```text
Finding
→ human SOC investigation
→ approved containment decision
→ enable approved RPZ response
→ expected DNS change
→ sinkhole/network evidence
→ verification
→ reset to safe state
```

Do not treat a rule-based detection, the implemented ML anomaly result, or a future AI summary as automatic authorization.

## Expected evidence later

- analyst-confirmed finding;
- who approved/performed containment;
- exact RPZ rule/pattern used for the scenario;
- pre-response DNS result;
- post-response `10.50.30.30` result;
- sinkhole access evidence;
- final reset and verification.

No Scenario 02 IR artifact exists here yet.

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%" alt="section divider" />

<div align="center">

**DNSentinel Scenario 02 · DGA + High NXDOMAIN**

[🏠 Scenario Home](../README.md) · [🏗️ Infrastructure](https://github.com/DNSentinel-Lab/DNS-Lab-Infrastructure) · [⬆ Back to top](#top)

</div>

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,12,19,24,30&height=75&section=footer" width="100%" alt="footer" />
