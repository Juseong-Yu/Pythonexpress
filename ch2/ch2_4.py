hour = int(input('시간을 입력하시오: '))
min = int(input('분을 입력하시오: '))

sec = hour*60*60 + min*60
print('{}시간 {}분은 {}초 입니다.'.format(hour,min,sec))