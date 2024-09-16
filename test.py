

def fact(x):
    if x == 1: 
        return 1
    return x * fact(x-1)

print(fact(5))


def test(x, y):
    a = x * 4 + y
    print(a)
    
test(1, 2)

