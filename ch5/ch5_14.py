def test(a,b):
    c=a/b 
    
    if (c - b) < 0.0001 and (c-b) > -0.0001:
        print(b)
    else:
        test(a,(b+a/b)/2)

test(2,1)