from datetime import datetime

date_str = "2025-8-22 14:22:1"

dt = datetime.strptime(date_str,"%Y-%m-%d %H:%M:%S")

print("解析后的对象：",dt)