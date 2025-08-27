def prime(x):
    for d in range(2, round(x**0.5)+1):
        if x%d==0:
            return False
    return True
primes = [x for x in range(2, 100000) if prime(x)]
print(primes)
def p_dels(x, dels):
    for d in primes:
        if x%d==0:
            dels.append(d)
            dels.append(x//d)
        if len(dels)>4:
            return []
    return dels

ans = {}
for x in range(700000, 10**9):
    des = p_dels(x, [])
    if len(des) == 4:
        r = sorted(des)[-1] - sorted(des)[0]
        if r <= 15:
            print(x, r)
            ans[x] = r
print("\n", ans)