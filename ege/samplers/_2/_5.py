def to3(x):
    res = ""
    while x>0:
        res+=str(x%3)
        x//=3
    return res[::-1]
def algo(n):
    R = to3(n)
    R += str(n%3)
    R = R[-1] + R
    return int(R,3)
mn = 9999999
for n in range(1, 1000000):
    a = algo(n)
    if mn > a and 1000<=a<=9999:
        mn = a
print(mn)

