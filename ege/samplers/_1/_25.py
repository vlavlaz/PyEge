#https://education.yandex.ru/ege/task/dc4c312e-1acd-406e-83a6-d4aac88cf80e
def dels(x):
    res = []
    for d in range(2, round(x**0.5)+1):
        if x % d == 0:
            res.append(d)
            res.append(x//d)
    return sorted(res)
def bigM(x):
    d = dels(x)
    if d: return d[0]+d[-1]
    else: return  0
for x in range(800001, 10000000):
    if bigM(x)%10 == 4:
        print(x, bigM(x))