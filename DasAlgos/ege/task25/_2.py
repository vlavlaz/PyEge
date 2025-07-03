#https://education.yandex.ru/ege/task/ba7d71e4-ead2-497b-b1ee-8a914efa02d9
#Может баг задания, может я бомж - хз перерешать позже

primes = []
for p in range(2, round(973146285**(1/2))+1):
    count = 0
    for l in range(1, round(p**(1/2))+1):
        if p % l== 0 :
            count += 1
    if count == 1:
        primes.append(p)
print(primes)
def count_deg(p, x):
    count = 0
    while x % p == 0:
        count += 1
        x //= p
    return count

def count_dels(x, primes):
    dels = 1
    for p in primes:
        if x % p == 0:
            dels *= (count_deg(p, x) + 1)
    return dels - 2


sqrs = []

for x in range(1, round(973146285**0.5)):
    if x**2 >= 159264873 and count_dels(x**2, primes)>1:
        sqrs.append(x**2)

for x in range(0, len(sqrs), 2000):
    print(x, sqrs[x], count_dels(sqrs[x], primes))
