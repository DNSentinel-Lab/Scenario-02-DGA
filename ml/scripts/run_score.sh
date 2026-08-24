#!/usr/bin/env bash
set -euo pipefail

: "${SPLUNK_ML_TOKEN:?Set SPLUNK_ML_TOKEN in your shell first}"

docker exec \
  -e SPLUNK_ML_TOKEN="$SPLUNK_ML_TOKEN" \
  dns-soc-ml \
  python -u /app/score_iforest.py 2>&1
