def prime(x):
    for d in range(2, round(x**0.5)+1):
        if x % d == 0:
            return False
    return True
mx = 0
primes = [x for x in range(1000000000, 1000100000) if prime(x)]
for i in range(0, len(primes)-1):
    if primes[i+1]-primes[i] > mx:
        print(primes[i+1]-primes[i])
        mx = primes[i+1]-primes[i]