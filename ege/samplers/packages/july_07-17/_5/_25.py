#https://education.yandex.ru/ege/task/448b1e4a-c031-4925-ad78-08ad58aaca6a
def dels(x):
    dels = []
    for d in range(1, round(x**0.5+1)):
        if x%d==0 and d != 1:
            dels.append(d); dels.append(x//d)
    return dels
def sumdel(x):
    su = 0
    for d in dels(x):
        if len(dels(d)) == 0:
            su += d
    return su
for x in range(500000, 1000000000):
    R = sumdel(x)
    if R > 2000 and R%10==7:
        print(x, R)