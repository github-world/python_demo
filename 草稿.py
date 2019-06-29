'''
a=[1,2,3,4]
b=[5,6,7,8]
c=[a,b]
print ([a+b])
print(c)
print(c[0])
print(c[1][0])

for i in range(10):

   a = input()

   if a == 'EOF':

       break

for i in range(2):
    a = input()
    if a =="EOF":
        break
'''
i = 0

while i < 5:

   i += 1

   for j in range(3):

       print (j)

       if j == 2:

           break

   for k in range(3):

       if k == 2:

           continue

       print (k)

   if i > 3:

       break

   print (i)