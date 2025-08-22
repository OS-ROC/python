# timedelta对象只有days、seconds、microseconds属性，
# 没有years、months、hours、minutes等属性


from datetime import datetime

dt1 = datetime(2025,8,22,13,22)
dt2 = datetime(2025,6,22,18,52)

delta = dt1 - dt2
print("时间差",delta)
print("天数差",delta.days)
print("秒数差",delta.seconds)


# 输出内容：
# 时间差 60 days, 18:30:00
# 天数差 60
# 秒数差 66600