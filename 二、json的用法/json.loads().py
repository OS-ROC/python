import json

from matplotlib.font_manager import json_load

# 创建JSON数据
json_data = '{"name": "curry" , "age": "18","city": "Golden"}'
print(json_data)

# 将JSON数据解析为python对象
data = json.loads(json_data)
print(data)



# 在上面的示例中，我们首先定义了一个包含JSON数据的字符串json_data。
# 然后，我们使用json.loads()函数将JSON数据解析为Python对象。
# 最后，我们打印Python对象以进行验证。