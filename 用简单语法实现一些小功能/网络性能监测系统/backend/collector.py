import subprocess
import time
import requests
import re
from db import SessionLocal
from models import NetworkMetric
from config import TEST_URL

def ping_host(host):
    cmd = ["ping", "-n", "4", host]
    result = subprocess.run(
        cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
        text=True, encoding="gbk"
    )

    latency = None
    loss = None
    for line in result.stdout.splitlines():
        if "丢失" in line:
            match = re.search(r"\((\d+)%\s*丢失\)", line)
            if match: loss = int(match.group(1))
        if "平均" in line:
            match = re.search(r"平均\s*=\s*(\d+)ms", line)
            if match: latency = int(match.group(1))

    return {"host": host, "latency_ms": latency, "packet_loss_percent": loss}

def http_response_time(url=TEST_URL):
    start = time.time()
    try:
        requests.get(url, timeout=5)
        return round((time.time() - start) * 1000, 2)
    except requests.RequestException:
        return None

def save_metric(host, latency, loss, http_ms):
    db = SessionLocal()
    metric = NetworkMetric(
        host=host,
        latency_ms=latency,
        packet_loss_percent=loss,
        http_response_ms=http_ms
    )
    db.add(metric)
    db.commit()
    db.close()
