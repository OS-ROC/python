from datetime import datetime

from sympy.physics.units import years

dt = datetime.now()

print("年：",dt.year)
print("月：",dt.month)
print("日：",dt.day)
print("时：",dt.hour)
print("分：",dt.minute)
print("秒：",dt.second)