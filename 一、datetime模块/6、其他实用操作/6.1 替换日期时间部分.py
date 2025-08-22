from datetime import datetime

dt = datetime.now()
print(dt)
new_dt = dt.replace(2018,6)
print("替换后的日期：",new_dt)