date = 0
dic = {}

while True:
    date = input('날짜를 입력하기오(종류를 원할시 -1): ')
    if date == "-1":
        break
    else:
        schedule = input('일정을 입력하시오: ')
    if date in dic.keys(): 
        dic[date].append(schedule)
        dic[date]
    else:
        lst = []
        lst.append(schedule)
        dic[date] = lst

print(dic)