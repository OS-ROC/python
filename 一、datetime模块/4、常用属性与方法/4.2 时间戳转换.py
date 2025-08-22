# 时间戳转换：是指从1970年1月1日（通用协调时间）至当前时间的总秒数（或毫秒数、纳秒数等）。
# 它通常用于数据库、计算机系统以及网络通信中，以确保事件或数据的时间顺序和一致性。


from datetime import datetime

dt = datetime.now()

# timestamp() 方法将datetime对象转换为Unix时间戳
# Unix时间戳是从1970年1月1日00:00:00 UTC开始计算的秒数
timestamp = dt.timestamp()   # 获取时间戳
print("时间戳：",timestamp)


dt_form_ts = datetime.fromtimestamp(timestamp)
print("时间戳转日期时间：",dt_form_ts)




