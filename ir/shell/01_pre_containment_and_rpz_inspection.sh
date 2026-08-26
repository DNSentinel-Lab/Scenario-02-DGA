#!/usr/bin/env bash
# Victim: preserve pre-containment result.
dig @10.50.30.10 ywvuacnec7gmul193uc.dga-test.soclab.abdul4rehman215.tech A

# Resolver: inspect current RPZ safe state.
sudo cat /etc/unbound/unbound.conf.d/dns-soc-rpz.conf
sudo cat /etc/unbound/rpz/dns-soc.rpz
sudo unbound-checkconf
