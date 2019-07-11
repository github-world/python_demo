a =eval(input())
n = int(a/2)+1
m = 1
for i in range(n):
    print((''*((a-m)//2))+('*'*m)+(''*((a-m)//2)))
    m+=2