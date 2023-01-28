l = [1,2,3,4,5,6,7,8,9,10]
lm = [-i if (i>=3 and i<=8) else i for i in l]
print('실행전', l)
print('실행후', lm)