n = int(input('n의 값을 입력하시오: '))

result = 0

for i in range(1,n+1):
    result += i**2

print('계산값은 {}입니다.'.format(result))