# Socket客户端编程

## 学习目标

基于Socket完成客户端程序开发

------

## Socket客户端编程步骤

### 主要分为以下几个步骤：

#### 1. 创建socket对象

python

```
import socket
socket_client = socket.socket()
```



#### 2. 连接到服务端

python

```
socket_client.connect(("localhost", 8888))
# 或
socket_client.connect(('127.0.0.1', 8888))
```



#### 3. 发送消息

python

```
while True:    # 可以通过无限循环来确保持续的发送消息给服务端
    send_msg = input("请输入要发送的消息")
    if send_msg == 'exit':
        # 通过特殊标记来确保可以退出无限循环
        break
    socket_client.send(send_msg.encode("UTF-8"))    # 消息需要编码为字节数组（UTF-8编码）
```



#### 4. 接收返回消息

python

```
while True:
    send_msg = input("请输入要发送的消息").encode("UTF-8")
    socket_client.send(send_msg)
    
    recv_data = socket_client.recv(1024)    # 1024是缓冲区大小，一般1024即可
    # recv方法是阻塞式的，即不接收到返回，就卡在这里等待
    print("服务端回复消息为：", recv_data.decode("UTF-8"))    # 接受的消息需要通过UTF-8解码为字符串
```



#### 5. 关闭链接

python

```
socket_client.close()    # 最后通过close关闭链接
```



------

## 完整客户端开发示例

python

```
import socket

# 创建socket对象
socket_client = socket.socket()

# 连接到服务器
socket_client.connect(('127.0.0.1', 8888))

while True:
    # 发送消息
    msg = input("请输入要给服务端发送的消息: ")
    if msg == "exit":
        break
    socket_client.send(msg.encode("utf-8"))
    
    # 接收返回消息
    recv_data = socket_client.recv(1024)    # 1024是缓冲区的大小，一般1024即可，同样recv方法是阻塞的
    print(f"服务端回复的消息是: {recv_data.decode('utf-8')}")

# 关闭连接
socket_client.close()
```



------

## 客户端编程关键点总结

### 1. 创建和连接

- `socket()` - 创建socket对象
- `connect()` - 连接到指定的服务端地址和端口

### 2. 发送消息

- `send()` - 发送数据到服务端
- 需要先使用 `encode("UTF-8")` 将字符串编码为字节数组

### 3. 接收消息

- `recv(1024)` - 从服务端接收数据，参数是缓冲区大小
- recv方法是**阻塞式**的，没有接收到数据时会一直等待
- 需要使用 `decode("UTF-8")` 将接收到的字节数组解码为字符串

### 4. 流程控制

- 可以使用 `while True` 循环实现持续通信
- 通过特殊标记（如 'exit'）来控制退出循环
- 最后需要调用 `close()` 方法关闭连接

### 5. 注意事项

1. 连接前确保服务端已启动并监听对应端口
2. 发送和接收数据时注意编码解码的一致性（通常使用UTF-8）
3. recv方法是阻塞的，设计时要考虑用户体验
4. 使用完socket后要及时关闭连接释放资源

------

## 客户端与服务端对比

| 步骤 | 服务端             | 客户端              |
| :--- | :----------------- | :------------------ |
| 1    | 创建socket对象     | 创建socket对象      |
| 2    | 绑定IP和端口(bind) | 连接服务端(connect) |
| 3    | 开始监听(listen)   | 发送消息(send)      |
| 4    | 接受连接(accept)   | 接收回复(recv)      |
| 5    | 接收消息(recv)     | 关闭连接(close)     |
| 6    | 发送回复(send)     |                     |
| 7    | 关闭连接(close)    |                     |

通过这种客户端-服务端模式，可以实现两个进程之间的双向网络通信。