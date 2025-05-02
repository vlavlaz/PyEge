f = open("13.txt")
s = [int(x) for x in f]
s15 = [x for x in s if x%15!=0]
min15 = min(s15)
res = [s[i]+s[i+1] for i in range(len(s)-1) if (s[i]%min15==0 and s[i+1]%min15==0)]
print(len(res), max(res))