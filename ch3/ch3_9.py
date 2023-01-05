import random

math = random.randint(1,4)
x = random.randint(1,100)
y = random.randint(1,100)

if math == 1:
    answer = int(input('{} + {}의 값은? '.format(x,y)))
    if answer == (x + y):
        print('맞았습니다.')
    else:
        print('틀렸습니다.답은 {}입니다.'.format(x+y))

if math == 2:
    answer = int(input('{} - {}의 값은? '.format(x,y)))
    if answer == (x - y):
        print('맞았습니다.')
    else:
        print('틀렸습니다.답은 {}입니다.'.format(x-y))

if math == 3:
    answer = int(input('{} // {}의 값은? '.format(x,y)))
    if answer == (x // y):
        print('맞았습니다.')
    else:
        print('틀렸습니다. 답은 {}입니다.'.format(x//y))

if math == 4:
    answer = int(input('{} * {}의 값은? '.format(x,y)))
    if answer == (x * y):
        print('맞았습니다.')
    else:
        print('틀렸습니다.답은 {}입니다.'.format(x*y))