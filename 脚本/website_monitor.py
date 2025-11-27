#!/usr/bin/env python3
"""
网站监控脚本 
功能：检查网站是否能正常访问
"""

import requests  # 导入requests库，用来发送HTTP请求,requests是Python最常用的HTTP请求库

# 要监控的网站列表
websites = [
    "https://www.baidu.com",
    "https://www.qq.com", 
    "http://localhost"
]

print("开始检查网站状态...")

for url in websites:
    try:
        # 发送请求(5秒超时)
        response = requests.get(url, timeout=5)
        
        # 检查状态码
        if response.status_code == 200:
            print(f"✅ {url} 正常")
        else:
            print(f"⚠️ {url} 异常 (状态码: {response.status_code})")
            
    except Exception as e:
        print(f"❌ {url} 连接失败: {e}")

print("检查完成")
