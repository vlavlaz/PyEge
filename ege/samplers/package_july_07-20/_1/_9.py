#https://education.yandex.ru/ege/task/59213ca9-5841-4d0e-90f4-d69569902d37
#WRONG: _1кондиция учитывала строки с нулём и без положительных чисел,
#поскольку для счета положительных чисел из длинны строки вычиталось
#кол-во отрицательных чисел.
#CORRECTED --> 3036.
f = open("_9.txt")
s = [c.split() for c in f]
def _1cond(stroke):
    c_neg = 0
    z_count = 0
    for x in stroke:
        if x < 0:
            c_neg += 1
        if x == 0: ####
            z_count+=1 ####
    if c_neg > 5-c_neg-z_count > 0:
        return True
    else: return False
def _2cond(stroke):
    mn_neg = 9999999999999999
    mx_pos = 0
    for x in stroke:
        if mn_neg > x and x < 0:
            mn_neg = x
        if mx_pos < x and x > 0:
            mx_pos = x
    if abs(mx_pos)<abs(mn_neg):
        return True
    else:
        return False

countASW = 0
for strr in s:
    stroke = []
    for t in strr:
        stroke.append(int(t))
    if _1cond(stroke) and _2cond(stroke):
        countASW += 1
        if 0 in stroke: print(stroke)
print(countASW)




