# PySpark RDD算子完整学习手册

## 📋 目录

1. 数据输入与输出流程
2. 数据转换算子
3. 数据聚合算子
4. 数据过滤与去重
5. 数据排序
6. 数据输出方法
7. 代码示例汇总

------

## 数据输入与输出流程

### 📊 Spark编程流程



```
数据输入 → RDD计算 → 数据输出
```



#### 数据输入方法：

- `sc.parallelize()` - 从Python对象创建RDD
- `sc.textFile()` - 从文件读取数据

#### 数据计算：

- 返回值是RDD的算子（如map、flatMap、filter等）
- 通过链式调用进行计算

#### 数据输出：

- 返回值是Python对象（如collect、reduce、count等）
- 输出到文件系统（如saveAsTextFile）

------

## 数据转换算子

### 1. **map算子**

**功能**：将RDD的数据逐条处理，返回新的RDD

**语法**：

```
rdd.map(func)
# func: (T) → U  # 接受一个参数，返回任意类型
```

**特点**：

- 支持链式调用
- 处理逻辑基于传入的函数

**示例**：

```
rdd.map(lambda x: x * 10).map(lambda x: x + 5)
```



### 2. **flatMap算子**

**功能**：对RDD执行map操作，然后进行解除嵌套操作

**语法**：

```
rdd.flatMap(func)
```

**特点**：

- 比map多出解除一层嵌套的功能
- 常用于拆分字符串或嵌套列表

**示例**：

```
# 输入：["a b c", "a c e", "e c a"]
# 输出：["a", "b", "c", "a", "c", "e", "e", "c", "a"]
rdd.flatMap(lambda x: x.split(" "))
```



------

## 数据聚合算子

### 3. **reduce算子**

**功能**：对RDD数据集按照传入的逻辑进行聚合

**语法**：

```
rdd.reduce(func)
# func: (T, T) → T  # 接受2个参数，返回1个值，类型一致
```



**示例**：

```
rdd.reduce(lambda a, b: a + b)  # 求和
```



### 4. **reduceByKey算子**

**功能**：针对KV型RDD，自动按照key分组，完成组内数据的聚合

**语法**：

```
rdd.reduceByKey(func)
# func: (v, v) → v  # 接受2个相同类型的参数，返回相同类型
```



**特点**：

- 自动按照key分组
- 函数只负责聚合，不理会分组
- 适用于词频统计等场景

**示例**：

```
# 输入：[('a', 1), ('a', 1), ('b', 1), ('b', 1)]
# 输出：[('b', 2), ('a', 2)]
rdd.reduceByKey(lambda a, b: a + b)
```



**聚合逻辑图示**：

```
[1, 2, 3, 4, 5]
↓ lambda a, b: a + b
1+2=3 → 3+3=6 → 6+4=10 → 10+5=15
```



------

## 数据过滤与去重

### 5. **filter算子**

**功能**：过滤想要的数据进行保留

**语法**：

```
rdd.filter(func)
# func: (T) → bool  # 接受1个参数，返回布尔值
```



**规则**：

- 返回True的数据被保留
- 返回False的数据被丢弃

**示例**：

```
# 保留奇数
rdd.filter(lambda x: x % 2 == 1)
```



### 6. **distinct算子**

**功能**：对RDD数据进行去重，返回新RDD

**语法**：

```
rdd.distinct()  # 无需传参
```



**示例**：

```
# 输入：[1, 1, 3, 3, 5, 5, 6, 6, 9, 9]
# 输出：[1, 3, 5, 6, 9]
rdd.distinct()
```



------

## 数据排序

### 7. **sortBy算子**

**功能**：对RDD数据进行排序，基于指定的排序依据

**语法**：

```
rdd.sortBy(func, ascending=False, numPartitions=1)
# func: (T) → U: 告知按照哪个数据进行排序
# ascending: True升序，False降序
# numPartitions: 用多少分区排序（全局排序需设为1）
```



**示例**：

```
# 按元组的第二个元素降序排序
result.sortBy(lambda x: x[1], ascending=False, numPartitions=1)
```



------

## 数据输出方法

### 将RDD转换为Python对象

#### 8. **collect算子**

**功能**：将RDD各个分区内的数据，统一收集到Driver中，形成一个List对象

**语法**：

```
rdd.collect()  # 返回值是list
```



#### 9. **take算子**

**功能**：取RDD的前N个元素，组合成list返回

**语法**：

```
rdd.take(N)
```



**示例**：

```
>>> sc.parallelize([3,2,1,4,5,6]).take(5)
[3, 2, 1, 4, 5]
```



#### 10. **count算子**

