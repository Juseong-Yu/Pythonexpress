food = int(input('음식 비용:'))
tip = input('팁 비율: ')
tip = int(tip[:-1])
total = food *((tip+100)/100)
print('총액: {}달러'.format(int(total)))
