# PyMySQL 使用指南



## 1. 简介

除了使用图形化工具，我们可以使用编程语言来执行 SQL 以操作数据库。在 Python 中，可以使用第三方库 `pymysql` 来完成对 MySQL 数据库的操作。



## 2. 安装

```bash
pip install pymysql
```



## 3. 连接数据库

使用以下代码创建与 MySQL 的数据库连接：

python

```
from pymysql import Connection

# 获取到 MySQL 数据库的连接对象
conn = Connection(
    host='localhost',    # 主机名（或 IP 地址）
    port=3306,           # 端口，默认 3306
    user='root',         # 账户名
    password='123456'    # 密码
)

# 打印 MySQL 数据库软件信息
print(conn.get_server_info())

# 关闭数据库连接
conn.close()
```



## 4. 执行 SQL 语句

### 4.1 执行非查询 SQL（如建表）

python

```
from pymysql import Connection

# 获取到 MySQL 数据库的连接对象
conn = Connection(
    host='localhost',
    port=3306,
    user='root',
    password='123456'
)

# 获取游标对象
cursor = conn.cursor()
conn.select_db("test")    # 先选择数据库

# 使用游标对象执行 SQL 语句
cursor.execute("CREATE TABLE test_pymysql(id INT, info VARCHAR(255))")

# 关闭数据库连接
conn.close()
```



### 4.2 执行插入操作与 commit 提交

默认情况下，`pymysql` 在执行插入、更新、删除等操作时**不会自动提交**，需要通过 `commit()` 确认更改。

python

```
from pymysql import Connection

# 构建到 MySQL 数据库的链接
conn = Connection(
    host="localhost",
    port=3306,
    user="root",
    password="123456"
)

cursor = conn.cursor()
conn.select_db("world")

# 执行插入 SQL
cursor.execute("INSERT INTO student VALUES(10001, '周杰轮', 31, '男')")

# 提交更改
conn.commit()

conn.close()
```



### 4.3 设置自动提交

可以在创建连接时设置 `autocommit=True` 来避免手动提交：

python

```
conn = Connection(
    host="localhost",
    port=3306,
    user="root",
    password="123456",
    autocommit=True  # 设置自动提交
)
```



## 5. 执行 SQL 查询

python

```
# 获取游标对象
cursor = conn.cursor()

# 执行查询
cursor.execute("SELECT * FROM student")

# 获取全部查询结果（元组形式）
results = cursor.fetchall()
print(results)
```



## 6. 总结

1. **Python 中操作 MySQL 的第三方库**：`pymysql`

2. **安装方式**：`pip install pymysql`

3. **获取连接对象**：

   python

   ```
   from pymysql import Connection
   conn = Connection(host, port, user, password)
   ```

   

4. **执行 SQL**：

   - 获取游标：`cursor = conn.cursor()`
   - 执行语句：`cursor.execute(sql)`
   - 查询结果：`cursor.fetchall()`

5. **提交更改**：

   - 手动提交：`conn.commit()`
   - 自动提交：创建连接时设置 `autocommit=True`

## 7. 示例 DDL

本次示例中需要创建一个名为 `py_sql` 的数据库，并创建 `orders` 表：

sql

```
CREATE TABLE orders(
    order_date DATE,
    order_id VARCHAR(255),
    money INT,
    province VARCHAR(10)
);
```



------

**注意**：实际使用中请替换主机、端口、用户名、密码和数据库名为你自己的配置。