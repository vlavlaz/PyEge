#https://education.yandex.ru/ege/task/c948f964-e4ef-455c-8de0-21e7d7ef2986
from DasAlgos.EGE import cs_conv
for n in range(199, 1, -1):
    _4 = str(cs_conv(n, 4))
    if _4[-3:] == "123":
        print(n, _4)