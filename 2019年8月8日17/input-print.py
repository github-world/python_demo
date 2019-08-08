def print_line():
    print('-'*50)
#输入和输出
print('hello,world')
#msg=input('pls enter:')
print('input msg:','hello,world')
print('----------------------')
#如何定义变量类型
# python 一切都是对象，pi与msg都是对象
num= 2
pi = 3.14
msg = 'goodluck'
#打印变量值与类型，type函数返回对象类型
print(pi,type(pi)) #浮点型
print(msg,type(msg)) #字符串
print(num,type(num)) #整数型
print_line()  #直接引用分割线函数
# 变量赋值形式？
score = 90
a=b=c=10
c=a+c
print(a+b,c)
#如何查看变量地址？ 使用id(x)
print(c)
print(id(a),id(b),id(c))
# 修改某个变量的值
c=8
print(a,b,c)
print(id(a),id(b),id(c))

print('''score''')
print_line()
#转义符
print(''' \'/\'' ''')
print('1\n2')
print('3\r4')
print('5\t6','5\t6')  #横向
print('7\v8','9\v10','9\v10')  #纵向

print_line()
#逻辑运算符and or not
a=1
b=2
print(a and b) #2

print(a and False and b) #2
print(a or b) #2
print(b or True or a) #2
print(a and True or  b) #2
print(not  a) #flase
