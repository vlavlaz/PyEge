#https://education.yandex.ru/ege/task/7102b1d9-1aed-45d5-bb07-8fb3361ed445
strokes = []
with open("xls.txt") as f:
    for s in f:
        stroke = s.split("\t")
        for i in range(0, len(stroke)):
            stroke[i] = int(stroke[i])
        strokes.append(stroke)
def _1cond(stroke):
    uniq = []
    for x in stroke:
        if x not in uniq:
            uniq.append(x)
    if len(uniq) == 4:
        return True
    else:
        return False
def _2cond(stroke):
    s = stroke.copy()
    mx = max(s)
    mn = min(s)
    su2 = 0
    s.remove(mx); s.remove(mn)
    for x in s:
        su2 += x**2
    if (mx+mn)**2 < su2:
        return True
    else:
        return False
cnt = 0
for stroke in strokes:
    if _1cond(stroke) and _2cond(stroke):
        cnt += 1
print(cnt)