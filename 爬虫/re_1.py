__author__ = 'cq'

import  re
from random import randrange,choice,randint
from string import ascii_lowercase as lc
from time import ctime


#生成数据文件
def generate_data():
    with open('./data.txt','w') as f:
        for i in range(randint(20,30)):
            tlds = ('com', 'edu', 'net', 'org', 'gov')
            dtint = randint(100000000,1200000000) #生成时间戳
            dtstr = ctime(dtint)  #将时间戳转化为特定时间格式
            llen = randrange(4, 8) #用户名长度
            login = ''.join(choice(lc) for i in range(llen))  #生成用户名
            dlen = randrange(llen,13)                         #域名长度
            dom = ''.join(choice(lc) for i in range(dlen))    #生成域名

            data_line = "%s::%s@%s.%s::%d-%d-%d\n" % (dtstr, login, dom, choice(tlds), dtint, llen, dlen)
            f.write(data_line) #写入文件
            print(data_line)   #打印每行记录



#匹配指定日期的行
def match_date():
    regex = '(Mon|Tue|Wed|Thu|Fri|Sat|Sun)(.*)'
    with open('./data.txt','r') as f:
        m = re.findall(regex,f.read())
        for i in m:
            print(i)




#匹配在某时间段内的记录
def match_time_slot():
    regex = ' ([0-9]{1,2}) .*([0-9]{4})::(.*)'
    # regex = ' ([0-9]{0,2}).*(::)(.*) '
    with open('./data.txt','r') as f:
        m = re.findall(regex,f.read())
        for i in m:
            if 2000 <= int(i[1]) and int(i[1]) <= 2020 and 20 <= int(i[0]) and int(i[0]) <= 31:
                print(i)


#匹配某名单中人员的记录
def match_name():
    regex = '::([a-z]{2,13})@([a-z]{2,13})\.(com|edu|net|org|gov)'
    with open('./data.txt','r') as f:
        m = re.findall(regex,f.read())
        for i in m:
            print(i)



def main():
    generate_data()
    print("\n---------------match_date--------------------\n")
    match_date()
    print("\n---------------match_time_slot--------------------\n")
    match_time_slot()
    print("\n---------------match_name--------------------\n")
    match_name()


if '__main__' == __name__:
    main()