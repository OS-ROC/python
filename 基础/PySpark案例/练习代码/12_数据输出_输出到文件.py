"""
演示将RDD输出到文件中
"""

from pyspark import SparkConf, SparkContext
import os
import json

os.environ["PYSPARK_PYTHON"] = r'D:\pycharm-2025.1.3.1\pycharmprojects\venv1\Scripts\python.exe'
os.environ["HADOOP_HOME"] = 'C:\hadoop'
conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
# conf.set("spark.default.parallelism", "1")
sc = SparkContext(conf=conf)

# 准备RDD1
rdd1 = sc.parallelize([1,2,3,4,5],numSlices=1)

# 准备RDD2
rdd2 = sc.parallelize([("Hello",3),("Spark",5),("Hi",7)],1)

# 准备RDD3
rdd3 = sc.parallelize([[1,3,5],[6,7,9],[11,13,11]],1)

# 输出到文件中
rdd1.saveAsTextFile("output1")
rdd2.saveAsTextFile("output2")
rdd3.saveAsTextFile("output3")