weight = float(input('무게(킬로그램): '))
height = float(input('키(미터): '))

BMI = weight / (height**2)

if BMI >= 20 and BMI <= 24.9:
    print('정상입니다.')

elif BMI >= 25 and BMI <= 29.9:
    print('과체중입니다.')

elif BMI >= 30:
    print('비만입니다.')

else:
    print('저체중입니다.')