### 一、Spark 与 PySpark 基础

1. **Spark 定义**Apache Spark 是用于**大规模数据处理**的统一分析引擎，是分布式计算框架，可调度集群处理 TB/PB 级数据（2009 年源于 UC Berkeley）。
2. **PySpark 定义**Spark 官方提供的 Python 第三方库，是 Spark 的 Python 实现：

- 可作为 Python 库直接使用；

- 也可将程序提交到 Spark 集群，实现分布式计算。

  

### 二、PySpark 环境准备

1. 安装 PySpark

```bash
# 直接安装
pip install pyspark
# 清华镜像加速
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pyspark
```

1. 构建执行环境入口对象（SparkContext）

   使用 PySpark 需先创建SparkContext对象（程序入口）

```python
# 导包
from pyspark import SparkConf, SparkContext
# 创建配置对象：设置运行模式（local[*]表示本地多线程）、应用名
conf = SparkConf().setMaster("local[*]").setAppName("test_spark_app")
# 创建SparkContext对象
sc = SparkContext(conf=conf)
# 打印PySpark版本
print(sc.version)
# 停止程序
sc.stop()
```

### 三、PySpark 编程模型

PySpark 编程分为**3 大步骤**，核心载体是**RDD 对象**：

1. 数据输入：通过`SparkContext`的方法读取数据，得到 RDD 对象；
2. 数据处理计算：调用 RDD 的成员方法，实现各类计算（返回值仍是 RDD）；
3. 数据输出：调用 RDD 的方法，完成数据写出（文件、数据库）或转换为 Python 数据类型。

### 四、RDD 对象

1. RDD 定义

   RDD（弹性分布式数据集）是 PySpark 的数据载体：

- 存储数据；
- 提供数据计算方法；
- 计算方法的返回值仍是 RDD（支持链式调用）。

1. **获取 RDD 对象的 2 种方式**

- 方式 1：Python 数据容器转 RDD

  

  通过SparkContext.parallelize()方法，将 list/tuple/set/dict/str 转换为 RDD：

```python
rdd = sc.parallelize(数据容器对象)
# 输出RDD内容（转为Python列表）
print(rdd.collect())
```

注意：字符串会拆分为单个字符；字典仅保留 key。

- 方式 2：读取文件转 RDD

  通过SparkContext.textFile()方法，读取文本文件：

```python
rdd = sc.textFile("文件路径")
# 输出RDD内容
print(rdd.collect())
```