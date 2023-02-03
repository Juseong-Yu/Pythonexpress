import random
S,B,Sy,D = 0,0,0,0
s = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()'
while S == 0 or B == 0 or Sy == 0 or D == 0:
    S,B,Sy,D = 0,0,0,0
    password = random.sample(s,8)
    for l in 'abcdefghijklmnopqrstuvwxyz':
        if l in password:
            S = 1
    for l in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        if l in password:
            B = 1
    for l in '1234567890':
        if l in password:
            Sy = 1
    for l in '!@#$%^&*()':
        if l in password:
            D = 1

print(''.join(password))