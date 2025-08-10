#https://education.yandex.ru/ege/task/4820b374-36df-4864-912e-ac63edcbab34
print("x y z w F")
for x in 0,1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                f = not (((1 <= z) or (not x)) and y)
                if not f:
                    print(y, x, z, w, f)
print("ANSW: y x z w")