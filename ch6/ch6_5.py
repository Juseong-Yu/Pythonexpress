l = ['aba', 'xyz', 'abc', '121']
count = 0

for i in l:
    if i[0]==i[-1]:
        count +=1
print('문자열의 개수 ={}'.format(count))