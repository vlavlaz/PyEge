def to5(x):
    res = ""
    while x > 0:
        res+=str(x%5)
        x//=5
    return res[::-1]

for y in range(1, 1501):
    a = to5(5**400+5**200-y)
    if a.count("0") == 150:
        print(y)