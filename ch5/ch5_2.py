a = int(input('정수를 입력하시오: '))
b = int(input('정수를 입력하시오: '))

def add(a,b):
    print('{} + {} = {}'.format(a,b,a+b))

def sub(a,b):
    print('{} - {} = {}'.format(a,b,a-b))

def multi(a,b):
    print('{} * {} = {}'.format(a,b,a*b))

def div(a,b):
    print('{} / {} = {}'.format(a,b,a/b))

add(a,b)
sub(a,b)
multi(a,b)
div(a,b)