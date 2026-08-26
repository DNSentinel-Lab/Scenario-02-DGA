#!/usr/bin/env bash
# Run on dns-soc-sinkhole01.
hostname
ip -4 addr
sudo systemctl is-active nginx
sudo ss -lntp | grep ':80'
curl -I http://127.0.0.1
curl http://127.0.0.1

# If nginx is inactive, inspect only before changing service state:
sudo systemctl status nginx --no-pager
