"""
演示RDD的reduceByKey成员方法的使用
"""
from pyspark import SparkConf,SparkContext
import os
os.environ['PYSPARK_PYTHON'] = r'D:\pycharm-2025.1.3.1\pycharmprojects\venv1\Scripts\python.exe'
conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)

# 准备一个RDD
rdd = sc.parallelize([("男",99),("男",88),("女",99),("女",66)])
# 求男生和女生两个组的成绩之和
rdd1 = rdd.reduceByKey(lambda x,y: x+y)
print(rdd1.collect())