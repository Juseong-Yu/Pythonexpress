for i in range(1,20):
    for j in range(1,i+1):
        if i % j == 0 and j != 1  and j != i :
            break
        if i-1 == j:
            print(i,end = ' ')