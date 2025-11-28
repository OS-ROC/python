#!/usr/bin/env python3
"""
Server Basic Information Check
检查服务器基础信息
"""

import os
import shutil
import psutil

print("=== Server Basic Information ===")

# CPU信息
print(f"CPU Cores: {psutil.cpu_count()}")  # 获取CPU核心数
print(f"CPU Usage: {psutil.cpu_percent(interval=1)}%")  # 获取CPU使用率(测量1秒)

# 内存信息  
memory = psutil.virtual_memory()  # 获取内存信息对象
print(f"Total Memory: {memory.total // 1024 // 1024} MB")  # 总内存(字节转MB)
print(f"Memory Usage: {memory.percent}%")  # 内存使用率百分比

# 磁盘信息
disk = shutil.disk_usage("/")  # 获取根目录磁盘使用情况
print(f"Total Disk: {disk.total // 1024 // 1024 // 1024} GB")  # 总磁盘空间(字节转GB)
print(f"Disk Usage: {(disk.used / disk.total) * 100:.1f}%")  # 磁盘使用率(保留1位小数)

# 系统负载(Linux系统专用)
if os.path.exists("/proc/loadavg"):  # 检查是否为Linux系统
    with open("/proc/loadavg", "r") as f:  # 打开负载文件
        load = f.read().split()[0:3]  # 读取并分割，取前3个负载值
    print(f"System Load: {', '.join(load)}")  # 输出1/5/15分钟平均负载
