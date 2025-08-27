with open("_4.txt") as f:
    s = f.readline()
mx = 0
fin = ""
for i in range(0, len(s)):
    sub_s = s[i]
    if s[i].isdigit():
        for j in range(i+1, len(s)):
            if s[j].isdigit():
                sub_s+=s[j]
                print(sub_s)
            else:
                break
    if len(sub_s) > mx:
        mx = len(sub_s)
        fin = sub_s
print(mx, fin)