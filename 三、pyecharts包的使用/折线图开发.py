## 计算圆的面积
# radius = float(input())
# area =  3.1415926*radius**2
# print("{:.2f}".format(area))



## 斐波拉契数列1000以下
# count1,count2 = 0,1
# while count1<1000:
#     print("%.f,"%count1,end='')         # end=''表示让输出的数字不换行
#     count1,count2 = count2,count1+count2
#


# import turtle
## 绘制五角星
# turtle.fillcolor("red")
# turtle.begin_fill()
# while True:
#     turtle.forward(200)
#     turtle.right(144)
#     if abs(turtle.pos()) < 1:
#         break
# turtle.end_fill()

## 画笔向右转1111111100度
#turtle.right(1111111100)




## 编写一个能进行货币间币值转换的小程序。
# 假设人民币和美元间汇率固定为：1美元 = 6.78人民币。
#
# cur=input("请输入后面带有符号$或￥的货币数值：")
# if cur[-1] == '$':
#     cur = float(cur[: -1]) * 6.78
#     print("%.2f￥"%cur)
# else :
#     cur = float(cur[:-1]) / 6.78
#     print("%.2f$"%cur)





## 编写一个能绘制蟒蛇基本形状的小程序。
'''


import turtle
turtle.setup(650, 350, 200, 200)
turtle._______
turtle.fd(-250)
turtle.pendown()
turtle.pensize(25)
turtle.pencolor("purple")
turtle._________
for i in range(4):
    turtle.________
    turtle.________
turtle.circle(40, 80/2)
turtle.fd(40)
turtle.circle(16, 180)
turtle.fd(40 * 2/3)
turtle.done()

'''


## 股价计算小程序

# name = "311寝室"
# stock_price = 31.44
# stock_code = "00231"
# increase_factor = 1.2
# increase_days = 7
# print(f"公司: {name}",f"股票代码: {stock_code}",f"当前股价: {stock_price}")
# print("每日增长系数：%s，经过%s天的增长后，股价达到了：%.2f"%(increase_days,increase_days,stock_price * increase_factor**increase_days))



## 欢迎登录小程序


# user_name = input()
# user_type = input()
#
# print(f"你好，{user_name},你是尊贵的：{user_type}用户，欢迎你的光临。")
# print("你好：%s,你是尊贵的：%s 用户，欢迎你的光临。"%(user_name,user_type))




## 登录程序

# name = str(input("please enter your name: "))
# password = str(input("please enter your password: "))
#
# if name == "liuzhuopeng" and password =="123456":
#     print("welcome to code world!")
# elif name != "liuzhuopeng" or password != "123456":
#     print("your name or password is wrong!")


## 成年人判断

# print("欢迎来到311儿童游乐场，儿童免费，成人收费。")
# age = int(input("请输入你的年龄："))
# if age >= 18:
#     print("你已成年，游玩需要补票10元。")
# print("祝你游玩愉快。")
#
# if int(input("please enter your age:")) >= 18:
#     print("you are a adult,need to pay extra 10 dollars")
# print("welcome to 311 children park!")


# print("欢迎来到311儿童游乐场，儿童免费，成人收费。")
# age = int(input("请输入你的年龄："))
# if age >= 18:
#     print("你已成年，游玩需要补票10元。")
# else:
#     print("你未成年，可以免费游玩")
#
# print("祝你游玩愉快。")


## 猜猜心里数字

#import random

# num = random.randint(1,10)
#
# speculate_num = int(input("请输入第一次猜想的数字："))
# if speculate_num == num:
#     print("恭喜你，第一次就猜对了！")
# elif int(input("不对，再猜一次：")) == num:
#     print("恭喜你猜对了！")
# elif int(input("不对，再猜最后一次：")) == num:
#     print("恭喜你猜对了！")
# else:print(f"Sorry，全部猜错啦，我想的是{num}")



## 使用if语句实现猜数字

# import random

