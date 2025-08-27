with open("_24.txt") as f:
    s = f.readline()
alf = "SQRP"
max_s = ""
for i in range(0, len(s)):
    sub_s = s[i]
    for j in range(i+1, len(s)):
        pair = s[j-1]+s[j]
        print(pair)
        if pair in alf:
            sub_s+=s[j]
        else:
            break
    if len(sub_s) > len(max_s):
        max_s = sub_s
        print(sub_s)
print(len(max_s), max_s)
print(len("PSQRPSQRPSQRPSQRPSQRPSQRPSQRPSQRPSQRPSQRPSQRPSQRPSQR"))
