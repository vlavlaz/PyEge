def dels(X):
    dels = []
    for d in range(2, round(X**0.5)+1):
        if X%d == 0:
            dels.append(d)
            if not X//d in dels: dels.append(X//d)
    return sorted(dels)
def bigM(x):
    d = dels(x)
    if d :
        return d[0]+d[-1]
    else: return 0
for x in range(800000, 1, -1):
    if bigM(x)%10 == 2:
        print(x, bigM(x))