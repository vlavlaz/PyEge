with open ("_24.txt") as f:
    s = str(f.readline())
mx = 0
for x in range(0, len(s)):
    sub_s = s[x]
    for y in range(x+1, len(s)):
        sub_s+=s[y]
        if "AHAHA" in sub_s:
            break
    if len(sub_s) > mx:
        mx = len(sub_s)
        print(sub_s)
print(mx-1)