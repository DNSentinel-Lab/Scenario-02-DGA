import os
import json
import requests
import urllib3
import joblib

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

SPLUNK_URL = "https://dns-soc-splunk:8089"
TOKEN = os.environ.get("SPLUNK_ML_TOKEN")

if not TOKEN:
    raise SystemExit("ERROR: SPLUNK_ML_TOKEN is not set")

artifact = joblib.load("/app/dns_iforest_v1.joblib")
model = artifact["model"]
FEATURES = artifact["features"]

SEARCH = r'''
search index=dns_soc_dns client_ip="10.50.30.20" qname=* qtype=* rcode=*
| where _time>=1787561668 AND _time<=1787561968
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

print(f"score_rows={len(rows)}")

if not rows:
    raise SystemExit("ERROR: no DGA feature rows returned")

X = [[r[f] for f in FEATURES] for r in rows]

predictions = model.predict(X)
scores = model.decision_function(X)

anomalies = 0

for row, pred, score in zip(rows, predictions, scores):
    label = "ANOMALY" if pred == -1 else "NORMAL"

    if pred == -1:
        anomalies += 1

    print(
        f"time={row['_time']} "
        f"client={row['client_ip']} "
        f"prediction={label} "
        f"score={score:.6f} "
        f"queries={int(row['query_count'])} "
        f"unique={int(row['unique_qnames'])} "
        f"nxdomain_ratio={row['nxdomain_ratio']:.4f} "
        f"avg_len={row['avg_qname_length']:.2f}"
    )

print(f"anomalies={anomalies}/{len(rows)}")
print("DGA scoring: OK")
