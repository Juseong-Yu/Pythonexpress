def getSorted(x,y):
    if x> y:
        return y,x
    else:
        return x,y
x = int(input('첫 번째 정수: '))
y = int(input('두 번재 정수: '))

print(getSorted(x,y))