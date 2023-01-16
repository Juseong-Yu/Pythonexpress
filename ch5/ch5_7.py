def getintRange(what,a,b):
    num = int(input('{}을 입력하시오({}부터 {}사이의 값): '.format(what,a,b)))
    if num >= a & num <= b:
        return num
    else:
        getintRange(what,a,b)

print('날짜를 입력하시오(월과 일)')

month = getintRange('월',1,12)

if month in [1,3,5,7,8,10,12]:
    day = getintRange('일',1,31)
elif month == 2:
    day = getintRange('일',1,28)
else:
    day = getintRange('일',1,30)


print('입력된 날짜는 {}월 {}일입니다.'.format(month,day))