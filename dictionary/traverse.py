'''
遍历
'''
language = {
    'web':'html+css+js',
    'data_base':'MySQL',
    'high-paid':'java',
    'total':3
}

for key, value in language.items():
    print('\n',key,':',value)
    
print('')
#字典里的字典的遍历
users = {
    'Sam':{
        'first':'sam',
        'last':'green',
        'loc':'5th.st'
    },
    'Dom':{
        'first':'dominic',
        'last':'toronto',
        'loc':'10th.r'
    }
}
for name, info in users.items():
    print('user:',name)
    print('  full name:',info['first'].title(),info['last'].title())
    print('  location:',info['loc'].upper())