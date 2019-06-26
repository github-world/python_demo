'''
假设需要这样一个程序：

我们先向程序输入一个值x，再输入一个值y。(x,y)表示一个点的坐标。程序要告诉我们这个点处在坐标系的哪一个象限。

x>=0，y>=0，输出1；

x<0，y>=0，输出2；

x<0，y<0，输出3；

x>=0，y<0，输出4。

'''
x=int(input('please input x:'))
y=int(input('please input y:'))
if x >=0:
    if y>=0:
        print('坐标所在第一象限')
    else:
        print('坐标所在第四象限')
else:
    if y<0:
        print('坐标所在第三象限')
    else:
        print('坐标所在二象限')
