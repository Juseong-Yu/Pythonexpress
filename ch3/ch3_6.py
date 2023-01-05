import random

choice = int(input('선택하시오(1:가위 2:바위 3:보) '))

computer = random.randint(1,3)
print('컴퓨터의 선택(1:가위 2:바위 3:보) {}',format(computer))

if choice == computer:
    print('비김')

elif choice+1 == computer or choice-2 == computer:
    print('컴퓨터가 이김')

else:
    print('내가 이김')