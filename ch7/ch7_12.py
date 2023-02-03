str1 = input('문자열을 입력하시오: ')
str2 = input('금칙어를 입력하시오: ')
lst1 = str1.split(' ') 
lst2 = str2.split(' ')
print(lst1,lst2)
for i in lst2:
    if i in lst1:
        st = str1.replace(i,"*"*len(i))
print(st)