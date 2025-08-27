#https://education.yandex.ru/ege/task/cbcfe90c-ece7-4807-a5b9-28820981c5be
print("a b c d F")
for a in 0, 1:
    for b in 0, 1:
        for c in 0, 1:
            for d in 0, 1:
                f = (a<=b) and (b<=c) and (c<=d)
                if f:
                    print(a,b,c,d,f)
print("ANSW: A C D B")