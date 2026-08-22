# SPL Workspace — Scenario 02 DGA + High NXDOMAIN Activity

**Status:** Planned — resolver fields are validated, but baseline/hunting/detection/validation searches have not been created for the scenario yet.

## Real input fields

Primary source:

```text
index=dns_soc_dns sourcetype=unbound:dns
```

Available persistent fields:

```text
event_type
client_ip
qname
qtype
rcode
response_time
cache_flag
response_size
```

## Final file pattern

Create these only after real searches exist:

```text
spl/
├── baseline.spl
├── hunting.spl
├── detection.spl
└── validation.spl
```

## Required development order

```text
baseline
-> hunting
-> initial rule-based DGA detection
-> controlled positive test
-> minimal benign/false-positive test
-> tune only if evidence requires it
-> final detection
-> validation
```

Potential future features derived from `qname` can include label length, entropy/randomness and digit ratio, but they are not claimed as existing fields yet.

## Rules

- Final thresholds come from the lab baseline + controlled DGA/high-NXDOMAIN behavior.
- NXDOMAIN **ratio** matters in addition to raw count.
- Keep `client_ip` as a primary pivot.
- Test benign NXDOMAIN patterns deliberately.
- Keep rule-based detection independently useful even if ML is later added.
- Do not create placeholder `.spl` files just to make the repository look complete.
