num = int(input('정수 = '))
total = num%10
num = num // 10
total += num%10
num =num//10
total += num%10
num =num//10
total += num%10
print(total)