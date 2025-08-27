strokes = []
with open("_9.txt") as f:
    for s in f:
        stroke = s.split("\t")
        for i in range(7):
            stroke[i] = int(stroke[i])
        strokes.append(stroke)
def valid(stroke):
    n = []
    d = []
    for x in stroke:
        if x%2==0:
            d.append(x)
        else:
            n.append(x)
    if len(n) < 2 or len(d) < 2:
        return False
    sun = 0
    mud = 1
    for x in n:
        sun += 3*x
    for x in d:
        mud *= x
    if sun > mud:
        return True
    return False
cnt = 0
for s in strokes:
    if valid(s):
        cnt += 1
print(cnt)