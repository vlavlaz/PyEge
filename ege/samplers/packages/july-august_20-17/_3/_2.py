#https://education.yandex.ru/ege/task/5e1d8be3-465b-4e31-a70d-78cbc1ee8e60
print("x u w y F")
for u in 0, 1:
    for w in 0,1:
        for x in 0, 1:
            for y in 0, 1:
                f = (x<=w) <= (u<=y)
                if not f:
                    print(x, u, w, y, f)
print("ANSW: X U W Y")