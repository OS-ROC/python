def print_file_info(filename):
    '''
    功能：打开一个文件，读取其内容；若文件不存在，则捕获异常，输出提示信息
    :param filename: 接收传入文件的路径
    :return: None
    '''
    f = None    # 初始化f为None
    try:
        f = open(filename,'r',encoding='utf-8')
        content = f.read()
        print(content)
    except Exception as e:   # 捕获所有异常
        print(e)

    finally:
        if f:   # 如果文件不存在，f为None(即False)，则不进入if语句
            f.close()   # 关闭文件
            print("-------------------")
            print("文件已关闭。")


def append_to_file(filename,data):
    '''
    功能：将传入的数据追加到一个文件中，若文件不存在则创建文件并传入
    :param filename: 接收传入文件的路径
    :param data: 接收传入数据
    :return: None
    '''
    with open(filename,'a',encoding='utf-8') as f:    # 这里使用with open不需要使用close或flush来关闭文件或刷新将数据存入硬盘
        f.write(data)


if __name__ == '__main__':    # # 用于测试，若是通过其他文件导入，这里则不会运行

    print_file_info('../bill1.txt')
    append_to_file('1.txt',"123")