# num = random.randint(1,10)
# speculate_num = int(input("第一次猜测："))
#
# if speculate_num == num:
#     print("恭喜你答对了！")
# elif speculate_num > num:
#     speculate_num = int(input("大了，第二次猜测："))
#     if speculate_num == num:
#         print("恭喜你答对了！")
#     elif speculate_num > num:
#         speculate_num = int(input("大了，第三次猜测："))
#         if speculate_num == num:
#             print("恭喜你答对了！")
#         else:print("您三次都错了")
# elif speculate_num < num:
#     speculate_num = int(input("小了,第二次猜测："))
#     if speculate_num == num:
#         print("恭喜你答对了！")
#     elif speculate_num > num:
#         speculate_num = int(input("小了，第三次猜测："))
#         if speculate_num == num:
#             print("恭喜你答对了！")
#         else:print("您三次都错了")



# import random
#
# num = random.randint(1,10)
#
# spe_num = int(input("请输入您第一次猜测的数字："))
# if spe_num == num:
#     print("你真棒，第一次就猜对了！")
# else:
#     if spe_num > num:
#         print("你猜大了哦。")
#     else:print("你猜小了哦")
#
#     spe_num = int(input("请输入第二次猜测的数字："))
#     if spe_num == num:
#         print("你真棒，猜对了！")
#     else:
#         if spe_num > num:
#             print("你猜大了哦。")
#         else:print("你猜小了哦")
#
#         spe_num = input("请输入第三次猜测的数字：")
#         if spe_num == num:
#             print("恭喜你，答对啦！")
#         else:print("你三次都答错了哦。")






##发工资小程序

# import random
#
# account_money= 10000
#
# for i in range(1,21):
#     employee_score = random.randint(1, 10)
#     if employee_score < 5:
#         print(f"员工{i}，绩效{employee_score}，低于5，不发工资，下一位。")
#     else:
#         print(f"向员工{i}发送工资1000元，账户余额{account_money-1000}元。")
#         account_money -= 1000
#         if account_money <= 0:
#             print("工资发完了，下个月领取吧。")
#             break


# import random
#
# account = 10000
# for x in range(1, 21):
#     employee_score = random.randint(1, 10)
#     if employee_score < 5:
#
#         print(f"员工{x}，绩效分{employee_score}，低于5，不发工资。")
#         continue
#     else:
#         account -= 1000
#         print(f"向员工{x}发放工资1000元，账户余额还剩余{account}。")
#
#     if account <= 0:
#         break
# print("工资发完了，下个月领取吧。")






# # 元组
# t1 = (666,True,"hello")
# t2 = ()  # 空元组
# t3 =tuple()  # 空元组
#
# print(t1,type(t1))
# print(t2,type(t2))
# print(t3,type(3))
#
# # 元组的嵌套
# print(t1[2])
# t4 = ((111,222,333),(666,777,888),("aaa",))   # 定义单个元素的元组，这个元素后面要加逗号
#
# # 下表索引取出内容
# s1 = t4[0]
# s2 = t4[1][2]
# s3 = t4[2]
# s4 = t4[2][0]
# print(s1,type(s1),s2,type(s2),s3,type(s3),s4,type(s4))

## 通过循环遍历元组
# index = 0
# count = 0
# while index < len(t4):
#     count += 1
#     print(f"元组第{count}个元素为{t4[index]}")
#     index += 1

# for i in t4:
#     count += 1
#     print(f"元组中第{count}个元素为{i}")

## 解决了无法读取嵌套元组下表索引的问题
# for element in t4:
#     if type(element) == tuple:
#         for item in element:
#             if item == 888:
#                 print(f"888的下表索引为[{t4.index(element)}][{element.index(888)}]")






# name = "im booker tao or tree people"
# print(f"字符串{name}中有{name.count("o")}个o")
# new_name = name.replace(" ","|")
# print(new_name)
# new_name1 = new_name.split("|")
# print(new_name1)





