# age_list.append(31)   # 向列表末尾添加单个元素
# age_list.extend([29,33,30]) # 向列表末尾添加多个元素
# print(age_list[0])    # 打印列表第一个元素，索引为0
# print(age_list[-1])   # 打印列表最后一个元素，索引为-1
# index = age_list.index(31)  # 把元素第一次出现在列表的索引赋值给index
# print(index)  # 打印索引


## 用while循环和for循环取出一个列表中的偶数
my_tlist = [1,2,3,4,5,6,7,8,9,10]   # 定义一个列表

# 定义while循环函数
def list_while(lst):
    '''

    :param lst: lst当作形参，用来接收列表my_list
    :return: 将新列表返回，在外面用一个变量接收
    '''

    index = 0   # 定义列表下表初始值为0
    new_list = []  # 定义一个空列表，用于接收偶数值
    while index < len(lst):   # len(lst)表示接收列表的长度
        if lst[index] % 2 == 0:   # 用于判断偶数
            new_list.append(lst[index])   # append方法将值添加到新列表
        index += 1  # 下表加1
    return new_list

def list_for(lst):
    '''

    :param lst: lst当作形参，用来接收列表my_list
    :return: 将新列表返回，在外面用一个变量接收
    '''
    new_list = []
    for element in lst:  # element中的值就是列表中的值
        if element % 2 == 0:
            new_list.append(element)  ## append方法将值添加到新列表
    return new_list

# 用变量接收函数返回值，并打印
a = list_while(my_tlist)
print("通过while循环，从列表：[1,2,3,4,5,6,7,8,9,10]中取出偶数，组成新列表：%s"%a)
b = list_for(my_tlist)
print("通过for循环，从列表：[1,2,3,4,5,6,7,8,9,10]中取出偶数，组成新列表：%s"%b)
