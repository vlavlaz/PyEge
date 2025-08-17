def to7(x):
    res = ""
    while x > 0:
        res += str(x%7)
        x//=7
    return res[::-1]
def algo(n):
    R = to7(n)
    if n % 7 == 0:
        R += R[-2:]
    else:
        R += to7((n%7)*2)
    return int(R, 7)
for n in range(1, 100000000):
    if algo(n) < 220:
        print(n)