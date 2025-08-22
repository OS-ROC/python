from datetime import datetime,timezone,timedelta

# UTC时间
utc_time = datetime.now(timezone.utc)
print("UTC时间：",utc_time)

# 创建自定义时区（东八区）
tz_cst = timezone(timedelta(hours=+8))
local_time = datetime.now(tz_cst)
print("东八区时间：",local_time)