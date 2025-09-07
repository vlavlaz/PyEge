#https://education.yandex.ru/ege/task/9097af0b-1758-4760-bdf2-1ea86d55cef4

print("z y x w f")
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                f = (x or y) and (not (y == z)) and not w
                if f:
                    print(z, y, x, w, f)
