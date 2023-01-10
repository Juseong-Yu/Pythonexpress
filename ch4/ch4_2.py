my_list = [11, 22, 23, 99, 81, 93, 35]
total = 0

for i in my_list:
    total += i

print('정수들의 합은: {}'.format(total))

total = 0
for j in range(len(my_list)):
    total = total + my_list[j]

print('정수들의 합은: {}'.format(total))