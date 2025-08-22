from datetime import datetime

dt = datetime.now()

print("星期几（0-6）：",dt.weekday())   # 返回0（周一）到6（周日）

print("星期几（1-7）：",dt.isoweekday())   # 返回1（周一）到7（周日）(Python 3.11+)

# 转换为中文星期几
weekday_cn = ["星期一","星期二","星期三","星期四","星期五","星期六","星期日"]

print(weekday_cn[dt.weekday()])




###总结
# date: 处理日期（年、月、日）
# time: 处理时间（时、分、秒、微秒）
# datetime: 处理日期+时间
# timedelta: 处理时间间隔
# strftime/strptime: 字符串与日期时间互相转换时区处理需结合
# timezone 或第三方库（如 pytz）