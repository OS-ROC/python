'''
## 版本1

import random

num = random.randint(1,100)

guess_num = int(input("请输入你猜的数字："))
i = 1
while guess_num != num:
    if guess_num > num:
        print("你猜大了")
    else:print("你猜小了")
    guess_num = int(input("请继续输入你猜的数字："))
    i += 1
    if guess_num == num:
        print(f"恭喜你猜对了,总共猜了{i}次。")

'''


## 版本2

# import random
# num = random.randint(1,100)
# count = 0
# flag = True
# while flag:
#     guess_num = int(input("请输入你猜的数字："))
#     count += 1
#     if guess_num == num:
#         print("恭喜你，答对了!总共猜了{}次".format(count))
#         flag = False
#     else:
#         if guess_num > num:
#             print("猜大了。")
#         else:
#             print("猜小了")











