'''
这一章学习如何处理部分元素
'''

cars = ['audi', 'BMW', 'porsche', 'ducati', 'farrari', 'VW', 'bugatti']
#打印指定片段
#list[a:b]从a到b号（从0开始计数，不处理b）。如果没有a，默认a=0;没有b，默认到结尾
print(cars[2:5])
#['porsche', 'ducati', 'farrari']
print(cars[:6])
#['audi', 'BMW', 'porsche', 'ducati', 'farrari', 'VW']
print(cars[:])
#全部打印
print(cars[-3:])
#灵活运用负索引。['farrari', 'VW', 'bugatti']

print('----------------------------------------')

#遍历切片
for car in cars[4:8]:
    print(car)

#复制列表
new_cars = cars[:]
print(cars)
print(new_cars)