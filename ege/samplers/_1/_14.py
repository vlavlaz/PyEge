#https://education.yandex.ru/ege/task/8aeb48b1-195e-40c0-a5d7-d6622b69e935
alf = "0123456789a"
def to11(x):
    res = ""
    while x > 0:
        res+=alf[x%11]
        x//=11
    return res[::-1]

for x in range(1, 3001):
    eq = to11(9*11**210+8*11**150 - x)
    if eq.count("0") == 60:
        print(x)
