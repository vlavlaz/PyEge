def algo(s1):
    s = str(s1)
    while "8858" in s or "555" in s:
        if "8858" in s:
            s = s.replace("8858", "4", 1)
        else: s = s.replace("555", "58", 1)
        if "5858" in s:
            s = s.replace("5858", "85", 1)
    return s
def dsum(s):
    su = 0
    for x in s:
        su += int(x)
    return su
for n in range(4, 10001):
    res = algo("8"+"5"*n)
    if dsum(res) == 66:
        print(n)