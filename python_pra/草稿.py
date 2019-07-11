'''
m=20
print('{:-^20}'.format(m))
print(m)
'''

d= ord(input())

for i in range(0,len(d)):
    if str[i] == '':
        print('',end='')
    elif str[i] in ['x','y','z']:
        print((ord(str)),end='')