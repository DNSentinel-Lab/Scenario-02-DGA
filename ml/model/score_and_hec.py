import os
import json
import requests
import urllib3
import joblib

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

SPLUNK_URL = "https://dns-soc-splunk:8089"
HEC_URL = "https://dns-soc-splunk:8088/services/collector/event"

REST_TOKEN = os.environ.get("SPLUNK_ML_TOKEN")
HEC_TOKEN = os.environ.get("SPLUNK_ML_HEC_TOKEN")

if not REST_TOKEN:
    raise SystemExit("ERROR: SPLUNK_ML_TOKEN missing")

if not HEC_TOKEN:
    raise SystemExit("ERROR: SPLUNK_ML_HEC_TOKEN missing")

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
    headers={"Authorization": f"Bearer {REST_TOKEN}"},
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

if not rows:
    raise SystemExit("ERROR: no score rows returned")

X = [[r[f] for f in FEATURES] for r in rows]
predictions = model.predict(X)
scores = model.decision_function(X)

sent = 0

for row, pred, score in zip(rows, predictions, scores):
    label = "ANOMALY" if pred == -1 else "NORMAL"

    event = {
        "event_type": "dns_ml_iforest_score",
        "model": "dns_iforest_v1",
        "scenario": "scenario_02_dga",
        "client_ip": row["client_ip"],
        "window_time": row["_time"],
        "prediction": label,
        "prediction_value": int(pred),
        "anomaly_score": float(score),
        "query_count": int(row["query_count"]),
        "unique_qnames": int(row["unique_qnames"]),
        "nxdomain_count": int(row["nxdomain_count"]),
        "nxdomain_ratio": float(row["nxdomain_ratio"]),
        "avg_qname_length": float(row["avg_qname_length"]),
        "max_qname_length": float(row["max_qname_length"]),
        "unique_tlds": int(row["unique_tlds"]),
        "a_count": int(row["a_count"]),
        "aaaa_count": int(row["aaaa_count"]),
    }

    payload = {
        "host": "dns-soc-ml",
        "source": "isolation-forest",
        "sourcetype": "dns_soc:ml:iforest",
        "index": "dns_soc_ml",
        "event": event,
    }

    r = requests.post(
        HEC_URL,
        headers={"Authorization": f"Splunk {HEC_TOKEN}"},
        json=payload,
        verify=False,
        timeout=15,
    )

    print(
        f"{row['_time']} "
        f"{label} "
        f"score={score:.6f} "
        f"HEC_HTTP={r.status_code}"
    )

    if r.status_code != 200:
        print("HEC_RESPONSE:", r.text)
        raise SystemExit("ERROR: HEC write failed")

    sent += 1

print(f"events_sent={sent}")
print("ML HEC write-back: OK")
