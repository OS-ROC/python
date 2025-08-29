

'''


## 打印九九乘法表
i = 1
# 外循环定义行数
while i <= 9:
    j = 1

    # 内循环定义每一行有多少个元素
    while j <= i:
        print(f"{j}*{i}={j*i}\t",end='')   # 把每一行的内容打印出来，\t表示两个元素之间的间隔，也可以用空格代替，end则是为了使其不换行输出

        j += 1   # 当j不再<=i时跳出内循环
    i += 1
    print()  # 实现一个换行功能

'''


## 打印九九乘法表(使用continue)

# for i in range(1,10):
#
#     for j in range(1,10):
#         if j <= i:
#             print(f"{j}*{i}={j*i} ",end='')
#         else:
#             continue
#
#
#     print()

## 打印九九乘法表
for i in range(1, 10):

    for j in range(1, i+1):

        print(f"{j}*{i}={j * i} ", end='')


    print()


