#!/usr/bin/env python3
"""
自动备份 - 备份文件和数据库
"""

import os
import shutil
import datetime
import subprocess

def backup_files(source_dir, backup_dir):
    """备份文件"""
    # 生成时间戳，用于唯一备份名称
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_name = f"backup_{timestamp}"  # 备份文件夹名称
    backup_path = os.path.join(backup_dir, backup_name)  # 完整备份路径
    
    try:
        # 创建备份目录
        os.makedirs(backup_path, exist_ok=True)
        
        # 检查源目录是否存在
        if os.path.exists(source_dir):
            # 复制整个目录
            shutil.copytree(source_dir, os.path.join(backup_path, "files"))
            print(f"✅ 备份成功: {backup_path}")
        else:
            print(f"⚠️ 源目录不存在: {source_dir}")
            
    except Exception as e:
        print(f"❌ 备份失败: {e}")

# 使用示例
if __name__ == "__main__":
    # 备份网站文件到临时目录
    backup_files("/var/www/html", "/tmp/backups")
