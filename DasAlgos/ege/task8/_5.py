alf = "ВЕНОСТЧЬ"
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
                        su = ""
                        for c in word:
                            if c == "В":
                                su += "0"
                            if c == "Е":
                                su += "1"
                            if c == "Н":
                                su += "2"
                            if c == "О":
                                su += "3"
                            if c == "С":
                                su += "4"
                            if c == "Т":
                                su += '5'
                            if c == "Ч":
                                su += '6'
                            if c == "Ь":
                                su += '7'
                        if word.count("О") >= 2 and _1 in "ОЕ":
                            cnt += 1
                            print(word, int(su, 8)+1)
print(cnt)
