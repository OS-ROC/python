def str_reverse(s):
    '''
    功能：接收传入字符串，并将字符串反转返回
    :param s: 接收字符串
    :return: 返回经过处理的值
    '''
    return s[::-1]


def substr(s,start,end):
    '''
    功能：按照下表start和end，字符串进行切片
    :param s: 接收字符串
    :param start: 起点索引
    :param end: 终点索引
    :return: 返回按照[start，end]进行切片的值
    '''
    return s[start:end]


if __name__ == '__main__':    # 用于测试，若是通过其他文件导入，这里则不会运行
    print(str_reverse('hello world'))
    print(substr("hello world",5,10))

