import random
field = [["'"for i in range(10)] for j in range(10)]

for i in range(10):
    for j in range(10):
        R = random.random()
        if R < 0.3:
            field[i][j] = '#'
        print(field[i][j],end =' ')
    print()