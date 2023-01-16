def large(a,b):
    result = 0

    if a % b == 0 or b % a == 0:
        return min(a,b)

    if a < b:
        tmp = b-a
        return large(a,tmp)
    else :
        tmp = a-b
        return large(b,tmp)


a = int(input('첫 번째 정수: '))
b = int(input('두 번째 정수: '))

print(large(a,b))