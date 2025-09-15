with open("_24.txt") as f:
    s = f.readline()

mx = 0
mx_s = ""
for i in range(0, len(s)-1):
    sub_s = s[i]
    cnt = 0
    print(i)
    if s[i]+s[i+1] == "BD":
        for j in range(i+1, len(s)):
            sub_s+=s[j]
            if s[j-1]+s[j] == "BD":
                cnt += 1
                if cnt == 119:
                    break
    if mx < len(sub_s):
        mx = len(sub_s)
        mx_s = sub_s
print(mx-1, mx_s)