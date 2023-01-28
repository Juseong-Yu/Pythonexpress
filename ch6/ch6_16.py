list1 = [i for i in range(2,101)]

i = 0
while i < len(list1):
    num = list1[i]
    print(num,end =' ')
    list1.remove(num)
    j = 1
    while j <len(list1):
        if list1[j] % num == 0:
            list1.pop(j)
        j += 1