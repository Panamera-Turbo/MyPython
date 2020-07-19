'''
函数
'''
#定义函数
def hello(user):
    print('\nhello,world,',user)

user = 'chase'
hello(user.title())

#传递参数
#传递参数时，可以像C语言一样
def MyCar(name,car):
    print(car.title(),'belongs to',name)

MyCar('Tom','audi')

# 还可以依照关键字直接传递
MyCar(car='porsche',name='Susan')

#参数可以有默认值,且有默认值的参数位置放在最后
#为了使参数是可选的，可以先给形参指定一个默认的空值
# *varies 将创建一个元组，来接受任意数量的实参
def MyChoice(name,*cars,choice=True,food='cake',addition=''):
    if(choice):
        print(name,'will buy:')
        for car in cars:
            print(car)
        print(food,addition)

MyChoice('Ethan','audi','porsche')

#函数的返回值用return返回
def getFullName(first_name,last_name):
    person={'first name':first_name, 'last name':last_name}
    return person

FullName=getFullName('Ethan','Hunt')
print(FullName['first name'].title())