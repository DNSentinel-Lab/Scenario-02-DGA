import random
import string
import subprocess
import time
from datetime import datetime, timezone

RUN_SECONDS = 300
SLEEP = (0.4, 1.0)

def random_label():
    length = random.randint(14, 28)
    chars = string.ascii_lowercase + string.digits
    return "".join(random.choice(chars) for _ in range(length))

start = datetime.now(timezone.utc)
print(f"DGA_RUN_START={start.isoformat()}", flush=True)

end_at = time.time() + RUN_SECONDS

while time.time() < end_at:
    domain = f"{random_label()}.dga-test.soclab.abdul4rehman215.tech"

    subprocess.run(
        ["resolvectl", "query", "-t", "A", domain],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        timeout=10,
    )

    time.sleep(random.uniform(*SLEEP))

end = datetime.now(timezone.utc)
print(f"DGA_RUN_END={end.isoformat()}", flush=True)
