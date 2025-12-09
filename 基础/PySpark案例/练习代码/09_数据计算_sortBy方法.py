"""
演示RDD的sortBy成员方法的使用
"""

from pyspark import SparkConf,SparkContext
import os
os.environ["PYSPARK_PYTHON"] = r"D:\pycharm-2025.1.3.1\pycharmprojects\venv1\Scripts\python.exe"
conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)

# 1. 读取数据文件
rdd = sc.textFile("hello.txt")
# 2. 取出全部单词
word_rdd = rdd.flatMap(lambda x: x.split(" "))
# 3. 将所有单词都转换成二元元组，单词为Key，value设置为1
word_with_one_rdd = word_rdd.map(lambda x: (x, 1))
# 4. 分组并求和
result = word_with_one_rdd.reduceByKey(lambda x,y: x + y)
# 5. 对结果进行排序
result.sortBy(lambda x: x[1],ascending=False,numPartitions=1) # Fasle为降序，True为升序
print(result.collect())
sc.stop()