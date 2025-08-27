with open("_6.txt") as f:
    s = f.readline()
mx = 0
fin = ""

def valid(s):
    if s[0] not in "ABC" or s[1] not in "ABC":
        return False
    return True

for i in range(0, len(s)-1):
    sub_s = s[i]+s[i+1]
    if valid(sub_s):
        for j in range(i+2, len(s)-1, 2):
            a = s[j]+s[j+1]
            if valid(a):
                sub_s+=a
            else:
                break
    if len(sub_s) > mx:
        mx = len(sub_s)
        fin = sub_s
print(mx/2, fin)