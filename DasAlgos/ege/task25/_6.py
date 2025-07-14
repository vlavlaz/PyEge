#https://education.yandex.ru/ege/task/11a2bea7-160c-4f93-9663-c9cf6685ec56
from fnmatch import fnmatch
mask = "17*023?9"
def dsum(x):
    _x = str(x)
    su = 0
    for t in _x:
        su+=int(t)
    return su

for x in range(179500000, 10**10):
    if dsum(x) % 11 == 0:
        if fnmatch(str(x), mask):
            print(x, dsum(x)//11)
