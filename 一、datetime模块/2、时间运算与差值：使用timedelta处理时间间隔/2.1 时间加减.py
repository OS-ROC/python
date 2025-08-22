from datetime import timedelta,datetime

# 1.当前时间
now = datetime.now()
print("当前时间",now)

# 2，加5天
future = now + timedelta(days=5)
print("加五天：",future)

# 3.减4小时34分22秒
past = now - timedelta(hours=4,minutes=34,seconds=22)
print("减4小时34分22秒",past)


# 输出内容
# 当前时间 2025-08-22 13:30:41.103465
# 加五天： 2025-08-27 13:30:41.103465
# 减4小时34分22秒 2025-08-22 08:56:19.103465