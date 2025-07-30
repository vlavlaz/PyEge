with open("_24.txt") as f:
    s = f.readline()
that_s = ""
for i in range(0, len(s)):
    if s[i] in "123":
        wei = 2
    else:
        wei = -1
    sub_s = s[i]
    for j in range(i+1, len(s)):
        if s[j] in "123":
            wei += 2
        else:
            wei -= 1
        sub_s+=s[j]
        if wei == 0:
            break
    if wei == 0 and len(that_s) < len(sub_s):
        print(that_s)
        that_s = sub_s
print(that_s, len(that_s))
cntd = 0
cntl = 0
for c in that_s:
    if c in "123":
        cntd += 1
    else:
        cntl += 1
print(cntl, cntd)