lines = []
with open("_9.txt") as f:
    for stroke in f:
        s = stroke.split("\t")
        line = []
        for x in s:
            line.append(int(x))
        lines.append(line)
def valid(l):
    if l[0] + l[1] + l[2] +l[3] + l[4] + l[5] + l[6] >= 502:
        return False
    uniq = []
    c = l.copy()
    for X in l:
        if not X in uniq:
            uniq.append(X)
            c.remove(X)
    if len(uniq) != 5:
        return False
    if c[0] != c[1]:
        return False
    else:
        return True
cnt = 0
for line in lines:
    if valid(line):
        print(sorted(line))
        cnt += 1
print(cnt)