## 在字符串中取出"张本瑶荣"
'''

#使用切片和倒序方法
sentence = "辩答托依是我，荣瑶本张是我，人树陶是我"
# s1 = sentence[10:6:-1]   # 方法1
# s1 = sentence[::-1][8:12]  # 方法2
s1 = sentence[7:11][::-1]   # 方法3
print(s1)
'''
# 使用split和replace方法
sentence = "辩答托依是我，荣瑶本张是我，人树陶是我"
'''
方法1
s2 = sentence.split('，')
s2 = s2[1]
s2 = s2.replace("是我","")
s2 = s2[::-1]
print(s2)
'''

'''
方法2
s2 = sentence.split("，")[1].replace("是我","")[::-1]
print(s2)
'''





'''
# 定义一个空集合
# 通过for循环遍历列表
# 在for循环中将列表的元素添加到集合
# 最终得到元素去重后的集合对象，并打印输出

my_list = ['陶树人','账本','陶树人','账本','booker tao','tree people','booker tao','tree people','zhangben']
my_set = set()
for element in my_list:
    my_set.add(element)
print(f"存入数据后的集合为：{my_set}")

'''






# # 使用Matplotlib库创建了一个简单的散点图
#
#
# import matplotlib.pyplot as plt  # # 导入matplotlib的pyplot模块，别名为plt
# import numpy as np     # 导入numpy库，别名为np
#
# x = np.arange(15)   # 创建从0到14的整数数组作为x坐标：[0, 1, 2, ..., 14]
# y = np.random.randn(15)   # # 创建15个符合标准正态分布的随机数作为y坐标
# plt.scatter(x, y,color='black')   # 创建散点图，x为横坐标，y为纵坐标，点颜色为黑色
# plt.show()   # 显示图形


# import matplotlib.pyplot as plt
# import numpy as np
# np.random.seed(2025)    # 设置随机种子，确保结果可重现,数字可以为任何整数
#
# N = 100    # 设置点的数量为100个
# x = np.random.rand(N)     # 生成100个[0,1)之间的随机数作为x坐标
# y = np.random.rand(N)     # 生成100个[0,1)之间的随机数作为y坐标
#
# colors = np.random.randn(N)    # 生成100个随机颜色值（0-1之间的数值）
# area = (20*np.random.rand(N))**2     # 生成100个随机面积大小
#
# plt.scatter(x, y, s=area, c=colors, alpha=0.5)  # 创建散点图，alpha为透明度
# plt.show()







# employee_dict = {
#     "Booker Tao":{
#         "部门":"科技部",
#         "工资":3000,
#         "级别":1
#     },    "陶树人":{
#         "部门":"市场部",
#         "工资":5000,
#         "级别":2
#     },    "Tree People":{
#         "部门":"市场部",
#         "工资":7000,
#         "级别":3
#     },    "张本瑶荣":{
#         "部门":"科技部",
#         "工资":4000,
#         "级别":1
#     },    "陶喜芒芒":{
#         "部门":"市场部",
#         "工资":6000,
#         "级别":2
#     }
# }
#
# print(f"全体员工信息如下：\n{employee_dict}",end="\n")
#
#
# for employee in employee_dict:
#
#     if employee_dict[employee]["级别"] == 1:
#         employee_dict[employee]["级别"] += 1
#         employee_dict[employee]["工资"] += 1000
#
# print(f"全体员工级别为1的员工完成升值加薪操作后：\n{employee_dict}")















# def abc(computer):
#     result = computer(1,2)
#     print(result)
#     print(type(computer))
#
# def computer(a,b):
#     result = a+b
#     print(result)
#     return ''
# abc(computer)









# import matplotlib.pyplot as plt
# import math             # 导入数据函数库
#
# plt.rcParams['font.family'] = 'SimHei'   # 设置字体为黑体
# plt.rcParams['font.sans-serif'] = ['SimHei']
# plt.rcParams['axes.unicode_minus'] = False   # 解决符号显示为方块的问题
#
# x = range(0,10)  # x的数据
# fun1 = lambda i:math.sin(i)   # y=sin(x)计算函数
# y = list(map(fun1,x))         # 计算y轴数据并存入列表
# plt.plot(x,y,'r',marker='*')    # 绘制折线图，横坐标为x，纵坐标为y，颜色为红色，用*号标识数据
# plt.bar(x,y,alpha = 0.5,color = 'b',width = 0.3)    # 绘制柱形图，颜色为蓝色，透明的0.5，宽度0.3
#
# plt.xlabel("x 轴")  # x轴标记
# plt.ylabel("y 轴")  # y轴标记
# plt.title("图1 陶树人")     # 图像标题
# plt.show()          # 显示图像









