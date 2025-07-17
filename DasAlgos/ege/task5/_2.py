#https://education.yandex.ru/ege/task/9fb60578-88e4-465d-b603-dbf30d312808

from DasAlgos.EGE import *
def algo(x):
    x_5 = cs_conv(x, 5)
    if x % 5 == 0:
        x_5+=x_5[-3:]
    else:
        x_5+=cs_conv(x%5*5, 5)
    return x_5

for n in range (11, 1000):
    R = algo(n)
    if int(R, 5) > 375:
        print(n)
        break