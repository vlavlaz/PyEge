#https://education.yandex.ru/ege/task/8cf5f358-d940-4c96-b34d-e8448147eeb5
def algo(N):
    _2 = bin(N)[2:]
    if N%2==0:
        r = _2.count("0")
        _2 = _2 + "0"*r
    else:
        r = _2.count("1")
        _2 = "1" * r + _2
    return _2
for x in range(1, 10000):
    R = int(algo(x),2)
    if R > 2000:
        print(x, R)
        break
