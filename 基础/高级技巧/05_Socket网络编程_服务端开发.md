# Socket网络编程

## 学习目标

1. 了解什么是Socket网络编程
2. 基于Socket完成服务端程序开发

------

## 什么是Socket？

**Socket（简称套接字）** 是进程之间通信的一个工具，好比现实生活中的插座，所有的家用电器要想工作都是基于插座进行，进程之间想要进行网络通信需要Socket。

Socket负责进程之间的网络数据传输，好比数据的搬运工。

text

```
进程1    ───传输数据───>    socket    ───>    socket    ───>    进程2
```



大多数软件都使用到了Socket进行网络通讯。

------

## 客户端和服务端

两个进程之间通过Socket进行相互通讯，就必须有服务端和客户端。

- **Socket服务端**：等待其它进程的连接、可接受发来的消息、可以回复消息
- **Socket客户端**：主动连接服务端、可以发送消息、可以接收回复

text

```
    客户端
       │
       ├───> 服务端 <───┐
       │               │
    客户端              客户端
```



------

## Socket服务端编程

### 主要步骤：

#### 1. 创建socket对象

python

```
import socket
socket_server = socket.socket()
```



#### 2. 绑定socket_server到指定IP和端口

python

```
socket_server.bind(('127.0.0.1', 8888))
# 或
socket_server.bind(("localhost", 8888))
```



#### 3. 服务端开始监听端口

python

```
socket_server.listen(1)
# listen方法内接受一个整数化参数，表示接受的连接数量
# backlog为int整数，表示允许的连接数量，超出的会等待，可以不填，不填会自动设置一个合理值
```



#### 4. 接收客户端连接，获得连接对象

python

```
conn, address = socket_server.accept()
print(f"接收到客户端连接，连接来自: {address}")

# accept方法是阻塞方法，如果没有连接，会卡在当前这一行不向下执行代码  
# accept返回的是一个二元元组，可以使用上述形式，用两个变量接收二元元组的2个元素  
# 可以通过变量1、变量2 = socket_server.accept()的形式，直接接受二元元组内的两个元素
```



#### 5. 客户端连接后，通过recv方法，接收客户端发送的消息

python

```
while True:
    data = conn.recv(1024).decode("UTF-8")
    # recv方法的返回值是字节数组（Bytes），可以通过decode使用UTF-8解码为字符串
    # recv方法的传参是buffsize，缓冲区大小，一般设置为1024即可
    if data == 'exit':
        break
    print("接收到发送来的数据:", data)
    # 可以通过while True无限循环来持续和客户端进行数据交互
    # 可以通过判定客户端发来的特殊标记，如exit，来退出无限循环
```



#### 6. 通过conn（客户端当次连接对象），调用send方法回复消息

python

```
while True:
    data = conn.recv(1024).decode("UTF-8")
    if data == 'exit':
        break
    print("接收到发送来的数据:", data)
    
    # 发送回复信息
    msg = input("请输入回复消息: ")
    # encode可以将字符串编码为字节数组对象
    conn.send(msg.encode("UTF-8"))
```



#### 7. 关闭连接

python

```
conn.close()
socket_server.close()
```



------

## 完整服务端开发示例（包含详细注释）

### 示例1：演示Socket服务端开发

python

```
import socket

# 创建Socket对象
socket_server = socket.socket()
# 绑定IP地址和端口
socket_server.bind(('127.0.0.1', 8888))
# 监听端口
socket_server.listen(1)
# listen方法内接受一个整数化参数，表示接受的连接数量

# 等待客户端链接
# result:tuple = socket_server.accept()
# conn = result[0] # 客户端和服务端的连接对象
# address = result[1] # 客户端的地址信息
conn, address = socket_server.accept()
# accept方法返回的是二元元组（连接对象、客户端地址信息）
# 可以通过变量1、变量2 = socket_server.accept()的形式，直接接受二元元组内的两个元素
# accept()方法，是阻塞的方法。等待客户端链接，如果没有链接，就卡在这一行不向下执行了

print(f"接受到了客户端的连接，客户端的信息是：{address}")
while True:
    # 接受客户端信息，要使用客户端和服务端的本次连接对象，而非socket_server对象
    data:str = conn.recv(1024).decode("utf-8")
    # recv接受的参数是缓冲区大小，一般给1024即可
    # recv方法的返回值是一个字符数组也就是bytes对象，不是字符串，可以通过decode方法通过UTF-8编码，将字符数组转换为字符串对象
    print(f"客户端发送的消息是：{data}")
    # 发送回复信息
    msg = input("请输入你要和客户端回复的消息。")
    if msg == "exit":
        break
    conn.send(msg.encode("utf-8"))
    # encode可以将字符串编码为字节数组对象
    
# 关闭链接
conn.close()
socket_server.close()
```



### 示例2：实现服务端并结合客户端进行测试

python

```
import socket

# 创建Socket对象
socket_server = socket.socket()
# 绑定本地主机和端口8888
socket_server.bind(("localhost", 8888))
# 监听端口，允许1个连接
socket_server.listen(1)
# 接受客户端连接
conn, address = socket_server.accept()

print(f"接收到客户端连接，连接来自: {address}")

while True:
    # 接收客户端数据，每次最多1024字节
    data = conn.recv(1024).decode("UTF-8")
    # 如果客户端发送exit，则退出循环
    if data == 'exit':
        break
    print("接收到发送来的数据: ", data)
    # 获取用户输入的回复消息
    reply = input("请输入回复消息: ").encode("UTF-8")
    # 发送回复给客户端
    conn.send(reply)

# 关闭连接
conn.close()
socket_server.close()
```



**运行结果示例：**

text

```
接收到客户端连接，连接来自: ('127.0.0.1', 2334)
接收到发送来的数据: 保持连接
请输入回复消息: 保持连接
接收到发送来的数据: 今天不想上课
请输入回复消息: 明天必须来
接收到发送来的数据: 封锁，触发会持续
请输入回复消息: OK

Process finished with exit code 0
```



------

## 客户端工具推荐

可以使用网络调试助手作为客户端进行测试：

**下载地址**：

- GitHub: https://github.com/nicedayzhu/netAssist/releases

------

## 总结

### 1. 什么是Socket？

Socket（简称套接字）是进程之间通信的一个工具。

### 2. 什么是服务端、客户端？

- **服务端**：等待连接、接收消息、回复消息
- **客户端**：主动连接、发送消息、接收回复

### 3. Socket服务端编程关键点

1. `accept()` - 阻塞方法，等待客户端连接
2. `recv(1024)` - 接收数据，返回字节数组，需解码
3. `decode("UTF-8")` - 将字节数组解码为字符串
4. `send()` - 发送数据，需先将字符串编码为字节数组
5. `encode("UTF-8")` - 将字符串编码为字节数组
6. `close()` - 关闭连接，释放资源
7. 通过特殊标记（如'exit'）控制通信结束

### 4. 编程步骤总结

1. 创建Socket对象 → `socket()`
2. 绑定IP和端口 → `bind()`
3. 开始监听 → `listen()`
4. 接受连接 → `accept()`
5. 接收和发送消息 → `recv()` / `send()`
6. 关闭连接 → `close()`