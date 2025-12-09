"""
完成练习案例：JSON商品统计
需求：
1. 各个城市销售额排名，从大到小
2. 全部城市，有哪些商品类别在售卖
3. 北京市有哪些商品类别在售卖
"""

from pyspark import SparkConf, SparkContext
import os
import json

os.environ["PYSPARK_PYTHON"] = r'D:\pycharm-2025.1.3.1\pycharmprojects\venv1\Scripts\python.exe'
conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)

# TODO 需求1： 城市销售额排名
# 1.1 读取文件得到RDD
file_rdd = sc.textFile("orders.txt")
# 1.2 取出一个个JSON字符串
json_str_rdd = file_rdd.flatMap(lambda x: x.split("|"))
# 1.3 将一个个JSON字符串转换为字典
dict_rdd = json_str_rdd.map(lambda x: json.loads(x))
# 1.4 取出城市和销售额数据
# (城市，销售额)
city_with_money_rdd = dict_rdd.map(lambda x: (x["areaName"], int(x["money"])))
# 1.5 按城市分组按销售额聚合
city_result_rdd = city_with_money_rdd.reduceByKey(lambda x, y: x + y)
# 1.6 按销售额聚合结果进行排序
result1_rdd = city_result_rdd.sortBy(lambda x: x[1], ascending=False,numPartitions=1)
print("需求1的结果：",result1_rdd.collect())
# TODO 需求2： 全部城市有哪些商品类别在售卖
# 2.1 取出全部的商品类别
category_rdd = dict_rdd.map(lambda x: (x["category"])).distinct()
print("需求2的结果：",category_rdd.collect())
# 2.2 对全部商品类别进行去重
# TODO 需求3： 北京市有哪些商品类别在售卖
# 3.1 过滤北京市的数据
BeiJing_data_rdd = dict_rdd.filter(lambda x: x["areaName"] == "北京" )
# 3.2 取出全部商品类别
result3_rdd = BeiJing_data_rdd.map(lambda x: x["category"]).distinct()
print("需求3的结果：",result3_rdd.collect())
# 3.3 进行商品类别去重



# # 需求1
# rdd = sc.textFile("orders.txt")
# city_money_rdd = rdd.flatMap(lambda x: x.split("|")).map(lambda x: json.loads(x)).map(lambda x: (x["areaName"],int(x["money"])))
# city_sells_rdd = city_money_rdd.reduceByKey(lambda x, y: x + y).sortBy(lambda x: x[1],ascending=False,numPartitions=1)
#
# # 需求2
# all_city_item_rdd = rdd.flatMap(lambda x: x.split("|")).map(lambda x: json.loads(x)).map(lambda x: (x["areaName"],x["category"])).distinct()
#
# # 需求3
# BeiJing_item_rdd = rdd.flatMap(lambda x: x.split("|")).map(lambda x: json.loads(x)).map(lambda x: (x["areaName"],x["category"])).filter(lambda x: x[0] == "北京").distinct()
#
#
#
#
#
# # city_money_rdd = rdd1.map()
# print("需求1的结果",city_sells_rdd.collect())
# print("需求2的结果",all_city_item_rdd.collect())
# print("需求3的结果",BeiJing_item_rdd.collect())
# # city_money()
#
# sc.stop()