# import matplotlib.pyplot as plt
# import math             # 导入数据函数库
#
# plt.rcParams['font.family'] = 'SimHei'   # 设置字体为黑体
# plt.rcParams['font.sans-serif'] = ['SimHei']
# plt.rcParams['axes.unicode_minus'] = False   # 解决符号显示为方块的问题
#
# x = range(0,10)  # x的数据
# fun1 = lambda i:math.sin(i)   # y=sin(x)计算函数
# y = list(map(fun1,x))         # 计算y轴数据并存入列表
# plt.subplot(2,2,1)
# plt.plot(x,y,'r',marker='*')    # 绘制折线图，横坐标为x，纵坐标为y，颜色为红色，用*号标识数据
# plt.grid(linestyle=":",color='b')   # 显示虚线，蓝色网格线
# plt.plot(x,y,color='r',marker='1',label="sin(x)")    # label参数用来设置图例字符串
# plt.legend(loc="lower left")   # 图例显示在左下角
# plt.xlim(0,10)   # 设置x轴的坐标范围，解决了左边0点没有在坐标轴上的问题
# ticks = ["A1","A2","A3","A4","A5","A6","A7","A8","A9","A10"]   # 用列表定义准备替换x的字符串
# plt.xticks(x,ticks)  # 把x替换成ticks中的内容，x提供位置，ticks提供内容
# plt.xlabel("x 轴")  # x轴标记
# plt.ylabel("y 轴")  # y轴标记
# plt.title("图1 陶树人")     # 图像标题
#
#
# plt.subplot(2,2,2)
# plt.bar(x,y,alpha = 0.5,color = 'b',width = 0.3)    # 绘制柱形图，颜色为蓝色，透明的0.5，宽度0.3
# plt.xlabel("x 轴")  # x轴标记
# plt.ylabel("y 轴")  # y轴标记
# plt.title("图1 陶树人")     # 图像标题
# plt.show()          # 显示图像




# import matplotlib.pyplot as plt
# import math
# plt.rcParams['font.family'] = 'SimHei'
# plt.rcParams['font.sans-serif'] = ["SimHei"]
# plt.rcParams["axes.unicode_minus"] = False
#
# x = range(0,10)
# fun1 = lambda i:math.sin(i)
# fun2 = lambda i:math.cos(i)
# y1 = list(map(fun1,x))
# y2 = list(map(fun2,x))
# plt.subplot(2,1,1)
# plt.plot(x,y1,'r',marker='*',label="sin(x)")
# plt.plot(x,y2,'g',marker='o',label="cos(x)")
# plt.xlim(0,12)
# plt.legend(loc="lower left")
# plt.xlabel("x 轴")
# plt.ylabel("y 轴")
# plt.title("图1 sin和cos图",color="r",fontsize=15)
# plt.grid(linestyle = ":",color="b")
#
# plt.subplot(2,1,2)
# plt.plot(x,y1,'y',marker='D',label = "sin(x)")
# plt.legend(loc = "lower right")
# plt.xlim(0,12)
# ticks = ["a","b","c","d","e","f","g","h","i","j"]
# plt.xticks(x,ticks)
#
# plt.show()









## flask服务器

# from flask import Flask,request
#
# app = Flask(__name__)
#
# @app.route("/index",methods=["GET","POST"])
# def index():
#     if request.method == "GET":
#         name = request.args.get("name")
#         age = request.args.get("age")
#
#         return f"首页内容GET:name={name},age={age}"
#     else:
#         return "首页内容POST"
# @app.route("/<name>")
# def hello(name):
#     return f"你好{name}"
# if __name__ == "__main__":
#     app.run(debug=True,host="127.0.0.1",port=8080)





