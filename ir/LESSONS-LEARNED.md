# Scenario 02 IR — Lessons Learned

1. **Raw DNS evidence must be independently reproduced.** The 836 raw Unbound events represented query/reply logging; counting only `event_type="reply"` reproduced the 418-reply SOC metric.
2. **Do not over-attribute DNS.** Resolver logs proved abnormal DNS behavior and client scope, not process identity or malware.
3. **Contain the observed namespace, not the client IP.** The RPZ action was intentionally narrow: `*.dga-test.soclab.abdul4rehman215.tech` → `10.50.30.30`.
4. **Preserve before-state before policy change.** The same observed qname was saved as NXDOMAIN before RPZ enforcement.
5. **Backups inside an include directory can be live configuration.** In this lab, `dns-soc-rpz.conf.ir-backup` remained inside `/etc/unbound/unbound.conf.d/` and carried an active `rpz-action-override: disabled`. Journal logs showed `rpz-disabled` even though the main file was edited. Moving the backup to `/root/` and restarting Unbound resolved the issue.
6. **Use runtime logs to distinguish rule matching from enforcement.** `journalctl` proved the wildcard matched while enforcement remained disabled.
7. **A sinkhole redirect is not complete end-to-end proof if the sinkhole service is down.** The sinkhole EC2 had been off; after it was started, nginx was active on `10.50.30.30:80` and the victim received HTTP 200.
8. **Prove unrelated DNS still works.** `ssm.us-east-1.amazonaws.com` continued to resolve normally during and after containment.
9. **Splunk field formatting can break exact equality searches.** The exact qname filter returned zero, while a distinctive substring search found the before/after events and showed NXDOMAIN → NOERROR.
10. **Reset is part of containment.** The exercise ended only after the safe/non-enforcing RPZ state was restored and normal resolver behavior was re-proven.
