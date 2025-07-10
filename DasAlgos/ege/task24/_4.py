#https://education.yandex.ru/ege/task/bcd7eb8e-445f-413b-a844-6e8394d50eb7
f = open("_4.txt")
stroke = ""
for x in f:
    stroke+=x
mx = 0
for start in range(0, len(stroke)):
    sub_s = ""
    if stroke[start] == "E":
        for k in range(start+1, len(stroke)):
            sub_s += stroke[k]
            if stroke[k] == "E" or stroke[k] not in "ND":
                if len(sub_s) > mx:
                    mx = len(sub_s)
                break
print(mx)