a = int(input('첫 번째 정수를 입력하시오: '))
b = int(input('두 번째 정수를 입력하시오: '))

k = 1
for i in range(1,a+1):
    if a % i == 0 and b % i == 0:
        k = i

print('{}과 {}의 최대 공약수는 {}입니다.'.format(a,b,k))