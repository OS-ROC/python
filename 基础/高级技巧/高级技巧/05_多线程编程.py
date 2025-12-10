"""
演示多线程编程的使用
"""
import time
import threading

def sing(msg):
    while True:
        print(msg)
        time.sleep(1)


def dance(msg):
    while True:
        print(msg)
        time.sleep(1)

if __name__ == '__main__':
    # 创建一个唱歌的线程
    sing_thread = threading.Thread(target=sing,args=("我要唱歌 哈哈哈...",))
    # 创建一个跳舞的线程
    dance_thread = threading.Thread(target=dance,kwargs={"msg":"我在跳舞 啦啦啦..."})

    # 让线程开始工作
    sing_thread.start()
    dance_thread.start()