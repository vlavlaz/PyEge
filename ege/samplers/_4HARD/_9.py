strokes = []
with open("_9.txt") as f:
    for s in f:
        stroke = s.split("\t")
        res = []
        for x in stroke:
            res.append(int(x))
        strokes.append(res)
def _1cond(stroke):
    uniq = []
    s = stroke.copy()
    for x in stroke:
        if x not in uniq:
            uniq.append(x)
            s.remove(x)
    if len(uniq) == 4:
        if s[0]==s[1]:
            return True
        else: return False
    else: return False
def _2cond(stroke):
    chet = 0
    nech = 0
    for x in stroke:
        if x % 2 ==0:
            chet += 1
        else:
            nech += 1
    if chet > nech:
        return True
    else: return False
def _3cond(stroke):
    s = sorted(stroke)
    sulse = s[0]+s[1]+s[2]+s[3]
    if (s[4]+s[5]) > 2*sulse:
        return True
    else:
        return False
ans = 0
for s in strokes:
    cnt = 0
    if _1cond(s):
        cnt+=1
    if _2cond(s):
        cnt+=1
    if _3cond(s):
        cnt+=1
    if cnt >= 2:
        ans += 1
print(ans)