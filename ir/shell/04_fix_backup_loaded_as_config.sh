#!/usr/bin/env bash
# In this lab the backup .conf inside /etc/unbound/unbound.conf.d was still loaded,
# preserving rpz-action-override: disabled. Move it outside the include directory.
sudo grep -RniE 'rpz-action-override|rpz:|zonefile|rpz-log-name' /etc/unbound
sudo mv /etc/unbound/unbound.conf.d/dns-soc-rpz.conf.ir-backup /root/dns-soc-rpz.conf.ir-backup
sudo grep -RniE 'rpz-action-override|rpz:|zonefile|rpz-log-name' /etc/unbound
sudo unbound-checkconf
sudo systemctl restart unbound
sudo systemctl is-active unbound
sudo unbound-control flush ywvuacnec7gmul193uc.dga-test.soclab.abdul4rehman215.tech
