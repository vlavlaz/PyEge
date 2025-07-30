def dels(x):
    dels = []
    for d in range(1, round(x**0.5)+1):
        if x%d==0:
            if d not in dels:    dels.append(d)
            if x//d not in dels: dels.append(x//d)
    return sorted(dels)
primes = [x for x in range(round(965324**0.5)+1) if len(dels(x)) == 2]
#print(primes)
for x in range(326782, 965325):
    uniq = []
    for p1 in primes:
        if x%p1==0:
            for p2 in primes:
                if x % p2 == 0:
                    for p3 in primes:
                        if x % p3 == 0:
                            if x/p1/p2/p3 == 1:
                                p = [p1, p2, p3]
                                if p1 != p2 and p2!=p3 and p3!=p1:
                                    d = max(p)-min(p)
                                    if d <= 12:
                                        if x not in uniq: print(x, d, p)
                                        uniq.append(x)



