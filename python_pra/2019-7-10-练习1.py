'''
#eval() 函数用来执行一个字符串表达式,并返回表达式的值。
eval(expression[, globals[, locals]])
参数
expression -- 表达式。
globals -- 变量作用域,全局命名空间,如果被提供,则必须是一个字典对象。
locals -- 变量作用域,局部命名空间,如果被提供,可以是任何映射对象。
#pow() 方法返回 xy（x的y次方） 的值。




n = eval(input())
m=pow(n,2)
if len('m')<=20:
    print('{:-^20}'.format(m))#正则表达式,有些看不懂,但是功能还是没毛病的。
else:
    print(m)
#13	{:^10d}	    13	中间对齐 (宽度为10)
'''
#天天向上的力量
a = eval(input())
b = pow(1+a*0.001,365)
c = pow(1-a*0.001,365)
d=int(b/c)
print("{:.2f},{:.2f},{}".format(a,b,c,d))