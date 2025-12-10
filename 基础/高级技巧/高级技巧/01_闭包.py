"""
演示Python的闭包特性
"""

# # 简单闭包
# def outer(logo):
#
#     def inner(msg):
#         print(f"<{logo}>{msg}<{logo}>")
#     return inner
#
# fn1 = outer("BookerTao")
# fn1("陶树人")
# fn1("账本")
#
# fn2 = outer("张本")
# fn2("ZhangBen")

# 使用nonlocal关键词修改外部函数的值
# def outer(num1):
#
#     def inner(num2):
#         nonlocal num1
#         num1 += num2
#         print(num1)
#     return inner
#
# fn = outer(10)
# fn(10)
# fn(30)

# 使用闭包实现ATM小案例
def account_create(init_amount=0):

    def atm(num,depoist=True):
        nonlocal init_amount
        if depoist:
            init_amount += num
            print(f"存款:+{num},账户余额:{init_amount}")
        else:
            init_amount -= num
            print(f"存款:-{num},账户余额:{init_amount}")

    return atm

atm = account_create()
atm(100)
atm(200)
atm(50,depoist=False)

