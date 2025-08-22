# 一、datetime模块有date、time、datetime、timedelta等核心类
# datetime.date处理日期
# datetime.time处理时间
# datetime.datetime处理日期和时间
# timedelta处理时间间隔

#1、获取当前日期和时间
from datetime import datetime,date

now = datetime.now()   # 当前日期时间
print(now)

today = date.today()    # 当前日期
print(today)

current_time = datetime.now().time()  # 当前时间（需通过datetime获取）
print(current_time)


#输出内容
# 当前日期时间: 2025-02-22 22:00:05.031346
# 当前日期: 2025-02-22
# 当前时间: 22:00:05.112021



