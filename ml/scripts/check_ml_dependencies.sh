#!/usr/bin/env bash
set -euo pipefail

docker exec -i dns-soc-ml python - <<'PY'
import requests
import sklearn
import joblib

print("requests:", requests.__version__)
print("sklearn:", sklearn.__version__)
print("joblib:", joblib.__version__)
print("ML dependencies: OK")
PY
