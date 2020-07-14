names = ['cpp', 'c', 'c#', 'java', 'python', 'php']
print(names)

#永久排序
#list.sort() 字典序
#list.sort(reverse=True) 反字典序
names.sort()
print(names)
names.sort(reverse=True)
print(names)
print('-------------------------------------------------')
#临时排序
#sorted(list)
print(sorted(names))
print('-------------------------------------------------')
#倒序
#list.reverse()
#改变时永久的，若需在此恢复，只需再倒序一次
names = ['cpp', 'c', 'c#', 'java', 'python', 'php']
print("origin order:", names)
names.reverse()
print("changed order", names)