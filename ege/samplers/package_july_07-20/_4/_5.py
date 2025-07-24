#https://education.yandex.ru/ege/task/65bc5b5a-439d-4f2e-b1cd-c6927ace1c2d

#ALOWED DIGITS: 1, 3, 6, 7, 9
def algo(N):
    _n = str(N)
    _n = _n.replace("3", "4")
    _n = _n.replace("7", "8")
    R = 1
    for x in _n:
        R*=int(x)
    return R
for n in range(1, 1000000):
    _n = str(n)
    if _n.count("0") > 0 or _n.count("2") > 0 or _n.count("4") > 0 or _n.count("5") > 0 or _n.count("8") > 0:
        continue
    R = algo(n)
    if len(_n) == 4 and R==256:
        print(n)