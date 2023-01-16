def deci2bin(n):
    count = 0
    result = 0

    while n>=1:
        result += n%2*(10**count)
        n = n//2
        count += 1

    return result

num = int(input('10진수: '))
print(deci2bin(num))