"""
读取文件转换成RDD，并完成：
    1. 打印输出：热门搜索时间段（小时精度）Top3
    2. 打印输出：热门搜索词Top3
    3. 打印输出： 统计黑马程序员关键字在哪个时间段被搜索最多
    4. 将数据转换为JSON格式，写出为文件
"""

from pyspark import SparkConf, SparkContext
import os
import json
os.environ['PYSPARK_PYTHON'] = r'D:\pycharm-2025.1.3.1\pycharmprojects\venv1\Scripts\python.exe'
os.environ['HADOOP_HOME'] = 'C:\hadoop'
conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
conf.set("spark.default.parallelism", "1")
sc = SparkContext(conf=conf)

# 读取文件转换成RDD
file_rdd = sc.textFile("search_log.txt")
# TODO 需求1： 热门搜索时间段Top3（小时精度）
# 1.1 取出全部的时间并转换为小时
# 1.2 转换为(小时, 1) 的二元元组
# 1.3 Key分组聚合Value
# 1.4 排序（降序）
# 1.5 取前3
result1 = file_rdd.map(lambda x: (x.split('\t')[0][:2],1)).\
    reduceByKey(lambda x, y: x + y).\
    sortBy(lambda x: x[1],ascending=False,numPartitions=1).\
    take(3)
print("需求1的结果：",result1)

# TODO 需求2： 热门搜索词Top3
# 2.1 取出全部的搜索词
# 2.2 (词, 1) 二元元组
# 2.3 分组聚合
# 2.4 排序
# 2.5 Top3
result2 = file_rdd.map(lambda x: (x.split('\t')[2],1)).\
    reduceByKey(lambda x,y: x + y).\
    sortBy(lambda x: x[1],ascending=False,numPartitions=1).\
    take(3)
print("需求2的结果：",result2)

# TODO 需求3： 统计黑马程序员关键字在什么时段被搜索的最多
# 3.1 过滤内容，只保留黑马程序员关键词
# 3.2 转换为(小时, 1) 的二元元组
# 3.3 Key分组聚合Value
# 3.4 排序（降序）
# 3.5 取前1
result3 = file_rdd.map(lambda x: x.split('\t')).\
    filter(lambda x: x[2] == "黑马程序员").\
    map(lambda x: (x[0][:2],1)).\
    reduceByKey(lambda x,y: x + y).\
    sortBy(lambda x: x[1],ascending=False,numPartitions=1).\
    take(1)
print(result3)

# TODO 需求4： 将数据转换为JSON格式，写出到文件中
# 4.1 转换为JSON格式的RDD
# 4.2 写出为文件
file_rdd.map(lambda x: x.split('\t')).\
    map(lambda x: {"time":x[0],"user_id":x[1],"key_word":x[2],"rant1":x[3],"rant2":x[4],"url":x[5]}).\
    saveAsTextFile("json_output")















# from pyspark import SparkConf, SparkContext
# import os
# import json
#
# os.environ["PYSPARK_PYTHON"] = r'D:\pycharm-2025.1.3.1\pycharmprojects\venv1\Scripts\python.exe'
# os.environ["HADOOP_HOME"] = 'C:\hadoop'
# conf = SparkConf().setMaster('local[*]').setAppName('test_spark')
# sc = SparkContext(conf=conf)
#
# file_rdd = sc.textFile("search_log.txt")
# # print(file_rdd.collect())
#
# # 需求1
# json_str_rdd = file_rdd.map(lambda x: x.split("\t")).map(lambda x: x[0]).map(lambda x: x[:2]).map(lambda x: (x,1)).reduceByKey(lambda x,y:x+y).sortBy(lambda x: x[1],ascending=False,numPartitions=1).filter(lambda x: x[1] >= 2989)
# print("需求1的结果：",json_str_rdd.collect())
#
# # 需求2
# rdd2 = file_rdd.map(lambda x: x.split("\t")).map(lambda x: x[2]).map(lambda x: (x,1)).reduceByKey(lambda x,y:x+y).sortBy(lambda x: x[1],ascending=False,numPartitions=1).filter(lambda x: x[1] >= 2002)
# print("需求2的结果：",rdd2.collect())
#
# # 需求3
# rdd3 = file_rdd.map(lambda x: x.split("\t")).filter(lambda x: x[2] == "黑马程序员").map(lambda x: x[0][:2]).sortBy(lambda x: x[1],ascending=False,numPartitions=1).map(lambda x:(x,1)).reduceByKey(lambda x,y: x + y).sortBy(lambda x: x[1],ascending=False,numPartitions=1)
# # rdd3 = file_rdd.map(lambda x: x.split("\t")).map(lambda x: x[0]).map(lambda x: x[:2])
# print("需求3的结果：",rdd3.collect())
#
#
# # 将数据转换为json
# # json_data = file_rdd.map(lambda x: x.split("\t")).map(lambda x: x[0]).map(lambda x: x[:2]).map(lambda x: (x,1)).reduceByKey(lambda x,y:x+y).sortBy(lambda x: x[1],ascending=False,numPartitions=1).filter(lambda x: x[1] >= 2989).map(lambda x: json.loads(x[0]))
# json_data1 = json_str_rdd.map(lambda x: json.dumps({"date":x[0]}))
# json_data2 = rdd2.map(lambda x: json.dumps({"word":x[0]}))
# json_data3 = rdd3.map(lambda x: json.dumps({"itheima":x[0]}))
# print(json_data1.map(lambda x: json.loads(x)).collect())
# print(json_data2.map(lambda x: json.loads(x)).collect())
# print(json_data3.map(lambda x: json.loads(x)).collect())
#
#
# # 将数据输出到文件
# json_data1.saveAsTextFile("output4")
# json_data2.saveAsTextFile("output5")
# json_data3.saveAsTextFile("output6")