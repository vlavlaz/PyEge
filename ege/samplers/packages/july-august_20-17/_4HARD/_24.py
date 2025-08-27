with open("_24.txt") as f:
    s = f.readline()
mx = 0
for i in range(0, len(s)):
    uniq = s[i]
    for j in range(i+1, len(s)):
        if not s[j] in uniq:
            uniq+=s[j]
        else:
            break
    if len(uniq) > mx:
        mx = len(uniq)
print(mx)
