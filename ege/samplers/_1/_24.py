#https://education.yandex.ru/ege/task/3594e81a-4775-400e-97ce-64c0fcd1e711
with open("_24.txt") as f:
    s = f.readline()
mx = 0
that_s = ""
for i in range(0, len(s)):
    sub_s = ""
    for j in range(i+80, len(s)):
        sub_s = s[i::j]
        if sub_s.count("Y") != 80:
            continue
        else:
            if sub_s.count("2025")>=90:
                k = j
                while s[k] != "Y":
                    sub_s+=s[k]
                break
    if len(sub_s) > mx:
        mx = len(sub_s)
        that_s = sub_s
print(mx, that_s)

