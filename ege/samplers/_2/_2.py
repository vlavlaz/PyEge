#https://education.yandex.ru/ege/task/6e74e165-b36c-4015-90ed-f8760e150ee7
print("b c a d F")
for a in 0, 1:
    for b in 0, 1:
        for c in 0, 1:
            for d in 0, 1:
                f = c and (a or d) and (d <= b)
                if f: print(b, c, a, d, f)
print("ANSW: B C A D")
