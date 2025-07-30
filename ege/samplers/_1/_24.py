#https://education.yandex.ru/ege/task/bdfb8f12-2b10-4f4b-99b0-6d2e045552e2
s = ""
with open("_24.txt") as f:
    for x in f:
        s = x
alf = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
mx = 0
for i in range(0, len(s)):
    c_g = 0
    if s[i] in "AEIOUY":
        c_g = 1
    sub_s = s[i]
    for j in range(i+1, len(s)-1):
        if s[j] in "AEIOUY":
            c_g += 1
        if c_g == 2:
            break
        if alf.index(s[j-1]) < alf.index(s[j]):
            sub_s+=s[j]
        else:
            break
    if mx < len(sub_s):
        print(sub_s)
        mx = len(sub_s)
print(mx)
