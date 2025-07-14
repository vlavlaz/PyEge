#https://education.yandex.ru/ege/task/4e1f6f1f-125e-463a-b14e-77bb37d1dec0
strokes = []
with open("_5.txt") as f:
    for stroke in f:
        s = stroke.split("\t")
        #s[-1] = s[-1][:-1]
        for i in range(len(s)):
            s[i] = int(s[i])
        strokes.append(s)
print(strokes)
def check(stroke):
    uniq = stroke.copy()
    rep = []
    for i in range(0, 8):
        for j in range(i+1, 8):
            if stroke[i] == stroke[j] and not stroke[i] in rep:
                rep.append(stroke[i])
    for x in rep:
        while x in uniq:
            uniq.remove(x)
    if len(rep) < 2:
        return False
    sur = 0
    suq = 0
    for x in rep:
        sur += x
    for x in uniq:
        suq += x
    if sur < suq:
        return True
    else:
        return False
count = 0
for stroke in strokes:
    if check(stroke):
        count += 1
        print(stroke)
print(count)
