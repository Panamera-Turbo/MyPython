'''
Python的元组与列表类似，不同之处在于元组的元素不能修改。
元组使用小括号，列表使用方括号。
'''

# 创建
# 元组创建很简单，只需要在括号中添加元素，并使用逗号隔开即可
cars = ('audi', 'BMW', 'porsche', 'ducati')
print(cars)
#若修改，会报错
# cars[2] = 'VW'

#遍历类似于list。略

# 元组不可修改，但是存储元组的变量可以被直接赋值，例如
cars = ('cars_ALREADY_changed')
print("\n",cars)
