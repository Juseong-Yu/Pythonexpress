def table(booked):
    print('-'*20)
    print('1 2 3 4 5 6 7 8 9 10')
    print('-'*20)
    for i in range (10):
        for j in range(10):
            if booked[i][j] == 1:
                print(1,end = ' ')
            else:
                print(0,end =' ')
        print()

booked = [[0 for i in range(10)] for j in range(10)]
num = 0

while True:
    table(booked)
    num1 = int(input('원하시는 좌석의 행번호를 입력하세요(종류는 -1): '))
    num2 = int(input('원하시는 좌석의 열번호를 입력하세요(종류는 -1): '))
    if num1 == -1 or num2 == -1:
        print('예약을 멈춥니다.')
        break
    elif booked[num1-1][num2-1] == 1:
        print('이미 예약된 좌석 입니다')
    else:
        booked[num1-1][num2-1] = 1
    