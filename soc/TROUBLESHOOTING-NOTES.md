<a id="top"></a>

> 🧭 [Scenario 02](../README.md) › [SOC Analyst](README.md) › **Troubleshooting Notes**

<div align="center">

![Scenario](https://img.shields.io/badge/Scenario_02-COMPLETE-2EA44F?style=flat-square) ![Workspace](https://img.shields.io/badge/Workspace-SOC_Analyst-0284C7?style=flat-square) ![Document](https://img.shields.io/badge/Document-Evidence_Backed-D966FF?style=flat-square)

</div>

<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%" alt="section divider" />

# 💡 Troubleshooting Notes

## 📌 Incorrect time-range views
Several early screenshots used Last 24 hours / Last 60 minutes while the investigation required a narrow five-minute window. These are preserved in `screenshots_all/` but excluded from curated public evidence.

## 🔎 Baseline SPL error
The original baseline search attempted `round(avg(...),2)` directly inside `stats`. Splunk rejected that syntax.

Fix: calculate `avg(...)` in `stats`, then round the resulting fields with a later `eval`.

See:
- [`06_baseline_original_failed_test.spl`](spl/06_baseline_original_failed_test.spl)
- [`07_baseline_corrected.spl`](spl/07_baseline_corrected.spl)

## 🧠 Duplicate ML fields after `spath`
`dns_soc_ml` fields were already extracted. Running `spath` again caused duplicate multivalue display values.

Fix: remove `spath` and table the existing fields directly.

See:
- [`12_ml_spath_duplicate_test.spl`](spl/12_ml_spath_duplicate_test.spl)
- [`13_ml_clean_final.spl`](spl/13_ml_clean_final.spl)

## 🤖 Duplicate AI fields after `spath`
`dns_soc_ai` fields were already extracted. Running `spath` again produced duplicate multivalue display values.

Fix: remove `spath` and use `mvindex(...,0)` to normalize extracted multivalue fields in the clean table.

See:
- [`15_ai_spath_duplicate_test.spl`](spl/15_ai_spath_duplicate_test.spl)
- [`16_ai_summary_clean_final.spl`](spl/16_ai_summary_clean_final.spl)

## 💡 Public documentation recommendation
Keep troubleshooting/error screenshots in the full archive for reproducibility, but use only the curated evidence images for the GitHub case narrative.
<img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%" alt="section divider" />

<div align="center">

**DNSentinel Scenario 02 · Evidence before verdict · Humans before automation**

[🏠 Scenario Home](../README.md) · [🔎 SOC Analyst](README.md) · [⬆ Back to top](#top)

</div>

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=30,24,19,12,6&height=75&section=footer" width="100%" alt="DNSentinel Scenario 02 footer" />