# import numpy as np
#
# a = np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(a)
# print(a.dtype)
# print(a.shape)
# print(a.ndim)
# print(a.size)
# b = np.array([[1.23,2,3],[4,5,6],[7,8,9]])
# print(b)
# c = np.array([[1,2,3],[4,5,6],[7,8,9]],dtype=float)
# print(c)
#
# p = np.array([1,2,3])
# x = np.array([[1],[2],[3],[4]])
# y = np.array([[1,2,3],[4,5,6]])
# print(p+x)
# print()
# print(p+y)



# import pandas as pd
#
# data1 = {
#     'name':['slave_1','slave_2','slave_3','slave_4','slave_5',],
#     'gender':['male','female','male','female','male'],
#     'age':[21,24,22,24,23],
#     'height':[174,178,167,179,181]
# }
#
# df1 = pd.DataFrame(data1)
# print(df1)






# import time
#
# f = open(r"C:\Users\suci\Desktop\123.txt",'r',encoding="utf-8")
# content = f.read(11)
# print(f"123.txt中的内容是：\n{content}")
#
# f = open(r"C:\Users\suci\Desktop\123.txt",'r',encoding="utf-8")
# lines = f.readlines()
# print(lines)
#
# f = open(r"C:\Users\suci\Desktop\123.txt",'r',encoding="utf-8")
# line1 = f.readline()
# line2 = f.readline()
# line3 = f.readline()
# print(f"第一行的内容是：{line1}")
# print(f"第二行的内容是：{line2}")
# print(f"第三行的内容是：{line3}")
#
# count = 0
# for line in open(r"C:\Users\suci\Desktop\123.txt",'r',encoding="utf-8"):
#     count += 1
#     print(f"第{count}行的数据为{line}")
# f.close()
# time.sleep(10000)




# with open("word.txt",'r',encoding='utf-8') as f:
#     words = f.read().split()    # split()默认使用空格和换行符划分单词
#     count = 0
#     for word in words:
#         if word == "tao":
#             count += 1
#     print(f"tao出现了{count}次")
#
#
# f = open("word.txt","r",encoding='utf-8')
# content = f.read()
# count = content.count("tree")
# print(f"tree出现了{count}次")
#









#
#
# f = open("bill.txt","r",encoding="utf-8")
# f.close()
# lines = f.readlines()
# print(lines)
# print(type(lines))
# for line in lines:
#     line = line.strip()
#     for word in line.split(","):
#         if word == "正式":
#             open("bill.txt.bak","a",encoding="utf-8").write(f"{line}\n")
#             flush()
#
#
#         else:
#             continue
#



# fr = open("bill.txt","r",encoding="utf-8")   # 读取原文件
# fx = open("bill.txt.bak","w",encoding="utf-8")   # 写入备份文件
#
# for line in fr:
#     line = line.strip()   # 去除前后的换行符和空格
#
#     if line.split(",")[4] == "测试":     # 这里注意如果没有把line.split()赋值给一个变量的话这里就只会暂时是列表形式，所以可以直接用索引；如果在该语句下一行使用type(line)还是会显示类型str
#         continue
#
#     fx.write(f"{line}\n")  # 因为前面去掉了换行符，这里输出时要加上
#
# fr.close()  # 关闭文件，将内容存进硬盘
# fx.close()
#









# from pyecharts.charts impoprt Line
# from pyecharts.options import TitleOpts, LegendOpts, ToolboxOpts, VisualMapOpts
#
# line = Line()   # 创建一个折线图对象
#
# line.add_xaxis(["中国","美国","日本"])   # x轴数据
# line.add_yaxis("GDP",[20,30,10])  # y轴数据
#
# # 设置全局配置项
# line.set_global_opts(
#     title_opts=TitleOpts(title="GDP展示",pos_left="center",pos_bottom="1%"),
#     legend_opts=LegendOpts(is_show=True),
#     toolbox_opts=ToolboxOpts(is_show=True),
#     visualmap_opts=VisualMapOpts(is_show=True),
# )
#
# # 通过render方法，将代码生成图像
# line.render()
# ## 会生成一个render.html文件
#







