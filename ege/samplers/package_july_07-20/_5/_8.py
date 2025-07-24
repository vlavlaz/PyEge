#https://education.yandex.ru/ege/task/1769ee78-deec-48be-a248-12165baef040
alf = "ВЕЧНОСТЬ"
cnt = 0
for _1 in alf:
    for _2 in alf:
        for _3 in alf:
            for _4 in alf:
                for _5 in alf:
                    for _6 in alf:
                        if _6 not in "ЕОТЬ":
                            continue
                        word = _1+_2+_3+_4+_5+_6
                        if word.count("О") >= 2 and _1 in "ОЕЬ":
                            cnt += 1
                            print(word)
print(cnt)
