#https://education.yandex.ru/ege/task/7595fc66-a7ba-47d7-885e-17db99cf2811
f = open("_1.txt")
strrs = [strr.split() for strr in f]
N = int(strrs[0][0])
rows = []
plcs = []
for strr in strrs:
    if int(strr[0]) == N : continue
    rows.append(int(strr[0]))
    plcs.append(int(strr[1]))

def is_good_row(x, y):
    if abs(x - y) == 14:
        return True
    else:
        return False
good_rows_plcs = {}
for i in range (0, len(rows)):
    space = [plcs[i]]
    for j in range(i+1, len(plcs)):
        if rows[i] == rows[j]:
            space.append(plcs[j])
    for x in space:
        for y in space:
            if is_good_row(x, y):
                good_rows_plcs[rows[i]] = [x, y]
a = max(good_rows_plcs.keys())
print(a, good_rows_plcs[a])
