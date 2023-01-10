import random

inner = 0
outer = 0
for i in range(10000000):
    x = random.random()
    y = random.random()
    if x**2 + y**2 <= 1:
        inner += 1
    else:
        outer += 1
print(inner/(outer+inner)*4)