num1 =int(input('input a number:'))
num2 =int(input('input a number2:'))
def isEqual(num1, num2):

   if num1<num2:

       print('too small')

       return False

   if num1>num2:

       print ('too big')

       return False

   if num1==num2:

       print ('bingo')

       return True