num = int(input('입력할 값의 개수: '))
l = []
for i in range(num):
    n = int(input())
    l.append(n)

total = sum(l)
print('값의 합계= {}'.format(total))