from flask import Flask, render_template, jsonify, request,send_file,make_response
from db import SessionLocal
from models import NetworkMetric
from config import MONITOR_HOSTS
import psutil
from datetime import datetime, timedelta
import json
from io import BytesIO

app = Flask(__name__, template_folder="../frontend/templates")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/network/<metric>")
def network_page(metric):
    if metric not in ["latency", "packetloss", "http"]:
        metric = "latency"
    return render_template("network.html", metric=metric, hosts=MONITOR_HOSTS)


@app.route("/logs")
def system_logs():
    db = SessionLocal()

    range_type = request.args.get("range", "30d")
    page = int(request.args.get("page", 1))
    per_page = 15

    now = datetime.utcnow()

    if range_type == "1h":
        start_time = now - timedelta(hours=1)
    elif range_type == "24h":
        start_time = now - timedelta(days=1)
    elif range_type == "7d":
        start_time = now - timedelta(days=7)
    else:
        start_time = now - timedelta(days=30)

    logs_query = db.query(NetworkMetric).filter(NetworkMetric.created_at >= start_time)
    total_logs = logs_query.count()
    logs = logs_query.order_by(NetworkMetric.created_at.desc())\
                     .offset((page - 1) * per_page)\
                     .limit(per_page)\
                     .all()

    db.close()

    LOCAL_OFFSET = timedelta(hours=8)
    for log in logs:
        log.created_at = log.created_at + LOCAL_OFFSET

    total_pages = (total_logs + per_page - 1) // per_page

    return render_template(
        "logs.html",
        logs=logs,
        current_range=range_type,
        current_page=page,
        total_pages=total_pages
    )

@app.route("/logs/download")
def download_logs():
    db = SessionLocal()

    # 获取区间参数，和分页页面参数无关
    range_type = request.args.get("range", "30d")

    now = datetime.utcnow()
    if range_type == "1h":
        start_time = now - timedelta(hours=1)
    elif range_type == "24h":
        start_time = now - timedelta(days=1)
    elif range_type == "7d":
        start_time = now - timedelta(days=7)
    else:  # 30d 或未知参数
        start_time = now - timedelta(days=30)

    logs = db.query(NetworkMetric).filter(NetworkMetric.created_at >= start_time)\
                                 .order_by(NetworkMetric.created_at.desc()).all()
    db.close()

    LOCAL_OFFSET = timedelta(hours=8)
    logs_data = []
    for log in logs:
        logs_data.append({
            "id": log.id,
            "host": log.host,
            "latency_ms": log.latency_ms,
            "packet_loss_percent": log.packet_loss_percent,
            "http_response_ms": log.http_response_ms,
            "created_at": (log.created_at + LOCAL_OFFSET).strftime("%Y-%m-%d %H:%M:%S")
        })

    # 将 JSON 写入内存
    json_bytes = BytesIO()
    json_bytes.write(json.dumps(logs_data, ensure_ascii=False, indent=2).encode("utf-8"))
    json_bytes.seek(0)

    # 返回文件下载
    return send_file(
        json_bytes,
        mimetype="application/json",
        as_attachment=True,
        download_name=f"system_logs_{range_type}.json"
    )

@app.route("/api/network_metrics")
def api_network_metrics():
    db = SessionLocal()
    metrics = db.query(NetworkMetric).filter(NetworkMetric.host.in_(MONITOR_HOSTS))\
        .order_by(NetworkMetric.created_at.desc()).limit(200).all()
    db.close()
    metrics.reverse()

    hosts = list({m.host for m in metrics})
    data_by_host = {h: {
        "latency_ms": [],
        "packet_loss_percent": [],
        "http": [],
        "created_at": []
    } for h in hosts}

    for m in metrics:
        h = m.host
        data_by_host[h]["latency_ms"].append(m.latency_ms or 0)
        data_by_host[h]["packet_loss_percent"].append(m.packet_loss_percent or 0)
        data_by_host[h]["http"].append(m.http_response_ms or 0)
        data_by_host[h]["created_at"].append(m.created_at.strftime("%Y-%m-%d %H:%M:%S"))

    for h in MONITOR_HOSTS:
        if h not in data_by_host:
            data_by_host[h] = {"latency_ms": [], "packet_loss_percent": [], "http": [], "created_at": []}

    return jsonify(data_by_host)


@app.route("/api/home_metrics")
def api_home_metrics():
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage("C:/")
    net_io = psutil.net_io_counters()

    total_traffic_mb = round((net_io.bytes_sent + net_io.bytes_recv) / 1024 / 1024, 2)

    return jsonify({
        "memory_percent": memory.percent,
        "disk_percent": disk.percent,
        "total_traffic_mb": total_traffic_mb,
        "memory_used": round(memory.used / 1024 / 1024, 2),
        "memory_total": round(memory.total / 1024 / 1024, 2),
        "disk_used": round(disk.used / 1024 / 1024 / 1024, 2),
        "disk_total": round(disk.total / 1024 / 1024 / 1024, 2),
        "net_sent_mb": round(net_io.bytes_sent / 1024 / 1024, 2),
        "net_recv_mb": round(net_io.bytes_recv / 1024 / 1024, 2)
    })


@app.route("/home_detail/<metric>")
def home_detail(metric):
    if metric not in ["memory", "disk", "traffic"]:
        metric = "memory"
    return render_template("home_detail.html", metric=metric)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
