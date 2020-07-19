# 从另一个.py模块导入,无后缀py
import func1

fullname = func1.getName('Ethan','Hunt')
print(fullname)

#只导入另外.py的一个函数:from 文件 import 函数
#导入所有函数:from 文件 import *
from func2 import setPrice

car={'brand':'audi'}
setPrice(car,400000)
print(car)

#给函数指定别名：from 文件 import 函数 as 别名
from func2 import getPrice as get 

price = get(car)
print(price)

