#https://education.yandex.ru/ege/task/7a1cd054-b366-41c5-b596-99e0d45835fd

print("x y z w F")
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                f = (y == (not w)) <= (not (w and (x ==(x or (w <= z)))))
                if not f:
                    print(x,y,z,w,f)
print("ANSWER: Y Z W X")