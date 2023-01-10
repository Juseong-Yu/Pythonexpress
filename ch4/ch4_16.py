n = int(input('게임판의 크기: '))

for i in range(n):
    for j in range(n):
        print('---',end =' ')
    print()
    for k in range(n+1):
        print('|',end = '   ')
    print()
for j in range(n):
    print('---',end =' ')
print()