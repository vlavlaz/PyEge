#https://education.yandex.ru/ege/task/0f0be116-5c24-4561-8675-493fe3c6ba53
def to5(x):
    res = ""
    while x > 0:
        res += str(x%5)
        x//=5
    return res[::-1]
def algo(n):
    _5 = to5(n)
    if n % 25 == 0:
        R = _5[-3:] + _5
    else:
        R = _5 + to5(n % 25)
    return R
for n in range(1, 100000):
    R = algo(n)
    print(n, int(R,5), R)
    if int(R, 5) > 10000:
      print(n, int(R,5), R)
      break