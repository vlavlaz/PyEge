strokes = []
with open("_9.txt") as f:
    for l in f:
        strokes.append(list(map(int, l.split("\t"))))
def valid(s):
    uniq = []
    s1 = s.copy()
    for x in s:
        if x not in uniq:
            uniq.append(x)
            s1.remove(x)
    if not(len(uniq) == 5 and s1[0]!=s1[1]):
        return False
    surep = s1[0]+s1[-1]
    sunech = 0
    for x in s:
        if x%2==1:
            sunech+=x
    if surep <= sunech:
        return True
    return False
cnt = 0
for s in strokes:
    if valid(s):
        print(s)
        print(s[0]+s[1]+s[2]+s[3]+s[4]+s[5]+s[6])
        break
