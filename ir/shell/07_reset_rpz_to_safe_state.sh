#!/usr/bin/env bash
# Resolver: restore original safe/non-enforcing state after containment evidence is preserved.
sudo cp /root/dns-soc-rpz.conf.ir-backup /etc/unbound/unbound.conf.d/dns-soc-rpz.conf
sudo cp /etc/unbound/rpz/dns-soc.rpz.ir-backup /etc/unbound/rpz/dns-soc.rpz

sudo cat /etc/unbound/unbound.conf.d/dns-soc-rpz.conf
sudo tail -n 5 /etc/unbound/rpz/dns-soc.rpz
sudo unbound-checkconf
sudo systemctl restart unbound
sudo systemctl is-active unbound
sudo unbound-control flush ywvuacnec7gmul193uc.dga-test.soclab.abdul4rehman215.tech

# Victim: prove reset and normal DNS health.
dig @10.50.30.10 ywvuacnec7gmul193uc.dga-test.soclab.abdul4rehman215.tech A
dig @10.50.30.10 ssm.us-east-1.amazonaws.com A
