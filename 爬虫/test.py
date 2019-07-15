import re
str1='hello,world,life is short,use Python .WHAT?'
a =re.search(r'\w+',str1)
print(a.group())  #hello
