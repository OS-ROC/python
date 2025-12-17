from apscheduler.schedulers.blocking import BlockingScheduler
from collector import ping_host, http_response_time, save_metric
from config import MONITOR_HOSTS, TEST_URL, INTERVAL_MINUTES
from datetime import datetime

def collect_job():
    for host in MONITOR_HOSTS:
        ping_result = ping_host(host)
        http_ms = http_response_time(TEST_URL)
        save_metric(
            host=ping_result["host"],
            latency=ping_result["latency_ms"],
            loss=ping_result["packet_loss_percent"],
            http_ms=http_ms
        )
    print(f"[{datetime.now()}] 多主机数据已采集并入库")

if __name__ == "__main__":
    scheduler = BlockingScheduler()
    scheduler.add_job(collect_job, "interval", minutes=INTERVAL_MINUTES)
    print(f"定时采集已启动，每 {INTERVAL_MINUTES} 分钟采集一次")
    scheduler.start()
