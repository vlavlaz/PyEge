# https://education.yandex.ru/ege/task/bc22a1e4-4d9f-4514-be43-3b8bd6d3be35
from EGE import BIG_NUM
f = open("_3.txt")
s = ""
for x in f:
    s = x
minl = BIG_NUM

for i in range(0, len(s)):
    sub_s = ""
    if s[i] == "E":
        j = i
        while sub_s.count("E") < 240 and len(sub_s) < minl:
            sub_s += s[j]
            j+=1
        if minl > len(sub_s):
            print(sub_s)
            print(len(sub_s))
            minl = len(sub_s)
print(minl)
