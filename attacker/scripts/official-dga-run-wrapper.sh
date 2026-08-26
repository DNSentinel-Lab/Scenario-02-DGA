#!/usr/bin/env bash
set -u

GEN="/opt/dns-soc-ml-generators/dga_dns.py"

echo "===== SCENARIO 02 OFFICIAL DGA RUN ====="
printf 'HOST: '; hostname
printf 'GENERATOR: %s\n' "$GEN"
printf 'GENERATOR_SHA256: '; sha256sum "$GEN" | awk '{print $1}'
DGA_RUN_START=$(date -u '+%Y-%m-%dT%H:%M:%SZ')
echo "DGA_RUN_START: $DGA_RUN_START"
cd "$(dirname "$GEN")" || exit 1
python3 "$(basename "$GEN")"
DGA_RC=$?
DGA_RUN_END=$(date -u '+%Y-%m-%dT%H:%M:%SZ')
echo "DGA_RUN_END: $DGA_RUN_END"
echo "GENERATOR_EXIT_CODE: $DGA_RC"
echo "===== OFFICIAL DGA RUN COMPLETE ====="
exit "$DGA_RC"
