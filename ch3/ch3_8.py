test_result = input('체중과 키를 입력하시오:').split()

weight = int(test_result[0])
height = int(test_result[1])

if weight > (height-100)*0.9:
    print('과체중입니다.')

elif weight < (height-100)*0.9:
    print('저체중입니다.')

else:
    print('표준입니다.')