import math
column = ['각도', 'sin값' , 'cos값']
print('%-8s%-8s%-8s' %(column[0],column[1],column[2]))

for i in range(0,100,10):
    print('%-8s%-8s%-8s'%(i, round(math.sin(math.pi*i/180),3), round(math.cos(math.pi*i/180),3)))