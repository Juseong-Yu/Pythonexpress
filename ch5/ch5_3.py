def calc(a,b):
    print('{}, {}, {}, {}이 반환되었습니다.'.format(a+b,a-b,a*b,a/b))

a = int(input('정수를 입력하시오: '))
b = int(input('정수를 입력하시오: '))

calc(a,b)