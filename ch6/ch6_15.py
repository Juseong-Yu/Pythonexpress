import random
table = []
for i in range(10):
    rollet = random.randint(1,37)
    if rollet <= 18 :
        table.append(0)
    else:
        table.append(1)

count = 0
tmp = 2
max = 0
for j in table:
    if j == tmp:
        count += 1
        if max < count:
            max = count
    else:
        count = 1
    tmp = j
print(table)
print(max)        