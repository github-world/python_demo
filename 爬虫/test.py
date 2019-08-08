'''
def add(x,y):  #x,y 是形式参数
    return x+y
c=add(2-1,4-3)  #实际参数
d=add(4,5),add('a','n'),add([3],[4])

print(c,d)
'''
def add(x=4,y=5):
    return x+y
a =add(),add(x=5),add(y=7),add(6, 10),add(6, y=7),add(x=5, y=6),add(y=5, x=6)
b=add()
c= add(x=5,)

print(a)
print(b)
#add(x=5,6),add(y=8,4),add(11, x=20)  #报错么????
