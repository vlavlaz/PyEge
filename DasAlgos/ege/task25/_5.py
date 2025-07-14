#https://education.yandex.ru/ege/task/8fb83bf7-7231-4859-bba5-b29fe5790a7d
from fnmatch import fnmatch
mask = "48*15*0"
for x in range (42000, 10**10, 42):
    if fnmatch(str(x), mask):
        print(x, x//42)