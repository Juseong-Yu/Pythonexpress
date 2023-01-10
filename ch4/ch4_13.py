my_list = [0,1]

n = int(input('몇 번째 항까지 구할까요?: '))
for i in range(2,n+1):
    tmp = my_list[i-2]+my_list[i-1]
    my_list.append(tmp)

print(my_list)