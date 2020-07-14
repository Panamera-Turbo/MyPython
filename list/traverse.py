'''
循环
'''

# 用for循环打印
cars = ['audi', 'BMW', 'porsche', 'ducati', 'farrari', 'VW', 'bugatti']
for car in cars:
    #注意，不要遗漏冒号
    print(car.upper())#car是临时变量，随便取，这样便于理解而已
    print(car.title() , "is a(n) nice car\n")

print("That's all. Thanks")#注意缩进
print('------------------------------------------')
#数值列表

#range(a,b,c) 从a开始，步长c，递增至大于等于b停止（不含b），生成数字
#若没有c，默认c = 1
for value in range(0,5,2):
    print(value)#不会打印5
#list(range(a,b，c)) 置换为列表[a,a+1,...,b-1]
numbers = list(range(0,6))
print(numbers)
#一种简略写法
squares = [new_value**2 for new_value in range(1,11,1) ]
print(squares)
