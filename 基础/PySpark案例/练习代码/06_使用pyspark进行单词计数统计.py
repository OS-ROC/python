"""
单词计数统计
"""
from pyspark import SparkConf, SparkContext
import os
os.environ["PYSPARK_PYTHON"] = r'D:\pycharm-2025.1.3.1\pycharmprojects\venv1\Scripts\python.exe'

# 1. 构建执行环境入口对象
conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)
# 2. 读取数据文件
rdd = sc.textFile("hello.txt")
# 3. 取出全部单词
word_rdd = rdd.flatMap(lambda x: x.split(" "))
# 4. 将所有单词都转换成二元元组，单词为Key，value设置为1
word_with_one_rdd = word_rdd.map(lambda x: (x, 1))
# 5. 分组并求和
result = word_with_one_rdd.reduceByKey(lambda x,y: x + y)
# 6. 打印输出结果
print(result.collect())
sc.stop()