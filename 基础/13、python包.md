# Python 包与第三方包学习笔记

## 一、Python 包

### 1. 学习目标
- 了解什么是 Python 包
- 掌握如何自定义包

### 2. 什么是 Python 包？
- **物理结构**：一个包含 `__init__.py` 文件的文件夹，其中可包含多个模块文件。
- **逻辑本质**：包的本质依然是模块。
- **示例结构**：
    - my_package/
        - init.py
        - my_module1.py
        - my_module2.py
...


- **作用**：帮助管理多个模块文件，将相关模块组织在一起。

### 3. 快速入门
1. 新建包 `my_package`（Pycharm 中自动创建 `__init__.py`）。
2. 在包内创建模块（如 `my_module1.py`、`my_module2.py`）。
3. 编写模块代码：
 ```python
 # my_module1.py
 print(1)
 def info_print1():
     print('my_module1')
 
 # my_module2.py
 print(2)
 def info_print2():
     print('my_module2')
```
### 4. 导入包
方式一：import 包名.模块名
```python
import my_package.my_module1
import my_package.my_module2

my_package.my_module1.info_print1()
my_package.my_module2.info_print2()
```
方式二：from 包名 import *（需配置 `__all__`）
- 在 `__init__`.py 中设置允许导入的模块列表：

```python
__all__ = ["my_module2"]  # 仅允许导入 my_module2
```
- 使用：

```python
from my_package import *
my_module2.info_print2()  # 可调用
# my_module1.info_print1()  # 报错，不在 __all__ 列表中
```
<strong>注意</strong>：`__all__` 仅对 from ... import * 有效，对 import xxx 无效。

### 5. 总结
- Python 包：是一个包含多个模块的文件夹，通过 __init__.py 标识为包。

- `__init__`.py 作用：标识文件夹为 Python 包（非普通文件夹）。

- `__all__` 作用：控制 from ... import * 可导入的模块列表（与模块中的 `__all__` 功能一致）。

## 二、第三方包
### 1. 学习目标
- 了解什么是第三方包

- 掌握使用 pip 安装第三方包

### 2. 什么是第三方包？
- 非 Python 官方内置，由第三方提供的功能包。

- 作用：扩展 Python 功能，提高开发效率。

常见第三方包：

- 科学计算：numpy

- 数据分析：pandas

- 大数据计算：pyspark、apache-flink

- 图形可视化：matplotlib、pyecharts

- 人工智能：tensorflow

### 3. 安装第三方包 - pip
通过命令提示符使用 pip 安装：

```bash
pip install 包名称
```
网络优化（使用国内镜像源加速下载）：

```bash
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple 包名称
```
（清华大学镜像源示例）


### 4. 总结
第三方包：非官方内置，需安装后使用，可扩展功能。

安装方式：

- 命令行：pip install 包名称

- 使用国内镜像：pip install -i https://pypi.tuna.tsinghua.edu.cn/simple 包名称

- Pycharm 中也可直接安装（图形化操作）。