**功能**：计算RDD有多少条数据，返回值是一个数字

**语法**：

```
rdd.count()
```



**示例**：

```
>>> sc.parallelize([3,2,1,4,5,6]).count()
6
```



### 将RDD输出到文件

#### 11. **saveAsTextFile算子**

**功能**：将RDD的数据写入文本文件中

**语法**：

```
rdd.saveAsTextFile("路径")
```



**特点**：

- 支持本地写出、HDFS等文件系统
- 输出结果是一个文件夹
- 有几个分区就输出多少个结果文件

------

## 分区控制

### 修改RDD分区数为1的方法

#### 方法1：SparkConf对象设置全局并行度

```
conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
conf.set("spark.default.parallelism", "1")  # 设置为1个分区
sc = SparkContext(conf=conf)
```



#### 方法2：创建RDD时设置分区数

```
rdd1 = sc.parallelize([1, 2, 3, 4, 5], numSlices=1)
# 简写形式
rdd1 = sc.parallelize([1, 2, 3, 4, 5], 1)
```



------

## 代码示例汇总

### 完整WordCount示例（带排序）

```
from pyspark import SparkConf, SparkContext
import os

os.environ["PYSPARK_PYTHON"] = r"python解释器路径"
conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)

# 1. 读取数据文件
rdd = sc.textFile("hello.txt")

# 2. 取出全部单词
word_rdd = rdd.flatMap(lambda x: x.split(" "))

# 3. 转换为二元元组
word_with_one_rdd = word_rdd.map(lambda x: (x, 1))

# 4. 分组并求和
result = word_with_one_rdd.reduceByKey(lambda x, y: x + y)

# 5. 按词频降序排序
sorted_result = result.sortBy(lambda x: x[1], ascending=False, numPartitions=1)

print(sorted_result.collect())
sc.stop()
```



### 数据输出综合示例

```
from pyspark import SparkConf, SparkContext
import os

os.environ["PYSPARK_PYTHON"] = r"python解释器路径"
conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)

# 准备RDD
rdd = sc.parallelize([1, 2, 3, 4, 5])

# collect算子
rdd_list = rdd.collect()
print(f"collect结果: {rdd_list}, 类型: {type(rdd_list)}")

# reduce算子
num = rdd.reduce(lambda x, y: x + y)
print(f"reduce求和结果: {num}")

# take算子
take_list = rdd.take(3)
print(f"take前3个: {take_list}")

# count算子
num_count = rdd.count()
print(f"元素个数: {num_count}")
```



### 文件输出示例

```
from pyspark import SparkConf, SparkContext
import os

os.environ["PYSPARK_PYTHON"] = r"python解释器路径"
os.environ["HADOOP_HOME"] = 'hadoop路径'
conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)

# 创建RDD（设置为1个分区）
rdd1 = sc.parallelize([1, 2, 3, 4, 5], 1)
rdd2 = sc.parallelize([("Hello", 3), ("Spark", 5), ("Hi", 7)], 1)
rdd3 = sc.parallelize([[1, 3, 5], [6, 7, 9], [11, 13, 11]], 1)

# 输出到文件
rdd1.saveAsTextFile("output1")
rdd2.saveAsTextFile("output2")
rdd3.saveAsTextFile("output3")
```



------

## 🎯 关键要点总结

| 算子类型 | 算子名称       | 主要功能       | 返回值类型 |
| :------- | :------------- | :------------- | :--------- |
| 转换算子 | map            | 逐条处理数据   | RDD        |
| 转换算子 | flatMap        | 处理并解除嵌套 | RDD        |
| 聚合算子 | reduce         | 数据聚合       | Python值   |
| 聚合算子 | reduceByKey    | 按key分组聚合  | RDD        |
| 过滤算子 | filter         | 条件过滤       | RDD        |
| 去重算子 | distinct       | 数据去重       | RDD        |
| 排序算子 | sortBy         | 数据排序       | RDD        |
| 输出算子 | collect        | 收集为列表     | List       |
| 输出算子 | take           | 取前N个        | List       |
| 输出算子 | count          | 统计数量       | Int        |
| 输出算子 | saveAsTextFile | 输出到文件     | 无         |

### 注意事项：

1. **链式调用**：对于返回值是新RDD的算子，可以通过链式调用多次处理
2. **全局排序**：使用sortBy进行全局排序时需要设置`numPartitions=1`
3. **分区控制**：可以通过配置或参数控制RDD的分区数
4. **环境配置**：需要正确配置Python和Hadoop环境路径
5. **数据倾斜**：reduceByKey可能遇到数据倾斜问题，需要注意优化