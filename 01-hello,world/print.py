'''
运行：
方法一：python3 hello_world.py
方法二：直接点击右边那个三角运行
'''

print("hello,MOTHER_FUCKER!!!!!!")
print("hello,world\n"*2)
# print('skfh')
print(8878*8989)

a = 10 
a = 9
b = 9
print(a + b)
print(a**2)#乘方运算：**
a = "hello"
b = "WORLD"     #变量不强调类型
c = "pYTHON"

#拼接字符串,+
full_name = a.upper() + "," + b.lower() + "," + c.title()
#全大写,全小写，仅大写首字母
print(full_name)
d = " " +full_name + " "
print(d.rstrip())   #删除末尾空白
print(d.lstrip())   #删除开头空白
print(d.split())    #删除两端空白


print("'hello'")#打印含引号的内容

#查看类型
a = True    #bool
b = []      #列表
c = {}      #字典
d = "sfsf"  #字符串
print(type(a), type(b), type(c), type(d))#逗号分隔