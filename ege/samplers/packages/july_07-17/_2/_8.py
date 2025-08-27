#https://education.yandex.ru/ege/task/08a16fb2-3773-4f00-8961-cfa21b2e65a9
alf = "ГИПЕРБОЛА"
g = "ИЕОА"
s = "ГПРБЛ"
count = 0
for _1 in alf:
    if _1 in g:
        continue
    for _2 in alf:
        for _3 in alf:
            for _4 in alf:
                for _5 in alf:
                    for _6 in alf:
                        if _6 in g:
                            continue
                        word = _1 + _2 + _3 + _4 + _5 + _6
                        if _2 in g and _3 in s:
                            continue
                        if _3 in g and _2 in s and _4 in s:
                            continue
                        if _4 in g and _3 in s and _5 in s:
                            continue
                        if _5 in g and _4 in s:
                            continue
                        count += 1
print(count)