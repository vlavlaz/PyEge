def to16(x):
    res = ""
    alf = "0123456789abcdef"
    while x > 0:
        res += alf[x%16]
        x //=16
    return res[::-1]
for x in range(401, 100000):
    a = to16(16**560 + 16**120 - x)
    if a . count("0") == 442:
        print(x)
        break