strokes = []
with open("_9.txt") as f:
    for x in f:
        stroke = x.split("\t")
        for i in range(4):
            stroke[i] = int(stroke[i])
        strokes.append(stroke)
def _1cond(stroke):
    uniq = []
    for x in stroke:
        if x not in uniq:
            uniq.append(x)
    if len(uniq)==4:
        return True
    else:
        return False
def _2cond(stroke):
    s = stroke.copy()
    mx = max(s); s.remove(mx)
    mn = min(s); s.remove(mn)
    x, y, = s[0], s[1]
    if (mx+mn)/2<=(x+y)/2:
        return True
    else:
        return False
cnt = 0
for stroke in strokes:
    if _1cond(stroke) and _2cond(stroke):
       cnt+=1
print(cnt)