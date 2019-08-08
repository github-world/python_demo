'''
字符串和list之间有很多不得不说的事。比如有同学想要用python去自动抓取某个网页上的下载链接,那就需要对网页的代码进行处理。处理的过程中,免不了要在字符串和list之间进行很多操作。
'''
sentence = ' you can do best , because , good good study , day day up '
print(sentence.split())
'''
join则是把一个list中的所有字符串连接成一个字符串。
'''
list1=['google','baidu','sougou','yaoohu'];
list2=[1,2,3,4,5];
list3=['a','b','c','d'];
#访问列表中的值
print('list1[0]:',list1[0])
print(list2[2:4])
#更新list1里面的第三个值为 sina
print('list1里面第三个值为:',list1[2])
list1[2]='sina'
print('list1更新后第三个值为：',list1[2])
#删除最后一条信息
print('list1最后一条信息为:',list1)
del list1[3]
print('list1最后一条信息已删除',list1)
#python列表脚本操作符
print(['hi']*4)
a=[1,2,3,4,5]
b=['a','b','c']
print(len(a),len(b))
print(a+b)
print(4*[a])
print('b' in b)
for x in [1, 2, 3]: print(x, end=" ")
for x in [1,2,4,6,8]:print(x,end='')
##输出science end=参数不设置,默认为末尾换行/n,end=''末尾为空所以不换行
#嵌套列表
a=[1,2,3,4]
b=[5,6,7,8]
c=[a,b]
print ([a+b])
print(c)
print(c[0])
print(c[1][0])
#字符串的索引和切片
var= 'goodlike'
for a in var:
    print(a)

var= 'goodlike'
for a in var:
    print(a)
print('''\\\\\\\\'\'''')
print (var[0])
print(var[-1])
