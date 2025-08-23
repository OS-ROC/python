# Python 库管理常用命令

## 1. 安装库

- 单个库安装命令：

  ```bash
  pip install requests
  ```

- 批量安装库：

  1. 新建一个 txt 文件（例如在桌面创建 `要安装的库.txt`）。
  2. 在 txt 文件中添加需要安装的库名，每行一个，例如：

     ```
     bs4
     requests
     ```

  3. 执行批量安装命令：

     ```bash
     pip install -r C:\Users\Ms-xiao\Desktop\要安装的库.txt
     ```

## 2. 库的卸载

- 单个库卸载命令：

  ```bash
  pip uninstall bs4
  ```

  输入 `y` + 回车键确认卸载，`n` 取消卸载。

- 直接卸载（跳过询问）：

  ```bash
  pip uninstall -y bs4
  ```

- 批量卸载库：

  1. 新建一个 txt 文件，把要删除的库名放入其中（每行一个）。
  2. 执行批量卸载命令：

     ```bash
     pip uninstall -y -r C:\Users\Ms-xiao\Desktop\要删除的库.txt
     ```

## 3. 帮助信息

- 查看 pip 命令的用法：

  ```bash
  pip -h
  # 或者
  pip --help
  ```

## 4. 查看已安装的第三方库

```bash
pip list
```

## 5. 显示 pip 的版本

```bash
pip --version
```

## 6. 库的版本升级

- 完整命令：

  ```bash
  pip install --upgrade 库名
  ```

- 简写形式：

  ```bash
  pip install -U 库名
  ```

- 例如升级 pip 本身：

  ```bash
  pip install --upgrade pip
  ```

## 7. 导出已安装的库列表

- 将已安装的库列表保存到桌面文件：

  ```bash
  pip freeze > C:\Users\Ms-xiao\Desktop\我的python库.txt
  ```

## 8. 显示已安装包的详细信息

```bash
pip show -f