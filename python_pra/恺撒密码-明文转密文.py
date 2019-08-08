'''
#2019年7月10日16:42:13
#凯撒密码是古罗马凯撒大帝用来对军事情报进行加解密的算法,它采用了替换方法对信息中的每一个英文字符循环替换为字母表序列中该字符后面的第三个字符,即,字母表的对应关系如下：
原文：A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
密文：D E F G H I J K L M N O P Q R S T U V W X Y Z A B C
'''
Str = input()
for i in range(0, len(Str)):
    if Str[i] == ' ':
        print(' ', end="") #输出空字符,然后末尾不换行。
    elif Str[i] in ['x', 'y', 'z']:
        # print('{}'.format(chr(ord(Str[i]) - 23)), end="") #另一种写法
        # ord()函数主要用来返回对应字符的ascii码,chr()主要用来表示ascii码对应的字符他的输入时数字,可以用十进制,也可以用十六进制。
        print(chr(ord(Str[i])-23),end='')
    else:
        # print('{}'.format(chr(ord(Str[i]) + 3)), end="") #另一种写法
        print(chr(ord(Str[i])+3),end='')

