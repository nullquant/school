# x&33 = 0 → (x&45≠0 → x&А ≠ 0)




print(bin(33))
print(bin(45))

def test(x, A):
    if not(x&33 == 0) or (not(x&45 != 0) or (x&A !=0)):
        return 1
    return 0

for A in range(1,15):

    ok = True
    for x in range(0, 1000000):
        if test(x,A) != 1:
            ok = False
            break
    
    if ok:
        print(A)



ok = False
if not ok:
    print('!!!')



# (x < A)∨(y < A)∨(y > x − 5)∨(y < 2x − 15)


for A in range(0, 10):

    ok = 1
    for x in range(-100, 100):
        for y in range(-100, 100):
            t2 = (x<A) or (y<A) or (y>x-5) or (y<2*x-15)
            if not t2:
                ok = 2
                
    if ok == 1:
        print(A)

        


