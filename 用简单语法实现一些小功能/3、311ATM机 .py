#
# # 查询余额功能
# def inquire(balance,show):
#
#     '''
#
#     :param balance: 用来接收现有余额
#     :param show: 如果show为True就打印函数头部
#     :return: 这里因为此函数没有修改值，不需要加return
#     '''
#     if show:
#         print("==========查询余额==========")
#     print(f"陶树人，您好，您的余额剩余{balance}元。")
#
# # 存款功能
# def save_money(balance, num):
#     '''
#
#     :param balance: 用来接收money的值
#     :param num: 输入要存入的金额数目
#     :return: 用于返回修改或未修改的值，然后赋值给全局变量money
#     '''
#     print("==========存款==========")
#     if num <= 0:
#         print("金额不能为0或负数！")
#         return balance
#     else:
#         balance += num
#         print(f"陶树人，您好，您本次存款{num}元。")
#         inquire(balance, False)
#         return balance
#
# # 取款功能
# def get_money(balance, num):
#     '''
#
#     :param balance: 用来接收money的值
#     :param num: 输入要取出的金额数目
#     :return: 用于返回修改或未修改的值，然后赋值给全局变量money
#     '''
#     print("==========取款==========")
#     if num <= 0:
#         print("金额不能为0或负数")
#         return balance
#     elif balance < num:
#         print("余额不足")
#         return balance
#     else:
#         balance -= num
#         print(f"陶树人，您好，您本次取出{num}元。")
#         inquire(balance, False)
#         return balance
#         # break
# # 退出功能
# def exit_atm():
#     print("==========程序退出==========")
#     print("欢迎您的使用，祝您生活愉快。")
#
# # 主菜单
# def main():
#
#
#     print("================主菜单================")
#     print("陶树人，您好，欢迎来到311银行ATM。请选择操作：")
#     print("查询余额\t[输入1]")
#     print("存款  \t[输入2]")
#     print("取款  \t[输入3]")
#     print("退出  \t[输入4]")
#     return input("请输入你需要的服务对应的数字：")
#
# # 登录功能
# def login():
#
#     while True:
#         account = input("请输入您的账号：")
#         if account == '':
#             print("账号不能为空。")
#             continue
#         password = input("请输入您的密码：")
#         if password == '':
#             print("密码不能为空。")
#             continue
#         if account == "123456" and password == "123456":
#            print("登录成功！")
#            break
#
#         else:
#             print("你的账号或密码有错误，请重新输入！")
#             continue
#
#
# login()
# money = 100000
# while True:
#     user_input = main()  # 用一个字面量接收main()函数的input输入值
#     if user_input == "1":
#         inquire(money,True)
#
#     elif user_input == '2':
#         try:     # try-except语句用于处理异常代码，如果输入的不是int类型就执行except语句
#             num = int(input("请输入您想存入的金额数目："))
#             money = save_money(money,num)   #接收save_money()函数return的返回值，实现对余额的修改
#         except ValueError:
#             print("请输入有效的数字。")
#     elif user_input == '3':
#         try:
#             num = int(input("请输入您想取出的金额数目："))
#             money = get_money(money,num)
#         except ValueError:
#             print("请输入有效的数字。")
#     elif user_input == '4':
#         exit_atm()
#         break    # 退出程序（退出循环）
#     else:    # 避免其他非法输入导致程序崩溃
#         print("请输入正确的序号！")





## 面向对象版

"""
ATM模拟系统 - 面向对象实现版本

该模块实现了一个简单的ATM机模拟系统，包含登录验证、查询余额、存款、取款等功能。
采用面向对象设计，支持多个独立ATM实例运行。
"""

# 定义一个类对函数进行封装
class ATM():
    def __init__(self):  # 初始化函数
        self.balance = 10000   # 将余额初始化为10000
        self.runing = True  # 初始化run函数中的runing为True,控制主循环的运行状态
    # 查询余额功能
    def inquire(self,show):
        '''
        :param show: 如果show为False，在后面调用时就会把查询余额的表头去掉
        :return: 直接打印，返回None，用于封装
        '''
        if show:
            print("==========查询余额==========")
        print(f"陶树人，您好，您的余额剩余{self.balance}元。")

    # 存款功能
    def save_money(self, num):
        '''
        :param num: 用来接收存入的值
        :return:
        '''
        print("==========存款==========")
        if num <= 0:
            print("金额不能为0或负数！")
        else:
            self.balance += num
            print(f"陶树人，您好，您本次存款{num}元。")
            self.inquire(False)

    # 取款功能
    def get_money(self,num):
        '''
        :param num: 用于接收取出的值
        :return:
        '''
        print("==========取款==========")
        if num <= 0:
            print("金额不能为0或负数")
        elif self.balance < num:
            print("余额不足")
        else:
            self.balance -= num
            print(f"陶树人，您好，您本次取出{num}元。")
            self.inquire(False)

    # 退出功能
    def exit_atm(self):
        print("==========程序退出==========")
        print("欢迎您的使用，祝您生活愉快。")

    # 主菜单
    def main(self):
        print("================主菜单================")
        print("陶树人，您好，欢迎来到311银行ATM。请选择操作：")
        print("查询余额\t[输入1]")
        print("存款  \t[输入2]")
        print("取款  \t[输入3]")
        print("退出  \t[输入4]")
        return input("请输入你需要的服务对应的数字：")

    # 登录功能
    def login(self):
        while True:
            account = input("请输入您的账号：")
            if account == '':
                print("账号不能为空。")
                continue
            password = input("请输入您的密码：")
            if password == '':
                print("密码不能为空。")
                continue
            if account == "123456" and password == "123456":
               print("登录成功！")
               break
            else:
                print("你的账号或密码有错误，请重新输入！")
                continue
    def run(self):
        while self.runing:
            user_input = self.main()  # 用一个字面量接收main()函数的input输入值
            if user_input == "1":
                atm.inquire(True)
            elif user_input == '2':
                try:  # try-except语句用于处理异常代码，如果输入的不是int类型就执行except语句
                    num = int(input("请输入您想存入的金额数目："))
                    self.save_money(num)  # 接收save_money()函数return的返回值，实现对余额的修改
                except ValueError:
                    print("请输入有效的数字。")
            elif user_input == '3':
                try:
                    num = int(input("请输入您想取出的金额数目："))
                    self.get_money(num)
                except ValueError:
                    print("请输入有效的数字。")
            elif user_input == '4':
                self.exit_atm()
                break  # 退出程序（退出循环）
            else:  # 避免其他非法输入导致程序崩溃
                print("请输入正确的序号！")

atm = ATM()    # 创建第一个实例
atm.login()    # 登录界面
atm.run()      # 调用run函数

atm2 = ATM()    # 创建第二个实例
atm2.login()    # 登录界面
atm2.run()      # 调用run函数