# '''
# 演示可视化需求：折线图开发
# '''
#
# import json
# from pyecharts.charts import Line
# from pyecharts.options import TitleOpts, LabelOpts, ToolboxOpts,LegendOpts,VisualMapOpts
#
# # 处理数据
# f_us = open("D:\数据分析\课件资料\资料\第1-12章资料\资料\资料\可视化案例数据\折线图数据\美国.txt",'r',encoding='utf-8')
# us_data = f_us.read()   # 美国的全部内容
#
# f_jp = open("D:\数据分析\课件资料\资料\第1-12章资料\资料\资料\可视化案例数据\折线图数据\日本.txt",'r',encoding='utf-8')
# jp_data = f_jp.read()    # 日本的全部内容
# f_in = open("D:\数据分析\课件资料\资料\第1-12章资料\资料\资料\可视化案例数据\折线图数据\印度.txt",'r',encoding='utf-8')
# in_data = f_in.read()    # 印度的全部内容
#
# # 去掉不合JSON规范的开头
# us_data = us_data.replace("jsonp_1629344292311_69436(","")
# jp_data = jp_data.replace("jsonp_1629350871167_29498(","")
# in_data = in_data.replace("jsonp_1629350745930_63180(","")
#
# # 去掉不合JSON规范的结尾(与开头用了不同的方法，具体情况具体分析)
# us_data = us_data[:-2]
# jp_data = jp_data[:-2]
# in_data = in_data[:-2]
#
# # 将JSON转换成python字典
# us_dict = json.loads(us_data)
# jp_dict = json.loads(jp_data)
# in_dict = json.loads(in_data)
#
# # 利用在线工具获取数据集的结构，获取trend key
# us_trend_dict = us_dict["data"][0]["trend"]
# jp_trend_dict = jp_dict["data"][0]["trend"]
# in_trend_dict = in_dict["data"][0]["trend"]
#
# # 获取日期数据，用于x轴，取2020年（到314下标结束）
# us_x_data = us_trend_dict["updateDate"][:314]
# jp_x_data = jp_trend_dict["updateDate"][:314]
# in_x_data = in_trend_dict["updateDate"][:314]
#
# # 获取确诊数据，用于y轴，取2020年（到314结束）
# us_y_data = us_trend_dict["list"][0]["data"][:314]
# jp_y_data = jp_trend_dict["list"][0]["data"][:314]
# in_y_data = in_trend_dict["list"][0]["data"][:314]
#
# # 生成图表
# line = Line()
# # 添加x轴数据
# line.add_xaxis(us_x_data)
# # 添加y轴数据
# line.add_yaxis("美国确诊人数",us_y_data,label_opts=LabelOpts(is_show=False))   # label_opts=LabelOpts(is_show=False)的作用是不显示折线上各个点的数据，让图标更加美观
# line.add_yaxis("日本确诊人数",jp_y_data,label_opts=LabelOpts(is_show=False))
# line.add_yaxis("印度确诊人数",in_y_data,label_opts=LabelOpts(is_show=False))
#
# # 设置全局配置项
# line.set_global_opts(
#
#     # 设置折线图的标题，位置居中，距离底部百分之一
#     title_opts=TitleOpts(title="美日印三国确诊人数对比图",pos_left="center",pos_bottom="1%"),
#     # 显示工具箱
#     toolbox_opts=ToolboxOpts(is_show=True),
#     # 显示图例（默认为显示）
#     legend_opts=LegendOpts(is_show=True),
#     # 显示图色对比
#     # visualmap_opts=VisualMapOpts(is_show=True)
#
# )
#
# # 全局配置项一定要用在render方法前
# # 调用render方法，生成图表
# line.render()
#
# # 关闭文件对象
# f_us.close()
# f_jp.close()
# f_in.close()


