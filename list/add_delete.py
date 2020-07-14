'''
方括号表示列表[]
逗号用来分隔元素
通常列表命名选择用复数，如letters，words，names等等
'''

names = ["C", "cpp", "java", "python"]
print(names)
#直接打印会直接打印列表，包括括号
print(names[0])
#访问第i个元素：list[i]
print(names[1].title())
print(names[-2].upper())#会打印JAVA
#负数表示倒数第n个
print("-------------添加-----------------")
#添加元素
cars = []
# list.append(内容) -->加到列表尾
cars.append("audi")
cars.append("porsche")
print(cars)
# list.insert(位置，内容) -->加到任意位置
cars.insert(0,"BMW")
print(cars)
print("-------------删除-----------------")
#删除元素
#del list[i] -->删除第i个
del cars[0]
print(cars)
#pop() 弹出。可以被继续访问
#【1】list.pop(),默认弹出列表尾
#【2】list.pop(i)，弹出元素list[i]
language = names.pop()
print(language)
language = names.pop(0)
print(language)
print(names)
#remove 根据值删除元素
#list.remove(待删除的值)
names.remove("cpp")
print(names)
print('-------------长度------------------')
#求长度：len(list)
print(names)
print("长度为",len(names))
print('-------------------------------')

