def algo(n):
    s = str(n)
    digs = []
    susq = 0
    for x in s:
        digs.append(int(x))
        if int(x) % 2 == 0:
            susq += int(x)
    susq = susq**2
    dcub = (max(digs) - min(digs))**3
    if susq <= dcub:
        return int(str(susq)+str(dcub))
    else:
        return int(str(dcub)+str(susq))
for x in range(1000, 10000):
    if algo(x) == 4343:
        print(x)
        break