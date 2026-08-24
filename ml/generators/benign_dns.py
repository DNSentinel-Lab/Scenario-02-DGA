import random
import subprocess
import time
from datetime import datetime, timezone

DOMAINS = [
    "example.com",
    "google.com",
    "ubuntu.com",
    "github.com",
    "python.org",
    "wikipedia.org",
    "cloudflare.com",
    "amazon.com",
    "microsoft.com",
    "ietf.org",
]

BENIGN_NX = [
    "benign-missing-01.soclab.abdul4rehman215.tech",
    "benign-missing-02.soclab.abdul4rehman215.tech",
]

RUN_SECONDS = 900
NORMAL_SLEEP = (3, 10)

start = datetime.now(timezone.utc)
print(f"BENIGN_RUN_START={start.isoformat()}", flush=True)

end_at = time.time() + RUN_SECONDS

while time.time() < end_at:
    if random.random() < 0.06:
        domain = random.choice(BENIGN_NX)
    else:
        domain = random.choice(DOMAINS)

    qtype = random.choice(["A", "AAAA"])

    subprocess.run(
        ["resolvectl", "query", "-t", qtype, domain],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        timeout=10,
    )

    time.sleep(random.uniform(*NORMAL_SLEEP))

end = datetime.now(timezone.utc)
print(f"BENIGN_RUN_END={end.isoformat()}", flush=True)
