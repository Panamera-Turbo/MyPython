# 字典是另一种可变容器模型，且可存储任意类型对象。

# 字典的每个键值对(key=>value)对用冒号(:)分割，每个对之间用逗号(,)分割，
# 整个字典包括在花括号{}中 ,格式为：
# d = {key1 : value1, key2 : value2 }

# 键必须是唯一的，但值则不必。
# 值可以取任何数据类型，但键必须是不可变的，如字符串，数字或元组。

print('')
#创建
cars = {
    'Sport':'Porsche',
    'Business':'audi'
}
#访问
print(cars['Sport'])
#添加
cars['Expensive'] = 'Bentley'
print(cars)
#删除
del cars['Expensive']
print(cars)
