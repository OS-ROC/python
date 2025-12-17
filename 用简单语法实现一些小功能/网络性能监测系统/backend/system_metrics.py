import psutil

def get_system_metrics():
    # 内存占用
    mem = psutil.virtual_memory()
    mem_percent = mem.percent

    # 磁盘占用
    disk = psutil.disk_usage("/")
    disk_percent = disk.percent

    # 当月流量 (示例用总流量)
    net = psutil.net_io_counters()
    total_mb = (net.bytes_sent + net.bytes_recv) / 1024 / 1024

    return {
        "memory_percent": mem_percent,
        "disk_percent": disk_percent,
        "total_traffic_mb": round(total_mb, 2)
    }
