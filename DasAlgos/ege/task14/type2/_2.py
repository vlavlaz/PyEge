#https://education.yandex.ru/ege/task/d540f2de-90b8-42c9-8075-3410eccdeeeb
import EGE
for x in range(1, 2301):
    num = EGE.cs_conv(7**350 + 7**150 - x, 7)
    if num.count("0") == 200:
        print(x)

