x , y, z = eval(input("3개의 정수를 입력하시오: "))

if x > y:
    if y > z:
        min = z
    else:
        min = y
else:
    if x > z:
        min = z
    else:
        min = x

print('가장 작은 정수는 {}입니다.'.format(min))
