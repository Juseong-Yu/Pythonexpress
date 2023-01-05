import math
r = int(input('원의 반지름: '))

if r >= 0:
    print('원의 면적: {}'.format(math.pi*r*r))

else:
    print('잘못된 값입니다.')