#https://education.yandex.ru/ege/task/83b21e05-822c-44b1-b785-f14418c83449
from fnmatch import fnmatch
mask = "?2*4*0"
nmask = "1*7*"
for x in range(42, 2*10**8, 42):
    if fnmatch(str(x), mask):
        if not fnmatch(str(x), nmask):
            print(x, x//42)