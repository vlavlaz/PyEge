def algo(s1):
    s = str(s1)
    while ">1" in s or ">2" in s or ">3" in s:
        if ">1" in s:
            s = s.replace(">1", "21>3")
        if ">2" in s:
            s = s.replace(">2", "32>")
        if ">3" in s:
            s = s.replace(">3", "11>2")
    return s
def getS(x):
    res = ""
    while x > 0:
        res += str(x%3)
        x//=3
    res = res[::-1]
    res = res.replace("2", "3")
    res = res.replace("1", "2")
    res = res.replace("0", "1")
    return res
print(algo(">1")) # 1-> 3*1, 2*2, 1*3
print(algo(">2")) # 2-> 1*2, 1*3
print(algo(">3")) # 3-> 2*1, 1*2, 1*3

#17*1 -> 51*1, 34*2, 17*3
#10*3 -> 71*1, 44*2, 27*3
#10*2 -> 
for x in range(1, 10000000000):
    t = getS(x)[1:]
    s = algo(">" + t)
    if s.count("1") == 71 and s.count("2") == 54 and s.count("3") == 37:
        print(s)
        break