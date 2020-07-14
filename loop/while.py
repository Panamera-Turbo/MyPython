'''
while循环
'''
number = 0
while number < 5:
    print(number+10)
    number += 1

# 让用户选择何时退出
print('\n--------------------------------\n第一次实验')
a = '\n输入的内容会被重复'
a += '\nwq保存退出:'
message = ''
while message != 'wq':
    message = input(a)
    if message != 'wq':
        print(message)

print('--------------------------------\n第二次实验')
# 使用标志
active = True
a = '\n输入的内容会被重复'
a += '\nwq保存退出:'

while active:
    message = input(a)
    if message == 'wq':
        active = False
    else:
        print(message)

print('-----------------------------')
#break退出循环
#continue继续下一次循环