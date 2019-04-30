import json
# 原始数据
dict1 = {
    'name': '翠花',
    'age': 18,
    'nickname': 'GreenFlower',
}
print("原始数据类型为："+str(type(dict1)))
 
# 将字典转换为JSON格式的字符串
t1 = json.dumps(dict1, ensure_ascii=False)
print("字典转JSON后数据类型为："+str(type(t1)))
print(t1)
 
# 将JSON格式的字符串转化为字典
t2 = json.loads(t1)
print("JSON转字典后数据类型为："+str(type(t2)))
print(t2)

# 将字典转换为JSON格式的字符串，并将转化后的结果写入文件
filename = 'test1.json'
with open(filename, 'w', encoding='UTF-8') as f:
    json.dump(dict1, f, ensure_ascii=False)
 
# 从文件读取JSON格式的字符串，并将其转化为字典
with open(filename, 'r', encoding='UTF-8') as f:
    aa = json.load(f)
    print("读取JSON文件中的内容：")

