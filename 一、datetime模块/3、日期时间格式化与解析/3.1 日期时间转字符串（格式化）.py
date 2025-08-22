# 使用 strftime() 和 strptime() 进行字符串转换。

from datetime import datetime

dt = datetime.now()

# 格式化为字符串
formatted = dt.strftime("%Y-%m-%d %H:%M:%S")
print("格式化后：",formatted)

# 自定义格式
custom_format = dt.strftime("%A %d %B %Y")
print("自定义格式：",custom_format)


# 常用的strftime格式代码：
#
# 代码	含义	示例
# %Y	4位数年份	2024
# %y	2位数年份	24
# %m	2位数月份	01-12
# %B	完整月份名	January
# %b	缩写月份名	Jan
# %d	2位数日期	01-31
# %A	完整星期名	Monday
# %a	缩写星期名	Mon
# %H	24小时制小时	00-23
# %I	12小时制小时	01-12
# %M	分钟	00-59
# %S	秒	00-59
# %p	AM/PM	AM/PM
