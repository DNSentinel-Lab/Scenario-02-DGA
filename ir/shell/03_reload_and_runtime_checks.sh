#!/usr/bin/env bash
sudo systemctl reload unbound
sudo systemctl is-active unbound
sudo journalctl -u unbound --since "2 minutes ago" --no-pager | tail -30

sudo unbound-control flush ywvuacnec7gmul193uc.dga-test.soclab.abdul4rehman215.tech
sudo unbound-control status
sudo journalctl -u unbound --since "3 minutes ago" --no-pager | grep -Ei "rpz|ywvuacnec7gmul193uc"
