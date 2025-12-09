"""
演示RDD的filter成员方法的使用
"""

from pyspark import SparkConf,SparkContext
import os
os.environ["PYSPARK_PYTHON"] = r'D\pycharm-2025.1.3.1\pycharmprojects\venv1\Scripts\python.exe'
conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)

# 准备一个RDD
rdd = sc.parallelize([1,2,3,4,5])
# 对RDD的数据进行过滤
rdd1 = rdd.filter(lambda x: x % 2 == 0)
rdd1.collect()
print(rdd1.collect())

