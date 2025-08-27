#https://education.yandex.ru/ege/task/a47b4628-55a3-490f-8966-28f020130818
def valid_K(x):
    mnd = 2
    for d in range(2, int(x**0.5)+1):
        if x%d == 0: mnd = d; break
    return mnd+x//mnd
def count_dels(x):
    dels = []
    for d in range(2, int(x**0.5)+1):
        if x%d == 0:
            dels.append(d); dels.append(x//d)
    return len(dels)
for x in range(650000, 2**32):
    if len(str(valid_K(x))) == 4 and count_dels(x) == 6:
        print(x, valid_K(x))

