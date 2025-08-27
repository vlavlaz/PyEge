#https://education.yandex.ru/ege/task/33fcf00e-3931-472c-8628-5dd4d4cdefdd
print("y x w z F")
for x in 0 , 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                f = (z <= x) and ((not y) and ((not w) == y))
                if not f: print(y, x, w ,z , f)
print("ANSW: Y X W Z")