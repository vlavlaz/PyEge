#https://education.yandex.ru/ege/task/d4584e0e-7f27-47de-bf19-688170399d46
def conv(x):
    alf = "0123456789abcdefghijklmno"
    n = ""
    while x > 0:
        n+=alf[x%25]
        x//=25
    return n[::-1]
for x in range(900000, 1000000):
    a = 25**340+25**79-5**60 + x
    _a = conv(a)
    print(_a)
    if _a.count("0") == 287:
        print(x)