import os
import json
import requests
import urllib3
import joblib

from sklearn.ensemble import IsolationForest

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

SPLUNK_URL = "https://dns-soc-splunk:8089"
TOKEN = os.environ.get("SPLUNK_ML_TOKEN")

if not TOKEN:
    raise SystemExit("ERROR: SPLUNK_ML_TOKEN is not set inside dns-soc-ml")

FEATURES = [
    "query_count",
    "unique_qnames",
    "nxdomain_count",
    "nxdomain_ratio",
    "avg_qname_length",
    "max_qname_length",
    "unique_tlds",
    "a_count",
    "aaaa_count",
]

SEARCH = r'''
search index=dns_soc_dns client_ip="10.50.30.20" qname=* qtype=* rcode=*
| where
    (_time>=1787557606 AND _time<=1787558509)
    OR
    (_time>=1787559382 AND _time<=1787560288)
| eval qname_len=len(qname)
| eval tld=mvindex(split(rtrim(qname,"."),"."),-1)
| bin _time span=1m
| stats
    count as query_count
    dc(qname) as unique_qnames
    sum(eval(if(rcode="NXDOMAIN",1,0))) as nxdomain_count
    avg(qname_len) as avg_qname_length
    max(qname_len) as max_qname_length
    dc(tld) as unique_tlds
    sum(eval(if(qtype="A",1,0))) as a_count
    sum(eval(if(qtype="AAAA",1,0))) as aaaa_count
    by _time client_ip
| eval nxdomain_ratio=nxdomain_count/query_count
| table _time client_ip query_count unique_qnames nxdomain_count nxdomain_ratio avg_qname_length max_qname_length unique_tlds a_count aaaa_count
| sort _time
'''

resp = requests.post(
    f"{SPLUNK_URL}/servicesNS/dns_soc_ml_reader/search/search/v2/jobs/export",
    headers={"Authorization": f"Bearer {TOKEN}"},
    data={
        "search": SEARCH,
        "output_mode": "json",
    },
    verify=False,
    timeout=60,
)

resp.raise_for_status()

rows = []

for line in resp.text.splitlines():
    if not line.strip():
        continue

    obj = json.loads(line)
    result = obj.get("result")

    if not result:
        continue

    row = {
        "_time": result.get("_time"),
        "client_ip": result.get("client_ip"),
    }

    for field in FEATURES:
        row[field] = float(result[field])

    rows.append(row)

print(f"feature_rows={len(rows)}")

if len(rows) < 30:
    raise SystemExit(f"ERROR: expected >=30 feature rows, got {len(rows)}")

train_rows = rows[:24]
holdout_rows = rows[24:]

X_train = [[r[f] for f in FEATURES] for r in train_rows]
X_holdout = [[r[f] for f in FEATURES] for r in holdout_rows]

model = IsolationForest(
    n_estimators=200,
    contamination=0.10,
    random_state=42,
)

model.fit(X_train)

train_pred = model.predict(X_train)
holdout_pred = model.predict(X_holdout)

train_anomalies = sum(1 for x in train_pred if x == -1)
holdout_anomalies = sum(1 for x in holdout_pred if x == -1)

artifact = {
    "model": model,
    "features": FEATURES,
    "training_rows": len(train_rows),
    "holdout_rows": len(holdout_rows),
}

joblib.dump(artifact, "/app/dns_iforest_v1.joblib")

print(f"training_rows={len(train_rows)}")
print(f"holdout_rows={len(holdout_rows)}")
print(f"train_anomalies={train_anomalies}")
print(f"holdout_anomalies={holdout_anomalies}")
print("model_path=/app/dns_iforest_v1.joblib")
print("Isolation Forest training: OK")
