#!/usr/bin/env python3
"""
Port Scanner - Check open ports on server
端口扫描 - 检查服务器开放端口
"""

import socket  # 导入socket库，用于网络连接和端口扫描

def scan_ports(host, start_port, end_port):
    """扫描指定主机的端口范围"""
    # 打印扫描开始信息
    print(f"Scanning {host} ports {start_port}-{end_port}")
    
    # 创建一个空列表，用于存储发现的开放端口
    open_ports = []
    
    # 循环遍历指定范围内的每一个端口
    for port in range(start_port, end_port + 1):
        # 创建一个TCP socket对象
        # socket.AF_INET 表示使用IPv4地址族
        # socket.SOCK_STREAM 表示使用TCP协议（面向连接的可靠传输）
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # 设置连接超时时间为1秒，避免在关闭的端口上等待太久
        
        try:
            # 尝试连接到目标主机和端口
            # connect_ex()方法尝试建立TCP连接，但不会抛出异常，而是返回错误代码
            # 返回值为0表示连接成功，非0值表示连接失败（错误代码）
            result = sock.connect_ex((host, port))
            
            # 检查连接结果，如果返回0说明端口开放
            if result == 0:  # 0表示连接成功，端口开放
                open_ports.append(port)  # 将开放端口添加到列表中
                print(f"✅ Port {port} open")  # 打印端口开放信息
            
            # 关闭socket连接，释放系统资源
            sock.close()
            
        except Exception as e:
            # 如果扫描过程中发生任何异常，捕获并打印错误信息
            # 但不会停止扫描，会继续扫描下一个端口
            print(f"Error scanning port {port}: {e}")
    
    # 扫描完成后，打印汇总结果
    print(f"\nScan completed! Open ports: {open_ports}")

# 使用示例
if __name__ == "__main__":
    # 当脚本被直接运行时（不是被导入时），执行以下代码
    # 扫描本地主机的所有端口（从1到65535）
    scan_ports("localhost", 1, 65535)
