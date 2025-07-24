#https://education.yandex.ru/ege/task/1630a1f6-eb68-4a20-8be5-6c1552224ed7
def to5(x):
    res = ""
    if x == 0: return 0
    while x > 0:
        res+=str(x%5)
        x//=5
    return res[::-1]
mx0 = 0
ans = 0
for x in range(1, 2031):
    a = to5(5**100 - x)
    if a.count("0") > mx0:
        mx0 = a.count("0")
        ans = x
print(ans)
