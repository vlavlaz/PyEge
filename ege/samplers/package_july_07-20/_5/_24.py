s = ""
with open("_24.txt") as f:
    for x in f:
        s = x
t_s = ""
mxl = 0
s = s.replace("E", "A")
s = s.replace("C", "B")
s = s.replace("D", "B")
s = s.replace("F", "B")
for i in range(0, len(s)):
    sub_s = s[i]
    cnt = 0
    for j in range(i+1, len(s)):
        sub_s += s[j]
        if s[j-1] == "A":
            if s[j] == "B":
                cnt+=1
                if cnt == 130:
                    break
    if len(sub_s) > mxl:
        mxl = len(sub_s)
        t_s = sub_s
print(mxl, t_s)
