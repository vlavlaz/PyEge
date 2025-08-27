#https://education.yandex.ru/ege/task/5642b4b5-20a8-4bcf-a5d2-fc5a3ed1b9da
from fnmatch import fnmatch
mask = "10*2426?"
for i in range(0, 10**10, 9799):
    if i % 8465 == 0 and fnmatch(str(i), mask):
        print(i, i/8465/9799)
for i in range(0, 10**10, 9799):
    if fnmatch(str(i), mask):
        print(i, i/9799)
for i in range(0, 10**10, 8465):
    if fnmatch(str(i), mask):
        print(i, i/8465)
