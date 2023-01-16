def testPrime(n):
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

for i in range(2,101):
    if testPrime(i) == True:
        print(i,end = ' ')
    else:
        continue