import re
print(re.match('ww','www.baidu.com').span())
print(re.match('com','www.baidu.com'))

line = 'cats are smart than dogs'
 matchObj = re.match(r'(.*) are (.*?) .*', line, re.M | re.I)

if matchObj:
    print("matchObj.group() : ", matchObj.group())
    print("matchObj.group(1) : ", matchObj.group(1))
    print("matchObj.group(2) : ", matchObj.group(2))
else:
    print("No match!!")


