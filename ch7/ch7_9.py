chr1 = input('첫 번째 문자열: ')
chr2 = input('두 번째 문자열: ')
intersec = set(chr1) & set(chr2)
print(f'모두 포함된 글자: {intersec}')