#https://education.yandex.ru/ege/task/b21d9d79-e2ed-434c-94d2-9152bbcba6e7

def algo(n):
    r = bin(n)[2:]
    if n%3==0:
        r = r + r[-3:]
    else:
        o = bin((n%3)*3)[2:]
        r = r + o
    return int(r, 2)
print(algo(26))
for n in range(1, 10000):
    print(algo(n))
    if algo(n) >= 200:
        print(n)
        break
