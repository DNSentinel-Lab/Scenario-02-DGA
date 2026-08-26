# Scenario 02 IR/Defender Command Ledger

This file records the commands/searches used during the Incident Responder / Defender phase. It deliberately includes successful checks, failed diagnostic attempts, and the fix that made RPZ enforcement work.

## Splunk validation sequence

1. Raw event presence — `spl/01_raw_dns_window_presence.spl`
2. Core DNS metrics — `spl/02_core_dns_metrics.spl`
3. One-minute windows — `spl/03_one_minute_validation.spl`
4. Raw qname examples — `spl/04_raw_qname_examples.spl`
5. Client scope — `spl/05_client_scope.spl`
6. Non-NXDOMAIN review — `spl/06_non_nxdomain_review.spl`
7. Endpoint/process telemetry availability — `spl/07_endpoint_telemetry_availability.spl`
8. Historical recurrence — `spl/08_historical_recurrence.spl`
9. Current activity — `spl/09_current_activity_check.spl`
10. Exact-qname before/after attempt — `spl/10_before_after_exact_qname_attempt.spl` (returned 0 because of field-format matching)
11. Substring before/after search — `spl/11_before_after_substring_match.spl` (successful)
12. Broad namespace fallback — `spl/12_namespace_broad_fallback.spl` (provided as fallback; not required once #11 succeeded)

## Resolver / victim / sinkhole sequence

- Preserve pre-containment NXDOMAIN with `dig`.
- Inspect RPZ safe state and validate `unbound-checkconf`.
- Back up RPZ files, add only `*.dga-test.soclab.abdul4rehman215.tech A 10.50.30.30`, and comment the safe override after explicit approval.
- Reload/restart Unbound and flush the selected qname.
- Diagnose `rpz-disabled` in journal output.
- Discover the `.ir-backup` config inside `/etc/unbound/unbound.conf.d/` still carried an active `rpz-action-override: disabled` directive.
- Move that backup to `/root/`, restart Unbound, and re-test.
- Prove the exact same qname now resolves to `10.50.30.30`.
- Verify the sinkhole service and normal DNS.
- Restore the backed-up safe RPZ state and prove the qname returns NXDOMAIN again.

See `shell/` for command files.
