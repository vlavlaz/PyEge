#https://education.yandex.ru/ege/task/89ed586b-3157-4429-b569-0041d7adbd6d
def algo(s):
    s = str(s)
    while "4444" in s or "844" in s or "84" in s:
        if "4444" in s:
            s = s.replace("4444", "884", 1)
        if "844" in s:
            s = s.replace("844", "488", 1)
        if "84" in s:
            s = s.replace("84", "3343", 1)
    return s
for n in range(4, 10001):
    out = algo("8"+"4"*n)
    if len(out) < 20:
        print(n)
