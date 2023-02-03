d = {1:10,2:20,3:30,4:40,5:50,6:60}
key = int(input('키를 입력하시오: '))
if key in d.keys():
    print(f'키 {key}는 딕셔너리 안에 있습니다.')
else:
    print(f'키 {key}는 딕셔너리 안에 없습니다.')