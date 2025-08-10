def algo(n):
    s = str(n)
    while "55" in s or "150" in s or "555" in s:
        if "55" in s:
            s = s.replace("55", "615", 1)
        if "150" in s:
            s = s.replace("150", "5950", 1)
        if "555" in s:
            s = s.replace("555", "50", 1)
    return s
def nechmult(s):
    mult = 1
    for x in s:
        if int(x) % 2 == 1:
            mult *= int(x)
    return mult
for n in range(4, 10001):
    stroke = "0"+"5"*n
    if nechmult(stroke) > 100000:
        print(n)
        print(stroke)
        break
