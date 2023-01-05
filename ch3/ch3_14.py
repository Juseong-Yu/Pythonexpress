import math

a = int(input('a를 입력하시오: '))
b = int(input('b를 입력하시오: '))
c = int(input('c를 입력하시오: '))

if b**2 - 4*a*c > 0:
    temp = b**2 - 4*a*c
    num1 = (-b + math.sqrt(temp))/(2*a)
    num2 = (-b - math.sqrt(temp))/(2*a)
    print('실근은 {}과 {}입니다.'.format(num1,num2))

elif b**2 - 4*a*c == 0:
    num1 = -b/(2*a)
    print('실근은 {}입니다.'.format(num1))

else:
    print('실근이 존재하지 않습니다')