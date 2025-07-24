#https://education.yandex.ru/ege/task/da9b8fa5-490a-48c5-a9c2-542e3343c920
print("a b c d F")
for a in 0, 1:
    for b in 0, 1:
        for c in 0, 1:
            for d in 0, 1:
                f = ((a and b) <= c) and ((b and c) <= d)
                if not f:
                    print(a,b,c,d,f)
print("ASWER: d b a c")