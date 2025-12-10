"""
演示非单例模式的效果
"""

class StrTools:
    pass

s1 = StrTools()
s2 = StrTools()
print(s1)
print(s2)
print(id(s1))
print(id(s2))