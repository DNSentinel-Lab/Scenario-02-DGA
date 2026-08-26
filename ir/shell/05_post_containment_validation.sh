#!/usr/bin/env bash
# Victim: same qname should now return 10.50.30.30.
dig @10.50.30.10 ywvuacnec7gmul193uc.dga-test.soclab.abdul4rehman215.tech A

# Normal DNS safety check.
dig @10.50.30.10 ssm.us-east-1.amazonaws.com A
# Optional additional normal-domain check.
dig @10.50.30.10 example.com A

# End-to-end sinkhole HTTP check.
curl -I http://10.50.30.30
curl http://10.50.30.30
