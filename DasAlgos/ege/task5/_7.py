def to3(x):
    res = ""
    if x == 0: return 0
    while x > 0:
        res+=str(x%3)
        x//=3
    return res[::-1]
def algo(n):
    _3 = to3(n)
    R = ""
    if n%3==0:
        for c in _3:
            R += c*2
    else:
        for c in _3:
            if c == "0":
                R += "1" * 2
            elif c == "1":
                R += "2" * 2
            elif c == "2":
                R += "0" * 2
    return R
for n in range(1, 10000001):
    R = int(algo(n), 3)
    if R > 120:
        print(n, R)
        break



