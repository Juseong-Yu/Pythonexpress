def checkPass():
    num = 0
    upper = 0
    lower = 0

    p = input('패스워드를 입력하시오: ')

    for i in p:
        if i >= 'a' and i <= 'z':
            lower += 1
        elif i >='A' and i <= 'Z':
            upper += 1
        elif i >= '0' and  i <= '9':
            num += 1

    if num == 0 or upper == 0 or lower == 0 or len(p) < 8:
        print('사용할 수 없습니다. 다시 입력하세요! \n')
        checkPass()
    else:
        print('사용할 수 있습니다.')

checkPass()
