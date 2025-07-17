def algo(s1):
    s = str(s1)
    while "17" in s or "377" in s or "777" in s:
        if "17" in s:
            s = s.replace("17", "1", 1)
        if "377" in s:
            s = s.replace("377", "73", 1)
        if "777" in s:
            s = s.replace("777", "3", 1)
    return s
for n in range(1, 10000):
    ss = algo("1" + "7"*n)
    if ss.count("3") == 2:
        print(n, ss)
        break