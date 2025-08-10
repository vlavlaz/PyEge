def dels(x):
    dels = []
    for d in range(2, round(x**0.5)+1):
        if x%d==0:
            dels.append(d)
            dels.append(x//d)
    return dels.copy()
for x in range(10**8, 10**9):
    if len(dels(x)) == 4:
        r = sorted(dels(x))[-1] - sorted(dels(x))[0]
        if r <= 15:
            print(x, r)