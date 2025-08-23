import json

# 定义一个包含键值对的python字典
data = {
    "name": 'kevin',
    "age": 18,
    "city": "Seattle"
}
print(data)

# 将python字典转换为JSON字符串
json_data = json.dumps(data)
print(json_data)



# 在上面的示例中，我们首先定义了一个包含键值对的Python字典data。
# 然后，我们使用json.dumps()函数将Python字典转换为JSON字符串，
# 并将其保存在变量json_data中。
# 最后，我们打印JSON字符串以进行验证。