s = ""
with open("_6.txt") as f:
    for x in f:
        s = x
#ABA or BAB o ABABAB - good.
flag_a = False
mx = 0
that_s = ""
flag_b = False
for start in range(0 ,len(s)):
    sub_s =""
    if s[start] == "A":
        flag_a = True
        sub_s+="A"
    elif s[start] == "B":
        sub_s+="B"
        flag_b = True
    else: continue
    for i in range(start+1, len(s)):
        if flag_a:
            if s[i] == "B":
                sub_s+="B"
                flag_b = True
                flag_a = False
                continue
            else:
                break
        if flag_b:
            if s[i] == "A":
                sub_s+="A"
                flag_b = False
                flag_a = True
                continue
            else:
                break
    l = len(sub_s)
    if l > mx:
        mx = l
        that_s = sub_s
print(that_s, mx)