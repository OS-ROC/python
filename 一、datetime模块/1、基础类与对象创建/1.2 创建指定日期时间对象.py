#2. 创建指定日期/时间对象

from datetime import datetime,date,time

# 1.创建日期对象
d = date(2025,8,22)
print(type(d))    # 输出：<class 'datetime.date'>
print("指定日期：",d)

# 2.创建时间对象
t = time(13,20,23)
print(type(t))
print("指定时间：",t)

# 3.创建日期时间对象
dt = datetime(2025,8,22,13,22,45)
print(type(dt))
print("指定日期时间：",dt)


# 输出内容
# <class 'datetime.date'>
# 指定日期： 2025-08-22
# <class 'datetime.time'>
# 指定时间： 13:20:23
# <class 'datetime.datetime'>
# 指定日期时间： 2025-08-22 13:22:45