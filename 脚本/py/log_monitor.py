#!/usr/bin/env python3
"""
日志文件监控 - 发现关键词时告警
"""

import time

def monitor_log(file_path, keywords):
    """监控日志文件"""
    print(f"开始监控日志文件: {file_path}")
    
    try:
        # 初始定位到文件末尾
        with open(file_path, 'r') as file:
            file.seek(0, 2)  # 跳到文件末尾，忽略已有内容
        
        # 主监控循环
        while True:
            # 读取文件内容
            with open(file_path, 'r') as file:
                lines = file.readlines()
                
            # 检查最后10行
            for line in lines[-10:]:
                for keyword in keywords:
                    if keyword in line:
                        print(f"🚨 发现关键词: {keyword}")
                        print(f"   日志内容: {line.strip()}")
            
            time.sleep(5)  # 每5秒检查一次
            
    except FileNotFoundError:
        print(f"日志文件不存在: {file_path}")
    except KeyboardInterrupt:
        print("监控已停止")

# 使用示例
if __name__ == "__main__":
    # 监控nginx错误日志，查找错误关键词
    monitor_log("/var/log/nginx/error.log", ["error", "exception", "failed"])
