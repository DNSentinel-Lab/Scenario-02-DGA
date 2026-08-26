# Scenario 02 — Master Evidence Index

This folder is the cross-role evidence map for the completed Scenario 02 case. Detailed evidence stays with the role that produced it; this page links the layers into one auditable chain.

## Engineering evidence

| Area | Evidence |
|---|---|
| ML Engineering | [`ml-engineering-validation.md`](ml-engineering-validation.md) |
| Detection Engineering | [`../detection-engineering/detection-engineering-validation.md`](../detection-engineering/detection-engineering-validation.md) |
| Detection validation CSV | [`detection-v1-validation-output.csv`](detection-v1-validation-output.csv) |
| Detection screenshots | [`../screenshots/detection-engineering/`](../screenshots/detection-engineering/) |
| ML screenshots | [`../screenshots/ml/`](../screenshots/ml/) |

## Official operator ground truth

| Evidence | Location |
|---|---|
| Official command / wrapper | [`../screenshots/attacker/01-official-dga-execution-command.png`](../screenshots/attacker/01-official-dga-execution-command.png) |
| Generator completion / timing | [`../screenshots/attacker/02-official-dga-generator-complete.png`](../screenshots/attacker/02-official-dga-generator-complete.png) |
| Ground-truth summary | [`../screenshots/attacker/03-official-dga-ground-truth-summary.png`](../screenshots/attacker/03-official-dga-ground-truth-summary.png) |
| Operator record | [`../attacker/ground-truth-template.md`](../attacker/ground-truth-template.md) |

## SOC investigation evidence

The curated SOC set is indexed in [`../soc/evidence/README.md`](../soc/evidence/README.md).

Flagship evidence chain:

```text
E01/E02  Detection hit + five windows
E03/E04  raw DNS + qname structure
E05      same-client baseline
E06/E07  historical recurrence
E08      ML second opinion
E09/E10  AI review + human validation
E11      non-NXDOMAIN review
E12      dashboard
E13      final resolver-visible scope
```

## Incident Response evidence

The curated IR set is indexed in [`../ir/evidence/README.md`](../ir/evidence/README.md).

Flagship containment chain:

```text
E02   independent core metrics
E04   qname examples
E08   recurrence
E10   pre-containment NXDOMAIN
E14   post-containment → 10.50.30.30
E17   end-to-end sinkhole HTTP 200
E18   unrelated DNS unaffected
E19   Splunk NXDOMAIN → NOERROR
E20   RPZ safe state restored
E21   post-reset NXDOMAIN
```

## Final comparison

The cross-role reveal and timing alignment are documented in [`../exercise/final-comparison.md`](../exercise/final-comparison.md).

## Evidence rule

A screenshot is included because it proves a claim. Backend chat/progress screenshots, repeated views, wrong-time-range checks, and minor syntax corrections are not part of the public case narrative.
