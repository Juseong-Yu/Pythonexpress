list1 = [80, 20, 20, 30, 60, 30]
print(f'주어진 리스트: {list1}')
list2 = list(set(list1))
list2.sort()
print(f'정리된 리스트: {list2}')