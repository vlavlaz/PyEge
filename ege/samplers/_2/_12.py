#https://education.yandex.ru/ege/task/2ada5a06-1d3c-4302-b356-8796eb5fc06f
def sumd(X):
    s = str(X)
    su = 0
    for x in s:
        su += int(x)
    return su
def algo(s):
    s = str(s)
    while "444" in s or "333" in s:
        if "444" in s:
            s = s.replace("444", "3", 1)
        else:
            s = s.replace("333", "3344", 1)
        if "3443" in s:
            s = s.replace("3443", "0", 1)
    return s
print(sumd(algo(50*"4")), algo(50*"4"))