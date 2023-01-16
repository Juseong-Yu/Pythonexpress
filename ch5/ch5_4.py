def getGrade(grade):
    if grade > 90:
        return 'A'
    elif grade > 80:
        return 'B'
    elif grade > 70:
        return 'C'
    elif grade > 60:
        return 'D'
    else:
        return 'F'

grade = int(input('점수를 입력하세요: '))
print(getGrade(grade))