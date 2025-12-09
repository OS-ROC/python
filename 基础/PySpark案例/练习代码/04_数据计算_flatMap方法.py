"""
演示RDD的flatMap成员方法的使用
"""
from pyspark import SparkConf,SparkContext
import os
os.environ['PYSPARK_PYTHON'] = r'D:\pycharm-2025.1.3.1\pycharmprojects\venv1\Scripts\python.exe'
conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)

# 准备一个RDD
rdd = sc.parallelize(["Boker Tao 账本 树人","张本 gaoshou","highhand 陶李芬芳 立德树人"])

# 需求，将RDD数据里面的一个个单词提炼出来
rdd1 = rdd.flatMap(lambda x: x.split(" "))
print(rdd1.collect())
