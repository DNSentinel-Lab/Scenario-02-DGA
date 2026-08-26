#!/usr/bin/env bash
# Wrong-host diagnostic (this was accidentally run on dns-soc-victim01 and correctly failed):
sudo cat /etc/unbound/unbound.conf.d/dns-soc-rpz.conf
sudo cat /etc/unbound/rpz/dns-soc.rpz
sudo grep -Rni "rpz-action-override\|zonefile\|dns-soc-rpz" /etc/unbound

# RPZ runtime diagnosis:
sudo journalctl -u unbound --since "3 minutes ago" --no-pager | grep -Ei "rpz|ywvuacnec7gmul193uc"
sudo grep -RniE 'rpz-action-override|rpz:|zonefile|rpz-log-name' /etc/unbound

# This exact command was attempted but this Unbound build cannot print the option and returned a fatal error:
sudo unbound-checkconf -o include

# Sinkhole reachability test when the sinkhole EC2 was off (expected connection failure at that moment):
curl -I http://10.50.30.30
curl http://10.50.30.30
