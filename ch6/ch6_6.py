l1 = [1,2,3,4,5,6]
l2 = [6,7,8,9,10]
def same_thing1(l1,l2):
    for i in l1:
        if i in l2:
            return True
    return False

def same_thing2(l1,l2):
    for i in l1:
        for j in l2:
            if i == j:
                return True
    return False
print(same_thing1(l1,l2))
print(same_thing2(l1,l2))