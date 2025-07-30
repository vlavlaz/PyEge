with open("_24.txt") as f:
    s = f.readline()
mx = 0
for i in range(0, len(s)):
    if s[i] in "123":
        wei = 2
        cnt = 1
    else:
        wei = -1
        cnt = 0
    for j in range(i+1, len(s)):
        if s[j] in "123":
            wei+=2
            cnt+=1
        else:
            wei-=1
        if wei == 0:
            if mx < cnt:
                mx = cnt
                print(cnt)
print(mx*3)