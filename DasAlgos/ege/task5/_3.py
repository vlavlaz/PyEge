#https://education.yandex.ru/ege/task/afe8a9d0-8162-4f92-9e87-1c2dc7265290
from DasAlgos.EGE import cs_conv
for N in range (100000):
    _3 = str(cs_conv(N, 3))
    sorted_3 = []
    for c in _3:
        sorted_3.append(int(c))
    sorted_3 = sorted(sorted_3, reverse=True)
    mx = str(max(sorted_3))
    R = ""
    for x in sorted_3:
        R+=str(x)
    R+=mx
    if int(R,3) < 1200:
        print(R)
        print(int(R,3))