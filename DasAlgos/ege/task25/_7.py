def dels(x):
    dels = []
    for d in range(1, round(x**0.5+1)):
        if x%d==0 and d != 1:
            dels.append(d); dels.append(x//d)
    return dels
def sumdel(x):
    su = 0
    for d in dels(x):
        if len(dels(d)) == 0:
            su += d
    return su
print(sumdel(20))
for x in range(500000, 1000000000):
    R = sumdel(x)
    if R > 2000 and R%1000==7:
        print(x, R)