def getMoneyText(amount):
    ones = amount % 10
    tens = (amount // 10) % 10
    hundreds = (amount // 100) % 10
    
    if amount == 1000:
        print('천 원')
    else:
        print('{} {} {}원'.format(text(hundreds,'백'),text(tens,'십'),text(ones,'')))

def text(num,letter):
    if num == 1:
        return '일' + letter
    elif num == 2:
        return '이' + letter
    elif num == 3:
        return '삼' + letter
    elif num == 4:
        return '사' + letter
    elif num == 5:
        return '오' + letter
    elif num == 6:
        return '육' + letter
    elif num == 7:
        return '칠' + letter
    elif num == 8:
        return '팔' + letter
    elif num == 9:
        return '구' + letter
    else:
        return ' '

amount = int(input('1000 이하의 금액을 입력하시오: '))
getMoneyText(amount)