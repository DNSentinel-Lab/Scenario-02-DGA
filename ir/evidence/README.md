# Scenario 02 IR — Curated Evidence

This folder preserves the official E01–E21 Incident Response evidence chain.

## Validation

| Evidence | Purpose |
|---|---|
| E01 | raw DNS window presence |
| E02 | independently reproduced core DNS metrics |
| E03 | five one-minute windows |
| E04 | generated-looking qname examples |
| E05 | resolver-visible client scope |
| E06 | non-NXDOMAIN review |
| E07 | endpoint/process telemetry availability |
| E08 | historical recurrence |
| E09 | current-activity check |

## Containment and verification

| Evidence | Purpose |
|---|---|
| E10 | pre-containment NXDOMAIN |
| E11 | pre-change RPZ safe state |
| E12 | Scenario 02 RPZ rule staged |
| E13 | RPZ runtime activated |
| E14 | same qname redirected to `10.50.30.30` |
| E15 | sinkhole service health |
| E16 | sinkhole local HTTP 200 |
| E17 | victim-to-sinkhole HTTP 200 |
| E18 | unrelated DNS unaffected |
| E19 | Splunk before/after `NXDOMAIN → NOERROR` |
| E20 | RPZ safe state restored |
| E21 | post-reset qname returned to NXDOMAIN |

The source package manifest is retained as [`EVIDENCE-MANIFEST.csv`](EVIDENCE-MANIFEST.csv).
