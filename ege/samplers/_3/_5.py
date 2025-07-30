def algo(n):
    R = bin(n)[2:]
    if n % 2 == 1:
        R = "1"+R[:-2]+"10"
    else:
        R = "10"+R[2:]+"1"
    return int(R, 2)
mn = 999999999
for n in range(33, 1000000):
    R = algo(n)
    if R < mn:
        print(R)
        mn = R
print(mn)
