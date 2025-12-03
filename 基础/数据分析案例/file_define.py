"""
和文件相关的类定义
"""
import json

from data_define import Record


# 先定义一个抽象类用来做顶层设计，确定有哪些功能需要实现
class FileReader:
    def read_data(self) -> list[Record]:
        """读取文件的数据，读到的每一条数据都转换为Record对象，将他们都封装到list内返回即可"""
        pass

class TextFilReader(FileReader):
    def __init__(self,path):
        self.path = path

    def read_data(self) -> list[Record]:
        f = open(self.path,"r",encoding="utf-8")
        record_list:list[Record] = []
        for line in f.readlines():
            line = line.strip()
            data_list = line.split(",")
            record = Record(data_list[0],data_list[1],int(data_list[2]),data_list[3])
            record_list.append(record)

        f.close()
        return record_list


class JsonFilReader(FileReader):
    def __init__(self,path):
        self.path = path

    def read_data(self):
        f = open(self.path,"r",encoding="utf-8")
        record_list:list[Record] = []
        for line in f.readlines():
            data_dict = json.loads(line)
            record = Record(data_dict["date"],data_dict["order_id"],int(data_dict["money"]),data_dict["province"])
            record_list.append(record)

        f.close()
        return record_list



if __name__ == '__main__':
    # a = TextFilReader(r"D:\数据分析\课件资料\资料\第13章资料\2011年1月销售数据.txt")
    # list1 = a.read_data()
    # for record in list1:
    #     print(record)

    b = JsonFilReader(r"D:\数据分析\课件资料\资料\第13章资料\2011年2月销售数据JSON.txt")
    list2 = b.read_data()
    for record in list2:
        print(record)
