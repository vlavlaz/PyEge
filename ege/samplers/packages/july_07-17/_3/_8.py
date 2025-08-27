#https://education.yandex.ru/ege/task/60c1a00c-2fd4-472e-b4aa-50791d6bddb8
#7 lets
alf = "КАБИНЕТ"
count = 0
for _1 in alf:
    for _2 in alf:
        if _2 in _1:
            continue
        for _3 in alf:
            if _3 in _1+_2:
                continue
            for _4 in alf:
                if _4 in _1+_2+_3:
                    continue
                for _5 in alf:
                    if _5 in _1+_2+_3+_4 :
                        continue
                    for _6 in alf:
                        if _6 in _1+_2+_3+_4+_5:
                            continue
                        for _7 in alf:
                            if _7 in _1+_2+_3+_4+_5+_6:
                                continue
                            if _7 in "АИЕ":
                                continue
                            word = _1+_2+_3+_4+_5+_6+_7
                            count += 1
                            print(word.count("К"),word.count("А"),word.count("Б"),word.count("И"),word.count("Н"),word.count("Е"),word.count("Т") )
print(count)