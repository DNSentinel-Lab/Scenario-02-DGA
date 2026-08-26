#!/usr/bin/env bash
# Resolver only. Run only after explicit human approval.
sudo cp /etc/unbound/unbound.conf.d/dns-soc-rpz.conf /etc/unbound/unbound.conf.d/dns-soc-rpz.conf.ir-backup
sudo cp /etc/unbound/rpz/dns-soc.rpz /etc/unbound/rpz/dns-soc.rpz.ir-backup

echo '*.dga-test.soclab.abdul4rehman215.tech A 10.50.30.30' | sudo tee -a /etc/unbound/rpz/dns-soc.rpz
sudo sed -i 's/^[[:space:]]*rpz-action-override:[[:space:]]*disabled/    # rpz-action-override: disabled/' /etc/unbound/unbound.conf.d/dns-soc-rpz.conf

sudo cat /etc/unbound/unbound.conf.d/dns-soc-rpz.conf
sudo tail -n 5 /etc/unbound/rpz/dns-soc.rpz
sudo unbound-checkconf
