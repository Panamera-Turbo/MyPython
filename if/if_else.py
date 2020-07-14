#判等运算符 == , !=
a = 'Audi'
print(a == 'audi')#Python大小写敏感
print(a != 'audi')
print(a.lower() == 'audi','\n')


#且 --> and
#或 --> or
a = 9
print(a <= 10 and a > 0)
print(a >0 or a == -1)

cars = ['audi', 'BMW', 'porsche', 'ducati', 'farrari', 'VW', 'bugatti']

# 检查特定值是否在列表/元组等中
if 'audi' in cars:
    print('in')
if 'AUDI' not in cars:
    print('none')

#else if简写为elif
if 'VW' not in cars:
    print('Porsche NO.1')
elif 'das auto' in cars:
    print('great')
else:
    print('Dad is dad') 