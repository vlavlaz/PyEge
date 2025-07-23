#https://education.yandex.ru/ege/task/0c13be3e-1a92-4507-89ec-075d19ecc39c
def algo(s1):
    s = str(s1)
    while "52" in s or "2222" in s or "1112" in s:
        if "52" in s:
            s = s.replace("52", "11", 1)
            s = s.replace("2222", "5", 1)
        else:
            s = s.replace("1112", "2", 1)
    return s
def sumd(s):
    su = 0
    for x in s:
        su += int(x)
    return su
for n in range(3, 10001):
    res = algo("5"+"2"*n)
    if sumd(res) == 1685:
        print(n)