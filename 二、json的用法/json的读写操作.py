import json

data = {
    "name": "durant",
    "age": 19,
    "city": "seattle",
    "$number": 123,
    "$array": [1,2,3,4]
}

# 写入JSON数据
with open('test.json','w') as f:
    json.dump(data, f)

# 读取数据，解析test.json文件并返回到python字典然后将其打印出来
with open('test.json','r') as f:
    data = json.load(f)
    print(data)