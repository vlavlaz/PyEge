def to9(x):
    res = ""
    while x > 0:
        res+=str(x%9)
        x//=9
    return res[::-1]
mx0 = 0
for x in range(0, 1950):
    a = to9(72070+7400 - x)
    if a.count("0") > mx0:
        print(a)
        mx0 = a.count("0")
print(mx0)